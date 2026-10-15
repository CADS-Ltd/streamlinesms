"""Concept 7 - Chapters. Editorial and calm, set in Fraunces and Inter: the site
tells Streamline's story in chapters, using the consultancy strapline "Assess the
risk. Plan the response. Protect your people." An editorial cover hero with lines
rising from a mask and a slow Ken Burns photo, scrollytelling chapters with a
sticky photo stage that wipes between chapters, a "Contents" services index whose
photo crossfades to the row you point at, a scroll-lit pull-quote on a navy
island, drop caps, and article-style closing lines."""
from common import *  # noqa: F401,F403
import content as C

NAME = "Chapters"
FONTS = "https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300..600;1,9..144,300..600&family=Inter:wght@400;500;600&display=swap"

STRAP_CONSULT = C.PAGES["risk-needs-consultancy"]["sections"][0][1]["strap"]  # "Assess the risk. Plan the response. Protect your people."
CHAPTER_LINES = [s.strip() + "." for s in STRAP_CONSULT.split(".") if s.strip()]
SVC = {s["key"]: s for s in C.SERVICES}
ROMAN = ["I", "II", "III", "IV", "V"]

# The three chapters: strapline line, service, photo, which of its list items to show
CHAPTERS = [
    (CHAPTER_LINES[0], SVC["consultancy"], "assessor", [0, 1, 2]),
    (CHAPTER_LINES[1], SVC["training"], "session", [0, 1, 3]),
    (CHAPTER_LINES[2], SVC["event"], "festival", [0, 2, 3]),
]

# Contents index rows: (number, title, text, slug, photo, minor)
INDEX = [
    (SVC["event"]["title"], SVC["event"]["text"], SVC["event"]["slug"], "fete", False),
    (SVC["training"]["title"], SVC["training"]["text"], SVC["training"]["slug"], "cpr-room", False),
    (SVC["consultancy"]["title"], SVC["consultancy"]["text"], SVC["consultancy"]["slug"], "jacket", False),
    (C.CAREERS["title"], C.CAREERS["text"], C.CAREERS["slug"], "cpr-outdoor", True),
    ("Recruitment", C.PAGES["recruitment"]["hero"]["body"][0], "recruitment", "stall", True),
]

CONSULT = C.PAGES["risk-needs-consultancy"]["sections"][2][1]
PEOPLE = C.PAGES["about"]["sections"][2][1]
QUOTE_WORDS = C.MATHEW_QUOTE.split(" ")
QUOTE_EM_FROM = QUOTE_WORDS.index("That")


def _index_css():
    out = ""
    for i in range(len(INDEX)):
        out += '.sms-chapindex[data-active="%d"] .sms-chapindex__shot--%d { opacity: 1; transform: scale(1); }\n' % (i, i)
        out += '.sms-chapindex[data-active="%d"] .sms-chapindex__cap--%d { opacity: 1; transform: none; }\n' % (i, i)
        out += '.sms-chapindex[data-active="%d"] .sms-chapindex__item--%d .sms-chapindex__num { color: var(--sms-green); }\n' % (i, i)
    return out


def _quote_css():
    n = len(QUOTE_WORDS)
    out = "@supports (animation-timeline: view()) {\n"
    out += "  @keyframes sms-chap-word { from { opacity: 0.2; } to { opacity: 1; } }\n"
    out += "  .sms-chapquote .sms-chapquote__text { view-timeline-name: --sms-chapquote; }\n"
    out += "  .sms-chapquote .sms-chapquote__w { animation: sms-chap-word linear both; animation-timeline: --sms-chapquote; }\n"
    for i in range(n):
        start = 5 + i * (30.0 / n)
        out += "  .sms-chapquote .sms-chapquote__w:nth-child(%d) { animation-range: cover %.1f%% cover %.1f%%; }\n" % (i + 1, start, start + 8)
    out += "}\n"
    return out


HEADS = ["feature", "cards", "steps", "checklist", "faq", "quotes", "people", "contact", "links", "marquee", "booking"]


def _sel(fmt):
    return ",\n".join(fmt % (b, b) for b in HEADS)


