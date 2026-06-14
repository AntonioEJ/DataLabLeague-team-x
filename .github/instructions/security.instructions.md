# Security Instructions - Data Lab League

Instrucciones especializadas para seguridad, secrets management, y compliance.

## Scope

Aplica a:
- Credenciales y secretos
- Acceso a datos sensibles
- Compliance regulatorio
- Auditoría y logging de seguridad
- OWASP Top 10

## Principios de Seguridad

1. **Defense in Depth**: Múltiples capas de protección
2. **Least Privilege**: Acceso mínimo necesario
3. **Fail Secure**: Fallar seguro, no abierto
4. **Never Trust User Input**: Validar y sanitizar siempre
5. **Security by Default**: Secure defaults, opt-in para riesgos

## Secrets Management

### ❌ NUNCA Hacer Esto

```python
# Hardcoded secrets
DB_PASSWORD = "admin123"
API_KEY = "sk-abc123xyz"
AWS_ACCESS_KEY = "AKIAIOSFODNN7EXAMPLE"

# In git (¡NUNCA!)
git add config.py  # Si contiene secrets → BAD
```

### ✅ Correcto: Environment Variables

```python
import os
from dotenv import load_dotenv

load_dotenv()  # Load from .env (gitignored)

DB_PASSWORD = os.environ["DB_PASSWORD"]
API_KEY = os.environ.get("API_KEY")  # Default safe
AWS_ACCESS_KEY = os.environ["AWS_ACCESS_KEY_ID"]
```

### .env File (Gitignored)

```bash
# .env (NEVER COMMIT)
DB_PASSWORD=secure_password_here
API_KEY=sk-abc123xyz
AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE
AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
GOOGLE_SHEETS_CREDENTIALS=/path/to/credentials.json
```

### .gitignore

```
# Never commit these
.env
.env.local
*.key
*.pem
credentials.json
secrets/
config/production.yml
```

### Secrets en GitHub

```bash
# Use GitHub Secrets for CI/CD
# Settings → Secrets and variables → Actions → New repository secret
# Name: DB_PASSWORD
# Value: (actual password)

# Access in workflows:
# env:
#   DB_PASSWORD: ${{ secrets.DB_PASSWORD }}
```

## Data Access Control

### Row-Level Security

```python
# ✅ Correcto: Filtrar datos por usuario
@app.get("/customers")
def get_customers(current_user: User):
    """Solo usuarios ven sus propios clientes"""
    query = db.query(Customer).filter(
        Customer.owned_by_user_id == current_user.id
    )
    return query.all()

# ❌ Incorrecto: Todos ven todos los datos
def get_customers():
    return db.query(Customer).all()
```

### PII (Personally Identifiable Information)

```python
from data.privacy import mask_pii

# Sensitive fields que requieren máscara
SENSITIVE_FIELDS = ["email", "phone", "ssn", "credit_card"]

def export_customer_data(customer):
    """Exportar datos sin exponer PII"""
    data = customer.to_dict()
    for field in SENSITIVE_FIELDS:
        if field in data:
            data[field] = mask_pii(data[field])
    return data
```

## OWASP Top 10

### 1. SQL Injection

```python
# ❌ Vulnerable
query = f"SELECT * FROM users WHERE id = {user_id}"
db.execute(query)

# ✅ Seguro: Parameterized queries
query = "SELECT * FROM users WHERE id = ?"
db.execute(query, (user_id,))

# ✅ Better: ORM (SQLAlchemy)
user = db.query(User).filter(User.id == user_id).first()
```

### 2. Authentication & Authorization

```python
from fastapi import HTTPException, Depends
from fastapi.security import HTTPBearer

security = HTTPBearer()

@app.get("/protected")
async def protected_route(credentials = Depends(security)):
    """Verificar token en cada request"""
    user = verify_token(credentials.credentials)
    if not user:
        raise HTTPException(status_code=401)
    return {"message": f"Hello {user.name}"}
```

### 3. Sensitive Data Exposure

