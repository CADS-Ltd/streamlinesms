"""Concept 8 - Kinetic. Typography that moves: the words themselves are the
visuals. Bricolage Grotesque (variable weight and width) set big and confident on
white pages, with a navy island or two and a navy footer.

Homepage: a huge strapline revealed line by line beside a slowly panning
shield-shaped photo, a scroll-velocity marquee of the three services, stacking
service cards, a navy spotlight that follows the pointer, a kinetic word wall of
who we work with, magnetic primary buttons, FAQs and a big typographic CTA band.

Inner extras: Recruitment gets the pathway as stacking cards with giant numbers
plus the values as a kinetic word row; Medical Training gets the course list as
a giant hover list that reveals each course's duration."""
import re

from common import *  # noqa: F401,F403
import content as C

NAME = "Kinetic"
FONTS = "https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wdth,wght@12..96,75..100,200..800&display=swap"

REC = C.PAGES["recruitment"]["sections"]
COURSES = C.PAGES["medical-training"]["sections"][0][1]

CSS = r"""
/* ===== Concept 8 theme: kinetic ===== */
.sms-page {
  --sms-font: "Bricolage Grotesque", "Arial Narrow", Arial, sans-serif;
  --sms-radius: 1.75rem;
  --sms-radius-sm: 1rem;
  --sms-max: 80rem;
  --sms-kin-ease: cubic-bezier(0.19, 1, 0.22, 1);
  --sms-step-2: clamp(2.1rem, 1.3rem + 3.2vw, 4.25rem);
  font-size: clamp(1.0313rem, 0.99rem + 0.2vw, 1.125rem);
  font-optical-sizing: auto;
}
.sms-page .sms-mark { color: var(--sms-green); }
.sms-page ::selection { background: var(--sms-navy); color: #ffffff; }

/* Buttons: chunky pills; primary ones are magnetic (JS sets --sms-mx / --sms-my) */
.sms-page .sms-btn { padding: 1rem 1.55rem; font-size: 1rem; font-weight: 700; letter-spacing: 0; }
.sms-page .sms-btn--primary { box-shadow: none; transform: translate3d(var(--sms-mx, 0px), var(--sms-my, 0px), 0); transition: transform 0.35s var(--sms-kin-ease), background-color 0.25s, border-color 0.25s; }
.sms-page .sms-btn--primary:hover { border-color: var(--sms-navy); background: var(--sms-navy); transform: translate3d(var(--sms-mx, 0px), calc(var(--sms-my, 0px) - 2px), 0); }
.sms-page .sms-btn--outline { border-color: var(--sms-navy); color: var(--sms-navy); }
.sms-page .sms-btn--outline:hover { background: var(--sms-navy); color: #ffffff; }

/* Header */
.sms-header { border-bottom: 1px solid var(--sms-line); background: rgba(255, 255, 255, 0.96); }
.sms-header .sms-header__link { font-size: 0.975rem; font-weight: 600; }
.sms-header .sms-header__link::after { height: 3px; }
.sms-header .sms-header__summary { background: var(--sms-navy); color: #ffffff; }
.sms-header .sms-header__panel { border-radius: 1.25rem; box-shadow: 0 0 0 1px var(--sms-line), 0 24px 60px rgba(6, 30, 53, 0.16); }
.sms-header .sms-header__panel-link { font-weight: 600; }

/* Footer: navy, plus a big drifting wordmark above it */
.sms-footer { background: var(--sms-navy); color: rgba(255, 255, 255, 0.84); }
.sms-footer .sms-footer__heading,
.sms-footer .sms-footer__tag { color: #ffffff; }
.sms-footer .sms-footer__tag { font-size: 1.15rem; font-weight: 700; }
.sms-footer .sms-footer__link { color: rgba(255, 255, 255, 0.84); }
.sms-footer .sms-footer__link:hover { color: var(--sms-green-on-navy); }
.sms-footer .sms-footer__base { border-color: rgba(255, 255, 255, 0.16); }
.sms-footer a:focus-visible { outline-color: var(--sms-green-on-navy); }
.sms-kinsign { overflow: hidden; padding: clamp(2.5rem, 1.5rem + 3vw, 4.5rem) 0 0; background: var(--sms-navy); }
.sms-kinsign .sms-kinsign__word { display: inline-block; margin-left: var(--sms-gutter); color: var(--sms-green-on-navy); font-size: clamp(5rem, 1rem + 20vw, 19rem); font-weight: 800; font-stretch: 84%; line-height: 0.82; letter-spacing: -0.04em; white-space: nowrap; -webkit-text-fill-color: transparent; -webkit-text-stroke: max(1.5px, 0.012em) var(--sms-green-on-navy); }

/* Shared eyebrow + display heading */
.sms-feature .sms-feature__eyebrow,
.sms-cards .sms-cards__eyebrow,
.sms-steps .sms-steps__eyebrow,
.sms-checklist .sms-checklist__eyebrow,
.sms-faq .sms-faq__eyebrow,
.sms-quotes .sms-quotes__eyebrow,
.sms-people .sms-people__eyebrow,
.sms-contact .sms-contact__eyebrow,
.sms-links .sms-links__eyebrow,
.sms-marquee .sms-marquee__eyebrow,
.sms-booking .sms-booking__eyebrow,
.sms-kinhero .sms-kinhero__eyebrow,
.sms-kinpage .sms-kinpage__eyebrow,
.sms-kinstack .sms-kinstack__eyebrow,
.sms-kinpair .sms-kinpair__eyebrow,
.sms-kinwall .sms-kinwall__eyebrow,
.sms-kincourse .sms-kincourse__eyebrow,
.sms-kinpath .sms-kinpath__eyebrow,
.sms-kinvalues .sms-kinvalues__title { display: inline-flex; align-items: center; gap: 0.6rem; margin: 0 0 1rem; color: var(--sms-green); font-size: 0.8125rem; font-weight: 700; letter-spacing: 0.14em; line-height: 1.3; text-transform: uppercase; }
.sms-feature .sms-feature__eyebrow::before,
.sms-cards .sms-cards__eyebrow::before,
.sms-steps .sms-steps__eyebrow::before,
.sms-checklist .sms-checklist__eyebrow::before,
.sms-faq .sms-faq__eyebrow::before,
.sms-quotes .sms-quotes__eyebrow::before,
.sms-people .sms-people__eyebrow::before,
.sms-contact .sms-contact__eyebrow::before,
.sms-links .sms-links__eyebrow::before,
.sms-marquee .sms-marquee__eyebrow::before,
.sms-booking .sms-booking__eyebrow::before,
.sms-kinhero .sms-kinhero__eyebrow::before,
.sms-kinpage .sms-kinpage__eyebrow::before,
.sms-kinstack .sms-kinstack__eyebrow::before,
.sms-kinpair .sms-kinpair__eyebrow::before,
.sms-kinwall .sms-kinwall__eyebrow::before,
.sms-kincourse .sms-kincourse__eyebrow::before,
.sms-kinpath .sms-kinpath__eyebrow::before,
.sms-kinvalues .sms-kinvalues__title::before { content: ""; flex: 0 0 auto; width: 0.55rem; height: 0.55rem; border-radius: 50%; background: currentColor; }
.sms-feature .sms-feature__title,
.sms-cards .sms-cards__title,
.sms-steps .sms-steps__title,
.sms-checklist .sms-checklist__title,
.sms-faq .sms-faq__title,
.sms-quotes .sms-quotes__title,
.sms-people .sms-people__title,
.sms-contact .sms-contact__title,
.sms-links .sms-links__title,
.sms-marquee .sms-marquee__title,
.sms-booking .sms-booking__title { margin: 0 0 1.1rem; font-size: var(--sms-step-2); font-weight: 800; font-stretch: 80%; line-height: 0.98; letter-spacing: -0.025em; }
.sms-contact .sms-contact__title { font-size: clamp(1.9rem, 1.3rem + 2.2vw, 3rem); }
.sms-cards .sms-cards__head,
.sms-steps .sms-steps__head,
.sms-checklist .sms-checklist__head,
.sms-people .sms-people__head,
.sms-links .sms-links__head { max-width: 54rem; }

/* Strong, simple cards */
.sms-cards .sms-cards__item,
.sms-cards.sms-tone-white .sms-cards__item { border-radius: 1.5rem; background: #ffffff; box-shadow: inset 0 0 0 1.5px var(--sms-line); transition: transform 0.4s var(--sms-kin-ease), box-shadow 0.3s; }
.sms-cards .sms-cards__item:hover { box-shadow: inset 0 0 0 2px var(--sms-navy); transform: translateY(-4px); }
.sms-cards .sms-cards__icon,
.sms-cards.sms-tone-white .sms-cards__icon { border-radius: 0.9rem; background: var(--sms-navy); color: var(--sms-green-on-navy); }
.sms-cards .sms-cards__item:hover .sms-cards__icon { transform: rotate(-6deg); }
.sms-cards .sms-cards__num { color: var(--sms-navy); font-size: 2.75rem; font-weight: 800; font-stretch: 84%; }
.sms-cards .sms-cards__name { font-size: clamp(1.3rem, 1.15rem + 0.6vw, 1.65rem); font-weight: 750; font-stretch: 88%; line-height: 1.12; letter-spacing: -0.01em; }
.sms-cards .sms-cards__meta,
.sms-cards.sms-tone-white .sms-cards__meta { background: var(--sms-pale-2); }
.sms-cards .sms-cards__link { color: var(--sms-navy); text-decoration: underline; text-decoration-color: var(--sms-green); text-decoration-thickness: 2px; text-underline-offset: 5px; }

/* Feature: angled photo crop */
.sms-feature .sms-feature__frame { aspect-ratio: 4 / 3.6; border-radius: 0; box-shadow: none; clip-path: polygon(10% 0, 100% 0, 100% 100%, 0 100%); }
.sms-feature.sms-feature--flip .sms-feature__frame { clip-path: polygon(0 0, 90% 0, 100% 100%, 0 100%); }
.sms-feature .sms-feature__blob { right: -3%; bottom: -5%; width: 60%; border-radius: 0; background: var(--sms-mint); clip-path: polygon(16% 0, 100% 0, 100% 100%, 0 100%); animation: none; }
.sms-feature.sms-feature--flip .sms-feature__blob { left: -3%; clip-path: polygon(0 0, 84% 0, 100% 100%, 0 100%); }
.sms-feature .sms-feature__lead { font-size: clamp(1.15rem, 1.05rem + 0.4vw, 1.35rem); }
.sms-feature .sms-feature__strap { background: var(--sms-navy); color: #ffffff; }
.sms-feature .sms-feature__strap-icon { color: var(--sms-green-on-navy); }
.sms-feature .sms-feature__chips-title { font-size: 1.1rem; font-weight: 750; }
.sms-page .sms-chips__item,
.sms-feature.sms-tone-white .sms-chips__item { background: #ffffff; box-shadow: inset 0 0 0 1.5px var(--sms-line); }
.sms-page .sms-chips__icon { background: var(--sms-navy); color: var(--sms-green-on-navy); }
.sms-feature .sms-watermark,
.sms-cards .sms-watermark,
.sms-steps .sms-watermark,
.sms-quotes .sms-watermark,
.sms-people .sms-watermark,
.sms-claim .sms-watermark,
.sms-checklist .sms-watermark { display: none; }

/* Steps: navy tiles and a bold green line */
.sms-steps .sms-steps__badge { border-radius: 1rem; background: var(--sms-navy); color: var(--sms-green-on-navy); }
.sms-steps .sms-steps__num { background: var(--sms-green); }
.sms-steps .sms-steps__line { background: var(--sms-line); }
.sms-steps .sms-steps__name { font-size: 1.25rem; font-weight: 750; font-stretch: 90%; line-height: 1.2; }
.sms-steps .sms-steps__note { box-shadow: inset 0 0 0 1.5px var(--sms-line); }

/* Checklist */
.sms-checklist .sms-checklist__item { background: #ffffff; box-shadow: inset 0 0 0 1.5px var(--sms-line); font-size: 1.1rem; font-weight: 650; line-height: 1.35; }
.sms-checklist .sms-checklist__icon { border-radius: 0.9rem; background: var(--sms-navy); color: var(--sms-green-on-navy); }

/* Notice */
.sms-notice .sms-notice__box { box-shadow: inset 0 0 0 2px var(--sms-navy); }
.sms-notice .sms-notice__badge { border-radius: 1rem; background: var(--sms-navy); color: var(--sms-green-on-navy); }
.sms-notice .sms-notice__title { font-size: clamp(1.4rem, 1.2rem + 0.8vw, 1.9rem); font-weight: 800; font-stretch: 85%; line-height: 1.1; }

/* FAQ: big ruled list */
.sms-faq .sms-faq__item,
.sms-faq.sms-tone-white .sms-faq__item { margin: 0; border-radius: 0; background: transparent; box-shadow: none; border-bottom: 1.5px solid var(--sms-line); }
.sms-faq .sms-faq__list > .sms-faq__item:first-child { border-top: 1.5px solid var(--sms-line); }
.sms-faq .sms-faq__q { padding: 1.35rem 3.5rem 1.35rem 0; font-size: clamp(1.1rem, 1.02rem + 0.35vw, 1.3rem); font-weight: 700; font-stretch: 92%; line-height: 1.3; }
.sms-faq .sms-faq__q::after { right: 0; background: var(--sms-navy); color: #ffffff; }
.sms-faq .sms-faq__q:hover { color: var(--sms-green); }
.sms-faq .sms-faq__a { padding: 0 3rem 1.4rem 0; }
.sms-faq .sms-faq__all-toggle { margin-top: 1.5rem; border-color: var(--sms-navy); }

/* Quotes */
.sms-quotes .sms-quotes__item { background: var(--sms-pale); }
.sms-quotes .sms-quotes__icon { border-radius: 0.9rem; background: var(--sms-navy); color: var(--sms-green-on-navy); }
.sms-quotes .sms-quotes__text { font-size: clamp(1.3rem, 1.1rem + 0.9vw, 1.9rem); font-weight: 600; font-stretch: 90%; line-height: 1.28; letter-spacing: -0.01em; }

/* People */
.sms-people .sms-people__frame { border-radius: 0; box-shadow: none; clip-path: polygon(8% 0, 100% 0, 100% 100%, 0 100%); }
.sms-people .sms-people__person,
.sms-people.sms-tone-white .sms-people__person { background: #ffffff; box-shadow: inset 0 0 0 1.5px var(--sms-line); }
.sms-people .sms-people__role { background: var(--sms-navy); color: #ffffff; }
.sms-people .sms-people__name { font-size: clamp(1.6rem, 1.3rem + 1.2vw, 2.3rem); font-weight: 800; font-stretch: 82%; line-height: 1.05; }
.sms-people .sms-people__tags { color: var(--sms-green); }
.sms-people .sms-people__shared-title { font-size: clamp(1.5rem, 1.2rem + 1.2vw, 2.2rem); font-weight: 800; font-stretch: 85%; line-height: 1.1; }
.sms-people .sms-people__shared a:focus-visible,
.sms-people .sms-people__shared summary:focus-visible { outline-color: var(--sms-green-on-navy); }

/* Links */
.sms-links .sms-links__link { box-shadow: inset 0 0 0 1.5px var(--sms-line); }
.sms-links .sms-links__link:hover { box-shadow: inset 0 0 0 2px var(--sms-navy); }
.sms-links .sms-links__icon { border-radius: 0.9rem; background: var(--sms-navy); color: var(--sms-green-on-navy); }
.sms-links .sms-links__name { font-size: 1.4rem; font-weight: 800; font-stretch: 85%; line-height: 1.1; }
.sms-links .sms-links__go { color: var(--sms-navy); text-decoration: underline; text-decoration-color: var(--sms-green); text-decoration-thickness: 2px; text-underline-offset: 5px; }

/* Claim: giant type */
.sms-claim .sms-claim__icon,
.sms-claim.sms-tone-pale .sms-claim__icon { border-radius: 1rem; background: var(--sms-navy); color: var(--sms-green-on-navy); }
.sms-claim .sms-claim__text { max-width: 60rem; font-size: clamp(1.9rem, 1.2rem + 3vw, 3.9rem); font-weight: 800; font-stretch: 80%; line-height: 1.02; letter-spacing: -0.025em; }

/* Contact */
.sms-contact .sms-contact__detail { background: #ffffff; box-shadow: inset 0 0 0 1.5px var(--sms-line); }
.sms-contact .sms-contact__icon { border-radius: 0.8rem; background: var(--sms-navy); color: var(--sms-green-on-navy); }
.sms-contact .sms-contact__value { font-size: clamp(1.2rem, 1.05rem + 0.6vw, 1.5rem); font-weight: 800; font-stretch: 90%; }
.sms-contact .sms-contact__form { box-shadow: inset 0 0 0 2px var(--sms-navy); }
.sms-contact .sms-contact__form-title { font-size: clamp(1.4rem, 1.2rem + 0.8vw, 1.9rem); font-weight: 800; font-stretch: 85%; line-height: 1.1; }
.sms-contact .sms-contact__booklink { background: var(--sms-pale); }

/* Booking wizard */
.sms-booking .sms-booking__form { box-shadow: inset 0 0 0 2px var(--sms-navy); }
.sms-booking .sms-booking__step-title { font-size: clamp(1.8rem, 1.3rem + 2vw, 3rem); font-weight: 800; font-stretch: 80%; line-height: 1; letter-spacing: -0.02em; }
.sms-booking .sms-booking__service-card { border-width: 1.5px; }
.sms-booking .sms-booking__service-input:checked + .sms-booking__service-card { border-color: var(--sms-navy); box-shadow: inset 0 0 0 1px var(--sms-navy); background: var(--sms-pale); }
.sms-booking .sms-booking__service-icon { border-radius: 0.9rem; background: var(--sms-navy); color: var(--sms-green-on-navy); }
.sms-booking .sms-booking__service-name { font-size: 1.15rem; font-weight: 750; }
.sms-booking .sms-booking__help { background: var(--sms-mint); }
.sms-booking .sms-booking__done-title { font-weight: 800; font-stretch: 85%; }
.sms-booking .sms-booking__summary a:focus-visible { outline-color: var(--sms-green-on-navy); }

/* ---------- Inner page hero: very large line-reveal title, angled photo ---------- */
.sms-kinpage { position: relative; overflow: hidden; padding: clamp(2.25rem, 1.5rem + 3vw, 4.5rem) 0 clamp(3rem, 2rem + 4vw, 6rem); }
.sms-kinpage .sms-kinpage__inner { display: grid; gap: clamp(2.25rem, 1.5rem + 3vw, 4rem); align-items: center; width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-kinpage .sms-kinpage__copy { min-width: 0; }
.sms-kinpage .sms-kinpage__crumb { margin-bottom: 1.5rem; color: var(--sms-ink-soft); font-size: 0.9rem; font-weight: 600; animation: sms-kin-fade 0.8s var(--sms-kin-ease) 0.05s both; }
.sms-kinpage .sms-kinpage__crumb-link { color: var(--sms-navy); text-decoration-color: var(--sms-green); text-decoration-thickness: 2px; text-underline-offset: 4px; }
.sms-kinpage .sms-kinpage__eyebrow { animation: sms-kin-fade 0.8s var(--sms-kin-ease) 0.12s both; }
.sms-kinpage .sms-kinpage__title { margin: 0 0 1.5rem; color: var(--sms-navy); font-size: clamp(2.7rem, 1.5rem + 5vw, 6.4rem); font-weight: 800; font-stretch: 85%; line-height: 0.92; letter-spacing: -0.01em; }
.sms-kinpage .sms-kinpage__m { display: inline-block; overflow: hidden; vertical-align: top; padding: 0 0.03em 0.12em; margin: 0 -0.03em -0.12em; }
.sms-kinpage .sms-kinpage__w { display: inline-block; animation: sms-kin-rise 1s var(--sms-kin-ease) both; animation-delay: calc(0.12s + var(--i, 0) * 0.07s); }
.sms-kinpage .sms-kinpage__sub { margin-bottom: 0.6rem; color: var(--sms-green); font-size: 1.15rem; font-weight: 700; }
.sms-kinpage .sms-kinpage__lead { max-width: 36rem; color: var(--sms-ink-soft); font-size: clamp(1.1rem, 1.02rem + 0.35vw, 1.3rem); line-height: 1.55; animation: sms-kin-fade 0.9s var(--sms-kin-ease) 0.45s both; }
.sms-kinpage .sms-kinpage__lead p { margin: 0 0 0.75rem; }
.sms-kinpage .sms-kinpage__actions { display: flex; flex-wrap: wrap; gap: 0.75rem; margin-top: 1.75rem; animation: sms-kin-fade 0.9s var(--sms-kin-ease) 0.55s both; }
.sms-kinpage .sms-kinpage__media { position: relative; z-index: 0; min-width: 0; width: 100%; max-width: 34rem; justify-self: center; }
.sms-kinpage .sms-kinpage__slab { position: absolute; z-index: -1; left: 22%; right: -6%; top: 8%; bottom: -6%; background: var(--sms-mint); clip-path: polygon(16% 0, 100% 0, 100% 100%, 0 100%); }
.sms-kinpage .sms-kinpage__frame { aspect-ratio: 4 / 4.3; border-radius: 0; background: var(--sms-pale); clip-path: polygon(14% 0, 100% 0, 100% 100%, 0 100%); }
.sms-kinpage .sms-kinpage__chips { display: flex; flex-wrap: wrap; gap: 0.5rem; margin: 1rem 0 0; padding: 0; list-style: none; }
.sms-kinpage .sms-kinpage__chip { display: inline-flex; align-items: center; gap: 0.5rem; min-width: 0; padding: 0.55rem 1rem 0.55rem 0.6rem; border-radius: 999px; background: var(--sms-navy); color: #ffffff; font-size: 0.9375rem; font-weight: 650; line-height: 1.3; }
.sms-kinpage .sms-kinpage__chip-icon { width: 1.6rem; height: 1.6rem; padding: 0.3rem; border-radius: 50%; background: rgba(130, 208, 110, 0.16); color: var(--sms-green-on-navy); }
.sms-kinpage .sms-kinpage__chip-text { min-width: 0; }
@media (min-width: 60em) {
  .sms-kinpage .sms-kinpage__inner { grid-template-columns: minmax(0, 1.2fr) minmax(0, 0.8fr); }
  .sms-kinpage .sms-kinpage__media { max-width: none; }
  .sms-kinpage .sms-kinpage__chips { position: absolute; left: -1.5rem; bottom: 1.5rem; flex-direction: column; align-items: flex-start; max-width: 80%; margin: 0; }
}

/* ---------- CTA: a big typographic band ---------- */
.sms-kinband { position: relative; overflow: hidden; padding: clamp(4rem, 2.5rem + 6vw, 8.5rem) 0; background: var(--sms-mint); }
.sms-kinband .sms-kinband__inner { width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-kinband .sms-kinband__title { max-width: 16ch; margin: 0 0 clamp(1.5rem, 1rem + 2vw, 2.5rem); color: var(--sms-navy); font-size: clamp(2.7rem, 1.3rem + 6vw, 7.5rem); font-weight: 800; font-stretch: 84%; line-height: 0.9; letter-spacing: -0.012em; }
.sms-kinband .sms-kinband__row { display: grid; gap: 1.5rem; align-items: end; }
.sms-kinband .sms-kinband__text { max-width: 38rem; min-width: 0; color: var(--sms-navy); font-size: clamp(1.1rem, 1.02rem + 0.35vw, 1.3rem); line-height: 1.55; }
.sms-kinband .sms-kinband__text p { margin: 0; }
.sms-kinband .sms-kinband__actions { display: flex; flex-wrap: wrap; gap: 0.75rem; min-width: 0; }
.sms-kinband .sms-kinband__phone { display: inline-flex; flex-direction: column; gap: 0.35rem; margin-top: clamp(2rem, 1.5rem + 2vw, 3.5rem); padding-top: clamp(1.5rem, 1rem + 2vw, 2.5rem); border-top: 2px solid var(--sms-navy); color: var(--sms-navy); text-decoration: none; }
.sms-kinband .sms-kinband__phone-label { min-width: 0; font-size: 0.875rem; font-weight: 700; letter-spacing: 0.14em; text-transform: uppercase; }
.sms-kinband .sms-kinband__phone-num { position: relative; min-width: 0; font-size: clamp(2.4rem, 1.2rem + 5.2vw, 6.25rem); font-weight: 800; font-stretch: 85%; line-height: 1; letter-spacing: -0.02em; }
.sms-kinband .sms-kinband__phone-num::after { content: ""; position: absolute; left: 0; right: 0; bottom: -0.08em; height: 0.07em; background: var(--sms-green); transform: scaleX(0.25); transform-origin: left; transition: transform 0.6s var(--sms-kin-ease); }
.sms-kinband .sms-kinband__phone:hover .sms-kinband__phone-num::after,
.sms-kinband .sms-kinband__phone:focus-visible .sms-kinband__phone-num::after { transform: scaleX(1); }
@media (min-width: 60em) {
  .sms-kinband .sms-kinband__row { grid-template-columns: minmax(0, 1fr) auto; }
}

/* ---------- Home hero: the strapline, line by line ---------- */
.sms-kinhero { position: relative; overflow: hidden; padding: clamp(2rem, 1.25rem + 2.5vw, 3.5rem) 0 clamp(3rem, 2rem + 4vw, 5rem); }
.sms-kinhero .sms-kinhero__inner { display: grid; gap: clamp(2.5rem, 1.5rem + 4vw, 4rem); align-items: center; width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-kinhero .sms-kinhero__copy { min-width: 0; }
.sms-kinhero .sms-kinhero__eyebrow { animation: sms-kin-fade 0.8s var(--sms-kin-ease) 0.05s both; }
.sms-kinhero .sms-kinhero__title { margin: 0 0 clamp(1.5rem, 1rem + 2vw, 2.25rem); color: var(--sms-navy); font-size: clamp(3.4rem, 1.5rem + 11vw, 7.75rem); font-weight: 800; font-stretch: 84%; line-height: 0.86; letter-spacing: -0.012em; }
.sms-kinhero .sms-kinhero__line { display: block; overflow: hidden; padding: 0 0.04em 0.12em; margin: 0 -0.04em -0.12em; }
.sms-kinhero .sms-kinhero__word { display: inline-block; transform-origin: 0 100%; animation: sms-kin-rise 1.15s var(--sms-kin-ease) both; }
.sms-kinhero .sms-kinhero__line:nth-child(2) .sms-kinhero__word { animation-delay: 0.1s; }
.sms-kinhero .sms-kinhero__line:nth-child(3) .sms-kinhero__word { animation-delay: 0.2s; }
.sms-kinhero .sms-kinhero__line:nth-child(4) .sms-kinhero__word { animation-delay: 0.3s; }
.sms-kinhero .sms-kinhero__word--accent { color: var(--sms-green); }
.sms-kinhero .sms-kinhero__lead { max-width: 40rem; color: var(--sms-ink-soft); font-size: clamp(1.1rem, 1.02rem + 0.4vw, 1.35rem); line-height: 1.55; animation: sms-kin-fade 0.9s var(--sms-kin-ease) 0.5s both; }
.sms-kinhero .sms-kinhero__lead p { margin: 0 0 0.6rem; }
.sms-kinhero .sms-kinhero__lead strong { color: var(--sms-navy); font-weight: 650; }
.sms-kinhero .sms-kinhero__actions { display: flex; flex-wrap: wrap; gap: 0.75rem; margin-top: 1.75rem; animation: sms-kin-fade 0.9s var(--sms-kin-ease) 0.6s both; }
.sms-kinhero .sms-kinhero__visual { position: relative; min-width: 0; width: min(78%, 25rem); justify-self: center; aspect-ratio: 14 / 17; animation: sms-kin-fade 1.1s var(--sms-kin-ease) 0.35s both; }
.sms-kinhero .sms-kinhero__defs { position: absolute; width: 0; height: 0; overflow: hidden; }
.sms-kinhero .sms-kinhero__back { position: absolute; inset: 0; color: var(--sms-mint); transform: translate(7%, 5%); }
.sms-kinhero .sms-kinhero__back-svg { display: block; width: 100%; height: 100%; }
.sms-kinhero .sms-kinhero__shield { position: absolute; inset: 0; overflow: hidden; background: var(--sms-navy); -webkit-clip-path: url(#sms-kin-shield); clip-path: url(#sms-kin-shield); }
.sms-kinhero .sms-kinhero__img { position: absolute; left: -12%; top: -6%; display: block; width: 124%; height: 112%; object-fit: cover; animation: sms-kin-pan 24s ease-in-out infinite alternate; }
.sms-kinhero .sms-kinhero__ring { position: absolute; left: -14%; bottom: 4%; width: 38%; aspect-ratio: 1; border-radius: 50%; background: #ffffff; color: var(--sms-navy); box-shadow: 0 0 0 1.5px var(--sms-line); }
.sms-kinhero .sms-kinhero__ring-svg { display: block; width: 100%; height: 100%; animation: sms-spin 36s linear infinite; }
.sms-kinhero .sms-kinhero__ring-text { fill: currentColor; font-size: 15.5px; font-weight: 700; letter-spacing: 0.12em; text-transform: uppercase; }
.sms-kinhero .sms-kinhero__ring-icon { position: absolute; left: 50%; top: 50%; width: 34%; height: 34%; margin: -17% 0 0 -17%; color: var(--sms-green); }
@media (min-width: 60em) {
  .sms-kinhero .sms-kinhero__inner { grid-template-columns: minmax(0, 1.5fr) minmax(0, 0.62fr); }
  .sms-kinhero .sms-kinhero__visual { width: 100%; }
}
@keyframes sms-kin-rise { from { transform: translateY(108%) skewY(5deg); } to { transform: none; } }
@keyframes sms-kin-fade { from { opacity: 0; transform: translateY(22px); } to { opacity: 1; transform: none; } }
@keyframes sms-kin-pan { from { transform: translate3d(-5%, 2%, 0) scale(1.02); } to { transform: translate3d(5%, -3%, 0) scale(1.1); } }

/* ---------- Scroll-velocity marquee of the three services ---------- */
.sms-kindrift { position: relative; overflow: hidden; padding: clamp(1.5rem, 1rem + 1.5vw, 2.5rem) 0; border-top: 2px solid var(--sms-navy); border-bottom: 2px solid var(--sms-navy); }
.sms-kindrift .sms-kindrift__viewport { overflow: hidden; }
.sms-kindrift .sms-kindrift__track { display: flex; flex-wrap: wrap; justify-content: center; gap: 0.25rem 0; margin: 0; padding: 0 var(--sms-gutter); list-style: none; }
.sms-kindrift .sms-kindrift__item { display: inline-flex; align-items: center; min-width: 0; color: var(--sms-navy); font-size: clamp(1.9rem, 1rem + 3.6vw, 3.75rem); font-weight: 800; font-stretch: 84%; line-height: 1.05; letter-spacing: -0.02em; white-space: nowrap; }
.sms-kindrift .sms-kindrift__item::after { content: ""; flex: 0 0 auto; width: 0.2em; height: 0.2em; margin: 0 0.42em; border-radius: 50%; background: var(--sms-green); }
.sms-kindrift .sms-kindrift__item--outline { -webkit-text-fill-color: transparent; -webkit-text-stroke: max(1.5px, 0.018em) var(--sms-navy); }
.sms-kindrift .sms-kindrift__item--dup { display: none; }
.sms-kindrift:not(.is-live) .sms-kindrift__item:nth-child(3)::after { display: none; }
@media (max-width: 47.99em) {
  .sms-kindrift:not(.is-live) .sms-kindrift__item::after { display: none; }
}
.sms-kindrift .sms-kindrift__pause { display: none; }
.sms-kindrift.is-live .sms-kindrift__track { flex-wrap: nowrap; justify-content: flex-start; width: max-content; padding: 0; will-change: transform; }
.sms-kindrift.is-live .sms-kindrift__item { font-size: clamp(3rem, 1.3rem + 7.2vw, 8.75rem); line-height: 1.1; }
.sms-kindrift.is-live .sms-kindrift__item--dup { display: inline-flex; }
.sms-kindrift.is-live .sms-kindrift__pause { position: absolute; right: var(--sms-gutter); bottom: 0.5rem; display: inline-flex; align-items: center; gap: 0.4rem; padding: 0.3rem 0.75rem; border: 0; border-radius: 999px; background: #ffffff; box-shadow: inset 0 0 0 1.5px var(--sms-line); color: var(--sms-navy); cursor: pointer; font: inherit; font-size: 0.8125rem; font-weight: 700; }
.sms-kindrift .sms-kindrift__pause:hover { box-shadow: inset 0 0 0 1.5px var(--sms-navy); }

/* ---------- Services as stacking cards ---------- */
.sms-kinstack { position: relative; padding: var(--sms-section) 0; }
.sms-kinstack .sms-kinstack__inner { width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-kinstack .sms-kinstack__head { display: grid; gap: 1.25rem; align-items: end; margin-bottom: clamp(2rem, 1.5rem + 2.5vw, 4rem); }
.sms-kinstack .sms-kinstack__heading { min-width: 0; }
.sms-kinstack .sms-kinstack__title { margin: 0; color: var(--sms-navy); font-size: clamp(2.6rem, 1.4rem + 5.4vw, 7rem); font-weight: 800; font-stretch: 84%; line-height: 0.9; letter-spacing: -0.012em; }
.sms-kinstack .sms-kinstack__intro { max-width: 30rem; min-width: 0; color: var(--sms-ink-soft); font-size: 1.1rem; }
.sms-kinstack .sms-kinstack__intro p { margin: 0; }
.sms-kinstack .sms-kinstack__list { display: grid; gap: 1.25rem; margin: 0; padding: 0; list-style: none; view-timeline-name: --sms-kinstack; }
.sms-kinstack .sms-kinstack__item { min-width: 0; }
.sms-kinstack .sms-kinstack__card { position: relative; display: grid; overflow: hidden; border-radius: 2rem; background: var(--sms-pale); color: var(--sms-navy); transform-origin: 50% 0; }
.sms-kinstack .sms-kinstack__card::after { content: ""; position: absolute; inset: 0; z-index: 3; border-radius: inherit; background: var(--sms-navy); opacity: 0; pointer-events: none; }
.sms-kinstack .sms-kinstack__card--1 { background: var(--sms-navy); color: #ffffff; }
.sms-kinstack .sms-kinstack__card--2 { background: var(--sms-pale); box-shadow: inset 0 0 0 1.5px var(--sms-line); }
.sms-kinstack .sms-kinstack__card--3 { background: var(--sms-mint); }
.sms-kinstack .sms-kinstack__body { display: flex; flex-direction: column; min-width: 0; padding: clamp(1.5rem, 1rem + 2.5vw, 3.25rem); }
.sms-kinstack .sms-kinstack__top { display: flex; align-items: center; justify-content: space-between; gap: 1rem; min-width: 0; }
.sms-kinstack .sms-kinstack__num { min-width: 0; font-size: 0.9375rem; font-weight: 700; letter-spacing: 0.14em; }
.sms-kinstack .sms-kinstack__icon { width: 3.25rem; height: 3.25rem; padding: 0.75rem; border-radius: 1rem; background: var(--sms-navy); color: var(--sms-green-on-navy); }
.sms-kinstack .sms-kinstack__card--1 .sms-kinstack__icon { background: rgba(130, 208, 110, 0.16); }
.sms-kinstack .sms-kinstack__name { margin: clamp(1rem, 0.6rem + 1.5vw, 2rem) 0 1rem; font-size: clamp(2.5rem, 1.3rem + 4.4vw, 5.6rem); font-weight: 800; font-stretch: 84%; line-height: 0.9; letter-spacing: -0.012em; }
.sms-kinstack .sms-kinstack__text { max-width: 34rem; color: var(--sms-ink-soft); font-size: clamp(1.05rem, 1rem + 0.3vw, 1.2rem); line-height: 1.55; }
.sms-kinstack .sms-kinstack__card--1 .sms-kinstack__text { color: #c9d6e2; }
.sms-kinstack .sms-kinstack__card--3 .sms-kinstack__text { color: var(--sms-navy); }
.sms-kinstack .sms-kinstack__text p { margin: 0; }
.sms-kinstack .sms-kinstack__feats { display: grid; gap: 0.55rem 1.5rem; margin: 1.5rem 0 0; padding: 0; list-style: none; }
.sms-kinstack .sms-kinstack__feat { display: flex; align-items: flex-start; gap: 0.6rem; min-width: 0; font-size: 0.975rem; font-weight: 600; line-height: 1.4; }
.sms-kinstack .sms-kinstack__feat-icon { width: 1.25rem; height: 1.25rem; margin-top: 0.05rem; color: var(--sms-green); }
.sms-kinstack .sms-kinstack__card--1 .sms-kinstack__feat-icon { color: var(--sms-green-on-navy); }
.sms-kinstack .sms-kinstack__card--3 .sms-kinstack__feat-icon { color: var(--sms-navy); }
.sms-kinstack .sms-kinstack__feat-text { min-width: 0; }
.sms-kinstack .sms-kinstack__actions { display: flex; flex-wrap: wrap; gap: 0.75rem; margin-top: auto; padding-top: 1.75rem; }
.sms-kinstack .sms-kinstack__card--1 .sms-btn--outline { border-color: #ffffff; color: #ffffff; }
.sms-kinstack .sms-kinstack__card--1 .sms-btn--outline:hover { background: #ffffff; color: var(--sms-navy); }
.sms-kinstack .sms-kinstack__card--1 .sms-btn--primary:hover { border-color: #ffffff; background: #ffffff; color: var(--sms-navy); }
.sms-kinstack .sms-kinstack__card--1 a:focus-visible { outline-color: var(--sms-green-on-navy); }
.sms-kinstack .sms-kinstack__media { position: relative; order: -1; min-width: 0; aspect-ratio: 16 / 10; }
.sms-kinstack .sms-kinstack__frame { position: absolute; inset: 0.75rem 0.75rem 0; border-radius: 1.4rem; }
@media (min-width: 40em) {
  .sms-kinstack .sms-kinstack__feats { grid-template-columns: repeat(2, minmax(0, 1fr)); }
}
@media (min-width: 60em) {
  .sms-kinstack .sms-kinstack__head { grid-template-columns: minmax(0, 1.3fr) minmax(0, 0.7fr); }
  .sms-kinstack .sms-kinstack__intro { justify-self: end; }
  .sms-kinstack .sms-kinstack__card { grid-template-columns: minmax(0, 1.2fr) minmax(0, 0.8fr); }
  .sms-kinstack .sms-kinstack__media { order: 0; aspect-ratio: auto; min-height: 24rem; }
  .sms-kinstack .sms-kinstack__frame { inset: 0.85rem; }
}
@media (min-width: 60em) and (min-height: 46em) {
  .sms-kinstack .sms-kinstack__list { gap: 0; }
  .sms-kinstack .sms-kinstack__item { position: sticky; top: calc(6.25rem + var(--i, 0) * 1.6rem); padding-bottom: 8vh; }
  .sms-kinstack .sms-kinstack__item:last-child { padding-bottom: 0; }
  .sms-kinstack .sms-kinstack__card { height: min(41rem, calc(100vh - 11.5rem)); }
}
@supports (animation-timeline: view()) {
  @media (min-width: 60em) and (min-height: 46em) {
    @keyframes sms-kin-shrink { to { transform: scale(0.92); } }
    @keyframes sms-kin-dim { to { opacity: 0.32; } }
    .sms-kinstack .sms-kinstack__card { animation: sms-kin-shrink linear both; animation-timeline: --sms-kinstack; animation-range: exit-crossing calc(var(--i, 0) / 3 * 100%) exit-crossing calc((var(--i, 0) + 1) / 3 * 100%); }
    .sms-kinstack .sms-kinstack__card::after { animation: sms-kin-dim linear both; animation-timeline: --sms-kinstack; animation-range: exit-crossing calc(var(--i, 0) / 3 * 100%) exit-crossing calc((var(--i, 0) + 1) / 3 * 100%); }
    .sms-kinstack .sms-kinstack__card--1::after { background: #000000; }
    .sms-kinstack .sms-kinstack__item:last-child .sms-kinstack__card,
    .sms-kinstack .sms-kinstack__item:last-child .sms-kinstack__card::after { animation: none; }
  }
}

/* ---------- Careers and Recruitment: the smaller pair ---------- */
.sms-kinpair { padding: 0 0 var(--sms-section); }
.sms-kinpair .sms-kinpair__inner { width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-kinpair .sms-kinpair__title { margin: 0 0 1.5rem; color: var(--sms-navy); font-size: clamp(1.8rem, 1.3rem + 2vw, 2.75rem); font-weight: 800; font-stretch: 80%; line-height: 1; letter-spacing: -0.02em; }
.sms-kinpair .sms-kinpair__grid { display: grid; gap: 1rem; margin: 0; padding: 0; list-style: none; }
.sms-kinpair .sms-kinpair__item { min-width: 0; }
.sms-kinpair .sms-kinpair__link { display: grid; grid-template-columns: minmax(0, 1fr) auto; gap: 0.75rem 1.5rem; align-items: end; height: 100%; padding: clamp(1.5rem, 1rem + 2vw, 2.5rem); border-radius: 1.75rem; box-shadow: inset 0 0 0 2px var(--sms-navy); color: var(--sms-navy); text-decoration: none; transition: background-color 0.35s, color 0.35s; }
.sms-kinpair .sms-kinpair__body { min-width: 0; }
.sms-kinpair .sms-kinpair__kicker { display: block; margin-bottom: 0.5rem; color: var(--sms-green); font-size: 0.8125rem; font-weight: 700; letter-spacing: 0.14em; text-transform: uppercase; }
.sms-kinpair .sms-kinpair__name { display: block; margin-bottom: 0.75rem; font-size: clamp(1.8rem, 1.2rem + 2.4vw, 3.1rem); font-weight: 800; font-stretch: 85%; line-height: 0.95; letter-spacing: -0.025em; transition: transform 0.5s var(--sms-kin-ease); }
.sms-kinpair .sms-kinpair__text { display: block; max-width: 30rem; color: var(--sms-ink-soft); }
.sms-kinpair .sms-kinpair__go { display: block; margin-top: 1rem; font-weight: 700; text-decoration: underline; text-decoration-color: var(--sms-green); text-decoration-thickness: 2px; text-underline-offset: 5px; }
.sms-kinpair .sms-kinpair__arrow { display: grid; place-items: center; width: 3.5rem; height: 3.5rem; min-width: 0; border-radius: 50%; background: var(--sms-navy); color: #ffffff; transition: transform 0.5s var(--sms-kin-ease); }
.sms-kinpair .sms-kinpair__arrow-icon { width: 1.35rem; height: 1.35rem; }
.sms-kinpair .sms-kinpair__link:hover,
.sms-kinpair .sms-kinpair__link:focus-visible { background: var(--sms-navy); color: #ffffff; }
.sms-kinpair .sms-kinpair__link:hover .sms-kinpair__text,
.sms-kinpair .sms-kinpair__link:focus-visible .sms-kinpair__text { color: #c9d6e2; }
.sms-kinpair .sms-kinpair__link:hover .sms-kinpair__kicker,
.sms-kinpair .sms-kinpair__link:focus-visible .sms-kinpair__kicker { color: var(--sms-green-on-navy); }
.sms-kinpair .sms-kinpair__link:hover .sms-kinpair__name { transform: translateX(0.5rem); }
.sms-kinpair .sms-kinpair__link:hover .sms-kinpair__arrow,
.sms-kinpair .sms-kinpair__link:focus-visible .sms-kinpair__arrow { background: var(--sms-green); transform: rotate(-45deg); }
@media (min-width: 52em) {
  .sms-kinpair .sms-kinpair__grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
}

/* ---------- Navy spotlight: a soft light follows the pointer ---------- */
.sms-kinspot { position: relative; overflow: hidden; padding: var(--sms-section) 0; background: var(--sms-navy); color: #ffffff; }
.sms-kinspot .sms-kinspot__light { position: absolute; left: 72%; top: 28%; z-index: 0; width: 56rem; height: 56rem; margin: -28rem 0 0 -28rem; border-radius: 50%; background: radial-gradient(circle, rgba(130, 208, 110, 0.22), rgba(130, 208, 110, 0.07) 38%, rgba(130, 208, 110, 0) 66%); pointer-events: none; }
.sms-kinspot.is-live .sms-kinspot__light { left: 0; top: 0; opacity: 0; transition: opacity 0.6s; }
.sms-kinspot.is-live.is-lit .sms-kinspot__light { opacity: 1; }
.sms-kinspot .sms-kinspot__inner { position: relative; z-index: 1; width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-kinspot .sms-kinspot__eyebrow { display: inline-flex; align-items: center; gap: 0.6rem; margin-bottom: 1.25rem; color: var(--sms-green-on-navy); font-size: 0.8125rem; font-weight: 700; letter-spacing: 0.14em; text-transform: uppercase; }
.sms-kinspot .sms-kinspot__eyebrow::before { content: ""; width: 0.55rem; height: 0.55rem; border-radius: 50%; background: currentColor; }
.sms-kinspot .sms-kinspot__title { margin: 0 0 clamp(2rem, 1.5rem + 3vw, 4rem); color: #ffffff; font-size: clamp(2.9rem, 1.2rem + 7.4vw, 9rem); font-weight: 800; font-stretch: 84%; line-height: 0.88; letter-spacing: -0.012em; }
.sms-kinspot .sms-kinspot__w { display: inline-grid; }
.sms-kinspot .sms-kinspot__w::after { content: attr(data-text); grid-area: 1 / 1; font-weight: 800; visibility: hidden; }
.sms-kinspot .sms-kinspot__wt { grid-area: 1 / 1; min-width: 0; }
.sms-kinspot .sms-mark { color: var(--sms-green-on-navy); }
.sms-kinspot .sms-kinspot__grid { display: grid; gap: clamp(2rem, 1.5rem + 3vw, 4.5rem); }
.sms-kinspot .sms-kinspot__main { min-width: 0; }
.sms-kinspot .sms-kinspot__lead { max-width: 38rem; color: #dbe5ee; font-size: clamp(1.1rem, 1.02rem + 0.4vw, 1.35rem); line-height: 1.55; }
.sms-kinspot .sms-kinspot__lead p { margin: 0; }
.sms-kinspot .sms-more__toggle { color: var(--sms-green-on-navy); }
.sms-kinspot .sms-more__body { color: #dbe5ee; }
.sms-kinspot .sms-kinspot__quote { margin: 2rem 0 0; padding: 1.5rem 0 0 1.5rem; border-left: 3px solid var(--sms-green-on-navy); }
.sms-kinspot .sms-kinspot__quote-text { margin: 0; color: #ffffff; font-size: clamp(1.15rem, 1.05rem + 0.5vw, 1.45rem); font-weight: 600; line-height: 1.45; }
.sms-kinspot .sms-kinspot__quote-text p { margin: 0; }
.sms-kinspot .sms-kinspot__cite { display: block; margin-top: 0.85rem; color: var(--sms-green-on-navy); font-size: 0.9375rem; font-weight: 700; }
.sms-kinspot .sms-kinspot__actions { display: flex; flex-wrap: wrap; gap: 0.75rem; margin-top: 2rem; }
.sms-kinspot .sms-btn--outline { border-color: #ffffff; color: #ffffff; }
.sms-kinspot .sms-btn--outline:hover { background: #ffffff; color: var(--sms-navy); }
.sms-kinspot a:focus-visible,
.sms-kinspot summary:focus-visible { outline-color: var(--sms-green-on-navy); }
.sms-kinspot .sms-kinspot__points { display: grid; gap: 0; align-content: start; min-width: 0; margin: 0; padding: 0; border-top: 1px solid rgba(255, 255, 255, 0.18); list-style: none; }
.sms-kinspot .sms-kinspot__point { display: grid; grid-template-columns: 2.75rem minmax(0, 1fr); gap: 1rem; min-width: 0; padding: 1.35rem 0; border-bottom: 1px solid rgba(255, 255, 255, 0.18); }
.sms-kinspot .sms-kinspot__point-icon { width: 2.75rem; height: 2.75rem; padding: 0.6rem; border-radius: 0.85rem; background: rgba(130, 208, 110, 0.14); color: var(--sms-green-on-navy); }
.sms-kinspot .sms-kinspot__point-body { min-width: 0; }
.sms-kinspot .sms-kinspot__point-title { margin: 0 0 0.25rem; color: #ffffff; font-size: 1.3rem; font-weight: 750; font-stretch: 88%; line-height: 1.2; }
.sms-kinspot .sms-kinspot__point-text { color: #c9d6e2; }
.sms-kinspot .sms-kinspot__point-text p { margin: 0; }
@media (min-width: 60em) {
  .sms-kinspot .sms-kinspot__grid { grid-template-columns: minmax(0, 1.1fr) minmax(0, 0.9fr); }
}
@supports (animation-timeline: view()) {
  @keyframes sms-kin-weigh { from { font-weight: 250; } to { font-weight: 800; } }
  .sms-kinspot .sms-kinspot__wt { animation: sms-kin-weigh linear both; animation-timeline: view(); animation-range: entry 70% cover 48%; }
}

/* ---------- Who we work with: a kinetic word wall ---------- */
.sms-kinwall { padding: var(--sms-section) 0; }
.sms-kinwall .sms-kinwall__inner { width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-kinwall .sms-kinwall__head { max-width: 46rem; margin: 0 auto clamp(2rem, 1.5rem + 2vw, 3.5rem); text-align: center; }
.sms-kinwall .sms-kinwall__title { margin: 0; color: var(--sms-navy); font-size: clamp(1.9rem, 1.3rem + 2.4vw, 3.25rem); font-weight: 800; font-stretch: 80%; line-height: 1; letter-spacing: -0.02em; }
.sms-kinwall .sms-kinwall__list { display: flex; flex-wrap: wrap; justify-content: center; align-items: baseline; gap: 0.15em 0.5em; margin: 0; padding: 0; list-style: none; color: var(--sms-navy); font-size: clamp(2rem, 1rem + 4.2vw, 5.4rem); line-height: 1.02; letter-spacing: -0.025em; }
.sms-kinwall .sms-kinwall__item { min-width: 0; max-width: 100%; text-align: center; }
.sms-kinwall .sms-kinwall__item--m { font-size: 0.62em; }
.sms-kinwall .sms-kinwall__item--l { font-size: 0.8em; }
.sms-kinwall .sms-kinwall__item--green { color: var(--sms-green); }
.sms-kinwall .sms-kinwall__word,
.sms-kinvalues .sms-kinwall__word { display: inline-grid; max-width: 100%; }
.sms-kinwall .sms-kinwall__word::after,
.sms-kinvalues .sms-kinwall__word::after { content: attr(data-text); grid-area: 1 / 1; height: 0; overflow: hidden; font-weight: 800; font-stretch: var(--sms-s, 100%); visibility: hidden; }
.sms-kinwall .sms-kinwall__txt,
.sms-kinvalues .sms-kinwall__txt { grid-area: 1 / 1; justify-self: center; min-width: 0; transition: font-weight 0.5s var(--sms-kin-ease); }
.sms-kinwall .sms-kinwall__note { margin: clamp(2rem, 1.5rem + 2vw, 3rem) 0 0; color: var(--sms-ink-soft); font-size: 0.9375rem; text-align: center; }

/* ---------- Medical Training: a giant hover list of courses ---------- */
.sms-kincourse { padding: var(--sms-section) 0; }
.sms-kincourse .sms-kincourse__inner { width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-kincourse .sms-kincourse__head { display: grid; gap: 1.25rem; align-items: end; margin-bottom: clamp(2rem, 1.5rem + 2vw, 3.5rem); }
.sms-kincourse .sms-kincourse__heading { min-width: 0; }
.sms-kincourse .sms-kincourse__title { margin: 0; color: var(--sms-navy); font-size: var(--sms-step-2); font-weight: 800; font-stretch: 80%; line-height: 0.98; letter-spacing: -0.025em; }
.sms-kincourse .sms-kincourse__lead { max-width: 28rem; min-width: 0; color: var(--sms-ink-soft); font-size: 1.1rem; }
.sms-kincourse .sms-kincourse__lead p { margin: 0; }
.sms-kincourse .sms-kincourse__list { margin: 0; padding: 0; border-top: 2px solid var(--sms-navy); list-style: none; }
.sms-kincourse .sms-kincourse__item { min-width: 0; border-bottom: 1.5px solid var(--sms-line); }
.sms-kincourse .sms-kincourse__link { position: relative; display: grid; grid-template-columns: 2.25rem minmax(0, 1fr); gap: 0.4rem 1rem; align-items: baseline; padding: clamp(1.1rem, 0.8rem + 1vw, 1.6rem) 0; color: var(--sms-navy); text-decoration: none; }
.sms-kincourse .sms-kincourse__num { min-width: 0; color: var(--sms-green); font-size: 0.9375rem; font-weight: 700; letter-spacing: 0.1em; }
.sms-kincourse .sms-kincourse__name { display: grid; min-width: 0; font-size: clamp(1.75rem, 1rem + 3.4vw, 4.4rem); line-height: 0.98; letter-spacing: -0.025em; }
.sms-kincourse .sms-kincourse__name::after { content: attr(data-text); grid-area: 1 / 1; height: 0; overflow: hidden; font-weight: 800; font-stretch: 100%; visibility: hidden; }
.sms-kincourse .sms-kincourse__txt { grid-area: 1 / 1; min-width: 0; font-weight: 500; font-stretch: 85%; transition: font-weight 0.5s var(--sms-kin-ease), font-stretch 0.5s var(--sms-kin-ease), color 0.3s; }
.sms-kincourse .sms-kincourse__meta { grid-column: 2; display: grid; gap: 0.2rem; min-width: 0; color: var(--sms-ink-soft); font-size: 0.975rem; line-height: 1.45; transition: opacity 0.45s var(--sms-kin-ease), transform 0.45s var(--sms-kin-ease); }
.sms-kincourse .sms-kincourse__dur { display: inline-flex; align-items: flex-start; gap: 0.4rem; min-width: 0; color: var(--sms-navy); font-weight: 700; }
.sms-kincourse .sms-kincourse__dur-icon { width: 1.1rem; height: 1.1rem; margin-top: 0.12rem; color: var(--sms-green); }
.sms-kincourse .sms-kincourse__dur-text,
.sms-kincourse .sms-kincourse__extra { min-width: 0; }
.sms-kincourse .sms-kincourse__go { display: none; }
.sms-kincourse .sms-kincourse__link:hover .sms-kincourse__txt,
.sms-kincourse .sms-kincourse__link:focus-visible .sms-kincourse__txt { font-weight: 800; font-stretch: 100%; }
.sms-kincourse .sms-kincourse__foot { display: flex; flex-wrap: wrap; gap: 0.75rem; margin-top: 2rem; }
@media (min-width: 60em) {
  .sms-kincourse .sms-kincourse__head { grid-template-columns: minmax(0, 1.3fr) minmax(0, 0.7fr); }
  .sms-kincourse .sms-kincourse__lead { justify-self: end; }
  .sms-kincourse .sms-kincourse__link { grid-template-columns: 3.5rem minmax(0, 1fr) minmax(0, 17rem) 3.5rem; align-items: center; gap: 1.5rem; }
  .sms-kincourse .sms-kincourse__meta { grid-column: auto; }
  .sms-kincourse .sms-kincourse__go { display: grid; place-items: center; width: 3.25rem; height: 3.25rem; min-width: 0; border-radius: 50%; box-shadow: inset 0 0 0 1.5px var(--sms-line); color: var(--sms-navy); transition: transform 0.5s var(--sms-kin-ease), background-color 0.3s, color 0.3s; }
  .sms-kincourse .sms-kincourse__go-icon { width: 1.2rem; height: 1.2rem; }
  .sms-kincourse .sms-kincourse__link:hover .sms-kincourse__go,
  .sms-kincourse .sms-kincourse__link:focus-visible .sms-kincourse__go { background: var(--sms-navy); color: #ffffff; transform: rotate(-45deg); }
}
@media (min-width: 60em) and (hover: hover) and (pointer: fine) and (prefers-reduced-motion: no-preference) {
  .sms-kincourse .sms-kincourse__meta { opacity: 0; transform: translateX(-1rem); }
  .sms-kincourse .sms-kincourse__link:hover .sms-kincourse__meta,
  .sms-kincourse .sms-kincourse__link:focus-visible .sms-kincourse__meta { opacity: 1; transform: none; }
}

/* ---------- Recruitment: pathway as stacking cards with giant numbers ---------- */
.sms-kinpath { padding: var(--sms-section) 0; }
.sms-kinpath .sms-kinpath__inner { width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-kinpath .sms-kinpath__head { display: grid; gap: 1.25rem; align-items: end; margin-bottom: clamp(2rem, 1.5rem + 2.5vw, 3.5rem); }
.sms-kinpath .sms-kinpath__heading { min-width: 0; }
.sms-kinpath .sms-kinpath__title { margin: 0; color: var(--sms-navy); font-size: clamp(2.6rem, 1.4rem + 5vw, 6.5rem); font-weight: 800; font-stretch: 84%; line-height: 0.9; letter-spacing: -0.012em; }
.sms-kinpath .sms-kinpath__lead { max-width: 30rem; min-width: 0; color: var(--sms-ink-soft); font-size: 1.1rem; }
.sms-kinpath .sms-kinpath__lead p { margin: 0; }
.sms-kinpath .sms-kinpath__list { display: grid; gap: 1rem; margin: 0; padding: 0; list-style: none; view-timeline-name: --sms-kinpath; }
.sms-kinpath .sms-kinpath__item { min-width: 0; }
.sms-kinpath .sms-kinpath__card { position: relative; display: grid; grid-template-columns: auto minmax(0, 1fr); gap: 0.5rem clamp(1rem, 0.5rem + 2vw, 2.5rem); align-items: center; overflow: hidden; padding: clamp(1.25rem, 0.8rem + 2vw, 2.75rem) clamp(1.25rem, 0.8rem + 2.5vw, 3.25rem); border-radius: 1.75rem; background: var(--sms-pale); color: var(--sms-navy); transform-origin: 50% 0; }
.sms-kinpath .sms-kinpath__card::after { content: ""; position: absolute; inset: 0; border-radius: inherit; background: var(--sms-navy); opacity: 0; pointer-events: none; }
.sms-kinpath .sms-kinpath__card--navy { background: var(--sms-navy); color: #ffffff; }
.sms-kinpath .sms-kinpath__card--mint { background: var(--sms-mint); }
.sms-kinpath .sms-kinpath__card--pale { background: var(--sms-pale); box-shadow: inset 0 0 0 1.5px var(--sms-line); }
.sms-kinpath .sms-kinpath__num { min-width: 0; color: var(--sms-green); font-size: clamp(4.5rem, 2.5rem + 9vw, 11rem); font-weight: 800; font-stretch: 84%; line-height: 0.8; letter-spacing: -0.05em; }
.sms-kinpath .sms-kinpath__card--navy .sms-kinpath__num { color: var(--sms-green-on-navy); }
.sms-kinpath .sms-kinpath__card--mint .sms-kinpath__num { color: var(--sms-navy); }
.sms-kinpath .sms-kinpath__body { display: grid; gap: 0.75rem; justify-items: start; min-width: 0; }
.sms-kinpath .sms-kinpath__icon { width: 2.75rem; height: 2.75rem; padding: 0.6rem; border-radius: 0.85rem; background: var(--sms-navy); color: var(--sms-green-on-navy); }
.sms-kinpath .sms-kinpath__card--navy .sms-kinpath__icon { background: rgba(130, 208, 110, 0.16); }
.sms-kinpath .sms-kinpath__name { margin: 0; font-size: clamp(1.6rem, 1rem + 2.8vw, 3.6rem); font-weight: 800; font-stretch: 80%; line-height: 0.98; letter-spacing: -0.025em; }
@media (min-width: 60em) {
  .sms-kinpath .sms-kinpath__head { grid-template-columns: minmax(0, 1.2fr) minmax(0, 0.8fr); }
  .sms-kinpath .sms-kinpath__lead { justify-self: end; }
}
@media (min-width: 60em) and (min-height: 40em) {
  .sms-kinpath .sms-kinpath__list { gap: 0; }
  .sms-kinpath .sms-kinpath__item { position: sticky; top: calc(6.25rem + var(--i, 0) * 1.1rem); padding-bottom: 12vh; }
  .sms-kinpath .sms-kinpath__item:last-child { padding-bottom: 0; }
  .sms-kinpath .sms-kinpath__card { min-height: 17rem; }
}
@supports (animation-timeline: view()) {
  @media (min-width: 60em) and (min-height: 40em) {
    .sms-kinpath .sms-kinpath__card { animation: sms-kin-shrink linear both; animation-timeline: --sms-kinpath; animation-range: exit-crossing calc(var(--i, 0) / 5 * 100%) exit-crossing calc((var(--i, 0) + 1) / 5 * 100%); }
    .sms-kinpath .sms-kinpath__card::after { animation: sms-kin-dim linear both; animation-timeline: --sms-kinpath; animation-range: exit-crossing calc(var(--i, 0) / 5 * 100%) exit-crossing calc((var(--i, 0) + 1) / 5 * 100%); }
    .sms-kinpath .sms-kinpath__card--navy::after { background: #000000; }
    .sms-kinpath .sms-kinpath__item:last-child .sms-kinpath__card,
    .sms-kinpath .sms-kinpath__item:last-child .sms-kinpath__card::after { animation: none; }
  }
}

.sms-kinstack .sms-kinstack__name,
.sms-kinstack .sms-kinstack__text,
.sms-kinstack .sms-kinstack__feats,
.sms-kinstack .sms-kinstack__actions,
.sms-kinpath .sms-kinpath__name,
.sms-kinvalues .sms-kinwall__word { min-width: 0; }

/* ---------- Recruitment: values as a kinetic word row ---------- */
.sms-kinvalues { padding: 0 0 var(--sms-section); }
.sms-kinvalues .sms-kinvalues__inner { width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: clamp(2.5rem, 1.5rem + 4vw, 5rem) var(--sms-gutter) 0; border-top: 2px solid var(--sms-navy); text-align: center; }
.sms-kinvalues .sms-kinvalues__list { display: flex; flex-wrap: wrap; justify-content: center; align-items: center; gap: 0.1em 0; margin: 0 0 clamp(1.5rem, 1rem + 2vw, 2.5rem); padding: 0; list-style: none; color: var(--sms-navy); font-size: clamp(2.4rem, 1rem + 6vw, 7.75rem); line-height: 1; letter-spacing: -0.01em; }
.sms-kinvalues .sms-kinvalues__item { display: inline-flex; align-items: center; min-width: 0; }
.sms-kinvalues .sms-kinvalues__item::after { content: ""; flex: 0 0 auto; width: 0.16em; height: 0.16em; margin: 0 0.35em; border-radius: 50%; background: var(--sms-green); }
.sms-kinvalues .sms-kinvalues__item:last-child::after { display: none; }
.sms-kinvalues .sms-kinvalues__item:nth-child(even) { color: var(--sms-green); }
.sms-kinvalues .sms-kinvalues__text { max-width: 44rem; margin: 0 auto; color: var(--sms-ink-soft); font-size: clamp(1.05rem, 1rem + 0.3vw, 1.2rem); }
.sms-kinvalues .sms-kinvalues__text p { margin: 0; }
.sms-kinvalues .sms-kinvalues__actions { display: flex; flex-wrap: wrap; justify-content: center; gap: 0.75rem; margin-top: 1.75rem; }

/* Drifting footer wordmark (scroll-driven, decorative) */
@supports (animation-timeline: view()) {
  @keyframes sms-kin-slide { from { transform: translateX(32%); } to { transform: none; } }
  .sms-kinsign .sms-kinsign__word { animation: sms-kin-slide linear both; animation-timeline: view(); animation-range: cover 0% cover 50%; }
}
"""

