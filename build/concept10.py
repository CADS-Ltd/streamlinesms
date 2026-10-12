"""Concept 10 - Horizon. The calm, cinematic feel of the Pristine Motors round 4
concepts with new elements, in Streamline's original colours: a slow film strip of
photos under the hero, a big typographic service list with a photo that follows the
pointer, the mission statement lighting up word by word as you scroll, a
where-we-work map that pulses out from Swadlincote, and a booking journey that
scrolls sideways as you scroll down."""
from common import *  # noqa: F401,F403
import content as C
import light

NAME = "Horizon"
DARK = False
CINE = True
FONTS = "https://fonts.googleapis.com/css2?family=Montserrat:wght@200;300;400;500;600;700&display=swap"

CSS = light.css([".sms-hcta .sms-hcta__box", ".sms-hhero .sms-hhero__chips", ".sms-footer"]) + r"""
/* ===== Concept 10 theme: horizon ===== */
.sms-page { --sms-radius: 1.5rem; --sms-radius-sm: 0.9rem; --sms-hw: 200; }
.sms-page .sms-mark { color: var(--sms-title); font-weight: 700; }
.sms-page .sms-kicker::before { box-shadow: none; }

/* ---------- Page hero (inner pages): big type, then a wide photo band ---------- */
.sms-hhero { position: relative; padding: clamp(3rem, 2rem + 4vw, 6rem) 0 0; background: linear-gradient(180deg, var(--sms-pale), var(--sms-bg) 70%); }
.sms-hhero .sms-hhero__inner { width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-hhero .sms-hhero__crumb { margin-bottom: 1.5rem; color: var(--sms-ink-soft); font-size: var(--sms-step--1); }
.sms-hhero .sms-hhero__crumb-link { color: var(--sms-ink); }
.sms-hhero .sms-hhero__title { max-width: 15em; margin: 0 0 2rem; color: var(--sms-title); font-size: clamp(2.5rem, 1.3rem + 4.8vw, 5.6rem); font-weight: 200; line-height: 1.03; letter-spacing: -0.04em; }
.sms-hhero .sms-hhero__row { display: grid; gap: 1.5rem; align-items: end; padding-top: 2rem; border-top: 1px solid var(--sms-line); }
.sms-hhero .sms-hhero__lead { max-width: 38rem; min-width: 0; color: var(--sms-ink); font-size: var(--sms-step-1); font-weight: 300; line-height: 1.65; }
.sms-hhero .sms-hhero__lead p { margin: 0 0 0.75rem; }
.sms-hhero .sms-hhero__sub { margin-bottom: 0.5rem; color: var(--sms-accent); font-weight: 500; }
.sms-hhero .sms-hhero__actions { display: flex; flex-wrap: wrap; gap: 0.75rem; min-width: 0; }
.sms-hhero .sms-hhero__band { position: relative; width: 100%; max-width: var(--sms-max); margin: clamp(2rem, 1.5rem + 2vw, 3.5rem) auto 0; padding: 0 var(--sms-gutter); }
.sms-hhero .sms-hhero__frame { aspect-ratio: 21 / 8; box-shadow: var(--sms-shadow-lg); }
.sms-hhero .sms-hhero__chips { position: absolute; left: calc(var(--sms-gutter) + 1rem); bottom: 1rem; display: flex; flex-wrap: wrap; gap: 0.5rem; max-width: calc(100% - 2 * var(--sms-gutter) - 2rem); background: transparent; }
.sms-hhero .sms-hhero__chip { display: inline-flex; align-items: center; gap: 0.5rem; min-width: 0; padding: 0.5rem 0.95rem 0.5rem 0.6rem; border-radius: 999px; background: rgba(6, 30, 53, 0.78); color: #ffffff; font-size: var(--sms-step--1); -webkit-backdrop-filter: blur(8px); backdrop-filter: blur(8px); }
.sms-hhero .sms-hhero__chip-icon { width: 1.1rem; height: 1.1rem; color: var(--sms-accent); }
.sms-hhero .sms-hhero__chip-text { min-width: 0; }
@media (min-width: 60em) {
  .sms-hhero .sms-hhero__row { grid-template-columns: minmax(0, 1fr) auto; }
}
@media (max-width: 40em) {
  .sms-hhero .sms-hhero__frame { aspect-ratio: 4 / 3; }
}

/* ---------- CTA (navy panel) ---------- */
.sms-hcta { padding: var(--sms-section) 0; }
.sms-hcta .sms-hcta__inner { width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-hcta .sms-hcta__box { position: relative; overflow: hidden; padding: clamp(2.5rem, 1.5rem + 4vw, 5.5rem) clamp(1.5rem, 1rem + 3vw, 4rem); border-radius: var(--sms-radius); background: radial-gradient(70% 90% at 50% 120%, rgba(64, 127, 54, 0.55), transparent 70%), linear-gradient(180deg, #0b2a47, #061e35); text-align: center; }
.sms-hcta .sms-hcta__line { position: absolute; left: 10%; right: 10%; bottom: 2.25rem; height: 1px; background: linear-gradient(90deg, transparent, rgba(130, 208, 110, 0.5), transparent); opacity: 0.6; transform-origin: center; animation: sms-breathe 6s ease-in-out infinite; pointer-events: none; }
.sms-hcta .sms-hcta__title { position: relative; max-width: 16em; margin: 0 auto 1rem; color: var(--sms-title); font-size: clamp(2.1rem, 1.3rem + 3.2vw, 4rem); font-weight: 200; line-height: 1.06; letter-spacing: -0.035em; }
.sms-hcta .sms-hcta__text { position: relative; max-width: 36rem; margin: 0 auto; color: var(--sms-ink-soft); }
.sms-hcta .sms-hcta__text p { margin: 0; }
.sms-hcta .sms-hcta__actions { position: relative; display: flex; flex-wrap: wrap; justify-content: center; gap: 0.75rem; margin-top: 2rem; }
.sms-hcta .sms-hcta__call { position: relative; margin-top: 1rem; color: var(--sms-ink-soft); font-size: var(--sms-step--1); }
.sms-hcta .sms-hcta__call a { color: var(--sms-title); text-underline-offset: 4px; }
@keyframes sms-breathe { 0%, 100% { transform: scaleX(0.6); } 50% { transform: scaleX(1); } }

/* ---------- Home hero with a drifting film strip ---------- */
.sms-horizon { position: relative; overflow: hidden; padding: clamp(3.5rem, 2.5rem + 4vw, 6.5rem) 0 clamp(2.5rem, 2rem + 2vw, 4rem); background: linear-gradient(180deg, var(--sms-pale), var(--sms-bg) 75%); }
.sms-horizon .sms-horizon__inner { width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-horizon .sms-horizon__title { max-width: 14em; margin: 0 0 2.25rem; color: var(--sms-title); font-size: clamp(2.5rem, 1.2rem + 5vw, 5.9rem); font-weight: 200; line-height: 1.02; letter-spacing: -0.045em; }
.sms-horizon .sms-horizon__row { display: grid; gap: 1.5rem; align-items: end; padding-top: 2rem; border-top: 1px solid var(--sms-line); }
.sms-horizon .sms-horizon__lead { max-width: 36rem; min-width: 0; color: var(--sms-ink); font-size: var(--sms-step-1); font-weight: 300; line-height: 1.65; }
.sms-horizon .sms-horizon__lead p { margin: 0 0 0.6rem; }
.sms-horizon .sms-horizon__area { color: var(--sms-ink-soft); font-size: var(--sms-step--1); }
.sms-horizon .sms-horizon__actions { display: flex; flex-wrap: wrap; gap: 0.75rem; min-width: 0; }
.sms-horizon .sms-horizon__strip { margin-top: clamp(2.5rem, 2rem + 2vw, 4rem); overflow: hidden; -webkit-mask-image: linear-gradient(90deg, transparent, #000 6%, #000 94%, transparent); mask-image: linear-gradient(90deg, transparent, #000 6%, #000 94%, transparent); }
.sms-horizon .sms-horizon__track { display: flex; gap: 1rem; width: max-content; margin: 0; padding: 0 0 0.5rem; list-style: none; animation: sms-film 70s linear infinite; }
.sms-horizon .sms-horizon__strip:hover .sms-horizon__track,
.sms-horizon .sms-horizon__strip:focus-within .sms-horizon__track { animation-play-state: paused; }
.sms-horizon .sms-horizon__item { min-width: 0; }
.sms-horizon .sms-horizon__card { position: relative; display: block; width: clamp(13rem, 10rem + 9vw, 19rem); overflow: hidden; border-radius: 1.25rem; color: #ffffff; text-decoration: none; }
.sms-horizon .sms-horizon__img { display: block; width: 100%; height: auto; aspect-ratio: 4 / 5; object-fit: cover; transition: transform 1.2s var(--sms-ease); }
.sms-horizon .sms-horizon__card:hover .sms-horizon__img { transform: scale(1.05); }
.sms-horizon .sms-horizon__cap { position: absolute; left: 0; right: 0; bottom: 0; padding: 3rem 1.1rem 1rem; background: linear-gradient(0deg, rgba(6, 30, 53, 0.85), transparent); font-size: var(--sms-step--1); font-weight: 500; }
@keyframes sms-film { to { transform: translateX(-50%); } }
@media (min-width: 60em) {
  .sms-horizon .sms-horizon__row { grid-template-columns: minmax(0, 1fr) auto; }
}

/* ---------- Service index with a photo that follows the pointer ---------- */
.sms-svc { position: relative; padding: var(--sms-section) 0; }
.sms-svc .sms-svc__inner { width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-svc .sms-svc__head { display: grid; gap: 1.25rem; align-items: end; margin-bottom: clamp(2rem, 1.5rem + 2vw, 3rem); }
.sms-svc .sms-svc__heading { min-width: 0; }
.sms-svc .sms-svc__title { margin: 0; color: var(--sms-title); font-size: clamp(2.2rem, 1.3rem + 3.4vw, 4.2rem); font-weight: 200; line-height: 1.05; letter-spacing: -0.035em; }
.sms-svc .sms-svc__intro { max-width: 28rem; min-width: 0; color: var(--sms-ink-soft); }
.sms-svc .sms-svc__intro p { margin: 0; }
.sms-svc .sms-svc__list { margin: 0; padding: 0; border-top: 1px solid var(--sms-line); list-style: none; }
.sms-svc .sms-svc__item { min-width: 0; border-bottom: 1px solid var(--sms-line); }
.sms-svc .sms-svc__link { position: relative; display: grid; grid-template-columns: 2.5rem minmax(0, 1fr) auto; gap: 0.5rem 1.25rem; align-items: center; padding: clamp(1.25rem, 1rem + 1vw, 2rem) 0; color: var(--sms-ink); text-decoration: none; }
.sms-svc .sms-svc__num { min-width: 0; color: var(--sms-ink-soft); font-size: 0.8125rem; letter-spacing: 0.18em; }
.sms-svc .sms-svc__body { min-width: 0; }
.sms-svc .sms-svc__name { display: block; color: var(--sms-title); font-size: clamp(1.7rem, 1.1rem + 2.6vw, 3.4rem); font-weight: 200; line-height: 1.08; letter-spacing: -0.03em; transition: transform 0.6s var(--sms-ease); }
.sms-svc .sms-svc__line { display: block; margin-top: 0.35rem; color: var(--sms-ink-soft); font-size: var(--sms-step--1); }
.sms-svc .sms-svc__thumb { display: block; width: 5.5rem; height: 4.25rem; border-radius: 0.75rem; object-fit: cover; }
.sms-svc .sms-svc__go { position: absolute; right: 0; top: 50%; display: none; place-items: center; width: 3rem; height: 3rem; margin-top: -1.5rem; border-radius: 50%; box-shadow: inset 0 0 0 1px var(--sms-ring-line); transition: transform 0.5s var(--sms-ease), background-color 0.4s, color 0.4s; }
.sms-svc .sms-svc__go-icon { width: 1.1rem; height: 1.1rem; }
.sms-svc .sms-svc__link:hover .sms-svc__name,
.sms-svc .sms-svc__link:focus-visible .sms-svc__name { transform: translateX(0.75rem); }
.sms-svc .sms-svc__link:hover .sms-svc__go { background: var(--sms-accent); color: var(--sms-on-accent); transform: rotate(-45deg); }
.sms-svc .sms-svc__float { position: absolute; left: 0; top: 0; z-index: 3; width: 17rem; aspect-ratio: 4 / 3; overflow: hidden; border-radius: 1.1rem; box-shadow: 0 30px 60px rgba(6, 30, 53, 0.25); opacity: 0; transform: translate3d(var(--fx, 0px), var(--fy, 0px), 0) scale(0.9); transition: opacity 0.35s var(--sms-ease), transform 0.35s var(--sms-ease); pointer-events: none; }
.sms-svc .sms-svc__float.is-on { opacity: 1; transform: translate3d(var(--fx, 0px), var(--fy, 0px), 0) scale(1); }
.sms-svc .sms-svc__float-img { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; opacity: 0; transition: opacity 0.35s; }
.sms-svc .sms-svc__float-img.is-on { opacity: 1; }
.sms-svc.is-live .sms-svc__thumb { display: none; }
.sms-svc.is-live .sms-svc__go { display: grid; }
.sms-svc.is-live .sms-svc__link { padding-right: 4rem; }
@media (min-width: 60em) {
  .sms-svc .sms-svc__head { grid-template-columns: minmax(0, 1.2fr) minmax(0, 0.8fr); }
  .sms-svc .sms-svc__intro { justify-self: end; }
  .sms-svc .sms-svc__link { grid-template-columns: 4rem minmax(0, 1fr) auto; padding-right: 4rem; }
}

/* ---------- Mission and vision that light up word by word ---------- */
.sms-scrub { padding: var(--sms-section) 0; background: var(--sms-pale); view-timeline-name: --sms-scrub; }
.sms-scrub .sms-scrub__inner { width: 100%; max-width: 62rem; margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-scrub .sms-scrub__block { margin: 0; }
.sms-scrub .sms-scrub__block + .sms-scrub__block { margin-top: clamp(2.5rem, 2rem + 2vw, 4rem); }
.sms-scrub .sms-scrub__text { margin: 0; color: var(--sms-title); font-size: clamp(1.6rem, 1.1rem + 2.2vw, 3rem); font-weight: 300; line-height: 1.3; letter-spacing: -0.02em; }
.sms-scrub .sms-scrub__text p { margin: 0; }
.sms-scrub .sms-scrub__w { display: inline; }
.sms-scrub .sms-scrub__cite { display: block; margin-top: 1.25rem; color: var(--sms-ink-soft); font-size: var(--sms-step--1); font-style: normal; }
.sms-scrub .sms-scrub__more { margin-top: 2rem; }
@supports (animation-timeline: view()) {
  @keyframes sms-word { from { opacity: 0.16; } to { opacity: 1; } }
  .sms-scrub .sms-scrub__w { animation: sms-word linear both; animation-timeline: view(); animation-range: cover 18% cover 42%; }
}

/* ---------- Where we work: a map that pulses out from Swadlincote ---------- */
.sms-area { padding: var(--sms-section) 0; }
.sms-area .sms-area__inner { display: grid; gap: clamp(2.5rem, 1.5rem + 4vw, 5rem); align-items: center; width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-area .sms-area__copy { min-width: 0; }
.sms-area .sms-area__title { margin: 0 0 1.5rem; color: var(--sms-title); font-size: clamp(2.2rem, 1.3rem + 3.2vw, 4rem); font-weight: 200; line-height: 1.05; letter-spacing: -0.035em; }
.sms-area .sms-area__text { max-width: 32rem; color: var(--sms-ink-soft); }
.sms-area .sms-area__text p { margin: 0 0 1rem; }
.sms-area .sms-area__places { margin-top: 1.5rem; }
.sms-area .sms-area__visual { position: relative; min-width: 0; padding: clamp(1rem, 0.6rem + 1.5vw, 1.75rem); border-radius: var(--sms-radius); background: var(--sms-pale); box-shadow: inset 0 0 0 1px var(--sms-line); }
.sms-area .sms-area__map { position: relative; }
.sms-area .sms-area__svg { display: block; width: 100%; height: auto; }
.sms-area .sms-area__pulse { position: absolute; left: 50%; top: 50%; width: 22%; aspect-ratio: 1; margin: -11% 0 0 -11%; border-radius: 50%; box-shadow: inset 0 0 0 2px rgba(64, 127, 54, 0.6); opacity: 0; animation: sms-pulse 4.5s ease-out infinite; pointer-events: none; }
.sms-area .sms-area__pulse--2 { animation-delay: 1.5s; }
.sms-area .sms-area__pulse--3 { animation-delay: 3s; }
@keyframes sms-pulse { 0% { opacity: 0.9; transform: scale(0.3); } 100% { opacity: 0; transform: scale(3.4); } }
@media (min-width: 60em) {
  .sms-area .sms-area__inner { grid-template-columns: minmax(0, 0.85fr) minmax(0, 1.15fr); }
}

/* ---------- Booking journey that scrolls sideways ---------- */
.sms-hscroll { position: relative; padding: var(--sms-section) 0; view-timeline-name: --sms-hscroll; }
.sms-hscroll .sms-hscroll__sticky { width: 100%; }
.sms-hscroll .sms-hscroll__head { display: grid; gap: 1.25rem; align-items: end; width: 100%; max-width: var(--sms-max); margin: 0 auto clamp(1.75rem, 1.25rem + 2vw, 3rem); padding: 0 var(--sms-gutter); }
.sms-hscroll .sms-hscroll__heading { min-width: 0; }
.sms-hscroll .sms-hscroll__title { margin: 0; color: var(--sms-title); font-size: clamp(2.2rem, 1.3rem + 3.2vw, 4rem); font-weight: 200; line-height: 1.05; letter-spacing: -0.035em; }
.sms-hscroll .sms-hscroll__intro { max-width: 28rem; min-width: 0; color: var(--sms-ink-soft); }
.sms-hscroll .sms-hscroll__intro p { margin: 0; }
.sms-hscroll .sms-hscroll__viewport { overflow-x: auto; padding: 0 var(--sms-gutter) 1rem; scroll-snap-type: x mandatory; scrollbar-width: thin; }
.sms-hscroll .sms-hscroll__track { display: flex; gap: 1rem; width: max-content; margin: 0 auto; padding: 0; list-style: none; }
.sms-hscroll .sms-hscroll__card { display: flex; flex-direction: column; width: min(78vw, 24rem); min-width: 0; min-height: 20rem; padding: clamp(1.5rem, 1rem + 1.5vw, 2.25rem); border-radius: var(--sms-radius); background: var(--sms-surface); box-shadow: inset 0 0 0 1px var(--sms-line), 0 18px 40px rgba(6, 30, 53, 0.06); scroll-snap-align: start; }
.sms-hscroll .sms-hscroll__num { color: var(--sms-accent); font-size: clamp(3rem, 2.4rem + 2.4vw, 4.5rem); font-weight: 200; line-height: 1; letter-spacing: -0.04em; }
.sms-hscroll .sms-hscroll__name { margin: auto 0 0.6rem; padding-top: 2rem; color: var(--sms-title); font-size: var(--sms-step-1); font-weight: 500; }
.sms-hscroll .sms-hscroll__text { color: var(--sms-ink-soft); font-size: var(--sms-step--1); }
.sms-hscroll .sms-hscroll__text p { margin: 0; }
.sms-hscroll .sms-hscroll__text ul { margin: 0; padding-left: 1.1rem; }
.sms-hscroll .sms-hscroll__card--end { justify-content: center; background: var(--sms-pale); }
.sms-hscroll .sms-hscroll__card--end .sms-hscroll__name { margin-top: 0; padding-top: 0; }
.sms-hscroll .sms-hscroll__card--end .sms-btn { align-self: flex-start; margin-top: 1.25rem; }
@media (min-width: 60em) {
  .sms-hscroll .sms-hscroll__head { grid-template-columns: minmax(0, 1.2fr) minmax(0, 0.8fr); }
  .sms-hscroll .sms-hscroll__intro { justify-self: end; }
}
.sms-hscroll .sms-hscroll__head,
.sms-hscroll .sms-hscroll__viewport,
.sms-hscroll .sms-hscroll__num,
.sms-hscroll .sms-hscroll__name,
.sms-hscroll .sms-hscroll__text { min-width: 0; }
@supports (animation-timeline: view()) {
  @media (min-width: 60em) and (prefers-reduced-motion: no-preference) {
    @keyframes sms-hmove { from { transform: translateX(0); } to { transform: translateX(calc(-100% + 100vw - 2 * var(--sms-gutter))); } }
    .sms-hscroll { height: 320vh; padding: 0; }
    .sms-hscroll .sms-hscroll__sticky { position: sticky; top: 0; display: flex; flex-direction: column; justify-content: center; height: 100vh; overflow: hidden; }
    .sms-hscroll .sms-hscroll__viewport { overflow: visible; scroll-snap-type: none; }
    .sms-hscroll .sms-hscroll__track { margin: 0; animation: sms-hmove linear both; animation-timeline: --sms-hscroll; animation-range: contain 0% contain 100%; }
  }
}
"""

