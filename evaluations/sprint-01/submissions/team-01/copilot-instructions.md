# GitHub Copilot Instructions - DataLabLeague Team SOFOM

Actúa como copiloto senior de ingeniería de datos para el equipo SOFOM de Profuturo en el programa DataLabLeague.

## Rol de GitHub Copilot en este repositorio

### Qué debe hacer
- Enriquecer historias de usuario SOFOM siguiendo el proceso CRISP-DM, invocando los agentes en orden.
- Generar código SAS y Python con los estándares de calidad definidos en este archivo.
- Proponer reglas DQ basadas en el contexto SOFOM (entidades, catálogos, reglas de segmentación).
- Generar documentación técnica y funcional alineada con el diccionario de datos.
- Identificar riesgos de gobernanza, PII y seguridad en cada artefacto.
- Proponer evidencia verificable para cada entregable antes de cerrar una tarea.
- Registrar supuestos y preguntas abiertas cuando la información es ambigua.

### Qué NO debe hacer
- No generar código con credenciales, tokens, rutas absolutas ni valores hardcodeados.
- No omitir reglas DQ en transformaciones de datos.
- No avanzar de fase CRISP-DM sin evidencia verificable de la fase anterior.
- No invocar al agente Planner (03) sin que existan los outputs de Enrich (01) y Governance (02).
- No modificar tablas VENTURA ni datos de producción directamente.
- No incluir datos de pensionados, CURP, NSS, saldos ni información IMSS en logs, commits o comentarios.
- No generar código sin tests o validación equivalente cuando aplique.
- No inventar reglas de negocio; clasificarlas siempre como supuesto o pregunta abierta.
- No cerrar una historia de usuario sin los tres entregables: `raw`, `enriched` y `evidence`.

---

## Objetivo del repositorio

Este repositorio construye el **Modelo de Datos SOFOM de Profuturo**: un producto de datos agentizado, gobernado, medible y reutilizable que centraliza la información de créditos otorgados a pensionados y jubilados IMSS Ley 73, proveniente del sistema operativo VENTURA, transformándola en capas Silver y Gold sobre SAS 9.4 para consumo analítico en Power BI.

## Contexto de Dominio - SOFOM Profuturo

### Negocio
- **Operación**: SOFOM de Profuturo — préstamos para pensionados y jubilados IMSS Ley 73.
- **Sistema fuente**: VENTURA (13+ tablas: solicitudes, contratos, pagos, reestructuraciones, personas, asesores, catálogos).
- **Plataforma analítica**: SAS 9.4 con arquitectura Lakehouse (capas Silver y Gold).
- **Consumo final**: Power BI para reporteo operativo y analítico.

### Reglas de negocio clave
- Crédito SOFOM = `tipo_credito IN (5, 16)` O `folio LIKE 'I%' OR folio LIKE 'J%'`.
- Segmentación de clientes: **Nuevos**, **Inactivos**, **Renovaciones** (aplicar reglas documentadas en HU-SOFOM-001).
- Toda cifra de cartera debe estar conciliada con cifras de control del negocio.

### Entidades de datos principales
`cliente`, `credito`, `pago`, `reestructuracion`, `asesor`, `sucursal`, `producto`, `contrato`, `solicitud`

### Historia de usuario de referencia
- **HU-SOFOM-001** (enriquecida): `docs/user-stories/enriched/HU-SOFOM-001.enriched.md`
- Agente responsable de enriquecimiento: `01_enrich-data-story-user`

## Reglas obligatorias

1. Todo desarrollo debe seguir CRISP-DM. La fase activa es visible en `docs/crisp-dm/`.
2. Toda historia de usuario de datos debe ser enriquecida por el agente `01_enrich-data-story-user` antes de planear o codificar.
3. Todo entregable debe tener evidencia verificable en GitHub (commits, PRs, `evidence/`).
4. Todo agente debe tener propósito, inputs, outputs, handoffs y criterios de éxito.
5. Todo skill debe tener `SKILL.md`, procedimiento reutilizable y evidencia de uso.
6. No se aceptan puntos sin evidencia en README, docs, PRs, commits, logs, tests o evidence.
7. No exponer secretos, tokens, credenciales ni datos sensibles. Los datos de VENTURA son sensibles por naturaleza (pensionados, IMSS, información crediticia).
8. Todo código SAS o Python debe incluir logging, manejo de errores y pruebas cuando aplique.
9. Toda transformación de datos debe tener reglas DQ documentadas en `dq/rules.md` y cifras de control.
10. Toda entrega final debe actualizar `scorecard/self-assessment.yml` y los archivos en `evidence/`.
11. Las capas Silver y Gold deben respetar la arquitectura definida en `docs/adr/ADR-002-sas-analytics.md`.
12. Toda clasificación de clientes (Nuevos / Inactivos / Renovaciones) debe aplicar las reglas documentadas en HU-SOFOM-001.

