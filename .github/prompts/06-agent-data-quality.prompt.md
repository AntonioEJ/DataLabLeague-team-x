# Prompt Template: Agent 06 - Data Quality

**Propósito**: Definir y validar reglas de calidad de datos.

**Agente**: `@06_data-quality`

**Input**: `execution-plan.json` + Clasificación de datos de Agent 02  
**Output**: `dq-rules.json` + `validation-schema.json` + `quality-dashboard-spec.md`

---

## 📋 Template

```markdown
@06_data-quality

Necesito definir reglas de calidad de datos para:

### Proyecto
[Nombre del caso de uso]

### Datos a Validar
[Entidades y campos clave del planner-input.json]

### Criterios de Calidad
1. **Completitud**: [% mínimo de registros no nulos]
2. **Precisión**: [rangos válidos, formato, tipos]
3. **Consistencia**: [reglas de negocio, lógica]
4. **Unicidad**: [campos que no deben duplicarse]
5. **Validez temporal**: [campos de fecha, time series]

### Cifras de Control
- **Conteo de registros**: [baseline esperado]
- **Suma de importes**: [validación de totales]
- **Máximo/mínimo**: [límites esperados]
- **Valores únicos**: [cardinalidad esperada]

### Dashboard de Monitoreo
- Métricas clave: [% completitud, % válidos, etc.]
- Frecuencia de chequeo: [diaria, horaria, etc.]
- Alertas: [condiciones de disparo]

---

Por favor genera:
✓ Reglas DQ documentadas
✓ Esquema de validación
✓ Cifras de control baselines
✓ Especificación de dashboard
```

---

## 📌 Next Step
→ **Agent 07: Documentation** para documentar

---

**Referencia**: [CLAUDE.md - Agent 06](../../CLAUDE.md#06--data-quality-agent)
