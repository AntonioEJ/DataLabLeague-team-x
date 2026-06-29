# Prompt Template: Agent 08 - Compliance & Security

**Propósito**: Revisar seguridad OWASP Top 10, privacidad y cumplimiento normativo.

**Agente**: `@08_compliance-security`

**Input**: Código de Agent 04 + Governance de Agent 02  
**Output**: `security-review.md` + `compliance-checklist.md` + `vulnerability-scan.md`

---

## 📋 Template

```markdown
@08_compliance-security

Necesito revisar seguridad y cumplimiento para:

### Proyecto
[Nombre del caso de uso]

### Contexto de Seguridad
- **Datos sensibles**: [PII, financieros, médicos, etc.]
- **Regulaciones aplicables**: [LFPDPPP, CNBV, GDPR, etc.]
- **Ambiente**: [cloud, on-prem, híbrido]

### Áreas de Revisión
1. **OWASP Top 10**: [inyección, autenticación, exposición de datos, etc.]
2. **Privacidad**: [consentimiento, retención, derechos ARCO]
3. **Acceso**: [controles, auditoría, segregación de roles]
4. **Encriptación**: [en tránsito, en reposo]
5. **Gestión de secretos**: [credenciales, tokens, API keys]

### Checklist de Cumplimiento
- [ ] Sin credenciales hardcodeadas
- [ ] Credenciales en variables de entorno o secrets manager
- [ ] Logging de accesos sensitivos
- [ ] Validación de inputs
- [ ] Salida segura de datos
- [ ] Cumple LFPDPPP (México)
- [ ] Cumple CNBV (si aplica)

---

Por favor revisa:
✓ Vulnerabilidades OWASP
✓ Cumplimiento de privacidad
✓ Controles de acceso
✓ Gestión de secretos
✓ Auditoría y logging
```

---

## 📌 Next Step
→ **Agent 09: Deployment** para preparar despliegue

---

**Referencia**: [CLAUDE.md - Agent 08](../../CLAUDE.md#08--compliance--security-agent)
