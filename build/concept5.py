"""Concept 5 - Graphite. Dark, refined and closest to Pristine Motors concept K:
near-black graphite, Urbanist in light weights with an italic green accent, a
floating glass header, a big centred headline over a photo comparison that sweeps
itself, service tiles that tilt towards the pointer, a course-length picker and
tabbed Skilled / Proportionate / Reliable diagrams."""
from common import *  # noqa: F401,F403
import content as C
import dark

NAME = "Graphite"
DARK = True
FONTS = "https://fonts.googleapis.com/css2?family=Urbanist:ital,wght@0,200;0,300;0,400;0,500;0,600;0,700;1,200;1,300;1,400&display=swap"

COURSES = [
    ("Emergency First Aid at Work", "Emergency First Aid at Work", 1, "Usually one day", ""),
    ("First Aid at Work", "First Aid at Work", 3, "Usually three days", ""),
    ("Requalification", "First Aid at Work requalification", 2, "Usually two days", ""),
    ("Paediatric", "Paediatric First Aid", 2, "Usually two days", ""),
    ("FREC 3", "FREC 3", 5, "Usually five classroom-based training days", "With assessments."),
    ("FREC 4", "FREC 4", 5, "Usually five classroom-based training days", "Alongside completion of a portfolio and workbooks."),
]


def _course_css():
    out = dark.seg_css(".sms-course", "course", len(COURSES), "sms-course__out")
    for i, c in enumerate(COURSES):
        out += ".sms-course .sms-course__r%d:checked ~ * .sms-course__day:nth-child(-n+%d) { opacity: 1; transform: none; }\n" % (i, c[2])
        out += ".sms-course .sms-course__r%d:checked ~ * .sms-course__day:nth-child(-n+%d) .sms-course__dot { background: var(--sms-accent); box-shadow: 0 0 14px var(--sms-glow); }\n" % (i, c[2])
    return out


