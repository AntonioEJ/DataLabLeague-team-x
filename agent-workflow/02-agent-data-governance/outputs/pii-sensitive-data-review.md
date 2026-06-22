# Revisión de PII y Datos Sensibles

**Agente**: 02 - Agent Data Governance  
**Fecha**: _pendiente_  
**Versión**: 1.0  
**Estado**: draft

## Marco Regulatorio Aplicable

- LFPDPPP (Ley Federal de Protección de Datos Personales en Posesión de los Particulares)
- CNBV (regulación financiera aplicable)
- Políticas internas de privacidad

## Inventario de Campos PII

| Tabla / Entidad | Campo | Tipo PII | Sensibilidad | Control Requerido |
|---|---|---|---|---|
| _pendiente_ | _pendiente_ | Directo / Indirecto | _pendiente_ | Enmascarar / Pseudoanonimizar / Restringir |

## Inventario de Datos Sensibles (No PII)

| Tabla / Entidad | Campo | Razón de Sensibilidad | Control Requerido |
|---|---|---|---|
| _pendiente_ | _pendiente_ | _pendiente_ | _pendiente_ |

## Controles Definidos

| Control | Aplica Para | Responsable de Implementar |
|---|---|---|
| Enmascaramiento en ambientes no productivos | PII directo | Custodio Técnico |
| Pseudoanonimización | PII indirecto | Custodio Técnico |
| Cifrado en tránsito y reposo | Datos restringidos | Custodio Técnico |
| Acceso solo con aprobación explícita | Datos sensibles | Data Owner |
| Auditoría de acceso | PII + sensibles | Custodio Técnico |

## Evaluación de Impacto en Privacidad (PIA)

_[¿Se requiere una Evaluación de Impacto en Privacidad? Sí / No. Si sí, ¿quién la realiza?]_

## Decisión de Privacidad

- [ ] Sin PII ni datos sensibles — sin restricciones adicionales
- [ ] Con PII — controles implementados o planificados
- [ ] Con datos sensibles — revisión adicional requerida
- [ ] Requiere PIA antes de continuar