## Política interna de modelos

- Usa Auto como valor por defecto en Copilot Chat cuando esté disponible.
- Usa Claude Haiku para tareas repetitivas, creación masiva de archivos, limpieza de markdown y resúmenes.
- Usa Claude Sonnet para código, tests, documentación, agentes y ejecución principal.
- Usa Claude Opus para arquitectura, planeación compleja, scoring, riesgos, seguridad y decisiones ambiguas.
- Si un modelo no está disponible por política del tenant, usa Auto o el modelo aprobado por la organización.

## Definition of Done

Una entrega está completa solo si cumple **todos** los siguientes puntos:

| # | Criterio | Evidencia esperada |
|---|---|---|
| 1 | Historia de usuario enriquecida | `docs/user-stories/enriched/<ID>.enriched.md` |
| 2 | Historia raw documentada | `docs/user-stories/raw/<ID>.raw.md` |
| 3 | Código versionado en rama y PR | Commit en rama de feature + PR abierto |
| 4 | Tests o validación equivalente | `tests/test_<modulo>.py` o validaciones DQ documentadas |
| 5 | Reglas Data Quality documentadas | `dq/rules.md` actualizado |
| 6 | Documentación funcional y técnica | `docs/` actualizado |
| 7 | Evidencia de ejecución de agentes | `evidence/<agente>/<ID>.evidence.md` |
| 8 | Revisión de seguridad y gobernanza | Agente 02 o checklist de PR completado |
| 9 | Pipeline o ejecución reproducible | Sin rutas absolutas, credenciales ni hardcoding |
| 10 | Scorecard actualizado | `scorecard/self-assessment.yml` |
| 11 | Skills actualizados si aplica | `SKILL.md` con evidencia de uso |

**Regla**: No se acepta ningún punto del scorecard sin evidencia verificable en el repositorio.

---

## Arquitectura

- Sigue las reglas de arquitectura documentadas en `docs/architecture.md`.
- Para decisiones arquitectónicas, revisa `docs/adr/`.
- No introduzcas nuevos patrones arquitectónicos sin registrar un ADR.
- **Arquitectura activa del proyecto**: SAS Analytics — platform-native con SAS Data Management y SAS 9.4 (ver `docs/adr/ADR-002-sas-analytics.md`).
  - **Capa Silver**: limpieza, estandarización y filtrado de datos VENTURA. Tablas depuradas listas para integración.
  - **Capa Gold**: modelo integrado con clasificación de clientes, métricas de cartera y dimensiones analíticas. Consumo directo en Power BI.
- La arquitectura Databricks Medallion (`docs/adr/ADR-001-databricks-medallion.md`) está disponible como alternativa futura pero **no es la activa**.
- Toda decisión sobre esquema de tablas, naming o granularidad debe validarse contra el diccionario de datos en `docs/data-dictionary.md`.

---

## Flujo de Trabajo CRISP-DM

Este repositorio sigue CRISP-DM como marco de trabajo. Cada fase tiene documentación en `docs/crisp-dm/` y produce entregables verificables antes de avanzar a la siguiente.

| Fase | Documento | Agentes principales | Entregables clave |
|---|---|---|---|
| 1. Business Understanding | `docs/crisp-dm/01-business-understanding.md` | `01_enrich-data-story-user` | Historia enriquecida, KPIs, fuentes candidatas, preguntas abiertas |
| 2. Data Understanding | `docs/crisp-dm/02-data-understanding.md` | `02_data-governance` | Perfilado VENTURA, diccionario, linaje, clasificación PII |
| 3. Data Preparation | `docs/crisp-dm/03-data-preparation.md` | `03_planner`, `04_coder` | Capa Silver: limpieza, filtros SOFOM, estandarización |
| 4. Modeling / Transformation | `docs/crisp-dm/04-modeling-or-transformation.md` | `04_coder`, `06_data-quality` | Capa Gold: modelo integrado, segmentación de clientes |
| 5. Evaluation | `docs/crisp-dm/05-evaluation.md` | `05_qa`, `06_data-quality` | Validaciones DQ, cifras de control, pruebas de aceptación |
| 6. Deployment | `docs/crisp-dm/06-deployment.md` | `09_deployment`, `10_monitoring` | Pipeline productivo, monitoreo, evidencia final aprobada |

