"""Concept 11 - Contour. The refined, layered feel of the Pristine Motors round 4
concepts with new elements, in Streamline's original colours: fanned photo cards
that spread out, service panels that open up, flip cards for what to expect, a
bespoke-training topic explorer and a get-your-quote-ready checklist. Every
interactive piece is HTML and CSS only, so the whole concept works without
JavaScript."""
from common import *  # noqa: F401,F403
import content as C
import light

NAME = "Contour"
DARK = False
CINE = True
FONTS = "https://fonts.googleapis.com/css2?family=Outfit:wght@200;300;400;500;600;700&display=swap"

PANELS = [
    ("event-medical-cover", "Event Medical Cover", "festival", "heart", "Skilled. Proportionate. Reliable.", C.SERVICES[0]["text"],
     ["Community events and village fetes", "Sports and combat-sports events", "Small festivals and outdoor activities"]),
    ("medical-training", "Medical Training", "cpr-room", "cap", "Qualsafe Registered Centre", C.SERVICES[1]["text"],
     ["Emergency First Aid at Work", "First Aid at Work", "FREC 3 and FREC 4"]),
    ("risk-needs-consultancy", "Risk & Needs Consultancy", "assessor", "clipboard", "Free initial consultation", C.SERVICES[2]["text"],
     ["First Aid Needs Assessment", "Risk Assessment Writing", "Event Medical Plans"]),
    ("pre-hospital-career-support", "Pre-Hospital Career Support", "cpr-outdoor", "compass", "Honest, frontline-informed support", C.CAREERS["text"],
     ["Interview preparation", "Mock assessments", "Feedback & development"]),
    ("recruitment", "Recruitment", "team", "users", "Interested in working with us?", "We are looking to hear from experienced professionals who can support our growing services.",
     ["Trainers", "Safety operatives", "Clinicians"]),
]

SECTORS = [
    ("heart", "Care Homes & Social Care", ["Falls awareness", "Post-fall assessment", "Head injuries", "Pain recognition in people living with advanced dementia", "Recognising deterioration", "Sepsis awareness", "Common medical emergencies"]),
    ("trophy", "Sports Clubs & Activity Providers", ["Head injury and concussion awareness", "Fracture management", "Sprains and strains", "Bleeding", "Wound care", "Collapse and emergency response during sporting activities"]),
    ("school", "Schools & Education", ["Head injuries", "Asthma", "Anaphylaxis", "Seizures", "Bleeding", "Burns", "Minor injuries", "Responding to common medical emergencies involving children and young people"]),
    ("briefcase", "Workplaces & Businesses", ["Medical emergency awareness", "Incident response", "Escalation", "First aid refreshers", "Realistic scenario-based training based around your workplace risks"]),
    ("sparkle", "Something Specific?", []),
]

QUOTE = [("calendar", "Event type, date, times, venue and postcode"), ("users", "Expected attendance and age range"), ("music", "Activities and alcohol arrangements"),
         ("file", "Previous incidents and existing provision"), ("route", "Risk assessment, site plan and emergency access"), ("clipboard", "Any organiser or venue requirements")]


def _panels_css():
    n = len(PANELS)
    out = ""
    for i in range(n):
        r = ".sms-panels .sms-panels__r%d:checked" % i
        cols = " ".join("minmax(0, 3.6fr)" if j == i else "minmax(0, 1fr)" for j in range(n))
        out += "@media (min-width: 60em) {\n  %s ~ * .sms-panels__row { grid-template-columns: %s; }\n}\n" % (r, cols)
        out += "%s ~ * .sms-panels__panel--%d .sms-panels__body { opacity: 1; visibility: visible; transform: none; }\n" % (r, i)
        out += "%s ~ * .sms-panels__panel--%d .sms-panels__tab { opacity: 0; pointer-events: none; }\n" % (r, i)
        out += "%s ~ * .sms-panels__panel--%d { min-height: 26rem; }\n" % (r, i)
        out += "@media (max-width: 59.99em) {\n  %s ~ * .sms-panels__panel--%d .sms-panels__body { display: flex; }\n}\n" % (r, i)
        out += "%s ~ * .sms-panels__panel--%d .sms-panels__img { opacity: 1; transform: scale(1); }\n" % (r, i)
        out += ".sms-panels .sms-panels__r%d:focus-visible ~ * .sms-panels__panel--%d { outline: 3px solid var(--sms-accent); outline-offset: 3px; }\n" % (i, i)
    return out


def _explore_css():
    out = ".sms-explore .sms-explore__panel { display: none; }\n"
    for i in range(len(SECTORS)):
        r = ".sms-explore .sms-explore__r%d" % i
        out += "%s:checked ~ * .sms-explore__opt--%d { background: var(--sms-ink); color: #ffffff; box-shadow: none; }\n" % (r, i)
        out += "%s:checked ~ * .sms-explore__opt--%d .sms-explore__opt-icon { background: rgba(255, 255, 255, 0.12); color: #ffffff; }\n" % (r, i)
        out += "%s:focus-visible ~ * .sms-explore__opt--%d { outline: 3px solid var(--sms-accent); outline-offset: 3px; }\n" % (r, i)
        out += "%s:checked ~ * .sms-explore__panel--%d { display: block; }\n" % (r, i)
    return out


def _ready_css():
    n = len(QUOTE)
    out = ""
    for i in range(n):
        r = ".sms-ready .sms-ready__c%d" % i
        out += "%s:checked ~ * .sms-ready__seg--%d { opacity: 1; transform: none; }\n" % (r, i)
        out += "%s:checked ~ * .sms-ready__item--%d .sms-ready__box { background: var(--sms-accent); box-shadow: inset 0 0 0 2px var(--sms-accent); color: #ffffff; }\n" % (r, i)
        out += "%s:checked ~ * .sms-ready__item--%d .sms-ready__tick { opacity: 1; transform: none; }\n" % (r, i)
        out += "%s:checked ~ * .sms-ready__item--%d .sms-ready__label { color: var(--sms-ink-soft); text-decoration: line-through; text-decoration-color: rgba(64, 127, 54, 0.6); }\n" % (r, i)
        out += "%s:focus-visible ~ * .sms-ready__item--%d .sms-ready__box { outline: 3px solid var(--sms-accent); outline-offset: 3px; }\n" % (r, i)
    chain = " ~ ".join(".sms-ready__c%d:checked" % i for i in range(n))
    out += ".sms-ready %s ~ * .sms-ready__done { display: flex; }\n" % chain
    out += ".sms-ready %s ~ * .sms-ready__todo { display: none; }\n" % chain
    return out