RISE = [".sms-kinpage .sms-kinpage__frame"]
ENTRANCE = []
REVEAL = [".sms-kinstack .sms-kinstack__head", ".sms-kinpair .sms-kinpair__item", ".sms-kinspot .sms-kinspot__grid",
          ".sms-kinwall .sms-kinwall__head", ".sms-kinband .sms-kinband__inner", ".sms-kincourse .sms-kincourse__head",
          ".sms-kincourse .sms-kincourse__item", ".sms-kinpath .sms-kinpath__head", ".sms-kinvalues .sms-kinvalues__inner"]
LOOP = [".sms-kinhero .sms-kinhero__word", ".sms-kinhero .sms-kinhero__eyebrow", ".sms-kinhero .sms-kinhero__lead", ".sms-kinhero .sms-kinhero__actions",
        ".sms-kinhero .sms-kinhero__visual", ".sms-kinhero .sms-kinhero__img", ".sms-kinhero .sms-kinhero__ring-svg",
        ".sms-kinpage .sms-kinpage__w", ".sms-kinpage .sms-kinpage__crumb", ".sms-kinpage .sms-kinpage__eyebrow", ".sms-kinpage .sms-kinpage__lead",
        ".sms-kinpage .sms-kinpage__actions", ".sms-kinstack .sms-kinstack__card", ".sms-kinstack .sms-kinstack__card::after",
        ".sms-kinpath .sms-kinpath__card", ".sms-kinpath .sms-kinpath__card::after", ".sms-kinspot .sms-kinspot__wt", ".sms-kinsign .sms-kinsign__word"]
