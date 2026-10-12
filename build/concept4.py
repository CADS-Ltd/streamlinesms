"""Concept 4 - Night shift. Dark, cinematic and closest to Pristine Motors concept J:
midnight navy, Montserrat in light weights with one bold phrase, an inspection-light
hero, a strip of real facts, a before/assessed site diagram, a scroll story with a
pinned photo and a scroll-linked Assess / Plan / Protect ring."""
from common import *  # noqa: F401,F403
import content as C
import dark

NAME = "Night shift"
DARK = True
FONTS = "https://fonts.googleapis.com/css2?family=Montserrat:wght@200;300;400;500;600;700&display=swap"

SCENE_SEG = dark.seg_css(".sms-scene", "scene", 2)

CSS = r"""
/* ===== Concept 4 theme: night shift ===== */
.sms-page { --sms-radius: 1.6rem; --sms-radius-sm: 0.9rem; }
.sms-page .sms-mark { color: #ffffff; font-weight: var(--sms-sw); }

/* ---------- Page hero (inner pages): photo under a midnight shade ---------- */
.sms-nhero { position: relative; z-index: 0; overflow: hidden; margin-top: -4.8rem; padding: clamp(8rem, 6rem + 6vw, 11rem) 0 clamp(4rem, 3rem + 4vw, 6.5rem); }
.sms-nhero .sms-nhero__media { position: absolute; z-index: -3; inset: 0; }
.sms-nhero .sms-nhero__frame { width: 100%; height: 100%; border-radius: 0; background: var(--sms-bg); }
.sms-nhero .sms-nhero__frame .sms-photo__img { animation: sms-zoom 2.4s var(--sms-ease) both; }
.sms-nhero .sms-nhero__shade { position: absolute; z-index: -2; inset: 0; background: linear-gradient(90deg, rgba(5, 12, 22, 0.96) 0%, rgba(5, 12, 22, 0.86) 45%, rgba(5, 12, 22, 0.62) 100%), linear-gradient(0deg, var(--sms-bg) 0%, rgba(5, 12, 22, 0) 40%); }
.sms-nhero .sms-nhero__glow { position: absolute; z-index: -1; right: -10%; top: 10%; width: 46rem; max-width: 90vw; aspect-ratio: 1; border-radius: 50%; background: radial-gradient(circle, rgba(130, 208, 110, 0.16), transparent 62%); animation: sms-float 14s ease-in-out infinite; pointer-events: none; }
.sms-nhero .sms-nhero__inner { position: relative; width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-nhero .sms-nhero__crumb { margin-bottom: 1.75rem; color: var(--sms-ink-soft); font-size: var(--sms-step--1); }
.sms-nhero .sms-nhero__crumb-link { color: var(--sms-ink); }
.sms-nhero .sms-nhero__title { max-width: 16em; margin: 0 0 1.5rem; color: #ffffff; font-size: clamp(2.5rem, 1.4rem + 4.6vw, 5.4rem); font-weight: 200; line-height: 1.04; letter-spacing: -0.035em; }
.sms-nhero .sms-nhero__sub { margin-bottom: 0.75rem; color: var(--sms-accent); font-weight: 500; }
.sms-nhero .sms-nhero__lead { max-width: 38rem; color: var(--sms-ink); font-size: var(--sms-step-1); line-height: 1.65; }
.sms-nhero .sms-nhero__lead p { margin: 0 0 0.75rem; }
.sms-nhero .sms-nhero__row { display: flex; flex-wrap: wrap; align-items: center; gap: 1rem 1.25rem; margin-top: 2rem; }
.sms-nhero .sms-nhero__card { display: grid; gap: 0.5rem; min-width: 0; padding: 1rem 1.4rem; border-radius: var(--sms-radius-sm); background: rgba(12, 25, 41, 0.7); box-shadow: inset 0 0 0 1px var(--sms-line); -webkit-backdrop-filter: blur(10px); backdrop-filter: blur(10px); }
.sms-nhero .sms-nhero__fact { display: flex; align-items: center; gap: 0.6rem; min-width: 0; font-size: var(--sms-step--1); }
.sms-nhero .sms-nhero__fact-icon { width: 1.1rem; height: 1.1rem; color: var(--sms-accent); }
.sms-nhero .sms-nhero__fact-text { min-width: 0; }
.sms-nhero .sms-nhero__actions { display: flex; flex-wrap: wrap; gap: 0.75rem; min-width: 0; }

/* ---------- CTA (glowing panel) ---------- */
.sms-ncta { padding: var(--sms-section) 0; }
.sms-ncta .sms-ncta__inner { width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-ncta .sms-ncta__box { position: relative; display: grid; gap: 2rem; align-items: center; overflow: hidden; padding: clamp(2rem, 1.2rem + 3.5vw, 4.5rem); border-radius: var(--sms-radius); background: radial-gradient(60% 120% at 20% 110%, rgba(64, 127, 54, 0.45), transparent 70%), linear-gradient(180deg, #0d1c2e, #091522); box-shadow: inset 0 0 0 1px var(--sms-line); }
.sms-ncta .sms-ncta__copy { min-width: 0; }
.sms-ncta .sms-ncta__title { margin: 0 0 1rem; color: #ffffff; font-size: clamp(2rem, 1.3rem + 2.8vw, 3.5rem); font-weight: 200; line-height: 1.08; letter-spacing: -0.03em; }
.sms-ncta .sms-ncta__text { max-width: 36rem; color: var(--sms-ink-soft); }
.sms-ncta .sms-ncta__text p { margin: 0; }
.sms-ncta .sms-ncta__side { display: grid; gap: 1rem; justify-items: start; min-width: 0; }
.sms-ncta .sms-ncta__actions { display: flex; flex-wrap: wrap; gap: 0.75rem; min-width: 0; }
.sms-ncta .sms-ncta__call { min-width: 0; color: var(--sms-ink-soft); font-size: var(--sms-step--1); }
.sms-ncta .sms-ncta__call a { color: #ffffff; text-underline-offset: 4px; }
@media (min-width: 60em) {
  .sms-ncta .sms-ncta__box { grid-template-columns: minmax(0, 1.5fr) minmax(0, 1fr); }
  .sms-ncta .sms-ncta__side { justify-items: end; text-align: right; }
}

/* ---------- Home: inspection-light hero ---------- */
.sms-torch { position: relative; z-index: 0; overflow: hidden; margin-top: -4.8rem; padding: clamp(9rem, 7rem + 8vw, 13rem) 0 clamp(3rem, 2rem + 3vw, 4.5rem); }
.sms-torch .sms-torch__base { position: absolute; z-index: -1; inset: 0; overflow: hidden; }
.sms-torch .sms-torch__img { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; }
.sms-torch .sms-torch__shade { position: absolute; inset: 0; background: rgba(5, 12, 22, 0.84); transition: opacity 0.9s var(--sms-ease); }
.sms-torch .sms-torch__fade { position: absolute; inset: 0; background: linear-gradient(0deg, var(--sms-bg) 8%, rgba(5, 12, 22, 0.35) 60%, rgba(5, 12, 22, 0.6) 100%); }
.sms-torch .sms-torch__lens { position: absolute; left: 0; top: 0; display: none; width: 30rem; height: 30rem; margin: -15rem 0 0 -15rem; overflow: hidden; -webkit-mask-image: radial-gradient(circle closest-side, #000 45%, transparent 100%); mask-image: radial-gradient(circle closest-side, #000 45%, transparent 100%); transform: translate3d(var(--x, 60vw), var(--y, 16rem), 0); transition: opacity 0.9s var(--sms-ease); pointer-events: none; }
.sms-torch.is-live .sms-torch__lens { display: block; }
.sms-torch .sms-torch__lens-inner { position: absolute; left: 0; top: 0; width: var(--bw, 100vw); height: var(--bh, 40rem); transform: translate3d(calc(15rem - var(--x, 60vw)), calc(15rem - var(--y, 16rem)), 0); }
.sms-torch .sms-torch__lens-img { display: block; width: 100%; height: 100%; object-fit: cover; filter: brightness(0.82); }
.sms-torch .sms-torch__spot { position: absolute; right: 8%; top: 18%; width: 30rem; max-width: 80vw; aspect-ratio: 1; border-radius: 50%; background: radial-gradient(circle, rgba(130, 208, 110, 0.14), transparent 62%); pointer-events: none; }
.sms-torch.is-live .sms-torch__spot { display: none; }
.sms-torch.is-lit .sms-torch__shade { opacity: 0.55; }
.sms-torch.is-lit .sms-torch__lens { opacity: 0; }
.sms-torch .sms-torch__hint { position: absolute; right: var(--sms-gutter); top: 7.5rem; display: none; color: var(--sms-ink-soft); font-size: 0.75rem; letter-spacing: 0.24em; text-transform: uppercase; }
.sms-torch .sms-torch__inner { position: relative; text-shadow: 0 1px 24px rgba(4, 10, 18, 0.7); width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-torch .sms-torch__title { margin: 0 0 2rem; color: #ffffff; font-size: clamp(2.6rem, 1.1rem + 6.4vw, 6.6rem); font-weight: 200; line-height: 1.02; letter-spacing: -0.04em; }
.sms-torch .sms-torch__line { display: block; }
.sms-torch .sms-torch__line--b { font-weight: 700; letter-spacing: -0.045em; }
.sms-torch .sms-torch__rule { height: 1px; margin-bottom: 2rem; background: var(--sms-line); transform-origin: left; }
.sms-torch .sms-torch__row { display: grid; gap: 1.75rem; align-items: end; }
.sms-torch .sms-torch__lead { max-width: 36rem; min-width: 0; color: var(--sms-ink); font-size: var(--sms-step-1); line-height: 1.65; }
.sms-torch .sms-torch__lead p { margin: 0 0 0.75rem; }
.sms-torch .sms-torch__note { color: var(--sms-ink-soft); font-size: var(--sms-step-0); }
.sms-torch .sms-torch__note[hidden] { display: none; }
.sms-torch .sms-torch__actions { display: flex; flex-wrap: wrap; align-items: center; gap: 0.75rem; min-width: 0; }
.sms-torch .sms-torch__switch { display: inline-flex; align-items: center; gap: 0.75rem; min-width: 0; padding: 0.45rem 1.2rem 0.45rem 0.45rem; border: 0; border-radius: 999px; background: rgba(12, 25, 41, 0.75); box-shadow: inset 0 0 0 1px var(--sms-line); color: var(--sms-ink); cursor: pointer; font: inherit; font-size: var(--sms-step--1); font-weight: 500; }
.sms-torch .sms-torch__switch[hidden] { display: none; }
.sms-torch .sms-torch__track { position: relative; display: block; flex: 0 0 auto; width: 3.1rem; height: 1.8rem; border-radius: 999px; background: rgba(255, 255, 255, 0.1); }
.sms-torch .sms-torch__knob { position: absolute; left: 0.2rem; top: 0.2rem; width: 1.4rem; height: 1.4rem; border-radius: 50%; background: #ffffff; transition: transform 0.45s var(--sms-ease); }
.sms-torch .sms-torch__switch[aria-pressed="true"] .sms-torch__track { background: var(--sms-accent); }
.sms-torch .sms-torch__switch[aria-pressed="true"] .sms-torch__knob { transform: translateX(1.3rem); }
@media (min-width: 60em) {
  .sms-torch { display: flex; align-items: flex-end; min-height: clamp(40rem, 30rem + 22vw, 52rem); }
  .sms-torch .sms-torch__inner { flex: 1 1 auto; }
  .sms-torch .sms-torch__base { left: auto; width: 68%; }
  .sms-torch .sms-torch__fade { background: linear-gradient(90deg, var(--sms-bg) 0%, rgba(5, 12, 22, 0.5) 40%, rgba(5, 12, 22, 0) 70%), linear-gradient(0deg, var(--sms-bg) 0%, rgba(5, 12, 22, 0) 35%); }
  .sms-torch .sms-torch__row { grid-template-columns: minmax(0, 1fr) auto; }
}
@media (hover: hover) and (pointer: fine) and (min-width: 60em) {
  .sms-torch.is-live .sms-torch__hint { display: block; }
}

/* ---------- Home: facts strip ---------- */
.sms-facts { border-top: 1px solid var(--sms-line); border-bottom: 1px solid var(--sms-line); }
.sms-facts .sms-facts__list { display: grid; width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: 0 var(--sms-gutter); list-style: none; }
.sms-facts .sms-facts__item { min-width: 0; border-bottom: 1px solid var(--sms-line); }
.sms-facts .sms-facts__item:last-child { border-bottom: 0; }
.sms-facts .sms-facts__link { display: grid; gap: 0.35rem; height: 100%; padding: 1.75rem 0; color: var(--sms-ink); text-decoration: none; transition: background-color 0.4s; }
.sms-facts .sms-facts__link:hover { background: rgba(255, 255, 255, 0.03); }
.sms-facts .sms-facts__label { min-width: 0; color: var(--sms-ink-soft); font-size: 0.75rem; font-weight: 500; letter-spacing: 0.2em; text-transform: uppercase; }
.sms-facts .sms-facts__value { min-width: 0; color: #ffffff; font-size: clamp(2rem, 1.6rem + 1.5vw, 2.75rem); font-weight: 200; line-height: 1.15; letter-spacing: -0.02em; }
.sms-facts .sms-facts__unit { font-size: 0.5em; font-weight: 300; letter-spacing: 0; }
.sms-facts .sms-facts__note { min-width: 0; color: var(--sms-accent); font-size: var(--sms-step--1); font-weight: 400; }
@media (min-width: 40em) {
  .sms-facts .sms-facts__list { grid-template-columns: repeat(2, minmax(0, 1fr)); }
  .sms-facts .sms-facts__item:nth-child(odd) { border-right: 1px solid var(--sms-line); }
  .sms-facts .sms-facts__item:nth-child(3) { border-bottom: 0; }
  .sms-facts .sms-facts__item:nth-child(even) .sms-facts__link { padding-left: 1.75rem; }
}
@media (min-width: 64em) {
  .sms-facts .sms-facts__list { grid-template-columns: repeat(4, minmax(0, 1fr)); }
  .sms-facts .sms-facts__item { border-bottom: 0; border-right: 1px solid var(--sms-line); }
  .sms-facts .sms-facts__item:last-child { border-right: 0; }
  .sms-facts .sms-facts__item + .sms-facts__item .sms-facts__link { padding-left: 1.75rem; }
}

/* ---------- Scene diagram: unassessed / assessed ---------- */
.sms-scene { position: relative; padding: var(--sms-section) 0; }
.sms-scene .sms-scene__inner { display: grid; gap: clamp(2.5rem, 1.5rem + 4vw, 5rem); align-items: center; width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-scene .sms-scene__copy { min-width: 0; }
.sms-scene .sms-scene__title { margin: 0 0 1.5rem; color: #ffffff; font-size: clamp(2.1rem, 1.3rem + 3vw, 3.9rem); font-weight: 200; line-height: 1.06; letter-spacing: -0.035em; }
.sms-scene .sms-scene__text { max-width: 34rem; color: var(--sms-ink-soft); }
.sms-scene .sms-scene__text p { margin: 0 0 1.25rem; }
.sms-scene .sms-scene__visual { min-width: 0; }
.sms-scene .sms-scene__card { padding: clamp(1rem, 0.6rem + 1.5vw, 1.75rem); border-radius: var(--sms-radius); background: linear-gradient(180deg, #0c1a2a, #08121e); box-shadow: inset 0 0 0 1px var(--sms-line), var(--sms-shadow-lg); }
.sms-scene .sms-scene__svg { display: block; width: 100%; height: auto; }
.sms-scene .sms-scene__after { opacity: 0; transition: opacity 0.7s var(--sms-ease); }
.sms-scene .sms-scene__before { opacity: 1; transition: opacity 0.7s var(--sms-ease); }
.sms-scene .sms-scene__cap { margin: 1rem 0 0; color: var(--sms-ink); font-size: var(--sms-step--1); }
.sms-scene .sms-scene__cap--after { display: none; }
.sms-scene .sms-scene__r1:checked ~ * .sms-scene__after { opacity: 1; }
.sms-scene .sms-scene__r1:checked ~ * .sms-scene__before { opacity: 0.25; }
.sms-scene .sms-scene__r1:checked ~ * .sms-scene__cap--before { display: none; }
.sms-scene .sms-scene__r1:checked ~ * .sms-scene__cap--after { display: block; }
""" + SCENE_SEG + r"""
@media (min-width: 60em) {
  .sms-scene .sms-scene__inner { grid-template-columns: minmax(0, 0.85fr) minmax(0, 1.15fr); }
}

/* ---------- Home: scroll story with a pinned photo ---------- */
.sms-story { padding: var(--sms-section) 0; }
.sms-story .sms-story__inner { width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-story .sms-story__head { display: grid; gap: 1.5rem; align-items: end; margin-bottom: clamp(2.5rem, 1.5rem + 3vw, 4rem); }
.sms-story .sms-story__heading { min-width: 0; }
.sms-story .sms-story__title { margin: 0; color: #ffffff; font-size: clamp(2.2rem, 1.3rem + 3.4vw, 4.2rem); font-weight: 200; line-height: 1.05; letter-spacing: -0.035em; }
.sms-story .sms-story__intro { max-width: 30rem; min-width: 0; color: var(--sms-ink-soft); }
.sms-story .sms-story__intro p { margin: 0; }
.sms-story .sms-story__grid { display: grid; gap: 2rem; }
.sms-story .sms-story__media { display: none; min-width: 0; }
.sms-story .sms-story__frame { position: sticky; top: 6.5rem; overflow: hidden; aspect-ratio: 4 / 4.6; border-radius: var(--sms-radius); background: var(--sms-surface); box-shadow: inset 0 0 0 1px var(--sms-line), var(--sms-shadow-lg); }
.sms-story .sms-story__img { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; opacity: 0; transform: scale(1.06); transition: opacity 0.9s var(--sms-ease), transform 1.4s var(--sms-ease); }
.sms-story .sms-story__img.is-active,
.sms-story .sms-story__img:first-child { opacity: 1; transform: none; }
.sms-story.is-live .sms-story__img:first-child:not(.is-active) { opacity: 0; transform: scale(1.06); }
.sms-story .sms-story__bar { position: absolute; left: 1.5rem; right: 1.5rem; bottom: 1.4rem; display: flex; align-items: center; gap: 1rem; color: #ffffff; font-size: 0.8125rem; letter-spacing: 0.12em; }
.sms-story .sms-story__bar::before { content: ""; position: absolute; z-index: -1; left: -1.5rem; right: -1.5rem; bottom: -1.4rem; height: 7rem; background: linear-gradient(0deg, rgba(5, 12, 22, 0.85), transparent); }
.sms-story .sms-story__track { position: relative; flex: 1 1 auto; height: 1px; background: rgba(255, 255, 255, 0.3); }
.sms-story .sms-story__fill { position: absolute; inset: 0; background: var(--sms-accent); transform: scaleX(0.2); transform-origin: left; transition: transform 0.8s var(--sms-ease); }
.sms-story .sms-story__list { margin: 0; padding: 0; list-style: none; }
.sms-story .sms-story__chapter { min-width: 0; padding: 2.5rem 0; border-top: 1px solid var(--sms-line); }
.sms-story .sms-story__inline { aspect-ratio: 16 / 10; margin-bottom: 1.5rem; }
.sms-story .sms-story__count { margin-bottom: 1rem; color: var(--sms-ink-soft); font-size: 0.8125rem; letter-spacing: 0.2em; }
.sms-story .sms-story__name { margin: 0 0 0.75rem; color: #ffffff; font-size: clamp(2rem, 1.4rem + 2.2vw, 3.2rem); font-weight: 200; line-height: 1.08; letter-spacing: -0.03em; }
.sms-story .sms-story__name b { font-weight: 700; }
.sms-story .sms-story__meta { margin-bottom: 1rem; color: var(--sms-accent); font-weight: 400; }
.sms-story .sms-story__text { max-width: 32rem; margin-bottom: 1.5rem; color: var(--sms-ink-soft); }
.sms-story .sms-story__text p { margin: 0; }
.sms-story .sms-story__link { display: inline-flex; align-items: center; gap: 0.9rem; min-width: 0; margin-top: 1.5rem; color: #ffffff; font-weight: 500; text-decoration: none; }
.sms-story .sms-story__go { display: grid; place-items: center; width: 2.75rem; height: 2.75rem; border-radius: 50%; box-shadow: inset 0 0 0 1px rgba(255, 255, 255, 0.35); transition: transform 0.4s var(--sms-ease), background-color 0.4s; }
.sms-story .sms-story__go-icon { width: 1.1rem; height: 1.1rem; }
.sms-story .sms-story__link:hover .sms-story__go { background: var(--sms-accent); color: #04121f; transform: translateX(4px); }
@media (min-width: 60em) {
  .sms-story.is-live .sms-story__chapter { opacity: 0.4; transition: opacity 0.6s var(--sms-ease); }
  .sms-story.is-live .sms-story__chapter.is-active { opacity: 1; }
  .sms-story .sms-story__head { grid-template-columns: minmax(0, 1.2fr) minmax(0, 0.8fr); }
  .sms-story .sms-story__intro { justify-self: end; }
  .sms-story .sms-story__grid { grid-template-columns: minmax(0, 1fr) minmax(0, 0.9fr); gap: clamp(3rem, 2rem + 4vw, 6rem); }
  .sms-story .sms-story__media { display: block; }
  .sms-story .sms-story__inline { display: none; }
  .sms-story .sms-story__chapter { display: flex; flex-direction: column; justify-content: center; min-height: 72vh; padding: 3rem 0; }
}

/* ---------- Home: Assess / Plan / Protect ring ---------- */
.sms-ring { padding: var(--sms-section) 0; background: var(--sms-pale); view-timeline-name: --sms-ring; }
.sms-ring .sms-ring__inner { width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-ring .sms-ring__head { display: grid; gap: 1.5rem; align-items: end; margin-bottom: clamp(2.5rem, 1.5rem + 3vw, 4rem); }
.sms-ring .sms-ring__title { min-width: 0; margin: 0; color: #ffffff; font-size: clamp(2.1rem, 1.3rem + 3.2vw, 4rem); font-weight: 200; line-height: 1.06; letter-spacing: -0.035em; }
.sms-ring .sms-ring__title b { display: block; font-weight: 700; }
.sms-ring .sms-ring__intro { max-width: 30rem; min-width: 0; color: var(--sms-ink-soft); }
.sms-ring .sms-ring__intro p { margin: 0; }
.sms-ring .sms-ring__grid { display: grid; gap: clamp(2rem, 1.5rem + 3vw, 4rem); align-items: center; }
.sms-ring .sms-ring__visual { position: relative; width: min(100%, 24rem); margin: 0 auto; aspect-ratio: 1; }
.sms-ring .sms-ring__svg { display: block; width: 100%; height: 100%; }
.sms-ring .sms-ring__orbit { position: absolute; left: 8.33%; top: 8.33%; width: 83.33%; height: 83.33%; pointer-events: none; }
.sms-ring .sms-ring__dot { position: absolute; left: 50%; top: 0; width: 0.9rem; height: 0.9rem; margin: -0.45rem 0 0 -0.45rem; border-radius: 50%; background: var(--sms-accent); box-shadow: 0 0 18px 4px var(--sms-glow); }
.sms-ring .sms-ring__node { position: absolute; display: grid; justify-items: center; gap: 0.4rem; width: 7rem; margin-left: -3.5rem; color: #ffffff; font-size: var(--sms-step--1); font-weight: 600; text-align: center; }
.sms-ring .sms-ring__node--0 { left: 50%; top: 8.33%; margin-top: -0.65rem; }
.sms-ring .sms-ring__node--1 { left: 86.1%; top: 70.8%; margin-top: -0.65rem; }
.sms-ring .sms-ring__node--2 { left: 13.9%; top: 70.8%; margin-top: -0.65rem; }
.sms-ring .sms-ring__pip { display: block; width: 1.3rem; height: 1.3rem; border-radius: 50%; background: var(--sms-accent); box-shadow: 0 0 0 5px var(--sms-pale), 0 0 0 6px var(--sms-line-green); }
.sms-ring .sms-ring__node--1 .sms-ring__pip,
.sms-ring .sms-ring__node--2 .sms-ring__pip { order: -1; }
.sms-ring .sms-ring__node--0 { flex-direction: column-reverse; }
.sms-ring .sms-ring__centre { position: absolute; inset: 0; display: grid; place-content: center; gap: 0.35rem; text-align: center; pointer-events: none; }
.sms-ring .sms-ring__centre-label { color: var(--sms-ink-soft); font-size: 0.6875rem; letter-spacing: 0.22em; text-transform: uppercase; }
.sms-ring .sms-ring__centre-text { color: #ffffff; font-size: clamp(1.25rem, 1.1rem + 0.6vw, 1.6rem); font-weight: 300; }
.sms-ring .sms-ring__list { margin: 0; padding: 0; border-top: 1px solid var(--sms-line); list-style: none; }
.sms-ring .sms-ring__stage { display: grid; grid-template-columns: 2.5rem minmax(0, 1fr); gap: 1rem; padding: 1.5rem 0; border-bottom: 1px solid var(--sms-line); }
.sms-ring .sms-ring__stage-dot { width: 0.75rem; height: 0.75rem; margin-top: 0.55rem; border-radius: 50%; background: var(--sms-accent); box-shadow: 0 0 0 4px var(--sms-mint); }
.sms-ring .sms-ring__stage-body { min-width: 0; }
.sms-ring .sms-ring__stage-name { margin: 0 0 0.35rem; color: #ffffff; font-size: var(--sms-step-1); font-weight: 400; }
.sms-ring .sms-ring__stage-text { color: var(--sms-ink-soft); }
.sms-ring .sms-ring__stage-text p { margin: 0; }
@media (min-width: 60em) {
  .sms-ring .sms-ring__head { grid-template-columns: minmax(0, 1.2fr) minmax(0, 0.8fr); }
  .sms-ring .sms-ring__intro { justify-self: end; }
  .sms-ring .sms-ring__grid { grid-template-columns: minmax(0, 0.9fr) minmax(0, 1.1fr); }
}
@supports (animation-timeline: view()) {
  @keyframes sms-orbit { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }
  @keyframes sms-light { from { opacity: 0.25; transform: scale(0.85); } to { opacity: 1; transform: none; } }
  .sms-ring .sms-ring__orbit { animation: sms-orbit linear both; animation-timeline: --sms-ring; animation-range: entry 40% exit 10%; }
  .sms-ring .sms-ring__node--0,
  .sms-ring .sms-ring__stage:nth-child(1) { animation: sms-light linear both; animation-timeline: --sms-ring; animation-range: entry 40% entry 70%; }
  .sms-ring .sms-ring__node--1,
  .sms-ring .sms-ring__stage:nth-child(2) { animation: sms-light linear both; animation-timeline: --sms-ring; animation-range: entry 75% contain 15%; }
  .sms-ring .sms-ring__node--2,
  .sms-ring .sms-ring__stage:nth-child(3) { animation: sms-light linear both; animation-timeline: --sms-ring; animation-range: contain 20% contain 45%; }
}

.sms-ring .sms-ring__heading,
.sms-ring .sms-ring__label,
.sms-ring .sms-ring__pip,
.sms-ring .sms-ring__centre-label,
.sms-ring .sms-ring__centre-text,
.sms-ring .sms-ring__list,
.sms-ring .sms-ring__visual,
.sms-ring .sms-ring__stage-dot,
.sms-story .sms-story__num,
.sms-story .sms-story__track,
.sms-story .sms-story__list,
.sms-story .sms-story__count,
.sms-story .sms-story__meta,
.sms-story .sms-story__name,
.sms-story .sms-story__text,
.sms-story .sms-story__go,
.sms-story .sms-pills,
.sms-torch .sms-torch__inner,
.sms-torch .sms-torch__track,
.sms-voice .sms-voice__media { min-width: 0; }

/* ---------- Home: a personal message ---------- */
.sms-voice { padding: var(--sms-section) 0; }
.sms-voice .sms-voice__inner { display: grid; gap: clamp(2rem, 1.5rem + 3vw, 4.5rem); align-items: center; width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-voice .sms-voice__frame { aspect-ratio: 1; max-width: 30rem; box-shadow: var(--sms-shadow-lg); }
.sms-voice .sms-voice__quote { min-width: 0; margin: 0; }
.sms-voice .sms-voice__text { margin: 0 0 1.5rem; color: #ffffff; font-size: clamp(1.35rem, 1.1rem + 1.1vw, 2rem); font-weight: 200; line-height: 1.45; letter-spacing: -0.01em; }
.sms-voice .sms-voice__text p { margin: 0; }
.sms-voice .sms-voice__cite { display: block; color: var(--sms-ink-soft); font-style: normal; }
.sms-voice .sms-voice__claim { display: flex; gap: 1rem; align-items: center; max-width: 34rem; margin-top: 2rem; padding: 1.1rem 1.4rem; border-radius: var(--sms-radius-sm); background: var(--sms-mint); box-shadow: inset 0 0 0 1px var(--sms-line-green); color: var(--sms-ink); }
.sms-voice .sms-voice__claim-icon { width: 2.5rem; height: 2.5rem; padding: 0.55rem; border-radius: 50%; background: var(--sms-accent); color: #04121f; }
.sms-voice .sms-voice__claim-text { min-width: 0; }
@media (min-width: 56em) {
  .sms-voice .sms-voice__inner { grid-template-columns: minmax(0, 0.8fr) minmax(0, 1.2fr); }
}
"""

