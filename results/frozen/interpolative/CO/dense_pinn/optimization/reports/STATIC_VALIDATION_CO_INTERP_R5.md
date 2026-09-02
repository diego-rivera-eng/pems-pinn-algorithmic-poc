# Validación técnica — CO INTERP OPT R5

- Notebook: 04_Gold_Standard_PINN_CO_INTERP_OPT - R5.ipynb
- SHA-256: 7685A2C54626A3BEB5792D77DCC33EB19D5884683D89AC3A7D4898632D6A2612
- Celdas: 127
- Validación estática: PASS
- SMOKE científico serial: PASS
- Equivalencia paralela local: NO EJECUTADA por fallo nativo pyarrow/loky en Windows
- FULL_AUTO: NO EJECUTADO
- TEST abierto: NO

## Checklist

- PASS — json
- PASS — cell_order
- PASS — code_syntax
- PASS — protocol_r1_immutable
- PASS — source_references_unchanged
- PASS — target_co_only
- PASS — features_exactly_nine
- PASS — physics_fixed_cdp_neg
- PASS — no_historical_candidates
- PASS — test_target_closed
- PASS — optuna_single_writer
- PASS — median_pruner_fold_unit
- PASS — barrier_2_plus_3
- PASS — dynamic_early_stop
- PASS — adaptive_stop_constants
- PASS — confirmation_10x5x5
- PASS — pcd_gate_95
- PASS — lbfgs_policy
- PASS — matched_ablation_5x5
- PASS — representative_seed_rule
- PASS — final_epochs_median
- PASS — nine_opt_figures
- PASS — no_custom_python_dependency

## Desviación de entorno

El preflight de 2–3 procesos debe repetirse en Google Colab. El entorno local presentó una excepción nativa de pyarrow al importar dependencias en procesos loky; la ruta serial permitida por el notebook completó el SMOKE. Esta incidencia no autoriza FULL_AUTO paralelo hasta obtener PASS en Colab.
