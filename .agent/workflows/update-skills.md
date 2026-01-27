---
description: Update existing Agent Skills to the latest version
---

This workflow helps you keep your skills up to date.

1. **Attempt Automatic Update**
   - Run the standard update command:
     ```bash
     npx skills update
     ```
   - *Note: This requires a valid `skills.lock` file to track installations.*

2. **Manual Update (Reliable Fallback)**
   - If the automatic update doesn't identify skills (e.g., "No skills tracked"), you can force an update by re-adding the skill.
   - Use the `/add-skill` workflow or run:
     ```bash
     npx skills add <owner/repo>
     ```
   - Examples:
     - `npx skills add vercel-labs/agent-skills`
     - `npx skills add remotion-dev/skills`
     - `npx skills add anthropics/skills`

3. **Verify**
   - Check the `SKILL.md` content or file timestamp to ensure it's new.