CSS = light.css([".sms-ccta .sms-ccta__box", ".sms-footer"]) + r"""
/* ===== Concept 11 theme: contour ===== */
.sms-page { --sms-font: "Outfit", "Montserrat", Arial, sans-serif; --sms-radius: 1.75rem; --sms-radius-sm: 1rem; --sms-hw: 300; }
.sms-page .sms-mark { color: var(--sms-accent); font-weight: inherit; }

/* Fanned photo cards (used by the heroes) */
.sms-page .sms-fan { position: relative; width: min(100%, 30rem); margin: 0 auto; aspect-ratio: 1 / 1.05; }
.sms-page .sms-fan__card { position: absolute; left: 14%; top: 6%; width: 72%; aspect-ratio: 4 / 5; overflow: hidden; border-radius: 1.5rem; background: var(--sms-pale); box-shadow: 0 24px 50px rgba(6, 30, 53, 0.18); transition: transform 0.8s var(--sms-ease); }
.sms-page .sms-fan__card--0 { z-index: 3; transform: rotate(0deg); animation: sms-deal0 1s var(--sms-ease) backwards; }
.sms-page .sms-fan__card--1 { z-index: 2; transform: translateX(-16%) rotate(-8deg); animation: sms-deal1 1s var(--sms-ease) 0.12s backwards; }
.sms-page .sms-fan__card--2 { z-index: 1; transform: translateX(16%) rotate(8deg); animation: sms-deal2 1s var(--sms-ease) 0.24s backwards; }
.sms-page .sms-fan:hover .sms-fan__card--1 { transform: translateX(-34%) rotate(-14deg); }
.sms-page .sms-fan:hover .sms-fan__card--2 { transform: translateX(34%) rotate(14deg); }
.sms-page .sms-fan:hover .sms-fan__card--0 { transform: translateY(-3%); }
.sms-page .sms-fan__img { display: block; width: 100%; height: 100%; object-fit: cover; }
.sms-page .sms-fan__label { position: absolute; left: 0.9rem; bottom: 0.9rem; display: inline-flex; align-items: center; gap: 0.45rem; max-width: calc(100% - 1.8rem); padding: 0.45rem 0.85rem 0.45rem 0.5rem; border-radius: 999px; background: rgba(255, 255, 255, 0.92); color: var(--sms-ink); font-size: var(--sms-step--1); font-weight: 500; }
.sms-page .sms-fan__label-icon { width: 1.5rem; height: 1.5rem; padding: 0.25rem; border-radius: 50%; background: var(--sms-mint); color: var(--sms-accent); }
.sms-page .sms-fan__label-text { min-width: 0; }
@keyframes sms-deal0 { from { transform: translateY(12%) rotate(0deg); } to { transform: rotate(0deg); } }
@keyframes sms-deal1 { from { transform: translateY(12%) rotate(0deg); } to { transform: translateX(-16%) rotate(-8deg); } }
@keyframes sms-deal2 { from { transform: translateY(12%) rotate(0deg); } to { transform: translateX(16%) rotate(8deg); } }

/* ---------- Page hero (inner pages): text and a fan of photos ---------- */
.sms-chero { position: relative; overflow: hidden; padding: clamp(3rem, 2rem + 4vw, 5.5rem) 0 clamp(3rem, 2rem + 3vw, 5rem); background: radial-gradient(60rem 30rem at 90% 10%, rgba(64, 127, 54, 0.1), transparent 60%), linear-gradient(180deg, var(--sms-pale), var(--sms-bg)); }
.sms-chero .sms-chero__inner { display: grid; gap: clamp(2.5rem, 1.5rem + 4vw, 4rem); align-items: center; width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-chero .sms-chero__copy { min-width: 0; }
.sms-chero .sms-chero__crumb { margin-bottom: 1.5rem; color: var(--sms-ink-soft); font-size: var(--sms-step--1); }
.sms-chero .sms-chero__crumb-link { color: var(--sms-ink); }
.sms-chero .sms-chero__title { margin: 0 0 1.5rem; color: var(--sms-title); font-size: clamp(2.4rem, 1.4rem + 4vw, 4.8rem); font-weight: 300; line-height: 1.04; letter-spacing: -0.035em; }
.sms-chero .sms-chero__sub { margin-bottom: 0.6rem; color: var(--sms-accent); font-weight: 500; }
.sms-chero .sms-chero__lead { max-width: 36rem; color: var(--sms-ink); font-size: var(--sms-step-1); font-weight: 300; line-height: 1.65; }
.sms-chero .sms-chero__lead p { margin: 0 0 0.75rem; }
.sms-chero .sms-chero__actions { display: flex; flex-wrap: wrap; gap: 0.75rem; margin-top: 1.75rem; }
.sms-chero .sms-chero__pills { margin-top: 1.5rem; }
.sms-chero .sms-chero__media { min-width: 0; }
@media (min-width: 60em) {
  .sms-chero .sms-chero__inner { grid-template-columns: minmax(0, 1.1fr) minmax(0, 0.9fr); }
}

/* ---------- CTA (brand green band) ---------- */
.sms-ccta { padding: var(--sms-section) 0; }
.sms-ccta .sms-ccta__inner { width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-ccta .sms-ccta__box { position: relative; display: grid; gap: 2rem; align-items: center; overflow: hidden; padding: clamp(2rem, 1.2rem + 3.5vw, 4.5rem); border-radius: var(--sms-radius); background: #407f36; color: #ffffff; }
.sms-ccta .sms-ccta__box::before { content: ""; position: absolute; right: -8rem; top: -10rem; width: 28rem; height: 28rem; border-radius: 50%; background: radial-gradient(closest-side, rgba(255, 255, 255, 0.16), transparent); animation: sms-float 12s ease-in-out infinite; pointer-events: none; }
.sms-ccta .sms-ccta__copy { position: relative; min-width: 0; }
.sms-ccta .sms-ccta__title { margin: 0 0 1rem; color: #ffffff; font-size: clamp(2rem, 1.3rem + 2.8vw, 3.5rem); font-weight: 300; line-height: 1.08; letter-spacing: -0.03em; }
.sms-ccta .sms-ccta__text { max-width: 36rem; color: #ffffff; }
.sms-ccta .sms-ccta__text p { margin: 0; }
.sms-ccta .sms-ccta__side { position: relative; display: grid; gap: 1rem; justify-items: start; min-width: 0; }
.sms-ccta .sms-ccta__actions { display: flex; flex-wrap: wrap; gap: 0.75rem; min-width: 0; }
.sms-ccta .sms-btn--primary { border-color: #ffffff; background: #ffffff; color: #061e35; }
.sms-ccta .sms-btn--primary:hover { box-shadow: 0 12px 40px rgba(6, 30, 53, 0.25); }
.sms-ccta .sms-btn--outline { border-color: rgba(255, 255, 255, 0.7); color: #ffffff; }
.sms-ccta .sms-btn--outline:hover { border-color: #ffffff; background: transparent; color: #ffffff; }
.sms-ccta .sms-ccta__call { min-width: 0; color: #ffffff; font-size: var(--sms-step--1); }
.sms-ccta .sms-ccta__call a { color: #ffffff; font-weight: 600; text-underline-offset: 4px; }
@media (min-width: 60em) {
  .sms-ccta .sms-ccta__box { grid-template-columns: minmax(0, 1.5fr) minmax(0, 1fr); }
  .sms-ccta .sms-ccta__side { justify-items: end; text-align: right; }
}

/* ---------- Home hero ---------- */
.sms-contour { position: relative; overflow: hidden; padding: clamp(3.5rem, 2.5rem + 4vw, 6.5rem) 0 clamp(3rem, 2rem + 3vw, 5rem); background: radial-gradient(60rem 34rem at 85% 0%, rgba(64, 127, 54, 0.12), transparent 60%), linear-gradient(180deg, var(--sms-pale), var(--sms-bg)); }
.sms-contour .sms-contour__inner { display: grid; gap: clamp(2.5rem, 1.5rem + 4vw, 4rem); align-items: center; width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-contour .sms-contour__copy { min-width: 0; }
.sms-contour .sms-contour__title { margin: 0 0 1.5rem; color: var(--sms-title); font-size: clamp(2.7rem, 1.3rem + 5.4vw, 6rem); font-weight: 300; line-height: 1; letter-spacing: -0.04em; }
.sms-contour .sms-contour__line { display: block; }
.sms-contour .sms-contour__lead { max-width: 34rem; color: var(--sms-ink); font-size: var(--sms-step-1); font-weight: 300; line-height: 1.65; }
.sms-contour .sms-contour__lead p { margin: 0; }
.sms-contour .sms-contour__actions { display: flex; flex-wrap: wrap; gap: 0.75rem; margin-top: 2rem; }
.sms-contour .sms-contour__pills { margin-top: 1.5rem; }
.sms-contour .sms-contour__media { min-width: 0; }
@media (min-width: 60em) {
  .sms-contour .sms-contour__inner { grid-template-columns: minmax(0, 1.05fr) minmax(0, 0.95fr); }
}

/* ---------- Service panels that open up ---------- */
.sms-panels { padding: var(--sms-section) 0; }
.sms-panels .sms-panels__inner { width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-panels .sms-panels__head { display: grid; gap: 1.25rem; align-items: end; margin-bottom: clamp(2rem, 1.5rem + 2vw, 3rem); }
.sms-panels .sms-panels__heading { min-width: 0; }
.sms-panels .sms-panels__title { margin: 0; color: var(--sms-title); font-size: clamp(2.2rem, 1.3rem + 3.4vw, 4.2rem); font-weight: 300; line-height: 1.05; letter-spacing: -0.035em; }
.sms-panels .sms-panels__intro { max-width: 28rem; min-width: 0; color: var(--sms-ink-soft); }
.sms-panels .sms-panels__intro p { margin: 0; }
.sms-panels .sms-panels__row { display: grid; gap: 0.75rem; }
.sms-panels .sms-panels__panel { position: relative; min-width: 0; min-height: 4.75rem; overflow: hidden; border-radius: 1.5rem; background: var(--sms-navy); color: #ffffff; }
.sms-panels .sms-panels__img { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; opacity: 0.45; transform: scale(1.08); transition: opacity 0.8s var(--sms-ease), transform 1.2s var(--sms-ease); }
.sms-panels .sms-panels__shade { position: absolute; inset: 0; background: linear-gradient(0deg, rgba(6, 30, 53, 0.95) 20%, rgba(6, 30, 53, 0.6) 100%); }
.sms-panels .sms-panels__tab { position: absolute; inset: 0; z-index: 2; display: flex; align-items: center; gap: 0.9rem; padding: 1rem 1.25rem; cursor: pointer; transition: opacity 0.4s var(--sms-ease); }
.sms-panels .sms-panels__tab:hover .sms-panels__tab-name { color: #c6f2b8; }
.sms-panels .sms-panels__num { min-width: 0; color: rgba(255, 255, 255, 0.75); font-size: 0.8125rem; letter-spacing: 0.18em; }
.sms-panels .sms-panels__tab-name { min-width: 0; font-size: var(--sms-step-1); font-weight: 400; transition: color 0.3s; }
.sms-panels .sms-panels__body { position: relative; z-index: 3; display: flex; flex-direction: column; justify-content: flex-end; height: 100%; min-height: inherit; padding: clamp(1.5rem, 1rem + 1.5vw, 2.5rem); opacity: 0; visibility: hidden; transform: translateY(14px); transition: opacity 0.6s var(--sms-ease), transform 0.6s var(--sms-ease), visibility 0s; }
.sms-panels .sms-panels__meta { display: inline-flex; align-items: center; gap: 0.5rem; margin-bottom: 0.75rem; color: #c6f2b8; font-size: var(--sms-step--1); font-weight: 500; }
.sms-panels .sms-panels__meta-icon { width: 1.1rem; height: 1.1rem; }
.sms-panels .sms-panels__name { margin: 0 0 0.75rem; color: #ffffff; font-size: clamp(1.8rem, 1.3rem + 2vw, 2.9rem); font-weight: 300; line-height: 1.08; letter-spacing: -0.025em; }
.sms-panels .sms-panels__text { max-width: 34rem; color: rgba(255, 255, 255, 0.86); }
.sms-panels .sms-panels__text p { margin: 0 0 1.1rem; }
.sms-panels .sms-panels__pills .sms-pill { box-shadow: inset 0 0 0 1px rgba(255, 255, 255, 0.35); color: #ffffff; }
.sms-panels .sms-panels__link { display: inline-flex; align-items: center; gap: 0.5rem; margin-top: 1.25rem; color: #ffffff; font-weight: 500; }
@media (max-width: 59.99em) {
  .sms-panels .sms-panels__body { display: none; }
}
@media (min-width: 60em) {
  .sms-panels .sms-panels__head { grid-template-columns: minmax(0, 1.2fr) minmax(0, 0.8fr); }
  .sms-panels .sms-panels__intro { justify-self: end; }
  .sms-panels .sms-panels__row { grid-template-columns: repeat(5, minmax(0, 1fr)); height: 30rem; }
  .sms-panels .sms-panels__panel { min-height: 0; }
  .sms-panels .sms-panels__tab { flex-direction: column; align-items: flex-start; justify-content: space-between; padding: 1.5rem 1.25rem; }
  .sms-panels .sms-panels__tab-name { font-size: var(--sms-step-0); line-height: 1.3; }
}
""" + _panels_css() + r"""

/* ---------- Flip cards: what to expect ---------- */
.sms-flip { padding: var(--sms-section) 0; background: var(--sms-pale); }
.sms-flip .sms-flip__inner { width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-flip .sms-flip__head { max-width: 44rem; margin-bottom: clamp(2rem, 1.5rem + 2vw, 3rem); }
.sms-flip .sms-flip__title { margin: 0 0 1rem; color: var(--sms-title); font-size: clamp(2.2rem, 1.3rem + 3.2vw, 4rem); font-weight: 300; line-height: 1.05; letter-spacing: -0.035em; }
.sms-flip .sms-flip__lead { color: var(--sms-ink-soft); }
.sms-flip .sms-flip__lead p { margin: 0 0 0.5rem; }
.sms-flip .sms-flip__grid { display: grid; gap: 1rem; margin: 0; padding: 0; list-style: none; }
.sms-flip .sms-flip__item { min-width: 0; perspective: 1200px; }
.sms-flip .sms-flip__toggle { position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0); clip-path: inset(50%); white-space: nowrap; }
.sms-flip .sms-flip__card { position: relative; display: block; min-height: 16rem; cursor: pointer; transform-style: preserve-3d; transition: transform 0.8s var(--sms-ease); }
.sms-flip .sms-flip__face { position: absolute; inset: 0; display: flex; flex-direction: column; padding: 1.75rem; border-radius: 1.5rem; -webkit-backface-visibility: hidden; backface-visibility: hidden; }
.sms-flip .sms-flip__face--front { justify-content: space-between; background: var(--sms-surface); box-shadow: inset 0 0 0 1px var(--sms-line), 0 14px 34px rgba(6, 30, 53, 0.06); }
.sms-flip .sms-flip__face--back { justify-content: center; background: var(--sms-navy); color: #ffffff; transform: rotateY(180deg); }
.sms-flip .sms-flip__icon { width: 3.25rem; height: 3.25rem; padding: 0.75rem; border-radius: 50%; background: var(--sms-mint); color: var(--sms-accent); }
.sms-flip .sms-flip__name { display: block; color: var(--sms-title); font-size: var(--sms-step-1); font-weight: 400; line-height: 1.3; }
.sms-flip .sms-flip__hint { display: inline-flex; align-items: center; gap: 0.4rem; margin-top: 0.5rem; color: var(--sms-accent); font-size: var(--sms-step--1); font-weight: 500; }
.sms-flip .sms-flip__hint-icon { width: 1rem; height: 1rem; }
.sms-flip .sms-flip__back-name { display: block; margin-bottom: 0.75rem; color: #c6f2b8; font-size: var(--sms-step--1); font-weight: 500; letter-spacing: 0.16em; text-transform: uppercase; }
.sms-flip .sms-flip__back-text { display: block; font-size: var(--sms-step-1); font-weight: 300; line-height: 1.5; }
.sms-flip .sms-flip__toggle:checked + .sms-flip__card { transform: rotateY(180deg); }
.sms-flip .sms-flip__toggle:focus-visible + .sms-flip__card .sms-flip__face { outline: 3px solid var(--sms-accent); outline-offset: 3px; }
.sms-flip .sms-flip__steps { display: flex; flex-wrap: wrap; align-items: center; gap: 0.75rem; margin-top: 2rem; color: var(--sms-ink-soft); font-size: var(--sms-step--1); letter-spacing: 0.2em; text-transform: uppercase; }
.sms-flip .sms-flip__card:hover .sms-flip__face--front { box-shadow: inset 0 0 0 1px var(--sms-line-green), 0 18px 40px rgba(6, 30, 53, 0.1); }
.sms-flip .sms-flip__step,
.sms-flip .sms-flip__front-body,
.sms-flip .sms-flip__icon,
.sms-flip .sms-flip__back-name,
.sms-flip .sms-flip__back-text,
.sms-panels .sms-panels__meta,
.sms-panels .sms-panels__name,
.sms-panels .sms-panels__text,
.sms-panels .sms-panels__link,
.sms-panels .sms-pills { min-width: 0; }
@media (min-width: 46em) {
  .sms-flip .sms-flip__grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
}
@media (min-width: 64em) {
  .sms-flip .sms-flip__grid { grid-template-columns: repeat(4, minmax(0, 1fr)); }
}

/* ---------- Bespoke training topic explorer ---------- */
.sms-explore { padding: var(--sms-section) 0; }
.sms-explore .sms-explore__inner { display: grid; gap: clamp(2rem, 1.5rem + 3vw, 4rem); width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-explore .sms-explore__copy { min-width: 0; }
.sms-explore .sms-explore__title { margin: 0 0 1.25rem; color: var(--sms-title); font-size: clamp(2.2rem, 1.3rem + 3.2vw, 4rem); font-weight: 300; line-height: 1.05; letter-spacing: -0.035em; }
.sms-explore .sms-explore__text { max-width: 32rem; color: var(--sms-ink-soft); }
.sms-explore .sms-explore__text p { margin: 0 0 1rem; }
.sms-explore .sms-explore__opts { display: flex; flex-wrap: wrap; gap: 0.5rem; margin-top: 1.5rem; }
.sms-explore .sms-explore__opt { display: inline-flex; align-items: center; gap: 0.6rem; min-width: 0; padding: 0.5rem 1rem 0.5rem 0.5rem; border-radius: 999px; background: var(--sms-surface); box-shadow: inset 0 0 0 1px var(--sms-line); color: var(--sms-ink); cursor: pointer; font-weight: 400; transition: background-color 0.3s, color 0.3s, transform 0.3s var(--sms-ease); }
.sms-explore .sms-explore__opt:hover { transform: translateY(-2px); }
.sms-explore .sms-explore__opt-icon { width: 2rem; height: 2rem; padding: 0.45rem; border-radius: 50%; background: var(--sms-mint); color: var(--sms-accent); }
.sms-explore .sms-explore__opt-text { min-width: 0; }
.sms-explore .sms-explore__stage { min-width: 0; }
.sms-explore .sms-explore__panel { padding: clamp(1.5rem, 1rem + 2vw, 2.5rem); border-radius: var(--sms-radius); background: radial-gradient(70% 90% at 100% 0%, rgba(64, 127, 54, 0.12), transparent 60%), var(--sms-pale); box-shadow: inset 0 0 0 1px var(--sms-line); }
.sms-explore .sms-explore__name { margin: 0 0 1.25rem; color: var(--sms-title); font-size: clamp(1.6rem, 1.3rem + 1.4vw, 2.3rem); font-weight: 300; line-height: 1.15; }
.sms-explore .sms-explore__tags { display: flex; flex-wrap: wrap; gap: 0.5rem; margin: 0; padding: 0; list-style: none; }
.sms-explore .sms-explore__tag { min-width: 0; padding: 0.55rem 1rem; border-radius: 999px; background: var(--sms-surface); box-shadow: inset 0 0 0 1px var(--sms-line-green); color: var(--sms-ink); font-size: var(--sms-step--1); animation: sms-fade-up 0.5s var(--sms-ease) both; }
.sms-explore .sms-explore__tag:nth-child(2) { animation-delay: 0.05s; }
.sms-explore .sms-explore__tag:nth-child(3) { animation-delay: 0.1s; }
.sms-explore .sms-explore__tag:nth-child(4) { animation-delay: 0.15s; }
.sms-explore .sms-explore__tag:nth-child(5) { animation-delay: 0.2s; }
.sms-explore .sms-explore__tag:nth-child(6) { animation-delay: 0.25s; }
.sms-explore .sms-explore__tag:nth-child(7) { animation-delay: 0.3s; }
.sms-explore .sms-explore__tag:nth-child(8) { animation-delay: 0.35s; }
.sms-explore .sms-explore__note { margin-top: 1.5rem; color: var(--sms-ink-soft); font-size: var(--sms-step--1); }
.sms-explore .sms-explore__note p { margin: 0 0 1rem; }
""" + _explore_css() + r"""
@media (min-width: 60em) {
  .sms-explore .sms-explore__inner { grid-template-columns: minmax(0, 0.9fr) minmax(0, 1.1fr); align-items: start; }
}

/* ---------- Get your quote ready checklist ---------- */
.sms-ready { padding: var(--sms-section) 0; background: var(--sms-pale); counter-reset: sms-ready; }
.sms-ready .sms-ready__in { position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0); clip-path: inset(50%); white-space: nowrap; }
.sms-ready .sms-ready__in:checked { counter-increment: sms-ready; }
.sms-ready .sms-ready__inner { display: grid; gap: clamp(2rem, 1.5rem + 3vw, 4rem); width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-ready .sms-ready__copy { min-width: 0; }
.sms-ready .sms-ready__title { margin: 0 0 1.25rem; color: var(--sms-title); font-size: clamp(2.2rem, 1.3rem + 3.2vw, 4rem); font-weight: 300; line-height: 1.05; letter-spacing: -0.035em; }
.sms-ready .sms-ready__text { max-width: 32rem; color: var(--sms-ink-soft); }
.sms-ready .sms-ready__text p { margin: 0 0 1rem; }
.sms-ready .sms-ready__panel { min-width: 0; padding: clamp(1.5rem, 1rem + 2vw, 2.5rem); border-radius: var(--sms-radius); background: var(--sms-surface); box-shadow: inset 0 0 0 1px var(--sms-line), var(--sms-shadow-lg); }
.sms-ready .sms-ready__bar { display: grid; grid-template-columns: repeat(6, minmax(0, 1fr)); gap: 0.35rem; margin-bottom: 0.75rem; }
.sms-ready .sms-ready__seg { min-width: 0; height: 0.5rem; border-radius: 999px; background: var(--sms-accent); opacity: 0.15; transform: scaleY(0.6); transition: opacity 0.4s var(--sms-ease), transform 0.4s var(--sms-ease); }
.sms-ready .sms-ready__count { margin-bottom: 1.25rem; color: var(--sms-ink-soft); font-size: var(--sms-step--1); }
.sms-ready .sms-ready__count-n::before { content: counter(sms-ready); color: var(--sms-title); font-weight: 600; }
.sms-ready .sms-ready__list { display: grid; gap: 0.5rem; margin: 0; padding: 0; list-style: none; }
.sms-ready .sms-ready__item { min-width: 0; }
.sms-ready .sms-ready__label { display: flex; align-items: center; gap: 0.9rem; min-width: 0; padding: 0.85rem 1rem; border-radius: 1rem; background: var(--sms-pale); color: var(--sms-ink); cursor: pointer; transition: color 0.3s; }
.sms-ready .sms-ready__box { position: relative; display: grid; place-items: center; flex: 0 0 auto; min-width: 0; width: 1.6rem; height: 1.6rem; border-radius: 0.5rem; background: var(--sms-surface); box-shadow: inset 0 0 0 2px var(--sms-line); color: transparent; }
.sms-ready .sms-ready__tick { width: 1.1rem; height: 1.1rem; color: #ffffff; opacity: 0; transform: scale(0.4); transition: opacity 0.3s, transform 0.3s var(--sms-ease); }
.sms-ready .sms-ready__icon { width: 1.25rem; height: 1.25rem; color: var(--sms-accent); }
.sms-ready .sms-ready__words { min-width: 0; }
.sms-ready .sms-ready__done { display: none; align-items: center; gap: 0.75rem; margin-top: 1.25rem; padding: 1rem 1.25rem; border-radius: 1rem; background: var(--sms-mint); color: var(--sms-ink); font-weight: 500; animation: sms-fade-up 0.5s var(--sms-ease) both; }
.sms-ready .sms-ready__done-icon { color: var(--sms-accent); }
.sms-ready .sms-ready__done-text { min-width: 0; }
.sms-ready .sms-ready__todo { margin-top: 1.25rem; color: var(--sms-ink-soft); font-size: var(--sms-step--1); }
.sms-ready .sms-ready__todo p { margin: 0; }
.sms-ready .sms-ready__actions { display: flex; flex-wrap: wrap; gap: 0.75rem; margin-top: 1.5rem; }
""" + _ready_css() + r"""
@media (min-width: 60em) {
  .sms-ready .sms-ready__inner { grid-template-columns: minmax(0, 0.9fr) minmax(0, 1.1fr); align-items: center; }
}
"""