RISE = [".sms-hhero .sms-hhero__title", ".sms-horizon .sms-horizon__title"]
ENTRANCE = [".sms-hhero .sms-hhero__crumb", ".sms-hhero .sms-kicker", ".sms-horizon .sms-kicker", ".sms-hhero .sms-hhero__row", ".sms-horizon .sms-horizon__row",
            ".sms-hhero .sms-hhero__band", ".sms-horizon .sms-horizon__strip"]
REVEAL = [".sms-svc .sms-svc__head", ".sms-svc .sms-svc__item", ".sms-area .sms-area__copy", ".sms-area .sms-area__visual", ".sms-hcta .sms-hcta__box"]
LOOP = [".sms-horizon .sms-horizon__track", ".sms-hcta .sms-hcta__line", ".sms-area .sms-area__pulse", ".sms-scrub .sms-scrub__w", ".sms-hscroll .sms-hscroll__track"]
TRANS = [".sms-horizon .sms-horizon__img", ".sms-svc .sms-svc__name", ".sms-svc .sms-svc__go", ".sms-svc .sms-svc__float", ".sms-svc .sms-svc__float-img"]

SKIP = {"event-medical-cover": [2], "about": [0]}


def page_hero(ctx, h, crumb=True):
    crumb_html = '<div class="sms-hhero__crumb"><a class="sms-hhero__crumb-link" href="%s">Home</a> / %s</div>' % (ctx.href("home"), e(LABEL[ctx.slug])) if crumb else ""
    sub = '<div class="sms-hhero__sub">%s</div>' % e(h["sub"]) if h.get("sub") else ""
    acts = '<div class="sms-hhero__actions">%s</div>' % buttons(ctx, h["buttons"]) if h.get("buttons") else ""
    chips_html = "".join('<span class="sms-hhero__chip">%s<span class="sms-hhero__chip-text">%s</span></span>' % (icon(ic, "sms-hhero__chip-icon"), e(t)) for ic, t in h.get("chips", [])[:2])
    return """<section class="sms-hhero">
  <div class="sms-hhero__inner">
    %s
    <div class="sms-kicker">%s</div>
    <h1 class="sms-hhero__title">%s</h1>
    <div class="sms-hhero__row"><div class="sms-hhero__lead">%s%s</div>%s</div>
  </div>
  <div class="sms-hhero__band">%s<div class="sms-hhero__chips">%s</div></div>
</section>
""" % (crumb_html, e(h["eyebrow"]), e(h["title"]), sub, paras(h["body"]), acts, photo(ctx, h["photo"], lazy=False, figcls="sms-hhero__frame"), chips_html)


