"""Concept 1 - Editorial split, friendly. White and airy with soft mint blobs, big rounded
photos with floating badges, a zig-zag of services and gentle motion throughout."""
from common import *  # noqa: F401,F403
import content as C

NAME = "Editorial split"

CSS = r"""
/* ===== Concept 1 theme ===== */
.sms-page .sms-mark { color: var(--sms-navy); background: linear-gradient(180deg, transparent 60%, var(--sms-mint) 60%); padding: 0 0.08em; -webkit-box-decoration-break: clone; box-decoration-break: clone; }

/* Footer: navy */
.sms-footer { background: var(--sms-navy); color: rgba(255, 255, 255, 0.82); }
.sms-footer .sms-footer__heading,
.sms-footer .sms-footer__tag { color: var(--sms-white); }
.sms-footer .sms-footer__link { color: rgba(255, 255, 255, 0.82); }
.sms-footer .sms-footer__link:hover { color: var(--sms-green-on-navy); }
.sms-footer .sms-footer__base { border-color: rgba(255, 255, 255, 0.16); }

/* ---------- Page hero (split with photo) ---------- */
.sms-phero { position: relative; z-index: 0; overflow: hidden; padding: clamp(2.5rem, 1.5rem + 4vw, 5rem) 0 clamp(3.5rem, 2.5rem + 4vw, 6rem); }
.sms-phero .sms-phero__glow { position: absolute; z-index: -1; left: -10rem; top: -12rem; width: 34rem; height: 34rem; border-radius: 50%; background: var(--sms-pale-2); animation: sms-float 14s ease-in-out infinite; }
.sms-phero .sms-phero__inner { position: relative; display: grid; gap: clamp(2.5rem, 1.5rem + 4vw, 5rem); align-items: center; width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-phero .sms-phero__copy { min-width: 0; }
.sms-phero .sms-phero__crumb { margin-bottom: 1.25rem; color: var(--sms-ink-soft); font-size: var(--sms-step--1); }
.sms-phero .sms-phero__crumb-link { color: var(--sms-ink-soft); }
.sms-phero .sms-phero__eyebrow { display: inline-flex; align-items: center; gap: 0.5rem; margin-bottom: 1.1rem; padding: 0.4rem 0.9rem 0.4rem 0.45rem; border-radius: 999px; background: var(--sms-pale-2); color: var(--sms-navy); font-size: var(--sms-step--1); font-weight: 700; }
.sms-phero .sms-phero__eyebrow-icon { width: 1.6rem; height: 1.6rem; padding: 0.3rem; border-radius: 50%; background: var(--sms-green); color: var(--sms-white); }
.sms-phero .sms-phero__title { margin: 0 0 1.25rem; font-size: var(--sms-step-3); font-weight: 700; line-height: 1.08; letter-spacing: -0.025em; }
.sms-phero .sms-phero__sub { margin-bottom: 0.75rem; font-size: var(--sms-step-1); font-weight: 600; line-height: 1.45; }
.sms-phero .sms-phero__body { max-width: 34rem; color: var(--sms-ink-soft); font-size: var(--sms-step-1); line-height: 1.55; }
.sms-phero .sms-phero__body p { margin: 0 0 0.75rem; }
.sms-phero .sms-phero__actions { display: flex; flex-wrap: wrap; gap: 0.75rem; margin-top: 1.75rem; }
.sms-phero .sms-phero__media { position: relative; z-index: 0; min-width: 0; width: 100%; max-width: 30rem; margin: 0 auto; padding: 1.5rem 1.5rem 2.5rem; }
.sms-phero .sms-phero__shape { position: absolute; z-index: -1; inset: 8% 0 0 12%; border-radius: 46% 54% 44% 56% / 52% 46% 54% 48%; background: var(--sms-mint); animation: sms-float 10s ease-in-out infinite; }
.sms-phero .sms-phero__frame { aspect-ratio: 4 / 4.6; border-radius: 2rem 7rem 2rem 2rem; box-shadow: var(--sms-shadow-lg); }
.sms-phero .sms-phero__frame .sms-photo__img { animation: sms-zoom 1.4s var(--sms-ease) both; }
.sms-phero .sms-phero__chip { position: absolute; z-index: 2; display: inline-flex; align-items: center; gap: 0.5rem; max-width: 15rem; padding: 0.6rem 1rem 0.6rem 0.6rem; border-radius: 999px; background: var(--sms-white); box-shadow: var(--sms-shadow-lg); font-size: var(--sms-step--1); font-weight: 700; line-height: 1.25; animation: sms-bob 5s ease-in-out infinite; }
.sms-phero .sms-phero__chip--a { left: 0; bottom: 14%; }
.sms-phero .sms-phero__chip--b { right: 0; top: 10%; animation-delay: -2.5s; }
.sms-phero .sms-phero__chip-icon { width: 2rem; height: 2rem; padding: 0.4rem; border-radius: 50%; background: var(--sms-mint); color: var(--sms-green); }
.sms-phero .sms-phero__chip-text { min-width: 0; }
@media (min-width: 52em) {
  .sms-phero .sms-phero__inner { grid-template-columns: minmax(0, 1.1fr) minmax(0, 0.9fr); }
  .sms-phero .sms-phero__media { max-width: none; }
  .sms-phero .sms-phero__chip--a { left: -1.5rem; }
}

/* ---------- CTA (pale box with photo bubbles) ---------- */
.sms-cta { padding: var(--sms-section) 0; }
.sms-cta .sms-cta__box { position: relative; display: grid; gap: 1.75rem; align-items: center; overflow: hidden; padding: clamp(2rem, 1.2rem + 3vw, 3.75rem); border-radius: 2rem; background: var(--sms-pale); }
.sms-cta .sms-cta__wm { position: absolute; right: -3rem; bottom: -4rem; width: clamp(12rem, 9rem + 10vw, 18rem); height: auto; opacity: 0.08; pointer-events: none; animation: sms-spin 80s linear infinite; }
.sms-cta .sms-cta__faces { display: flex; min-width: 0; }
.sms-cta .sms-cta__face { flex: 0 0 auto; min-width: 0; width: clamp(4rem, 3rem + 3vw, 5.5rem); height: auto; aspect-ratio: 1; margin-right: -1rem; border: 4px solid var(--sms-pale); border-radius: 50%; box-shadow: var(--sms-shadow); transition: transform 0.3s var(--sms-ease); }
.sms-cta .sms-cta__face:hover { transform: translateY(-6px); }
.sms-cta .sms-cta__copy { position: relative; min-width: 0; }
.sms-cta .sms-cta__title { margin: 0 0 0.6rem; font-size: var(--sms-step-2); font-weight: 700; line-height: 1.2; }
.sms-cta .sms-cta__text { max-width: 38rem; color: var(--sms-ink-soft); }
.sms-cta .sms-cta__text p { margin: 0; }
.sms-cta .sms-cta__actions { position: relative; display: flex; flex-wrap: wrap; gap: 0.75rem; min-width: 0; }
@media (min-width: 56em) {
  .sms-cta .sms-cta__box { grid-template-columns: auto minmax(0, 1fr); column-gap: 2.5rem; }
  .sms-cta .sms-cta__faces { grid-row: span 2; }
}

/* ---------- Home: credentials ---------- */
.sms-creds { padding: 0 0 clamp(1rem, 0.5rem + 2vw, 2rem); }
.sms-creds .sms-creds__inner { width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-creds .sms-creds__list { display: grid; gap: 0.75rem; min-width: 0; margin: 0; padding: 0; list-style: none; }
.sms-creds .sms-creds__item { display: flex; align-items: center; gap: 0.85rem; min-width: 0; padding: 1rem 1.25rem; border-radius: var(--sms-radius); background: var(--sms-pale); font-size: var(--sms-step--1); font-weight: 600; line-height: 1.45; transition: transform 0.3s var(--sms-ease); }
.sms-creds .sms-creds__item:hover { transform: translateY(-4px); }
.sms-creds .sms-creds__badge { flex: 0 0 auto; min-width: 0; width: 3rem; height: auto; border-radius: 0.5rem; }
.sms-creds .sms-creds__icon { width: 3rem; height: 3rem; padding: 0.7rem; border-radius: 50%; background: var(--sms-white); color: var(--sms-green); }
.sms-creds .sms-creds__text { min-width: 0; }
@media (min-width: 52em) {
  .sms-creds .sms-creds__list { grid-template-columns: repeat(3, minmax(0, 1fr)); }
}

/* ---------- Home: zig-zag services ---------- */
.sms-zig { padding: var(--sms-section) 0; overflow: hidden; }
.sms-zig .sms-zig__inner { width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-zig .sms-zig__head { max-width: 40rem; margin-bottom: clamp(2.5rem, 2rem + 2vw, 4rem); }
.sms-zig .sms-zig__eyebrow { display: inline-flex; align-items: center; gap: 0.5rem; margin-bottom: 0.9rem; color: var(--sms-green); font-size: var(--sms-step--1); font-weight: 700; letter-spacing: 0.12em; text-transform: uppercase; }
.sms-zig .sms-zig__eyebrow::before { content: ""; flex: 0 0 auto; width: 1.5rem; height: 3px; border-radius: 3px; background: var(--sms-green); }
.sms-zig .sms-zig__title { margin: 0 0 1rem; font-size: var(--sms-step-2); font-weight: 700; line-height: 1.18; }
.sms-zig .sms-zig__lead { color: var(--sms-ink-soft); font-size: var(--sms-step-1); line-height: 1.55; }
.sms-zig .sms-zig__lead p { margin: 0; }
.sms-zig .sms-zig__list { display: grid; gap: clamp(3rem, 2rem + 4vw, 6rem); margin: 0; padding: 0; list-style: none; }
.sms-zig .sms-zig__item { display: grid; gap: clamp(1.5rem, 1rem + 3vw, 4rem); align-items: center; min-width: 0; }
.sms-zig .sms-zig__media { position: relative; z-index: 0; min-width: 0; }
.sms-zig .sms-zig__frame { aspect-ratio: 5 / 4; border-radius: 2rem; box-shadow: var(--sms-shadow-lg); }
.sms-zig .sms-zig__num { position: absolute; z-index: 2; left: 0.75rem; top: 0.75rem; display: grid; place-items: center; width: 3.5rem; height: 3.5rem; border-radius: 50%; background: var(--sms-green); color: var(--sms-white); font-size: var(--sms-step-1); font-weight: 700; box-shadow: var(--sms-shadow); }
.sms-zig .sms-zig__dot { position: absolute; z-index: -1; right: -1rem; bottom: -1.5rem; width: 45%; aspect-ratio: 1; border-radius: 50%; background: var(--sms-mint); animation: sms-float 11s ease-in-out infinite; }
.sms-zig .sms-zig__body { min-width: 0; }
.sms-zig .sms-zig__icon { width: 3.25rem; height: 3.25rem; margin-bottom: 1rem; padding: 0.75rem; border-radius: 1rem; background: var(--sms-mint); color: var(--sms-green); }
.sms-zig .sms-zig__name { margin: 0 0 0.75rem; font-size: var(--sms-step-2); font-weight: 700; line-height: 1.2; }
.sms-zig .sms-zig__text { max-width: 34rem; margin-bottom: 1.25rem; color: var(--sms-ink-soft); font-size: var(--sms-step-1); line-height: 1.55; }
.sms-zig .sms-zig__text p { margin: 0; }
.sms-zig .sms-zig__actions { margin-top: 1.5rem; }
.sms-zig .sms-zig__more { display: flex; flex-wrap: wrap; align-items: center; gap: 0.75rem 1.5rem; margin-top: clamp(3rem, 2rem + 3vw, 5rem); padding: 1.5rem 1.75rem; border-radius: var(--sms-radius); background: var(--sms-pale); }
.sms-zig .sms-zig__more-icon { width: 3rem; height: 3rem; padding: 0.7rem; border-radius: 50%; background: var(--sms-white); color: var(--sms-green); }
.sms-zig .sms-zig__more-text { flex: 1 1 18rem; min-width: 0; color: var(--sms-ink-soft); }
.sms-zig .sms-zig__more-text strong { color: var(--sms-navy); }
@media (min-width: 56em) {
  .sms-zig .sms-zig__item { grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); }
  .sms-zig .sms-zig__item:nth-child(even) .sms-zig__media { order: 2; }
  .sms-zig .sms-zig__num { left: -1rem; top: -1rem; width: 4rem; height: 4rem; }
}

/* ---------- Home: about ---------- */
.sms-habout { position: relative; overflow: hidden; padding: var(--sms-section) 0; background: var(--sms-pale); }
.sms-habout .sms-habout__inner { position: relative; display: grid; gap: clamp(2.5rem, 1.5rem + 4vw, 5rem); align-items: center; width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-habout .sms-habout__media { position: relative; min-width: 0; }
.sms-habout .sms-habout__frame { aspect-ratio: 4 / 3.2; border-radius: 2rem 2rem 7rem 2rem; box-shadow: var(--sms-shadow-lg); }
.sms-habout .sms-habout__claim { position: relative; z-index: 2; max-width: 22rem; margin: -3rem 1rem 0 auto; padding: 1.25rem 1.5rem; border-radius: var(--sms-radius); background: var(--sms-green); color: var(--sms-white); font-weight: 700; line-height: 1.45; box-shadow: var(--sms-shadow-lg); animation: sms-bob 6s ease-in-out infinite; }
.sms-habout .sms-habout__claim p { margin: 0; }
.sms-habout .sms-habout__main { min-width: 0; }
.sms-habout .sms-habout__eyebrow { display: inline-flex; align-items: center; gap: 0.5rem; margin-bottom: 0.9rem; color: var(--sms-green); font-size: var(--sms-step--1); font-weight: 700; letter-spacing: 0.12em; text-transform: uppercase; }
.sms-habout .sms-habout__eyebrow::before { content: ""; flex: 0 0 auto; width: 1.5rem; height: 3px; border-radius: 3px; background: var(--sms-green); }
.sms-habout .sms-habout__title { margin: 0 0 1.25rem; font-size: var(--sms-step-2); font-weight: 700; line-height: 1.18; }
.sms-habout .sms-habout__lead { color: var(--sms-navy); font-size: var(--sms-step-1); line-height: 1.55; }
.sms-habout .sms-habout__lead p { margin: 0; }
.sms-habout .sms-habout__points { display: grid; gap: 0.75rem; margin: 1.75rem 0 0; padding: 0; list-style: none; }
.sms-habout .sms-habout__point { display: flex; gap: 0.85rem; align-items: flex-start; min-width: 0; padding: 1rem 1.25rem; border-radius: var(--sms-radius); background: var(--sms-white); transition: transform 0.3s var(--sms-ease); }
.sms-habout .sms-habout__point:hover { transform: translateX(6px); }
.sms-habout .sms-habout__point-icon { width: 2.5rem; height: 2.5rem; padding: 0.55rem; border-radius: 50%; background: var(--sms-mint); color: var(--sms-green); }
.sms-habout .sms-habout__point-body { min-width: 0; }
.sms-habout .sms-habout__point-title { margin: 0 0 0.15rem; font-size: var(--sms-step-0); font-weight: 700; }
.sms-habout .sms-habout__point-text { color: var(--sms-ink-soft); font-size: var(--sms-step--1); }
.sms-habout .sms-habout__point-text p { margin: 0; }
.sms-habout .sms-habout__link { margin-top: 1.75rem; }
@media (min-width: 56em) {
  .sms-habout .sms-habout__inner { grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); }
}
"""

