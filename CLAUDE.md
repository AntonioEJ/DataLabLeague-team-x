# CLAUDE - Guía Detallada de Agentes

Documentación detallada del flujo de agentes en `agent-workflow/` para Data Lab League.

---

## Encadenamiento de Agentes

### Flujo Principal (Mandatory Path)

#### 00 — Shared Context
**Directorio**: `agent-workflow/00-shared/`  
**Tipo**: Contexto compartido (no es un agente ejecutor)

Contenedor de contexto reutilizable entre todos los agentes.

**Artefactos**:
- `context.md` — Contexto general del proyecto
- `data-sources.md` — Catálogo de fuentes de datos disponibles
- `risk-register.md` — Registro de riesgos identificados

**Handoff**: Consumido por todos los agentes

---

#### 01 — Enrich Data Story User Agent
**Directorio**: `agent-workflow/01-enrich-data-story-user/`  
**Archivo Config**: `.github/agents/01_enrich-data-story-user.agent.md`  
**Fase CRISP-DM**: Business Understanding

Punto de entrada inicial. Especializado en enriquecimiento de historias de usuario de datos. Conecta necesidad de negocio, KPI, decisión, fuentes, granularidad, reglas DQ, criterios de aceptación y evidencia.

**Propósito**: Transformar casos de uso ambiguos en data stories ricas y listas para governance.

**Inputs**:
- Caso de uso del usuario (natural language)
- `agent-workflow/00-shared/context.md`
- `agent-workflow/00-shared/data-sources.md`

**Outputs**:
- `agent-workflow/01-enrich-data-story-user/outputs/data-story-enriched.md`
- `agent-workflow/01-enrich-data-story-user/outputs/planner-input.json` (preliminar) ⚠️ **NO ES LA VERSIÓN FINAL**

**Evidencia de Alineación**:
- Caso de uso enriquecido con KPIs y decisiones de negocio
- Data story documentada
- Input preliminar generado

**Quality Gates**:
- [ ] Caso de uso enriquecido con objetivo de negocio claro
- [ ] KPIs y decisiones identificadas
- [ ] Fuentes de datos preliminares mapeadas
- [ ] `planner-input.json` preliminar generado

**Handoff**: → **Agent 02 Data Governance (OBLIGATORIO)**

---

#### 02 — Data Governance Agent ⚠️ CHECKPOINT CRÍTICO
**Directorio**: `agent-workflow/02-agent-data-governance/`  
**Archivo Config**: `.github/agents/02_data-governance.agent.md`  
**Fase CRISP-DM**: Business Understanding / Data Understanding

**POSICIÓN OBLIGATORIA**: Entre Agent 01 y Agent 03. Ningún producto de datos puede avanzar a planificación técnica sin pasar por governance.

**Propósito**: Validar y enriquecer el `planner-input.json` preliminar con gobierno de datos: ownership, clasificación, PII, datos sensibles, lineage, data catalog, data contracts, controles de acceso y aprobaciones regulatorias.

**Inputs**:
- `agent-workflow/01-enrich-data-story-user/outputs/planner-input.json` (preliminar)
- `agent-workflow/00-shared/context.md`
- `agent-workflow/00-shared/data-sources.md`
- `agent-workflow/00-shared/risk-register.md`

**Outputs**:
- `agent-workflow/02-agent-data-governance/outputs/governance-assessment.md`
- `agent-workflow/02-agent-data-governance/outputs/data-classification.md`
- `agent-workflow/02-agent-data-governance/outputs/data-ownership.md`
- `agent-workflow/02-agent-data-governance/outputs/pii-sensitive-data-review.md`
- `agent-workflow/02-agent-data-governance/outputs/data-catalog-requirements.md`
- `agent-workflow/02-agent-data-governance/outputs/lineage-requirements.md`
- `agent-workflow/02-agent-data-governance/outputs/data-contracts-requirements.md`
- `agent-workflow/02-agent-data-governance/outputs/access-control-requirements.md`
- `agent-workflow/02-agent-data-governance/outputs/governance-risks.md`
- `agent-workflow/02-agent-data-governance/outputs/governance-decision-log.md`
- **`agent-workflow/02-agent-data-governance/outputs/planner-input.json`** ← **OUTPUT PRINCIPAL (GOBERNADO)**

