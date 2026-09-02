# Addendum computacional post hoc — CO — R1

Estado: `COMPLETE`. Campaña append-only; los notebooks, manifiestos y checkpoints
base permanecen congelados.

## Resultado principal en CUDA

| model_family | parameter_count | checkpoint_mb_decimal | latency_batch1_p50_ms | latency_batch1_p95_ms | throughput_batch4096_p50_rows_s | forward_linear_macs_per_row |
| --- | --- | --- | --- | --- | --- | --- |
| DENSE_PINN | 62977 | 0.261215 | 0.1847 | 0.431305 | 2.38285e+07 | 62304 |
| TT_PINN | 12582 | 0.068373 | 1.2206 | 2.03603 | 2.36858e+06 | 41598 |

La TT-PINN reduce parámetros en
`80.02%`, el checkpoint en
`73.83%` y los MAC lineales
del forward en `33.23%`.
En esta GPU, su razón de latencia TT/denso fue
`6.61x` y su razón de throughput
TT/denso fue `0.099x`.

La compresión de parámetros no implica aceleración automática: la contracción TT
se descompone en varios `einsum`, crea temporales y lanza más operaciones pequeñas.

## Alcance de las métricas

- Entradas estandarizadas sintéticas y deterministas; no se abrió ningún dataset,
  target, predicción ni métrica TEST.
- Latencia: tiempo de pared del forward más sincronización del dispositivo, batch 1.
- Throughput principal: filas/s para batch 4096; se preservan todas las muestras.
- Memoria: `torch.cuda.max_memory_allocated/reserved`; describe el asignador de
  PyTorch, no la VRAM total del proceso.
- MAC/FLOP: costo analítico de capas lineales por fila; `FLOP=2*MAC` bajo convención
  FMA2. Excluye bias, activaciones, loss físico y backward.
- Paso de entrenamiento: dos pasos (cold/steady) sobre una copia desechable en
  memoria, con batch ya preparado y regularizador físico de primera derivada.
  Esa copia cambia y se elimina; no se guarda. El hash del checkpoint persistente
  se verifica antes/después. No equivale a tiempo de convergencia ni energía.
- Tiempo total de entrenamiento a convergencia y energía: `NOT_MEASURED`; exigirían
  una campaña nueva de reentrenamiento pareado.

## Complejidad por arquitectura

| target | model_family | forward_linear_macs_per_row | forward_linear_flops_per_row | scope |
| --- | --- | --- | --- | --- |
| CO | DENSE_PINN | 62304 | 124608 | linear_forward_only_excludes_bias_activation_loss_backward |
| CO | TT_PINN | 41598 | 83196 | linear_forward_only_excludes_bias_activation_loss_backward |

## Fidelidad respecto al paper TT-PINN

| criterion | status | evidence |
| --- | --- | --- |
| Hidden dense matrices represented by 2d three-way TT cores | CONFORMANT | tt_contract.tensor_format=TT_2D_SEPARATED_3WAY_CORES |
| Boundary TT ranks r0=r2d=1 | CONFORMANT | Every frozen hidden-layer rank vector starts and ends at 1 |
| Forward pass contracts TT cores without reconstructing dense W | CONFORMANT | contract_tt_cores uses sequential einsum; contract flag is false |
| TT cores were optimized end-to-end by autograd | CONFORMANT | Base notebook gradient/reload tests and final TT checkpoint |
| Dense input/output boundaries and biases retained | CONFORMANT | Frozen TT architecture contract |
| Uniform TT rank chosen without predictive metrics | ADAPTATION | Maximum rank satisfying the predeclared parameter/state_dict budget |
| Paper PDE residual plus IC/BC/collocation objective reproduced | NOT_REPRODUCED | CO uses a monotonic first-derivative regularizer, not a PDE residual with initial/boundary conditions |
| Paper PDE benchmark suite reproduced | NOT_REPRODUCED | Industrial emissions regression task, not the paper PDE systems |
| Paper optimizer, activation, initialization, and iteration schedule reproduced | EXPERIMENTAL_DIFFERENCE | Inherited emissions-model configuration differs from the paper experiments |
| Edge-computing hardware reproduced | NOT_REPRODUCED | Local desktop CPU and NVIDIA RTX GPU benchmark |
| Scientifically accurate model label | PARTIAL_METHOD_CONFORMANCE | Physics-monotonic regression compressed with the paper's TT architecture; not a full reproduction of the paper's PDE methodology |

Conclusión: es una **regresión físico-monótona comprimida con la arquitectura TT
del paper**. La representación, rangos frontera y contracción directa son fieles;
no es una reproducción integral de la metodología PDE del paper ni de su hardware edge.
