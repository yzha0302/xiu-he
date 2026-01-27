---
name: html-presentation
description: |
  Create professional single-file HTML slide presentations with sophisticated visual design.
  MANDATORY TRIGGERS: presentation, slides, slide deck, pitch deck, HTML slides, lecture slides, keynote-style, slideshow
  Use when users request presentation creation, slide generation, or converting content into visual presentation format.
---

# HTML Presentation

Create single-file HTML presentations with professional visual design, smooth navigation, and domain-appropriate aesthetics.

## Workflow

1. **Anchor** — Establish visual direction
2. **Map** — Match domain to aesthetic system
3. **Structure** — Define slide skeleton
4. **Build** — Generate HTML with layout components
5. **Refine** — Polish spacing, typography, balance

## Step 1: Anchor

Before designing, establish a visual anchor:

**If user provides images:**
- Extract 2-3 dominant colors
- Note lighting (warm/cool/neutral)
- Identify texture/mood

**If no images:**
- Ask for reference images or brand colors
- Or search: "[domain] exhibition design" / "[domain] presentation design"

Never start without an anchor.

## Step 2: Map Domain to Aesthetics

See `references/aesthetics.md` for complete mapping. Quick reference:

| Domain | Font Style | Color Direction | Layout Style |
|--------|-----------|-----------------|--------------|
| Museum/Academic | Serif | Gold + charcoal + cream | Large whitespace, centered |
| Tech/SaaS | Clean sans | Blue-purple gradients | Cards, grids |
| Finance | Serif or clean sans | Navy + gold + white | Data-heavy, structured |
| Creative/Fashion | Thin sans | Black + white + one accent | Full-bleed, minimal text |
| Medical/Science | Neutral sans | Blue + white + green | Clean, diagram-friendly |
| Education | Friendly sans | Warm, high contrast | Clear hierarchy, icons |

## Step 3: Structure Content

Define skeleton before writing CSS:

```
Slide 1: Title (hero)
Slide 2: Problem/Question (text-image)
Slide 3: Timeline (timeline)
Slide 4: Data (stats)
Slide 5: Comparison (two-column)
Slide 6: Quote (quote)
Slide 7: Conclusion (centered)
```

Each type has a layout component in `references/layouts.md`.

## Step 4: Build

### Required Architecture

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>[Title]</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link href="[Google Fonts]" rel="stylesheet">
    <style>
        :root { /* CSS Variables */ }
        /* Slide styles */
    </style>
</head>
<body>
    <div class="progress-bar" id="progressBar"></div>
    <div class="presentation">
        <!-- Slides with data-slide="N" -->
    </div>
    <nav class="nav"><!-- Buttons --></nav>
    <script>/* Navigation */</script>
</body>
</html>
```

### CSS Variable System (Required)

```css
:root {
    --primary: [accent];
    --primary-light: [lighter];
    --primary-dark: [darker];
    --bg-dark: [main bg];
    --bg-medium: [secondary bg];
    --text-primary: [main text];
    --text-secondary: [muted];
    --font-display: [heading font];
    --font-body: [body font];
}
```

### Required Components

1. **Progress bar** — Top, shows completion %
2. **Slide container** — 100vw × 100vh, opacity transitions
3. **Navigation** — Buttons + keyboard (← →)
4. **Counter** — "N / Total" display

## Step 5: Refine Checklist

- [ ] Spacing uses consistent scale (15/30/60px)
- [ ] Max 3 text hierarchy levels
- [ ] Images have onerror fallback
- [ ] Keyboard nav works
- [ ] Progress bar updates
- [ ] Has @media (max-width: 1200px) breakpoint

## Resources

- `references/aesthetics.md` — Domain-aesthetic mapping, font pairings, color palettes
- `references/layouts.md` — Slide layout components (hero, timeline, stats, quote, comparison, grid)
- `assets/base-template.html` — Minimal working starter template
