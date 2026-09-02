# Informe técnico — XGBoost CO walk-forward FINAL R1F_STD

## Diseño

Se consumió sin cambios la configuración 54da4c07c37bc77d482bdba3f32fd36870adc3eb31e2795748e35698894442a7 y la
política de 144 árboles. Se entrenaron diez modelos con DEV
2011–2014 antes de abrir 2015. El ensamble es la media aritmética de las diez
semillas predeclaradas. No se aplicaron restricciones monotónicas, pérdida
física, sintéticos, selección de variables, escalamiento de X ni clipping.

## Resultado WF04 — TEST 2015

- R² del ensamble: 0.525790.
- RMSE: 1.538956 mg/m³.
- MAE: 0.945574 mg/m³.
- Sesgo: -0.746127 mg/m³.
- RMSE del decil superior: 3.470343 mg/m³.
- Predicciones negativas: 0.000000 %.

## Complejidad

- Árboles: 144.
- Nodos: 11142.
- Hojas: 5643.
- UBJ representativo: 0.453125 MiB.
- UBJ de diez modelos: 4.545921 MiB.
- Latencia CPU motor, batch=1: mediana=
  0.076150 ms,
  p95=0.217600 ms y
  p99=0.273876 ms.
- Latencia CPU end-to-end, batch=1: mediana=
  0.076800 ms,
  p95=0.186035 ms y
  p99=0.276784 ms.
- Throughput CPU sobre 7384 filas:
  548759.643 muestras/s.

## Alcance

Los resultados describen la frontera prospectiva 2011–2014 → 2015. No
demuestran desempeño fuera del periodo observado, causalidad ni conformidad
regulatoria PEMS/CEMS/RATA.
