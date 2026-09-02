# Informe técnico — CO interpolativo FINAL R5F_STD

## Contrato

El notebook consumió la configuración `e5d4ddb830ce31387f933b4c4522485991650de24af4aed05e4225610ccd9be8` del trial
89, la seed representativa
126, 85 épocas y `USE_LBFGS=False`. Todas las
decisiones se congelaron con DEV antes de abrir TEST.

## Resultado TEST

- R²: 0.531662
- RMSE: 1.136981 mg/m³
- MAE: 0.593432 mg/m³
- NRMSE_mean: 53.926 %
- PCD CDP_NEG: 99.121 %
- Estado físico: PASS

`NRMSE_mean` no representa Relative Accuracy, RATA ni PS-16. TEST fue abierto una
sola vez y no produjo reentrenamiento, sustitución de candidato ni ajuste de seed,
épocas, lambda o física.
