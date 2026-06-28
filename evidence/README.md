# Evidence Package — Presentación y Evaluación

## Propósito

Esta carpeta contiene la **evidencia consolidada** del proyecto DataLab League para:
- **Presentación** ante jurados y stakeholders
- **Evaluación** de competencias y resultados
- **Demostración** de cumplimiento y calidad
- **Entrega final** del proyecto

> **Nota**: Para tracking operativo del workflow de agentes, ver [`agent-workflow/evidence/`](../agent-workflow/evidence/)

---

## Contenido

### 1. Data Story
Narrativa del proyecto enriquecida con datos y contexto.

### 2. Skills
Demostración de skills y competencias aplicadas.

### 3. Testing
Evidencia de testing y validación de calidad.

### 4. Data Quality
Reportes y métricas de calidad de datos.

### 5. Governance
Políticas, estándares y cumplimiento implementado.

### 6. Demo
Demostración funcional del proyecto.

## Estructura

```
evidence/
├── data-story.md

## Contribuidores

- Jose Antonio Esparza
├── skills.md
├── testing.md
├── data-quality.md
├── governance.md
├── demo.md
├── courses/
│   ├── course-1.md
│   └── course-2.md
└── skills/
    ├── skill-1.md
    └── skill-2.md
```

## Relación con Agent Workflow

Esta evidencia se alimenta del proceso documentado en:

```
agent-workflow/
├── 01-enrich.../evidence/     ─┐
├── 02-governance.../evidence/  │
├── 03-planner.../evidence/     │  Evidencia granular
├── ...                         ├─ por agente
├── 10-monitoring.../evidence/ ─┘
└── evidence/                    
    └── evidence-index.md  ← Índice operativo
                ↓
        Consolidan y resumen
                ↓
         evidence/ (raíz)  ← Presentación final
```

## Uso

Este paquete se genera automáticamente mediante el Evidence Packager skill
y se actualiza continuamente durante el proyecto.

## Validación

Cada documento incluye:
- [ ] Fecha de generación
- [ ] Versión
- [ ] Checksum de integridad
- [ ] Aprobaciones requeridas
- [ ] Referencias a evidencia

## Entrega

La evidencia se empaqueta en:
- Formato HTML para visualización
- Formato PDF para archivo
- Formato ZIP para distribución
- Repositorio de versiones