TRANS = [".sms-kinband .sms-kinband__phone-num::after", ".sms-kinpair .sms-kinpair__link", ".sms-kinpair .sms-kinpair__name", ".sms-kinpair .sms-kinpair__arrow",
         ".sms-kinspot .sms-kinspot__light", ".sms-kinwall .sms-kinwall__txt", ".sms-kinvalues .sms-kinwall__txt", ".sms-kincourse .sms-kincourse__txt",
         ".sms-kincourse .sms-kincourse__meta", ".sms-kincourse .sms-kincourse__go"]

SKIP = {"medical-training": [0], "recruitment": [0, 1, 2]}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _segments(text):
    """[(piece, accented)] from text with [[accent]] marks."""
    out = []
    for part in re.split(r"(\[\[.+?\]\])", text):
        if not part:
            continue
        if part.startswith("[["):
            out.append((part[2:-2], True))
        else:
            out.append((part, False))
    return out


def reveal_words(text, block):
    """Each word in its own mask so the title slides up line by line."""
    out, i = [], 0
    for piece, accent in _segments(text):
        for w in piece.split():
            out.append('<span class="sms-%s__m"><span class="sms-%s__w%s" style="--i: %d">%s</span></span>' % (
                block, block, " sms-mark" if accent else "", i, e(w)))
            i += 1
    return " ".join(out)


