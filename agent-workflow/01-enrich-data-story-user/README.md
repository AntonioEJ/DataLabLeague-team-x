# Agente 01: Enrich Data Story User

## Rol

Convierte el requerimiento inicial de negocio en una **historia de usuario de datos enriquecida** y una especificación funcional inicial del producto de datos.

Este es el **punto de entrada** de toda la cadena. Su output principal (`planner-input.json`) es entregado a **Agent Data Governance** para validación antes de llegar a Agent Planner.

## Fase CRISP-DM

- Business Understanding
- Data Understanding

## Inputs Esperados

| Archivo | Descripción |
|---|---|
| `inputs/initial-requirement.md` | Requerimiento inicial en texto libre |
| `inputs/source-documents.md` | Documentos fuente opcionales (PDF, specs, etc.) |

## Outputs Esperados

| Archivo | Descripción |
|---|---|
| `outputs/enriched-user-story.json` | Historia de usuario enriquecida |
| `outputs/crisp-dm-requirements.json` | Requerimientos mapeados a fases CRISP-DM |
| `outputs/data-product-specification.json` | Especificación funcional del producto |
| `outputs/data-quality-rules.json` | Reglas DQ iniciales identificadas |
| `outputs/governance-security-requirements.json` | Requerimientos de gobierno y seguridad identificados |
| `outputs/acceptance-criteria.json` | Criterios de aceptación del producto |
| `outputs/planner-input.json` | **Output principal** — input preliminar para Agent Data Governance |

## Criterios de Calidad

- [ ] KPIs de negocio definidos con fórmula y umbral
- [ ] Fuentes de datos identificadas con nombre y sistema origen
- [ ] Granularidad del producto definida (fila = ¿qué entidad?)
- [ ] Reglas de negocio documentadas
- [ ] Stakeholders identificados
- [ ] Restricciones y dependencias documentadas

## Evidencia Requerida

- Commit con `planner-input.json` en `outputs/`
- `planner-input.json` copiado a `02-agent-data-governance/inputs/`

## Siguiente Agente

**02 — Agent Data Governance**

El `planner-input.json` generado aquí es **preliminar**. Agent Data Governance lo valida y enriquece antes de pasarlo a Agent Planner.

## Definition of Done

- [ ] `outputs/planner-input.json` existe con `status: "draft"` o superior
- [ ] `outputs/planner-input.json` tiene campos: `business_context`, `objective`, `scope`, `data_sources`, `kpis`, `business_rules`
- [ ] `handoff/handoff-to-agent-data-governance.json` tiene `quality_gate.passed: true`
- [ ] `02-agent-data-governance/inputs/planner-input.json` existe
- [ ] Evidencia registrada en `evidence/`
