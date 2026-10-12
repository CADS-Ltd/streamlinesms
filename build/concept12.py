"""Concept 12 - Signal. The calm, precise feel of the Pristine Motors round 4
concepts with new elements, in Streamline's original colours: a slow radar sweep
behind the hero, a first aid needs assessment grid that lights up factor by factor
as you scroll, a five-step consultation stepper, and a career journey line where
you pick your starting point."""
from common import *  # noqa: F401,F403
import content as C
import light
import dark

NAME = "Signal"
DARK = False
CINE = True
FONTS = "https://fonts.googleapis.com/css2?family=Urbanist:ital,wght@0,300;0,400;0,500;0,600;0,700;1,300;1,400&display=swap"

FACTORS = [("briefcase", "The work undertaken"), ("alert", "Likely hazards"), ("users", "Workforce size"), ("firstaid", "First aid kit levels"),
           ("clipboard", "Kit storage and monitoring"), ("user", "First aider numbers"), ("calendar", "Absence cover"), ("phone", "Emergency service response arrangements")]

CONSULT = C.PAGES["risk-needs-consultancy"]["sections"][2][1]["items"]
STARTS = C.PAGES["pre-hospital-career-support"]["sections"][0][1]["chips"]
CAREER_STEPS = C.PAGES["pre-hospital-career-support"]["sections"][2][1]["items"]


def _stepper_css():
    n = len(CONSULT)
    out = dark.seg_css(".sms-stepper", "step", n, "sms-stepper__p")
    for i in range(n):
        out += ".sms-stepper .sms-step__r%d:checked ~ * .sms-stepper__fill { transform: scaleX(%.3f); }\n" % (i, (i + 1) / n)
        out += ".sms-stepper .sms-step__r%d:checked ~ * .sms-stepper__dot:nth-child(-n+%d) { background: var(--sms-accent); box-shadow: 0 0 0 4px var(--sms-mint); }\n" % (i, i + 1)
    return out


def _career_css():
    out = ".sms-career .sms-career__out { display: none; }\n"
    for i in range(len(STARTS)):
        r = ".sms-career .sms-career__r%d" % i
        out += "%s:checked ~ * .sms-career__start--%d { background: var(--sms-ink); color: #ffffff; box-shadow: none; }\n" % (r, i)
        out += "%s:checked ~ * .sms-career__start--%d .sms-career__start-icon { background: rgba(255, 255, 255, 0.14); color: #ffffff; }\n" % (r, i)
        out += "%s:focus-visible ~ * .sms-career__start--%d { outline: 3px solid var(--sms-accent); outline-offset: 3px; }\n" % (r, i)
        out += "%s:checked ~ * .sms-career__out--%d { display: block; }\n" % (r, i)
    return out


