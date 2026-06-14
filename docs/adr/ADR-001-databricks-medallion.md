# ADR-001: Databricks Medallion Architecture

**Status**: Accepted

**Date**: 2026-06-14

**Authors**: Data Lab League Engineering Team

---

## Problema (Context)

Data Lab League necesita una arquitectura de datos escalable, modular y gobernada para procesar volúmenes crecientes de datos en Databricks. La solución debe permitir:

- Ingesta de datos desde múltiples fuentes
- Transformación incremental de datos
- Validación de calidad en cada etapa
- Linaje de datos transparente
- Escalabilidad a nivel enterprise

**Constraints**:
- Infraestructura disponible: Databricks con Apache Spark
- Team skills: Python, PySpark, SQL
- Requisito: Gobernanza de datos con audit trail

---

## Opciones Evaluadas

### Opción 1: Databricks Medallion Architecture (Bronze/Silver/Gold)

**Descripción**: Arquitectura de capas (medallion) con clara separación entre ingesta, transformación y consumo.

**Pros**:
- Arquitectura estándar en Databricks, bien documentada
- Separación clara de concerns entre capas
- Facilita linaje de datos y auditoría
- Escalable a petabytes con Spark
- Permite gobernanza y DQ rules en cada capa
- Muchos patterns y best practices disponibles

**Contras**:
- Requiere gestión manual de múltiples datasets
- Overhead de almacenamiento (datos duplicados en capas)
- Complejidad inicial de setup

**Costo Estimado**: Medium

**Esfuerzo de Implementación**: Medium

---

### Opción 2: Flat Data Lake (Single Layer)

**Descripción**: Todos los datos en una sola capa con transformaciones aplicadas al query time.

**Pros**:
- Simplicity inicial
- Menos storage overhead
- Fewer moving parts

**Contras**:
- Difícil de gobernar y auditar
- Query performance sufre con datos sucios
- No hay clara separación entre raw y processed
- Riesgo de data quality issues en downstream

**Costo Estimado**: Low

**Esfuerzo de Implementación**: Low

---

### Opción 3: Data Vault 2.0

**Descripción**: Arquitectura normalizada con hub, link, satellite tables.

**Pros**:
- Excelente para auditoria y histórico
- Maneja cambios dimensionales complejos

**Contras**:
- Curva de aprendizaje alta
- Complejidad significativa
- Overkill para mayoría de casos de uso

**Costo Estimado**: High

**Esfuerzo de Implementación**: High

---

## Decisión (Decision)

**Elegimos: Databricks Medallion Architecture (Bronze/Silver/Gold)**

**Justificación**:

1. **Balance óptimo**: Equilibra simplicity vs. gobernanza
2. **Standard en industria**: Widely adopted, proven patterns
3. **Alineación con infraestructura**: Databricks native, optimizado para Spark
4. **Escalabilidad**: Proven a petabyte scale
5. **Gobernanza**: Cada capa permite DQ rules y auditoría
6. **Team alignment**: Nuestro equipo tiene skills en Spark/Python

**Trade-offs aceptados**:
- Overhead de almacenamiento (datos en 3 capas)
- Complejidad de orquestación multi-capa
- Mantenimiento de múltiples job definitions

---

## Consecuencias (Consequences)

### Positivas

- Clara separación de concerns (ingesta, transformación, consumo)
- Linaje de datos trazable end-to-end
- DQ rules aplicables en cada capa
- Facilita debugging y auditoría
- Escalable según crecimiento de datos
- Permite especialización: data engineers (Silver), analytics engineers (Gold)

### Negativas

- Duplicación de datos consume almacenamiento
- Orchestration es más compleja (3 stages vs. 1)
- Require manual data lineage management (si no hay Databricks lineage API)

### Futuras Consideraciones

- Evaluar Databricks Lineage APIs para automatizar tracking
- Considerar Databricks Unity Catalog para gobernanza centralizada
- Posible transición a Delta Sharing si requerimos data marketplace

---

## Estructura de Capas

### Bronze (Ingestion)

```
/data/bronze/
├── source1_yyyy_mm_dd.parquet
├── source2_yyyy_mm_dd.parquet
└── ...
```

**Características**:
- Raw data as-is from source
- Minimalist transformations (schema inference, partitioning)
- Audit columns: ingestion_date, source, filename
- SLA: Daily or streaming ingestion
- Retention: 12-24 months (or per policy)

