# Evidencia Global — Tracking Operativo

## Propósito

Esta carpeta contiene el **índice operativo** del workflow de agentes:
- **Tracking** de ejecución de cada agente (EVD-001 a EVD-010)
- **Estado** de fases CRISP-DM
- **Referencias** a commits, PRs, outputs de cada agente
- **Cierre de ciclo** con `final-product-evidence.json`

> **Nota**: Para evidencia consolidada de presentación/evaluación, ver [`/evidence/`](../../evidence/)

---

## Flujo de Evidencia

```
Agentes individuales
├── 01-enrich.../evidence/     → outputs, decisiones, handoffs
├── 02-governance.../evidence/ → aprobaciones, clasificación
├── 03-planner.../evidence/    → plan técnico, ADRs
├── ...
└── 10-monitoring.../evidence/ → final-product-evidence.json
          ↓
    Se registran en
          ↓
  evidence-index.md (este directorio)
          ↓
    Se consolidan en
          ↓
  /evidence/ (raíz) → Presentación final
```

---

## Índice de Evidencia

Ver [evidence-index.md](evidence-index.md) para el registro completo de:
- Evidencia por agente
- Estado de fases CRISP-DM
- Último cierre de ciclo
- Referencias a commits/PRs