def cta(ctx, d):
    btns = [(l, t) for l, t in d["buttons"] if t != "tel"]
    return """<section class="sms-hcta">
  <div class="sms-hcta__inner">
    <div class="sms-hcta__box">
      <span class="sms-hcta__line" aria-hidden="true"></span>
      <h2 class="sms-hcta__title">%s</h2>
      <div class="sms-hcta__text">%s</div>
      <div class="sms-hcta__actions">%s</div>
      <div class="sms-hcta__call">Or call us on <a href="tel:%s">%s</a></div>
    </div>
  </div>
</section>
""" % (e(d["title"]), paras(d["text"]), buttons(ctx, btns) if btns else "", PHONE_TEL, PHONE)


def chrome_top(ctx):
    return header(ctx, "blue")


def chrome_bottom(ctx):
    return footer(ctx, "white")


# ---------------------------------------------------------------------------
# Sections
# ---------------------------------------------------------------------------

def scrub(ctx, blocks, link=True):
    out = ""
    for label, text in blocks:
        words = e(text).split(" ")
        spans = " ".join('<span class="sms-scrub__w">%s</span>' % w for w in words)
        out += '<figure class="sms-scrub__block"><div class="sms-kicker">%s</div><blockquote class="sms-scrub__text"><p>%s</p></blockquote></figure>' % (e(label), spans)
    more_html = '<div class="sms-scrub__more"><a class="sms-arrowlink" href="%s">About Streamline&nbsp;<span class="sms-arrow" aria-hidden="true">&rarr;</span></a></div>' % ctx.href("about") if link else ""
    return '<section class="sms-scrub"><div class="sms-scrub__inner">%s%s</div></section>\n' % (out, more_html)