RISE = [".sms-nhero .sms-nhero__title", ".sms-torch .sms-torch__title"]
ENTRANCE = [".sms-nhero .sms-nhero__crumb", ".sms-torch .sms-kicker", ".sms-nhero .sms-kicker", ".sms-torch .sms-torch__rule", ".sms-nhero .sms-nhero__lead", ".sms-torch .sms-torch__row", ".sms-nhero .sms-nhero__row", ".sms-facts .sms-facts__item"]
REVEAL = [".sms-scene .sms-scene__copy", ".sms-scene .sms-scene__visual", ".sms-story .sms-story__head", ".sms-story .sms-story__media",
          ".sms-ring .sms-ring__head", ".sms-ring .sms-ring__visual", ".sms-voice .sms-voice__media", ".sms-voice .sms-voice__quote", ".sms-ncta .sms-ncta__box"]
LOOP = [".sms-nhero .sms-nhero__glow", ".sms-nhero .sms-nhero__frame .sms-photo__img", ".sms-ring .sms-ring__orbit",
        ".sms-ring .sms-ring__node--0", ".sms-ring .sms-ring__node--1", ".sms-ring .sms-ring__node--2", ".sms-ring .sms-ring__stage:nth-child(1)",
        ".sms-ring .sms-ring__stage:nth-child(2)", ".sms-ring .sms-ring__stage:nth-child(3)"]
