"""Concept 1 - Editorial split. White and airy, soft green highlight, big portrait photos."""
from common import *  # noqa: F401,F403
import content as C

NAME = "Editorial split"

CSS = r"""
/* ===== Concept 1 theme ===== */
.sms-page { --sms-radius: 0.75rem; --sms-mark-bg: #cfe5c9; }
.sms-page .sms-mark { background: linear-gradient(180deg, transparent 58%, var(--sms-mark-bg) 58%); padding: 0 0.08em; -webkit-box-decoration-break: clone; box-decoration-break: clone; }

/* Footer: navy */
.sms-footer { background: var(--sms-navy); color: rgba(255, 255, 255, 0.82); }
.sms-footer .sms-footer__heading,
.sms-footer .sms-footer__tag { color: var(--sms-white); }
.sms-footer .sms-footer__link { color: rgba(255, 255, 255, 0.82); }
.sms-footer .sms-footer__link:hover { color: var(--sms-green-on-navy); }
.sms-footer .sms-footer__base { border-color: rgba(255, 255, 255, 0.16); }

/* ---------- Page hero (split) ---------- */
.sms-phero { overflow: hidden; padding: clamp(2.5rem, 1.5rem + 4vw, 5rem) 0 clamp(3rem, 2rem + 4vw, 5.5rem); }
.sms-phero .sms-phero__inner { display: grid; gap: clamp(2.5rem, 1.5rem + 4vw, 5rem); align-items: center; width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-phero .sms-phero__copy { min-width: 0; }
.sms-phero .sms-phero__crumb { margin-bottom: 1.5rem; color: var(--sms-ink-soft); font-size: var(--sms-step--1); }
.sms-phero .sms-phero__crumb-link { color: var(--sms-ink-soft); }
.sms-phero .sms-phero__eyebrow { margin-bottom: 1rem; color: var(--sms-green); font-size: var(--sms-step--1); font-weight: 700; letter-spacing: 0.12em; text-transform: uppercase; }
.sms-phero .sms-phero__title { margin: 0 0 1.25rem; font-size: var(--sms-step-3); font-weight: 700; line-height: 1.1; letter-spacing: -0.02em; }
.sms-phero .sms-phero__sub { margin-bottom: 1rem; font-size: var(--sms-step-1); font-weight: 600; line-height: 1.45; }
.sms-phero .sms-phero__body { max-width: 36rem; color: var(--sms-ink-soft); }
.sms-phero .sms-phero__body p { margin: 0 0 1rem; }
.sms-phero .sms-phero__actions { display: flex; flex-wrap: wrap; gap: 0.75rem; margin-top: 1.75rem; }
.sms-phero .sms-phero__media { position: relative; min-width: 0; max-width: 24rem; margin: 0; }
.sms-phero .sms-phero__media::before { content: ""; position: absolute; inset: 1.5rem -1.5rem -1.5rem 1.5rem; z-index: -1; border-radius: var(--sms-radius); background: var(--sms-pale-2); }
.sms-phero .sms-phero__img { display: block; width: 100%; height: auto; border-radius: var(--sms-radius); }
.sms-phero .sms-phero__badge { position: absolute; left: 0.75rem; bottom: 1.5rem; display: grid; place-items: center; width: clamp(4.5rem, 3.5rem + 3vw, 6rem); aspect-ratio: 1; border-radius: 50%; background: var(--sms-white); box-shadow: 0 10px 30px rgba(6, 30, 53, 0.15); }
.sms-phero .sms-phero__badge-img { display: block; width: 58%; height: auto; }
.sms-phero .sms-phero__panel { min-width: 0; padding: clamp(1.5rem, 1rem + 2vw, 2.5rem); border-radius: var(--sms-radius); background: var(--sms-pale); }
.sms-phero .sms-phero__panel-label { color: var(--sms-ink-soft); font-size: var(--sms-step--1); font-weight: 700; letter-spacing: 0.12em; text-transform: uppercase; }
.sms-phero .sms-phero__panel-value { display: block; margin: 0.25rem 0 1.25rem; color: var(--sms-navy); font-size: var(--sms-step-1); font-weight: 700; line-height: 1.25; text-decoration: none; overflow-wrap: anywhere; }
.sms-phero .sms-phero__panel-value:hover { color: var(--sms-green); }
@media (min-width: 46em) {
  .sms-phero .sms-phero__inner { grid-template-columns: minmax(0, 1.15fr) minmax(0, 0.85fr); }
  .sms-phero .sms-phero__media { max-width: none; }
  .sms-phero .sms-phero__badge { left: -1.25rem; }
}

/* ---------- CTA band ---------- */
.sms-cta { padding: var(--sms-section) 0; }
.sms-cta .sms-cta__box { position: relative; display: grid; gap: 1.5rem; overflow: hidden; padding: clamp(2rem, 1.2rem + 3vw, 4rem); border-radius: var(--sms-radius); background: var(--sms-pale); }
.sms-cta .sms-cta__wm { position: absolute; right: -2rem; top: 50%; width: clamp(10rem, 8rem + 10vw, 18rem); height: auto; opacity: 0.1; transform: translateY(-50%); pointer-events: none; }
.sms-cta .sms-cta__copy { position: relative; min-width: 0; max-width: 40rem; }
.sms-cta .sms-cta__title { margin: 0 0 0.75rem; font-size: var(--sms-step-2); font-weight: 700; line-height: 1.2; }
.sms-cta .sms-cta__text { color: var(--sms-ink-soft); }
.sms-cta .sms-cta__text p { margin: 0; }
.sms-cta .sms-cta__actions { position: relative; display: flex; flex-wrap: wrap; gap: 0.75rem; min-width: 0; }
@media (min-width: 56em) {
  .sms-cta .sms-cta__box { grid-template-columns: minmax(0, 1.4fr) minmax(0, 1fr); align-items: center; }
  .sms-cta .sms-cta__actions { justify-content: flex-end; padding-right: 6rem; }
}

/* ---------- Home: credentials strip ---------- */
.sms-creds { border-top: 1px solid var(--sms-line); border-bottom: 1px solid var(--sms-line); }
.sms-creds .sms-creds__inner { width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: 1.5rem var(--sms-gutter); }
.sms-creds .sms-creds__list { display: grid; gap: 1rem 2.5rem; min-width: 0; margin: 0; padding: 0; list-style: none; }
.sms-creds .sms-creds__item { display: flex; align-items: center; gap: 0.85rem; min-width: 0; font-size: var(--sms-step--1); font-weight: 600; line-height: 1.45; }
.sms-creds .sms-creds__badge { flex: 0 0 auto; min-width: 0; width: 3rem; height: auto; }
.sms-creds .sms-creds__dot { flex: 0 0 auto; min-width: 0; width: 0.6rem; height: 0.6rem; border-radius: 50%; background: var(--sms-green); }
@media (min-width: 52em) {
  .sms-creds .sms-creds__list { grid-template-columns: repeat(3, minmax(0, 1fr)); align-items: center; }
}

/* ---------- Home: services index ---------- */
.sms-svc { padding: var(--sms-section) 0; }
.sms-svc .sms-svc__inner { width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-svc .sms-svc__eyebrow { margin-bottom: 0.85rem; color: var(--sms-green); font-size: var(--sms-step--1); font-weight: 700; letter-spacing: 0.12em; text-transform: uppercase; }
.sms-svc .sms-svc__title { margin: 0 0 clamp(2rem, 1.5rem + 2vw, 3rem); font-size: var(--sms-step-2); font-weight: 700; line-height: 1.2; }
.sms-svc .sms-svc__list { margin: 0; padding: 0; border-top: 2px solid var(--sms-navy); list-style: none; }
.sms-svc .sms-svc__item { min-width: 0; border-bottom: 1px solid var(--sms-line); }
.sms-svc .sms-svc__link { display: grid; grid-template-columns: 3rem minmax(0, 1fr); gap: 0.75rem 1rem; padding: clamp(1.75rem, 1.3rem + 1.5vw, 2.75rem) 0; color: var(--sms-navy); text-decoration: none; }
.sms-svc .sms-svc__num { min-width: 0; color: var(--sms-green); font-size: var(--sms-step-1); font-weight: 700; }
.sms-svc .sms-svc__body { min-width: 0; }
.sms-svc .sms-svc__name { margin: 0 0 0.5rem; font-size: var(--sms-step-2); font-weight: 700; line-height: 1.2; }
.sms-svc .sms-svc__desc { max-width: 38rem; color: var(--sms-ink-soft); }
.sms-svc .sms-svc__desc p { margin: 0 0 1rem; }
.sms-svc .sms-svc__chips { display: flex; flex-wrap: wrap; gap: 0.5rem; margin: 0; padding: 0; list-style: none; }
.sms-svc .sms-svc__chip { min-width: 0; padding: 0.3rem 0.75rem; border-radius: 999px; background: var(--sms-pale-2); font-size: var(--sms-step--1); font-weight: 600; }
.sms-svc .sms-svc__cta { grid-column: 2; min-width: 0; color: var(--sms-green); font-weight: 700; }
.sms-svc .sms-svc__link:hover .sms-svc__name { color: var(--sms-green); }
.sms-svc .sms-svc__more { display: flex; flex-wrap: wrap; align-items: center; gap: 0.5rem 1.5rem; margin-top: 2rem; padding: 1.25rem 1.5rem; border-radius: var(--sms-radius); background: var(--sms-pale); }
.sms-svc .sms-svc__more-text { min-width: 0; color: var(--sms-ink-soft); }
.sms-svc .sms-svc__more-link { min-width: 0; color: var(--sms-green); font-weight: 700; text-decoration: none; }
@media (min-width: 52em) {
  .sms-svc .sms-svc__link { grid-template-columns: 5rem minmax(0, 1.3fr) minmax(0, 0.7fr); align-items: start; }
  .sms-svc .sms-svc__cta { grid-column: 3; justify-self: end; padding-top: 0.5rem; text-align: right; }
}

/* ---------- Home: about ---------- */
.sms-habout { position: relative; overflow: hidden; padding: var(--sms-section) 0; background: var(--sms-pale); }
.sms-habout .sms-habout__wm { position: absolute; left: -5rem; bottom: -6rem; width: clamp(16rem, 12rem + 18vw, 28rem); height: auto; opacity: 0.07; pointer-events: none; }
.sms-habout .sms-habout__inner { position: relative; display: grid; gap: clamp(2.5rem, 1.5rem + 4vw, 5rem); width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-habout .sms-habout__main { min-width: 0; }
.sms-habout .sms-habout__eyebrow { margin-bottom: 0.85rem; color: var(--sms-green); font-size: var(--sms-step--1); font-weight: 700; letter-spacing: 0.12em; text-transform: uppercase; }
.sms-habout .sms-habout__title { margin: 0 0 1.5rem; font-size: var(--sms-step-2); font-weight: 700; line-height: 1.2; }
.sms-habout .sms-habout__body { max-width: 38rem; color: var(--sms-ink-soft); }
.sms-habout .sms-habout__body p { margin: 0 0 1rem; }
.sms-habout .sms-habout__aside { min-width: 0; }
.sms-habout .sms-habout__claim { margin: 0 0 2rem; padding: 1.5rem 1.75rem; border-radius: var(--sms-radius); background: var(--sms-white); font-size: var(--sms-step-1); font-weight: 700; line-height: 1.45; }
.sms-habout .sms-habout__claim p { margin: 0; }
.sms-habout .sms-habout__points { display: grid; gap: 1.25rem; margin: 0; padding: 0; list-style: none; }
.sms-habout .sms-habout__point { min-width: 0; padding-left: 1.25rem; border-left: 3px solid var(--sms-green); }
.sms-habout .sms-habout__point-title { margin: 0 0 0.25rem; font-size: var(--sms-step-0); font-weight: 700; }
.sms-habout .sms-habout__point-text { color: var(--sms-ink-soft); font-size: var(--sms-step--1); }
.sms-habout .sms-habout__point-text p { margin: 0; }
.sms-habout .sms-habout__link { display: inline-block; margin-top: 1rem; }
@media (min-width: 52em) {
  .sms-habout .sms-habout__inner { grid-template-columns: minmax(0, 1.2fr) minmax(0, 0.8fr); }
}
"""