def weigh_words(text):
    """Spotlight title: words that gain weight as they scroll into view (box reserved at full weight)."""
    out = []
    for piece, accent in _segments(text):
        for w in piece.split():
            out.append('<span class="sms-kinspot__w%s" data-text="%s"><span class="sms-kinspot__wt">%s</span></span>' % (
                " sms-mark" if accent else "", attr(w), e(w)))
    return " ".join(out)


def word(text, weight, stretch):
    """A wall word: the box is sized at full weight and width, so shifting the weight never reflows the wall."""
    return '<span class="sms-kinwall__word" data-text="%s" style="--sms-s: %d%%"><span class="sms-kinwall__txt" data-w="%d" style="font-weight: %d; font-stretch: %d%%">%s</span></span>' % (
        attr(text), stretch, weight, weight, stretch, e(text))


# ---------------------------------------------------------------------------
# Page hero, CTA band, chrome
# ---------------------------------------------------------------------------

def page_hero(ctx, h):
    crumb = '<div class="sms-kinpage__crumb"><a class="sms-kinpage__crumb-link" href="%s">Home</a> <span aria-hidden="true">/</span> %s</div>' % (ctx.href("home"), e(LABEL[ctx.slug]))
    sub = '<div class="sms-kinpage__sub">%s</div>' % e(h["sub"]) if h.get("sub") else ""
    acts = '<div class="sms-kinpage__actions">%s</div>' % buttons(ctx, h["buttons"]) if h.get("buttons") else ""
    chips_html = "".join('<li class="sms-kinpage__chip">%s<span class="sms-kinpage__chip-text">%s</span></li>' % (icon(ic, "sms-kinpage__chip-icon"), e(t)) for ic, t in h.get("chips", [])[:2])
    return """<section class="sms-kinpage">
  <div class="sms-kinpage__inner">
    <div class="sms-kinpage__copy">
      %s
      <div class="sms-kinpage__eyebrow">%s</div>
      <h1 class="sms-kinpage__title">%s</h1>
      <div class="sms-kinpage__lead">%s%s</div>
      %s
    </div>
    <div class="sms-kinpage__media">
      <div class="sms-kinpage__slab" aria-hidden="true"></div>
      %s
      <ul class="sms-kinpage__chips">%s</ul>
    </div>
  </div>
</section>
""" % (crumb, e(h["eyebrow"]), reveal_words(h["title"], "kinpage"), sub, paras(h["body"]), acts,
       photo(ctx, h["photo"], lazy=False, parallax=False, figcls="sms-kinpage__frame"), chips_html)


