# Data Product Contract Template

> **Instrucciones**: Copia este template, nómbralo `[nombre-producto].contract.md` y colócalo en `contracts/data-products/`. Completa todos los campos `TODO`. Los campos marcados con `*` son obligatorios.

---

## Metadatos del Contrato

| Campo | Valor |
|---|---|
| **ID Contrato** | DP-XXX |
| **Versión** | 0.1.0 |
| **Estado** | Draft / Active / Deprecated |
| **Fecha Creación** | YYYY-MM-DD |
| **Última Actualización** | YYYY-MM-DD |
| **Próxima Revisión** | YYYY-MM-DD |
| **PR de Aprobación** | # |

---

## 1. Identificación del Producto de Datos *

| Campo | Valor |
|---|---|
| **Nombre del Producto** | TODO |
| **Nombre Técnico** | `todo_nombre_tecnico` |
| **Descripción** | TODO: Descripción de 2-3 líneas del producto de datos |
| **Dominio de Negocio** | TODO (e.g., Crédito, Inversiones, Seguros) |
| **Fase CRISP-DM Principal** | TODO (Business Understanding / Deployment) |

---

## 2. Owners *

| Rol | Nombre | Equipo | Contacto |
|---|---|---|---|
| **Owner de Negocio** | TODO | TODO | TODO |
| **Owner Técnico** | TODO | TODO | TODO |
| **Data Steward** | TODO | TODO | TODO |
| **Productor de Datos** | TODO | TODO | TODO |

---

## 3. Objetivo y Alcance *

### Objetivo de Negocio
> TODO: ¿Qué decisión de negocio o KPI habilita este producto de datos?

### KPIs Asociados
- TODO KPI 1
- TODO KPI 2

### Alcance
> TODO: Qué incluye y qué NO incluye este producto de datos.

**Incluye**:
- TODO

**Excluye**:
- TODO

---

## 4. Consumidores *

| Consumidor | Equipo | Caso de Uso | Tipo de Acceso | Frecuencia | Contrato Vigente |
|---|---|---|---|---|---|
| TODO | TODO | TODO | Lectura | Diaria | Sí / No |

---

## 5. Fuentes de Datos *

| Fuente | Sistema | Tabla / Endpoint | Frecuencia de Actualización | Owner | Confiabilidad |
|---|---|---|---|---|---|
| TODO | TODO | TODO | TODO | TODO | TODO |

---

## 6. Grano *

> TODO: Descripción exacta de lo que representa **una fila** de este producto de datos.

**Ejemplo**: "Un registro representa la posición consolidada de un cliente en una cartera específica al cierre del día."

---

## 7. Campos de Salida *

| Nombre Campo | Tipo | Descripción | Obligatorio | PII | Clasificación | Regla de Negocio |
|---|---|---|---|---|---|---|
| `id_cliente` | `STRING` | Identificador único del cliente | Sí | No | Interno | Clave primaria, no nulo |
| `TODO_campo` | `TODO` | TODO | TODO | TODO | TODO | TODO |

---

## 8. Reglas de Negocio *

| ID Regla | Descripción | Campo(s) Afectados | Ejemplo |
|---|---|---|---|
| RN-001 | TODO | TODO | TODO |
| RN-002 | TODO | TODO | TODO |

---

## 9. Lineage de Datos *

```
[Fuente 1: TODO] ──→ [Transformación: TODO] ──→ [Producto: TODO] ──→ [Consumidor: TODO]
[Fuente 2: TODO] ──→
```

**Transformaciones principales**:
1. TODO: descripción de transformación 1
2. TODO: descripción de transformación 2

**Referencia al pipeline**: `pipeline/TODO`

---

## 10. Reglas de Calidad

> Ver contrato completo en [../quality/TODO.quality-contract.md](../quality/TODO.quality-contract.md)

**Resumen**:

| Dimensión | Umbral Mínimo | Umbral Aceptable |
|---|---|---|
| Completitud | 95% | 98% |
| Validez | 99% | 99.5% |
| Unicidad | 100% | 100% |
| Puntualidad | SLA: antes de 08:00 | SLA: antes de 07:00 |

---

## 11. SLA / SLO

> Ver contrato completo en [../slas/TODO.sla-slo.md](../slas/TODO.sla-slo.md)

**Resumen**:

| Indicador | Compromiso |
|---|---|
| Disponibilidad | 99.5% mensual |
| Hora de publicación | 08:00 (hora de CDMX) |
| Latencia máxima | 15 minutos desde fuente |
| Frescura máxima | T+1 día |
| RTO (Recovery Time) | 4 horas |

---

## 12. Seguridad y Privacidad

| Campo | Valor |
|---|---|
| **Clasificación General** | Confidencial / Público / Restringido |
| **Contiene PII** | Sí / No |
| **Datos Sensibles** | TODO (e.g., saldos, scoring, comportamiento) |
| **Cifrado en Tránsito** | TLS 1.2+ |
| **Cifrado en Reposo** | AES-256 |
| **Acceso Requiere** | TODO (e.g., rol `data-analyst`, VPN) |
| **Masking Requerido** | TODO campos: TODO |

---

## 13. Gobierno

> Ver contrato completo en [../governance/TODO.governance-contract.md](../governance/TODO.governance-contract.md)

**Clasificación de Datos**: TODO

**Retención**: TODO años

**Jurisdicción**: TODO (e.g., México, GDPR)

---

## 14. Data Catalog

| Campo | Valor |
|---|---|
| **Nombre en Catálogo** | TODO |
| **Colección** | TODO |
| **Tags** | TODO |
| **URL en Catálogo** | TODO |

---

## 15. Criterios de Aceptación *

- [ ] TODO CA-001: Los datos se publican antes de las 08:00
- [ ] TODO CA-002: Completitud > 98%
- [ ] TODO CA-003: Ningún campo clave es nulo
- [ ] TODO CA-004: Los IDs son únicos
- [ ] TODO CA-005: Valores dentro de rangos esperados

---

## 16. Versionamiento

| Versión | Fecha | Cambios | Autor | PR |
|---|---|---|---|---|
| 0.1.0 | YYYY-MM-DD | Creación inicial | TODO | # |

**Política de Versionamiento**:
- `MAJOR`: Cambio breaking (eliminación de campos, cambio de grano)
- `MINOR`: Nuevos campos, nuevas reglas
- `PATCH`: Corrección de documentación, actualización de umbrales

---

## 17. Aprobaciones *

| Rol | Nombre | Fecha | Estado |
|---|---|---|---|
| Owner de Negocio | TODO | TODO | Pendiente |
| Owner Técnico | TODO | TODO | Pendiente |
| Data Governance Lead | TODO | TODO | Pendiente |

---

**Template Version**: 1.0.0
**Template Location**: `contracts/templates/data-contract-template.md`
