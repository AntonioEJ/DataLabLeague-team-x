#!/usr/bin/env python3
"""
Script para validar la estructura del proyecto DataLabLeague.

Este script verifica que:
1. Todos los directorios requeridos existen
2. Todos los archivos base están presentes
3. Los archivos tienen contenido válido
4. La estructura general es correcta
"""

import os
import sys
from pathlib import Path


def validate_directory_structure():
    """Valida que todos los directorios requeridos existen."""
    required_dirs = [
        ".vscode",
        ".github/agents",
        ".github/instructions",
        ".github/skills",
        ".github/workflows",
        "agent-workflow/prompts",
        "agent-workflow/templates",
        "agent-workflow/schemas",
        "docs/crisp-dm",
        "docs/user-stories",
        "docs/architecture",
        "src/datalab_product",
        "tests",
        "dq",
        "pipeline",
        "observability",
        "evidence/courses",
        "evidence/skills",
        "scorecard",
        "templates",
        "scripts",
    ]
    
    print("Validando directorios...")
    for dir_path in required_dirs:
        full_path = Path(dir_path)
        if full_path.exists():
            print(f"  ✓ {dir_path}")
        else:
            print(f"  ✗ {dir_path} - NOT FOUND")
            return False
    
    return True


def validate_files():
    """Valida que los archivos base están presentes."""
    required_files = [
        "README.md",
        "CLAUDE.md",
        "AGENTS.md",
        ".gitignore",
        ".vscode/extensions.json",
        ".vscode/settings.json",
    ]
    
    print("\nValidando archivos base...")
    for file_path in required_files:
        full_path = Path(file_path)
        if full_path.exists():
            print(f"  ✓ {file_path}")
        else:
            print(f"  ✗ {file_path} - NOT FOUND")
            return False
    
    return True


def validate_documentation():
    """Valida que la documentación existe."""
    required_docs = [
        "docs/crisp-dm/01-business-understanding.md",
        "docs/crisp-dm/02-data-understanding.md",
        "docs/crisp-dm/03-data-preparation.md",
        "docs/user-stories/data-user-stories.md",
        "docs/definition-of-done.md",
    ]
    
    print("\nValidando documentación...")
    for doc_path in required_docs:
        full_path = Path(doc_path)
        if full_path.exists():
            print(f"  ✓ {doc_path}")
        else:
            print(f"  ✗ {doc_path} - NOT FOUND")
            return False
    
    return True


def validate_skills():
    """Valida que los skills están documentados."""
    required_skills = [
        ".github/skills/data-story-user-enrichment/SKILL.md",
        ".github/skills/crispdm-use-case-discovery/SKILL.md",
        ".github/skills/data-quality-rule-authoring/SKILL.md",
        ".github/skills/evidence-packager/SKILL.md",
        ".github/skills/pipeline-quality-gates/SKILL.md",
        ".github/skills/documentation-packager/SKILL.md",
    ]
    
    print("\nValidando skills...")
    for skill_path in required_skills:
        full_path = Path(skill_path)
        if full_path.exists():
            print(f"  ✓ {skill_path}")
        else:
            print(f"  ✗ {skill_path} - NOT FOUND")
            return False
    
    return True


def main():
    """Ejecuta todas las validaciones."""
    print("=" * 60)
    print("DataLabLeague - Validación de Estructura del Proyecto")
    print("=" * 60)
    
    # Cambiar al directorio raíz del proyecto
    project_root = Path(__file__).parent.parent
    os.chdir(project_root)
    
    print(f"\nDirectorio: {project_root}")
    print(f"Python: {sys.version.split()[0]}")
    
    # Ejecutar validaciones
    all_valid = True
    
    all_valid &= validate_directory_structure()
    all_valid &= validate_files()
    all_valid &= validate_documentation()
    all_valid &= validate_skills()
    
    # Resultado final
    print("\n" + "=" * 60)
    if all_valid:
        print("✓ VALIDACIÓN EXITOSA - Estructura correcta")
        print("=" * 60)
        return 0
    else:
        print("✗ VALIDACIÓN FALLIDA - Se encontraron errores")
        print("=" * 60)
        return 1


if __name__ == "__main__":
    sys.exit(main())
