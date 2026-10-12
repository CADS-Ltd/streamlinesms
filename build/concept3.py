"""Concept 3 - Bold brand. The most branded option: green top bar, full-width photo
heroes with boxed headlines and solid green highlights, angled brand edges, tabbed services."""
from common import *  # noqa: F401,F403
import content as C

NAME = "Bold brand"

CSS = r"""
/* ===== Concept 3 theme ===== */
.sms-page { --sms-radius: 0.375rem; --sms-radius-sm: 0.375rem; }
.sms-page .sms-mark { padding: 0 0.22em; background: var(--sms-green); color: var(--sms-white); -webkit-box-decoration-break: clone; box-decoration-break: clone; }
.sms-cards .sms-cards__item { border: 0; border-bottom: 4px solid var(--sms-green); box-shadow: 0 8px 24px rgba(6, 30, 53, 0.08); }
.sms-steps .sms-steps__item { border: 0; border-left: 4px solid var(--sms-green); box-shadow: 0 8px 24px rgba(6, 30, 53, 0.08); }

/* Footer: navy with a green top edge */
.sms-footer { border-top: 6px solid var(--sms-green); background: var(--sms-navy); color: rgba(255, 255, 255, 0.82); }
.sms-footer .sms-footer__heading { color: var(--sms-green-on-navy); }
.sms-footer .sms-footer__tag { color: var(--sms-white); }
.sms-footer .sms-footer__link { color: rgba(255, 255, 255, 0.82); }
.sms-footer .sms-footer__link:hover { color: var(--sms-green-on-navy); }
.sms-footer .sms-footer__base { border-color: rgba(255, 255, 255, 0.16); }

/* ---------- Page hero (photo, boxed headline) ---------- */
.sms-phero { position: relative; overflow: hidden; padding: 0 0 clamp(4.5rem, 3rem + 5vw, 7rem); background: var(--sms-pale); }
.sms-phero.sms-phero--plain { padding-top: clamp(3rem, 2rem + 4vw, 5rem); }
.sms-phero .sms-phero__bg { display: block; width: 100%; height: auto; margin-bottom: 2rem; object-fit: cover; }
@media (min-width: 48em) {
  .sms-phero { display: flex; align-items: center; min-height: clamp(26rem, 18rem + 22vw, 36rem); padding-top: clamp(3rem, 2rem + 4vw, 5rem); }
  .sms-phero.sms-phero--plain { min-height: 0; }
  .sms-phero .sms-phero__bg { position: absolute; inset: 0; height: 100%; margin: 0; object-position: 70% 50%; }
}
.sms-phero .sms-phero__edge { position: absolute; left: 0; right: 0; bottom: -1px; height: clamp(2rem, 1rem + 3.5vw, 4rem); background: var(--sms-green); clip-path: polygon(0 100%, 100% 0, 100% 100%); }
.sms-phero .sms-phero__inner { position: relative; z-index: 1; width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-phero .sms-phero__crumb { display: inline-block; margin-bottom: 1rem; padding: 0.3rem 0.7rem; background: var(--sms-white); color: var(--sms-navy); font-size: var(--sms-step--1); }
.sms-phero .sms-phero__crumb-link { color: var(--sms-navy); }
.sms-phero .sms-phero__eyebrow { display: table; margin-bottom: 0.75rem; padding: 0.35rem 0.75rem; background: var(--sms-green); color: var(--sms-white); font-size: var(--sms-step--1); font-weight: 700; letter-spacing: 0.12em; text-transform: uppercase; }
.sms-phero .sms-phero__title { max-width: 20ch; margin: 0 0 1.5rem; font-size: var(--sms-step-3); font-weight: 700; line-height: 1.32; letter-spacing: -0.015em; }
.sms-phero .sms-phero__title-text { padding: 0 0.22em; background: var(--sms-navy); color: var(--sms-white); -webkit-box-decoration-break: clone; box-decoration-break: clone; }
.sms-phero .sms-phero__card { max-width: 36rem; padding: clamp(1.25rem, 1rem + 1vw, 1.75rem); border-left: 4px solid var(--sms-green); background: var(--sms-white); box-shadow: 0 12px 30px rgba(6, 30, 53, 0.12); }
.sms-phero .sms-phero__sub { margin-bottom: 0.6rem; font-weight: 700; }
.sms-phero .sms-phero__body { color: var(--sms-ink-soft); }
.sms-phero .sms-phero__body p { margin: 0 0 0.75rem; }
.sms-phero .sms-phero__actions { display: flex; flex-wrap: wrap; gap: 0.75rem; margin-top: 1.25rem; }

/* ---------- CTA band (green, angled) ---------- */
.sms-cta { position: relative; overflow: hidden; margin-top: clamp(1rem, 0.5rem + 2vw, 2rem); padding: clamp(4.5rem, 3rem + 5vw, 7rem) 0 clamp(3.5rem, 2.5rem + 4vw, 5.5rem); background: var(--sms-green); color: var(--sms-white); clip-path: polygon(0 clamp(1.5rem, 1rem + 2vw, 3rem), 100% 0, 100% 100%, 0 100%); }
.sms-cta .sms-cta__wm { position: absolute; right: 2%; bottom: -4rem; width: clamp(12rem, 9rem + 14vw, 22rem); height: auto; opacity: 0.14; pointer-events: none; }
.sms-cta .sms-cta__inner { position: relative; display: grid; gap: 1.5rem; }
.sms-cta .sms-cta__copy { min-width: 0; max-width: 42rem; }
.sms-cta .sms-cta__title { margin: 0 0 0.75rem; font-size: var(--sms-step-2); font-weight: 700; line-height: 1.2; }
.sms-cta .sms-cta__text p { margin: 0; }
.sms-cta .sms-cta__actions { display: flex; flex-wrap: wrap; gap: 0.75rem; min-width: 0; }
.sms-cta .sms-cta__btn { display: inline-block; min-width: 0; padding: 0.9rem 1.35rem; border: 2px solid var(--sms-white); border-radius: var(--sms-radius-sm); font-size: var(--sms-step--1); font-weight: 600; text-decoration: none; transition: transform 0.2s ease; }
.sms-cta .sms-cta__btn:hover { transform: translateY(-2px); }
.sms-cta .sms-cta__btn--main { background: var(--sms-white); color: var(--sms-navy); }
.sms-cta .sms-cta__btn--alt { background: transparent; color: var(--sms-white); }
@media (min-width: 56em) {
  .sms-cta .sms-cta__inner { grid-template-columns: minmax(0, 1.4fr) minmax(0, 1fr); align-items: center; }
  .sms-cta .sms-cta__actions { justify-content: flex-end; }
}

/* ---------- Home: three paths ---------- */
.sms-paths { position: relative; z-index: 2; margin-top: clamp(-4rem, -1rem - 3vw, -2rem); }
.sms-paths .sms-paths__inner { width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-paths .sms-paths__list { display: grid; gap: 1rem; margin: 0; padding: 0; list-style: none; }
.sms-paths .sms-paths__item { min-width: 0; }
.sms-paths .sms-paths__link { display: flex; flex-direction: column; gap: 0.6rem; height: 100%; padding: clamp(1.5rem, 1.1rem + 1.5vw, 2.25rem); border-bottom: 4px solid var(--sms-green); background: var(--sms-white); box-shadow: 0 12px 30px rgba(6, 30, 53, 0.12); color: var(--sms-navy); text-decoration: none; transition: transform 0.2s ease; }
.sms-paths .sms-paths__link:hover { transform: translateY(-4px); }
.sms-paths .sms-paths__label { min-width: 0; color: var(--sms-green); font-size: var(--sms-step--1); font-weight: 700; letter-spacing: 0.12em; text-transform: uppercase; }
.sms-paths .sms-paths__cta { min-width: 0; font-size: var(--sms-step-1); font-weight: 700; line-height: 1.35; }
.sms-paths .sms-paths__go { min-width: 0; margin-top: auto; color: var(--sms-green); font-size: 1.25rem; }
@media (min-width: 48em) {
  .sms-paths .sms-paths__list { grid-template-columns: repeat(3, minmax(0, 1fr)); }
}

/* ---------- Home: services (tabs) ---------- */
.sms-tabs { padding: var(--sms-section) 0; }
.sms-tabs .sms-tabs__inner { width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-tabs .sms-tabs__head { display: grid; gap: 1rem; margin-bottom: clamp(2rem, 1.5rem + 2vw, 3rem); }
.sms-tabs .sms-tabs__title { min-width: 0; margin: 0; font-size: var(--sms-step-2); font-weight: 700; line-height: 1.2; }
.sms-tabs .sms-tabs__intro { min-width: 0; max-width: 38rem; color: var(--sms-ink-soft); }
.sms-tabs .sms-tabs__intro p { margin: 0; }
.sms-tabs .sms-tabs__bar { display: flex; flex-wrap: wrap; gap: 0.5rem; margin: 0 0 1rem; }
.sms-tabs .sms-tabs__bar[hidden] { display: none; }
.sms-tabs .sms-tabs__tab { flex: 0 1 auto; min-width: 0; padding: 0.75rem 1.2rem; border: 2px solid var(--sms-navy); border-radius: var(--sms-radius-sm); background: var(--sms-white); color: var(--sms-navy); cursor: pointer; font: inherit; font-size: var(--sms-step--1); font-weight: 700; line-height: 1.3; text-align: left; }
.sms-tabs .sms-tabs__tab[aria-selected="true"] { border-color: var(--sms-green); background: var(--sms-green); color: var(--sms-white); }
.sms-tabs .sms-tabs__panels { display: grid; gap: 1rem; }
.sms-tabs .sms-tabs__panel { display: grid; gap: 1.5rem clamp(2rem, 1rem + 4vw, 4.5rem); min-width: 0; padding: clamp(1.5rem, 1rem + 2vw, 3rem); border-left: 4px solid var(--sms-green); background: var(--sms-pale); }
.sms-tabs .sms-tabs__panel[hidden] { display: none; }
.sms-tabs .sms-tabs__main { min-width: 0; }
.sms-tabs .sms-tabs__name { margin: 0 0 1rem; font-size: var(--sms-step-1); font-weight: 700; }
.sms-tabs .sms-tabs__desc { color: var(--sms-ink-soft); }
.sms-tabs .sms-tabs__desc p { margin: 0 0 1rem; }
.sms-tabs .sms-tabs__aside { min-width: 0; }
.sms-tabs .sms-tabs__list { margin: 0; padding: 0; list-style: none; font-size: var(--sms-step--1); }
.sms-tabs .sms-tabs__item { position: relative; min-width: 0; padding: 0.55rem 0 0.55rem 1.5rem; border-top: 1px solid var(--sms-line); }
.sms-tabs .sms-tabs__item::before { content: ""; position: absolute; left: 0.1rem; top: 0.95rem; width: 0.55rem; height: 0.3rem; border-left: 2px solid var(--sms-green); border-bottom: 2px solid var(--sms-green); transform: rotate(-45deg); }
.sms-tabs .sms-tabs__more { margin-top: 1.5rem; color: var(--sms-ink-soft); }
.sms-tabs .sms-tabs__more-link { color: var(--sms-green); font-weight: 700; }
@media (min-width: 52em) {
  .sms-tabs .sms-tabs__head { grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); align-items: end; }
  .sms-tabs .sms-tabs__panel { grid-template-columns: minmax(0, 1.2fr) minmax(0, 0.8fr); }
}

/* ---------- Home: approach ---------- */
.sms-approach { position: relative; overflow: hidden; padding: var(--sms-section) 0; background: var(--sms-pale); }
.sms-approach .sms-approach__wm { position: absolute; left: -4rem; top: -3rem; width: clamp(14rem, 10rem + 16vw, 24rem); height: auto; opacity: 0.07; pointer-events: none; }
.sms-approach .sms-approach__inner { position: relative; display: grid; gap: clamp(2.5rem, 1.5rem + 4vw, 5rem); width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-approach .sms-approach__main { min-width: 0; }
.sms-approach .sms-approach__title { margin: 0 0 1.25rem; font-size: var(--sms-step-2); font-weight: 700; line-height: 1.3; }
.sms-approach .sms-approach__body { max-width: 36rem; color: var(--sms-ink-soft); }
.sms-approach .sms-approach__body p { margin: 0 0 1rem; }
.sms-approach .sms-approach__claim { max-width: 36rem; margin-top: 1.5rem; padding: 1.25rem 1.5rem; border-left: 4px solid var(--sms-green); background: var(--sms-white); font-weight: 700; }
.sms-approach .sms-approach__claim p { margin: 0; }
.sms-approach .sms-approach__side { min-width: 0; }
.sms-approach .sms-approach__quote { margin: 0 0 2.5rem; padding: clamp(1.5rem, 1rem + 2vw, 2.5rem); border-bottom: 4px solid var(--sms-green); background: var(--sms-white); box-shadow: 0 12px 30px rgba(6, 30, 53, 0.08); }
.sms-approach .sms-approach__quote-label { margin-bottom: 1rem; color: var(--sms-green); font-size: var(--sms-step--1); font-weight: 700; letter-spacing: 0.12em; text-transform: uppercase; }
.sms-approach .sms-approach__quote-text { margin: 0; font-size: var(--sms-step-1); font-weight: 500; line-height: 1.55; }
.sms-approach .sms-approach__quote-text p { margin: 0; }
.sms-approach .sms-approach__cite { display: block; margin-top: 1.25rem; color: var(--sms-ink-soft); font-size: var(--sms-step--1); font-style: normal; }
.sms-approach .sms-approach__who-title { margin: 0 0 1rem; font-size: var(--sms-step-0); font-weight: 700; }
.sms-approach .sms-approach__who { display: flex; flex-wrap: wrap; gap: 0.5rem; margin: 0; padding: 0; list-style: none; }
.sms-approach .sms-approach__who-item { min-width: 0; padding: 0.35rem 0.8rem; border: 1px solid var(--sms-line-green); background: var(--sms-white); font-size: var(--sms-step--1); font-weight: 600; }
@media (min-width: 52em) {
  .sms-approach .sms-approach__inner { grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); }
}
"""