CSS = r"""
/* ===== Concept 7 theme: chapters ===== */
.sms-page {
  --sms-font: "Inter", "Helvetica Neue", Arial, sans-serif;
  --sms-serif: "Fraunces", Georgia, "Times New Roman", serif;
  --sms-radius: 0.25rem;
  --sms-radius-sm: 0.25rem;
  --sms-shadow: none;
  --sms-shadow-lg: 0 40px 80px -40px rgba(6, 30, 53, 0.28);
  --sms-max: 78rem;
  --sms-step-2: clamp(2rem, 1.3rem + 2.6vw, 3.4rem);
  --sms-section: clamp(4rem, 2.8rem + 5vw, 8rem);
  --sms-rule: rgba(6, 30, 53, 0.14);
  --sms-wipe: cubic-bezier(0.77, 0, 0.18, 1);
  --sms-soft: cubic-bezier(0.2, 0.8, 0.2, 1);
  line-height: 1.7;
  text-rendering: optimizeLegibility;
}
.sms-page .sms-mark { color: var(--sms-green); font-style: italic; }

/* Buttons: quiet, rectangular, navy first */
.sms-page .sms-btn { gap: 0.5rem; padding: 0.95rem 1.5rem; border-width: 1px; border-radius: 0.25rem; font-size: 0.9375rem; font-weight: 500; letter-spacing: 0.005em; transition: background-color 0.35s var(--sms-ease), color 0.35s var(--sms-ease), border-color 0.35s var(--sms-ease); }
.sms-page .sms-btn:hover { transform: none; }
.sms-page .sms-btn--primary { border-color: var(--sms-navy); background: var(--sms-navy); color: var(--sms-white); box-shadow: none; }
.sms-page .sms-btn--primary:hover { border-color: var(--sms-green); background: var(--sms-green); }
.sms-page .sms-btn--outline { border-color: rgba(6, 30, 53, 0.4); background: transparent; color: var(--sms-navy); }
.sms-page .sms-btn--outline:hover { border-color: var(--sms-navy); background: var(--sms-navy); color: var(--sms-white); }
.sms-page .sms-more__toggle { font-size: 0.875rem; font-weight: 600; }
.sms-page .sms-photo { border-radius: 0.25rem; }

/* Shared editorial label (small caps style) */
.sms-page .sms-chaplabel { display: flex; align-items: center; gap: 0.75rem; margin-bottom: 1.25rem; color: var(--sms-green); font-size: 0.75rem; font-weight: 600; letter-spacing: 0.2em; line-height: 1.4; text-transform: uppercase; }
.sms-page .sms-chaplabel::before { content: ""; flex: 0 0 auto; width: 2rem; height: 1px; background: currentColor; }
/* Drop cap */
.sms-page .sms-chapdrop > p:first-child::first-letter { float: left; margin: 0.08em 0.035em 0 -0.02em; color: var(--sms-green); font-family: var(--sms-serif); font-size: 4.4em; font-weight: 400; line-height: 0.8; }

/* ---------- Masthead strip + header ---------- */
.sms-chapmast { background: var(--sms-navy); color: rgba(255, 255, 255, 0.86); font-size: 0.8125rem; }
.sms-chapmast .sms-chapmast__inner { display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 0.25rem 1.5rem; width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: 0.5rem var(--sms-gutter); }
.sms-chapmast .sms-chapmast__strap { display: none; min-width: 0; margin: 0; color: var(--sms-white); font-family: var(--sms-serif); font-size: 0.9375rem; font-style: italic; font-weight: 300; }
.sms-chapmast .sms-chapmast__links { display: flex; flex-wrap: wrap; gap: 0.25rem 1.5rem; min-width: 0; }
.sms-chapmast .sms-chapmast__link { min-width: 0; color: rgba(255, 255, 255, 0.86); text-decoration: none; overflow-wrap: anywhere; }
.sms-chapmast .sms-chapmast__link:hover { color: var(--sms-green-on-navy); }
.sms-chapmast .sms-chapmast__link:focus-visible { outline-color: var(--sms-green-on-navy); }
@media (min-width: 48em) {
  .sms-chapmast .sms-chapmast__strap { display: block; }
}
.sms-header { border-bottom: 1px solid var(--sms-line); background: rgba(255, 255, 255, 0.94); }
.sms-header .sms-header__inner { min-height: 4.5rem; }
.sms-header .sms-header__link { border-radius: 0; font-size: 0.875rem; font-weight: 500; }
.sms-header .sms-header__link::after { left: 0.7rem; right: 0.7rem; bottom: 0.2rem; height: 1px; }
.sms-header .sms-header__cta { padding: 0.7rem 1.1rem; font-size: 0.875rem; }
.sms-header .sms-header__summary { border-radius: 0.25rem; background: transparent; box-shadow: inset 0 0 0 1px var(--sms-line); font-weight: 500; }
.sms-header .sms-header__panel { border-radius: 0.25rem; box-shadow: 0 0 0 1px var(--sms-line), 0 30px 60px -20px rgba(6, 30, 53, 0.25); }
.sms-header .sms-header__panel-link { border-radius: 0.2rem; font-weight: 500; }

/* ---------- Footer: navy, serif sign-off ---------- */
.sms-footer { background: var(--sms-navy); color: rgba(255, 255, 255, 0.8); }
.sms-footer .sms-footer__tag { margin-bottom: 1.5rem; color: var(--sms-white); font-family: var(--sms-serif); font-size: clamp(1.5rem, 1.2rem + 1vw, 2rem); font-weight: 300; line-height: 1.15; }
.sms-footer .sms-footer__heading { margin-bottom: 1.1rem; padding-bottom: 0.75rem; border-bottom: 1px solid rgba(255, 255, 255, 0.14); color: var(--sms-white); font-family: var(--sms-serif); font-size: 1.125rem; font-style: italic; font-weight: 400; letter-spacing: 0; text-transform: none; }
.sms-footer .sms-footer__link { color: rgba(255, 255, 255, 0.8); }
.sms-footer .sms-footer__link:hover { color: var(--sms-green-on-navy); }
.sms-footer .sms-footer__link:focus-visible,
.sms-footer .sms-footer__badge-link:focus-visible { outline-color: var(--sms-green-on-navy); }
.sms-footer .sms-footer__base { border-color: rgba(255, 255, 255, 0.14); color: rgba(255, 255, 255, 0.7); }

/* ---------- Shared section heads, in the editorial voice ---------- */
""" + _sel(".sms-%s .sms-%s__eyebrow") + r""" { gap: 0.75rem; margin-bottom: 1.25rem; color: var(--sms-green); font-size: 0.75rem; font-weight: 600; letter-spacing: 0.2em; }
""" + _sel(".sms-%s .sms-%s__eyebrow::before") + r""" { width: 2rem; height: 1px; border-radius: 0; background: currentColor; }
""" + _sel(".sms-%s .sms-%s__title") + r""" { margin-bottom: 1.25rem; font-family: var(--sms-serif); font-weight: 350; line-height: 1.08; letter-spacing: -0.02em; }
.sms-page .sms-watermark { display: none; }

/* Feature */
.sms-feature .sms-feature__blob { display: none; }
.sms-feature .sms-feature__media::before { content: ""; position: absolute; z-index: -1; top: 0.9rem; left: 0.9rem; right: -0.6rem; bottom: -0.9rem; border: 1px solid var(--sms-line-green); border-radius: 0.25rem; }
.sms-feature .sms-feature__frame { aspect-ratio: 4 / 4.4; box-shadow: none; }
.sms-feature .sms-feature__lead { color: var(--sms-navy); font-family: var(--sms-serif); font-size: clamp(1.25rem, 1.1rem + 0.5vw, 1.5rem); font-weight: 300; line-height: 1.45; }
.sms-feature .sms-feature__strap { padding: 0.15rem 0 0.15rem 1rem; border-left: 2px solid var(--sms-green); border-radius: 0; background: none; font-family: var(--sms-serif); font-size: 1.25rem; font-style: italic; font-weight: 400; line-height: 1.4; }
.sms-feature .sms-feature__strap-icon { display: none; }
.sms-feature .sms-feature__chips-title { margin-top: 2rem; font-family: var(--sms-serif); font-size: 1.125rem; font-weight: 500; }
.sms-page .sms-chips { display: grid; gap: 0 2rem; border-top: 1px solid var(--sms-rule); }
.sms-page .sms-chips .sms-chips__item { gap: 0.75rem; padding: 0.7rem 0; border-bottom: 1px solid var(--sms-rule); border-radius: 0; background: none; box-shadow: none; font-weight: 500; }
.sms-page .sms-chips .sms-chips__item:hover { transform: none; }
.sms-page .sms-chips .sms-chips__icon { width: 1.25rem; height: 1.25rem; padding: 0; border-radius: 0; background: none; color: var(--sms-green); }
@media (min-width: 40em) {
  .sms-page .sms-chips { grid-template-columns: repeat(2, minmax(0, 1fr)); }
}
@media (min-width: 56em) {
  .sms-feature .sms-feature__media::before { top: 1.5rem; left: 1.5rem; right: -1.5rem; bottom: -1.5rem; }
  .sms-feature.sms-feature--flip .sms-feature__media::before { left: -1.5rem; right: 1.5rem; }
}

/* Cards: ruled, no shadows */
.sms-cards .sms-cards__grid { gap: clamp(1.25rem, 0.8rem + 1.5vw, 2rem); }
.sms-cards .sms-cards__grid .sms-cards__item { padding: 1.75rem 1.5rem 1.75rem; border-top: 1px solid var(--sms-navy); border-radius: 0; background: var(--sms-white); box-shadow: none; }
.sms-cards.sms-tone-white .sms-cards__grid .sms-cards__item { padding-left: 0; padding-right: 0; background: transparent; }
.sms-cards .sms-cards__item::before { content: ""; position: absolute; left: 0; right: 0; top: -1px; height: 2px; background: var(--sms-green); transform: scaleX(0); transform-origin: left; transition: transform 0.6s var(--sms-ease); }
.sms-cards .sms-cards__item:hover { transform: none; }
.sms-cards .sms-cards__item:hover::before { transform: scaleX(1); }
.sms-cards .sms-cards__grid .sms-cards__icon { width: 2rem; height: 2rem; padding: 0; border-radius: 0; background: none; color: var(--sms-green); }
.sms-cards .sms-cards__item:hover .sms-cards__icon { transform: none; }
.sms-cards .sms-cards__num { color: var(--sms-green); font-family: var(--sms-serif); font-size: 1.75rem; font-style: italic; font-weight: 300; }
.sms-cards .sms-cards__name { font-family: var(--sms-serif); font-size: clamp(1.25rem, 1.15rem + 0.4vw, 1.5rem); font-weight: 450; line-height: 1.22; letter-spacing: -0.005em; }
.sms-cards .sms-cards__grid .sms-cards__meta { padding: 0; border-radius: 0; background: none; color: var(--sms-ink-soft); font-weight: 500; }
.sms-cards .sms-cards__list-title { font-size: 0.75rem; font-weight: 600; letter-spacing: 0.16em; }
.sms-cards .sms-cards__list-item { border-bottom: 1px solid var(--sms-rule); }

/* Steps */
.sms-steps .sms-steps__line { width: 1px; background: var(--sms-line-green); }
.sms-steps .sms-steps__item { align-content: start; }
.sms-steps .sms-steps__badge { border: 1px solid var(--sms-green); background: var(--sms-white); color: var(--sms-green); box-shadow: 0 0 0 8px var(--sms-white); }
.sms-steps.sms-tone-pale .sms-steps__badge { background: var(--sms-pale); box-shadow: 0 0 0 8px var(--sms-pale); }
.sms-steps .sms-steps__num { right: -0.55rem; top: -0.55rem; width: 1.6rem; height: 1.6rem; background: var(--sms-navy); font-family: var(--sms-serif); font-size: 0.875rem; font-style: italic; font-weight: 400; }
.sms-steps .sms-steps__name { font-family: var(--sms-serif); font-size: 1.25rem; font-weight: 450; line-height: 1.25; }
.sms-steps .sms-steps__text { font-size: 0.9375rem; }
.sms-steps .sms-steps__note { padding: 0.2rem 0 0.2rem 1.25rem; border-left: 2px solid var(--sms-green); border-radius: 0; background: none; }
.sms-steps.sms-tone-white .sms-steps__note { background: none; }
@media (min-width: 60em) {
  .sms-steps .sms-steps__line { height: 1px; }
}

/* Checklist */
.sms-checklist .sms-checklist__grid { gap: 0 2rem; }
.sms-checklist .sms-checklist__grid .sms-checklist__item { padding: 1.4rem 0; border-top: 1px solid var(--sms-navy); border-radius: 0; background: none; font-family: var(--sms-serif); font-size: 1.25rem; font-weight: 400; line-height: 1.35; }
.sms-checklist .sms-checklist__item:hover { transform: none; }
.sms-checklist .sms-checklist__icon { width: 2rem; height: 2rem; padding: 0; border-radius: 0; background: none; }

/* Notice */
.sms-notice .sms-notice__box { border: 1px solid var(--sms-rule); border-left: 3px solid var(--sms-green); border-radius: 0.25rem; box-shadow: none; }
.sms-notice .sms-notice__badge { border: 1px solid var(--sms-green); background: none; }
.sms-notice .sms-notice__label { font-size: 0.75rem; font-weight: 600; letter-spacing: 0.2em; }
.sms-notice .sms-notice__title { font-family: var(--sms-serif); font-size: clamp(1.4rem, 1.2rem + 0.8vw, 1.85rem); font-weight: 400; line-height: 1.2; }

/* FAQ: a ruled list */
.sms-faq .sms-faq__list { border-bottom: 1px solid var(--sms-rule); }
.sms-faq .sms-faq__list .sms-faq__item { margin: 0; border-top: 1px solid var(--sms-rule); border-radius: 0; background: none; box-shadow: none; }
.sms-faq .sms-faq__q { padding: 1.35rem 3.25rem 1.35rem 0; font-family: var(--sms-serif); font-size: clamp(1.0625rem, 1rem + 0.3vw, 1.25rem); font-weight: 400; line-height: 1.35; }
.sms-faq .sms-faq__q::after { right: 0; width: 2rem; height: 2rem; margin-top: -1rem; border: 1px solid var(--sms-line-green); background: none; font-family: var(--sms-font); font-size: 1.15rem; font-weight: 300; }
.sms-faq .sms-faq__a { padding: 0 3rem 1.5rem 0; }
.sms-faq .sms-faq__input { border-radius: 0.25rem; }
.sms-faq .sms-faq__all-toggle { margin-top: 1.25rem; border-width: 1px; border-radius: 0.25rem; font-weight: 500; }

/* Quotes (mission / vision) */
.sms-quotes .sms-quotes__grid { gap: clamp(2rem, 1.5rem + 2vw, 4rem); }
.sms-quotes .sms-quotes__item { padding: 2rem 0 0; border-top: 1px solid var(--sms-navy); border-radius: 0; background: none; }
.sms-quotes .sms-quotes__icon { display: none; }
.sms-quotes .sms-quotes__label { margin-bottom: 1rem; font-size: 0.75rem; font-weight: 600; letter-spacing: 0.2em; }
.sms-quotes .sms-quotes__text { font-family: var(--sms-serif); font-size: clamp(1.3rem, 1.1rem + 0.8vw, 1.75rem); font-weight: 300; line-height: 1.4; }

/* People (fallback styling) */
.sms-people .sms-people__person { border-top: 1px solid var(--sms-navy); border-radius: 0; box-shadow: none; }
.sms-people .sms-people__name,
.sms-people .sms-people__shared-title { font-family: var(--sms-serif); font-weight: 400; }
.sms-people .sms-people__frame { box-shadow: none; }

/* Links (contact page) */
.sms-links .sms-links__grid { gap: clamp(1rem, 0.6rem + 1.5vw, 1.75rem); }
.sms-links .sms-links__link { position: relative; padding: 1.75rem 1.5rem; border-top: 1px solid var(--sms-navy); border-radius: 0; background: var(--sms-white); box-shadow: none; }
.sms-links .sms-links__link::before { content: ""; position: absolute; left: 0; right: 0; top: -1px; height: 2px; background: var(--sms-green); transform: scaleX(0); transform-origin: left; transition: transform 0.6s var(--sms-ease); }
.sms-links .sms-links__link:hover { transform: none; }
.sms-links .sms-links__link:hover::before { transform: scaleX(1); }
.sms-links .sms-links__icon { width: 2rem; height: 2rem; padding: 0; border-radius: 0; background: none; }
.sms-links .sms-links__name { font-family: var(--sms-serif); font-size: 1.375rem; font-weight: 450; line-height: 1.2; }

/* Claim */
.sms-claim .sms-claim__icon { width: 2.25rem; height: 2.25rem; padding: 0; background: none; }
.sms-claim.sms-tone-pale .sms-claim__icon { background: none; }
.sms-claim .sms-claim__text { max-width: 52rem; font-family: var(--sms-serif); font-size: clamp(1.6rem, 1.1rem + 2vw, 2.75rem); font-style: italic; font-weight: 300; line-height: 1.25; letter-spacing: -0.01em; }

/* Contact */
.sms-contact .sms-contact__details { gap: 0; border-top: 1px solid var(--sms-rule); }
.sms-contact .sms-contact__detail { padding: 1.2rem 0; border-bottom: 1px solid var(--sms-rule); border-radius: 0; background: none; }
.sms-contact .sms-contact__detail:hover { transform: none; }
.sms-contact .sms-contact__icon { border: 1px solid var(--sms-line-green); background: none; }
.sms-contact .sms-contact__label { font-size: 0.75rem; font-weight: 600; letter-spacing: 0.16em; }
.sms-contact .sms-contact__value { font-family: var(--sms-serif); font-size: 1.3rem; font-weight: 450; }
.sms-contact .sms-contact__form { border: 1px solid var(--sms-rule); border-top: 1px solid var(--sms-navy); box-shadow: none; }
.sms-contact .sms-contact__form-title { font-family: var(--sms-serif); font-size: 1.6rem; font-weight: 400; line-height: 1.2; }
.sms-contact .sms-contact__booklink { background: var(--sms-pale); }

/* Marquee */
.sms-marquee .sms-marquee__item { border-radius: 0.25rem; box-shadow: none; font-weight: 500; }

/* Booking wizard */
.sms-booking .sms-booking__form { border: 1px solid var(--sms-rule); border-top: 1px solid var(--sms-navy); box-shadow: none; }
.sms-booking .sms-booking__step-title { font-family: var(--sms-serif); font-weight: 350; letter-spacing: -0.015em; }
.sms-booking .sms-booking__service-card { border-width: 1px; }
.sms-booking .sms-booking__service-icon { padding: 0.55rem; border-radius: 50%; background: var(--sms-pale-2); }
.sms-booking .sms-booking__service-name { font-family: var(--sms-serif); font-size: 1.125rem; font-weight: 500; }
.sms-booking .sms-booking__progress-dot { border-width: 1px; font-family: var(--sms-serif); font-weight: 500; }
.sms-booking .sms-booking__chip-text { border-width: 1px; font-weight: 500; }
.sms-booking .sms-booking__toggle { border-radius: 0.3rem; }
.sms-booking .sms-booking__toggle-opt span { border-radius: 0.2rem; font-weight: 500; }
.sms-booking .sms-booking__summary-title { font-family: var(--sms-serif); font-size: 1.25rem; font-weight: 400; }
.sms-booking .sms-booking__help { background: var(--sms-pale-2); }
.sms-booking .sms-booking__help-title { font-family: var(--sms-serif); font-size: 1.25rem; font-weight: 400; }
.sms-booking .sms-booking__done-title { font-family: var(--sms-serif); font-weight: 350; }

/* ---------- Motion keyframes ---------- */
@keyframes sms-chap-rise { from { transform: translateY(110%); } to { transform: none; } }
@keyframes sms-chap-up { from { opacity: 0; transform: translateY(14px); } to { opacity: 1; transform: none; } }
@keyframes sms-chap-curtain { from { transform: scaleY(1); } to { transform: scaleY(0); } }
@keyframes sms-chap-drift { from { transform: scale(1.04) translate3d(0, 0, 0); } to { transform: scale(1.14) translate3d(-2.2%, -1.6%, 0); } }
@keyframes sms-chap-settle { from { transform: scale(1.1); } to { transform: scale(1); } }

/* ---------- Home: editorial cover ---------- */
.sms-chapcover { position: relative; overflow: hidden; padding: clamp(2rem, 1rem + 3vw, 3.75rem) 0 clamp(1rem, 0.5rem + 2vw, 2.5rem); background: var(--sms-white); }
.sms-chapcover .sms-chapcover__inner { width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-chapcover .sms-chapcover__top { display: flex; flex-wrap: wrap; align-items: baseline; justify-content: space-between; gap: 0.5rem 2rem; margin-bottom: clamp(2rem, 1rem + 3.5vw, 4rem); padding-bottom: 1rem; border-bottom: 1px solid var(--sms-navy); }
.sms-chapcover .sms-chapcover__kicker { display: flex; flex-wrap: wrap; gap: 0.35rem 1.75rem; min-width: 0; margin: 0; padding: 0; list-style: none; animation: sms-chap-up 0.9s var(--sms-soft) 0.05s both; }
.sms-chapcover .sms-chapcover__kicker-item { min-width: 0; }
.sms-chapcover .sms-chapcover__kicker-link { color: var(--sms-navy); font-size: 0.75rem; font-weight: 600; letter-spacing: 0.18em; text-decoration: none; text-transform: uppercase; }
.sms-chapcover .sms-chapcover__kicker-link:hover { color: var(--sms-green); }
.sms-chapcover .sms-chapcover__folio { display: none; min-width: 0; color: var(--sms-ink-soft); font-family: var(--sms-serif); font-size: 0.9375rem; font-style: italic; }
.sms-chapcover .sms-chapcover__title { margin: 0 0 clamp(2rem, 1rem + 3vw, 3.5rem); font-family: var(--sms-serif); font-size: clamp(3.2rem, 0.7rem + 8.4vw, 8.6rem); font-weight: 300; line-height: 0.95; letter-spacing: -0.035em; }
.sms-chapcover .sms-chapcover__line { display: block; overflow: hidden; margin-bottom: -0.12em; padding: 0 0.12em 0.12em 0; }
.sms-chapcover .sms-chapcover__rise { display: block; animation: sms-chap-rise 1.3s var(--sms-soft) 0.1s both; }
.sms-chapcover .sms-chapcover__line + .sms-chapcover__line .sms-chapcover__rise { animation-delay: 0.24s; }
.sms-chapcover .sms-chapcover__grid { display: grid; gap: clamp(2.5rem, 1.5rem + 3vw, 4rem); }
.sms-chapcover .sms-chapcover__copy { min-width: 0; }
.sms-chapcover .sms-chapcover__lead { max-width: 30rem; margin: 0; color: var(--sms-navy); font-size: clamp(1.0625rem, 1rem + 0.35vw, 1.25rem); line-height: 1.65; animation: sms-chap-up 0.9s var(--sms-soft) 0.45s both; }
.sms-chapcover .sms-chapcover__actions { display: flex; flex-wrap: wrap; gap: 0.75rem; margin-top: 2rem; animation: sms-chap-up 0.9s var(--sms-soft) 0.6s both; }
.sms-chapcover .sms-chapcover__area { display: flex; gap: 0.6rem; max-width: 26rem; margin: 2.25rem 0 0; padding-top: 1.25rem; border-top: 1px solid var(--sms-rule); color: var(--sms-ink-soft); font-size: 0.875rem; line-height: 1.55; animation: sms-chap-up 0.9s var(--sms-soft) 0.75s both; }
.sms-chapcover .sms-chapcover__area-icon { width: 1.1rem; height: 1.1rem; margin-top: 0.1rem; color: var(--sms-green); }
.sms-chapcover .sms-chapcover__area-text { min-width: 0; }
.sms-chapcover .sms-chapcover__figure { min-width: 0; margin: 0; }
.sms-chapcover .sms-chapcover__frame { position: relative; overflow: hidden; aspect-ratio: 4 / 3; border-radius: 0.25rem; background: var(--sms-pale); }
.sms-chapcover .sms-chapcover__img { display: block; width: 100%; height: 100%; object-fit: cover; transform-origin: 60% 40%; animation: sms-chap-drift 32s ease-in-out infinite alternate; }
.sms-chapcover .sms-chapcover__curtain,
.sms-chaphero .sms-chaphero__curtain { position: absolute; inset: 0; background: var(--sms-white); transform: scaleY(0); transform-origin: top; animation: sms-chap-curtain 1.4s var(--sms-wipe) 0.3s both; }
.sms-chapcover .sms-chapcover__caption,
.sms-chaphero .sms-chaphero__caption,
.sms-chapdir .sms-chapdir__plate-cap { display: flex; gap: 0.75rem; margin-top: 0.9rem; color: var(--sms-ink-soft); font-size: 0.8125rem; line-height: 1.5; }
.sms-chapcover .sms-chapcover__caption::before,
.sms-chaphero .sms-chaphero__caption::before,
.sms-chapdir .sms-chapdir__plate-cap::before { content: ""; flex: 0 0 auto; width: 1.5rem; height: 1px; margin-top: 0.72em; background: var(--sms-navy); }
.sms-chapcover .sms-chapcover__toc { display: grid; margin: clamp(3rem, 2rem + 3vw, 5rem) 0 0; padding: 0; border-top: 1px solid var(--sms-navy); list-style: none; animation: sms-chap-up 0.9s var(--sms-soft) 0.9s both; }
.sms-chapcover .sms-chapcover__toc-item { min-width: 0; border-bottom: 1px solid var(--sms-rule); }
.sms-chapcover .sms-chapcover__toc-link { display: grid; grid-template-columns: 2.75rem minmax(0, 1fr) auto; gap: 1rem; align-items: baseline; padding: 1.15rem 0; color: var(--sms-navy); text-decoration: none; }
.sms-chapcover .sms-chapcover__toc-num { min-width: 0; color: var(--sms-green); font-family: var(--sms-serif); font-size: 1.125rem; font-style: italic; }
.sms-chapcover .sms-chapcover__toc-body { display: grid; gap: 0.1rem; min-width: 0; }
.sms-chapcover .sms-chapcover__toc-name { min-width: 0; font-family: var(--sms-serif); font-size: 1.375rem; font-weight: 400; line-height: 1.2; }
.sms-chapcover .sms-chapcover__toc-svc { min-width: 0; color: var(--sms-ink-soft); font-size: 0.8125rem; }
.sms-chapcover .sms-chapcover__toc-go { min-width: 0; color: var(--sms-green); transition: transform 0.4s var(--sms-ease); }
.sms-chapcover .sms-chapcover__toc-link:hover .sms-chapcover__toc-name { color: var(--sms-green); }
.sms-chapcover .sms-chapcover__toc-link:hover .sms-chapcover__toc-go { transform: translateY(4px); }
@media (min-width: 72em) {
  .sms-chapcover .sms-chapcover__folio { display: block; }
}
@media (min-width: 60em) {
  .sms-chapcover .sms-chapcover__toc { grid-template-columns: repeat(3, minmax(0, 1fr)); }
  .sms-chapcover .sms-chapcover__toc-item { border-bottom: 0; }
  .sms-chapcover .sms-chapcover__toc-item + .sms-chapcover__toc-item { border-left: 1px solid var(--sms-rule); }
  .sms-chapcover .sms-chapcover__toc-link { padding: 1.35rem 1.5rem 1.35rem 0; }
  .sms-chapcover .sms-chapcover__toc-item + .sms-chapcover__toc-item .sms-chapcover__toc-link { padding-left: 1.5rem; }
}
@media (min-width: 60em) {
  .sms-chapcover .sms-chapcover__grid { grid-template-columns: minmax(0, 0.78fr) minmax(0, 1.22fr); gap: 5rem; align-items: start; }
  .sms-chapcover .sms-chapcover__frame { aspect-ratio: 16 / 10.5; }
}

/* ---------- Home: scrollytelling chapters ---------- */
.sms-chapstory { position: relative; padding: var(--sms-section) 0; background: var(--sms-white); }
.sms-chapstory .sms-chapstory__inner { width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-chapstory .sms-chapstory__head { display: grid; gap: 0 4rem; align-items: end; margin-bottom: clamp(3rem, 2rem + 4vw, 6rem); }
.sms-chapstory .sms-chapstory__head-main { min-width: 0; }
.sms-chapstory .sms-chapstory__title { margin: 0 0 1.75rem; font-family: var(--sms-serif); font-size: clamp(2.3rem, 1.3rem + 3.8vw, 4.8rem); font-weight: 300; line-height: 1.02; letter-spacing: -0.03em; }
.sms-chapstory .sms-chapstory__title-line { display: block; }
.sms-chapstory .sms-chapstory__lead { min-width: 0; max-width: 36rem; color: var(--sms-ink-soft); font-size: var(--sms-step-1); line-height: 1.6; }
.sms-chapstory .sms-chapstory__lead p { margin: 0; }
.sms-chapstory .sms-chapstory__stage { display: none; min-width: 0; }
.sms-chapstory .sms-chapstory__list { display: grid; min-width: 0; gap: clamp(4rem, 3rem + 4vw, 7rem); margin: 0; padding: 0; list-style: none; }
.sms-chapstory .sms-chapstory__chapter { display: grid; gap: 2rem; align-items: center; min-width: 0; scroll-margin-top: 6rem; }
.sms-chapstory .sms-chapstory__photo { min-width: 0; margin: 0; }
.sms-chapstory .sms-chapstory__photo-frame { overflow: hidden; aspect-ratio: 4 / 3; border-radius: 0.25rem; background: var(--sms-pale); }
.sms-chapstory .sms-chapstory__photo-img { display: block; width: 100%; height: 100%; object-fit: cover; }
.sms-chapstory .sms-chapstory__text { position: relative; min-width: 0; }
.sms-chapstory .sms-chapstory__label { display: flex; flex-wrap: wrap; align-items: baseline; gap: 0.35rem 1rem; margin-bottom: 1.1rem; }
.sms-chapstory .sms-chapstory__roman { min-width: 0; color: var(--sms-green); font-family: var(--sms-serif); font-size: 1.125rem; font-style: italic; }
.sms-chapstory .sms-chapstory__service { min-width: 0; color: var(--sms-ink-soft); font-size: 0.75rem; font-weight: 600; letter-spacing: 0.2em; text-transform: uppercase; }
.sms-chapstory .sms-chapstory__name { margin: 0 0 1.25rem; font-family: var(--sms-serif); font-size: clamp(2.2rem, 1.5rem + 2.6vw, 3.75rem); font-weight: 350; line-height: 1.03; letter-spacing: -0.025em; }
.sms-chapstory .sms-chapstory__desc { max-width: 34rem; margin: 0 0 1.75rem; color: var(--sms-ink-soft); font-size: var(--sms-step-1); line-height: 1.6; }
.sms-chapstory .sms-chapstory__points { max-width: 34rem; margin: 0 0 2rem; padding: 0; border-top: 1px solid var(--sms-rule); list-style: none; }
.sms-chapstory .sms-chapstory__point { display: flex; align-items: center; gap: 0.8rem; min-width: 0; padding: 0.8rem 0; border-bottom: 1px solid var(--sms-rule); font-weight: 500; }
.sms-chapstory .sms-chapstory__point-icon { width: 1.25rem; height: 1.25rem; color: var(--sms-green); }
.sms-chapstory .sms-chapstory__point-text { min-width: 0; }
.sms-chapstory .sms-chapstory__actions { display: flex; flex-wrap: wrap; align-items: center; gap: 1rem 1.75rem; }
.sms-page .sms-chaplink { min-width: 0; color: var(--sms-navy); font-weight: 500; text-decoration: underline; text-decoration-color: var(--sms-green); text-decoration-thickness: 1px; text-underline-offset: 0.35em; transition: color 0.3s var(--sms-ease); }
.sms-page .sms-chaplink:hover { color: var(--sms-green); }
/* Stage pieces */
.sms-chapstory .sms-chapstory__frame { position: relative; min-width: 0; min-height: 0; overflow: hidden; border-radius: 0.25rem; background: var(--sms-pale); }
.sms-chapstory .sms-chapstory__shot { position: absolute; inset: 0; z-index: 0; width: 100%; height: 100%; object-fit: cover; clip-path: inset(100% 0 0 0); transform: scale(1.14); transition: clip-path 1.15s var(--sms-wipe), transform 1.9s var(--sms-soft); }
.sms-chapstory[data-dir="up"] .sms-chapstory__shot:not(.is-active):not(.is-prev) { clip-path: inset(0 0 100% 0); }
.sms-chapstory .sms-chapstory__shot.is-prev { z-index: 1; clip-path: inset(0 0 0 0); transform: scale(1); }
.sms-chapstory .sms-chapstory__shot.is-active { z-index: 2; clip-path: inset(0 0 0 0); transform: scale(1); }
.sms-chapstory .sms-chapstory__meta { display: grid; grid-template-columns: 8.5rem minmax(0, 1fr); gap: 1.5rem; align-items: end; min-width: 0; padding-top: 1.25rem; border-top: 1px solid var(--sms-navy); }
.sms-chapstory .sms-chapstory__numerals { position: relative; min-width: 0; height: 5.6rem; overflow: hidden; }
.sms-chapstory .sms-chapstory__numeral,
.sms-chapsteps .sms-chapsteps__numeral { position: absolute; left: 0; bottom: 0; color: var(--sms-green); font-family: var(--sms-serif); font-weight: 300; line-height: 1; letter-spacing: -0.03em; opacity: 0; transform: translateY(70%); transition: opacity 0.6s var(--sms-ease), transform 0.9s var(--sms-soft); }
.sms-chapstory .sms-chapstory__numeral { font-size: 5.5rem; font-style: italic; }
.sms-chapstory .sms-chapstory__numeral.is-done,
.sms-chapsteps .sms-chapsteps__numeral.is-done { opacity: 0; transform: translateY(-70%); }
.sms-chapstory .sms-chapstory__numeral.is-active,
.sms-chapsteps .sms-chapsteps__numeral.is-active { opacity: 1; transform: none; }
.sms-chapstory .sms-chapstory__progress { display: grid; gap: 0.85rem; min-width: 0; padding-bottom: 0.9rem; }
.sms-chapstory .sms-chapstory__rail,
.sms-chapsteps .sms-chapsteps__rail { display: grid; grid-auto-columns: minmax(0, 1fr); grid-auto-flow: column; gap: 0.4rem; min-width: 0; }
.sms-chapstory .sms-chapstory__tick,
.sms-chapsteps .sms-chapsteps__tick { position: relative; min-width: 0; height: 2px; overflow: hidden; background: var(--sms-line); }
.sms-chapstory .sms-chapstory__tick-fill,
.sms-chapsteps .sms-chapsteps__tick-fill { position: absolute; inset: 0; background: var(--sms-green); transform: scaleX(0); transform-origin: left; transition: transform 0.8s var(--sms-soft); }
.sms-chapstory .sms-chapstory__tick.is-done .sms-chapstory__tick-fill,
.sms-chapsteps .sms-chapsteps__tick.is-done .sms-chapsteps__tick-fill { transform: scaleX(1); }
.sms-chapstory .sms-chapstory__captions { position: relative; min-width: 0; height: 1.5rem; }
.sms-chapstory .sms-chapstory__caption { position: absolute; left: 0; top: 0; right: 0; overflow: hidden; color: var(--sms-ink-soft); font-size: 0.8125rem; white-space: nowrap; text-overflow: ellipsis; opacity: 0; transform: translateY(6px); transition: opacity 0.5s var(--sms-ease), transform 0.6s var(--sms-ease); }
.sms-chapstory .sms-chapstory__caption.is-active { opacity: 1; transform: none; }
@media (min-width: 48em) {
  .sms-chapstory .sms-chapstory__chapter { grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); gap: 3rem 4rem; }
  .sms-chapstory .sms-chapstory__chapter:nth-child(even) .sms-chapstory__photo { order: 2; }
  .sms-chapstory .sms-chapstory__photo-frame { aspect-ratio: 4 / 4.6; }
}
@media (min-width: 60em) {
  .sms-chapstory .sms-chapstory__head { grid-template-columns: minmax(0, 1.4fr) minmax(0, 0.6fr); }
  .sms-chapstory .sms-chapstory__title { margin-bottom: 0; }
  .sms-chapstory .sms-chapstory__lead { padding-bottom: 0.6rem; }
  .sms-chapstory.is-scrolly .sms-chapstory__body { display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 0.95fr); gap: clamp(3rem, 1rem + 5vw, 7rem); align-items: start; }
  .sms-chapstory.is-scrolly .sms-chapstory__stage { position: sticky; top: 6rem; display: grid; grid-template-rows: minmax(0, 1fr) auto; gap: 1.5rem; height: calc(100vh - 7.5rem); min-height: 30rem; max-height: 54rem; }
  .sms-chapstory.is-scrolly .sms-chapstory__list { gap: 0; }
  .sms-chapstory.is-scrolly .sms-chapstory__chapter { display: flex; align-items: center; min-height: calc(100vh - 6rem); padding: 3rem 0; }
  .sms-chapstory.is-scrolly .sms-chapstory__chapter:first-child { min-height: calc(100vh - 12rem); align-items: flex-start; padding-top: 6rem; }
  .sms-chapstory.is-scrolly .sms-chapstory__photo { display: none; }
  .sms-chapstory.is-scrolly .sms-chapstory__text { padding-left: 2.5rem; }
  .sms-chapstory.is-scrolly .sms-chapstory__text::before { content: ""; position: absolute; left: 0; top: 0.4rem; bottom: 0.4rem; width: 1px; background: var(--sms-line); }
  .sms-chapstory.is-scrolly .sms-chapstory__text::after { content: ""; position: absolute; left: 0; top: 0.4rem; bottom: 0.4rem; width: 2px; margin-left: -0.5px; background: var(--sms-green); transform: scaleY(0); transform-origin: top; transition: transform 1s var(--sms-soft); }
  .sms-chapstory.is-scrolly .sms-chapstory__chapter.is-active .sms-chapstory__text::after { transform: scaleY(1); }
}

/* ---------- Home: contents (services index) ---------- */
.sms-chapindex { position: relative; padding: var(--sms-section) 0; background: var(--sms-pale); }
.sms-chapindex .sms-chapindex__inner { display: grid; gap: 3rem; width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-chapindex .sms-chapindex__main { min-width: 0; }
.sms-chapindex .sms-chapindex__head { max-width: 40rem; margin-bottom: clamp(2rem, 1.5rem + 2vw, 3.5rem); }
.sms-chapindex .sms-chapindex__title { margin: 0 0 1rem; font-family: var(--sms-serif); font-size: var(--sms-step-2); font-weight: 350; line-height: 1.08; letter-spacing: -0.02em; }
.sms-chapindex .sms-chapindex__lead { color: var(--sms-ink-soft); font-size: var(--sms-step-1); line-height: 1.55; }
.sms-chapindex .sms-chapindex__lead p { margin: 0; }
.sms-chapindex .sms-chapindex__list { margin: 0; padding: 0; border-top: 1px solid var(--sms-navy); list-style: none; }
.sms-chapindex .sms-chapindex__item { min-width: 0; border-bottom: 1px solid var(--sms-rule); }
.sms-chapindex .sms-chapindex__row { position: relative; display: grid; grid-template-columns: 2.5rem minmax(0, 1fr) auto; gap: 0 1rem; align-items: center; padding: 1.6rem 0; color: var(--sms-navy); text-decoration: none; }
.sms-chapindex .sms-chapindex__row::after { content: ""; position: absolute; left: 0; right: 0; bottom: -1px; height: 1px; background: var(--sms-green); transform: scaleX(0); transform-origin: left; transition: transform 0.7s var(--sms-soft); }
.sms-chapindex .sms-chapindex__row:hover::after,
.sms-chapindex .sms-chapindex__row:focus-visible::after { transform: scaleX(1); }
.sms-chapindex .sms-chapindex__num { align-self: start; min-width: 0; padding-top: 0.5rem; color: var(--sms-ink-soft); font-family: var(--sms-serif); font-size: 1.0625rem; font-style: italic; transition: color 0.4s var(--sms-ease); }
.sms-chapindex .sms-chapindex__body { display: grid; gap: 0.45rem; min-width: 0; }
.sms-chapindex .sms-chapindex__name { min-width: 0; font-family: var(--sms-serif); font-size: clamp(1.7rem, 1.2rem + 2vw, 2.9rem); font-weight: 350; line-height: 1.06; letter-spacing: -0.02em; transition: transform 0.6s var(--sms-soft), color 0.4s var(--sms-ease); }
.sms-chapindex .sms-chapindex__text { min-width: 0; max-width: 34rem; color: var(--sms-ink-soft); font-size: 0.9375rem; line-height: 1.6; }
.sms-chapindex .sms-chapindex__go { display: grid; place-items: center; min-width: 0; width: 2.75rem; height: 2.75rem; border: 1px solid rgba(6, 30, 53, 0.25); border-radius: 50%; color: var(--sms-navy); transition: background-color 0.4s var(--sms-ease), color 0.4s var(--sms-ease), border-color 0.4s var(--sms-ease), transform 0.5s var(--sms-soft); }
.sms-chapindex .sms-chapindex__go-icon { width: 1.1rem; height: 1.1rem; }
.sms-chapindex .sms-chapindex__row:hover .sms-chapindex__name { transform: translateX(0.5rem); }
.sms-chapindex .sms-chapindex__row:hover .sms-chapindex__go,
.sms-chapindex .sms-chapindex__row:focus-visible .sms-chapindex__go { border-color: var(--sms-navy); background: var(--sms-navy); color: var(--sms-white); }
.sms-chapindex .sms-chapindex__also { margin: 3rem 0 0; padding-bottom: 0.8rem; border-bottom: 1px solid var(--sms-navy); color: var(--sms-ink-soft); font-size: 0.75rem; font-weight: 600; letter-spacing: 0.2em; text-transform: uppercase; }
.sms-chapindex .sms-chapindex__list--minor { border-top: 0; }
.sms-chapindex .sms-chapindex__item--minor .sms-chapindex__row { padding: 1.2rem 0; }
.sms-chapindex .sms-chapindex__item--minor .sms-chapindex__name { font-size: clamp(1.3rem, 1.1rem + 0.8vw, 1.7rem); }
.sms-chapindex .sms-chapindex__item--minor .sms-chapindex__num { padding-top: 0.25rem; }
.sms-chapindex .sms-chapindex__aside { display: none; min-width: 0; }
.sms-chapindex .sms-chapindex__figure { min-width: 0; margin: 0; }
.sms-chapindex .sms-chapindex__frame { position: relative; overflow: hidden; aspect-ratio: 4 / 5; border-radius: 0.25rem; background: var(--sms-mint); }
.sms-chapindex .sms-chapindex__shot { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; opacity: 0; transform: scale(1.06); transition: opacity 0.8s var(--sms-ease), transform 1.6s var(--sms-soft); }
.sms-chapindex .sms-chapindex__caps { position: relative; min-width: 0; height: 1.5rem; margin-top: 0.9rem; }
.sms-chapindex .sms-chapindex__cap { position: absolute; left: 0; top: 0; display: flex; gap: 0.75rem; color: var(--sms-ink-soft); font-size: 0.8125rem; opacity: 0; transform: translateY(6px); transition: opacity 0.5s var(--sms-ease), transform 0.6s var(--sms-ease); }
.sms-chapindex .sms-chapindex__cap::before { content: ""; flex: 0 0 auto; width: 1.5rem; height: 1px; margin-top: 0.72em; background: var(--sms-navy); }
""" + _index_css() + r"""
@media (min-width: 60em) {
  .sms-chapindex .sms-chapindex__inner { grid-template-columns: minmax(0, 1.25fr) minmax(0, 0.75fr); gap: clamp(3rem, 1rem + 5vw, 6.5rem); align-items: start; }
  .sms-chapindex .sms-chapindex__aside { position: sticky; top: 7rem; display: block; margin-top: 7.5rem; }
}

/* ---------- Home: pull-quote on a navy island ---------- */
.sms-chapquote { position: relative; overflow: clip; padding: clamp(5rem, 3.5rem + 6vw, 10rem) 0; background: var(--sms-navy); color: var(--sms-white); }
.sms-chapquote .sms-chapquote__inner { position: relative; width: 100%; max-width: 68rem; margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-chapquote .sms-chapquote__glyph { position: absolute; right: var(--sms-gutter); top: -3rem; color: rgba(130, 208, 110, 0.16); font-family: var(--sms-serif); font-size: clamp(10rem, 6rem + 14vw, 22rem); font-weight: 300; line-height: 1; pointer-events: none; }
.sms-chapquote .sms-chapquote__glyph::before { content: "\201C"; }
.sms-chapquote .sms-chaplabel { color: var(--sms-green-on-navy); }
.sms-chapquote .sms-chapquote__fig { position: relative; margin: 0; }
.sms-chapquote .sms-chapquote__text { margin: 0; color: var(--sms-white); font-family: var(--sms-serif); font-size: clamp(1.7rem, 0.95rem + 3vw, 3.5rem); font-weight: 300; line-height: 1.2; letter-spacing: -0.015em; }
.sms-chapquote .sms-chapquote__text p { margin: 0; }
.sms-chapquote .sms-chapquote__w--open { margin-left: -0.42em; }
.sms-chapquote .sms-chapquote__w--em { color: var(--sms-green-on-navy); font-style: italic; }
.sms-chapquote .sms-chapquote__cite { display: flex; align-items: center; gap: 1rem; margin-top: clamp(2.5rem, 2rem + 2vw, 3.5rem); padding-top: 1.5rem; border-top: 1px solid rgba(255, 255, 255, 0.16); }
.sms-chapquote .sms-chapquote__face { flex: 0 0 auto; min-width: 0; width: 4rem; height: 4rem; border-radius: 0.25rem; object-fit: cover; }
.sms-chapquote .sms-chapquote__who { display: grid; gap: 0.15rem; min-width: 0; }
.sms-chapquote .sms-chapquote__name { min-width: 0; color: var(--sms-white); font-family: var(--sms-serif); font-size: 1.25rem; font-weight: 400; font-style: normal; }
.sms-chapquote .sms-chapquote__role { min-width: 0; color: rgba(255, 255, 255, 0.78); font-size: 0.875rem; }
@media (min-width: 60em) {
  .sms-chapquote .sms-chapquote__glyph { right: -2rem; top: -6rem; }
}
""" + _quote_css() + r"""

/* ---------- Home: about with a drop cap ---------- */
.sms-chapabout { position: relative; padding: var(--sms-section) 0; background: var(--sms-white); }
.sms-chapabout .sms-chapabout__inner { display: grid; gap: clamp(3rem, 2rem + 3vw, 5rem); width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-chapabout .sms-chapabout__main { min-width: 0; }
.sms-chapabout .sms-chapabout__title { margin: 0 0 2rem; font-family: var(--sms-serif); font-size: var(--sms-step-2); font-weight: 350; line-height: 1.08; letter-spacing: -0.02em; }
.sms-chapabout .sms-chapabout__body { max-width: 40rem; color: var(--sms-navy); font-size: clamp(1.0625rem, 1rem + 0.25vw, 1.1875rem); line-height: 1.75; }
.sms-chapabout .sms-chapabout__body > p { margin: 0 0 1rem; }
.sms-chapabout .sms-chapabout__body .sms-more__body { color: var(--sms-navy); }
.sms-chapabout .sms-chapabout__actions { display: flex; flex-wrap: wrap; gap: 0.75rem; margin-top: 2.25rem; }
.sms-chapabout .sms-chapabout__aside { min-width: 0; }
.sms-chapabout .sms-chapabout__values { margin: 0; padding: 0; border-top: 1px solid var(--sms-navy); list-style: none; }
.sms-chapabout .sms-chapabout__value { display: grid; grid-template-columns: 2.5rem minmax(0, 1fr); gap: 0 1rem; min-width: 0; padding: 1.35rem 0; border-bottom: 1px solid var(--sms-rule); }
.sms-chapabout .sms-chapabout__value-num { min-width: 0; padding-top: 0.15rem; color: var(--sms-green); font-family: var(--sms-serif); font-size: 1.0625rem; font-style: italic; }
.sms-chapabout .sms-chapabout__value-body { min-width: 0; }
.sms-chapabout .sms-chapabout__value-title { margin: 0 0 0.3rem; font-family: var(--sms-serif); font-size: 1.25rem; font-weight: 450; line-height: 1.25; }
.sms-chapabout .sms-chapabout__value-text { margin: 0; color: var(--sms-ink-soft); font-size: 0.9375rem; line-height: 1.6; }
@media (min-width: 60em) {
  .sms-chapabout .sms-chapabout__inner { grid-template-columns: minmax(0, 1.2fr) minmax(0, 0.8fr); gap: clamp(4rem, 2rem + 5vw, 7rem); }
  .sms-chapabout .sms-chapabout__aside { padding-top: 2.4rem; }
}

/* ---------- Inner page hero (editorial) ---------- */
.sms-chaphero { position: relative; overflow: hidden; padding: clamp(2rem, 1rem + 3.5vw, 4.5rem) 0 clamp(3rem, 2rem + 4vw, 6rem); border-bottom: 1px solid var(--sms-line); background: var(--sms-white); }
.sms-chaphero .sms-chaphero__inner { display: grid; gap: clamp(2.5rem, 1.5rem + 3vw, 5rem); align-items: end; width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-chaphero .sms-chaphero__copy { min-width: 0; }
.sms-chaphero .sms-chaphero__crumb { display: flex; flex-wrap: wrap; gap: 0.5rem; margin-bottom: clamp(1.75rem, 1rem + 2.5vw, 3rem); color: var(--sms-ink-soft); font-size: 0.8125rem; animation: sms-chap-up 0.9s var(--sms-soft) 0.05s both; }
.sms-chaphero .sms-chaphero__crumb-link,
.sms-chaphero .sms-chaphero__crumb-sep,
.sms-chaphero .sms-chaphero__crumb-here { min-width: 0; }
.sms-chaphero .sms-chaphero__crumb-link { color: var(--sms-ink-soft); text-underline-offset: 0.25em; }
.sms-chaphero .sms-chaphero__crumb-link:hover { color: var(--sms-navy); }
.sms-chaphero .sms-chaplabel { animation: sms-chap-up 0.9s var(--sms-soft) 0.15s both; }
.sms-chaphero .sms-chaphero__title { margin: 0 0 1.5rem; font-family: var(--sms-serif); font-size: clamp(2.6rem, 1.3rem + 4.6vw, 5.4rem); font-weight: 300; line-height: 1; letter-spacing: -0.03em; }
.sms-chaphero .sms-chaphero__mask { display: block; overflow: hidden; margin-bottom: -0.14em; padding: 0 0.12em 0.14em 0; }
.sms-chaphero .sms-chaphero__rise { display: block; animation: sms-chap-rise 1.2s var(--sms-soft) 0.15s both; }
.sms-chaphero .sms-chaphero__deck { margin: 0 0 1rem; color: var(--sms-navy); font-family: var(--sms-serif); font-size: clamp(1.25rem, 1.1rem + 0.6vw, 1.6rem); font-style: italic; font-weight: 300; line-height: 1.35; animation: sms-chap-up 0.9s var(--sms-soft) 0.35s both; }
.sms-chaphero .sms-chaphero__lead { max-width: 36rem; color: var(--sms-ink-soft); font-size: var(--sms-step-1); line-height: 1.6; animation: sms-chap-up 0.9s var(--sms-soft) 0.45s both; }
.sms-chaphero .sms-chaphero__lead p { margin: 0 0 0.75rem; }
.sms-chaphero .sms-chaphero__actions { display: flex; flex-wrap: wrap; gap: 0.75rem; margin-top: 1.75rem; animation: sms-chap-up 0.9s var(--sms-soft) 0.6s both; }
.sms-chaphero .sms-chaphero__notes { display: flex; flex-wrap: wrap; gap: 0.6rem 1.75rem; margin: 2.25rem 0 0; padding: 1.25rem 0 0; border-top: 1px solid var(--sms-rule); color: var(--sms-navy); font-size: 0.875rem; font-weight: 500; list-style: none; animation: sms-chap-up 0.9s var(--sms-soft) 0.75s both; }
.sms-chaphero .sms-chaphero__note { display: inline-flex; align-items: center; gap: 0.5rem; min-width: 0; }
.sms-chaphero .sms-chaphero__note-icon { width: 1.1rem; height: 1.1rem; color: var(--sms-green); }
.sms-chaphero .sms-chaphero__note-text { min-width: 0; }
.sms-chaphero .sms-chaphero__figure { min-width: 0; margin: 0; }
.sms-chaphero .sms-chaphero__frame { position: relative; overflow: hidden; aspect-ratio: 4 / 3; border-radius: 0.25rem; background: var(--sms-pale); }
.sms-chaphero .sms-chaphero__img { display: block; width: 100%; height: 100%; object-fit: cover; animation: sms-chap-settle 2.6s var(--sms-soft) 0.2s both; }
@media (min-width: 60em) {
  .sms-chaphero .sms-chaphero__inner { grid-template-columns: minmax(0, 1.3fr) minmax(0, 0.7fr); }
  .sms-chaphero .sms-chaphero__frame { aspect-ratio: 4 / 5; }
}

/* ---------- CTA: the closing line of an article ---------- */
.sms-chapcta { position: relative; padding: var(--sms-section) 0; background: var(--sms-white); }
.sms-chapcta .sms-chapcta__inner { width: 100%; max-width: 52rem; margin: 0 auto; padding: 0 var(--sms-gutter); text-align: center; }
.sms-chapcta .sms-chapcta__orn { display: flex; align-items: center; justify-content: center; gap: 1rem; margin-bottom: 2.25rem; color: var(--sms-green); }
.sms-chapcta .sms-chapcta__orn-line { min-width: 0; width: 3.5rem; height: 1px; background: currentColor; }
.sms-chapcta .sms-chapcta__orn-mark { min-width: 0; width: 0.45rem; height: 0.45rem; background: currentColor; transform: rotate(45deg); }
.sms-chapcta .sms-chapcta__title { margin: 0 0 1.5rem; font-family: var(--sms-serif); font-size: clamp(2.2rem, 1.3rem + 3.4vw, 4.4rem); font-weight: 300; line-height: 1.04; letter-spacing: -0.03em; }
.sms-chapcta .sms-chapcta__text { max-width: 40rem; margin: 0 auto; color: var(--sms-ink-soft); font-family: var(--sms-serif); font-size: clamp(1.125rem, 1rem + 0.45vw, 1.375rem); font-style: italic; font-weight: 300; line-height: 1.55; }
.sms-chapcta .sms-chapcta__text p { margin: 0 0 0.75rem; }
.sms-chapcta .sms-chapcta__text p:last-child { margin-bottom: 0; }
.sms-chapcta .sms-chapcta__text p:last-child::after { content: ""; display: inline-block; width: 0.5em; height: 0.5em; margin-left: 0.45em; background: var(--sms-green); }
.sms-chapcta .sms-chapcta__actions { display: flex; flex-wrap: wrap; justify-content: center; gap: 0.75rem; margin-top: 2.5rem; }
.sms-chapcta .sms-chapcta__call { margin: 1.5rem 0 0; color: var(--sms-ink-soft); font-size: 0.875rem; }
.sms-chapcta .sms-chapcta__call-link { color: var(--sms-navy); font-weight: 600; text-underline-offset: 0.3em; }

/* ---------- Risk & Needs Consultancy: the five steps as chapters ---------- */
.sms-chapsteps { position: relative; padding: var(--sms-section) 0; background: var(--sms-white); }
.sms-chapsteps .sms-chapsteps__inner { display: grid; gap: clamp(2.5rem, 1.5rem + 3vw, 5rem); width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-chapsteps .sms-chapsteps__aside { min-width: 0; }
.sms-chapsteps .sms-chapsteps__title { margin: 0 0 1.25rem; font-family: var(--sms-serif); font-size: var(--sms-step-2); font-weight: 350; line-height: 1.08; letter-spacing: -0.02em; }
.sms-chapsteps .sms-chapsteps__lead { max-width: 32rem; color: var(--sms-ink-soft); font-size: var(--sms-step-1); line-height: 1.6; }
.sms-chapsteps .sms-chapsteps__lead p { margin: 0; }
.sms-chapsteps .sms-chapsteps__meter { display: none; }
.sms-chapsteps .sms-chapsteps__numerals { position: relative; min-width: 0; width: 8.4rem; height: 7rem; overflow: hidden; }
.sms-chapsteps .sms-chapsteps__numeral { font-size: 7rem; line-height: 0.95; }
.sms-chapsteps .sms-chapsteps__of { min-width: 0; padding-bottom: 0.75rem; color: var(--sms-ink-soft); font-family: var(--sms-serif); font-size: 1.25rem; font-style: italic; }
.sms-chapsteps .sms-chapsteps__rail { grid-column: 1 / -1; margin-top: 1rem; }
.sms-chapsteps .sms-chapsteps__main { min-width: 0; }
.sms-chapsteps .sms-chapsteps__list { margin: 0; padding: 0; border-top: 1px solid var(--sms-navy); list-style: none; }
.sms-chapsteps .sms-chapsteps__step { position: relative; min-width: 0; padding: 2rem 0; border-bottom: 1px solid var(--sms-rule); }
.sms-chapsteps .sms-chapsteps__step-num,
.sms-chapsteps .sms-chapsteps__name,
.sms-chapsteps .sms-chapsteps__text { min-width: 0; }
.sms-chapsteps .sms-chapsteps__step-num { margin-bottom: 0.6rem; color: var(--sms-green); font-family: var(--sms-serif); font-size: 1.0625rem; font-style: italic; }
.sms-chapsteps .sms-chapsteps__name { margin: 0 0 0.75rem; font-family: var(--sms-serif); font-size: clamp(1.5rem, 1.2rem + 1.2vw, 2.3rem); font-weight: 400; line-height: 1.12; letter-spacing: -0.015em; transition: color 0.5s var(--sms-ease); }
.sms-chapsteps .sms-chapsteps__text { max-width: 36rem; color: var(--sms-ink-soft); font-size: 1.0625rem; line-height: 1.7; }
.sms-chapsteps .sms-chapsteps__text p { margin: 0; }
.sms-chapsteps .sms-chapsteps__note { display: flex; gap: 0.9rem; margin-top: 2.5rem; padding: 1.25rem 1.5rem; border-left: 3px solid var(--sms-green); background: var(--sms-pale); color: var(--sms-ink-soft); font-size: 0.9375rem; }
.sms-chapsteps .sms-chapsteps__note-icon { color: var(--sms-green); }
.sms-chapsteps .sms-chapsteps__note-text { min-width: 0; }
.sms-chapsteps .sms-chapsteps__note-text p { margin: 0; }
.sms-chapsteps .sms-chapsteps__actions { display: flex; flex-wrap: wrap; gap: 0.75rem; margin-top: 2rem; }
@media (min-width: 60em) {
  .sms-chapsteps .sms-chapsteps__inner { grid-template-columns: minmax(0, 0.9fr) minmax(0, 1.1fr); align-items: start; gap: clamp(3rem, 1rem + 5vw, 7rem); }
  .sms-chapsteps .sms-chapsteps__aside { align-self: stretch; }
  .sms-chapsteps .sms-chapsteps__sticky { position: sticky; top: 7rem; }
  .sms-chapsteps.is-scrolly .sms-chapsteps__meter { display: grid; grid-template-columns: auto minmax(0, 1fr); gap: 0.25rem 1.25rem; align-items: end; margin-top: 3rem; padding-top: 1.5rem; border-top: 1px solid var(--sms-navy); }
  .sms-chapsteps.is-scrolly .sms-chapsteps__list { border-top: 0; }
  .sms-chapsteps.is-scrolly .sms-chapsteps__step { display: flex; flex-direction: column; justify-content: center; min-height: 52vh; padding: 2.5rem 0 2.5rem 2.5rem; border-bottom: 0; }
  .sms-chapsteps.is-scrolly .sms-chapsteps__step::before { content: ""; position: absolute; left: 0; top: 2.5rem; bottom: 2.5rem; width: 1px; background: var(--sms-line); }
  .sms-chapsteps.is-scrolly .sms-chapsteps__step::after { content: ""; position: absolute; left: 0; top: 2.5rem; bottom: 2.5rem; width: 2px; margin-left: -0.5px; background: var(--sms-green); transform: scaleY(0); transform-origin: top; transition: transform 1s var(--sms-soft); }
  .sms-chapsteps.is-scrolly .sms-chapsteps__step.is-active::after { transform: scaleY(1); }
  .sms-chapsteps.is-scrolly .sms-chapsteps__step:not(.is-active) .sms-chapsteps__name { color: var(--sms-ink-soft); }
}

/* ---------- About: directors as editorial profile spreads ---------- */
.sms-chapdir { position: relative; padding: var(--sms-section) 0; background: var(--sms-white); }
.sms-chapdir .sms-chapdir__inner { width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-chapdir .sms-chapdir__top { display: grid; gap: 2.5rem; align-items: end; margin-bottom: clamp(3rem, 2rem + 4vw, 5.5rem); }
.sms-chapdir .sms-chapdir__head { min-width: 0; }
.sms-chapdir .sms-chapdir__title { margin: 0 0 1.25rem; font-family: var(--sms-serif); font-size: var(--sms-step-2); font-weight: 350; line-height: 1.08; letter-spacing: -0.02em; }
.sms-chapdir .sms-chapdir__lead { max-width: 34rem; color: var(--sms-ink-soft); font-size: var(--sms-step-1); line-height: 1.6; }
.sms-chapdir .sms-chapdir__lead p { margin: 0; }
.sms-chapdir .sms-chapdir__plate { min-width: 0; margin: 0; }
.sms-chapdir .sms-chapdir__plate-frame { overflow: hidden; aspect-ratio: 16 / 10; border-radius: 0.25rem; background: var(--sms-pale); }
.sms-chapdir .sms-chapdir__plate-img { display: block; width: 100%; height: 100%; object-fit: cover; }
.sms-chapdir .sms-chapdir__list { margin: 0; padding: 0; list-style: none; }
.sms-chapdir .sms-chapdir__spread { display: grid; gap: 2rem; min-width: 0; padding: clamp(2.5rem, 2rem + 3vw, 4.5rem) 0; border-top: 1px solid var(--sms-navy); }
.sms-chapdir .sms-chapdir__side { min-width: 0; }
.sms-chapdir .sms-chapdir__num { margin-bottom: 1rem; color: var(--sms-green); font-family: var(--sms-serif); font-size: 1.125rem; font-style: italic; }
.sms-chapdir .sms-chapdir__role { color: var(--sms-ink-soft); font-size: 0.75rem; font-weight: 600; letter-spacing: 0.2em; text-transform: uppercase; }
.sms-chapdir .sms-chapdir__name { margin: 0.6rem 0 1.75rem; font-family: var(--sms-serif); font-size: clamp(2.3rem, 1.5rem + 2.8vw, 3.9rem); font-weight: 300; line-height: 1.02; letter-spacing: -0.03em; }
.sms-chapdir .sms-chapdir__pulls { margin: 0; padding: 0; border-top: 1px solid var(--sms-rule); list-style: none; }
.sms-chapdir .sms-chapdir__pull { display: flex; align-items: baseline; gap: 0.85rem; min-width: 0; padding: 0.7rem 0; border-bottom: 1px solid var(--sms-rule); color: var(--sms-navy); font-family: var(--sms-serif); font-size: clamp(1.15rem, 1.05rem + 0.4vw, 1.375rem); font-style: italic; font-weight: 300; line-height: 1.3; }
.sms-chapdir .sms-chapdir__pull::before { content: ""; flex: 0 0 auto; width: 1rem; height: 1px; transform: translateY(-0.3em); background: var(--sms-green); }
.sms-chapdir .sms-chapdir__bio { min-width: 0; max-width: 40rem; color: var(--sms-navy); font-size: clamp(1.0625rem, 1rem + 0.25vw, 1.1875rem); line-height: 1.75; }
.sms-chapdir .sms-chapdir__bio > p { margin: 0 0 1rem; }
.sms-chapdir .sms-chapdir__bio .sms-more__body { color: var(--sms-navy); }
.sms-chapdir .sms-chapdir__shared { display: grid; gap: 1.5rem 4rem; margin-top: 1rem; padding: clamp(2rem, 1.2rem + 3vw, 4rem); border-radius: 0.25rem; background: var(--sms-navy); color: var(--sms-white); }
.sms-chapdir .sms-chapdir__shared-head { min-width: 0; }
.sms-chapdir .sms-chapdir__shared .sms-chaplabel { color: var(--sms-green-on-navy); }
.sms-chapdir .sms-chapdir__shared-title { margin: 0; color: var(--sms-white); font-family: var(--sms-serif); font-size: clamp(1.9rem, 1.3rem + 2.2vw, 3rem); font-weight: 300; line-height: 1.06; letter-spacing: -0.02em; }
.sms-chapdir .sms-chapdir__shared-body { min-width: 0; color: rgba(255, 255, 255, 0.88); font-size: 1.0625rem; }
.sms-chapdir .sms-chapdir__shared-body > p { margin: 0 0 1rem; }
.sms-chapdir .sms-chapdir__shared .sms-more__toggle { color: var(--sms-green-on-navy); }
.sms-chapdir .sms-chapdir__shared .sms-more__body { color: rgba(255, 255, 255, 0.88); }
.sms-chapdir .sms-chapdir__shared .sms-more__toggle:focus-visible { outline-color: var(--sms-green-on-navy); }
@media (min-width: 60em) {
  .sms-chapdir .sms-chapdir__top { grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); gap: 5rem; }
  .sms-chapdir .sms-chapdir__spread { grid-template-columns: minmax(0, 0.85fr) minmax(0, 1.15fr); gap: clamp(3rem, 1rem + 5vw, 7rem); }
  .sms-chapdir .sms-chapdir__spread:nth-child(even) .sms-chapdir__side { order: 2; }
  .sms-chapdir .sms-chapdir__shared { grid-template-columns: minmax(0, 0.8fr) minmax(0, 1.2fr); }
}
"""

