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

---

## Principios Fundamentales de Ingeniería de datos

Todos los productos de datos deben seguir estos principios:

### 1. Legibilidad sobre complejidad
- Preferir implementaciones explícitas y mantenibles
- Evitar abstracciones innecesarias
- Evitar over-engineering y comportamiento mágico
- El código debe ser comprensible en minutos, no horas

### 2. Mentalidad production-first
- Asumir que todo código puede ejecutarse en producción
- Incluir logging y error handling
- Ser testeable y observable
- Evitar hardcoding de paths y credenciales
- Soportar ejecución en cloud

### 3. Reproducibilidad
Cada workflow debe ser reproducible en:
- Desarrollo local
- Docker
- CI/CD
- SageMaker / Notebooks en cloud
- ECS/Fargate / Kubernetes
- Servidores de producción

### 4. Modularidad
- Separar lógica de negocio, infraestructura, acceso a datos
- Evitar monolithic scripts
- Cada componente debe tener una responsabilidad clara

---

## Estándares de Código

### Python 3.11+
Todo código debe ser compatible con Python 3.11 mínimo.

### PEP 8 - Convenciones de Nombres

| Elemento | Convención | Ejemplo |
|---|---|---|
| Módulos | `snake_case` | `data_loader.py` |
| Paquetes | `snake_case` | `etl/` |
| Clases | `PascalCase` | `DataPipeline` |
| Funciones | `snake_case` | `load_dataframe()` |
| Variables | `snake_case` | `train_df` |
| Constantes | `UPPER_SNAKE_CASE` | `MAX_RETRIES = 3` |
| Miembros privados | `_underscore` | `_internal_cache` |

### Formato de Código

- Línea máxima: **88 caracteres** (Black-compatible)
- Indentación: **4 espacios** (nunca tabs)
- Líneas en blanco:
  - 2 líneas entre definiciones top-level
  - 1 línea entre métodos en una clase
- Imports ordenados:
  1. Standard library
  2. Third-party
  3. Local/project imports
- Un import por línea
- Evitar wildcard imports (`from x import *`)

### Type Annotations (Requeridas)

```python
# ✅ Correcto
def compute_rmse(y_true: list[float], y_pred: list[float]) -> float:
    """Calcula RMSE entre valores reales y predichos."""
    pass

# ❌ Incorrecto
def compute_rmse(y_true, y_pred):
    pass
```

- Todos los parámetros y retornos deben tener type hints
- Usar `Optional[T]` o `T | None` para valores nulables
- Usar `list[T]`, `dict[K, V]`, `tuple[T, ...]` (lowercase, Python 3.9+)
- Evitar `Any` sin justificación explícita

### Docstrings (Google Style)

```python
def load_predictions(shop_id: int, date: str) -> pd.DataFrame:
    """Carga registros de predicción para tienda y fecha.

    Args:
        shop_id: Identificador único de tienda.
        date: Fecha destino en formato ISO (YYYY-MM-DD).

    Returns:
        DataFrame con registros de predicción.

    Raises:
        ValueError: Si shop_id es negativo o date está malformado.
    """
```

### Error Handling

```python
# ✅ Correcto
try:
    result = load_data(path)
except FileNotFoundError as e:
    logger.error("Data file not found: %s", path)
    raise

# ❌ Incorrecto
try:
    result = load_data(path)
except Exception:
    pass  # Silent failure
```

### Logging (No print())

```python
import logging

logger = logging.getLogger(__name__)

logger.info("Loading data from %s", file_path)
logger.warning("Missing values detected: %d rows", missing_count)
logger.error("Failed to connect to database: %s", str(e))
```

### Configuración (No hardcoding)

```python
# ✅ Correcto
DB_HOST = os.environ["DB_HOST"]
DB_PASSWORD = os.environ.get("DB_PASSWORD", "default_safe_value")

# ❌ Incorrecto
DB_HOST = "localhost"
DB_PASSWORD = "admin123"
```

### Testing con pytest

- Usar `pytest` para todos los tests
- Archivos: `test_<module>.py`
- Funciones: `test_<comportamiento>()`
- Usar fixtures sobre setup/teardown
- Mock de dependencias externas (DB, S3, APIs)

---

## Criterios de Calidad de Código

Todo código generado o revisado debe cumplir estos 10 criterios:

1. **PEP 8 compliance** — naming, formatting, imports, line length
2. **Type annotations** — presence and correctness
3. **Docstrings** — completeness and style
4. **Error handling** — specificity, logging, no silent failures
5. **Logging** — correct use of `logging` module, appropriate levels
6. **Configuration** — no hardcoded secrets, paths, or credentials
7. **Security** — OWASP Top 10 awareness (injection, secrets exposure, etc.)
8. **Modularity** — separation of concerns, no monolithic logic
9. **Testability** — functions are testable, side effects are isolated
10. **Reproducibility** — no environment-specific assumptions

---

## Agentes Especializados

Para tareas específicas invoca los agentes disponibles en `.github/agents/`:

- **00_enrich-data-story-user** — Enriquecer historias de usuario de datos
- **01_planner** — Planificación y estructuración de casos de uso
- **02_data-quality** — Reglas DQ y validación de datos
- **03_coder** — Implementación de código
- **04_qa** — Pruebas y aseguramiento de calidad
- **05_documentation** — Generación de documentación
- **06_compliance-security** — Cumplimiento y seguridad
- **07_pipeline** — Orquestación de pipelines
- **08_observability** — Logging, métricas y monitoreo
- **09_reviewer** — Revisión de código (read-only)
