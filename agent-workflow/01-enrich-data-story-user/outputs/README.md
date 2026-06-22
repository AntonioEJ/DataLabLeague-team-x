# Outputs — Agente 01: Enrich Data Story User

## Qué se Guarda Aquí

Artefactos generados por Agente 01. El output principal es `planner-input.json`.

## Archivos

| Archivo | Descripción | Tipo |
|---|---|---|
| `enriched-user-story.json` | Historia de usuario enriquecida | JSON |
| `crisp-dm-requirements.json` | Requerimientos por fase CRISP-DM | JSON |
| `data-product-specification.json` | Especificación funcional del producto | JSON |
| `data-quality-rules.json` | Reglas DQ identificadas en el requerimiento | JSON |
| `governance-security-requirements.json` | Requerimientos de gobierno y seguridad | JSON |
| `acceptance-criteria.json` | Criterios de aceptación | JSON |
| `planner-input.json` | **Input principal para Agent Data Governance** | JSON |

## Reglas

- `planner-input.json` es el artefacto que avanza a la cadena — debe copiarse a `02-agent-data-governance/inputs/`.
- No modificar estos archivos una vez en estado `approved`.
- Si hay corrección, incrementar versión.

## Relación con PR

- El PR debe incluir `planner-input.json` con `status: "draft"` mínimo.
