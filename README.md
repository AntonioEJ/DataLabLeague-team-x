# DataLabLeague - Team X

## Descripción

Proyecto de DataLabLeague para el equipo X enfocado en datos, calidad e innovación.

## Estructura del Proyecto

- `docs/` - Documentación del proyecto
- `src/` - Código fuente
- `tests/` - Pruebas unitarias
- `dq/` - Reglas de calidad de datos
- `pipeline/` - Pipelines de datos
- `observability/` - Logging y métricas
- `evidence/` - Evidencia de cumplimiento
- `scorecard/` - Auto-evaluación y métricas
- `contracts/` - Contratos de datos, calidad, interfaces, SLA/SLO y gobierno

## Contracts

Los contratos son artefactos de primera clase de este repositorio. Toda transformación, interfaz o producto de datos debe tener sus contratos formalizados antes de pasar a producción.

**Ubicación**: `/contracts/`

**¿Qué son los contratos?** Documentos que definen compromisos formales sobre:
- Qué datos se producen y cómo (Data Product Contract)
- Qué calidad deben tener (Data Quality Contract)
- Cómo se entregan entre sistemas (Interface Contract)
- Cuándo y con qué disponibilidad (SLA/SLO Contract)
- Cómo se gobiernan (Governance Contract)

**Cómo crear uno nuevo**:
1. Elige el template en `contracts/templates/`
2. Nómbralo según la [convención de nombres](contracts/README.md#convención-de-nombres)
3. Colócalo en la subcarpeta correspondiente
4. Regístralo en `contracts/contracts.md`
5. Abre un PR con el checklist de contratos

**Relación con Data Quality**: Las reglas en `dq/rules.md` implementan los compromisos formalizados en `contracts/quality/`.

**Relación con CRISP-DM**: Los contratos se crean y actualizan en cada fase del ciclo CRISP-DM. Ver `contracts/README.md` para la tabla de correspondencia.

**Revisión en PR**: Todo PR que modifique datos, esquemas o pipelines debe completar el checklist de contratos del PR template.

## Inicio Rápido

1. Clonar el repositorio
2. Instalar dependencias
3. Ejecutar tests

## Documentación

Consulte la documentación en `docs/` para más detalles.

## Contribuidores

- Jose Antonio Esparza
- Team 