TRANS = [".sms-torch .sms-torch__shade", ".sms-torch .sms-torch__lens", ".sms-torch .sms-torch__knob", ".sms-facts .sms-facts__link",
         ".sms-scene .sms-scene__after", ".sms-scene .sms-scene__before", ".sms-story .sms-story__img", ".sms-story .sms-story__fill",
         ".sms-story .sms-story__go", ".sms-story.is-live .sms-story__chapter"]


def title_html(text):
    """'Event Medical Cover' -> 'Event Medical <b>Cover</b>' (bold last word, J style)."""
    words = text.split(" ")
    if len(words) == 1:
        return "<b>%s</b>" % e(text)
    return "%s <b>%s</b>" % (e(" ".join(words[:-1])), e(words[-1]))


def page_hero(ctx, h, crumb=True):
    crumb_html = '<div class="sms-nhero__crumb"><a class="sms-nhero__crumb-link" href="%s">Home</a> / %s</div>' % (ctx.href("home"), e(LABEL[ctx.slug])) if crumb else ""
    sub = '<div class="sms-nhero__sub">%s</div>' % e(h["sub"]) if h.get("sub") else ""
    facts = "".join('<div class="sms-nhero__fact">%s<span class="sms-nhero__fact-text">%s</span></div>' % (icon(ic, "sms-nhero__fact-icon"), e(t)) for ic, t in h.get("chips", [])[:2])
    card = '<div class="sms-nhero__card">%s</div>' % facts if facts else ""
    acts = '<div class="sms-nhero__actions">%s</div>' % buttons(ctx, h["buttons"]) if h.get("buttons") else ""
    return """<section class="sms-nhero">
  <div class="sms-nhero__media">%s</div>
  <div class="sms-nhero__shade" aria-hidden="true"></div>
  <div class="sms-nhero__glow" aria-hidden="true"></div>
  <div class="sms-nhero__inner">
    %s
    <div class="sms-kicker">%s</div>
    <h1 class="sms-nhero__title">%s</h1>
    <div class="sms-nhero__lead">%s%s</div>
    <div class="sms-nhero__row">%s%s</div>
  </div>
</section>
""" % (photo(ctx, h["photo"], lazy=False, parallax=False, figcls="sms-nhero__frame"), crumb_html, e(h["eyebrow"]), e(h["title"]), sub, paras(h["body"]), acts, card)


