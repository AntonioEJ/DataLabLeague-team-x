# MCP Instructions - Data Lab League

Instrucciones especializadas para configuración y desarrollo de Model Context Protocol (MCP) servers.

## Scope

Aplica a:
- Configuración de MCP servers
- Integración con GitHub Copilot
- Conexión a resources personalizados
- Extensiones de Copilot

## MCP Architecture

MCP permite que Copilot acceda a:
- Bases de datos
- APIs externas
- Sistemas de archivos
- Servicios en cloud
- Custom tools

## Estándares MCP

### 1. Server Configuration

```json
{
  "mcpServers": {
    "data-lab": {
      "command": "python",
      "args": ["./mcp_server.py"],
      "env": {
        "API_KEY": "${env:DATA_LAB_API_KEY}"
      }
    }
  }
}
```

**Reglas**:
- Nunca hardcodear credenciales
- Usar `${env:VAR_NAME}` para variables de ambiente
- Documentar dependencias requeridas
- Versionar configuración en `version` field

### 2. Resource Definitions

```python
class MCPResource:
    """Define resources accesibles a Copilot"""
    
    name: str  # Nombre único
    description: str  # Breve descripción
    uri: str  # Identificador
    mime_type: str  # Tipo de contenido
    read_only: bool  # Si es modificable
```

**Reglas**:
- Resource names deben ser descriptivos: `data_lab_queries`, no `resource1`
- Incluir descripción clara de qué expone
- Marcar `read_only: true` para operaciones de solo lectura
- Validar permisos antes de exponer

### 3. Tool Definitions

```python
@mcp_tool
def execute_query(sql: str) -> dict:
    """Ejecuta queries SQL contra data warehouse
    
    Args:
        sql: SQL query (SELECT only)
    
    Returns:
        Query results como dict/JSON
    
    Raises:
        ValueError: Si query no es SELECT
        ConnectionError: Si DW no responde
    """
```

**Reglas**:
- Incluir docstring completo (Google style)
- Type hints obligatorios
- Validación de inputs (SQL injection, permissions)
- Return types deben ser serializables JSON

### 4. Security

- ✅ Validar **TODOS** los inputs desde Copilot
- ✅ Usar allowlists para queries permitidas
- ✅ Implementar rate limiting
- ✅ Log de acceso: quién llamó qué, cuándo
- ❌ NO exponer credenciales en responses
- ❌ NO permitir arbitrary code execution

**Ejemplo seguro**:
```python
# ✅ Correcto: Allowlist de queries
ALLOWED_QUERIES = [
    "SELECT COUNT(*) FROM customers",
    "SELECT * FROM orders WHERE date > ?",
]

@mcp_tool
def query_data(query_id: int) -> list:
    """Ejecuta query preaprobada"""
    if query_id not in range(len(ALLOWED_QUERIES)):
        raise ValueError("Invalid query_id")
    
    query = ALLOWED_QUERIES[query_id]
    return execute_sql(query)

# ❌ Incorrecto: Arbitrary SQL
@mcp_tool
def query_data(sql: str):
    return execute_sql(sql)  # SQL injection risk!
```

### 5. Error Handling

```python
@mcp_tool
def fetch_data(source: str) -> dict:
    try:
        return {"status": "ok", "data": load_data(source)}
    except ConnectionError as e:
        logger.error("Connection failed", extra={"source": source})
        return {"status": "error", "error": "Service unavailable"}
    except ValueError as e:
        return {"status": "error", "error": str(e)}
```

### 6. Testing MCP

```bash
# Verificar server inicia
mcp-cli start-server --config settings.json

# Test tools
mcp-cli call-tool --tool query_data --args '{"sql": "SELECT 1"}'

# Test resources
mcp-cli list-resources --server data-lab
```

### 7. Documentation

Cada MCP server debe tener:
- README con setup instructions
- List de resources expuestos
- List de tools disponibles
- Security model
- Rate limits y quotas
- Example usage en `.github/examples/`

---

## Configuración en copilot-instructions.md

```markdown
## Model Context Protocol (MCP)

- Usa MCP servers para acceso a resources externos
- Configura en `~/.config/code/settings.json`
- Documenta: README, resources, tools disponibles
- Valida TODOS los inputs
- Implementa allowlists, no blocklists
- Log de acceso y auditoría
```

---

**Consulta**: `.github/copilot-instructions.md` para estándares generales.
