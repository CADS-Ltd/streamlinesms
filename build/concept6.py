"""Concept 6 - Pulse. Dark navy with green light: the most brand-led of the dark
concepts, blending J and K. A heartbeat line draws itself across the heroes, a
which-service-do-you-need chooser (works without JavaScript), a swipeable rail of
event types, cards that stack as you scroll, a qualification-validity timeline and
a recruitment pathway that fills in as you scroll."""
from common import *  # noqa: F401,F403
import content as C
import dark

NAME = "Pulse"
DARK = True
FONTS = "https://fonts.googleapis.com/css2?family=Outfit:wght@200;300;400;500;600;700&display=swap"

CHOICES = [
    ("event", "heart", "Medical cover for an event", "event-medical-cover", "Event Medical Cover", "book:event", "Book us for your medical cover",
     "From small local events to large-scale public gatherings, we provide professional, reliable and proportionate medical cover that gives you peace of mind.",
     ["Community events, village fetes and charity events", "Sports and combat-sports events", "Small festivals and outdoor activities"]),
    ("training", "cap", "Training for me or my team", "medical-training", "Medical Training", "book:training", "Book your next training session",
     "Accredited first aid and workplace safety training delivered by real frontline professionals in Swadlincote and beyond.",
     ["Emergency First Aid at Work", "First Aid at Work and requalification", "FREC 3 and FREC 4"]),
    ("consultancy", "clipboard", "Advice on workplace or event safety", "risk-needs-consultancy", "Risk & Needs Consultancy", "book:consultancy", "Request a FREE initial Consultation",
     "We help businesses and event organisers understand their risks, meet their legal obligations, and ensure they have the right plans, people and equipment in place.",
     ["First Aid Needs Assessment", "Risk Assessment Writing", "Event Medical Plans"]),
    ("careers", "compass", "Support with a pre-hospital career", "pre-hospital-career-support", "Pre-Hospital Career Support", "book:careers", "Complete this form to get started",
     "Take your next step in a pre-hospital career with tailored interview preparation, mock assessments and honest, practical feedback.",
     ["Interview preparation", "Mock assessments", "Feedback & development"]),
    ("join", "users", "Working with Streamline", "recruitment", "Recruitment", "contact", "Expression of Interest form",
     "We are looking to hear from experienced professionals who can support our growing services.",
     ["Training roles delivering first aid and clinical courses", "Safety operatives with health & safety experience", "Clinicians for event, medical, and business cover"]),
]


def _choose_css():
    out = ".sms-choose .sms-choose__panel { display: none; }\n"
    for i in range(len(CHOICES)):
        r = ".sms-choose .sms-choose__r%d" % i
        out += "%s:checked ~ * .sms-choose__opt--%d { background: var(--sms-mint); box-shadow: inset 0 0 0 1.5px var(--sms-accent); color: var(--sms-title); }\n" % (r, i)
        out += "%s:checked ~ * .sms-choose__opt--%d .sms-choose__tick { opacity: 1; transform: none; }\n" % (r, i)
        out += "%s:focus-visible ~ * .sms-choose__opt--%d { outline: 3px solid var(--sms-accent); outline-offset: 3px; }\n" % (r, i)
        out += "%s:checked ~ * .sms-choose__panel--%d { display: block; }\n" % (r, i)
    return out


VALID_CSS = dark.seg_css(".sms-valid", "valid", 2)

