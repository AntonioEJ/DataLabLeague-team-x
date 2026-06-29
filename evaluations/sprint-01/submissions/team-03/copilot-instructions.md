# GitHub Copilot Instructions — CoE BI DataLab League: Carteras

## 1. Propósito y alcance

Este repositorio forma parte de la iniciativa **DataLab League** del CoE de Business Intelligence de Profuturo. Su objetivo es construir un **producto de datos agentizado** que automatice el ciclo de vida de tickets de requerimiento BI, desde la recepción del formulario Microsoft Forms hasta la generación de planes de trabajo bajo CRISP-DM.

### ¿Qué hace este repositorio?

- Recibe tickets de solicitud BI desde un Excel exportado de Microsoft Forms.
- Valida completitud de campos con criterios de severidad (Crítica > Alta > Media > Baja).
- Clasifica cada ticket: Completo, Incompleto, Requiere aclaración, No viable.
- Genera outputs estructurados: `ticket.json` (fuente de verdad) y `resumen.html` (visualización).
- Permite edición post-sesión: actualizar reglas de negocio, asignar complejidad T-Shirt, cambiar prioridad.
- Alimenta al agente de Planes de Trabajo con el JSON enriquecido para estimar tiempos CRISP-DM.

### ¿Qué NO hace?

- No genera código SQL, ETL ni soluciones técnicas hasta que un ticket sea clasificado como **Completo**.
- No inventa información. Si un campo no está presente, se reporta como faltante.
- No ejecuta operaciones destructivas sobre datos de producción.
- No almacena credenciales, tokens ni información sensible en el código.

---

## 2. Alineación con DataLab League y CRISP-DM

### DataLab League

Este proyecto pertenece al equipo **Carteras** dentro de la competencia DataLab League. El producto de datos se enfoca en la **gestión inteligente del intake de requerimientos BI**, reduciendo tiempos de atención y mejorando la trazabilidad del ciclo de vida de cada solicitud.

### CRISP-DM aplicado al producto

El producto sigue las fases de CRISP-DM adaptadas al contexto de gestión de tickets BI:

| Fase CRISP-DM | Aplicación en este producto |
|---|---|
| **Business Understanding** | Entender el requerimiento del solicitante a través del formulario de Forms. Validar que la información sea suficiente para iniciar análisis. |
| **Data Understanding** | Explorar los datos del Excel de Forms: 39 columnas, múltiples hojas, datos con duplicados y columnas con sufijo numérico. Mapear campos Excel ↔ modelo interno. |
| **Data Preparation** | Limpiar, normalizar y estructurar los datos del ticket en un `ticket.json` estandarizado. Resolver ambigüedades de nombres de columna. |
| **Modeling** | Clasificar tickets automáticamente por completitud. Cruzar prioridad × complejidad con la matriz de SLAs para estimar tiempos. |
| **Evaluation** | Validar que la clasificación sea correcta. El humano (Líder BI) confirma o ajusta post-sesión de entendimiento. |
| **Deployment** | El `ticket.json` enriquecido es consumido por el Agent Plan para generar el plan de trabajo con fases, tiempos y entregables CRISP-DM. |

### Fases del sprint actual (Sprint 1)

- ✅ Business Understanding: Definición del problema y alcance
- ✅ Data Understanding: Exploración del Excel real (1754 registros, 39 columnas)
- ✅ Data Preparation: Scripts de extracción, normalización y mapeo de campos
- ✅ Modeling: Clasificación automática de tickets + matriz SLA
- 🔜 Evaluation: Validación con datos reales en sesión con el equipo
- 🔜 Deployment: Integración con Agent Plan (Sprint 2)

---

## 3. Estándares de desarrollo y calidad

### Lenguaje y estilo de código

- **Python 3.13+** como lenguaje principal.
- Usar **type hints** en funciones públicas.
- Docstrings en formato Google para funciones con lógica de negocio.
- Variables y funciones en `snake_case`. Clases en `PascalCase`.
- Archivos de configuración en **JSON** (no YAML ni TOML).
- HTML generado con inline styles (sin dependencias externas).

### Estructura de archivos

```
src/{nombre_agente}/
├── scripts/       # Lógica ejecutable
├── assets/        # Recursos estáticos (logos, templates)
└── config/        # Configuración declarativa (JSON)
```

