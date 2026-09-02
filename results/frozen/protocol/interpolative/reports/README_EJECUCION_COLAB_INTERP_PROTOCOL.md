# Ejecución en Google Colab

1. Conserve los CSV en `Turbine_Emissions_PINN/data/raw/`.
2. Abra `notebooks/00_PEMS_PINN_INTERP_PROTOCOL - R1.ipynb`.
3. Use **Runtime → Run all** con un entorno CPU.
4. Los resultados quedan en `models/interp/work_pinn_interp_protocol/`.

El notebook carga solamente las nueve variables operativas. Los nombres CO y NOX se
verifican en los encabezados, pero sus valores no se materializan.