CSS = r"""
/* ===== Concept 6 theme: pulse ===== */
.sms-page {
  --sms-bg: #04101d;
  --sms-surface: #0a1a2c;
  --sms-pale: #061626;
  --sms-ink: #eaf1f6;
  --sms-ink-soft: #a9bccb;
  --sms-line: rgba(160, 200, 230, 0.15);
  --sms-accent: #86d673;
  --sms-mint: rgba(134, 214, 115, 0.12);
  --sms-line-green: rgba(134, 214, 115, 0.28);
  --sms-glow: rgba(134, 214, 115, 0.4);
  --sms-font: "Outfit", "Montserrat", Arial, sans-serif;
  --sms-radius: 1.5rem;
  --sms-hw: 300;
  --sms-header-bg: rgba(4, 16, 29, 0.78);
  background: radial-gradient(90rem 50rem at 85% -10%, rgba(64, 127, 54, 0.16), transparent 60%), var(--sms-bg);
}
.sms-page .sms-mark { background: linear-gradient(90deg, #86d673, #c6f2b8); -webkit-background-clip: text; background-clip: text; color: transparent; font-weight: inherit; }
.sms-cards .sms-cards__icon,
.sms-links .sms-links__icon,
.sms-quotes .sms-quotes__icon { background: linear-gradient(140deg, rgba(134, 214, 115, 0.25), rgba(134, 214, 115, 0.05)); box-shadow: inset 0 0 0 1px var(--sms-line-green); }

/* Top bar: quiet, on the dark */
.sms-topbar { border-bottom: 1px solid var(--sms-line); background: #020a14; color: var(--sms-ink-soft); }
.sms-topbar .sms-topbar__text { color: var(--sms-ink-soft); font-weight: 400; letter-spacing: 0.06em; }
.sms-topbar .sms-topbar__link { color: var(--sms-ink); font-weight: 400; }
.sms-topbar .sms-topbar__icon { color: var(--sms-accent); }
.sms-header { background: var(--sms-header-bg); }

/* Heartbeat line (draws itself with transforms only) */
.sms-page .sms-ecg { position: relative; overflow: hidden; height: clamp(3.5rem, 2.5rem + 4vw, 6rem); pointer-events: none; }
.sms-page .sms-ecg__wipe { position: absolute; inset: 0; overflow: hidden; animation: sms-ecg-wipe 2.4s var(--sms-ease) 0.3s both; }
.sms-page .sms-ecg__inner { position: absolute; inset: 0; animation: sms-ecg-unwipe 2.4s var(--sms-ease) 0.3s both; }
.sms-page .sms-ecg__svg { display: block; width: 100%; height: 100%; }
.sms-page .sms-ecg__scan { position: absolute; top: 0; bottom: 0; left: 0; width: 18%; background: linear-gradient(90deg, transparent, rgba(134, 214, 115, 0.22), transparent); animation: sms-ecg-scan 6s linear 2.6s infinite; transform: translateX(-100%); }
@keyframes sms-ecg-wipe { from { transform: translateX(-100%); } to { transform: none; } }
@keyframes sms-ecg-unwipe { from { transform: translateX(100%); } to { transform: none; } }
@keyframes sms-ecg-scan { from { transform: translateX(-100%); } to { transform: translateX(560%); } }

/* ---------- Page hero (inner pages): split with a monitor-style photo ---------- */
.sms-phero6 { position: relative; overflow: hidden; padding: clamp(3rem, 2rem + 4vw, 5.5rem) 0 0; }
.sms-phero6 .sms-phero6__inner { display: grid; gap: clamp(2rem, 1.5rem + 3vw, 4rem); align-items: center; width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-phero6 .sms-phero6__copy { min-width: 0; }
.sms-phero6 .sms-phero6__crumb { margin-bottom: 1.5rem; color: var(--sms-ink-soft); font-size: var(--sms-step--1); }
.sms-phero6 .sms-phero6__crumb-link { color: var(--sms-ink); }
.sms-phero6 .sms-phero6__title { margin: 0 0 1.5rem; color: var(--sms-title); font-size: clamp(2.4rem, 1.4rem + 4vw, 4.8rem); font-weight: 300; line-height: 1.04; letter-spacing: -0.035em; }
.sms-phero6 .sms-phero6__sub { margin-bottom: 0.6rem; color: var(--sms-accent); font-weight: 500; }
.sms-phero6 .sms-phero6__lead { max-width: 36rem; color: var(--sms-ink); font-size: var(--sms-step-1); font-weight: 300; line-height: 1.65; }
.sms-phero6 .sms-phero6__lead p { margin: 0 0 0.75rem; }
.sms-phero6 .sms-phero6__actions { display: flex; flex-wrap: wrap; gap: 0.75rem; margin-top: 1.75rem; }
.sms-phero6 .sms-phero6__media { position: relative; min-width: 0; }
.sms-phero6 .sms-phero6__frame { aspect-ratio: 4 / 3.2; border-radius: var(--sms-radius); box-shadow: 0 0 0 1px var(--sms-line-green), 0 30px 80px rgba(0, 0, 0, 0.5), 0 0 60px rgba(64, 127, 54, 0.25); }
.sms-phero6 .sms-phero6__frame .sms-photo__img { animation: sms-zoom 2s var(--sms-ease) both; }
.sms-phero6 .sms-phero6__badges { position: absolute; left: 1rem; right: 1rem; bottom: 1rem; display: flex; flex-wrap: wrap; gap: 0.5rem; }
.sms-phero6 .sms-phero6__badge { display: inline-flex; align-items: center; gap: 0.5rem; min-width: 0; padding: 0.5rem 0.9rem 0.5rem 0.55rem; border-radius: 999px; background: rgba(4, 16, 29, 0.78); box-shadow: inset 0 0 0 1px var(--sms-line); color: var(--sms-title); font-size: var(--sms-step--1); -webkit-backdrop-filter: blur(8px); backdrop-filter: blur(8px); }
.sms-phero6 .sms-phero6__badge-icon { width: 1.6rem; height: 1.6rem; padding: 0.3rem; border-radius: 50%; background: var(--sms-accent); color: var(--sms-on-accent); }
.sms-phero6 .sms-phero6__badge-text { min-width: 0; }
.sms-phero6 .sms-ecg { margin-top: clamp(1.5rem, 1rem + 2vw, 3rem); }
@media (min-width: 60em) {
  .sms-phero6 .sms-phero6__inner { grid-template-columns: minmax(0, 1.1fr) minmax(0, 0.9fr); }
}

/* ---------- CTA band with the heartbeat line ---------- */
.sms-pcta { position: relative; overflow: hidden; padding: var(--sms-section) 0 0; }
.sms-pcta .sms-pcta__inner { position: relative; width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-pcta .sms-pcta__box { display: grid; gap: 1.75rem; align-items: center; padding: clamp(2rem, 1.2rem + 3.5vw, 4rem); border-radius: var(--sms-radius); background: radial-gradient(70% 140% at 100% 0%, rgba(64, 127, 54, 0.4), transparent 60%), linear-gradient(160deg, #0b2036, #071526); box-shadow: inset 0 0 0 1px var(--sms-line-green); }
.sms-pcta .sms-pcta__copy { min-width: 0; }
.sms-pcta .sms-pcta__title { margin: 0 0 0.9rem; color: var(--sms-title); font-size: clamp(2rem, 1.3rem + 2.6vw, 3.4rem); font-weight: 300; line-height: 1.08; letter-spacing: -0.03em; }
.sms-pcta .sms-pcta__text { max-width: 36rem; color: var(--sms-ink-soft); }
.sms-pcta .sms-pcta__text p { margin: 0; }
.sms-pcta .sms-pcta__actions { display: flex; flex-wrap: wrap; gap: 0.75rem; min-width: 0; }
.sms-pcta .sms-pcta__call { display: block; margin-top: 0.75rem; color: var(--sms-ink-soft); font-size: var(--sms-step--1); }
.sms-pcta .sms-pcta__call a { color: var(--sms-title); text-underline-offset: 4px; }
.sms-pcta .sms-pcta__side { min-width: 0; }
@media (min-width: 60em) {
  .sms-pcta .sms-pcta__box { grid-template-columns: minmax(0, 1.5fr) minmax(0, 1fr); }
  .sms-pcta .sms-pcta__side { justify-self: end; text-align: right; }
  .sms-pcta .sms-pcta__actions { justify-content: flex-end; }
}

/* ---------- Home hero ---------- */
.sms-pulse { position: relative; overflow: hidden; padding: clamp(3rem, 2rem + 4vw, 6rem) 0 0; }
.sms-pulse .sms-pulse__inner { display: grid; gap: clamp(2.5rem, 1.5rem + 4vw, 4.5rem); align-items: center; width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-pulse .sms-pulse__copy { min-width: 0; }
.sms-pulse .sms-pulse__title { margin: 0 0 1.5rem; color: var(--sms-title); font-size: clamp(2.6rem, 1.4rem + 4.2vw, 5.1rem); font-weight: 300; line-height: 1; letter-spacing: -0.04em; }
.sms-pulse .sms-pulse__line { display: block; }
.sms-pulse .sms-pulse__lead { max-width: 34rem; color: var(--sms-ink); font-size: var(--sms-step-1); font-weight: 300; line-height: 1.65; }
.sms-pulse .sms-pulse__lead p { margin: 0; }
.sms-pulse .sms-pulse__actions { display: flex; flex-wrap: wrap; gap: 0.75rem; margin-top: 2rem; }
.sms-pulse .sms-pulse__media { position: relative; min-width: 0; padding: 0 0 3rem 0; }
.sms-pulse .sms-pulse__main { aspect-ratio: 4 / 3.3; box-shadow: 0 0 0 1px var(--sms-line-green), 0 30px 80px rgba(0, 0, 0, 0.5), 0 0 70px rgba(64, 127, 54, 0.28); }
.sms-pulse .sms-pulse__small { position: absolute; left: -1rem; bottom: 0; width: 44%; aspect-ratio: 1; border: 5px solid var(--sms-bg); border-radius: 1.25rem; box-shadow: 0 20px 50px rgba(0, 0, 0, 0.5); animation: sms-bob 7s ease-in-out infinite; }
.sms-pulse .sms-pulse__chip { position: absolute; right: -0.5rem; top: 1.5rem; display: inline-flex; align-items: center; gap: 0.6rem; max-width: 70%; padding: 0.6rem 1rem 0.6rem 0.6rem; border-radius: 999px; background: rgba(4, 16, 29, 0.82); box-shadow: inset 0 0 0 1px var(--sms-line-green); color: var(--sms-title); font-size: var(--sms-step--1); -webkit-backdrop-filter: blur(8px); backdrop-filter: blur(8px); animation: sms-float 9s ease-in-out infinite; }
.sms-pulse .sms-pulse__chip-icon { width: 1.9rem; height: 1.9rem; padding: 0.4rem; border-radius: 50%; background: var(--sms-accent); color: var(--sms-on-accent); }
.sms-pulse .sms-pulse__chip-text { min-width: 0; }
.sms-pulse .sms-ecg { margin-top: clamp(2rem, 1.5rem + 2vw, 3.5rem); }
@media (min-width: 60em) {
  .sms-pulse .sms-pulse__inner { grid-template-columns: minmax(0, 1.05fr) minmax(0, 0.95fr); }
}

/* ---------- Which service do you need? (radio cards) ---------- */
.sms-choose { padding: var(--sms-section) 0; }
.sms-choose .sms-choose__inner { width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-choose .sms-choose__head { max-width: 44rem; margin-bottom: clamp(2rem, 1.5rem + 2vw, 3rem); }
.sms-choose .sms-choose__title { margin: 0 0 1rem; color: var(--sms-title); font-size: clamp(2.2rem, 1.3rem + 3.2vw, 4rem); font-weight: 300; line-height: 1.05; letter-spacing: -0.035em; }
.sms-choose .sms-choose__intro { color: var(--sms-ink-soft); }
.sms-choose .sms-choose__intro p { margin: 0; }
.sms-choose .sms-choose__grid { display: grid; gap: 1.5rem; align-items: start; }
.sms-choose .sms-choose__opts { display: grid; gap: 0.6rem; margin: 0; padding: 0; border: 0; min-width: 0; }
.sms-choose .sms-choose__legend { margin-bottom: 0.75rem; padding: 0; color: var(--sms-ink-soft); font-size: 0.75rem; letter-spacing: 0.24em; text-transform: uppercase; }
.sms-choose .sms-choose__opt { position: relative; display: flex; align-items: center; gap: 0.9rem; min-width: 0; padding: 1rem 3rem 1rem 1rem; border-radius: 1.1rem; background: var(--sms-surface); box-shadow: inset 0 0 0 1px var(--sms-line); color: var(--sms-ink); cursor: pointer; font-weight: 400; transition: transform 0.3s var(--sms-ease), background-color 0.3s; }
.sms-choose .sms-choose__opt:hover { transform: translateX(4px); }
.sms-choose .sms-choose__opt-icon { width: 2.6rem; height: 2.6rem; padding: 0.6rem; border-radius: 0.8rem; background: var(--sms-mint); color: var(--sms-accent); }
.sms-choose .sms-choose__opt-text { min-width: 0; }
.sms-choose .sms-choose__tick { position: absolute; right: 1rem; top: 50%; width: 1.5rem; height: 1.5rem; margin-top: -0.75rem; padding: 0.25rem; border-radius: 50%; background: var(--sms-accent); color: var(--sms-on-accent); opacity: 0; transform: scale(0.4); transition: opacity 0.3s, transform 0.3s var(--sms-ease); }
.sms-choose .sms-choose__panel { min-width: 0; padding: clamp(1.5rem, 1rem + 2vw, 2.5rem); border-radius: var(--sms-radius); background: radial-gradient(80% 120% at 100% 0%, rgba(64, 127, 54, 0.22), transparent 60%), var(--sms-surface); box-shadow: inset 0 0 0 1px var(--sms-line-green); animation: sms-fade-up 0.5s var(--sms-ease) both; }
.sms-choose .sms-choose__label { margin-bottom: 0.75rem; color: var(--sms-accent); font-size: var(--sms-step--1); font-weight: 500; letter-spacing: 0.18em; text-transform: uppercase; }
.sms-choose .sms-choose__name { margin: 0 0 0.75rem; color: var(--sms-title); font-size: clamp(1.8rem, 1.4rem + 1.6vw, 2.6rem); font-weight: 300; line-height: 1.1; letter-spacing: -0.02em; }
.sms-choose .sms-choose__text { color: var(--sms-ink-soft); }
.sms-choose .sms-choose__text p { margin: 0 0 1.25rem; }
.sms-choose .sms-choose__actions { display: flex; flex-wrap: wrap; gap: 0.75rem; margin-top: 1.5rem; }
""" + _choose_css() + r"""
@media (min-width: 60em) {
  .sms-choose .sms-choose__grid { grid-template-columns: minmax(0, 0.9fr) minmax(0, 1.1fr); gap: 2.5rem; }
  .sms-choose .sms-choose__panel { position: sticky; top: 8rem; }
}

/* ---------- Event types rail ---------- */
.sms-rail { padding: var(--sms-section) 0; background: var(--sms-pale); }
.sms-rail .sms-rail__inner { width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-rail .sms-rail__head { display: grid; gap: 1.25rem; align-items: end; margin-bottom: clamp(1.75rem, 1.25rem + 2vw, 2.75rem); }
.sms-rail .sms-rail__title { min-width: 0; margin: 0 0 1rem; color: var(--sms-title); font-size: clamp(2.2rem, 1.3rem + 3.2vw, 4rem); font-weight: 300; line-height: 1.05; letter-spacing: -0.035em; }
.sms-rail .sms-rail__intro { max-width: 34rem; min-width: 0; color: var(--sms-ink-soft); }
.sms-rail .sms-rail__intro p { margin: 0; }
.sms-rail .sms-rail__nav { display: flex; gap: 0.5rem; min-width: 0; }
.sms-rail .sms-rail__nav[hidden] { display: none; }
.sms-rail .sms-rail__btn { display: grid; place-items: center; width: 3rem; height: 3rem; border: 0; border-radius: 50%; background: transparent; box-shadow: inset 0 0 0 1px var(--sms-ring-line); color: var(--sms-title); cursor: pointer; transition: transform 0.3s var(--sms-ease), background-color 0.3s; }
.sms-rail .sms-rail__btn:hover { background: var(--sms-accent); color: var(--sms-on-accent); }
.sms-rail .sms-rail__btn-icon { width: 1.2rem; height: 1.2rem; }
.sms-rail .sms-rail__btn--prev .sms-rail__btn-icon { transform: rotate(180deg); }
.sms-rail .sms-rail__track { display: grid; grid-auto-columns: minmax(16rem, 78%); grid-auto-flow: column; gap: 1rem; margin: 0; padding: 0.25rem 0 1.25rem; overflow-x: auto; list-style: none; scroll-snap-type: x mandatory; scrollbar-width: thin; scrollbar-color: rgba(134, 214, 115, 0.5) transparent; }
.sms-rail .sms-rail__card { position: relative; display: flex; flex-direction: column; min-width: 0; min-height: 19rem; overflow: hidden; padding: 1.75rem; border-radius: var(--sms-radius); background: linear-gradient(160deg, #0d2238, #081727); box-shadow: inset 0 0 0 1px var(--sms-line); scroll-snap-align: start; }
.sms-rail .sms-rail__card::before { content: ""; position: absolute; right: -4rem; top: -4rem; width: 14rem; height: 14rem; border-radius: 50%; background: radial-gradient(closest-side, rgba(134, 214, 115, 0.2), transparent); }
.sms-rail .sms-rail__num { position: relative; color: var(--sms-ink-soft); font-size: 0.8125rem; letter-spacing: 0.2em; }
.sms-rail .sms-rail__icon { position: relative; width: 4rem; height: 4rem; margin: 1.5rem 0 auto; padding: 0.9rem; border-radius: 1.2rem; background: var(--sms-mint); box-shadow: inset 0 0 0 1px var(--sms-line-green); color: var(--sms-accent); }
.sms-rail .sms-rail__name { position: relative; margin: 2rem 0 0.4rem; color: var(--sms-title); font-size: var(--sms-step-1); font-weight: 400; }
.sms-rail .sms-rail__text { position: relative; color: var(--sms-ink-soft); font-size: var(--sms-step--1); }
.sms-rail .sms-rail__text p { margin: 0; }
.sms-rail .sms-rail__foot { display: flex; flex-wrap: wrap; align-items: center; gap: 1rem 1.5rem; margin-top: 1rem; color: var(--sms-ink-soft); font-size: var(--sms-step--1); }
@media (min-width: 48em) {
  .sms-rail .sms-rail__track { grid-auto-columns: minmax(16rem, 42%); }
}
@media (min-width: 64em) {
  .sms-rail .sms-rail__head { grid-template-columns: minmax(0, 1fr) auto; }
  .sms-rail .sms-rail__track { grid-auto-columns: minmax(16rem, 30%); }
}

/* ---------- Stacking cards ---------- */
.sms-stack { padding: var(--sms-section) 0; }
.sms-stack .sms-stack__inner { display: grid; gap: clamp(2rem, 1.5rem + 3vw, 4rem); width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-stack .sms-stack__copy { min-width: 0; }
.sms-stack .sms-stack__title { margin: 0 0 1.25rem; color: var(--sms-title); font-size: clamp(2.2rem, 1.3rem + 3.2vw, 4rem); font-weight: 300; line-height: 1.05; letter-spacing: -0.035em; }
.sms-stack .sms-stack__text { max-width: 32rem; color: var(--sms-ink-soft); }
.sms-stack .sms-stack__text p { margin: 0 0 1rem; }
.sms-stack .sms-stack__claim { display: flex; gap: 0.9rem; align-items: center; max-width: 32rem; margin-top: 1.5rem; padding: 1rem 1.25rem; border-radius: 1.1rem; background: var(--sms-mint); box-shadow: inset 0 0 0 1px var(--sms-line-green); color: var(--sms-ink); }
.sms-stack .sms-stack__claim-icon { width: 2.4rem; height: 2.4rem; padding: 0.55rem; border-radius: 50%; background: var(--sms-accent); color: var(--sms-on-accent); }
.sms-stack .sms-stack__claim-text { min-width: 0; }
.sms-stack .sms-stack__list { display: grid; gap: 1.25rem; margin: 0; padding: 0; list-style: none; }
.sms-stack .sms-stack__card { position: sticky; display: grid; gap: 1rem; min-width: 0; padding: clamp(1.5rem, 1rem + 2vw, 2.5rem); border-radius: var(--sms-radius); background: linear-gradient(160deg, #0f2740, #0a1a2c); box-shadow: inset 0 0 0 1px var(--sms-line), 0 -20px 50px rgba(0, 0, 0, 0.35); }
.sms-stack .sms-stack__card:nth-child(1) { top: 7rem; }
.sms-stack .sms-stack__card:nth-child(2) { top: 8.25rem; }
.sms-stack .sms-stack__card:nth-child(3) { top: 9.5rem; }
.sms-stack .sms-stack__card:nth-child(4) { top: 10.75rem; }
.sms-stack .sms-stack__top { display: flex; align-items: center; justify-content: space-between; gap: 1rem; }
.sms-stack .sms-stack__icon { width: 3.25rem; height: 3.25rem; padding: 0.75rem; border-radius: 1rem; background: var(--sms-mint); box-shadow: inset 0 0 0 1px var(--sms-line-green); color: var(--sms-accent); }
.sms-stack .sms-stack__num { color: var(--sms-ink-soft); font-size: 0.8125rem; letter-spacing: 0.2em; }
.sms-stack .sms-stack__name { margin: 0; color: var(--sms-title); font-size: clamp(1.5rem, 1.25rem + 1vw, 2.1rem); font-weight: 300; line-height: 1.15; }
.sms-stack .sms-stack__desc { color: var(--sms-ink-soft); }
.sms-stack .sms-stack__desc p { margin: 0; }
@media (min-width: 60em) {
  .sms-stack .sms-stack__inner { grid-template-columns: minmax(0, 0.9fr) minmax(0, 1.1fr); }
  .sms-stack .sms-stack__copy { position: sticky; top: 8rem; align-self: start; }
  .sms-stack .sms-stack__list { gap: 2.5rem; padding-bottom: 6rem; }
}

/* ---------- Qualification validity timeline ---------- */
.sms-valid { padding: var(--sms-section) 0; background: var(--sms-pale); }
.sms-valid .sms-valid__inner { display: grid; gap: clamp(2.5rem, 1.5rem + 4vw, 5rem); align-items: center; width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-valid .sms-valid__copy { min-width: 0; }
.sms-valid .sms-valid__title { margin: 0 0 1.25rem; color: var(--sms-title); font-size: clamp(2.2rem, 1.3rem + 3.2vw, 4rem); font-weight: 300; line-height: 1.05; letter-spacing: -0.035em; }
.sms-valid .sms-valid__text { max-width: 32rem; color: var(--sms-ink-soft); }
.sms-valid .sms-valid__text p { margin: 0 0 1rem; }
.sms-valid .sms-valid__panel { min-width: 0; padding: clamp(1.25rem, 0.8rem + 2vw, 2.25rem); border-radius: var(--sms-radius); background: var(--sms-surface); box-shadow: inset 0 0 0 1px var(--sms-line), var(--sms-shadow-lg); }
.sms-valid .sms-valid__years { display: grid; gap: 0.9rem; margin: 0; padding: 0; list-style: none; }
.sms-valid .sms-valid__year { display: grid; grid-template-columns: 4.5rem minmax(0, 1fr); gap: 0.75rem; align-items: center; }
.sms-valid .sms-valid__ylabel { color: var(--sms-ink-soft); font-size: var(--sms-step--1); }
.sms-valid .sms-valid__months { display: grid; grid-template-columns: repeat(12, minmax(0, 1fr)); gap: 0.25rem; }
.sms-valid .sms-valid__m { height: 2.2rem; border-radius: 0.45rem; background: rgba(134, 214, 115, 0.28); }
.sms-valid .sms-valid__m--r { position: relative; background: rgba(134, 214, 115, 0.28); }
.sms-valid .sms-valid__m--r::after { content: ""; position: absolute; inset: -0.2rem; border-radius: 0.55rem; background: var(--sms-accent); box-shadow: 0 0 16px var(--sms-glow); opacity: 0; transform: scale(0.6); transition: opacity 0.4s var(--sms-ease), transform 0.4s var(--sms-ease); }
.sms-valid .sms-valid__key { display: flex; flex-wrap: wrap; gap: 0.5rem 1.25rem; margin-top: 1.25rem; color: var(--sms-ink-soft); font-size: var(--sms-step--1); }
.sms-valid .sms-valid__swatch { display: inline-block; width: 0.9rem; height: 0.9rem; margin-right: 0.4rem; border-radius: 0.25rem; background: rgba(134, 214, 115, 0.28); vertical-align: -0.1rem; }
.sms-valid .sms-valid__swatch--r { background: var(--sms-accent); }
.sms-valid .sms-valid__keyr { display: none; }
.sms-valid .sms-valid__out { margin-top: 1.25rem; padding-top: 1.25rem; border-top: 1px solid var(--sms-line); color: var(--sms-ink); }
.sms-valid .sms-valid__out p { margin: 0; }
.sms-valid .sms-valid__out--1 { display: none; }
.sms-valid .sms-valid__r1:checked ~ * .sms-valid__m--r::after { opacity: 1; transform: none; }
.sms-valid .sms-valid__r1:checked ~ * .sms-valid__keyr { display: inline; }
.sms-valid .sms-valid__r1:checked ~ * .sms-valid__out--0 { display: none; }
.sms-valid .sms-valid__r1:checked ~ * .sms-valid__out--1 { display: block; }
""" + VALID_CSS + r"""
@media (min-width: 60em) {
  .sms-valid .sms-valid__inner { grid-template-columns: minmax(0, 0.85fr) minmax(0, 1.15fr); }
}

.sms-choose .sms-choose__panels,
.sms-rail .sms-rail__heading,
.sms-rail .sms-rail__note,
.sms-rail .sms-rail__btn,
.sms-rail .sms-rail__num,
.sms-rail .sms-rail__name,
.sms-rail .sms-rail__text,
.sms-stack .sms-stack__list,
.sms-stack .sms-stack__top,
.sms-stack .sms-stack__num,
.sms-stack .sms-stack__name,
.sms-stack .sms-stack__desc,
.sms-valid .sms-valid__year,
.sms-valid .sms-valid__ylabel,
.sms-valid .sms-valid__months,
.sms-valid .sms-valid__m,
.sms-valid .sms-valid__keyitem,
.sms-valid .sms-valid__keyr,
.sms-path .sms-path__heading,
.sms-path .sms-path__dot { min-width: 0; }

/* ---------- Recruitment pathway that fills as you scroll ---------- */
.sms-path { padding: var(--sms-section) 0; view-timeline-name: --sms-path; }
.sms-path .sms-path__inner { width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-path .sms-path__head { display: grid; gap: 1.25rem; align-items: end; margin-bottom: clamp(2rem, 1.5rem + 2vw, 3.25rem); }
.sms-path .sms-path__title { min-width: 0; margin: 0; color: var(--sms-title); font-size: clamp(2.2rem, 1.3rem + 3.2vw, 4rem); font-weight: 300; line-height: 1.05; letter-spacing: -0.035em; }
.sms-path .sms-path__intro { max-width: 30rem; min-width: 0; color: var(--sms-ink-soft); }
.sms-path .sms-path__intro p { margin: 0 0 1rem; }
.sms-path .sms-path__track { position: relative; }
.sms-path .sms-path__line { position: absolute; left: 1.4rem; top: 1.4rem; bottom: 1.4rem; width: 2px; background: var(--sms-line); }
.sms-path .sms-path__fill { position: absolute; inset: 0; background: linear-gradient(180deg, var(--sms-accent), rgba(134, 214, 115, 0.4)); transform-origin: top; }
.sms-path .sms-path__list { position: relative; display: grid; gap: 1.25rem; margin: 0; padding: 0; list-style: none; }
.sms-path .sms-path__step { display: grid; grid-template-columns: 2.8rem minmax(0, 1fr); gap: 1rem; align-items: center; min-width: 0; }
.sms-path .sms-path__dot { display: grid; place-items: center; width: 2.8rem; height: 2.8rem; border-radius: 50%; background: var(--sms-bg); box-shadow: inset 0 0 0 1.5px var(--sms-accent), 0 0 0 6px var(--sms-bg); color: var(--sms-accent); }
.sms-path .sms-path__dot-icon { width: 1.2rem; height: 1.2rem; }
.sms-path .sms-path__name { min-width: 0; margin: 0; color: var(--sms-title); font-size: var(--sms-step-0); font-weight: 400; line-height: 1.35; }
@media (min-width: 60em) {
  .sms-path .sms-path__head { grid-template-columns: minmax(0, 1.2fr) minmax(0, 0.8fr); }
  .sms-path .sms-path__line { left: 1.4rem; right: 1.4rem; top: 1.4rem; bottom: auto; width: auto; height: 2px; }
  .sms-path .sms-path__fill { transform-origin: left; background: linear-gradient(90deg, var(--sms-accent), rgba(134, 214, 115, 0.4)); }
  .sms-path .sms-path__list { grid-auto-columns: minmax(0, 1fr); grid-auto-flow: column; gap: 1.5rem; }
  .sms-path .sms-path__step { grid-template-columns: minmax(0, 1fr); align-items: start; }
}
@supports (animation-timeline: view()) {
  .sms-path .sms-path__fill { animation: sms-grow-y linear both; animation-timeline: --sms-path; animation-range: entry 50% contain 40%; }
  @media (min-width: 60em) {
    .sms-path .sms-path__fill { animation-name: sms-grow-x; }
  }
}
"""

