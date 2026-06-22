# Agente 08: Agent Compliance / Security

## Rol

Revisa seguridad, privacidad, cumplimiento normativo, secretos, accesos y riesgos del producto de datos antes del despliegue.

## Fase CRISP-DM

- Evaluation
- Deployment

## Inputs Esperados

| Archivo | Origen |
|---|---|
| `inputs/compliance-input.json` | `07-agent-documentation/outputs/compliance-input.json` |

## Outputs Esperados

| Archivo | Descripción |
|---|---|
| `outputs/security-review.md` | Revisión OWASP Top 10 |
| `outputs/privacy-review.md` | Revisión LFPDPPP / CNBV |
| `outputs/compliance-checklist.md` | Checklist de cumplimiento |
| `outputs/risks-and-mitigations.md` | Riesgos y mitigaciones |
| `outputs/deployment-input.json` | **Output principal** — con `deployment_approved: true` |

## Aprobaciones Requeridas

- CISO (si hay hallazgos de seguridad críticos)
- Compliance Officer (para datos regulados)

## Siguiente Agente

**09 — Agent Deployment**

## Definition of Done

- [ ] OWASP checklist completo
- [ ] LFPDPPP revisado
- [ ] `deployment_approved: true` en `deployment-input.json`
- [ ] `handoff/handoff-to-agent-deployment.json` con `quality_gate.passed: true`
- [ ] `09-agent-deployment/inputs/deployment-input.json` existe
