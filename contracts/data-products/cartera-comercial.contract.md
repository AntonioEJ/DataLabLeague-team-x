# Cartera Comercial — Data Product Contract

> **Estado**: Draft | **Versión**: 0.1.0 | **ID**: DP-001

---

## Metadatos del Contrato

| Campo | Valor |
|---|---|
| **ID Contrato** | DP-001 |
| **Versión** | 0.1.0 |
| **Estado** | Draft |
| **Fecha Creación** | 2026-06-18 |
| **Última Actualización** | 2026-06-18 |
| **Próxima Revisión** | 2026-09-18 |

---

## 1. Identificación del Producto de Datos

| Campo | Valor |
|---|---|
| **Nombre del Producto** | Cartera Comercial |
| **Nombre Técnico** | `cartera_comercial` |
| **Descripción** | Consolidado diario de posiciones de cartera comercial por cliente. Agrega saldos, tasas y comportamiento de pago de productos de crédito comercial. |
| **Dominio de Negocio** | Crédito Comercial |
| **Fase CRISP-DM Principal** | Deployment |

---

## 2. Owners

| Rol | Nombre | Equipo | Contacto |
|---|---|---|---|
| **Owner de Negocio** | TODO | Crédito Comercial | TODO |
| **Owner Técnico** | TODO | Data Engineering | TODO |
| **Data Steward** | TODO | Gobierno de Datos | TODO |

---

## 3. Objetivo y Alcance

### Objetivo de Negocio
Proporcionar a los equipos de crédito y riesgo la posición actualizada de la cartera comercial para soportar decisiones de límites, alertas tempranas y reportes regulatorios.

### KPIs Asociados
- Exposición total cartera comercial (MXN)
- Clientes en mora > 30 días
- Concentración por sector económico

### Alcance

**Incluye**:
- Créditos comerciales activos
- Posición al cierre del día anterior (T-1)
- Clientes con contrato vigente

**Excluye**:
- Créditos en proceso de liquidación definitiva
- Cartera hipotecaria (ver producto separado)

---

## 4. Consumidores

| Consumidor | Equipo | Caso de Uso | Tipo de Acceso | Frecuencia |
|---|---|---|---|---|
| Dashboard Ejecutivo | Business Intelligence | Monitoreo KPIs diarios | Lectura | Diaria |
| Modelo de Riesgo | Data Science | Features para scoring | Lectura | Diaria |
| Reporte Regulatorio | Compliance | Reporte CNBV | Lectura | Mensual |

---

## 5. Fuentes de Datos

| Fuente | Sistema | Tabla | Frecuencia | Owner |
|---|---|---|---|---|
| Sistema Core Bancario | TODO Core | `CREDITOS.POSICION_DIARIA` | Diaria 01:00 | TI Banca |
| CRM Comercial | TODO CRM | `CLIENTES.PERFIL_COMERCIAL` | Diaria 00:30 | Comercial |
| Catálogo de Sectores | TODO | `CATALOGOS.SECTOR_ECONOMICO` | Mensual | Riesgo |

---

## 6. Grano

Una fila representa la **posición consolidada de un cliente en un producto de crédito comercial específico al cierre del día**.

**Clave única**: `id_cliente + id_producto + fecha_corte`

---

## 7. Campos de Salida

| Nombre Campo | Tipo | Obligatorio | PII | Clasificación | Descripción |
|---|---|---|---|---|---|
| `id_cliente` | `STRING` | Sí | No | Interno | ID único del cliente |
| `id_producto` | `STRING` | Sí | No | Interno | ID único del producto de crédito |
| `fecha_corte` | `DATE` | Sí | No | Interno | Fecha de la posición (T-1) |
| `saldo_capital` | `DECIMAL(18,2)` | Sí | No | Confidencial | Saldo de capital pendiente (MXN) |
| `tasa_interes` | `DECIMAL(6,4)` | Sí | No | Confidencial | Tasa de interés anual |
| `dias_atraso` | `INTEGER` | Sí | No | Confidencial | Días de atraso en pago |
| `sector_economico` | `STRING` | No | No | Interno | Sector SCIAN del cliente |

---

## 8. Reglas de Negocio

| ID | Descripción | Campo |
|---|---|---|
| RN-001 | `saldo_capital` debe ser >= 0 | `saldo_capital` |
| RN-002 | `dias_atraso` = 0 si el pago está al corriente | `dias_atraso` |
| RN-003 | La fecha de corte debe ser T-1 (día hábil anterior) | `fecha_corte` |
| RN-004 | Solo incluir clientes con contrato de crédito vigente | Todos |

---

## 9. Lineage de Datos

```
[Core Bancario: CREDITOS.POSICION_DIARIA]  ──→
[CRM: CLIENTES.PERFIL_COMERCIAL]           ──→  [Bronze: raw_cartera] ──→ [Silver: clean_cartera] ──→ [Gold: cartera_comercial] ──→ [Dashboard / Modelos / Reportes]
[Catálogos: SECTOR_ECONOMICO]              ──→
```

**Transformaciones principales**:
1. Ingesta diaria desde Core Bancario y CRM vía pipeline `pipeline/cartera-comercial`
2. Limpieza y deduplicación en capa Silver
3. Enriquecimiento con sector económico y cálculo de días de atraso en Gold

---

## 10. Reglas de Calidad (Resumen)

> Ver contrato completo: [../quality/cartera-comercial.quality-contract.md](../quality/cartera-comercial.quality-contract.md) _(pendiente de crear)_

| Dimensión | Umbral |
|---|---|
| Completitud | ≥ 98% |
| Unicidad de clave | 100% |
| Validez `saldo_capital >= 0` | 100% |
| Publicación antes de 08:00 | SLA |

---

## 11. SLA / SLO (Resumen)

> Ver contrato completo: [../slas/cartera-comercial.sla-slo.md](../slas/cartera-comercial.sla-slo.md) _(pendiente de crear)_

| Indicador | Compromiso |
|---|---|
| Disponibilidad mensual | 99.5% |
| Hora de publicación | 08:00 CDMX |
| Latencia desde Core | < 30 minutos |
| RTO | 4 horas |

---

## 12. Clasificación y Seguridad

| Atributo | Valor |
|---|---|
| Clasificación | Confidencial |
| Contiene PII | No (IDs internos, no datos personales directos) |
| Datos Sensibles | Saldos, tasas, comportamiento de pago |
| Cifrado en tránsito | TLS 1.2+ |
| Acceso requiere | Rol `data-analyst` o superior, VPN |

---

## 13. Criterios de Aceptación

- [ ] CA-001: Datos publicados antes de las 08:00 CDMX
- [ ] CA-002: Completitud de campos obligatorios ≥ 98%
- [ ] CA-003: Zero registros con `saldo_capital < 0`
- [ ] CA-004: Clave `id_cliente + id_producto + fecha_corte` es única
- [ ] CA-005: `fecha_corte` = T-1 (día hábil previo)
- [ ] CA-006: Reconciliación COUNT(*) vs. Core con tolerancia 0

---

## 14. Aprobaciones

| Rol | Nombre | Fecha | Estado |
|---|---|---|---|
| Owner de Negocio | TODO | - | Pendiente |
| Owner Técnico | TODO | - | Pendiente |
| Data Governance Lead | TODO | - | Pendiente |

---

**Contrato ID**: DP-001 | **Versión**: 0.1.0 | **Template**: `contracts/templates/data-contract-template.md`
