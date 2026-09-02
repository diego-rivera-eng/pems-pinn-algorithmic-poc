# Informe técnico — protocolo walk-forward R1

## Resultado

El diseño quedó **FROZEN** con 29,349 filas de desarrollo,
tres folds de selección y un fold FINAL protegido:

- WF01: 2011 → 2012;
- WF02: 2011–2012 → 2013;
- WF03: 2011–2013 → 2014;
- WF04: 2011–2014 → 2015.

`gap_records = 0` y `temporal_weighting = uniform` son decisiones fijas. NOx
utiliza `TIT_INC`; CO utiliza `CDP_NEG`. `lambda_phys` permanece dentro del
espacio de optimización de cada consumidor.

## Protección de TEST

El protocolo no materializó variables ni objetivos de 2015, no calculó su hash
de contenido y no produjo métricas de TEST. El año solo puede abrirse en un
notebook WF FINAL después de recibir un handoff FROZEN del OPT correspondiente.

## Alcance

La evidencia es prospectiva anual dentro del dominio histórico 2011–2015. No
constituye certificación regulatoria, RATA, homologación PEMS/CEMS ni prueba de
causalidad física.
