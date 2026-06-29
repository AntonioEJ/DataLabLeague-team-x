# CoE BI DataLab League — Equipo Carteras

## Producto de datos: Gestión Inteligente de Tickets BI

### Problema de negocio

El equipo de Business Intelligence de Profuturo recibe solicitudes de requerimientos a través de Microsoft Forms. Actualmente, el proceso de intake es **manual y propenso a errores**: los tickets llegan incompletos, sin reglas de negocio claras, y sin una clasificación que permita priorizar la atención. Esto genera:

- **Retrabajos** por falta de información en sesiones de entendimiento.
- **Tiempos muertos** esperando aclaraciones que pudieron detectarse al inicio.
- **Falta de trazabilidad** sobre qué se acordó en cada sesión y quién modificó qué.

### Solución: Producto de datos agentizado

Un sistema de agentes de GitHub Copilot que automatiza el ciclo de vida del ticket BI:

1. **Recepción** — Descarga automática del Excel desde SharePoint.
2. **Validación** — Clasificación instantánea por completitud de campos.
3. **Enriquecimiento** — Generación de resumen HTML + JSON estructurado.
4. **Gestión post-sesión** — Edición de reglas, asignación de complejidad, trazabilidad.
5. **Handoff** — El JSON enriquecido alimenta al agente de planes de trabajo (Sprint 2).

### Usuarios y consumidores

| Rol | Cómo consume el producto |
|---|---|
| **Líder BI** | Invoca al agente para validar tickets, editar reglas post-sesión, asignar complejidad |
| **Especialista BI** | Consulta el `resumen.html` antes de la sesión de entendimiento |
| **Dirección Técnica** | Revisa el `index.json` para monitorear volumen y estado de tickets |
| **Agente de Planes (futuro)** | Lee `ticket.json` para proponer plan CRISP-DM con tiempos estimados |

### Decisiones que habilita

- ¿El ticket tiene suficiente información para iniciar? → Clasificación automática.
- ¿Cuánto tiempo nos tomará? → Cruce prioridad × complejidad T-Shirt × SLA.
- ¿Qué se acordó en sesión? → Historial versionado de reglas de negocio.
- ¿Quién modificó qué y cuándo? → Auditoría completa en `historial_cambios[]`.

---

## Contexto: DataLab League

| Campo | Valor |
|---|---|
| **Equipo** | Carteras |
| **Competencia** | DataLab League — CoE Business Intelligence, Profuturo |
| **Sprint actual** | Sprint 1 |
| **Metodología** | CRISP-DM |
| **Repositorio** | `Profuturo-Data-EUC/coe-bi-datalab-league-CARTERAS` |

---

## Alcance y fuera de alcance

### Alcance (Sprint 1)

- ✅ Lectura y validación automática de tickets desde Excel real de Forms.
- ✅ Clasificación por completitud (Completo / Incompleto / Requiere aclaración / No viable).
- ✅ Generación de `ticket.json` como fuente de verdad.
- ✅ Generación de `resumen.html` con logo corporativo, alertas y bitácora.
- ✅ Edición post-sesión: reglas de negocio, complejidad T-Shirt, prioridad.
- ✅ Trazabilidad completa de cambios (autor, fecha, tipo).
- ✅ Descarga automática del Excel desde SharePoint (SSO del navegador).

### Fuera de alcance

- ❌ Generación de código SQL, ETL o soluciones técnicas.
- ❌ Envío automático de emails (shelved por restricciones de relay corporativo).
- ❌ Agente de planes de trabajo (Sprint 2).
- ❌ Integración con sistemas de tickets externos (ServiceNow, Jira).

---

## Estructura del repositorio

```
├── .github/
│   ├── copilot-instructions.md         # Instrucciones para GitHub Copilot (40 pts rúbrica)
│   ├── agents/
│   │   └── enrich-agent.agent.md       # Definición del Agent Enrich
│   └── skills/
│       └── enrich/SKILL.md             # Skill: capacidades del agente
│
├── src/enrich/                         # Código fuente del Agent Enrich
│   ├── scripts/
│   │   ├── validar_ticket.py           # Leer Excel → Validar → Generar outputs
│   │   ├── editar_ticket.py            # Editar tickets existentes post-sesión
│   │   ├── generar_resumen.py          # Template HTML (importable)
│   │   └── descargar_excel.py          # Descarga automática desde SharePoint
│   ├── assets/
│   │   └── logo.png                    # Logo corporativo Profuturo
│   └── config/
│       ├── campos-forms.json           # Mapeo: columnas Excel ↔ modelo interno
│       ├── criterios-validacion.json   # Reglas de clasificación
│       └── sla-matrix.json             # Matriz SLAs: impacto × complejidad
│
├── input/                              # Excel de Forms (no versionado, en .gitignore)
├── outputs/enrich/                     # Outputs generados (no versionados)
│   ├── index.json                      # Índice maestro de tickets
│   └── HI{folio}/                      # Carpeta por ticket
│       ├── ticket.json                 # Fuente de verdad completa
│       └── resumen.html                # Resumen visual
│
├── .env                                # Variables de entorno (no versionado)
├── .gitignore                          # Excluye: .env, input/, outputs/
└── README.md                           # Este archivo
```

---

## Metodología CRISP-DM

El producto de datos sigue CRISP-DM adaptado al contexto de gestión de tickets:

