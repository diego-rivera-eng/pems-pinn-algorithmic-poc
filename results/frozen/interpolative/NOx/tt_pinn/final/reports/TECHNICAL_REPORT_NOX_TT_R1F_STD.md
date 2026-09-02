# Informe técnico - NOx TT-PINN R1F_STD

## Identidad y alcance

- Versión: `TT_PINN_NOX_INTERP_FINAL_R1F_STD`.
- Fuente: `05_TT_PINN_NOX_INTERP_FINAL - R1F_STD.ipynb`.
- SHA-256 de la fuente: `9dbb4ef0a5671daba41fff05003295346e136be52d760d2b32e9dba2922aada1`.
- Derivación: baseline densa autenticada `04_Gold_Standard_PINN_NOX_INTERP_FINAL - R6F_STD.ipynb`.
- Semilla/épocas heredadas: `84` / `100`.
- Modelos TT entrenados: `1`; ensembles: `0`.
- Búsqueda o selección TT por métricas: `False`.

## Contrato Tensor-Train

- Formato: `TT_2D_SEPARATED_3WAY_CORES`.
- Orden: `3`; rango uniforme: `12`.
- Parámetros densos/TT: `69187` / `13891`.
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
  "R2": 0.7685886952250564,
  "RMSE": 4.510648475061918,
  "MAE": 3.0611336998269394,
  "NRMSE_range": 0.04912222536228069,
  "NRMSE_std": 0.48101736816495627,
  "bias": 0.3552179519307738,
  "residual_std": 4.496966289077898,
  "pearson_r": 0.877512989924361,
  "slope": 0.7680270168742128,
  "intercept": 14.432788098891304,
  "negative_prediction_pct": 0.0,
  "NRMSE_mean_pct": 7.432735227925932
}
```

Física TT TEST:

```text
{
  "split": "TEST",
  "physics_mode": "TIT_INC",
  "physics_feature": "TIT",
  "expected_derivative_sign": ">= 0",
  "PCD_pct": 100.0,
  "violation_pct": 0.0,
  "near_zero_pct": 0.0,
  "physical_gradient_mean": 0.896102786064148,
  "physical_gradient_median": 0.713744044303894,
  "physical_gradient_q05": 0.3067200481891632,
  "physical_gradient_q95": 2.198380708694458,
  "dimensionless_gradient_mean": 1.314880132675171,
  "diagnostic_feature": "CDP",
  "diagnostic_negative_gradient_pct": 87.109375,
  "diagnostic_positive_gradient_pct": 12.890625,
  "diagnostic_near_zero_pct": 0.0,
  "diagnostic_gradient_median": -3.313124418258667
}
```

Comparación densa/TT:

```text
metric,dense,tt,tt_minus_dense
R2,0.7748021023445689,0.7685886952250564,-0.006213407119512571
RMSE,4.449680856256315,4.510648475061918,0.060967618805602974
MAE,3.034638218763398,3.0611336998269394,0.026495481063541604
bias,0.7416671261139448,0.3552179519307738,-0.386449174183171
pearson_r,0.8839968734316708,0.877512989924361,-0.006483883507309773
PCD_pct,100.0,100.0,0.0

```

No inferioridad predeclarada: `PASS`. Los márgenes
son supuestos de ingeniería R1F_STD, no valores del artículo TT-PINN ni
una norma PEMS. El resultado es informativo y nunca activa ajuste.

## Cierre de gobernanza

- Modelo, configuración y contrato TT conservaron sus hashes post-TEST.
- TEST no eligió rango, arquitectura, seed, épocas ni hiperparámetros.
- No hubo búsqueda, ranking, ensemble ni reentrenamiento post-TEST.
