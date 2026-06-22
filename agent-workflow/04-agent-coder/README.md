# Agente 04: Agent Coder

## Rol

Implementa o prepara los componentes técnicos del producto de datos según el plan técnico de Agent Planner. Documenta los archivos modificados y genera el input para Agent QA.

## Fase CRISP-DM

- Data Preparation
- Modeling / Business Logic

## Inputs Esperados

| Archivo | Origen |
|---|---|
| `inputs/coder-input.json` | `03-agent-planner/outputs/coder-input.json` |

## Outputs Esperados

| Archivo | Descripción |
|---|---|
| `outputs/implementation-summary.md` | Resumen de implementación |
| `outputs/changed-files.md` | Lista de archivos creados/modificados |
| `outputs/code-components.json` | Mapa de componentes implementados |
| `outputs/qa-input.json` | **Output principal** para Agent QA |

## Estándares de Código

- PEP 8, Python 3.11+
- Type annotations requeridas
- Docstrings Google Style
- Logging con `logging` module (sin `print()`)
- Sin hardcoding de credenciales o paths
- Error handling específico (sin `except Exception: pass`)

## Siguiente Agente

**05 — Agent QA**

## Definition of Done

- [ ] Código sigue estándares del repo
- [ ] Sin credenciales hardcodeadas
- [ ] `outputs/qa-input.json` con mapa de componentes
- [ ] `handoff/handoff-to-agent-qa.json` con `quality_gate.passed: true`
- [ ] `05-agent-qa/inputs/qa-input.json` existe