CSS = r"""
/* ===== Concept 5 theme: graphite ===== */
.sms-page {
  --sms-bg: #0a0c0f;
  --sms-surface: #14181d;
  --sms-pale: #101317;
  --sms-ink: #edf0f3;
  --sms-ink-soft: #b0b8c1;
  --sms-line: rgba(220, 228, 236, 0.13);
  --sms-accent: #8fd67c;
  --sms-mint: rgba(143, 214, 124, 0.1);
  --sms-line-green: rgba(143, 214, 124, 0.24);
  --sms-glow: rgba(143, 214, 124, 0.32);
  --sms-field: #0e1114;
  --sms-font: "Urbanist", "Montserrat", Arial, sans-serif;
  --sms-radius: 1.75rem;
  --sms-radius-sm: 1rem;
  --sms-hw: 200;
  --sms-header-bg: rgba(20, 24, 29, 0.76);
  --sms-hair: rgba(255, 255, 255, 0.04);
  font-size: clamp(1.03rem, 0.98rem + 0.22vw, 1.1rem);
}
.sms-page .sms-mark { color: var(--sms-accent); font-style: italic; font-weight: inherit; }
.sms-page .sms-btn { font-weight: 500; }
.sms-page .sms-btn--primary { border-color: #f2f5f7; background: #f2f5f7; color: #0a0c0f; }
.sms-page .sms-btn--primary:hover { box-shadow: 0 12px 40px rgba(242, 245, 247, 0.18); }
.sms-page .sms-kicker { color: var(--sms-ink-soft); letter-spacing: 0.32em; }
.sms-page .sms-kicker::before { display: none; }
.sms-cards .sms-cards__name,
.sms-steps .sms-steps__name,
.sms-people .sms-people__name,
.sms-links .sms-links__name { font-weight: 400; }
.sms-cards .sms-cards__icon,
.sms-links .sms-links__icon { border-radius: 50%; }

/* Floating glass header */
.sms-header { padding-top: 0.75rem; border-bottom: 0; background: transparent; -webkit-backdrop-filter: none; backdrop-filter: none; }
.sms-header .sms-header__inner { width: calc(100% - 2 * var(--sms-gutter)); min-height: 4rem; padding: 0.4rem 0.45rem 0.4rem 1.25rem; border-radius: 999px; background: var(--sms-header-bg); box-shadow: inset 0 0 0 1px var(--sms-line), 0 18px 50px rgba(0, 0, 0, 0.35); -webkit-backdrop-filter: blur(14px); backdrop-filter: blur(14px); }
.sms-header .sms-header__logo-img { width: clamp(9.5rem, 8rem + 5vw, 12rem); }
.sms-header .sms-header__summary { background: transparent; box-shadow: none; }
.sms-header .sms-header__link::after { display: none; }
.sms-header .sms-header__link[aria-current="page"] { color: var(--sms-title); text-decoration: underline; text-decoration-color: var(--sms-accent); text-underline-offset: 0.5em; }
.sms-header .sms-header__cta { padding: 0.8rem 1.25rem; }

/* ---------- Page hero (inner pages): centred, then a wide photo ---------- */
.sms-ghero { position: relative; z-index: 0; overflow: hidden; margin-top: -5rem; padding: clamp(8rem, 6.5rem + 5vw, 10.5rem) 0 clamp(3rem, 2rem + 3vw, 4.5rem); text-align: center; }
.sms-ghero::before { content: ""; position: absolute; z-index: -1; left: 50%; top: -18rem; width: 70rem; height: 40rem; margin-left: -35rem; border-radius: 50%; background: radial-gradient(closest-side, rgba(120, 140, 160, 0.18), transparent); pointer-events: none; }
.sms-ghero .sms-ghero__inner { width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-ghero .sms-ghero__crumb { margin-bottom: 1.75rem; color: var(--sms-ink-soft); font-size: var(--sms-step--1); }
.sms-ghero .sms-ghero__crumb-link { color: var(--sms-ink); }
.sms-ghero .sms-kicker { justify-content: center; }
.sms-ghero .sms-ghero__title { max-width: 14em; margin: 0 auto 1.5rem; color: var(--sms-title); font-size: clamp(2.6rem, 1.3rem + 5.4vw, 6rem); font-weight: 200; line-height: 1.02; letter-spacing: -0.04em; }
.sms-ghero .sms-ghero__sub { margin-bottom: 0.6rem; color: var(--sms-accent); font-weight: 500; }
.sms-ghero .sms-ghero__lead { max-width: 40rem; margin: 0 auto; color: var(--sms-ink); font-size: var(--sms-step-1); font-weight: 300; line-height: 1.65; }
.sms-ghero .sms-ghero__lead p { margin: 0 0 0.75rem; }
.sms-ghero .sms-ghero__actions { display: flex; flex-wrap: wrap; justify-content: center; gap: 0.75rem; margin-top: 2rem; }
.sms-ghero .sms-ghero__pills { justify-content: center; margin-top: 1.5rem; }
.sms-ghero .sms-ghero__media { width: 100%; max-width: 72rem; margin: clamp(2.5rem, 2rem + 2vw, 4rem) auto 0; padding: 0 var(--sms-gutter); }
.sms-ghero .sms-ghero__frame { aspect-ratio: 16 / 8; box-shadow: inset 0 0 0 1px var(--sms-line), var(--sms-shadow-lg); }
.sms-ghero .sms-ghero__frame .sms-photo__img { animation: sms-zoom 2.2s var(--sms-ease) both; }

/* ---------- CTA ---------- */
.sms-gcta { padding: var(--sms-section) 0; }
.sms-gcta .sms-gcta__inner { width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-gcta .sms-gcta__box { display: grid; gap: 2rem; align-items: center; padding: clamp(2rem, 1.2rem + 3.5vw, 4.5rem); border-radius: var(--sms-radius); background: radial-gradient(55% 140% at 25% 120%, rgba(110, 130, 150, 0.3), transparent 70%), #13171c; box-shadow: inset 0 0 0 1px var(--sms-line); }
.sms-gcta .sms-gcta__copy { min-width: 0; }
.sms-gcta .sms-gcta__title { margin: 0 0 1rem; color: var(--sms-title); font-size: clamp(2.1rem, 1.3rem + 3vw, 3.8rem); font-weight: 200; line-height: 1.06; letter-spacing: -0.035em; }
.sms-gcta .sms-gcta__text { max-width: 36rem; color: var(--sms-ink-soft); }
.sms-gcta .sms-gcta__text p { margin: 0; }
.sms-gcta .sms-gcta__side { display: grid; gap: 1rem; justify-items: start; min-width: 0; }
.sms-gcta .sms-gcta__actions { display: flex; flex-wrap: wrap; gap: 0.75rem; min-width: 0; }
.sms-gcta .sms-gcta__call { min-width: 0; color: var(--sms-ink-soft); font-size: var(--sms-step--1); }
.sms-gcta .sms-gcta__call a { color: var(--sms-title); text-underline-offset: 4px; }
@media (min-width: 60em) {
  .sms-gcta .sms-gcta__box { grid-template-columns: minmax(0, 1.5fr) minmax(0, 1fr); }
  .sms-gcta .sms-gcta__side { justify-items: end; text-align: right; }
}

/* ---------- Home: centred hero and photo sweep ---------- */
.sms-ghome { position: relative; z-index: 0; overflow: hidden; margin-top: -5rem; padding: clamp(9rem, 7rem + 6vw, 12rem) 0 clamp(3rem, 2rem + 3vw, 4.5rem); text-align: center; }
.sms-ghome::before { content: ""; position: absolute; z-index: -1; left: 50%; top: -20rem; width: 80rem; height: 46rem; margin-left: -40rem; border-radius: 50%; background: radial-gradient(closest-side, rgba(120, 140, 160, 0.2), transparent); pointer-events: none; }
.sms-ghome .sms-ghome__inner { width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-ghome .sms-kicker { justify-content: center; }
.sms-ghome .sms-ghome__title { max-width: 13em; margin: 0 auto 1.75rem; color: var(--sms-title); font-size: clamp(2.8rem, 1.2rem + 6.6vw, 7.2rem); font-weight: 200; line-height: 1; letter-spacing: -0.045em; }
.sms-ghome .sms-ghome__lead { max-width: 38rem; margin: 0 auto; color: var(--sms-ink); font-size: var(--sms-step-1); font-weight: 300; line-height: 1.65; }
.sms-ghome .sms-ghome__lead p { margin: 0; }
.sms-ghome .sms-ghome__actions { display: flex; flex-wrap: wrap; justify-content: center; gap: 0.75rem; margin-top: 2rem; }

.sms-sweep { width: 100%; max-width: 72rem; margin: clamp(2.5rem, 2rem + 2.5vw, 4.5rem) auto 0; padding: 0 var(--sms-gutter); }
.sms-sweep .sms-sweep__view { --pos: 50%; position: relative; overflow: hidden; aspect-ratio: 16 / 8.5; border-radius: var(--sms-radius); background: var(--sms-surface); box-shadow: inset 0 0 0 1px var(--sms-line), var(--sms-shadow-lg); touch-action: pan-y; }
.sms-sweep .sms-sweep__img { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; }
.sms-sweep .sms-sweep__clip { position: absolute; inset: 0; overflow: hidden; transform: translateX(calc(var(--pos) - 100%)); }
.sms-sweep .sms-sweep__top { position: absolute; inset: 0; transform: translateX(calc(100% - var(--pos))); }
.sms-sweep .sms-sweep__handle { position: absolute; inset: 0; transform: translateX(calc(var(--pos) - 50%)); pointer-events: none; }
.sms-sweep .sms-sweep__line { position: absolute; left: 50%; top: 0; bottom: 0; width: 2px; margin-left: -1px; background: rgba(255, 255, 255, 0.85); }
.sms-sweep .sms-sweep__knob { position: absolute; left: 50%; top: 50%; display: grid; place-items: center; width: 3rem; height: 3rem; margin: -1.5rem 0 0 -1.5rem; border-radius: 50%; background: rgba(10, 12, 15, 0.7); box-shadow: inset 0 0 0 1px rgba(255, 255, 255, 0.6); color: #ffffff; -webkit-backdrop-filter: blur(6px); backdrop-filter: blur(6px); }
.sms-sweep .sms-sweep__knob-icon { width: 1.2rem; height: 1.2rem; }
.sms-sweep .sms-sweep__tag { position: absolute; top: 1.1rem; z-index: 2; padding: 0.35rem 0.85rem; border-radius: 999px; background: rgba(10, 12, 15, 0.7); color: #ffffff; font-size: 0.75rem; font-weight: 500; letter-spacing: 0.24em; text-transform: uppercase; }
.sms-sweep .sms-sweep__tag--a { left: 1.1rem; }
.sms-sweep .sms-sweep__tag--b { right: 1.1rem; }
.sms-sweep .sms-sweep__range { position: absolute; inset: 0; z-index: 3; width: 100%; height: 100%; margin: 0; opacity: 0; cursor: ew-resize; }
.sms-sweep .sms-sweep__range[hidden] { display: none; }
.sms-sweep .sms-sweep__range:focus-visible ~ .sms-sweep__handle .sms-sweep__knob { outline: 3px solid var(--sms-accent); outline-offset: 3px; }
.sms-sweep .sms-sweep__pills { justify-content: center; margin-top: 1.5rem; }
.sms-sweep .sms-caption { text-align: center; }

/* ---------- Home: tilting service tiles ---------- */
.sms-tiles { padding: var(--sms-section) 0; }
.sms-tiles .sms-tiles__inner { width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-tiles .sms-tiles__head { display: grid; gap: 1.25rem; align-items: end; margin-bottom: clamp(2rem, 1.5rem + 2vw, 3.25rem); }
.sms-tiles .sms-tiles__title { min-width: 0; margin: 0; color: var(--sms-title); font-size: clamp(2.3rem, 1.3rem + 3.6vw, 4.4rem); font-weight: 200; line-height: 1.04; letter-spacing: -0.04em; }
.sms-tiles .sms-tiles__intro { max-width: 26rem; min-width: 0; color: var(--sms-ink-soft); }
.sms-tiles .sms-tiles__intro p { margin: 0; }
.sms-tiles .sms-tiles__grid { display: grid; gap: 1rem; margin: 0; padding: 0; list-style: none; perspective: 1000px; }
.sms-tiles .sms-tiles__item { min-width: 0; }
.sms-tiles .sms-tiles__link { --rx: 0deg; --ry: 0deg; position: relative; display: flex; flex-direction: column; justify-content: space-between; gap: 2.5rem; height: 100%; min-height: 15rem; overflow: hidden; padding: 1.75rem; border-radius: var(--sms-radius); background: var(--sms-surface); box-shadow: inset 0 0 0 1px var(--sms-line); color: var(--sms-ink); text-decoration: none; transform: rotateX(var(--rx)) rotateY(var(--ry)); transition: transform 0.6s var(--sms-ease); }
.sms-tiles .sms-tiles__link.is-tilting { transition: transform 0.12s linear; }
.sms-tiles .sms-tiles__glare { position: absolute; z-index: 1; left: 0; top: 0; width: 28rem; height: 28rem; margin: -14rem 0 0 -14rem; border-radius: 50%; background: radial-gradient(closest-side, rgba(255, 255, 255, 0.12), transparent); opacity: 0; transform: translate(var(--gx, 50%), var(--gy, 50%)); transition: opacity 0.4s; pointer-events: none; }
.sms-tiles .sms-tiles__link.is-tilting .sms-tiles__glare { opacity: 1; }
.sms-tiles .sms-tiles__bg { position: absolute; z-index: 0; inset: 0; width: 100%; height: 100%; object-fit: cover; opacity: 0.5; transition: transform 1.2s var(--sms-ease); }
.sms-tiles .sms-tiles__link:hover .sms-tiles__bg { transform: scale(1.04); }
.sms-tiles .sms-tiles__shade { position: absolute; z-index: 0; inset: 0; background: linear-gradient(0deg, rgba(10, 12, 15, 0.92) 10%, rgba(10, 12, 15, 0.35) 70%); }
.sms-tiles .sms-tiles__top,
.sms-tiles .sms-tiles__bottom { position: relative; z-index: 2; min-width: 0; }
.sms-tiles .sms-tiles__top { display: flex; align-items: flex-start; justify-content: space-between; gap: 1rem; }
.sms-tiles .sms-tiles__label { min-width: 0; color: var(--sms-ink-soft); font-size: var(--sms-step--1); }
.sms-tiles .sms-tiles__icon { width: 2.6rem; height: 2.6rem; padding: 0.6rem; border-radius: 50%; background: var(--sms-mint); color: var(--sms-accent); }
.sms-tiles .sms-tiles__name { margin: 0 0 0.4rem; color: var(--sms-title); font-size: clamp(1.5rem, 1.25rem + 1vw, 2.1rem); font-weight: 300; line-height: 1.1; letter-spacing: -0.02em; }
.sms-tiles .sms-tiles__text { color: var(--sms-ink-soft); font-size: var(--sms-step--1); }
.sms-tiles .sms-tiles__text p { margin: 0; }
.sms-tiles .sms-tiles__item--big .sms-tiles__link { min-height: 22rem; }
.sms-tiles .sms-tiles__item--big .sms-tiles__name { font-size: clamp(2rem, 1.4rem + 2vw, 3rem); }
.sms-tiles .sms-tiles__item--big .sms-tiles__text { max-width: 28rem; color: var(--sms-ink); font-size: var(--sms-step-0); }
@media (min-width: 48em) {
  .sms-tiles .sms-tiles__grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
  .sms-tiles .sms-tiles__item--big { grid-column: 1 / -1; }
}
@media (min-width: 64em) {
  .sms-tiles .sms-tiles__head { grid-template-columns: minmax(0, 1.3fr) minmax(0, 0.7fr); }
  .sms-tiles .sms-tiles__intro { justify-self: end; }
  .sms-tiles .sms-tiles__grid { grid-template-columns: minmax(0, 1.25fr) repeat(2, minmax(0, 1fr)); grid-auto-rows: minmax(14rem, auto); }
  .sms-tiles .sms-tiles__item--big { grid-column: auto; grid-row: span 2; }
  .sms-tiles .sms-tiles__item--big .sms-tiles__link { min-height: 100%; }
}

.sms-tiles .sms-tiles__heading { min-width: 0; }

/* ---------- Course length picker ---------- */
.sms-course { padding: var(--sms-section) 0; background: var(--sms-pale); }
.sms-course .sms-course__inner { display: grid; gap: clamp(2.5rem, 1.5rem + 4vw, 5rem); align-items: center; width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-course .sms-course__copy { min-width: 0; }
.sms-course .sms-course__title { margin: 0 0 1.5rem; color: var(--sms-title); font-size: clamp(2.2rem, 1.3rem + 3.2vw, 4rem); font-weight: 200; line-height: 1.05; letter-spacing: -0.04em; }
.sms-course .sms-course__text { max-width: 30rem; color: var(--sms-ink-soft); }
.sms-course .sms-course__text p { margin: 0 0 1rem; }
.sms-course .sms-course__actions { display: flex; flex-wrap: wrap; gap: 0.75rem; margin-top: 1.75rem; }
.sms-course .sms-course__panel { min-width: 0; padding: clamp(1.25rem, 0.8rem + 2vw, 2.25rem); border-radius: var(--sms-radius); background: var(--sms-surface); box-shadow: inset 0 0 0 1px var(--sms-line), var(--sms-shadow-lg); }
.sms-course .sms-seg { border-radius: 1.4rem; }
.sms-course .sms-course__label { margin: 1.25rem 0 0.9rem; color: var(--sms-ink-soft); font-size: 0.75rem; letter-spacing: 0.24em; text-transform: uppercase; }
.sms-course .sms-course__days { display: grid; grid-template-columns: repeat(5, minmax(0, 1fr)); gap: 0.5rem; margin: 0; padding: 0; list-style: none; }
.sms-course .sms-course__day { display: grid; justify-items: center; gap: 0.6rem; min-width: 0; padding: 1rem 0.25rem 0.85rem; border-radius: 1rem; background: var(--sms-hair); box-shadow: inset 0 0 0 1px var(--sms-line); color: var(--sms-ink-soft); font-size: 0.8125rem; opacity: 0.45; transform: scale(0.94); transition: opacity 0.45s var(--sms-ease), transform 0.45s var(--sms-ease); }
.sms-course .sms-course__dot { min-width: 0; width: 0.85rem; height: 0.85rem; border-radius: 50%; background: rgba(255, 255, 255, 0.18); }
.sms-course .sms-course__out { margin-top: 1.5rem; padding-top: 1.25rem; border-top: 1px solid var(--sms-line); animation: sms-fade-up 0.5s var(--sms-ease) both; }
.sms-course .sms-course__big { color: var(--sms-title); font-size: clamp(2.6rem, 2rem + 2.2vw, 3.6rem); font-weight: 200; line-height: 1; letter-spacing: -0.03em; }
.sms-course .sms-course__unit { color: var(--sms-ink-soft); font-size: 0.4em; font-weight: 300; letter-spacing: 0; }
.sms-course .sms-course__name { margin: 0.6rem 0 0.2rem; color: var(--sms-title); font-weight: 500; }
.sms-course .sms-course__meta { color: var(--sms-accent); }
.sms-course .sms-course__note { margin-top: 1.25rem; color: var(--sms-ink-soft); font-size: var(--sms-step--1); }
.sms-course .sms-course__note p { margin: 0; }
""" + _course_css() + r"""
@media (min-width: 60em) {
  .sms-course .sms-course__inner { grid-template-columns: minmax(0, 0.85fr) minmax(0, 1.15fr); }
}

/* ---------- Skilled / Proportionate / Reliable diagrams ---------- */
.sms-spr { padding: var(--sms-section) 0; }
.sms-spr .sms-spr__inner { display: grid; gap: clamp(2.5rem, 1.5rem + 4vw, 5rem); align-items: start; width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-spr .sms-spr__copy { min-width: 0; }
.sms-spr .sms-spr__title { margin: 0 0 1.5rem; color: var(--sms-title); font-size: clamp(2.2rem, 1.3rem + 3.2vw, 4rem); font-weight: 200; line-height: 1.05; letter-spacing: -0.04em; }
.sms-spr .sms-spr__rows { margin: 1.5rem 0 0; padding: 0; border-top: 1px solid var(--sms-line); list-style: none; }
.sms-spr .sms-spr__row { padding: 1.1rem 0; border-bottom: 1px solid var(--sms-line); }
.sms-spr .sms-spr__name { margin: 0 0 0.3rem; color: var(--sms-title); font-size: var(--sms-step-1); font-weight: 400; }
.sms-spr .sms-spr__text { color: var(--sms-ink-soft); }
.sms-spr .sms-spr__text p { margin: 0; }
.sms-spr .sms-spr__visual { min-width: 0; }
.sms-spr .sms-spr__card { padding: clamp(1rem, 0.6rem + 1.5vw, 1.75rem); border-radius: var(--sms-radius); background: linear-gradient(180deg, #161a20, #101317); box-shadow: inset 0 0 0 1px var(--sms-line), var(--sms-shadow-lg); }
.sms-spr .sms-spr__svg { display: block; width: 100%; height: auto; }
.sms-spr .sms-spr__cap { margin: 1rem 0 0; color: var(--sms-ink); font-size: var(--sms-step--1); }
.sms-spr .sms-spr__p0,
.sms-spr .sms-spr__p1,
.sms-spr .sms-spr__p2 { animation: sms-fade-up 0.5s var(--sms-ease) both; }
""" + dark.seg_css(".sms-spr", "spr", 3, "sms-spr__p") + r"""
@media (min-width: 60em) {
  .sms-spr .sms-spr__inner { grid-template-columns: minmax(0, 0.85fr) minmax(0, 1.15fr); }
  .sms-spr .sms-spr__visual { position: sticky; top: 7rem; }
}

/* ---------- How it works: timeline that fills as you scroll ---------- */
.sms-how { padding: var(--sms-section) 0; background: var(--sms-pale); }
.sms-how .sms-how__inner { display: grid; gap: clamp(2.5rem, 1.5rem + 4vw, 5rem); width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-how .sms-how__copy { min-width: 0; }
.sms-how .sms-how__title { margin: 0 0 1.5rem; color: var(--sms-title); font-size: clamp(2.2rem, 1.3rem + 3.2vw, 4rem); font-weight: 200; line-height: 1.05; letter-spacing: -0.04em; }
.sms-how .sms-how__text { max-width: 30rem; color: var(--sms-ink-soft); }
.sms-how .sms-how__text p { margin: 0 0 1.25rem; }
.sms-how .sms-how__track { position: relative; min-width: 0; }
.sms-how .sms-how__line { position: absolute; left: 0.55rem; top: 0.7rem; bottom: 0.7rem; width: 1px; background: var(--sms-line); }
.sms-how .sms-how__fill { position: absolute; inset: 0; background: var(--sms-accent); transform-origin: top; }
.sms-how .sms-how__list { position: relative; margin: 0; padding: 0; list-style: none; }
.sms-how .sms-how__step { position: relative; padding: 0 0 2.25rem 3rem; }
.sms-how .sms-how__step:last-child { padding-bottom: 0; }
.sms-how .sms-how__ring { position: absolute; left: 0; top: 0.3rem; width: 1.15rem; height: 1.15rem; border-radius: 50%; background: var(--sms-pale); box-shadow: inset 0 0 0 2px var(--sms-accent); }
.sms-how .sms-how__name { margin: 0 0 0.35rem; color: var(--sms-title); font-size: clamp(1.35rem, 1.15rem + 0.8vw, 1.8rem); font-weight: 300; line-height: 1.2; letter-spacing: -0.015em; }
.sms-how .sms-how__desc { color: var(--sms-ink-soft); }
.sms-how .sms-how__desc p { margin: 0; }
@media (min-width: 60em) {
  .sms-how .sms-how__inner { grid-template-columns: minmax(0, 0.9fr) minmax(0, 1.1fr); }
  .sms-how .sms-how__copy { position: sticky; top: 7rem; align-self: start; }
}
@supports (animation-timeline: view()) {
  .sms-how .sms-how__fill { animation: sms-grow-y linear both; animation-timeline: view(); animation-range: entry 30% cover 60%; }
}
"""

