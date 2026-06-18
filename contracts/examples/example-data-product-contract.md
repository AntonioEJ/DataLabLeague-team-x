# Example — Data Product Contract Completo

Este ejemplo muestra cómo se relacionan todos los contratos de un producto de datos:

```
contracts/
└── data-products/
    └── cartera-comercial.contract.md     ← Contrato maestro del producto
└── quality/
    └── data-quality-contract.md          ← Reglas DQ (referenciado desde DP)
└── interfaces/
    └── interface-contract.md             ← Acuerdo de entrega con Core Bancario
└── slas/
    └── sla-slo-contract.md               ← Compromisos de servicio
└── governance/
    └── governance-contract.md            ← Clasificación, acceso, retención
```

## Flujo de Creación Recomendado

1. Primero: crear **Data Product Contract** (`DP-XXX`) — define el qué
2. Luego: crear **Interface Contracts** (`IF-XXX`) — define el cómo llegan los datos
3. Luego: crear **Data Quality Contract** (`DQ-XXX`) — define los umbrales de calidad
4. Luego: crear **SLA/SLO Contract** (`SL-XXX`) — define los tiempos de entrega
5. Finalmente: crear **Governance Contract** (`GV-XXX`) — define gobierno y cumplimiento
6. Registrar todos en `contracts/contracts.md`

## Ejemplo de Contrato Completo para Cartera Comercial

Ver archivos en:
- [../data-products/cartera-comercial.contract.md](../data-products/cartera-comercial.contract.md)
- [../quality/data-quality-contract.md](../quality/data-quality-contract.md)
- [../interfaces/interface-contract.md](../interfaces/interface-contract.md)
- [../slas/sla-slo-contract.md](../slas/sla-slo-contract.md)
- [../governance/governance-contract.md](../governance/governance-contract.md)

## Relaciones entre Contratos

```
DP-001 (Cartera Comercial)
├── referencias → IF-001 (Core Bancario to Cartera)
├── referencias → DQ-001 (Data Quality Rules)
├── referencias → SL-001 (SLA/SLO Cartera)
└── referencias → GV-001 (Governance Cartera)
```

Cada contrato tiene su propio ID secuencial, versión y estado. El DP es el contrato "padre" que referencia los demás.
