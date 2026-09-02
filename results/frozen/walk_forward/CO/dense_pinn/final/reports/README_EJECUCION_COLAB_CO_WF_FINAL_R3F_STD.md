# Ejecución en Google Colab

1. Conserve la estructura canónica Turbine_Emissions_PINN.
2. Verifique que PROTOCOL R1 y la campaña CO OPT R3 estén FROZEN.
3. Abra 04_Gold_Standard_PINN_CO_WF_FINAL - R3F_STD.ipynb.
4. Seleccione GPU y use Runtime → Run all.
5. No ejecute celdas fuera de orden.

El notebook acepta solo CDP_NEG, entrena diez modelos con DEV completo antes de
abrir TEST y evalúa ∂CO/∂CDP ≤ 0. Los resultados quedan en
models/wf/work_pinn_co_wf_final_r3_std/.
