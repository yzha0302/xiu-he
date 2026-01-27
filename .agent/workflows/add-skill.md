---
description: Automated discovery and installation of Agent Skills from skills.sh
---

This workflow helps you find and install "Agent Skills" from the skills.sh ecosystem.

1. **Identify Target Skill**
   - **Scenario A: User provided a specific repo (e.g., `owner/repo`)**
     - Proceed directly to step 3 using that identifier.
   - **Scenario B: User provided a topic (e.g., "react", "seo") or nothing**
     - Use `read_url_content` to fetch `https://skills.sh/`.
     - Inspect the "Skills Leaderboard" section (typically around chunk 3-5).
     - **If topic provided:** Filter the list for skills matching the keyword in their name or description.
     - **If no topic:** Extract the top 10-15 trending skills.
     - Present the list to the user with the format: `Skill Name` - `owner/repo` - `Description/Link`.

2. **Select Skill**
   - Ask the user to confirm which skill they want to install from the list.
   - Wait for their response to get the specific `owner/repo`.

3. **Install Skill**
   - Run the installation command:
     ```bash
     npx skills add <owner/repo>
     ```
   - *Note: You can auto-run this command if the user explicitly confirmed the selection.*

4. **Verify Installation**
   - Run a check to confirm the skill was added (e.g., check for new files in `.cursor/rules` or run `npx skills check`).
   - Notify the user that the skill is ready to use. 
