"""Shared helpers, page shell and section renderers for the Streamline concepts.

Every concept renders the same content (build/content.py). A concept supplies its
own tokens, header/footer styling, page hero, CTA band and homepage, and can
override the look of the shared sections below through its CSS.
"""
import html
import re

SITE = "https://www.streamlinesms.co.uk"
PHONE = "01283 358789"
PHONE_TEL = "01283358789"
EMAIL = "hello@streamlinesms.co.uk"

# slug -> (nav label, short label)
PAGES = [
    ("event-medical-cover", "Event Medical Cover"),
    ("medical-training", "Medical Training"),
    ("risk-needs-consultancy", "Risk & Needs Consultancy"),
    ("pre-hospital-career-support", "Pre-Hospital Career Support"),
    ("recruitment", "Recruitment"),
    ("about", "About Us"),
    ("contact", "Contact Us"),
]
MAIN_NAV = ["event-medical-cover", "medical-training", "risk-needs-consultancy", "about", "contact"]
LABEL = dict(PAGES)
LABEL["home"] = "Home"

NAMED = {
    0x2019: "&rsquo;", 0x2018: "&lsquo;", 0x201C: "&ldquo;", 0x201D: "&rdquo;",
    0x2013: "&ndash;", 0x2014: "&mdash;", 0x2192: "&rarr;", 0x2197: "&nearr;",
    0x00B7: "&middot;", 0x00A0: "&nbsp;", 0x2026: "&hellip;", 0x2191: "&uarr;", 0x2193: "&darr;",
}


def ascii_html(s):
    """Return s with every non-ASCII character written as an HTML entity."""
    out = []
    for ch in s:
        o = ord(ch)
        if o < 128:
            out.append(ch)
        else:
            out.append(NAMED.get(o, "&#%d;" % o))
    return "".join(out)


def e(text):
    """Escape plain text and apply [[highlight]] markup."""
    t = html.escape(text, quote=False)
    return re.sub(r"\[\[(.+?)\]\]", r'<span class="sms-mark">\1</span>', t)


def plain(text):
    return re.sub(r"\[\[(.+?)\]\]", r"\1", text)


def attr(text):
    return html.escape(plain(text), quote=True)


class Ctx:
    def __init__(self, concept, slug):
        self.concept = concept
        self.slug = slug
        self.root = "" if slug == "home" else "../"
        self.placeholders = []
        self.image_text = []

    def href(self, slug):
        if slug == "home":
            return "%sconcept-%d.html" % (self.root, self.concept)
        if self.slug == "home":
            return "concept-%d/%s.html" % (self.concept, slug)
        return "%s.html" % slug

    def asset(self, name):
        return self.root + "assets/" + name

    def ph(self, kind, alt, note, cls, lazy=True, extra=""):
        """Photo placeholder image. kind: portrait | landscape | wide."""
        dims = {"portrait": (800, 1000), "landscape": (1200, 800), "wide": (1600, 640), "hero": (1600, 800)}[kind]
        self.placeholders.append("assets/placeholder-%s.svg - %s" % (kind, note))
        return '<img class="%s" src="%s" alt="%s" width="%d" height="%d"%s%s>' % (
            cls, self.asset("placeholder-%s.svg" % kind), attr(alt), dims[0], dims[1],
            ' loading="lazy"' if lazy else "", extra)


