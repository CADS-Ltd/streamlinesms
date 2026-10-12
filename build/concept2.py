"""Concept 2 - Centred statement, friendly. Light, rounded and welcoming: centred pale-green
heroes with floating bubbles and a photo collage, photo service cards, green CTA bands."""
from common import *  # noqa: F401,F403
import content as C

NAME = "Centred statement"

SECOND = {"home": "cpr-outdoor", "event-medical-cover": "stall", "medical-training": "cpr-outdoor", "risk-needs-consultancy": "jacket",
          "pre-hospital-career-support": "cpr-outdoor", "recruitment": "stall", "about": "team", "contact": "directors", "book": "festival"}

CSS = r"""
/* ===== Concept 2 theme ===== */
.sms-page { --sms-radius: 1.5rem; }
.sms-page .sms-mark { color: var(--sms-green); }
.sms-cards .sms-cards__head,
.sms-steps .sms-steps__head,
.sms-people .sms-people__head,
.sms-links .sms-links__head,
.sms-checklist .sms-checklist__head { margin-left: auto; margin-right: auto; text-align: center; }
.sms-cards .sms-cards__item { text-align: center; align-items: center; }
.sms-cards .sms-cards__top { justify-content: center; }
.sms-cards .sms-cards__meta { align-self: center; }
.sms-cards .sms-cards__icon { width: 4rem; height: 4rem; padding: 0.95rem; border-radius: 50%; }
.sms-cards .sms-cards__list { text-align: left; }
.sms-cards .sms-cards__num { display: none; }

/* Footer: light */
.sms-footer { border-top: 1px solid var(--sms-line-green); background: var(--sms-pale); color: var(--sms-navy); }
.sms-footer .sms-footer__link { color: var(--sms-navy); }
.sms-footer .sms-footer__link:hover { color: var(--sms-green); }
.sms-footer .sms-footer__heading { color: var(--sms-green); }
.sms-footer .sms-footer__base { border-color: var(--sms-line-green); color: var(--sms-ink-soft); }
.sms-footer .sms-footer__badge { border: 1px solid var(--sms-line); }

/* ---------- Page hero (centred, light, collage) ---------- */
.sms-phero { position: relative; }
.sms-phero .sms-phero__band { position: relative; z-index: 0; overflow: hidden; padding: clamp(3rem, 2rem + 4vw, 5.5rem) 0 clamp(9rem, 6rem + 12vw, 16rem); background: var(--sms-pale); text-align: center; }
.sms-phero .sms-phero__bubble { position: absolute; z-index: -1; border-radius: 50%; background: var(--sms-mint); animation: sms-float 12s ease-in-out infinite; }
.sms-phero .sms-phero__bubble--a { left: -4rem; top: 3rem; width: 14rem; height: 14rem; }
.sms-phero .sms-phero__bubble--b { right: 6%; top: -3rem; width: 9rem; height: 9rem; animation-delay: -4s; }
.sms-phero .sms-phero__bubble--c { right: -3rem; bottom: 4rem; width: 6rem; height: 6rem; background: var(--sms-white); animation-delay: -7s; }
.sms-phero .sms-phero__inner { position: relative; width: 100%; max-width: 54rem; margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-phero .sms-phero__crumb { margin-bottom: 1.25rem; color: var(--sms-ink-soft); font-size: var(--sms-step--1); }
.sms-phero .sms-phero__crumb-link { color: var(--sms-ink-soft); }
.sms-phero .sms-phero__eyebrow { display: inline-flex; align-items: center; gap: 0.5rem; margin-bottom: 1.25rem; padding: 0.45rem 1rem 0.45rem 0.5rem; border-radius: 999px; background: var(--sms-white); color: var(--sms-green); font-size: var(--sms-step--1); font-weight: 700; box-shadow: 0 6px 18px rgba(6, 30, 53, 0.06); }
.sms-phero .sms-phero__eyebrow-icon { width: 1.6rem; height: 1.6rem; padding: 0.3rem; border-radius: 50%; background: var(--sms-mint); }
.sms-phero .sms-phero__title { margin: 0 auto 1.25rem; font-size: var(--sms-step-3); font-weight: 700; line-height: 1.08; letter-spacing: -0.025em; }
.sms-phero .sms-phero__sub { margin-bottom: 0.75rem; font-size: var(--sms-step-1); font-weight: 600; }
.sms-phero .sms-phero__body { max-width: 40rem; margin: 0 auto; color: var(--sms-ink-soft); font-size: var(--sms-step-1); line-height: 1.6; }
.sms-phero .sms-phero__body p { margin: 0 0 0.6rem; }
.sms-phero .sms-phero__actions { display: flex; flex-wrap: wrap; justify-content: center; gap: 0.75rem; margin-top: 2rem; }
.sms-phero .sms-phero__collage { position: relative; z-index: 1; width: 100%; max-width: var(--sms-max); margin: clamp(-13rem, -5rem - 9vw, -7rem) auto 0; padding: 0 var(--sms-gutter); }
.sms-phero .sms-phero__main { aspect-ratio: 16 / 7; border-radius: 2rem; box-shadow: var(--sms-shadow-lg); }
.sms-phero .sms-phero__main .sms-photo__img { animation: sms-zoom 1.4s var(--sms-ease) both; }
.sms-phero .sms-phero__second { position: absolute; z-index: 2; right: calc(var(--sms-gutter) + 1.5rem); bottom: -2.5rem; width: clamp(7rem, 5rem + 9vw, 13rem); aspect-ratio: 1; border: 6px solid var(--sms-white); border-radius: 50%; box-shadow: var(--sms-shadow-lg); animation: sms-bob 6s ease-in-out infinite; }
.sms-phero .sms-phero__chips { position: absolute; z-index: 2; left: calc(var(--sms-gutter) + 1.25rem); bottom: -1.5rem; display: flex; flex-wrap: wrap; gap: 0.5rem; max-width: 60%; }
.sms-phero .sms-phero__chip { display: inline-flex; align-items: center; gap: 0.5rem; min-width: 0; padding: 0.6rem 1rem 0.6rem 0.6rem; border-radius: 999px; background: var(--sms-white); box-shadow: var(--sms-shadow-lg); font-size: var(--sms-step--1); font-weight: 700; animation: sms-bob 5s ease-in-out infinite; }
.sms-phero .sms-phero__chip:nth-child(2) { animation-delay: -2.5s; }
.sms-phero .sms-phero__chip-icon { width: 2rem; height: 2rem; padding: 0.4rem; border-radius: 50%; background: var(--sms-mint); color: var(--sms-green); }
.sms-phero .sms-phero__chip-text { min-width: 0; }
.sms-phero .sms-phero__spacer { height: clamp(3rem, 2rem + 3vw, 4.5rem); }
@media (max-width: 47.99em) {
  .sms-phero .sms-phero__chips { position: static; max-width: none; margin-top: 1rem; }
  .sms-phero .sms-phero__chip { animation: none; }
  .sms-phero .sms-phero__second { right: calc(var(--sms-gutter) + 0.75rem); bottom: auto; top: -2.5rem; width: 6rem; border-width: 4px; }
  .sms-phero .sms-phero__spacer { height: 2rem; }
}

/* ---------- CTA band (green, centred) ---------- */
.sms-cta { position: relative; z-index: 0; overflow: hidden; padding: clamp(3.5rem, 2.5rem + 4vw, 6rem) 0; background: var(--sms-green); color: var(--sms-white); text-align: center; }
.sms-cta .sms-cta__bubble { position: absolute; z-index: -1; border-radius: 50%; background: rgba(255, 255, 255, 0.1); animation: sms-float 12s ease-in-out infinite; }
.sms-cta .sms-cta__bubble--a { left: -3rem; bottom: -4rem; width: 14rem; height: 14rem; }
.sms-cta .sms-cta__bubble--b { right: 8%; top: -2rem; width: 8rem; height: 8rem; animation-delay: -5s; }
.sms-cta .sms-cta__wm { display: block; width: 4.5rem; height: auto; margin: 0 auto 1.25rem; animation: sms-bob 5s ease-in-out infinite; }
.sms-cta .sms-cta__inner { position: relative; }
.sms-cta .sms-cta__title { max-width: 40rem; margin: 0 auto 0.75rem; font-size: var(--sms-step-2); font-weight: 700; line-height: 1.2; }
.sms-cta .sms-cta__text { max-width: 40rem; margin: 0 auto; }
.sms-cta .sms-cta__text p { margin: 0; }
.sms-cta .sms-cta__actions { display: flex; flex-wrap: wrap; justify-content: center; gap: 0.75rem; margin-top: 2rem; }
.sms-cta .sms-cta__btn { display: inline-flex; align-items: center; gap: 0.35rem; min-width: 0; padding: 0.95rem 1.4rem; border: 2px solid var(--sms-white); border-radius: 999px; font-size: var(--sms-step--1); font-weight: 700; text-decoration: none; transition: transform 0.25s var(--sms-ease); }
.sms-cta .sms-cta__btn:hover { transform: translateY(-3px); }
.sms-cta .sms-cta__btn--main { background: var(--sms-white); color: var(--sms-navy); }
.sms-cta .sms-cta__btn--alt { background: transparent; color: var(--sms-white); }

/* ---------- Home: trust strip ---------- */
.sms-why { position: relative; z-index: 2; padding: clamp(1rem, 0.5rem + 2vw, 2rem) 0 clamp(3rem, 2rem + 3vw, 4.5rem); }
.sms-why .sms-why__inner { width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-why .sms-why__list { display: grid; gap: 1rem; margin: 0; padding: 0; list-style: none; }
.sms-why .sms-why__item { min-width: 0; padding: 1.5rem; border-radius: var(--sms-radius); background: var(--sms-white); box-shadow: var(--sms-shadow); text-align: center; transition: transform 0.3s var(--sms-ease); }
.sms-why .sms-why__item:hover { transform: translateY(-6px); }
.sms-why .sms-why__icon { width: 3.5rem; height: 3.5rem; margin-bottom: 0.9rem; padding: 0.85rem; border-radius: 50%; background: var(--sms-mint); color: var(--sms-green); }
.sms-why .sms-why__title { margin: 0 0 0.35rem; font-size: var(--sms-step-0); font-weight: 700; }
.sms-why .sms-why__text { color: var(--sms-ink-soft); font-size: var(--sms-step--1); }
.sms-why .sms-why__text p { margin: 0; }
@media (min-width: 40em) {
  .sms-why .sms-why__list { grid-template-columns: repeat(2, minmax(0, 1fr)); }
}
@media (min-width: 64em) {
  .sms-why .sms-why__list { grid-template-columns: repeat(4, minmax(0, 1fr)); }
}

/* ---------- Home: services ---------- */
.sms-hsvc { padding: var(--sms-section) 0; background: var(--sms-pale); }
.sms-hsvc .sms-hsvc__inner { width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-hsvc .sms-hsvc__head { max-width: 44rem; margin: 0 auto clamp(2.5rem, 2rem + 2vw, 3.5rem); text-align: center; }
.sms-hsvc .sms-hsvc__title { margin: 0 0 1rem; font-size: var(--sms-step-2); font-weight: 700; line-height: 1.18; }
.sms-hsvc .sms-hsvc__lead { color: var(--sms-ink-soft); font-size: var(--sms-step-1); line-height: 1.55; }
.sms-hsvc .sms-hsvc__lead p { margin: 0; }
.sms-hsvc .sms-hsvc__grid { display: grid; gap: clamp(1.25rem, 0.8rem + 1.5vw, 1.75rem); margin: 0; padding: 0; list-style: none; }
.sms-hsvc .sms-hsvc__card { position: relative; display: flex; flex-direction: column; min-width: 0; overflow: hidden; border-radius: var(--sms-radius); background: var(--sms-white); box-shadow: var(--sms-shadow); transition: transform 0.35s var(--sms-ease); }
.sms-hsvc .sms-hsvc__card:hover { transform: translateY(-8px); }
.sms-hsvc .sms-hsvc__media { position: relative; min-width: 0; }
.sms-hsvc .sms-hsvc__frame { aspect-ratio: 4 / 3; border-radius: 0; }
.sms-hsvc .sms-hsvc__frame .sms-photo__img { transition: transform 0.6s var(--sms-ease); }
.sms-hsvc .sms-hsvc__card:hover .sms-photo__img { transform: scale(1.06); }
.sms-hsvc .sms-hsvc__icon { position: absolute; z-index: 2; left: 1.5rem; bottom: -1.75rem; width: 3.5rem; height: 3.5rem; padding: 0.85rem; border: 4px solid var(--sms-white); border-radius: 50%; background: var(--sms-green); color: var(--sms-white); box-sizing: content-box; }
.sms-hsvc .sms-hsvc__body { display: flex; flex: 1 1 auto; flex-direction: column; min-width: 0; padding: 2.5rem clamp(1.5rem, 1.1rem + 1.5vw, 2rem) clamp(1.5rem, 1.1rem + 1.5vw, 2rem); }
.sms-hsvc .sms-hsvc__name { min-width: 0; margin: 0 0 0.6rem; font-size: var(--sms-step-1); font-weight: 700; line-height: 1.3; }
.sms-hsvc .sms-hsvc__text { min-width: 0; margin-bottom: 1.25rem; color: var(--sms-ink-soft); }
.sms-hsvc .sms-hsvc__text p { margin: 0; }
.sms-hsvc .sms-hsvc__link { align-self: flex-start; min-width: 0; margin-top: auto; padding-top: 1.25rem; }
.sms-hsvc .sms-chips__item { background: var(--sms-pale); box-shadow: none; }
.sms-hsvc .sms-hsvc__extra { display: flex; flex-wrap: wrap; align-items: center; justify-content: center; gap: 0.75rem 1.5rem; margin-top: 2.5rem; padding: 1.25rem 1.5rem; border-radius: 999px; background: var(--sms-white); text-align: center; }
.sms-hsvc .sms-hsvc__extra-icon { width: 2.5rem; height: 2.5rem; padding: 0.55rem; border-radius: 50%; background: var(--sms-mint); color: var(--sms-green); }
.sms-hsvc .sms-hsvc__extra-text { min-width: 0; color: var(--sms-ink-soft); }
.sms-hsvc .sms-hsvc__extra-link { min-width: 0; color: var(--sms-green); font-weight: 700; text-decoration: none; }
@media (min-width: 46em) and (max-width: 63.99em) {
  .sms-hsvc .sms-hsvc__card { flex-direction: row; }
  .sms-hsvc .sms-hsvc__media { flex: 0 0 40%; }
  .sms-hsvc .sms-hsvc__frame { height: 100%; aspect-ratio: auto; }
  .sms-hsvc .sms-hsvc__icon { left: auto; right: -1.75rem; bottom: 1.5rem; }
  .sms-hsvc .sms-hsvc__body { padding-left: 3rem; }
}
@media (min-width: 64em) {
  .sms-hsvc .sms-hsvc__grid { grid-template-columns: repeat(3, minmax(0, 1fr)); }
}
"""