RISE = [".sms-phero6 .sms-phero6__title", ".sms-pulse .sms-pulse__title"]
ENTRANCE = [".sms-phero6 .sms-phero6__crumb", ".sms-phero6 .sms-kicker", ".sms-pulse .sms-kicker", ".sms-phero6 .sms-phero6__lead", ".sms-pulse .sms-pulse__lead",
            ".sms-phero6 .sms-phero6__actions", ".sms-pulse .sms-pulse__actions", ".sms-phero6 .sms-phero6__media", ".sms-pulse .sms-pulse__media"]
REVEAL = [".sms-choose .sms-choose__head", ".sms-choose .sms-choose__grid", ".sms-rail .sms-rail__head", ".sms-rail .sms-rail__track",
          ".sms-stack .sms-stack__copy", ".sms-valid .sms-valid__copy", ".sms-valid .sms-valid__panel", ".sms-path .sms-path__head", ".sms-path .sms-path__step", ".sms-pcta .sms-pcta__box"]
LOOP = [".sms-page .sms-ecg__wipe", ".sms-page .sms-ecg__inner", ".sms-page .sms-ecg__scan", ".sms-phero6 .sms-phero6__frame .sms-photo__img",
        ".sms-pulse .sms-pulse__small", ".sms-pulse .sms-pulse__chip", ".sms-choose .sms-choose__panel", ".sms-path .sms-path__fill"]
