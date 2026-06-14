# Data Mapping

## Descripción
Mapeo de datos entre fuentes y transformaciones aplicadas.

## Flujo General

```
[Fuente 1] --\
[Fuente 2] ---+---> [Transformación] ---> [Dataset Final]
[Fuente 3] --/
```

## Mapeos por Fuente

### Mapeo 1: Source System A to Staging
**Fuente**: Source System A
**Destino**: Staging Layer
**Frecuencia**: Daily

| Campo Origen | Transformación | Campo Destino | Validación |
|-------------|----------------|---------------|-----------|
| source_id | CAST to UUID | user_id | NOT NULL |
| full_name | SPLIT | first_name, last_name | Length > 0 |
| email_addr | LOWER TRIM | email | VALID EMAIL |
| create_date | CONVERT TZ | created_at | IS DATE |

### Mapeo 2: Staging to Processing
**Fuente**: Staging Layer
**Destino**: Processing Layer
**Frecuencia**: Daily

| Campo Origen | Transformación | Campo Destino | Validación |
|-------------|----------------|---------------|-----------|
| user_id | -- | user_id | -- |
| email | JOIN with validation table | verified_email | EMAIL IN LIST |
| created_at | GROUP BY DATE | cohort_date | -- |

### Mapeo 3: Processing to Output
**Fuente**: Processing Layer
**Destino**: Output/Reporting
**Frecuencia**: Daily

| Campo Origen | Transformación | Campo Destino | Validación |
|-------------|----------------|---------------|-----------|
| user_id | -- | user_id | -- |
| verified_email | ANONYMIZE | hashed_email | NOT NULL |
| cohort_date | -- | cohort_date | -- |

## Transformaciones Complejas

### Feature Engineering
- user_tenure = current_date - created_at
- email_domain = EXTRACT(DOMAIN FROM email)
- user_segment = CASE WHEN tenure > 365 THEN 'LOYAL' ELSE 'NEW' END

### Agregaciones
- daily_active_users = COUNT(DISTINCT user_id) per day
- email_domain_distribution = COUNT(*) GROUP BY email_domain

## Data Quality Validations

- [ ] No valores nulos en campos requeridos
- [ ] Email válido
- [ ] Fechas en rango válido
- [ ] Datos duplicados identificados
- [ ] Valores fuera de rango detectados