def cta(ctx, d):
    btns = [(l, t) for l, t in d["buttons"] if t != "tel"]
    acts = buttons(ctx, btns) if btns else ""
    return """<section class="sms-ncta">
  <div class="sms-ncta__inner">
    <div class="sms-ncta__box">
      <div class="sms-ncta__copy"><h2 class="sms-ncta__title">%s</h2><div class="sms-ncta__text">%s</div></div>
      <div class="sms-ncta__side">
        <div class="sms-ncta__actions">%s</div>
        <div class="sms-ncta__call">Or call us on <a href="tel:%s">%s</a></div>
      </div>
    </div>
  </div>
</section>
""" % (e(d["title"]), paras(d["text"]), acts, PHONE_TEL, PHONE)


def chrome_top(ctx):
    return header(ctx, "white")


def chrome_bottom(ctx):
    return footer(ctx, "white")


# ---------------------------------------------------------------------------
# Scene diagram: an illustrated event site, before and after it is assessed
# ---------------------------------------------------------------------------

def _crowd():
    dots = []
    for row in range(8):
        for col in range(15):
            n = (row * 37 + col * 91) % 17
            if n in (3, 11):
                continue
            x = 78 + col * 17 + (n % 5) - 2
            y = 128 + row * 15 + (n % 4) - 1
            dots.append('<circle cx="%d" cy="%d" r="3.1"/>' % (x, y))
    return "".join(dots)


