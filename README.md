# DataLabLeague - Team X

## Descripción

Proyecto de DataLabLeague para el equipo X enfocado en datos, calidad e innovación.

## Estructura del Proyecto

- `docs/` - Documentación del proyecto
- `src/` - Código fuente
- `tests/` - Pruebas unitarias
- `dq/` - Reglas de calidad de datos
- `pipeline/` - Pipelines de datos
- `observability/` - Logging y métricas
- `evidence/` - Evidencia de cumplimiento
- `scorecard/` - Auto-evaluación y métricas
- `contracts/` - Contratos de datos, calidad, interfaces, SLA/SLO y gobierno
- `agent-workflow/` - Orquestación de agentes IA encadenados (CRISP-DM)

## Contracts

Los contratos son artefactos de primera clase de este repositorio. Toda transformación, interfaz o producto de datos debe tener sus contratos formalizados antes de pasar a producción.

**Ubicación**: `/contracts/`

**¿Qué son los contratos?** Documentos que definen compromisos formales sobre:
- Qué datos se producen y cómo (Data Product Contract)
- Qué calidad deben tener (Data Quality Contract)
- Cómo se entregan entre sistemas (Interface Contract)
- Cuándo y con qué disponibilidad (SLA/SLO Contract)
- Cómo se gobiernan (Governance Contract)