RISE = [".sms-phero .sms-phero__title", ".sms-phero .sms-phero__frame"]
ENTRANCE = [".sms-phero .sms-phero__eyebrow", ".sms-phero .sms-phero__sub", ".sms-phero .sms-phero__body", ".sms-phero .sms-phero__actions"]
REVEAL = [".sms-creds .sms-creds__item", ".sms-zig .sms-zig__head", ".sms-zig .sms-zig__media", ".sms-zig .sms-zig__body", ".sms-zig .sms-zig__more",
          ".sms-habout .sms-habout__media", ".sms-habout .sms-habout__main", ".sms-cta .sms-cta__box"]
LOOP = [".sms-phero .sms-phero__glow", ".sms-phero .sms-phero__shape", ".sms-phero .sms-phero__chip", ".sms-phero .sms-phero__frame .sms-photo__img",
        ".sms-cta .sms-cta__wm", ".sms-zig .sms-zig__dot", ".sms-habout .sms-habout__claim"]
TRANS = [".sms-cta .sms-cta__face", ".sms-creds .sms-creds__item", ".sms-habout .sms-habout__point"]


def page_hero(ctx, h, crumb=True):
    btns = '<div class="sms-phero__actions">%s</div>' % buttons(ctx, h["buttons"]) if h.get("buttons") else ""
    sub = '<div class="sms-phero__sub">%s</div>' % e(h["sub"]) if h.get("sub") else ""
    crumb_html = '<div class="sms-phero__crumb"><a class="sms-phero__crumb-link" href="%s">Home</a> / %s</div>' % (ctx.href("home"), e(LABEL[ctx.slug])) if crumb and ctx.slug != "home" else ""
    chips_html = ""
    for i, (ic, t) in enumerate(h.get("chips", [])[:2]):
        chips_html += '<div class="sms-phero__chip sms-phero__chip--%s">%s<span class="sms-phero__chip-text">%s</span></div>' % ("ab"[i], icon(ic, "sms-phero__chip-icon"), e(t))
    return """<section class="sms-phero">
  <div class="sms-phero__glow" aria-hidden="true"></div>
  <div class="sms-phero__inner">
    <div class="sms-phero__copy">
      %s
      <div class="sms-phero__eyebrow">%s%s</div>
      <h1 class="sms-phero__title">%s</h1>
      %s
      <div class="sms-phero__body">%s</div>
      %s
    </div>
    <div class="sms-phero__media">
      <div class="sms-phero__shape" aria-hidden="true"></div>
      %s
      %s
    </div>
  </div>
</section>
""" % (crumb_html, icon("shield", "sms-phero__eyebrow-icon"), e(h["eyebrow"]), e(h["title"]), sub, paras(h["body"]), btns,
       photo(ctx, h["photo"], lazy=False, parallax=False, figcls="sms-phero__frame"), chips_html)


