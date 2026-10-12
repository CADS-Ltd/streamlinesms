"""Concept 2 - Centred statement. Light and friendly: pale-green centred heroes with the
logo shield behind, wide photos overlapping the hero, cards, a green CTA band, light footer."""
from common import *  # noqa: F401,F403
import content as C

NAME = "Centred statement"

CSS = r"""
/* ===== Concept 2 theme ===== */
.sms-page { --sms-radius: 1rem; }
.sms-page .sms-btn { border-radius: 999px; }
.sms-page .sms-mark { color: var(--sms-green); }
.sms-cards .sms-cards__item { border: 0; border-top: 4px solid var(--sms-green); box-shadow: 0 12px 32px rgba(6, 30, 53, 0.07); }
.sms-steps .sms-steps__item { border: 0; box-shadow: 0 12px 32px rgba(6, 30, 53, 0.07); }
.sms-cards .sms-cards__head,
.sms-steps .sms-steps__head,
.sms-people .sms-people__head,
.sms-links .sms-links__head,
.sms-checklist .sms-checklist__head { margin-left: auto; margin-right: auto; text-align: center; }
.sms-checklist .sms-checklist__list { justify-content: center; }
.sms-steps .sms-steps__note { margin-left: auto; margin-right: auto; text-align: center; }

/* Footer: light */
.sms-footer { border-top: 1px solid var(--sms-line-green); background: var(--sms-pale); color: var(--sms-navy); }
.sms-footer .sms-footer__link { color: var(--sms-navy); }
.sms-footer .sms-footer__link:hover { color: var(--sms-green); }
.sms-footer .sms-footer__heading { color: var(--sms-green); }
.sms-footer .sms-footer__base { border-color: var(--sms-line-green); color: var(--sms-ink-soft); }
.sms-footer .sms-footer__badge { border: 1px solid var(--sms-line); }

/* ---------- Page hero (centred, light) ---------- */
.sms-phero { position: relative; }
.sms-phero .sms-phero__band { position: relative; overflow: hidden; padding: clamp(3rem, 2rem + 4vw, 6rem) 0 clamp(3rem, 2rem + 4vw, 5.5rem); background: var(--sms-pale); text-align: center; }
.sms-phero.sms-phero--photo .sms-phero__band { padding-bottom: clamp(8rem, 5rem + 12vw, 15rem); }
.sms-phero .sms-phero__wm { position: absolute; left: 50%; top: 50%; width: clamp(18rem, 12rem + 30vw, 40rem); height: auto; opacity: 0.06; transform: translate(-50%, -50%); pointer-events: none; }
.sms-phero .sms-phero__inner { position: relative; width: 100%; max-width: 58rem; margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-phero .sms-phero__crumb { margin-bottom: 1.25rem; color: var(--sms-ink-soft); font-size: var(--sms-step--1); }
.sms-phero .sms-phero__crumb-link { color: var(--sms-ink-soft); }
.sms-phero .sms-phero__eyebrow { display: inline-block; margin-bottom: 1.25rem; padding: 0.4rem 1rem; border-radius: 999px; background: var(--sms-white); color: var(--sms-green); font-size: var(--sms-step--1); font-weight: 700; letter-spacing: 0.1em; text-transform: uppercase; }
.sms-phero .sms-phero__title { margin: 0 auto 1.25rem; font-size: var(--sms-step-3); font-weight: 700; line-height: 1.1; letter-spacing: -0.02em; }
.sms-phero .sms-phero__sub { margin-bottom: 1rem; font-size: var(--sms-step-1); font-weight: 600; }
.sms-phero .sms-phero__body { max-width: 42rem; margin: 0 auto; color: var(--sms-ink-soft); font-size: var(--sms-step-1); line-height: 1.6; }
.sms-phero .sms-phero__body p { margin: 0 0 0.75rem; }
.sms-phero .sms-phero__actions { display: flex; flex-wrap: wrap; justify-content: center; gap: 0.75rem; margin-top: 2rem; }
.sms-phero .sms-phero__note { margin-top: 1.75rem; color: var(--sms-ink-soft); font-size: var(--sms-step--1); font-weight: 600; }
.sms-phero .sms-phero__media { position: relative; width: 100%; max-width: var(--sms-max); margin: clamp(-12rem, -4rem - 9vw, -6rem) auto 0; padding: 0 var(--sms-gutter); }
.sms-phero .sms-phero__img { display: block; width: 100%; height: auto; border-radius: var(--sms-radius); box-shadow: 0 20px 50px rgba(6, 30, 53, 0.12); }

/* ---------- CTA band (green) ---------- */
.sms-cta { position: relative; overflow: hidden; padding: clamp(3.5rem, 2.5rem + 4vw, 6rem) 0; background: var(--sms-green); color: var(--sms-white); text-align: center; }
.sms-cta .sms-cta__wm { position: absolute; right: -3rem; bottom: -5rem; width: clamp(14rem, 10rem + 16vw, 24rem); height: auto; opacity: 0.12; pointer-events: none; }
.sms-cta .sms-cta__inner { position: relative; }
.sms-cta .sms-cta__title { margin: 0 auto 0.75rem; max-width: 40rem; font-size: var(--sms-step-2); font-weight: 700; line-height: 1.2; }
.sms-cta .sms-cta__text { max-width: 40rem; margin: 0 auto; }
.sms-cta .sms-cta__text p { margin: 0; }
.sms-cta .sms-cta__actions { display: flex; flex-wrap: wrap; justify-content: center; gap: 0.75rem; margin-top: 2rem; }
.sms-cta .sms-cta__btn { display: inline-block; min-width: 0; padding: 0.9rem 1.4rem; border: 2px solid var(--sms-white); border-radius: 999px; font-size: var(--sms-step--1); font-weight: 600; text-decoration: none; transition: transform 0.2s ease; }
.sms-cta .sms-cta__btn:hover { transform: translateY(-2px); }
.sms-cta .sms-cta__btn--main { background: var(--sms-white); color: var(--sms-navy); }
.sms-cta .sms-cta__btn--alt { background: transparent; color: var(--sms-white); }

/* ---------- Home: why strip ---------- */
.sms-why { padding: clamp(3rem, 2rem + 3vw, 4.5rem) 0; }
.sms-why .sms-why__inner { width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-why .sms-why__list { display: grid; gap: 2rem; margin: 0; padding: 0; list-style: none; }
.sms-why .sms-why__item { min-width: 0; text-align: center; }
.sms-why .sms-why__icon { display: block; width: 2.75rem; height: auto; margin: 0 auto 1rem; }
.sms-why .sms-why__title { margin: 0 0 0.4rem; font-size: var(--sms-step-0); font-weight: 700; }
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
.sms-hsvc .sms-hsvc__title { margin: 0 0 1rem; font-size: var(--sms-step-2); font-weight: 700; line-height: 1.2; }
.sms-hsvc .sms-hsvc__lead { color: var(--sms-ink-soft); }
.sms-hsvc .sms-hsvc__lead p { margin: 0; }
.sms-hsvc .sms-hsvc__grid { display: grid; gap: clamp(1rem, 0.6rem + 1.5vw, 1.75rem); margin: 0; padding: 0; list-style: none; }
.sms-hsvc .sms-hsvc__card { display: flex; flex-direction: column; min-width: 0; overflow: hidden; border-radius: var(--sms-radius); background: var(--sms-white); box-shadow: 0 12px 32px rgba(6, 30, 53, 0.07); transition: transform 0.25s ease; }
.sms-hsvc .sms-hsvc__card:hover { transform: translateY(-4px); }
.sms-hsvc .sms-hsvc__media { min-width: 0; margin: 0; }
.sms-hsvc .sms-hsvc__img { display: block; width: 100%; height: auto; }
.sms-hsvc .sms-hsvc__body { display: flex; flex: 1 1 auto; flex-direction: column; min-width: 0; padding: clamp(1.5rem, 1.1rem + 1.5vw, 2.25rem); border-top: 4px solid var(--sms-green); }
.sms-hsvc .sms-hsvc__name { margin: 0 0 0.6rem; font-size: var(--sms-step-1); font-weight: 700; line-height: 1.3; }
.sms-hsvc .sms-hsvc__text { margin-bottom: 1rem; color: var(--sms-ink-soft); }
.sms-hsvc .sms-hsvc__text p { margin: 0; }
.sms-hsvc .sms-hsvc__points { margin: 0 0 1.5rem; padding: 0; list-style: none; font-size: var(--sms-step--1); }
.sms-hsvc .sms-hsvc__point { position: relative; min-width: 0; padding: 0.4rem 0 0.4rem 1.25rem; border-top: 1px solid var(--sms-line); }
.sms-hsvc .sms-hsvc__point::before { content: ""; position: absolute; left: 0; top: 0.95rem; width: 0.4rem; height: 0.4rem; border-radius: 50%; background: var(--sms-green); }
.sms-hsvc .sms-hsvc__link { align-self: flex-start; min-width: 0; margin-top: auto; }
.sms-hsvc .sms-hsvc__extra { display: flex; flex-wrap: wrap; align-items: center; justify-content: center; gap: 0.75rem 1.5rem; margin-top: 2rem; text-align: center; }
.sms-hsvc .sms-hsvc__extra-text { min-width: 0; color: var(--sms-ink-soft); }
.sms-hsvc .sms-hsvc__extra-link { min-width: 0; color: var(--sms-green); font-weight: 700; text-decoration: none; }
@media (min-width: 46em) and (max-width: 59.99em) {
  .sms-hsvc .sms-hsvc__card { flex-direction: row; }
  .sms-hsvc .sms-hsvc__media { flex: 0 0 38%; }
  .sms-hsvc .sms-hsvc__img { height: 100%; object-fit: cover; }
  .sms-hsvc .sms-hsvc__body { border-top: 0; border-left: 4px solid var(--sms-green); }
}
@media (min-width: 60em) {
  .sms-hsvc .sms-hsvc__grid { grid-template-columns: repeat(3, minmax(0, 1fr)); }
}
"""

