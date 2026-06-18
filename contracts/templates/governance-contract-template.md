# Governance Contract Template

> **Instrucciones**: Copia este template, nómbralo `[nombre-producto].governance-contract.md` y colócalo en `contracts/governance/`. Completa todos los campos `TODO`. Requiere aprobación de Data Governance Lead.

---

## Metadatos del Contrato

| Campo | Valor |
|---|---|
| **ID Contrato** | GV-XXX |
| **Producto de Datos** | TODO |
| **Versión** | 0.1.0 |
| **Estado** | Draft / Active / Deprecated |
| **Fecha Creación** | YYYY-MM-DD |
| **Última Actualización** | YYYY-MM-DD |
| **Revisión Próxima** | YYYY-MM-DD |
| **Jurisdicción** | TODO (e.g., México, UE/GDPR, EUA) |

---

## 1. Partes del Contrato

| Rol | Nombre | Equipo |
|---|---|---|
| **Data Owner** | TODO | TODO |
| **Data Steward** | TODO | TODO |
| **Data Governance Lead** | TODO | TODO |
| **Responsable de Seguridad** | TODO | TODO |
| **Responsable Legal / Compliance** | TODO | TODO |

---

## 2. Clasificación de Datos *

### Nivel de Confidencialidad

| Campo / Dataset | Clasificación | Justificación |
|---|---|---|
| Dataset completo | TODO | TODO |
| `id_cliente` | Interno | Identificador sin PII directo |
| `TODO_campo_PII` | Restringido | Contiene nombre o identificador personal |
| `TODO_campo` | Público | Datos agregados sin PII |

**Clasificaciones válidas**:
- **Público**: Datos de dominio público, sin restricciones
- **Interno**: Uso interno de la empresa, no publicable
- **Confidencial**: Acceso limitado a roles autorizados
- **Restringido**: Acceso muy limitado, datos regulados o críticos

---

## 3. Datos PII (Personally Identifiable Information) *

| Campo | Categoría PII | Tratamiento | Masking | Base Legal |
|---|---|---|---|---|
| `nombre_cliente` | PII Directo | Pseudoanonimización | Sí | Consentimiento |
| `email` | PII Directo | Enmascaramiento | Sí | Contrato |
| `rfc` | PII Fiscal | Encriptación | Sí | Obligación legal |
| `TODO_campo` | TODO | TODO | TODO | TODO |

**Campos con PII**: Sí / No

**Requiere DPA (Data Processing Agreement)**: Sí / No

---

## 4. Datos Sensibles (No PII)

| Campo | Tipo de Sensibilidad | Tratamiento | Justificación |
|---|---|---|---|
| `saldo_cuenta` | Financiero | Acceso con rol | Dato financiero regulado |
| `score_crediticio` | Financiero / Scoring | Solo lectura | Impacta decisiones de crédito |
| `TODO_campo` | TODO | TODO | TODO |

---

## 5. Roles de Acceso y Mínimo Privilegio *

| Rol | Tipo de Acceso | Campos Permitidos | Restricciones |
|---|---|---|---|
| `data-analyst` | SELECT | Todos excepto PII directo | Solo en ambiente analítico |
| `data-engineer` | SELECT + INSERT | Todos (pipeline) | Solo vía pipeline, no manual |
| `data-scientist` | SELECT | Datos anonimizados | Solo en sandbox |
| `auditor` | SELECT (read-only) | Logs y metadata | Tiempo limitado, auditado |
| `admin` | Full | Todos | Con doble aprobación |
| `TODO_rol` | TODO | TODO | TODO |

**Repositorio de roles**: TODO (e.g., IAM, LDAP, Azure AD)

**Proceso de solicitud de acceso**: TODO

---

## 6. Masking y Anonimización *

| Campo | Técnica | Regla | Roles Exentos |
|---|---|---|---|
| `nombre_cliente` | Pseudoanonimización | `HASH(nombre)` | `admin` |
| `email` | Masking parcial | `a***@***.com` | `data-engineer` |
| `rfc` | Encriptación | AES-256, clave manejada | `admin` |
| `TODO_campo` | TODO | TODO | TODO |

---

## 7. Retención de Datos *

| Dataset / Campo | Periodo de Retención | Acción al Vencer | Justificación Legal |
|---|---|---|---|
| Datos operacionales | 5 años | Archivado → eliminación | Obligación fiscal |
| Logs de auditoría | 7 años | Archivado | Normativa financiera |
| Datos de entrenamiento ML | 2 años | Revisión + eliminación | Política interna |
| PII de clientes activos | Durante vigencia del contrato | Anonimización | LFPDPPP |
| PII de clientes inactivos | 3 años tras baja | Eliminación | LFPDPPP |

---

## 8. Auditoría *

### ¿Qué se audita?

- [x] Acceso a datos (quién, cuándo, desde dónde)
- [x] Modificaciones o eliminaciones de datos
- [x] Exportaciones de datos
- [x] Cambios de roles o permisos
- [ ] TODO

### Logs de Auditoría

| Log | Herramienta | Retención | Acceso |
|---|---|---|---|
| Acceso a datos | TODO | 7 años | Solo auditores y compliance |
| Modificaciones | TODO | 7 años | Solo auditores |
| Pipeline executions | `observability/logging.md` | 2 años | Data Engineering |

---

## 9. Marco Regulatorio y Restricciones de Uso *

| Regulación | Aplica | Controles Implementados |
|---|---|---|
| LFPDPPP (México) | Sí / No | TODO |
| CNBV (Regulación financiera) | Sí / No | TODO |
| GDPR (UE) | Sí / No | TODO |
| CCPA (California) | Sí / No | TODO |
| PCI DSS | Sí / No | TODO |
| SOX | Sí / No | TODO |

**Restricciones de uso**:
- [ ] No compartir con terceros sin autorización escrita
- [ ] No usar para entrenamiento de modelos sin aprobación
- [ ] No exportar fuera del ambiente autorizado
- [ ] TODO restricción adicional

---

## 10. Transferencias de Datos

| Destino | Tipo | Mecanismo Aprobado | Requiere DPA | Estado |
|---|---|---|---|---|
| TODO_sistema | Interno | TODO | No | TODO |
| TODO_proveedor | Tercero | TODO | Sí | TODO |

---

## 11. Incidentes de Seguridad / Privacidad

| Fecha | Descripción | Afectados | Notificación | Resolución |
|---|---|---|---|---|
| - | - | - | - | - |

**Tiempo máximo para notificar incidente regulatorio**: 72 horas (GDPR) / TODO días (LFPDPPP)

---

## 12. Aprobaciones *

| Rol | Nombre | Fecha | Estado |
|---|---|---|---|
| Data Owner | TODO | TODO | Pendiente |
| Data Governance Lead | TODO | TODO | Pendiente |
| Compliance / Legal | TODO | TODO | Pendiente |
| CISO / Seguridad | TODO | TODO | Pendiente |

---

**Template Version**: 1.0.0
**Template Location**: `contracts/templates/governance-contract-template.md`
