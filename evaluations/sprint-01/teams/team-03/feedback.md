# Feedback — Team 03 (Team Carteras)

**Sprint**: Sprint 01  
**Equipo**: Team Carteras  
**Estado**: completed  
**Generado por**: sprint-01-evaluator-agent  
**Fecha**: 2026-06-22

---

## Puntaje Final

| Entregable | Obtenido | Máximo |
|-----------|---------|--------|
| GitHub Copilot Instructions | 36.50 | 40 |
| README general | 18.50 | 20 |
| **Total** | **55.00** | **60** |

**Estado**: 🏆 **Sobresaliente** (91.7%)

---

## Fortalezas

1. **Data Quality más granular de los equipos evaluados**: 4 capas de validación (Existencia, Coherencia, Completitud, Consistencia) con jerarquía Crítica > Alta > Media > Baja y umbrales cuantitativos precisos (ej. "3+ campos Críticos faltantes → No viable"). Es un estándar DQ production-ready.

2. **Trazabilidad de cambios inmutable**: El diseño de `historial_cambios[]` con fecha, acción, autor y detalle garantiza auditoría completa. La inmutabilidad del historial como principio de gobierno es excelente.

3. **Arquitectura de agentes muy clara**: Diagrama ASCII del flujo, tabla de handoffs con artefacto/formato, inputs/outputs por agente completamente definidos. Un evaluador externo puede entender la arquitectura sin preguntar al equipo.

4. **Producto ejecutado con datos reales**: Scripts probados con 1754 registros reales del Excel de Forms. Esto diferencia al equipo de entregas solo documentales.

5. **CRISP-DM adaptado al contexto**: El diagrama CRISP-DM del README está adaptado al problema de tickets BI, no es una copia genérica. Cada fase tiene un entregable concreto.

6. **Separación de concerns en principios de gobierno**: "Agent Enrich enriquece datos; Agent Plan genera planes. No se mezclan responsabilidades." Este principio protege la escalabilidad del sistema en sprints futuros.

---

## Oportunidades de Mejora

### Importantes (impactan puntaje y riesgos técnicos)

1. **Agregar linters y formatters**: Black, flake8 e isort (o equivalentes) no están mencionados en `copilot-instructions.md`. Sin ellos, Copilot puede generar código que no siga el estándar definido. Solución: agregar en Sección 3 una línea:
   > Formatear con Black (88 chars), verificar con flake8, ordenar imports con isort.

2. **Framework formal de testing**: "Scripts ejecutables standalone" no es equivalente a pruebas unitarias. Agregar pytest con cobertura mínima (ej. 70%) protege contra regresiones en Sprint 2 cuando se agregue Agent Plan.

3. **LFPDPPP explícito**: Los tickets pueden contener datos personales (nombre, correo, área del solicitante). La Sección 5 menciona CONSAR y CNBV pero no LFPDPPP. Agregar una línea sobre protección de datos personales.

4. **DQ y gobernanza en README**: El README no menciona calidad de datos ni gobierno. Agregar una sección breve (5-10 líneas) que resuma lo que está en copilot-instructions. Esto hace el README más completo para lectores que no revisan los archivos de Copilot.

### Menores

5. **Data Owner y Steward formales**: Definir explícitamente quién es el Data Owner y el Data Steward del producto (actualmente solo se menciona el desarrollador principal y la Dirección Técnica).

6. **DoD con rutas de evidencia**: Cada criterio del DoD debería mapear a una ruta específica en el repositorio (ej. "PR aprobado a qa → Tab Pull Requests del repo").

---

## Riesgos Identificados

1. **[Medio] Sin pytest, riesgo de regresión en Sprint 2**: Cuando se agregue Agent Plan y la integración con ticket.json se vuelva más compleja, la falta de pruebas unitarias puede generar bugs difíciles de detectar.

2. **[Bajo] Gap LFPDPPP**: Si los tickets de Forms incluyen nombre/correo del solicitante (probable), la ausencia de controles LFPDPPP puede ser un gap regulatorio ante una auditoría.

---

## Acciones Recomendadas para Sprint 2

1. Agregar `black`, `flake8` e `isort` en `copilot-instructions.md` Sección 3 y configurar un `pre-commit` hook o CI check.
2. Crear un directorio `tests/` con pruebas unitarias para `validar_ticket.py` y `editar_ticket.py` usando pytest.
3. Agregar en `copilot-instructions.md` Sección 5 una mención explícita a LFPDPPP.
4. Agregar en `README.md` una sección "Calidad de Datos y Gobierno" con los puntos clave.

---

## Comentario Final

Team Carteras demuestra una sólida combinación de pensamiento de producto, ejecución técnica y rigor en datos con 55/60 puntos (91.7%). Es el equipo con la mejor arquitectura de DQ del sprint. Las correcciones requeridas son menores y rápidas de implementar. Están muy bien posicionados para Sprint 2.