# ---------------------------------------------------------------------------
# Base CSS shared by all concepts (tokens are set per concept on .sms-page)
# ---------------------------------------------------------------------------
BASE_CSS = r"""
.sms-page {
  --sms-navy: #061e35;
  --sms-navy-2: #0b3152;
  --sms-green: #407f36;
  --sms-green-on-navy: #82d06e;
  --sms-pale: #f4f8f3;
  --sms-pale-2: #eef7ec;
  --sms-white: #ffffff;
  --sms-ink-soft: #405365;
  --sms-line: #d9e2e7;
  --sms-line-green: #dde5dc;
  --sms-font: "Montserrat", Arial, sans-serif;
  --sms-step--1: clamp(0.8125rem, 0.79rem + 0.1vw, 0.875rem);
  --sms-step-0: clamp(1rem, 0.96rem + 0.2vw, 1.0625rem);
  --sms-step-1: clamp(1.125rem, 1.06rem + 0.3vw, 1.3125rem);
  --sms-step-2: clamp(1.5rem, 1.25rem + 1.1vw, 2.125rem);
  --sms-step-3: clamp(2rem, 1.4rem + 2.7vw, 3.5rem);
  --sms-gutter: clamp(1rem, 0.6rem + 2vw, 2.5rem);
  --sms-section: clamp(3.5rem, 2.5rem + 4.5vw, 6.5rem);
  --sms-max: 72rem;
  --sms-radius: 0.75rem;
  --sms-radius-sm: 0.5rem;
  margin: 0;
  background: var(--sms-white);
  color: var(--sms-navy);
  font-family: var(--sms-font);
  font-size: var(--sms-step-0);
  line-height: 1.65;
  -webkit-font-smoothing: antialiased;
}
.sms-page *,
.sms-page *::before,
.sms-page *::after { box-sizing: border-box; }
.sms-page a:focus-visible,
.sms-page button:focus-visible,
.sms-page summary:focus-visible,
.sms-page input:focus-visible,
.sms-page select:focus-visible,
.sms-page textarea:focus-visible { outline: 3px solid var(--sms-green); outline-offset: 3px; }
.sms-page .sms-skip { position: absolute; left: -999px; top: 0; z-index: 20; padding: 0.75rem 1rem; background: var(--sms-navy); color: var(--sms-white); }
.sms-page .sms-skip:focus { left: 1rem; top: 1rem; }
.sms-page .sms-visually-hidden { position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0); clip-path: inset(50%); white-space: nowrap; }

/* Global buttons (Elementor: global button styles) */
.sms-page .sms-btn { display: inline-flex; align-items: center; gap: 0.5rem; min-width: 0; padding: 0.9rem 1.35rem; border: 2px solid transparent; border-radius: var(--sms-radius-sm); font-size: var(--sms-step--1); font-weight: 600; line-height: 1.25; text-decoration: none; transition: transform 0.2s ease; }
.sms-page .sms-btn:hover { transform: translateY(-2px); }
.sms-page .sms-btn--primary { border-color: var(--sms-green); background: var(--sms-green); color: var(--sms-white); }
.sms-page .sms-btn--outline { border-color: var(--sms-navy); background: transparent; color: var(--sms-navy); }
.sms-page .sms-btn--outline:hover { background: var(--sms-navy); color: var(--sms-white); }
.sms-page .sms-btn--light { border-color: var(--sms-white); background: var(--sms-white); color: var(--sms-navy); }
.sms-page .sms-arrow { display: inline-block; transition: transform 0.2s ease; }
.sms-page a:hover .sms-arrow { transform: translateX(4px); }

/* Shared inner widths */
.sms-header .sms-header__inner,
.sms-topbar .sms-topbar__inner,
.sms-intro .sms-intro__inner,
.sms-cards .sms-cards__inner,
.sms-steps .sms-steps__inner,
.sms-checklist .sms-checklist__inner,
.sms-notice .sms-notice__inner,
.sms-faq .sms-faq__inner,
.sms-quotes .sms-quotes__inner,
.sms-people .sms-people__inner,
.sms-contact .sms-contact__inner,
.sms-links .sms-links__inner,
.sms-claim .sms-claim__inner,
.sms-cta .sms-cta__inner,
.sms-footer .sms-footer__inner {
  width: 100%;
  max-width: var(--sms-max);
  margin: 0 auto;
  padding-left: var(--sms-gutter);
  padding-right: var(--sms-gutter);
}

/* ---------- Top bar ---------- */
.sms-topbar { background: var(--sms-green); color: var(--sms-white); font-size: var(--sms-step--1); }
.sms-topbar .sms-topbar__inner { display: flex; flex-wrap: wrap; justify-content: space-between; gap: 0.25rem 1.5rem; padding-top: 0.5rem; padding-bottom: 0.5rem; }
.sms-topbar .sms-topbar__text { display: none; min-width: 0; font-weight: 600; }
.sms-topbar .sms-topbar__links { display: flex; flex-wrap: wrap; gap: 0.25rem 1.5rem; min-width: 0; }
.sms-topbar .sms-topbar__link { min-width: 0; color: var(--sms-white); font-weight: 600; text-decoration: none; overflow-wrap: anywhere; }
.sms-topbar .sms-topbar__link:hover { text-decoration: underline; }
@media (min-width: 48em) {
  .sms-topbar .sms-topbar__text { display: block; }
}

/* ---------- Header ---------- */
.sms-header { position: relative; z-index: 5; border-bottom: 1px solid var(--sms-line); background: var(--sms-white); }
.sms-header .sms-header__inner { display: flex; align-items: center; justify-content: space-between; gap: 1.5rem; min-height: 4.75rem; }
.sms-header .sms-header__logo { display: block; flex: 0 0 auto; min-width: 0; line-height: 0; }
.sms-header .sms-header__logo-img { display: block; width: clamp(10.5rem, 8rem + 8vw, 13.5rem); height: auto; }
.sms-header .sms-header__nav { display: none; min-width: 0; }
.sms-header .sms-header__list { display: flex; align-items: center; gap: clamp(0.9rem, 0.2rem + 1.1vw, 1.75rem); min-width: 0; margin: 0; padding: 0; list-style: none; }
.sms-header .sms-header__item { min-width: 0; }
.sms-header .sms-header__link { display: block; padding: 0.4rem 0; border-bottom: 2px solid transparent; color: var(--sms-navy); font-size: var(--sms-step--1); font-weight: 500; text-decoration: none; white-space: nowrap; }
.sms-header .sms-header__link:hover { border-bottom-color: var(--sms-green); }
.sms-header .sms-header__link[aria-current="page"] { border-bottom-color: var(--sms-green); font-weight: 700; }
.sms-header .sms-header__cta { flex: 0 0 auto; min-width: 0; }
.sms-header .sms-header__menu { position: relative; min-width: 0; }
.sms-header .sms-header__summary { display: flex; align-items: center; gap: 0.5rem; padding: 0.6rem 0.9rem; border: 1px solid var(--sms-line); border-radius: var(--sms-radius-sm); background: var(--sms-white); color: var(--sms-navy); cursor: pointer; font-size: var(--sms-step--1); font-weight: 600; list-style: none; }
.sms-header .sms-header__summary::-webkit-details-marker { display: none; }
.sms-header .sms-header__bars { display: block; min-width: 0; width: 1.1rem; height: 2px; background: currentColor; box-shadow: 0 -5px 0 currentColor, 0 5px 0 currentColor; }
.sms-header .sms-header__panel { position: absolute; right: 0; top: calc(100% + 0.5rem); z-index: 10; width: min(19rem, calc(100vw - 2rem)); padding: 0.5rem; border: 1px solid var(--sms-line); border-radius: var(--sms-radius-sm); background: var(--sms-white); box-shadow: 0 12px 30px rgba(6, 30, 53, 0.14); }
.sms-header .sms-header__panel-list { margin: 0; padding: 0; list-style: none; }
.sms-header .sms-header__panel-item { min-width: 0; }
.sms-header .sms-header__panel-link { display: block; padding: 0.7rem 0.8rem; border-radius: 0.35rem; color: var(--sms-navy); font-weight: 500; text-decoration: none; }
.sms-header .sms-header__panel-link:hover { background: var(--sms-pale); }
.sms-header .sms-header__panel-link[aria-current="page"] { background: var(--sms-pale); font-weight: 700; }
.sms-header .sms-header__panel-sep { height: 1px; margin: 0.4rem 0.8rem; background: var(--sms-line); }
@media (min-width: 70em) {
  .sms-header .sms-header__nav { display: flex; align-items: center; gap: 1.75rem; }
  .sms-header .sms-header__menu { display: none; }
}

/* ---------- Section heads (shared pattern) ---------- */
.sms-intro .sms-intro__eyebrow,
.sms-cards .sms-cards__eyebrow,
.sms-steps .sms-steps__eyebrow,
.sms-checklist .sms-checklist__eyebrow,
.sms-faq .sms-faq__eyebrow,
.sms-quotes .sms-quotes__eyebrow,
.sms-people .sms-people__eyebrow,
.sms-contact .sms-contact__eyebrow,
.sms-links .sms-links__eyebrow {
  margin-bottom: 0.85rem;
  color: var(--sms-green);
  font-size: var(--sms-step--1);
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
}
.sms-intro .sms-intro__title,
.sms-cards .sms-cards__title,
.sms-steps .sms-steps__title,
.sms-checklist .sms-checklist__title,
.sms-faq .sms-faq__title,
.sms-quotes .sms-quotes__title,
.sms-people .sms-people__title,
.sms-contact .sms-contact__title,
.sms-links .sms-links__title {
  margin: 0 0 1rem;
  font-size: var(--sms-step-2);
  font-weight: 700;
  line-height: 1.2;
  letter-spacing: -0.01em;
}
.sms-cards .sms-cards__head,
.sms-steps .sms-steps__head,
.sms-checklist .sms-checklist__head,
.sms-people .sms-people__head,
.sms-links .sms-links__head,
.sms-quotes .sms-quotes__head { max-width: 46rem; margin-bottom: clamp(2rem, 1.5rem + 2vw, 3rem); }
.sms-cards .sms-cards__lead,
.sms-steps .sms-steps__lead,
.sms-checklist .sms-checklist__lead,
.sms-people .sms-people__lead,
.sms-links .sms-links__lead,
.sms-faq .sms-faq__lead { color: var(--sms-ink-soft); }
.sms-cards .sms-cards__lead p,
.sms-steps .sms-steps__lead p,
.sms-checklist .sms-checklist__lead p,
.sms-people .sms-people__lead p,
.sms-links .sms-links__lead p,
.sms-faq .sms-faq__lead p { margin: 0 0 0.75rem; }

/* Tone: alternating light bands */
.sms-intro,
.sms-cards,
.sms-steps,
.sms-checklist,
.sms-notice,
.sms-faq,
.sms-quotes,
.sms-people,
.sms-contact,
.sms-links,
.sms-claim { position: relative; padding: var(--sms-section) 0; overflow: hidden; }
.sms-intro.sms-tone-pale,
.sms-cards.sms-tone-pale,
.sms-steps.sms-tone-pale,
.sms-checklist.sms-tone-pale,
.sms-notice.sms-tone-pale,
.sms-faq.sms-tone-pale,
.sms-quotes.sms-tone-pale,
.sms-people.sms-tone-pale,
.sms-contact.sms-tone-pale,
.sms-links.sms-tone-pale,
.sms-claim.sms-tone-pale { background: var(--sms-pale); }

/* Brand watermark: the shield from the logo */
.sms-intro .sms-watermark,
.sms-cards .sms-watermark,
.sms-steps .sms-watermark,
.sms-quotes .sms-watermark,
.sms-people .sms-watermark,
.sms-claim .sms-watermark,
.sms-checklist .sms-watermark { position: absolute; right: -4rem; bottom: -5rem; width: clamp(14rem, 10rem + 18vw, 26rem); height: auto; opacity: 0.07; pointer-events: none; }

/* ---------- Intro (prose + aside) ---------- */
.sms-intro .sms-intro__inner { position: relative; display: grid; gap: clamp(2rem, 1.5rem + 3vw, 4.5rem); }
.sms-intro .sms-intro__main { min-width: 0; }
.sms-intro .sms-intro__body { max-width: 40rem; color: var(--sms-ink-soft); }
.sms-intro .sms-intro__body p { margin: 0 0 1rem; }
.sms-intro .sms-intro__strap { margin-top: 1.5rem; font-size: var(--sms-step-1); font-weight: 700; color: var(--sms-navy); }
.sms-intro .sms-intro__aside { align-self: start; min-width: 0; padding: clamp(1.5rem, 1.1rem + 1.5vw, 2.25rem); border-radius: var(--sms-radius); background: var(--sms-pale); }
.sms-intro.sms-tone-pale .sms-intro__aside { background: var(--sms-white); }
.sms-intro .sms-intro__aside-title { margin: 0 0 1rem; font-size: var(--sms-step-0); font-weight: 700; }
.sms-intro .sms-intro__list { margin: 0; padding: 0; list-style: none; font-size: var(--sms-step--1); }
.sms-intro .sms-intro__list-item { position: relative; min-width: 0; padding: 0.6rem 0 0.6rem 1.6rem; border-top: 1px solid var(--sms-line); }
.sms-intro .sms-intro__list-item::before { content: ""; position: absolute; left: 0.15rem; top: 1rem; width: 0.6rem; height: 0.32rem; border-left: 2px solid var(--sms-green); border-bottom: 2px solid var(--sms-green); transform: rotate(-45deg); }
.sms-intro .sms-intro__aside-note { margin-top: 1rem; color: var(--sms-ink-soft); font-size: var(--sms-step--1); }
.sms-intro .sms-intro__aside-note p { margin: 0; }
@media (min-width: 56em) {
  .sms-intro .sms-intro__inner { grid-template-columns: minmax(0, 1.3fr) minmax(0, 0.9fr); }
}

/* ---------- Cards ---------- */
.sms-cards .sms-cards__inner { position: relative; }
.sms-cards .sms-cards__grid { display: grid; gap: clamp(1rem, 0.6rem + 1.5vw, 1.75rem); margin: 0; padding: 0; list-style: none; }
.sms-cards .sms-cards__item { display: flex; flex-direction: column; min-width: 0; padding: clamp(1.5rem, 1.1rem + 1.5vw, 2.25rem); border: 1px solid var(--sms-line); border-radius: var(--sms-radius); background: var(--sms-white); }
.sms-cards .sms-cards__num { margin-bottom: 0.75rem; color: var(--sms-green); font-size: var(--sms-step--1); font-weight: 700; letter-spacing: 0.1em; }
.sms-cards .sms-cards__name { margin: 0 0 0.6rem; font-size: var(--sms-step-1); font-weight: 700; line-height: 1.3; }
.sms-cards .sms-cards__meta { margin-bottom: 0.6rem; color: var(--sms-green); font-size: var(--sms-step--1); font-weight: 600; }
.sms-cards .sms-cards__text { color: var(--sms-ink-soft); }
.sms-cards .sms-cards__text p { margin: 0 0 0.75rem; }
.sms-cards .sms-cards__list-title { margin: 0.75rem 0 0.5rem; font-size: var(--sms-step--1); font-weight: 700; letter-spacing: 0.08em; text-transform: uppercase; }
.sms-cards .sms-cards__list { margin: 0; padding: 0; list-style: none; font-size: var(--sms-step--1); }
.sms-cards .sms-cards__list-item { position: relative; min-width: 0; padding: 0.45rem 0 0.45rem 1.25rem; border-top: 1px solid var(--sms-line); }
.sms-cards .sms-cards__list-item::before { content: ""; position: absolute; left: 0; top: 1rem; width: 0.4rem; height: 0.4rem; border-radius: 50%; background: var(--sms-green); }
.sms-cards .sms-cards__link { align-self: flex-start; margin-top: auto; padding-top: 1rem; color: var(--sms-green); font-weight: 700; text-decoration: none; }
.sms-cards .sms-cards__link:hover { text-decoration: underline; }
@media (min-width: 46em) {
  .sms-cards .sms-cards__grid--2,
  .sms-cards .sms-cards__grid--3,
  .sms-cards .sms-cards__grid--4 { grid-template-columns: repeat(2, minmax(0, 1fr)); }
}
@media (min-width: 64em) {
  .sms-cards .sms-cards__grid--3 { grid-template-columns: repeat(3, minmax(0, 1fr)); }
  .sms-cards .sms-cards__grid--4 { grid-template-columns: repeat(4, minmax(0, 1fr)); }
}

/* ---------- Steps ---------- */
.sms-steps .sms-steps__inner { position: relative; }
.sms-steps .sms-steps__list { display: grid; gap: 1rem; margin: 0; padding: 0; list-style: none; counter-reset: sms-step; }
.sms-steps .sms-steps__item { position: relative; min-width: 0; padding: 1.5rem 1.5rem 1.5rem 4.5rem; border-radius: var(--sms-radius); background: var(--sms-white); border: 1px solid var(--sms-line); }
.sms-steps .sms-steps__item::before { counter-increment: sms-step; content: counter(sms-step); position: absolute; left: 1.25rem; top: 1.35rem; display: grid; place-items: center; width: 2.25rem; height: 2.25rem; border-radius: 50%; background: var(--sms-green); color: var(--sms-white); font-weight: 700; }
.sms-steps .sms-steps__name { margin: 0 0 0.35rem; font-size: var(--sms-step-0); font-weight: 700; line-height: 1.35; }
.sms-steps .sms-steps__text { color: var(--sms-ink-soft); font-size: var(--sms-step--1); }
.sms-steps .sms-steps__text p { margin: 0 0 0.5rem; }
.sms-steps .sms-steps__note { max-width: 46rem; margin-top: 1.75rem; color: var(--sms-ink-soft); font-size: var(--sms-step--1); }
.sms-steps .sms-steps__note p { margin: 0; }
@media (min-width: 52em) {
  .sms-steps .sms-steps__list--row { grid-template-columns: repeat(auto-fit, minmax(13rem, 1fr)); }
  .sms-steps .sms-steps__list--row .sms-steps__item { padding: 4.25rem 1.5rem 1.5rem; }
  .sms-steps .sms-steps__list--row .sms-steps__item::before { left: 1.5rem; top: 1.5rem; }
}

/* ---------- Checklist (pills) ---------- */
.sms-checklist .sms-checklist__inner { position: relative; }
.sms-checklist .sms-checklist__list { display: flex; flex-wrap: wrap; gap: 0.6rem; margin: 0; padding: 0; list-style: none; }
.sms-checklist .sms-checklist__item { min-width: 0; padding: 0.55rem 1rem; border: 1px solid var(--sms-line-green); border-radius: 999px; background: var(--sms-white); font-size: var(--sms-step--1); font-weight: 600; }

/* ---------- Notice ---------- */
.sms-notice .sms-notice__box { display: grid; gap: 1rem; padding: clamp(1.5rem, 1rem + 2vw, 2.75rem); border: 2px dashed var(--sms-line-green); border-radius: var(--sms-radius); background: var(--sms-white); }
.sms-notice .sms-notice__label { color: var(--sms-green); font-size: var(--sms-step--1); font-weight: 700; letter-spacing: 0.12em; text-transform: uppercase; }
.sms-notice .sms-notice__title { margin: 0; font-size: var(--sms-step-1); font-weight: 700; }
.sms-notice .sms-notice__text { max-width: 46rem; color: var(--sms-ink-soft); }
.sms-notice .sms-notice__text p { margin: 0 0 0.6rem; }
.sms-notice .sms-notice__actions { display: flex; flex-wrap: wrap; gap: 0.75rem; }

/* ---------- FAQ ---------- */
.sms-faq .sms-faq__inner { display: grid; gap: clamp(2rem, 1.5rem + 2vw, 4rem); }
.sms-faq .sms-faq__head { min-width: 0; }
.sms-faq .sms-faq__list { min-width: 0; border-top: 1px solid var(--sms-line); }
.sms-faq .sms-faq__item { border-bottom: 1px solid var(--sms-line); }
.sms-faq .sms-faq__q { position: relative; padding: 1.15rem 2.75rem 1.15rem 0; cursor: pointer; font-weight: 600; line-height: 1.4; list-style: none; }
.sms-faq .sms-faq__q::-webkit-details-marker { display: none; }
.sms-faq .sms-faq__q::after { content: "+"; position: absolute; right: 0.25rem; top: 0.95rem; display: grid; place-items: center; width: 1.75rem; height: 1.75rem; border-radius: 50%; background: var(--sms-pale-2); color: var(--sms-green); font-size: 1.25rem; font-weight: 500; line-height: 1; transition: transform 0.2s ease; }
.sms-faq .sms-faq__item[open] .sms-faq__q::after { transform: rotate(45deg); }
.sms-faq .sms-faq__q:hover { color: var(--sms-green); }
.sms-faq .sms-faq__a { padding: 0 0 1.4rem; color: var(--sms-ink-soft); }
.sms-faq .sms-faq__a p { margin: 0 0 0.6rem; }
.sms-faq .sms-faq__a ul { margin: 0 0 0.6rem; padding-left: 1.25rem; }
.sms-faq .sms-faq__a li { margin-bottom: 0.25rem; }
.sms-faq .sms-faq__a a { color: var(--sms-green); font-weight: 600; }
.sms-faq .sms-faq__more { margin-top: 1.5rem; }
@media (min-width: 56em) {
  .sms-faq .sms-faq__inner { grid-template-columns: minmax(0, 0.8fr) minmax(0, 1.4fr); }
  .sms-faq .sms-faq__head { position: sticky; top: 1.5rem; align-self: start; }
}

/* ---------- Quotes (mission / vision) ---------- */
.sms-quotes .sms-quotes__inner { position: relative; }
.sms-quotes .sms-quotes__grid { display: grid; gap: clamp(1rem, 0.6rem + 1.5vw, 1.75rem); }
.sms-quotes .sms-quotes__item { min-width: 0; margin: 0; padding: clamp(1.5rem, 1rem + 2vw, 2.5rem); border-left: 4px solid var(--sms-green); border-radius: var(--sms-radius); background: var(--sms-white); }
.sms-quotes .sms-quotes__label { margin-bottom: 0.75rem; color: var(--sms-green); font-size: var(--sms-step--1); font-weight: 700; letter-spacing: 0.12em; text-transform: uppercase; }
.sms-quotes .sms-quotes__text { margin: 0; font-size: var(--sms-step-1); font-weight: 500; line-height: 1.55; }
.sms-quotes .sms-quotes__text p { margin: 0; }
.sms-quotes .sms-quotes__cite { display: block; margin-top: 1rem; color: var(--sms-ink-soft); font-size: var(--sms-step--1); font-style: normal; }
@media (min-width: 52em) {
  .sms-quotes .sms-quotes__grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
}

/* ---------- People (directors) ---------- */
.sms-people .sms-people__inner { position: relative; }
.sms-people .sms-people__grid { display: grid; gap: clamp(2rem, 1.5rem + 2vw, 3rem); margin: 0; padding: 0; list-style: none; }
.sms-people .sms-people__person { display: grid; gap: 1.25rem; align-content: start; min-width: 0; }
.sms-people .sms-people__media { min-width: 0; max-width: 18rem; margin: 0; }
.sms-people .sms-people__img { display: block; width: 100%; height: auto; border-radius: var(--sms-radius); }
.sms-people .sms-people__info { min-width: 0; }
.sms-people .sms-people__role { margin-bottom: 0.25rem; color: var(--sms-green); font-size: var(--sms-step--1); font-weight: 700; letter-spacing: 0.12em; text-transform: uppercase; }
.sms-people .sms-people__name { margin: 0 0 0.35rem; font-size: var(--sms-step-1); font-weight: 700; line-height: 1.3; }
.sms-people .sms-people__tags { margin-bottom: 1rem; color: var(--sms-ink-soft); font-size: var(--sms-step--1); font-weight: 600; }
.sms-people .sms-people__bio { color: var(--sms-ink-soft); }
.sms-people .sms-people__bio p { margin: 0 0 0.85rem; }
.sms-people .sms-people__shared { max-width: 48rem; margin-top: clamp(2.5rem, 2rem + 2vw, 4rem); padding: clamp(1.5rem, 1rem + 2vw, 2.5rem); border-radius: var(--sms-radius); background: var(--sms-white); }
.sms-people.sms-tone-white .sms-people__shared { background: var(--sms-pale); }
.sms-people .sms-people__shared-label { margin-bottom: 0.5rem; color: var(--sms-green); font-size: var(--sms-step--1); font-weight: 700; letter-spacing: 0.12em; text-transform: uppercase; }
.sms-people .sms-people__shared-title { margin: 0 0 0.75rem; font-size: var(--sms-step-1); font-weight: 700; }
.sms-people .sms-people__shared-text { color: var(--sms-ink-soft); }
.sms-people .sms-people__shared-text p { margin: 0 0 0.75rem; }
@media (min-width: 52em) {
  .sms-people .sms-people__grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
}

/* ---------- Links (shortcut cards) ---------- */
.sms-links .sms-links__grid { display: grid; gap: 1rem; margin: 0; padding: 0; list-style: none; }
.sms-links .sms-links__item { min-width: 0; }
.sms-links .sms-links__link { display: flex; flex-direction: column; gap: 0.5rem; height: 100%; padding: 1.5rem; border: 1px solid var(--sms-line); border-radius: var(--sms-radius); background: var(--sms-white); color: var(--sms-navy); text-decoration: none; }
.sms-links .sms-links__link:hover { border-color: var(--sms-green); }
.sms-links .sms-links__name { min-width: 0; font-size: var(--sms-step-1); font-weight: 700; }
.sms-links .sms-links__text { min-width: 0; color: var(--sms-ink-soft); font-size: var(--sms-step--1); }
.sms-links .sms-links__go { min-width: 0; margin-top: auto; color: var(--sms-green); font-size: var(--sms-step--1); font-weight: 700; }
@media (min-width: 46em) {
  .sms-links .sms-links__grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
}
@media (min-width: 64em) {
  .sms-links .sms-links__grid { grid-template-columns: repeat(4, minmax(0, 1fr)); }
}

/* ---------- Claim (statement) ---------- */
.sms-claim .sms-claim__inner { position: relative; }
.sms-claim .sms-claim__text { max-width: 50rem; margin: 0 auto; font-size: var(--sms-step-2); font-weight: 700; line-height: 1.35; text-align: center; }
.sms-claim .sms-claim__text p { margin: 0; }

/* ---------- Contact (details + form) ---------- */
.sms-contact .sms-contact__inner { display: grid; gap: clamp(2rem, 1.5rem + 3vw, 4rem); }
.sms-contact .sms-contact__info { min-width: 0; }
.sms-contact .sms-contact__lead { margin-bottom: 1rem; font-size: var(--sms-step-1); font-weight: 600; }
.sms-contact .sms-contact__text { color: var(--sms-ink-soft); }
.sms-contact .sms-contact__text p { margin: 0 0 1rem; }
.sms-contact .sms-contact__details { display: grid; gap: 1rem; margin: 1.5rem 0 0; padding: 0; list-style: none; }
.sms-contact .sms-contact__detail { min-width: 0; padding: 1.25rem 1.5rem; border-radius: var(--sms-radius); background: var(--sms-pale); }
.sms-contact.sms-tone-pale .sms-contact__detail { background: var(--sms-white); }
.sms-contact .sms-contact__label { margin-bottom: 0.25rem; color: var(--sms-ink-soft); font-size: var(--sms-step--1); font-weight: 700; letter-spacing: 0.12em; text-transform: uppercase; }
.sms-contact .sms-contact__value { color: var(--sms-navy); font-size: var(--sms-step-1); font-weight: 700; text-decoration: none; overflow-wrap: anywhere; }
.sms-contact .sms-contact__value:hover { color: var(--sms-green); }
.sms-contact .sms-contact__small { color: var(--sms-ink-soft); font-size: var(--sms-step--1); }
.sms-contact .sms-contact__small p { margin: 0 0 0.5rem; }
.sms-contact .sms-contact__form { display: grid; gap: 1.1rem; align-content: start; min-width: 0; padding: clamp(1.5rem, 1rem + 2vw, 2.5rem); border: 1px solid var(--sms-line); border-radius: var(--sms-radius); background: var(--sms-white); }
.sms-contact .sms-contact__form-title { margin: 0; font-size: var(--sms-step-1); font-weight: 700; }
.sms-contact .sms-contact__field { display: grid; gap: 0.35rem; min-width: 0; }
.sms-contact .sms-contact__field-label { font-size: var(--sms-step--1); font-weight: 600; }
.sms-contact .sms-contact__input { width: 100%; min-width: 0; padding: 0.8rem 0.9rem; border: 1px solid #8a99a6; border-radius: var(--sms-radius-sm); background: var(--sms-white); color: var(--sms-navy); font: inherit; }
.sms-contact .sms-contact__input--area { min-height: 8rem; resize: vertical; }
.sms-contact .sms-contact__row { display: grid; gap: 1.1rem; }
.sms-contact .sms-contact__note { padding: 0.75rem 1rem; border-radius: var(--sms-radius-sm); background: var(--sms-pale-2); color: var(--sms-navy); font-size: var(--sms-step--1); }
.sms-contact .sms-contact__note p { margin: 0; }
.sms-contact .sms-contact__submit { justify-self: start; cursor: pointer; font: inherit; font-size: var(--sms-step--1); font-weight: 600; }
.sms-contact .sms-contact__status { color: var(--sms-green); font-weight: 600; }
@media (min-width: 40em) {
  .sms-contact .sms-contact__row { grid-template-columns: repeat(2, minmax(0, 1fr)); }
}
@media (min-width: 60em) {
  .sms-contact .sms-contact__inner { grid-template-columns: minmax(0, 0.9fr) minmax(0, 1.1fr); }
}

/* ---------- Flex and grid children: allow shrinking ---------- */
.sms-cards .sms-cards__list-title,
.sms-cards .sms-cards__list,
.sms-cards .sms-cards__meta,
.sms-cards .sms-cards__name,
.sms-cards .sms-cards__num,
.sms-cards .sms-cards__text,
.sms-contact .sms-contact__field-label,
.sms-contact .sms-contact__form-title,
.sms-contact .sms-contact__note,
.sms-contact .sms-contact__row,
.sms-contact .sms-contact__status,
.sms-notice .sms-notice__actions,
.sms-notice .sms-notice__label,
.sms-notice .sms-notice__text,
.sms-notice .sms-notice__title,
.sms-phero .sms-phero__inner,
.sms-phero .sms-phero__badge-img,
.sms-hsvc .sms-hsvc__name,
.sms-hsvc .sms-hsvc__points,
.sms-hsvc .sms-hsvc__text { min-width: 0; }

/* ---------- Footer (structure; colours per concept) ---------- */
.sms-footer { padding: clamp(3rem, 2rem + 3vw, 4.5rem) 0 2.5rem; font-size: var(--sms-step--1); }
.sms-footer .sms-footer__inner { display: grid; gap: 2.5rem; }
.sms-footer .sms-footer__brand { min-width: 0; }
.sms-footer .sms-footer__logo { display: block; width: clamp(10.5rem, 8rem + 8vw, 13rem); height: auto; margin-bottom: 1.25rem; }
.sms-footer .sms-footer__tag { margin-bottom: 1.25rem; font-weight: 600; }
.sms-footer .sms-footer__badges { display: flex; flex-wrap: wrap; align-items: center; gap: 1rem; }
.sms-footer .sms-footer__badge-link { display: inline-block; min-width: 0; line-height: 0; }
.sms-footer .sms-footer__badge { display: block; min-width: 0; height: auto; border-radius: 0.25rem; background: var(--sms-white); }
.sms-footer .sms-footer__badge--qualsafe { width: 4.5rem; padding: 0.3rem; }
.sms-footer .sms-footer__badge--ate { width: 8rem; }
.sms-footer .sms-footer__col { min-width: 0; }
.sms-footer .sms-footer__heading { margin: 0 0 1rem; font-size: var(--sms-step--1); font-weight: 700; letter-spacing: 0.12em; text-transform: uppercase; }
.sms-footer .sms-footer__list { margin: 0; padding: 0; list-style: none; }
.sms-footer .sms-footer__list-item { margin-bottom: 0.45rem; }
.sms-footer .sms-footer__link { text-decoration: none; }
.sms-footer .sms-footer__link:hover { text-decoration: underline; }
.sms-footer .sms-footer__company { line-height: 1.7; }
.sms-footer .sms-footer__company p { margin: 0; }
.sms-footer .sms-footer__base { grid-column: 1 / -1; min-width: 0; padding-top: 1.5rem; border-top: 1px solid; }
.sms-footer .sms-footer__base p { margin: 0; }
@media (min-width: 46em) {
  .sms-footer .sms-footer__inner { grid-template-columns: repeat(2, minmax(0, 1fr)); }
}
@media (min-width: 64em) {
  .sms-footer .sms-footer__inner { grid-template-columns: minmax(0, 1.3fr) repeat(3, minmax(0, 1fr)); }
}
"""

