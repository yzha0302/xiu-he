# Domain-Aesthetic Mapping

## Quick Lookup Table

| Domain | Display Font | Body Font | Primary | Background | Accent |
|--------|-------------|-----------|---------|------------|--------|
| Museum/Academic | Cormorant Garamond | Inter | #C9A962 (gold) | #1C1C1C (charcoal) | #F5F0E8 (cream) |
| Tech/SaaS | DM Sans | Inter | #6366F1 (indigo) | #0F172A (slate) | #22D3EE (cyan) |
| Finance/Corporate | Libre Baskerville | Source Sans Pro | #1E3A5F (navy) | #FFFFFF | #C9A962 (gold) |
| Creative/Fashion | Bebas Neue | Montserrat | #000000 | #FFFFFF | #FF3366 (magenta) |
| Medical/Science | IBM Plex Sans | IBM Plex Sans | #0077B6 (medical blue) | #F8FAFC | #10B981 (green) |
| Education/Training | Nunito | Open Sans | #F59E0B (amber) | #FFFBEB | #3B82F6 (blue) |
| Luxury/Premium | Playfair Display | Lato | #B8860B (dark gold) | #0A0A0A | #E5E5E5 |
| Startup/Modern | Space Grotesk | Inter | #8B5CF6 (violet) | #18181B | #F472B6 (pink) |
| Legal/Government | Merriweather | Open Sans | #1F2937 (gray-800) | #F9FAFB | #DC2626 (red) |
| Environmental/NGO | Lora | Work Sans | #059669 (emerald) | #ECFDF5 | #0891B2 (teal) |

## Detailed Palettes

### Museum/Academic
```css
:root {
    --primary: #C9A962;
    --primary-light: #E8D5A3;
    --primary-dark: #8B7355;
    --bg-dark: #1C1C1C;
    --bg-medium: #2A2A2A;
    --bg-light: #F5F0E8;
    --text-primary: #FAF8F5;
    --text-secondary: rgba(255,255,255,0.6);
    --text-muted: rgba(255,255,255,0.3);
    --font-display: 'Cormorant Garamond', Georgia, serif;
    --font-body: 'Inter', -apple-system, sans-serif;
}
```
**Characteristics:** Warm gold accents, dark backgrounds, large whitespace, serif headings for authority, restrained decoration.

**Google Fonts:** `https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400&family=Inter:wght@300;400;500;600&display=swap`

### Tech/SaaS
```css
:root {
    --primary: #6366F1;
    --primary-light: #A5B4FC;
    --primary-dark: #4338CA;
    --bg-dark: #0F172A;
    --bg-medium: #1E293B;
    --bg-light: #F1F5F9;
    --text-primary: #F8FAFC;
    --text-secondary: #94A3B8;
    --text-muted: #475569;
    --font-display: 'DM Sans', sans-serif;
    --font-body: 'Inter', sans-serif;
}
```
**Characteristics:** Cool gradients, dark mode default, card-based layouts, clean sans-serif, subtle shadows.

**Google Fonts:** `https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&family=Inter:wght@300;400;500;600&display=swap`

### Finance/Corporate
```css
:root {
    --primary: #1E3A5F;
    --primary-light: #3B5998;
    --primary-dark: #0F2744;
    --bg-dark: #1E3A5F;
    --bg-medium: #F8FAFC;
    --bg-light: #FFFFFF;
    --text-primary: #1F2937;
    --text-secondary: #6B7280;
    --accent: #C9A962;
    --font-display: 'Libre Baskerville', Georgia, serif;
    --font-body: 'Source Sans Pro', sans-serif;
}
```
**Characteristics:** Navy + gold, light backgrounds, data visualization friendly, trustworthy serif headings.

**Google Fonts:** `https://fonts.googleapis.com/css2?family=Libre+Baskerville:wght@400;700&family=Source+Sans+Pro:wght@300;400;600&display=swap`

### Creative/Fashion
```css
:root {
    --primary: #000000;
    --primary-light: #333333;
    --bg-dark: #000000;
    --bg-light: #FFFFFF;
    --text-primary: #000000;
    --text-light: #FFFFFF;
    --accent: #FF3366;
    --font-display: 'Bebas Neue', sans-serif;
    --font-body: 'Montserrat', sans-serif;
}
```
**Characteristics:** High contrast black/white, one bold accent, full-bleed images, minimal text, dramatic typography.

**Google Fonts:** `https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Montserrat:wght@300;400;500;600&display=swap`

### Medical/Science
```css
:root {
    --primary: #0077B6;
    --primary-light: #48CAE4;
    --primary-dark: #03045E;
    --bg-dark: #03045E;
    --bg-light: #F8FAFC;
    --bg-white: #FFFFFF;
    --text-primary: #1E293B;
    --text-secondary: #64748B;
    --success: #10B981;
    --font-display: 'IBM Plex Sans', sans-serif;
    --font-body: 'IBM Plex Sans', sans-serif;
}
```
**Characteristics:** Clinical blues, clean whites, diagram-friendly, neutral typography, clear data presentation.

**Google Fonts:** `https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@300;400;500;600&display=swap`

### Luxury/Premium
```css
:root {
    --primary: #B8860B;
    --primary-light: #DAA520;
    --primary-dark: #8B6914;
    --bg-dark: #0A0A0A;
    --bg-medium: #1A1A1A;
    --bg-light: #E5E5E5;
    --text-primary: #FAFAFA;
    --text-secondary: #A3A3A3;
    --font-display: 'Playfair Display', Georgia, serif;
    --font-body: 'Lato', sans-serif;
}
```
**Characteristics:** Deep blacks, gold metallics, elegant serifs, generous spacing, subtle animations.

**Google Fonts:** `https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;500;600;700&family=Lato:wght@300;400;700&display=swap`

## Font Pairing Principles

1. **Contrast in style** — Pair serif display with sans-serif body (or vice versa)
2. **Similar x-height** — Fonts should feel balanced at same size
3. **Shared mood** — Both fonts should fit the domain's tone
4. **Weight range** — Display font needs 2+ weights, body needs 3+

## Color Application Rules

1. **Primary** — Headlines, buttons, key accents (10-15% of design)
2. **Background** — Main slide backdrop (70-80%)
3. **Text primary** — Body text, main content
4. **Text secondary** — Captions, metadata, muted elements
5. **Accent** — Highlights, hover states, data visualization points
