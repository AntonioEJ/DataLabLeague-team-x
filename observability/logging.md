# Logging Strategy

## Descripción
Estrategia de logging para trazabilidad y debugging.

## Niveles de Log

| Nivel | Descripción | Ejemplo | Retención |
|-------|-------------|---------|-----------|
| DEBUG | Detalles internos | Variable values | 7 días |
| INFO | Eventos normales | Pipeline started | 30 días |
| WARN | Situaciones anormales | Data quality issue | 90 días |
| ERROR | Errores de negocio | Validation failed | 180 días |
| CRITICAL | Errores fatales | System down | 1 año |

## Formato de Log

```json
{
  "timestamp": "2024-06-14T10:30:45.123Z",
  "level": "INFO",
  "service": "pipeline",
  "component": "extraction",
  "user": "system",
  "request_id": "uuid",
  "message": "Successfully extracted 1000 records",
  "duration_ms": 2500,
  "status": "SUCCESS",
  "metadata": {
    "source": "main_db",
    "records": 1000,
    "batch_id": "batch_123"
  }
}
```

## Categorías de Logs

### Operacionales
- Pipeline execution
- Data extraction
- Processing steps
- Validations
- Distributions

### Seguridad
- Authentication attempts
- Authorization checks
- Data access events
- Configuration changes
- Audit events

### Performance
- Query duration
- Data volume processed
- Memory usage
- Error rates
- Latency metrics

## Almacenamiento

- **Tipo**: Centralized logging (ELK/Splunk/CloudWatch)
- **Retención**: Según tabla anterior
- **Índices**: Por fecha y nivel
- **Alertas**: Automáticas para errores críticos
- **Búsqueda**: Full-text habilitada

## Consultas Comunes

```
# Errores en últimas 24h
level:ERROR timestamp:>now-24h

# Slowest pipelines
service:pipeline duration_ms:>5000

# Security events
level:WARN OR level:ERROR tags:security

# Extraction issues
component:extraction status:FAILED
```

## Compliance

- [ ] Logs incluyen información de usuario
- [ ] Timestamps en UTC
- [ ] Request IDs para tracing distribuido
- [ ] Sensible data masked
- [ ] Archiving automático
