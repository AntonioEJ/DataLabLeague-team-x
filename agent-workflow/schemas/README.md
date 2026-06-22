# Schemas — DataLab League Agent Workflow

## Propósito

Contiene los JSON Schemas (draft-07) para validar los artefactos de la cadena de agentes.

## Archivos

| Schema | Valida | Usado por |
|---|---|---|
| `agent-input.schema.json` | Artefactos de input genéricos | Todos los agentes |
| `agent-output.schema.json` | Artefactos de output genéricos | Todos los agentes |
| `handoff.schema.json` | Artefactos de handoff | Todos los agentes |
| `planner-input.schema.json` | `planner-input.json` (preliminar y gobernado) | Agentes 01, 02, 03 |

## Validación

Para validar un artefacto contra su schema:

```bash
# Con ajv-cli
npx ajv validate -s schemas/planner-input.schema.json -d 02-agent-data-governance/outputs/planner-input.json

# Con jsonschema (Python)
python -c "
import json, jsonschema
schema = json.load(open('schemas/planner-input.schema.json'))
data = json.load(open('02-agent-data-governance/outputs/planner-input.json'))
jsonschema.validate(data, schema)
print('Valid')
"
```

## Notas

- `planner-input.schema.json` incluye la sección `governance` que es completada por Agente 02.
- El campo `governance.governance_approved` es **requerido** y debe ser `true` antes de que Agente 03 consuma el artefacto.
