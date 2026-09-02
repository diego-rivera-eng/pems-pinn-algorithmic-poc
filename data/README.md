# Datos

## Origen

Los archivos de `raw/` son copias byte a byte de los cinco CSV publicados por
UCI Machine Learning Repository como *Gas Turbine CO and NOx Emission Data
Set*, DOI [`10.24432/C5WC95`](https://doi.org/10.24432/C5WC95).

UCI declara 36.733 observaciones, once variables y cinco años de medición. La
licencia indicada por la fuente es [CC BY
4.0](https://creativecommons.org/licenses/by/4.0/). Al redistribuir o reutilizar
los datos se debe mantener una atribución adecuada a la fuente y a sus autores.

## Esquema

Cada CSV contiene las columnas:

```text
AT, AP, AH, AFDP, GTEP, TIT, TAT, TEY, CDP, CO, NOX
```

Las primeras nueve son variables de operación/ambiente y `CO`, `NOX` son los
objetivos. Las unidades y definiciones autorizadas deben consultarse en la
ficha UCI; este repositorio no redefine el diccionario de datos original.

| Archivo | Año | Filas | Bytes | SHA-256 |
|---|---:|---:|---:|---|
| `gt_2011.csv` | 2011 | 7.411 | 562.921 | `d87ceef9aa59533cc7d924d10de241b1b06ecd11f9b26bab59191ea0f8a76b9a` |
| `gt_2012.csv` | 2012 | 7.628 | 577.617 | `be54b9d0e1a7de40c55d32fa489e75de892b000c066b5a09f09a19124ee29100` |
| `gt_2013.csv` | 2013 | 7.152 | 540.334 | `13c437bb440ec2045bd12057e6654c41dd4107a661eac16ba2e878e897a08f9e` |
| `gt_2014.csv` | 2014 | 7.158 | 541.009 | `c2a03c92c9c3207aad0c6be7de8d9b5b4bfa4720ad0efb2c1f21b6cec4d3f3fa` |
| `gt_2015.csv` | 2015 | 7.384 | 556.928 | `9b08f35fde0d4b138232a605db4093c2b8bf9d6757e6f1fbd9534ad616c13591` |

Las cifras de filas excluyen la cabecera. `MANIFEST.sha256` permite verificar
la integridad sin abrir los datos.

## Uso dentro del estudio

- Protocolo interpolativo: combinación de los cinco años, bloqueo operativo,
  29.845 filas DEV y 6.888 filas TEST.
- Protocolo *walk-forward*: ventanas expansivas WF01–WF04; 2015 es el TEST
  externo final de 7.384 filas.

No se aplica una licencia nueva a estos CSV. El aviso temporal del archivo
`LICENSE` cubre solo material original del repositorio.

