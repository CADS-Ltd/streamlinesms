"""Shared helpers, page shell, components and motion for the Streamline concepts.

Every concept renders the same content (build/content.py). A concept supplies its
own tokens, page hero, CTA band, footer colours and homepage, and restyles the
shared sections through its CSS.
"""
import html
import re

import content as C

SITE = "https://www.streamlinesms.co.uk"
PHONE = "01283 358789"
PHONE_TEL = "01283358789"
EMAIL = "hello@streamlinesms.co.uk"

PAGES = [
    ("event-medical-cover", "Event Medical Cover"),
    ("medical-training", "Medical Training"),
    ("risk-needs-consultancy", "Risk & Needs Consultancy"),
    ("pre-hospital-career-support", "Pre-Hospital Career Support"),
    ("recruitment", "Recruitment"),
    ("about", "About Us"),
    ("contact", "Contact Us"),
    ("book", "Book Online"),
]
MAIN_NAV = ["event-medical-cover", "medical-training", "risk-needs-consultancy", "about", "contact"]
LABEL = dict(PAGES)
LABEL["home"] = "Home"

NAMED = {
    0x2019: "&rsquo;", 0x2018: "&lsquo;", 0x201C: "&ldquo;", 0x201D: "&rdquo;",
    0x2013: "&ndash;", 0x2014: "&mdash;", 0x2192: "&rarr;", 0x2197: "&nearr;",
    0x00B7: "&middot;", 0x00A0: "&nbsp;", 0x2026: "&hellip;", 0x2191: "&uarr;", 0x2193: "&darr;",
    0x2212: "&minus;", 0x00D7: "&times;",
}


def ascii_html(s):
    out = []
    for ch in s:
        o = ord(ch)
        out.append(ch if o < 128 else NAMED.get(o, "&#%d;" % o))
    return "".join(out)


def e(text):
    t = html.escape(text, quote=False)
    return re.sub(r"\[\[(.+?)\]\]", r'<span class="sms-mark">\1</span>', t)


def plain(text):
    return re.sub(r"\[\[(.+?)\]\]", r"\1", text)


def attr(text):
    return html.escape(plain(text), quote=True)


def split_first(text):
    """First sentence and the rest (exact substrings of the original)."""
    m = re.search(r"(?<=[.!?])\s+(?=[A-Z“])", text)
    if not m:
        return text, ""
    return text[:m.start()], text[m.end():]


# ---------------------------------------------------------------------------
# Icons: simple 24px line icons drawn for these concepts, in the style of the
# green line icons already used in Streamline's own graphics.
# ---------------------------------------------------------------------------
ICONS = {
    "check": '<path d="M20 6 9 17l-5-5"/>',
    "shield": '<path d="M12 3l7 3v6c0 4.5-3 7.5-7 9-4-1.5-7-4.5-7-9V6z"/><path d="M9 12l2 2 4-4"/>',
    "users": '<circle cx="9" cy="8" r="3.2"/><path d="M3 20c0-3.3 2.7-6 6-6s6 2.7 6 6"/><circle cx="17" cy="9" r="2.4"/><path d="M16.5 14.2c2.6.4 4.5 2.6 4.5 5.3"/>',
    "user": '<circle cx="12" cy="8" r="4"/><path d="M4 21c0-4.4 3.6-8 8-8s8 3.6 8 8"/>',
    "heart": '<path d="M12 20s-7.5-4.6-7.5-10.3A4.2 4.2 0 0 1 12 7.2a4.2 4.2 0 0 1 7.5 2.5C19.5 15.4 12 20 12 20z"/><path d="M7.5 12h2.3l1.4-2.6 1.9 5.2 1.4-2.6h2"/>',
    "clipboard": '<rect x="5" y="4" width="14" height="17" rx="2"/><path d="M9 3h6v3H9z"/><path d="M9 13l2 2 4-4"/>',
    "calendar": '<rect x="3.5" y="5" width="17" height="16" rx="2"/><path d="M3.5 10h17M8 3v4M16 3v4"/>',
    "phone": '<path d="M6 3.5h3.2l1.6 4.4-2.1 1.3a11 11 0 0 0 6.1 6.1l1.3-2.1 4.4 1.6V18a2.5 2.5 0 0 1-2.6 2.5A16 16 0 0 1 3.5 6.1 2.5 2.5 0 0 1 6 3.5z"/>',
    "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3.5 7l8.5 6 8.5-6"/>',
    "pin": '<path d="M12 21s-7-6-7-11a7 7 0 0 1 14 0c0 5-7 11-7 11z"/><circle cx="12" cy="10" r="2.5"/>',
    "cap": '<path d="M2 9l10-5 10 5-10 5z"/><path d="M6 11v5c3.5 2.3 8.5 2.3 12 0v-5"/><path d="M22 9v6"/>',
    "firstaid": '<rect x="3" y="7" width="18" height="13" rx="2"/><path d="M9 7V5h6v2"/><path d="M12 10.5v6M9 13.5h6"/>',
    "tent": '<path d="M2.5 20h19"/><path d="M12 4L4 20"/><path d="M12 4l8 16"/><path d="M12 12.5L9.2 20h5.6z"/>',
    "briefcase": '<rect x="3" y="7" width="18" height="13" rx="2"/><path d="M9 7V5h6v2"/><path d="M3 12.5h18"/>',
    "trophy": '<path d="M8 4h8v5a4 4 0 0 1-8 0z"/><path d="M8 6H5.5a2.5 2.5 0 0 0 2.6 3.5"/><path d="M16 6h2.5a2.5 2.5 0 0 1-2.6 3.5"/><path d="M12 13v4M8.5 20h7M10 17h4"/>',
    "music": '<path d="M9 18V5l11-2v13"/><circle cx="6.5" cy="18" r="2.5"/><circle cx="17.5" cy="16" r="2.5"/>',
    "school": '<path d="M3 21h18"/><path d="M5 21V9.5L12 5l7 4.5V21"/><path d="M10 21v-5h4v5"/><circle cx="12" cy="11" r="1.6"/>',
    "building": '<rect x="5" y="3" width="14" height="18" rx="1.5"/><path d="M9 7h2M13 7h2M9 11h2M13 11h2M9 15h2M13 15h2"/>',
    "fire": '<path d="M12 21c-3.9 0-6.5-2.6-6.5-6 0-3.8 3.5-5.8 4-9.5 2.8 1.6 4.8 4.4 4.8 7.2.9-.7 1.4-1.7 1.6-2.9 1.5 1.4 2.6 3.4 2.6 5.2 0 3.4-2.6 6-6.5 6z"/>',
    "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3.2 2"/>',
    "chat": '<path d="M4 5h16v11H9.5L4 20z"/><path d="M8 10h8M8 13h5"/>',
    "search": '<circle cx="11" cy="11" r="7"/><path d="M20 20l-4-4"/>',
    "compass": '<circle cx="12" cy="12" r="9"/><path d="M15.5 8.5l-2 5-5 2 2-5z"/>',
    "route": '<circle cx="6" cy="18" r="2.5"/><circle cx="18" cy="6" r="2.5"/><path d="M8.5 18H15a3 3 0 0 0 0-6H9a3 3 0 0 1 0-6h6.5"/>',
    "star": '<path d="M12 3.5l2.6 5.3 5.9.9-4.3 4.1 1 5.8L12 16.9l-5.2 2.7 1-5.8L3.5 9.7l5.9-.9z"/>',
    "target": '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1.2"/>',
    "award": '<circle cx="12" cy="9" r="6"/><path d="M8.5 14 7 21l5-2.8 5 2.8-1.5-7"/>',
    "hardhat": '<path d="M3 18h18"/><path d="M5 18v-2.5a7 7 0 0 1 14 0V18"/><path d="M10 9V6h4v3"/>',
    "file": '<path d="M6 3h8l4 4v14H6z"/><path d="M14 3v4h4"/><path d="M9 13h6M9 17h6"/>',
    "sparkle": '<path d="M12 3l1.8 5.2L19 10l-5.2 1.8L12 17l-1.8-5.2L5 10l5.2-1.8z"/><path d="M19 16l.8 2.2L22 19l-2.2.8L19 22l-.8-2.2L16 19l2.2-.8z"/>',
    "arrow": '<path d="M5 12h14"/><path d="M13 6l6 6-6 6"/>',
    "plus": '<path d="M12 5v14M5 12h14"/>',
    "minus": '<path d="M5 12h14"/>',
    "quote": '<path d="M9.5 7H6v5h3.5c0 2.5-1.2 4-3.5 4.5"/><path d="M18 7h-3.5v5H18c0 2.5-1.2 4-3.5 4.5"/>',
    "alert": '<path d="M12 3.5l9 16H3z"/><path d="M12 10v4.5M12 17.5v.1"/>',
}


def icon(name, cls=""):
    return '<svg class="sms-icon%s" viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">%s</svg>' % (
        (" " + cls) if cls else "", ICONS[name])


class Ctx:
    def __init__(self, concept, slug):
        self.concept = concept
        self.slug = slug
        self.root = "" if slug == "home" else "../"
        self.photos = []
        self.notes = []

    def href(self, slug):
        if slug == "home":
            return "%sconcept-%d.html" % (self.root, self.concept)
        if self.slug == "home":
            return "concept-%d/%s.html" % (self.concept, slug)
        return "%s.html" % slug

    def asset(self, name):
        return self.root + "assets/" + name


def photo(ctx, key, cls="", lazy=True, parallax=True, figcls=""):
    f, w, h, focus, alt = C.PHOTOS[key]
    ctx.photos.append("assets/photos/" + f)
    return '<figure class="sms-photo%s"><img class="sms-photo__img%s%s" src="%s" alt="%s" width="%d" height="%d" style="object-position: %s"%s></figure>' % (
        (" " + figcls) if figcls else "", " sms-parallax" if parallax else "", (" " + cls) if cls else "",
        ctx.asset("photos/" + f), attr(alt), w, h, focus, ' loading="lazy"' if lazy else ' fetchpriority="high"')


def link(ctx, target):
    """target: page slug, 'book', 'book:<service>', 'tel', 'mail' or absolute URL."""
    if target == "tel":
        return "tel:" + PHONE_TEL
    if target == "mail":
        return "mailto:" + EMAIL
    if target.startswith("http") or target.startswith("#"):
        return target
    if target.startswith("book:"):
        return ctx.href("book") + "?service=" + target.split(":", 1)[1]
    return ctx.href(target)


