# Brand reference - Streamline Safety & Medical Solutions

Extracted on 2026-10-06 from the live Squarespace site's CSS, not estimated from screenshots.

Sources:

- **Theme CSS**: `reference/css/site.css`, downloaded from
  `https://static1.squarespace.com/static/versioned-site-css/69fb44d38d058e2a40ee72f8/35/5c5a519771c10ba3470d8101/69fb44d38d058e2a40ee72f8/1834/site.css`.
  The `?nocustom=true` version is byte-identical, so the site has no global Custom CSS.
- **Inline `<style>` blocks**: the custom code blocks embedded in each page's HTML in `reference/*.html`.
  These are where the site's own hand-written components (CTA buttons, trust strip, FAQ accordions, values cards) set their colours.

## Core brand colours

These two hex values are declared by name as the brand colours in the site's own code blocks, for example
`--sms-navy: #061E35; --sms-green: #407F36;` (home.html, `.sms-trust-strip`),
`--streamline-navy: #061E35; --streamline-green: #407F36;` (home.html, CTA block) and
`--navy:#061E35; --green:#407F36;` (`.sl-faq` on every service page).

| Role | Hex | Where found |
|---|---|---|
| Brand navy (primary text, dark backgrounds) | `#061E35` | Inline styles on home, about, event cover, training, consultancy, careers. Defined as `--sms-navy`, `--streamline-navy` and `--navy` |
| Brand green (accent, buttons, borders, highlights) | `#407F36` | Same pages. Defined as `--sms-green`, `--streamline-green` and `--green` |

## Squarespace theme palette (site.css `:root`)

The template's global colour settings. They are close to, but not exactly, the hand-coded values above. Squarespace stores them as HSL; the hex values below are exact conversions.

| Squarespace variable | HSL in CSS | Hex | Notes |
|---|---|---|---|
| `--black-hsl` | `209,80%,12%` | `#061F37` | Theme "black". The same navy as `#061E35`, give or take rounding |
| `--accent-hsl` / `--safeDarkAccent-hsl` | `112,40%,35%` | `#3F7D36` | Theme accent. The same green as `#407F36`, give or take rounding |
| `--darkAccent-hsl` | `209,57%,19%` | `#15314C` | Theme dark accent, a lighter navy |
| `--lightAccent-hsl` | `45,7%,95%` | `#F3F3F1` | Theme light accent, a warm off-white |
| `--white-hsl` | `0,0%,100%` | `#FFFFFF` | White |

**Recommendation for the concepts:** use `#061E35` and `#407F36` as the two brand colours, because they are the values the site's own components declare by name. Treat the theme values as rounding variants of the same colours.

## Supporting tints and shades already used on the site

All of these come from the inline component styles. Every one is a tint or shade of the navy or the green.

| Hex | Use on the live site | Where found |
|---|---|---|
| `#0A2C49` | Gradient start on the navy CTA buttons (`linear-gradient(135deg,#0a2c49 0%,var(--navy) 72%)`) | home.html, `.streamline-single a` |
| `#0B3152` | Gradient end on a navy panel (`linear-gradient(135deg, #061e35 0%, #0b3152 100%)`) | home.html, medical-training.html |
| `#65A85A` | Green border on button hover | home.html, `.streamline-single a:hover` |
| `#67B957` | Light green gradient on the CTA left edge bar | home.html, medical-training.html |
| `#82D06E` | Brightest green, border on button hover | home.html, medical-training.html |
| `#4F9243` | Green variant | medical-training.html |
| `#F4F8F3` | Pale green-white panel background (`--pale`) | FAQ blocks on every service page |
| `#F3F8F2`, `#EEF7EC` | Pale green panel variants | medical-training.html, risk-needs-consultancy.html |
| `#DFE6E0`, `#DDE5DC`, `#DDE5E1` | Pale green-grey borders | aboutus.html, medical-training.html |
| `#D9E2E7`, `#D9E4EC`, `#D7E2E9` | Pale blue-grey borders (FAQ `details` border) | FAQ blocks, medical-training.html |
| `#496177` | Soft navy text (`--sms-text-soft`) | home.html, `.sms-trust-strip` |
| `#405365` | Muted navy body text (`.sl-faq__intro`) | FAQ blocks |
| `#334A5C` | Muted navy body text (`.sl-faq__answer`) | FAQ blocks |
| `#607786`, `#5F6B76`, `#66727C` | Muted grey-blue text | medical-training.html |

## Contrast pre-check (WCAG 2.x)

| Foreground | On `#FFFFFF` | On `#F4F8F3` | On `#061E35` |
|---|---|---|---|
| `#061E35` navy | 16.87 | 15.72 | n/a |
| `#407F36` green | 4.88 (AA for body text) | 4.54 (AA, only just) | 3.46 (large text only) |
| `#65A85A` | 2.88 (fails) | 2.68 (fails) | 5.87 (AA) |
| `#82D06E` | 1.88 (fails) | 1.75 (fails) | 8.99 (AA) |
| `#496177` | 6.44 | 6.00 | fails |
| `#334A5C` | 9.23 | 8.60 | fails |

Takeaways for the concepts: green text is fine on white. On navy, green text needs to be a lighter tint the site already uses (`#65A85A` or `#82D06E`). White text on the green `#407F36` is 4.88:1, so it passes AA for button labels.

## Typography

| Role | Family | Weight / style | Where found |
|---|---|---|---|
| Headings | **Montserrat** | 400 normal (theme default) | site.css `--heading-font-font-family:"Montserrat"` |
| Body | **Montserrat** | 400 normal | site.css `--body-font-font-family:"Montserrat"` |
| Meta / small caps labels | **Montserrat** | 400 normal | site.css `--meta-font-font-family:"Montserrat"` |
| Buttons | **Montserrat** | 400 normal | site.css `--primary-button-font-font-family:"Montserrat"` |
| Navigation | Montserrat (inherits body) | | site.css `--site-navigation-font-font-family:var(--body-font-font-family)` |
| Header button (template setting) | Newsreader | 400 normal | site.css `--header-button-font-font-family:"Newsreader"`. The header has no CTA button on any page, so Newsreader never renders. Treat it as a leftover template setting |

The hand-coded blocks load Montserrat from Google Fonts at weights 400, 500, 600, 700 and 800:
`https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800&display=swap` (home.html)
and use it with the fallback stack `'Montserrat', Arial, sans-serif`.

The logo wordmark ("STREAMLINE / SAFETY & MEDICAL SOLUTIONS") is part of the logo image, not live text.

## Logo files

- `assets/streamline-s-m-sol-logo-blue-long.png`: full-colour horizontal logo for light backgrounds (2500 x 443, transparent PNG)
- `assets/streamline-s-m-sol-logo-white-long.png`: white/green horizontal logo for dark backgrounds (2500 x 443, transparent PNG)
