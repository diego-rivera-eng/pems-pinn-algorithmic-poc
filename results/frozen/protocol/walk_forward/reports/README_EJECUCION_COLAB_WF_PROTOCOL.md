# Ejecución en Google Colab — protocolo WF R1

1. Conserve `gt_2011.csv` a `gt_2015.csv` en `data/raw/`.
2. Abra `notebooks/00_PEMS_PINN_WF_PROTOCOL - R1.ipynb`.
3. Ejecute **Runtime → Run all** en CPU.
4. Revise que todos los gates de SEC-06 estén en `PASS`.
5. Consuma los manifiestos de `models/wf/work_pinn_wf_protocol/` desde los
   notebooks OPT y FINAL.

El protocolo materializa X solo para 2011–2014. De 2015 lee únicamente el
encabezado; no construye X, y, hashes de contenido ni métricas de ese año.