RISE = [".sms-chapcover .sms-chapcover__figure", ".sms-chaphero .sms-chaphero__figure"]
ENTRANCE = []
REVEAL = [".sms-chapstory .sms-chapstory__head", ".sms-chapindex .sms-chapindex__head", ".sms-chapindex .sms-chapindex__item",
          ".sms-chapquote .sms-chapquote__cite", ".sms-chapabout .sms-chapabout__main", ".sms-chapabout .sms-chapabout__value",
          ".sms-chapcta .sms-chapcta__inner", ".sms-chapsteps .sms-chapsteps__aside", ".sms-chapsteps .sms-chapsteps__note",
          ".sms-chapdir .sms-chapdir__top", ".sms-chapdir .sms-chapdir__spread", ".sms-chapdir .sms-chapdir__shared"]
LOOP = [".sms-chapcover .sms-chapcover__kicker", ".sms-chapcover .sms-chapcover__rise", ".sms-chapcover .sms-chapcover__lead",
        ".sms-chapcover .sms-chapcover__actions", ".sms-chapcover .sms-chapcover__area", ".sms-chapcover .sms-chapcover__toc",
        ".sms-chapcover .sms-chapcover__img", ".sms-chapcover .sms-chapcover__curtain",
        ".sms-chaphero .sms-chaphero__crumb", ".sms-chaphero .sms-chaplabel", ".sms-chaphero .sms-chaphero__rise", ".sms-chaphero .sms-chaphero__deck",
        ".sms-chaphero .sms-chaphero__lead", ".sms-chaphero .sms-chaphero__actions", ".sms-chaphero .sms-chaphero__notes",
        ".sms-chaphero .sms-chaphero__img", ".sms-chaphero .sms-chaphero__curtain",
        ".sms-chapquote .sms-chapquote__w"]
