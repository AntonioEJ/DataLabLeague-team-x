# Handoff — Agente 01: Enrich Data Story User

## Qué se Guarda Aquí

El handoff formal de Agente 01 hacia Agent Data Governance.

## Archivos

| Archivo | Descripción |
|---|---|
| `handoff-to-agent-data-governance.md` | Resumen narrativo del handoff |
| `handoff-to-agent-data-governance.json` | Artefacto JSON estructurado con quality gate |

## Reglas

- El JSON debe tener `quality_gate.passed: true` antes de que Agente 02 comience.
- El campo `blockers` debe estar vacío para hacer handoff.
- Toda pregunta abierta bloqueante debe resolverse antes de `quality_gate.passed: true`.
