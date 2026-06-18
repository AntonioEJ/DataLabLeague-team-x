# Interface Contract Template

> **Instrucciones**: Copia este template, nómbralo `[origen]-to-[destino].interface-contract.md` y colócalo en `contracts/interfaces/`. Completa todos los campos `TODO`.

---

## Metadatos del Contrato

| Campo | Valor |
|---|---|
| **ID Contrato** | IF-XXX |
| **Versión** | 0.1.0 |
| **Estado** | Draft / Active / Deprecated |
| **Fecha Creación** | YYYY-MM-DD |
| **Última Actualización** | YYYY-MM-DD |

---

## 1. Partes del Contrato *

| Rol | Sistema | Equipo | Contacto |
|---|---|---|---|
| **Proveedor** | TODO (e.g., SAP, CRM, Oracle) | TODO | TODO |
| **Consumidor** | TODO (e.g., producto-datos-x) | TODO | TODO |
| **Intermediario** | TODO (e.g., pipeline, ETL) | TODO | TODO |

---

## 2. Descripción de la Interfaz *

> TODO: Descripción breve de qué datos entrega esta interfaz, con qué propósito y con qué frecuencia.

**Caso de uso**: TODO

**Frecuencia**: Diaria / Horaria / Batch semanal / Tiempo real / On-demand

**Ventana horaria**: TODO (e.g., "Disponible entre 02:00 y 06:00 para extracción")

---

## 3. Formato y Protocolo *

| Atributo | Valor |
|---|---|
| **Formato de entrega** | CSV / Parquet / JSON / Avro / Delta / API REST |
| **Encoding** | UTF-8 |
| **Compresión** | gzip / snappy / sin compresión |
| **Protocolo de transferencia** | SFTP / S3 / API REST / Kafka / JDBC |
| **Autenticación** | OAuth2 / API Key / Certificado mTLS |
| **Ruta / Endpoint** | `s3://TODO/ruta/` o `https://TODO/api/v1/endpoint` |

---

## 4. Esquema de Datos *

| Campo | Tipo | Longitud | Obligatorio | Descripción | Ejemplo | Reglas de Validación |
|---|---|---|---|---|---|---|
| `id_cliente` | `STRING` | 20 | Sí | Identificador único del cliente | `CLI-0001234` | NOT NULL, REGEX `^CLI-[0-9]{7}$` |
| `fecha_operacion` | `DATE` | - | Sí | Fecha de la operación | `2026-06-18` | NOT NULL, formato ISO 8601 |
| `monto` | `DECIMAL(18,2)` | - | Sí | Monto de la operación | `12500.00` | NOT NULL, >= 0 |
| `TODO_campo` | `TODO` | TODO | TODO | TODO | TODO | TODO |

**Encoding de valores especiales**:
- Nulos: `NULL` (no usar `""` ni `"N/A"`)
- Fechas: ISO 8601 (`YYYY-MM-DD`)
- Decimales: punto (`.`) como separador decimal

---

## 5. Validaciones Requeridas por el Consumidor

> El consumidor debe validar estas reglas al recibir los datos.

| ID | Validación | Acción si Falla |
|---|---|---|
| V-001 | Registro no vacío (`COUNT(*) > 0`) | Rechazar lote y notificar |
| V-002 | `id_cliente` NOT NULL | Rechazar fila |
| V-003 | `fecha_operacion` no futura | Rechazar fila |
| V-004 | Checksum de archivo coincide | Rechazar lote |
| V-005 | TODO | TODO |

---

## 6. Manejo de Errores

| Escenario | Comportamiento del Proveedor | Comportamiento del Consumidor |
|---|---|---|
| Archivo no llega a tiempo | Notificar al consumidor | Esperar X horas, escalar |
| Archivo corrupto / malformado | Reenviar archivo | Rechazar y notificar |
| Schema incorrecto | TODO | Rechazar y notificar |
| Campos faltantes obligatorios | TODO | Rechazar fila |
| Valores fuera de rango | TODO | Log + cuarentena |

**Canal de notificación**: TODO (e.g., email, Teams, PagerDuty)

**Tiempo máximo de respuesta a error**: TODO horas

---

## 7. Compatibilidad y Versionado

**Política de compatibilidad**:
- Nuevos campos opcionales → backward compatible
- Eliminación de campos → versión MAJOR + aviso con 30 días de anticipación
- Cambio de tipo → versión MAJOR + aviso con 30 días de anticipación
- Cambio de formato → requiere acuerdo escrito en nuevo contrato

**Versión actual del esquema**: 1.0.0

**Historial de cambios de esquema**:

| Versión | Fecha | Cambio | Impacto |
|---|---|---|---|
| 1.0.0 | YYYY-MM-DD | Versión inicial | - |

---

## 8. SLA de la Interfaz

| Indicador | Compromiso |
|---|---|
| Disponibilidad mensual | 99.5% |
| Hora de entrega (ventana) | TODO |
| Latencia máxima | TODO |
| Reintento máximo | TODO veces |
| Tiempo de notificación de error | < 30 minutos |

---

## 9. Aprobaciones

| Rol | Nombre | Fecha | Estado |
|---|---|---|---|
| Proveedor (Técnico) | TODO | TODO | Pendiente |
| Consumidor (Técnico) | TODO | TODO | Pendiente |
| Arquitecto de Datos | TODO | TODO | Pendiente |

---

**Template Version**: 1.0.0
**Template Location**: `contracts/templates/interface-contract-template.md`
