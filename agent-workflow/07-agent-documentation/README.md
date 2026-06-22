# Agente 07: Agent Documentation

## Rol

Genera la documentación funcional, técnica, diccionario de datos y linaje del producto de datos.

## Fase CRISP-DM

- Deployment

## Inputs Esperados

| Archivo | Origen |
|---|---|
| `inputs/documentation-input.json` | `06-agent-data-quality/outputs/documentation-input.json` |

## Outputs Esperados

| Archivo | Descripción |
|---|---|
| `outputs/functional-documentation.md` | Documentación funcional |
| `outputs/technical-documentation.md` | Documentación técnica |
| `outputs/data-dictionary.md` | Diccionario de datos |
| `outputs/lineage.md` | Linaje del dato |
| `outputs/compliance-input.json` | **Output principal** para Agent Compliance |

## Siguiente Agente

**08 — Agent Compliance / Security**

## Definition of Done

- [ ] Documentación funcional y técnica completa
- [ ] Diccionario de datos con todos los campos
- [ ] `handoff/handoff-to-agent-compliance-security.json` con `quality_gate.passed: true`
- [ ] `08-agent-compliance-security/inputs/compliance-input.json` existe
