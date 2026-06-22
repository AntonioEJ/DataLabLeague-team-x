# Evaluator Prompt — Sprint 01

Prompt listo para usar con el agente `sprint-01-evaluator` en GitHub Copilot Chat.

---

## Prompt de Evaluación

Copia y adapta este prompt para evaluar cada equipo:

```
Actúa como Sprint 01 Evaluator Agent de DataLab League.

Evalúa el equipo indicado usando las rúbricas de:
- /evaluations/sprint-01/rubrics/githubcopilot-instructions-rubric.md
- /evaluations/sprint-01/rubrics/readme-rubric.md
- /evaluations/sprint-01/rubrics/sprint-01-total-rubric.md

Equipo a evaluar: [TEAM-ID] — [NOMBRE DEL EQUIPO]

Los archivos del equipo están disponibles localmente en este repositorio:
- README.md: `evaluations/sprint-01/submissions/[team-id]/README.md`
- Copilot Instructions: `evaluations/sprint-01/submissions/[team-id]/copilot-instructions.md`

Debes revisar:
- README.md del equipo en la ruta local indicada.
- copilot-instructions.md del equipo en la ruta local indicada.
- Evidencia disponible en este repositorio.
- Relación con DataLab League y CRISP-DM.
- Claridad, calidad, gobernanza, trazabilidad y accionabilidad.

El puntaje máximo es:
- GitHub Copilot Instructions: 40 puntos.
- README general: 20 puntos.
- Total: 60 puntos.

No modifiques los archivos evaluados.

Genera:
- /evaluations/sprint-01/teams/[team-id]/evaluation-result.md
- /evaluations/sprint-01/teams/[team-id]/evaluation-result.json
- /evaluations/sprint-01/teams/[team-id]/feedback.md

Actualiza:
- /evaluations/sprint-01/scoring-summary.md
- /evaluations/sprint-01/sprint-01-scoreboard.md (cuando los 3 equipos estén evaluados)

Si falta evidencia, registra el faltante y asigna puntaje conforme a la rúbrica.

Cada evaluación debe incluir:
- puntaje por criterio con % aplicado
- justificación explícita basada en el contenido evaluado
- fortalezas observadas
- oportunidades de mejora priorizadas
- riesgos identificados
- acciones recomendadas concretas
- comentario final profesional y constructivo
```

---

## Cómo Usar Este Prompt

1. Abre GitHub Copilot Chat.
2. Selecciona el agente `sprint-01-evaluator`.
3. Reemplaza `[TEAM-ID]`, `[NOMBRE DEL EQUIPO]`, `[URL DEL REPOSITORIO]` y `[BRANCH A EVALUAR]`.
4. Pega el prompt y ejecuta.
5. Revisa los archivos generados en `teams/team-XX/`.
6. Haz commit de los resultados.

---

## Ejemplo para Team 01

```
Actúa como Sprint 01 Evaluator Agent de DataLab League.

Evalúa el equipo indicado usando las rúbricas de:
- /evaluations/sprint-01/rubrics/githubcopilot-instructions-rubric.md
- /evaluations/sprint-01/rubrics/readme-rubric.md
- /evaluations/sprint-01/rubrics/sprint-01-total-rubric.md

Equipo a evaluar: team-01 — Team 01

Los archivos del equipo están disponibles localmente:
- README.md: evaluations/sprint-01/submissions/team-01/README.md
- Copilot Instructions: evaluations/sprint-01/submissions/team-01/copilot-instructions.md

[... instrucciones completas del prompt arriba ...]
```
