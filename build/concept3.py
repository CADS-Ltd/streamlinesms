"""Concept 3 - Bold brand, friendly. The most branded option: green top bar, split photo
heroes with boxed navy and green headlines, angled brand shapes, booking panels and
tabbed services with photos."""
from common import *  # noqa: F401,F403
import content as C

NAME = "Bold brand"

CSS = r"""
/* ===== Concept 3 theme ===== */
.sms-page { --sms-radius: 0.75rem; --sms-radius-sm: 0.5rem; }
.sms-page .sms-btn { border-radius: 0.6rem; }
.sms-page .sms-mark { padding: 0 0.22em; background: var(--sms-green); color: var(--sms-white); -webkit-box-decoration-break: clone; box-decoration-break: clone; }
.sms-page .sms-chips__item { border-radius: 0.6rem; }
.sms-page .sms-chips__icon { border-radius: 0.4rem; background: var(--sms-green); color: var(--sms-white); }
.sms-cards .sms-cards__item { border-bottom: 4px solid var(--sms-green); }
.sms-cards .sms-cards__icon { border-radius: 0.6rem; background: var(--sms-green); color: var(--sms-white); }
.sms-cards.sms-tone-white .sms-cards__icon { background: var(--sms-green); }
.sms-links .sms-links__icon,
.sms-quotes .sms-quotes__icon { border-radius: 0.6rem; background: var(--sms-green); color: var(--sms-white); }
.sms-steps .sms-steps__badge { border-radius: 0.75rem; }
.sms-feature .sms-feature__blob { border-radius: 0.75rem; background: var(--sms-green); opacity: 0.18; transform: rotate(6deg); animation: none; }
.sms-feature .sms-feature__frame { border-radius: 0.75rem; }

/* Footer: navy with a green top edge */
.sms-footer { border-top: 6px solid var(--sms-green); background: var(--sms-navy); color: rgba(255, 255, 255, 0.82); }
.sms-footer .sms-footer__heading { color: var(--sms-green-on-navy); }
.sms-footer .sms-footer__tag { color: var(--sms-white); }
.sms-footer .sms-footer__link { color: rgba(255, 255, 255, 0.82); }
.sms-footer .sms-footer__link:hover { color: var(--sms-green-on-navy); }
.sms-footer .sms-footer__base { border-color: rgba(255, 255, 255, 0.16); }

/* ---------- Page hero (split: boxed headline + angled photo) ---------- */
.sms-phero { position: relative; z-index: 0; display: grid; overflow: hidden; background: var(--sms-pale); }
.sms-phero::before { content: ""; position: absolute; z-index: -1; inset: 0; background: repeating-linear-gradient(135deg, transparent 0 22px, rgba(64, 127, 54, 0.05) 22px 44px); }
.sms-phero .sms-phero__media { position: relative; min-width: 0; height: clamp(15rem, 10rem + 25vw, 22rem); }
.sms-phero .sms-phero__frame { height: 100%; border-radius: 0; clip-path: polygon(0 0, 100% 0, 100% 86%, 0 100%); }
.sms-phero .sms-phero__frame .sms-photo__img { animation: sms-zoom 1.6s var(--sms-ease) both; }
.sms-phero .sms-phero__bar { position: absolute; z-index: 1; left: 0; right: 0; bottom: -1px; height: 3.5rem; background: var(--sms-green); clip-path: polygon(0 100%, 100% 30%, 100% 55%, 0 100%); }
.sms-phero .sms-phero__inner { position: relative; z-index: 2; min-width: 0; width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: clamp(2rem, 1.5rem + 3vw, 4rem) var(--sms-gutter) clamp(3.5rem, 2.5rem + 4vw, 6rem); }
.sms-phero .sms-phero__copy { min-width: 0; max-width: 40rem; }
.sms-phero .sms-phero__crumb { display: inline-block; margin-bottom: 1rem; padding: 0.3rem 0.7rem; border-radius: 0.4rem; background: var(--sms-white); color: var(--sms-navy); font-size: var(--sms-step--1); }
.sms-phero .sms-phero__crumb-link { color: var(--sms-navy); }
.sms-phero .sms-phero__eyebrow { display: table; margin-bottom: 0.75rem; padding: 0.35rem 0.75rem; border-radius: 0.4rem; background: var(--sms-green); color: var(--sms-white); font-size: var(--sms-step--1); font-weight: 700; letter-spacing: 0.12em; text-transform: uppercase; }
.sms-phero .sms-phero__title { margin: 0 0 1.5rem; font-size: clamp(1.8rem, 1.3rem + 2.4vw, 3.1rem); font-weight: 700; line-height: 1.36; letter-spacing: -0.015em; }
.sms-phero .sms-phero__title-text { padding: 0 0.22em; background: var(--sms-navy); color: var(--sms-white); -webkit-box-decoration-break: clone; box-decoration-break: clone; }
.sms-phero .sms-phero__card { max-width: 34rem; padding: clamp(1.25rem, 1rem + 1vw, 1.75rem); border-left: 5px solid var(--sms-green); border-radius: 0 0.75rem 0.75rem 0; background: var(--sms-white); box-shadow: var(--sms-shadow-lg); }
.sms-phero .sms-phero__sub { margin-bottom: 0.6rem; font-weight: 700; }
.sms-phero .sms-phero__body { color: var(--sms-ink-soft); }
.sms-phero .sms-phero__body p { margin: 0 0 0.6rem; }
.sms-phero .sms-phero__actions { display: flex; flex-wrap: wrap; gap: 0.75rem; margin-top: 1.25rem; }
.sms-phero .sms-phero__chips { display: flex; flex-wrap: wrap; gap: 0.5rem; margin-top: 1.25rem; }
.sms-phero .sms-phero__chip { display: inline-flex; align-items: center; gap: 0.5rem; min-width: 0; padding: 0.5rem 0.85rem 0.5rem 0.5rem; border-radius: 0.6rem; background: var(--sms-white); box-shadow: var(--sms-shadow); font-size: var(--sms-step--1); font-weight: 700; }
.sms-phero .sms-phero__chip-icon { width: 1.9rem; height: 1.9rem; padding: 0.4rem; border-radius: 0.4rem; background: var(--sms-green); color: var(--sms-white); }
.sms-phero .sms-phero__chip-text { min-width: 0; }
@media (min-width: 60em) {
  .sms-phero { grid-template-columns: minmax(0, 1fr); min-height: clamp(30rem, 20rem + 18vw, 38rem); }
  .sms-phero .sms-phero__media { position: absolute; top: 0; right: 0; bottom: 0; width: 48%; height: auto; }
  .sms-phero .sms-phero__frame { clip-path: polygon(14% 0, 100% 0, 100% 100%, 0 100%); }
  .sms-phero .sms-phero__bar { left: auto; right: 0; top: 0; bottom: 0; width: 48%; height: auto; clip-path: polygon(14% 0, 16% 0, 2% 100%, 0 100%); }
  .sms-phero .sms-phero__inner { display: flex; align-items: center; }
  .sms-phero .sms-phero__copy { max-width: 54%; }
}

/* ---------- CTA band (green, angled, with photo) ---------- */
.sms-cta { position: relative; z-index: 0; overflow: hidden; margin-top: clamp(1rem, 0.5rem + 2vw, 2rem); background: var(--sms-green); color: var(--sms-white); clip-path: polygon(0 clamp(1.5rem, 1rem + 2vw, 3rem), 100% 0, 100% 100%, 0 100%); }
.sms-cta .sms-cta__media { display: none; }
.sms-cta .sms-cta__inner { position: relative; display: grid; gap: 1.5rem; padding-top: clamp(4.5rem, 3rem + 5vw, 7rem); padding-bottom: clamp(3.5rem, 2.5rem + 4vw, 5.5rem); }
.sms-cta .sms-cta__copy { min-width: 0; max-width: 40rem; }
.sms-cta .sms-cta__title { margin: 0 0 0.75rem; font-size: var(--sms-step-2); font-weight: 700; line-height: 1.2; }
.sms-cta .sms-cta__text p { margin: 0; }
.sms-cta .sms-cta__actions { display: flex; flex-wrap: wrap; gap: 0.75rem; min-width: 0; }
.sms-cta .sms-cta__btn { display: inline-flex; align-items: center; gap: 0.35rem; min-width: 0; padding: 0.95rem 1.35rem; border: 2px solid var(--sms-white); border-radius: 0.6rem; font-size: var(--sms-step--1); font-weight: 700; text-decoration: none; transition: transform 0.25s var(--sms-ease); }
.sms-cta .sms-cta__btn:hover { transform: translateY(-3px); }
.sms-cta .sms-cta__btn--main { background: var(--sms-white); color: var(--sms-navy); }
.sms-cta .sms-cta__btn--alt { background: transparent; color: var(--sms-white); }
@media (min-width: 60em) {
  .sms-cta .sms-cta__media { position: absolute; z-index: -1; display: block; top: 0; right: 0; bottom: 0; width: 38%; }
  .sms-cta .sms-cta__frame { height: 100%; border-radius: 0; clip-path: polygon(20% 0, 100% 0, 100% 100%, 0 100%); }
  .sms-cta .sms-cta__inner { padding-right: calc(38% + var(--sms-gutter)); }
}

/* ---------- Home: three paths ---------- */
.sms-paths { position: relative; z-index: 3; margin-top: clamp(-3.5rem, -1rem - 2.5vw, -2rem); }
.sms-paths .sms-paths__inner { width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-paths .sms-paths__list { display: grid; gap: 1rem; margin: 0; padding: 0; list-style: none; }
.sms-paths .sms-paths__item { min-width: 0; }
.sms-paths .sms-paths__link { position: relative; display: flex; flex-direction: column; gap: 0.6rem; height: 100%; overflow: hidden; padding: 1.5rem 1.5rem 1.75rem; border-bottom: 5px solid var(--sms-green); border-radius: 0.75rem; background: var(--sms-white); box-shadow: var(--sms-shadow-lg); color: var(--sms-navy); text-decoration: none; transition: transform 0.3s var(--sms-ease); }
.sms-paths .sms-paths__link:hover { transform: translateY(-6px); }
.sms-paths .sms-paths__icon { width: 3rem; height: 3rem; padding: 0.7rem; border-radius: 0.6rem; background: var(--sms-green); color: var(--sms-white); transition: transform 0.3s var(--sms-ease); }
.sms-paths .sms-paths__link:hover .sms-paths__icon { transform: rotate(-8deg) scale(1.08); }
.sms-paths .sms-paths__label { min-width: 0; color: var(--sms-green); font-size: var(--sms-step--1); font-weight: 700; letter-spacing: 0.12em; text-transform: uppercase; }
.sms-paths .sms-paths__cta { min-width: 0; font-size: var(--sms-step-1); font-weight: 700; line-height: 1.35; }
.sms-paths .sms-paths__go { min-width: 0; margin-top: auto; color: var(--sms-green); font-weight: 700; }
@media (min-width: 48em) {
  .sms-paths .sms-paths__list { grid-template-columns: repeat(3, minmax(0, 1fr)); }
}

/* ---------- Home: tabs ---------- */
.sms-tabs { padding: var(--sms-section) 0; overflow-x: clip; }
.sms-tabs .sms-tabs__inner { width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-tabs .sms-tabs__head { display: grid; gap: 1rem; margin-bottom: clamp(2rem, 1.5rem + 2vw, 3rem); }
.sms-tabs .sms-tabs__title { min-width: 0; margin: 0; font-size: var(--sms-step-2); font-weight: 700; line-height: 1.3; }
.sms-tabs .sms-tabs__intro { min-width: 0; max-width: 38rem; color: var(--sms-ink-soft); font-size: var(--sms-step-1); line-height: 1.55; }
.sms-tabs .sms-tabs__intro p { margin: 0; }
.sms-tabs .sms-tabs__bar { display: flex; flex-wrap: wrap; gap: 0.5rem; margin: 0 0 1.25rem; }
.sms-tabs .sms-tabs__bar[hidden] { display: none; }
.sms-tabs .sms-tabs__tab { display: inline-flex; align-items: center; gap: 0.5rem; flex: 0 1 auto; min-width: 0; padding: 0.75rem 1.15rem; border: 2px solid var(--sms-navy); border-radius: 0.6rem; background: var(--sms-white); color: var(--sms-navy); cursor: pointer; font: inherit; font-size: var(--sms-step--1); font-weight: 700; line-height: 1.3; text-align: left; transition: transform 0.2s var(--sms-ease); }
.sms-tabs .sms-tabs__tab:hover { transform: translateY(-2px); }
.sms-tabs .sms-tabs__tab-icon { width: 1.25rem; height: 1.25rem; }
.sms-tabs .sms-tabs__tab[aria-selected="true"] { border-color: var(--sms-green); background: var(--sms-green); color: var(--sms-white); }
.sms-tabs .sms-tabs__panels { display: grid; gap: 1.25rem; }
.sms-tabs .sms-tabs__panel { display: grid; overflow: hidden; min-width: 0; border-radius: 0.75rem; background: var(--sms-pale); }
.sms-tabs .sms-tabs__panel[hidden] { display: none; }
.sms-tabs .sms-tabs__panel:not([hidden]) { animation: sms-slide-in 0.45s var(--sms-ease) both; }
.sms-tabs .sms-tabs__frame { aspect-ratio: 16 / 10; border-radius: 0; }
.sms-tabs .sms-tabs__main { min-width: 0; padding: clamp(1.5rem, 1rem + 2vw, 2.75rem); }
.sms-tabs .sms-tabs__name { margin: 0 0 0.75rem; font-size: var(--sms-step-2); font-weight: 700; line-height: 1.2; }
.sms-tabs .sms-tabs__desc { color: var(--sms-ink-soft); font-size: var(--sms-step-1); line-height: 1.55; }
.sms-tabs .sms-tabs__desc p { margin: 0; }
.sms-tabs .sms-tabs__list-title { margin: 1.25rem 0 0.6rem; font-size: var(--sms-step-0); font-weight: 700; }
.sms-tabs .sms-tabs__actions { margin-top: 1.5rem; }
.sms-tabs .sms-tabs__more { display: flex; flex-wrap: wrap; align-items: center; gap: 0.75rem 1rem; margin-top: 1.5rem; color: var(--sms-ink-soft); }
.sms-tabs .sms-tabs__more-link { min-width: 0; color: var(--sms-green); font-weight: 700; }
@media (min-width: 56em) {
  .sms-tabs .sms-tabs__head { grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); align-items: end; }
  .sms-tabs .sms-tabs__panel { grid-template-columns: minmax(0, 0.9fr) minmax(0, 1.1fr); }
  .sms-tabs .sms-tabs__frame { height: 100%; aspect-ratio: auto; min-height: 24rem; }
}

/* ---------- Home: approach ---------- */
.sms-approach { position: relative; overflow: hidden; padding: var(--sms-section) 0; background: var(--sms-pale); }
.sms-approach .sms-approach__inner { position: relative; display: grid; gap: clamp(2.5rem, 1.5rem + 4vw, 5rem); width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-approach .sms-approach__main { min-width: 0; }
.sms-approach .sms-approach__title { margin: 0 0 1.25rem; font-size: var(--sms-step-2); font-weight: 700; line-height: 1.3; }
.sms-approach .sms-approach__lead { max-width: 36rem; color: var(--sms-navy); font-size: var(--sms-step-1); line-height: 1.55; }
.sms-approach .sms-approach__lead p { margin: 0; }
.sms-approach .sms-approach__claim { display: flex; gap: 1rem; align-items: center; max-width: 36rem; margin-top: 1.75rem; padding: 1.25rem 1.5rem; border-left: 5px solid var(--sms-green); border-radius: 0 0.75rem 0.75rem 0; background: var(--sms-white); font-weight: 700; }
.sms-approach .sms-approach__claim-icon { width: 2.75rem; height: 2.75rem; padding: 0.6rem; border-radius: 0.6rem; background: var(--sms-green); color: var(--sms-white); }
.sms-approach .sms-approach__claim p { min-width: 0; margin: 0; }
.sms-approach .sms-approach__side { position: relative; min-width: 0; }
.sms-approach .sms-approach__frame { aspect-ratio: 4 / 3; border-radius: 0.75rem; box-shadow: var(--sms-shadow-lg); }
.sms-approach .sms-approach__quote { position: relative; z-index: 2; margin: -4rem 1rem 0; padding: clamp(1.25rem, 1rem + 1.5vw, 2rem); border-bottom: 5px solid var(--sms-green); border-radius: 0.75rem; background: var(--sms-white); box-shadow: var(--sms-shadow-lg); }
.sms-approach .sms-approach__quote-label { margin-bottom: 0.75rem; color: var(--sms-green); font-size: var(--sms-step--1); font-weight: 700; letter-spacing: 0.12em; text-transform: uppercase; }
.sms-approach .sms-approach__quote-text { margin: 0; font-size: var(--sms-step-0); font-weight: 600; line-height: 1.55; }
.sms-approach .sms-approach__quote-text p { margin: 0; }
.sms-approach .sms-approach__cite { display: block; margin-top: 1rem; color: var(--sms-ink-soft); font-size: var(--sms-step--1); font-style: normal; }
@media (min-width: 56em) {
  .sms-approach .sms-approach__inner { grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); align-items: center; }
}
"""

