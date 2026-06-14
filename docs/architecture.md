# Arquitectura - Data Lab League

## Visión General

Este documento describe los patrones arquitectónicos soportados para productos de datos en Data Lab League.

## Principios Arquitectónicos

1. **Modularidad**: Componentes independientes, desacoplados, testables
2. **Reproducibilidad**: Mismo código → mismo resultado en cualquier ambiente
3. **Gobernanza**: Linaje de datos, DQ rules, auditoría y compliance
4. **Escalabilidad**: Capaz de crecer con volumen de datos
5. **Observabilidad**: Logging, metrics, alerting en todos los niveles

## Arquitecturas Soportadas

### 1. Databricks Medallion Architecture

**Descripción**: Enfoque de capas (Bronze/Silver/Gold) optimizado para transformación de datos en Databricks.

**Características**:
- Bronze: Raw data (ingestion)
- Silver: Cleaned, deduplicated, validated data
- Gold: Business-ready, aggregated data

**Cuándo usar**:
- Infraestructura en Databricks disponible
- Alto volumen de datos (100GB+)
- Necesidad de transformaciones complejas
- Equipo con experiencia en Apache Spark

**Documentación**: Ver [ADR-001-databricks-medallion.md](./adr/ADR-001-databricks-medallion.md)

### 2. SAS Analytics Architecture

**Descripción**: Platform-native approach aprovechando SAS Data Management, SAS Viya, y SAS Studio.

**Características**:
- SAS Data Management para gobernanza
- SAS Viya para modelado y análisis
- SAS Studio para desarrollo y ejecución

**Cuándo usar**:
- Infraestructura SAS existente (SAS 9.x, Viya)
- Requisitos de cumplimiento normativo estrictos
- Equipo con expertise en SAS
- Necesidad de integración con soluciones SAS legacy

**Documentación**: Ver [ADR-002-sas-analytics.md](./adr/ADR-002-sas-analytics.md)

## Decisiones Arquitectónicas (ADRs)

Toda decisión arquitectónica debe estar documentada en `docs/adr/`. Ver template en [ADR-template.md](./adr/ADR-template.md).

Ejemplos:
- [ADR-001: Databricks Medallion Architecture](./adr/ADR-001-databricks-medallion.md)
- [ADR-002: SAS Analytics Architecture](./adr/ADR-002-sas-analytics.md)

## Flujo de Decisión Arquitectónica

```
¿Nueva arquitectura requerida?
├─ NO → Usa arquitectura existente
└─ SÍ
   ├─ ¿Databricks disponible? → Evalúa Medallion
   ├─ ¿SAS disponible? → Evalúa SAS Analytics
   └─ Crea ADR con:
      - Contexto y problema
      - Opciones evaluadas
      - Decisión y justificación
      - Consecuencias
      - Ejemplo de implementación
```

## Estándares Cross-Architecture

Independiente de la arquitectura elegida:

- **Data Quality**: Todas las capas deben validar DQ rules
- **Linaje**: Documentar flujo de datos: source → transformations → output
- **Testing**: Unit tests para transformaciones, integration tests para pipelines
- **Logging**: Debug, info, warning, error levels con contexto
- **Configuración**: Environment variables, no hardcoding
- **Versionado**: Git para código; data versioning strategy para outputs

## Migración Entre Arquitecturas

Si necesitas cambiar de arquitectura:

1. Crear ADR documentando razones y plan
2. Implementar componentes en paralelo
3. Validar parity con arquitectura antigua
4. Migrar datos e histórico
5. Decommission arquitectura anterior
6. Actualizar documentación y evidencia

---

**Last Updated**: 2026-06-14
**Maintainer**: Data Lab League Team
