# Governance Assessment Template

**Agente**: 02 - Agent Data Governance  
**Fecha**: {{FECHA}}  
**Versión**: 1.0  
**Estado**: draft  
**CRISP-DM**: Business Understanding / Data Understanding

---

## 1. Identificación del Producto de Datos

- **Nombre**: {{NOMBRE_PRODUCTO}}
- **Área de negocio**: {{AREA}}
- **Objetivo**: {{OBJETIVO}}

---

## 2. Clasificación de Datos

| Entidad / Campo | Nivel de Clasificación | Justificación |
|---|---|---|
| | público / interno / confidencial / restringido | |

**Nivel más alto del producto**: {{NIVEL_CLASIFICACION}}

---

## 3. Ownership

| Rol | Nombre | Área | Contacto |
|---|---|---|---|
| **Data Owner** | | | |
| **Data Steward** | | | |
| **Custodio Técnico** | | | |

---

## 4. PII y Datos Sensibles

### 4.1 Campos PII Identificados

| Campo | Tabla | Tipo de PII | Control Requerido |
|---|---|---|---|
| | | Nombre / RFC / CURP / NSS / Dirección / Email / Teléfono / Otro | Enmascarar / Pseudoanonimizar / Cifrar |

### 4.2 Datos Sensibles (no PII)

| Campo | Tabla | Razón de Sensibilidad | Control |
|---|---|---|---|
| | | | |

### 4.3 Evaluación de Impacto en Privacidad (PIA)

- [ ] No se requiere PIA
- [ ] Se requiere PIA — responsable: {{RESPONSABLE_PIA}}

---

## 5. Finalidad de Uso

**Finalidad principal**: {{FINALIDAD}}

**Usos permitidos**:
- {{USO_1}}

**Restricciones de uso**:
- {{RESTRICCION_1}}

---

## 6. Controles de Acceso

**Principio rector**: Mínimo privilegio

| Rol | Tipo de Acceso | Restricciones | Ambiente |
|---|---|---|---|
| | lectura / escritura / admin | | dev / qa / prod |

**Controles técnicos requeridos**:
- [ ] MFA
- [ ] Row-Level Security
- [ ] Column Masking
- [ ] Cifrado en reposo
- [ ] Cifrado en tránsito
- [ ] Logs de auditoría

---

## 7. Data Catalog

- **Registro requerido**: Sí / No
- **Herramienta**: {{HERRAMIENTA_CATALOG}}
- **Responsable de registro**: {{RESPONSABLE}}
- **Metadatos requeridos**: esquema, owner, clasificación, reglas DQ, lineage

---

## 8. Lineage

**Flujo**:
```
{{SISTEMA_ORIGEN}} → {{TRANSFORMACION}} → {{DESTINO}}
```

**Nivel de documentación**:
- [ ] Tabla
- [ ] Columna
- [ ] Transformación

---

## 9. Data Contracts

| ID | Productor | Consumidor | Estado |
|---|---|---|---|
| DC-001 | | | nuevo / existente / a revisar |

---

## 10. Retención y Auditoría

- **Período de retención**: {{DIAS}} días
- **Política**: {{POLITICA_RETENCION}}
- **Auditoría de acceso requerida**: Sí / No

---

## 11. Riesgos Regulatorios

| ID | Riesgo | Regulación | Probabilidad | Impacto | Mitigación |
|---|---|---|---|---|---|
| GRSK-001 | | LFPDPPP / CNBV / Otra | alta / media / baja | alto / medio / bajo | |

---

## 12. Riesgos de Uso Indebido

| ID | Riesgo | Descripción | Mitigación |
|---|---|---|---|
| GRSK-X | | | |

---

## 13. Decisión de Gobierno

- [ ] **Aprobado** — puede avanzar a Agent Planner sin restricciones
- [ ] **Aprobado con condiciones** — ver sección 14
- [ ] **Rechazado** — ver issues

---

## 14. Condiciones para Agent Planner

_[Si aprobado con condiciones, describir qué debe considerar Agent Planner en la arquitectura y el diseño]_

1. {{CONDICION_1}}
2. {{CONDICION_2}}

---

## 15. Aprobaciones

| Rol | Nombre | Fecha | Notas |
|---|---|---|---|
| Data Owner | | | |
| Data Governance Lead | | | |
| CISO (si aplica) | | | |
| Compliance Officer (si aplica) | | | |
