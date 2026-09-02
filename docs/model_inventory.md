# Inventario de modelos

## Modelos representativos

Además de los seis representantes de la tabla, se distribuyen los ensambles
compactos completos. El inventario contiene 46 pesos;
`manifests/model_catalog.csv` documenta también 18 binarios XGBoost–NOx no
incluidos por tamaño.

| ID | Versión | Objetivo | Semilla | Tamaño | Métrica R² | Archivo |
|---|---|---|---:|---:|---:|---|
| dense-interp-co | R5F_STD | CO | 126 | 261.215 B | 0.5317 | `models/dense_pinn/interpolative/CO/final_model_seed_126.pt` |
| dense-interp-nox | R6F_STD | NOx | 84 | 286.885 B | 0.7748 | `models/dense_pinn/interpolative/NOx/final_model_seed_84.pt` |
| tt-interp-co | R1F_STD | CO | 126 | 68.373 B | 0.5222 | `models/tt_pinn/interpolative/CO/tt_final_model_seed_126.pt` |
| tt-interp-nox | R1F_STD | NOx | 84 | 74.829 B | 0.7686 | `models/tt_pinn/interpolative/NOx/tt_final_model_seed_84.pt` |
| xgb-interp-co | R1F_STD | CO | 42 | 2.076.456 B | 0.5081 | `models/xgboost/interpolative/CO/XGBOOST_CO_INTERP_seed42.ubj` |
| xgb-interp-nox | R1F_STD | NOx | 42 | 133.653.329 B | 0.7449 | `models/xgboost/interpolative/NOx/XGBOOST_NOX_INTERP_seed42.ubj` |

Los SHA-256 completos están en `manifests/model_inventory.csv`. Los metadatos
XGBoost se incluyen junto con los binarios distribuidos.

## Complejidad reportada en el trabajo académico

| Modelo | Objetivo | Parámetros / nodos | Tamaño serializado (MiB) |
|---|---|---:|---:|
| PINN densa | CO | 62.977 parámetros | 0.249 |
| TT-PINN | CO | 12.582 parámetros | 0.065 |
| XGBoost | CO | 320 árboles / 54.838 nodos | 1.980 |
| PINN densa | NOx | 69.187 parámetros | 0.274 |
| TT-PINN | NOx | 13.891 parámetros | 0.071 |
| XGBoost | NOx | 1.445 árboles / 3.902.865 nodos | 127.462 |

TT-PINN reduce parámetros aproximadamente 80,02 % en CO y 79,92 % en NOx
frente a Dense. En CO, TT no supera el criterio informativo de no inferioridad
física: su PCD cae cerca de 1,42 puntos porcentuales, por encima del margen de
un punto. Sí cumple los criterios de R², RMSE, MAE y almacenamiento.

## Modelos no distribuidos

- Nueve binarios XGBoost–NOx interpolativos y nueve *walk-forward*: se registran
  con SHA-256 en el catálogo y no se incluyen por su tamaño agregado.
- Checkpoints y estados de optimización: artefactos operativos fuera del
  alcance de esta distribución.
- XGBoost R2 *budget-matched*: análisis poshoc congelado contra generaciones
  Dense anteriores a las finales seleccionadas.

## Carga segura

Verifique el checksum antes de cargar. Para `.pt`, prefiera una ruta que cargue
solo pesos y reconstruya la arquitectura desde el contrato JSON. Nunca confíe
en un checkpoint de procedencia desconocida.