RISE = [".sms-ghero .sms-ghero__title", ".sms-ghome .sms-ghome__title"]
ENTRANCE = [".sms-ghero .sms-ghero__crumb", ".sms-ghero .sms-kicker", ".sms-ghome .sms-kicker", ".sms-ghero .sms-ghero__lead", ".sms-ghome .sms-ghome__lead",
            ".sms-ghero .sms-ghero__actions", ".sms-ghome .sms-ghome__actions", ".sms-ghero .sms-ghero__media", ".sms-sweep .sms-sweep__view"]
REVEAL = [".sms-tiles .sms-tiles__head", ".sms-tiles .sms-tiles__item", ".sms-course .sms-course__copy", ".sms-course .sms-course__panel",
          ".sms-spr .sms-spr__copy", ".sms-spr .sms-spr__card", ".sms-how .sms-how__copy", ".sms-how .sms-how__step", ".sms-gcta .sms-gcta__box"]
LOOP = [".sms-ghero .sms-ghero__frame .sms-photo__img", ".sms-how .sms-how__fill", ".sms-course .sms-course__out",
        ".sms-spr .sms-spr__p0", ".sms-spr .sms-spr__p1", ".sms-spr .sms-spr__p2"]
TRANS = [".sms-tiles .sms-tiles__link", ".sms-tiles .sms-tiles__glare", ".sms-tiles .sms-tiles__bg", ".sms-course .sms-course__day"]

