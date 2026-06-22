# Handoff — Agente 02: Agent Data Governance

## Archivos

| Archivo | Descripción |
|---|---|
| `handoff-to-agent-planner.md` | Resumen narrativo del handoff hacia Agent Planner |
| `handoff-to-agent-planner.json` | Artefacto JSON con quality gate |

## Regla Especial

El handoff de Agent Data Governance requiere **aprobaciones humanas**:
- Data Owner: firma que los datos pueden procesarse para el propósito declarado
- Data Governance Lead: valida clasificación, controles y riesgos

`quality_gate.passed: true` solo se puede marcar después de obtener estas aprobaciones.