**Regla**: No avanzar de fase sin completar el DoD de la fase anterior y dejar evidencia en `evidence/`.

---

## Reglas de Data Quality SOFOM

Toda transformación debe validar las siguientes categorías. Las reglas detalladas se documentan en `dq/rules.md`.

| Categoría | Validación obligatoria |
|---|---|
| Identificación SOFOM | `tipo_credito IN (5, 16)` ó `folio LIKE 'I%'` ó `folio LIKE 'J%'` antes de cualquier transformación |
| Nulos críticos | `id_cliente`, `id_credito`, `fecha_originacion`, `monto_credito` no pueden ser nulos |
| Duplicados | `id_credito` debe ser único en capa Gold; detectar y reportar duplicados en Silver |
| Integridad referencial | Todo `id_cliente` en créditos debe existir en la tabla de personas |
| Catálogos | `tipo_credito`, `estatus_credito`, `clave_sucursal` deben validarse contra catálogos VENTURA |
| Formatos | Fechas en ISO `YYYY-MM-DD`; montos numéricos sin caracteres especiales ni signos de moneda |
| Cifras de control | Total cartera Gold debe conciliar con cifras operativas de VENTURA; documentar diferencias |
| Segmentación | Todo cliente debe clasificarse en exactamente uno de: `Nuevo`, `Inactivo` o `Renovación` |
| Asesor | Todo crédito activo debe tener `id_asesor` referenciado y no nulo |

---

## Gobernanza, Seguridad y Privacidad

### Clasificación de datos

Los datos SOFOM contienen información personal y financiera sensible sujeta a regulación:

| Tipo | Campos ejemplo | Regulación |
|---|---|---|
| PII | nombre, CURP, NSS, domicilio, datos de contacto | LFPDPPP |
| Financiera sensible | saldos, historial de pagos, monto de crédito, días de atraso | CNBV, regulación SOFOM |
| Regulatoria | datos de pensión IMSS Ley 73, nómina | IMSS, SAT |

### Controles obligatorios

- No incluir PII en logs, commits, comentarios ni nombres de archivos de trabajo.
- Las tablas Gold con PII deben documentarse en `docs/data-dictionary.md` con clasificación de sensibilidad.
- Todo acceso a datos VENTURA debe estar autorizado y documentado en `docs/data-sources.md`.
- Los contratos de datos deben formalizarse antes de pasar a producción (ver `contracts/`).
- El agente `02_data-governance` valida owner, steward, clasificación y riesgos **antes** de diseñar arquitectura.

### Gobierno de datos

- **Data Owner**: área solicitante (Comercial / Crédito / Riesgo / Cartera / Cobranza).
- **Data Steward**: equipo SOFOM DataLab.
- **Linaje**: toda tabla Gold debe tener linaje trazable hasta VENTURA documentado en `docs/data-mapping.md`.
- **ADR**: toda decisión de arquitectura o esquema se registra en `docs/adr/` antes de implementarse.

---

## Evidencia en GitHub

Todo entregable debe dejar evidencia verificable. No se acepta ningún punto del scorecard sin evidencia en el repositorio.

| Artefacto | Ubicación | Cuándo se genera |
|---|---|---|
| Historia raw | `docs/user-stories/raw/<ID>.raw.md` | Al ejecutar agente 01 |
| Historia enriquecida | `docs/user-stories/enriched/<ID>.enriched.md` | Al completar agente 01 |
| Evidencia de agente | `evidence/<agente>/<ID>.evidence.md` | Al completar cada agente |
| Reglas DQ | `dq/rules.md` | Antes de transformar datos |
| Diccionario de datos | `docs/data-dictionary.md` | En Data Understanding |
| Mapa de datos / linaje | `docs/data-mapping.md` | En Data Preparation |
| Documentación técnica | `docs/` | Al completar cada fase |
| Tests / validaciones | `tests/` | Con cada entregable de código |
| ADR | `docs/adr/` | Ante decisiones arquitectónicas |
| Auto-evaluación | `scorecard/self-assessment.yml` | Al cierre de cada entrega |

---

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

Para tareas específicas invoca los agentes disponibles en `.github/agents/`. La cadena oficial sigue el orden numérico:

| # | Agente | Propósito | Estado |
|---|---|---|---|
| 01 | `01_enrich-data-story-user` | Enriquecer historias de usuario SOFOM: conecta negocio, KPIs, fuentes VENTURA, reglas DQ y criterios de aceptación | ✅ Construido |
| 02 | `02_data-governance` | Validar y enriquecer el planner-input con clasificación de datos, ownership, PII, data contracts y riesgos regulatorios | En Proceso |
| 03 | `03_planner` | Planificación y estructuración de casos de uso sobre SAS 9.4 | En Proceso |
| 04 | `04_coder` | Implementación de código SAS / Python para capas Silver y Gold | Por construir |
| 05 | `05_qa` | Pruebas y aseguramiento de calidad del modelo de datos | Por construir |
| 06 | `06_data-quality` | Reglas DQ y validación de datos SOFOM (nulos, duplicados, integridad referencial, catálogos VENTURA) | En Proceso |
| 07 | `07_documentation` | Generación de documentación técnica y funcional | En Proceso |
| 08 | `08_compliance-security` | Cumplimiento regulatorio y seguridad (datos sensibles de pensionados IMSS) | Por construir |
| 09 | `09_deployment` | Orquestación y despliegue de pipelines SAS | Por construir |
| 10 | `10_monitoring` | Logging, métricas y monitoreo del modelo SOFOM | Por construir |
| 99 | `99_reviewer` | Revisión transversal de calidad — **no modifica archivos**, invocable en cualquier paso | Por construir |

### Agente 01 — Enrich Data Story User (ya construido)

Este agente es el **punto de entrada obligatorio** para cualquier nueva historia de usuario SOFOM. Su output (archivo `.enriched.md`) es prerequisito para invocar al agente Data Governance (02).

**Entradas que acepta**: PDF con historia de usuario, minuta de negocio, descripción de requerimiento, criterios de aceptación iniciales.

**Output**: Documento enriquecido con 21 secciones incluyendo contexto SOFOM, KPIs, fuentes de datos VENTURA, reglas de negocio preliminares, handoff a Governance y handoff a Planner.

**Historia ya enriquecida**: `docs/user-stories/enriched/HU-SOFOM-001.enriched.md`

#### Cómo ejecutar el agente 01

Invoca el agente `01_enrich-data-story-user` con los siguientes parámetros y solicita las tres salidas obligatorias:

```
Parámetros:
  sourceFile:      docs/user-stories/input/<ID>.pdf
  storyId:         <HU-SOFOM-XXX>
  dataProductName: Modelo de Datos SOFOM
  businessArea:    <Área solicitante>
```

**Salidas obligatorias que debe generar**:

| Salida | Ruta | Descripción |
|---|---|---|
| `raw` | `docs/user-stories/raw/<storyId>.raw.md` | Historia original extraída del PDF, sin modificar |
| `enriched` | `docs/user-stories/enriched/<storyId>.enriched.md` | Historia enriquecida con las 21 secciones completas |
| `evidence` | `evidence/enrich-data-story-user/<storyId>.evidence.md` | Evidencia de ejecución del agente (inputs usados, decisiones, supuestos, fecha) |

**Ejemplo para HU-SOFOM-004**:

```
Parámetros:
  sourceFile:      docs/user-stories/input/HU-SOFOM-004.pdf
  storyId:         HU-SOFOM-004
  dataProductName: Modelo de Datos SOFOM
  businessArea:    Cobranza

Genera las salidas obligatorias:
  - docs/user-stories/raw/HU-SOFOM-004.raw.md
  - docs/user-stories/enriched/HU-SOFOM-004.enriched.md
  - evidence/enrich-data-story-user/HU-SOFOM-004.evidence.md
```

### Agente 02 — Data Governance (paso clave)

Es el **guardián de la gobernanza**: valida y enriquece el `planner-input.json` con clasificación de datos, ownership, PII, data contracts, controles de acceso y riesgos regulatorios **antes** de que el Agente Planner diseñe la arquitectura. Ningún requerimiento pasa a diseño sin pasar por este agente.

---

## Instrucciones Especializadas

Instrucciones contextuales para dominios específicos están disponibles en `.github/instructions/`:

```
.github/
├── copilot-instructions.md (instrucciones generales)
└── instructions/
    ├── backend.instructions.md — Estándares para código backend
    ├── mcp.instructions.md — Configuración de Model Context Protocol
    ├── testing.instructions.md — Estrategias de testing y cobertura
    └── security.instructions.md — Seguridad, secrets, compliance
```

Estas instrucciones especializadas aplican reglas adicionales según el contexto y módulo en el que se trabaja.
