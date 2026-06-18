# Data Quality Contract Template

> **Instrucciones**: Copia este template, nómbralo `[nombre-producto].quality-contract.md` y colócalo en `contracts/quality/`. Completa todos los campos `TODO`. Los campos marcados con `*` son obligatorios.

---

## Metadatos del Contrato

| Campo | Valor |
|---|---|
| **ID Contrato** | DQ-XXX |
| **Producto de Datos** | TODO |
| **Versión** | 0.1.0 |
| **Estado** | Draft / Active / Deprecated |
| **Fecha Creación** | YYYY-MM-DD |
| **Última Actualización** | YYYY-MM-DD |
| **Owner DQ** | TODO |

---

## 1. Dimensiones de Calidad *

### 1.1 Completitud

> ¿Qué porcentaje de los campos requeridos tienen valor no nulo?

| Campo | Regla | Umbral Mínimo | Umbral Aceptable | Severidad |
|---|---|---|---|---|
| `id_cliente` | NOT NULL | 100% | 100% | Crítico |
| `TODO_campo` | NOT NULL | TODO% | TODO% | TODO |

**Cálculo**:
```
completitud = (registros_sin_nulos / total_registros) * 100
```

---

### 1.2 Unicidad

> ¿Existen registros duplicados en la clave definida?

| Clave | Regla | Umbral | Severidad |
|---|---|---|---|
| `id_cliente + fecha` | UNIQUE | 100% | Crítico |
| `TODO_campo` | TODO | TODO% | TODO |

**Cálculo**:
```
unicidad = (registros_unicos / total_registros) * 100
```

---

### 1.3 Validez

> ¿Los valores están dentro del dominio esperado (tipos, rangos, formatos)?

| Campo | Regla de Validez | Ejemplo Válido | Ejemplo Inválido | Umbral | Severidad |
|---|---|---|---|---|---|
| `email` | Formato RFC 5321 | `a@b.com` | `no-email` | 99% | Mayor |
| `monto` | `>= 0` | `1500.00` | `-100` | 100% | Crítico |
| `TODO_campo` | TODO | TODO | TODO | TODO% | TODO |

---

### 1.4 Consistencia

> ¿Los datos son coherentes entre sí y entre fuentes?

| Regla | Descripción | Umbral | Severidad |
|---|---|---|---|
| RC-001 | `saldo_actual` debe ser igual a `saldo_inicial + movimientos` | 100% | Crítico |
| RC-002 | TODO | TODO% | TODO |

---

### 1.5 Exactitud

> ¿Los valores reflejan correctamente la realidad?

| Campo | Fuente de Verdad | Tolerancia | Método Verificación | Frecuencia |
|---|---|---|---|---|
| `TODO_campo` | TODO | TODO | Reconciliación vs. fuente | Diaria |

---

### 1.6 Integridad Referencial

> ¿Las claves foráneas apuntan a registros válidos?

| Campo FK | Tabla Referenciada | Regla | Umbral | Severidad |
|---|---|---|---|---|
| `id_cliente` | `dim_clientes` | FK válida | 100% | Crítico |
| `TODO_campo` | TODO | TODO | TODO% | TODO |

---

### 1.7 Puntualidad / Frescura

> ¿Los datos están disponibles dentro del tiempo esperado?

| Indicador | Compromiso | Tolerancia | Severidad |
|---|---|---|---|
| Disponibilidad | Antes de 08:00 | 15 min | Mayor |
| Frescura máxima | T+1 día | T+2 días | Mayor |
| Latencia desde fuente | < 15 min | 30 min | Menor |

---

### 1.8 Trazabilidad / Linaje

> ¿Se puede rastrear el origen de cada dato?

| Requerimiento | Estado | Evidencia |
|---|---|---|
| Linaje documentado en contrato DP | Sí / No | [../data-products/TODO.contract.md] |
| Pipeline versionado en Git | Sí / No | `pipeline/TODO` |
| Logs de transformación disponibles | Sí / No | `observability/logging.md` |

---

### 1.9 Reconciliación

> ¿Los totales del producto coinciden con los de la fuente original?

| Métrica | Fuente | Producto | Tolerancia | Frecuencia |
|---|---|---|---|---|
| `COUNT(*)` | TODO | TODO | 0 registros | Diaria |
| `SUM(monto)` | TODO | TODO | < 0.01% | Diaria |
| `TODO_métrica` | TODO | TODO | TODO | TODO |

---

## 2. Cifras de Control *

| Indicador | Valor Esperado | Tolerancia | Acción si Falla |
|---|---|---|---|
| Total de registros (diario) | TODO ± 10% | TODO | Notificar y bloquear publicación |
| Suma de montos | TODO ± 0.01% | TODO | Notificar y escalar |
| Nulls en campo clave | 0 | 0 | Detener pipeline |

---

## 3. Reglas Implementadas

> Lista de reglas con referencia a implementación en código

| ID Regla | Dimensión | Descripción | Implementación | Estado |
|---|---|---|---|---|
| DQ-001 | Completitud | `id_cliente` NOT NULL | `dq/rules.md#R001` | Implementada |
| DQ-002 | Unicidad | Dedup por `id + fecha` | `dq/rules.md#R002` | Implementada |
| DQ-003 | TODO | TODO | TODO | TODO |

---

## 4. Umbrales de Aceptación y Rechazo

| Dimensión | Score Aceptable | Score de Alerta | Score de Rechazo |
|---|---|---|---|
| Completitud | ≥ 98% | 95–98% | < 95% |
| Unicidad | 100% | < 100% | < 100% |
| Validez | ≥ 99% | 97–99% | < 97% |
| Puntualidad | Antes de 08:00 | 08:00–08:30 | Después de 08:30 |

**Score DQ General**: Promedio ponderado de todas las dimensiones. Rechazo si < 95%.

---

## 5. Escalamiento por Falla DQ

| Severidad | Condición | Acción | Responsable | SLA de Resolución |
|---|---|---|---|---|
| **Crítico** | Campo clave con nulos / Score < 90% | Detener pipeline + notificar | TODO | 2 horas |
| **Mayor** | Completitud 90–95% | Alerta + revisión | TODO | 4 horas |
| **Menor** | Score 95–98% | Log + monitoreo | TODO | Próximo ciclo |

---

## 6. Aprobaciones

| Rol | Nombre | Fecha | Estado |
|---|---|---|---|
| Data Engineer | TODO | TODO | Pendiente |
| Data Steward | TODO | TODO | Pendiente |

---

**Template Version**: 1.0.0
**Template Location**: `contracts/templates/quality-contract-template.md`