def cta(ctx, d):
    btns = [(l, t) for l, t in d["buttons"] if t != "tel"]
    return """<section class="sms-kinband">
  <div class="sms-kinband__inner">
    <h2 class="sms-kinband__title">%s</h2>
    <div class="sms-kinband__row">
      <div class="sms-kinband__text">%s</div>
      <div class="sms-kinband__actions">%s</div>
    </div>
    <a class="sms-kinband__phone" href="tel:%s"><span class="sms-kinband__phone-label">Or call us on</span><span class="sms-kinband__phone-num">%s</span></a>
  </div>
</section>
""" % (e(d["title"]), paras(d["text"]), buttons(ctx, btns) if btns else "", PHONE_TEL, PHONE)


def chrome_top(ctx):
    return header(ctx, "blue")


def chrome_bottom(ctx):
    return '<div class="sms-kinsign" aria-hidden="true"><span class="sms-kinsign__word">Streamline</span></div>\n' + footer(ctx, "white")


# ---------------------------------------------------------------------------
# Homepage sections
# ---------------------------------------------------------------------------
SHIELD_PATH = "M0.5,0 L1,0.13 L1,0.5 C1,0.77 0.79,0.93 0.5,1 C0.21,0.93 0,0.77 0,0.5 L0,0.13 Z"