MISSION = C.PAGES["about"]["sections"][0][1]["items"]


def area_svg():
    dots = ""
    for y in range(20, 420, 22):
        for x in range(20, 560, 22):
            dx, dy = (x - 280) / 280.0, (y - 210) / 210.0
            d = dx * dx + dy * dy
            if d < 1:
                dots += '<circle cx="%d" cy="%d" r="1.6" opacity="%.2f"/>' % (x, y, max(0.12, 0.55 - d * 0.45))
    lab = lambda x, y, t, a="middle": '<text x="%d" y="%d" text-anchor="%s" font-size="14" font-weight="600" fill="#061e35">%s</text>' % (x, y, a, t)
    return """<svg class="sms-area__svg" viewBox="0 0 560 420" role="img" aria-label="Swadlincote in the centre, with Derbyshire to the north, Staffordshire to the west and Leicestershire to the south-east, inside the wider East Midlands." xmlns="http://www.w3.org/2000/svg">
  <g fill="#405365">%s</g>
  <circle cx="280" cy="210" r="190" fill="none" stroke="rgba(64,127,54,0.35)" stroke-dasharray="3 7"/>
  <circle cx="280" cy="210" r="118" fill="rgba(64,127,54,0.06)" stroke="rgba(64,127,54,0.45)" stroke-dasharray="4 6"/>
  <circle cx="280" cy="210" r="9" fill="#407f36"/>
  <circle cx="280" cy="210" r="16" fill="none" stroke="#407f36" stroke-width="1.5"/>
  %s
  %s
  %s
  %s
  %s
  <text x="280" y="402" text-anchor="middle" font-size="12" fill="#405365">Wider East Midlands</text>
</svg>""" % (dots, lab(280, 246, "Swadlincote"), lab(280, 120, "Derbyshire"), lab(150, 214, "Staffordshire"), lab(392, 290, "Leicestershire"),
             '<path d="M280 128v60M168 210h96M370 280l-80-60" stroke="rgba(6,30,53,0.18)" stroke-dasharray="2 5"/>')