TRANS = [".sms-choose .sms-choose__opt", ".sms-choose .sms-choose__tick", ".sms-rail .sms-rail__btn", ".sms-valid .sms-valid__m--r::after"]


def ecg(cls=""):
    pts = []
    x = 0
    for beat in (170, 560, 950):
        pts += ["%d,70" % (beat - 60), "%d,62" % (beat - 44), "%d,70" % (beat - 30), "%d,70" % (beat - 8), "%d,84" % (beat - 2),
                "%d,10" % (beat + 8), "%d,104" % (beat + 18), "%d,70" % (beat + 26), "%d,70" % (beat + 60), "%d,56" % (beat + 78), "%d,70" % (beat + 96)]
    path = "M0,70 " + " ".join("L" + p for p in pts) + " L1200,70"
    return """<div class="sms-ecg%s" aria-hidden="true">
  <div class="sms-ecg__wipe"><div class="sms-ecg__inner"><svg class="sms-ecg__svg" viewBox="0 0 1200 120" preserveAspectRatio="none" focusable="false" xmlns="http://www.w3.org/2000/svg">
    <path class="sms-ecg__glow" d="%s" fill="none" stroke="rgba(134,214,115,0.25)" stroke-width="6" stroke-linejoin="round" vector-effect="non-scaling-stroke"/>
    <path class="sms-ecg__line" d="%s" fill="none" stroke="#86d673" stroke-width="2" stroke-linejoin="round" vector-effect="non-scaling-stroke"/>
  </svg></div></div>
  <span class="sms-ecg__scan"></span>
</div>""" % ((" " + cls) if cls else "", path, path)