def buttons(ctx, btns, extra_cls=""):
    out = []
    for i, (label, target) in enumerate(btns):
        style = "primary" if i == 0 else "outline"
        arrow = '&nbsp;<span class="sms-arrow" aria-hidden="true">&rarr;</span>' if i == 0 else ""
        out.append('<a class="sms-btn sms-btn--%s%s" href="%s">%s%s</a>' % (style, extra_cls, link(ctx, target), e(label), arrow))
    return "".join(out)


def paras(lst):
    return "".join("<p>%s</p>" % e(p) for p in lst)


def more(inner, label_open="Read more", label_close="Show less"):
    if not inner:
        return ""
    return ('<details class="sms-more"><summary class="sms-more__toggle"><span class="sms-more__label sms-more__label--open">%s</span>'
            '<span class="sms-more__label sms-more__label--close">%s</span>%s</summary><div class="sms-more__body">%s</div></details>') % (
        label_open, label_close, icon("plus", "sms-more__icon"), inner)


def chips(items, cls="sms-chips"):
    return '<ul class="%s">%s</ul>' % (cls, "".join('<li class="sms-chips__item">%s<span class="sms-chips__text">%s</span></li>' % (icon(i, "sms-chips__icon"), e(t)) for i, t in items))


def tone(d):
    return " sms-tone-%s" % d.get("tone", "white")


def sid(d):
    return ' id="%s"' % d["id"] if d.get("id") else ""


def head_block(block, d):
    out = ""
    if d.get("eyebrow"):
        out += '<div class="sms-%s__eyebrow">%s</div>' % (block, e(d["eyebrow"]))
    if d.get("title"):
        out += '<h2 class="sms-%s__title">%s</h2>' % (block, e(d["title"]))
    if d.get("lead"):
        out += '<div class="sms-%s__lead">%s</div>' % (block, paras(d["lead"]))
    return out


def watermark(ctx, color="blue"):
    return '<img class="sms-watermark" src="%s" alt="" width="378" height="399" loading="lazy" aria-hidden="true">' % ctx.asset("streamline-shield-%s.png" % color)