def area(ctx, heading="Which areas do you [[cover?]]"):
    places = "".join('<li class="sms-pills__item"><span class="sms-pill">%s</span></li>' % t for t in ["South Derbyshire", "Derbyshire", "Leicestershire", "Staffordshire", "Wider East Midlands", "UK-wide, where possible"])
    return """<section class="sms-area" id="area">
  <div class="sms-area__inner">
    <div class="sms-area__copy">
      <div class="sms-kicker">Where we work</div>
      <h2 class="sms-area__title">%s</h2>
      <div class="sms-area__text"><p>We are based in Swadlincote and regularly support events across Derbyshire, Leicestershire, Staffordshire and the wider East Midlands. UK-wide cover may be possible depending on staffing, travel and event needs.</p></div>
      <ul class="sms-pills sms-area__places">%s</ul>
    </div>
    <div class="sms-area__visual">
      <div class="sms-area__map">%s<span class="sms-area__pulse" aria-hidden="true"></span><span class="sms-area__pulse sms-area__pulse--2" aria-hidden="true"></span><span class="sms-area__pulse sms-area__pulse--3" aria-hidden="true"></span></div>
      <p class="sms-caption">Illustration, not to scale.</p>
    </div>
  </div>
</section>
""" % (e(heading), places, area_svg())


