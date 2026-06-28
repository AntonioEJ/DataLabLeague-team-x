# Evidencia — Agente 02: Agent Data Governance ⚠️

## Propósito

Esta carpeta contiene la evidencia **CRÍTICA** del checkpoint de governance, incluyendo aprobaciones, clasificación de datos, y decisiones regulatorias.

## ⚠️ CHECKPOINT OBLIGATORIO

Este agente es el **guardián de la gobernanza**. Sin esta evidencia completa, el workflow NO puede avanzar a Agent 03 Planner.

## Qué se Guarda Aquí

Referencias a evidencia en GitHub relacionada con la revisión de gobierno:

- **Governance approvals**: Aprobaciones de Data Owner y Governance Lead
- **Data classification**: Decisiones de clasificación de datos
- **PII inventory**: Inventario de PII identificado
- **Risk assessment**: Evaluación de riesgos regulatorios (LFPDPPP, CNBV)
- **Access control**: Matriz de controles de acceso
- **Data contracts**: Contratos de datos identificados
- **Regulatory compliance**: Evidencia de cumplimiento normativo
- **Handoffs**: Documento de handoff con aprobación formal

## Relación con Índice Global

La evidencia de este agente se registra en:
- **Registro operativo**: [`agent-workflow/evidence/evidence-index.md`](../../evidence/evidence-index.md) (EVD-002)
- **Output principal**: [`outputs/planner-input.json`](../outputs/planner-input.json) (gobernado) ← **ARTEFACTO CRÍTICO**
- **Handoff**: [`handoff/handoff-to-agent-planner.json`](../handoff/handoff-to-agent-planner.json) (con `governance_approved: true`)

## Quality Gates Requeridos

- [ ] `governance.governance_approved: true` en `outputs/planner-input.json`
- [ ] Aprobación firmada de Data Owner
- [ ] Aprobación firmada de Governance Lead
- [ ] Todas las entidades y campos clasificados
- [ ] Campos PII inventariados con controles definidos
- [ ] Riesgos regulatorios evaluados y mitigados
- [ ] Data contracts identificados
- [ ] `planner-input.json` gobernado copiado a `03-agent-planner/inputs/`

## Commits Esperados

Evidencia esperada en Git:
- [ ] Commit con `outputs/governance-assessment.md`
- [ ] Commit con `outputs/data-classification.md`
- [ ] Commit con `outputs/planner-input.json` (gobernado)
- [ ] Commit con aprobaciones en evidencia
- [ ] Commit con `handoff/handoff-to-agent-planner.json`
- [ ] SHA commit registrado en `evidence-index.md` (EVD-002)

## Criterios de Evidencia Completa

- [ ] Clasificación de datos completa (público/interno/confidencial/restringido)
- [ ] Data Owner, Steward y Custodio asignados
- [ ] PII inventariado con plan de enmascaramiento/encriptación
- [ ] Riesgos regulatorios documentados y aceptados
- [ ] Data contracts definidos
- [ ] Aprobaciones formales obtenidas y documentadas
- [ ] `planner-input.json` gobernado validado contra schema
- [ ] Handoff formal a Agent 03 Planner completado
- [ ] Evidencia versionada en Git

## Formato de Registro

```markdown
## EVD-XXX: [Descripción]
- **Tipo**: commit | pr | issue | file | log
- **Referencia**: [hash, número de PR, URL]
- **Fecha**: YYYY-MM-DD
- **Descripción**: [Qué evidencia]
```

---

_Sin evidencia registrada aún._
