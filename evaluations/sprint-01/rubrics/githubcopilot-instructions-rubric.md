# Rúbrica — GitHub Copilot Instructions

**Entregable**: `githubcopilot-instructions.md` o equivalente (`.github/copilot-instructions.md`, `GitHub-copilot-instructions.md`, `.github/instructions/githubcopilot-instructions.md`)  
**Valor total**: 40 puntos  
**Sprint**: Sprint 01

---

## Escala de Evaluación

| Nivel | % | Descripción |
|-------|---|---|
| No cumple | 0% | No existe o no cumple en absoluto |
| Superficial | 25% | Mención mínima sin profundidad |
| Parcial | 50% | Cumple en aspectos generales con gaps importantes |
| Bueno | 75% | Cumple bien, con oportunidades menores |
| Completo | 100% | Claro, completo y accionable |

---

## A. Claridad del propósito y alcance — 5 puntos

El archivo establece de forma clara para qué existe, qué contexto tiene el repositorio y qué se espera de GitHub Copilot.

### Indicadores

| Indicador | Descripción |
|-----------|---|
| Propósito definido | Define claramente para qué existe el archivo |
| Contexto del repositorio | Explica el contexto del repositorio (tipo de proyecto, tecnologías, equipo) |
| Tipo de producto de datos | Indica el tipo de producto de datos que se construye |
| Delimitación de Copilot | Delimita qué debe y qué no debe hacer Copilot |

### Puntaje A

| Nivel | % | Puntos |
|-------|---|--------|
| No cumple | 0% | 0.00 |
| Superficial | 25% | 1.25 |
| Parcial | 50% | 2.50 |
| Bueno | 75% | 3.75 |
| Completo | 100% | 5.00 |

---

## B. Alineación con DataLab League y CRISP-DM — 6 puntos

El archivo conecta el trabajo del equipo con la dinámica de la competencia y con la metodología CRISP-DM.

### Indicadores

| Indicador | Descripción |
|-----------|---|
| DataLab League | Menciona la dinámica DataLab League y la competencia |
| Flujo por agentes | Explica el flujo de trabajo por agentes (enrich → governance → planner → ...) |
| CRISP-DM | Alinea el trabajo con CRISP-DM como metodología |
| Fases CRISP-DM | Distingue fases relevantes: Business Understanding, Data Understanding, Data Preparation, Evaluation, Deployment, Monitoring |

### Puntaje B

| Nivel | % | Puntos |
|-------|---|--------|
| No cumple | 0% | 0.00 |
| Superficial | 25% | 1.50 |
| Parcial | 50% | 3.00 |
| Bueno | 75% | 4.50 |
| Completo | 100% | 6.00 |

---

## C. Estándares de desarrollo y calidad — 7 puntos

El archivo define buenas prácticas de desarrollo que Copilot debe seguir al generar código.

### Indicadores

| Indicador | Descripción |
|-----------|---|
| Buenas prácticas de código | PEP 8, naming conventions, estructura de módulos, etc. |
| Testing | Menciona testing con pytest u equivalente |
| Linters / formatters | Menciona Black, flake8, isort, mypy u equivalente |
| Docstrings / documentación técnica | Solicita docstrings Google-style u otro estándar |
| Mantenibilidad | Incluye criterios de mantenibilidad |
| Modularidad y reusabilidad | Solicita separación de concerns y reusabilidad |

### Puntaje C

| Nivel | % | Puntos |
|-------|---|--------|
| No cumple | 0% | 0.00 |
| Superficial | 25% | 1.75 |
| Parcial | 50% | 3.50 |
| Bueno | 75% | 5.25 |
| Completo | 100% | 7.00 |

---

## D. Data Quality y validaciones — 6 puntos

El archivo define expectativas de calidad de datos que deben guiar el trabajo de Copilot.

### Indicadores

| Indicador | Descripción |
|-----------|---|
| Reglas de calidad | Incluye reglas de calidad de datos |
| Dimensiones de calidad | Menciona completitud, unicidad, validez, consistencia, frescura o reconciliación |
| Pruebas de datos | Define expectativas de pruebas de datos (Great Expectations, dbt tests, etc.) |
| Evidencia de validaciones | Solicita evidencia de validaciones ejecutadas |

