# Prompt Template: Agent 07 - Documentation

**Propósito**: Generar documentación funcional, técnica y lineage.

**Agente**: `@07_documentation`

**Input**: Código de Agent 04 + Tests de Agent 05 + DQ de Agent 06  
**Output**: README + `data-dictionary.md` + `lineage-diagram.md` + `operations-guide.md`

---

## 📋 Template

```markdown
@07_documentation

Necesito generar documentación para:

### Proyecto
[Nombre del caso de uso]

### Componentes a Documentar
1. **README**: [descripción, setup, cómo usar]
2. **Data Dictionary**: [entidades, campos, tipos, descripciones]
3. **Lineage**: [flujo de datos, transformaciones]
4. **Operations**: [cómo monitorear, troubleshoot, maintener]

### Audiencia
- **Usuarios finales**: [analistas, stakeholders]
- **Operadores**: [SREs, devops]
- **Desarrolladores**: [futuros contribuyentes]

### Elementos Obligatorios
- Descripción del caso de uso
- Arquitectura de alto nivel
- Instrucciones de setup
- Ejemplos de uso
- Guía de troubleshooting
- Contacto/owner del proyecto

---

Por favor genera:
✓ Documentación clara y accesible
✓ Ejemplos de uso
✓ Diagramas de lineage
✓ Guía operacional
```

---

## 📌 Next Step
→ **Agent 08: Compliance & Security** para revisión

---

**Referencia**: [CLAUDE.md - Agent 07](../../CLAUDE.md#07--documentation-agent)
