# Prompt Template: Agent 05 - QA

**Propósito**: Diseñar y ejecutar pruebas técnicas, funcionales y de regresión.

**Agente**: `@05_qa`

**Input**: Código de Agent 04  
**Output**: Tests + `test-report.md` + `coverage-report.md`

---

## 📋 Template

```markdown
@05_qa

Necesito diseñar y ejecutar pruebas para:

### Proyecto
[Nombre del caso de uso]

### Código a Probar
[Referencia al código de Agent 04]

### Escenarios de Prueba
1. **Casos positivos**: [flujos happy path]
2. **Casos negativos**: [errores esperados]
3. **Casos edge**: [límites, valores nulos, etc.]

### Criterios de Aceptación
- Cobertura mínima: 80%
- Todos los errores capturados
- Validaciones de entrada y salida
- Performance aceptable

### Ambiente de Testing
- [Base de datos: dev/test/prod]
- [Volumen de datos: muestra/completo]
- [Herramientas: pytest, spark-testing-base, etc.]

---

Por favor crea:
✓ Tests unitarios (funciones aisladas)
✓ Tests de integración (componentes interconectados)
✓ Tests de regresión (casos previos)
✓ Reporte de cobertura
```

---

## 📌 Next Step
→ **Agent 06: Data Quality** para validaciones DQ

---

**Referencia**: [CLAUDE.md - Agent 05](../../CLAUDE.md#05--qa-agent)