RISE = [".sms-chero .sms-chero__title", ".sms-contour .sms-contour__title"]
ENTRANCE = [".sms-chero .sms-chero__crumb", ".sms-chero .sms-kicker", ".sms-contour .sms-kicker", ".sms-chero .sms-chero__lead", ".sms-contour .sms-contour__lead",
            ".sms-chero .sms-chero__actions", ".sms-contour .sms-contour__actions"]
REVEAL = [".sms-panels .sms-panels__head", ".sms-panels .sms-panels__row", ".sms-flip .sms-flip__head", ".sms-flip .sms-flip__item",
          ".sms-explore .sms-explore__copy", ".sms-explore .sms-explore__stage", ".sms-ready .sms-ready__copy", ".sms-ready .sms-ready__panel", ".sms-ccta .sms-ccta__box"]
LOOP = [".sms-page .sms-fan__card--0", ".sms-page .sms-fan__card--1", ".sms-page .sms-fan__card--2", ".sms-ccta .sms-ccta__box::before",
        ".sms-explore .sms-explore__tag", ".sms-ready .sms-ready__done"]
TRANS = [".sms-page .sms-fan__card", ".sms-panels .sms-panels__img", ".sms-panels .sms-panels__tab", ".sms-panels .sms-panels__tab-name", ".sms-panels .sms-panels__body",
         ".sms-flip .sms-flip__card", ".sms-explore .sms-explore__opt", ".sms-ready .sms-ready__seg", ".sms-ready .sms-ready__tick", ".sms-ready .sms-ready__label"]

