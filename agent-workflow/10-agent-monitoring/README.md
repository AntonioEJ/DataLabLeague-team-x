# Agente 10: Agent Monitoring

## Rol

Define el monitoreo, observabilidad, alertas, métricas operativas y mejora continua del producto de datos. Cierra el ciclo CRISP-DM con `final-product-evidence.json`.

## Fase CRISP-DM

- Monitoring & Continuous Improvement

## Inputs Esperados

| Archivo | Origen |
|---|---|
| `inputs/monitoring-input.json` | `09-agent-deployment/outputs/monitoring-input.json` |

## Outputs Esperados

| Archivo | Descripción |
|---|---|
| `outputs/monitoring-plan.md` | Plan de monitoreo y observabilidad |
| `outputs/observability-metrics.md` | KPIs operativos y SLAs |
| `outputs/alerts.md` | Configuración de alertas P1/P2 |
| `outputs/continuous-improvement-backlog.md` | Backlog de mejora continua |
| `outputs/final-product-evidence.json` | **Cierre del ciclo CRISP-DM** |

## KPIs Operativos Mínimos

- Disponibilidad ≥99.5%
- DQ score operativo ≥98%
- Latencia de datos <15 min
- Hora de publicación ≤08:00 CDMX (si aplica)

## Siguiente Agente

**Fin del ciclo.** Si hay mejoras, reiniciar en Agente 01.

## Definition of Done

- [ ] KPIs operativos definidos con umbral y alerta
- [ ] Alertas P1/P2 configuradas
- [ ] `final-product-evidence.json` en estado `approved`
- [ ] Backlog de mejora continua tiene ≥1 ítem
- [ ] `final-handoff.json` con `quality_gate.passed: true`