SKIP = {"event-medical-cover": [1]}


def page_hero(ctx, h, crumb=True):
    crumb_html = '<div class="sms-ghero__crumb"><a class="sms-ghero__crumb-link" href="%s">Home</a> / %s</div>' % (ctx.href("home"), e(LABEL[ctx.slug])) if crumb else ""
    sub = '<div class="sms-ghero__sub">%s</div>' % e(h["sub"]) if h.get("sub") else ""
    acts = '<div class="sms-ghero__actions">%s</div>' % buttons(ctx, h["buttons"]) if h.get("buttons") else ""
    pills = "".join('<li class="sms-pills__item"><span class="sms-pill">%s</span></li>' % e(t) for _, t in h.get("chips", []))
    return """<section class="sms-ghero">
  <div class="sms-ghero__inner">
    %s
    <div class="sms-kicker">%s</div>
    <h1 class="sms-ghero__title">%s</h1>
    <div class="sms-ghero__lead">%s%s</div>
    %s
    <ul class="sms-pills sms-ghero__pills">%s</ul>
  </div>
  <div class="sms-ghero__media">%s</div>
</section>
""" % (crumb_html, e(h["eyebrow"]), e(h["title"]), sub, paras(h["body"]), acts, pills, photo(ctx, "team" if h["photo"] == "directors" else h["photo"], lazy=False, parallax=False, figcls="sms-ghero__frame"))