RISE = [".sms-phero .sms-phero__title", ".sms-phero .sms-phero__frame"]
ENTRANCE = [".sms-phero .sms-phero__eyebrow", ".sms-phero .sms-phero__card", ".sms-phero .sms-phero__chips", ".sms-paths .sms-paths__item"]
REVEAL = [".sms-tabs .sms-tabs__head", ".sms-tabs .sms-tabs__panels", ".sms-approach .sms-approach__main", ".sms-approach .sms-approach__side", ".sms-cta .sms-cta__inner"]
LOOP = [".sms-phero .sms-phero__frame .sms-photo__img"]
TRANS = [".sms-cta .sms-cta__btn", ".sms-paths .sms-paths__link", ".sms-paths .sms-paths__icon", ".sms-tabs .sms-tabs__tab"]
OPEN = [".sms-tabs .sms-tabs__panel:not([hidden])"]


def page_hero(ctx, h, crumb=True):
    btns = '<div class="sms-phero__actions">%s</div>' % buttons(ctx, h["buttons"]) if h.get("buttons") else ""
    sub = '<div class="sms-phero__sub">%s</div>' % e(h["sub"]) if h.get("sub") else ""
    crumb_html = '<div class="sms-phero__crumb"><a class="sms-phero__crumb-link" href="%s">Home</a> / %s</div>' % (ctx.href("home"), e(LABEL[ctx.slug])) if crumb and ctx.slug != "home" else ""
    chips_html = "".join('<div class="sms-phero__chip">%s<span class="sms-phero__chip-text">%s</span></div>' % (icon(ic, "sms-phero__chip-icon"), e(t)) for ic, t in h.get("chips", [])[:2])
    return """<section class="sms-phero">
  <div class="sms-phero__media">%s<div class="sms-phero__bar" aria-hidden="true"></div></div>
  <div class="sms-phero__inner">
    <div class="sms-phero__copy">
      %s
      <div class="sms-phero__eyebrow">%s</div>
      <h1 class="sms-phero__title"><span class="sms-phero__title-text">%s</span></h1>
      <div class="sms-phero__card">%s<div class="sms-phero__body">%s</div>%s</div>
      <div class="sms-phero__chips">%s</div>
    </div>
  </div>
</section>
""" % (photo(ctx, h["photo"], lazy=False, parallax=False, figcls="sms-phero__frame"), crumb_html, e(h["eyebrow"]), e(h["title"]), sub, paras(h["body"]), btns, chips_html)


