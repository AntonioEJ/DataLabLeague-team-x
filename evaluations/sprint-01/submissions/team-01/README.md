# DataLabLeague - Team SOFOM

## Descripción Ejecutiva

**Problema de negocio**: Profuturo opera una línea SOFOM que otorga préstamos a pensionados y jubilados IMSS Ley 73. La información de clientes, créditos, pagos, reestructuraciones y asesores reside en el sistema operativo **VENTURA**, dispersa en más de 13 tablas sin una capa analítica integrada. Esto impide la visibilidad consolidada de la cartera y la toma de decisiones informada sobre originación, cobranza y riesgo crediticio.

**Producto de datos que se construye**: **Modelo de Datos SOFOM** — un Lakehouse en capas Silver y Gold sobre SAS 9.4 que integra, depura y clasifica la información SOFOM para consumo analítico en Power BI.

**Decisiones que habilita el producto**:
- Seguimiento de cartera activa, vencida y en cobranza por sucursal, ejecutivo y producto.
- Identificación automática de clientes elegibles para renovación de crédito.
- Análisis de morosidad, días de atraso y comportamiento de pago.
- Gestión comercial y seguimiento de desempeño por asesor.
- Reporteo operativo y analítico conciliado con cifras del sistema VENTURA.

**Usuarios y consumidores**:
- Analistas de Cartera, Comercial, Riesgo y Cobranza de la operación SOFOM.
- Equipos directivos que consumen reportes en Power BI.

---

## Contexto DataLab League y Equipo

**Programa**: DataLabLeague — programa de Profuturo para construir productos de datos gobernados, medibles y reutilizables siguiendo CRISP-DM, con agentes IA encadenados y evidencia verificable en GitHub.

**Repositorio**: `coe-bi-datalab-league-SOFOM`

**Equipo SOFOM**:

| Integrante | Rol |
|---|---|
| Jose Antonio Esparza | Lead |
| Diego Hernández | Ingeniero de Datos |
| Gustavo Montiel | Ingeniero de Datos |
| Fernando Lopez | Ingeniero de Datos |
| Ricardo Meneses | Ingeniero de Datos |

---

## Producto de Datos y Alcance

### En alcance
- Integración de tablas VENTURA: solicitudes, contratos, pagos, reestructuraciones, personas, asesores y catálogos.
- Filtrado de créditos SOFOM: `tipo_credito IN (5, 16)` ó `folio LIKE 'I%'` / `folio LIKE 'J%'`.
- **Capa Silver**: limpieza, estandarización y filtrado de datos VENTURA.
- **Capa Gold**: modelo integrado con clasificación de clientes (Nuevos, Inactivos, Renovaciones), métricas de cartera y dimensiones analíticas.
- Consumo en Power BI con cifras conciliadas.
- Historias de usuario: HU-SOFOM-001 a HU-SOFOM-004.

### Fuera de alcance
- Modificación directa de tablas VENTURA (solo lectura).
- Créditos no SOFOM (tipo distinto a 5 y 16, folios sin prefijo I/J).
- Integración con sistemas distintos a VENTURA en esta fase.
- Modelos predictivos o scoring crediticio.
- Automatización de cobranza o generación de contratos.

---

## Estructura del Repositorio

```
coe-bi-datalab-league-SOFOM/
├── .github/
│   ├── copilot-instructions.md   ← Instrucciones para GitHub Copilot
│   └── agents/                   ← Definición de 11 agentes IA (.agent.md)
├── docs/
│   ├── crisp-dm/                 ← Documentación y entregables por fase
│   ├── adr/                      ← Architecture Decision Records
│   ├── user-stories/
│   │   ├── input/                ← PDFs fuente de historias de usuario
│   │   ├── raw/                  ← Historias extraídas sin modificar
│   │   └── enriched/             ← Historias enriquecidas por agente 01
│   ├── architecture.md
│   ├── data-dictionary.md
│   └── data-mapping.md
├── dq/
│   └── rules.md                  ← Reglas de Data Quality SOFOM
├── evidence/                     ← Evidencia de ejecución por agente y entrega
│   └── enrich-data-story-user/   ← Evidencia del agente 01
├── scorecard/                    ← Auto-evaluación y métricas del equipo
├── contracts/                    ← Contratos de datos, calidad, SLA/SLO y gobierno
├── src/                          ← Código fuente SAS / Python
├── tests/                        ← Pruebas unitarias y validaciones DQ
├── pipeline/                     ← Pipelines de datos
└── observability/                ← Logging y métricas
```