**Responsabilidades**:
- Clasificar datos (público/interno/confidencial/restringido)
- Asignar Data Owner, Data Steward y Custodio Técnico
- Inventariar PII y datos sensibles
- Definir controles de acceso y enmascaramiento
- Evaluar riesgos regulatorios (LFPDPPP, CNBV)
- Documentar data contracts y lineage requeridos
- Obtener aprobaciones de Data Owner y Governance Lead

**Quality Gates** (CRÍTICOS):
- [ ] Todas las entidades y campos clasificados
- [ ] Data Owner, Steward y Custodio asignados
- [ ] Campos PII inventariados con controles definidos
- [ ] Data contracts identificados
- [ ] Controles de acceso documentados
- [ ] Riesgos regulatorios evaluados
- [ ] **`governance.governance_approved: true`** en el output
- [ ] `governance.conditions_for_planner` completado
- [ ] `planner-input.json` gobernado copiado a `03-agent-planner/inputs/`
- [ ] Aprobación de Data Owner obtenida
- [ ] Aprobación de Data Governance Lead obtenida

**Evidencia Requerida**:
- Commit con `outputs/planner-input.json` gobernado
- Aprobaciones documentadas en `governance-assessment.md`
- Evidencia en `agent-workflow/02-agent-data-governance/evidence/`

**Handoff**: → **Agent 03 Planner** (solo con `governance_approved: true`)

**⚠️ REGLA CRÍTICA**: Sin `governance.governance_approved: true` → NO SE PUEDE avanzar a Agent 03

---

#### 03 — Planner Agent
**Directorio**: `agent-workflow/03-agent-planner/`  
**Archivo Config**: `.github/agents/03_planner.agent.md`  
**Fase CRISP-DM**: Business Understanding / Data Understanding

Especializado en planificación de proyectos y estructuración de casos de uso.

**Inputs**:
- `agent-workflow/03-agent-planner/inputs/planner-input.json` (gobernado) ← **VERSIÓN OFICIAL CON GOVERNANCE**
- `agent-workflow/00-shared/context.md`

**Outputs**:
- `agent-workflow/03-agent-planner/outputs/execution-plan.json`
- `agent-workflow/03-agent-planner/outputs/architecture-decision.md`
- `agent-workflow/03-agent-planner/outputs/implementation-roadmap.md`
- `agent-workflow/03-agent-planner/outputs/data-flow-diagram.md`

**Responsabilidades**:
- Diseñar arquitectura técnica (Databricks Medallion / SAS Analytics)
- Generar plan de ejecución detallado
- Identificar dependencias y secuenciamiento de agentes
- Respetar restricciones de governance (`governance.conditions_for_planner`)

**Evidencia de Alineación**:
- Caso de uso definido
- Meta de tablero
- Contrato de datos
- SLAs y criterios de aceptación
- Arquitectura seleccionada con justificación

**Quality Gates**:
- [ ] `execution-plan.json` generado con secuencia de agentes
- [ ] Arquitectura seleccionada (Medallion o SAS Analytics)
- [ ] ADR creado si se introduce nuevo patrón
- [ ] Restricciones de governance respetadas

**Handoff**: → Agents 04-10 (según `execution-plan.json`)

---

### Flujo de Implementación (Post-Planning)

#### 04 — Coder Agent
**Directorio**: `agent-workflow/04-agent-coder/`  
**Archivo Config**: `.github/agents/04_coder.agent.md`  
**Fase CRISP-DM**: Data Preparation / Modeling / Implementation

Especializado en implementación de código y desarrollo de funcionalidades.

**Inputs**:
- `agent-workflow/03-agent-planner/outputs/execution-plan.json`

