# SLA/SLO Contract Template

> **Instrucciones**: Copia este template, nómbralo `[nombre-producto].sla-slo.md` y colócalo en `contracts/slas/`. Completa todos los campos `TODO`.

---

## Metadatos del Contrato

| Campo | Valor |
|---|---|
| **ID Contrato** | SL-XXX |
| **Producto de Datos** | TODO |
| **Versión** | 0.1.0 |
| **Estado** | Draft / Active / Deprecated |
| **Vigencia** | YYYY-MM-DD al YYYY-MM-DD |
| **Fecha Revisión** | YYYY-MM-DD |

---

## 1. Partes del Acuerdo

| Rol | Nombre | Equipo | Contacto |
|---|---|---|---|
| **Productor** | TODO | TODO | TODO |
| **Consumidor principal** | TODO | TODO | TODO |
| **Responsable SRE/Ops** | TODO | TODO | TODO |

---

## 2. Disponibilidad *

| Indicador | SLO (Objetivo) | SLA (Compromiso) | Penalización por Incumplimiento |
|---|---|---|---|
| Disponibilidad mensual | 99.9% | 99.5% | Notificación + plan de mejora |
| Disponibilidad en ventana crítica | 100% | 99.8% | Escalamiento inmediato |
| Uptime del pipeline | 99% | 98% | Revisión técnica |

**Ventana de mantenimiento programado**: TODO (e.g., Domingos 02:00–04:00)

**Tiempo máximo de mantenimiento**: TODO horas/mes

---

## 3. Hora de Publicación *

| Dataset / Producto | Hora Comprometida | Tolerancia | Zona Horaria |
|---|---|---|---|
| TODO_producto | 08:00 | ± 15 min | America/Mexico_City (CDMX) |
| TODO_producto_2 | TODO | TODO | TODO |

**Frecuencia**: Diaria / Semanal / Mensual / Batch

**Días de publicación**: Lunes a Viernes / Todos los días / TODO

---

## 4. Latencia *

| Indicador | Objetivo (SLO) | Máximo (SLA) | Medición |
|---|---|---|---|
| Latencia end-to-end (fuente → disponible) | < 10 min | < 30 min | Tiempo promedio diario |
| Latencia de ingesta (fuente → Bronze) | < 5 min | < 15 min | Percentil 95 |
| Latencia de transformación (Bronze → Gold) | < 5 min | < 15 min | Percentil 95 |
| Latencia de entrega al consumidor | < 1 min | < 5 min | Percentil 99 |

---

## 5. Frescura de Datos *

| Indicador | Objetivo | Máximo Aceptable | Acción si Excede |
|---|---|---|---|
| Frescura de datos | T+1 hora | T+4 horas | Alerta automática |
| Datos más recientes | Mismo día | T-1 día | Notificación |
| Retraso máximo tolerable | 2 horas | 4 horas | Escalar a Ops |

---

## 6. Tiempo de Recuperación (Incidentes) *

| Severidad | Descripción | RTO (Recovery Time Objective) | RPO (Recovery Point Objective) |
|---|---|---|---|
| **P1 Crítico** | Datos no disponibles en ventana crítica | 2 horas | 0 pérdida de datos |
| **P2 Mayor** | Retraso > 2h o datos incorrectos | 4 horas | < 1 ciclo |
| **P3 Menor** | Retraso < 1h o warning de calidad | 8 horas | < 1 día |
| **P4 Info** | Alerta de monitoreo sin impacto | Próximo sprint | N/A |

---

## 7. Severidad de Incidentes y Escalamiento

| Nivel | Condición | Canal Inicial | Escalamiento Nivel 1 | Escalamiento Nivel 2 |
|---|---|---|---|---|
| **P1 Crítico** | Datos no disponibles o incorrectos en producción | TODO (PagerDuty/Teams) | TODO Engineering Lead | TODO VP Datos |
| **P2 Mayor** | Retraso significativo o degradación de calidad | TODO canal | TODO Data Engineer | TODO Engineering Lead |
| **P3 Menor** | Warning de monitoreo | TODO Slack | TODO Data Engineer | - |
| **P4 Info** | Notificación informativa | Dashboard | - | - |

---

## 8. Canales de Soporte

| Canal | Disponibilidad | Tiempo de Respuesta | Uso |
|---|---|---|---|
| TODO (Teams/Slack) | 24/7 para P1, L-V 9-18 otros | P1: 15 min, Otros: 2h | Incidentes |
| Email: TODO@empresa.com | L-V 9-18 | 4 horas | Consultas |
| Dashboard: TODO URL | 24/7 | - | Monitoreo |
| On-call: TODO | 24/7 solo P1 | 15 min | Escalamiento P1 |

---

## 9. Métricas de Seguimiento

| Métrica | Herramienta | Dashboard | Frecuencia de Reporte |
|---|---|---|---|
| Disponibilidad % | TODO | TODO URL | Mensual |
| Tiempo de publicación | TODO | TODO URL | Diario |
| Latencia promedio | TODO | TODO URL | Diario |
| Incidentes por severidad | TODO | TODO URL | Semanal |

---

## 10. Historial de Incidentes

| Fecha | Severidad | Descripción | RTO Real | Causa Raíz | Acción Preventiva |
|---|---|---|---|---|---|
| YYYY-MM-DD | P1 | TODO | TODO h | TODO | TODO |

---

## 11. Revisión y Vigencia

Este contrato se revisa:
- Cada **TODO meses**
- Cuando cambia significativamente la arquitectura
- Cuando un incidente revela compromisos no alcanzables

**Proceso de cambio**: PR + aprobación de productor + consumidor principal

---

## 12. Aprobaciones

| Rol | Nombre | Fecha | Estado |
|---|---|---|---|
| Owner de Negocio | TODO | TODO | Pendiente |
| Owner Técnico / SRE | TODO | TODO | Pendiente |
| Consumidor Principal | TODO | TODO | Pendiente |

---

**Template Version**: 1.0.0
**Template Location**: `contracts/templates/sla-slo-template.md`