TRANS = [".sms-chapmast .sms-chapmast__link", ".sms-chapcover .sms-chapcover__toc-go", ".sms-page .sms-chaplink",
         ".sms-cards .sms-cards__item::before", ".sms-links .sms-links__link::before",
         ".sms-chapstory .sms-chapstory__shot", ".sms-chapstory .sms-chapstory__numeral", ".sms-chapstory .sms-chapstory__tick-fill",
         ".sms-chapstory .sms-chapstory__caption", ".sms-chapstory.is-scrolly .sms-chapstory__text::after",
         ".sms-chapindex .sms-chapindex__row::after", ".sms-chapindex .sms-chapindex__num", ".sms-chapindex .sms-chapindex__name",
         ".sms-chapindex .sms-chapindex__go", ".sms-chapindex .sms-chapindex__shot", ".sms-chapindex .sms-chapindex__cap",
         ".sms-chapsteps .sms-chapsteps__numeral", ".sms-chapsteps .sms-chapsteps__tick-fill", ".sms-chapsteps .sms-chapsteps__name",
         ".sms-chapsteps.is-scrolly .sms-chapsteps__step::after"]

SKIP = {"risk-needs-consultancy": [0, 1, 2], "about": [0, 1, 2]}


# ---------------------------------------------------------------------------
# Shared pieces
# ---------------------------------------------------------------------------