**Dónde están los agentes**: `.github/agents/` — 11 archivos `.agent.md` con propósito, inputs, outputs y handoffs.

**Dónde están los inputs**: `docs/user-stories/input/` (PDFs fuente).

**Dónde están los outputs**: `docs/user-stories/raw/` y `docs/user-stories/enriched/`.

**Dónde están las evidencias**: `evidence/<agente>/<ID>.evidence.md`.

**Dónde están los handoffs**: documentados en cada `.enriched.md` y `.evidence.md` (secciones 20 y 21).

---

## Metodología CRISP-DM

Este proyecto aplica CRISP-DM como marco de trabajo iterativo. Cada fase produce entregables verificables antes de avanzar a la siguiente.

| Fase | Estado | Agentes | Entregables clave |
|---|---|---|---|
| 1. Business Understanding | ✅ En progreso | `01_enrich-data-story-user` | Historias enriquecidas en `docs/user-stories/enriched/` |
| 2. Data Understanding | 🔲 Por iniciar | `02_data-governance` | Perfilado VENTURA, diccionario, clasificación PII |
| 3. Data Preparation | 🔲 Por iniciar | `03_planner`, `04_coder` | Capa Silver: limpieza y transformación en SAS 9.4 |
| 4. Modeling / Transformation | 🔲 Por iniciar | `04_coder`, `06_data-quality` | Capa Gold: modelo integrado y segmentación de clientes |
| 5. Evaluation | 🔲 Por iniciar | `05_qa`, `06_data-quality` | Validaciones DQ, cifras de control, pruebas de aceptación |
| 6. Deployment | 🔲 Por iniciar | `09_deployment`, `10_monitoring` | Pipeline productivo, monitoreo y evidencia final aprobada |

Documentación detallada por fase: [`docs/crisp-dm/`](docs/crisp-dm/)

---

## Cadena de Agentes IA

Los agentes GitHub Copilot encadenan el trabajo siguiendo CRISP-DM. Sus definiciones viven en `.github/agents/`.

```
PDF / requerimiento inicial
        ↓
01 Enrich Data Story User  →  .enriched.md + .raw.md + .evidence.md
        ↓
02 Data Governance         →  planner-input.json (gobernado) ← PASO CLAVE
        ↓
03 Planner                 →  coder-input.json
        ↓
04 Coder                   →  código SAS/Python + qa-input.json
        ↓
05 QA                      →  data-quality-input.json
        ↓
06 Data Quality            →  documentation-input.json
        ↓
07 Documentation           →  compliance-input.json
        ↓
08 Compliance / Security   →  deployment-input.json
        ↓
09 Deployment              →  monitoring-input.json
        ↓
10 Monitoring              →  final-product-evidence.json
        ↑
99 Reviewer (transversal)  —  invocable en cualquier paso, no modifica archivos
```

