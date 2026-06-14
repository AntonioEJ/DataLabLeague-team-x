# Agentes de GitHub Copilot

## Descripción General

Este documento describe los agentes personalizados de GitHub Copilot para el proyecto DataLabLeague.

## Modelo de Agentes - Data Product (Cadena de Valor Agenticia)

![Profuturo - Modelo de agentes Data Product](./docs/images/profuturo-agents-model.png)

**Referencia**: Profuturo - O1 Modelo de agentes Data Product (cadena de valor agenticia)

## Estrategia de Flujo

```
Caso de uso
    ↓
Data Story enriquecida (Enrich Data Story User Agent)
    ↓
Agentes Especializados (Planner, Coder, QA, etc.)
    ↓
Skills Reutilizables
    ↓
Código
    ↓
Testing
    ↓
Data Quality Rules
    ↓
Evidencia
    ↓
Playbook Reutilizable
```

## Agentes Disponibles

### Agents Core (Fase 1)

#### 00. Enrich Data Story User Agent
**Archivo**: `.github/agents/00_enrich-data-story-user.agent.md`

Punto de entrada inicial. Especializado en enriquecimiento de historias de usuario de datos. Conecta necesidad de negocio, KPI, decisión, fuentes, granularidad, reglas DQ, criterios de aceptación y evidencia.

**Propósito**: Transformar casos de uso ambiguos en data stories ricas y listas para implementación.

---

#### 01. Planner Agent
**Archivo**: `.github/agents/01_planner.agent.md`
**Fase CRISP-DM**: Entendimiento del Negocio

Especializado en planificación de proyectos y estructuración de casos de uso.

**Evidencia de Alineación**:
- Caso de uso definido
- Meta de tablero
- Contrato de datos
- SLAs y criterios de aceptación

---

#### 03. Coder Agent
**Archivo**: `.github/agents/03_coder.agent.md`
**Fase CRISP-DM**: Preparación de Datos / Implementación

Especializado en implementación de código y desarrollo de funcionalidades.

**Evidencia de Alineación**:
- Código generado o refactorizado
- Modularidad y configuración
- Commits documentados

---

#### 04. QA Agent
**Archivo**: `.github/agents/04_qa.agent.md`
**Fase CRISP-DM**: Evaluación

Especializado en pruebas, validación y aseguramiento de calidad.

**Evidencia de Alineación**:
- Pruebas ejecutadas
- Validaciones y escenarios positivos/negativos
- Reporte de resultados

---

#### 05. Documentation Agent
**Archivo**: `.github/agents/05_documentation.agent.md`
**Fase CRISP-DM**: Despliegue / Operación

Especializado en generación y mantenimiento de documentación.

**Evidencia de Alineación**:
- README y docstrings
- Diccionario de datos
- Linaje de datos
- Guía de operación

---

#### 02. Data Quality Agent
**Archivo**: `.github/agents/02_data-quality.agent.md`
**Fase CRISP-DM**: Entendimiento y Preparación de Datos

Especializado en calidad de datos y validación.

**Evidencia de Alineación**:
- Reglas DQ definidas
- Score de calidad
- Validación de nulos, duplicados y anomalías

---

### Agents Complementarios

#### 06. Compliance & Security Agent
**Archivo**: `.github/agents/06_compliance-security.agent.md`

Especializado en cumplimiento normativo y seguridad.

#### 07. Pipeline Agent
**Archivo**: `.github/agents/07_pipeline.agent.md`

Especializado en pipelines de datos y orquestación.

#### 08. Observability Agent
**Archivo**: `.github/agents/08_observability.agent.md`

Especializado en logging, métricas y monitoreo.

## Configuración

Ver `.github/agents/` para configuración específica de cada agente.

## Punto de Entrada

El flujo comienza siempre con el **Enrich Data Story User Agent**, que enriquece la entrada del usuario antes de pasar a otros agentes especializados.

## Requisitos de Orquestación

Diseñar y orquestar agentes **incluye obligatoriamente**:

- **GitHub Copilot Instructions** (`.github/copilot-instructions.md`)
- **Prompts** (`.github/prompts/*.prompt.md`)
- **Agents** (`.github/agents/*.agent.md`)
- **Skills** (`.github/skills/*/SKILL.md`)

Cada agente debe tener configuración completa con propósito, inputs, outputs, handoffs y criterios de éxito.