def _caption(text, cls):
    return '<figcaption class="%s">%s</figcaption>' % (cls, e(text))


def page_hero(ctx, h):
    crumb = '<nav class="sms-chaphero__crumb" aria-label="Breadcrumb"><a class="sms-chaphero__crumb-link" href="%s">Home</a><span class="sms-chaphero__crumb-sep" aria-hidden="true">/</span><span class="sms-chaphero__crumb-here" aria-current="page">%s</span></nav>' % (
        ctx.href("home"), e(LABEL[ctx.slug]))
    deck = '<p class="sms-chaphero__deck">%s</p>' % e(h["sub"]) if h.get("sub") else ""
    acts = '<div class="sms-chaphero__actions">%s</div>' % buttons(ctx, h["buttons"]) if h.get("buttons") else ""
    notes = ""
    if h.get("chips"):
        notes = '<ul class="sms-chaphero__notes">%s</ul>' % "".join(
            '<li class="sms-chaphero__note">%s<span class="sms-chaphero__note-text">%s</span></li>' % (icon(ic, "sms-chaphero__note-icon"), e(t)) for ic, t in h["chips"])
    alt = C.PHOTOS[h["photo"]][4]
    return """<section class="sms-chaphero">
  <div class="sms-chaphero__inner">
    <div class="sms-chaphero__copy">
      %s
      <div class="sms-chaplabel">%s</div>
      <h1 class="sms-chaphero__title"><span class="sms-chaphero__mask"><span class="sms-chaphero__rise">%s</span></span></h1>
      %s
      <div class="sms-chaphero__lead">%s</div>
      %s
      %s
    </div>
    <figure class="sms-chaphero__figure">
      <div class="sms-chaphero__frame">%s<span class="sms-chaphero__curtain" aria-hidden="true"></span></div>
      %s
    </figure>
  </div>
</section>
""" % (crumb, e(h["eyebrow"]), e(h["title"]), deck, paras(h["body"]), acts, notes,
       photo_img(ctx, h["photo"], "sms-chaphero__img", lazy=False, decorative=True), _caption(alt, "sms-chaphero__caption"))