REVEAL_SELECTORS = [
    ".sms-intro .sms-intro__main", ".sms-intro .sms-intro__aside",
    ".sms-cards .sms-cards__item", ".sms-steps .sms-steps__item",
    ".sms-checklist .sms-checklist__list", ".sms-notice .sms-notice__box",
    ".sms-faq .sms-faq__item", ".sms-quotes .sms-quotes__item",
    ".sms-people .sms-people__person", ".sms-people .sms-people__shared",
    ".sms-links .sms-links__item", ".sms-claim .sms-claim__text",
    ".sms-contact .sms-contact__info", ".sms-contact .sms-contact__form",
    ".sms-footer .sms-footer__inner",
]
TRANSITION_SELECTORS = [
    ".sms-page .sms-btn", ".sms-page .sms-arrow", ".sms-faq .sms-faq__q::after",
]


def motion_css(reveal_extra, rise_selectors, transition_extra):
    rev = REVEAL_SELECTORS + reveal_extra
    css = "\n/* ---------- Scroll reveal (progressive) ---------- */\n"
    css += "@supports (animation-timeline: view()) {\n"
    css += "  @keyframes sms-reveal {\n    from { opacity: 0; transform: translateY(24px); }\n    to { opacity: 1; transform: none; }\n  }\n"
    css += "  " + ",\n  ".join(rev) + " {\n"
    css += "    animation: sms-reveal linear both;\n    animation-timeline: view();\n    animation-range: entry 0% entry 80%;\n  }\n}\n"
    css += "\n/* ---------- Hero entrance (transform only: LCP) ---------- */\n"
    css += "@keyframes sms-rise { from { transform: translateY(14px); } to { transform: none; } }\n"
    css += ",\n".join(rise_selectors) + " { animation: sms-rise 0.7s cubic-bezier(0.2, 0.7, 0.2, 1) both; }\n"
    css += "\n/* ---------- Reduced motion ---------- */\n@media (prefers-reduced-motion: reduce) {\n"
    css += "  " + ",\n  ".join(rev + rise_selectors) + " {\n    animation: none;\n    animation-timeline: none;\n  }\n"
    css += "  " + ",\n  ".join(TRANSITION_SELECTORS + transition_extra) + " { transition: none; }\n}\n"
    return css


