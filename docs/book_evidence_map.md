# Mapa de evidencia del trabajo académico

Este documento relaciona el repositorio con el Capítulo 10 y los Apéndices A y
B de Rivera (2026), *Metodología Conceptual para la Implementación de Sistemas de Monitoreo Predictivo de Emisiones (PEMS) Basados en Redes Neuronales Informadas por la Física (PINNs) Aplicado a Fuentes Fijas de Combustión en el Sector Petróleo y Gas Colombiano*. Los nombres públicos de los archivos permanecen
estables aunque cambie la composición editorial del documento académico.

## Tablas

| Elemento académico | Contenido | Evidencia primaria | Resumen navegable |
|---|---|---|---|
| Tabla 32 | Desempeño interpolativo Dense/TT/XGBoost en CO/NOx | `results/frozen/interpolative/<objetivo>/<modelo>/final/tables/` | `results/frozen/interpolative/metrics_summary.csv` |
| Tabla 33 | Parámetros/nodos y tamaño serializado | `model_complexity.csv`, finales Dense/TT y addendum computacional | `results/frozen/computational_benchmark/model_size_summary.csv` |
| Tabla 34 | Ensambles *walk-forward* en 2015 | cuatro `test_metrics_ensemble.json` | `results/frozen/walk_forward/metrics_summary.csv` |

Para XGBoost interpolativo, la Tabla 32 utiliza la fila `seed=42` de
`test_metrics_by_seed.csv`; no utiliza la métrica de ensamble. Para Dense y TT,
las semillas representativas son CO 126 y NOx 84.

## Figuras

| Figura académica | Archivo del repositorio | Datos disponibles |
|---:|---|---|
| 16 | No distribuida; es un esquema adaptado de literatura externa | Consulte la fuente citada en el trabajo académico |
| 17 | `figures/protocol/interpolative_protocol.png` | manifiestos y asignación de `configs/protocols/interpolative/` y `results/frozen/protocol/interpolative/` |
| 18 | `figures/dense_pinn/train_test_segments.png` | tablas finales Dense CO/NOx |
| 19 | `figures/dense_pinn/parity_residuals.png` | predicciones/métricas finales Dense |
| 20 | `figures/tt_pinn/train_test_segments.png` | tablas finales TT CO/NOx |
| 21 | `figures/tt_pinn/parity_residuals.png` | predicciones/métricas finales TT |
| 22 | `figures/physical_consistency/dense_tt_gradients_pdp.png` | `results/frozen/figure_data/physical_consistency_pdp.csv` y `physical_gradients_test.csv` |
| 23 | `figures/xgboost/train_test_segments.png` | tablas finales XGBoost CO/NOx |
| 24 | `figures/xgboost/parity_residuals.png` | predicciones/métricas finales XGBoost |
| 25 | `figures/pareto/r2_vs_serialized_size.png` | `results/frozen/figure_data/pareto_r2_size.csv` y resultados Pareto R4 |

`figures/xgboost/local_effects_supplementary.png` corresponde a material
suplementario y no a una figura numerada del documento académico.

## Apéndice A — Algoritmos y prueba de concepto

| Requisito | Ubicación |
|---|---|
| Protocolos y particiones | `notebooks/00_protocol/`, `configs/protocols/`, `results/frozen/protocol/` |
| Configuración y optimización | notebooks `optimization.ipynb`, `configs/models/` y tablas `optimization/` |
| Evaluación final | notebooks `final.ipynb`, `results/frozen/**/final/` |
| Modelos representativos | `models/` y `manifests/model_inventory.csv` |
| Resultados, gráficos y diagnósticos | `results/`, `figures/`, `reports/executed/` |
| Integridad y procedencia | `manifests/` y `scripts/verify_release.py` |

## Apéndice B — Validación *walk-forward*

El apéndice se sustenta en:

- protocolo y contratos en `configs/protocols/walk_forward/`;
- notebook de protocolo en `notebooks/00_protocol/walk_forward_protocol.ipynb`;
- optimización y finales Dense/XGBoost para ambos objetivos en
  `notebooks/04_walk_forward/`;
- métricas, predicciones, auditorías de TEST y complejidad en
  `results/frozen/walk_forward/`;
- descripción de las cuatro ventanas y de la prueba externa 2015 en
  `docs/methodology.md`.

TT-PINN no forma parte de este protocolo. El apéndice compara Dense y XGBoost y
presenta la caída de desempeño de NOx como evidencia de cambio temporal.

## Consistencia documental

La estructura del trabajo académico sitúa el Capítulo 10 en las páginas
lógicas 124–172, el Apéndice A en la 212 y el Apéndice B en la 213. Los valores
de las Tablas 32–34 se contrastaron con las salidas seleccionadas. El documento
académico no se redistribuye desde este repositorio.

## Referencia

Rivera, D. A. (2026). *Metodología Conceptual para la Implementación de Sistemas de Monitoreo Predictivo de Emisiones (PEMS) Basados en Redes Neuronales Informadas por la Física (PINNs) Aplicado a Fuentes Fijas de Combustión en el Sector Petróleo y Gas Colombiano* [Trabajo de grado de maestría, Universidad
Industrial de Santander].
