# Agentes de GitHub Copilot

## Descripción General

Este documento describe los agentes personalizados de GitHub Copilot para el proyecto DataLabLeague.

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

### 1. Enrich Data Story User Agent
**Archivo**: `enrich-data-story-user.agent.md`

Especializado en enriquecimiento de historias de usuario de datos. Conecta necesidad de negocio, KPI, decisión, fuentes, granularidad, reglas DQ, criterios de aceptación y evidencia.

**Propósito**: Transformar casos de uso ambiguos en data stories ricas y listas para implementación.

### 2. Planner Agent
Especializado en planificación de proyectos y estructuración de casos de uso.

### 3. Coder Agent
Especializado en implementación de código y desarrollo de funcionalidades.

### 4. QA Agent
Especializado en pruebas, validación y aseguramiento de calidad.

### 5. Documentation Agent
Especializado en generación y mantenimiento de documentación.

### 6. Compliance & Security Agent
Especializado en cumplimiento normativo y seguridad.

### 7. Data Quality Agent
Especializado en calidad de datos y validación.

### 8. Pipeline Agent
Especializado en pipelines de datos y orquestación.

### 9. Observability Agent
Especializado en logging, métricas y monitoreo.

## Configuración

Ver `.github/agents/` para configuración específica de cada agente.

## Punto de Entrada

El flujo comienza siempre con el **Enrich Data Story User Agent**, que enriquece la entrada del usuario antes de pasar a otros agentes especializados.
