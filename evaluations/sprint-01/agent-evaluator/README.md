# Agent Evaluator — Sprint 01

Esta carpeta contiene el agente evaluador para Sprint 1 de DataLab League.

## Archivos

| Archivo | Descripción |
|---------|---|
| `sprint-01-evaluator.agent.md` | Definición del agente evaluador |
| `evaluator-prompt.md` | Prompt listo para evaluar a cada equipo |
| `evaluation-input-template.json` | Template de input para el agente |
| `evaluation-output-template.json` | Template de output del agente |

## Cómo Usar

1. Abrir GitHub Copilot Chat en modo agente.
2. Seleccionar `sprint-01-evaluator` desde `.github/agents/99_sprint-01-evaluator.agent.md`.
3. Copiar el prompt de `evaluator-prompt.md`.
4. Proporcionar el `evaluation-input-template.json` con los datos del equipo.
5. El agente generará los archivos de resultado en `teams/team-XX/`.
