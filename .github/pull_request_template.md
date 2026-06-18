## Descripción del Pull Request

> Reemplaza este texto con una descripción clara de qué cambia y por qué.

## Tipo de Cambio

- [ ] Nueva funcionalidad
- [ ] Corrección de bug
- [ ] Refactoring (sin cambio funcional)
- [ ] Documentación
- [ ] Nuevo producto de datos / pipeline
- [ ] Cambio de esquema o datos
- [ ] Nuevo contrato de datos

---

## Checklist General

- [ ] El código sigue los estándares de `.github/copilot-instructions.md`
- [ ] Los tests pasan (`pytest`)
- [ ] La documentación está actualizada
- [ ] No se exponen secretos, tokens ni credenciales
- [ ] El código tiene logging y manejo de errores
- [ ] La evidencia en GitHub está actualizada

---

## Checklist de Contratos de Datos

> Completa esta sección si el PR modifica datos, esquemas, pipelines, reglas de negocio o productos de datos.

### Contrato de Datos

- [ ] ¿Se creó o actualizó el Data Product Contract correspondiente? (`contracts/data-products/`)
- [ ] ¿El contrato tiene owner de negocio y owner técnico definidos?
- [ ] ¿El grano del producto está documentado?
- [ ] ¿Los campos de salida están documentados con tipo y descripción?
- [ ] ¿El lineage está actualizado (`source → transformaciones → output`)?

### Calidad de Datos

- [ ] ¿Se creó o actualizó el Data Quality Contract? (`contracts/quality/`)
- [ ] ¿Las reglas DQ están implementadas en `dq/rules.md`?
- [ ] ¿Los umbrales de aceptación y rechazo están definidos?
- [ ] ¿Las cifras de control están documentadas?

### Interfaces

- [ ] ¿Se creó o actualizó el Interface Contract si hay nuevo origen o destino? (`contracts/interfaces/`)
- [ ] ¿El formato, esquema y frecuencia de entrega están documentados?

### SLA / SLO

- [ ] ¿Se actualizó el SLA/SLO Contract si cambian tiempos de entrega o disponibilidad? (`contracts/slas/`)
- [ ] ¿La hora de publicación, latencia y RTO están definidos?

### Gobierno y Seguridad

- [ ] ¿Se actualizó el Governance Contract si cambia clasificación de datos, PII o accesos? (`contracts/governance/`)
- [ ] ¿La clasificación de datos está definida (Público / Interno / Confidencial / Restringido)?
- [ ] ¿Los roles de acceso están documentados con mínimo privilegio?
- [ ] ¿Las políticas de retención están documentadas?

### Índice Maestro

- [ ] ¿Se registró el contrato en `contracts/contracts.md`?

---

## Checklist de Definition of Done (Contrato)

> Marca si el contrato cumple todos los criterios para ser considerado completo.

- [ ] Contrato creado o actualizado con nombre convencional
- [ ] Owner de negocio definido
- [ ] Owner técnico definido
- [ ] Consumidores documentados
- [ ] Fuentes definidas
- [ ] Grano definido
- [ ] Campos de salida documentados
- [ ] Reglas de negocio documentadas
- [ ] Reglas de calidad documentadas con umbrales
- [ ] SLA/SLO definido
- [ ] Clasificación de datos definida
- [ ] Controles de seguridad y privacidad definidos
- [ ] Lineage documentado
- [ ] Criterios de aceptación definidos y verificables
- [ ] Aprobación de negocio registrada (este PR)
- [ ] Aprobación técnica registrada (este PR)

---

## Archivos Modificados / Creados

> Lista los archivos relevantes de este PR.

- `TODO`

---

## Referencias

> Links a contratos, historias de usuario, evidencias, ADRs, tickets.

- Contrato relacionado: `contracts/TODO`
- Historia de usuario: `docs/user-stories/TODO`
- Evidencia: `evidence/TODO`
