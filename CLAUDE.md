# Claude Configuration

Configuración de Claude y prompts para el proyecto DataLabLeague.

## Agentes Disponibles (00-09)

### Core Agents (Cadena de Valor CRISP-DM)

- **00_enrich-data-story-user** — Entrada inicial para enriquecer historias de usuario
- **01_planner** — Planificación y estructuración de casos de uso
- **02_data-quality** — Calidad de datos y validación
- **03_coder** — Implementación de código
- **04_qa** — Pruebas y aseguramiento de calidad
- **05_documentation** — Generación de documentación
- **06_compliance-security** — Cumplimiento y seguridad
- **07_pipeline** — Orquestación de pipelines
- **08_observability** — Logging, métricas y monitoreo

### Complementary Agent

- **09_reviewer** — Análisis y revisión de código (read-only)

## Skills Disponibles

- Data Story User Enrichment
- CRISP-DM Use Case Discovery
- Data Quality Rule Authoring
- Evidence Packager
- Pipeline Quality Gates
- Documentation Packager

## Guía de Uso

Para invocar un agente o skill:

1. Especifica el nombre del agente/skill en tu prompt
2. Proporciona contexto sobre qué necesitas (código, análisis, documentación, etc.)
3. El agente seguirá su configuración en `.claude/agents/*.agent.md` o `.claude/skills/*/SKILL.md`

## Entrypoint

Comienza siempre con **00_enrich-data-story-user** para enriquecer la entrada del usuario antes de pasar a otros agentes especializados.

---

**Nota**: Todos los agentes están configurados en `.claude/agents/` y sincronizados con `.github/agents/` para coherencia con GitHub Copilot.
