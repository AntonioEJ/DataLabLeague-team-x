# Agent Workflow — DataLab League

## Propósito

Esta carpeta contiene la infraestructura operativa de orquestación de agentes IA para el proyecto DataLab League.

Define la cadena de trabajo encadenada, donde **el output de cada agente se convierte en el input del siguiente**, garantizando trazabilidad, gobernanza y reproducibilidad en cada producto de datos.

---

## Dinámica DataLab League

DataLab League opera bajo el modelo de **cadena de valor agenticia**: cada agente especializado toma un artefacto estructurado, ejecuta su rol CRISP-DM, produce evidencia verificable y entrega al siguiente agente mediante un handoff formal.

El flujo siempre inicia con un requerimiento de negocio y cierra con `final-product-evidence.json`.

---

## Cadena de Agentes

```
requerimiento inicial
    ↓
01 Enrich Data Story User
    ↓ planner-input.json (preliminar)
02 Agent Data Governance
    ↓ planner-input.json (gobernado)
03 Agent Planner
    ↓ coder-input.json
04 Agent Coder
    ↓ qa-input.json
05 Agent QA
    ↓ data-quality-input.json
06 Agent Data Quality
    ↓ documentation-input.json
07 Agent Documentation
    ↓ compliance-input.json
08 Agent Compliance / Security
    ↓ deployment-input.json
09 Agent Deployment
    ↓ monitoring-input.json
10 Agent Monitoring
    ↓ final-product-evidence.json
```

---

## Rol de Agent Data Governance (paso 02)

Agent Data Governance es el **guardián de la gobernanza** antes de la planificación técnica. Recibe el `planner-input.json` preliminar generado por Enrich Data Story User, lo enriquece con:

- Clasificación de datos y ownership
- Identificación de PII y datos sensibles
- Requerimientos de data catalog y lineage
- Data contracts y controles de acceso
- Riesgos regulatorios (LFPDPPP, CNBV)
- Aprobaciones requeridas

Produce un `planner-input.json` **gobernado y validado** que es el input oficial de Agent Planner.

---

## Relación con CRISP-DM

| Fase CRISP-DM | Agentes |
|---|---|
| Business Understanding | 01 Enrich, 02 Data Governance, 03 Planner |
| Data Understanding | 01 Enrich, 02 Data Governance, 03 Planner |
| Data Preparation | 03 Planner, 04 Coder, 06 Data Quality |
| Modeling / Business Logic | 03 Planner, 04 Coder, 05 QA |
| Evaluation | 05 QA, 06 Data Quality, 08 Compliance |
| Deployment | 07 Documentation, 09 Deployment |
| Monitoring & Improvement | 10 Monitoring |

---

## Estructura de Carpetas

```
agent-workflow/
├── README.md                     ← este archivo
├── workflow-map.md               ← tabla completa de agentes
├── agent-chain.md                ← orden, pre/postcondiciones, criterios
├── handoff-protocol.md           ← protocolo formal de transferencia
├── naming-conventions.md         ← convenciones de nombres y versiones
├── 00-shared/                    ← contexto compartido por todos los agentes
├── 01-enrich-data-story-user/
├── 02-agent-data-governance/
├── 03-agent-planner/
├── 04-agent-coder/
├── 05-agent-qa/
├── 06-agent-data-quality/
├── 07-agent-documentation/
├── 08-agent-compliance-security/
├── 09-agent-deployment/
├── 10-agent-monitoring/
├── templates/                    ← plantillas reutilizables
├── schemas/                      ← JSON Schemas de validación
└── evidence/                     ← índice global de evidencia (tracking operativo)
```

---

## Flujo de Evidencia

### Tres Niveles de Evidencia

1. **Evidencia Granular** (por agente)
   - Ubicación: `agent-workflow/XX-agent-name/evidence/`
   - Contenido: Logs, decisiones, outputs, handoffs del agente específico
   - Propósito: Trazabilidad detallada de ejecución

2. **Tracking Operativo** (workflow)
   - Ubicación: `agent-workflow/evidence/`
   - Contenido: `evidence-index.md` con registro EVD-001 a EVD-010
   - Propósito: Índice central de evidencia del workflow

3. **Presentación Final** (raíz)
   - Ubicación: `evidence/` (raíz del repositorio)
   - Contenido: Data story, skills, testing, DQ, governance, demo
   - Propósito: Evidencia consolidada para evaluación DataLab League

### Relación

```
Agentes (XX-agent-name/evidence/)
        ↓
Workflow (agent-workflow/evidence/evidence-index.md)
        ↓
Presentación (evidence/)
```

Cada carpeta de agente tiene la misma estructura interna:

```
XX-agent-name/
├── README.md
├── inputs/
├── outputs/
├── handoff/
└── evidence/
```

---

## Inputs, Outputs, Handoff y Evidence

| Subcarpeta | Contenido |
|---|---|
| `inputs/` | Artefactos recibidos del agente anterior. No modificar directamente. |
| `outputs/` | Artefactos producidos por este agente. Incluye el input del siguiente. |
| `handoff/` | Documento de transferencia formal (MD + JSON). |
| `evidence/` | Referencias a commits, PRs, screenshots, logs de evidencia. |

---

## Cómo Usar Este Workflow

1. Leer `00-shared/context.md` para entender el contexto del producto de datos.
2. Identificar el agente activo según la fase CRISP-DM.
3. Leer el artefacto en `inputs/` del agente actual.
4. Ejecutar el rol del agente y producir los artefactos en `outputs/`.
5. Actualizar `00-shared/assumptions.md`, `open-questions.md` y `risk-register.md` si aplica.
6. Completar el artefacto en `handoff/` y marcar `quality_gate.passed: true`.
7. Copiar el output principal a `inputs/` del siguiente agente.
8. Dejar evidencia en `evidence/` (commits, PRs).

---

## Validación del Paso Entre Agentes

Un agente puede entregar al siguiente **solo si**:

- [ ] Todos los outputs obligatorios existen y están en estado `approved` o `ready_for_next_agent`.
- [ ] El handoff JSON tiene `quality_gate.passed: true`.
- [ ] Las preguntas abiertas bloqueantes están resueltas.
- [ ] La evidencia en GitHub está registrada.
- [ ] Para paso 01→02: `planner-input.json` preliminar existe.
- [ ] Para paso 02→03: `planner-input.json` gobernado existe con campos de gobierno completos.

---

## Definition of Done del Workflow

El workflow de un producto de datos está completo cuando:

- [ ] `final-product-evidence.json` existe en `10-agent-monitoring/outputs/`.
- [ ] Los 10 agentes tienen outputs en estado `approved`.
- [ ] `evidence-index.md` lista evidencia de los 10 agentes.
- [ ] `README.md` raíz del repositorio menciona el cierre del ciclo.
- [ ] No hay preguntas abiertas bloqueantes sin resolver.

---

## Referencia

- [workflow-map.md](workflow-map.md) — tabla completa de la cadena
- [agent-chain.md](agent-chain.md) — precondiciones, postcondiciones y criterios
- [handoff-protocol.md](handoff-protocol.md) — protocolo de transferencia
- [00-shared/](00-shared/README.md) — contexto compartido