def cta(ctx, d):
    btns = [(l, t) for l, t in d["buttons"] if t != "tel"]
    has_tel = any(t == "tel" for _, t in d["buttons"])
    call = '<p class="sms-chapcta__call">Or call us on <a class="sms-chapcta__call-link" href="tel:%s">%s</a></p>' % (PHONE_TEL, PHONE) if has_tel else ""
    return """<section class="sms-chapcta">
  <div class="sms-chapcta__inner">
    <div class="sms-chapcta__orn" aria-hidden="true"><span class="sms-chapcta__orn-line"></span><span class="sms-chapcta__orn-mark"></span><span class="sms-chapcta__orn-line"></span></div>
    <h2 class="sms-chapcta__title">%s</h2>
    <div class="sms-chapcta__text">%s</div>
    <div class="sms-chapcta__actions">%s</div>
    %s
  </div>
</section>
""" % (e(d["title"]), paras(d["text"]), buttons(ctx, btns), call)


def chrome_top(ctx):
    mast = """<div class="sms-chapmast">
  <div class="sms-chapmast__inner">
    <p class="sms-chapmast__strap">%s</p>
    <div class="sms-chapmast__links"><a class="sms-chapmast__link" href="tel:%s">%s</a><a class="sms-chapmast__link" href="mailto:%s">%s</a></div>
  </div>
</div>
""" % (e(STRAP_CONSULT), PHONE_TEL, PHONE, EMAIL, EMAIL)
    return mast + header(ctx, "blue")