def _hazard(x, y):
    return '<path d="M%d %dl10 17h-20z" fill="none" stroke-width="1.6" stroke-linejoin="round"/>' % (x, y - 11)


def _label(x, y, text, anchor="start"):
    return '<text x="%d" y="%d" text-anchor="%s" font-size="13" font-weight="500" fill="#e9eff5" stroke="#08121e" stroke-width="4" paint-order="stroke">%s</text>' % (x, y, anchor, text)


SCENE_HAZARDS = [(262, 72), (376, 190), (150, 266)]


def scene_svg():
    hz = "".join(_hazard(x, y) for x, y in SCENE_HAZARDS)
    rings = "".join('<circle cx="%d" cy="%d" r="22" fill="rgba(130,208,110,0.08)" stroke="#82d06e" stroke-width="1.6"/>' % (x, y) for x, y in SCENE_HAZARDS)
    qs = "".join('<text x="%d" y="%d" font-size="15" font-weight="600" fill="#aebccb">?</text>' % (x + 14, y - 8) for x, y in SCENE_HAZARDS)
    return """<svg class="sms-scene__svg" viewBox="0 0 600 360" role="img" aria-labelledby="sms-scene-t sms-scene-d" xmlns="http://www.w3.org/2000/svg">
  <title id="sms-scene-t">Illustration of an event site</title>
  <desc id="sms-scene-d">A field with a stage, a crowd and an entrance from the road. When assessed, the hazards are ringed, a first aid point is marked and an emergency access route runs in from the road.</desc>
  <rect x="0" y="300" width="600" height="60" fill="#07101a"/>
  <line x1="0" y1="330" x2="600" y2="330" stroke="rgba(255,255,255,0.18)" stroke-width="2" stroke-dasharray="14 12"/>
  <rect x="16" y="16" width="568" height="268" rx="18" fill="#0b1a2b" stroke="rgba(170,195,220,0.28)" stroke-width="1.5"/>
  <rect x="436" y="278" width="64" height="12" fill="#0b1a2b"/>
  <text x="468" y="276" text-anchor="middle" font-size="11" fill="#aebccb">Entrance</text>
  <rect x="56" y="40" width="176" height="56" rx="8" fill="rgba(255,255,255,0.06)" stroke="rgba(170,195,220,0.3)"/>
  <text x="144" y="73" text-anchor="middle" font-size="13" fill="#aebccb">Stage</text>
  <g fill="rgba(174,188,203,0.55)">%s</g>
  <g class="sms-scene__before" stroke="#ffcf66">%s</g>
  <g class="sms-scene__before">%s</g>
  <g class="sms-scene__after">
    %s
    <g stroke="#82d06e">%s</g>
    <path d="M468 344V196" fill="none" stroke="#82d06e" stroke-width="3" stroke-dasharray="9 7" stroke-linecap="round"/>
    <circle cx="468" cy="178" r="20" fill="#82d06e"/>
    <path d="M468 168v20M458 178h20" stroke="#04121f" stroke-width="4" stroke-linecap="round"/>
    %s
    %s
    %s
    <rect x="474" y="30" width="96" height="30" rx="15" fill="rgba(130,208,110,0.14)" stroke="#82d06e"/>
    <text x="522" y="50" text-anchor="middle" font-size="12" font-weight="600" fill="#e9eff5">Site plan</text>
  </g>
</svg>""" % (_crowd(), hz, qs, rings, hz, _label(468, 148, "First aid provision", "middle"), _label(456, 250, "Emergency access", "end"), _label(296, 76, "Hazards identified"))


