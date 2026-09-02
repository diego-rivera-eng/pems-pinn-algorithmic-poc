# Reportes y evidencia ejecutada

`executed/v1.0.0/` preserva un espejo versionado de los notebooks ejecutados que
también se presentan en `notebooks/`. Es evidencia inmutable y no un punto de
edición. Las rutas de perfil de usuario se sustituyeron por `<USER_HOME>` en
los archivos transformados; el SHA-256 del original y el de la copia pública
figuran en el manifiesto de migración.

Las salidas pueden contener información del entorno de cómputo y referencias a
rutas empleadas durante los experimentos. Se conservan por trazabilidad y no
forman parte de la interfaz pública del repositorio.
