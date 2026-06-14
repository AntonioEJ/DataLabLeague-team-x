# Data User Story Template

## Plantilla para Historias de Usuario Enriquecidas con Datos

---

## Identificación

**ID**: [US-XXX]
**Título**: [Título descriptivo de la historia]
**Epic**: [Epic a la que pertenece]
**Estimación**: [Story Points]
**Prioridad**: [Critical/High/Medium/Low]

## Descripción

**Como** [rol de usuario]
**Quiero** [acción que quiere realizar]
**Para que** [beneficio o valor que obtendrá]

## Contexto de Datos

### Fuentes de Datos Requeridas

| Fuente | Tabla/Entidad | Campos | Volumen Estimado | Frecuencia |
|--------|---------------|--------|------------------|-----------|
| | | | | |

### Diccionario de Datos Relevante

| Campo | Tipo | Descripción | Validación |
|-------|------|-------------|-----------|
| | | | |

### Data Quality Requerida

- Completitud: ____%
- Validez: ____%
- Consistencia: ____%
- Timeliness: ____

### Mapeo de Datos

```
[Fuente A] --\
[Fuente B] ---+---> [Transformación] ---> [Output]
[Fuente C] --/
```

## Criterios de Aceptación

```gherkin
Scenario: [Nombre del escenario]
  Given [Precondición]
  When [Acción]
  Then [Resultado esperado]
  And [Validación adicional]
```

Ejemplos:
- [ ] Criterio 1
- [ ] Criterio 2
- [ ] Criterio 3

## Dependencias

**Dependencias técnicas**:
- [ ] Prerequisito 1
- [ ] Prerequisito 2

**Dependencias de datos**:
- [ ] Data source 1 disponible
- [ ] Calidad validada

**Dependencias de equipo**:
- [ ] Review de datos completado
- [ ] Aprobación de propietario

## Notas Técnicas

- Complejidad de integración: [Alta/Media/Baja]
- Riesgos identificados: [Listar]
- Supuestos documentados: [Listar]

## Definición de Hecho

Que cumpla con todos los criterios de aceptación y que:
- [ ] Requisitos de datos entendidos
- [ ] Código revisado
- [ ] Tests escritos y pasando
- [ ] Data quality validada
- [ ] Documentación actualizada
- [ ] Aprobado por product owner

## Notas

[Espacio para notas adicionales]

---

**Creado por**: [Nombre]
**Fecha de creación**: [Fecha]
**Última actualización**: [Fecha]