SKIP = {"medical-training": [2], "event-medical-cover": [2]}

FAN_EXTRAS = ["team", "festival", "cpr-room", "assessor", "session", "stall", "fete"]


def fan(ctx, photos, labels=None, lazy=False):
    cards = ""
    for i, ph in enumerate(photos[:3]):
        lab = ""
        if labels and i < len(labels) and labels[i]:
            ic, t = labels[i]
            lab = '<span class="sms-fan__label">%s<span class="sms-fan__label-text">%s</span></span>' % (icon(ic, "sms-fan__label-icon"), e(t))
        cards += '<div class="sms-fan__card sms-fan__card--%d">%s%s</div>' % (i, photo_img(ctx, ph, "sms-fan__img", lazy=lazy if i == 0 else True, decorative=i > 0), lab)
    return '<div class="sms-fan">%s</div>' % cards


def page_hero(ctx, h, crumb=True):
    crumb_html = '<div class="sms-chero__crumb"><a class="sms-chero__crumb-link" href="%s">Home</a> / %s</div>' % (ctx.href("home"), e(LABEL[ctx.slug])) if crumb else ""
    sub = '<div class="sms-chero__sub">%s</div>' % e(h["sub"]) if h.get("sub") else ""
    acts = '<div class="sms-chero__actions">%s</div>' % buttons(ctx, h["buttons"]) if h.get("buttons") else ""
    pills = "".join('<li class="sms-pills__item"><span class="sms-pill">%s</span></li>' % e(t) for _, t in h.get("chips", []))
    main = "team" if h["photo"] == "directors" else h["photo"]
    extras = [p for p in FAN_EXTRAS if p != main][:2]
    return """<section class="sms-chero">
  <div class="sms-chero__inner">
    <div class="sms-chero__copy">
      %s
      <div class="sms-kicker">%s</div>
      <h1 class="sms-chero__title">%s</h1>
      <div class="sms-chero__lead">%s%s</div>
      %s
      <ul class="sms-pills sms-chero__pills">%s</ul>
    </div>
    <div class="sms-chero__media">%s</div>
  </div>
</section>
""" % (crumb_html, e(h["eyebrow"]), e(h["title"]), sub, paras(h["body"]), acts, pills, fan(ctx, [main] + extras))


