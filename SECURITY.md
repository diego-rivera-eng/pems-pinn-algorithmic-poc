# Security policy

## Model artifacts

Do not load a model obtained from an untrusted source. PyTorch checkpoint
formats can invoke unsafe deserialization paths, and serialized ML artifacts
should be treated as executable input. Verify each file against
`manifests/model_inventory.csv` and `manifests/release_checksums.sha256` before
loading it.

Use the safest loading mode supported by the installed library. For PyTorch,
prefer `weights_only=True` when the checkpoint structure permits it. XGBoost
`.ubj` files should be loaded only by a compatible, patched XGBoost release.

## Data and notebooks

Inspect notebook cells before executing them. Some notebooks preserve
environment setup, package-installation calls and path contracts from the
original experiments. Run them in an isolated environment without production
credentials.

No secret or API credential is required by this project. Report accidental
credential exposure privately to the repository owner before opening a public
issue.