**Cómo crear uno nuevo**:
1. Elige el template en `contracts/templates/`
2. Nómbralo según la [convención de nombres](contracts/README.md#convención-de-nombres)
3. Colócalo en la subcarpeta correspondiente
4. Regístralo en `contracts/contracts.md`
5. Abre un PR con el checklist de contratos

**Relación con Data Quality**: Las reglas en `dq/rules.md` implementan los compromisos formalizados en `contracts/quality/`.

**Relación con CRISP-DM**: Los contratos se crean y actualizan en cada fase del ciclo CRISP-DM. Ver `contracts/README.md` para la tabla de correspondencia.

**Revisión en PR**: Todo PR que modifique datos, esquemas o pipelines debe completar el checklist de contratos del PR template.

## Evidencia

Este proyecto mantiene tres niveles de evidencia documentados en [`docs/evidence-architecture.md`](docs/evidence-architecture.md):

1. **Evidencia Granular** (`agent-workflow/XX-agent-name/evidence/`) — Trazabilidad por agente
2. **Tracking Operativo** (`agent-workflow/evidence/`) — Índice central del workflow
3. **Presentación Final** (`evidence/`) — Evidencia consolidada para evaluación

**Relación**: La evidencia granular alimenta el tracking operativo, que a su vez consolida la presentación final.

**Para jurados y evaluadores**: Ver [`evidence/`](evidence/)  
**Para tracking del workflow**: Ver [`agent-workflow/evidence/evidence-index.md`](agent-workflow/evidence/evidence-index.md)  
**Para arquitectura completa**: Ver [`docs/evidence-architecture.md`](docs/evidence-architecture.md)

## Inicio Rápido

1. Clonar el repositorio
2. Instalar dependencias
3. Ejecutar tests

## Documentación

Consulte la documentación en `docs/` para más detalles.

---

## Agent Workflow

La carpeta `/agent-workflow/` contiene la infraestructura de orquestación de agentes IA para producir datos gobernados, medibles y trazables siguiendo CRISP-DM.

### Cadena de Agentes

```
requerimiento inicial
    ↓
01 Enrich Data Story User  →  planner-input.json (preliminar)
    ↓
02 Agent Data Governance   →  planner-input.json (gobernado) ← PASO CLAVE
    ↓
03 Agent Planner           →  coder-input.json
    ↓
04 Agent Coder             →  qa-input.json
    ↓
05 Agent QA                →  data-quality-input.json
    ↓
06 Agent Data Quality      →  documentation-input.json
    ↓
07 Agent Documentation     →  compliance-input.json
    ↓
08 Agent Compliance/Sec    →  deployment-input.json
    ↓
09 Agent Deployment        →  monitoring-input.json
    ↓
10 Agent Monitoring        →  final-product-evidence.json
```

**Agent Data Governance (paso 02)** es el guardián de la gobernanza: valida y enriquece el `planner-input.json` con clasificación de datos, ownership, PII, data contracts, controles de acceso y riesgos regulatorios **antes** de que Agent Planner diseñe la arquitectura.

### Cómo Usar

1. Leer `agent-workflow/00-shared/context.md` para entender el contexto del producto.
2. Iniciar en `agent-workflow/01-enrich-data-story-user/inputs/initial-requirement.md`.
3. Seguir la cadena: cada `handoff/handoff-*.json` indica el siguiente paso.
4. El ciclo cierra cuando `10-agent-monitoring/outputs/final-product-evidence.json` está en estado `approved`.

### Evidencia para Pull Requests

Todo PR que avance la cadena de agentes debe completar el **Agent Workflow Checklist** del PR template y dejar evidencia en `agent-workflow/evidence/evidence-index.md`.

Ver [`agent-workflow/README.md`](agent-workflow/README.md) para documentación completa.

---

## GitHub Copilot Agents

Las instrucciones de los agentes para GitHub Copilot viven en `.github/agents/`.

Los artefactos operativos generados por los agentes viven en `/agent-workflow/`.

### Cadena oficial de ejecución

| # | Agente | Archivo |
|---|---|---|
| 01 | Enrich Data Story User | `.github/agents/01_enrich-data-story-user.agent.md` |
| 02 | Data Governance | `.github/agents/02_data-governance.agent.md` |
| 03 | Planner | `.github/agents/03_planner.agent.md` |
| 04 | Coder | `.github/agents/04_coder.agent.md` |
| 05 | QA | `.github/agents/05_qa.agent.md` |
| 06 | Data Quality | `.github/agents/06_data-quality.agent.md` |
| 07 | Documentation | `.github/agents/07_documentation.agent.md` |
| 08 | Compliance / Security | `.github/agents/08_compliance-security.agent.md` |
| 09 | Deployment | `.github/agents/09_deployment.agent.md` |
| 10 | Monitoring | `.github/agents/10_monitoring.agent.md` |
| 99 | Reviewer (transversal) | `.github/agents/99_reviewer.agent.md` |

El agente **Reviewer (99)** es un agente transversal de revisión y aseguramiento de calidad. Puede invocarse en cualquier punto de la cadena y **no modifica archivos**.

---

## Sprint 1 Evaluation

La carpeta `/evaluations/sprint-01/` contiene la infraestructura formal de evaluación para el Sprint 1 de DataLab League.

### Entregables Evaluados

| Entregable | Puntos |
|-----------|--------|
| GitHub Copilot Instructions (`githubcopilot-instructions.md` o equivalente) | 40 |
| README general del repositorio | 20 |
| **Total Sprint 1** | **60** |

### Estructura de Evaluación

| Carpeta / Archivo | Descripción |
|-------------------|---|
| `evaluations/sprint-01/rubrics/` | Rúbricas de evaluación por entregable |
| `evaluations/sprint-01/teams/team-01/` | Resultados para Team 01 |
| `evaluations/sprint-01/teams/team-02/` | Resultados para Team 02 |
| `evaluations/sprint-01/teams/team-03/` | Resultados para Team 03 |
| `evaluations/sprint-01/scoring-summary.md` | Resumen comparativo de puntajes |
| `evaluations/sprint-01/sprint-01-scoreboard.md` | Ranking y badges |
| `evaluations/sprint-01/agent-evaluator/` | Agente evaluador del sprint |

### Agente Evaluador

El agente evaluador está disponible en `.github/agents/99_sprint-01-evaluator.agent.md`.

Utiliza el prompt en `evaluations/sprint-01/agent-evaluator/evaluator-prompt.md` para evaluar cada equipo.

---

## Contribuidores

- Jose Antonio Esparza
- Team 
