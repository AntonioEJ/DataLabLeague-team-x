---
name: data-story-user-enrichment
description: Enriquece historias de usuario de datos conectando necesidad de negocio, KPI, decisión, fuentes, granularidad, reglas DQ, criterios de aceptación y evidencia. Úsalo cuando una historia de datos sea ambigua o necesite pasar de negocio a implementación.
argument-hint: "[nombre del caso de uso] [KPI objetivo]"
---

# Data Story User Enrichment Skill

## Propósito

Convertir una necesidad de negocio en una historia de usuario de datos enriquecida, lista para diseño, implementación, pruebas, Data Quality y documentación.

## Cuándo usar este skill

Usa este skill cuando:

- El caso de uso aún está ambiguo.
- Falta conectar la historia con un KPI.
- Falta granularidad de datos.
- Faltan criterios de aceptación.
- Faltan reglas DQ.
- Faltan fuentes de datos.
- Se necesita preparar un backlog de producto de datos.

## Inputs

- Nombre del squad.
- Sponsor.
- Usuario de negocio.
- Problema.
- KPI objetivo.
- Meta de tablero.
- Fuentes disponibles.
- Frecuencia.
- Restricciones.
- Riesgos.

## Procedimiento

1. Identifica el usuario de negocio.
2. Redacta la historia base:
   `Como [rol], quiero [capacidad], para [decisión o KPI].`
3. Conecta la historia con un KPI medible.
4. Define la decisión que habilita.
5. Identifica fuentes de datos.
6. Define granularidad.
7. Lista métricas y dimensiones.
8. Propón reglas DQ.
9. Define cifras control.
10. Escribe criterios de aceptación.
11. Marca supuestos y preguntas abiertas.
12. Actualiza evidencia.

## Output esperado

Genera o actualiza:

- `docs/user-stories/data-user-stories.md`
- `docs/user-stories/data-story-map.md`
- `docs/user-stories/kpi-decision-map.md`
- `docs/user-stories/acceptance-criteria.md`
- `evidence/data-story.md`

## Plantilla de salida

```md
# Historia de usuario de datos

## Historia

Como [rol],
quiero [capacidad de datos],
para [decisión o KPI].

## KPI vinculado

TODO

## Decisión que habilita

TODO

## Fuentes de datos

TODO

## Granularidad

TODO

## Métricas

TODO

## Dimensiones

TODO

## Reglas DQ sugeridas

TODO

## Cifras control

TODO

## Criterios de aceptación

Given TODO
When TODO
Then TODO

## Supuestos

TODO

## Preguntas abiertas

TODO

## Evidencia

TODO
```
