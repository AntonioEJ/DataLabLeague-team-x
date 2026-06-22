# Requerimientos de Control de Acceso

**Agente**: 02 - Agent Data Governance  
**Fecha**: _pendiente_  
**Estado**: draft

## Principio Rector

**Mínimo privilegio**: cada usuario, sistema o rol tiene acceso únicamente a lo que necesita para su función.

## Matriz de Acceso por Entidad

| Entidad | Rol | Tipo de Acceso | Restricciones |
|---|---|---|---|
| _pendiente_ | Data Owner | lectura + escritura supervisada | sin datos PII en claro |
| _pendiente_ | Analista | solo lectura | vista enmascarada |
| _pendiente_ | Sistema ETL | lectura de origen | solo campos necesarios |
| _pendiente_ | Consumidor API | lectura | solo campos autorizados |

## Controles Técnicos Requeridos

| Control | Aplica Para | Prioridad |
|---|---|---|
| Autenticación MFA | Acceso a datos confidenciales | alta |
| Row-Level Security (RLS) | Datos segmentados por organización/región | media |
| Column Masking | PII en ambientes no productivos | alta |
| Cifrado en reposo | Datos restringidos | alta |
| Cifrado en tránsito | Todas las integraciones | alta |
| Logs de auditoría | Acceso a PII y datos sensibles | alta |
| Rotación de credenciales | Acceso a DBs y APIs | media |

## Ambientes

| Ambiente | Acceso a PII Real | Acceso a Datos Sensibles |
|---|---|---|
| Desarrollo (dev) | No — usar datos sintéticos | No |
| Pruebas (qa) | No — usar datos enmascarados | No |
| Producción (prod) | Sí — solo roles autorizados | Sí — solo roles autorizados |

## Responsable de Configurar Controles

_[Equipo de seguridad o Custodio Técnico]_