def scene(ctx, kicker="Our Consultancy Services", title="Safety Starts by Recognising [[Danger]]",
          text="In pre-hospital care, the first step is always to assess for danger. Before treatment begins, we look at the environment, identify risks, protect people from harm, and make sure the right support is in place.",
          link=True):
    radios, seg_html = dark.seg("scene", ["Unassessed", "Assessed"], 0, "Show the site")
    tag = "h2"
    more_link = '<a class="sms-arrowlink" href="%s">Risk &amp; Needs Consultancy&nbsp;<span class="sms-arrow" aria-hidden="true">&rarr;</span></a>' % ctx.href("risk-needs-consultancy") if link else ""
    return """<section class="sms-scene" id="danger">
  %s
  <div class="sms-scene__inner">
    <div class="sms-scene__copy">
      <div class="sms-kicker">%s</div>
      <%s class="sms-scene__title">%s</%s>
      <div class="sms-scene__text"><p>%s</p></div>
      %s
    </div>
    <div class="sms-scene__visual">
      %s
      <div class="sms-scene__card">
        %s
        <p class="sms-scene__cap sms-scene__cap--before">Unassessed: the hazards are there, but nobody has looked at the site, the people and the access together.</p>
        <p class="sms-scene__cap sms-scene__cap--after">Assessed: hazards identified, people protected from harm and the right support in place.</p>
        <p class="sms-caption">Illustration, not to scale.</p>
      </div>
    </div>
  </div>
</section>
""" % (radios, e(kicker), tag, e(title), tag, e(text), more_link, seg_html, scene_svg())


def inner_extra(ctx, slug):
    if slug == "risk-needs-consultancy":
        return scene(ctx, kicker="Our Consultancy Services", title="Assess the risk. Plan the response. [[Protect your people.]]",
                     text="Our Risk & Needs Consultancy applies that same practical, safety-first mindset to workplaces, events and public environments.", link=False)
    return ""


