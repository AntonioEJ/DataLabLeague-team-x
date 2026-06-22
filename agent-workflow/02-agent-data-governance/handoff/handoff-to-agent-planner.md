# Handoff: Agent Data Governance → Agent Planner

**Fecha**: 2026-06-22  
**Status**: draft  
**CRISP-DM**: Business Understanding → Data Understanding  

## Contexto

Agent Data Governance ha revisado el `planner-input.json` preliminar y lo ha enriquecido con:

- Clasificación de datos (nivel de sensibilidad)
- Data Ownership (Owner, Steward, Custodio)
- Inventario de PII y datos sensibles con controles
- Requerimientos de data catalog y lineage
- Data contracts identificados
- Controles de acceso con mínimo privilegio
- Riesgos regulatorios evaluados

## Input para Agent Planner

- **Archivo**: `03-agent-planner/inputs/planner-input.json`
- **Estado**: draft (gobernado)
- **Campo clave**: `governance.governance_approved`

## Qué Debe Hacer Agent Planner

1. Leer `planner-input.json` gobernado completo, incluyendo la sección `governance`.
2. Diseñar arquitectura que **respete los controles de acceso** definidos.
3. Planificar implementación de controles PII en el pipeline de datos.
4. Incluir en el backlog las tareas de data catalog, lineage y data contracts.
5. Agregar quality gates de gobierno en `quality-gates.md`.
6. Considerar las `conditions_for_planner` del campo `governance`.

## Restricciones Importantes para el Planner

_[Pendiente — a completar con restricciones específicas de gobierno]_

## Preguntas Abiertas

_Ninguna en este momento._

## Recomendación

Iniciar la arquitectura considerando los controles de PII y acceso como requerimientos de primera clase, no como afterthought.
