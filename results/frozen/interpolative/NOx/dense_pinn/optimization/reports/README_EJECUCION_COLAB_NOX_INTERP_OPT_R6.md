# Ejecución R6 en Google Colab

1. Ejecute 00_PEMS_PINN_INTERP_PROTOCOL - R1.ipynb y confirme estado FROZEN.
2. Abra 04_Gold_Standard_PINN_NOX_INTERP_OPT - R6.ipynb.
3. Verifique PROJECT_ROOT_PATH y ejecute primero RUN_MODE = SMOKE.
4. Sólo tras PASS, cambie a RUN_MODE = FULL_AUTO y use Runtime → Run all.
5. Observe el progreso con LIVE_MONITOR_PINN_CO_INTERP_R6.ipynb.

R6 usa un controlador único, RUN_STATE.json, checkpoint atómico después de cada
fold y escritor único. TEST permanece cerrado durante toda esta campaña.
