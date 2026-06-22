# Registro de Riesgos

Todos los riesgos identificados durante el workflow.

## Formato

```
### RSK-XXX: [Título]
- **Descripción**: [Qué puede salir mal]
- **Categoría**: técnico | datos | regulatorio | seguridad | negocio
- **Probabilidad**: alta | media | baja
- **Impacto**: alto | medio | bajo
- **Nivel**: crítico | alto | medio | bajo
- **Mitigación**: [Qué hacer para reducir probabilidad]
- **Contingencia**: [Qué hacer si ocurre]
- **Owner**: [Responsable de monitorear]
- **Agente que lo identificó**: [nombre del agente]
- **Estado**: abierto | mitigado | cerrado
```

---

### RSK-001: Ausencia de ownership de datos

- **Descripción**: Si los datos no tienen un Data Owner definido, no se pueden tomar decisiones de acceso, clasificación ni contratos.
- **Categoría**: datos / regulatorio
- **Probabilidad**: media
- **Impacto**: alto
- **Nivel**: alto
- **Mitigación**: Agent Data Governance solicita asignación de Data Owner antes de avanzar.
- **Contingencia**: Escalar a Chief Data Officer.
- **Owner**: Data Governance Lead
- **Agente que lo identificó**: 02-agent-data-governance
- **Estado**: abierto

### RSK-002: Datos PII sin controles de acceso

- **Descripción**: Exponer datos PII sin controles adecuados viola LFPDPPP y genera riesgo regulatorio.
- **Categoría**: regulatorio / seguridad
- **Probabilidad**: media
- **Impacto**: alto
- **Nivel**: crítico
- **Mitigación**: Agent Data Governance identifica PII y define controles antes de que Agent Planner diseñe la arquitectura.
- **Contingencia**: Enmascarar o pseudoanonimizar datos antes de cualquier procesamiento.
- **Owner**: Data Governance Lead + CISO
- **Agente que lo identificó**: 02-agent-data-governance
- **Estado**: abierto
