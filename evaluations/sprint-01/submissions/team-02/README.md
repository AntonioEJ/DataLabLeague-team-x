---

# 📌 2. `README.md`

```markdown
# 🧠 Ambiente Agéntico para Generación de Indicadores BI

## 📌 Descripción General

Este proyecto implementa un **ecosistema de agentes inteligentes** orientado a la construcción automatizada de indicadores de negocio (KPIs), desde el entendimiento del contexto hasta su implementación técnica y documentación.

El enfoque combina:

- Data Storytelling
- Planeación técnica
- Gobierno de datos
- Calidad de datos
- Desarrollo automatizado
- Documentación estructurada

---

## 🎯 Objetivo

Automatizar la creación de indicadores bajo un modelo:

- Reproducible
- Escalable
- Audit-ready
- Alineado a mejores prácticas de BI y Data Governance

---

## 🧩 Arquitectura del Sistema

El sistema está compuesto por los siguientes agentes:

| Agente | Función |
|------|--------|
| **Enrich Data Story** | Interpreta y estructura el contexto de negocio |
| **Planner** | Diseña la construcción técnica del indicador |
| **Data Governance** | Define fuentes, linaje y políticas |
| **Data Quality** | Valida la calidad de los datos |
| **Coder** | Implementa pipelines, queries y lógica |
| **Documentation** | Genera documentación técnica y funcional |

---

## 🔄 Flujo de Procesamiento

```text
1. Input (PDF / Formulario)
2. Enrich Data Story → Contexto estructurado (.md)
3. Planner → Plan técnico y KPIs
4. Data Governance → Modelo y linaje de datos
5. Data Quality → Reglas de validación
6. Coder → Implementación técnica
7. Documentation → Entregables finale.


# 📌 3.Estructura 

project/
│
├── agents/
│   ├── enrich/
│   ├── planner/
│   ├── governance/
│   ├── quality/
│   ├── coder/
│   └── documentation/
│
├── inputs/
│   ├── pdf/
│   └── forms/
│
├── outputs/
│   ├── indicators/
│   ├── code/
│   └── docs/
│
├── templates/
│   └── markdown/
│
├── config/
│   └── orchestration.yaml
│
└── README.md
