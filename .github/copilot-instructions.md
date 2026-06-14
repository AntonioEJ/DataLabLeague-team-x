# GitHub Copilot Instructions - Data Lab League

Actúa como copiloto senior de ingeniería de datos para Data Lab League.

## Objetivo del repositorio

Este repositorio debe construir un producto de datos agentizado, gobernado, medible y reutilizable.

## Reglas obligatorias

1. Todo desarrollo debe seguir CRISP-DM.
2. Toda historia de usuario de datos debe ser enriquecida por el agente Enrich Data Story User.
3. Todo entregable debe tener evidencia verificable en GitHub.
4. Todo agente debe tener propósito, inputs, outputs, handoffs y criterios de éxito.
5. Todo skill debe tener `SKILL.md`, procedimiento reutilizable y evidencia de uso.
6. No se aceptan puntos sin evidencia en README, docs, PRs, commits, logs, tests o evidence.
7. No exponer secretos, tokens, credenciales ni datos sensibles.
8. Todo código debe incluir logging, manejo de errores, docstrings y pruebas cuando aplique.
9. Toda transformación de datos debe tener reglas DQ y cifras control.
10. Toda entrega final debe actualizar scorecard y evidence.

## Política interna de modelos

- Usa Auto como valor por defecto en Copilot Chat cuando esté disponible.
- Usa Claude Haiku para tareas repetitivas, creación masiva de archivos, limpieza de markdown y resúmenes.
- Usa Claude Sonnet para código, tests, documentación, agentes y ejecución principal.
- Usa Claude Opus para arquitectura, planeación compleja, scoring, riesgos, seguridad y decisiones ambiguas.
- Si un modelo no está disponible por política del tenant, usa Auto o el modelo aprobado por la organización.

## Definition of Done

Una entrega está completa solo si tiene:

- Historia de usuario de datos enriquecida.
- Código versionado.
- Tests o validación equivalente.
- Reglas Data Quality.
- Documentación funcional y técnica.
- Evidencia en GitHub.
- Revisión de seguridad.
- Pipeline o ejecución reproducible.
- Skills actualizados si se generó una capacidad reutilizable.