# ---------------------------------------------------------------------------
# Shared markup pieces
# ---------------------------------------------------------------------------

def head(ctx, title, description, css):
    return """<!doctype html>
%s
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>%s</title>
<meta name="description" content="%s">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700&amp;display=swap">
<style>%s</style>
</head>
""" % ("%%COMMENT%%", html.escape(title, quote=False), attr(description), css)


def topbar(ctx, text):
    return """<div class="sms-topbar">
  <div class="sms-topbar__inner">
    <div class="sms-topbar__text">%s</div>
    <div class="sms-topbar__links">
      <a class="sms-topbar__link" href="tel:%s">%s</a>
      <a class="sms-topbar__link" href="mailto:%s">%s</a>
    </div>
  </div>
</div>
""" % (e(text), PHONE_TEL, PHONE, EMAIL, EMAIL)


def header(ctx, logo="blue", cta=None):
    cur = lambda s: ' aria-current="page"' if s == ctx.slug else ""
    items = "".join('<li class="sms-header__item"><a class="sms-header__link" href="%s"%s>%s</a></li>' % (ctx.href(s), cur(s), e(LABEL[s])) for s in MAIN_NAV)
    panel = '<li class="sms-header__panel-item"><a class="sms-header__panel-link" href="%s"%s>Home</a></li>' % (ctx.href("home"), cur("home"))
    panel += "".join('<li class="sms-header__panel-item"><a class="sms-header__panel-link" href="%s"%s>%s</a></li>' % (ctx.href(s), cur(s), e(LABEL[s])) for s, _ in PAGES)
    panel += '<li class="sms-header__panel-item" aria-hidden="true"><div class="sms-header__panel-sep"></div></li>'
    panel += '<li class="sms-header__panel-item"><a class="sms-header__panel-link" href="tel:%s">Call %s</a></li>' % (PHONE_TEL, PHONE)
    if cta is None:
        cta = '<a class="sms-btn sms-btn--primary sms-header__cta" href="tel:%s">%s</a>' % (PHONE_TEL, PHONE)
    return """<header class="sms-header">
  <div class="sms-header__inner">
    <a class="sms-header__logo" href="%s" aria-label="Streamline Safety &amp; Medical Solutions home">
      <img class="sms-header__logo-img" src="%s" alt="Streamline Safety &amp; Medical Solutions" width="2500" height="443">
    </a>
    <nav class="sms-header__nav" aria-label="Main">
      <ul class="sms-header__list">%s</ul>
      %s
    </nav>
    <details class="sms-header__menu">
      <summary class="sms-header__summary"><span class="sms-header__bars" aria-hidden="true"></span>Menu</summary>
      <nav class="sms-header__panel" aria-label="Mobile">
        <ul class="sms-header__panel-list">%s</ul>
      </nav>
    </details>
  </div>
</header>
""" % (ctx.href("home"), ctx.asset("streamline-s-m-sol-logo-%s-long.png" % logo), items, cta, panel)