### Convenciones de commits

```
feat: Nueva funcionalidad
fix: Corrección de bug
docs: Solo documentación
refactor: Cambio de estructura sin cambio funcional
```

### Branching

- `main` — Producción estable
- `qa` — Pre-producción, pruebas de integración
- `dev/{ID_EMPLEADO}` — Desarrollo individual

### Pruebas

- Cada script debe ser ejecutable standalone con datos de prueba.
- El flag `--archivo` permite apuntar a cualquier Excel para testing.
- Los outputs se generan en `outputs/` (ignorado por git) para no contaminar el repo.

---

## 4. Data Quality y validaciones

### Reglas de calidad de datos

El sistema implementa validaciones en múltiples capas:

| Capa | Qué valida | Ejemplo |
|---|---|---|
| **Existencia** | El campo tiene un valor no nulo y no vacío | `titulo` no puede estar vacío |
| **Coherencia** | El valor tiene sentido en contexto | `criterios_aceptacion` no puede ser solo "." |
| **Completitud** | Todos los campos de una severidad están presentes | Un ticket Completo tiene 100% de campos Críticos y Altos |
| **Consistencia** | Los datos no se contradicen entre sí | La dirección del responsable coincide con la dirección solicitante |

### Jerarquía de severidad de campos

1. **Crítica** — Sin este campo el ticket NO puede procesarse: folio, fecha, solicitante, título, dirección
2. **Alta** — Sin este campo no se puede definir alcance: reglas de negocio, tipo de componente, línea de negocio, criterios de aceptación
3. **Media** — Complementario pero importante: responsable BI, prioridad, documento de referencia
4. **Baja** — Informativo: recurrencia, atención urgente

### Umbrales de clasificación

- **3+ campos Críticos faltantes** → No viable
- **Cualquier Crítico o Alto faltante** → Incompleto
- **Campos presentes pero texto < 15 caracteres** (en reglas/criterios) → Requiere aclaración
- **Todo presente y coherente** → Completo

### Trazabilidad de cambios

Cada modificación a un ticket queda registrada en `historial_cambios[]` del JSON:
```json
{
  "fecha": "2026-06-19T10:31:22",
  "accion": "Reglas de negocio actualizadas a v2",
  "autor": "Daniel Avila",
  "detalle": "Tipo: Acuerdo de sesion"
}
```

---

## 5. Gobernanza, seguridad y cumplimiento

### Datos sensibles

- El campo `sensibilidad` indica si el ticket contiene información personal o confidencial.
- **NUNCA** incluir datos reales de clientes en commits, PRs ni outputs versionados.
- El Excel de entrada (`input/`) está en `.gitignore` — no se sube al repositorio.
- El archivo `.env` con URLs y configuración de servidores está en `.gitignore`.

### Control de acceso

- El Excel fuente vive en OneDrive corporativo con permisos controlados.
- La descarga usa **SSO del navegador** — no hay credenciales hardcodeadas.
- Solo el equipo BI y los solicitantes autorizados tienen acceso al Forms.

### Cumplimiento regulatorio

- Los tickets pueden contener referencias a información regulatoria (CONSAR, CNBV).
- El campo `riesgo` identifica si hay riesgo por incumplimiento normativo.
- La prioridad de atención se rige por la **Matriz de SLAs** definida por la Dirección Técnica de Negocio.

### Principios de gobierno de datos

1. **Fuente única de verdad:** El `ticket.json` es el documento maestro de cada ticket.
2. **Inmutabilidad del historial:** Los cambios se registran, nunca se sobrescriben.
3. **Separación de concerns:** El agente Enrich enriquece datos; el agente Plan genera planes. No se mezclan responsabilidades.
4. **Auditoría:** Todo cambio tiene autor, fecha y tipo.

---

## 6. Uso efectivo de agentes y artefactos

### Arquitectura de agentes

```
┌─────────────────────────────────────────────────────┐
│                   Usuario (Líder BI)                 │
│  "Dame los últimos 3 tickets de Comercial"          │
└─────────────────┬───────────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────────────┐
│              Agent Enrich (Orquestador)              │
│  Lee Excel → Valida → Genera HTML + JSON            │
│  Edita tickets post-sesión                          │
└─────────────────┬───────────────────────────────────┘
                  │ ticket.json (output)
                  ▼
┌─────────────────────────────────────────────────────┐
│           Agent Plan (Sprint 2 — futuro)            │
│  Lee ticket.json → Propone plan CRISP-DM            │
│  Cruza prioridad × complejidad × SLA               │
└─────────────────────────────────────────────────────┘
```