```
┌────────────────────────────────────────────────────────────────┐
│  CRISP-DM aplicado al Agent Enrich                             │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│  1. Business Understanding                                     │
│     └─ Formulario de Forms → ¿Qué necesita el solicitante?    │
│                                                                │
│  2. Data Understanding                                         │
│     └─ Excel 39 columnas, 1754 registros, 4 hojas             │
│     └─ Columnas con sufijo numérico (Forms duplica nombres)   │
│                                                                │
│  3. Data Preparation                                           │
│     └─ validar_ticket.py: normaliza, mapea, estructura        │
│     └─ Output: ticket.json estandarizado                       │
│                                                                │
│  4. Modeling                                                   │
│     └─ Clasificación automática por severidad de campos        │
│     └─ Cruce prioridad × complejidad → SLA estimado           │
│                                                                │
│  5. Evaluation                                                 │
│     └─ Líder BI valida en sesión de entendimiento              │
│     └─ editar_ticket.py registra acuerdos y ajustes            │
│                                                                │
│  6. Deployment                                                 │
│     └─ ticket.json → Agent Plan (Sprint 2)                     │
│     └─ Genera plan de trabajo con fases y tiempos CRISP-DM     │
│                                                                │
└────────────────────────────────────────────────────────────────┘
```

---

## Uso rápido

```bash
# Descargar Excel desde SharePoint (abre navegador con SSO)
python src/enrich/scripts/descargar_excel.py

# Generar resúmenes de los últimos 3 tickets de Comercial
python src/enrich/scripts/validar_ticket.py --ultimos 3 --direccion Comercial

# Generar sin filtro de dirección
python src/enrich/scripts/validar_ticket.py --ultimos 5 --direccion todas

# Editar ticket post-sesión
python src/enrich/scripts/editar_ticket.py --folio 1755 --complejidad M --autor "Daniel Avila"
python src/enrich/scripts/editar_ticket.py --folio 1755 --reglas "Nueva regla..." --tipo "Acuerdo de sesion"
```

O desde **GitHub Copilot** (seleccionar Agent Enrich):
> "Dame el resumen de los últimos 3 tickets de Comercial"

---

## Evidencia del Sprint 1

| Entregable | Estado | Ubicación |
|---|---|---|
| Instrucciones Copilot | ✅ Completo | `.github/copilot-instructions.md` |
| Agent Enrich funcional | ✅ Completo | `.github/agents/enrich-agent.agent.md` |
| Skill documentado | ✅ Completo | `.github/skills/enrich/SKILL.md` |
| Scripts ejecutables con Excel real | ✅ Probado con 1754 registros | `src/enrich/scripts/` |
| Configuración declarativa | ✅ Completo | `src/enrich/config/` |
| PR a QA | ✅ Merge #2 completado | Branch `qa` |
| Commits convencionales | ✅ `feat:`, `merge:` | Historial de commits |
| Data Quality implementado | ✅ Validaciones por severidad | `criterios-validacion.json` |
| Gobierno y trazabilidad | ✅ Historial inmutable en JSON | `ticket.json → historial_cambios[]` |

---

## Próximos pasos (Sprint 2)

1. **Agent Plan** — Agente que lee `ticket.json` y propone plan de trabajo CRISP-DM con fases, tiempos y entregables basado en la matriz de SLAs.
2. **Métricas de intake** — Dashboard de volumen, tiempos de atención y tasa de completitud.
3. **Notificaciones** — Alertas cuando un ticket lleva más de X días sin sesión.

---

## Equipo

| Rol | Nombre |
|---|---|
| Desarrollador principal | Daniel Avila (DA505364) |
| Dirección | Dirección Técnica de Negocio |
| Área | CoE Business Intelligence — Profuturo |
3. Copilot devolverá únicamente la lista de campos ausentes clasificados por severidad.

### Generar ficha documental

1. Escribe `/` y selecciona **Generar Ficha de Requerimiento BI**.
2. Pega el ticket previamente validado como Completo.
3. Copilot generará la ficha estructurada del requerimiento.

### Generar minuta de sesión de entendimiento

1. Escribe `/` y selecciona **Generar y Enviar Minuta BI**.
2. Proporciona los datos del ticket (o usa uno previamente validado).
3. Copilot generará una minuta corporativa en HTML.
4. Opcionalmente, envía la minuta por email a los participantes de la sesión.

**Nota:** Las minutas son documentos profesionales que sirven para convocar sesiones de entendimiento y documentar los temas a discutir con el solicitante.

---

## Cómo usar los agentes

Selecciona el agente desde el selector de agentes en Copilot Chat:

| Agente | Cuándo usarlo |
|---|---|
| **Intake BI Agent** | Ticket nuevo — dictamen completo |
| **Validador de Ticket BI** | Verificar campos obligatorios con detalle técnico |
| **Documentador BI** | Generar ficha de un ticket ya clasificado como Completo |

---

## Documentos de referencia clave

- [Diccionario de campos](.github/skills/ticket-bi/assets/campos-forms.md) — Mapeo de campos del Forms con severidad y uso BI.
- [Criterios de validación](.github/skills/ticket-bi/assets/criterios-validacion.md) — Lógica de clasificación de tickets.
- [Ejemplo completo](examples/ticket-completo.md) — Caso de referencia para ticket válido.
- [Ejemplo incompleto](examples/ticket-incompleto.md) — Caso de referencia para ticket deficiente.

---

## Principios del agente

- No inventa información.
- No genera queries ni soluciones técnicas con tickets incompletos.
- Responde siempre en español.
- Usa únicamente los datos presentes en el ticket recibido.