def page_hero(ctx, h, crumb=True):
    crumb_html = '<div class="sms-phero6__crumb"><a class="sms-phero6__crumb-link" href="%s">Home</a> / %s</div>' % (ctx.href("home"), e(LABEL[ctx.slug])) if crumb else ""
    sub = '<div class="sms-phero6__sub">%s</div>' % e(h["sub"]) if h.get("sub") else ""
    acts = '<div class="sms-phero6__actions">%s</div>' % buttons(ctx, h["buttons"]) if h.get("buttons") else ""
    badges = "".join('<span class="sms-phero6__badge">%s<span class="sms-phero6__badge-text">%s</span></span>' % (icon(ic, "sms-phero6__badge-icon"), e(t)) for ic, t in h.get("chips", [])[:2])
    ph = "team" if h["photo"] == "directors" else h["photo"]
    return """<section class="sms-phero6">
  <div class="sms-phero6__inner">
    <div class="sms-phero6__copy">
      %s
      <div class="sms-kicker">%s</div>
      <h1 class="sms-phero6__title">%s</h1>
      <div class="sms-phero6__lead">%s%s</div>
      %s
    </div>
    <div class="sms-phero6__media">%s<div class="sms-phero6__badges">%s</div></div>
  </div>
  %s
</section>
""" % (crumb_html, e(h["eyebrow"]), e(h["title"]), sub, paras(h["body"]), acts, photo(ctx, ph, lazy=False, parallax=False, figcls="sms-phero6__frame"), badges, ecg())


