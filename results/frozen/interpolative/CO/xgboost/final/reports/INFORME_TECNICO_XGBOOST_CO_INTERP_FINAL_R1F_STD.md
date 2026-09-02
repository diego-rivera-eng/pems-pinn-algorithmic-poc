# Informe técnico — XGBoost CO interpolativo FINAL R1F_STD

## Diseño

Se consumió sin cambios la configuración 9c254d014635ed5849756616f5ed8ef37b078c2ae7c2cf149831a2a07060d629 y la
política de 320 árboles. Se entrenaron diez modelos con DEV
completo antes de abrir TEST. El ensamble es la media aritmética de las diez
semillas predeclaradas. No se aplicaron restricciones monotónicas, pérdida
física, sintéticos, selección de variables, escalamiento de X ni clipping.

## Resultado TEST

- R² del ensamble: 0.508942.
- RMSE: 1.164232 mg/m³.
- MAE: 0.602052 mg/m³.
- Sesgo: -0.218088 mg/m³.
- RMSE del decil superior: 3.246676 mg/m³.
- Predicciones negativas: 0.000000 %.

## Complejidad

- Árboles: 320.
- Nodos: 54838.
- Hojas: 27579.
- UBJ representativo: 1.980263 MiB.
- UBJ de diez modelos: 19.762773 MiB.
- Latencia CPU motor, batch=1: mediana=
  0.082400 ms,
  p95=0.160095 ms y
  p99=0.215013 ms.
- Latencia CPU end-to-end, batch=1: mediana=
  0.085800 ms,
  p95=0.155885 ms y
  p99=0.199138 ms.
- Throughput CPU sobre 6888 filas:
  231092.085 muestras/s.

## Alcance

Los resultados describen interpolación dentro del soporte operativo del
protocolo R1. No demuestran transferencia temporal, extrapolación, relación
causal ni conformidad regulatoria PEMS/CEMS/RATA.