RISE = [".sms-phero .sms-phero__title", ".sms-phero .sms-phero__main"]
ENTRANCE = [".sms-phero .sms-phero__eyebrow", ".sms-phero .sms-phero__sub", ".sms-phero .sms-phero__body", ".sms-phero .sms-phero__actions"]
REVEAL = [".sms-why .sms-why__item", ".sms-hsvc .sms-hsvc__head", ".sms-hsvc .sms-hsvc__card", ".sms-hsvc .sms-hsvc__extra", ".sms-cta .sms-cta__inner"]
LOOP = [".sms-phero .sms-phero__bubble", ".sms-phero .sms-phero__second", ".sms-phero .sms-phero__chip", ".sms-phero .sms-phero__main .sms-photo__img",
        ".sms-cta .sms-cta__bubble", ".sms-cta .sms-cta__wm"]
TRANS = [".sms-cta .sms-cta__btn", ".sms-hsvc .sms-hsvc__card", ".sms-hsvc .sms-hsvc__frame .sms-photo__img", ".sms-why .sms-why__item"]


def page_hero(ctx, h, crumb=True):
    btns = '<div class="sms-phero__actions">%s</div>' % buttons(ctx, h["buttons"]) if h.get("buttons") else ""
    sub = '<div class="sms-phero__sub">%s</div>' % e(h["sub"]) if h.get("sub") else ""
    crumb_html = '<div class="sms-phero__crumb"><a class="sms-phero__crumb-link" href="%s">Home</a> / %s</div>' % (ctx.href("home"), e(LABEL[ctx.slug])) if crumb and ctx.slug != "home" else ""
    chips_html = "".join('<div class="sms-phero__chip">%s<span class="sms-phero__chip-text">%s</span></div>' % (icon(ic, "sms-phero__chip-icon"), e(t)) for ic, t in h.get("chips", [])[:2])
    second = photo(ctx, SECOND.get(ctx.slug, "team"), parallax=False, figcls="sms-phero__second")
    return """<section class="sms-phero">
  <div class="sms-phero__band">
    <div class="sms-phero__bubble sms-phero__bubble--a" aria-hidden="true"></div>
    <div class="sms-phero__bubble sms-phero__bubble--b" aria-hidden="true"></div>
    <div class="sms-phero__bubble sms-phero__bubble--c" aria-hidden="true"></div>
    <div class="sms-phero__inner">
      %s
      <div class="sms-phero__eyebrow">%s%s</div>
      <h1 class="sms-phero__title">%s</h1>
      %s
      <div class="sms-phero__body">%s</div>
      %s
    </div>
  </div>
  <div class="sms-phero__collage">
    %s
    %s
    <div class="sms-phero__chips">%s</div>
  </div>
  <div class="sms-phero__spacer" aria-hidden="true"></div>
</section>
""" % (crumb_html, icon("shield", "sms-phero__eyebrow-icon"), e(h["eyebrow"]), e(h["title"]), sub, paras(h["body"]), btns,
       photo(ctx, h["photo"], lazy=False, parallax=False, figcls="sms-phero__main"), second, chips_html)