def cta(ctx, d):
    faces = ""
    for k in ["directors", "team", "festival"]:
        f, w, hh, focus, alt = C.PHOTOS[k]
        ctx.photos.append("assets/photos/" + f)
        faces += '<img class="sms-cta__face" src="%s" alt="" width="%d" height="%d" loading="lazy" style="object-fit: cover; object-position: %s">' % (ctx.asset("photos/" + f), w, hh, focus)
    return """<section class="sms-cta">
  <div class="sms-cta__inner">
    <div class="sms-cta__box">
      <img class="sms-cta__wm" src="%s" alt="" width="378" height="399" loading="lazy" aria-hidden="true">
      <div class="sms-cta__faces" aria-hidden="true">%s</div>
      <div class="sms-cta__copy"><h2 class="sms-cta__title">%s</h2><div class="sms-cta__text">%s</div></div>
      <div class="sms-cta__actions">%s</div>
    </div>
  </div>
</section>
""" % (ctx.asset("streamline-shield-blue.png"), faces, e(d["title"]), paras(d["text"]), buttons(ctx, d["buttons"]))


def chrome_top(ctx):
    return header(ctx, "blue")


def chrome_bottom(ctx):
    return footer(ctx, "white")


def home(ctx):
    ctx.notes += ["Image-only copy used: \"Clinician-led safety and medical support\" (clinician-led-safety.png)",
                  "Image-only copy used: \"Mathew and Tom bring over 15 years of ambulance experience...\" (why-choose-us.png - use approved)"]
    hero = {"eyebrow": "Clinician-led safety and medical support",
            "title": "Clinician-Led Medical Cover, [[First Aid Training]] & Safety Consultancy",
            "sub": C.AREA, "body": [C.INTRO2],
            "buttons": [("Book online", "book"), ("Call 01283 358789", "tel")],
            "photo": "directors", "chips": [("award", "Qualsafe Registered Centre"), ("shield", "Fully insured")]}
    out = page_hero(ctx, hero, crumb=False)
    out += """<section class="sms-creds" aria-label="Credentials">
  <div class="sms-creds__inner">
    <ul class="sms-creds__list">
      <li class="sms-creds__item"><img class="sms-creds__badge" src="%s" alt="Qualsafe registered centre" width="1000" height="982" loading="lazy"><span class="sms-creds__text">Qualsafe Registered Centre &ndash; Centre No. 908578</span></li>
      <li class="sms-creds__item">%s<span class="sms-creds__text">Led by IOSH-qualified health and safety advisors</span></li>
      <li class="sms-creds__item">%s<span class="sms-creds__text">Fully insured, carefully planned and professionally delivered.</span></li>
    </ul>
  </div>
</section>
""" % (ctx.asset("whatsapp-image-2026-07-20-at-12.27.35.jpeg"), icon("shield", "sms-creds__icon"), icon("check", "sms-creds__icon"))
    rows = ""
    for i, s in enumerate(C.SERVICES, 1):
        rows += """<li class="sms-zig__item">
        <div class="sms-zig__media"><span class="sms-zig__num" aria-hidden="true">%02d</span><div class="sms-zig__dot" aria-hidden="true"></div>%s</div>
        <div class="sms-zig__body">
          %s
          <h3 class="sms-zig__name">%s</h3>
          <div class="sms-zig__text"><p>%s</p></div>
          %s
          <div class="sms-zig__actions">%s</div>
        </div>
      </li>""" % (i, photo(ctx, s["photo"], figcls="sms-zig__frame"), icon(s["icon"], "sms-zig__icon"), e(s["title"]), e(s["text"]), chips(s["list"]),
                  buttons(ctx, [(s["cta"], s["slug"])]))
    out += """<section class="sms-zig" id="services">
  <div class="sms-zig__inner">
    <div class="sms-zig__head"><div class="sms-zig__eyebrow">Our Services</div><h2 class="sms-zig__title">What We <span class="sms-mark">Provide</span></h2><div class="sms-zig__lead"><p>%s</p></div></div>
    <ol class="sms-zig__list">%s</ol>
    <div class="sms-zig__more">%s<div class="sms-zig__more-text"><strong>%s.</strong> %s</div>%s</div>
  </div>
</section>
""" % (e(C.INTRO), rows, icon(C.CAREERS["icon"], "sms-zig__more-icon"), e(C.CAREERS["title"]), e(C.CAREERS["text"]), buttons(ctx, [(C.CAREERS["cta"], C.CAREERS["slug"])]))
    pts = "".join('<li class="sms-habout__point">%s<div class="sms-habout__point-body"><h3 class="sms-habout__point-title">%s</h3><div class="sms-habout__point-text"><p>%s</p></div></div></li>' % (
        icon(ic, "sms-habout__point-icon"), e(t), e(x)) for ic, t, x in C.TRUST)
    out += """<section class="sms-habout" id="about">
  <div class="sms-habout__inner">
    <div class="sms-habout__media">%s<div class="sms-habout__claim"><p>%s</p></div></div>
    <div class="sms-habout__main">
      <div class="sms-habout__eyebrow">About Streamline</div>
      <h2 class="sms-habout__title">Protecting People. <span class="sms-mark">Preparing Organisations.</span></h2>
      <div class="sms-habout__lead"><p>%s</p></div>
      %s
      <ul class="sms-habout__points">%s</ul>
      <a class="sms-btn sms-btn--outline sms-habout__link" href="%s">Meet The Directors</a>
    </div>
  </div>
</section>
""" % (photo(ctx, "team", figcls="sms-habout__frame"), e(C.CLAIM_15), e(C.ABOUT_HOME[0]), more(paras(C.ABOUT_HOME[1:])), pts, ctx.href("about"))
    out += SHARED_RENDERERS["marquee"](ctx, {"eyebrow": "Who does Streamline work with?", "items": C.WHO})
    picks = ["Where is Streamline based?", "Who runs Streamline?", "Can Streamline provide more than one service?", "Do you offer a free initial discussion?", "Are you insured?", "How can I contact Streamline?"]
    allf = dict(C.faqs("home"))
    out += SHARED_RENDERERS["faq"](ctx, {"tone": "pale", "eyebrow": C.STRAP, "title": "General Streamline FAQs",
                                        "lead": ["Answers to common questions about Streamline Safety & Medical Solutions, our team, services, bookings and how we work."],
                                        "items": [(q, allf[q]) for q in picks], "show": 6})
    out += cta(ctx, {"title": "Still have a question?", "text": ["Speak to our team and we will be happy to help."],
                     "buttons": [("Book online", "book"), ("Contact Streamline", "contact")]})
    return out