# ---------------------------------------------------------------------------
# Homepage
# ---------------------------------------------------------------------------
STORY = [
    ("event-medical-cover", "Event Medical Cover", "festival", "Skilled. Proportionate. Reliable.",
     "From small local events to large-scale public gatherings, we provide professional, reliable and proportionate medical cover that gives you peace of mind.",
     ["Community events and village fetes", "Sports and combat-sports events", "Small festivals and outdoor activities"]),
    ("medical-training", "Medical Training", "cpr-room", "Qualsafe Registered Centre",
     "Accredited first aid and workplace safety training delivered by real frontline professionals in Swadlincote and beyond.",
     ["Emergency First Aid at Work", "First Aid at Work", "FREC 3 and FREC 4"]),
    ("risk-needs-consultancy", "Risk & Needs Consultancy", "assessor", "Free initial consultation",
     "We help businesses and event organisers understand their risks, meet their legal obligations, and ensure they have the right plans, people and equipment in place.",
     ["First Aid Needs Assessment", "Risk Assessment Writing", "Event Medical Plans"]),
    ("pre-hospital-career-support", "Pre-Hospital Career Support", "cpr-outdoor", "Honest, frontline-informed support",
     "Take your next step in a pre-hospital career with tailored interview preparation, mock assessments and honest, practical feedback.",
     ["Interview preparation", "Mock assessments", "Feedback & development"]),
    ("recruitment", "Recruitment", "team", "Interested in working with us?",
     "We are looking to hear from experienced professionals who can support our growing services.",
     ["Trainers", "Safety operatives", "Clinicians"]),
]

STAGES = [
    ("Assess", "We look at the environment and identify the risks, before problems occur."),
    ("Plan", "We help you put proportionate plans, people and equipment in place."),
    ("Protect", "Protect people from harm, and make sure the right support is in place."),
]


def ring_svg():
    return """<svg class="sms-ring__svg" viewBox="0 0 360 360" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg">
  <circle cx="180" cy="180" r="150" fill="none" stroke="rgba(170,195,220,0.2)" stroke-width="1.5"/>
  <circle cx="180" cy="180" r="118" fill="none" stroke="rgba(130,208,110,0.12)" stroke-width="1" stroke-dasharray="2 8"/>
</svg>"""