**Ejemplo Code**:
```python
# notebooks/bronze/ingest_customers.py
from pyspark.sql import SparkSession
import logging

logger = logging.getLogger(__name__)

spark = SparkSession.builder.appName("ingest_customers").getOrCreate()

source_path = "/mnt/sources/crm/customers/"
bronze_path = "/data/bronze/customers"

df = spark.read.parquet(source_path)
df = df.withColumn("ingestion_date", spark.current_date())
df = df.withColumn("source", lit("crm_system"))

df.write.mode("overwrite").partitionBy("ingestion_date").parquet(bronze_path)
logger.info(f"Ingested {df.count()} records to bronze")
```

---

### Silver (Transformation)

```
/data/silver/
├── customers/
├── orders/
├── products/
└── ...
```

**Características**:
- Cleaned, deduplicated, validated data
- Business rules applied
- DQ rules enforced
- Normalized schemas
- Audit columns: transformation_date, rule_version

**Ejemplo Code**:
```python
# notebooks/silver/transform_customers.py
from pyspark.sql.functions import col, when, coalesce
import logging

logger = logging.getLogger(__name__)

spark = SparkSession.builder.appName("transform_customers").getOrCreate()

# Read from bronze
df_bronze = spark.read.parquet("/data/bronze/customers")

# DQ: Remove nulls on key columns
df_clean = df_bronze.filter(col("customer_id").isNotNull())

# Normalize email
df_clean = df_clean.withColumn(
    "email",
    when(col("email").isNotNull(), lower(trim(col("email")))).otherwise(None)
)

# Deduplicate: keep latest by ingestion_date
df_dedup = df_clean.withColumn(
    "row_num",
    row_number().over(Window.partitionBy("customer_id").orderBy(desc("ingestion_date")))
).filter(col("row_num") == 1).drop("row_num")

# Add audit
df_dedup = df_dedup.withColumn("transformation_date", spark.current_date())

df_dedup.write.mode("overwrite").parquet("/data/silver/customers")
logger.info(f"Transformed {df_dedup.count()} records to silver")
```

---

### Gold (Consumption)

```
/data/gold/
├── analytics/
│   ├── customer_metrics/
│   ├── order_analytics/
├── bi_layer/
│   ├── dim_customers/
│   ├── fact_orders/
```

**Características**:
- Business-ready aggregations
- BI/Analytics optimized
- Star schema or denormalized
- Serve dashboards, ML models, reports
- Audit columns: publication_date, version

**Ejemplo Code**:
```python
# notebooks/gold/create_customer_metrics.py
from pyspark.sql.functions import count, sum as spark_sum, avg
import logging

logger = logging.getLogger(__name__)

spark = SparkSession.builder.appName("customer_metrics").getOrCreate()

# Read from silver
df_silver = spark.read.parquet("/data/silver/customers")

# Create metrics
df_metrics = df_silver.groupBy("customer_segment").agg(
    count("customer_id").alias("total_customers"),
    avg("lifetime_value").alias("avg_ltv"),
    spark_sum("total_orders").alias("total_orders")
).withColumn("publication_date", spark.current_date())

df_metrics.write.mode("overwrite").parquet("/data/gold/analytics/customer_metrics")
logger.info(f"Published {df_metrics.count()} metric records")
```

---

## Herramientas y Ecosistema

- **Workflow Orchestration**: Databricks Workflows / Apache Airflow
- **Data Quality**: Great Expectations / Databricks expectations
- **Testing**: Pytest para unit tests; dbt tests para transformations
- **Monitoring**: Databricks dashboards + logging

---

## Roadmap de Implementación

**Fase 1** (Mes 1-2): Bronze layer setup
- Ingesta de primeras 3 fuentes
- Setup de audit columns

**Fase 2** (Mes 3-4): Silver layer
- Transformaciones core
- DQ rules y validación

**Fase 3** (Mes 5-6): Gold layer
- Analytics datasets
- BI layer setup

**Fase 4** (Mes 7+): Gobernanza y observabilidad
- Lineage tracking
- Unity Catalog integration

---

## Referencias

- [Databricks Medallion Architecture](https://www.databricks.com/blog/2022/06/24/use-the-medallion-multi-hop-architecture.html)
- [Our architecture.md](../architecture.md)

---

## Historial

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-06-14 | Data Lab League Team | Creación del ADR |
