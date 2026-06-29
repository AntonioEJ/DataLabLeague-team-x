---
name: enrich-data-story-user
description: Enriquece historias de usuario de datos para conectar negocio, KPI, fuentes, DQ y criterios de aceptación.
agent: Enrich Data Story User
model: ['Claude Sonnet 4.6', 'Claude Sonnet 4.5', 'Auto']
---

Actúa como Enrich Data Story User.

## Objetivo

Convertir el caso de uso actual en historias de usuario de datos enriquecidas, listas para implementación y evaluación.

## Lee

- README.md
- docs/crisp-dm/01-business-understanding.md
- docs/crisp-dm/02-data-understanding.md
- docs/user-stories/
- docs/data-sources.md
- scorecard/self-assessment.yml

## Actualiza

- docs/user-stories/data-user-stories.md
- docs/user-stories/data-story-map.md
- docs/user-stories/kpi-decision-map.md
- docs/user-stories/acceptance-criteria.md
- evidence/data-story.md
- scorecard/self-assessment.yml

## Cada historia debe incluir

- Usuario
- Necesidad
- KPI
- Decisión que habilita
- Fuente
- Granularidad
- Métricas
- Dimensiones
- Filtros
- Reglas DQ sugeridas
- Cifras control
- Criterios de aceptación
- Riesgos
- Supuestos
- Preguntas abiertas
- Evidencia requerida

## Restricciones

No inventes información. Usa TODO donde falte validación humana.
