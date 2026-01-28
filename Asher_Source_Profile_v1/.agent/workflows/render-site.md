---
description: Convert the current or specified Markdown file into a premium "Ascension Reader" HTML website.
---

# Render Markdown Site

This workflow triggers the `render_markdown_site` skill to convert a markdown file into a standalone HTML file with Mermaid support.

1.  Identify the target markdown file. If not specified, ask the user or target the active file.
2.  Run the generation script:
    ```bash
    python3 ".agent/scripts/generate_html.py" --input "/path/to/your/file.md"
    ```
3.  Notify the user of the output location.
