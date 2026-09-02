#!/usr/bin/env python3
"""Verify the public release without loading models or retraining."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MIB = 1024 * 1024


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(MIB), b""):
            digest.update(chunk)
    return digest.hexdigest()


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


class Audit:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self.passes: list[str] = []

    def require(self, condition: bool, message: str) -> None:
        if condition:
            self.passes.append(message)
        else:
            self.errors.append(message)

    def warn(self, condition: bool, message: str) -> None:
        if condition:
            self.warnings.append(message)


def verify_data(audit: Audit) -> None:
    manifest = ROOT / "data" / "raw" / "MANIFEST.sha256"
    lines = [line.strip() for line in manifest.read_text(encoding="utf-8").splitlines() if line.strip()]
    audit.require(len(lines) == 5, "raw data manifest declares five files")
    total_rows = 0
    expected_header = "AT,AP,AH,AFDP,GTEP,TIT,TAT,TEY,CDP,CO,NOX"
    for line in lines:
        expected, name = line.split(maxsplit=1)
        path = manifest.parent / name.strip()
        audit.require(path.is_file(), f"raw data exists: {name}")
        if not path.is_file():
            continue
        audit.require(sha256(path) == expected.lower(), f"raw data checksum: {name}")
        with path.open("r", encoding="utf-8-sig", newline="") as handle:
            header = handle.readline().strip()
            rows = sum(1 for _ in handle)
        audit.require(header == expected_header, f"raw data schema: {name}")
        total_rows += rows
    audit.require(total_rows == 36733, "raw data contains 36,733 observations")


def verify_notebooks(audit: Audit) -> None:
    canonical = sorted((ROOT / "notebooks").rglob("*.ipynb"))
    executed = sorted((ROOT / "reports" / "executed" / "v1.0.0").rglob("*.ipynb"))
    audit.require(len(canonical) == 24, "24 executed canonical notebooks are present")
    audit.require(len(executed) == 24, "24 executed evidence notebooks are present")
    for path in canonical + executed:
        try:
            notebook = json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:  # noqa: BLE001
            audit.errors.append(f"invalid notebook JSON: {path.relative_to(ROOT)} ({exc})")
            continue
        audit.require(isinstance(notebook.get("cells"), list), f"notebook cells valid: {path.relative_to(ROOT)}")
        if path in canonical:
            code_cells = [cell for cell in notebook["cells"] if cell.get("cell_type") == "code"]
            output_count = sum(len(cell.get("outputs", [])) for cell in code_cells)
            error_count = sum(1 for cell in code_cells for output in cell.get("outputs", []) if output.get("output_type") == "error")
            fully_executed = all(cell.get("execution_count") is not None for cell in code_cells)
            audit.require(fully_executed, f"canonical notebook code cells are executed: {path.relative_to(ROOT)}")
            audit.require(output_count > 0, f"canonical notebook exposes results: {path.relative_to(ROOT)}")
            audit.require(error_count == 0, f"canonical notebook has no error outputs: {path.relative_to(ROOT)}")


def verify_migration(audit: Audit) -> None:
    rows = read_csv(ROOT / "manifests" / "migration_manifest.csv")
    audit.require(len(rows) == 971, "migration manifest has 971 curated records")
    for row in rows:
        relative = row["destination_relative_path"]
        path = ROOT / relative
        audit.require(path.is_file(), f"migrated artifact exists: {relative}")
        if path.is_file():
            audit.require(str(path.stat().st_size) == row["destination_size_bytes"], f"migrated size: {relative}")
            audit.require(sha256(path) == row["destination_sha256"].lower(), f"migrated checksum: {relative}")


def verify_models(audit: Audit) -> None:
    rows = read_csv(ROOT / "manifests" / "model_inventory.csv")
    audit.require(len(rows) == 46, "46 distributed model weights are inventoried")
    for row in rows:
        path = ROOT / row["relative_path"]
        audit.require(path.is_file(), f"model exists: {row['model_id']}")
        if path.is_file():
            audit.require(str(path.stat().st_size) == row["size_bytes"], f"model size: {row['model_id']}")
            audit.require(sha256(path) == row["sha256"].lower(), f"model checksum: {row['model_id']}")
    catalog = read_csv(ROOT / "manifests" / "model_catalog.csv")
    audit.require(len(catalog) == 104, "complete model catalog has 104 files")
    omitted = [row for row in catalog if row["distribution_status"].startswith("OMITTED")]
    audit.require(len(omitted) == 18, "18 oversized XGBoost-NOx binaries are explicitly catalogued as omitted")
    attributes = (ROOT / ".gitattributes").read_text(encoding="utf-8")
    audit.require("*.ubj filter=lfs" in attributes and "*.pt filter=lfs" in attributes, "model formats are assigned to Git LFS")
    large = [path for path in (ROOT / "models").rglob("*") if path.is_file() and path.stat().st_size > 100 * MIB]
    audit.warn(bool(large), f"{len(large)} model exceeds 100 MiB and requires Git LFS")


def verify_release_checksums(audit: Audit) -> None:
    manifest = ROOT / "manifests" / "release_checksums.sha256"
    records = [line for line in manifest.read_text(encoding="utf-8").splitlines() if line.strip()]
    for line in records:
        expected, relative = line.split("  ", 1)
        path = ROOT / relative
        audit.require(path.is_file(), f"release file exists: {relative}")
        if path.is_file():
            audit.require(sha256(path) == expected.lower(), f"release checksum: {relative}")


def verify_privacy_and_secrets(audit: Audit) -> None:
    text_suffixes = {".csv", ".ipynb", ".json", ".jsonl", ".md", ".py", ".txt", ".yml", ".yaml"}
    personal_patterns = ("C:\\Users\\diego", "C:\\\\Users\\\\diego", "C:/Users/diego")
    secret_patterns = [
        re.compile(r"ghp_[A-Za-z0-9]{30,}"),
        re.compile(r"github_pat_[A-Za-z0-9_]{30,}"),
        re.compile(r"sk-[A-Za-z0-9_-]{20,}"),
        re.compile(r"AKIA[0-9A-Z]{16}"),
        re.compile(r"AIza[0-9A-Za-z_-]{30,}"),
        re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    ]
    personal_hits: list[str] = []
    secret_hits: list[str] = []
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in text_suffixes:
            continue
        if path.resolve() == Path(__file__).resolve():
            continue
        try:
            text = path.read_text(encoding="utf-8-sig")
        except UnicodeDecodeError:
            continue
        relative = path.relative_to(ROOT).as_posix()
        if any(pattern in text for pattern in personal_patterns):
            personal_hits.append(relative)
        if any(pattern.search(text) for pattern in secret_patterns):
            secret_hits.append(relative)
    audit.require(not personal_hits, f"no personal home paths remain ({personal_hits})")
    audit.require(not secret_hits, f"no high-confidence credential patterns found ({secret_hits})")


def verify_metadata(audit: Audit) -> None:
    cff = (ROOT / "CITATION.cff").read_text(encoding="utf-8")
    audit.require("cff-version: 1.2.0" in cff and "title:" in cff and "authors:" in cff and "message:" in cff, "CITATION.cff has required CFF 1.2.0 fields")
    audit.require('version: "1.0.0"' in cff and 'date-released: "2026-09-01"' in cff, "CITATION.cff identifies release 1.0.0")
    license_text = (ROOT / "LICENSE").read_text(encoding="utf-8")
    audit.require("ALL RIGHTS RESERVED" in license_text and "SELECTION PENDING" not in license_text, "LICENSE contains the definitive rights notice")
    portability = read_csv(ROOT / "manifests" / "portability_findings.csv")
    audit.warn(bool(portability), f"{len(portability)} files retain declared legacy path references")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--strict-publication", action="store_true", help="treat warnings as failure")
    args = parser.parse_args()
    audit = Audit()

    verify_data(audit)
    verify_notebooks(audit)
    verify_migration(audit)
    verify_models(audit)
    verify_release_checksums(audit)
    verify_privacy_and_secrets(audit)
    verify_metadata(audit)

    print(f"PASS checks: {len(audit.passes)}")
    for warning in audit.warnings:
        print(f"WARN: {warning}")
    for error in audit.errors:
        print(f"ERROR: {error}")
    if audit.errors:
        print(f"FAIL: {len(audit.errors)} error(s)")
        return 1
    if args.strict_publication and audit.warnings:
        print(f"NOT PUBLICATION-READY: {len(audit.warnings)} warning(s)")
        return 2
    print("PASS: public release integrity verified")
    return 0


if __name__ == "__main__":
    sys.exit(main())