RISE = [".sms-phero .sms-phero__title"]
REVEAL = [".sms-tabs .sms-tabs__panels", ".sms-approach .sms-approach__main", ".sms-approach .sms-approach__side", ".sms-cta .sms-cta__inner"]
TRANS = [".sms-cta .sms-cta__btn", ".sms-paths .sms-paths__link"]


def page_hero(ctx, h, crumb=True):
    btns = '<div class="sms-phero__actions">%s</div>' % buttons(ctx, h["buttons"]) if h.get("buttons") else ""
    sub = '<div class="sms-phero__sub">%s</div>' % e(h["sub"]) if h.get("sub") else ""
    crumb_html = '<div class="sms-phero__crumb"><a class="sms-phero__crumb-link" href="%s">Home</a> / %s</div>' % (ctx.href("home"), e(LABEL[ctx.slug])) if crumb and ctx.slug != "home" else ""
    bg = ""
    if h.get("photo"):
        bg = ctx.ph("hero", "Placeholder for a genuine photo of " + h["photo"], h["photo"] + " (full-width hero background)", "sms-phero__bg", lazy=False)
    return """<section class="sms-phero%s">
  %s
  <div class="sms-phero__edge" aria-hidden="true"></div>
  <div class="sms-phero__inner">
    %s
    <div class="sms-phero__eyebrow">%s</div>
    <h1 class="sms-phero__title"><span class="sms-phero__title-text">%s</span></h1>
    <div class="sms-phero__card">%s<div class="sms-phero__body">%s</div>%s</div>
  </div>
</section>
""" % ("" if bg else " sms-phero--plain", bg, crumb_html, e(h["eyebrow"]), e(h["title"]), sub, paras(h["body"]), btns)