# ---------------------------------------------------------------------------
# Base CSS
# ---------------------------------------------------------------------------
BASE_CSS = r"""
.sms-page {
  --sms-navy: #061e35;
  --sms-navy-2: #0b3152;
  --sms-green: #407f36;
  --sms-green-on-navy: #82d06e;
  --sms-mint: #dcefd6;
  --sms-pale: #f4f8f3;
  --sms-pale-2: #eef7ec;
  --sms-white: #ffffff;
  --sms-ink-soft: #405365;
  --sms-line: #d9e2e7;
  --sms-line-green: #d3e4cf;
  --sms-font: "Montserrat", Arial, sans-serif;
  --sms-step--1: clamp(0.8125rem, 0.79rem + 0.1vw, 0.875rem);
  --sms-step-0: clamp(1rem, 0.96rem + 0.2vw, 1.0625rem);
  --sms-step-1: clamp(1.125rem, 1.06rem + 0.3vw, 1.3125rem);
  --sms-step-2: clamp(1.6rem, 1.3rem + 1.3vw, 2.375rem);
  --sms-step-3: clamp(2.1rem, 1.4rem + 3vw, 3.75rem);
  --sms-gutter: clamp(1rem, 0.6rem + 2vw, 2.5rem);
  --sms-section: clamp(3.5rem, 2.5rem + 4.5vw, 6.5rem);
  --sms-max: 74rem;
  --sms-radius: 1.25rem;
  --sms-radius-sm: 0.75rem;
  --sms-shadow: 0 18px 40px rgba(6, 30, 53, 0.08);
  --sms-shadow-lg: 0 24px 60px rgba(6, 30, 53, 0.14);
  --sms-ease: cubic-bezier(0.22, 0.8, 0.24, 1);
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
.sms-page .sms-skip { position: absolute; left: -999px; top: 0; z-index: 50; padding: 0.75rem 1rem; background: var(--sms-navy); color: var(--sms-white); }
.sms-page .sms-skip:focus { left: 1rem; top: 1rem; }
.sms-page .sms-visually-hidden { position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0); clip-path: inset(50%); white-space: nowrap; }

/* ---------- Global utilities (Elementor: global styles / classes) ---------- */
.sms-page .sms-icon { display: inline-block; flex: 0 0 auto; min-width: 0; width: 1.5rem; height: 1.5rem; vertical-align: middle; }
.sms-page .sms-btn { display: inline-flex; align-items: center; gap: 0.35rem; min-width: 0; padding: 0.95rem 1.4rem; border: 2px solid transparent; border-radius: 999px; font-size: var(--sms-step--1); font-weight: 700; line-height: 1.25; text-decoration: none; transition: transform 0.25s var(--sms-ease); }
.sms-page .sms-btn:hover { transform: translateY(-3px); }
.sms-page .sms-btn:active { transform: translateY(0) scale(0.98); }
.sms-page .sms-btn--primary { border-color: var(--sms-green); background: var(--sms-green); color: var(--sms-white); box-shadow: 0 10px 22px rgba(64, 127, 54, 0.28); }
.sms-page .sms-btn--outline { border-color: var(--sms-navy); background: transparent; color: var(--sms-navy); }
.sms-page .sms-btn--outline:hover { background: var(--sms-navy); color: var(--sms-white); }
.sms-page .sms-btn:disabled { box-shadow: none; opacity: 0.55; cursor: not-allowed; transform: none; }
.sms-page .sms-btn--light { border-color: var(--sms-white); background: var(--sms-white); color: var(--sms-navy); }
.sms-page .sms-arrow { display: inline-block; transition: transform 0.25s var(--sms-ease); }
.sms-page a:hover .sms-arrow,
.sms-page button:hover .sms-arrow { transform: translateX(5px); }
.sms-page .sms-mark { color: var(--sms-green); }

/* Photo frame (with gentle parallax on the image) */
.sms-page .sms-photo { position: relative; min-width: 0; margin: 0; overflow: hidden; border-radius: var(--sms-radius); background: var(--sms-pale); }
.sms-page .sms-photo__img { display: block; width: 100%; height: 100%; object-fit: cover; }

/* Read more */
.sms-page .sms-more { margin-top: 0.75rem; }
.sms-page .sms-arrow,
.sms-page .sms-more,
.sms-page .sms-more__label,
.sms-page .sms-chips { min-width: 0; }
.sms-page .sms-more__toggle { display: inline-flex; align-items: center; gap: 0.4rem; padding: 0.35rem 0; color: var(--sms-green); cursor: pointer; font-size: var(--sms-step--1); font-weight: 700; list-style: none; }
.sms-page .sms-more__toggle::-webkit-details-marker { display: none; }
.sms-page .sms-more__icon { width: 1.1rem; height: 1.1rem; transition: transform 0.3s var(--sms-ease); }
.sms-page .sms-more[open] .sms-more__icon { transform: rotate(45deg); }
.sms-page .sms-more__label--close { display: none; }
.sms-page .sms-more[open] .sms-more__label--open { display: none; }
.sms-page .sms-more[open] .sms-more__label--close { display: inline; }
.sms-page .sms-more__body { padding-top: 0.5rem; color: var(--sms-ink-soft); }
.sms-page .sms-more__body p { margin: 0 0 0.75rem; }
.sms-page .sms-more[open] .sms-more__body { animation: sms-drop 0.4s var(--sms-ease) both; }

/* Icon chips */
.sms-page .sms-chips { display: flex; flex-wrap: wrap; gap: 0.5rem; margin: 0; padding: 0; list-style: none; }
.sms-page .sms-chips__item { display: inline-flex; align-items: center; gap: 0.5rem; min-width: 0; padding: 0.5rem 0.9rem 0.5rem 0.6rem; border-radius: 999px; background: var(--sms-white); box-shadow: 0 4px 14px rgba(6, 30, 53, 0.06); font-size: var(--sms-step--1); font-weight: 600; line-height: 1.35; transition: transform 0.25s var(--sms-ease); }
.sms-page .sms-chips__item:hover { transform: translateY(-2px); }
.sms-page .sms-chips__icon { width: 1.75rem; height: 1.75rem; padding: 0.35rem; border-radius: 50%; background: var(--sms-mint); color: var(--sms-green); }
.sms-page .sms-chips__text { min-width: 0; }

/* Shared inner widths */
.sms-header .sms-header__inner,
.sms-topbar .sms-topbar__inner,
.sms-feature .sms-feature__inner,
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
.sms-marquee .sms-marquee__inner,
.sms-booking .sms-booking__inner,
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
.sms-topbar .sms-topbar__link { display: inline-flex; align-items: center; gap: 0.4rem; min-width: 0; color: var(--sms-white); font-weight: 600; text-decoration: none; overflow-wrap: anywhere; }
.sms-topbar .sms-topbar__link:hover { text-decoration: underline; }
.sms-topbar .sms-topbar__icon { width: 1rem; height: 1rem; }
@media (min-width: 48em) {
  .sms-topbar .sms-topbar__text { display: block; }
}

/* ---------- Header (sticky) ---------- */
.sms-header { position: sticky; top: 0; z-index: 30; border-bottom: 1px solid rgba(217, 226, 231, 0.7); background: rgba(255, 255, 255, 0.94); -webkit-backdrop-filter: blur(10px); backdrop-filter: blur(10px); }
.sms-header .sms-header__inner { display: flex; align-items: center; justify-content: space-between; gap: 1.5rem; min-height: 4.75rem; }
.sms-header .sms-header__logo { display: block; flex: 0 0 auto; min-width: 0; line-height: 0; transition: transform 0.3s var(--sms-ease); }
.sms-header .sms-header__logo:hover { transform: scale(1.03); }
.sms-header .sms-header__logo-img { display: block; width: clamp(10.5rem, 8rem + 8vw, 13.5rem); height: auto; }
.sms-header .sms-header__nav { display: none; min-width: 0; }
.sms-header .sms-header__list { display: flex; align-items: center; gap: clamp(0.25rem, 0rem + 0.6vw, 0.75rem); min-width: 0; margin: 0; padding: 0; list-style: none; }
.sms-header .sms-header__item { min-width: 0; }
.sms-header .sms-header__link { position: relative; display: block; padding: 0.5rem 0.7rem; border-radius: 999px; color: var(--sms-navy); font-size: var(--sms-step--1); font-weight: 600; text-decoration: none; white-space: nowrap; }
.sms-header .sms-header__link::after { content: ""; position: absolute; left: 0.7rem; right: 0.7rem; bottom: 0.2rem; height: 2px; border-radius: 2px; background: var(--sms-green); transform: scaleX(0); transform-origin: left; transition: transform 0.3s var(--sms-ease); }
.sms-header .sms-header__link:hover::after,
.sms-header .sms-header__link[aria-current="page"]::after { transform: scaleX(1); }
.sms-header .sms-header__cta { flex: 0 0 auto; min-width: 0; }
.sms-header .sms-header__menu { position: relative; min-width: 0; }
.sms-header .sms-header__summary { display: flex; align-items: center; gap: 0.5rem; padding: 0.6rem 1rem; border-radius: 999px; background: var(--sms-pale-2); color: var(--sms-navy); cursor: pointer; font-size: var(--sms-step--1); font-weight: 700; list-style: none; }
.sms-header .sms-header__summary::-webkit-details-marker { display: none; }
.sms-header .sms-header__bars { display: block; min-width: 0; width: 1.1rem; height: 2px; background: currentColor; box-shadow: 0 -5px 0 currentColor, 0 5px 0 currentColor; }
.sms-header .sms-header__panel { position: absolute; right: 0; top: calc(100% + 0.6rem); z-index: 40; width: min(20rem, calc(100vw - 2rem)); padding: 0.6rem; border-radius: var(--sms-radius); background: var(--sms-white); box-shadow: var(--sms-shadow-lg); }
.sms-header .sms-header__menu[open] .sms-header__panel { animation: sms-pop 0.3s var(--sms-ease) both; }
.sms-header .sms-header__panel-list { margin: 0; padding: 0; list-style: none; }
.sms-header .sms-header__panel-item { min-width: 0; }
.sms-header .sms-header__panel-link { display: flex; align-items: center; gap: 0.6rem; padding: 0.7rem 0.8rem; border-radius: var(--sms-radius-sm); color: var(--sms-navy); font-weight: 600; text-decoration: none; }
.sms-header .sms-header__panel-link:hover { background: var(--sms-pale); }
.sms-header .sms-header__panel-link[aria-current="page"] { background: var(--sms-pale-2); }
.sms-header .sms-header__panel-icon { width: 1.25rem; height: 1.25rem; color: var(--sms-green); }
.sms-header .sms-header__panel-sep { height: 1px; margin: 0.4rem 0.8rem; background: var(--sms-line); }
@media (min-width: 72em) {
  .sms-header .sms-header__nav { display: flex; align-items: center; gap: 1.25rem; }
  .sms-header .sms-header__menu { display: none; }
}

/* ---------- Section heads ---------- */
.sms-feature .sms-feature__eyebrow,
.sms-cards .sms-cards__eyebrow,
.sms-steps .sms-steps__eyebrow,
.sms-checklist .sms-checklist__eyebrow,
.sms-faq .sms-faq__eyebrow,
.sms-quotes .sms-quotes__eyebrow,
.sms-people .sms-people__eyebrow,
.sms-contact .sms-contact__eyebrow,
.sms-links .sms-links__eyebrow,
.sms-marquee .sms-marquee__eyebrow,
.sms-booking .sms-booking__eyebrow {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  margin-bottom: 0.9rem;
  color: var(--sms-green);
  font-size: var(--sms-step--1);
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
}
.sms-feature .sms-feature__eyebrow::before,
.sms-cards .sms-cards__eyebrow::before,
.sms-steps .sms-steps__eyebrow::before,
.sms-checklist .sms-checklist__eyebrow::before,
.sms-faq .sms-faq__eyebrow::before,
.sms-quotes .sms-quotes__eyebrow::before,
.sms-people .sms-people__eyebrow::before,
.sms-contact .sms-contact__eyebrow::before,
.sms-links .sms-links__eyebrow::before,
.sms-marquee .sms-marquee__eyebrow::before,
.sms-booking .sms-booking__eyebrow::before { content: ""; flex: 0 0 auto; width: 1.5rem; height: 3px; border-radius: 3px; background: var(--sms-green); }
.sms-feature .sms-feature__title,
.sms-cards .sms-cards__title,
.sms-steps .sms-steps__title,
.sms-checklist .sms-checklist__title,
.sms-faq .sms-faq__title,
.sms-quotes .sms-quotes__title,
.sms-people .sms-people__title,
.sms-contact .sms-contact__title,
.sms-links .sms-links__title,
.sms-marquee .sms-marquee__title,
.sms-booking .sms-booking__title {
  margin: 0 0 1rem;
  font-size: var(--sms-step-2);
  font-weight: 700;
  line-height: 1.18;
  letter-spacing: -0.015em;
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
.sms-faq .sms-faq__lead { color: var(--sms-ink-soft); font-size: var(--sms-step-1); line-height: 1.55; }
.sms-cards .sms-cards__lead p,
.sms-steps .sms-steps__lead p,
.sms-checklist .sms-checklist__lead p,
.sms-people .sms-people__lead p,
.sms-links .sms-links__lead p,
.sms-faq .sms-faq__lead p { margin: 0 0 0.75rem; }

.sms-feature,
.sms-cards,
.sms-steps,
.sms-checklist,
.sms-notice,
.sms-faq,
.sms-quotes,
.sms-people,
.sms-contact,
.sms-links,
.sms-claim,
.sms-marquee,
.sms-booking { position: relative; padding: var(--sms-section) 0; overflow: hidden; }
.sms-feature.sms-tone-pale,
.sms-cards.sms-tone-pale,
.sms-steps.sms-tone-pale,
.sms-checklist.sms-tone-pale,
.sms-notice.sms-tone-pale,
.sms-faq.sms-tone-pale,
.sms-quotes.sms-tone-pale,
.sms-people.sms-tone-pale,
.sms-contact.sms-tone-pale,
.sms-links.sms-tone-pale,
.sms-claim.sms-tone-pale,
.sms-marquee.sms-tone-pale,
.sms-booking.sms-tone-pale { background: var(--sms-pale); }
.sms-faq { overflow: visible; }

.sms-feature .sms-watermark,
.sms-cards .sms-watermark,
.sms-steps .sms-watermark,
.sms-quotes .sms-watermark,
.sms-people .sms-watermark,
.sms-claim .sms-watermark,
.sms-checklist .sms-watermark { position: absolute; right: -4rem; bottom: -5rem; width: clamp(14rem, 10rem + 18vw, 26rem); height: auto; opacity: 0.06; pointer-events: none; animation: sms-spin 80s linear infinite; }

/* ---------- Feature (photo + text) ---------- */
.sms-feature .sms-feature__inner { position: relative; display: grid; gap: clamp(2rem, 1.5rem + 3vw, 4.5rem); align-items: center; }
.sms-feature .sms-feature__media { position: relative; z-index: 0; min-width: 0; }
.sms-feature .sms-feature__frame { aspect-ratio: 4 / 3.4; box-shadow: var(--sms-shadow-lg); }
.sms-feature .sms-feature__blob { position: absolute; z-index: -1; right: -6%; bottom: -8%; width: 70%; aspect-ratio: 1; border-radius: 42% 58% 55% 45% / 48% 42% 58% 52%; background: var(--sms-mint); animation: sms-float 9s ease-in-out infinite; }
.sms-feature .sms-feature__main { min-width: 0; }
.sms-feature .sms-feature__lead { max-width: 38rem; font-size: var(--sms-step-1); line-height: 1.55; color: var(--sms-navy); }
.sms-feature .sms-feature__lead p { margin: 0; }
.sms-feature .sms-feature__strap { display: inline-flex; align-items: center; gap: 0.5rem; margin-top: 1rem; padding: 0.6rem 1rem; border-radius: 999px; background: var(--sms-mint); color: var(--sms-navy); font-weight: 700; }
.sms-feature .sms-feature__strap-icon { color: var(--sms-green); }
.sms-feature .sms-feature__chips-title { margin: 1.75rem 0 0.75rem; font-size: var(--sms-step-0); font-weight: 700; }
.sms-feature .sms-feature__actions { display: flex; flex-wrap: wrap; gap: 0.75rem; margin-top: 1.75rem; }
.sms-feature.sms-tone-white .sms-chips__item { background: var(--sms-pale); box-shadow: none; }
@media (min-width: 56em) {
  .sms-feature .sms-feature__inner { grid-template-columns: minmax(0, 0.95fr) minmax(0, 1.05fr); }
  .sms-feature.sms-feature--flip .sms-feature__media { order: 2; }
  .sms-feature.sms-feature--flip .sms-feature__blob { right: auto; left: -6%; }
}

/* ---------- Cards ---------- */
.sms-cards .sms-cards__inner { position: relative; }
.sms-cards .sms-cards__grid { display: grid; gap: clamp(1rem, 0.6rem + 1.5vw, 1.5rem); margin: 0; padding: 0; list-style: none; }
.sms-cards .sms-cards__item { position: relative; display: flex; flex-direction: column; min-width: 0; padding: clamp(1.5rem, 1.1rem + 1.5vw, 2.1rem); border-radius: var(--sms-radius); background: var(--sms-white); box-shadow: var(--sms-shadow); transition: transform 0.35s var(--sms-ease); }
.sms-cards.sms-tone-white .sms-cards__item { background: var(--sms-pale); box-shadow: none; }
.sms-cards .sms-cards__item:hover { transform: translateY(-6px); }
.sms-cards .sms-cards__top { display: flex; align-items: center; justify-content: space-between; gap: 1rem; min-width: 0; margin-bottom: 1.1rem; }
.sms-cards .sms-cards__icon { width: 3.25rem; height: 3.25rem; padding: 0.75rem; border-radius: 1rem; background: var(--sms-mint); color: var(--sms-green); transition: transform 0.35s var(--sms-ease); }
.sms-cards.sms-tone-white .sms-cards__icon { background: var(--sms-white); }
.sms-cards .sms-cards__item:hover .sms-cards__icon { transform: rotate(-8deg) scale(1.08); }
.sms-cards .sms-cards__num { min-width: 0; color: var(--sms-green); font-size: 2rem; font-weight: 700; line-height: 1; opacity: 1; }
.sms-cards .sms-cards__name { min-width: 0; margin: 0 0 0.5rem; font-size: var(--sms-step-1); font-weight: 700; line-height: 1.3; }
.sms-cards .sms-cards__meta { display: inline-flex; align-self: flex-start; align-items: center; gap: 0.35rem; min-width: 0; margin-bottom: 0.6rem; padding: 0.25rem 0.7rem; border-radius: 999px; background: var(--sms-pale-2); color: var(--sms-navy); font-size: var(--sms-step--1); font-weight: 600; }
.sms-cards.sms-tone-white .sms-cards__meta { background: var(--sms-white); }
.sms-cards .sms-cards__meta-icon { width: 1rem; height: 1rem; color: var(--sms-green); }
.sms-cards .sms-cards__text { min-width: 0; color: var(--sms-ink-soft); }
.sms-cards .sms-cards__text p { margin: 0; }
.sms-cards .sms-cards__list-title { margin: 0.5rem 0 0.4rem; font-size: var(--sms-step--1); font-weight: 700; letter-spacing: 0.08em; text-transform: uppercase; color: var(--sms-navy); }
.sms-cards .sms-cards__list { margin: 0; padding: 0; list-style: none; font-size: var(--sms-step--1); }
.sms-cards .sms-cards__list-item { display: flex; gap: 0.5rem; min-width: 0; padding: 0.35rem 0; }
.sms-cards .sms-cards__list-item > span { min-width: 0; }
.sms-cards .sms-cards__check { width: 1.1rem; height: 1.1rem; margin-top: 0.15rem; color: var(--sms-green); }
.sms-cards .sms-cards__link { align-self: flex-start; min-width: 0; margin-top: auto; padding-top: 1rem; color: var(--sms-green); font-weight: 700; text-decoration: none; }
@media (min-width: 46em) {
  .sms-cards .sms-cards__grid--2,
  .sms-cards .sms-cards__grid--3,
  .sms-cards .sms-cards__grid--4 { grid-template-columns: repeat(2, minmax(0, 1fr)); }
}
@media (min-width: 64em) {
  .sms-cards .sms-cards__grid--3 { grid-template-columns: repeat(3, minmax(0, 1fr)); }
  .sms-cards .sms-cards__grid--4 { grid-template-columns: repeat(4, minmax(0, 1fr)); }
}

/* ---------- Steps (timeline) ---------- */
.sms-steps .sms-steps__inner { position: relative; }
.sms-steps .sms-steps__track { position: relative; }
.sms-steps .sms-steps__line { position: absolute; left: 1.5rem; top: 1rem; bottom: 1rem; width: 3px; border-radius: 3px; background: var(--sms-line-green); }
.sms-steps .sms-steps__line-fill { display: block; width: 100%; height: 100%; border-radius: 3px; background: var(--sms-green); transform-origin: top; }
.sms-steps .sms-steps__list { position: relative; display: grid; gap: 1.25rem; margin: 0; padding: 0; list-style: none; }
.sms-steps .sms-steps__item { position: relative; display: grid; grid-template-columns: 3.25rem minmax(0, 1fr); gap: 1rem; min-width: 0; }
.sms-steps .sms-steps__badge { position: relative; display: grid; place-items: center; min-width: 0; width: 3.25rem; height: 3.25rem; border-radius: 50%; background: var(--sms-green); color: var(--sms-white); box-shadow: 0 0 0 6px var(--sms-white); }
.sms-steps.sms-tone-pale .sms-steps__badge { box-shadow: 0 0 0 6px var(--sms-pale); }
.sms-steps .sms-steps__badge-icon { width: 1.4rem; height: 1.4rem; }
.sms-steps .sms-steps__num { position: absolute; right: -0.35rem; top: -0.35rem; display: grid; place-items: center; width: 1.4rem; height: 1.4rem; border-radius: 50%; background: var(--sms-navy); color: var(--sms-white); font-size: 0.75rem; font-weight: 700; }
.sms-steps .sms-steps__body { min-width: 0; padding: 0.35rem 0 0.5rem; }
.sms-steps .sms-steps__name { margin: 0 0 0.25rem; font-size: var(--sms-step-0); font-weight: 700; line-height: 1.35; }
.sms-steps .sms-steps__text { color: var(--sms-ink-soft); font-size: var(--sms-step--1); }
.sms-steps .sms-steps__text p { margin: 0; }
.sms-steps .sms-steps__note { display: flex; gap: 0.75rem; max-width: 48rem; margin-top: 2rem; padding: 1rem 1.25rem; border-radius: var(--sms-radius-sm); background: var(--sms-white); color: var(--sms-ink-soft); font-size: var(--sms-step--1); }
.sms-steps.sms-tone-white .sms-steps__note { background: var(--sms-pale); }
.sms-steps .sms-steps__note-icon { color: var(--sms-green); }
.sms-steps .sms-steps__note-text { min-width: 0; }
.sms-steps .sms-steps__note-text p { margin: 0; }
@media (min-width: 60em) {
  .sms-steps .sms-steps__line { left: 1.6rem; right: 1.6rem; top: 1.55rem; bottom: auto; width: auto; height: 3px; }
  .sms-steps .sms-steps__line-fill { transform-origin: left; }
  .sms-steps .sms-steps__list { grid-auto-columns: minmax(0, 1fr); grid-auto-flow: column; gap: 1.5rem; }
  .sms-steps .sms-steps__item { grid-template-columns: minmax(0, 1fr); gap: 1rem; }
}

/* ---------- Checklist (icon tiles) ---------- */
.sms-checklist .sms-checklist__inner { position: relative; }
.sms-checklist .sms-checklist__grid { display: grid; gap: 1rem; margin: 0; padding: 0; list-style: none; }
.sms-checklist .sms-checklist__item { display: flex; align-items: center; gap: 1rem; min-width: 0; padding: 1.25rem 1.5rem; border-radius: var(--sms-radius); background: var(--sms-pale); font-weight: 600; transition: transform 0.3s var(--sms-ease); }
.sms-checklist .sms-checklist__item:hover { transform: translateY(-4px); }
.sms-checklist .sms-checklist__icon { width: 3rem; height: 3rem; padding: 0.7rem; border-radius: 50%; background: var(--sms-white); color: var(--sms-green); }
.sms-checklist .sms-checklist__text { min-width: 0; }
@media (min-width: 52em) {
  .sms-checklist .sms-checklist__grid { grid-template-columns: repeat(3, minmax(0, 1fr)); }
}

/* ---------- Notice ---------- */
.sms-notice .sms-notice__box { display: grid; gap: 1.25rem; align-items: center; padding: clamp(1.5rem, 1rem + 2vw, 2.5rem); border-radius: var(--sms-radius); background: var(--sms-white); box-shadow: var(--sms-shadow); }
.sms-notice .sms-notice__badge { display: grid; place-items: center; min-width: 0; width: 4rem; height: 4rem; border-radius: 50%; background: var(--sms-mint); color: var(--sms-green); }
.sms-notice .sms-notice__badge-icon { width: 1.9rem; height: 1.9rem; }
.sms-notice .sms-notice__body { min-width: 0; }
.sms-notice .sms-notice__label { color: var(--sms-green); font-size: var(--sms-step--1); font-weight: 700; letter-spacing: 0.12em; text-transform: uppercase; }
.sms-notice .sms-notice__title { margin: 0.25rem 0 0.5rem; font-size: var(--sms-step-1); font-weight: 700; }
.sms-notice .sms-notice__text { color: var(--sms-ink-soft); }
.sms-notice .sms-notice__text p { margin: 0; }
.sms-notice .sms-notice__actions { display: flex; flex-wrap: wrap; gap: 0.75rem; min-width: 0; }
@media (min-width: 60em) {
  .sms-notice .sms-notice__box { grid-template-columns: auto minmax(0, 1fr) auto; }
}

/* ---------- FAQ ---------- */
.sms-faq .sms-faq__inner { display: grid; gap: clamp(2rem, 1.5rem + 2vw, 4rem); }
.sms-faq .sms-faq__head { min-width: 0; }
.sms-faq .sms-faq__search { position: relative; margin-top: 1.5rem; }
.sms-faq .sms-faq__search[hidden] { display: none; }
.sms-faq .sms-faq__search-label { display: block; margin-bottom: 0.4rem; font-size: var(--sms-step--1); font-weight: 700; }
.sms-faq .sms-faq__search-icon { position: absolute; left: 1rem; bottom: 0.85rem; width: 1.25rem; height: 1.25rem; color: var(--sms-ink-soft); }
.sms-faq .sms-faq__input { width: 100%; min-width: 0; padding: 0.85rem 1rem 0.85rem 2.9rem; border: 1px solid #8a99a6; border-radius: 999px; background: var(--sms-white); color: var(--sms-navy); font: inherit; }
.sms-faq .sms-faq__list { min-width: 0; }
.sms-faq .sms-faq__item { margin-bottom: 0.75rem; border-radius: var(--sms-radius-sm); background: var(--sms-white); box-shadow: 0 4px 16px rgba(6, 30, 53, 0.05); }
.sms-faq.sms-tone-white .sms-faq__item { background: var(--sms-pale); box-shadow: none; }
.sms-faq .sms-faq__item[hidden] { display: none; }
.sms-faq .sms-faq__q { position: relative; padding: 1.1rem 3.5rem 1.1rem 1.25rem; cursor: pointer; font-weight: 600; line-height: 1.4; list-style: none; }
.sms-faq .sms-faq__q::-webkit-details-marker { display: none; }
.sms-faq .sms-faq__q::after { content: "+"; position: absolute; right: 1rem; top: 50%; display: grid; place-items: center; width: 1.9rem; height: 1.9rem; margin-top: -0.95rem; border-radius: 50%; background: var(--sms-mint); color: var(--sms-green); font-size: 1.3rem; font-weight: 500; line-height: 1; transition: transform 0.3s var(--sms-ease); }
.sms-faq .sms-faq__item[open] .sms-faq__q::after { transform: rotate(45deg); }
.sms-faq .sms-faq__q:hover { color: var(--sms-green); }
.sms-faq .sms-faq__a { padding: 0 1.25rem 1.25rem; color: var(--sms-ink-soft); }
.sms-faq .sms-faq__item[open] .sms-faq__a { animation: sms-drop 0.4s var(--sms-ease) both; }
.sms-faq .sms-faq__a p { margin: 0 0 0.6rem; }
.sms-faq .sms-faq__a ul { margin: 0 0 0.6rem; padding-left: 1.25rem; }
.sms-faq .sms-faq__a li { margin-bottom: 0.25rem; }
.sms-faq .sms-faq__a a { color: var(--sms-green); font-weight: 600; }
.sms-faq .sms-faq__all-toggle { display: inline-flex; align-items: center; gap: 0.5rem; margin: 0.5rem 0 1rem; padding: 0.7rem 1.2rem; border: 2px solid var(--sms-navy); border-radius: 999px; cursor: pointer; font-size: var(--sms-step--1); font-weight: 700; list-style: none; }
.sms-faq .sms-faq__all-toggle::-webkit-details-marker { display: none; }
.sms-faq .sms-faq__all[open] > .sms-faq__all-toggle { display: none; }
.sms-faq .sms-faq__empty { padding: 1rem 0; color: var(--sms-ink-soft); }
.sms-faq .sms-faq__empty[hidden] { display: none; }
@media (min-width: 56em) {
  .sms-faq .sms-faq__inner { grid-template-columns: minmax(0, 0.8fr) minmax(0, 1.4fr); }
  .sms-faq .sms-faq__head { position: sticky; top: 7rem; align-self: start; }
}

/* ---------- Quotes ---------- */
.sms-quotes .sms-quotes__inner { position: relative; }
.sms-quotes .sms-quotes__grid { display: grid; gap: clamp(1rem, 0.6rem + 1.5vw, 1.75rem); }
.sms-quotes .sms-quotes__item { position: relative; min-width: 0; margin: 0; padding: clamp(1.75rem, 1.2rem + 2vw, 2.75rem); border-radius: var(--sms-radius); background: var(--sms-pale); }
.sms-quotes .sms-quotes__icon { width: 3rem; height: 3rem; margin-bottom: 1rem; padding: 0.7rem; border-radius: 1rem; background: var(--sms-white); color: var(--sms-green); }
.sms-quotes .sms-quotes__label { margin-bottom: 0.6rem; color: var(--sms-green); font-size: var(--sms-step--1); font-weight: 700; letter-spacing: 0.12em; text-transform: uppercase; }
.sms-quotes .sms-quotes__text { margin: 0; font-size: var(--sms-step-1); font-weight: 600; line-height: 1.5; }
.sms-quotes .sms-quotes__text p { margin: 0; }
@media (min-width: 52em) {
  .sms-quotes .sms-quotes__grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
}

/* ---------- People ---------- */
.sms-people .sms-people__inner { position: relative; }
.sms-people .sms-people__top { display: grid; gap: clamp(2rem, 1.5rem + 2vw, 3.5rem); align-items: center; margin-bottom: clamp(2rem, 1.5rem + 2vw, 3rem); }
.sms-people .sms-people__head { min-width: 0; margin-bottom: 0; }
.sms-people .sms-people__frame { aspect-ratio: 16 / 11; box-shadow: var(--sms-shadow-lg); }
.sms-people .sms-people__grid { display: grid; gap: clamp(1rem, 0.6rem + 1.5vw, 1.5rem); margin: 0; padding: 0; list-style: none; }
.sms-people .sms-people__person { min-width: 0; padding: clamp(1.5rem, 1.1rem + 1.5vw, 2.25rem); border-radius: var(--sms-radius); background: var(--sms-white); box-shadow: var(--sms-shadow); }
.sms-people.sms-tone-white .sms-people__person { background: var(--sms-pale); box-shadow: none; }
.sms-people .sms-people__role { display: inline-block; margin-bottom: 0.5rem; padding: 0.2rem 0.7rem; border-radius: 999px; background: var(--sms-mint); color: var(--sms-navy); font-size: var(--sms-step--1); font-weight: 700; }
.sms-people .sms-people__name { margin: 0 0 0.3rem; font-size: var(--sms-step-1); font-weight: 700; line-height: 1.3; }
.sms-people .sms-people__tags { margin-bottom: 0.9rem; color: var(--sms-green); font-size: var(--sms-step--1); font-weight: 600; }
.sms-people .sms-people__bio { color: var(--sms-ink-soft); }
.sms-people .sms-people__bio p { margin: 0; }
.sms-people .sms-people__shared { margin-top: clamp(1.5rem, 1rem + 2vw, 2.5rem); padding: clamp(1.5rem, 1rem + 2vw, 2.5rem); border-radius: var(--sms-radius); background: var(--sms-navy); color: var(--sms-white); }
.sms-people .sms-people__shared-label { color: var(--sms-green-on-navy); font-size: var(--sms-step--1); font-weight: 700; letter-spacing: 0.12em; text-transform: uppercase; }
.sms-people .sms-people__shared-title { margin: 0.4rem 0 0.75rem; font-size: var(--sms-step-1); font-weight: 700; }
.sms-people .sms-people__shared-text { color: rgba(255, 255, 255, 0.86); }
.sms-people .sms-people__shared-text p { margin: 0; }
.sms-people .sms-people__shared .sms-more__toggle { color: var(--sms-green-on-navy); }
.sms-people .sms-people__shared .sms-more__body { color: rgba(255, 255, 255, 0.86); }
@media (min-width: 52em) {
  .sms-people .sms-people__top { grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); }
  .sms-people .sms-people__grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
}

/* ---------- Links ---------- */
.sms-links .sms-links__grid { display: grid; gap: 1rem; margin: 0; padding: 0; list-style: none; }
.sms-links .sms-links__item { min-width: 0; }
.sms-links .sms-links__link { display: flex; flex-direction: column; gap: 0.6rem; height: 100%; padding: 1.75rem 1.5rem; border-radius: var(--sms-radius); background: var(--sms-white); box-shadow: var(--sms-shadow); color: var(--sms-navy); text-decoration: none; transition: transform 0.35s var(--sms-ease); }
.sms-links .sms-links__link:hover { transform: translateY(-6px); }
.sms-links .sms-links__icon { width: 3rem; height: 3rem; padding: 0.7rem; border-radius: 1rem; background: var(--sms-mint); color: var(--sms-green); }
.sms-links .sms-links__name { min-width: 0; font-size: var(--sms-step-1); font-weight: 700; }
.sms-links .sms-links__text { min-width: 0; color: var(--sms-ink-soft); font-size: var(--sms-step--1); }
.sms-links .sms-links__go { min-width: 0; margin-top: auto; color: var(--sms-green); font-size: var(--sms-step--1); font-weight: 700; }
@media (min-width: 46em) {
  .sms-links .sms-links__grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
}
@media (min-width: 64em) {
  .sms-links .sms-links__grid { grid-template-columns: repeat(4, minmax(0, 1fr)); }
}

/* ---------- Claim ---------- */
.sms-claim .sms-claim__inner { position: relative; text-align: center; }
.sms-claim .sms-claim__icon { width: 3.5rem; height: 3.5rem; margin-bottom: 1.25rem; padding: 0.8rem; border-radius: 50%; background: var(--sms-mint); color: var(--sms-green); }
.sms-claim.sms-tone-pale .sms-claim__icon { background: var(--sms-white); }
.sms-claim .sms-claim__text { max-width: 48rem; margin: 0 auto; font-size: var(--sms-step-2); font-weight: 700; line-height: 1.3; }
.sms-claim .sms-claim__text p { margin: 0; }

/* ---------- Marquee (who we work with) ---------- */
.sms-marquee .sms-marquee__inner { text-align: center; }
.sms-marquee .sms-marquee__viewport { overflow: hidden; margin-top: 1.5rem; -webkit-mask-image: linear-gradient(90deg, transparent, #000 8%, #000 92%, transparent); mask-image: linear-gradient(90deg, transparent, #000 8%, #000 92%, transparent); }
.sms-marquee .sms-marquee__track { display: flex; width: max-content; gap: 0.75rem; margin: 0; padding: 0.5rem 0; list-style: none; animation: sms-marquee 40s linear infinite; }
.sms-marquee .sms-marquee__viewport:hover .sms-marquee__track { animation-play-state: paused; }
.sms-marquee .sms-marquee__item { display: inline-flex; align-items: center; gap: 0.5rem; min-width: 0; padding: 0.7rem 1.2rem; border-radius: 999px; background: var(--sms-white); box-shadow: 0 4px 14px rgba(6, 30, 53, 0.06); font-weight: 600; white-space: nowrap; }
.sms-marquee.sms-tone-white .sms-marquee__item { background: var(--sms-pale); box-shadow: none; }
.sms-marquee .sms-marquee__icon { width: 1.1rem; height: 1.1rem; color: var(--sms-green); }

/* ---------- Contact ---------- */
.sms-contact .sms-contact__inner { display: grid; gap: clamp(2rem, 1.5rem + 3vw, 4rem); }
.sms-contact .sms-contact__info { min-width: 0; }
.sms-contact .sms-contact__text { color: var(--sms-ink-soft); }
.sms-contact .sms-contact__text p { margin: 0 0 1rem; }
.sms-contact .sms-contact__details { display: grid; gap: 0.75rem; margin: 1.5rem 0 0; padding: 0; list-style: none; }
.sms-contact .sms-contact__detail { display: flex; gap: 1rem; align-items: flex-start; min-width: 0; padding: 1.1rem 1.25rem; border-radius: var(--sms-radius); background: var(--sms-pale); transition: transform 0.3s var(--sms-ease); }
.sms-contact .sms-contact__detail:hover { transform: translateX(4px); }
.sms-contact .sms-contact__icon { width: 2.75rem; height: 2.75rem; padding: 0.65rem; border-radius: 50%; background: var(--sms-white); color: var(--sms-green); }
.sms-contact .sms-contact__detail-body { min-width: 0; }
.sms-contact .sms-contact__label { color: var(--sms-ink-soft); font-size: var(--sms-step--1); font-weight: 700; letter-spacing: 0.1em; text-transform: uppercase; }
.sms-contact .sms-contact__value { color: var(--sms-navy); font-size: var(--sms-step-1); font-weight: 700; text-decoration: none; overflow-wrap: anywhere; }
.sms-contact .sms-contact__value:hover { color: var(--sms-green); }
.sms-contact .sms-contact__small { color: var(--sms-ink-soft); font-size: var(--sms-step--1); }
.sms-contact .sms-contact__small p { margin: 0 0 0.4rem; }
.sms-contact .sms-contact__form { display: grid; gap: 1rem; align-content: start; min-width: 0; padding: clamp(1.5rem, 1rem + 2vw, 2.5rem); border-radius: var(--sms-radius); background: var(--sms-white); box-shadow: var(--sms-shadow-lg); }
.sms-contact .sms-contact__form-title { min-width: 0; margin: 0; font-size: var(--sms-step-1); font-weight: 700; }
.sms-contact .sms-contact__booklink { min-width: 0; padding: 1rem 1.25rem; border-radius: var(--sms-radius-sm); background: var(--sms-mint); font-size: var(--sms-step--1); }
.sms-contact .sms-contact__booklink p { margin: 0; }
.sms-contact .sms-contact__booklink a { color: var(--sms-navy); font-weight: 700; }
.sms-contact .sms-contact__field { display: grid; gap: 0.35rem; min-width: 0; }
.sms-contact .sms-contact__field-label { min-width: 0; font-size: var(--sms-step--1); font-weight: 600; }
.sms-contact .sms-contact__input { width: 100%; min-width: 0; padding: 0.85rem 1rem; border: 1px solid #8a99a6; border-radius: var(--sms-radius-sm); background: var(--sms-white); color: var(--sms-navy); font: inherit; }
.sms-contact .sms-contact__input--area { min-height: 8rem; resize: vertical; }
.sms-contact .sms-contact__row { display: grid; gap: 1rem; min-width: 0; }
.sms-contact .sms-contact__note { min-width: 0; color: var(--sms-ink-soft); font-size: var(--sms-step--1); }
.sms-contact .sms-contact__note p { margin: 0; }
.sms-contact .sms-contact__submit { justify-self: start; cursor: pointer; font: inherit; font-size: var(--sms-step--1); font-weight: 700; }
.sms-contact .sms-contact__status { min-width: 0; color: var(--sms-green); font-weight: 600; }
@media (min-width: 40em) {
  .sms-contact .sms-contact__row { grid-template-columns: repeat(2, minmax(0, 1fr)); }
}
@media (min-width: 60em) {
  .sms-contact .sms-contact__inner { grid-template-columns: minmax(0, 0.9fr) minmax(0, 1.1fr); }
}

/* ---------- Footer ---------- */
.sms-footer { padding: clamp(3rem, 2rem + 3vw, 4.5rem) 0 2.5rem; font-size: var(--sms-step--1); }
.sms-footer .sms-footer__inner { display: grid; gap: 2.5rem; }
.sms-footer .sms-footer__brand { min-width: 0; }
.sms-footer .sms-footer__logo { display: block; width: clamp(10.5rem, 8rem + 8vw, 13rem); height: auto; margin-bottom: 1.25rem; }
.sms-footer .sms-footer__tag { margin-bottom: 1.25rem; font-weight: 600; }
.sms-footer .sms-footer__badges { display: flex; flex-wrap: wrap; align-items: center; gap: 1rem; }
.sms-footer .sms-footer__badge-link { display: inline-block; min-width: 0; line-height: 0; transition: transform 0.3s var(--sms-ease); }
.sms-footer .sms-footer__badge-link:hover { transform: translateY(-3px); }
.sms-footer .sms-footer__badge { display: block; min-width: 0; height: auto; border-radius: 0.5rem; background: var(--sms-white); }
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

/* ---------- Keyframes (time-based; transform / opacity only) ---------- */
@keyframes sms-drop { from { opacity: 0; transform: translateY(-8px); } to { opacity: 1; transform: none; } }
@keyframes sms-pop { from { opacity: 0; transform: translateY(-6px) scale(0.97); } to { opacity: 1; transform: none; } }
@keyframes sms-float { 0%, 100% { transform: translate(0, 0) rotate(0deg); } 50% { transform: translate(-10px, -14px) rotate(6deg); } }
@keyframes sms-bob { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-8px); } }
@keyframes sms-spin { to { transform: rotate(360deg); } }
@keyframes sms-marquee { to { transform: translateX(-50%); } }
@keyframes sms-rise { from { transform: translateY(18px); } to { transform: none; } }
@keyframes sms-fade-up { from { opacity: 0; transform: translateY(18px); } to { opacity: 1; transform: none; } }
@keyframes sms-zoom { from { transform: scale(1.08); } to { transform: scale(1); } }
@keyframes sms-slide-in { from { opacity: 0; transform: translateX(24px); } to { opacity: 1; transform: none; } }
@keyframes sms-tick { 0% { opacity: 0; transform: scale(0.4); } 60% { opacity: 1; transform: scale(1.12); } 100% { opacity: 1; transform: scale(1); } }
"""

