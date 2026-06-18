# Índice Maestro de Contratos - Data Lab League

## Propósito

Este documento es el registro central de todos los contratos de datos activos en el repositorio. Toda implementación de producto de datos debe tener su contrato registrado aquí antes de pasar a producción.

## Alcance

Cubre todos los productos de datos, interfaces, acuerdos de calidad, SLA/SLO y contratos de gobierno del proyecto DataLabLeague.

---

## Tipos de Contratos Registrados

| Código | Tipo | Descripción |
|---|---|---|
| `DP` | Data Product Contract | Contrato completo del producto de datos |
| `DQ` | Data Quality Contract | Reglas de calidad por dimensión |
| `IF` | Interface Contract | Acuerdo de interfaz entre proveedor y consumidor |
| `SL` | SLA/SLO Contract | Compromisos de nivel de servicio |
| `GV` | Governance Contract | Clasificación, privacidad, acceso y cumplimiento |
| `SC` | Schema Contract | Definición de esquema y versión |

---

## Registro de Contratos

| ID | Tipo | Nombre | Producto Asociado | Owner Negocio | Owner Técnico | Versión | Estado | Última Actualización | Clasificación | Ruta | Evidencia/PR |
|----|------|--------|-------------------|---------------|---------------|---------|--------|----------------------|---------------|------|--------------|
| DP-001 | Data Product | Cartera Comercial | cartera-comercial | TODO | TODO | 0.1.0 | Draft | 2026-06-18 | Confidencial | [contracts/data-products/cartera-comercial.contract.md](data-products/cartera-comercial.contract.md) | - |
| DQ-001 | Data Quality | DQ Cartera Comercial | cartera-comercial | TODO | TODO | 0.1.0 | Draft | 2026-06-18 | - | [contracts/quality/data-quality-contract.md](quality/data-quality-contract.md) | - |
| IF-001 | Interface | Interfaz Ejemplo | cartera-comercial | TODO | TODO | 0.1.0 | Draft | 2026-06-18 | - | [contracts/interfaces/interface-contract.md](interfaces/interface-contract.md) | - |
| SL-001 | SLA/SLO | SLA Cartera Comercial | cartera-comercial | TODO | TODO | 0.1.0 | Draft | 2026-06-18 | - | [contracts/slas/sla-slo-contract.md](slas/sla-slo-contract.md) | - |
| GV-001 | Governance | Governance Cartera Comercial | cartera-comercial | TODO | TODO | 0.1.0 | Draft | 2026-06-18 | PII | [contracts/governance/governance-contract.md](governance/governance-contract.md) | - |

> **Nota**: Agrega una fila cada vez que se registre un nuevo contrato. El ID debe ser único y secuencial por tipo.

---

## Consumidores Registrados

| Consumidor | Producto | Tipo de Acceso | Contrato Vigente |
|---|---|---|---|
| TODO | cartera-comercial | Lectura | DP-001 |

---

## Estado de Contratos por Producto

### cartera-comercial

| Contrato | Estado | Fecha Aprobación |
|---|---|---|
| Data Product (DP-001) | Draft | Pendiente |
| Data Quality (DQ-001) | Draft | Pendiente |
| Interface (IF-001) | Draft | Pendiente |
| SLA/SLO (SL-001) | Draft | Pendiente |
| Governance (GV-001) | Draft | Pendiente |

---

## Historial de Cambios

| Fecha | Contrato | Cambio | Autor | PR |
|---|---|---|---|---|
| 2026-06-18 | Todos | Creación inicial de estructura | Data Lab League Team | - |

---

## Cómo Agregar un Nuevo Contrato

1. Elige el template correcto en `/contracts/templates/`
2. Crea el archivo con la convención de nombres:
   - Data Product: `[nombre].contract.md`
   - Quality: `[nombre].quality-contract.md`
   - Interface: `[origen]-to-[destino].interface-contract.md`
   - SLA/SLO: `[nombre].sla-slo.md`
   - Governance: `[nombre].governance-contract.md`
3. Coloca el archivo en la subcarpeta correspondiente
4. Registra el contrato en la tabla de este archivo
5. Abre un PR con el checklist de contratos completo
6. Obtén aprobación de owner de negocio y técnico
7. Actualiza el estado a `Active` tras merge

---

**Última actualización**: 2026-06-18
**Mantenedor**: Data Lab League Team
