# Prompt Template: Agent 04 - Coder

**Propósito**: Implementar código, transformaciones y pipeline.

**Agente**: `@04_coder`

**Input**: `execution-plan.json` de Agent 03  
**Output**: Código implementado + `implementation-summary.md`

---

## 📋 Template

```markdown
@04_coder

Necesito implementar los componentes técnicos para:

### Proyecto
[Nombre del caso de uso]

### Plan de Ejecución
[Pegar execution-plan.json de Agent 03]

### Componentes a Implementar
1. **Ingesta de datos**: [fuentes, formato, frecuencia]
2. **Transformaciones**: [reglas de negocio, cálculos]
3. **Almacenamiento**: [bronze/silver/gold o equivalente]
4. **APIs/Outputs**: [interfaces de consumo]

### Requisitos de Código
- **Lenguaje**: Python 3.11+
- **Framework**: [Spark, Pandas, otro]
- **Configuración**: [credenciales externalizadas, logging, error handling]
- **Testing**: [cobertura mínima 80%]

### Estándares a Seguir
- PEP 8 compliance
- Type annotations completas
- Docstrings en Google style
- Configuración sin hardcoding
- Logging en lugar de print()

---

Por favor implementa:
✓ Código modular y testeable
✓ Manejo de errores explícito
✓ Documentación inline
✓ Sin exposición de credenciales
```

---

## 📌 Next Step
→ **Agent 05: QA** para testing

---

**Referencia**: [CLAUDE.md - Agent 04](../../CLAUDE.md#04--coder-agent)
