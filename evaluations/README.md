# Evaluations

Esta carpeta contiene la infraestructura formal de evaluación para la competencia **DataLab League**.

## ¿Qué es esta carpeta?

`/evaluations/` administra las evaluaciones por sprint de los equipos participantes en DataLab League. Cada sprint tiene su propia subcarpeta con rúbricas, evidencias, resultados y herramientas de evaluación.

## Organización por Sprint

```
evaluations/
├── README.md                    ← Este archivo
└── sprint-01/                   ← Evaluación Sprint 1
    ├── README.md
    ├── evaluation-guide.md
    ├── scoring-summary.md
    ├── sprint-01-scoreboard.md
    ├── rubrics/                 ← Rúbricas por entregable
    ├── teams/                   ← Resultados por equipo
    ├── agent-evaluator/         ← Agente evaluador del sprint
    └── templates/               ← Templates reutilizables
```

Cada sprint nuevo debe crear una carpeta `sprint-XX/` siguiendo la misma estructura.

## Evidencia a Revisar

Para cada sprint se revisa:

- Los entregables definidos por el sprint (README, instrucciones Copilot, código, pipelines, etc.)
- Evidencia verificable en GitHub: commits, PRs, archivos versionados, tests ejecutados
- Calidad de datos, gobernanza y documentación
- Consistencia con los criterios de la cadena de agentes de DataLab League

## Registro de Resultados

Los resultados se registran en:

- `teams/team-XX/evaluation-result.json` — Resultado estructurado
- `teams/team-XX/evaluation-result.md` — Resultado legible
- `teams/team-XX/feedback.md` — Retroalimentación accionable
- `scoring-summary.md` — Resumen comparativo de todos los equipos
- `sprint-XX-scoreboard.md` — Ranking y badges

## Relación con DataLab League

DataLab League es una competencia de ingeniería de datos con evaluación por sprints. Cada sprint evalúa entregables específicos alineados con CRISP-DM y buenas prácticas de ingeniería de datos. Los equipos son evaluados con criterios consistentes, objetivos y trazables.

## Relación con GitHub Copilot Business

Los entregables evaluados incluyen el uso efectivo de GitHub Copilot: instrucciones, agentes, skills y prompts. Se evalúa si el equipo configuró Copilot de forma que ayude a producir datos de calidad, con gobernanza, documentación y evidencia.

## Trazabilidad en GitHub

Toda evaluación debe ser:

- **Versionada**: el resultado queda en un commit de la rama `chore/evaluate-sprint-XX-team-YY`
- **Revisable**: los archivos de resultado son legibles y estructurados (JSON + Markdown)
- **Auditable**: cada puntaje tiene justificación en `feedback.md`
- **Accionable**: el feedback incluye pasos concretos de mejora

## Sprints

| Sprint | Carpeta | Estado | Total puntos |
|--------|---------|--------|-------------|
| Sprint 01 | `sprint-01/` | activo | 60 |
