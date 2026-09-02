# Informe técnico - CO TT-PINN R1F_STD

## Identidad y alcance

- Versión: `TT_PINN_CO_INTERP_FINAL_R1F_STD`.
- Fuente: `05_TT_PINN_CO_INTERP_FINAL - R1F_STD.ipynb`.
- SHA-256 de la fuente: `b713f45a7a42f8bacd5eb29a888e0b0b154747e11d7b6aa16915d85d9e436de1`.
- Derivación: baseline densa autenticada `04_Gold_Standard_PINN_CO_INTERP_FINAL - R5F_STD.ipynb`.
- Semilla/épocas heredadas: `126` / `85`.
- Modelos TT entrenados: `1`; ensembles: `0`.
- Búsqueda o selección TT por métricas: `False`.

## Contrato Tensor-Train

- Formato: `TT_2D_SEPARATED_3WAY_CORES`.
- Orden: `3`; rango uniforme: `11`.
- Parámetros densos/TT: `62977` / `12582`.
- Reconstrucción densa en `forward`: `False`.
- Entrada, salida y sesgos: densos; transiciones ocultas: TT.

## TEST y resultados

TEST se materializó una vez dentro de esta ejecución TT después de firmar,
serializar y recargar el modelo. La baseline densa ya había utilizado TEST
en su ejecución histórica; el notebook no afirma virginidad global.

Métricas TT TEST:

```text
{
  "split": "TEST",
  "role": "FINAL_HOLDOUT",
  "R2": 0.5222426348684107,
  "RMSE": 1.1483571412682714,
  "MAE": 0.6001136108819702,
  "NRMSE_range": 0.04519145783169148,
  "NRMSE_std": 0.6911497698084126,
  "bias": -0.26652373047599637,
  "residual_std": 1.117081192594041,
  "pearson_r": 0.7402910719003412,
  "slope": 0.5426325809548488,
  "intercept": 0.6977961952449316,
  "negative_prediction_pct": 0.0,
  "NRMSE_mean_pct": 54.4654501834103
}
```

Física TT TEST:

```text
{
  "split": "TEST",
  "physics_mode": "CDP_NEG",
  "physics_feature": "CDP",
  "expected_derivative_sign": "<= 0",
  "PCD_pct": 97.705078125,
  "violation_pct": 2.294921875,
  "near_zero_pct": 0.0,
  "physical_gradient_mean": -0.24129602313041687,
  "physical_gradient_median": -0.19395555555820465,
  "physical_gradient_q05": -0.6768106818199158,
  "physical_gradient_q95": -0.01886782981455326,
  "dimensionless_gradient_mean": -0.14883428812026978,
  "diagnostic_feature": "TIT",
  "diagnostic_negative_gradient_pct": 45.703125,
  "diagnostic_positive_gradient_pct": 54.296875,
  "diagnostic_near_zero_pct": 0.0,
  "diagnostic_gradient_median": 0.010038177482783794
}
```

Comparación densa/TT:

```text
metric,dense,tt,tt_minus_dense
R2,0.5316617033943354,0.5222426348684107,-0.009419068525924668
RMSE,1.1369807611652285,1.1483571412682714,0.011376380103042871
MAE,0.593431860573036,0.6001136108819702,0.006681750308934253
bias,-0.2074544107602015,-0.26652373047599637,-0.05906931971579488
pearson_r,0.7403056722428606,0.7402910719003412,-1.4600342519432985e-05
PCD_pct,99.12109375,97.705078125,-1.416015625

```

No inferioridad predeclarada: `NOT_MET_INFORMATIONAL`. Los márgenes
son supuestos de ingeniería R1F_STD, no valores del artículo TT-PINN ni
una norma PEMS. El resultado es informativo y nunca activa ajuste.

## Cierre de gobernanza

- Modelo, configuración y contrato TT conservaron sus hashes post-TEST.
- TEST no eligió rango, arquitectura, seed, épocas ni hiperparámetros.
- No hubo búsqueda, ranking, ensemble ni reentrenamiento post-TEST.