**Outputs**:
- Código implementado en `src/` o rutas definidas
- `agent-workflow/04-agent-coder/outputs/implementation-summary.md`
- `agent-workflow/04-agent-coder/outputs/code-structure.md`

**Evidencia de Alineamiento**:
- Código generado o refactorizado
- Modularidad y configuración
- Commits documentados

**Quality Gates**:
- [ ] PEP 8 compliance
- [ ] Type annotations
- [ ] Docstrings (Google style)
- [ ] Error handling y logging
- [ ] Sin hardcoding de credenciales

**Handoff**: → Agent 05 QA

---

#### 05 — QA Agent
**Directorio**: `agent-workflow/05-agent-qa/`  
**Archivo Config**: `.github/agents/05_qa.agent.md`  
**Fase CRISP-DM**: Evaluation

Especializado en pruebas, validación y aseguramiento de calidad.

**Inputs**:
- Código de Agent 04
- `agent-workflow/03-agent-planner/outputs/execution-plan.json`

**Outputs**:
- Tests en `tests/`
- `agent-workflow/05-agent-qa/outputs/test-report.md`
- `agent-workflow/05-agent-qa/outputs/coverage-report.md`

**Evidencia de Alineamiento**:
- Pruebas ejecutadas
- Validaciones y escenarios positivos/negativos
- Reporte de resultados

**Handoff**: → Agent 06 Data Quality

---

#### 06 — Data Quality Agent
**Directorio**: `agent-workflow/06-agent-data-quality/`  
**Archivo Config**: `.github/agents/06_data-quality.agent.md`  
**Fase CRISP-DM**: Data Understanding / Data Preparation

Especializado en calidad de datos y validación.

**Inputs**:
- `agent-workflow/03-agent-planner/outputs/execution-plan.json`
- `agent-workflow/02-agent-data-governance/outputs/data-classification.md`
- Código de Agent 04

**Outputs**:
- `agent-workflow/06-agent-data-quality/outputs/dq-rules.json`
- `agent-workflow/06-agent-data-quality/outputs/validation-schema.json`
- `agent-workflow/06-agent-data-quality/outputs/quality-dashboard-spec.md`

**Evidencia de Alineamiento**:
- Reglas DQ definidas
- Score de calidad
- Validación de nulos, duplicados y anomalías

**Handoff**: → Agent 07 Documentation

---

#### 07 — Documentation Agent
**Directorio**: `agent-workflow/07-agent-documentation/`  
**Archivo Config**: `.github/agents/07_documentation.agent.md`  
**Fase CRISP-DM**: Deployment / Operation

Especializado en generación y mantenimiento de documentación.

**Inputs**:
- Código de Agent 04
- Tests de Agent 05
- DQ Rules de Agent 06
- Plan de Agent 03

**Outputs**:
- `README.md` actualizado
- `agent-workflow/07-agent-documentation/outputs/data-dictionary.md`
- `agent-workflow/07-agent-documentation/outputs/lineage-diagram.md`
- `agent-workflow/07-agent-documentation/outputs/operations-guide.md`

**Evidencia de Alineamiento**:
- README y docstrings
- Diccionario de datos
- Linaje de datos
- Guía de operación

**Handoff**: → Agent 08 Compliance & Security

---

### Flujo de Aseguramiento (Post-Implementation)

#### 08 — Compliance & Security Agent
**Directorio**: `agent-workflow/08-agent-compliance-security/`  
**Archivo Config**: `.github/agents/08_compliance-security.agent.md`

Especializado en cumplimiento normativo y seguridad.

**Inputs**:
- Código de Agent 04
- Documentación de Agent 07
- Governance de Agent 02

**Outputs**:
- `agent-workflow/08-agent-compliance-security/outputs/security-review.md`
- `agent-workflow/08-agent-compliance-security/outputs/compliance-checklist.md`
- `agent-workflow/08-agent-compliance-security/outputs/vulnerability-scan.md`

