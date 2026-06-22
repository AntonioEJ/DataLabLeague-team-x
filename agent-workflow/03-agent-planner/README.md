# Agente 03: Agent Planner

## Rol

Genera el **plan técnico-funcional** del producto de datos: épicas, features, tareas, arquitectura, backlog, quality gates y plan de sprints.

**Solo debe iniciar si recibió el `planner-input.json` gobernado de Agent Data Governance.**

## Fase CRISP-DM

- Data Understanding
- Data Preparation

## Inputs Esperados

| Archivo | Origen |
|---|---|
| `inputs/planner-input.json` | `02-agent-data-governance/outputs/planner-input.json` (gobernado) |

## Outputs Esperados

| Archivo | Descripción |
|---|---|
| `outputs/product-plan.json` | Plan completo del producto |
| `outputs/sprint-plan.json` | Plan de sprints y entregas |
| `outputs/backlog.json` | Backlog de épicas, features y tareas |
| `outputs/architecture-plan.md` | Arquitectura técnica seleccionada |
| `outputs/task-breakdown.md` | Desglose de tareas por agente |
| `outputs/risk-plan.md` | Plan de gestión de riesgos |
| `outputs/quality-gates.md` | Quality gates para todos los agentes |
| `outputs/coder-input.json` | **Output principal** para Agent Coder |

## Siguiente Agente

**04 — Agent Coder**

## Definition of Done

- [ ] Arquitectura documentada (Medallion o SAS según ADR)
- [ ] `outputs/coder-input.json` con spec técnica completa
- [ ] Quality gates definidos para todos los agentes
- [ ] `handoff/handoff-to-agent-coder.json` con `quality_gate.passed: true`
- [ ] `04-agent-coder/inputs/coder-input.json` existe
