# Informe técnico — NOx interpolativo FINAL R6F_STD

## Contrato

Se consumió la configuración bd63d936348b6886210e5ede9b0487741c724167eca7256629e6519c58109fa5 del trial
37, la seed 84,
100 épocas y USE_LBFGS=False. Todas las decisiones fueron
congeladas con DEV antes de abrir TEST.

## Resultado TEST

- R²: 0.774802
- RMSE: 4.449681 mg/m³
- MAE: 3.034638 mg/m³
- NRMSE_mean: 7.332 %
- PCD TIT_INC: 100.000 %
- Estado físico informativo: PASS

TEST fue abierto una vez. Los hashes del modelo, la configuración y el
manifiesto permanecieron idénticos antes y después de la evaluación. No hubo
selección, ajuste ni reentrenamiento post hoc. El gradiente respecto de CDP
se reporta únicamente como diagnóstico y no es una restricción física.