def cta(ctx, d):
    btns = [(l, t) for l, t in d["buttons"] if t != "tel"]
    return """<section class="sms-gcta">
  <div class="sms-gcta__inner">
    <div class="sms-gcta__box">
      <div class="sms-gcta__copy"><h2 class="sms-gcta__title">%s</h2><div class="sms-gcta__text">%s</div></div>
      <div class="sms-gcta__side">
        <div class="sms-gcta__actions">%s</div>
        <div class="sms-gcta__call">Or call us on <a href="tel:%s">%s</a></div>
      </div>
    </div>
  </div>
</section>
""" % (e(d["title"]), paras(d["text"]), buttons(ctx, btns) if btns else "", PHONE_TEL, PHONE)


def chrome_top(ctx):
    return header(ctx, "white")


def chrome_bottom(ctx):
    return footer(ctx, "white")


# ---------------------------------------------------------------------------
# Course length picker (real durations from the Medical Training FAQ)
# ---------------------------------------------------------------------------

def course(ctx):
    radios, seg_html = dark.seg("course", [c[0] for c in COURSES], 1, "Choose a course")
    days = "".join('<li class="sms-course__day"><span class="sms-course__dot" aria-hidden="true"></span>Day %d</li>' % (i + 1) for i in range(5))
    outs = ""
    for i, (short, name, n, meta, extra) in enumerate(COURSES):
        outs += '<div class="sms-course__out sms-course__out%d"><div class="sms-course__big">%d<span class="sms-course__unit"> %s</span></div><div class="sms-course__name">%s</div><div class="sms-course__meta">%s%s</div></div>' % (
            i, n, "day" if n == 1 else "days", e(name), e(meta), (". " + e(extra)) if extra else "")
    return """<section class="sms-course" id="courses">
  %s
  <div class="sms-course__inner">
    <div class="sms-course__copy">
      <div class="sms-kicker">Medical Training</div>
      <h2 class="sms-course__title">How long do the courses <span class="sms-mark">take?</span></h2>
      <div class="sms-course__text"><p>Choose a course to see how many training days it usually takes. Availability may vary, so please contact us for current dates and options.</p></div>
      <div class="sms-course__actions">%s</div>
    </div>
    <div class="sms-course__panel">
      %s
      <div class="sms-course__label" aria-hidden="true">Training days</div>
      <ol class="sms-course__days" aria-hidden="true">%s</ol>
      %s
      <div class="sms-course__note"><p>Streamline Safety &amp; Medical Solutions is a Qualsafe Registered Centre &ndash; Centre No. 908578. Many workplace and pre-hospital qualifications are valid for three years.</p></div>
    </div>
  </div>
</section>
""" % (radios, buttons(ctx, [("Book your next training session", "book:training"), ("View our training catalogue of courses", C.CATALOGUE)]), seg_html, days, outs)


