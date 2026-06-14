# Data Dictionary

## Descripción
Diccionario de datos para todas las entidades y campos del proyecto.

## Template

### Entidad: [Nombre]
**Descripción**: [Descripción]
**Fuente**: [Sistema/Base de datos]
**Propietario**: [Área/Persona]

| Campo | Tipo | Rango/Valores | Nuleable | Descripción | Ejemplo |
|-------|------|--------------|---------|------------|---------|
| field_1 | String | | NO | Descripción | valor |
| field_2 | Integer | 0-100 | YES | Descripción | 50 |
| field_3 | Date | YYYY-MM-DD | NO | Descripción | 2024-01-01 |

---

## Entidades

### Entidad: User
**Descripción**: Información de usuarios del sistema
**Fuente**: System Database
**Propietario**: IT Department

| Campo | Tipo | Descripción |
|-------|------|------------|
| user_id | UUID | Identificador único |
| name | String | Nombre del usuario |
| email | String | Email único |
| created_at | Timestamp | Fecha de creación |
| status | Enum | ACTIVE, INACTIVE |

### Entidad: Project
**Descripción**: Proyectos de DataLabLeague
**Fuente**: Project Management System
**Propietario**: Product Team

| Campo | Tipo | Descripción |
|-------|------|------------|
| project_id | UUID | Identificador único |
| name | String | Nombre del proyecto |
| phase | String | Fase CRISP-DM |
| status | Enum | PLANNING, ACTIVE, COMPLETED |

### Entidad: Data Quality
**Descripción**: Métricas de calidad de datos
**Fuente**: Data Quality System
**Propietario**: Data Governance Team

| Campo | Tipo | Descripción |
|-------|------|------------|
| quality_id | UUID | Identificador único |
| dataset_name | String | Nombre del dataset |
| completeness | Decimal | % de registros completos |
| validity | Decimal | % de valores válidos |
| timestamp | Timestamp | Fecha de medición |