RISE = [".sms-phero .sms-phero__title", ".sms-phero .sms-phero__media"]
REVEAL = [".sms-creds .sms-creds__item", ".sms-svc .sms-svc__item", ".sms-habout .sms-habout__main",
          ".sms-habout .sms-habout__aside", ".sms-cta .sms-cta__box"]
TRANS = []


def page_hero(ctx, h, crumb=True, h1_override=None):
    btns = '<div class="sms-phero__actions">%s</div>' % buttons(ctx, h["buttons"]) if h.get("buttons") else ""
    sub = '<div class="sms-phero__sub">%s</div>' % e(h["sub"]) if h.get("sub") else ""
    crumb_html = '<div class="sms-phero__crumb"><a class="sms-phero__crumb-link" href="%s">Home</a> / %s</div>' % (ctx.href("home"), e(LABEL[ctx.slug])) if crumb and ctx.slug != "home" else ""
    if h.get("photo"):
        side = """<figure class="sms-phero__media">%s
      <div class="sms-phero__badge" aria-hidden="true"><img class="sms-phero__badge-img" src="%s" alt="" width="378" height="399"></div>
    </figure>""" % (ctx.ph("portrait", "Placeholder for a genuine photo of " + h["photo"], h["photo"], "sms-phero__img", lazy=False), ctx.asset("streamline-shield-blue.png"))
    else:
        side = """<div class="sms-phero__panel">
      <div class="sms-phero__panel-label">Telephone</div><a class="sms-phero__panel-value" href="tel:%s">%s</a>
      <div class="sms-phero__panel-label">Email</div><a class="sms-phero__panel-value" href="mailto:%s">%s</a>
    </div>""" % (PHONE_TEL, PHONE, EMAIL, EMAIL)
    return """<section class="sms-phero">
  <div class="sms-phero__inner">
    <div class="sms-phero__copy">
      %s
      <div class="sms-phero__eyebrow">%s</div>
      <h1 class="sms-phero__title">%s</h1>
      %s
      <div class="sms-phero__body">%s</div>
      %s
    </div>
    %s
  </div>
</section>
""" % (crumb_html, e(h["eyebrow"]), e(h1_override or h["title"]), sub, paras(h["body"]), btns, side)


