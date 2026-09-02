# Informe técnico — CO walk-forward FINAL R3F_STD

## Diseño ejecutado

Se consumió la configuración 4c3e9076ccc96176de854e87f203d92c46b381da88c87bfadeda70af2126f1c2 seleccionada por CO OPT R3,
exclusivamente con modo `CDP_NEG` y 30 épocas congeladas. La
política adaptativa R3 se verificó solo como procedencia y no intervino en TEST. Se
entrenaron 10 modelos con todo DEV. Escaladores, escalas físicas
robustas, sintéticos CDP y pesos quedaron ajustados antes de abrir TEST.

## Resultado TEST

- R² multisemilla: media=0.463581, DE=0.018884.
- RMSE multisemilla: media=1.636564 mg/m³,
  DE=0.028689 mg/m³.
- PCD de ∂CO/∂CDP≤0: media=99.936523 %,
  DE=0.056616 %.
- Violación CDP: media=0.063477 %.
- Mediana de ∂CO/∂CDP: media entre semillas=-0.650420.
- R² del ensamble predeclarado: 0.476388.
- RMSE del ensamble: 1.617133 mg/m³.

## Huella computacional

- Semilla representativa: 42.
- Parámetros entrenables: 50273.
- Memoria teórica FP32: 0.191776 MiB.
- State dict serializado: 0.195928 MiB.
- Latencia CPU del motor, batch=1: mediana=
  0.048900 ms,
  p95=0.068405 ms.
- Latencia CPU end-to-end, batch=1: mediana=
  0.160550 ms,
  p95=0.228215 ms.
- Throughput CPU: 4785948.114 muestras/s.

## Interpretación

La derivada negativa respecto a CDP expresa sensibilidad local de la superficie
aprendida; no establece causalidad ni una ley global. Esta evaluación no demuestra
transferencia temporal, extrapolación ni conformidad regulatoria. No se evaluaron
restricciones físicas respecto a TIT ni combinaciones duales.