CSS = light.css([".sms-shero .sms-shero__panel", ".sms-signal", ".sms-scta .sms-scta__box", ".sms-footer"]) + r"""
/* ===== Concept 12 theme: signal ===== */
.sms-page { --sms-font: "Urbanist", "Montserrat", Arial, sans-serif; --sms-radius: 1.5rem; --sms-radius-sm: 0.9rem; --sms-hw: 300; font-size: clamp(1.03rem, 0.98rem + 0.22vw, 1.1rem); }
.sms-page .sms-mark { color: var(--sms-accent); font-style: italic; font-weight: inherit; }

/* Radar sweep (hero background) */
.sms-page .sms-radar { position: absolute; z-index: 0; width: 46rem; aspect-ratio: 1; border-radius: 50%; pointer-events: none; }
.sms-page .sms-radar__rings { position: absolute; inset: 0; border-radius: 50%; background: repeating-radial-gradient(circle, transparent 0 3.7rem, rgba(130, 208, 110, 0.18) 3.7rem calc(3.7rem + 1px)); -webkit-mask-image: radial-gradient(circle, #000 55%, transparent 72%); mask-image: radial-gradient(circle, #000 55%, transparent 72%); }
.sms-page .sms-radar__sweep { position: absolute; inset: 0; border-radius: 50%; background: conic-gradient(from 0deg, rgba(130, 208, 110, 0) 0%, rgba(130, 208, 110, 0.06) 12%, rgba(130, 208, 110, 0.28) 21.5%, rgba(130, 208, 110, 0) 22%, rgba(130, 208, 110, 0) 100%); -webkit-mask-image: radial-gradient(circle, #000 55%, transparent 72%); mask-image: radial-gradient(circle, #000 55%, transparent 72%); animation: sms-sweep 9s linear infinite; }
.sms-page .sms-radar__blip { position: absolute; width: 0.6rem; height: 0.6rem; border-radius: 50%; background: #82d06e; box-shadow: 0 0 14px rgba(130, 208, 110, 0.9); opacity: 0; animation: sms-blip 9s linear infinite; }
.sms-page .sms-radar__blip--1 { left: 64%; top: 30%; animation-delay: 1.1s; }
.sms-page .sms-radar__blip--2 { left: 30%; top: 62%; animation-delay: 5.4s; }
.sms-page .sms-radar__blip--3 { left: 70%; top: 66%; animation-delay: 3.4s; }
@keyframes sms-sweep { to { transform: rotate(360deg); } }
@keyframes sms-blip { 0% { opacity: 0; transform: scale(0.4); } 3% { opacity: 1; transform: scale(1); } 30% { opacity: 0; transform: scale(1); } 100% { opacity: 0; } }

/* ---------- Page hero (inner pages): light text column and a navy photo panel ---------- */
.sms-shero { position: relative; overflow: hidden; padding: clamp(3rem, 2rem + 4vw, 5.5rem) 0 clamp(3rem, 2rem + 3vw, 5rem); background: var(--sms-pale); }
.sms-shero .sms-shero__inner { display: grid; gap: clamp(2rem, 1.5rem + 3vw, 3.5rem); align-items: stretch; width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-shero .sms-shero__copy { display: flex; flex-direction: column; justify-content: center; min-width: 0; }
.sms-shero .sms-shero__crumb { margin-bottom: 1.5rem; color: var(--sms-ink-soft); font-size: var(--sms-step--1); }
.sms-shero .sms-shero__crumb-link { color: var(--sms-ink); }
.sms-shero .sms-shero__title { margin: 0 0 1.5rem; color: var(--sms-title); font-size: clamp(2.5rem, 1.4rem + 4.4vw, 5.2rem); font-weight: 300; line-height: 1.02; letter-spacing: -0.04em; }
.sms-shero .sms-shero__sub { margin-bottom: 0.6rem; color: var(--sms-accent); font-weight: 600; }
.sms-shero .sms-shero__lead { max-width: 36rem; color: var(--sms-ink); font-size: var(--sms-step-1); font-weight: 400; line-height: 1.6; }
.sms-shero .sms-shero__lead p { margin: 0 0 0.75rem; }
.sms-shero .sms-shero__actions { display: flex; flex-wrap: wrap; gap: 0.75rem; margin-top: 1.75rem; }
.sms-shero .sms-shero__panel { position: relative; min-width: 0; min-height: 20rem; overflow: hidden; border-radius: var(--sms-radius); background: var(--sms-navy); }
.sms-shero .sms-shero__img { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; opacity: 0.6; }
.sms-shero .sms-shero__shade { position: absolute; inset: 0; background: linear-gradient(0deg, rgba(6, 30, 53, 0.9), rgba(6, 30, 53, 0.1) 60%); }
.sms-shero .sms-radar { left: 50%; top: 50%; width: 34rem; margin: -17rem 0 0 -17rem; }
.sms-shero .sms-shero__facts { position: absolute; left: 1.25rem; right: 1.25rem; bottom: 1.25rem; z-index: 2; display: grid; gap: 0.5rem; }
.sms-shero .sms-shero__fact { display: flex; align-items: center; gap: 0.6rem; min-width: 0; color: #ffffff; font-size: var(--sms-step--1); font-weight: 500; }
.sms-shero .sms-shero__fact-icon { width: 1.75rem; height: 1.75rem; padding: 0.35rem; border-radius: 50%; background: var(--sms-accent); color: var(--sms-on-accent); }
.sms-shero .sms-shero__fact-text { min-width: 0; }
.sms-shero .sms-shero__crumb,
.sms-shero .sms-kicker,
.sms-shero .sms-shero__title,
.sms-shero .sms-shero__sub,
.sms-shero .sms-shero__lead,
.sms-shero .sms-shero__actions,
.sms-stepper .sms-stepper__big { min-width: 0; }
@media (min-width: 60em) {
  .sms-shero .sms-shero__inner { grid-template-columns: minmax(0, 1.15fr) minmax(0, 0.85fr); }
  .sms-shero .sms-shero__panel { min-height: 28rem; }
}

/* ---------- CTA ---------- */
.sms-scta { padding: var(--sms-section) 0; }
.sms-scta .sms-scta__inner { width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-scta .sms-scta__box { position: relative; display: grid; gap: 2rem; align-items: center; overflow: hidden; padding: clamp(2rem, 1.2rem + 3.5vw, 4.5rem); border-radius: var(--sms-radius); background: linear-gradient(160deg, #0b2a47, #061e35); }
.sms-scta .sms-radar { right: -14rem; top: 50%; width: 36rem; margin-top: -18rem; opacity: 0.8; }
.sms-scta .sms-scta__copy { position: relative; z-index: 1; min-width: 0; }
.sms-scta .sms-scta__title { margin: 0 0 1rem; color: var(--sms-title); font-size: clamp(2rem, 1.3rem + 2.8vw, 3.5rem); font-weight: 300; line-height: 1.06; letter-spacing: -0.035em; }
.sms-scta .sms-scta__text { max-width: 36rem; color: var(--sms-ink-soft); }
.sms-scta .sms-scta__text p { margin: 0; }
.sms-scta .sms-scta__side { position: relative; z-index: 1; display: grid; gap: 1rem; justify-items: start; min-width: 0; }
.sms-scta .sms-scta__actions { display: flex; flex-wrap: wrap; gap: 0.75rem; min-width: 0; }
.sms-scta .sms-scta__call { min-width: 0; color: var(--sms-ink-soft); font-size: var(--sms-step--1); }
.sms-scta .sms-scta__call a { color: var(--sms-title); text-underline-offset: 4px; }
@media (min-width: 60em) {
  .sms-scta .sms-scta__box { grid-template-columns: minmax(0, 1.5fr) minmax(0, 1fr); }
  .sms-scta .sms-scta__side { justify-items: end; text-align: right; }
}

/* ---------- Home hero: navy with the radar ---------- */
.sms-signal { position: relative; overflow: hidden; padding: clamp(4rem, 3rem + 5vw, 8rem) 0 0; background: radial-gradient(70rem 40rem at 80% 30%, #0b2f50, var(--sms-bg) 70%); }
.sms-signal .sms-radar { right: -10rem; top: 50%; margin-top: -23rem; }
.sms-signal .sms-signal__inner { position: relative; z-index: 1; width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-signal .sms-signal__title { max-width: 12em; margin: 0 0 1.75rem; color: var(--sms-title); font-size: clamp(2.8rem, 1.3rem + 6vw, 6.8rem); font-weight: 300; line-height: 0.98; letter-spacing: -0.045em; }
.sms-signal .sms-signal__lead { max-width: 34rem; color: var(--sms-ink); font-size: var(--sms-step-1); line-height: 1.6; }
.sms-signal .sms-signal__lead p { margin: 0; }
.sms-signal .sms-signal__actions { display: flex; flex-wrap: wrap; gap: 0.75rem; margin-top: 2rem; }
.sms-signal .sms-signal__band { position: relative; z-index: 1; margin-top: clamp(3rem, 2rem + 4vw, 5.5rem); border-top: 1px solid var(--sms-line); background: rgba(255, 255, 255, 0.03); }
.sms-signal .sms-signal__list { display: grid; width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: 0 var(--sms-gutter); list-style: none; }
.sms-signal .sms-signal__item { min-width: 0; border-bottom: 1px solid var(--sms-line); }
.sms-signal .sms-signal__item:last-child { border-bottom: 0; }
.sms-signal .sms-signal__link { display: flex; align-items: center; gap: 0.9rem; padding: 1.4rem 0; color: var(--sms-ink); text-decoration: none; }
.sms-signal .sms-signal__icon { width: 2.6rem; height: 2.6rem; padding: 0.6rem; border-radius: 50%; box-shadow: inset 0 0 0 1px var(--sms-line-green); color: var(--sms-accent); transition: background-color 0.4s, color 0.4s; }
.sms-signal .sms-signal__name { min-width: 0; font-size: var(--sms-step-0); font-weight: 500; }
.sms-signal .sms-signal__go { min-width: 0; margin-left: auto; color: var(--sms-accent); transition: transform 0.4s var(--sms-ease); }
.sms-signal .sms-signal__link:hover .sms-signal__icon { background: var(--sms-accent); color: var(--sms-on-accent); }
.sms-signal .sms-signal__link:hover .sms-signal__go { transform: translateX(4px); }
@media (min-width: 60em) {
  .sms-signal .sms-signal__list { grid-template-columns: repeat(3, minmax(0, 1fr)); }
  .sms-signal .sms-signal__item { border-bottom: 0; border-right: 1px solid var(--sms-line); }
  .sms-signal .sms-signal__item:last-child { border-right: 0; }
  .sms-signal .sms-signal__item + .sms-signal__item .sms-signal__link { padding-left: 1.75rem; }
  .sms-signal .sms-signal__link { padding-right: 1.75rem; }
}

/* ---------- First aid needs assessment grid ---------- */
.sms-scan { padding: var(--sms-section) 0; view-timeline-name: --sms-scan; }
.sms-scan .sms-scan__inner { display: grid; gap: clamp(2.5rem, 1.5rem + 4vw, 5rem); align-items: center; width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-scan .sms-scan__copy { min-width: 0; }
.sms-scan .sms-scan__title { margin: 0 0 1.5rem; color: var(--sms-title); font-size: clamp(2.2rem, 1.3rem + 3.2vw, 4rem); font-weight: 300; line-height: 1.04; letter-spacing: -0.04em; }
.sms-scan .sms-scan__text { max-width: 32rem; color: var(--sms-ink-soft); }
.sms-scan .sms-scan__text p { margin: 0 0 1rem; }
.sms-scan .sms-scan__panel { position: relative; min-width: 0; overflow: hidden; padding: clamp(1.25rem, 0.8rem + 2vw, 2rem); border-radius: var(--sms-radius); background: var(--sms-pale); box-shadow: inset 0 0 0 1px var(--sms-line); }
.sms-scan .sms-scan__beam { position: absolute; left: 0; right: 0; top: 0; height: 30%; background: linear-gradient(180deg, transparent, rgba(64, 127, 54, 0.12), transparent); transform: translateY(-100%); pointer-events: none; }
.sms-scan .sms-scan__grid { position: relative; display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 0.6rem; margin: 0; padding: 0; list-style: none; }
.sms-scan .sms-scan__cell { display: flex; flex-direction: column; gap: 0.75rem; min-width: 0; padding: 1.1rem; border-radius: 1rem; background: var(--sms-surface); box-shadow: inset 0 0 0 1px var(--sms-line); }
.sms-scan .sms-scan__icon { width: 2.4rem; height: 2.4rem; padding: 0.55rem; border-radius: 0.75rem; background: var(--sms-mint); color: var(--sms-accent); }
.sms-scan .sms-scan__name { min-width: 0; color: var(--sms-ink); font-size: var(--sms-step--1); font-weight: 600; line-height: 1.35; }
.sms-scan .sms-scan__out { position: relative; display: flex; align-items: center; gap: 0.75rem; margin-top: 1rem; padding: 1rem 1.25rem; border-radius: 1rem; background: var(--sms-navy); color: #ffffff; font-weight: 500; }
.sms-scan .sms-scan__out-icon { color: #82d06e; }
.sms-scan .sms-scan__out-text { min-width: 0; }
@media (min-width: 40em) {
  .sms-scan .sms-scan__grid { grid-template-columns: repeat(4, minmax(0, 1fr)); }
}
@media (min-width: 60em) {
  .sms-scan .sms-scan__inner { grid-template-columns: minmax(0, 0.85fr) minmax(0, 1.15fr); }
}
@supports (animation-timeline: view()) {
  @keyframes sms-cell { from { opacity: 0.25; transform: scale(0.94); } to { opacity: 1; transform: none; } }
  @keyframes sms-beam { from { transform: translateY(-100%); } to { transform: translateY(380%); } }
  .sms-scan .sms-scan__beam { animation: sms-beam linear both; animation-timeline: --sms-scan; animation-range: entry 40% contain 60%; }
  .sms-scan .sms-scan__cell { animation: sms-cell linear both; animation-timeline: --sms-scan; }
  .sms-scan .sms-scan__cell:nth-child(1) { animation-range: entry 40% entry 55%; }
  .sms-scan .sms-scan__cell:nth-child(2) { animation-range: entry 46% entry 61%; }
  .sms-scan .sms-scan__cell:nth-child(3) { animation-range: entry 52% entry 67%; }
  .sms-scan .sms-scan__cell:nth-child(4) { animation-range: entry 58% entry 73%; }
  .sms-scan .sms-scan__cell:nth-child(5) { animation-range: entry 64% entry 79%; }
  .sms-scan .sms-scan__cell:nth-child(6) { animation-range: entry 70% entry 85%; }
  .sms-scan .sms-scan__cell:nth-child(7) { animation-range: entry 76% entry 91%; }
  .sms-scan .sms-scan__cell:nth-child(8) { animation-range: entry 82% entry 97%; }
}

/* ---------- Five-step consultation stepper ---------- */
.sms-stepper { padding: var(--sms-section) 0; background: var(--sms-pale); }
.sms-stepper .sms-stepper__inner { width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-stepper .sms-stepper__head { display: grid; gap: 1.25rem; align-items: end; margin-bottom: clamp(2rem, 1.5rem + 2vw, 3rem); }
.sms-stepper .sms-stepper__heading { min-width: 0; }
.sms-stepper .sms-stepper__title { margin: 0; color: var(--sms-title); font-size: clamp(2.2rem, 1.3rem + 3.2vw, 4rem); font-weight: 300; line-height: 1.04; letter-spacing: -0.04em; }
.sms-stepper .sms-stepper__intro { max-width: 30rem; min-width: 0; color: var(--sms-ink-soft); }
.sms-stepper .sms-stepper__intro p { margin: 0; }
.sms-stepper .sms-stepper__card { padding: clamp(1.5rem, 1rem + 2vw, 2.75rem); border-radius: var(--sms-radius); background: var(--sms-surface); box-shadow: inset 0 0 0 1px var(--sms-line), var(--sms-shadow-lg); }
.sms-stepper .sms-seg { margin-bottom: 1.5rem; }
.sms-stepper .sms-stepper__track { position: relative; height: 2px; margin: 0 0 2rem; background: var(--sms-line); }
.sms-stepper .sms-stepper__fill { position: absolute; inset: 0; background: var(--sms-accent); transform: scaleX(0.2); transform-origin: left; transition: transform 0.6s var(--sms-ease); }
.sms-stepper .sms-stepper__dots { position: absolute; left: 0; right: 0; top: -0.45rem; display: flex; justify-content: space-between; }
.sms-stepper .sms-stepper__dot { min-width: 0; width: 0.95rem; height: 0.95rem; border-radius: 50%; background: var(--sms-line); transition: background-color 0.4s, box-shadow 0.4s; }
.sms-stepper .sms-stepper__p0,
.sms-stepper .sms-stepper__p1,
.sms-stepper .sms-stepper__p2,
.sms-stepper .sms-stepper__p3,
.sms-stepper .sms-stepper__p4 { animation: sms-fade-up 0.5s var(--sms-ease) both; }
.sms-stepper .sms-stepper__panel { display: grid; gap: 1.5rem; }
.sms-stepper .sms-stepper__big { color: var(--sms-accent); font-size: clamp(3.5rem, 2.6rem + 3.6vw, 6rem); font-weight: 300; line-height: 0.9; letter-spacing: -0.04em; }
.sms-stepper .sms-stepper__body { min-width: 0; }
.sms-stepper .sms-stepper__name { margin: 0 0 0.75rem; color: var(--sms-title); font-size: clamp(1.6rem, 1.3rem + 1.4vw, 2.4rem); font-weight: 400; line-height: 1.15; }
.sms-stepper .sms-stepper__text { max-width: 44rem; color: var(--sms-ink-soft); font-size: var(--sms-step-1); line-height: 1.6; }
.sms-stepper .sms-stepper__text p { margin: 0; }
.sms-stepper .sms-stepper__note { display: flex; gap: 0.75rem; margin-top: 2rem; padding-top: 1.5rem; border-top: 1px solid var(--sms-line); color: var(--sms-ink-soft); font-size: var(--sms-step--1); }
.sms-stepper .sms-stepper__note-icon { color: var(--sms-accent); }
.sms-stepper .sms-stepper__note-text { min-width: 0; }
.sms-stepper .sms-stepper__note-text p { margin: 0; }
.sms-stepper .sms-stepper__actions { display: flex; flex-wrap: wrap; gap: 0.75rem; margin-top: 1.5rem; }
""" + _stepper_css() + r"""
@media (min-width: 60em) {
  .sms-stepper .sms-stepper__head { grid-template-columns: minmax(0, 1.2fr) minmax(0, 0.8fr); }
  .sms-stepper .sms-stepper__intro { justify-self: end; }
  .sms-stepper .sms-stepper__panel { grid-template-columns: 9rem minmax(0, 1fr); align-items: start; }
}

/* ---------- Career journey: pick your starting point ---------- */
.sms-career { padding: var(--sms-section) 0; }
.sms-career .sms-career__inner { display: grid; gap: clamp(2rem, 1.5rem + 3vw, 4rem); width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-career .sms-career__copy { min-width: 0; }
.sms-career .sms-career__title { margin: 0 0 1.25rem; color: var(--sms-title); font-size: clamp(2.2rem, 1.3rem + 3.2vw, 4rem); font-weight: 300; line-height: 1.04; letter-spacing: -0.04em; }
.sms-career .sms-career__text { max-width: 32rem; color: var(--sms-ink-soft); }
.sms-career .sms-career__text p { margin: 0 0 1rem; }
.sms-career .sms-career__label { margin: 1.5rem 0 0.75rem; color: var(--sms-ink-soft); font-size: 0.75rem; font-weight: 600; letter-spacing: 0.24em; text-transform: uppercase; }
.sms-career .sms-career__starts { display: grid; gap: 0.5rem; }
.sms-career .sms-career__start { display: flex; align-items: center; gap: 0.75rem; min-width: 0; padding: 0.6rem 1rem 0.6rem 0.6rem; border-radius: 1rem; background: var(--sms-surface); box-shadow: inset 0 0 0 1px var(--sms-line); color: var(--sms-ink); cursor: pointer; font-weight: 500; transition: background-color 0.3s, color 0.3s, transform 0.3s var(--sms-ease); }
.sms-career .sms-career__start:hover { transform: translateX(4px); }
.sms-career .sms-career__start-icon { width: 2.2rem; height: 2.2rem; padding: 0.5rem; border-radius: 0.7rem; background: var(--sms-mint); color: var(--sms-accent); }
.sms-career .sms-career__start-text { min-width: 0; }
.sms-career .sms-career__map { min-width: 0; padding: clamp(1.5rem, 1rem + 2vw, 2.5rem); border-radius: var(--sms-radius); background: var(--sms-pale); box-shadow: inset 0 0 0 1px var(--sms-line); }
.sms-career .sms-career__out { margin-bottom: 1.75rem; padding: 1rem 1.25rem; border-radius: 1rem; background: var(--sms-navy); color: #ffffff; animation: sms-fade-up 0.5s var(--sms-ease) both; }
.sms-career .sms-career__out-label { display: block; color: #82d06e; font-size: 0.75rem; font-weight: 600; letter-spacing: 0.2em; text-transform: uppercase; }
.sms-career .sms-career__out-name { display: block; margin-top: 0.25rem; font-weight: 500; }
.sms-career .sms-career__line { position: relative; margin: 0; padding: 0; list-style: none; }
.sms-career .sms-career__line::before { content: ""; position: absolute; left: 1.05rem; top: 1rem; bottom: 1rem; width: 2px; background: repeating-linear-gradient(180deg, var(--sms-accent) 0 6px, transparent 6px 12px); }
.sms-career .sms-career__step { position: relative; display: grid; grid-template-columns: 2.2rem minmax(0, 1fr); gap: 1rem; padding-bottom: 1.5rem; }
.sms-career .sms-career__step:last-child { padding-bottom: 0; }
.sms-career .sms-career__num { position: relative; display: grid; place-items: center; min-width: 0; width: 2.2rem; height: 2.2rem; border-radius: 50%; background: var(--sms-surface); box-shadow: inset 0 0 0 2px var(--sms-accent); color: var(--sms-accent); font-weight: 700; }
.sms-career .sms-career__body { min-width: 0; padding-top: 0.2rem; }
.sms-career .sms-career__name { margin: 0 0 0.3rem; color: var(--sms-title); font-size: var(--sms-step-1); font-weight: 500; }
.sms-career .sms-career__desc { color: var(--sms-ink-soft); font-size: var(--sms-step--1); }
.sms-career .sms-career__desc p { margin: 0; }
.sms-career .sms-career__actions { display: flex; flex-wrap: wrap; gap: 0.75rem; margin-top: 1.75rem; }
""" + _career_css() + r"""
@media (min-width: 60em) {
  .sms-career .sms-career__inner { grid-template-columns: minmax(0, 0.95fr) minmax(0, 1.05fr); align-items: start; }
}
"""

