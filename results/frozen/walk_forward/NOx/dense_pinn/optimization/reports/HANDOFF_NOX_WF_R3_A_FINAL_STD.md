# Handoff NOx walk-forward: OPT a FINAL_STD

## Estado congelado

- Estado: FROZEN
- Protocolo productor: `00_PEMS_PINN_WF_PROTOCOL - R1.ipynb`
- Notebook fuente: `04_Gold_Standard_PINN_NOX_WF_OPT - R3_POC_EFFICIENT.ipynb`
- Notebook destino: `04_Gold_Standard_PINN_NOX_WF_FINAL - R3F_STD.ipynb`
- Consumidor directo autorizado: `04_Gold_Standard_PINN_NOX_WF_FINAL - R3F_STD.ipynb`
- Fuente de selección: DEV-only, WF01–WF03 completos.
- TEST abierto o evaluado: no.
- Trial campeón: 33
- Hash de configuración: `5ada2f51dcae4126cb82b6f20799db63ace1cb77867d975d33a59b39e85e7e05`
- Hash de asignación: `54b1229774a57cb5e708340040e8171839cd320b72cd90058879a7f9e638f89b`
- Hash de folds: `2b4f6970215ab0ea6c2d3f3d8bb3288ba5c22c8c54af0a9f853f9a649c3b2dcd`

## Configuración ganadora

- Arquitectura: `[128, 160, 192, 128]`
- Activación: `tanh`
- Optimizador: `AdamW`
- Learning rate: `0.003385820092605622`
- Batch size: `512`
- Transformación del objetivo: `log1p`
- Lambda física: `4.784133019826852`
- Modo físico: `TIT_INC`
- kNN heredado del protocolo: `k=20, q=0.99`

## Presupuesto efectivo de Optuna

- Intentados: 55
- Completos: 55
- Podados: 0
- Fallidos: 0
- Anchors: evaluación obligatoria en tres folds.
- Trials: evaluación completa de WF01–WF03, sin screening temporal parcial.
- Parada: hard cap R2 preservado; fallback Top-3 R3 versionado.
- La densidad competitiva R2 no fue reetiquetada como suficiente.
- El ganador solo se congeló después de confirmación multisemilla.

## Confirmación y ablación

- Confirmación inicial: hasta 3 candidatos × 3 semillas × 3 folds.
- Finalistas: hasta 2 candidatos × 5 semillas × 3 folds.
- Campeón: seleccionado después de la ampliación común.
- Ablación pareada: 3 semillas × 3 folds.

## Política final de épocas

- `FINAL_EPOCHS`: 45
- Rango observado: 5 a 155
- Número de observaciones: 15

## Ablación pareada PINN menos MLP sobre DEV

- `delta_R2`: media=0.181225, DE=0.254057, mediana=0.0227148
- `delta_RMSE`: media=-1.0274, DE=1.32404, mediana=-0.227132
- `delta_MAE`: media=-1.14342, DE=1.49189, mediana=-0.279412
- `delta_bias_abs`: media=-1.49988, DE=2.14289, mediana=-0.369065
- `delta_training_time`: media=20.5459, DE=11.7061, mediana=21.3468
- `delta_PCD`: media=24.9891, DE=10.0349, mediana=24.707

El notebook FINAL debe verificar los hashes, entrenar con la política congelada y
abrir TEST una sola vez para la evaluación final. Este handoff no contiene métricas
de TEST.
