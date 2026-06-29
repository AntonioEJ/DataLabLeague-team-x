# 🤖 Copilot Instructions – Ambiente Agéntico para Generación de Indicadores BI

## 📋 Tabla de Contenidos
- [Objetivo](#-objetivo)
- [Contexto del Sistema](#-contexto-del-sistema)
- [Arquitectura Agéntica](#-arquitectura-agéntica)
- [Flujo Orquestado](#-flujo-orquestado)
- [Especificaciones Técnicas](#-especificaciones-técnicas)
- [Restricciones y Buenas Prácticas](#️-restricciones-y-buenas-prácticas)
- [Resultado Esperado](#-resultado-esperado)

---

## 🎯 Objetivo

Este documento define las **instrucciones operativas para GitHub Copilot** dentro del ecosistema agéntico orientado a la generación, enriquecimiento, validación e implementación de **indicadores de negocio (KPIs)**, asegurando:

- ✅ **Consistencia** en la generación de artefactos
- ✅ **Trazabilidad** end-to-end de procesos
- ✅ **Cumplimiento** de gobierno y calidad de datos
- ✅ **Automatización** inteligente del ciclo completo

---

## 🧠 Contexto del Sistema

El entorno está compuesto por **múltiples agentes especializados** que operan de forma orquestada para transformar un contexto inicial en entregables ejecutables:

### 📥 Entradas del Sistema
- Documentos PDF con contexto de negocio
- Formularios estructurados de requisitos
- Inputs de usuario/stakeholders
- Fuentes de datos existentes

### 📤 Salidas del Sistema
- **Indicadores estructurados** con definiciones formales
- **Modelos de datos** alineados a arquitectura empresarial
- **Código ejecutable** (SQL, Python, pipelines)
- **Documentación técnica y funcional** completa
- **Validaciones de calidad** y controles de gobierno

---

## 🧩 Arquitectura Agéntica

### 1. 🟦 Enrich Data Story Agent
**Rol:** Interpretar y enriquecer el contexto inicial con inteligencia de negocio

#### 📥 Entradas
- PDF / Documento base con contexto de negocio
- Formulario estructurado de requisitos
- Inputs de stakeholders

#### 📤 Salidas
Documento `.md` estructurado con:
- **Contexto del indicador**: Descripción del problema de negocio
- **Objetivo estratégico**: Alineación con metas organizacionales
- **Variables clave**: Dimensiones y métricas identificadas
- **Hipótesis analítica**: Supuestos y relaciones esperadas
- **Métricas candidatas**: Lista priorizada de posibles KPIs

#### 🤖 Instrucciones para Copilot
```yaml
Tareas:
  - Analizar el contexto de negocio y extraer objetivos estratégicos
  - Identificar variables medibles y sus relaciones
  - Traducir narrativa de negocio a términos analíticos
  - Estructurar información en formato Markdown reutilizable
  - Generar preguntas de clarificación si hay ambigüedades

Formato de salida:
  - Usar encabezados H2/H3 para estructura
  - Incluir tablas para variables y métricas
  - Agregar sección de supuestos y restricciones
  - Documentar fuentes de información

Validaciones:
  - Verificar que el objetivo sea SMART (Específico, Medible, Alcanzable, Relevante, Temporal)
  - Confirmar alineación con estrategia organizacional
  - Identificar gaps de información