RISE = [".sms-shero .sms-shero__title", ".sms-signal .sms-signal__title"]
ENTRANCE = [".sms-shero .sms-shero__crumb", ".sms-shero .sms-kicker", ".sms-signal .sms-kicker", ".sms-shero .sms-shero__lead", ".sms-signal .sms-signal__lead",
            ".sms-shero .sms-shero__actions", ".sms-signal .sms-signal__actions", ".sms-shero .sms-shero__panel", ".sms-signal .sms-signal__band"]
REVEAL = [".sms-scan .sms-scan__copy", ".sms-stepper .sms-stepper__head", ".sms-stepper .sms-stepper__card", ".sms-career .sms-career__copy", ".sms-career .sms-career__map", ".sms-scta .sms-scta__box"]
LOOP = [".sms-page .sms-radar__sweep", ".sms-page .sms-radar__blip", ".sms-scan .sms-scan__beam", ".sms-scan .sms-scan__cell",
        ".sms-stepper .sms-stepper__p0", ".sms-stepper .sms-stepper__p1", ".sms-stepper .sms-stepper__p2", ".sms-stepper .sms-stepper__p3", ".sms-stepper .sms-stepper__p4", ".sms-career .sms-career__out"]
TRANS = [".sms-signal .sms-signal__icon", ".sms-signal .sms-signal__go", ".sms-stepper .sms-stepper__fill", ".sms-stepper .sms-stepper__dot", ".sms-career .sms-career__start"]

