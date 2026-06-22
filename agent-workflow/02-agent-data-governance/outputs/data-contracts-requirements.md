# Requerimientos de Data Contracts

**Agente**: 02 - Agent Data Governance  
**Fecha**: _pendiente_  
**Estado**: draft

## Qué es un Data Contract

Acuerdo formal entre el **productor** y el **consumidor** de datos que define:
- Esquema esperado
- Calidad mínima
- Frecuencia de entrega
- SLAs
- Responsabilidades ante incumplimiento

## Inventario de Data Contracts Requeridos

| ID | Productor | Consumidor | Entidad | Estado |
|---|---|---|---|---|
| DC-001 | _pendiente_ | _pendiente_ | _pendiente_ | nuevo / existente / a revisar |

## Campos Mínimos por Data Contract

- `contract_id`: identificador único
- `producer`: sistema o equipo productor
- `consumer`: sistema o equipo consumidor
- `entity`: nombre de la entidad o tabla
- `schema`: campos, tipos, obligatoriedad
- `quality_sla`: DQ score mínimo esperado
- `delivery_frequency`: diaria / horaria / en tiempo real
- `latency_sla`: tiempo máximo de entrega
- `owner`: responsable del contrato
- `start_date` / `review_date`
- `violation_protocol`: qué pasa si se rompe el contrato

## Data Contracts Existentes

_[Lista de contratos ya firmados relacionados con este producto]_

## Contratos a Crear

_[Lista de contratos nuevos requeridos]_

## Herramienta de Data Contracts

_[Soda, Great Expectations, OpenDataContract, manual, etc.]_