RISE = [".sms-phero .sms-phero__title"]
REVEAL = [".sms-phero .sms-phero__media", ".sms-why .sms-why__item", ".sms-hsvc .sms-hsvc__card", ".sms-cta .sms-cta__inner"]
TRANS = [".sms-cta .sms-cta__btn", ".sms-hsvc .sms-hsvc__card"]


def page_hero(ctx, h, crumb=True):
    btns = '<div class="sms-phero__actions">%s</div>' % buttons(ctx, h["buttons"]) if h.get("buttons") else ""
    sub = '<div class="sms-phero__sub">%s</div>' % e(h["sub"]) if h.get("sub") else ""
    note = '<div class="sms-phero__note">%s</div>' % e(h["note"]) if h.get("note") else ""
    crumb_html = '<div class="sms-phero__crumb"><a class="sms-phero__crumb-link" href="%s">Home</a> / %s</div>' % (ctx.href("home"), e(LABEL[ctx.slug])) if crumb and ctx.slug != "home" else ""
    media = ""
    if h.get("photo"):
        media = '<figure class="sms-phero__media">%s</figure>' % ctx.ph("wide", "Placeholder for a genuine photo of " + h["photo"], h["photo"], "sms-phero__img", lazy=False)
    return """<section class="sms-phero%s">
  <div class="sms-phero__band">
    <img class="sms-phero__wm" src="%s" alt="" width="378" height="399" aria-hidden="true">
    <div class="sms-phero__inner">
      %s
      <div class="sms-phero__eyebrow">%s</div>
      <h1 class="sms-phero__title">%s</h1>
      %s
      <div class="sms-phero__body">%s</div>
      %s
      %s
    </div>
  </div>
  %s
</section>
""" % (" sms-phero--photo" if media else "", ctx.asset("streamline-shield-blue.png"), crumb_html, e(h["eyebrow"]), e(h["title"]), sub, paras(h["body"]), btns, note, media)