def cta(ctx, d):
    btns = "".join('<a class="sms-cta__btn sms-cta__btn--%s" href="%s">%s</a>' % ("main" if i == 0 else "alt", link(ctx, t), e(l)) for i, (l, t) in enumerate(d["buttons"]))
    return """<section class="sms-cta">
  <img class="sms-cta__wm" src="%s" alt="" width="374" height="395" loading="lazy" aria-hidden="true">
  <div class="sms-cta__inner">
    <div class="sms-cta__copy"><h2 class="sms-cta__title">%s</h2><div class="sms-cta__text">%s</div></div>
    <div class="sms-cta__actions">%s</div>
  </div>
</section>
""" % (ctx.asset("streamline-shield-white.png"), e(d["title"]), paras(d["text"]), btns)


def chrome_top(ctx):
    return topbar(ctx, C.STRAP) + header(ctx, "blue")


def chrome_bottom(ctx):
    return footer(ctx, "white")


TAB_PANELS = [
    ("event-medical-cover", "Event Medical Cover",
     ["We deliver high-quality medical support across a wide range of events and environments, from community gatherings and sporting events to concerts, public events and planned workplace operations.",
      "Our services are flexible, scalable and tailored to the specific risks, audience profile, venue layout and operational needs of your event."],
     "Book us for your medical cover", "What events can Streamline cover?",
     ["Community events, village fetes and charity events", "Business showcases and corporate events", "Sports and combat-sports events", "School events and private functions", "Small festivals and outdoor activities"]),
    ("medical-training", "Medical Training",
     ["Our courses are practical, scenario-based, and designed around real-world environments, helping learners build confidence, competence, and the ability to respond effectively.",
      "Streamline Safety & Medical Solutions is a Qualsafe Registered Centre – Centre No. 908578, allowing us to deliver nationally recognised, regulated qualifications alongside bespoke in-house training."],
     "Book your next training session", "What medical training courses do you provide?",
     ["Emergency First Aid at Work", "First Aid at Work and requalification", "Paediatric and emergency paediatric first aid", "CPR, AED and basic life support", "FREC 3", "FREC 4", "Bespoke workplace medical training"]),
    ("risk-needs-consultancy", "Risk & Needs Consultancy",
     ["In pre-hospital care, the first step is always to assess for danger. Before treatment begins, we look at the environment, identify risks, protect people from harm, and make sure the right support is in place.",
      "Led by IOSH-qualified health and safety advisors with real-world medical and operational experience, we help you identify hazards, understand your responsibilities, and put proportionate plans, people and equipment in place before problems occur."],
     "Book a free consultation for your business", "Our Consultancy Services",
     ["First Aid Needs Assessment", "Risk Assessment Writing", "Gap Assessment", "Event Medical Plans", "Safe System of Work (SSoW) Advice", "Fire Safety Assessment"]),
]