SKIP = {"risk-needs-consultancy": [2], "pre-hospital-career-support": [0, 2]}


def radar():
    return '<div class="sms-radar" aria-hidden="true"><span class="sms-radar__rings"></span><span class="sms-radar__sweep"></span><span class="sms-radar__blip sms-radar__blip--1"></span><span class="sms-radar__blip sms-radar__blip--2"></span><span class="sms-radar__blip sms-radar__blip--3"></span></div>'


def page_hero(ctx, h, crumb=True):
    crumb_html = '<div class="sms-shero__crumb"><a class="sms-shero__crumb-link" href="%s">Home</a> / %s</div>' % (ctx.href("home"), e(LABEL[ctx.slug])) if crumb else ""
    sub = '<div class="sms-shero__sub">%s</div>' % e(h["sub"]) if h.get("sub") else ""
    acts = '<div class="sms-shero__actions">%s</div>' % buttons(ctx, h["buttons"]) if h.get("buttons") else ""
    facts = "".join('<div class="sms-shero__fact">%s<span class="sms-shero__fact-text">%s</span></div>' % (icon(ic, "sms-shero__fact-icon"), e(t)) for ic, t in h.get("chips", [])[:2])
    ph = "team" if h["photo"] == "directors" else h["photo"]
    return """<section class="sms-shero">
  <div class="sms-shero__inner">
    <div class="sms-shero__copy">
      %s
      <div class="sms-kicker">%s</div>
      <h1 class="sms-shero__title">%s</h1>
      <div class="sms-shero__lead">%s%s</div>
      %s
    </div>
    <div class="sms-shero__panel">%s<span class="sms-shero__shade" aria-hidden="true"></span>%s<div class="sms-shero__facts">%s</div></div>
  </div>
</section>
""" % (crumb_html, e(h["eyebrow"]), e(h["title"]), sub, paras(h["body"]), acts, photo_img(ctx, ph, "sms-shero__img", lazy=False), radar(), facts)


