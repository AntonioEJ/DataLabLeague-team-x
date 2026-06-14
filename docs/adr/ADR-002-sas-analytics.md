# ADR-002: SAS Analytics Architecture

**Status**: Accepted

**Date**: 2026-06-14

**Authors**: Data Lab League Engineering Team

---

## Problema (Context)

Organizaciones con infraestructura SAS existente (SAS 9.x o Viya) requieren una arquitectura de datos moderna que aproveche inversión SAS mientras mantiene gobernanza, escalabilidad y compliance.

**Constraints**:
- Infraestructura disponible: SAS Viya o SAS 9.x
- Requisitos de compliance: auditoría, data lineage, encryption
- Team skills: SAS, SAS Data Management, SAS Studio
- Integración requerida: legacy systems, SAS reports, Viya analytics

---

## Opciones Evaluadas

### Opción 1: SAS Analytics Architecture (SAS Viya + SAS Data Management)

**Descripción**: Platform-native approach leveraging SAS Viya for analytics/ML, SAS Data Management for governance, SAS Studio for development.

**Pros**:
- Platform nativa, fully integrated
- Excelente gobernanza y compliance (GDPR, HIPAA ready)
- SAS Data Management centraliza políticas DQ
- SAS Viya = machine learning, time series, forecasting
- SAS Studio = IDE moderna con debugging
- Audit trail automático en todas las operaciones
- Security integrado: roles, row-level security

**Contras**:
- Licensing cost puede ser alto
- Curva de aprendizaje para Viya
- Menor community vs. Spark/Python
- Escalabilidad limitada vs. distributed systems

**Costo Estimado**: High (licensing)

**Esfuerzo de Implementación**: Medium

---

### Opción 2: Hybrid Approach (SAS + Open Source)

**Descripción**: Combinar SAS Data Management con Apache Spark / Python.

**Pros**:
- Flexibility de open source
- SAS para governance, Spark para compute

**Contras**:
- Complejidad de mantener dos stacks
- Duplicación de data management logic
- Problemas de sincronización

**Costo Estimado**: High (licensing + engineering)

**Esfuerzo de Implementación**: High

---

### Opción 3: Cloud Migration (AWS/Azure)

**Descripción**: Migrar completamente a cloud analytics (BigQuery, Redshift, etc.).

**Pros**:
- Escalabilidad cloud-native
- Costo variable (OPEX vs. CAPEX)
- Menos operational overhead

**Contras**:
- Riesgo alto de migración
- Pérdida de inversión SAS
- Team retraining requerido

**Costo Estimado**: High (migration + new tools)

**Esfuerzo de Implementación**: Very High

---

## Decisión (Decision)

**Elegimos: SAS Analytics Architecture (SAS Viya + SAS Data Management)**

**Justificación**:

1. **Maximiza inversión existente**: Aprovecha infraestructura SAS ya en place
2. **Gobernanza nativa**: SAS Data Management es enterprise-grade
3. **Compliance**: Auditoría automática, lineage, encryption
4. **Integración**: Conecta con legacy systems SAS sin redevelopment
5. **Equipo**: Nuestro equipo tiene expertise SAS

**Trade-offs aceptados**:
- Menor flexibility vs. open source
- Community más pequeña para troubleshooting
- Licensing costs vs. open source alternatives

---

## Consecuencias (Consequences)

### Positivas

- Gobernanza centralizada y automatizada
- Compliance ready para regulaciones
- Linaje de datos integrado
- Analytics y ML dentro de la misma plataforma
- Auditoría completa (quién hizo qué, cuándo)
- Seguridad nivel enterprise (encryption, roles, SSO)

### Negativas

- Licensing costs significativos
- Escalabilidad limitada para big data (vs. Spark)
- Menos comunidad online para support
- Algunos advanced analytics requieren complementos pagos

### Futuras Consideraciones

- Evaluar SAS Viya 4 para arquitectura cloud-native
- Considerar integración con Lakehouse (Delta Lake + SAS)
- Posible migration a open standards si costs justifican

---

## Arquitectura General

```
┌─────────────────────────────────────────────────────────────────┐
│                        SAS Analytics Stack                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Data Sources ─→ SAS Data Management ─→ SAS Viya ─→ Consumers │
│  (Files, DB)     (Governance, DQ)     (Analytics, ML)  (BI)    │
│                                                                 │
│  • Data lineage tracking    • Data quality rules             │
│  • Metadata management      • Statistical modeling           │
│  • Audit trail              • Machine learning               │
│  • Security policies        • Forecasting                    │
│                             • Time series analysis           │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Capas Lógicas

### 1. Data Management Layer (SAS Data Management)

**Responsabilidad**: Ingesta, gobernanza, data quality

**Características**:
- Metadata repository centralizado
- Data lineage mapping
- Quality rules y validaciones
- Classification y tagging
- Audit logging
- Security policies

**Ejemplo Configuración**:
```sas
/* SAS Data Management Configuration */
proc cas;
session casauto;

/* Define data quality rules */
DATA quality_rules;
    input rule_name $ source_table $ check_logic $;
    datalines;
    customer_id_not_null customers customer_id IS NOT NULL
    email_valid customers email REGEX ^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$
    order_date_recent orders order_date >= TODAY() - 365
    ;
run;

/* Register lineage */
proc metalib;
    create mtlib="CASAUTO.FOUNDATION" group="DATA_MANAGEMENT";