def cta(ctx, d):
    btns = [(l, t) for l, t in d["buttons"] if t != "tel"]
    return """<section class="sms-ccta">
  <div class="sms-ccta__inner">
    <div class="sms-ccta__box">
      <div class="sms-ccta__copy"><h2 class="sms-ccta__title">%s</h2><div class="sms-ccta__text">%s</div></div>
      <div class="sms-ccta__side"><div class="sms-ccta__actions">%s</div><div class="sms-ccta__call">Or call us on <a href="tel:%s">%s</a></div></div>
    </div>
  </div>
</section>
""" % (e(d["title"]), paras(d["text"]), buttons(ctx, btns) if btns else "", PHONE_TEL, PHONE)


def chrome_top(ctx):
    return header(ctx, "blue")


def chrome_bottom(ctx):
    return footer(ctx, "white")


# ---------------------------------------------------------------------------
# Sections (all HTML and CSS: radios and checkboxes, no script)
# ---------------------------------------------------------------------------

def panels(ctx):
    radios = "".join('<input class="sms-seg__radio sms-panels__r%d" type="radio" name="sms-panels" id="sms-panels-%d"%s>' % (i, i, " checked" if i == 0 else "") for i in range(len(PANELS)))
    cells = ""
    for i, (slug, title, ph, ic, meta, text, pills) in enumerate(PANELS):
        pl = "".join('<li class="sms-pills__item"><span class="sms-pill">%s</span></li>' % e(p) for p in pills)
        cells += """<div class="sms-panels__panel sms-panels__panel--%d">
        %s<span class="sms-panels__shade" aria-hidden="true"></span>
        <label class="sms-panels__tab" for="sms-panels-%d"><span class="sms-panels__num">%02d</span><span class="sms-panels__tab-name">%s</span></label>
        <div class="sms-panels__body">
          <div class="sms-panels__meta">%s%s</div>
          <h3 class="sms-panels__name">%s</h3>
          <div class="sms-panels__text"><p>%s</p></div>
          <ul class="sms-pills sms-panels__pills">%s</ul>
          <a class="sms-panels__link" href="%s">Find out more&nbsp;<span class="sms-arrow" aria-hidden="true">&rarr;</span></a>
        </div>
      </div>""" % (i, photo_img(ctx, ph, "sms-panels__img", decorative=True), i, i + 1, e(title), icon(ic, "sms-panels__meta-icon"), e(meta), e(title), e(text), pl, ctx.href(slug))
    return """<section class="sms-panels" id="services">
  %s
  <div class="sms-panels__inner">
    <div class="sms-panels__head">
      <div class="sms-panels__heading"><div class="sms-kicker">Our Services</div><h2 class="sms-panels__title">What We <span class="sms-mark">Provide</span></h2></div>
      <div class="sms-panels__intro"><p>Choose a service to open it up. %s</p></div>
    </div>
    <div class="sms-panels__row">%s</div>
  </div>
</section>
""" % (radios, e(C.INTRO), cells)