JOURNEY = [
    ("What information is needed for a quote?", '<ul><li>Event type, date, times, venue and postcode</li><li>Expected attendance and age range</li><li>Activities and alcohol arrangements</li><li>Previous incidents and existing provision</li><li>Risk assessment, site plan and emergency access</li><li>Any organiser or venue requirements</li></ul>'),
    ("A clear quotation", "<p>When booking Streamline Safety &amp; Medical Solutions, we will provide you with a clear quotation based on your event requirements.</p>"),
    ("Booking confirmed", "<p>Your booking will be confirmed once this has been agreed and any required booking information has been completed.</p>"),
    ("If your event details change", "<p>If your event details change, such as timings, attendance or activities, please let us know so we can make sure the medical provision remains suitable.</p>"),
    ("Terms &amp; Conditions", "<p>Full Medical Cover Booking Terms &amp; Conditions will be provided when you choose to book with us, so you can review everything before confirming your booking.</p>"),
]


def hscroll(ctx):
    ctx.notes.append("Image-only copy used: \"Book Your Event Medical Cover\" heading (book-your-medical-cover.png)")
    cards = "".join('<li class="sms-hscroll__card"><span class="sms-hscroll__num" aria-hidden="true">%02d</span><h3 class="sms-hscroll__name">%s</h3><div class="sms-hscroll__text">%s</div></li>' % (i + 1, t, body) for i, (t, body) in enumerate(JOURNEY))
    cards += '<li class="sms-hscroll__card sms-hscroll__card--end"><h3 class="sms-hscroll__name">How early should I book?</h3><div class="sms-hscroll__text"><p>Contact us as early as possible. For an event within one month, contact us directly as well as submitting any online enquiry.</p></div>%s</li>' % buttons(ctx, [("Book us for your medical cover", "book:event")])
    return """<section class="sms-hscroll" id="booking">
  <div class="sms-hscroll__sticky">
    <div class="sms-hscroll__head">
      <div class="sms-hscroll__heading"><div class="sms-kicker">Booking information</div><h2 class="sms-hscroll__title">Book Your Event <span class="sms-mark">Medical Cover</span></h2></div>
      <div class="sms-hscroll__intro"><p>If you have any questions, we are always happy to discuss your event and requirements with you.</p></div>
    </div>
    <div class="sms-hscroll__viewport" tabindex="0" aria-label="Booking steps">
      <ol class="sms-hscroll__track">%s</ol>
    </div>
  </div>
</section>
""" % cards