def cta(ctx, d):
    btns = "".join('<a class="sms-cta__btn sms-cta__btn--%s" href="%s">%s%s</a>' % (
        "main" if i == 0 else "alt", link(ctx, t), e(l), '&nbsp;<span class="sms-arrow" aria-hidden="true">&rarr;</span>' if i == 0 else "") for i, (l, t) in enumerate(d["buttons"]))
    return """<section class="sms-cta">
  <div class="sms-cta__media" aria-hidden="true">%s</div>
  <div class="sms-cta__inner">
    <div class="sms-cta__copy"><h2 class="sms-cta__title">%s</h2><div class="sms-cta__text">%s</div></div>
    <div class="sms-cta__actions">%s</div>
  </div>
</section>
""" % (photo(ctx, "team", figcls="sms-cta__frame"), e(d["title"]), paras(d["text"]), btns)


def chrome_top(ctx):
    return topbar(ctx, C.STRAP) + header(ctx, "blue")


def chrome_bottom(ctx):
    return footer(ctx, "white")


TAB_PANELS = [
    ("event-medical-cover", "Event Medical Cover", "heart", "festival",
     "We deliver high-quality medical support across a wide range of events and environments, from community gatherings and sporting events to concerts, public events and planned workplace operations.",
     "Book us for your medical cover", "What events can Streamline cover?",
     [("tent", "Community events, village fetes and charity events"), ("briefcase", "Business showcases and corporate events"), ("trophy", "Sports and combat-sports events"), ("school", "School events and private functions"), ("music", "Small festivals and outdoor activities")]),
    ("medical-training", "Medical Training", "cap", "cpr-room",
     "Our courses are practical, scenario-based, and designed around real-world environments, helping learners build confidence, competence, and the ability to respond effectively.",
     "Book your next training session", "What medical training courses do you provide?",
     [("firstaid", "Emergency First Aid at Work"), ("firstaid", "First Aid at Work and requalification"), ("school", "Paediatric and emergency paediatric first aid"), ("heart", "CPR, AED and basic life support"), ("award", "FREC 3"), ("award", "FREC 4")]),
    ("risk-needs-consultancy", "Risk & Needs Consultancy", "clipboard", "assessor",
     "In pre-hospital care, the first step is always to assess for danger. Before treatment begins, we look at the environment, identify risks, protect people from harm, and make sure the right support is in place.",
     "Book a free consultation for your business", "Our Consultancy Services",
     [("clipboard", "First Aid Needs Assessment"), ("file", "Risk Assessment Writing"), ("search", "Gap Assessment"), ("route", "Event Medical Plans"), ("hardhat", "Safe System of Work (SSoW) Advice"), ("fire", "Fire Safety Assessment")]),
]