def footer(ctx, logo="white"):
    svc = "".join('<li class="sms-footer__list-item"><a class="sms-footer__link" href="%s">%s</a></li>' % (ctx.href(s), e(LABEL[s])) for s in ["event-medical-cover", "medical-training", "risk-needs-consultancy", "pre-hospital-career-support"])
    more = "".join('<li class="sms-footer__list-item"><a class="sms-footer__link" href="%s">%s</a></li>' % (ctx.href(s), e(LABEL[s])) for s in ["home", "about", "recruitment", "contact"])
    more += '<li class="sms-footer__list-item"><a class="sms-footer__link" href="%s/privacy-policy">Our Privacy Policy</a></li>' % SITE
    more += '<li class="sms-footer__list-item"><a class="sms-footer__link" href="%s/staff-portal">Staff Portal</a></li>' % SITE
    return """<footer class="sms-footer">
  <div class="sms-footer__inner">
    <div class="sms-footer__brand">
      <img class="sms-footer__logo" src="%s" alt="Streamline Safety &amp; Medical Solutions" width="2500" height="443" loading="lazy">
      <div class="sms-footer__tag">Protecting People. Supporting Business.</div>
      <div class="sms-footer__badges">
        <img class="sms-footer__badge sms-footer__badge--qualsafe" src="%s" alt="Qualsafe registered centre" width="1000" height="982" loading="lazy">
        <a class="sms-footer__badge-link" href="https://www.addtoevent.co.uk/suppliers/streamline-safety-medical-solutions"><img class="sms-footer__badge sms-footer__badge--ate" src="%s" alt="Add To Event Featured Supplier" width="188" height="53" loading="lazy"></a>
      </div>
    </div>
    <div class="sms-footer__col">
      <h2 class="sms-footer__heading">Our Services</h2>
      <ul class="sms-footer__list">%s</ul>
    </div>
    <div class="sms-footer__col">
      <h2 class="sms-footer__heading">Explore Our Site</h2>
      <ul class="sms-footer__list">%s</ul>
    </div>
    <div class="sms-footer__col">
      <h2 class="sms-footer__heading">Contact</h2>
      <div class="sms-footer__company">
        <p><a class="sms-footer__link" href="tel:%s">%s</a></p>
        <p><a class="sms-footer__link" href="mailto:%s">%s</a></p>
        <p>&nbsp;</p>
        <p>Streamline Safety &amp; Medical Solutions Ltd</p>
        <p>Registered in England &amp; Wales</p>
        <p>Company No. 17203554</p>
        <p>Registered Office: 8 Cobblestone Drive, Swadlincote, Derbyshire, DE11 0FL</p>
      </div>
    </div>
    <div class="sms-footer__base"><p>Pitch concept by CADS. Not the live Streamline website.</p></div>
  </div>
</footer>
""" % (ctx.asset("streamline-s-m-sol-logo-%s-long.png" % logo), ctx.asset("whatsapp-image-2026-07-20-at-12.27.35.jpeg"),
       ctx.asset("featured-landscape-purple-medium.png"), svc, more, PHONE_TEL, PHONE, EMAIL, EMAIL)