def chrome_bottom(ctx):
    return footer(ctx, "white")


# ---------------------------------------------------------------------------
# Inner page extras
# ---------------------------------------------------------------------------

def consult_steps(ctx):
    items = CONSULT["items"]
    n = len(items)
    numerals = "".join('<span class="sms-chapsteps__numeral" data-sms-at="%d">%02d</span>' % (i, i + 1) for i in range(n))
    ticks = "".join('<span class="sms-chapsteps__tick" data-sms-at="%d"><span class="sms-chapsteps__tick-fill"></span></span>' % i for i in range(n))
    steps = "".join("""<li class="sms-chapsteps__step" data-sms-scrolly-item data-sms-at="%d" data-i="%d">
          <div class="sms-chapsteps__step-num">Step %02d</div>
          <h3 class="sms-chapsteps__name">%s</h3>
          <div class="sms-chapsteps__text"><p>%s</p></div>
        </li>""" % (i, i, i + 1, e(it["title"]), e(it["text"])) for i, it in enumerate(items))
    return """<section class="sms-chapsteps" id="consultation" data-sms-scrolly>
  <div class="sms-chapsteps__inner">
    <div class="sms-chapsteps__aside">
      <div class="sms-chapsteps__sticky">
        <div class="sms-chaplabel">%s</div>
        <h2 class="sms-chapsteps__title">%s</h2>
        <div class="sms-chapsteps__lead">%s</div>
        <div class="sms-chapsteps__meter" aria-hidden="true">
          <div class="sms-chapsteps__numerals">%s</div>
          <div class="sms-chapsteps__of">of %02d</div>
          <div class="sms-chapsteps__rail">%s</div>
        </div>
      </div>
    </div>
    <div class="sms-chapsteps__main">
      <ol class="sms-chapsteps__list">%s</ol>
      <div class="sms-chapsteps__note">%s<div class="sms-chapsteps__note-text">%s</div></div>
      <div class="sms-chapsteps__actions">%s</div>
    </div>
  </div>
</section>
""" % (e(CONSULT["eyebrow"]), e(CONSULT["title"]), paras(CONSULT["lead"]), numerals, n, ticks, steps,
       icon("alert", "sms-chapsteps__note-icon"), paras(CONSULT["note"]), buttons(ctx, [("Request a FREE initial Consultation", "book:consultancy")]))


def directors(ctx):
    spreads = ""
    for i, p in enumerate(PEOPLE["items"]):
        pulls = "".join('<li class="sms-chapdir__pull">%s</li>' % e(t.strip()) for t in p["tags"].split("·"))
        spreads += """<li class="sms-chapdir__spread">
        <div class="sms-chapdir__side">
          <div class="sms-chapdir__num" aria-hidden="true">%s</div>
          <div class="sms-chapdir__role">Director</div>
          <h3 class="sms-chapdir__name">%s</h3>
          <ul class="sms-chapdir__pulls">%s</ul>
        </div>
        <div class="sms-chapdir__bio sms-chapdrop"><p>%s</p>%s</div>
      </li>""" % (ROMAN[i], e(p["name"]), pulls, e(p["bio"][0]), more(paras(p["bio"][1:])))
    s = PEOPLE["shared"]
    alt = C.PHOTOS[PEOPLE["photo"]][4]
    return """<section class="sms-chapdir" id="directors">
  <div class="sms-chapdir__inner">
    <div class="sms-chapdir__top">
      <div class="sms-chapdir__head">
        <div class="sms-chaplabel">%s</div>
        <h2 class="sms-chapdir__title">%s</h2>
        <div class="sms-chapdir__lead">%s</div>
      </div>
      <figure class="sms-chapdir__plate"><div class="sms-chapdir__plate-frame">%s</div>%s</figure>
    </div>
    <ol class="sms-chapdir__list">%s</ol>
    <div class="sms-chapdir__shared">
      <div class="sms-chapdir__shared-head"><div class="sms-chaplabel">%s</div><h3 class="sms-chapdir__shared-title">%s</h3></div>
      <div class="sms-chapdir__shared-body"><p>%s</p>%s</div>
    </div>
  </div>
</section>
""" % (e(PEOPLE["eyebrow"]), e(PEOPLE["title"]), paras(PEOPLE["lead"]),
       photo_img(ctx, PEOPLE["photo"], "sms-chapdir__plate-img", decorative=True), _caption(alt, "sms-chapdir__plate-cap"),
       spreads, e(s["label"]), e(s["title"]), e(s["text"][0]), more(paras(s["text"][1:])))


def inner_extra(ctx, slug):
    secs = C.PAGES[slug]["sections"]
    if slug == "risk-needs-consultancy":
        return SHARED_RENDERERS["feature"](ctx, secs[0][1]) + SHARED_RENDERERS["cards"](ctx, secs[1][1]) + consult_steps(ctx)
    if slug == "about":
        return SHARED_RENDERERS["quotes"](ctx, secs[0][1]) + SHARED_RENDERERS["cards"](ctx, secs[1][1]) + directors(ctx)
    return ""


# ---------------------------------------------------------------------------
# Homepage
# ---------------------------------------------------------------------------

def cover(ctx):
    kicker = "".join('<li class="sms-chapcover__kicker-item"><a class="sms-chapcover__kicker-link" href="%s">%s</a></li>' % (ctx.href(s["slug"]), e(s["title"])) for s in C.SERVICES)
    toc = "".join("""<li class="sms-chapcover__toc-item"><a class="sms-chapcover__toc-link" href="#chapter-%d">
          <span class="sms-chapcover__toc-num" aria-hidden="true">%s</span>
          <span class="sms-chapcover__toc-body"><span class="sms-chapcover__toc-name">%s</span><span class="sms-chapcover__toc-svc">%s</span></span>
          <span class="sms-chapcover__toc-go" aria-hidden="true">&darr;</span>
        </a></li>""" % (i + 1, ROMAN[i], e(line), e(svc["title"])) for i, (line, svc, _, _) in enumerate(CHAPTERS))
    first, second = [x.strip() + "." for x in C.STRAP.split(".") if x.strip()]
    return """<section class="sms-chapcover">
  <div class="sms-chapcover__inner">
    <div class="sms-chapcover__top">
      <ul class="sms-chapcover__kicker" aria-label="Our services">%s</ul>
      <p class="sms-chapcover__folio">Streamline Safety &amp; Medical Solutions</p>
    </div>
    <h1 class="sms-chapcover__title"><span class="sms-chapcover__line"><span class="sms-chapcover__rise">%s</span></span><span class="sms-chapcover__line"><span class="sms-chapcover__rise sms-mark">%s</span></span></h1>
    <div class="sms-chapcover__grid">
      <div class="sms-chapcover__copy">
        <p class="sms-chapcover__lead">%s</p>
        <div class="sms-chapcover__actions">%s</div>
        <p class="sms-chapcover__area">%s<span class="sms-chapcover__area-text">%s</span></p>
      </div>
      <figure class="sms-chapcover__figure">
        <div class="sms-chapcover__frame">%s<span class="sms-chapcover__curtain" aria-hidden="true"></span></div>
        %s
      </figure>
    </div>
    <ol class="sms-chapcover__toc" aria-label="Chapters">%s</ol>
  </div>
</section>
""" % (kicker, e(first), e(second), e(C.INTRO), buttons(ctx, [("Book online", "book"), ("Call 01283 358789", "tel")]),
       icon("pin", "sms-chapcover__area-icon"), e(C.AREA),
       photo_img(ctx, "team", "sms-chapcover__img", lazy=False, decorative=True), _caption(C.PHOTOS["team"][4], "sms-chapcover__caption"), toc)


