# Streamline Safety & Medical Solutions: website concepts, handover notes

These are pitch concepts by CADS for Streamline Safety & Medical Solutions Ltd (https://www.streamlinesms.co.uk). They are not production code, but are built to port to WordPress/Elementor.

- `index.html`: links to the twelve concepts and every page in each
- `concept-1.html` to `concept-12.html`: the homepages
- `concept-N/`: the eight inner pages for each concept: `event-medical-cover`, `medical-training`, `risk-needs-consultancy`, `pre-hospital-career-support`, `recruitment`, `about`, `contact` and `book` (the interactive booking demo)
- `build/`: the generator. All 108 pages are built from one content file, so the wording is identical in every concept
- `reference/`: raw HTML of the live site, its CSS, `brand.md`, `content.md` and `images.md`
- `assets/`: logo, logo shield, badges, every image downloaded from the live site, and `assets/photos/` (the crops used in the designs; see below)

## Editing and rebuilding

Every page is standalone, with its own inline CSS and JS, and is pure ASCII. Don't edit the HTML by hand. Edit the source files and rebuild:

```
python3 build/build.py
```

To rebuild just one or two concepts while working on them (the index is skipped): `SMS_ONLY=4,5 python3 build/build.py`.

| File | Holds |
|---|---|
| `build/content.py` | All page copy, taken from the live site. FAQs are read straight from the saved pages in `reference/` |
| `build/common.py` | Header, footer, shared sections (intro, cards, steps, FAQ, people, contact form and others), icons, base CSS and motion rules |
| `build/booking.py` | The booking wizard: markup, CSS and script |
| `build/dark.py` | The shared structure for concepts 10 to 12 (originally written for a dark direction, since removed), plus the radio-button switch helpers used by their interactive pieces |
| `build/light.py` | The colours for concepts 10 to 12: Streamline's original palette, plus navy "islands" for the photo heroes, panels and footer |
| `build/concept1.py` to `concept12.py` | Each concept's theme: colours, fonts and highlight style, page hero, call-to-action band, footer colours, homepage layout and any interactive pieces added to inner pages |

## Round 7: concepts 4 to 9 (one signature idea each)

The brief: six more concepts to replace the removed 4 to 9, clearly different from the others, in the same colours, showing as much craft as possible while staying clean and easy to read. Each is built around one signature interactive idea. Everything works without JavaScript, and all motion switches off for visitors who ask for reduced motion.

- **Concept 4, Lifeline** (Plus Jakarta Sans). A heartbeat (ECG) line is the thread of the site:
  - the hero trace draws itself, then a glowing dot travels along it past three round photo "beats" that link to the three services
  - a thin line down the side of the homepage fills as you scroll, with a marker at each section (wide screens)
  - service cards are "monitors" with their own live trace, which quickens on hover or focus
  - "From enquiry to your event": the four booking-information sentences from the Event Medical Cover page, lighting up along a trace as you scroll
  - inner pages: the timeline replaces the booking block on Event Medical Cover; the course list becomes readout rows on a navy monitor on Medical Training
- **Concept 5, Bento** (Manrope). Product-page polish:
  - the homepage is a grid of tiles of different sizes (services, Qualsafe centre number, where we work, the 15-years line, contact)
  - tiles tilt gently towards the mouse with a soft glare (not on touch screens), and assemble as you scroll
  - a course finder: pick a course to see how long it usually takes, then book
  - inner pages: the course finder replaces the course cards on Medical Training; on Risk & Needs Consultancy the six services are tiles that open to show "What this includes"
- **Concept 6, Concierge** (Figtree). The page talks to you:
  - the hero is a sentence to complete, "I'm looking for [service] for [who or what]". The second list changes with the first and comes from the site's own lists (event types, bespoke training examples, industries, career starting points). The answer shows the right service, its list, one real FAQ chosen for that option, and booking buttons
  - "We support [schools]" rolls through the site's list of who Streamline works with
  - services as a calm menu that opens to show photo, list and buttons
  - inner pages: Contact gets a "What can we help with?" helper (in place of the service links); Event Medical Cover gets the sentence builder for event types, with the quote information as a "Have these ready" checklist (nothing is saved or sent)
- **Concept 7, Chapters** (Fraunces and Inter). Editorial, magazine style:
  - a serif cover hero with a slow photo drift
  - the services told as three chapters using the consultancy strapline, Assess the risk / Plan the response / Protect your people, beside a sticky photo that wipes to the next chapter, with a roman numeral and a progress rail (stacked on phones)
  - a "Contents" list of services where the photo beside it changes to the row you point at
  - Mathew's quote as a large pull-quote whose words fade in as you scroll
  - inner pages: the five free-consultation steps become scrolling chapters on Risk & Needs Consultancy; the directors become magazine profile spreads on About
- **Concept 8, Kinetic** (Bricolage Grotesque, a variable font). Bold, moving type:
  - a huge line-by-line headline beside a shield shape filled with a photo
  - a strip of service names that drifts and speeds up or reverses with your scrolling (with a pause button)
  - service cards that stack on top of each other as you scroll (wide screens)
  - a navy section where a soft light follows the pointer, and a "who we work with" word wall whose words swell as the pointer passes
  - buttons that lean slightly towards the pointer
  - inner pages: the recruitment pathway becomes stacking cards with giant numbers, plus the values as a word row; the course list on Medical Training becomes a big hover list that reveals each course length
- **Concept 9, Blueprint** (Space Grotesk and IBM Plex Mono). A precise planning look on grid paper:
  - framed photos with crosshairs, dimension lines and figure captions
  - services as numbered spec sheets
  - an event site plan (drawn for the concept) that draws itself as it scrolls in, with numbered points that open the "What information is needed for a quote?" items and two Event Medical Plans items. A numbered list beside it carries the same information
  - inner pages: the site plan replaces the booking block on Event Medical Cover; Risk & Needs Consultancy gets a workplace floor plan with the eight factors the First Aid Needs Assessment considers
- **Short labels written by CADS** (none make claims): section and step labels such as "Course finder", "Selected course", "Where we work", "At a glance", "From enquiry to your event", "Your quotation", "Terms to review", "Booking confirmed", "If details change", "How can we help?", "Tap the green words to change them.", "From our FAQs", "Have these ready", "What can we help with?", "Our services, in three chapters", "Chapter I of III", "Contents", "Also from Streamline", "Careers & Recruitment", "Pause motion", "REF 01" to "REF 05", "Fig. 01", "Select a numbered point to explore", and the plan labels (Stage, Arena, Stalls, First aid, Emergency access and so on). Plans and diagrams are marked "Illustration, not to scale".
- **Shared fix:** photo frames used `overflow: hidden`, which stopped the gentle photo parallax from ever moving (it sat still, slightly zoomed). They now use `overflow: clip`, so the parallax described in round 3 works in every concept.

## Round 6: concepts 10, 11 and 12 (calm, cinematic feel, original colours)

The brief this time: the feel of the Pristine Motors concepts J and K, but not their elements. So these three keep the mood (light display type, generous space, calm and precise motion, explainers you can play with) with their own new elements. All three use Streamline's original colours.

- **Concept 10, Horizon** (Montserrat):
  - a slow film strip of photos drifting under the hero, which pauses on hover
  - a big typographic service list where a photo follows the pointer from row to row (on touch screens each row shows a small photo instead)
  - the mission statement lighting up word by word as you scroll
  - a where-we-work map that pulses out from Swadlincote, from the FAQ "Which areas do you cover?"
  - the booking information as a journey that scrolls sideways while you scroll down (on phones, and in browsers without scroll-driven animation, it is a swipeable row)
  - inner pages: the sideways journey replaces the booking block on Event Medical Cover, the word-by-word mission and vision replace the quote cards on About, and Contact gets the map
- **Concept 11, Contour** (Outfit). Every interactive piece is HTML and CSS only, so the whole concept works without JavaScript:
  - a fan of photo cards that deals in and spreads out on hover
  - service panels that open up when you pick one; on phones they become an accordion
  - "What to expect" flip cards that turn over
  - a bespoke training explorer that shows the real example topics for care homes, sports clubs, schools and workplaces
  - a "What information is needed for a quote?" checklist with a progress bar and an all-ready message; nothing is saved or sent
  - inner pages: Medical Training gets the flip cards and explorer (in place of the four expectation cards), and Event Medical Cover gets the checklist (in place of the booking block)
- **Concept 12, Signal** (Urbanist):
  - a slow radar sweep with blips behind the navy hero and call-to-action
  - a first aid needs assessment grid of the eight factors from the consultancy page, which lights up one by one under a scanning beam as you scroll
  - a five-step consultation stepper with a progress line
  - a career journey where you pick your starting point (the seven groups the live site lists) above the four-step support line
  - inner pages: Risk & Needs Consultancy gets the grid and stepper (in place of the steps block), and Pre-Hospital Career Support gets the journey (in place of the intro and steps)
- Short interface labels such as "Turn over", "Your starting point", "Choose a service to open it up" and "Tick off what you already know" are CADS labels, not claims. Maps and diagrams are marked "Illustration, not to scale".

## Rounds 4 and 5: replaced

The first concepts 4 to 6 (dark, cinematic) and 7 to 9 (the same layouts in the original colours) were removed at CADS's request, and the numbers were reused in round 7. The old versions are in the git history (commits `5a3fe7a` and `25ec156`) if anything from them is wanted later.

## Round 3: friendlier, photos, motion, less text, booking demo

- **Photos instead of placeholders.** Every placeholder is replaced with a crop of the client's own images from the live site (see "Images used"). Most of these images appear to be AI-generated, so they are stand-ins to show the layout with real Streamline imagery. Replace them with genuine photos before launch. Stock photography was offered as the alternative.
- **Friendlier.** Rounded photo frames, soft green blobs and tints, pill buttons, line icons on every card and list, and small floating labels on the hero photos.
- **Animated.** Hero photos and headlines rise in. Sections, cards and timeline steps reveal as you scroll, with a staggered order. Photos drift gently (parallax), hero labels float, a scrolling strip shows the service areas, and buttons, cards and photos respond on hover. The process steps draw a growing line. All of this is turned off for visitors who ask for reduced motion.
- **Less reading per section.** Each block shows its first sentence. The rest sits behind "Read more". Lists became icon chips, steps became a timeline, and long FAQ lists show five questions, with "Show all" and a live search. No copy was removed; it is all one click away.
- **Interactive booking demo (`book.html` in each concept).** A four-step form: choose a service, answer questions for that service, add your details, then check and send. It has a progress bar, a live summary panel, friendly validation, and a confirmation screen with a demo reference number. Service buttons across the site open it with that service already chosen (`book.html?service=event`, `training`, `consultancy` or `careers`). Extras show what is possible:
  - a notice when the event date is less than a month away, based on the live FAQ's advice to phone directly for an event within one month
  - a "what would you like covered" box that appears only when Bespoke Course is chosen
  - a plus/minus learner counter and an attendance slider
  - Without JavaScript it falls back to one long form, and the send button stays disabled. Nothing is sent or stored in any case. On the live site this would connect to a form plugin and email the team.
- **Short labels.** Chip and hero labels are shortened versions of sentences on the live pages (mostly FAQ answers), for example the industries list on the consultancy page. "Demo form: nothing is sent" is a CADS label for the demo.

## Round 2: changes from Mathew's feedback (12 October)

Mathew asked for a site that is lighter, warmer and less corporate, with the Streamline branding obvious at first glance (his example was nexusmedical.co.uk), and with the three main services immediately clear without overwhelming visitors.

- **More brand colour.** Each concept now highlights key words in brand green, in a different style per concept. The shield from the logo appears as a watermark and as a brand mark. Concept 3 adds a green top bar and angled green edges. The shield was cut from the official logo file (`assets/streamline-shield-blue.png` and `-white.png`).
- **Three main services first.** Event Medical Cover, Medical Training and Risk & Needs Consultancy lead every homepage and the main navigation. Pre-Hospital Career Support and Recruitment are still one click away, from a secondary link on the homepages, the mobile menu and the footer.
- **Lighter.** Concept 2's navy hero is now a pale-green centred hero with a light footer. The only remaining navy blocks are the footers in concepts 1 and 3 and the boxed headlines in concept 3.
- **Bigger photos.** Hero photo areas are larger. Concept 3's hero is a full-width photo, like Nexus.
- **Detail is still there, but tidier.** The live site's FAQs are kept word for word in collapsible sections on each service page, so nothing is lost.

## How the twelve concepts differ

1. **Concept 1, editorial split.** White and airy. Split heroes pair the headline with a rounded photo frame on a soft green blob, with floating labels. Key words get a soft green highlight. Homepage services alternate photo and text in a numbered zig-zag. A bobbing green card carries the 15 years line. Call-to-action panels are pale green with three round team photos.
2. **Concept 2, centred statement.** Light and friendly. Pale-green centred heroes with floating bubbles lead into a wide photo collage, with a round second photo and labels. Key words are in green, a strip of four icon cards explains why to choose Streamline, and services are photo cards that zoom on hover. Call-to-action bands are solid green, and the footer is light.
3. **Concept 3, bold brand.** The most branded option and the closest to Nexus. A green top bar sits above split heroes with an angled photo, headlines boxed in navy and solid green, and a white intro card. Three "Find out more" panels lead to the services, which sit in tabs with photos. The approach section pairs "Working With You, Not Simply For You" with a festival photo and Mathew's quote.

4. **Concept 4, Lifeline.** A heartbeat line drawn through the site: hero trace with photo beats, monitor-style service cards, a scroll-filled line and a booking timeline.
5. **Concept 5, Bento.** A grid of tiles that tilt towards the pointer, a course finder and consultancy tiles that open up.
6. **Concept 6, Concierge.** A sentence the visitor completes, answered with the right service and a real FAQ; warm and conversational.
7. **Concept 7, Chapters.** Editorial serif design; three scrolling chapters beside a sticky photo, a contents list and a big pull-quote.
8. **Concept 8, Kinetic.** Bold moving type: a scroll-reactive marquee, stacking service cards, a pointer spotlight and a swelling word wall.
9. **Concept 9, Blueprint.** Grid paper and spec sheets; an event site plan and a workplace floor plan with points to explore.
10. **Concept 10, Horizon.** Calm and typographic: a film strip of photos, a big service list with a photo that follows the pointer, a word-by-word mission, a pulsing area map and a sideways booking journey.
11. **Concept 11, Contour.** Layered and tactile: fanned photo cards, service panels that open up, flip cards, a bespoke topic explorer and a quote checklist. Works fully without JavaScript.
12. **Concept 12, Signal.** Precise and calm: a radar sweep on navy, a needs-assessment grid that scans as you scroll, a consultation stepper and a career journey picker.

All twelve use the same logo, the same copy and the site's own navy `#061E35` and green `#407F36`. On navy panels, green text uses the site's lighter tint `#82D06E` for contrast. Neutrals and tints are taken from the live site's own CSS.

## Placeholders used

No placeholder images, numbers or contact details remain. The real phone number, email and address are used throughout. Each page lists its photos and notes in a comment block at the top.

| Item | Where | What is needed |
|---|---|---|
| Photos in `assets/photos/` | Every page | Genuine photos to replace the stand-ins. Most source images appear to be AI-generated (see below) |
| Contact form | Contact pages | Not connected. Shows a "concept only" message. To be wired to a WordPress form plugin (for example Gravity Forms or Elementor Forms) |
| Booking demo | `book.html` pages | Not connected. Shows how a booking form could work. To be rebuilt in the chosen form plugin (multi-step forms and conditional fields are supported by Gravity Forms and Elementor Pro Forms) |

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
- **Links:** buttons that say "book", "request" or "register interest" open the concept's booking demo with the right service chosen. The training catalogue goes to the client's Google Drive file. The privacy policy and staff portal go to the live site.

## Images used, with source URLs

The logo, the shield cut from it, the two badges, and eleven photos cropped from the client's own site images. Crops remove navy fades and baked-in text. No stock and no new AI images were added. The full assessment of all 51 downloaded images is in `reference/images.md`.

**Important:** most of these source photos appear to be AI-generated or AI-composited (garbled lettering on uniforms, lanyards and signs). They show the layouts with Streamline's own imagery, but they should be replaced with genuine photos of the team before launch. Licensed stock photography is the fallback if genuine photos can't be supplied in time.

| File | Used in | Source |
|---|---|---|
| `assets/streamline-s-m-sol-logo-blue-long.png` | Headers, light footer (concept 2), index | https://images.squarespace-cdn.com/content/v1/69fb44d38d058e2a40ee72f8/1e84c56b-50f3-408b-885a-4058acdc3db5/Streamline+S%26M+Sol+Logo+Blue+Long.png |
| `assets/streamline-s-m-sol-logo-white-long.png` | Navy footers (concepts 1 and 3) | https://images.squarespace-cdn.com/content/v1/69fb44d38d058e2a40ee72f8/07b3f2d8-2aa6-48c6-9b1d-8b0055833a83/Streamline+S%26M+Sol+Logo+white+Long.png |
| `assets/streamline-shield-blue.png`, `assets/streamline-shield-white.png` | Watermarks and brand marks | Cropped by CADS from the two logo files above. No new artwork |
| `assets/whatsapp-image-2026-07-20-at-12.27.35.jpeg` (Qualsafe registered centre badge) | Concept 1 credentials strip, all footers | https://images.squarespace-cdn.com/content/v1/69fb44d38d058e2a40ee72f8/624ea3d0-f9c6-4379-aca1-455f406240d1/WhatsApp+Image+2026-07-20+at+12.27.35.jpeg |
| `assets/featured-landscape-purple-medium.png` (Add To Event Featured Supplier badge) | All footers | https://www.addtoevent.co.uk/sites/default/files/badges/featured_landscape_purple_medium.png |

| Photo | Used in | Cropped from | Note |
|---|---|---|---|
| `assets/photos/event-medics-festival.jpg` | Event medical cover, homepages, About | https://images.squarespace-cdn.com/content/v1/69fb44d38d058e2a40ee72f8/e63058a6-8081-443c-9dd4-375d98e20f84/medical+cover+patrol.png | Appears AI-generated (garbled logo text on polos) |
| `assets/photos/team-at-event.jpg` | Homepages, About, Recruitment, CTAs | https://images.squarespace-cdn.com/content/v1/69fb44d38d058e2a40ee72f8/475a0e79-6e42-4dac-8276-625899219649/people+at+event.png | Appears AI-generated (garbled uniform text) |
| `assets/photos/medic-at-village-fete.jpg` | Event Medical Cover | https://images.squarespace-cdn.com/content/v1/69fb44d38d058e2a40ee72f8/f290b100-02c1-4a34-a3b3-b745d5b58cfb/man+and+village.png | Appears AI-generated |
| `assets/photos/cpr-training-room.jpg` | Medical Training, homepages | https://images.squarespace-cdn.com/content/v1/69fb44d38d058e2a40ee72f8/70cefefa-3c61-4924-ac94-d60deda71dfa/TRAINING.png | Appears AI-generated |
| `assets/photos/training-session.jpg` | Medical Training, Career Support | https://images.squarespace-cdn.com/content/v1/69fb44d38d058e2a40ee72f8/8c4d46ae-20ed-45db-b851-22fc69ba65ff/Codex+Image+8+Sept+2026%2C+18_03_40.png | Cropped to the part that looks like a genuine photo. The filename says Codex, so confirm |
| `assets/photos/cpr-outdoor.jpg` | Career Support, concept 2 | https://images.squarespace-cdn.com/content/v1/69fb44d38d058e2a40ee72f8/c775d5cf-9289-48d5-9f9a-a096ccef4e39/test+3.png | Looks genuine, but low resolution |
| `assets/photos/event-stall.jpg` | Event Medical Cover, Recruitment, Book | https://images.squarespace-cdn.com/content/v1/69fb44d38d058e2a40ee72f8/fe4bdb21-b650-4dbc-95ab-5decdd2c7203/test+4.png | Appears AI-generated (garbled signs) |
| `assets/photos/assessor-hi-vis.jpg` | Risk & Needs Consultancy, homepages | https://images.squarespace-cdn.com/content/v1/69fb44d38d058e2a40ee72f8/7847547e-df2b-4acd-8444-fb47d61f300c/risk+and+needs+2.png | Appears AI-generated |
| `assets/photos/branded-jacket-warehouse.jpg` | Risk & Needs Consultancy | https://images.squarespace-cdn.com/content/v1/69fb44d38d058e2a40ee72f8/de3df2b9-aece-46ad-a2f3-a8208287ef31/WAREHOUSE+AND+SOFT+SHELL.png | Appears AI-generated |
| `assets/photos/office-phone.jpg` | Contact | https://images.squarespace-cdn.com/content/v1/69fb44d38d058e2a40ee72f8/b768590a-cd1d-4bdd-b16d-f4724c10ee1b/tom+and+PC.png | Appears AI-generated |
| `assets/photos/directors.jpg` | About, homepages (concepts 1 and 2) | https://images.squarespace-cdn.com/content/v1/69fb44d38d058e2a40ee72f8/37d56115-4ea9-4e12-b84c-e6baddecbf70/mobile+me+%26+tom.png | Possibly AI-generated (garbled lanyard text) |

Usage rights to check:

- **Qualsafe badge.** Qualsafe's own logo, so check their brand guidelines for registered centres.
- **Add To Event badge.** Add To Event's own badge, served from their site and meant to be embedded by suppliers.
- **The client's images.** The photos are the client's own, from their live site. The uncropped originals in `assets/` are kept for reference only. They are publicly visible on GitHub Pages under `/streamlinesms/assets/`. Delete them from the repo if that's a concern.

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

## Accessibility and build checks (all 54 pages plus the index)

- **Contrast (WCAG AA):** every text/background pair as rendered was measured in Chromium at 375px, 800px and 1440px, with FAQ panels open. All pass.
  - The tightest pairs are green on the pale panel (4.54:1) and green on white or white on green (4.88:1).
  - Concept 1's highlight is navy on a pale green tint (12.62:1). The automated checker misreads this gradient as black, so it was checked by hand.
  - Green text on navy uses the site's own lighter tint `#82D06E`.
  - On concepts 10 to 12 the checker also flags text over gradient panels, because it reads the first colour stop as a solid colour. These were worked out by hand at the brightest point of each gradient: the tightest is light grey text on the green glow of the navy call-to-action panels, at about 5:1.
- **Layout:** no horizontal scrolling at 375px, 800px or 1440px on any page.
- **Without JavaScript:** the `details` mobile menu, "Read more" and "Show all questions" work everywhere. Concept 3's homepage tabs show all three service panels stacked. Concepts 11 and 12's panels, flip cards, explorer, checklist, stepper and career picker still work, because they are radio buttons and checkboxes. The FAQ search box is hidden. The booking demo shows as one long form. The contact and booking send buttons stay disabled, so nothing can be posted.
- **Code rules:**
  - Pure ASCII source with HTML entities; one `h1` per page; no skipped heading levels; every `img` has `alt`, `width` and `height`.
  - Every CSS selector is scoped to its section root. Global tokens, buttons and the highlight sit on `.sms-page`, which maps to Elementor Site Settings and global classes.
  - `min-width: 0` is set on every flex and grid child, verified in the browser.
- **Motion:**
  - Only `transform` and `opacity` are animated.
  - Page headlines and hero photos (the LCP elements) animate in with `transform` only, so they are never invisible.
  - Scroll reveals sit inside `@supports (animation-timeline: view())` and use entry-only ranges. The photo parallax and the timeline line sit in the same block; they follow the element while it is on screen, by design. Browsers without support (currently Firefox and Safari) show everything in place, with the hero entrance, floating labels, scrolling strip and hover effects still running.
  - `prefers-reduced-motion` sets `animation: none` and `animation-timeline: none`, and turns off transitions.

## Porting notes (WordPress/Elementor)

- Navigation links between the concept's own pages are relative. The privacy policy and staff portal still point at the live site.
- Each `<section class="sms-...">` maps to one Elementor container. Its scoped CSS can go into that container's Custom CSS, or into the theme stylesheet.
- Prose sits in `div` containers, as Elementor's Text Editor widget outputs it.
- Concept 3's homepage tabs use a small inline script that builds on HTML which works without it. Elementor's Tabs widget could replace it, but check it falls back as cleanly.
- The booking demo is for showing what's possible. Rebuild it in the chosen form plugin rather than porting the script; keep the service-specific questions, the conditional fields and the `?service=` preselect.
- Scroll-driven animations are plain CSS, so they can go into the theme stylesheet or Elementor's Custom CSS. Elementor's own Motion Effects could replace the parallax.
- Icons are inline SVG line icons drawn by CADS. They could be swapped for an icon set the theme already loads.
- Shared sections (intro, cards, steps, FAQ, people, links, contact) map naturally to saved Elementor templates or global widgets.
- Concepts 11 and 12's interactive pieces are radio buttons and checkboxes with CSS, which Elementor can hold in an HTML widget, or rebuild with its Tabs and Toggle widgets. Concept 10's pointer-following photo is a short inline script; its sideways booking journey and word-by-word mission are plain CSS.
- Concepts 10 to 12 set their colours by changing a handful of tokens (`--sms-ink`, `--sms-surface`, `--sms-accent` and others) on `.sms-page`. These map to Elementor Global Colours.
- Fonts: Montserrat from Google Fonts on concepts 1 to 3 and 10, matching the live site (concept 10 adds the 200 and 300 weights). Concept 11 uses Outfit and concept 12 uses Urbanist. Either can switch to Montserrat.
