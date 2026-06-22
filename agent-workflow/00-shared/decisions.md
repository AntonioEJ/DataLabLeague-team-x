# Decisiones

Registro de decisiones arquitectónicas, de negocio y de gobierno tomadas durante el workflow.

## Formato

```
### DEC-XXX: [Título]
- **Fecha**: YYYY-MM-DD
- **Tomada por**: [Persona o agente]
- **Contexto**: [Por qué era necesario decidir]
- **Decisión**: [Qué se decidió]
- **Alternativas consideradas**: [Qué más se evaluó]
- **Consecuencias**: [Impacto de la decisión]
- **Estado**: vigente | revisada | revertida
```

---

### DEC-001: CRISP-DM como metodología base del workflow

- **Fecha**: 2026-06-22
- **Tomada por**: Data Architecture Lead
- **Contexto**: Se requería una metodología estándar para organizar el trabajo de los agentes de IA.
- **Decisión**: Usar CRISP-DM como framework de referencia para todas las fases del workflow.
- **Alternativas consideradas**: TDSP (Microsoft), KDD, proceso ad-hoc.
- **Consecuencias**: Todos los artefactos referencian la fase CRISP-DM. Los agentes están alineados a fases específicas.
- **Estado**: vigente

### DEC-002: Agent Data Governance como paso obligatorio antes de Planner

- **Fecha**: 2026-06-22
- **Tomada por**: Data Governance Lead
- **Contexto**: Se detectó que sin revisión de gobierno antes de la planificación técnica, los productos de datos llegaban a producción sin clasificación de datos, sin ownership claro y sin controles de PII.
- **Decisión**: Insertar Agent Data Governance como paso 02, entre Enrich Data Story User y Agent Planner.
- **Alternativas consideradas**: Governance al final del ciclo, governance como revisión paralela.
- **Consecuencias**: Agent Planner recibe un `planner-input.json` gobernado y validado. Aumenta el tiempo inicial del ciclo pero reduce riesgos regulatorios.
- **Estado**: vigente
