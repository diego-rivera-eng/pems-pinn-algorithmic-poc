# Informe técnico — XGBoost NOX interpolativo FINAL R1F_STD

## Diseño

Se consumió sin cambios la configuración 6f348ea7343fe566f381e96842be3d4a5087f4d1624eaafd5196ff830bd676b8 y la
política de 1445 árboles. Se entrenaron diez modelos con DEV
completo antes de abrir TEST. El ensamble es la media aritmética de las diez
semillas predeclaradas. No se aplicaron restricciones monotónicas, pérdida
física, sintéticos, selección de variables, escalamiento de X ni clipping.

## Resultado TEST

- R² del ensamble: 0.744565.
- RMSE: 4.738998 mg/m³.
- MAE: 3.182540 mg/m³.
- Sesgo: 0.328661 mg/m³.
- RMSE del decil superior: 8.624623 mg/m³.
- Predicciones negativas: 0.000000 %.

## Complejidad

- Árboles: 1445.
- Nodos: 3902865.
- Hojas: 1952155.
- UBJ representativo: 127.461747 MiB.
- UBJ de diez modelos: 1276.389494 MiB.
- Latencia CPU motor, batch=1: mediana=
  0.254750 ms,
  p95=0.354655 ms y
  p99=0.398785 ms.
- Latencia CPU end-to-end, batch=1: mediana=
  0.258950 ms,
  p95=0.360725 ms y
  p99=0.484265 ms.
- Throughput CPU sobre 6888 filas:
  12145.380 muestras/s.

## Alcance

Los resultados describen interpolación dentro del soporte operativo del
protocolo R1. No demuestran transferencia temporal, extrapolación, relación
causal ni conformidad regulatoria PEMS/CEMS/RATA.
