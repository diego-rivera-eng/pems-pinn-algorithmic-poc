# Handoff CO walk-forward: OPT a FINAL_STD

## Estado congelado

- Estado: FROZEN
- Protocolo productor: `00_PEMS_PINN_WF_PROTOCOL - R1.ipynb`
- Notebook fuente: `04_Gold_Standard_PINN_CO_WF_OPT - R3_POC_EFFICIENT.ipynb`
- Notebook destino: `04_Gold_Standard_PINN_CO_WF_FINAL - R3F_STD.ipynb`
- Consumidor directo autorizado: `04_Gold_Standard_PINN_CO_WF_FINAL - R3F_STD.ipynb`
- Fuente de selección: DEV-only, WF01–WF03 completos.
- TEST abierto o evaluado: no.
- Trial campeón: 44
- Hash de configuración: `4c3e9076ccc96176de854e87f203d92c46b381da88c87bfadeda70af2126f1c2`
- Hash de asignación: `54b1229774a57cb5e708340040e8171839cd320b72cd90058879a7f9e638f89b`
- Hash de folds: `2b4f6970215ab0ea6c2d3f3d8bb3288ba5c22c8c54af0a9f853f9a649c3b2dcd`

## Configuración ganadora

- Arquitectura: `[160, 96, 128, 160]`
- Activación: `silu`
- Optimizador: `NAdam`
- Learning rate: `0.005161791616846958`
- Batch size: `128`
- Transformación del objetivo: `original`
- Lambda física: `3.072177718432149`
- Modo físico: `CDP_NEG`
- kNN heredado del protocolo: `k=20, q=0.99`

## Presupuesto efectivo de Optuna

- Intentados: 55
- Completos: 55
- Podados: 0
- Fallidos: 0
- Motivo de parada: PRACTICAL_PLATEAU
- Modo de autorización: PRIMARY_COMPETITIVE_GATES
- Anchors: evaluación obligatoria en tres folds.
- Trials: evaluación completa de WF01–WF03, sin screening temporal parcial.
- Parada primaria: suficiencia competitiva y mejora material predefinidas.
- Fallback: Top-3 jerárquico únicamente al hard cap.
- El fallback no congela un ganador: exige confirmación multisemilla.

## Confirmación y ablación

- Confirmación inicial: hasta 3 candidatos × 3 semillas × 3 folds.
- Finalistas: hasta 2 candidatos × 5 semillas × 3 folds.
- Campeón: seleccionado después de la ampliación común.
- Ablación pareada: 3 semillas × 3 folds.

## Política final de épocas

- `FINAL_EPOCHS`: 30
- Rango observado: 5 a 115
- Número de observaciones: 15

## Ablación pareada PINN menos MLP sobre DEV

- `delta_R2`: media=0.0783833, DE=0.0541837, mediana=0.0578193
- `delta_RMSE`: media=-0.138771, DE=0.0865398, mediana=-0.0987283
- `delta_MAE`: media=-0.102255, DE=0.056547, mediana=-0.0832066
- `delta_bias_abs`: media=-0.104858, DE=0.120017, mediana=-0.107723
- `delta_training_time`: media=64.0184, DE=22.105, mediana=67.6025
- `delta_PCD`: media=43.5547, DE=10.5117, mediana=46.875

El notebook FINAL debe verificar los hashes, entrenar con la política congelada y
abrir TEST una sola vez para la evaluación final. Este handoff no contiene métricas
de TEST.