REVEAL_SELECTORS = [
    ".sms-feature .sms-feature__media", ".sms-feature .sms-feature__main",
    ".sms-cards .sms-cards__head", ".sms-cards .sms-cards__item",
    ".sms-steps .sms-steps__head", ".sms-steps .sms-steps__item",
    ".sms-checklist .sms-checklist__head", ".sms-checklist .sms-checklist__item", ".sms-notice .sms-notice__box",
    ".sms-faq .sms-faq__head", ".sms-faq .sms-faq__list",
    ".sms-quotes .sms-quotes__item", ".sms-people .sms-people__top",
    ".sms-people .sms-people__person", ".sms-people .sms-people__shared",
    ".sms-links .sms-links__item", ".sms-claim .sms-claim__inner",
    ".sms-contact .sms-contact__info", ".sms-contact .sms-contact__form",
    ".sms-marquee .sms-marquee__inner", ".sms-booking .sms-booking__inner",
    ".sms-footer .sms-footer__inner",
]
STAGGER_PARENTS = [".sms-cards .sms-cards__item", ".sms-steps .sms-steps__item", ".sms-checklist .sms-checklist__item",
                   ".sms-links .sms-links__item", ".sms-quotes .sms-quotes__item", ".sms-people .sms-people__person"]
LOOP_SELECTORS = [".sms-feature .sms-feature__blob", ".sms-feature .sms-watermark", ".sms-cards .sms-watermark",
                  ".sms-steps .sms-watermark", ".sms-quotes .sms-watermark", ".sms-people .sms-watermark",
                  ".sms-claim .sms-watermark", ".sms-checklist .sms-watermark", ".sms-marquee .sms-marquee__track"]