def watermark(ctx, color="blue"):
    return '<img class="sms-watermark" src="%s" alt="" width="378" height="399" loading="lazy" aria-hidden="true">' % ctx.asset("streamline-shield-%s.png" % color)


def paras(lst):
    return "".join("<p>%s</p>" % e(p) for p in lst)


def link(ctx, target):
    """target: page slug, 'tel', 'mail' or absolute URL."""
    if target == "tel":
        return "tel:" + PHONE_TEL
    if target == "mail":
        return "mailto:" + EMAIL
    if target.startswith("http") or target.startswith("#"):
        return target
    return ctx.href(target)


def buttons(ctx, btns, extra_cls=""):
    out = []
    for i, (label, target) in enumerate(btns):
        style = "primary" if i == 0 else "outline"
        out.append('<a class="sms-btn sms-btn--%s%s" href="%s">%s</a>' % (style, extra_cls, link(ctx, target), e(label)))
    return "".join(out)


def tone(d):
    return " sms-tone-%s" % d.get("tone", "white")


def head_block(block, d):
    out = ""
    if d.get("eyebrow"):
        out += '<div class="sms-%s__eyebrow">%s</div>' % (block, e(d["eyebrow"]))
    if d.get("title"):
        out += '<h2 class="sms-%s__title">%s</h2>' % (block, e(d["title"]))
    if d.get("lead"):
        out += '<div class="sms-%s__lead">%s</div>' % (block, paras(d["lead"]))
    return out


