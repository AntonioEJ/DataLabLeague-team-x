# Glosario

Términos del dominio de negocio, datos y tecnología usados en este producto de datos.

## Formato

```
**[Término]**: [Definición clara y concisa]. Sinónimos: [si aplica].
```

---

**Agent Workflow**: Cadena de agentes IA especializados que trabajan secuencialmente para producir un producto de datos gobernado, medible y trazable.

**Artefacto**: Cualquier archivo estructurado (JSON, Markdown) producido por un agente como input u output de la cadena.

**CRISP-DM**: Cross-Industry Standard Process for Data Mining. Metodología base del workflow con 7 fases: Business Understanding, Data Understanding, Data Preparation, Modeling, Evaluation, Deployment, Monitoring.

**Data Contract**: Acuerdo formal entre productor y consumidor de datos que define esquema, calidad, frecuencia y SLAs.

**Data Governance**: Conjunto de políticas, procesos y responsabilidades para asegurar la disponibilidad, usabilidad, integridad y seguridad de los datos.

**Data Owner**: Persona responsable de los datos desde el punto de vista de negocio. Define quién puede acceder y para qué.

**Data Steward**: Persona responsable de la calidad, catalogación y cumplimiento de políticas de datos.

**Handoff**: Transferencia formal de control entre un agente y el siguiente, mediante artefactos JSON y Markdown con quality gate.

**PII (Personally Identifiable Information)**: Información que puede identificar directa o indirectamente a una persona natural (nombre, RFC, CURP, NSS, dirección, etc.).

**planner-input.json**: Artefacto principal de la cadena. Lo genera Agente 01 (preliminar), lo valida Agente 02 (gobernado) y lo consume Agente 03 (Planner).

**Quality Gate**: Criterio binario (pass/fail) que debe cumplirse antes de que un agente haga handoff al siguiente.