def cta(ctx, d):
    return """<section class="sms-cta">
  <div class="sms-cta__inner">
    <div class="sms-cta__box">
      <img class="sms-cta__wm" src="%s" alt="" width="378" height="399" loading="lazy" aria-hidden="true">
      <div class="sms-cta__copy"><h2 class="sms-cta__title">%s</h2><div class="sms-cta__text">%s</div></div>
      <div class="sms-cta__actions">%s</div>
    </div>
  </div>
</section>
""" % (ctx.asset("streamline-shield-blue.png"), e(d["title"]), paras(d["text"]), buttons(ctx, d["buttons"]))


def chrome_top(ctx):
    cta_btn = '<a class="sms-btn sms-btn--outline sms-header__cta" href="tel:%s">%s</a>' % (PHONE_TEL, PHONE)
    return header(ctx, "blue", cta_btn)


def chrome_bottom(ctx):
    return footer(ctx, "white")


def home(ctx):
    ctx.image_text.append("\"Clinician-led safety and medical support\" (clinician-led-safety.png)")
    ctx.image_text.append("\"Mathew and Tom bring over 15 years of ambulance experience...\" (why-choose-us.png - use approved)")
    hero = {"eyebrow": "Clinician-led safety and medical support",
            "title": "Clinician-Led Medical Cover, [[First Aid Training]] & Safety Consultancy",
            "sub": C.AREA, "body": [C.INTRO, C.INTRO2],
            "buttons": [("Book your next training session", "medical-training"), ("Book us for your medical cover", "event-medical-cover")],
            "photo": "directors Mathew Stones and Tom Wilkes in Streamline uniform"}
    out = page_hero(ctx, hero, crumb=False)
    out += """<section class="sms-creds" aria-label="Credentials">
  <div class="sms-creds__inner">
    <ul class="sms-creds__list">
      <li class="sms-creds__item"><img class="sms-creds__badge" src="%s" alt="Qualsafe registered centre" width="1000" height="982" loading="lazy">Qualsafe Registered Centre &ndash; Centre No. 908578</li>
      <li class="sms-creds__item"><span class="sms-creds__dot" aria-hidden="true"></span>Led by IOSH-qualified health and safety advisors</li>
      <li class="sms-creds__item"><span class="sms-creds__dot" aria-hidden="true"></span>Fully insured, carefully planned and professionally delivered.</li>
    </ul>
  </div>
</section>
""" % ctx.asset("whatsapp-image-2026-07-20-at-12.27.35.jpeg")
    rows = ""
    for i, s in enumerate(C.SERVICES, 1):
        chips = "".join('<li class="sms-svc__chip">%s</li>' % e(x) for x in s["list"][:4])
        rows += """<li class="sms-svc__item"><a class="sms-svc__link" href="%s">
        <div class="sms-svc__num" aria-hidden="true">%02d</div>
        <div class="sms-svc__body"><h3 class="sms-svc__name">%s</h3><div class="sms-svc__desc"><p>%s</p></div><ul class="sms-svc__chips">%s</ul></div>
        <div class="sms-svc__cta">%s&nbsp;<span class="sms-arrow" aria-hidden="true">&rarr;</span></div>
      </a></li>""" % (ctx.href(s["slug"]), i, e(s["title"]), e(s["text"]), chips, e(s["cta"]))
    out += """<section class="sms-svc" id="services">
  <div class="sms-svc__inner">
    <div class="sms-svc__eyebrow">Our Services</div>
    <h2 class="sms-svc__title">What We Provide</h2>
    <ol class="sms-svc__list">%s</ol>
    <div class="sms-svc__more"><div class="sms-svc__more-text">%s</div><a class="sms-svc__more-link" href="%s">%s&nbsp;<span class="sms-arrow" aria-hidden="true">&rarr;</span></a></div>
  </div>
</section>
""" % (rows, e(C.CAREERS["text"]), ctx.href(C.CAREERS["slug"]), e(C.CAREERS["title"]))
    pts = "".join('<li class="sms-habout__point"><h3 class="sms-habout__point-title">%s</h3><div class="sms-habout__point-text"><p>%s</p></div></li>' % (e(t), e(x)) for t, x in [C.TRUST[0], C.TRUST[1], C.TRUST[3]])
    out += """<section class="sms-habout" id="about">
  <img class="sms-habout__wm" src="%s" alt="" width="378" height="399" loading="lazy" aria-hidden="true">
  <div class="sms-habout__inner">
    <div class="sms-habout__main">
      <div class="sms-habout__eyebrow">About Streamline</div>
      <h2 class="sms-habout__title">Protecting People. [[Preparing Organisations.]]</h2>
      <div class="sms-habout__body">%s</div>
      <a class="sms-btn sms-btn--outline sms-habout__link" href="%s">Meet The Directors</a>
    </div>
    <div class="sms-habout__aside">
      <div class="sms-habout__claim"><p>%s</p></div>
      <ul class="sms-habout__points">%s</ul>
    </div>
  </div>
</section>
""" % (ctx.asset("streamline-shield-blue.png"), paras(C.ABOUT_HOME), ctx.href("about"), e(C.CLAIM_15), pts)
    picks = ["Where is Streamline based?", "Who runs Streamline?", "Can Streamline provide more than one service?", "Do you offer a free initial discussion?", "Are you insured?", "How can I contact Streamline?"]
    allf = dict(C.faqs("home"))
    out += SHARED_RENDERERS["faq"](ctx, {"eyebrow": "Protecting People. Supporting Business.", "title": "General Streamline FAQs",
                                        "lead": ["Answers to common questions about Streamline Safety & Medical Solutions, our team, services, bookings and how we work."],
                                        "items": [(q, allf[q]) for q in picks]})
    out += cta(ctx, {"title": "Still have a question?", "text": ["Speak to our team and we will be happy to help."],
                     "buttons": [("Contact Streamline", "contact"), ("Call 01283 358789", "tel")]})
    return out.replace('Protecting People. [[Preparing Organisations.]]', e('Protecting People. [[Preparing Organisations.]]'))