# ---------------------------------------------------------------------------
# Section renderers
# ---------------------------------------------------------------------------

def r_intro(ctx, d):
    aside = ""
    if d.get("aside"):
        a = d["aside"]
        items = "".join('<li class="sms-intro__list-item">%s</li>' % e(i) for i in a.get("items", []))
        note = '<div class="sms-intro__aside-note">%s</div>' % paras(a["note"]) if a.get("note") else ""
        aside = '<div class="sms-intro__aside"><h3 class="sms-intro__aside-title">%s</h3><ul class="sms-intro__list">%s</ul>%s</div>' % (e(a["title"]), items, note)
    strap = '<div class="sms-intro__strap">%s</div>' % e(d["strap"]) if d.get("strap") else ""
    wm = watermark(ctx) if d.get("watermark") else ""
    return """<section class="sms-intro%s"%s>
  %s
  <div class="sms-intro__inner">
    <div class="sms-intro__main">%s<div class="sms-intro__body">%s</div>%s</div>
    %s
  </div>
</section>
""" % (tone(d), sid(d), wm, head_block("intro", d), paras(d["body"]), strap, aside)


def sid(d):
    return ' id="%s"' % d["id"] if d.get("id") else ""


def r_cards(ctx, d):
    cols = d.get("cols", 3)
    items = []
    for i, it in enumerate(d["items"], 1):
        h = ""
        if d.get("numbered"):
            h += '<div class="sms-cards__num" aria-hidden="true">%02d</div>' % i
        h += '<h3 class="sms-cards__name">%s</h3>' % e(it["title"])
        if it.get("meta"):
            h += '<div class="sms-cards__meta">%s</div>' % e(it["meta"])
        if it.get("text"):
            h += '<div class="sms-cards__text">%s</div>' % paras(it["text"] if isinstance(it["text"], list) else [it["text"]])
        if it.get("list"):
            if it.get("list_title"):
                h += '<div class="sms-cards__list-title">%s</div>' % e(it["list_title"])
            h += '<ul class="sms-cards__list">%s</ul>' % "".join('<li class="sms-cards__list-item">%s</li>' % e(x) for x in it["list"])
        if it.get("link"):
            h += '<a class="sms-cards__link" href="%s">%s&nbsp;<span class="sms-arrow" aria-hidden="true">&rarr;</span></a>' % (link(ctx, it["link"][1]), e(it["link"][0]))
        items.append('<li class="sms-cards__item">%s</li>' % h)
    wm = watermark(ctx) if d.get("watermark") else ""
    return """<section class="sms-cards%s"%s>
  %s
  <div class="sms-cards__inner">
    <div class="sms-cards__head">%s</div>
    <ul class="sms-cards__grid sms-cards__grid--%d">%s</ul>
  </div>
</section>
""" % (tone(d), sid(d), wm, head_block("cards", d), cols, "".join(items))


def r_steps(ctx, d):
    items = "".join('<li class="sms-steps__item"><h3 class="sms-steps__name">%s</h3>%s</li>' % (
        e(it["title"]), '<div class="sms-steps__text">%s</div>' % paras(it["text"] if isinstance(it["text"], list) else [it["text"]]) if it.get("text") else "") for it in d["items"])
    note = '<div class="sms-steps__note">%s</div>' % paras(d["note"]) if d.get("note") else ""
    row = " sms-steps__list--row" if d.get("row") else ""
    wm = watermark(ctx) if d.get("watermark") else ""
    return """<section class="sms-steps%s"%s>
  %s
  <div class="sms-steps__inner">
    <div class="sms-steps__head">%s</div>
    <ol class="sms-steps__list%s">%s</ol>
    %s
  </div>
</section>
""" % (tone(d), sid(d), wm, head_block("steps", d), row, items, note)


def r_checklist(ctx, d):
    items = "".join('<li class="sms-checklist__item">%s</li>' % e(i) for i in d["items"])
    return """<section class="sms-checklist%s"%s>
  <div class="sms-checklist__inner">
    <div class="sms-checklist__head">%s</div>
    <ul class="sms-checklist__list">%s</ul>
  </div>
</section>
""" % (tone(d), sid(d), head_block("checklist", d), items)


def r_notice(ctx, d):
    acts = '<div class="sms-notice__actions">%s</div>' % buttons(ctx, d["buttons"]) if d.get("buttons") else ""
    return """<section class="sms-notice%s"%s>
  <div class="sms-notice__inner">
    <div class="sms-notice__box">
      <div class="sms-notice__label">%s</div>
      <h2 class="sms-notice__title">%s</h2>
      <div class="sms-notice__text">%s</div>
      %s
    </div>
  </div>
</section>
""" % (tone(d), sid(d), e(d["label"]), e(d["title"]), paras(d["text"]), acts)


def r_faq(ctx, d):
    items = []
    for q, a in d["items"]:
        a = a.replace(SITE + "/contact-us", ctx.href("contact"))
        items.append('<details class="sms-faq__item"><summary class="sms-faq__q">%s</summary><div class="sms-faq__a">%s</div></details>' % (e(q), a))
    more = ""
    if d.get("more"):
        more = '<div class="sms-faq__more"><a class="sms-btn sms-btn--outline" href="%s">%s</a></div>' % (link(ctx, d["more"][1]), e(d["more"][0]))
    return """<section class="sms-faq%s"%s>
  <div class="sms-faq__inner">
    <div class="sms-faq__head">%s%s</div>
    <div class="sms-faq__list">%s</div>
  </div>
</section>
""" % (tone(d), sid(d), head_block("faq", d), more, "".join(items))


def r_quotes(ctx, d):
    items = "".join('<figure class="sms-quotes__item"><div class="sms-quotes__label">%s</div><blockquote class="sms-quotes__text"><p>%s</p></blockquote>%s</figure>' % (
        e(it["label"]), e(it["text"]), '<figcaption class="sms-quotes__cite">%s</figcaption>' % e(it["cite"]) if it.get("cite") else "") for it in d["items"])
    wm = watermark(ctx) if d.get("watermark") else ""
    hb = head_block("quotes", d)
    return """<section class="sms-quotes%s"%s>
  %s
  <div class="sms-quotes__inner">
    %s
    <div class="sms-quotes__grid">%s</div>
  </div>
</section>
""" % (tone(d), sid(d), wm, '<div class="sms-quotes__head">%s</div>' % hb if hb else "", items)


