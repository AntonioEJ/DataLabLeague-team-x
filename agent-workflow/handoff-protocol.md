# Handoff Protocol — DataLab League

## ¿Qué es un Handoff?

Un handoff es la **transferencia formal y documentada** del control de un agente al siguiente en la cadena. Consiste en:

1. Un archivo Markdown (`.md`) que resume el contexto para el agente receptor.
2. Un archivo JSON (`.json`) con estructura validable por schema, que incluye el quality gate.

---

## ¿Cuándo se Puede Entregar al Siguiente Agente?

Un agente puede hacer handoff **solo cuando**:

- [ ] Todos los outputs obligatorios están en estado `approved` o `ready_for_next_agent`.
- [ ] `quality_gate.passed: true` en el handoff JSON.
- [ ] No hay preguntas abiertas bloqueantes (`blockers` vacío o con mitigación).
- [ ] La evidencia en GitHub está registrada (commit, PR o issue).
- [ ] El input del siguiente agente existe en `XX-agent/inputs/`.

---

## Estructura Mínima del Handoff JSON

```json
{
  "metadata": {
    "artifact_type": "agent_handoff",
    "source_agent": "XX-agent-name",
    "target_agent": "YY-agent-name",
    "version": "1.0",
    "status": "ready_for_next_agent",
    "created_at": "YYYY-MM-DD",
    "requires_human_review": false
  },
  "handoff_summary": {
    "business_context": "...",
    "technical_context": "...",
    "crisp_dm_phase": "...",
    "completed_work": ["..."],
    "pending_work": [],
    "key_decisions": ["..."],
    "known_limitations": []
  },
  "artifacts": {
    "inputs_used": ["..."],
    "outputs_generated": ["..."],
    "evidence": [],
    "required_next_inputs": ["..."]
  },
  "quality_gate": {
    "passed": true,
    "checks": [
      { "name": "...", "result": "pass", "notes": "" }
    ],
    "issues": [],
    "required_approvals": []
  },
  "open_questions": [],
  "assumptions": [],
  "risks": [],
  "blockers": [],
  "recommendation_to_next_agent": "..."
}
```

---

## Checklist de Transferencia

Antes de marcar `quality_gate.passed: true`, verifica:

- [ ] Todos los outputs obligatorios del agente están creados.
- [ ] El input del siguiente agente (`XX-input.json`) existe en la carpeta `inputs/` del siguiente agente.
- [ ] Las preguntas abiertas bloqueantes están resueltas o mitigadas.
- [ ] Los supuestos están documentados en `handoff.json > assumptions`.
- [ ] Los riesgos identificados están en `00-shared/risk-register.md`.
- [ ] La evidencia (commit/PR) está registrada en `evidence/`.
- [ ] `00-shared/decisions.md` refleja las decisiones tomadas.

---

## Reglas para Preguntas Abiertas

- Toda pregunta abierta debe tener ID único: `OQ-001`, `OQ-002`, etc.
- Se registran en `00-shared/open-questions.md` Y en el campo `open_questions` del handoff JSON.
- Una pregunta bloqueante (`priority: high`, `blocks_next_agent: true`) impide el handoff.
- Una pregunta no bloqueante puede incluirse en el handoff con `blocks_next_agent: false`.

---

## Reglas para Supuestos

- Todo supuesto debe tener origen documentado (`source`).
- Si el supuesto resulta falso, se convierte en pregunta abierta bloqueante.
- Los supuestos se listan en `00-shared/assumptions.md`.

---

## Reglas para Riesgos

- Todo riesgo tiene: `id`, `description`, `probability` (high/medium/low), `impact`, `mitigation`, `owner`.
- Los riesgos se registran en `00-shared/risk-register.md`.
- Un riesgo con `probability: high` + `impact: high` requiere revisión humana antes del handoff.

---

## Registrar Evidencia en GitHub

Toda evidencia se registra en el campo `artifacts.evidence` del handoff JSON:

```json
{
  "type": "commit",
  "reference": "abc1234",
  "description": "Agrega planner-input.json gobernado"
}
```

Tipos válidos: `commit`, `pr`, `issue`, `file`, `screenshot`, `log`, `other`.

---

## Regla Especial: Agent Data Governance (Paso 02)

Agent Data Governance tiene un rol especial en la cadena:

1. **Recibe** `planner-input.json` preliminar de Agente 01.
2. **Valida y enriquece** el artefacto con campos de gobierno.
3. **Produce** `planner-input.json` gobernado en `02-agent-data-governance/outputs/`.
4. **Copia** el artefacto a `03-agent-planner/inputs/planner-input.json`.

**El `planner-input.json` gobernado es el input oficial del Agent Planner.** Agent Planner NO debe usar el `planner-input.json` preliminar del Agente 01 directamente.

Campos de gobierno que debe agregar Agente 02:

```json
"governance": {
  "reviewed_by": "Agent Data Governance",
  "review_date": "YYYY-MM-DD",
  "data_classification": "...",
  "data_ownership": { "owner": "...", "steward": "...", "custodian": "..." },
  "pii_fields": [],
  "sensitive_fields": [],
  "data_contracts": [],
  "access_control": {},
  "lineage": {},
  "regulatory_risks": [],
  "approved_by": [],
  "governance_approved": false
}
```

`governance_approved: true` es condición necesaria para que el handoff de Agente 02 tenga `quality_gate.passed: true`.

---

## Formato del Handoff Markdown (.md)

```markdown
# Handoff: [Agente Origen] → [Agente Destino]

**Fecha**: YYYY-MM-DD
**Status**: ready_for_next_agent
**CRISP-DM**: [fase]

## Contexto

[Qué hizo este agente y por qué]

## Trabajo Completado

- [item 1]
- [item 2]

## Input para el Siguiente Agente

- Archivo: `XX-agent/inputs/YY-input.json`
- Estado: ready

## Preguntas Abiertas

[Ninguna / lista]

## Recomendación

[Qué debe hacer el siguiente agente primero]
```
