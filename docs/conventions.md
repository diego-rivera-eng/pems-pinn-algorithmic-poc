# Convenciones de mantenimiento

## Rutas y versiones

- Las rutas públicas son relativas a la raíz del repositorio.
- Los nombres estables (`final.ipynb`, `metrics_summary.csv`) viven en Git; las
  versiones se expresan en manifiestos, tags y releases.
- Una revisión científica nueva no sobrescribe artefactos `FROZEN`; produce un
  conjunto nuevo con linaje explícito.

## Estados

- `PROTOCOL`: partición/dominio congelado.
- `OPTIMIZATION`: búsqueda y confirmación sin acceso a TEST.
- `FINAL_CANONICAL`: consumidor autorizado de una optimización congelada.
- `SUPPORTING_ANALYSIS`: comparación o diagnóstico derivado.
- `EXECUTED_EVIDENCE`: notebook ejecutado preservado, no editable.
- `SUPPLEMENTARY`: válido para contexto, no autoritativo para las tablas del
  manuscrito.
- `ARCHIVED_OR_EXCLUDED`: respaldo, intermedio, duplicado o artefacto operativo.

## Cambios de resultados

Todo cambio que altere datos, particiones, features, búsqueda, semilla,
restricción física o definición de métrica invalida resultados aguas abajo. La
actualización debe incluir:

1. versión nueva;
2. manifiesto de inputs y SHA-256;
3. auditoría de acceso a TEST;
4. comparación contra la versión anterior;
5. actualización del mapa de evidencia y changelog.