def r_people(ctx, d):
    ppl = []
    for p in d["items"]:
        img = ctx.ph("portrait", "Placeholder for a portrait of %s, Director" % p["name"], "portrait of %s" % p["name"], "sms-people__img")
        ppl.append("""<li class="sms-people__person">
        <figure class="sms-people__media">%s</figure>
        <div class="sms-people__info">
          <div class="sms-people__role">Director</div>
          <h3 class="sms-people__name">%s</h3>
          <div class="sms-people__tags">%s</div>
          <div class="sms-people__bio">%s</div>
        </div>
      </li>""" % (img, e(p["name"]), e(p["tags"]), paras(p["bio"])))
    shared = ""
    if d.get("shared"):
        s = d["shared"]
        shared = '<div class="sms-people__shared"><div class="sms-people__shared-label">%s</div><h3 class="sms-people__shared-title">%s</h3><div class="sms-people__shared-text">%s</div></div>' % (e(s["label"]), e(s["title"]), paras(s["text"]))
    wm = watermark(ctx) if d.get("watermark") else ""
    return """<section class="sms-people%s"%s>
  %s
  <div class="sms-people__inner">
    <div class="sms-people__head">%s</div>
    <ul class="sms-people__grid">%s</ul>
    %s
  </div>
</section>
""" % (tone(d), sid(d), wm, head_block("people", d), "".join(ppl), shared)


def r_links(ctx, d):
    items = "".join('<li class="sms-links__item"><a class="sms-links__link" href="%s"><span class="sms-links__name">%s</span><span class="sms-links__text">%s</span><span class="sms-links__go">%s&nbsp;<span class="sms-arrow" aria-hidden="true">&rarr;</span></span></a></li>' % (
        link(ctx, it["link"]), e(it["title"]), e(it["text"]), e(it["go"])) for it in d["items"])
    return """<section class="sms-links%s"%s>
  <div class="sms-links__inner">
    <div class="sms-links__head">%s</div>
    <ul class="sms-links__grid">%s</ul>
  </div>
</section>
""" % (tone(d), sid(d), head_block("links", d), items)


def r_claim(ctx, d):
    wm = watermark(ctx) if d.get("watermark") else ""
    if d.get("image_text"):
        ctx.image_text.append(d["image_text"])
    return """<section class="sms-claim%s"%s>
  %s
  <div class="sms-claim__inner"><div class="sms-claim__text"><p>%s</p></div></div>
</section>
""" % (tone(d), sid(d), wm, e(d["text"]))


def r_contact(ctx, d):
    opts = "".join('<option>%s</option>' % e(o) for o in ["General enquiry", "Event Medical Cover", "Medical Training", "Risk & Needs Consultancy", "Pre-Hospital Career Support", "Recruitment"])
    ctx.placeholders.append("Contact form - not connected; to be wired to the WordPress form plugin")
    form = """<form class="sms-contact__form" action="#" method="post" data-sms-form>
      <h3 class="sms-contact__form-title">%s</h3>
      <div class="sms-contact__row">
        <div class="sms-contact__field"><label class="sms-contact__field-label" for="sms-f-name">Name</label><input class="sms-contact__input" id="sms-f-name" name="name" type="text" autocomplete="name"></div>
        <div class="sms-contact__field"><label class="sms-contact__field-label" for="sms-f-phone">Telephone</label><input class="sms-contact__input" id="sms-f-phone" name="phone" type="tel" autocomplete="tel"></div>
      </div>
      <div class="sms-contact__field"><label class="sms-contact__field-label" for="sms-f-email">Email</label><input class="sms-contact__input" id="sms-f-email" name="email" type="email" autocomplete="email"></div>
      <div class="sms-contact__field"><label class="sms-contact__field-label" for="sms-f-topic">What is your enquiry about?</label><select class="sms-contact__input" id="sms-f-topic" name="topic">%s</select></div>
      <div class="sms-contact__field"><label class="sms-contact__field-label" for="sms-f-msg">Message</label><textarea class="sms-contact__input sms-contact__input--area" id="sms-f-msg" name="message"></textarea></div>
      <div class="sms-contact__note"><p>Concept only: this form is not connected yet. Please call or email us.</p></div>
      <button class="sms-btn sms-btn--primary sms-contact__submit" type="submit">Send enquiry</button>
      <div class="sms-contact__status" role="status" aria-live="polite"></div>
    </form>""" % (e(d.get("form_title", "Use our form below to contact us")), opts)
    return """<section class="sms-contact%s"%s>
  <div class="sms-contact__inner">
    <div class="sms-contact__info">
      %s
      %s
      <div class="sms-contact__text">%s</div>
      <ul class="sms-contact__details">
        <li class="sms-contact__detail"><div class="sms-contact__label">Telephone</div><a class="sms-contact__value" href="tel:%s">%s</a></li>
        <li class="sms-contact__detail"><div class="sms-contact__label">Email</div><a class="sms-contact__value" href="mailto:%s">%s</a></li>
        <li class="sms-contact__detail"><div class="sms-contact__label">Registered Office</div><div class="sms-contact__small"><p>Streamline Safety &amp; Medical Solutions Ltd, 8 Cobblestone Drive, Swadlincote, Derbyshire, DE11 0FL</p><p>Please note: This is our registered office address for official correspondence only and is not open to visitors or walk-in enquiries.</p></div></li>
      </ul>
    </div>
    %s
  </div>
</section>
""" % (tone(d), sid(d), head_block("contact", d), '<div class="sms-contact__lead">%s</div>' % e(d["lead_line"]) if d.get("lead_line") else "",
       paras(d.get("body", [])), PHONE_TEL, PHONE, EMAIL, EMAIL, form)


FORM_JS = """<script>
(function () {
  var forms = document.querySelectorAll('[data-sms-form]');
  Array.prototype.forEach.call(forms, function (form) {
    form.addEventListener('submit', function (ev) {
      ev.preventDefault();
      var status = form.querySelector('[role="status"]');
      if (status) status.textContent = 'Thanks - this is a concept, so nothing has been sent. Please call 01283 358789 or email hello@streamlinesms.co.uk.';
    });
  });
})();
</script>
"""

SHARED_RENDERERS = {
    "intro": r_intro, "cards": r_cards, "steps": r_steps, "checklist": r_checklist,
    "notice": r_notice, "faq": r_faq, "quotes": r_quotes, "people": r_people,
    "links": r_links, "claim": r_claim, "contact": r_contact,
}


def comment(concept, name, slug, ctx):
    lines = ["  Streamline Safety & Medical Solutions - Concept %d (%s): %s" % (concept, name, "Home" if slug == "home" else LABEL[slug]),
             "  Pitch concept by CADS. Not production code. Built for porting to WordPress / Elementor.",
             "  Generated by build/build.py from build/content.py - edit those, then rebuild.",
             "",
             "  PLACEHOLDERS ON THIS PAGE"]
    seen = []
    for p in ctx.placeholders:
        if p not in seen:
            seen.append(p)
    lines += ["  - " + p for p in seen] or ["  - none"]
    lines += ["", "  TEXT TAKEN FROM IMAGES ON THE LIVE SITE (confirm with client)"]
    it = []
    for t in ctx.image_text:
        if t not in it:
            it.append(t)
    lines += ["  - " + t for t in it] or ["  - none"]
    lines += ["", "  No statistics, reviews, response times or accreditations have been invented.",
              "  All other copy is from reference/content.md / the live site."]
    return "<!--\n" + "\n".join(lines) + "\n-->"
