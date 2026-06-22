# Naming Conventions — DataLab League Agent Workflow

## Carpetas de Agentes

| Patrón | Ejemplo |
|---|---|
| `XX-agent-name` (XX = número 2 dígitos) | `01-enrich-data-story-user` |

Números reservados:
- `01` — Enrich Data Story User
- `02` — Agent Data Governance
- `03` — Agent Planner
- `04` — Agent Coder
- `05` — Agent QA
- `06` — Agent Data Quality
- `07` — Agent Documentation
- `08` — Agent Compliance Security
- `09` — Agent Deployment
- `10` — Agent Monitoring

## Subcarpetas Estándar

Cada agente tiene exactamente estas 4 subcarpetas:

```
inputs/
outputs/
handoff/
evidence/
```

## Nombres de Archivos de Input

| Archivo | Origen |
|---|---|
| `initial-requirement.md` | Documento inicial del negocio |
| `planner-input.json` | Output de Agentes 01 o 02 |
| `coder-input.json` | Output de Agente 03 |
| `qa-input.json` | Output de Agente 04 |
| `data-quality-input.json` | Output de Agente 05 |
| `documentation-input.json` | Output de Agente 06 |
| `compliance-input.json` | Output de Agente 07 |
| `deployment-input.json` | Output de Agente 08 |
| `monitoring-input.json` | Output de Agente 09 |

## Nombres de Archivos de Handoff

| Patrón | Ejemplo |
|---|---|
| `handoff-to-agent-{name}.md` | `handoff-to-agent-planner.md` |
| `handoff-to-agent-{name}.json` | `handoff-to-agent-planner.json` |
| `final-handoff.md` | Solo para Agente 10 |
| `final-handoff.json` | Solo para Agente 10 |

## Nombres de Artefactos JSON

Todos los artefactos JSON siguen el patrón:
- `kebab-case.json`
- Sin espacios, sin caracteres especiales
- Inglés

Ejemplos: `planner-input.json`, `governance-assessment.json`, `final-product-evidence.json`

## Versionamiento de Artefactos

Campo `version` en formato `"MAJOR.MINOR"`:

| Cambio | Regla |
|---|---|
| Corrección menor | MINOR +1 (1.0 → 1.1) |
| Cambio funcional | MAJOR +1 (1.1 → 2.0) |
| Rechazo y rehacer | MAJOR +1 |

## Estados Permitidos

Los artefactos JSON usan el campo `status`:

| Estado | Descripción |
|---|---|
| `draft` | En construcción, no listo para revisión |
| `in_review` | Listo para revisión, esperando aprobación |
| `approved` | Aprobado, puede ser input del siguiente agente |
| `rejected` | Rechazado, requiere correcciones |
| `ready_for_next_agent` | Aprobado y copiado a inputs del siguiente |
| `archived` | Versión anterior, reemplazada por versión nueva |

## Fechas

Todas las fechas en formato ISO 8601:

```
YYYY-MM-DD
```

Ejemplo: `2026-06-22`

## Convención para Artefactos JSON

Todo JSON de agente debe incluir estos campos en `metadata`:

```json
{
  "metadata": {
    "artifact_type": "agent_input | agent_output | agent_handoff",
    "agent_name": "nombre-del-agente",
    "version": "1.0",
    "status": "draft",
    "created_at": "YYYY-MM-DD",
    "updated_at": "YYYY-MM-DD"
  }
}
```

## Convención para Artefactos Markdown

Los archivos Markdown de outputs y handoffs deben tener encabezado:

```markdown
# [Título del Artefacto]

**Agente**: XX - Nombre del Agente
**Fecha**: YYYY-MM-DD
**Versión**: 1.0
**Estado**: draft | in_review | approved
**CRISP-DM**: [fase]
```

## IDs de Artefactos Transversales

| Tipo | Patrón |
|---|---|
| Preguntas abiertas | `OQ-001`, `OQ-002` |
| Decisiones | `DEC-001`, `DEC-002` |
| Riesgos | `RSK-001`, `RSK-002` |
| Evidencias | `EVD-001`, `EVD-002` |
