# Dependencias y linaje de artefactos

## Grafo principal

```mermaid
flowchart TD
    D[data/raw/gt_2011..2015.csv]
    PI[Protocolo interpolativo R1]
    PW[Protocolo walk-forward R1]
    D --> PI
    D --> PW

    PI --> DCO[Dense CO OPT R5]
    PI --> DNO[Dense NOx OPT R6]
    PI --> XCO[XGBoost CO OPT R1]
    PI --> XNO[XGBoost NOx OPT R1]

    DCO --> DCOF[Dense CO R5F_STD]
    DNO --> DNOF[Dense NOx R6F_STD]
    DCO --> TCO[TT-PINN CO R1F_STD]
    DNO --> TNO[TT-PINN NOx R1F_STD]
    XCO --> XCOF[XGBoost CO R1F_STD]
    XNO --> XNOF[XGBoost NOx R1F_STD]

    PW --> WDC[Dense CO WF R3/R3F_STD]
    PW --> WDN[Dense NOx WF R3/R3F_STD]
    PW --> WXC[XGBoost CO WF R1/R1F_STD]
    PW --> WXN[XGBoost NOx WF R1/R1F_STD]

    DCOF --> T32[Tabla 32]
    DNOF --> T32
    TCO --> T32
    TNO --> T32
    XCOF --> T32
    XNOF --> T32
    DCOF --> T33[Tabla 33]
    DNOF --> T33
    TCO --> T33
    TNO --> T33
    XCOF --> T33
    XNOF --> T33
    WDC --> T34[Tabla 34]
    WDN --> T34
    WXC --> T34
    WXN --> T34
```

## Contratos de dependencia

- El protocolo es inmutable aguas arriba de toda búsqueda de hiperparámetros.
- La optimización no puede abrir TEST y debe congelar configuración/política
  antes del notebook final.
- El notebook final verifica hashes de sus entradas, entrena semillas
  predeclaradas y abre TEST una vez.
- TT-PINN consume la configuración Dense seleccionada para aislar el efecto de
  compresión; no realiza una búsqueda oportunista independiente.
- Los resúmenes y figuras son consumidores, nunca fuentes autoritativas de
  métricas.

## Dependencias de software

| Área | Dependencias directas |
|---|---|
| Datos y métricas | NumPy, pandas, SciPy, scikit-learn |
| PINN Dense/TT | PyTorch, matplotlib, psutil |
| Optimización | Optuna, joblib |
| Línea base | XGBoost |
| Notebooks | Jupyter/IPython, nbconvert |
| Colab histórico | `google.colab` opcional, no requerido por el repositorio |

El addendum computacional TT-PINN tiene una dependencia heredada en
`tools.tt_pinn_computational_benchmark_r1`. Sus resultados se preservan como evidencia, pero esa ejecución no constituye
una receta portable desde la distribución pública.
