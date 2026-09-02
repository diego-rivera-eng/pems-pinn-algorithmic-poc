# Informe técnico — XGBoost NOX walk-forward FINAL R1F_STD

## Diseño

Se consumió sin cambios la configuración c3f6ea945fde5b226dc4d00e915ecd01e3ca02514412e66a095d3e589af67e5b y la
política de 1032 árboles, derivadas de WF01–WF03. Se entrenaron
diez modelos con DEV 2011–2014 completo antes de abrir 2015. El ensamble es la
media aritmética de las diez semillas predeclaradas. No se aplicaron
restricciones monotónicas, pérdida física, sintéticos, selección de variables,
escalamiento de X ni clipping.

## Resultado WF04 / 2015

- R² del ensamble: 0.127531.
- RMSE: 10.397689 mg/m³.
- MAE: 8.493789 mg/m³.
- Sesgo: 7.624277 mg/m³.
- RMSE del decil superior: 9.508015 mg/m³.
- Predicciones negativas: 0.000000 %.

## Complejidad

- Árboles: 1032.
- Nodos: 762196.
- Hojas: 381614.
- UBJ representativo: 25.364484 MiB.
- UBJ de diez modelos: 253.154952 MiB.
- Latencia CPU motor, batch=1: mediana=
  0.135800 ms,
  p95=0.455330 ms y
  p99=0.678594 ms.
- Latencia CPU end-to-end, batch=1: mediana=
  0.145000 ms,
  p95=0.318575 ms y
  p99=0.447769 ms.
- Throughput CPU sobre 7384 filas:
  20264.562 muestras/s.

## Alcance

Los resultados describen transferencia prospectiva desde DEV 2011–2014 hacia
la frontera anual 2015. No demuestran desempeño fuera de ese horizonte,
relación causal ni conformidad regulatoria PEMS/CEMS/RATA.
