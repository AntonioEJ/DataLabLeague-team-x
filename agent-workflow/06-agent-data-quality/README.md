# Agente 06: Agent Data Quality

## Rol

Valida las reglas de calidad de datos: completitud, unicidad, consistencia, exactitud, frescura, validez y unicidad. Genera cifras de control y reconciliación.

## Fase CRISP-DM

- Data Preparation
- Evaluation

## Inputs Esperados

| Archivo | Origen |
|---|---|
| `inputs/data-quality-input.json` | `05-agent-qa/outputs/data-quality-input.json` |

## Outputs Esperados

| Archivo | Descripción |
|---|---|
| `outputs/data-quality-report.json` | Reporte con 7 dimensiones DQ |
| `outputs/validation-results.md` | Resultados de validación |
| `outputs/control-totals.md` | Cifras de control |
| `outputs/reconciliation-report.md` | Reconciliación de datos |
| `outputs/documentation-input.json` | **Output principal** para Agent Documentation |

## Umbral

- DQ score global ≥98%

## Siguiente Agente

**07 — Agent Documentation**

## Definition of Done

- [ ] 7 dimensiones DQ evaluadas
- [ ] DQ score ≥98%
- [ ] Control totals documentados
- [ ] `handoff/handoff-to-agent-documentation.json` con `quality_gate.passed: true`
- [ ] `07-agent-documentation/inputs/documentation-input.json` existe
