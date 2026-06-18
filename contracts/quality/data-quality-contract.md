# Data Quality Contract — Cartera Comercial

> **Estado**: Draft | **Versión**: 0.1.0 | **ID**: DQ-001

---

## Metadatos

| Campo | Valor |
|---|---|
| **ID Contrato** | DQ-001 |
| **Producto de Datos** | Cartera Comercial |
| **Data Product Contract** | [../data-products/cartera-comercial.contract.md](../data-products/cartera-comercial.contract.md) |
| **Versión** | 0.1.0 |
| **Estado** | Draft |
| **Owner DQ** | TODO Data Engineer |

---

## Reglas de Calidad por Dimensión

### Completitud

| Campo | Umbral Mínimo | Severidad |
|---|---|---|
| `id_cliente` | 100% | Crítico |
| `id_producto` | 100% | Crítico |
| `fecha_corte` | 100% | Crítico |
| `saldo_capital` | 100% | Crítico |
| `dias_atraso` | 100% | Mayor |
| `sector_economico` | 70% | Menor |

### Unicidad

| Clave | Umbral | Severidad |
|---|---|---|
| `id_cliente + id_producto + fecha_corte` | 100% | Crítico |

### Validez

| Campo | Regla | Umbral | Severidad |
|---|---|---|---|
| `saldo_capital` | >= 0 | 100% | Crítico |
| `tasa_interes` | > 0 AND <= 1 | 100% | Crítico |
| `dias_atraso` | >= 0 | 100% | Crítico |
| `fecha_corte` | = T-1 día hábil | 100% | Crítico |

### Puntualidad

| Indicador | Compromiso | Tolerancia | Severidad |
|---|---|---|---|
| Publicación antes de 08:00 CDMX | 08:00 | ± 15 min | Mayor |

### Reconciliación

| Métrica | Tolerancia |
|---|---|
| COUNT(*) vs. Core Bancario | 0 registros de diferencia |
| SUM(saldo_capital) vs. Core | < 0.01% de diferencia |

---

## Cifras de Control

| Indicador | Valor Esperado | Tolerancia | Acción si Falla |
|---|---|---|---|
| Total registros diarios | TODO ± 5% | TODO | Notificar y pausar |
| Suma saldos (MXN) | TODO ± 0.01% | TODO | Escalar inmediato |
| Clientes únicos | TODO ± 2% | TODO | Revisar fuente |

---

## Implementación

| Regla | Archivo de Implementación |
|---|---|
| Completitud | `dq/rules.md` |
| Unicidad | `dq/rules.md` |
| Validez saldos | `dq/rules.md` |
| Reconciliación | `dq/rules.md` |

---

**ID**: DQ-001 | **Versión**: 0.1.0
