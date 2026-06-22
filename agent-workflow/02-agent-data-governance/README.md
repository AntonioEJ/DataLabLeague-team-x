# Agente 02: Agent Data Governance

## Rol

Agent Data Governance es el **guardián de la gobernanza del dato** en la cadena de agentes.

Su propósito es **revisar, validar y enriquecer** el `planner-input.json` preliminar generado por Agente 01, incorporando todos los requerimientos de gobierno de datos antes de que Agent Planner diseñe la arquitectura técnica.

**Sin aprobación de Agent Data Governance, Agent Planner no puede iniciar.**

## Fase CRISP-DM

- Business Understanding
- Data Understanding

## ¿Por Qué Existe Este Agente?

Los productos de datos que llegan a producción sin revisión de gobierno generan:

- Exposición de PII sin controles
- Violaciones a LFPDPPP y CNBV
- Falta de ownership claro → nadie puede autorizar acceso
- Ausencia de lineage → imposible auditar el dato
- Data contracts inexistentes → integraciones frágiles

Agent Data Governance elimina estos riesgos antes de que se diseñe la arquitectura.

## Inputs Esperados

| Archivo | Descripción |
|---|---|
| `inputs/planner-input.json` | `planner-input.json` preliminar de Agente 01 |

## Outputs Esperados

| Archivo | Descripción |
|---|---|
| `outputs/governance-assessment.md` | Evaluación general de gobierno del producto |
| `outputs/data-classification.md` | Clasificación de datos (público/interno/confidencial/restringido) |
| `outputs/data-ownership.md` | Data Owner, Steward y Custodio asignados |
| `outputs/pii-sensitive-data-review.md` | Identificación y controles de PII y datos sensibles |
| `outputs/data-catalog-requirements.md` | Requerimientos para catálogo de datos |
| `outputs/lineage-requirements.md` | Requerimientos de trazabilidad y linaje |
| `outputs/data-contracts-requirements.md` | Requerimientos de contratos de datos |
| `outputs/access-control-requirements.md` | Controles de acceso y mínimo privilegio |
| `outputs/governance-risks.md` | Riesgos regulatorios y de gobierno identificados |
| `outputs/governance-decision-log.md` | Decisiones de gobierno tomadas |
| `outputs/planner-input.json` | **Output principal** — `planner-input.json` gobernado para Agent Planner |

## Criterios de Calidad

- [ ] Todos los datos clasificados con nivel de sensibilidad
- [ ] Data Owner, Steward y Custodio asignados con nombre y rol
- [ ] PII/datos sensibles identificados y controles definidos
- [ ] Data contracts identificados (existentes o a crear)
- [ ] Controles de acceso con principio de mínimo privilegio documentados
- [ ] Riesgos regulatorios evaluados
- [ ] `planner-input.json` gobernado tiene `governance.governance_approved: true`

## Evidencia Requerida

- Commit con `outputs/planner-input.json` gobernado
- Commit con archivos de governance outputs
- `03-agent-planner/inputs/planner-input.json` debe ser el archivo gobernado

## Siguiente Agente

**03 — Agent Planner**

## Definition of Done

- [ ] `outputs/planner-input.json` tiene `governance.governance_approved: true`
- [ ] `outputs/data-classification.md` completo
- [ ] `outputs/data-ownership.md` con Owner, Steward y Custodio definidos
- [ ] `outputs/pii-sensitive-data-review.md` completo
- [ ] `handoff/handoff-to-agent-planner.json` tiene `quality_gate.passed: true`
- [ ] `03-agent-planner/inputs/planner-input.json` es copia del gobernado
- [ ] Evidencia registrada en `evidence/`
