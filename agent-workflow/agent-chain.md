# Agent Chain — Orden de Ejecución y Criterios

## Orden de Ejecución

```
01 → 02 → 03 → 04 → 05 → 06 → 07 → 08 → 09 → 10
```

Cada paso es **secuencial y obligatorio**. No se puede saltar un agente.

---

## Agente 01: Enrich Data Story User

**Fase CRISP-DM**: Business Understanding / Data Understanding

**Precondiciones**:
- Requerimiento inicial disponible (texto, PDF, o historia base)
- Contexto de negocio documentado en `00-shared/context.md`

**Postcondiciones**:
- Historia de usuario enriquecida con KPIs, fuentes y reglas de negocio
- `planner-input.json` preliminar creado con `status: "draft"`

**Entradas obligatorias**:
- `inputs/initial-requirement.md`
- `inputs/source-documents.md` (si existen)

**Salidas obligatorias**:
- `outputs/enriched-user-story.json`
- `outputs/planner-input.json` (preliminar — para Agent Data Governance)

**Criterios para avanzar**:
- [ ] KPIs de negocio definidos
- [ ] Fuentes de datos identificadas
- [ ] Granularidad definida
- [ ] Reglas de negocio documentadas
- [ ] `planner-input.json` tiene campos: `business_context`, `objective`, `scope`, `data_sources`, `kpis`

**Errores comunes**:
- Scope indefinido → bloquear y registrar en open-questions
- Fuentes sin owner → registrar en governance-risks para Agent Data Governance
- KPIs sin denominador → agregar como pregunta abierta

---

## Agente 02: Agent Data Governance

**Fase CRISP-DM**: Business Understanding / Data Understanding

**Precondiciones**:
- `planner-input.json` preliminar de Agente 01 disponible en `inputs/`
- Acceso a catálogo de datos y registro de entidades PII

**Postcondiciones**:
- Datos clasificados con nivel de sensibilidad
- Ownership y stewardship asignados
- PII y datos sensibles identificados
- Data contracts, lineage y acceso definidos
- `planner-input.json` gobernado en `outputs/` con campos de gobierno completos

**Entradas obligatorias**:
- `inputs/planner-input.json` (del Agente 01)

**Salidas obligatorias**:
- `outputs/governance-assessment.md`
- `outputs/data-classification.md`
- `outputs/data-ownership.md`
- `outputs/pii-sensitive-data-review.md`
- `outputs/planner-input.json` (gobernado — para Agent Planner)

**Criterios para avanzar**:
- [ ] Clasificación de datos documentada
- [ ] Ownership con nombre y rol
- [ ] PII/datos sensibles identificados y mitigados
- [ ] Data contracts definidos o anotados como pendientes
- [ ] Controles de acceso documentados
- [ ] `planner-input.json` gobernado tiene sección `governance` completa
- [ ] `requires_human_review` evaluado

**Errores comunes**:
- Datos sin clasificar → no avanzar a Planner
- Ownership sin definir → escalar a Data Owner
- PII sin controles → bloquear hasta definir mitigación

---

## Agente 03: Agent Planner

**Fase CRISP-DM**: Data Understanding / Data Preparation

**Precondiciones**:
- `planner-input.json` gobernado de Agente 02 disponible
- Aprobaciones de gobierno completadas

**Postcondiciones**:
- Plan técnico-funcional documentado
- Backlog y sprints definidos
- Quality gates para todos los agentes siguientes definidos

**Entradas obligatorias**:
- `inputs/planner-input.json` (gobernado, del Agente 02)

**Salidas obligatorias**:
- `outputs/product-plan.json`
- `outputs/coder-input.json` (para Agent Coder)

**Criterios para avanzar**:
- [ ] Arquitectura seleccionada (Medallion o SAS)
- [ ] Épicas y features definidas
- [ ] Quality gates documentados
- [ ] Riesgos técnicos identificados
- [ ] `coder-input.json` tiene spec técnica completa

---

## Agente 04: Agent Coder

**Fase CRISP-DM**: Data Preparation / Modeling

**Precondiciones**:
- `coder-input.json` de Agente 03 disponible
- Entorno de desarrollo configurado

**Postcondiciones**:
- Código implementado o preparado
- Archivos modificados documentados
- `qa-input.json` generado

**Entradas obligatorias**:
- `inputs/coder-input.json`

**Salidas obligatorias**:
- `outputs/implementation-summary.md`
- `outputs/changed-files.md`
- `outputs/qa-input.json` (para Agent QA)

**Criterios para avanzar**:
- [ ] Código sigue PEP 8 y estándares del repo
- [ ] Logging y error handling incluidos
- [ ] Sin hardcoding de credenciales o paths
- [ ] Docstrings en funciones principales
- [ ] `qa-input.json` incluye mapa de componentes

---

## Agente 05: Agent QA

**Fase CRISP-DM**: Modeling / Evaluation

**Precondiciones**:
- `qa-input.json` de Agente 04 disponible
- Código accesible para pruebas

