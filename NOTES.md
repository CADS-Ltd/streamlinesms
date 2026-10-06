# Streamline Safety & Medical Solutions: homepage concepts, handover notes

These are pitch concepts by CADS for a first meeting with Streamline Safety & Medical Solutions Ltd (https://www.streamlinesms.co.uk). They are not production code, but are built to port to WordPress/Elementor.

- `index.html`: links to the three concepts
- `concept-1.html`, `concept-2.html`, `concept-3.html`: each a standalone homepage, with its CSS and JS inline
- `reference/`: raw HTML of the live site, its CSS, `brand.md`, `content.md` and `images.md`
- `assets/`: logo, badges, the two photo placeholders, and every image downloaded from the live site (most are reference only and not used; see below)

## How the three concepts differ

1. **Concept 1, editorial split.** A split hero puts the headline, copy and three booking links beside a portrait photo. Services follow as a numbered list (01-04), then an about section with the trust points, then the FAQs.
2. **Concept 2, centred statement.** A full-width navy hero centres the headline and buttons with no image. Below it sit a four-point "why choose" strip, the services as a 2x2 grid of cards with bullet points, and a section on the two directors.
3. **Concept 3, three paths.** A large left-aligned headline sits over three big booking panels, followed by a wide photo band. Services are in tabs, then comes a "Working With You" section with Mathew's quote and the client types.

All three use the same logo, the same copy from `reference/content.md`, and the site's own navy `#061E35` and green `#407F36`. Neutrals and tints are taken from the live site's own CSS.

## Placeholders used

No number, statistic or contact placeholders were needed. The real phone number, email and address are used throughout. The only placeholders are photos:

| File | Concept / location | What should go there |
|---|---|---|
| `assets/placeholder-portrait.svg` | Concept 1, hero (right column) | A genuine photo of Mathew and Tom, or of the team at work |
| `assets/placeholder-portrait.svg` | Concept 2, Meet The Directors (Mathew Stones) | A genuine portrait of Mathew |
| `assets/placeholder-portrait.svg` | Concept 2, Meet The Directors (Thomas Wilkes) | A genuine portrait of Tom |
| `assets/placeholder-wide.svg` | Concept 3, photo band under the hero | A genuine landscape photo of the team at an event or training session |

Each file also lists its placeholders in a comment block at the top.

### Copy taken from images on the live site

These lines appear on the live site, but only as text inside images, not as live text. Confirm them with the client before going live.

- "Mathew and Tom bring over 15 years of ambulance experience between them, with even more expertise across our wider team." Used in all three concepts, as approved.
- "Clinician-led safety and medical support". Concept 1 hero eyebrow.
- "Working With You, Not Simply For You." and the two paragraphs under it. Concept 3.
- Mathew Stones' quote: "We truly care about the people and organisations we support..." Concept 3.

## Images used, with source URLs

Only the logo, the two badges and the CADS placeholders are used. Most of the site's photos look AI-generated or AI-composited, and the rest are graphics with text baked in, so none of them are used. The full assessment of all 51 downloaded images is in `reference/images.md`.

| File | Used in | Source URL |
|---|---|---|
| `assets/streamline-s-m-sol-logo-blue-long.png` | Header (concepts 1 and 3), index | https://images.squarespace-cdn.com/content/v1/69fb44d38d058e2a40ee72f8/1e84c56b-50f3-408b-885a-4058acdc3db5/Streamline+S%26M+Sol+Logo+Blue+Long.png |
| `assets/streamline-s-m-sol-logo-white-long.png` | Header (concept 2), all footers | https://images.squarespace-cdn.com/content/v1/69fb44d38d058e2a40ee72f8/07b3f2d8-2aa6-48c6-9b1d-8b0055833a83/Streamline+S%26M+Sol+Logo+white+Long.png |
| `assets/whatsapp-image-2026-07-20-at-12.27.35.jpeg` (Qualsafe registered centre badge) | Concept 1 credentials strip, all footers | https://images.squarespace-cdn.com/content/v1/69fb44d38d058e2a40ee72f8/624ea3d0-f9c6-4379-aca1-455f406240d1/WhatsApp+Image+2026-07-20+at+12.27.35.jpeg |
| `assets/featured-landscape-purple-medium.png` (Add To Event Featured Supplier badge) | All footers | https://www.addtoevent.co.uk/sites/default/files/badges/featured_landscape_purple_medium.png |
| `assets/placeholder-portrait.svg`, `assets/placeholder-wide.svg` | See placeholders | Made by CADS for these concepts. Not client images |

Usage rights to check:

- **Qualsafe badge.** Qualsafe's own logo, so check their brand guidelines for registered centres.
- **Add To Event badge.** Add To Event's own badge, served from their site and meant to be embedded by suppliers.
- **The other images in `assets/`.** These come from the client's live site and are kept for reference only. They will be publicly visible on GitHub Pages under `/streamlinesms/assets/`. Delete them from the repo if that's a concern.

## Things on the live site that looked out of date or inconsistent

- **Broken link:** the homepage "What We Provide" medical cover card links to `/medical-cover`, which doesn't exist. The page is `/event-medical-cover`.
- **Broken images:** all five About page images (two director portraits, three "Streamline In Practice" photos) are linked from a personal OneDrive folder. They return a web page instead of an image, so every visitor sees a broken image. "Mathew teaching ILS.jpg" may well be a genuine photo worth having.
- **Typo:** "Expert medical teams. Precession solutions." should be "Precision". The event cover graphic also says "Experience Medical Team", which should be "Experienced".
- **Qualsafe centre number:** "908578" in the text, "0908578" on the badge.
- **Booking notice:** the FAQ says to phone directly "for an event within one month". The booking banner image says "less than 14 days away".
- **Google reviews:** the homepage says "See what our clients say in the Google reviews below", but no reviews appear in the page.
- **Strapline:** varies between "Protecting People. Supporting Business." and "PROTECTING PEOPLE. SUPPORTING BUSINESSES.", and the homepage heading is "Protecting People. Preparing Organisations."
- **Area served:** varies. The hero and meta description include Nottinghamshire. The "Where is Streamline based?" FAQ lists South Derbyshire, Leicestershire, Staffordshire and the wider East Midlands only.
- **Text in images:** much of the key copy is baked into images, including the services cards, "Why choose", Mathew's message, the process steps and the event types. Every content image has an empty `alt=""`, so screen readers and search engines get none of that text.
- **AI imagery:** several images are named "ChatGPT Image..." or "Codex Image...". Most of the photos show signs of AI generation, such as garbled lettering on uniforms, lanyards and signs, and the same generated trainer appearing in several scenes. Most visitors won't notice, but it's a credibility risk for a clinical business.
- **Placeholder-style filenames:** "test 2.png" to "test 5.png" are still in use on the homepage.
- **Public courses:** the Medical Training page says "No public courses currently scheduled", and the course catalogue is a Google Drive link.
- **Business hours:** set in Squarespace (Mon-Fri 08:00-18:00, Sat 10:00-18:00, Sun 10:00-17:00) but not shown anywhere on the site.
- **Leftovers:** a Squarespace `/cart` link sits in the header markup on a site with no shop. "Our Services" is a folder whose URL, `/our-services`, isn't a real page. Staff Portal (password-protected) appears in the public navigation.
- **Recruitment page:** a sentence is missing its full stop ("...we will continue the conversation").
- **Facebook link:** uses a `profile.php?id=` URL rather than a named page.

## Trust signals found on the site

- Qualsafe Registered Centre, Centre No. 908578 (Qualsafe named as the awarding organisation)
- Add To Event Featured Supplier badge
- "Led by IOSH-qualified health and safety advisors" (consultancy)
- "Fully insured, carefully planned and professionally delivered", plus an FAQ saying insurance evidence can be supplied
- Company details: company no. 17203554, registered in England & Wales, registered office in Swadlincote
- Named directors with backgrounds (current frontline ambulance service; industrial rescue)
- "Over 15 years of ambulance experience" between the directors (image only)
- Google reviews referenced (no content visible)
- Detailed FAQs, booking terms mentioned, privacy policy

## Questions for the client (trust signals a safety and medical business would usually show)

These are questions only. Nothing here has been added to the designs.

1. Can we show your Google rating and some named reviews or testimonials? Which ones are you happy to publish?
2. Which insurance do you hold (public liability, employers' liability, medical malpractice / professional indemnity), with which insurer and at what level of cover? Can we state that on the site?
3. Are you registered with the CQC, or have you confirmed your event medical work falls outside CQC registration? Clients commissioning event cover often ask.
4. Are your clinicians registered with the HCPC (paramedics) or the NMC? Can we say so?
5. Are all staff DBS-checked? To what level?
6. Who leads clinical governance? Is there a named clinical lead or medical director?
7. Do you work to the Purple Guide / Event Safety Guide? (One of your homepage graphics says "Advice on HSE & Purple Guide principles", but the live text doesn't.)
8. Are you a member of any trade or professional bodies, such as the First Aid Industry Body (FAIB) or IOSH (corporate or individual)?
9. What is your ICO data protection registration number? The privacy policy refers to the ICO but doesn't give one.
10. Can we name any clients, events or organisations you've worked with, or show case studies?
11. How long has Streamline been trading? We have not stated or assumed this anywhere.
12. Do you have published safeguarding, complaints and equipment/vehicle standards policies we can link to?
13. Can you send genuine photos of the team, training sessions and events, including the originals of the OneDrive images?
14. Do you want your opening hours (set in Squarespace but not shown) published?

## Personal mobile numbers

None found. The only phone number anywhere on the site, in the visible text and in the page code, is the landline **01283 358789**.

## Accessibility and build checks

- **Contrast (WCAG AA):** every text/background pair as rendered was measured in Chromium at 375px and 1440px, with FAQ panels open. All pass. The closest pairs:
  - green `#407F36` on the pale panel `#F4F8F3`: 4.54:1 (small text, passes AA only just)
  - green `#407F36` on white: 4.88:1
  - white on green buttons: 4.88:1

  No colours needed fixing. By design, green text on navy uses the site's own lighter tint `#82D06E` (8.99:1), because the brand green `#407F36` on navy is only 3.46:1 and would fail for small text.
- **Layout:** checked at 375px, 800px and 1440px with no horizontal scrolling. Concept 3 was also checked with JavaScript off (all four service panels show stacked). The `details` mobile menu was checked opening with JavaScript off on all three concepts.
- **Code rules:**
  - Pure ASCII source with HTML entities; one `h1` per page; no skipped heading levels; every `img` has `alt`, `width` and `height`.
  - Every CSS selector is scoped to its section root. Global tokens and base styles sit on `.sms-page` (the `body` class), which maps to Elementor Site Settings.
  - `min-width: 0` is set on every flex and grid child, verified in the browser.
- **Motion:**
  - Hover effects only.
  - The hero headline (the LCP element) animates in with `transform` only.
  - Scroll reveals sit inside `@supports (animation-timeline: view())` and use entry-only ranges (`entry 0% entry 80%`).
  - `prefers-reduced-motion` sets `animation: none` and `animation-timeline: none`.

## Porting notes (WordPress/Elementor)

- Navigation and service links point at the live site's existing pages. Change them to the new WordPress URLs when porting.
- Each `<section class="sms-...">` maps to one Elementor container. Its scoped CSS can go into that container's Custom CSS, or into the theme stylesheet.
- Prose sits in `div` containers, as Elementor's Text Editor widget outputs it.
- Concept 3's tabs use a small inline script that builds on HTML which works without it. Elementor's Tabs widget could replace it, but check it falls back as cleanly.
- Fonts: Montserrat 400/500/600/700 from Google Fonts, matching the live site.