def home(ctx):
    ctx.notes += ["Image-only copy used: \"Clinician-led safety and medical support\" (clinician-led-safety.png)",
                  "Image-only copy used: Mathew Stones' quote \"We truly care about the people...\" (footer-homepage.png)",
                  "Image-only copy used: \"Mathew and Tom bring over 15 years of ambulance experience...\" (why-choose-us.png - use approved)",
                  "Hero: the inspection light is an enhancement; without JavaScript the photo shows under a dark shade"]
    base = photo_img(ctx, "festival", "sms-torch__img", lazy=False)
    lens = photo_img(ctx, "festival", "sms-torch__lens-img", lazy=False, decorative=True)
    out = """<section class="sms-torch" data-sms-torch>
  <div class="sms-torch__base">
    %s
    <div class="sms-torch__shade" aria-hidden="true"></div>
    <div class="sms-torch__lens" aria-hidden="true"><div class="sms-torch__lens-inner">%s</div></div>
    <div class="sms-torch__fade" aria-hidden="true"></div>
  </div>
  <div class="sms-torch__spot" aria-hidden="true"></div>
  <div class="sms-torch__hint" aria-hidden="true">Move the light</div>
  <div class="sms-torch__inner">
    <div class="sms-kicker">Clinician-led safety and medical support</div>
    <h1 class="sms-torch__title"><span class="sms-torch__line">Protecting People.</span> <span class="sms-torch__line sms-torch__line--b">Supporting Business.</span></h1>
    <div class="sms-torch__rule" aria-hidden="true"></div>
    <div class="sms-torch__row">
      <div class="sms-torch__lead">
        <p>%s</p>
        <p class="sms-torch__note" hidden data-sms-torch-note>In pre-hospital care, the first step is always to assess for danger. Move the light across the scene, then switch the lights on.</p>
      </div>
      <div class="sms-torch__actions">
        <button class="sms-torch__switch" type="button" aria-pressed="false" hidden data-sms-switch><span class="sms-torch__track" aria-hidden="true"><span class="sms-torch__knob"></span></span>Lights on</button>
        %s
      </div>
    </div>
  </div>
</section>
""" % (base, lens, e(C.INTRO2), buttons(ctx, [("Book online", "book")]))

    facts = [
        ("event-medical-cover", "Event Medical Cover", "FREC 3", "", "The minimum grade for many events we support"),
        ("medical-training", "Medical Training", "908578", "", "Qualsafe Registered Centre number"),
        ("risk-needs-consultancy", "Risk & Needs Consultancy", "Free", "", "Initial consultation, with no obligation"),
        ("about", "Our directors", "15+", " years", "Of ambulance experience between them"),
    ]
    items = "".join('<li class="sms-facts__item"><a class="sms-facts__link" href="%s"><span class="sms-facts__label">%s</span><span class="sms-facts__value">%s<span class="sms-facts__unit">%s</span></span><span class="sms-facts__note">%s</span></a></li>' % (
        ctx.href(s), e(l), e(v), e(u), e(n)) for s, l, v, u, n in facts)
    out += '<section class="sms-facts" aria-label="Streamline at a glance"><ul class="sms-facts__list">%s</ul></section>\n' % items

    out += scene(ctx)

    frames, chapters = "", ""
    for i, (slug, title, ph, meta, text, pills) in enumerate(STORY):
        frames += photo_img(ctx, ph, "sms-story__img%s" % (" is-active" if i == 0 else ""), decorative=True).replace("<img ", '<img data-sms-frame="%d" ' % i, 1)
        pl = "".join('<li class="sms-pills__item"><span class="sms-pill">%s</span></li>' % e(p) for p in pills)
        chapters += """<li class="sms-story__chapter%s" data-sms-chapter="%d">
          %s
          <div class="sms-story__count">%02d</div>
          <h3 class="sms-story__name">%s</h3>
          <div class="sms-story__meta">%s</div>
          <div class="sms-story__text"><p>%s</p></div>
          <ul class="sms-pills">%s</ul>
          <a class="sms-story__link" href="%s">%s<span class="sms-story__go" aria-hidden="true">%s</span></a>
        </li>""" % (" is-active" if i == 0 else "", i, photo(ctx, ph, figcls="sms-story__inline", parallax=False), i + 1, title_html(title), e(meta), e(text), pl, ctx.href(slug), e(title), icon("arrow", "sms-story__go-icon"))
    out += """<section class="sms-story" id="services" data-sms-story>
  <div class="sms-story__inner">
    <div class="sms-story__head">
      <div class="sms-story__heading"><div class="sms-kicker">Our Services</div><h2 class="sms-story__title">What We <span class="sms-mark">Provide</span></h2></div>
      <div class="sms-story__intro"><p>%s</p></div>
    </div>
    <div class="sms-story__grid">
      <div class="sms-story__media" aria-hidden="true">
        <div class="sms-story__frame">%s
          <div class="sms-story__bar"><span class="sms-story__num" data-sms-frame-num>01</span><span class="sms-story__track"><span class="sms-story__fill" data-sms-frame-bar></span></span><span class="sms-story__num">05</span></div>
        </div>
      </div>
      <ol class="sms-story__list">%s</ol>
    </div>
  </div>
</section>
""" % (e(C.INTRO), frames, chapters)

    nodes = "".join('<div class="sms-ring__node sms-ring__node--%d"><span class="sms-ring__pip" aria-hidden="true"></span><span class="sms-ring__label">%s</span></div>' % (i, e(n)) for i, (n, _) in enumerate(STAGES))
    stages = "".join('<li class="sms-ring__stage"><span class="sms-ring__stage-dot" aria-hidden="true"></span><div class="sms-ring__stage-body"><h3 class="sms-ring__stage-name">%s</h3><div class="sms-ring__stage-text"><p>%s</p></div></div></li>' % (e(n), e(t)) for n, t in STAGES)
    out += """<section class="sms-ring" id="approach">
  <div class="sms-ring__inner">
    <div class="sms-ring__head">
      <div class="sms-ring__heading"><div class="sms-kicker">Our approach</div><h2 class="sms-ring__title">Assess the risk. Plan the response. <b>Protect your people.</b></h2></div>
      <div class="sms-ring__intro"><p>%s</p></div>
    </div>
    <div class="sms-ring__grid">
      <div class="sms-ring__visual">
        %s
        <div class="sms-ring__orbit" aria-hidden="true"><span class="sms-ring__dot"></span></div>
        %s
        <div class="sms-ring__centre" aria-hidden="true"><span class="sms-ring__centre-label">Safety first</span><span class="sms-ring__centre-text">Assess &middot; Plan &middot; Protect</span></div>
      </div>
      <ol class="sms-ring__list">%s</ol>
    </div>
  </div>
</section>
""" % (e("Our Risk & Needs Consultancy applies that same practical, safety-first mindset to workplaces, events and public environments."), ring_svg(), nodes, stages)

    out += """<section class="sms-voice">
  <div class="sms-voice__inner">
    <div class="sms-voice__media">%s</div>
    <figure class="sms-voice__quote">
      <div class="sms-kicker">A personal message from Mathew</div>
      <blockquote class="sms-voice__text"><p>%s</p></blockquote>
      <figcaption class="sms-voice__cite">Mathew Stones, Director</figcaption>
      <div class="sms-voice__claim">%s<span class="sms-voice__claim-text">%s</span></div>
    </figure>
  </div>
</section>
""" % (photo(ctx, "team", figcls="sms-voice__frame"), e(C.MATHEW_QUOTE), icon("heart", "sms-voice__claim-icon"), e(C.CLAIM_15))

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
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* Inspection light: a lens that follows the pointer and shows the photo unshaded */
  var torch = document.querySelector('[data-sms-torch]');
  if (torch) {
    var base = torch.querySelector('.sms-torch__base');
    var cur = { x: 0, y: 0 }, tgt = { x: 0, y: 0 }, running = false;
    var measure = function () {
      var r = base.getBoundingClientRect();
      torch.style.setProperty('--bw', r.width + 'px');
      torch.style.setProperty('--bh', r.height + 'px');
      return r;
    };
    var paint = function () {
      torch.style.setProperty('--x', cur.x.toFixed(1) + 'px');
      torch.style.setProperty('--y', cur.y.toFixed(1) + 'px');
    };
    var step = function () {
      var k = reduce ? 1 : 0.08;
      cur.x += (tgt.x - cur.x) * k; cur.y += (tgt.y - cur.y) * k; paint();
      if (Math.abs(tgt.x - cur.x) > 0.3 || Math.abs(tgt.y - cur.y) > 0.3) { window.requestAnimationFrame(step); } else { running = false; }
    };
    var go = function () { if (!running) { running = true; window.requestAnimationFrame(step); } };
    var aim = function (ev) { var r = base.getBoundingClientRect(); tgt.x = ev.clientX - r.left; tgt.y = ev.clientY - r.top; go(); };
    var r0 = measure();
    tgt.x = r0.width * 0.6; tgt.y = r0.height * 0.4;
    cur.x = reduce ? tgt.x : r0.width * 0.96; cur.y = reduce ? tgt.y : r0.height * 0.08;
    paint();
    torch.classList.add('is-live');
    torch.addEventListener('pointermove', aim);
    torch.addEventListener('pointerdown', aim);
    window.addEventListener('resize', measure);
    window.setTimeout(go, 350);
    var note = torch.querySelector('[data-sms-torch-note]');
    if (note) { note.hidden = false; }
    var sw = torch.querySelector('[data-sms-switch]');
    if (sw) {
      sw.hidden = false;
      sw.addEventListener('click', function () {
        var on = sw.getAttribute('aria-pressed') !== 'true';
        sw.setAttribute('aria-pressed', on ? 'true' : 'false');
        torch.classList.toggle('is-lit', on);
      });
    }
  }

  /* Scroll story: the chapter in the middle of the screen sets the pinned photo */
  var story = document.querySelector('[data-sms-story]');
  if (story && 'IntersectionObserver' in window) {
    var chapters = story.querySelectorAll('[data-sms-chapter]');
    var frames = story.querySelectorAll('[data-sms-frame]');
    var num = story.querySelector('[data-sms-frame-num]');
    var bar = story.querySelector('[data-sms-frame-bar]');
    var set = function (i) {
      Array.prototype.forEach.call(chapters, function (c) { c.classList.toggle('is-active', c.getAttribute('data-sms-chapter') === i); });
      Array.prototype.forEach.call(frames, function (f) { f.classList.toggle('is-active', f.getAttribute('data-sms-frame') === i); });
      if (num) { num.textContent = '0' + (Number(i) + 1); }
      if (bar) { bar.style.transform = 'scaleX(' + ((Number(i) + 1) / chapters.length) + ')'; }
    };
    story.classList.add('is-live');
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { set(en.target.getAttribute('data-sms-chapter')); } });
    }, { rootMargin: '-45% 0px -45% 0px' });
    Array.prototype.forEach.call(chapters, function (c) { io.observe(c); });
  }
})();
</script>
"""


def scripts(ctx, main):
    return JS if ("data-sms-torch" in main or "data-sms-story" in main) else ""
