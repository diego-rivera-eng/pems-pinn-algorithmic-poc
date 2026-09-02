# Alcance de la publicación

La versión 1.0.0 constituye la distribución pública de la evidencia
computacional asociada al Capítulo 10 y a los Apéndices A y B de Rivera (2026),
*Metodología Conceptual para la Implementación de Sistemas de Monitoreo Predictivo de Emisiones (PEMS) Basados en Redes Neuronales Informadas por la Física (PINNs) Aplicado a Fuentes Fijas de Combustión en el Sector Petróleo y Gas Colombiano*.

## Elementos incluidos

- 24 notebooks ejecutados con resultados visibles y espejo versionado.
- Cinco archivos de datos originales con atribución y SHA-256.
- Configuraciones, resultados, figuras y auditorías congeladas de las campañas
  canónicas.
- 46 pesos de modelo distribuidos y un catálogo completo de 104 artefactos de
  modelo o metadatos.
- Manifiestos de inventario, migración, evidencia académica, portabilidad e
  integridad.
- Bibliografía del trabajo de maestría y de las once fuentes documentales
  asociadas.

## Elementos no distribuidos

- El documento académico completo.
- Copias de seguridad, archivos temporales, checkpoints, estados Optuna,
  monitores y ejecuciones fallidas.
- Duplicados exactos o versiones sustituidas por una campaña canónica.
- La Figura 16, por corresponder a una adaptación de literatura externa.
- Dieciocho binarios XGBoost–NOx de gran tamaño; sus metadatos, tamaño y
  SHA-256 permanecen en `manifests/model_catalog.csv`.

## Condiciones de uso

El material original del repositorio está sujeto al aviso de derechos de
`LICENSE`. Los datos UCI conservan la licencia CC BY 4.0. Los modelos son una
prueba de concepto académica y no sustituyen un sistema certificado de
monitoreo de emisiones.

## Verificación

`python scripts/verify_release.py` comprueba datos, notebooks, migración,
modelos, checksums, rutas personales, patrones de credenciales y metadatos de
publicación sin cargar modelos ni reentrenar.