**Postcondiciones**:
- Plan de pruebas ejecutado
- Defectos documentados por severidad
- Sin defectos P0 abiertos

**Entradas obligatorias**:
- `inputs/qa-input.json`

**Salidas obligatorias**:
- `outputs/test-results.json`
- `outputs/data-quality-input.json` (para Agent Data Quality)

**Criterios para avanzar**:
- [ ] Cobertura de tests ≥80%
- [ ] Sin defectos P0 abiertos
- [ ] Escenarios positivos y negativos ejecutados
- [ ] `data-quality-input.json` incluye datasets de prueba

---

## Agente 06: Agent Data Quality

**Fase CRISP-DM**: Data Preparation / Evaluation

**Precondiciones**:
- `data-quality-input.json` de Agente 05 disponible
- Reglas DQ definidas en `00-shared/`

**Postcondiciones**:
- 7 dimensiones DQ evaluadas
- DQ score ≥98%
- Control totals reconciliados

**Entradas obligatorias**:
- `inputs/data-quality-input.json`

**Salidas obligatorias**:
- `outputs/data-quality-report.json`
- `outputs/documentation-input.json` (para Agent Documentation)

**Criterios para avanzar**:
- [ ] DQ score global ≥98%
- [ ] Sin anomalías críticas sin resolución
- [ ] Control totals documentados
- [ ] `documentation-input.json` incluye reglas DQ validadas

---

## Agente 07: Agent Documentation

**Fase CRISP-DM**: Deployment

**Precondiciones**:
- `documentation-input.json` de Agente 06 disponible
- Todos los outputs de agentes previos accesibles

**Postcondiciones**:
- Documentación funcional y técnica completa
- Diccionario de datos actualizado
- Lineage documentado

**Entradas obligatorias**:
- `inputs/documentation-input.json`

**Salidas obligatorias**:
- `outputs/functional-documentation.md`
- `outputs/technical-documentation.md`
- `outputs/data-dictionary.md`
- `outputs/lineage.md`
- `outputs/compliance-input.json` (para Agent Compliance)

---

## Agente 08: Agent Compliance / Security

**Fase CRISP-DM**: Evaluation / Deployment

**Precondiciones**:
- `compliance-input.json` de Agente 07 disponible
- Security checklist disponible en templates

**Postcondiciones**:
- OWASP Top 10 evaluado
- LFPDPPP/CNBV revisado
- `deployment_approved: true`

**Entradas obligatorias**:
- `inputs/compliance-input.json`

**Salidas obligatorias**:
- `outputs/security-review.md`
- `outputs/privacy-review.md`
- `outputs/deployment-input.json` (para Agent Deployment)

**Criterios para avanzar**:
- [ ] Sin vulnerabilidades críticas abiertas
- [ ] `deployment_approved: true`
- [ ] Aprobación de CISO y Compliance Officer si aplica

---

## Agente 09: Agent Deployment

**Fase CRISP-DM**: Deployment

**Precondiciones**:
- `deployment-input.json` de Agente 08 con `deployment_approved: true`

**Postcondiciones**:
- Plan de despliegue ejecutado o documentado
- Release notes generadas
- Rollback plan disponible

**Entradas obligatorias**:
- `inputs/deployment-input.json`

**Salidas obligatorias**:
- `outputs/deployment-plan.md`
- `outputs/release-notes.md`
- `outputs/rollback-plan.md`
- `outputs/monitoring-input.json` (para Agent Monitoring)

---

## Agente 10: Agent Monitoring

**Fase CRISP-DM**: Monitoring & Continuous Improvement

**Precondiciones**:
- `monitoring-input.json` de Agente 09 disponible
- Producto desplegado o en staging

**Postcondiciones**:
- KPIs operativos definidos
- Alertas configuradas
- Backlog de mejora continua creado
- `final-product-evidence.json` generado

**Entradas obligatorias**:
- `inputs/monitoring-input.json`

**Salidas obligatorias**:
- `outputs/monitoring-plan.md`
- `outputs/alerts.md`
- `outputs/final-product-evidence.json`

**Criterios de cierre del ciclo**:
- [ ] Disponibilidad objetivo ≥99.5% documentada
- [ ] DQ score operativo ≥98%
- [ ] Alertas P1/P2 configuradas
- [ ] `final-product-evidence.json` en estado `approved`
- [ ] Backlog de mejora continua tiene al menos 1 ítem

---

## Manejo de Bloqueantes

| Tipo | Acción |
|---|---|
| Pregunta sin respuesta | Registrar en `00-shared/open-questions.md`, no avanzar |
| Riesgo nuevo | Registrar en `00-shared/risk-register.md` |
| Rechazo de handoff | Regresar al agente anterior con retroalimentación en handoff JSON |
| Dato faltante | Registrar como bloqueante en `handoff/*.json` con `blockers` |
| Aprobación pendiente | Marcar `requires_human_review: true` y esperar |
