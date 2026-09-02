# Modelos finales distribuidos

El repositorio distribuye 46 pesos finales (`.pt`/`.ubj`) y 40 archivos de
metadatos. Se incluyen completos:

- Dense y TT interpolativos disponibles;
- los diez modelos Dense *walk-forward* por objetivo;
- los diez modelos XGBoost–CO interpolativos;
- los diez modelos XGBoost–CO *walk-forward*.

Para XGBoost–NOx se distribuye `seed42` y los metadatos de las diez semillas. Los
nueve binarios restantes de cada escenario se catalogan por tamaño y SHA-256 en
`manifests/model_catalog.csv`, pero no se duplican en esta versión:

- ensamble interpolativo completo: aproximadamente 1,338 GB;
- ensamble *walk-forward* completo: aproximadamente 265 MB.

El inventario de los 46 pesos presentes está en
`manifests/model_inventory.csv`; el catálogo completo contiene 64 binarios y 40
metadatos. Todos los `.pt` y `.ubj` presentes usan Git LFS.

No cargue pesos descargados sin verificar su checksum. Véase `SECURITY.md`.
