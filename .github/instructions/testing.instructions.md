# Testing Instructions - Data Lab League

Instrucciones especializadas para estrategias de testing y cobertura de código.

## Scope

Aplica a:
- Unit tests
- Integration tests
- Data quality tests
- Performance tests
- End-to-end tests

## Principios de Testing

1. **Test Pyramid**: Muchos unit tests, algunos integration tests, pocos E2E tests
2. **Arrange-Act-Assert (AAA)**: Setup → Ejecutar → Verificar
3. **DRY in Tests**: Reutilizar fixtures, eliminar duplication
4. **Fast Feedback**: Tests deben ejecutar rápido (<100ms ideal)
5. **Deterministic**: Mismo resultado siempre, no flaky tests

## Unit Tests

```python
# tests/data/test_transformations.py
import pytest
from data.transformations import clean_customer_data

class TestCustomerTransformations:
    
    @pytest.fixture
    def sample_data(self):
        """Arrange: Preparar datos de prueba"""
        return {
            "customer_id": 123,
            "email": "  JOHN@EXAMPLE.COM  ",
            "name": "John Doe"
        }
    
    def test_normalize_email_lowercase(self, sample_data):
        """Act: Ejecutar transformación"""
        result = clean_customer_data(sample_data)
        
        """Assert: Verificar resultado"""
        assert result["email"] == "john@example.com"
    
    def test_handle_missing_email(self):
        """Test edge case: email nulo"""
        result = clean_customer_data({"customer_id": 456})
        assert result["email"] is None
    
    def test_invalid_customer_id(self):
        """Test error case: ID inválido"""
        with pytest.raises(ValueError):
            clean_customer_data({"customer_id": -1})
```

**Reglas**:
- 1 concepto por test
- Nombres descriptivos: `test_<feature>_<scenario>`
- Fixtures para datos reutilizables
- Exceptions testadas explícitamente
- Cobertura target: 80%+

## Integration Tests

```python
# tests/integration/test_database_layer.py
import pytest
from data.database import CustomerRepository

class TestDatabaseIntegration:
    
    @pytest.fixture
    def test_db(self):
        """Setup test database"""
        db = setup_test_db()
        yield db
        teardown_test_db()
    
    def test_save_and_retrieve_customer(self, test_db):
        """Test database round-trip"""
        repo = CustomerRepository(test_db)
        
        # Arrange
        customer = {"id": 1, "name": "Alice"}
        
        # Act
        repo.save(customer)
        retrieved = repo.get(1)
        
        # Assert
        assert retrieved["name"] == "Alice"
```

**Reglas**:
- Usa databases/services reales o muy realistas
- Isola cambios: cada test tiene setup/teardown
- Mock solo dependencias externas no controladas (APIs)
- Ejecuta en paralelo si posible

## Data Quality Tests

```python
# tests/quality/test_data_quality.py
import pytest
from data.quality import validate_customers

def test_no_duplicate_ids():
    """DQ Rule: customer_id debe ser único"""
    data = [
        {"customer_id": 1, "email": "a@test.com"},
        {"customer_id": 1, "email": "b@test.com"},  # Duplicate!
    ]
    
    issues = validate_customers(data)
    assert any(issue["rule"] == "duplicate_id" for issue in issues)

def test_email_format():
    """DQ Rule: email debe ser válido"""
    data = [{"customer_id": 1, "email": "invalid-email"}]
    
    issues = validate_customers(data)
    assert any(issue["rule"] == "invalid_email" for issue in issues)

def test_required_fields():
    """DQ Rule: No nulls en campos requeridos"""
    data = [{"customer_id": None, "email": "test@example.com"}]
    
    issues = validate_customers(data)
    assert any(issue["rule"] == "null_required_field" for issue in issues)
```

**Reglas**:
- Test cada DQ rule explícitamente
- Incluir casos positivos y negativos
- Documentar regla que valida

## Performance Tests

```python
# tests/performance/test_transformation_speed.py
import pytest
import time
from data.transformations import process_large_dataset

@pytest.mark.performance
def test_process_1m_records_under_5s():
    """Transformar 1M records debe ser rápido"""
    data = generate_test_data(1_000_000)
    
    start = time.time()
    result = process_large_dataset(data)
    duration = time.time() - start
    
    assert duration < 5.0
    assert len(result) == 1_000_000
```

**Reglas**:
- Mark tests con `@pytest.mark.performance`
- Benchmark contra baseline conocido
- Ejecuta en hardware consistente
- Documenta assumptions (machine, data size)

## Mocking y Fixtures

```python
# tests/conftest.py (Pytest auto-discovers)
import pytest
from unittest.mock import Mock

@pytest.fixture
def mock_api_client():
    """Mock para API externa"""
    client = Mock()
    client.get.return_value = {"status": 200, "data": []}
    return client

@pytest.fixture
def mock_database():
    """Mock para database"""
    db = Mock()
    db.query.return_value = [{"id": 1, "name": "Test"}]
    return db

# Usar en tests
def test_with_mock(mock_api_client):
    response = mock_api_client.get("/endpoint")
    assert response["status"] == 200
```

**Reglas**:
- Mock external services (APIs, DBs on CI)
- Use real services en integration tests
- Define fixtures en `conftest.py`
- Documenta qué cada mock hace

## Test Execution

```bash
# Todos los tests
pytest

# Solo unit tests
pytest tests/unit/

# Solo tests rápidos
pytest -m "not performance"

# Con cobertura
pytest --cov=src/ --cov-report=html

# Paralelo (rápido)
pytest -n auto

# Verbose output
pytest -v

# Stop on first failure
pytest -x
```

## CI/CD Integration

```yaml
# .github/workflows/test.yml
name: Tests
on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
      - run: pip install -r requirements-dev.txt
      - run: pytest --cov=src/ --cov-report=xml
      - run: codecov  # Upload coverage
```

## Coverage Targets

| Component | Target |
|-----------|--------|
| Logic (models, transforms) | 85%+ |
| API handlers | 80%+ |
| Utils | 70%+ |
| Configuration | Not required |
| Tests | N/A |

## Pre-commit Hooks

```bash
# .git/hooks/pre-commit
#!/bin/bash
pytest --cov=src/ || exit 1
```

---

**Consulta**: `.github/copilot-instructions.md` para estándares generales de Python.
