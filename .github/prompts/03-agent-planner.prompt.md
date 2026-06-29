# Prompt Template: Agent 03 - Planner

**Propósito**: Generar plan técnico-funcional y definir arquitectura.

**Agente**: `@03_planner`

**Input**: `planner-input.json` gobernado de Agent 02  
**Output**: `execution-plan.json` + `architecture-decision.md`

---

## 📋 Template

```markdown
@03_planner

Necesito generar el plan de ejecución técnico para este producto de datos:

### Proyecto
[Nombre y descripción breve del caso de uso enriquecido]

### Inputs Gobernados
[Pegar planner-input.json de Agent 02 con governance_approved: true]

### Requisitos Técnicos
- **Volumen de datos**: [ej: 100GB/mes]
- **Latencia requerida**: [ej: tiempo real, diario, semanal]
- **Usuarios finales**: [ej: 50 analistas, 100 stakeholders]
- **SLA**: [ej: 99.5% uptime]

### Arquitectura Candidata
- **Opciones**: Databricks Medallion / SAS Analytics / [otra]
- **Preferencia**: [justificar selección]
- **Restricciones**: [limitaciones técnicas o de negocio]

### Dependencias
- **Sistemas upstream**: [fuentes de datos]
- **Sistemas downstream**: [consumidores]
- **Integración requerida**: [APIs, ETLs existentes]

---

Por favor genera:
✓ Secuencia de agentes a ejecutar
✓ Arquitectura seleccionada con justificación
✓ Plan de ejecución con milestones
✓ Identificación de riesgos técnicos
```

---

## ✅ Ejemplo

```markdown
@03_planner

Necesito generar el plan de ejecución técnico para este producto de datos:

### Proyecto
Optimización de Inventario - Predicción de demanda por tienda y SKU

### Inputs Gobernados
[PLANNER_INPUT GOBERNADO]

### Requisitos Técnicos
- **Volumen**: 50GB histórico + 5GB/mes incremental
- **Latencia**: Diaria (actualización 6am)
- **Usuarios**: 200 tiendas + 30 analistas
- **SLA**: 99% uptime

### Arquitectura
- **Opción**: Databricks Medallion (ya usamos en empresa)
- **Justificación**: Familiar al equipo, integrado con Power BI existente
- **Restricciones**: Presupuesto limitado, timeline 8 semanas

### Dependencias
- **Upstream**: ERP, POS, API clima
- **Downstream**: Dashboards Power BI, API de recomendaciones
```

---

## 📌 Next Step
→ **Agent 04: Coder** para implementación

---

**Referencia**: [CLAUDE.md - Agent 03](../../CLAUDE.md#03--planner-agent)
