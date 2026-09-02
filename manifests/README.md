# Manifiestos

- `audit/`: inventario técnico del archivo experimental, imports y grupos de
  duplicados exactos.
- `migration_manifest.csv`: 971 relaciones origen relativo → destino relativo,
  con transformación, tamaño y SHA-256.
- `book_notebooks.csv`: correspondencia de los 22 notebooks vinculados al
  trabajo académico y dos análisis adicionales, con conteos de ejecución y
  salidas.
- `canonical_notebooks.csv`: rol, versión y estado de los notebooks canónicos.
- `model_inventory.csv`: los 46 pesos distribuidos.
- `model_catalog.csv`: catálogo de 64 binarios y 40 metadatos, incluidos 18
  binarios XGBoost–NOx no distribuidos por tamaño.
- `book_evidence_map.csv`: relación entre tablas, figuras, apéndices y archivos.
- `portability_findings.csv`: referencias históricas de ruta conservadas en la
  evidencia ejecutada.
- `release_checksums.sha256`: integridad de la versión 1.0.0.

Las rutas de origen son relativas y no exponen la ubicación privada del archivo
experimental.