### Agentes actuales

| Agente | Archivo | Responsabilidad |
|---|---|---|
| **Agent Enrich** | `.github/agents/enrich-agent.agent.md` | Leer tickets de Excel, validar, generar outputs, editar post-sesión |

### Handoffs entre agentes

| De | A | Artefacto | Formato |
|---|---|---|---|
| Excel Forms | Agent Enrich | Solicitudes BI | `.xlsx` en `input/` |
| Agent Enrich | Agent Plan (futuro) | Ticket enriquecido | `ticket.json` en `outputs/enrich/HI{folio}/` |
| Agent Enrich | Usuario | Resumen visual | `resumen.html` en `outputs/enrich/HI{folio}/` |

### Inputs y outputs por agente

**Agent Enrich:**
- **Input:** Excel de Microsoft Forms (`input/*.xlsx`)
- **Output por ticket:**
  - `outputs/enrich/HI{folio}/ticket.json` — Fuente de verdad (datos + historial + reglas + complejidad)
  - `outputs/enrich/HI{folio}/resumen.html` — Resumen visual conciso para stakeholders
- **Output global:** `outputs/enrich/index.json` — Índice maestro de todos los tickets procesados

### Skills

| Skill | Archivo | Descripción |
|---|---|---|
| enrich | `.github/skills/enrich/SKILL.md` | Define capacidades del Agent Enrich: leer, editar, descargar |

---

## 7. Evidencia en GitHub y Definition of Done

### Definition of Done — Sprint 1

Un entregable se considera **Done** cuando:

- [ ] El código está en el branch `dev/{ID}` y tiene PR aprobado a `qa`.
- [ ] Los scripts se ejecutan sin errores con el Excel real de Forms.
- [ ] Cada ticket procesado genera `ticket.json` + `resumen.html` correctos.
- [ ] La edición de tickets actualiza JSON y regenera HTML.
- [ ] La documentación (README, copilot-instructions) refleja el estado actual.
- [ ] No hay credenciales, datos personales ni archivos sensibles en el repo.
- [ ] Los commits tienen mensajes descriptivos con prefijo convencional.

### Evidencia verificable en GitHub

| Evidencia | Dónde |
|---|---|
| Estructura de agentes | `.github/agents/` |
| Instrucciones Copilot | `.github/copilot-instructions.md` |
| Skills documentadas | `.github/skills/enrich/SKILL.md` |
| Configuración declarativa | `src/enrich/config/*.json` |
| Scripts funcionales | `src/enrich/scripts/*.py` |
| Pull Requests con descripción | Tab "Pull requests" del repo |
| Commits convencionales | Historial de commits |

### Qué debe generar Copilot y qué NO

**Copilot DEBE:**
- Interpretar lenguaje natural del usuario y traducirlo a comandos del script.
- Ejecutar los scripts con los parámetros correctos.
- Reportar resultados de forma ejecutiva y en español.
- Respetar la clasificación de tickets sin inventar datos.

**Copilot NO DEBE:**
- Generar queries SQL ni soluciones técnicas sin ticket Completo.
- Inventar valores para campos faltantes.
- Modificar archivos de configuración sin instrucción explícita.
- Exponer datos sensibles en outputs versionados.
- Asignar complejidad T-Shirt (eso lo hace el Líder BI post-sesión).

---

## 8. Referencia rápida de comandos

```bash
# Leer últimos N tickets de una dirección
python src/enrich/scripts/validar_ticket.py --ultimos 3 --direccion Comercial

# Leer sin filtro de dirección
python src/enrich/scripts/validar_ticket.py --ultimos 5 --direccion todas

# Editar ticket: agregar reglas post-sesión
python src/enrich/scripts/editar_ticket.py --folio 1755 --reglas "..." --tipo "Acuerdo de sesion" --autor "Nombre"

# Editar ticket: asignar complejidad
python src/enrich/scripts/editar_ticket.py --folio 1755 --complejidad M

# Descargar Excel desde SharePoint (usa SSO del navegador)
python src/enrich/scripts/descargar_excel.py
```