def cta(ctx, d):
    btns = "".join('<a class="sms-cta__btn sms-cta__btn--%s" href="%s">%s%s</a>' % (
        "main" if i == 0 else "alt", link(ctx, t), e(l), '&nbsp;<span class="sms-arrow" aria-hidden="true">&rarr;</span>' if i == 0 else "") for i, (l, t) in enumerate(d["buttons"]))
    return """<section class="sms-cta">
  <div class="sms-cta__bubble sms-cta__bubble--a" aria-hidden="true"></div>
  <div class="sms-cta__bubble sms-cta__bubble--b" aria-hidden="true"></div>
  <div class="sms-cta__inner">
    <img class="sms-cta__wm" src="%s" alt="" width="374" height="395" loading="lazy" aria-hidden="true">
    <h2 class="sms-cta__title">%s</h2>
    <div class="sms-cta__text">%s</div>
    <div class="sms-cta__actions">%s</div>
  </div>
</section>
""" % (ctx.asset("streamline-shield-white.png"), e(d["title"]), paras(d["text"]), btns)


def chrome_top(ctx):
    return header(ctx, "blue")


def chrome_bottom(ctx):
    return footer(ctx, "blue")


def home(ctx):
    ctx.notes.append("Image-only copy used: \"Mathew and Tom bring over 15 years of ambulance experience...\" (why-choose-us.png - use approved)")
    hero = {"eyebrow": C.STRAP, "title": "Clinician-Led Medical Cover, [[First Aid Training]] & Safety Consultancy",
            "body": [C.AREA],
            "buttons": [("Book online", "book"), ("Call 01283 358789", "tel")],
            "photo": "team", "chips": [("award", "Qualsafe Registered Centre"), ("shield", "Fully insured")]}
    out = page_hero(ctx, hero, crumb=False)
    why = "".join('<li class="sms-why__item">%s<h3 class="sms-why__title">%s</h3><div class="sms-why__text"><p>%s</p></div></li>' % (icon(ic, "sms-why__icon"), e(t), e(x)) for ic, t, x in C.TRUST)
    out += """<section class="sms-why" aria-labelledby="sms-why-title">
  <div class="sms-why__inner">
    <h2 class="sms-visually-hidden" id="sms-why-title">Why Choose Streamline?</h2>
    <ul class="sms-why__list">%s</ul>
  </div>
</section>
""" % why
    cards = ""
    for s in C.SERVICES:
        cards += """<li class="sms-hsvc__card">
        <div class="sms-hsvc__media">%s%s</div>
        <div class="sms-hsvc__body">
          <h3 class="sms-hsvc__name">%s</h3>
          <div class="sms-hsvc__text"><p>%s</p></div>
          %s
          <a class="sms-btn sms-btn--primary sms-hsvc__link" href="%s">%s&nbsp;<span class="sms-arrow" aria-hidden="true">&rarr;</span></a>
        </div>
      </li>""" % (photo(ctx, s["photo"], parallax=False, figcls="sms-hsvc__frame"), icon(s["icon"], "sms-hsvc__icon"),
                  e(s["title"]), e(s["text"]), chips(s["list"][:3]), ctx.href(s["slug"]), e(s["cta"]))
    out += """<section class="sms-hsvc" id="services">
  <div class="sms-hsvc__inner">
    <div class="sms-hsvc__head"><h2 class="sms-hsvc__title">What We <span class="sms-mark">Provide</span></h2><div class="sms-hsvc__lead"><p>%s</p></div></div>
    <ul class="sms-hsvc__grid">%s</ul>
    <div class="sms-hsvc__extra">%s<span class="sms-hsvc__extra-text">%s</span><a class="sms-hsvc__extra-link" href="%s">%s&nbsp;<span class="sms-arrow" aria-hidden="true">&rarr;</span></a></div>
  </div>
</section>
""" % (e(C.INTRO), cards, icon(C.CAREERS["icon"], "sms-hsvc__extra-icon"), e(C.CAREERS["text"]), ctx.href(C.CAREERS["slug"]), e(C.CAREERS["title"]))
    out += SHARED_RENDERERS["people"](ctx, {"eyebrow": "Our Leadership Team", "title": "Meet The [[Directors.]]", "photo": "directors",
                                           "lead": ["At Streamline Safety & Medical Solutions, our leadership team brings together frontline ambulance experience, clinical knowledge, training expertise, and practical health and safety insight."],
                                           "items": C.DIRECTORS})
    out += SHARED_RENDERERS["claim"](ctx, {"tone": "pale", "text": C.CLAIM_15, "watermark": True})
    out += SHARED_RENDERERS["marquee"](ctx, {"eyebrow": "Who does Streamline work with?", "items": C.WHO})
    out += cta(ctx, {"title": "Contact Streamline", "text": ["Have any questions? We’re here to help."],
                     "buttons": [("Book online", "book"), ("Contact Us", "contact")]})
    return out