def inner_extra(ctx, slug):
    if slug == "event-medical-cover":
        return hscroll(ctx)
    if slug == "about":
        return scrub(ctx, [(it["label"], it["text"]) for it in MISSION], link=False)
    if slug == "contact":
        return area(ctx)
    return ""


# ---------------------------------------------------------------------------
# Homepage
# ---------------------------------------------------------------------------
STRIP = [("event-medical-cover", "festival", "Event Medical Cover"), ("medical-training", "cpr-room", "Medical Training"),
         ("risk-needs-consultancy", "assessor", "Risk & Needs Consultancy"), ("pre-hospital-career-support", "cpr-outdoor", "Pre-Hospital Career Support"),
         ("about", "team", "About Us"), ("event-medical-cover", "fete", "Event Medical Cover"), ("medical-training", "session", "Medical Training"),
         ("recruitment", "stall", "Recruitment")]

SVC = [("event-medical-cover", "Event Medical Cover", "festival", "Skilled. Proportionate. Reliable."),
       ("medical-training", "Medical Training", "cpr-room", "Clinician-led first aid and pre-hospital training"),
       ("risk-needs-consultancy", "Risk & Needs Consultancy", "assessor", "Expert advice, practical solutions"),
       ("pre-hospital-career-support", "Pre-Hospital Career Support", "cpr-outdoor", "Practical support. Confident career steps."),
       ("recruitment", "Recruitment", "team", "Interested in working with us?")]


