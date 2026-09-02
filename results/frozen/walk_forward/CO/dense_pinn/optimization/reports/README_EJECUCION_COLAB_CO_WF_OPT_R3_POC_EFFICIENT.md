# Ejecución en Google Colab

1. Conserve la estructura canónica `Turbine_Emissions_PINN`.
2. Ejecute `00_PEMS_PINN_WF_PROTOCOL - R1.ipynb` y confirme estado FROZEN.
3. Abra `04_Gold_Standard_PINN_CO_WF_OPT - R3_POC_EFFICIENT.ipynb`.
4. Verifique `PROJECT_ROOT_PATH` y utilice primero `RUN_MODE = "SMOKE"`.
5. Seleccione una GPU y use **Runtime → Run all**.
6. Si SMOKE finaliza, cambie a `RUN_MODE = "FULL_AUTO"`.

FULL_AUTO conserva checkpoints por trial, fase, candidato y semilla. Optuna usa
SQLite local y respalda un snapshot consistente en Drive después de cada trial.
TEST permanece cerrado. El único consumidor directo autorizado es
`04_Gold_Standard_PINN_CO_WF_FINAL - R3F_STD.ipynb`.