def story(ctx):
    n = len(CHAPTERS)
    shots = "".join('<img class="sms-chapstory__shot" data-sms-at="%d" src="%s" alt="" width="%d" height="%d" loading="lazy" style="object-position: %s">' % (
        i, ctx.asset("photos/" + C.PHOTOS[k][0]), C.PHOTOS[k][1], C.PHOTOS[k][2], C.PHOTOS[k][3]) for i, (_, _, k, _) in enumerate(CHAPTERS))
    numerals = "".join('<span class="sms-chapstory__numeral" data-sms-at="%d">%s</span>' % (i, ROMAN[i]) for i in range(n))
    ticks = "".join('<span class="sms-chapstory__tick" data-sms-at="%d"><span class="sms-chapstory__tick-fill"></span></span>' % i for i in range(n))
    caps = "".join('<span class="sms-chapstory__caption" data-sms-at="%d">Chapter %s of %s &middot; %s</span>' % (i, ROMAN[i], ROMAN[n - 1], e(svc["title"])) for i, (_, svc, _, _) in enumerate(CHAPTERS))
    chapters = ""
    for i, (line, svc, ph, picks) in enumerate(CHAPTERS):
        pts = "".join('<li class="sms-chapstory__point">%s<span class="sms-chapstory__point-text">%s</span></li>' % (icon(svc["list"][j][0], "sms-chapstory__point-icon"), e(svc["list"][j][1])) for j in picks)
        chapters += """<li class="sms-chapstory__chapter" id="chapter-%d" data-sms-scrolly-item data-sms-at="%d" data-i="%d">
          <figure class="sms-chapstory__photo"><div class="sms-chapstory__photo-frame">%s</div></figure>
          <div class="sms-chapstory__text">
            <div class="sms-chapstory__label"><span class="sms-chapstory__roman">Chapter %s</span><span class="sms-chapstory__service">%s</span></div>
            <h3 class="sms-chapstory__name">%s</h3>
            <p class="sms-chapstory__desc">%s</p>
            <ul class="sms-chapstory__points">%s</ul>
            <div class="sms-chapstory__actions">%s<a class="sms-chaplink" href="%s">Explore %s</a></div>
          </div>
        </li>""" % (i + 1, i, i, photo_img(ctx, ph, "sms-chapstory__photo-img"), ROMAN[i], e(svc["title"]), e(line), e(svc["text"]), pts,
                    buttons(ctx, [(svc["cta"], "book:" + svc["key"])]), ctx.href(svc["slug"]), e(svc["title"]))
    lines = "".join('<span class="sms-chapstory__title-line%s">%s</span>' % (" sms-mark" if i == len(CHAPTER_LINES) - 1 else "", e(l)) for i, l in enumerate(CHAPTER_LINES))
    return """<section class="sms-chapstory" id="chapters" data-sms-scrolly>
  <div class="sms-chapstory__inner">
    <div class="sms-chapstory__head">
      <div class="sms-chapstory__head-main">
        <div class="sms-chaplabel">Our services, in three chapters</div>
        <h2 class="sms-chapstory__title">%s</h2>
      </div>
      <div class="sms-chapstory__lead"><p>%s</p></div>
    </div>
    <div class="sms-chapstory__body">
      <div class="sms-chapstory__stage" aria-hidden="true">
        <div class="sms-chapstory__frame">%s</div>
        <div class="sms-chapstory__meta">
          <div class="sms-chapstory__numerals">%s</div>
          <div class="sms-chapstory__progress"><div class="sms-chapstory__rail">%s</div><div class="sms-chapstory__captions">%s</div></div>
        </div>
      </div>
      <ol class="sms-chapstory__list">%s</ol>
    </div>
  </div>
</section>
""" % (lines, e(C.INTRO2), shots, numerals, ticks, caps, chapters)


def contents(ctx):
    major = minor = ""
    shots = caps = ""
    for i, (title, text, slug, ph, is_minor) in enumerate(INDEX):
        row = """<li class="sms-chapindex__item sms-chapindex__item--%d%s"><a class="sms-chapindex__row" href="%s" data-i="%d">
          <span class="sms-chapindex__num" aria-hidden="true">%02d</span>
          <span class="sms-chapindex__body"><span class="sms-chapindex__name">%s</span><span class="sms-chapindex__text">%s</span></span>
          <span class="sms-chapindex__go" aria-hidden="true">%s</span>
        </a></li>""" % (i, " sms-chapindex__item--minor" if is_minor else "", ctx.href(slug), i, i + 1, e(title), e(text), icon("arrow", "sms-chapindex__go-icon"))
        if is_minor:
            minor += row
        else:
            major += row
        f, w, h, focus, _ = C.PHOTOS[ph]
        ctx.photos.append("assets/photos/" + f)
        shots += '<img class="sms-chapindex__shot sms-chapindex__shot--%d" src="%s" alt="" width="%d" height="%d" loading="lazy" style="object-position: %s">' % (i, ctx.asset("photos/" + f), w, h, focus)
        caps += '<span class="sms-chapindex__cap sms-chapindex__cap--%d">%02d &middot; %s</span>' % (i, i + 1, e(title))
    return """<section class="sms-chapindex" id="contents" data-sms-index data-active="0">
  <div class="sms-chapindex__inner">
    <div class="sms-chapindex__main">
      <div class="sms-chapindex__head">
        <div class="sms-chaplabel">Contents</div>
        <h2 class="sms-chapindex__title">What We <span class="sms-mark">Provide</span></h2>
        <div class="sms-chapindex__lead"><p>%s</p></div>
      </div>
      <ol class="sms-chapindex__list">%s</ol>
      <div class="sms-chapindex__also">Also from Streamline</div>
      <ol class="sms-chapindex__list sms-chapindex__list--minor" start="4">%s</ol>
    </div>
    <div class="sms-chapindex__aside" aria-hidden="true">
      <figure class="sms-chapindex__figure"><div class="sms-chapindex__frame">%s</div><div class="sms-chapindex__caps">%s</div></figure>
    </div>
  </div>
</section>
""" % (e(C.AREA), major, minor, shots, caps)


def pullquote(ctx):
    words = []
    for i, w in enumerate(QUOTE_WORDS):
        cls = "sms-chapquote__w"
        if i == 0:
            cls += " sms-chapquote__w--open"
        if i >= QUOTE_EM_FROM:
            cls += " sms-chapquote__w--em"
        words.append('<span class="%s">%s</span>' % (cls, e(w)))
    return """<section class="sms-chapquote" aria-label="A word from Mathew Stones">
  <div class="sms-chapquote__inner">
    <span class="sms-chapquote__glyph" aria-hidden="true"></span>
    <div class="sms-chaplabel">From the directors</div>
    <figure class="sms-chapquote__fig">
      <blockquote class="sms-chapquote__text"><p>%s</p></blockquote>
      <figcaption class="sms-chapquote__cite">%s<span class="sms-chapquote__who"><span class="sms-chapquote__name">Mathew Stones</span><span class="sms-chapquote__role">Director, alongside fellow director Thomas Wilkes</span></span></figcaption>
    </figure>
  </div>
</section>
""" % (" ".join(words), photo_img(ctx, "directors", "sms-chapquote__face", decorative=True))


def about(ctx):
    vals = "".join('<li class="sms-chapabout__value"><span class="sms-chapabout__value-num" aria-hidden="true">%02d</span><div class="sms-chapabout__value-body"><h3 class="sms-chapabout__value-title">%s</h3><p class="sms-chapabout__value-text">%s</p></div></li>' % (
        i + 1, e(t), e(x)) for i, (_, t, x) in enumerate(C.TRUST))
    return """<section class="sms-chapabout" id="about">
  <div class="sms-chapabout__inner">
    <div class="sms-chapabout__main">
      <div class="sms-chaplabel">About Streamline</div>
      <h2 class="sms-chapabout__title">%s</h2>
      <div class="sms-chapabout__body sms-chapdrop"><p>%s</p>%s</div>
      <div class="sms-chapabout__actions">%s</div>
    </div>
    <div class="sms-chapabout__aside">
      <ul class="sms-chapabout__values" aria-label="What you can expect">%s</ul>
    </div>
  </div>
</section>
""" % (e(C.PAGES["about"]["hero"]["title"]), e(C.ABOUT_HOME[0]), more(paras(C.ABOUT_HOME[1:])),
       buttons(ctx, [("Meet The Directors", "about")]).replace("sms-btn--primary", "sms-btn--outline"), vals)


def home(ctx):
    ctx.notes.append("Chapter headings use the strapline \"Assess the risk. Plan the response. Protect your people.\" from the Risk & Needs Consultancy page")
    ctx.notes.append("Mathew Stones quote words light up as it scrolls into view (scroll-driven CSS); fully visible without support or with reduced motion")
    out = cover(ctx)
    out += story(ctx)
    out += contents(ctx)
    out += pullquote(ctx)
    out += about(ctx)
    picks = ["What is Streamline Safety & Medical Solutions?", "What does “Protecting People. Supporting Business.” mean?", "Who runs Streamline?",
             "What makes Streamline different?", "Do you offer a free initial discussion?", "Are you insured?", "How can I contact Streamline?"]
    allf = dict(C.faqs("home"))
    out += SHARED_RENDERERS["faq"](ctx, {"tone": "pale", "eyebrow": C.STRAP, "title": "General Streamline [[FAQs]]",
                                        "lead": ["Answers to common questions about Streamline Safety & Medical Solutions, our team, services, bookings and how we work."],
                                        "items": [(q, allf[q]) for q in picks], "show": 6})
    out += cta(ctx, {"title": "Have any questions? We’re here to help.", "text": ["Speak to our team and we will be happy to help."],
                     "buttons": [("Book online", "book"), ("Contact Streamline", "contact"), ("Call", "tel")]})
    return out


JS = """<script>
(function () {
  var each = function (list, fn) { Array.prototype.forEach.call(list, fn); };
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (!reduce && 'IntersectionObserver' in window) {
    each(document.querySelectorAll('[data-sms-scrolly]'), function (sec) {
      var items = sec.querySelectorAll('[data-sms-scrolly-item]');
      var marks = sec.querySelectorAll('[data-sms-at]');
      var current = -1;
      var set = function (i) {
        if (i === current || isNaN(i)) return;
        sec.setAttribute('data-dir', i < current ? 'up' : 'down');
        each(marks, function (m) {
          var at = parseInt(m.getAttribute('data-sms-at'), 10);
          var was = m.classList.contains('is-active');
          m.classList.toggle('is-prev', was && at !== i);
          m.classList.toggle('is-active', at === i);
          m.classList.toggle('is-done', at <= i);
        });
        current = i;
      };
      sec.classList.add('is-scrolly');
      set(0);
      var io = new IntersectionObserver(function (entries) {
        each(entries, function (en) {
          if (en.isIntersecting) set(parseInt(en.target.getAttribute('data-i'), 10));
        });
      }, { rootMargin: '-45% 0px -45% 0px', threshold: 0 });
      each(items, function (it) { io.observe(it); });
    });
  }
  each(document.querySelectorAll('[data-sms-index]'), function (root) {
    each(root.querySelectorAll('[data-i]'), function (row) {
      var go = function () { root.setAttribute('data-active', row.getAttribute('data-i')); };
      row.addEventListener('mouseenter', go);
      row.addEventListener('focus', go);
    });
  });
})();
</script>
"""


def scripts(ctx, main):
    return JS if ("data-sms-scrolly" in main or "data-sms-index" in main) else ""