### Puntaje D

| Nivel | % | Puntos |
|-------|---|--------|
| No cumple | 0% | 0.00 |
| Superficial | 25% | 1.50 |
| Parcial | 50% | 3.00 |
| Bueno | 75% | 4.50 |
| Completo | 100% | 6.00 |

---

## E. Gobernanza, seguridad y cumplimiento — 6 puntos

El archivo incluye prácticas de gobernanza y seguridad aplicables al sector financiero o de datos personales.

### Indicadores

| Indicador | Descripción |
|-----------|---|
| Datos sensibles | Incluye control de datos sensibles |
| PII / privacidad | Incluye PII o privacidad cuando aplique (LFPDPPP) |
| Manejo de secretos | Incluye manejo de secretos, API keys, credenciales |
| Trazabilidad | Incluye trazabilidad y lineage |
| Control de accesos | Incluye principio de mínimo privilegio o controles de acceso |
| Sector financiero | Incluye principios relevantes para sector financiero (CNBV u otro) |

### Puntaje E

| Nivel | % | Puntos |
|-------|---|--------|
| No cumple | 0% | 0.00 |
| Superficial | 25% | 1.50 |
| Parcial | 50% | 3.00 |
| Bueno | 75% | 4.50 |
| Completo | 100% | 6.00 |

---

## F. Uso efectivo de agentes y artefactos — 5 puntos

El archivo describe cómo Copilot debe interactuar con la cadena de agentes y los artefactos del repositorio.

### Indicadores

| Indicador | Descripción |
|-----------|---|
| Interacción con agentes | Describe cómo Copilot debe interactuar con agentes |
| Referencia a `.github/agents/` | Hace referencia a la carpeta de agentes GitHub Copilot |
| Referencia a `/agent-workflow/` | Hace referencia a la carpeta operativa de la cadena |
| Inputs, outputs y handoffs | Explica la estructura de inputs, outputs y handoffs |
| Encadenamiento | Refuerza que el output de un agente alimenta al siguiente |

### Puntaje F

| Nivel | % | Puntos |
|-------|---|--------|
| No cumple | 0% | 0.00 |
| Superficial | 25% | 1.25 |
| Parcial | 50% | 2.50 |
| Bueno | 75% | 3.75 |
| Completo | 100% | 5.00 |

---

## G. Evidencia GitHub y Definition of Done — 5 puntos

El archivo define criterios de finalización y evidencia verificable en GitHub.

### Indicadores

| Indicador | Descripción |
|-----------|---|
| Evidencia esperada | Define evidencia esperada en commits, PRs o archivos |
| Definition of Done | Incluye criterios de DoD claros |
| Actualización de artefactos | Solicita actualización de README, documentación, pruebas o contratos |
| Verificabilidad | Es verificable y accionable |

### Puntaje G

| Nivel | % | Puntos |
|-------|---|--------|
| No cumple | 0% | 0.00 |
| Superficial | 25% | 1.25 |
| Parcial | 50% | 2.50 |
| Bueno | 75% | 3.75 |
| Completo | 100% | 5.00 |

---

## Hoja de Puntaje

| Criterio | Valor máx | Nivel asignado | % | Puntos obtenidos |
|----------|-----------|----------------|---|-----------------|
| A. Claridad del propósito y alcance | 5 | — | — | 0 |
| B. Alineación DataLab League / CRISP-DM | 6 | — | — | 0 |
| C. Estándares de desarrollo y calidad | 7 | — | — | 0 |
| D. Data Quality y validaciones | 6 | — | — | 0 |
| E. Gobernanza, seguridad y cumplimiento | 6 | — | — | 0 |
| F. Uso efectivo de agentes y artefactos | 5 | — | — | 0 |
| G. Evidencia GitHub y Definition of Done | 5 | — | — | 0 |
| **TOTAL** | **40** | | | **0** |