def home(ctx):
    ctx.notes += ["Image-only copy used: \"Working With You, Not Simply For You.\" and the paragraphs beneath it (why-choose-us.png)",
                  "Image-only copy used: Mathew Stones' quote \"We truly care about the people...\" (footer-homepage.png)",
                  "Image-only copy used: \"Mathew and Tom bring over 15 years of ambulance experience...\" (why-choose-us.png - use approved)",
                  "Image-only copy used: \"Clinician-led safety and medical support\" (clinician-led-safety.png)"]
    hero = {"eyebrow": "Clinician-led safety and medical support", "title": "Clinician-Led Medical Cover, [[First Aid Training]] & Safety Consultancy",
            "sub": C.AREA, "body": [C.INTRO2],
            "photo": "team", "chips": [("award", "Qualsafe Registered Centre"), ("shield", "Fully insured")]}
    out = page_hero(ctx, hero, crumb=False)
    paths = "".join('<li class="sms-paths__item"><a class="sms-paths__link" href="%s">%s<span class="sms-paths__label">%s</span><span class="sms-paths__cta">%s</span><span class="sms-paths__go">Find out more&nbsp;<span class="sms-arrow" aria-hidden="true">&rarr;</span></span></a></li>' % (
        ctx.href(s["slug"]), icon(s["icon"], "sms-paths__icon"), e(s["title"]), e(s["cta"])) for s in C.SERVICES)
    out += '<section class="sms-paths" aria-label="Book a service"><div class="sms-paths__inner"><ul class="sms-paths__list">%s</ul></div></section>\n' % paths
    tabs, panels = "", ""
    for i, (slug, title, ic, ph, desc, cta_l, lt, items) in enumerate(TAB_PANELS):
        tabs += '<button class="sms-tabs__tab" type="button" role="tab" id="sms-tab-%d" aria-controls="sms-panel-%d" aria-selected="%s"%s>%s%s</button>' % (
            i, i, "true" if i == 0 else "false", "" if i == 0 else ' tabindex="-1"', icon(ic, "sms-tabs__tab-icon"), e(title))
        panels += """<div class="sms-tabs__panel" id="sms-panel-%d" data-sms-panel>
        %s
        <div class="sms-tabs__main">
          <h3 class="sms-tabs__name">%s</h3>
          <div class="sms-tabs__desc"><p>%s</p></div>
          <h4 class="sms-tabs__list-title">%s</h4>
          %s
          <div class="sms-tabs__actions">%s</div>
        </div>
      </div>""" % (i, photo(ctx, ph, figcls="sms-tabs__frame"), e(title), e(desc), e(lt), chips(items), buttons(ctx, [(cta_l, slug)]))
    out += """<section class="sms-tabs" id="services">
  <div class="sms-tabs__inner">
    <div class="sms-tabs__head"><h2 class="sms-tabs__title">What We <span class="sms-mark">Provide</span></h2><div class="sms-tabs__intro"><p>%s</p></div></div>
    <div class="sms-tabs__bar" role="tablist" aria-label="Our services" hidden>%s</div>
    <div class="sms-tabs__panels">%s</div>
    <div class="sms-tabs__more">%s <a class="sms-tabs__more-link" href="%s">%s&nbsp;<span class="sms-arrow" aria-hidden="true">&rarr;</span></a></div>
  </div>
</section>
""" % (e(C.INTRO), tabs, panels, e(C.CAREERS["text"]), ctx.href(C.CAREERS["slug"]), e(C.CAREERS["title"]))
    out += """<section class="sms-approach" id="approach">
  <div class="sms-approach__inner">
    <div class="sms-approach__main">
      <h2 class="sms-approach__title">%s</h2>
      <div class="sms-approach__lead"><p>%s</p></div>
      %s
      <div class="sms-approach__claim">%s<p>%s</p></div>
    </div>
    <div class="sms-approach__side">
      %s
      <figure class="sms-approach__quote">
        <div class="sms-approach__quote-label">A personal message from Mathew</div>
        <blockquote class="sms-approach__quote-text"><p>%s</p></blockquote>
        <figcaption class="sms-approach__cite">Mathew Stones, Director</figcaption>
      </figure>
    </div>
  </div>
</section>
""" % (e(C.WORKING_WITH["title"]), e(C.WORKING_WITH["body"][0]), more(paras(C.WORKING_WITH["body"][1:])), icon("heart", "sms-approach__claim-icon"), e(C.CLAIM_15),
       photo(ctx, "festival", figcls="sms-approach__frame"), e(C.MATHEW_QUOTE))
    out += SHARED_RENDERERS["marquee"](ctx, {"eyebrow": "Who does Streamline work with?", "items": C.WHO})
    out += cta(ctx, {"title": "Have any questions? We’re here to help.",
                     "text": ["We offer an initial discussion to understand your requirements. Our risk and needs consultancy service also includes a free initial consultation before any chargeable work is agreed."],
                     "buttons": [("Book online", "book"), ("Contact Us", "contact")]})
    return out