TRANSITION_SELECTORS = [".sms-page .sms-btn", ".sms-page .sms-arrow", ".sms-page .sms-chips__item", ".sms-page .sms-more__icon",
                        ".sms-header .sms-header__logo", ".sms-header .sms-header__link::after", ".sms-cards .sms-cards__item",
                        ".sms-cards .sms-cards__icon", ".sms-checklist .sms-checklist__item", ".sms-faq .sms-faq__q::after",
                        ".sms-links .sms-links__link", ".sms-contact .sms-contact__detail", ".sms-footer .sms-footer__badge-link"]
OPEN_ANIM = [".sms-page .sms-more[open] .sms-more__body", ".sms-faq .sms-faq__item[open] .sms-faq__a",
             ".sms-header .sms-header__menu[open] .sms-header__panel"]


def motion_css(reveal_extra, rise_selectors, entrance_selectors, loop_extra, transition_extra, open_extra=()):
    rev = REVEAL_SELECTORS + list(reveal_extra)
    css = "\n/* ---------- Scroll-driven motion (progressive) ---------- */\n"
    css += "@supports (animation-timeline: view()) {\n"
    css += "  @keyframes sms-reveal {\n    from { opacity: 0; transform: translateY(36px) scale(0.98); }\n    to { opacity: 1; transform: none; }\n  }\n"
    css += "  @keyframes sms-parallax {\n    from { transform: scale(1.14) translateY(-4%); }\n    to { transform: scale(1.14) translateY(4%); }\n  }\n"
    css += "  @keyframes sms-grow-x { from { transform: scaleX(0); } to { transform: scaleX(1); } }\n"
    css += "  @keyframes sms-grow-y { from { transform: scaleY(0); } to { transform: scaleY(1); } }\n"
    css += "  " + ",\n  ".join(rev) + " {\n"
    css += "    animation: sms-reveal linear both;\n    animation-timeline: view();\n    animation-range: entry 0% entry 85%;\n  }\n"
    for n, start in [(2, 8), (3, 16), (4, 24), (5, 30), (6, 36)]:
        css += "  " + ",\n  ".join("%s:nth-child(6n+%d)" % (s, n) for s in STAGGER_PARENTS) + " { animation-range: entry %d%% entry 100%%; }\n" % start
    css += "  .sms-page .sms-parallax {\n    animation: sms-parallax linear both;\n    animation-timeline: view();\n    animation-range: cover 0% cover 100%;\n  }\n"
    css += "  .sms-steps .sms-steps__line-fill {\n    animation: sms-grow-y linear both;\n    animation-timeline: view();\n    animation-range: entry 10% cover 55%;\n  }\n"
    css += "  @media (min-width: 60em) {\n    .sms-steps .sms-steps__line-fill { animation-name: sms-grow-x; }\n  }\n"
    css += "}\n"
    css += "\n/* ---------- Hero entrance (LCP elements: transform only) ---------- */\n"
    css += ",\n".join(rise_selectors) + " { animation: sms-rise 0.9s var(--sms-ease) both; }\n"
    for i, sel in enumerate(entrance_selectors):
        css += "%s { animation: sms-fade-up 0.8s var(--sms-ease) %.2fs both; }\n" % (sel, 0.15 + i * 0.12)
    css += "\n/* ---------- Reduced motion ---------- */\n@media (prefers-reduced-motion: reduce) {\n"
    allanim = rev + list(rise_selectors) + list(entrance_selectors) + LOOP_SELECTORS + list(loop_extra) + [".sms-page .sms-parallax", ".sms-steps .sms-steps__line-fill"] + OPEN_ANIM + list(open_extra)
    css += "  " + ",\n  ".join(allanim) + " {\n    animation: none;\n    animation-timeline: none;\n  }\n"
    css += "  " + ",\n  ".join(TRANSITION_SELECTORS + list(transition_extra)) + " { transition: none; }\n"
    css += "  .sms-marquee .sms-marquee__track { flex-wrap: wrap; justify-content: center; width: auto; }\n"
    css += "  .sms-marquee .sms-marquee__item--dup { display: none; }\n"
    css += "}\n"
    return css


