# Prompt Template: Agent 02 - Data Governance

**Propósito**: Validar y enriquecer el `planner-input.json` con gobierno de datos (clasificación, PII, ownership, lineage).

**Agente**: `@02_data-governance`

**Input**: `planner-input.json` de Agent 01  
**Output**: `governance-assessment.md` + `planner-input.json` gobernado ⚠️ **CRÍTICO**

---

## 📋 Template

```markdown
@02_data-governance

Necesito validar y enriquecer el governance para este proyecto de datos:

### Información General
- **Proyecto**: [nombre del caso de uso]
- **Data Owner**: [nombre y rol]
- **Data Steward**: [nombre y rol]
- **Custodio Técnico**: [nombre y rol]

### Datos a Clasificar
[Pegar planner-input.json preliminar de Agent 01]

### Entidades y Campos
- **Entidades principales**: [ej: transacción, cliente, inventario]
- **Campos sensibles/PII identificados**: [ej: email, teléfono, coordenadas]
- **Campos confidenciales**: [ej: margen, estrategia de precios]

### Requisitos de Cumplimiento
- **Regulaciones aplicables**: [ej: LFPDPPP, CNBV, GDPR]
- **Restricciones de acceso**: [áreas que pueden acceder]
- **Retención de datos**: [cuánto tiempo guardar]

### Preguntas de Governance
1. ¿Qué datos necesitan ser enmascarados o anonimizados?
2. ¿Cuáles son los controles de acceso requeridos?
3. ¿Hay dependencias de otros productos de datos?
4. ¿Existen riesgos regulatorios especiales?

---

Por favor, valida y enriquece con:
- ✓ Clasificación de datos (público/interno/confidencial/restringido)
- ✓ Asignación de roles (Owner, Steward, Custodio)
- ✓ Inventario de PII y datos sensibles
- ✓ Controles de acceso y enmascaramiento
- ✓ Evaluación de riesgos regulatorios
- ✓ Data contracts y lineage requerido
- ✓ ⚠️ OBLIGATORIO: governance_approved = true
```

---

## ✅ Ejemplo Completo

```markdown
@02_data-governance

Necesito validar y enriquecer el governance para este proyecto de datos:

### Información General
- **Proyecto**: Optimización de Inventario
- **Data Owner**: Juan Rodríguez (Gerente Supply Chain)
- **Data Steward**: María García (Analista de Datos)
- **Custodio Técnico**: Carlos López (Ingeniero de Datos)

### Datos a Clasificar
[PLANNER_INPUT JSON]

### Entidades y Campos
- **Entidades principales**: transacción_inventario, sku_maestro, tienda
- **Campos sensibles**: ubicación_exacta, datos_cliente
- **Campos confidenciales**: margen_neto, estrategia_inventario

### Requisitos de Cumplimiento
- **Regulaciones**: CNBV (restricciones financieras)
- **Restricciones de acceso**: Solo áreas de Supply Chain y Finanzas
- **Retención**: 36 meses de histórico

### Preguntas
1. Enmascarar ubicaciones exactas excepto región
2. Acceso solo para gerentes y analistas autorizados
3. Dependencia de maestro de SKUs y tiendas
4. Riesgo bajo pero revisar exposición de márgenes
```

---

## ⚠️ Quality Gates (CRÍTICOS)

El agente DEBE validar:
- [ ] Todas las entidades clasificadas
- [ ] Data Owner y roles asignados
- [ ] Campos PII inventariados con controles
- [ ] Data contracts identificados
- [ ] Riesgos evaluados
- [ ] **`governance.governance_approved: true`**

❌ **NO se puede avanzar a Agent 03 sin**: `governance_approved: true`

---

## 📌 Next Step

Una vez governance está aprobado:
→ Pasar a **Agent 03: Planner** para generar plan técnico

**Comando siguiente**:
```
@03_planner
[Copiar outputs de Agent 02 con governance aprobado]
```

---

**Referencia**: [CLAUDE.md - Agent 02](../../CLAUDE.md#02--data-governance-agent-️-checkpoint-crítico)

**⚠️ IMPORTANTE**: Agent 02 es un **CHECKPOINT OBLIGATORIO**. Sin aprobación de governance, el caso de uso no puede avanzar.