def flip(ctx):
    items = C.PAGES["medical-training"]["sections"][2][1]["items"]
    cards = ""
    for i, it in enumerate(items):
        cards += """<li class="sms-flip__item"><input class="sms-flip__toggle" type="checkbox" id="sms-flip-%d"><label class="sms-flip__card" for="sms-flip-%d">
          <span class="sms-flip__face sms-flip__face--front">%s<span class="sms-flip__front-body"><span class="sms-flip__name">%s</span><span class="sms-flip__hint">Turn over%s</span></span></span>
          <span class="sms-flip__face sms-flip__face--back"><span class="sms-flip__back-name">%s</span><span class="sms-flip__back-text">%s</span></span>
        </label></li>""" % (i, i, icon(it["icon"], "sms-flip__icon"), e(it["title"]), icon("arrow", "sms-flip__hint-icon"), e(it["title"]), e(it["text"]))
    return """<section class="sms-flip" id="expect">
  <div class="sms-flip__inner">
    <div class="sms-flip__head"><div class="sms-kicker">Your training experience</div><h2 class="sms-flip__title">What to <span class="sms-mark">expect</span></h2>
      <div class="sms-flip__lead"><p>Practical training designed to help you build confidence, apply skills and respond effectively in real-world situations.</p></div></div>
    <ul class="sms-flip__grid">%s</ul>
    <div class="sms-flip__steps" aria-hidden="true"><span class="sms-flip__step">Learn</span><span class="sms-flip__step">&middot;</span><span class="sms-flip__step">Practise</span><span class="sms-flip__step">&middot;</span><span class="sms-flip__step">Apply</span></div>
  </div>
</section>
""" % cards


