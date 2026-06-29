# Prompt Template: Agent 10 - Monitoring

**Propósito**: Definir monitoreo, observabilidad, alertas y KPIs operativos.

**Agente**: `@10_monitoring`

**Input**: Deployment de Agent 09 + Código de Agent 04  
**Output**: `monitoring-dashboard.md` + `alert-rules.yaml` + `observability-config.md`

---

## 📋 Template

```markdown
@10_monitoring

Necesito configurar el monitoreo para:

### Proyecto
[Nombre del caso de uso]

### Métricas de Negocio
1. [KPI 1]: [definición, threshold, frecuencia]
2. [KPI 2]: [definición, threshold, frecuencia]
3. [...]

### Métricas Técnicas
- **Disponibilidad**: [SLA %, threshold de alerta]
- **Latencia**: [P50, P95, P99 máximos]
- **Throughput**: [registros/segundo mínimos]
- **Errores**: [tasa de error máxima, tipos]
- **Recursos**: [CPU, memoria, almacenamiento]

### Alertas Requeridas
1. [Alerta 1]: [condición, severidad, quien notificar]
2. [Alerta 2]: [condición, severidad, quien notificar]
3. [...]

### Dashboard de Monitoreo
- **Visualizaciones**: [gráficos, tablas, gauge]
- **Audiencia**: [SRE, product, negocio]
- **Refresh**: [real-time, 5min, diario]
- **Herramientas**: [Grafana, Datadog, CloudWatch, etc.]

### Runbooks de Operación
- [Problema 1]: [pasos para diagnosticar, solucionar]
- [Problema 2]: [pasos]
- [...]

---

Por favor genera:
✓ Dashboard de monitoreo
✓ Reglas de alerta
✓ Configuración de observabilidad
✓ Runbooks de troubleshooting
```

---

## ✅ Cierre del Ciclo CRISP-DM
Con Agent 10 se completa:
- ✓ Business Understanding (Agents 01-02)
- ✓ Data Understanding (Agents 02-03)
- ✓ Data Preparation (Agent 04)
- ✓ Modeling (Agent 04)
- ✓ Evaluation (Agents 05-06)
- ✓ Deployment (Agents 07-10)

---

## 📌 Next Step
→ **Evidence & Documentation** para cerrar el ciclo

Ejecuta:
```
git add agent-workflow/XX-agent-name/evidence/
git commit -m \"[evidencia] Producto de datos [nombre] completado\"
git push origin develop
```

---

**Referencia**: [CLAUDE.md - Agent 10](../../CLAUDE.md#10--monitoring-agent)

**Final**: El ciclo CRISP-DM está completo. Documentar evidencia en `evidence/final-product-evidence.json` para cerrar.
