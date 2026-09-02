# Reproducibilidad

## Verificación de la versión 1.0.0

La distribución permite comprobar de forma determinista:

- presencia, tamaño y SHA-256 de datos y modelos;
- validez JSON de 24 notebooks canónicos ejecutados y sus 24 espejos;
- ejecución completa, resultados visibles y ausencia de salidas de error;
- correspondencia entre resultados resumidos y evidencia académica;
- procedencia relativa de cada artefacto migrado;
- configuración de Git LFS para los formatos de modelo.

Ejecute:

```bash
python scripts/verify_release.py
```

El comando no deserializa modelos, no reentrena y no modifica la evidencia.

## Entorno de referencia y entornos de ejecución

`requirements.txt` y `environment.yml` proporcionan un entorno moderno de
inspección y adaptación con Python 3.12. Las campañas originales se ejecutaron
en más de una pila:

| Campaña | Python | Núcleo científico observado |
|---|---|---|
| Dense interpolativa final reciente | 3.12.10 | NumPy 2.4.6, pandas 3.0.5, scikit-learn 1.9.0, PyTorch 2.13.0+cu132 |
| TT-PINN y Dense *walk-forward* | 3.12.x | NumPy 2.1.3, pandas 2.2.3, scikit-learn 1.6.1, PyTorch 2.11.0+cu128 |
| XGBoost interpolativo/*walk-forward* | 3.12.x | NumPy 2.1.3, pandas 2.2.3, scikit-learn 1.6.1, XGBoost 3.0.1 |

Los JSON `ENVIRONMENT_*` de cada campaña documentan el entorno observado. No
existe un único lockfile capaz de recrear byte a byte todas las familias y
configuraciones de GPU.

## Instalación

```bash
git lfs install
python -m venv .venv
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python scripts/verify_release.py
```

Para CUDA, instale la compilación de PyTorch compatible con el controlador y la
plataforma. Los entornos `cu128` y `cu132` corresponden a ejecuciones distintas.

## Separación entre evidencia y nuevas ejecuciones

- `notebooks/`: notebooks canónicos ejecutados, con resultados visibles.
- `reports/executed/v1.0.0/`: espejo versionado e inmutable de esa evidencia.
- `results/frozen/`: tablas, figuras, reportes y auditorías por campaña.

No reejecute ni limpie `reports/executed/`. Una nueva ejecución debe escribir
en un directorio de trabajo separado y producir un conjunto de artefactos con
linaje y versión propios.

## Alcance de reproducción

La versión 1.0.0 certifica integridad, trazabilidad y visibilidad de resultados;
no afirma una reproducción byte a byte de todas las campañas desde un clon
limpio. Los notebooks conservan contratos de nombres y rutas de los
experimentos, instalación dinámica en algunas celdas y una dependencia local
del addendum TT-PINN. Estas condiciones están inventariadas en
`manifests/portability_findings.csv`.

Una replicación independiente debe adaptar esos contratos a la raíz del
repositorio, usar entornos por generación de campaña, registrar hardware y
comparar métricas con tolerancias explícitas. Las campañas largas requieren
recursos de cómputo acordes con los tiempos y configuraciones documentados.

## Archivos grandes

GitHub bloquea archivos mayores de 100 MiB en Git normal.
`XGBOOST_NOX_INTERP_seed42.ubj` tiene 133.653.329 bytes; por ello,
`.gitattributes` asigna `.ubj` y `.pt` a Git LFS.

```bash
git lfs install
git check-attr filter -- models/xgboost/interpolative/NOx/XGBOOST_NOX_INTERP_seed42.ubj
```