def explore(ctx):
    radios = "".join('<input class="sms-seg__radio sms-explore__r%d" type="radio" name="sms-explore" id="sms-explore-%d"%s>' % (i, i, " checked" if i == 0 else "") for i in range(len(SECTORS)))
    opts = "".join('<label class="sms-explore__opt sms-explore__opt--%d" for="sms-explore-%d">%s<span class="sms-explore__opt-text">%s</span></label>' % (
        i, i, icon(ic, "sms-explore__opt-icon"), e(n)) for i, (ic, n, _) in enumerate(SECTORS))
    panels_html = ""
    for i, (ic, name, topics) in enumerate(SECTORS):
        if topics:
            body = '<ul class="sms-explore__tags">%s</ul>' % "".join('<li class="sms-explore__tag">%s</li>' % e(t) for t in topics)
        else:
            body = '<div class="sms-explore__note"><p>If there is a particular condition, injury, scenario or area of medical training you would like your team to understand better, we can discuss creating a session specifically around your requirements.</p></div>'
        panels_html += '<div class="sms-explore__panel sms-explore__panel--%d"><h3 class="sms-explore__name">%s</h3>%s</div>' % (i, e(name), body)
    return """<section class="sms-explore" id="bespoke">
  %s
  <div class="sms-explore__inner">
    <div class="sms-explore__copy">
      <div class="sms-kicker">Group Bookings</div>
      <h2 class="sms-explore__title">Group &amp; Bespoke <span class="sms-mark">Training</span></h2>
      <div class="sms-explore__text"><p>Booking training as a group is a great way to support your workplace, club or organisation with practical training tailored to the people, risks and situations your team may face.</p></div>
      <div class="sms-explore__opts" role="group" aria-label="Examples of bespoke training">%s</div>
    </div>
    <div class="sms-explore__stage" aria-live="polite">
      %s
      <div class="sms-explore__note"><p>If you would like a tailored package, simply select &ldquo;Bespoke Course&rdquo; on the booking form and tell us what you would like the training to cover.</p>%s</div>
    </div>
  </div>
</section>
""" % (radios, opts, panels_html, buttons(ctx, [("Book your next training session", "book:training")]))