def cta(ctx, d):
    btns = [(l, t) for l, t in d["buttons"] if t != "tel"]
    return """<section class="sms-scta">
  <div class="sms-scta__inner">
    <div class="sms-scta__box">
      %s
      <div class="sms-scta__copy"><h2 class="sms-scta__title">%s</h2><div class="sms-scta__text">%s</div></div>
      <div class="sms-scta__side"><div class="sms-scta__actions">%s</div><div class="sms-scta__call">Or call us on <a href="tel:%s">%s</a></div></div>
    </div>
  </div>
</section>
""" % (radar(), e(d["title"]), paras(d["text"]), buttons(ctx, btns) if btns else "", PHONE_TEL, PHONE)


def chrome_top(ctx):
    return header(ctx, "blue")


def chrome_bottom(ctx):
    return footer(ctx, "white")


# ---------------------------------------------------------------------------
# Sections
# ---------------------------------------------------------------------------

def scan(ctx):
    cells = "".join('<li class="sms-scan__cell">%s<span class="sms-scan__name">%s</span></li>' % (icon(ic, "sms-scan__icon"), e(t)) for ic, t in FACTORS)
    return """<section class="sms-scan" id="assessment">
  <div class="sms-scan__inner">
    <div class="sms-scan__copy">
      <div class="sms-kicker">Risk &amp; Needs Consultancy</div>
      <h2 class="sms-scan__title">First Aid Needs <span class="sms-mark">Assessment</span></h2>
      <div class="sms-scan__text"><p>We evaluate your workplace to determine the level of first aid provision required.</p><p>It reviews whether first aid staff, equipment, facilities and arrangements are suitable.</p></div>
      %s
    </div>
    <div class="sms-scan__panel">
      <span class="sms-scan__beam" aria-hidden="true"></span>
      <ul class="sms-scan__grid">%s</ul>
      <div class="sms-scan__out">%s<span class="sms-scan__out-text">Clear, proportionate actions to strengthen your provision</span></div>
    </div>
  </div>
</section>
""" % (buttons(ctx, [("Request a FREE initial Consultation", "book:consultancy")]), cells, icon("check", "sms-scan__out-icon"))


