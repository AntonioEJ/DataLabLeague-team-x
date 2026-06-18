# Governance Contract — Cartera Comercial

> **Estado**: Draft | **Versión**: 0.1.0 | **ID**: GV-001

---

## Metadatos

| Campo | Valor |
|---|---|
| **ID Contrato** | GV-001 |
| **Producto de Datos** | Cartera Comercial |
| **Versión** | 0.1.0 |
| **Estado** | Draft |
| **Jurisdicción** | México (LFPDPPP, CNBV) |
| **Data Product Contract** | [../data-products/cartera-comercial.contract.md](../data-products/cartera-comercial.contract.md) |

---

## Clasificación de Datos

| Campo / Dataset | Clasificación |
|---|---|
| Dataset completo | Confidencial |
| `id_cliente` | Interno |
| `saldo_capital` | Confidencial |
| `tasa_interes` | Confidencial |
| `dias_atraso` | Confidencial |

---

## PII

| Contiene PII | Justificación |
|---|---|
| No | Los IDs de cliente son identificadores internos sin datos personales directos. Los datos financieros son sensibles pero no PII según LFPDPPP. |

> **Nota**: Si en el futuro se incorpora `nombre`, `rfc` o `email`, este contrato debe actualizarse y requiere DPA.

---

## Roles de Acceso

| Rol | Acceso | Restricciones |
|---|---|---|
| `data-analyst` | SELECT | Solo ambiente analítico, VPN requerida |
| `data-engineer` | SELECT + INSERT | Solo vía pipeline, no acceso manual a prod |
| `data-scientist` | SELECT | Solo datos de sandbox anonimizados |
| `auditor` | SELECT (read-only, logs) | Acceso temporal con aprobación |
| `admin` | Full | Doble aprobación, auditado |

---

## Retención

| Dataset | Retención | Acción al Vencer |
|---|---|---|
| Datos operacionales | 5 años | Archivado → eliminación controlada |
| Logs de pipeline | 2 años | Eliminación automática |
| Logs de auditoría de acceso | 7 años | Archivado |

---

## Regulaciones Aplicables

| Regulación | Aplica | Control |
|---|---|---|
| CNBV (Regulación Financiera) | Sí | Retención 5 años, acceso auditado |
| LFPDPPP | Sí (datos relacionados con personas) | Mínimo privilegio, no exportación sin autorización |
| GDPR | No | N/A |

---

## Aprobaciones

| Rol | Nombre | Estado |
|---|---|---|
| Data Owner | TODO | Pendiente |
| Data Governance Lead | TODO | Pendiente |
| Compliance / Legal | TODO | Pendiente |

---

**ID**: GV-001 | **Versión**: 0.1.0
