# Prompt Template: Agent 01 - Enrich Data Story User

**Propósito**: Enriquecer un caso de uso de negocio en una historia de usuario de datos estructurada.

**Agente**: `@enrich-data-story-user`

**Input**: Caso de uso ambiguo o parcialmente definido  
**Output**: `data-story-enriched.md` + `planner-input.json` preliminar

---

## 📋 Template

```markdown
@enrich-data-story-user

Necesito enriquecer este caso de uso de datos:

### Caso de Uso
[DESCRIPCIÓN DEL CASO DE USO - contexto y objetivo de negocio]

### Información Disponible
- **Área de negocio**: [área o departamento]
- **Stakeholder principal**: [propietario del caso]
- **Problema a resolver**: [qué problema específico soluciona]
- **Impacto esperado**: [beneficio cuantificable]

### Preguntas Clave
- ¿Cuál es el KPI principal que queremos mejorar?
- ¿Cuáles son las fuentes de datos principales?
- ¿Cuál es la granularidad de datos necesaria (por tienda, por fecha, etc.)?
- ¿Cuáles son los criterios de aceptación?

### Contexto Adicional
[Cualquier información adicional relevante - restricciones, dependencias, etc.]

---

Por favor, enriquece este caso de uso conectando:
- Necesidad de negocio
- KPIs y decisiones
- Fuentes de datos requeridas
- Reglas de calidad de datos
- Criterios de aceptación
- Evidencia esperada
```

---

## ✅ Ejemplo Completo

```markdown
@enrich-data-story-user

Necesito enriquecer este caso de uso de datos:

### Caso de Uso
Optimizar el nivel de inventario en tiendas para minimizar pérdida por vencimiento y mejorar disponibilidad de productos.

### Información Disponible
- **Área de negocio**: Supply Chain
- **Stakeholder principal**: Gerente de Inventario
- **Problema a resolver**: Actualmente hay 15% de pérdida por vencimiento y 8% de desabastecimiento
- **Impacto esperado**: Reducir pérdida a <5% e incrementar disponibilidad a >95%

### Preguntas Clave
- KPI principal: % de pérdida por vencimiento
- Fuentes: ERP (movimientos de inventario), POS (ventas), clima (por tienda)
- Granularidad: Diaria por SKU por tienda
- Criterios: Predicción con MAPE <10%

### Contexto Adicional
- 150 tiendas activas
- 50,000 SKUs
- Datos históricos: 24 meses
```

---

## 🔍 Qué Esperar como Output

El agente retornará:
- ✓ `data-story-enriched.md` — Historia de usuario estructurada
- ✓ `planner-input.json` — Documento preliminar listo para Agent 02 (Data Governance)
- ✓ Matriz KPI-Decisión-Fuentes
- ✓ Criterios de aceptación explícitos

---

## 📌 Next Step

Una vez enriquecida la historia de usuario:
→ Pasar a **Agent 02: Data Governance** para validación y clasificación

**Comando siguiente**:
```
@02_data-governance
[Copiar outputs de Agent 01]
```

---

**Referencia**: [CLAUDE.md - Agent 01](../../CLAUDE.md#01--enrich-data-story-user-agent)
