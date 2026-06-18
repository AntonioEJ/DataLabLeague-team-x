# Contracts - Data Lab League

## ¿Qué es esta carpeta?

`/contracts/` es el directorio central para administrar todos los contratos del producto de datos: contratos de datos, contratos funcionales, contratos técnicos, contratos de interfaces, reglas de calidad, SLA/SLO, acuerdos de consumo y evidencias de gobierno.

Los contratos son artefactos de primera clase en el ciclo de vida del producto de datos. Viven aquí, al mismo nivel que `docs/`, `src/`, `tests/` y `dq/`, porque representan los compromisos formales que gobiernan la creación, transformación y entrega de datos.

---

## Tipos de Contratos

| Tipo | Descripción | Subcarpeta |
|---|---|---|
| **Data Product Contract** | Define el producto de datos completo: fuentes, campos, reglas, SLA, consumidores | `data-products/` |
| **Data Quality Contract** | Reglas DQ por dimensión: completitud, validez, unicidad, puntualidad | `quality/` |
| **Interface Contract** | Acuerdo de entrega entre proveedor y consumidor: formato, esquema, frecuencia | `interfaces/` |
| **SLA/SLO Contract** | Compromisos de disponibilidad, latencia, frescura y recuperación | `slas/` |
| **Governance Contract** | Clasificación de datos, PII, privacidad, roles de acceso, retención | `governance/` |

---

## Estructura de la Carpeta

```
contracts/
├── README.md               ← Este archivo
├── contracts.md            ← Índice maestro de todos los contratos
├── data-products/          ← Contratos de productos de datos
│   └── README.md
├── schemas/                ← Contratos de esquemas y modelos
│   └── README.md
├── quality/                ← Contratos de calidad de datos
│   └── README.md
├── interfaces/             ← Contratos de interfaces entre sistemas
│   └── README.md
├── slas/                   ← Contratos de SLA/SLO
│   └── README.md
├── governance/             ← Contratos de gobierno y cumplimiento
│   └── README.md
├── templates/              ← Templates reutilizables para cada tipo
│   └── README.md
└── examples/               ← Ejemplos de contratos completos
    └── README.md
```

---

## Convención de Nombres

| Tipo de Contrato | Patrón | Ejemplo |
|---|---|---|
| Data Product | `[nombre-producto].contract.md` | `cartera-comercial.contract.md` |
| Data Quality | `[nombre-producto].quality-contract.md` | `cartera-comercial.quality-contract.md` |
| Interface | `[origen]-to-[producto].interface-contract.md` | `sap-to-cartera-comercial.interface-contract.md` |
| SLA/SLO | `[nombre-producto].sla-slo.md` | `cartera-comercial.sla-slo.md` |
| Governance | `[nombre-producto].governance-contract.md` | `cartera-comercial.governance-contract.md` |
| Schema | `[nombre-entidad].schema-contract.md` | `cliente.schema-contract.md` |

---

## ¿Cuándo se debe crear un contrato?

Crea o actualiza un contrato cuando:

- Se define un nuevo producto de datos
- Se agrega una nueva fuente de datos
- Se modifica un esquema de salida
- Cambian los consumidores o sus requisitos
- Se define o cambia un SLA/SLO
- Se clasifican datos sensibles o PII
- Se definen o modifican reglas de calidad
- Se establece una interfaz con un sistema externo
- Se lleva el producto a producción

---

## ¿Quién debe aprobar un contrato?

| Tipo | Aprobaciones Requeridas |
|---|---|
| Data Product | Owner de Negocio + Arquitecto de Datos |
| Data Quality | Data Engineer + Data Steward |
| Interface | Proveedor + Consumidor + Arquitecto |
| SLA/SLO | Owner de Negocio + Ops + Engineering |
| Governance | Data Governance Lead + Compliance + Legal (si aplica) |

---

## Relación con CRISP-DM

| Fase CRISP-DM | Contrato Relevante |
|---|---|
| **Business Understanding** | Data Product Contract (alcance, objetivo, KPI) |
| **Data Understanding** | Interface Contract + Schema Contract |
| **Data Preparation** | Data Quality Contract |
| **Modeling/Transformation** | Data Product Contract (reglas de negocio) |
| **Evaluation** | Data Quality Contract (criterios de aceptación) |
| **Deployment** | SLA/SLO Contract + Governance Contract |

---

## Relación con Data Quality

Las reglas en `/dq/rules.md` deben estar formalmente declaradas en un `quality-contract.md`. El contrato es el artefacto auditable y versionado; `dq/` contiene la implementación.

- Cada dimensión DQ (completitud, validez, unicidad, etc.) tiene una regla en el contrato
- El contrato define los umbrales aceptables
- Los tests en `/tests/` validan que la implementación cumple el contrato

---

## Relación con Gobierno, Seguridad y Cumplimiento

- Los `governance-contract.md` documentan clasificación de datos, PII y controles de acceso
- Se integran con `evidence/governance.md` para trazabilidad
- Toda clasificación PII o dato sensible debe tener governance contract antes de ir a producción
- Las restricciones de retención y auditoría son vinculantes

---

## Cómo se revisan en Pull Requests

Al enviar un PR que toque datos, esquemas, pipelines o reglas de negocio:

1. Verificar el checklist de contratos en el PR template
2. El revisor técnico valida consistencia entre contrato y código
3. El owner de negocio debe aprobar cambios al contrato de producto de datos
4. La aprobación queda evidenciada en el PR

---

## Qué evidencia debe quedar en GitHub

- PR con descripción que mencione el contrato afectado
- Commit con referencia al contrato actualizado
- Review aprobado por owner de negocio y técnico
- Link en `evidence/governance.md` hacia el PR

---

## Definition of Done para Contratos

Un contrato está completo cuando:

- [ ] Contrato creado o actualizado con nombre convencional
- [ ] Owner de negocio definido
- [ ] Owner técnico definido
- [ ] Consumidores documentados (quién usa los datos)
- [ ] Fuentes definidas (de dónde vienen los datos)
- [ ] Grano definido (qué representa una fila)
- [ ] Campos de salida documentados
- [ ] Reglas de negocio documentadas
- [ ] Reglas de calidad documentadas con umbrales
- [ ] SLA/SLO definido (disponibilidad, frescura, latencia)
- [ ] Clasificación de datos definida (PII, Confidencial, etc.)
- [ ] Controles de seguridad y privacidad definidos
- [ ] Lineage documentado (source → transformaciones → output)
- [ ] Criterios de aceptación definidos y verificables
- [ ] Aprobación de negocio registrada (PR o firma)
- [ ] Aprobación técnica registrada (PR review)
- [ ] Evidencia en Pull Request

---

**Mantenedor**: Data Lab League Team
**Última actualización**: 2026-06-18
