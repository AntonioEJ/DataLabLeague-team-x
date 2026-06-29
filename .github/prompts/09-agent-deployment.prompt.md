# Prompt Template: Agent 09 - Deployment

**Propósito**: Preparar y documentar el despliegue a producción.

**Agente**: `@09_deployment`

**Input**: Security review de Agent 08 + Código de Agent 04  
**Output**: `deployment-plan.md` + `rollback-procedure.md` + `release-notes.md`

---

## 📋 Template

```markdown
@09_deployment

Necesito preparar el despliegue para:

### Proyecto
[Nombre del caso de uso]

### Información de Despliegue
- **Ambiente destino**: [dev/staging/prod]
- **Tipo de despliegue**: [blue-green, canary, rolling, etc.]
- **Ventana de despliegue**: [horario, duración]
- **Rollback automático**: [sí/no, condiciones]

### Componentes a Desplegar
1. [Componente 1 - ambiente, recurso, configuración]
2. [Componente 2]
3. [...]

### Pasos Pre-Despliegue
- [ ] Tests de humo ejecutados
- [ ] Backups creados
- [ ] Stakeholders notificados
- [ ] Plan de rollback listo

### Validaciones Post-Despliegue
- [ ] Servicio está online
- [ ] Métricas en rango esperado
- [ ] Sin errores críticos en logs
- [ ] Usuarios pueden acceder

### Plan de Rollback
- [Pasos para revertir]
- [Datos a restaurar]
- [Tiempo estimado]

---

Por favor genera:
✓ Plan de despliegue paso a paso
✓ Estrategia de rollback
✓ Checklist pre/post despliegue
✓ Release notes
```

---

## 📌 Next Step
→ **Agent 10: Monitoring** para configurar observabilidad

---

**Referencia**: [CLAUDE.md - Agent 09](../../CLAUDE.md#09--deployment-agent)
