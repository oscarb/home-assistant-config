# Agent Directives & Home Assistant Rules

## General Principles
- Do not attempt to clone, download, or fabricate third-party Python packages into `custom_components/`.
- Assume all custom integrations must be installed by the user via HACS or official repos.

## Dependency Notification Protocol
If the requested automation or configuration requires a component, integration, or custom card that is NOT part of Home Assistant Core:
1. Append an exact markdown section at the very end of your final response:
   
   ### 📦 Required Pre-requisites & Downloads
   - **Integration Name**: [Official GitHub / HACS Link]
   - **Installation Method**: (e.g., HACS default, custom repository URL, or HA Core integration)
   - **Required Entities / Setup**: List any entities the user must configure before this automation works.

2. Do not write placeholder python files.