# ---------------------------------------------------------------------------
# Skilled / Proportionate / Reliable diagrams
# ---------------------------------------------------------------------------

def _t(x, y, text, size=13, anchor="middle", fill="#edf0f3", weight=400):
    return '<text x="%s" y="%s" text-anchor="%s" font-size="%d" font-weight="%d" fill="%s">%s</text>' % (x, y, anchor, size, weight, fill, text)


def svg_skilled():
    bars = [("First", "responders", 70), ("FREC 3", "medics", 115), ("Ambulance", "clinicians", 160), ("Registered", "clinicians", 205)]
    out = ""
    for i, (a, b, h) in enumerate(bars):
        x = 40 + i * 125
        hi = i == 1
        out += '<rect x="%d" y="%d" width="100" height="%d" rx="12" fill="%s" stroke="%s" stroke-width="1.5"/>' % (
            x, 250 - h, h, "rgba(143,214,124,0.22)" if hi else "rgba(255,255,255,0.05)", "#8fd67c" if hi else "rgba(220,228,236,0.25)")
        out += _t(x + 50, 274, a) + _t(x + 50, 291, b, fill="#b0b8c1")
    out += '<path d="M140 120V60" stroke="#8fd67c" stroke-width="1.5" stroke-dasharray="4 5"/>'
    out += '<circle cx="140" cy="56" r="4" fill="#8fd67c"/>' + _t(150, 40, "The minimum for many events we support", 13, "start", "#8fd67c", 500)
    out += '<path d="M40 250H515" stroke="rgba(220,228,236,0.25)"/>'
    return '<svg class="sms-spr__svg" viewBox="0 0 560 300" role="img" aria-label="Four levels of skill, from first responders through FREC 3 medics and ambulance clinicians to registered clinicians. FREC 3 is marked as the minimum for many events." xmlns="http://www.w3.org/2000/svg">%s</svg>' % out


def svg_proportionate():
    import math
    factors = ["Size", "Audience", "Location", "Activities", "Risks", "Access to emergency services"]
    out = '<circle cx="280" cy="150" r="118" fill="none" stroke="rgba(220,228,236,0.14)" stroke-dasharray="2 7"/>'
    for i, f in enumerate(factors):
        a = math.radians(-90 + i * 60)
        x, y = 280 + 118 * math.cos(a), 150 + 118 * math.sin(a)
        out += '<path d="M280 150L%.1f %.1f" stroke="rgba(143,214,124,0.35)" stroke-dasharray="3 5"/>' % (x, y)
        out += '<circle cx="%.1f" cy="%.1f" r="7" fill="#8fd67c"/>' % (x, y)
        anchor = "middle" if abs(math.cos(a)) < 0.2 else ("start" if math.cos(a) > 0 else "end")
        dx = 0 if anchor == "middle" else (14 if anchor == "start" else -14)
        dy = -16 if y < 100 else (28 if y > 200 else 5)
        if f.startswith("Access"):
            out += _t("%.1f" % (x + dx), "%.1f" % (y + dy), "Access to", 13, anchor) + _t("%.1f" % (x + dx), "%.1f" % (y + dy + 16), "emergency services", 13, anchor)
        else:
            out += _t("%.1f" % (x + dx), "%.1f" % (y + dy), f, 13, anchor)
    out += '<circle cx="280" cy="150" r="46" fill="rgba(143,214,124,0.14)" stroke="#8fd67c" stroke-width="1.5"/>' + _t(280, 147, "Your", 14, weight=500) + _t(280, 164, "event", 14, weight=500)
    return '<svg class="sms-spr__svg" viewBox="0 0 560 300" role="img" aria-label="Your event in the centre, assessed on six factors: size, audience, location, activities, risks and access to emergency services." xmlns="http://www.w3.org/2000/svg">%s</svg>' % out