def home(ctx):
    for t in ["\"Working With You, Not Simply For You.\" and the paragraphs beneath it (why-choose-us.png)",
              "Mathew Stones' quote \"We truly care about the people...\" (footer-homepage.png)",
              "\"Mathew and Tom bring over 15 years of ambulance experience...\" (why-choose-us.png - use approved)"]:
        ctx.image_text.append(t)
    hero = {"eyebrow": "Clinician-led safety and medical support", "title": "Clinician-Led Medical Cover, [[First Aid Training]] & Safety Consultancy",
            "sub": C.AREA, "body": [C.INTRO2],
            "photo": "the Streamline team in uniform at an event"}
    ctx.image_text.append("\"Clinician-led safety and medical support\" (clinician-led-safety.png)")
    out = page_hero(ctx, hero, crumb=False)
    paths = "".join('<li class="sms-paths__item"><a class="sms-paths__link" href="%s"><span class="sms-paths__label">%s</span><span class="sms-paths__cta">%s</span><span class="sms-paths__go" aria-hidden="true">&rarr;</span></a></li>' % (
        ctx.href(s["slug"]), e(s["title"]), e(s["cta"])) for s in C.SERVICES)
    out += '<section class="sms-paths" aria-label="Book a service"><div class="sms-paths__inner"><ul class="sms-paths__list">%s</ul></div></section>\n' % paths
    tabs, panels = "", ""
    for i, (slug, title, desc, cta_l, lt, items) in enumerate(TAB_PANELS):
        tabs += '<button class="sms-tabs__tab" type="button" role="tab" id="sms-tab-%d" aria-controls="sms-panel-%d" aria-selected="%s"%s>%s</button>' % (i, i, "true" if i == 0 else "false", "" if i == 0 else ' tabindex="-1"', e(title))
        panels += """<div class="sms-tabs__panel" id="sms-panel-%d" data-sms-panel>
        <div class="sms-tabs__main"><h3 class="sms-tabs__name">%s</h3><div class="sms-tabs__desc">%s</div><a class="sms-btn sms-btn--primary" href="%s">%s</a></div>
        <div class="sms-tabs__aside"><h4 class="sms-visually-hidden">%s</h4><ul class="sms-tabs__list">%s</ul></div>
      </div>""" % (i, e(title), paras(desc), ctx.href(slug), e(cta_l), e(lt), "".join('<li class="sms-tabs__item">%s</li>' % e(x) for x in items))
    out += """<section class="sms-tabs" id="services">
  <div class="sms-tabs__inner">
    <div class="sms-tabs__head"><h2 class="sms-tabs__title">What We <span class="sms-mark">Provide</span></h2><div class="sms-tabs__intro"><p>%s</p></div></div>
    <div class="sms-tabs__bar" role="tablist" aria-label="Our services" hidden>%s</div>
    <div class="sms-tabs__panels">%s</div>
    <div class="sms-tabs__more">%s <a class="sms-tabs__more-link" href="%s">%s</a></div>
  </div>
</section>
""" % (e(C.INTRO), tabs, panels, e(C.CAREERS["text"]), ctx.href(C.CAREERS["slug"]), e(C.CAREERS["title"]))
    who = "".join('<li class="sms-approach__who-item">%s</li>' % e(w) for w in C.WHO)
    out += """<section class="sms-approach" id="approach">
  <img class="sms-approach__wm" src="%s" alt="" width="378" height="399" loading="lazy" aria-hidden="true">
  <div class="sms-approach__inner">
    <div class="sms-approach__main">
      <h2 class="sms-approach__title">%s</h2>
      <div class="sms-approach__body">%s</div>
      <div class="sms-approach__claim"><p>%s</p></div>
    </div>
    <div class="sms-approach__side">
      <figure class="sms-approach__quote">
        <div class="sms-approach__quote-label">A personal message from Mathew</div>
        <blockquote class="sms-approach__quote-text"><p>%s</p></blockquote>
        <figcaption class="sms-approach__cite">Mathew Stones, Director</figcaption>
      </figure>
      <h3 class="sms-approach__who-title">Who does Streamline work with?</h3>
      <ul class="sms-approach__who">%s</ul>
    </div>
  </div>
</section>
""" % (ctx.asset("streamline-shield-blue.png"), e(C.WORKING_WITH["title"]), paras(C.WORKING_WITH["body"]), e(C.CLAIM_15), e(C.MATHEW_QUOTE), who)
    out += cta(ctx, {"title": "Have any questions? We’re here to help.",
                     "text": ["We offer an initial discussion to understand your requirements. Our risk and needs consultancy service also includes a free initial consultation before any chargeable work is agreed."],
                     "buttons": [("Contact Us", "contact"), ("Call 01283 358789", "tel")]})
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