def stepper(ctx):
    radios, seg_html = dark.seg("step", ["Step %d" % (i + 1) for i in range(len(CONSULT))], 0, "Consultation steps")
    dots = "".join('<span class="sms-stepper__dot"></span>' for _ in CONSULT)
    panels = ""
    for i, it in enumerate(CONSULT):
        panels += '<div class="sms-stepper__p%d"><div class="sms-stepper__panel"><div class="sms-stepper__big" aria-hidden="true">%02d</div><div class="sms-stepper__body"><h3 class="sms-stepper__name">%s</h3><div class="sms-stepper__text"><p>%s</p></div></div></div></div>' % (
            i, i + 1, e(it["title"]), e(it["text"]))
    note = C.PAGES["risk-needs-consultancy"]["sections"][2][1]["note"][0]
    return """<section class="sms-stepper" id="consultation">
  %s
  <div class="sms-stepper__inner">
    <div class="sms-stepper__head">
      <div class="sms-stepper__heading"><div class="sms-kicker">Free initial consultation</div><h2 class="sms-stepper__title">How Your Free Initial <span class="sms-mark">Consultation</span> Works</h2></div>
      <div class="sms-stepper__intro"><p>This is a no-obligation conversation where we take the time to learn about your current arrangements, any concerns you may have, and what you are hoping to achieve.</p></div>
    </div>
    <div class="sms-stepper__card">
      %s
      <div class="sms-stepper__track" aria-hidden="true"><span class="sms-stepper__fill"></span><span class="sms-stepper__dots">%s</span></div>
      %s
      <div class="sms-stepper__note">%s<div class="sms-stepper__note-text"><p>%s</p></div></div>
      <div class="sms-stepper__actions">%s</div>
    </div>
  </div>
</section>
""" % (radios, seg_html, dots, panels, icon("alert", "sms-stepper__note-icon"), e(note), buttons(ctx, [("Request a FREE initial Consultation", "book:consultancy")]))


