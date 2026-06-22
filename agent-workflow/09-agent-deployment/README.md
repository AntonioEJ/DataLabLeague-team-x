# Agente 09: Agent Deployment

## Rol

Define y documenta el despliegue del producto de datos: release notes, plan de despliegue, rollback y readiness productivo.

## Fase CRISP-DM

- Deployment

## Inputs Esperados

| Archivo | Origen |
|---|---|
| `inputs/deployment-input.json` | `08-agent-compliance-security/outputs/deployment-input.json` |

**Requiere `deployment_approved: true` en el input.**

## Outputs Esperados

| Archivo | Descripción |
|---|---|
| `outputs/deployment-plan.md` | Plan de despliegue |
| `outputs/release-notes.md` | Release notes del producto |
| `outputs/rollback-plan.md` | Plan de rollback |
| `outputs/monitoring-input.json` | **Output principal** para Agent Monitoring |

## Siguiente Agente

**10 — Agent Monitoring**

## Definition of Done

- [ ] Plan de despliegue documentado
- [ ] Release notes generadas
- [ ] Rollback plan disponible
- [ ] `handoff/handoff-to-agent-monitoring.json` con `quality_gate.passed: true`
- [ ] `10-agent-monitoring/inputs/monitoring-input.json` existe
