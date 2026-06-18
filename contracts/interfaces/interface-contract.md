# Interface Contract — Core Bancario to Cartera Comercial

> **Estado**: Draft | **Versión**: 0.1.0 | **ID**: IF-001

---

## Metadatos

| Campo | Valor |
|---|---|
| **ID Contrato** | IF-001 |
| **Versión** | 0.1.0 |
| **Estado** | Draft |
| **Fecha Creación** | 2026-06-18 |

---

## Partes

| Rol | Sistema | Equipo |
|---|---|---|
| **Proveedor** | Core Bancario (`CREDITOS.POSICION_DIARIA`) | TI Banca |
| **Consumidor** | Pipeline Cartera Comercial | Data Engineering |

---

## Descripción

Extracción diaria de posiciones de cartera comercial desde el Core Bancario hacia la capa Bronze del producto de datos Cartera Comercial.

**Frecuencia**: Diaria — disponible a las 01:00 CDMX
**Ventana de extracción**: 01:00 – 03:00 CDMX

---

## Formato y Protocolo

| Atributo | Valor |
|---|---|
| **Formato** | Parquet |
| **Encoding** | UTF-8 |
| **Compresión** | snappy |
| **Protocolo** | SFTP → S3 |
| **Ruta destino** | `s3://TODO/bronze/cartera-comercial/` |
| **Autenticación** | Certificado mTLS |

---

## Esquema

| Campo | Tipo | Obligatorio | Validación |
|---|---|---|---|
| `id_cliente` | `STRING` | Sí | NOT NULL |
| `id_producto` | `STRING` | Sí | NOT NULL |
| `fecha_corte` | `DATE` | Sí | NOT NULL, ISO 8601 |
| `saldo_capital` | `DECIMAL(18,2)` | Sí | NOT NULL, >= 0 |
| `tasa_interes` | `DECIMAL(6,4)` | Sí | > 0 AND <= 1 |
| `dias_atraso` | `INTEGER` | Sí | >= 0 |

---

## SLA de la Interfaz

| Indicador | Compromiso |
|---|---|
| Disponibilidad | Antes de 03:00 CDMX |
| Reintento máximo | 2 veces (con 30 min entre intentos) |
| Notificación de error | < 15 minutos |

---

**ID**: IF-001 | **Versión**: 0.1.0