run;
```

---

### 2. Transformation Layer (SAS Studio / SAS Viya)

**Responsabilidad**: Transformaciones, limpieza, agregaciones

**Características**:
- SAS Studio IDE modern
- Procedimientos nativos SAS
- CAS (in-memory analytics engine)
- Versioning de código
- Scheduling integrado

**Ejemplo Transformación**:
```sas
/* notebooks/silver/transform_customers.sas */

libname mydata cas sessref=casauto;

/* Read from bronze */
data work.customers_raw;
    set mydata.bronze_customers;
run;

/* Clean and deduplicate */
proc sort data=work.customers_raw 
    out=work.customers_dedup 
    nodupkey;
    by customer_id descending ingestion_date;
run;

/* Normalize emails */
data work.customers_clean;
    set work.customers_dedup;
    
    /* DQ: Remove nulls */
    if missing(customer_id) then delete;
    
    /* Normalize email */
    if not missing(email) then
        email = lowcase(trim(email));
    
    /* Add audit */
    transformation_date = today();
    
    keep customer_id email customer_name transformation_date ingestion_date;
run;

/* Write to silver */
proc casutil;
    load data=work.customers_clean
        out=mydata.silver_customers
        replace;
run;

/* Log transformation */
proc printto log="/var/logs/transformations.log" append;
run;
```

---

### 3. Analytics Layer (SAS Viya)

**Responsabilidad**: Modeling, forecasting, statistical analysis

**Características**:
- SAS Viya microservices (Visual Data Mining, Forecasting, etc.)
- Python/R integration
- Model registration y deployment
- REST APIs para integración

**Ejemplo Análisis**:
```python
# notebooks/gold/customer_analytics.py
import swat  # SAS SWAT (Scripting Wrapper for Analytics Transfer)

# Connect to CAS
conn = swat.CAS(hostname='cas.sas.com', port=5570)

# Load cleaned data
df = conn.read_csv('/data/silver/customers.csv')

# Statistical analysis
customer_summary = conn.groupby('customer_segment').agg({
    'customer_id': 'count',
    'lifetime_value': ['mean', 'std'],
    'total_orders': 'sum'
}).casout(name='CUSTOMER_METRICS', replace=True)

# Output to CAS table
customer_summary.to_table('GOLD_CUSTOMER_METRICS')
```

---

### 4. Consumption Layer (Reports, Dashboards, ML Models)

**Output Targets**:
- SAS Viya reports and dashboards
- External BI tools (Tableau, Power BI via APIs)
- Batch scoring jobs
- Real-time REST APIs

---

## Data Quality en SAS

```sas
/* Define DQ rules */
proc dataQuality;
    rules = {
        {
            name = 'customer_id_not_null',
            condition = 'NOT MISSING(customer_id)',
            severity = 'ERROR'
        },
        {
            name = 'email_valid',
            condition = 'PRXMATCH("^[A-Z0-9._%+-]+@[A-Z0-9.-]+\\.[A-Z]{2,}$", email)',
            severity = 'WARNING'
        }
    };
    
    /* Apply rules */
    proc qualityKnowledge;
        importRules from=rules;
        applyRules data=mydata.silver_customers
                  out=mydata.silver_customers_validated
                  reportOut=work.quality_report;
    run;
run;
```

---

## Gobernanza y Compliance

### Auditoría Automática

```sas
/* SAS Data Management tracks automatically: */
- User: quién accedió
- Action: qué hizo (read/modify/delete)
- Timestamp: cuándo
- Data: qué datos
- Source/Target: lineage completo
```

### Data Classification

```sas
proc metalib;
    /* Tag sensitive data */
    modify TABLE=CUSTOMERS / TAGS=('PII', 'CONFIDENTIAL', 'GDPR');
    modify COLUMN=email / TAGS=('PII', 'CONTACT_INFO');
    modify COLUMN=ssn / TAGS=('PII', 'HIGHLY_SENSITIVE');
run;
```

---

## Setup y Provisioning

**Requisitos**:
- SAS Viya 3.5+ o SAS 9.4+
- CAS engine (para performance)
- SAS Studio (IDE)
- SAS Data Management
- SAS Forecast Server (si needed)

**Installation Steps** (simplificado):
1. Provisionar SAS Viya en cloud (AWS, Azure, GCP) o on-premise
2. Configure SAS Data Management
3. Setup metadata repository
4. Configure security y roles
5. Connect data sources
6. Test transformations

---

## Roadmap de Implementación

**Fase 1** (Semana 1-2): Setup infrastructure
- Provisionar SAS Viya
- Configure SAS Data Management
- Setup metadata repository

**Fase 2** (Semana 3-4): Data ingestion
- Connect primeras 3 fuentes
- Define data quality rules
- Test lineage tracking

**Fase 3** (Semana 5-6): Transformations
- Build transformations en SAS Studio
- Implement DQ validation
- Schedule jobs

**Fase 4** (Semana 7-8): Analytics
- Create analytic datasets
- Deploy reports/dashboards

---

## Referencias

- [SAS Viya Documentation](https://documentation.sas.com/)
- [SAS Data Management](https://www.sas.com/en_us/software/data-management.html)
- [Our architecture.md](../architecture.md)

---

## Historial

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-06-14 | Data Lab League Team | Creación del ADR |