# ---------------------------------------------------------------------------
# Page shell
# ---------------------------------------------------------------------------

def head(ctx, title, description, css):
    return """<!doctype html>
%%COMMENT%%
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>""" + html.escape(title, quote=False) + """</title>
<meta name="description" content=\"""" + attr(description) + """\">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700&amp;display=swap">
<style>""" + css + """</style>
</head>
"""


def topbar(ctx, text):
    return """<div class="sms-topbar">
  <div class="sms-topbar__inner">
    <div class="sms-topbar__text">%s</div>
    <div class="sms-topbar__links">
      <a class="sms-topbar__link" href="tel:%s">%s%s</a>
      <a class="sms-topbar__link" href="mailto:%s">%s%s</a>
    </div>
  </div>
</div>
""" % (e(text), PHONE_TEL, icon("phone", "sms-topbar__icon"), PHONE, EMAIL, icon("mail", "sms-topbar__icon"), EMAIL)


PANEL_ICONS = {"home": "star", "event-medical-cover": "heart", "medical-training": "cap", "risk-needs-consultancy": "clipboard",
               "pre-hospital-career-support": "compass", "recruitment": "users", "about": "shield", "contact": "mail", "book": "calendar"}


def header(ctx, logo="blue", cta=None):
    cur = lambda s: ' aria-current="page"' if s == ctx.slug else ""
    items = "".join('<li class="sms-header__item"><a class="sms-header__link" href="%s"%s>%s</a></li>' % (ctx.href(s), cur(s), e(LABEL[s])) for s in MAIN_NAV)
    panel = ""
    for s in ["home"] + [p for p, _ in PAGES]:
        panel += '<li class="sms-header__panel-item"><a class="sms-header__panel-link" href="%s"%s>%s%s</a></li>' % (ctx.href(s), cur(s), icon(PANEL_ICONS[s], "sms-header__panel-icon"), e(LABEL[s]))
    panel += '<li class="sms-header__panel-item" aria-hidden="true"><div class="sms-header__panel-sep"></div></li>'
    panel += '<li class="sms-header__panel-item"><a class="sms-header__panel-link" href="tel:%s">%sCall %s</a></li>' % (PHONE_TEL, icon("phone", "sms-header__panel-icon"), PHONE)
    if cta is None:
        cta = '<a class="sms-btn sms-btn--primary sms-header__cta" href="%s">Book online&nbsp;<span class="sms-arrow" aria-hidden="true">&rarr;</span></a>' % ctx.href("book")
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
    more_l = "".join('<li class="sms-footer__list-item"><a class="sms-footer__link" href="%s">%s</a></li>' % (ctx.href(s), e(LABEL[s])) for s in ["home", "about", "recruitment", "contact", "book"])
    more_l += '<li class="sms-footer__list-item"><a class="sms-footer__link" href="%s/privacy-policy">Our Privacy Policy</a></li>' % SITE
    more_l += '<li class="sms-footer__list-item"><a class="sms-footer__link" href="%s/staff-portal">Staff Portal</a></li>' % SITE
    return """<footer class="sms-footer">
  <div class="sms-footer__inner">
    <div class="sms-footer__brand">
      <img class="sms-footer__logo" src="%s" alt="Streamline Safety &amp; Medical Solutions" width="2500" height="443" loading="lazy">
      <div class="sms-footer__tag">Protecting People. Supporting Business.</div>
      <div class="sms-footer__badges">
        <span class="sms-footer__badge-link"><img class="sms-footer__badge sms-footer__badge--qualsafe" src="%s" alt="Qualsafe registered centre" width="1000" height="982" loading="lazy"></span>
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
       ctx.asset("featured-landscape-purple-medium.png"), svc, more_l, PHONE_TEL, PHONE, EMAIL, EMAIL)


# ---------------------------------------------------------------------------
# Section renderers
# ---------------------------------------------------------------------------

def r_feature(ctx, d):
    body = d["body"]
    lead, rest = body[0], body[1:]
    strap = '<div class="sms-feature__strap">%s%s</div>' % (icon("shield", "sms-feature__strap-icon"), e(d["strap"])) if d.get("strap") else ""
    ch = ""
    if d.get("chips"):
        ch = '<h3 class="sms-feature__chips-title">%s</h3>%s' % (e(d["chips_title"]), chips(d["chips"]))
    acts = '<div class="sms-feature__actions">%s</div>' % buttons(ctx, d["buttons"]) if d.get("buttons") else ""
    wm = watermark(ctx) if d.get("watermark") else ""
    flip = " sms-feature--flip" if d.get("flip") else ""
    return """<section class="sms-feature%s%s"%s>
  %s
  <div class="sms-feature__inner">
    <div class="sms-feature__media"><div class="sms-feature__blob" aria-hidden="true"></div>%s</div>
    <div class="sms-feature__main">
      %s
      <div class="sms-feature__lead"><p>%s</p></div>
      %s
      %s
      %s
      %s
    </div>
  </div>