def hero(ctx):
    lines = [("Protecting", False), ("People.", False), ("Supporting", True), ("Business.", True)]
    title = " ".join('<span class="sms-kinhero__line"><span class="sms-kinhero__word%s">%s</span></span>' % (" sms-kinhero__word--accent" if a else "", w) for w, a in lines)
    ring_words = "Skilled &#183; Proportionate &#183; Reliable &#183; "
    return """<section class="sms-kinhero">
  <div class="sms-kinhero__inner">
    <div class="sms-kinhero__copy">
      <div class="sms-kinhero__eyebrow">Clinician-led safety and medical support</div>
      <h1 class="sms-kinhero__title">%s</h1>
      <div class="sms-kinhero__lead"><p>%s</p><p><strong>%s</strong></p></div>
      <div class="sms-kinhero__actions">%s</div>
    </div>
    <div class="sms-kinhero__visual" aria-hidden="true">
      <svg class="sms-kinhero__defs" focusable="false" width="0" height="0"><defs><clipPath id="sms-kin-shield" clipPathUnits="objectBoundingBox"><path d="%s"/></clipPath></defs></svg>
      <div class="sms-kinhero__back"><svg class="sms-kinhero__back-svg" viewBox="0 0 1 1" preserveAspectRatio="none" focusable="false"><path d="%s" fill="currentColor"/></svg></div>
      <div class="sms-kinhero__shield">%s</div>
      <div class="sms-kinhero__ring">
        <svg class="sms-kinhero__ring-svg" viewBox="0 0 200 200" focusable="false"><defs><path id="sms-kin-circle" d="M100,100 m-74,0 a74,74 0 1,1 148,0 a74,74 0 1,1 -148,0"/></defs><text class="sms-kinhero__ring-text"><textPath href="#sms-kin-circle" textLength="462" lengthAdjust="spacing">%s</textPath></text></svg>
        %s
      </div>
    </div>
  </div>
</section>
""" % (title, e(C.INTRO2), e(C.AREA), buttons(ctx, [("Book online", "book"), ("Call 01283 358789", "tel")]),
       SHIELD_PATH, SHIELD_PATH, photo_img(ctx, "festival", "sms-kinhero__img", lazy=False, decorative=True), ring_words, icon("heart", "sms-kinhero__ring-icon"))


