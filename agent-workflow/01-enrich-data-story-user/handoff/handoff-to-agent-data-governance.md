# Handoff: Enrich Data Story User → Agent Data Governance

**Fecha**: 2026-06-22  
**Status**: draft  
**CRISP-DM**: Business Understanding  

## Contexto

El Agente 01 (Enrich Data Story User) ha convertido el requerimiento inicial de negocio en una historia de usuario enriquecida con KPIs, fuentes, granularidad y reglas de negocio.

El `planner-input.json` generado es **preliminar** y requiere validación de gobierno antes de ser consumido por Agent Planner.

## Trabajo Completado

- Historia de usuario enriquecida generada
- `planner-input.json` preliminar con contexto de negocio, fuentes identificadas y requerimientos DQ iniciales

## Input para el Siguiente Agente

- **Archivo**: `02-agent-data-governance/inputs/planner-input.json`
- **Estado**: draft

## Qué Debe Hacer Agent Data Governance

1. Leer `inputs/planner-input.json` (preliminar).
2. Revisar fuentes de datos identificadas y clasificarlas.
3. Identificar PII y datos sensibles.
4. Definir ownership (Data Owner, Steward, Custodio).
5. Evaluar riesgos regulatorios (LFPDPPP, CNBV).
6. Definir data contracts y controles de acceso.
7. Completar la sección `governance` del `planner-input.json`.
8. Producir `planner-input.json` gobernado en `outputs/`.
9. Copiar `planner-input.json` gobernado a `03-agent-planner/inputs/`.

## Preguntas Abiertas

_Ninguna en este momento._

## Recomendación

Iniciar con la revisión de fuentes de datos y clasificación antes de definir ownership.
