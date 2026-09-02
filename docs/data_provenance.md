# Procedencia y gobernanza de datos

## Fuente primaria

UCI Machine Learning Repository publica el conjunto [*Gas Turbine CO and NOx
Emission Data Set*](https://archive.ics.uci.edu/dataset/551/gas+turbine+co+and+nox+emission+data+set),
donado en 2019, con DOI [`10.24432/C5WC95`](https://doi.org/10.24432/C5WC95).
La ficha declara 36.733 instancias horarias, sin valores faltantes, recopiladas
entre 2011 y 2015 en una turbina del noroeste de Turquía.

Cita recomendada por UCI:

> *Gas Turbine CO and NOx Emission Data Set* [Dataset]. (2019). UCI Machine
> Learning Repository. https://doi.org/10.24432/C5WC95.

## Licencia y redistribución

La ficha UCI declara CC BY 4.0. Los cinco CSV de `data/raw/` se mantienen byte a
byte y su integridad se verifica con `data/raw/MANIFEST.sha256`.

El repositorio no añade restricciones a los datos ni afirma propiedad sobre
ellos. El aviso de `LICENSE` se aplica únicamente al material original del
repositorio.

## Transformaciones

Los archivos raw no se limpian ni reordenan. Las particiones se derivan de
manifiestos de protocolo que conservan identificadores globales, año y fila
dentro del año. Las tablas de asignación y hashes están bajo
`results/frozen/protocol/` y los contratos bajo `configs/protocols/`.

## Límites de transferencia

El conjunto representa una turbina en Turquía y un rango operacional del caso
de estudio; no es evidencia directa para activos colombianos ni para arranque,
parada, baja carga o transitorios no cubiertos. El uso industrial requiere
caracterización local, control de calidad de sensores y validación independiente
frente a medición de referencia.