def home(ctx):
    items = ""
    for dup in (False, True):
        for slug, ph, cap in STRIP:
            img = photo_img(ctx, ph, "sms-horizon__img", lazy=dup, decorative=dup)
            attrs = ' aria-hidden="true"' if dup else ""
            tab = ' tabindex="-1"' if dup else ""
            items += '<li class="sms-horizon__item"%s><a class="sms-horizon__card" href="%s"%s>%s<span class="sms-horizon__cap">%s</span></a></li>' % (attrs, ctx.href(slug), tab, img, e(cap))
    out = """<section class="sms-horizon">
  <div class="sms-horizon__inner">
    <div class="sms-kicker">%s</div>
    <h1 class="sms-horizon__title">Clinician-Led Medical Cover, <span class="sms-mark">First Aid Training</span> &amp; Safety Consultancy</h1>
    <div class="sms-horizon__row">
      <div class="sms-horizon__lead"><p>%s</p><p class="sms-horizon__area">%s</p></div>
      <div class="sms-horizon__actions">%s</div>
    </div>
  </div>
  <div class="sms-horizon__strip"><ul class="sms-horizon__track">%s</ul></div>
</section>
""" % (e(C.STRAP), e(C.INTRO2), e(C.AREA), buttons(ctx, [("Book online", "book"), ("Call 01283 358789", "tel")]), items)

    rows, floats = "", ""
    for i, (slug, title, ph, line) in enumerate(SVC):
        rows += """<li class="sms-svc__item"><a class="sms-svc__link" href="%s" data-sms-float="%d">
          <span class="sms-svc__num" aria-hidden="true">%02d</span>
          <span class="sms-svc__body"><span class="sms-svc__name">%s</span><span class="sms-svc__line">%s</span></span>
          %s<span class="sms-svc__go" aria-hidden="true">%s</span>
        </a></li>""" % (ctx.href(slug), i, i + 1, e(title), e(line), photo_img(ctx, ph, "sms-svc__thumb", decorative=True), icon("arrow", "sms-svc__go-icon"))
        floats += photo_img(ctx, ph, "sms-svc__float-img", decorative=True).replace("<img ", '<img data-sms-float-img="%d" ' % i, 1)
    out += """<section class="sms-svc" id="services" data-sms-svc>
  <div class="sms-svc__inner">
    <div class="sms-svc__head">
      <div class="sms-svc__heading"><div class="sms-kicker">Our Services</div><h2 class="sms-svc__title">What We <span class="sms-mark">Provide</span></h2></div>
      <div class="sms-svc__intro"><p>%s</p></div>
    </div>
    <ul class="sms-svc__list">%s</ul>
  </div>
  <div class="sms-svc__float" aria-hidden="true">%s</div>
</section>
""" % (e(C.INTRO), rows, floats)

    out += scrub(ctx, [(MISSION[0]["label"], MISSION[0]["text"])])
    out += area(ctx, heading="Based in Swadlincote, working across the [[East Midlands]]")
    out += hscroll(ctx)
    picks = ["Who runs Streamline?", "Can Streamline provide more than one service?", "Do you offer a free initial discussion?", "Are you insured?", "How quickly will Streamline respond?", "How can I contact Streamline?"]
    allf = dict(C.faqs("home"))
    out += SHARED_RENDERERS["faq"](ctx, {"tone": "pale", "eyebrow": C.STRAP, "title": "General Streamline [[FAQs]]",
                                        "lead": ["Answers to common questions about Streamline Safety & Medical Solutions, our team, services, bookings and how we work."],
                                        "items": [(q, allf[q]) for q in picks if q in allf], "show": 6})
    out += cta(ctx, {"title": "Have any questions? We’re here to help.",
                     "text": ["We offer an initial discussion to understand your requirements, and our risk and needs consultancy includes a free initial consultation before any chargeable work is agreed."],
                     "buttons": [("Book online", "book"), ("Contact Us", "contact")]})
    return out


JS = """<script>
(function () {
  /* Service list: a photo follows the pointer over the rows (fine pointers only) */
  var fine = window.matchMedia('(hover: hover) and (pointer: fine)').matches;
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  Array.prototype.forEach.call(document.querySelectorAll('[data-sms-svc]'), function (sec) {
    if (!fine) { return; }
    var float = sec.querySelector('.sms-svc__float');
    var imgs = sec.querySelectorAll('[data-sms-float-img]');
    sec.classList.add('is-live');
    var cur = { x: 0, y: 0 }, tgt = { x: 0, y: 0 }, running = false;
    var step = function () {
      var k = reduce ? 1 : 0.18;
      cur.x += (tgt.x - cur.x) * k; cur.y += (tgt.y - cur.y) * k;
      float.style.setProperty('--fx', cur.x.toFixed(1) + 'px'); float.style.setProperty('--fy', cur.y.toFixed(1) + 'px');
      if (Math.abs(tgt.x - cur.x) > 0.5 || Math.abs(tgt.y - cur.y) > 0.5) { window.requestAnimationFrame(step); } else { running = false; }
    };
    Array.prototype.forEach.call(sec.querySelectorAll('[data-sms-float]'), function (row) {
      row.addEventListener('pointerenter', function () {
        var n = row.getAttribute('data-sms-float');
        Array.prototype.forEach.call(imgs, function (im) { im.classList.toggle('is-on', im.getAttribute('data-sms-float-img') === n); });
        float.classList.add('is-on');
      });
      row.addEventListener('pointerleave', function () { float.classList.remove('is-on'); });
      row.addEventListener('pointermove', function (ev) {
        var r = sec.getBoundingClientRect();
        tgt.x = ev.clientX - r.left + 24; tgt.y = ev.clientY - r.top - float.offsetHeight / 2;
        if (!float.classList.contains('was')) { cur.x = tgt.x; cur.y = tgt.y; float.classList.add('was'); }
        if (!running) { running = true; window.requestAnimationFrame(step); }
      });
    });
  });
})();
</script>
"""


def scripts(ctx, main):
    return JS if "data-sms-svc" in main else ""
