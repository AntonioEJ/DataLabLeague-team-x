# Agente 05: Agent QA

## Rol

Diseña y ejecuta pruebas técnicas, funcionales, de regresión y de integración del producto de datos.

## Fase CRISP-DM

- Modeling / Business Logic
- Evaluation

## Inputs Esperados

| Archivo | Origen |
|---|---|
| `inputs/qa-input.json` | `04-agent-coder/outputs/qa-input.json` |

## Outputs Esperados

| Archivo | Descripción |
|---|---|
| `outputs/test-plan.md` | Plan de pruebas |
| `outputs/test-results.json` | Resultados de ejecución |
| `outputs/defects.md` | Defectos por severidad (P0-P3) |
| `outputs/coverage-summary.md` | Cobertura de tests |
| `outputs/data-quality-input.json` | **Output principal** para Agent Data Quality |

## Criterios

- Cobertura ≥80%
- Sin defectos P0 abiertos antes del handoff
- Escenarios positivos y negativos ejecutados

## Siguiente Agente

**06 — Agent Data Quality**

## Definition of Done

- [ ] `outputs/test-results.json` generado
- [ ] Sin P0 abiertos
- [ ] `handoff/handoff-to-agent-data-quality.json` con `quality_gate.passed: true`
- [ ] `06-agent-data-quality/inputs/data-quality-input.json` existe
