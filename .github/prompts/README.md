# GitHub Copilot Agent Prompts

Templates y ejemplos de prompts para interactuar efectivamente con los agentes del workflow de Data Product.

## 📋 Estructura

Cada prompt está alineado con el agente correspondiente en `agent-workflow/XX-agent-name/`:

| Agent | Archivo | Propósito |
|---|---|---|
| **01** | `01-enrich-data-story-user.prompt.md` | Enriquecer historias de usuario |
| **02** | `02-data-governance.prompt.md` | Validar governance de datos |
| **03** | `03-agent-planner.prompt.md` | Generar plan técnico |
| **04** | `04-agent-coder.prompt.md` | Implementar código |
| **05** | `05-agent-qa.prompt.md` | Diseñar y ejecutar tests |
| **06** | `06-agent-data-quality.prompt.md` | Validar calidad de datos |
| **07** | `07-agent-documentation.prompt.md` | Generar documentación |
| **08** | `08-agent-compliance-security.prompt.md` | Revisar seguridad y cumplimiento |
| **09** | `09-agent-deployment.prompt.md` | Preparar despliegue |
| **10** | `10-agent-monitoring.prompt.md` | Configurar monitoreo |

## 🎯 Cómo usar

1. **Localiza el agente** que necesitas invocar en el workflow
2. **Abre el archivo** de prompt correspondiente
3. **Copia el template** y personaliza según tu caso de uso
4. **Pega en GitHub Copilot Chat** y ajusta parámetros

### Ejemplo de uso:

```
@04_coder
[Copiar contenido de 04-agent-coder.prompt.md y personalizar]

Implementa esta función según el plan...
```

## 📝 Convenciones

- Los prompts están en **Markdown** para fácil lectura
- Incluyen **placeholders** (`[PLACEHOLDER]`) para personalización
- Usan **bullets y secciones claras**
- Referencial a `agent-workflow/XX-agent-name/` directorios

## 🔗 Relación con agent-workflow

- `.github/prompts/` = Templates/ejemplos para usar agentes
- `agent-workflow/prompts/` = Prompts internos de ejecución de agentes
- `agent-workflow/templates/` = Templates de inputs/outputs
- `agent-workflow/schemas/` = Esquemas JSON para validación

---

**Última actualización**: 2026-06-29  
**Versión**: 1.0