TABS_JS = """<script>
(function () {
  var root = document.querySelector('.sms-tabs');
  if (!root) return;
  var bar = root.querySelector('[role="tablist"]');
  var tabs = Array.prototype.slice.call(root.querySelectorAll('[role="tab"]'));
  var panels = Array.prototype.slice.call(root.querySelectorAll('[data-sms-panel]'));
  if (!bar || !tabs.length) return;
  panels.forEach(function (p, i) { p.setAttribute('role', 'tabpanel'); p.setAttribute('aria-labelledby', tabs[i].id); p.setAttribute('tabindex', '0'); });
  function select(n, focus) {
    tabs.forEach(function (t, i) { var on = i === n; t.setAttribute('aria-selected', on ? 'true' : 'false'); t.tabIndex = on ? 0 : -1; panels[i].hidden = !on; });
    if (focus) tabs[n].focus();
  }
  tabs.forEach(function (t, i) {
    t.addEventListener('click', function () { select(i, false); });
    t.addEventListener('keydown', function (ev) {
      var n = null;
      if (ev.key === 'ArrowRight') n = (i + 1) % tabs.length;
      if (ev.key === 'ArrowLeft') n = (i - 1 + tabs.length) % tabs.length;
      if (ev.key === 'Home') n = 0;
      if (ev.key === 'End') n = tabs.length - 1;
      if (n !== null) { ev.preventDefault(); select(n, true); }
    });
  });
  bar.hidden = false;
  select(0, false);
})();
</script>
"""


def scripts(ctx, main):
    return TABS_JS if 'data-sms-panel' in main else ""