def drift(ctx):
    names = [s["title"] for s in C.SERVICES]
    items = ""
    for g in range(3):
        for i, n in enumerate(names):
            cls = "sms-kindrift__item" + (" sms-kindrift__item--outline" if i == 1 else "") + (" sms-kindrift__item--dup" if g else "")
            items += '<li class="%s"%s>%s</li>' % (cls, ' aria-hidden="true"' if g else "", e(n))
    return """<section class="sms-kindrift" aria-label="Our services" data-sms-drift="3">
  <div class="sms-kindrift__viewport"><ul class="sms-kindrift__track">%s</ul></div>
  <button class="sms-kindrift__pause" type="button" aria-pressed="false" data-sms-drift-toggle>Pause motion</button>
</section>
""" % items


def stack(ctx):
    cards = ""
    for i, s in enumerate(C.SERVICES):
        feats = "".join('<li class="sms-kinstack__feat">%s<span class="sms-kinstack__feat-text">%s</span></li>' % (icon("check", "sms-kinstack__feat-icon"), e(t)) for _, t in s["list"])
        cards += """<li class="sms-kinstack__item" style="--i: %d">
        <article class="sms-kinstack__card sms-kinstack__card--%d">
          <div class="sms-kinstack__body">
            <div class="sms-kinstack__top"><span class="sms-kinstack__num">%02d / %02d</span>%s</div>
            <h3 class="sms-kinstack__name">%s</h3>
            <div class="sms-kinstack__text"><p>%s</p></div>
            <ul class="sms-kinstack__feats">%s</ul>
            <div class="sms-kinstack__actions">%s</div>
          </div>
          <div class="sms-kinstack__media">%s</div>
        </article>
      </li>""" % (i, i + 1, i + 1, len(C.SERVICES), icon(s["icon"], "sms-kinstack__icon"), e(s["title"]), e(s["text"]), feats,
                  buttons(ctx, [(s["cta"], "book:" + s["key"]), ("Find out more", s["slug"])]), photo(ctx, s["photo"], figcls="sms-kinstack__frame"))
    return """<section class="sms-kinstack" id="services">
  <div class="sms-kinstack__inner">
    <div class="sms-kinstack__head">
      <div class="sms-kinstack__heading"><div class="sms-kinstack__eyebrow">Our Services</div><h2 class="sms-kinstack__title">What We <span class="sms-mark">Provide</span></h2></div>
      <div class="sms-kinstack__intro"><p>%s</p></div>
    </div>
    <ol class="sms-kinstack__list">%s</ol>
  </div>
</section>
""" % (e(C.INTRO), cards)


def pair(ctx):
    rec = C.PAGES["contact"]["sections"][1][1]["items"][3]
    items = [(C.CAREERS["slug"], "Career Support", C.CAREERS["title"], C.CAREERS["text"], C.CAREERS["cta"]),
             (rec["link"], "Recruitment", "Interested in Working With Us?", rec["text"], rec["go"])]
    lis = "".join("""<li class="sms-kinpair__item"><a class="sms-kinpair__link" href="%s">
        <span class="sms-kinpair__body"><span class="sms-kinpair__kicker">%s</span><span class="sms-kinpair__name">%s</span><span class="sms-kinpair__text">%s</span><span class="sms-kinpair__go">%s</span></span>
        <span class="sms-kinpair__arrow" aria-hidden="true">%s</span>
      </a></li>""" % (ctx.href(slug), e(k), e(n), e(t), e(go), icon("arrow", "sms-kinpair__arrow-icon")) for slug, k, n, t, go in items)
    return """<section class="sms-kinpair">
  <div class="sms-kinpair__inner">
    <h2 class="sms-kinpair__title">Careers &amp; Recruitment</h2>
    <ul class="sms-kinpair__grid">%s</ul>
  </div>
</section>
""" % lis


def spotlight(ctx):
    ctx.notes.append("Image-only copy used: \"Working With You, Not Simply For You.\" and Mathew's quote (working-with-you-not-simply-for-you.png)")
    pts = "".join('<li class="sms-kinspot__point">%s<div class="sms-kinspot__point-body"><h3 class="sms-kinspot__point-title">%s</h3><div class="sms-kinspot__point-text"><p>%s</p></div></div></li>' % (
        icon(ic, "sms-kinspot__point-icon"), e(t), e(x)) for ic, t, x in C.TRUST)
    return """<section class="sms-kinspot" id="why" data-sms-spot>
  <span class="sms-kinspot__light" aria-hidden="true"></span>
  <div class="sms-kinspot__inner">
    <div class="sms-kinspot__eyebrow">Why choose Streamline?</div>
    <h2 class="sms-kinspot__title">%s</h2>
    <div class="sms-kinspot__grid">
      <div class="sms-kinspot__main">
        <div class="sms-kinspot__lead"><p>%s</p></div>
        %s
        <figure class="sms-kinspot__quote"><blockquote class="sms-kinspot__quote-text"><p>%s</p></blockquote><figcaption class="sms-kinspot__cite">Mathew Stones, Director</figcaption></figure>
        <div class="sms-kinspot__actions">%s</div>
      </div>
      <ul class="sms-kinspot__points">%s</ul>
    </div>
  </div>
</section>
""" % (weigh_words(C.WORKING_WITH["title"]), e(C.WORKING_WITH["body"][0]), more(paras(C.WORKING_WITH["body"][1:])), e(C.MATHEW_QUOTE),
       buttons(ctx, [("Contact Streamline", "contact"), ("About Us", "about")]), pts)


WEIGHTS = [300, 800, 450, 700, 350, 600, 800, 400, 650, 300, 750]
STRETCH = [100, 75, 90, 80, 95, 75, 85, 100, 75, 90, 80]


def wall(ctx):
    lis = ""
    for i, w in enumerate(C.WHO):
        size = "" if len(w) <= 12 else (" sms-kinwall__item--l" if len(w) <= 18 else " sms-kinwall__item--m")
        tone_cls = " sms-kinwall__item--green" if i % 4 == 1 else ""
        lis += '<li class="sms-kinwall__item%s%s">%s</li>' % (size, tone_cls, word(w, WEIGHTS[i % len(WEIGHTS)], STRETCH[i % len(STRETCH)]))
    return """<section class="sms-kinwall" id="who">
  <div class="sms-kinwall__inner">
    <div class="sms-kinwall__head"><div class="sms-kinwall__eyebrow">%s</div><h2 class="sms-kinwall__title">Who does Streamline work with?</h2></div>
    <ul class="sms-kinwall__list" data-sms-wall>%s</ul>
  </div>
</section>
""" % (e(C.STRAP), lis)


def home(ctx):
    ctx.notes.append("Image-only copy used: \"Clinician-led safety and medical support\" (clinician-led-safety.png)")
    out = hero(ctx)
    out += drift(ctx)
    out += stack(ctx)
    out += pair(ctx)
    out += spotlight(ctx)
    out += wall(ctx)
    picks = ["Where is Streamline based?", "Who runs Streamline?", "Can Streamline provide more than one service?", "Do you offer a free initial discussion?", "Are you insured?", "How can I contact Streamline?"]
    allf = dict(C.faqs("home"))
    out += SHARED_RENDERERS["faq"](ctx, {"tone": "pale", "eyebrow": C.STRAP, "title": "General Streamline [[FAQs]]",
                                        "lead": ["Answers to common questions about Streamline Safety & Medical Solutions, our team, services, bookings and how we work."],
                                        "items": [(q, allf[q]) for q in picks], "show": 6})
    out += cta(ctx, {"title": "Still have a question?", "text": ["Speak to our team and we will be happy to help."],
                     "buttons": [("Book online", "book"), ("Contact Streamline", "contact")]})
    return out


