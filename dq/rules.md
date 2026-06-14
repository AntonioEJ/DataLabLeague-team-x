# Data Quality Rules

## Descripción
Conjunto de reglas de calidad de datos para validación y monitoreo.

## Reglas Generales

### Regla 1: Completitud (Completeness)
**Descripción**: Verificar que no hay valores nulos en campos requeridos
**Severidad**: CRÍTICA
**Umbral**: >= 95% completo

```sql
SELECT 
  COUNT(*) as total_records,
  COUNT(field_name) as non_null_records,
  ROUND(100.0 * COUNT(field_name) / COUNT(*), 2) as completeness_pct
FROM dataset
```

---

### Regla 2: Validez (Validity)
**Descripción**: Verificar que los valores están dentro de rangos válidos
**Severidad**: ALTA
**Umbral**: >= 99% válido

```sql
SELECT 
  COUNT(*) as total_records,
  COUNT(CASE WHEN field_name ~ '^[A-Z][a-z]+$' THEN 1 END) as valid_records,
  ROUND(100.0 * COUNT(CASE WHEN field_name ~ '^[A-Z][a-z]+$' THEN 1 END) / COUNT(*), 2) as validity_pct
FROM dataset
```

---

### Regla 3: Unicidad (Uniqueness)
**Descripción**: Verificar que identificadores son únicos
**Severidad**: CRÍTICA
**Umbral**: 100% únicos

```sql
SELECT 
  COUNT(*) as total_records,
  COUNT(DISTINCT unique_field) as unique_records,
  CASE WHEN COUNT(*) = COUNT(DISTINCT unique_field) 
    THEN 'PASS' ELSE 'FAIL' END as status
FROM dataset
```

---

### Regla 4: Consistencia (Consistency)
**Descripción**: Verificar que valores están consistentes entre tablas
**Severidad**: MEDIA
**Umbral**: >= 98% consistente

```sql
SELECT 
  COUNT(DISTINCT a.id) as ids_in_a,
  COUNT(DISTINCT b.id) as ids_in_b,
  COUNT(DISTINCT CASE WHEN a.id = b.id THEN a.id END) as matching_ids
FROM table_a a
FULL OUTER JOIN table_b b ON a.id = b.id
```

---

### Regla 5: Exactitud (Accuracy)
**Descripción**: Verificar que valores son exactos contra fuente de verdad
**Severidad**: ALTA
**Umbral**: >= 99% exacto

Requiere comparación con source of truth (master data).

---

### Regla 6: Oportunidad (Timeliness)
**Descripción**: Verificar que datos se actualizan en tiempo
**Severidad**: MEDIA
**Umbral**: Update delay < SLA

```sql
SELECT 
  MAX(updated_at) as last_update,
  CURRENT_TIMESTAMP - MAX(updated_at) as time_since_update
FROM dataset
```

## Escalas de Severidad

| Nivel | Acción | Escalación | Timeout |
|-------|--------|-----------|---------|
| CRÍTICA | Stop Pipeline | Inmediata | 1h |
| ALTA | Alert + Continue | 4h | 4h |
| MEDIA | Log + Monitor | 24h | 24h |
| BAJA | Log Only | Semanal | 7d |

## Monitoreo y Alertas

- [ ] Rules ejecutadas automáticamente
- [ ] Resultados guardados en audit log
- [ ] Alertas generadas para fallos
- [ ] Reportes diarios de calidad
- [ ] Dashboards actualizados en tiempo real
