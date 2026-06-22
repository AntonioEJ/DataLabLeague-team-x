# Sprint 01 — Evaluación DataLab League

## Objetivo del Sprint 1

Evaluar la capacidad de cada equipo para configurar un repositorio de datos enterprise con instrucciones efectivas para GitHub Copilot y un README general de calidad.

Sprint 1 marca el inicio de la competencia. Los entregables evaluados son la base que guiará el trabajo de los sprints siguientes.

## Entregables Evaluados

| # | Entregable | Puntos |
|---|---|---|
| 1 | `githubcopilot-instructions.md` (o equivalente) | 40 |
| 2 | `README.md` general del repositorio | 20 |
| **Total** | | **60** |

## Puntaje Total

**60 puntos máximos.**

| Rango | Estado |
|---|---|
| 54 – 60 | Sobresaliente |
| 45 – 53 | Sólido |
| 35 – 44 | En riesgo medio |
| < 35 | Crítico |

## Equipos Evaluados

| Equipo | Carpeta |
|---|---|
| Team 01 | `teams/team-01/` |
| Team 02 | `teams/team-02/` |
| Team 03 | `teams/team-03/` |

## Estructura de Carpetas

```
sprint-01/
├── README.md                        ← Este archivo
├── evaluation-guide.md              ← Guía para evaluadores
├── scoring-summary.md               ← Resumen comparativo de puntajes
├── sprint-01-scoreboard.md          ← Ranking y badges
├── rubrics/
│   ├── README.md
│   ├── githubcopilot-instructions-rubric.md   ← Rúbrica 40 pts
│   ├── readme-rubric.md                       ← Rúbrica 20 pts
│   └── sprint-01-total-rubric.md              ← Rúbrica total
├── teams/
│   ├── README.md
│   ├── team-01/
│   │   ├── README.md
│   │   ├── evidence-index.md
│   │   ├── evaluation-result.md
│   │   ├── evaluation-result.json
│   │   └── feedback.md
│   ├── team-02/
│   └── team-03/
├── agent-evaluator/
│   ├── README.md
│   ├── sprint-01-evaluator.agent.md
│   ├── evaluator-prompt.md
│   ├── evaluation-input-template.json
│   └── evaluation-output-template.json
└── templates/
    ├── README.md
    ├── team-evidence-template.md
    ├── evaluation-result-template.md
    ├── feedback-template.md
    └── scoring-template.json
```

## Reglas Generales de Evaluación

1. La evaluación es objetiva y basada en evidencia verificable en el repositorio.
2. Si un archivo no existe, se asigna 0 en los criterios correspondientes.
3. Cada puntaje debe tener justificación escrita.
4. El agente evaluador no modifica los entregables de los equipos.
5. Los resultados se registran en `teams/team-XX/` y se consolidan en `scoring-summary.md`.
6. El scoreboard se actualiza al finalizar todas las evaluaciones del sprint.

## Cómo Usar el Agente Evaluador

1. Abrir GitHub Copilot Chat en modo agente.
2. Seleccionar el agente `sprint-01-evaluator` (`.github/agents/99_sprint-01-evaluator.agent.md`).
3. Usar el prompt disponible en `agent-evaluator/evaluator-prompt.md`.
4. Proporcionar el `evaluation-input-template.json` completado con los datos del equipo.
5. El agente generará los archivos de resultado en `teams/team-XX/`.

## Cómo Registrar Evidencia y Resultados

1. El evaluador revisa los archivos del equipo y completa `teams/team-XX/evidence-index.md`.
2. Genera `evaluation-result.json` y `evaluation-result.md` con puntajes y justificaciones.
3. Genera `feedback.md` con hallazgos, fortalezas y acciones recomendadas.
4. Actualiza `scoring-summary.md` con los resultados consolidados.
5. Actualiza `sprint-01-scoreboard.md` con el ranking final.
6. Hace commit de todos los archivos de resultado.