</section>
""" % (flip, tone(d), sid(d), wm, photo(ctx, d["photo"], figcls="sms-feature__frame"), head_block("feature", d), e(lead), more(paras(rest)), strap, ch, acts)


def r_cards(ctx, d):
    cols = d.get("cols", 3)
    items = []
    for i, it in enumerate(d["items"], 1):
        top = '<div class="sms-cards__top">%s%s</div>' % (
            icon(it.get("icon", "check"), "sms-cards__icon"),
            '<span class="sms-cards__num" aria-hidden="true">%02d</span>' % i if d.get("numbered") else "")
        h = top + '<h3 class="sms-cards__name">%s</h3>' % e(it["title"])
        if it.get("meta"):
            h += '<div class="sms-cards__meta">%s%s</div>' % (icon("clock", "sms-cards__meta-icon"), e(it["meta"]))
        hidden = ""
        if it.get("text"):
            first, rest = split_first(it["text"])
            if d.get("compact") and not rest:
                h += '<div class="sms-cards__text"><p>%s</p></div>' % e(it["text"])
            else:
                h += '<div class="sms-cards__text"><p>%s</p></div>' % e(first)
                if rest:
                    hidden += "<p>%s</p>" % e(rest)
        if it.get("list"):
            hidden += '<div class="sms-cards__list-title">%s</div><ul class="sms-cards__list">%s</ul>' % (
                e(it.get("list_title", "")), "".join('<li class="sms-cards__list-item">%s<span>%s</span></li>' % (icon("check", "sms-cards__check"), e(x)) for x in it["list"]))
        label = it.get("list_title") if it.get("list") else "Read more"
        h += more(hidden, e(label) if label else "Read more")
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
    items = []
    for i, it in enumerate(d["items"], 1):
        txt = ""
        if it.get("text"):
            first, rest = split_first(it["text"])
            txt = '<div class="sms-steps__text"><p>%s</p></div>%s' % (e(first), more("<p>%s</p>" % e(rest)) if rest else "")
        items.append('<li class="sms-steps__item"><div class="sms-steps__badge">%s<span class="sms-steps__num" aria-hidden="true">%d</span></div><div class="sms-steps__body"><h3 class="sms-steps__name">%s</h3>%s</div></li>' % (
            icon(it.get("icon", "check"), "sms-steps__badge-icon"), i, e(it["title"]), txt))
    note = '<div class="sms-steps__note">%s<div class="sms-steps__note-text">%s</div></div>' % (icon("alert", "sms-steps__note-icon"), paras(d["note"])) if d.get("note") else ""
    wm = watermark(ctx) if d.get("watermark") else ""
    return """<section class="sms-steps%s"%s>
  %s
  <div class="sms-steps__inner">
    <div class="sms-steps__head">%s</div>
    <div class="sms-steps__track">
      <div class="sms-steps__line" aria-hidden="true"><span class="sms-steps__line-fill"></span></div>
      <ol class="sms-steps__list">%s</ol>
    </div>
    %s
  </div>
</section>
""" % (tone(d), sid(d), wm, head_block("steps", d), "".join(items), note)


def r_checklist(ctx, d):
    items = "".join('<li class="sms-checklist__item">%s<span class="sms-checklist__text">%s</span></li>' % (icon(i, "sms-checklist__icon"), e(t)) for i, t in d["items"])
    return """<section class="sms-checklist%s"%s>
  <div class="sms-checklist__inner">
    <div class="sms-checklist__head">%s</div>
    <ul class="sms-checklist__grid">%s</ul>
  </div>
</section>
""" % (tone(d), sid(d), head_block("checklist", d), items)


def r_notice(ctx, d):
    acts = '<div class="sms-notice__actions">%s</div>' % buttons(ctx, d["buttons"]) if d.get("buttons") else ""
    return """<section class="sms-notice%s"%s>
  <div class="sms-notice__inner">
    <div class="sms-notice__box">
      <div class="sms-notice__badge">%s</div>
      <div class="sms-notice__body">
        <div class="sms-notice__label">%s</div>
        <h2 class="sms-notice__title">%s</h2>
        <div class="sms-notice__text">%s</div>
      </div>
      %s
    </div>
  </div>
</section>
""" % (tone(d), sid(d), icon("calendar", "sms-notice__badge-icon"), e(d["label"]), e(d["title"]), paras(d["text"]), acts)


def r_faq(ctx, d):
    show = d.get("show", 5)
    rendered = []
    for q, a in d["items"]:
        a = a.replace(SITE + "/contact-us", ctx.href("contact"))
        rendered.append('<details class="sms-faq__item" data-sms-faq-item><summary class="sms-faq__q">%s</summary><div class="sms-faq__a">%s</div></details>' % (e(q), a))
    first, rest = rendered[:show], rendered[show:]
    rest_html = ""
    if rest:
        rest_html = '<details class="sms-faq__all" data-sms-faq-all><summary class="sms-faq__all-toggle">Show all %d questions %s</summary>%s</details>' % (
            len(rendered), icon("plus", "sms-more__icon"), "".join(rest))
    search = ""
    if d.get("search", True) and len(rendered) > show:
        search = """<div class="sms-faq__search" hidden data-sms-faq-search>
        <label class="sms-faq__search-label" for="sms-faq-q">Search these questions</label>
        %s<input class="sms-faq__input" id="sms-faq-q" type="search" placeholder="Type a word, e.g. FREC" autocomplete="off">
      </div>""" % icon("search", "sms-faq__search-icon")
    return """<section class="sms-faq%s"%s>
  <div class="sms-faq__inner">
    <div class="sms-faq__head">%s%s</div>
    <div class="sms-faq__list" data-sms-faq>%s%s<div class="sms-faq__empty" hidden data-sms-faq-empty>No questions match that search. Try another word, or call us on %s.</div></div>
  </div>