def ready(ctx, with_booking=False):
    ins = "".join('<input class="sms-ready__in sms-ready__c%d" type="checkbox" id="sms-ready-%d">' % (i, i) for i in range(len(QUOTE)))
    segs = "".join('<span class="sms-ready__seg sms-ready__seg--%d"></span>' % i for i in range(len(QUOTE)))
    items = "".join('<li class="sms-ready__item sms-ready__item--%d"><label class="sms-ready__label" for="sms-ready-%d"><span class="sms-ready__box" aria-hidden="true">%s</span>%s<span class="sms-ready__words">%s</span></label></li>' % (
        i, i, icon("check", "sms-ready__tick"), icon(ic, "sms-ready__icon"), e(t)) for i, (ic, t) in enumerate(QUOTE))
    extra = ""
    if with_booking:
        body = C.PAGES["event-medical-cover"]["sections"][2][1]["body"]
        extra = "<p>%s</p>%s" % (e(body[0]), more(paras(body[1:])))
        ctx.notes.append("Image-only copy used: \"Book Your Event Medical Cover\" heading (book-your-medical-cover.png)")
    title = "Book Your Event Medical Cover" if with_booking else "What information is needed for a [[quote?]]"
    return """<section class="sms-ready" id="quote">
  %s
  <div class="sms-ready__inner">
    <div class="sms-ready__copy">
      <div class="sms-kicker">%s</div>
      <h2 class="sms-ready__title">%s</h2>
      <div class="sms-ready__text"><p>Tick off what you already know before you book. This checklist is just for you: nothing is saved or sent.</p>%s</div>
    </div>
    <div class="sms-ready__panel">
      <div class="sms-ready__bar" aria-hidden="true">%s</div>
      <div class="sms-ready__count"><span class="sms-ready__count-n"></span> of 6 ready</div>
      <ul class="sms-ready__list">%s</ul>
      <div class="sms-ready__done">%s<span class="sms-ready__done-text">You have everything we need for a quote.</span></div>
      <div class="sms-ready__todo"><p>Not sure about some of these? That is fine. We are always happy to discuss your event and requirements with you.</p></div>
      <div class="sms-ready__actions">%s</div>
    </div>
  </div>
</section>
""" % (ins, "Booking information" if with_booking else "Event Medical Cover", e(title), extra, segs, items, icon("check", "sms-ready__done-icon"),
       buttons(ctx, [("Book us for your medical cover", "book:event")]))


def inner_extra(ctx, slug):
    if slug == "medical-training":
        return flip(ctx) + explore(ctx)
    if slug == "event-medical-cover":
        return ready(ctx, with_booking=True)
    return ""


# ---------------------------------------------------------------------------
# Homepage
# ---------------------------------------------------------------------------

def home(ctx):
    out = """<section class="sms-contour">
  <div class="sms-contour__inner">
    <div class="sms-contour__copy">
      <div class="sms-kicker">Event medical cover &middot; Training &middot; Consultancy</div>
      <h1 class="sms-contour__title"><span class="sms-contour__line">Protecting People.</span> <span class="sms-contour__line sms-mark">Supporting Business.</span></h1>
      <div class="sms-contour__lead"><p>%s</p></div>
      <div class="sms-contour__actions">%s</div>
      <ul class="sms-pills sms-contour__pills">%s</ul>
    </div>
    <div class="sms-contour__media">%s</div>
  </div>
</section>
""" % (e(C.INTRO), buttons(ctx, [("Book online", "book"), ("Our services", "#services")]),
       "".join('<li class="sms-pills__item"><span class="sms-pill">%s</span></li>' % t for t in ["Clinician-led", "Qualsafe Registered Centre", "Fully insured"]),
       fan(ctx, ["festival", "cpr-room", "assessor"], [("heart", "Event Medical Cover"), None, None]))
    out += panels(ctx)
    out += flip(ctx)
    out += explore(ctx)
    out += ready(ctx)
    out += cta(ctx, {"title": "Have any questions? We’re here to help.",
                     "text": ["We offer an initial discussion to understand your requirements, and our risk and needs consultancy includes a free initial consultation before any chargeable work is agreed."],
                     "buttons": [("Book online", "book"), ("Contact Us", "contact")]})
    ctx.notes.append("Every interactive piece on this concept is HTML and CSS only (radios and checkboxes): no JavaScript")
    return out


def scripts(ctx, main):
    return ""