| # | Agente | Input | Output | Estado |
|---|---|---|---|---|
| 01 | Enrich Data Story User | PDF historia de usuario | `.enriched.md` + `.raw.md` + `.evidence.md` | ✅ Construido |
| 02 | Data Governance | `.enriched.md` | `planner-input.json` gobernado | 🔄 En proceso |
| 03 | Planner | `planner-input.json` | `coder-input.json` | 🔄 En proceso |
| 04 | Coder | `coder-input.json` | Código SAS/Python + `qa-input.json` | 🔲 Por construir |
| 05 | QA | `qa-input.json` | Reporte QA + `dq-input.json` | 🔲 Por construir |
| 06 | Data Quality | `dq-input.json` | Reglas DQ + `documentation-input.json` | 🔄 En proceso |
| 07 | Documentation | `documentation-input.json` | Docs técnica + `compliance-input.json` | 🔄 En proceso |
| 08 | Compliance / Security | `compliance-input.json` | Revisión seg. + `deployment-input.json` | 🔲 Por construir |
| 09 | Deployment | `deployment-input.json` | Pipeline + `monitoring-input.json` | 🔲 Por construir |
| 10 | Monitoring | `monitoring-input.json` | `final-product-evidence.json` | 🔲 Por construir |
| 99 | Reviewer | Cualquier artefacto | Reporte de revisión (read-only) | 🔲 Por construir |

---

## Evidencia y Calidad

### Qué evidencia queda en GitHub

| Artefacto | Ubicación | Generado por |
|---|---|---|
| Historia raw | `docs/user-stories/raw/<ID>.raw.md` | Agente 01 |
| Historia enriquecida | `docs/user-stories/enriched/<ID>.enriched.md` | Agente 01 |
| Evidencia de agente | `evidence/<agente>/<ID>.evidence.md` | Cada agente |
| Reglas DQ | `dq/rules.md` | Agente 06 |
| Diccionario de datos | `docs/data-dictionary.md` | Agente 02 |
| Documentación técnica | `docs/` | Agente 07 |
| Contratos de datos | `contracts/` | Agente 02 / 08 |
| Tests / validaciones | `tests/` | Agente 04 / 05 |
| Auto-evaluación | `scorecard/self-assessment.yml` | Equipo |

### Definition of Done

Una entrega está completa solo si tiene: historia enriquecida, código versionado, reglas DQ, documentación, evidencia en GitHub, revisión de seguridad y scorecard actualizado. Ver definición completa en [`.github/copilot-instructions.md`](.github/copilot-instructions.md).

---

## Próximos Pasos

- [ ] Enriquecer historias HU-SOFOM-002, HU-SOFOM-003 y HU-SOFOM-004 con el agente `01_enrich-data-story-user`.
- [ ] Ejecutar agente `02_data-governance` sobre HU-SOFOM-001 enriquecida.
- [ ] Ejecutar agente `03_planner` para diseñar la arquitectura Silver en SAS 9.4.
- [ ] Documentar reglas DQ iniciales en `dq/rules.md`.
- [ ] Construir capa Silver con el agente `04_coder`.
- [ ] Validar cifras de control con agentes `05_qa` y `06_data-quality`.
- [ ] Cerrar sprint con `scorecard/self-assessment.yml` actualizado y evidencia completa en `evidence/`.

---

## Inicio Rápido

1. Clonar el repositorio.
2. Revisar el contexto del proyecto en `docs/crisp-dm/01-business-understanding.md`.
3. Leer la historia de usuario enriquecida de referencia: `docs/user-stories/enriched/HU-SOFOM-001.enriched.md`.
4. Invocar el agente `01_enrich-data-story-user` para nuevas historias de usuario.
5. Seguir la cadena de agentes en orden.

Documentación completa: [`docs/`](docs/) | Instrucciones Copilot: [`.github/copilot-instructions.md`](.github/copilot-instructions.md)

---

## Contribuidores

| Integrante | Rol |
|---|---|
| Jose Antonio Esparza | Lead |
| Diego Hernández | Ingeniero de Datos |
| Gustavo Montiel | Ingeniero de Datos |
| Fernando Lopez | Ingeniero de Datos |
| Ricardo Meneses | Ingeniero de Datos |

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

## Contribuidores

- Jose Antonio Esparza
- Team SOFOM
    - Diego Hernández
    - Gustavo Montiel
    - Fernando Lopez
    - Ricardo Meneses
