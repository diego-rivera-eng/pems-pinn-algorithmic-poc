# Metodología computacional

## Problema y variables

Se estiman dos respuestas continuas de una turbina de gas: CO y NOx. Las nueve
entradas son `AT`, `AP`, `AH`, `AFDP`, `GTEP`, `TIT`, `TAT`, `TEY` y `CDP`.
Los cinco archivos anuales reúnen 36.733 registros.

El estudio compara:

- **PINN densa:** red neuronal totalmente conectada con pérdida supervisada y
  penalización de consistencia física.
- **TT-PINN:** parametrización comprimida *tensor train*, evaluada solo en el
  protocolo interpolativo.
- **XGBoost:** línea base no física, usada en ambos protocolos.

## Restricciones físicas

Las PINN incorporan restricciones direccionales del modelo:

- CO: `∂CO/∂CDP ≤ 0`.
- NOx: `∂NOx/∂TIT ≥ 0`.

El porcentaje de consistencia direccional (`PCD`) mide la fracción de
evaluaciones que cumple el signo esperado. El umbral del 95 % fue un criterio
de control del experimento; no equivale a un límite regulatorio ni prueba causalidad.

## Protocolo interpolativo

1. Se concatenan 2011–2015 conservando identificadores de año y fila.
2. Se forman 168 bloques en el espacio operativo para reducir fuga por
   vecindad.
3. Se congelan 29.845 filas DEV y 6.888 TEST.
4. Solo DEV interviene en búsqueda y selección. La validación cruzada usa cinco
   folds de bloques.
5. El dominio operativo se controla mediante vecinos más cercanos con `k=20`
   y umbral en el cuantil `q=0.99`.
6. TEST se abre una vez después de congelar configuración, épocas y semilla
   representativa.

Los manifiestos autoritativos están bajo `configs/protocols/interpolative/` y
las asignaciones/auditorías bajo `results/frozen/protocol/interpolative/`.

## Protocolo *walk-forward*

Se usa una ventana expansiva, sin TT-PINN:

| Fold | Entrenamiento | Validación |
|---|---|---|
| WF01 | 2011 | 2012 |
| WF02 | 2011–2012 | 2013 |
| WF03 | 2011–2013 | 2014 |
| WF04 | 2011–2014 | 2015 |

Tras la selección, 2015 actúa como prueba externa final (7.384 registros) y se
reporta un ensamble de diez semillas. Las tablas finales se encuentran en
`results/frozen/walk_forward/`.

## Optimización y congelamiento

Las campañas usan Optuna y etapas de confirmación multisemilla. La selección
se basa únicamente en DEV/folds y produce una configuración, política de
entrenamiento y semilla representativa congeladas. Las auditorías `TARGET_ACCESS`,
`PRE_TEST_GATE`, `FROZEN_INPUT` y hashes documentan que el objetivo TEST no fue
usado durante selección.

Para Dense CO/NOx interpolativo se seleccionaron R5/R6; para Dense
*walk-forward*, R3. XGBoost usa R1 en el manuscrito. TT-PINN hereda las
configuraciones/contratos Dense y no abre una búsqueda independiente que pueda
favorecer retrospectivamente a la compresión.

## Métricas

- `R²`: coeficiente de determinación.
- `RMSE`: raíz del error cuadrático medio.
- `MAE`: error absoluto medio.
- `NRMSE_mean (%)`: RMSE normalizado por la media observada del objetivo.
- `bias`: media de `predicción − observación`.
- `PCD (%)`: consistencia con el signo físico esperado.
- tamaño serializado, parámetros/nodos, latencia y *throughput*: evidencia
  computacional, dependiente de formato y hardware.

Las métricas interpolativas de la Tabla 32 corresponden a la semilla
representativa (Dense/TT: CO 126, NOx 84; XGBoost: 42), no al promedio del
ensamble. Las métricas *walk-forward* de la Tabla 34 sí son de ensamble.

## Regla de trazabilidad

Un resultado resumido solo se considera canónico si puede enlazarse a:

```text
datos + protocolo congelado
  -> configuración/selección congelada
  -> ejecución final y modelo
  -> tabla/auditoría primaria
  -> resumen/figura del libro
```

La relación concreta está registrada en `docs/dependency_graph.md` y
`manifests/book_evidence_map.csv`.
