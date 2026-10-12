# Streamline Safety & Medical Solutions: website concepts, handover notes

These are pitch concepts by CADS for Streamline Safety & Medical Solutions Ltd (https://www.streamlinesms.co.uk). They are not production code, but are built to port to WordPress/Elementor.

- `index.html`: links to the three concepts and every page in each
- `concept-1.html`, `concept-2.html`, `concept-3.html`: the homepages
- `concept-N/`: the seven inner pages for each concept: `event-medical-cover`, `medical-training`, `risk-needs-consultancy`, `pre-hospital-career-support`, `recruitment`, `about` and `contact`
- `build/`: the generator. All 24 pages are built from one content file, so the wording is identical in every concept
- `reference/`: raw HTML of the live site, its CSS, `brand.md`, `content.md` and `images.md`
- `assets/`: logo, logo shield, badges, photo placeholders, and every image downloaded from the live site (most are reference only and not used; see below)

## Editing and rebuilding

Every page is standalone, with its own inline CSS and JS, and is pure ASCII. Don't edit the HTML by hand. Edit the source files and rebuild:

```
python3 build/build.py
```

| File | Holds |
|---|---|
| `build/content.py` | All page copy, taken from the live site. FAQs are read straight from the saved pages in `reference/` |
| `build/common.py` | Header, footer, shared sections (intro, cards, steps, FAQ, people, contact form and others), base CSS and motion rules |
| `build/concept1.py`, `concept2.py`, `concept3.py` | Each concept's theme: colours and highlight style, page hero, call-to-action band, footer colours and homepage layout |

## Round 2: changes from Mathew's feedback (12 October)

Mathew asked for a site that is lighter, warmer and less corporate, with the Streamline branding obvious at first glance (his example was nexusmedical.co.uk), and with the three main services immediately clear without overwhelming visitors.

- **More brand colour.** Each concept now highlights key words in brand green, in a different style per concept. The shield from the logo appears as a watermark and as a brand mark. Concept 3 adds a green top bar and angled green edges. The shield was cut from the official logo file (`assets/streamline-shield-blue.png` and `-white.png`).
- **Three main services first.** Event Medical Cover, Medical Training and Risk & Needs Consultancy lead every homepage and the main navigation. Pre-Hospital Career Support and Recruitment are still one click away, from a secondary link on the homepages, the mobile menu and the footer.
- **Lighter.** Concept 2's navy hero is now a pale-green centred hero with a light footer. The only remaining navy blocks are the footers in concepts 1 and 3 and the boxed headlines in concept 3.
- **Bigger photos.** Hero photo areas are larger. Concept 3's hero is a full-width photo, like Nexus.
- **Detail is still there, but tidier.** The live site's FAQs are kept word for word in collapsible sections on each service page, so nothing is lost.

## How the three concepts differ

1. **Concept 1, editorial split.** White and airy. Split heroes pair the headline with a large portrait photo, and key words get a soft green highlight underneath. Homepage services are a numbered list, and call-to-action panels are pale green.
2. **Concept 2, centred statement.** Light and friendly. Pale-green centred heroes have the logo shield behind them and a wide photo overlapping below. Key words are in green, services are cards topped with photos, call-to-action bands are solid green, and the footer is light.
3. **Concept 3, bold brand.** The most branded option and the closest to Nexus. A green top bar sits above full-width photo heroes with headlines boxed in navy and solid green, plus angled green edges. Three booking panels overlap the hero, and homepage services are in tabs.

All three use the same logo, the same copy and the site's own navy `#061E35` and green `#407F36`. Neutrals and tints are taken from the live site's own CSS.

## Placeholders used

No number, statistic or contact placeholders were needed. The real phone number, email and address are used throughout. Each page lists its own placeholders in a comment block at the top.

| Placeholder | Where | What should go there |
|---|---|---|
| `assets/placeholder-portrait.svg` | Concept 1 page heroes (all pages except Contact). About page director portraits in all three concepts. Concept 2 homepage directors | Genuine photos: directors in uniform, team at events, training, assessments, interview practice. Each page's comment says which |
| `assets/placeholder-wide.svg` | Concept 2 page heroes (all pages except Contact) | Wide genuine photo matching the page topic |
| `assets/placeholder-landscape.svg` | Concept 2 homepage service cards (x3) | One genuine photo per service |
| `assets/placeholder-hero.svg` | Concept 3 page heroes (all pages except Contact) | Full-width genuine hero photo matching the page topic |
| Contact form | Contact page, all three concepts | Not connected. Shows a "concept only" message. To be wired to a WordPress form plugin (for example Gravity Forms or Elementor Forms) |

### Copy taken from images on the live site

These lines appear on the live site, but only as text inside images. Confirm them with the client.

- "Mathew and Tom bring over 15 years of ambulance experience between them, with even more expertise across our wider team." Used on every homepage and every About page, as approved.
- "Clinician-led safety and medical support". Hero eyebrow on the concept 1 and 3 homepages.
- "Working With You, Not Simply For You." and the two paragraphs under it. Concept 3 homepage.
- Mathew Stones' quote: "We truly care about the people and organisations we support..." Concept 3 homepage.
- "Book Your Event Medical Cover" heading. Event Medical Cover pages.
- "Group Bookings" and "Examples of bespoke training" labels. Medical Training pages.
- "A clear process" heading and the values list Care / Integrity / Teamwork / Safety / Community. Recruitment pages.
- "Need a Specific Service?" card descriptions. Contact pages.

### Content notes

- **Typo left out:** the Event Medical Cover strapline "Expert medical teams. Precession solutions." is omitted, because it contains the typo. Ask the client whether they want it back, corrected to "Precision".
- **Links:** buttons that say "book" or "register interest" go to the concept's own Contact page. The training catalogue goes to the client's Google Drive file. The privacy policy and staff portal go to the live site.

## Images used, with source URLs

Only the logo, the shield cut from it, the two badges and the CADS placeholders are used. Most of the site's photos look AI-generated or AI-composited, and the rest are graphics with text baked in, so none of them are used. The full assessment of all 51 downloaded images is in `reference/images.md`.

| File | Used in | Source |
|---|---|---|
| `assets/streamline-s-m-sol-logo-blue-long.png` | Headers, light footer (concept 2), index | https://images.squarespace-cdn.com/content/v1/69fb44d38d058e2a40ee72f8/1e84c56b-50f3-408b-885a-4058acdc3db5/Streamline+S%26M+Sol+Logo+Blue+Long.png |
| `assets/streamline-s-m-sol-logo-white-long.png` | Navy footers (concepts 1 and 3) | https://images.squarespace-cdn.com/content/v1/69fb44d38d058e2a40ee72f8/07b3f2d8-2aa6-48c6-9b1d-8b0055833a83/Streamline+S%26M+Sol+Logo+white+Long.png |
| `assets/streamline-shield-blue.png`, `assets/streamline-shield-white.png` | Watermarks and brand marks | Cropped by CADS from the two logo files above. No new artwork |
| `assets/whatsapp-image-2026-07-20-at-12.27.35.jpeg` (Qualsafe registered centre badge) | Concept 1 credentials strip, all footers | https://images.squarespace-cdn.com/content/v1/69fb44d38d058e2a40ee72f8/624ea3d0-f9c6-4379-aca1-455f406240d1/WhatsApp+Image+2026-07-20+at+12.27.35.jpeg |
| `assets/featured-landscape-purple-medium.png` (Add To Event Featured Supplier badge) | All footers | https://www.addtoevent.co.uk/sites/default/files/badges/featured_landscape_purple_medium.png |
| `assets/placeholder-*.svg` | See placeholders | Made by CADS. Not client images |

Usage rights to check:

- **Qualsafe badge.** Qualsafe's own logo, so check their brand guidelines for registered centres.
- **Add To Event badge.** Add To Event's own badge, served from their site and meant to be embedded by suppliers.
- **The other images in `assets/`.** These come from the client's live site and are kept for reference only. They are publicly visible on GitHub Pages under `/streamlinesms/assets/`. Delete them from the repo if that's a concern.

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

## Accessibility and build checks (all 24 pages plus the index)

- **Contrast (WCAG AA):** every text/background pair as rendered was measured in Chromium at 375px, 800px and 1440px, with FAQ panels open. All pass.
  - The tightest pairs are green on the pale panel (4.54:1) and green on white or white on green (4.88:1).
  - Concept 1's highlight is navy on a pale green tint (12.62:1).
  - Green text on navy uses the site's own lighter tint `#82D06E`.
- **Layout:** no horizontal scrolling at 375px, 800px or 1440px on any page.
- **Without JavaScript:** the `details` mobile menu works everywhere. Concept 3's homepage tabs show all three service panels stacked. The contact form shows its "concept only" note.
- **Code rules:**
  - Pure ASCII source with HTML entities; one `h1` per page; no skipped heading levels; every `img` has `alt`, `width` and `height`.
  - Every CSS selector is scoped to its section root. Global tokens, buttons and the highlight sit on `.sms-page`, which maps to Elementor Site Settings and global classes.
  - `min-width: 0` is set on every flex and grid child, verified in the browser.
- **Motion:**
  - Hover effects only.
  - Page headlines (the LCP element) animate in with `transform` only.
  - Scroll reveals sit inside `@supports (animation-timeline: view())` and use entry-only ranges.
  - `prefers-reduced-motion` sets `animation: none` and `animation-timeline: none`.

## Porting notes (WordPress/Elementor)

- Navigation links between the concept's own pages are relative. The privacy policy and staff portal still point at the live site.
- Each `<section class="sms-...">` maps to one Elementor container. Its scoped CSS can go into that container's Custom CSS, or into the theme stylesheet.
- Prose sits in `div` containers, as Elementor's Text Editor widget outputs it.
- Concept 3's homepage tabs use a small inline script that builds on HTML which works without it. Elementor's Tabs widget could replace it, but check it falls back as cleanly.
- Shared sections (intro, cards, steps, FAQ, people, links, contact) map naturally to saved Elementor templates or global widgets.
- Fonts: Montserrat 400/500/600/700 from Google Fonts, matching the live site.