def cta(ctx, d):
    btns = "".join('<a class="sms-cta__btn sms-cta__btn--%s" href="%s">%s</a>' % ("main" if i == 0 else "alt", link(ctx, t), e(l)) for i, (l, t) in enumerate(d["buttons"]))
    return """<section class="sms-cta">
  <img class="sms-cta__wm" src="%s" alt="" width="374" height="395" loading="lazy" aria-hidden="true">
  <div class="sms-cta__inner">
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
    ctx.image_text.append("\"Mathew and Tom bring over 15 years of ambulance experience...\" (why-choose-us.png - use approved)")
    hero = {"eyebrow": C.STRAP, "title": "Clinician-Led Medical Cover, [[First Aid Training]] & Safety Consultancy",
            "body": [C.AREA],
            "buttons": [("Book your next training session", "medical-training"), ("Book us for your medical cover", "event-medical-cover"), ("Book a free consultation for your business", "risk-needs-consultancy")],
            "note": "Qualsafe Registered Centre – Centre No. 908578",
            "photo": "the Streamline team at work at an event"}
    out = page_hero(ctx, hero, crumb=False)
    why = "".join('<li class="sms-why__item"><img class="sms-why__icon" src="%s" alt="" width="378" height="399" loading="lazy" aria-hidden="true"><h3 class="sms-why__title">%s</h3><div class="sms-why__text"><p>%s</p></div></li>' % (ctx.asset("streamline-shield-blue.png"), e(t), e(x)) for t, x in C.TRUST)
    out += """<section class="sms-why" aria-labelledby="sms-why-title">
  <div class="sms-why__inner">
    <h2 class="sms-visually-hidden" id="sms-why-title">Why Choose Streamline?</h2>
    <ul class="sms-why__list">%s</ul>
  </div>