def svg_reliable():
    steps = ["First enquiry", "Clear quotation", "Booking confirmed", "Arrives prepared", "Post-event reporting"]
    out = '<path d="M50 150H510" stroke="rgba(220,228,236,0.25)" stroke-width="1.5"/><path d="M50 150H510" stroke="#8fd67c" stroke-width="2" stroke-dasharray="1 9" stroke-linecap="round"/>'
    for i, s in enumerate(steps):
        x = 50 + i * 115
        out += '<circle cx="%d" cy="150" r="11" fill="#14181d" stroke="#8fd67c" stroke-width="2"/><circle cx="%d" cy="150" r="4" fill="#8fd67c"/>' % (x, x)
        words = s.split(" ")
        y0 = 104 if i % 2 == 0 else 190
        out += _t(x, y0, words[0]) + _t(x, y0 + 17, " ".join(words[1:]), fill="#b0b8c1")
    return '<svg class="sms-spr__svg" viewBox="0 0 560 300" role="img" aria-label="A line from first enquiry, through a clear quotation, booking confirmed and arriving prepared, to post-event reporting." xmlns="http://www.w3.org/2000/svg">%s</svg>' % out


SPR_CAPS = [
    "From first responders through to registered clinicians, we ensure the right level of skill is matched to the needs of your event.",
    "Every event is assessed based on its size, audience, location, activities, risks and access to emergency services.",
    "Clear planning, professional communication and dependable delivery from the first enquiry through to post-event reporting.",
]


def spr(ctx, heading_level="h2"):
    radios, seg_html = dark.seg("spr", ["Skilled", "Proportionate", "Reliable"], 0, "Choose a diagram")
    items = C.PAGES["event-medical-cover"]["sections"][1][1]["items"]
    rows = ""
    for it in items:
        first, rest = split_first(it["text"])
        rows += '<li class="sms-spr__row"><h3 class="sms-spr__name">%s</h3><div class="sms-spr__text"><p>%s</p></div>%s</li>' % (e(it["title"]), e(first), more("<p>%s</p>" % e(rest)) if rest else "")
    panels = "".join('<div class="sms-spr__p%d">%s<p class="sms-spr__cap">%s</p></div>' % (i, svg, e(cap)) for i, (svg, cap) in enumerate(zip([svg_skilled(), svg_proportionate(), svg_reliable()], SPR_CAPS)))
    return """<section class="sms-spr" id="process">
  %s
  <div class="sms-spr__inner">
    <div class="sms-spr__copy">
      <div class="sms-kicker">Our Process</div>
      <%s class="sms-spr__title">Skilled. Proportionate. <span class="sms-mark">Reliable.</span></%s>
      <ul class="sms-spr__rows">%s</ul>
    </div>
    <div class="sms-spr__visual">
      %s
      <div class="sms-spr__card">%s<p class="sms-caption">Illustration, not to scale.</p></div>
    </div>
  </div>
</section>
""" % (radios, heading_level, heading_level, rows, seg_html, panels)


def inner_extra(ctx, slug):
    if slug == "event-medical-cover":
        return spr(ctx)
    if slug == "medical-training":
        return course(ctx)
    return ""


# ---------------------------------------------------------------------------
# Homepage
# ---------------------------------------------------------------------------
TILES = [
    ("event-medical-cover", "Event Medical Cover", "heart", "Skilled. Proportionate. Reliable.", C.SERVICES[0]["text"], "fete", True),
    ("medical-training", "Medical Training", "cap", "Qualsafe Registered Centre", "Clinician-led first aid and pre-hospital training.", None, False),
    ("risk-needs-consultancy", "Risk & Needs Consultancy", "clipboard", "Free initial consultation", "Assess the risk. Plan the response. Protect your people.", None, False),
    ("pre-hospital-career-support", "Pre-Hospital Career Support", "compass", "Interview preparation and mock assessments", "Practical Support. Confident Career Steps.", None, False),
    ("recruitment", "Recruitment", "users", "Trainers, safety operatives and clinicians", "Interested in Working With Us?", None, False),
]