**Handoff**: → Agent 09 Deployment

---

#### 09 — Deployment Agent
**Directorio**: `agent-workflow/09-agent-deployment/`  
**Archivo Config**: `.github/agents/09_deployment.agent.md`

Especializado en despliegue y delivery.

**Inputs**:
- Código de Agent 04
- Security review de Agent 08
- Documentation de Agent 07

**Outputs**:
- `agent-workflow/09-agent-deployment/outputs/deployment-plan.md`
- `agent-workflow/09-agent-deployment/outputs/rollback-procedure.md`
- `agent-workflow/09-agent-deployment/outputs/release-notes.md`

**Handoff**: → Agent 10 Monitoring

---

#### 10 — Monitoring Agent
**Directorio**: `agent-workflow/10-agent-monitoring/`  
**Archivo Config**: `.github/agents/10_monitoring.agent.md`

Especializado en observabilidad y monitoreo.

**Inputs**:
- Deployment de Agent 09
- Código de Agent 04

**Outputs**:
- `agent-workflow/10-agent-monitoring/outputs/monitoring-dashboard.md`
- `agent-workflow/10-agent-monitoring/outputs/alert-rules.yaml`
- `agent-workflow/10-agent-monitoring/outputs/observability-config.md`

**Handoff**: → Evidence & Closure

---

## Reglas de Encadenamiento

### OBLIGATORIAS (Non-Negotiable)

1. **Entrada**: Todo caso de uso DEBE iniciar con `01_enrich-data-story-user`
2. **Governance Gate**: `02_data-governance` es **OBLIGATORIO** entre Agent 01 y Agent 03
3. **No Skip**: No se puede omitir Agent 02 bajo ninguna circunstancia
4. **Quality Gate**: `governance.governance_approved: true` requerido para avanzar a Agent 03
5. **Artefacto Gobernado**: Agent 03 consume `planner-input.json` de Agent 02, no de Agent 01

### Flujo Correcto ✅

```
01_enrich → 02_governance → 03_planner → 04-10
```

### Flujos Incorrectos ❌

```
01_enrich → 03_planner  (falta governance)
02_governance → 04_coder  (falta planner)
```

---

## Estructura de Directorios

Cada agente en `agent-workflow/` tiene:

```
XX-agent-name/
├── README.md
├── inputs/
├── outputs/
├── handoff/
└── evidence/
```

---

## Configuración

- **Agent Config**: `.github/agents/` (configuración de agentes)
- **Workflow**: `agent-workflow/` (estructura de directorios y artefactos)
- **Schemas**: `agent-workflow/schemas/` (validación de inputs/outputs)
- **Templates**: `agent-workflow/templates/` (plantillas reutilizables)

---

## Definition of Done

Una entrega está completa solo si tiene:

- [ ] Historia de usuario de datos enriquecida (Agent 01)
- [ ] **Governance aprobado** (Agent 02) con `governance_approved: true`
- [ ] Plan de ejecución (Agent 03)
- [ ] Código implementado (Agent 04)
- [ ] Tests ejecutados (Agent 05)
- [ ] Reglas Data Quality validadas (Agent 06)
- [ ] Documentación completa (Agent 07)
- [ ] Revisión de seguridad (Agent 08)
- [ ] Deployment preparado (Agent 09)
- [ ] Monitoreo configurado (Agent 10)
- [ ] Evidencia en GitHub
- [ ] Skills actualizados si se generó capacidad reutilizable

---

## Invocación de Agentes

### En GitHub Copilot Chat

```markdown
@01_enrich-data-story-user 
Quiero enriquecer este caso de uso: [descripción]
```

```markdown
@04_coder
Implementa esta función según el plan...
```

### Workflow Completo

```markdown
Ejecuta el workflow completo desde Agent 01 hasta Agent 10 para este caso de uso:
[descripción detallada]
```

---

**Última actualización**: 2026-06-28  
**Versión**: 3.0 (Agent Workflow Structure Aligned)