def cta(ctx, d):
    btns = [(l, t) for l, t in d["buttons"] if t != "tel"]
    return """<section class="sms-pcta">
  <div class="sms-pcta__inner">
    <div class="sms-pcta__box">
      <div class="sms-pcta__copy"><h2 class="sms-pcta__title">%s</h2><div class="sms-pcta__text">%s</div></div>
      <div class="sms-pcta__side"><div class="sms-pcta__actions">%s</div><span class="sms-pcta__call">Or call us on <a href="tel:%s">%s</a></span></div>
    </div>
  </div>
  %s
</section>
""" % (e(d["title"]), paras(d["text"]), buttons(ctx, btns) if btns else "", PHONE_TEL, PHONE, ecg())


def chrome_top(ctx):
    return topbar(ctx, C.STRAP) + header(ctx, "white")


def chrome_bottom(ctx):
    return footer(ctx, "white")


# ---------------------------------------------------------------------------
# Reusable sections
# ---------------------------------------------------------------------------

def choose(ctx, title="What would you like [[help with?]]", intro="Choose what you need and we will point you to the right service. At this stage, you do not need to know exactly what service you require."):
    radios = "".join('<input class="sms-seg__radio sms-choose__r%d" type="radio" name="sms-choose" id="sms-choose-%d"%s>' % (i, i, " checked" if i == 0 else "") for i in range(len(CHOICES)))
    opts = "".join('<label class="sms-choose__opt sms-choose__opt--%d" for="sms-choose-%d">%s<span class="sms-choose__opt-text">%s</span>%s</label>' % (
        i, i, icon(c[1], "sms-choose__opt-icon"), e(c[2]), icon("check", "sms-choose__tick")) for i, c in enumerate(CHOICES))
    panels = ""
    for i, (key, ic, q, slug, name, book, book_l, text, items) in enumerate(CHOICES):
        pills = "".join('<li class="sms-pills__item"><span class="sms-pill">%s</span></li>' % e(t) for t in items)
        panels += """<div class="sms-choose__panel sms-choose__panel--%d">
        <div class="sms-choose__label">You need</div>
        <h3 class="sms-choose__name">%s</h3>
        <div class="sms-choose__text"><p>%s</p></div>
        <ul class="sms-pills">%s</ul>
        <div class="sms-choose__actions">%s</div>
      </div>""" % (i, e(name), e(text), pills, buttons(ctx, [(book_l, book), ("Find out more", slug)]))
    return """<section class="sms-choose" id="choose">
  %s
  <div class="sms-choose__inner">
    <div class="sms-choose__head"><div class="sms-kicker">Find the right service</div><h2 class="sms-choose__title">%s</h2><div class="sms-choose__intro"><p>%s</p></div></div>
    <div class="sms-choose__grid">
      <div class="sms-choose__opts">%s</div>
      <div class="sms-choose__panels" aria-live="polite">%s</div>
    </div>
  </div>
</section>
""" % (radios, e(title), e(intro), opts, panels)