def home(ctx):
    ctx.notes += ["Hero headline \"Protecting People. Preparing Organisations.\" is the live homepage heading",
                  "Photo comparison caption uses the live Medical Training line \"Learn · Practise · Apply\""]
    out = """<section class="sms-ghome">
  <div class="sms-ghome__inner">
    <div class="sms-kicker">Event medical cover &middot; Training &middot; Consultancy</div>
    <h1 class="sms-ghome__title">Protecting People. <span class="sms-mark">Preparing Organisations.</span></h1>
    <div class="sms-ghome__lead"><p>%s</p></div>
    <div class="sms-ghome__actions">%s</div>
  </div>
  <div class="sms-sweep" data-sms-sweep>
    <div class="sms-sweep__view">
      %s
      <div class="sms-sweep__clip"><div class="sms-sweep__top">%s</div></div>
      <span class="sms-sweep__tag sms-sweep__tag--a">Event</span>
      <span class="sms-sweep__tag sms-sweep__tag--b">Training</span>
      <input class="sms-sweep__range" type="range" min="0" max="100" value="50" aria-label="Compare the event with the training room" hidden>
      <div class="sms-sweep__handle" aria-hidden="true"><span class="sms-sweep__line"></span><span class="sms-sweep__knob">%s</span></div>
    </div>
    <p class="sms-caption">Learn &middot; Practise &middot; Apply. Drag across to move between the event and the training room.</p>
    <ul class="sms-pills sms-sweep__pills">%s</ul>
  </div>
</section>
""" % (e(C.INTRO2), buttons(ctx, [("Book online", "book"), ("Our services", "#services")]),
       photo_img(ctx, "session", "sms-sweep__img", lazy=False), photo_img(ctx, "festival", "sms-sweep__img", lazy=False),
       '<svg class="sms-icon sms-sweep__knob-icon" viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M9 6l-6 6 6 6M15 6l6 6-6 6"/></svg>',
       "".join('<li class="sms-pills__item"><span class="sms-pill">%s</span></li>' % t for t in ["Clinician-led", "Qualsafe Registered Centre", "Fully insured", "Free initial consultation"]))

    tiles = ""
    for slug, title, ic, label, text, ph, big in TILES:
        bg = (photo_img(ctx, ph, "sms-tiles__bg", decorative=True) + '<span class="sms-tiles__shade" aria-hidden="true"></span>') if ph else ""
        tiles += """<li class="sms-tiles__item%s"><a class="sms-tiles__link" href="%s" data-sms-tilt>%s<span class="sms-tiles__glare" aria-hidden="true"></span>
          <span class="sms-tiles__top"><span class="sms-tiles__label">%s</span>%s</span>
          <span class="sms-tiles__bottom"><span class="sms-tiles__name">%s</span><span class="sms-tiles__text"><p>%s</p></span></span>
        </a></li>""" % (" sms-tiles__item--big" if big else "", ctx.href(slug), bg, e(label), icon(ic, "sms-tiles__icon"), e(title), e(text))
    out += """<section class="sms-tiles" id="services">
  <div class="sms-tiles__inner">
    <div class="sms-tiles__head">
      <div class="sms-tiles__heading"><div class="sms-kicker">Our Services</div><h2 class="sms-tiles__title">What We <span class="sms-mark">Provide</span></h2></div>
      <div class="sms-tiles__intro"><p>%s</p></div>
    </div>
    <ul class="sms-tiles__grid">%s</ul>
  </div>
</section>
""" % (e(C.INTRO), tiles)

    out += course(ctx)
    out += spr(ctx)

    steps = C.PAGES["risk-needs-consultancy"]["sections"][2][1]["items"]
    lst = "".join('<li class="sms-how__step"><span class="sms-how__ring" aria-hidden="true"></span><h3 class="sms-how__name">%s</h3><div class="sms-how__desc"><p>%s</p></div></li>' % (
        e(s["title"]), e(split_first(s["text"])[0])) for s in steps)
    out += """<section class="sms-how" id="consultation">
  <div class="sms-how__inner">
    <div class="sms-how__copy">
      <div class="sms-kicker">Free initial consultation</div>
      <h2 class="sms-how__title">How your free initial <span class="sms-mark">consultation</span> works</h2>
      <div class="sms-how__text"><p>%s</p></div>
      %s
    </div>
    <div class="sms-how__track">
      <div class="sms-how__line" aria-hidden="true"><span class="sms-how__fill"></span></div>
      <ol class="sms-how__list">%s</ol>
    </div>
  </div>
</section>
""" % (e("This is a no-obligation conversation where we take the time to learn about your current arrangements, any concerns you may have, and what you are hoping to achieve."),
       buttons(ctx, [("Request a FREE initial Consultation", "book:consultancy")]), lst)

    out += cta(ctx, {"title": "Have any questions? We’re here to help.",
                     "text": ["Speak to our team about the right solution for your organisation, or book online in a few steps."],
                     "buttons": [("Book online", "book"), ("Contact Us", "contact")]})
    ctx.notes.append("Image-only copy used: \"Speak to our team about the right solution for your organisation.\" (footer-homepage.png)")
    return out


JS = """<script>
(function () {
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var fine = window.matchMedia('(hover: hover) and (pointer: fine)').matches;

  /* Photo comparison: drag, keys or a one-off sweep when it first comes into view */
  Array.prototype.forEach.call(document.querySelectorAll('[data-sms-sweep]'), function (box) {
    var view = box.querySelector('.sms-sweep__view');
    var input = box.querySelector('.sms-sweep__range');
    var touched = false;
    var set = function (v) { view.style.setProperty('--pos', v + '%'); };
    input.hidden = false;
    input.addEventListener('input', function () { touched = true; set(input.value); });
    set(input.value);
    if (reduce || !('IntersectionObserver' in window)) { return; }
    set(92); input.value = 92;
    var io = new IntersectionObserver(function (en) {
      if (!en[0].isIntersecting) { return; }
      io.disconnect();
      var t0 = null;
      window.setTimeout(function () {
        (function step(ts) {
          if (touched) { return; }
          if (t0 === null) { t0 = ts; }
          var p = Math.min(1, (ts - t0) / 2200);
          var k = p < 0.5 ? 4 * p * p * p : 1 - Math.pow(-2 * p + 2, 3) / 2;
          var v = 92 - 42 * k;
          input.value = Math.round(v); set(v.toFixed(2));
          if (p < 1) { window.requestAnimationFrame(step); }
        })(performance.now());
      }, 600);
    }, { threshold: 0.4 });
    io.observe(box);
  });

  /* Tiles lean towards the pointer and catch the light */
  if (fine && !reduce) {
    Array.prototype.forEach.call(document.querySelectorAll('[data-sms-tilt]'), function (card) {
      card.addEventListener('pointermove', function (ev) {
        var r = card.getBoundingClientRect();
        var px = (ev.clientX - r.left) / r.width, py = (ev.clientY - r.top) / r.height;
        card.classList.add('is-tilting');
        card.style.setProperty('--ry', ((px - 0.5) * 7).toFixed(2) + 'deg');
        card.style.setProperty('--rx', ((0.5 - py) * 7).toFixed(2) + 'deg');
        card.style.setProperty('--gx', (ev.clientX - r.left).toFixed(0) + 'px');
        card.style.setProperty('--gy', (ev.clientY - r.top).toFixed(0) + 'px');
      });
      card.addEventListener('pointerleave', function () {
        card.classList.remove('is-tilting');
        card.style.setProperty('--rx', '0deg'); card.style.setProperty('--ry', '0deg');
      });
    });
  }
})();
</script>
"""


def scripts(ctx, main):
    return JS if ("data-sms-sweep" in main or "data-sms-tilt" in main) else ""
