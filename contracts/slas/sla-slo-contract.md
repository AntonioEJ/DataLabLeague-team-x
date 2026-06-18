# SLA/SLO Contract — Cartera Comercial

> **Estado**: Draft | **Versión**: 0.1.0 | **ID**: SL-001

---

## Metadatos

| Campo | Valor |
|---|---|
| **ID Contrato** | SL-001 |
| **Producto de Datos** | Cartera Comercial |
| **Versión** | 0.1.0 |
| **Estado** | Draft |
| **Vigencia** | 2026-07-01 al 2026-12-31 |
| **Data Product Contract** | [../data-products/cartera-comercial.contract.md](../data-products/cartera-comercial.contract.md) |

---

## Disponibilidad

| Indicador | SLO | SLA |
|---|---|---|
| Disponibilidad mensual | 99.9% | 99.5% |
| Disponibilidad ventana crítica (06:00–10:00) | 100% | 99.8% |

---

## Hora de Publicación

| Dataset | Hora Comprometida | Tolerancia | Zona Horaria |
|---|---|---|---|
| `cartera_comercial` (Gold) | 08:00 | ± 15 min | America/Mexico_City |

---

## Latencia

| Indicador | Objetivo | Máximo |
|---|---|---|
| End-to-end (Core → Gold disponible) | < 15 min | < 30 min |
| Ingesta Bronze | < 5 min | < 15 min |
| Transformación Silver → Gold | < 10 min | < 20 min |

---

## Tiempo de Recuperación

| Severidad | RTO | RPO |
|---|---|---|
| P1 Crítico | 2 horas | Sin pérdida de datos |
| P2 Mayor | 4 horas | < 1 ciclo diario |
| P3 Menor | 8 horas | < 1 día |

---

## Escalamiento

| Severidad | Condición | Canal | SLA Resolución |
|---|---|---|---|
| P1 | Sin datos después de 08:30 | TODO PagerDuty | 2h |
| P2 | Retraso > 30 min | TODO Teams/Slack | 4h |
| P3 | Warning de calidad DQ | TODO Slack | 8h |

---

## Aprobaciones

| Rol | Nombre | Estado |
|---|---|---|
| Owner de Negocio | TODO | Pendiente |
| Owner Técnico | TODO | Pendiente |
| Consumidor Principal | TODO | Pendiente |

---

**ID**: SL-001 | **Versión**: 0.1.0