def career(ctx):
    radios = "".join('<input class="sms-seg__radio sms-career__r%d" type="radio" name="sms-career" id="sms-career-%d"%s>' % (i, i, " checked" if i == 0 else "") for i in range(len(STARTS)))
    starts = "".join('<label class="sms-career__start sms-career__start--%d" for="sms-career-%d">%s<span class="sms-career__start-text">%s</span></label>' % (
        i, i, icon(ic, "sms-career__start-icon"), e(t)) for i, (ic, t) in enumerate(STARTS))
    outs = "".join('<div class="sms-career__out sms-career__out--%d"><span class="sms-career__out-label">Your starting point</span><span class="sms-career__out-name">%s</span></div>' % (i, e(t)) for i, (_, t) in enumerate(STARTS))
    steps = "".join('<li class="sms-career__step"><span class="sms-career__num">%d</span><div class="sms-career__body"><h3 class="sms-career__name">%s</h3><div class="sms-career__desc"><p>%s</p></div></div></li>' % (
        i + 1, e(s["title"]), e(s["text"])) for i, s in enumerate(CAREER_STEPS))
    return """<section class="sms-career" id="career">
  %s
  <div class="sms-career__inner">
    <div class="sms-career__copy">
      <div class="sms-kicker">Pre-Hospital Career Support</div>
      <h2 class="sms-career__title">Starting Out in a Medical or <span class="sms-mark">Pre-Hospital Career?</span></h2>
      <div class="sms-career__text"><p>We offer tailored support for aspiring clinicians and pre-hospital professionals, helping you get ready for interviews, assessment days, and the next steps in your career.</p></div>
      <div class="sms-career__label">Support at every starting point</div>
      <div class="sms-career__starts" role="group" aria-label="Choose your starting point">%s</div>
    </div>
    <div class="sms-career__map" aria-live="polite">
      %s
      <ol class="sms-career__line">%s</ol>
      <div class="sms-career__actions">%s</div>
    </div>
  </div>
</section>
""" % (radios, starts, outs, steps, buttons(ctx, [("Complete this form to get started", "book:careers")]))


