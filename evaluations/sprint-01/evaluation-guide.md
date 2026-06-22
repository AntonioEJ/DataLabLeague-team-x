# Guía de Evaluación — Sprint 01

## Propósito

Esta guía describe el proceso paso a paso para evaluar los entregables del Sprint 1 de DataLab League de forma consistente, objetiva y trazable.

## Antes de Evaluar

1. Leer las rúbricas completas en `/evaluations/sprint-01/rubrics/`.
2. Obtener acceso al repositorio del equipo a evaluar.
3. Identificar la ubicación de los entregables (README.md y githubcopilot-instructions.md o equivalente).
4. Completar el archivo `evaluation-input-template.json` con los datos del equipo.
5. Verificar que el equipo haya hecho commits en su repositorio.

## Proceso de Evaluación

### Paso 1 — Recolección de evidencia

- Localizar `README.md` general del repositorio del equipo.
- Localizar `githubcopilot-instructions.md` o equivalente (`.github/copilot-instructions.md`, `GitHub-copilot-instructions.md`, etc.).
- Registrar URLs de PRs y commits relevantes.
- Completar `teams/team-XX/evidence-index.md`.

### Paso 2 — Evaluación de GitHub Copilot Instructions (40 pts)

Aplicar la rúbrica de `rubrics/githubcopilot-instructions-rubric.md`:

- A. Claridad del propósito y alcance — 5 pts
- B. Alineación con DataLab League y CRISP-DM — 6 pts
- C. Estándares de desarrollo y calidad — 7 pts
- D. Data Quality y validaciones — 6 pts
- E. Gobernanza, seguridad y cumplimiento — 6 pts
- F. Uso efectivo de agentes y artefactos — 5 pts
- G. Evidencia GitHub y Definition of Done — 5 pts

Escala por criterio: 0% / 25% / 50% / 75% / 100% del valor máximo.

### Paso 3 — Evaluación de README.md (20 pts)

Aplicar la rúbrica de `rubrics/readme-rubric.md`:

- A. Descripción ejecutiva del proyecto — 4 pts
- B. Contexto DataLab League y equipo — 3 pts
- C. Producto de datos y alcance — 4 pts
- D. Estructura del repositorio — 3 pts
- E. Metodología CRISP-DM — 3 pts
- F. Evidencia, calidad y próximos pasos — 3 pts

### Paso 4 — Cálculo del puntaje total

```
puntaje_total = puntaje_githubcopilot_instructions + puntaje_readme
```

Ver estados en `rubrics/sprint-01-total-rubric.md`.

### Paso 5 — Documentación de resultados

1. Completar `teams/team-XX/evaluation-result.json`.
2. Completar `teams/team-XX/evaluation-result.md`.
3. Escribir `teams/team-XX/feedback.md` con tono profesional y constructivo.
4. Actualizar `scoring-summary.md` con los puntajes del equipo.
5. Actualizar `sprint-01-scoreboard.md` cuando todos los equipos estén evaluados.

### Paso 6 — Commit y registro

```bash
git add evaluations/sprint-01/teams/team-XX/
git add evaluations/sprint-01/scoring-summary.md
git add evaluations/sprint-01/sprint-01-scoreboard.md
git commit -m "eval: register sprint-01 evaluation results for team-XX"
```

## Reglas del Evaluador

- No modificar los archivos del equipo evaluado.
- No inventar evidencia. Si no existe, registrar la ausencia.
- Justificar cada puntaje con referencia al contenido evaluado.
- Mantener criterios consistentes entre los tres equipos.
- Diferenciar hallazgos críticos, importantes y menores.
- Dar feedback accionable con acciones concretas.
- Tono profesional, claro y constructivo.

## Escala de Puntaje por Criterio

| Nivel | % | Descripción |
|-------|---|---|
| No cumple | 0% | No existe o es completamente irrelevante |
| Superficial | 25% | Mención mínima sin profundidad |
| Parcial | 50% | Cumple en aspectos generales pero con gaps importantes |
| Bueno | 75% | Cumple bien con oportunidades de mejora menores |
| Completo | 100% | Claro, completo y accionable |
