# Agent Directives & Home Assistant Rules

## General Principles
- Do not attempt to clone, download, or fabricate third-party Python packages into `custom_components/`.
- Assume all custom integrations must be installed by the user via HACS or official repos.

## File Organization & Automations
- **Automation ID**: Every automation must include a unique `id` key consisting of a random 8-character alphanumeric string (letters and digits, e.g., `id: "a7k9b2x4"`). Enclose the ID in quotes to ensure YAML parses it as a string.
- **Modular Files**: Try to keep related automations in the same file, but do not append completely unrelated automations to existing files. For each new, distinct feature or automation requested, where there is no file where it fits, create a new, descriptively named file inside the `automations/` directory.
- **Naming Conventions**: Use `snake_case` for filenames.
- **Root Configuration**: Only touch `configuration.yaml` if an official Core integration, template helper, or root include directive strictly requires it.

## Dependency Notification Protocol
If the requested automation or configuration requires a component, integration, or custom card that is NOT part of Home Assistant Core:
1. Append an exact markdown section at the very end of your final response:
   
   ### 📦 Required Pre-requisites & Downloads
   - **Integration Name**: [Official GitHub / HACS Link]
   - **Installation Method**: (e.g., HACS default, custom repository URL, or HA Core integration)
   - **Required Entities / Setup**: List any entities the user must configure before this automation works.

2. Do not write placeholder python files.
