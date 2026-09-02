# Notebooks ejecutados

Los 24 notebooks de esta carpeta conservan sus `execution_count`, tablas,
gráficos y salidas. Veintidós corresponden a insumos directos del trabajo de
maestría y dos documentan comparaciones de Pareto y latencia.

La verificación registra 1.445 objetos de salida, 592 celdas de código con
contador de ejecución y cero salidas de error. La correspondencia entre los
nombres de las campañas y las rutas canónicas está en
`manifests/book_notebooks.csv`.

## Orden lógico

1. `00_protocol/`: protocolos interpolativo y *walk-forward*.
2. `01_dense_pinn/`: optimización y final Dense para CO/NOx.
3. `02_tt_pinn/`: finales TT-PINN usados por el trabajo académico.
4. `03_xgboost/`: optimización y final interpolativos.
5. `04_walk_forward/`: optimización y final Dense/XGBoost para CO/NOx.
6. `05_comparison/`: Pareto, latencia y addenda computacionales TT.

## Uso

Los resultados pueden consultarse sin reejecutar. Las fuentes conservan
contratos de ruta de los experimentos y *fallbacks* de Colab; el alcance de una
nueva ejecución se explica en `docs/reproducibility.md`.

`reports/executed/v1.0.0/` mantiene el espejo versionado de la evidencia. Las
nuevas ejecuciones deben escribirse en un directorio separado y producir una
versión con linaje propio.