</section>
""" % (tone(d), sid(d), head_block("faq", d), search, "".join(first), rest_html, PHONE)


def r_quotes(ctx, d):
    items = "".join('<figure class="sms-quotes__item">%s<div class="sms-quotes__label">%s</div><blockquote class="sms-quotes__text"><p>%s</p></blockquote></figure>' % (
        icon(it.get("icon", "quote"), "sms-quotes__icon"), e(it["label"]), e(it["text"])) for it in d["items"])
    return """<section class="sms-quotes%s"%s>
  <div class="sms-quotes__inner"><div class="sms-quotes__grid">%s</div></div>
</section>
""" % (tone(d), sid(d), items)


def r_people(ctx, d):
    ppl = []
    for p in d["items"]:
        first, rest = split_first(p["bio"][0])
        hidden = ("<p>%s</p>" % e(rest) if rest else "") + paras(p["bio"][1:])
        ppl.append('<li class="sms-people__person"><div class="sms-people__role">Director</div><h3 class="sms-people__name">%s</h3><div class="sms-people__tags">%s</div><div class="sms-people__bio"><p>%s</p></div>%s</li>' % (
            e(p["name"]), e(p["tags"]), e(first), more(hidden)))
    shared = ""
    if d.get("shared"):
        s = d["shared"]
        shared = '<div class="sms-people__shared"><div class="sms-people__shared-label">%s</div><h3 class="sms-people__shared-title">%s</h3><div class="sms-people__shared-text"><p>%s</p></div>%s</div>' % (
            e(s["label"]), e(s["title"]), e(s["text"][0]), more(paras(s["text"][1:])))
    ph = photo(ctx, d["photo"], figcls="sms-people__frame") if d.get("photo") else ""
    return """<section class="sms-people%s"%s>
  <div class="sms-people__inner">
    <div class="sms-people__top"><div class="sms-people__head">%s</div>%s</div>
    <ul class="sms-people__grid">%s</ul>
    %s
  </div>
</section>
""" % (tone(d), sid(d), head_block("people", d), ph, "".join(ppl), shared)


def r_links(ctx, d):
    items = "".join('<li class="sms-links__item"><a class="sms-links__link" href="%s">%s<span class="sms-links__name">%s</span><span class="sms-links__text">%s</span><span class="sms-links__go">%s&nbsp;<span class="sms-arrow" aria-hidden="true">&rarr;</span></span></a></li>' % (
        link(ctx, it["link"]), icon(it.get("icon", "arrow"), "sms-links__icon"), e(it["title"]), e(it["text"]), e(it["go"])) for it in d["items"])
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
        ctx.notes.append("Image-only copy used: " + d["image_text"])
    return """<section class="sms-claim%s"%s>
  %s
  <div class="sms-claim__inner">%s<div class="sms-claim__text"><p>%s</p></div></div>
</section>
""" % (tone(d), sid(d), wm, icon("heart", "sms-claim__icon"), e(d["text"]))


def r_marquee(ctx, d):
    items = "".join('<li class="sms-marquee__item">%s%s</li>' % (icon("check", "sms-marquee__icon"), e(w)) for w in d["items"])
    dup = "".join('<li class="sms-marquee__item sms-marquee__item--dup" aria-hidden="true">%s%s</li>' % (icon("check", "sms-marquee__icon"), e(w)) for w in d["items"])
    return """<section class="sms-marquee%s"%s>
  <div class="sms-marquee__inner">
    %s
    <div class="sms-marquee__viewport"><ul class="sms-marquee__track">%s%s</ul></div>
  </div>
</section>
""" % (tone(d), sid(d), head_block("marquee", d), items, dup)


def r_contact(ctx, d):
    opts = "".join('<option>%s</option>' % e(o) for o in ["General enquiry", "Event Medical Cover", "Medical Training", "Risk & Needs Consultancy", "Pre-Hospital Career Support", "Recruitment"])
    form = """<form class="sms-contact__form" action="#" method="post" data-sms-form>
      <h3 class="sms-contact__form-title">%s</h3>
      <div class="sms-contact__booklink"><p>Booking cover, training or a consultation? <a href="%s">Try the online booking form&nbsp;<span class="sms-arrow" aria-hidden="true">&rarr;</span></a></p></div>
      <div class="sms-contact__row">
        <div class="sms-contact__field"><label class="sms-contact__field-label" for="sms-f-name">Name</label><input class="sms-contact__input" id="sms-f-name" name="name" type="text" autocomplete="name"></div>
        <div class="sms-contact__field"><label class="sms-contact__field-label" for="sms-f-phone">Telephone</label><input class="sms-contact__input" id="sms-f-phone" name="phone" type="tel" autocomplete="tel"></div>
      </div>
      <div class="sms-contact__field"><label class="sms-contact__field-label" for="sms-f-email">Email</label><input class="sms-contact__input" id="sms-f-email" name="email" type="email" autocomplete="email"></div>
      <div class="sms-contact__field"><label class="sms-contact__field-label" for="sms-f-topic">What is your enquiry about?</label><select class="sms-contact__input" id="sms-f-topic" name="topic">%s</select></div>
      <div class="sms-contact__field"><label class="sms-contact__field-label" for="sms-f-msg">Message</label><textarea class="sms-contact__input sms-contact__input--area" id="sms-f-msg" name="message"></textarea></div>
      <div class="sms-contact__note"><p>Concept only: this form is not connected yet.</p></div>
      <button class="sms-btn sms-btn--primary sms-contact__submit" type="submit" disabled>Send enquiry&nbsp;<span class="sms-arrow" aria-hidden="true">&rarr;</span></button>
      <div class="sms-contact__status" role="status" aria-live="polite"></div>
    </form>""" % (e(d.get("form_title", "Use our form below to contact us")), ctx.href("book"), opts)
    ctx.notes.append("Contact form is a concept and is not connected")
    return """<section class="sms-contact%s"%s>
  <div class="sms-contact__inner">
    <div class="sms-contact__info">
      %s
      <div class="sms-contact__text">%s</div>
      <ul class="sms-contact__details">
        <li class="sms-contact__detail">%s<div class="sms-contact__detail-body"><div class="sms-contact__label">Telephone</div><a class="sms-contact__value" href="tel:%s">%s</a></div></li>
        <li class="sms-contact__detail">%s<div class="sms-contact__detail-body"><div class="sms-contact__label">Email</div><a class="sms-contact__value" href="mailto:%s">%s</a></div></li>
        <li class="sms-contact__detail">%s<div class="sms-contact__detail-body"><div class="sms-contact__label">Registered Office</div><div class="sms-contact__small"><p>8 Cobblestone Drive, Swadlincote, Derbyshire, DE11 0FL</p><p>Please note: This is our registered office address for official correspondence only and is not open to visitors or walk-in enquiries.</p></div></div></li>
      </ul>
    </div>
    %s
  </div>
</section>
""" % (tone(d), sid(d), head_block("contact", d), paras(d.get("body", [])),
       icon("phone", "sms-contact__icon"), PHONE_TEL, PHONE, icon("mail", "sms-contact__icon"), EMAIL, EMAIL, icon("pin", "sms-contact__icon"), form)


FORM_JS = """<script>
(function () {
  Array.prototype.forEach.call(document.querySelectorAll('[data-sms-form]'), function (form) {
    var btn = form.querySelector('[type="submit"]');
    if (btn) btn.disabled = false;
    form.addEventListener('submit', function (ev) {
      ev.preventDefault();
      var status = form.querySelector('[role="status"]');
      if (status) status.textContent = 'Thanks - this is a concept, so nothing has been sent. Please call 01283 358789 or email hello@streamlinesms.co.uk.';
    });
  });
})();
</script>
"""

FAQ_JS = """<script>
(function () {
  Array.prototype.forEach.call(document.querySelectorAll('[data-sms-faq-search]'), function (box) {
    var section = box.closest('section');
    var input = box.querySelector('input');
    var items = section.querySelectorAll('[data-sms-faq-item]');
    var all = section.querySelector('[data-sms-faq-all]');
    var empty = section.querySelector('[data-sms-faq-empty]');
    box.hidden = false;
    input.addEventListener('input', function () {
      var q = input.value.trim().toLowerCase();
      var shown = 0;
      if (all && q) all.open = true;
      Array.prototype.forEach.call(items, function (it) {
        var hit = !q || it.textContent.toLowerCase().indexOf(q) !== -1;
        it.hidden = !hit;
        if (hit) shown++;
      });
      if (empty) empty.hidden = shown !== 0;
    });
  });
})();
</script>
"""

SHARED_RENDERERS = {
    "feature": r_feature, "cards": r_cards, "steps": r_steps, "checklist": r_checklist,
    "notice": r_notice, "faq": r_faq, "quotes": r_quotes, "people": r_people,
    "links": r_links, "claim": r_claim, "contact": r_contact, "marquee": r_marquee,
}


def comment(concept, name, slug, ctx):
    lines = ["  Streamline Safety & Medical Solutions - Concept %d (%s): %s" % (concept, name, "Home" if slug == "home" else LABEL[slug]),
             "  Pitch concept by CADS. Not production code. Built for porting to WordPress / Elementor.",
             "  Generated by build/build.py from build/content.py - edit those, then rebuild.",
             "",
             "  PHOTOS ON THIS PAGE: the client's own images from the live site, cropped. Most",
             "  appear AI-generated or AI-edited - replace with genuine photography before launch."]
    seen = []
    for p in ctx.photos:
        if p not in seen:
            seen.append(p)
    lines += ["  - " + p for p in seen] or ["  - none"]
    lines += ["", "  NOTES / COPY TO CONFIRM"]
    it = []
    for t in ctx.notes:
        if t not in it:
            it.append(t)
    lines += ["  - " + t for t in it] or ["  - none"]
    lines += ["", "  No statistics, reviews, response times or accreditations have been invented.",
              "  All other copy is from reference/content.md / the live site."]
    return "<!--\n" + "\n".join(lines) + "\n-->"
