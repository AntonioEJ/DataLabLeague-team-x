# Data Sources

## Descripción
Inventario y documentación de todas las fuentes de datos del proyecto.

## Fuentes de Datos

### Fuente 1: Main Database
**Tipo**: Relacional (PostgreSQL)
**Ubicación**: prod-db.internal
**Puerto**: 5432
**Contacto**: DBA Team
**Acceso**: Via SSH Tunnel

**Tablas Principales**:
- users (1M registros)
- projects (10K registros)
- tasks (100K registros)

**SLA**:
- Disponibilidad: 99.9%
- Latencia: < 100ms
- Backup: Diario

---

### Fuente 2: Analytics Warehouse
**Tipo**: Data Warehouse (Snowflake)
**Ubicación**: analytics.snowflakecomputing.com
**Database**: ANALYTICS_DB
**Contacto**: Analytics Team
**Acceso**: Via Service Account

**Schemas Principales**:
- staging (raw data)
- processed (transformed)
- reporting (aggregated)

**SLA**:
- Disponibilidad: 99.95%
- Latencia: < 500ms
- Update frequency: Horaria

---

### Fuente 3: API External
**Tipo**: REST API
**URL**: https://api.external.com
**Contacto**: External Provider
**Acceso**: API Key

**Endpoints**:
- /users (GET)
- /projects (GET)
- /metrics (GET)

**Rate Limiting**: 1000 req/hora
**SLA**: 99%
**Update Frequency**: Real-time

---

## Matriz de Fuentes

| Fuente | Frecuencia | Latencia | Confiabilidad | Ownership |
|--------|-----------|----------|---------------|-----------|
| Main DB | Real-time | <100ms | 99.9% | IT Ops |
| Warehouse | Hourly | <500ms | 99.95% | Analytics |
| External API | Real-time | <1s | 99% | External |

## Acceso y Seguridad

- [ ] Credenciales almacenadas en KeyVault
- [ ] Acceso logged y auditado
- [ ] Encriptación en tránsito
- [ ] VPN requerida para prod
- [ ] Revisión trimestral de permisos

## Calidad Esperada

- Completeness: > 95%
- Validity: > 99%
- Consistency: Verificado
- Timeliness: Según SLA