# ---------------------------------------------------------------------------
# Inner page extras
# ---------------------------------------------------------------------------

def courses(ctx):
    d = COURSES
    rows = ""
    for i, it in enumerate(d["items"], 1):
        meta = ""
        if it.get("meta"):
            meta += '<span class="sms-kincourse__dur">%s<span class="sms-kincourse__dur-text">%s</span></span>' % (icon("clock", "sms-kincourse__dur-icon"), e(it["meta"]))
        if it.get("text"):
            meta += '<span class="sms-kincourse__extra">%s</span>' % e(it["text"])
        rows += """<li class="sms-kincourse__item"><a class="sms-kincourse__link" href="%s">
        <span class="sms-kincourse__num" aria-hidden="true">%02d</span>
        <span class="sms-kincourse__name" data-text="%s"><span class="sms-kincourse__txt">%s</span></span>
        <span class="sms-kincourse__meta">%s<span class="sms-visually-hidden">: enquire about this course</span></span>
        <span class="sms-kincourse__go" aria-hidden="true">%s</span>
      </a></li>""" % (link(ctx, "book:training"), i, attr(it["title"]), e(it["title"]), meta, icon("arrow", "sms-kincourse__go-icon"))
    return """<section class="sms-kincourse" id="courses">
  <div class="sms-kincourse__inner">
    <div class="sms-kincourse__head">
      <div class="sms-kincourse__heading"><div class="sms-kincourse__eyebrow">%s</div><h2 class="sms-kincourse__title">%s</h2></div>
      <div class="sms-kincourse__lead">%s</div>
    </div>
    <ol class="sms-kincourse__list">%s</ol>
    <div class="sms-kincourse__foot">%s</div>
  </div>
</section>
""" % (e(d["eyebrow"]), e(d["title"]), paras(d["lead"]), rows,
       buttons(ctx, [("Book your next training session", "book:training"), ("View our training catalogue of courses", C.CATALOGUE)]))


PATH_TONES = ["navy", "mint", "pale", "navy", "mint"]


def pathway(ctx):
    d = REC[2][1]
    cards = ""
    n = len(d["items"])
    for i, it in enumerate(d["items"]):
        cards += """<li class="sms-kinpath__item" style="--i: %d">
        <div class="sms-kinpath__card sms-kinpath__card--%s">
          <span class="sms-kinpath__num" aria-hidden="true">%02d</span>
          <div class="sms-kinpath__body">%s<h3 class="sms-kinpath__name">%s</h3></div>
        </div>
      </li>""" % (i, PATH_TONES[i % len(PATH_TONES)], i + 1, icon(it["icon"], "sms-kinpath__icon"), e(it["title"]))
    return """<section class="sms-kinpath" id="pathway">
  <div class="sms-kinpath__inner">
    <div class="sms-kinpath__head">
      <div class="sms-kinpath__heading"><div class="sms-kinpath__eyebrow">%s</div><h2 class="sms-kinpath__title">%s</h2></div>
      <div class="sms-kinpath__lead">%s</div>
    </div>
    <ol class="sms-kinpath__list" style="--n: %d">%s</ol>
  </div>
</section>
""" % (e(d["eyebrow"]), e(d["title"]), paras(d["lead"]), n, cards)


def values(ctx):
    feat = REC[1][1]
    vals = [t for _, t in feat["chips"]]
    lis = "".join('<li class="sms-kinvalues__item">%s</li>' % word(v, [300, 800, 450, 750, 350][i % 5], [100, 75, 90, 80, 95][i % 5]) for i, v in enumerate(vals))
    return """<section class="sms-kinvalues" id="values">
  <div class="sms-kinvalues__inner">
    <h2 class="sms-kinvalues__title">%s</h2>
    <ul class="sms-kinvalues__list" data-sms-wall>%s</ul>
    <div class="sms-kinvalues__text"><p>%s</p></div>
    <div class="sms-kinvalues__actions">%s</div>
  </div>
</section>
""" % (e(feat["chips_title"]), lis, e(feat["body"][2]), buttons(ctx, feat["buttons"]))


def inner_extra(ctx, slug):
    if slug == "medical-training":
        return courses(ctx)
    if slug == "recruitment":
        ctx.notes.append("Recruitment: the values list sits in its own kinetic word row (taken from the Expression of Interest chips)")
        feat = dict(REC[1][1])
        feat.pop("chips", None)
        feat.pop("chips_title", None)
        feat.pop("buttons", None)
        feat["body"] = feat["body"][:2]
        out = SHARED_RENDERERS["checklist"](ctx, REC[0][1])
        out += SHARED_RENDERERS["feature"](ctx, feat)
        out += pathway(ctx)
        out += values(ctx)
        return out
    return ""


# ---------------------------------------------------------------------------
# Scripts (progressive enhancement; everything works without them)
# ---------------------------------------------------------------------------
JS = """<script>
(function () {
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var fine = window.matchMedia('(hover: hover) and (pointer: fine)').matches;
  var each = function (sel, fn) { Array.prototype.forEach.call(document.querySelectorAll(sel), fn); };
  var clamp = function (v, a, b) { return Math.max(a, Math.min(b, v)); };

  /* Magnetic primary buttons: a small pull towards the pointer */
  if (fine && !reduce) {
    each('.sms-btn--primary', function (b) {
      var raf = 0, mx = 0, my = 0;
      var paint = function () { raf = 0; b.style.setProperty('--sms-mx', mx.toFixed(1) + 'px'); b.style.setProperty('--sms-my', my.toFixed(1) + 'px'); };
      b.addEventListener('pointermove', function (ev) {
        if (b.disabled) { return; }
        var r = b.getBoundingClientRect();
        mx = clamp((ev.clientX - (r.left + r.width / 2)) * 0.22, -10, 10);
        my = clamp((ev.clientY - (r.top + r.height / 2)) * 0.32, -7, 7);
        if (!raf) { raf = window.requestAnimationFrame(paint); }
      }, { passive: true });
      b.addEventListener('pointerleave', function () { mx = 0; my = 0; if (!raf) { raf = window.requestAnimationFrame(paint); } });
    });
  }

  /* Service marquee: drifts by itself, speeds up and turns with scroll velocity */
  each('[data-sms-drift]', function (sec) {
    if (reduce) { return; }
    var track = sec.querySelector('.sms-kindrift__track');
    var toggle = sec.querySelector('[data-sms-drift-toggle]');
    var per = parseInt(sec.getAttribute('data-sms-drift'), 10) || 3;
    sec.classList.add('is-live');
    var group = 0, x = 0, v = -48, dir = -1, base = 48, lastY = window.scrollY, lastT = 0, visible = true, paused = false, raf = 0;
    var measure = function () { var items = track.children; group = items[per].offsetLeft - items[0].offsetLeft; };
    measure();
    if (document.fonts && document.fonts.ready) { document.fonts.ready.then(measure); }
    window.addEventListener('resize', measure, { passive: true });
    var frame = function (t) {
      raf = 0;
      var dt = lastT ? Math.min(0.05, (t - lastT) / 1000) : 0.016;
      lastT = t;
      var y = window.scrollY, dy = y - lastY;
      lastY = y;
      if (dy > 0) { dir = -1; } else if (dy < 0) { dir = 1; }
      var target = paused ? 0 : clamp(dir * base - (dy / Math.max(dt, 0.008)) * 0.35, -1800, 1800);
      v += (target - v) * Math.min(1, dt * 5);
      x += v * dt;
      if (group > 0) { while (x <= -group) { x += group; } while (x > 0) { x -= group; } }
      var skew = paused ? 0 : clamp((v - dir * base) * 0.006, -7, 7);
      track.style.transform = 'translate3d(' + x.toFixed(2) + 'px,0,0) skewX(' + skew.toFixed(2) + 'deg)';
      if (visible) { raf = window.requestAnimationFrame(frame); }
    };
    if ('IntersectionObserver' in window) {
      new IntersectionObserver(function (en) {
        visible = en[0].isIntersecting;
        if (visible && !raf) { lastT = 0; lastY = window.scrollY; raf = window.requestAnimationFrame(frame); }
      }).observe(sec);
    }
    raf = window.requestAnimationFrame(frame);
    if (toggle) {
      toggle.addEventListener('click', function () {
        paused = !paused;
        toggle.setAttribute('aria-pressed', paused ? 'true' : 'false');
        toggle.textContent = paused ? 'Play motion' : 'Pause motion';
      });
    }
  });

  /* Spotlight: a soft light follows the pointer across the navy (desktop only) */
  each('[data-sms-spot]', function (sec) {
    if (!fine || reduce) { return; }
    var light = sec.querySelector('.sms-kinspot__light');
    if (!light) { return; }
    sec.classList.add('is-live');
    var tx = 0, ty = 0, cx = 0, cy = 0, raf = 0, first = true;
    var step = function () {
      cx += (tx - cx) * 0.12; cy += (ty - cy) * 0.12;
      light.style.transform = 'translate3d(' + cx.toFixed(1) + 'px,' + cy.toFixed(1) + 'px,0)';
      if (Math.abs(tx - cx) > 0.5 || Math.abs(ty - cy) > 0.5) { raf = window.requestAnimationFrame(step); } else { raf = 0; }
    };
    sec.addEventListener('pointermove', function (ev) {
      var r = sec.getBoundingClientRect();
      tx = ev.clientX - r.left; ty = ev.clientY - r.top;
      if (first) { cx = tx; cy = ty; first = false; }
      sec.classList.add('is-lit');
      if (!raf) { raf = window.requestAnimationFrame(step); }
    }, { passive: true });
    sec.addEventListener('pointerleave', function () { sec.classList.remove('is-lit'); });
  });

  /* Word walls: words near the pointer swell in weight and width */
  each('[data-sms-wall]', function (wallEl) {
    if (!fine || reduce) { return; }
    var words = Array.prototype.slice.call(wallEl.querySelectorAll('[data-w]'));
    var rects = [], px = -1e5, py = -1e5, raf = 0;
    var measure = function () {
      rects = words.map(function (w) {
        var r = w.parentNode.getBoundingClientRect();
        return { x: r.left + r.width / 2 + window.scrollX, y: r.top + r.height / 2 + window.scrollY, w: +w.getAttribute('data-w') };
      });
    };
    var paint = function () {
      raf = 0;
      var reach = Math.max(180, wallEl.offsetWidth * 0.22);
      words.forEach(function (el, i) {
        var r = rects[i];
        var k = clamp(1 - Math.sqrt((px - r.x) * (px - r.x) + (py - r.y) * (py - r.y)) / reach, 0, 1);
        k = k * k * (3 - 2 * k);
        el.style.fontWeight = Math.round(r.w + (800 - r.w) * k);
      });
    };
    wallEl.addEventListener('pointerenter', measure);
    wallEl.addEventListener('pointermove', function (ev) {
      if (!rects.length) { measure(); }
      px = ev.pageX; py = ev.pageY;
      if (!raf) { raf = window.requestAnimationFrame(paint); }
    }, { passive: true });
    wallEl.addEventListener('pointerleave', function () { px = -1e5; py = -1e5; if (!raf) { raf = window.requestAnimationFrame(paint); } });
    window.addEventListener('resize', function () { rects = []; }, { passive: true });
  });
})();
</script>
"""


def scripts(ctx, main):
    return JS
