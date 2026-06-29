#!/bin/bash

# DataLabLeague structure validation script

REQUIRED_PATHS=(
    "README.md"
    "CLAUDE.md"
    "AGENTS.md"
    ".github/copilot-instructions.md"
    ".github/agents/00_enrich-data-story-user.agent.md"
    ".github/prompts/01-enrich-data-story-user.prompt.md"
    ".github/skills/data-story-user-enrichment/SKILL.md"
    "agent-workflow/schemas/agent-input.schema.json"
    "agent-workflow/templates/agent-input-template.json"
    "docs/crisp-dm/01-business-understanding.md"
    "docs/user-stories/data-user-stories.md"
    "docs/user-stories/kpi-decision-map.md"
    "docs/user-stories/acceptance-criteria.md"
    "evidence/data-story.md"
    "evidence/skills.md"
    "scorecard/self-assessment.yml"
    "scorecard/skills-assessment.yml"
)

main() {
    local missing=()
    
    for path in "${REQUIRED_PATHS[@]}"; do
        if [[ ! -e "$path" ]]; then
            missing+=("$path")
        fi
    done
    
    if [[ ${#missing[@]} -gt 0 ]]; then
        echo "Missing required paths:"
        for path in "${missing[@]}"; do
            echo "- $path"
        done
        return 1
    fi
    
    echo "Participant repository structure validation passed."
    return 0
}

main
exit $?
