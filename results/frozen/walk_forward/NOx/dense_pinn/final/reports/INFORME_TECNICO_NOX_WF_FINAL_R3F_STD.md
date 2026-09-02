# Informe técnico — NOx walk-forward FINAL R3F_STD

## Diseño ejecutado

Se consumió la configuración 5ada2f51dcae4126cb82b6f20799db63ace1cb77867d975d33a59b39e85e7e05 seleccionada por OPT R3 y
la política FROZEN de 45 épocas. Se entrenaron 10 modelos
con todo DEV. Los escaladores, sintéticos y pesos se ajustaron antes de abrir TEST.
La política adaptativa R3 se verificó solo como procedencia; no intervino en el
entrenamiento FINAL ni en la evaluación sobre TEST.

## Resultado TEST

- R² multisemilla: media=0.250349, DE=0.033736.
- RMSE multisemilla: media=9.635901 mg/m³,
  DE=0.217027 mg/m³.
- PCD TIT: media=99.008789 %, DE=0.446954 %.
- R² del ensamble predeclarado: 0.261133.
- RMSE del ensamble: 9.568526 mg/m³.

## Huella computacional

- Alcance paramétrico: semilla representativa 42.
- Parámetros entrenables: 77665.
- Parámetros totales: 77665.
- Memoria teórica de parámetros FP32:
  0.296268 MiB.
- State dict serializado: 0.300420 MiB.
- Latencia CPU del motor, batch=1: mediana=
  0.065000 ms,
  p95=0.152750 ms,
  p99=0.342335 ms.
- Latencia CPU end-to-end, batch=1: mediana=
  0.344050 ms,
  p95=0.391245 ms,
  p99=0.691412 ms.
- Throughput CPU: 3024865.815 muestras/s.
- Benchmark: CPU, FP32, 20 warm-ups,
  200 repeticiones y
  16 hilos PyTorch.

La latencia del motor mide entrada preprocesada, modelo y salida estandarizada.
La latencia end-to-end incorpora validación numérica, escalado, modelo e inversión
del objetivo. El tamaño serializado corresponde al state_dict, no a memoria RAM.

## Interpretación

Los resultados caracterizan predicción prospectiva walk-forward dentro del dominio
operativo representado por DEV. La consistencia física expresa una sensibilidad
local de la superficie aprendida y no una relación causal global. Esta evaluación
no demuestra transferencia temporal, extrapolación ni conformidad regulatoria.
