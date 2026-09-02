# Inventario técnico y criterios de curaduría

## Alcance y método

El inventario cubre el archivo histórico completo utilizado para construir la
prueba de concepto. Para cada elemento se registraron ruta relativa, tamaño,
extensión, fecha de modificación y SHA-256. Los notebooks se analizaron como
JSON para contar celdas, ejecuciones, salidas, imports y referencias de ruta.
Los duplicados se identificaron por igualdad de SHA-256 y tamaño.

Los registros completos están en:

- `manifests/audit/source_inventory.csv`
- `manifests/audit/notebook_inventory.csv`
- `manifests/audit/notebook_imports.csv`
- `manifests/audit/exact_duplicate_groups.csv`
- `manifests/audit/audit_summary.json`

## Magnitud del archivo experimental

| Indicador | Resultado |
|---|---:|
| Archivos | 6.382 |
| Tamaño total | 2.598.122.993 bytes (2,42 GiB) |
| Notebooks | 156 |
| Notebooks con error JSON | 0 |
| Grupos de duplicados exactos | 556 |
| Archivos pertenecientes a esos grupos | 1.685 |

Los tipos dominantes son 1.667 JSON, 1.460 CSV, 787 PNG, 573 PT, 480 UBJ,
247 Python, 235 joblib, 230 NPZ y 156 IPYNB. Los artefactos de modelos concentran
5.603 archivos y la mayor parte del volumen; los 480 UBJ suman cerca de 1,79
GiB.

## Selección canónica

| Alcance | Optimización | Final / evidencia | Disposición |
|---|---|---|---|
| Protocolo interpolativo | — | R1 ejecutado | Canónico |
| Protocolo *walk-forward* | — | R1 ejecutado | Canónico |
| Dense CO interpolativo | R5 | R5F_STD | Canónico |
| Dense NOx interpolativo | R6 | R6F_STD | Canónico |
| TT-PINN CO interpolativo | reutiliza Dense R5 | R1F_STD + addendum computacional R1 | Canónico |
| TT-PINN NOx interpolativo | reutiliza Dense R6 | R1F_STD + addendum computacional R1 | Canónico |
| XGBoost CO interpolativo | R1_POC_EFFICIENT | R1F_STD | Canónico para la Tabla 32 |
| XGBoost NOx interpolativo | R1_POC_EFFICIENT | R1F_STD | Canónico para la Tabla 32 |
| Dense CO/NOx *walk-forward* | R3_POC_EFFICIENT | R3F_STD | Canónico |
| XGBoost CO/NOx *walk-forward* | R1_POC_EFFICIENT | R1F_STD | Canónico |
| Pareto/latencia | análisis R5/R1 | salida definitiva R4 | Apoyo canónico |
| XGBoost `R2F_BUDGET_MATCHED` | poshoc | congelado contra Dense R4/R5 | Suplementario |

La selección R1F_STD para XGBoost interpolativo reproduce la procedencia y las
cifras de la Tabla 32. `R2F_BUDGET_MATCHED` se conserva como análisis
suplementario porque su presupuesto fue fijado contra generaciones Dense
anteriores a las seleccionadas (CO R4 frente a R5; NOx R5 frente a R6).

## Duplicados, versiones sustituidas y exclusiones

No forman parte de la estructura canónica:

- versiones sustituidas y variantes preliminares cuando existe una final
  posterior documentada;
- respaldos, temporales y copias previas a ajustes visuales;
- checkpoints, modelos por semilla no representativa y ensambles redundantes;
- bases de Optuna, estados de ejecución, monitores, logs vacíos, ejecuciones
  fallidas y cachés;
- duplicados exactos ya representados por una copia canónica;
- documentos administrativos o personales;
- la Figura 16, por corresponder a una adaptación de literatura externa.

Una exclusión indica que el archivo es intermedio, redundante, operativo,
sustituido o no redistribuible; no constituye una valoración de su validez
científica. El archivo experimental se preservó sin modificaciones.

## Dependencias observadas

Los 156 notebooks importan principalmente `pandas`, `numpy`, `pathlib`, `json`,
`os` y `matplotlib`; las campañas PINN añaden `torch`, las optimizaciones
`optuna` y las líneas base `xgboost`/`joblib`. Los contratos de protocolo son
dependencias aguas arriba de todas las campañas. TT-PINN depende de la
configuración Dense seleccionada y el addendum computacional utiliza una
herramienta histórica no incluida como módulo público independiente.

Los notebooks primarios preservan referencias a contratos de rutas usados en
los experimentos. Por ello, esta publicación distingue entre evidencia
ejecutada verificable y reproducción integral desde la topología pública.

## Resultado de la curaduría

El manifiesto de migración contiene 971 registros trazables. La distribución
incluye 24 notebooks canónicos ejecutados y 24 espejos versionados, cinco CSV,
modelos representativos y ensambles compactos, figuras, tablas fuente y
artefactos congelados de configuración, resultados y auditoría.

`manifests/migration_manifest.csv` relaciona cada copia con su ruta relativa y
hash de origen. Las rutas de perfil personal se sustituyeron por `<USER_HOME>`
en los archivos públicos transformados; el manifiesto registra el hash del
original y el de la copia. `manifests/release_checksums.sha256` cubre la versión
1.0.0.