def valid(ctx):
    radios, seg_html = dark.seg("valid", ["Qualification", "With annual refreshers"], 0, "Show refresher training")
    years = ""
    for y in range(3):
        months = "".join('<span class="sms-valid__m%s"></span>' % (" sms-valid__m--r" if m == 11 else "") for m in range(12))
        years += '<li class="sms-valid__year"><span class="sms-valid__ylabel">Year %d</span><span class="sms-valid__months" aria-hidden="true">%s</span></li>' % (y + 1, months)
    return """<section class="sms-valid" id="valid">
  %s
  <div class="sms-valid__inner">
    <div class="sms-valid__copy">
      <div class="sms-kicker">Qualifications</div>
      <h2 class="sms-valid__title">How long are qualifications <span class="sms-mark">valid?</span></h2>
      <div class="sms-valid__text"><p>Many workplace and pre-hospital qualifications are valid for three years. Some practical skills should be refreshed more regularly, and annual refresher training may be recommended.</p></div>
      %s
    </div>
    <div class="sms-valid__panel">
      %s
      <ol class="sms-valid__years">%s</ol>
      <div class="sms-valid__key" aria-hidden="true"><span class="sms-valid__keyitem"><span class="sms-valid__swatch"></span>Qualification valid</span><span class="sms-valid__keyr"><span class="sms-valid__swatch sms-valid__swatch--r"></span>Refresher training</span></div>
      <div class="sms-valid__out sms-valid__out--0"><p>Many workplace and pre-hospital qualifications are valid for three years.</p></div>
      <div class="sms-valid__out sms-valid__out--1"><p>Some practical skills should be refreshed more regularly, and annual refresher training may be recommended.</p></div>
      <p class="sms-caption">Illustration. Check the validity of your own qualification.</p>
    </div>
  </div>
</section>
""" % (radios, buttons(ctx, [("Book your next training session", "book:training")]), seg_html, years)


SKIP = {"contact": [1]}


def inner_extra(ctx, slug):
    if slug == "contact":
        return choose(ctx, title="Need a specific [[service?]]")
    if slug == "medical-training":
        return valid(ctx)
    return ""


# ---------------------------------------------------------------------------
# Homepage
# ---------------------------------------------------------------------------
EVENT_TYPES = [
    ("music", "Festivals & Concerts", "Professional cover for music events of any size."),
    ("tent", "Community Events", "Local fairs, fetes, carnivals and charity events."),
    ("briefcase", "Corporate Events", "Conferences, exhibitions and business events of all kinds."),
    ("trophy", "Sporting Events", "From grassroots to elite level competitions."),
    ("users", "Public Gatherings", "Fireworks, parades and large public attendances."),
]