```python
# ✅ Hash passwords con bcrypt
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

hashed = pwd_context.hash("plain_password")
is_valid = pwd_context.verify("plain_password", hashed)
```

### 4. XML External Entity (XXE)

```python
# ❌ Vulnerable a XXE
import xml.etree.ElementTree as ET
root = ET.fromstring(xml_input)  # Can load external entities

# ✅ Seguro: Deshabilitar entidades externas
from defusedxml import ElementTree
root = ElementTree.fromstring(xml_input)
```

### 5. Broken Access Control

```python
# ✅ Verificar permisos en CADA endpoint
@app.delete("/projects/{project_id}")
def delete_project(project_id: int, current_user: User):
    project = db.query(Project).get(project_id)
    
    # Verificar ownership
    if project.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized")
    
    db.delete(project)
```

### 6. Security Misconfiguration

```python
# ✅ Buenas prácticas
DEBUG = False  # NUNCA True en production
ALLOWED_HOSTS = ["example.com"]  # Whitelist
CSRF_TRUSTED_ORIGINS = ["https://example.com"]
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
```

### 7. Injection (Command, OS)

```python
# ❌ Vulnerable
import os
os.system(f"convert {user_input} output.jpg")

# ✅ Seguro: Use subprocess con array
import subprocess
subprocess.run(["convert", user_input, "output.jpg"], check=True)
```

## Encryption at Rest & in Transit

```python
# ✅ Encryption en transit (TLS/HTTPS)
# Usar HTTPS siempre, HSTS headers
# TLS 1.2+, strong ciphers

# ✅ Encryption at rest
from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)

encrypted = cipher.encrypt(b"sensitive data")
decrypted = cipher.decrypt(encrypted)
```

## Audit & Logging

```python
import logging

logger = logging.getLogger(__name__)

# Log security events
logger.warning("Login attempt failed", extra={
    "user_id": user_id,
    "ip": request.remote_addr,
    "timestamp": datetime.now().isoformat()
})

logger.info("Data export", extra={
    "user_id": user.id,
    "exported_records": 10000,
    "timestamp": datetime.now().isoformat()
})

# ✅ NUNCA log passwords, tokens, etc.
logger.error(f"Auth failed: {password}")  # ❌ BAD
logger.error(f"Auth failed for user {user_id}")  # ✅ OK
```

## Dependency Scanning

```bash
# Check for vulnerable dependencies
pip-audit

# Update vulnerable packages
pip install --upgrade vulnerable_package

# Lock versions
pip freeze > requirements.txt
```

## GDPR & Data Protection

### Data Retention

```python
from datetime import datetime, timedelta

# Delete old data per policy
def cleanup_old_records():
    """Delete records older than 1 year"""
    cutoff = datetime.now() - timedelta(days=365)
    db.query(LogEntry).filter(LogEntry.created_at < cutoff).delete()
    db.commit()
    logger.info("Cleaned up old log entries")
```

### Right to be Forgotten

```python
@app.delete("/users/{user_id}")
def delete_user_data(user_id: int, current_user: User):
    """GDPR: Right to be forgotten"""
    if user_id != current_user.id:
        raise HTTPException(status_code=403)
    
    # Delete all user data
    db.query(User).filter(User.id == user_id).delete()
    db.query(UserPreferences).filter(User.id == user_id).delete()
    db.commit()
    
    logger.info(f"Deleted user {user_id} per GDPR request")
```

## Security Checklist

- ✅ No hardcoded secrets
- ✅ Environment variables para credentials
- ✅ HTTPS/TLS siempre
- ✅ Input validation y sanitización
- ✅ Parameterized queries (no SQL injection)
- ✅ Authentication checks en cada endpoint
- ✅ Authorization (role-based access control)
- ✅ Sensitive data masked/encrypted
- ✅ Audit logging de eventos importantes
- ✅ Dependency scanning regular

---

**Consulta**: 
- `.github/copilot-instructions.md` para estándares generales
- OWASP Top 10: https://owasp.org/www-project-top-ten/
- GDPR: https://gdpr-info.eu/