def inner_extra(ctx, slug):
    if slug == "risk-needs-consultancy":
        return scan(ctx) + stepper(ctx)
    if slug == "pre-hospital-career-support":
        return career(ctx)
    return ""


# ---------------------------------------------------------------------------
# Homepage
# ---------------------------------------------------------------------------

def home(ctx):
    ctx.notes.append("Image-only copy used: \"Clinician-led safety and medical support\" (clinician-led-safety.png)")
    links = "".join('<li class="sms-signal__item"><a class="sms-signal__link" href="%s">%s<span class="sms-signal__name">%s</span><span class="sms-signal__go" aria-hidden="true">&rarr;</span></a></li>' % (
        ctx.href(s["slug"]), icon(s["icon"], "sms-signal__icon"), e(s["title"])) for s in C.SERVICES)
    out = """<section class="sms-signal">
  %s
  <div class="sms-signal__inner">
    <div class="sms-kicker">Clinician-led safety and medical support</div>
    <h1 class="sms-signal__title">Assess the risk. <span class="sms-mark">Protect your people.</span></h1>
    <div class="sms-signal__lead"><p>%s</p></div>
    <div class="sms-signal__actions">%s</div>
  </div>
  <div class="sms-signal__band"><ul class="sms-signal__list">%s</ul></div>
</section>
""" % (radar(), e(C.INTRO2), buttons(ctx, [("Book online", "book"), ("Contact Us", "contact")]), links)
    out += scan(ctx)
    out += stepper(ctx)
    out += career(ctx)
    picks = ["Where is Streamline based?", "Who runs Streamline?", "Can Streamline provide more than one service?", "Do you offer a free initial discussion?", "Are you insured?", "How can I contact Streamline?"]
    allf = dict(C.faqs("home"))
    out += SHARED_RENDERERS["faq"](ctx, {"tone": "pale", "eyebrow": C.STRAP, "title": "General Streamline [[FAQs]]",
                                        "lead": ["Answers to common questions about Streamline Safety & Medical Solutions, our team, services, bookings and how we work."],
                                        "items": [(q, allf[q]) for q in picks], "show": 6})
    out += cta(ctx, {"title": "Have any questions? We’re here to help.",
                     "text": ["We offer an initial discussion to understand your requirements, and our risk and needs consultancy includes a free initial consultation before any chargeable work is agreed."],
                     "buttons": [("Book online", "book"), ("Contact Us", "contact")]})
    return out


def scripts(ctx, main):
    return ""
