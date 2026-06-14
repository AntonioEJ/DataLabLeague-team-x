# Backend Instructions - Data Lab League

Instrucciones especializadas para desarrollo de código backend y APIs.

## Scope

Aplica a:
- Servicios backend (FastAPI, Flask, Django)
- ETL pipelines
- Data transformations
- Database interactions
- Message queues

## Estándares Adicionales

### 1. API Design

- RESTful endpoints con `GET`, `POST`, `PUT`, `DELETE`, `PATCH`
- Versionado de API: `/api/v1/`, `/api/v2/`
- Consistent response format:
  ```json
  {
    "status": "success|error",
    "data": {},
    "error": null,
    "timestamp": "ISO-8601"
  }
  ```
- HTTP status codes apropiados (200, 201, 400, 401, 403, 404, 500)

### 2. Database

- Use ORMs (SQLAlchemy, Django ORM) sobre raw SQL
- Connection pooling para production
- Migrations versionadas (Alembic, Django migrations)
- Transactions explícitas para operaciones multi-step
- Índices en columns frecuentemente buscadas

### 3. Dependencies

- Pin versions en `requirements.txt` o `pyproject.toml`
- Separar dev dependencies de production
- Revisar vulnerabilidades: `pip-audit`, `safety`
- Documentar por qué cada dependency

### 4. Logging en Backend

```python
# ✅ Correcto
logger.info("Processing batch", extra={
    "batch_id": batch_id,
    "record_count": len(records),
    "duration_ms": elapsed_ms
})

# ❌ Incorrecto
print(f"Processing batch {batch_id}")
```

### 5. Error Handling en APIs

```python
# ✅ Correcto
try:
    result = process_data(payload)
except ValidationError as e:
    logger.warning("Validation failed", extra={"error": str(e)})
    return {"status": "error", "error": str(e)}, 400
except Exception as e:
    logger.error("Unexpected error", exc_info=True)
    return {"status": "error", "error": "Internal server error"}, 500

# ❌ Incorrecto
result = process_data(payload)  # No error handling
```

### 6. Concurrency

- Use async/await para I/O-bound operations (databases, APIs)
- Thread pools para CPU-bound tasks
- Document deadlock/race condition risks

### 7. Testing Backend

- Unit tests para cada endpoint
- Integration tests para workflows
- Mock external dependencies (databases, APIs, message queues)
- Load testing para performance baselines

---

**Consulta**: `.github/copilot-instructions.md` para estándares generales que también aplican aquí.