</section>
""" % why
    cards = ""
    for s in C.SERVICES:
        pts = "".join('<li class="sms-hsvc__point">%s</li>' % e(x) for x in s["list"][:4])
        cards += """<li class="sms-hsvc__card">
        <figure class="sms-hsvc__media">%s</figure>
        <div class="sms-hsvc__body">
          <h3 class="sms-hsvc__name">%s</h3>
          <div class="sms-hsvc__text"><p>%s</p></div>
          <ul class="sms-hsvc__points">%s</ul>
          <a class="sms-btn sms-btn--primary sms-hsvc__link" href="%s">%s</a>
        </div>
      </li>""" % (ctx.ph("landscape", "Placeholder for a genuine photo of Streamline " + s["title"].lower(), s["title"] + " card photo", "sms-hsvc__img"),
                  e(s["title"]), e(s["text"]), pts, ctx.href(s["slug"]), e(s["cta"]))
    out += """<section class="sms-hsvc" id="services">
  <div class="sms-hsvc__inner">
    <div class="sms-hsvc__head"><h2 class="sms-hsvc__title">What We [[Provide]]</h2><div class="sms-hsvc__lead"><p>%s</p></div></div>
    <ul class="sms-hsvc__grid">%s</ul>
    <div class="sms-hsvc__extra"><span class="sms-hsvc__extra-text">%s</span><a class="sms-hsvc__extra-link" href="%s">%s&nbsp;<span class="sms-arrow" aria-hidden="true">&rarr;</span></a></div>
  </div>
</section>
""" % (e(C.INTRO), cards, e(C.CAREERS["text"]), ctx.href(C.CAREERS["slug"]), e(C.CAREERS["title"]))
    out = out.replace("What We [[Provide]]", e("What We [[Provide]]"))
    people = [dict(p, bio=p["bio"][:1]) for p in C.DIRECTORS]
    out += SHARED_RENDERERS["people"](ctx, {"eyebrow": "Our Leadership Team", "title": "Meet The [[Directors.]]",
                                           "lead": ["At Streamline Safety & Medical Solutions, our leadership team brings together frontline ambulance experience, clinical knowledge, training expertise, and practical health and safety insight."],
                                           "items": people})
    out += SHARED_RENDERERS["claim"](ctx, {"tone": "pale", "text": C.CLAIM_15, "watermark": True})
    out += cta(ctx, {"title": "Contact Streamline", "text": ["Have any questions? We’re here to help."],
                     "buttons": [("Contact Us", "contact"), ("Call 01283 358789", "tel")]})
    return out
