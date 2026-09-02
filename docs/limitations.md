# Limitaciones

## Científicas

- Los datos corresponden a una turbina y un periodo históricos; no demuestran
  generalización a otras máquinas, combustibles, sensores o regímenes.
- El caso Kaya cubre aproximadamente 75–100 % de carga y no caracteriza de
  forma suficiente arranque, parada, baja carga ni transitorios.
- La planta de origen está en Turquía; la transferencia a activos colombianos
  requiere datos y validación locales.
- La evaluación interpolativa mezcla años y controla similitud operacional por
  bloques, pero no sustituye una validación temporal.
- En *walk-forward* aparece degradación y sesgo, en especial para NOx; el cambio
  de distribución forma parte del resultado.
- Las restricciones físicas son monotonicidades parciales del modelo. PCD ≥95
  % no certifica cumplimiento ambiental ni validez causal.
- La monotonía NOx/TIT es una hipótesis *ceteris paribus*; para CO, la
  restricción se limita a `CDP_NEG`.
- XGBoost no se entrenó con la penalización física de las PINN; su análisis de
  signo es diagnóstico poshoc.
- TT-PINN no se incluyó en *walk-forward* y su comparación física en CO no
  supera el margen informativo de un punto porcentual.

## Computacionales

- Los resultados proceden de varias versiones de NumPy, pandas, scikit-learn,
  PyTorch y CUDA.
- Latencia y *throughput* dependen del hardware y solo son comparables bajo el
  protocolo y dispositivo declarados.
- El modelo XGBoost–NOx excede 100 MiB y requiere Git LFS.
- No se distribuyen todos los pesos multisemilla ni los estados Optuna.

## Reproducibilidad

- Los notebooks preservan código y contratos de nombres/rutas usados durante
  los experimentos.
- El addendum computacional TT depende de una utilidad histórica que no se
  distribuye como módulo público independiente.
- `requirements.txt` es un entorno de referencia, no un lockfile único para
  todas las campañas.
- La distribución verifica integridad y trazabilidad, pero no constituye una
  reproducción byte a byte desde un clon limpio.
- No existe en la evidencia una validación RATA/PS-16 ni una demostración de
  integración con DCS/SCADA o controles de ciberseguridad OT.

## Distribución

- El material original se publica bajo un aviso de derechos reservados, no una
  licencia de código abierto.
- La Figura 16 no se redistribuye porque es una adaptación de literatura
  externa.
- El trabajo de maestría completo no forma parte del repositorio; su referencia
  bibliográfica se incluye en `references/BIBLIOGRAPHY.md`.

## Uso responsable

Los modelos son una prueba de concepto académica. No deben emplearse para
control operativo, seguridad industrial, cumplimiento regulatorio ni decisiones
ambientales sin validación independiente, calibración de incertidumbre y
gobernanza del sistema de destino.