def home(ctx):
    ctx.notes += ["Image-only copy used: event types and their one-line descriptions (Event Medical Cover page images)",
                  "Image-only copy used: \"Working With You, Not Simply For You.\" and the paragraphs beneath it (why-choose-us.png)",
                  "Image-only copy used: \"Mathew and Tom bring over 15 years of ambulance experience...\" (why-choose-us.png - use approved)"]
    out = """<section class="sms-pulse">
  <div class="sms-pulse__inner">
    <div class="sms-pulse__copy">
      <div class="sms-kicker">%s</div>
      <h1 class="sms-pulse__title"><span class="sms-pulse__line">Clinician-Led.</span> <span class="sms-pulse__line sms-mark">Practical.</span> <span class="sms-pulse__line">Professional.</span></h1>
      <div class="sms-pulse__lead"><p>%s</p></div>
      <div class="sms-pulse__actions">%s</div>
    </div>
    <div class="sms-pulse__media">
      %s
      %s
      <div class="sms-pulse__chip">%s<span class="sms-pulse__chip-text">Qualsafe Registered Centre</span></div>
    </div>
  </div>
  %s
</section>
""" % (e(C.STRAP), e(C.INTRO), buttons(ctx, [("Book online", "book"), ("Find the right service", "#choose")]),
       photo(ctx, "team", lazy=False, parallax=False, figcls="sms-pulse__main"), photo(ctx, "cpr-outdoor", parallax=False, figcls="sms-pulse__small"),
       icon("award", "sms-pulse__chip-icon"), ecg())

    out += choose(ctx)

    cards = "".join('<li class="sms-rail__card"><span class="sms-rail__num">%02d</span>%s<h3 class="sms-rail__name">%s</h3><div class="sms-rail__text"><p>%s</p></div></li>' % (
        i + 1, icon(ic, "sms-rail__icon"), e(t), e(d)) for i, (ic, t, d) in enumerate(EVENT_TYPES))
    out += """<section class="sms-rail" id="events" data-sms-rail>
  <div class="sms-rail__inner">
    <div class="sms-rail__head">
      <div class="sms-rail__heading"><div class="sms-kicker">What type of medical support do we offer?</div><h2 class="sms-rail__title">Medical Support Built Around <span class="sms-mark">Your Event</span></h2>
      <div class="sms-rail__intro"><p>%s</p></div></div>
      <div class="sms-rail__nav" hidden>
        <button class="sms-rail__btn sms-rail__btn--prev" type="button" data-sms-rail-step="-1" aria-label="Previous event types">%s</button>
        <button class="sms-rail__btn" type="button" data-sms-rail-step="1" aria-label="Next event types">%s</button>
      </div>
    </div>
    <ul class="sms-rail__track" tabindex="0" aria-label="Event types">%s</ul>
    <div class="sms-rail__foot"><span class="sms-rail__note">Every event is reviewed before we confirm cover.</span><a class="sms-arrowlink" href="%s">Event Medical Cover&nbsp;<span class="sms-arrow" aria-hidden="true">&rarr;</span></a></div>
  </div>
</section>
""" % (e("We deliver high-quality medical support across a wide range of events and environments, from community gatherings and sporting events to concerts, public events and planned workplace operations."),
       icon("arrow", "sms-rail__btn-icon"), icon("arrow", "sms-rail__btn-icon"), cards, ctx.href("event-medical-cover"))

    stack = "".join('<li class="sms-stack__card"><div class="sms-stack__top">%s<span class="sms-stack__num">%02d / 04</span></div><h3 class="sms-stack__name">%s</h3><div class="sms-stack__desc"><p>%s</p></div></li>' % (
        icon(ic, "sms-stack__icon"), i + 1, e(t), e(d)) for i, (ic, t, d) in enumerate(C.TRUST))
    out += """<section class="sms-stack" id="why">
  <div class="sms-stack__inner">
    <div class="sms-stack__copy">
      <div class="sms-kicker">Why choose Streamline</div>
      <h2 class="sms-stack__title">%s</h2>
      <div class="sms-stack__text"><p>%s</p></div>
      %s
      <div class="sms-stack__claim">%s<span class="sms-stack__claim-text">%s</span></div>
    </div>
    <ol class="sms-stack__list">%s</ol>
  </div>
</section>
""" % (e(C.WORKING_WITH["title"]), e(C.WORKING_WITH["body"][0]), more(paras(C.WORKING_WITH["body"][1:])), icon("heart", "sms-stack__claim-icon"), e(C.CLAIM_15), stack)

    out += valid(ctx)

    rec = C.PAGES["recruitment"]["sections"][2][1]
    steps = "".join('<li class="sms-path__step"><span class="sms-path__dot">%s</span><h3 class="sms-path__name">%s</h3></li>' % (icon(it["icon"], "sms-path__dot-icon"), e(it["title"])) for it in rec["items"])
    out += """<section class="sms-path" id="join">
  <div class="sms-path__inner">
    <div class="sms-path__head">
      <div class="sms-path__heading"><div class="sms-kicker">Our recruitment pathway</div><h2 class="sms-path__title">Interested in <span class="sms-mark">Working With Us?</span></h2></div>
      <div class="sms-path__intro"><p>%s</p>%s</div>
    </div>
    <div class="sms-path__track">
      <div class="sms-path__line" aria-hidden="true"><span class="sms-path__fill"></span></div>
      <ol class="sms-path__list">%s</ol>
    </div>
  </div>
</section>
""" % (e(rec["lead"][0]), buttons(ctx, [("Expression of Interest form", "contact")]), steps)

    picks = ["Where is Streamline based?", "Who runs Streamline?", "Can Streamline provide more than one service?", "Do you offer a free initial discussion?", "Are you insured?", "How can I contact Streamline?"]
    allf = dict(C.faqs("home"))
    out += SHARED_RENDERERS["faq"](ctx, {"tone": "pale", "eyebrow": C.STRAP, "title": "General Streamline [[FAQs]]",
                                        "lead": ["Answers to common questions about Streamline Safety & Medical Solutions, our team, services, bookings and how we work."],
                                        "items": [(q, allf[q]) for q in picks], "show": 6})
    out += cta(ctx, {"title": "Have any questions? We’re here to help.",
                     "text": ["We offer an initial discussion to understand your requirements, and our risk and needs consultancy includes a free initial consultation before any chargeable work is agreed."],
                     "buttons": [("Book online", "book"), ("Contact Us", "contact")]})
    return out


JS = """<script>
(function () {
  /* Event-type rail: previous / next buttons (the rail scrolls natively without them) */
  Array.prototype.forEach.call(document.querySelectorAll('[data-sms-rail]'), function (rail) {
    var track = rail.querySelector('.sms-rail__track');
    var nav = rail.querySelector('.sms-rail__nav');
    if (!track || !nav) { return; }
    nav.hidden = false;
    var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    Array.prototype.forEach.call(nav.querySelectorAll('[data-sms-rail-step]'), function (btn) {
      btn.addEventListener('click', function () {
        var card = track.querySelector('.sms-rail__card');
        var step = card ? card.getBoundingClientRect().width + 16 : 300;
        track.scrollBy({ left: step * Number(btn.getAttribute('data-sms-rail-step')), behavior: reduce ? 'auto' : 'smooth' });
      });
    });
  });
})();
</script>
"""


def scripts(ctx, main):
    return JS if "data-sms-rail" in main else ""
