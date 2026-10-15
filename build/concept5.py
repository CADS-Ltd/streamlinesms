"""Concept 5 - Bento. Apple-style product-page polish in Streamline's own colours:
the homepage is a bento grid of rounded tiles of different sizes, like a calm,
well organised dashboard. Tiles assemble with a staggered entrance, lean gently
towards the pointer with a soft specular glare, and service tiles zoom their photo
and slide up what each service covers. A radio-driven course finder (works without
JavaScript), a second "why Streamline" bento with Mathew's quote, small bento page
heroes, and a consultancy bento whose tiles open to show what each service includes."""
from common import *  # noqa: F401,F403
import content as C
import light

NAME = "Bento"
DARK = False
CINE = True
FONTS = "https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&display=swap"

COURSES = C.PAGES["medical-training"]["sections"][0][1]
CONSULT = C.PAGES["risk-needs-consultancy"]["sections"][1][1]

ISLANDS = [".sms-bento .sms-bento__tile--navy", ".sms-phero .sms-phero__tile--navy", ".sms-finder .sms-finder__out",
           ".sms-why .sms-why__tile--navy", ".sms-bcta .sms-bcta__box", ".sms-cards .sms-cards__grid--3 > .sms-cards__item:first-child",
           ".sms-quotes .sms-quotes__item:first-child", ".sms-people .sms-people__shared", ".sms-booking .sms-booking__summary", ".sms-footer"]
# the green glow is pre-mixed onto navy (32% #407f36 over #061e35) so it stays an opaque Streamline tone
NAVY_BG = "radial-gradient(42rem 26rem at 100% 0%, #193d35, rgba(6, 30, 53, 0) 62%), linear-gradient(160deg, #0b3152, #061e35 62%)"


def _finder_css():
    n = len(COURSES["items"])
    out = ", ".join(".sms-finder .sms-finder__p%d" % i for i in range(n)) + " { display: none; min-width: 0; animation: sms-fade-up 0.5s var(--sms-ease) both; }\n"
    for i in range(n):
        r = ".sms-finder .sms-finder__r%d" % i
        out += "%s:checked ~ * .sms-finder__p%d { display: block; }\n" % (r, i)
        out += "%s:checked ~ * .sms-finder__chip--%d { border-color: #061e35; background: #061e35; color: #ffffff; }\n" % (r, i)
        out += "%s:checked ~ * .sms-finder__chip--%d .sms-finder__chip-icon { background: rgba(255, 255, 255, 0.14); color: #82d06e; }\n" % (r, i)
        out += "%s:focus-visible ~ * .sms-finder__chip--%d { outline: 3px solid #407f36; outline-offset: 3px; }\n" % (r, i)
    return out


CSS = light.css(ISLANDS) + ",\n".join(ISLANDS) + " { --sms-hl: rgba(255, 255, 255, 0.1); }\n" + r"""
/* ===== Concept 5 theme: bento ===== */
.sms-page {
  --sms-font: "Manrope", "Montserrat", Arial, sans-serif;
  --sms-bg: #f4f8f3;
  --sms-pale: #f4f8f3;
  --sms-radius: 1.75rem;
  --sms-radius-sm: 1rem;
  --sms-hw: 700;
  --sms-max: 78rem;
  --sms-hl: rgba(6, 30, 53, 0.08);
  --sms-gap: clamp(0.75rem, 0.55rem + 0.6vw, 1.125rem);
  --sms-section: clamp(3rem, 2rem + 3.5vw, 5.5rem);
  --sms-lift: 0 28px 50px -22px rgba(6, 30, 53, 0.28);
  --sms-inner-r: calc(var(--sms-radius) - 0.55rem);
  letter-spacing: -0.006em;
}
.sms-page .sms-mark { color: var(--sms-accent); font-weight: inherit; }
.sms-page .sms-btn { padding: 0.85rem 1.35rem; font-weight: 700; letter-spacing: 0; }
.sms-page .sms-btn--primary:hover { box-shadow: 0 14px 30px -12px var(--sms-glow); }
.sms-page .sms-kicker { gap: 0.6rem; margin-bottom: 1rem; font-size: 0.75rem; font-weight: 700; letter-spacing: 0.14em; }
.sms-page .sms-kicker::before { width: 0.4rem; height: 0.4rem; box-shadow: none; }
.sms-page .sms-arrowlink { font-weight: 700; text-decoration: none; }

/* ---------- Tiles (shared look + motion) ---------- */
.sms-page .sms-tile { position: relative; min-width: 0; overflow: hidden; isolation: isolate; border: 1px solid var(--sms-hl); border-radius: var(--sms-radius); background: var(--sms-surface); color: var(--sms-ink); box-shadow: 0 1px 2px rgba(6, 30, 53, 0.04); transition: transform 0.7s var(--sms-ease), box-shadow 0.5s var(--sms-ease), opacity 0.8s var(--sms-ease), translate 0.9s var(--sms-ease), scale 0.9s var(--sms-ease), background-color 0.4s; }
.sms-page .sms-tile.is-tilting { box-shadow: var(--sms-lift); transition: box-shadow 0.5s var(--sms-ease), opacity 0.8s var(--sms-ease), translate 0.9s var(--sms-ease), scale 0.9s var(--sms-ease); will-change: transform; }
.sms-page .sms-tile.is-armed { opacity: 0; translate: 0 2rem; scale: 0.97; }
.sms-page .sms-glare { position: absolute; left: 0; top: 0; z-index: 3; width: 34rem; height: 34rem; margin: -17rem 0 0 -17rem; border-radius: 50%; background: radial-gradient(circle, rgba(255, 255, 255, 0.22), rgba(255, 255, 255, 0) 62%); opacity: 0; pointer-events: none; transition: opacity 0.5s var(--sms-ease); }
.sms-page .sms-tile.is-hover .sms-glare { opacity: 1; }
@keyframes sms-assemble { from { opacity: 0; translate: 0 1.75rem; scale: 0.96; } to { opacity: 1; translate: 0 0; scale: 1; } }
@keyframes sms-assemble-t { from { translate: 0 1.75rem; scale: 0.97; } to { translate: 0 0; scale: 1; } }
.sms-page .sms-tile--in { animation: sms-assemble 0.9s var(--sms-ease) both; animation-delay: calc(var(--sms-i, 0) * 70ms + 120ms); }
.sms-page .sms-tile--in-t { animation: sms-assemble-t 0.9s var(--sms-ease) both; animation-delay: calc(var(--sms-i, 0) * 70ms + 60ms); }
.sms-page .sms-tile__label { min-width: 0; margin: 0 0 0.4rem; color: var(--sms-ink-soft); font-size: 0.75rem; font-weight: 700; letter-spacing: 0.14em; text-transform: uppercase; }

/* ---------- Header and footer ---------- */
.sms-header { border-bottom: 1px solid var(--sms-hl); background: rgba(244, 248, 243, 0.82); }
.sms-header .sms-header__link { color: var(--sms-ink); font-weight: 600; }
.sms-header .sms-header__summary { background: var(--sms-surface); box-shadow: inset 0 0 0 1px var(--sms-hl); }
.sms-header .sms-header__panel { border-radius: var(--sms-radius); }
.sms-footer { margin: clamp(1rem, 0.6rem + 1.5vw, 2rem) clamp(0.5rem, 0.2rem + 1vw, 1rem) clamp(0.5rem, 0.2rem + 1vw, 1rem); border-top: 0; border-radius: var(--sms-radius); background: """ + NAVY_BG + r"""; }
.sms-footer .sms-footer__heading { letter-spacing: 0.14em; font-weight: 700; }
.sms-footer .sms-footer__base { border-color: var(--sms-hl); }

/* ---------- Shared sections restyled as tiles ---------- */
.sms-feature.sms-tone-pale, .sms-cards.sms-tone-pale, .sms-steps.sms-tone-pale, .sms-checklist.sms-tone-pale, .sms-notice.sms-tone-pale,
.sms-faq.sms-tone-pale, .sms-quotes.sms-tone-pale, .sms-people.sms-tone-pale, .sms-contact.sms-tone-pale, .sms-links.sms-tone-pale,
.sms-claim.sms-tone-pale, .sms-marquee.sms-tone-pale, .sms-booking.sms-tone-pale { background: transparent; }
.sms-feature, .sms-cards, .sms-steps, .sms-checklist, .sms-notice, .sms-faq, .sms-quotes, .sms-people, .sms-contact,
.sms-links, .sms-claim, .sms-marquee, .sms-booking { padding: calc(var(--sms-section) * 0.55) 0; }
.sms-feature .sms-watermark, .sms-cards .sms-watermark, .sms-steps .sms-watermark, .sms-quotes .sms-watermark,
.sms-people .sms-watermark, .sms-claim .sms-watermark, .sms-checklist .sms-watermark { display: none; }
.sms-feature .sms-feature__eyebrow, .sms-cards .sms-cards__eyebrow, .sms-steps .sms-steps__eyebrow, .sms-checklist .sms-checklist__eyebrow,
.sms-faq .sms-faq__eyebrow, .sms-quotes .sms-quotes__eyebrow, .sms-people .sms-people__eyebrow, .sms-contact .sms-contact__eyebrow,
.sms-links .sms-links__eyebrow, .sms-marquee .sms-marquee__eyebrow, .sms-booking .sms-booking__eyebrow { gap: 0.6rem; margin-bottom: 1rem; font-size: 0.75rem; font-weight: 700; letter-spacing: 0.14em; }
.sms-feature .sms-feature__eyebrow::before, .sms-cards .sms-cards__eyebrow::before, .sms-steps .sms-steps__eyebrow::before, .sms-checklist .sms-checklist__eyebrow::before,
.sms-faq .sms-faq__eyebrow::before, .sms-quotes .sms-quotes__eyebrow::before, .sms-people .sms-people__eyebrow::before, .sms-contact .sms-contact__eyebrow::before,
.sms-links .sms-links__eyebrow::before, .sms-marquee .sms-marquee__eyebrow::before, .sms-booking .sms-booking__eyebrow::before { width: 0.4rem; height: 0.4rem; box-shadow: none; }
.sms-feature .sms-feature__title, .sms-cards .sms-cards__title, .sms-steps .sms-steps__title, .sms-checklist .sms-checklist__title,
.sms-faq .sms-faq__title, .sms-quotes .sms-quotes__title, .sms-people .sms-people__title, .sms-contact .sms-contact__title,
.sms-links .sms-links__title, .sms-marquee .sms-marquee__title, .sms-booking .sms-booking__title { font-size: clamp(1.9rem, 1.2rem + 2.6vw, 3.3rem); font-weight: 800; line-height: 1.06; letter-spacing: -0.04em; }

/* Feature: one big tile, photo inset */
.sms-feature .sms-feature__inner { width: calc(100% - 2 * var(--sms-gutter)); max-width: calc(var(--sms-max) - 2 * var(--sms-gutter)); padding: clamp(0.55rem, 0.4rem + 0.5vw, 0.8rem); gap: clamp(0.5rem, 0.2rem + 2.2vw, 2.5rem); align-items: stretch; border: 1px solid var(--sms-hl); border-radius: var(--sms-radius); background: var(--sms-surface); }
.sms-feature .sms-feature__blob { display: none; }
.sms-feature .sms-feature__frame { aspect-ratio: 4 / 3; border-radius: var(--sms-inner-r); box-shadow: none; }
.sms-feature .sms-feature__main { padding: clamp(0.85rem, 0.4rem + 1.8vw, 2.5rem) clamp(0.6rem, 0.2rem + 1.6vw, 2.25rem); }
.sms-feature .sms-feature__lead { color: var(--sms-ink); font-weight: 500; }
.sms-feature .sms-chips__item,
.sms-feature.sms-tone-white .sms-chips__item { background: var(--sms-pale); box-shadow: none; font-weight: 600; }
.sms-feature .sms-feature__strap { background: var(--sms-mint); box-shadow: none; font-weight: 700; }
.sms-feature .sms-feature__chips-title { font-weight: 700; }
@media (min-width: 56em) {
  .sms-feature .sms-feature__frame { height: 100%; min-height: 24rem; aspect-ratio: auto; }
}

/* Cards, links, checklist, quotes, people, notice, contact: hairline tiles */
.sms-cards .sms-cards__grid,
.sms-links .sms-links__grid,
.sms-checklist .sms-checklist__grid,
.sms-quotes .sms-quotes__grid,
.sms-people .sms-people__grid { gap: var(--sms-gap); }
.sms-cards .sms-cards__item,
.sms-cards.sms-tone-white .sms-cards__item,
.sms-cards.sms-tone-pale .sms-cards__item,
.sms-links .sms-links__link,
.sms-checklist .sms-checklist__item,
.sms-quotes .sms-quotes__item,
.sms-people .sms-people__person,
.sms-people.sms-tone-white .sms-people__person,
.sms-notice .sms-notice__box,
.sms-contact .sms-contact__detail,
.sms-contact .sms-contact__form { border: 1px solid var(--sms-hl); border-radius: var(--sms-radius); background: var(--sms-surface); box-shadow: none; }
.sms-cards .sms-cards__item:hover,
.sms-links .sms-links__link:hover { box-shadow: var(--sms-lift); transform: translateY(-4px); }
.sms-cards .sms-cards__grid--3 > .sms-cards__item:first-child,
.sms-quotes .sms-quotes__item:first-child,
.sms-people .sms-people__shared { border-color: transparent; background: """ + NAVY_BG + r"""; }
.sms-cards .sms-cards__icon,
.sms-links .sms-links__icon,
.sms-quotes .sms-quotes__icon { border-radius: 1rem; }
.sms-cards .sms-cards__name,
.sms-links .sms-links__name,
.sms-people .sms-people__name,
.sms-notice .sms-notice__title { font-weight: 700; letter-spacing: -0.02em; }
.sms-cards .sms-cards__num { font-weight: 800; letter-spacing: -0.04em; }
.sms-cards .sms-cards__link,
.sms-links .sms-links__go { font-weight: 700; }
.sms-checklist .sms-checklist__item { font-weight: 600; }
.sms-quotes .sms-quotes__text { font-weight: 600; letter-spacing: -0.015em; }
.sms-people .sms-people__frame { border-radius: var(--sms-radius); box-shadow: none; }
.sms-people .sms-people__shared { border-radius: var(--sms-radius); }
.sms-people .sms-people__role { font-weight: 700; }
.sms-contact .sms-contact__value { font-weight: 700; }
.sms-contact .sms-contact__form-title { font-weight: 700; }
.sms-contact .sms-contact__booklink { box-shadow: none; }

/* Steps: one tile per step */
.sms-steps .sms-steps__line { display: none; }
.sms-steps .sms-steps__list { gap: var(--sms-gap); }
.sms-steps .sms-steps__item { align-content: start; padding: clamp(1.1rem, 0.9rem + 0.8vw, 1.6rem); border: 1px solid var(--sms-hl); border-radius: var(--sms-radius); background: var(--sms-surface); }
.sms-steps .sms-steps__badge,
.sms-steps.sms-tone-pale .sms-steps__badge { border-radius: 1rem; background: var(--sms-mint); color: var(--sms-accent); box-shadow: none; }
.sms-steps .sms-steps__num { background: var(--sms-navy); color: #ffffff; }
.sms-steps .sms-steps__name { font-weight: 700; letter-spacing: -0.015em; }
.sms-steps .sms-steps__note,
.sms-steps.sms-tone-white .sms-steps__note { max-width: none; margin-top: var(--sms-gap); border: 1px solid var(--sms-hl); border-radius: var(--sms-radius-sm); background: var(--sms-surface); box-shadow: none; }

/* FAQ */
.sms-faq .sms-faq__item,
.sms-faq.sms-tone-white .sms-faq__item { margin-bottom: 0.6rem; border: 1px solid var(--sms-hl); border-radius: 1.25rem; background: var(--sms-surface); box-shadow: none; }
.sms-faq .sms-faq__q { padding: 1.15rem 3.75rem 1.15rem 1.4rem; font-weight: 600; }
.sms-faq .sms-faq__a { padding: 0 1.4rem 1.3rem; }
.sms-faq .sms-faq__all-toggle { border: 1px solid var(--sms-line); background: var(--sms-surface); font-weight: 700; }
.sms-faq .sms-faq__input { border-color: var(--sms-field-line); background: var(--sms-surface); }

/* Claim: a mint tile */
.sms-claim .sms-claim__inner { width: calc(100% - 2 * var(--sms-gutter)); max-width: calc(var(--sms-max) - 2 * var(--sms-gutter)); padding: clamp(2rem, 1.2rem + 3vw, 4rem) clamp(1.25rem, 0.8rem + 2.5vw, 4rem); border-radius: var(--sms-radius); background: var(--sms-mint); }
.sms-claim .sms-claim__icon,
.sms-claim.sms-tone-pale .sms-claim__icon { background: #ffffff; color: var(--sms-green); }
.sms-claim .sms-claim__text { color: var(--sms-navy); font-weight: 700; letter-spacing: -0.03em; }

/* Marquee */
.sms-marquee .sms-marquee__item,
.sms-marquee.sms-tone-white .sms-marquee__item { border: 1px solid var(--sms-hl); background: var(--sms-surface); box-shadow: none; font-weight: 600; }

/* Booking demo */
.sms-booking .sms-booking__form { border: 1px solid var(--sms-hl); background: var(--sms-surface); box-shadow: none; }
.sms-booking .sms-booking__service-card { border-width: 1px; }
.sms-booking .sms-booking__step-title { font-weight: 800; letter-spacing: -0.035em; }
.sms-booking .sms-booking__summary { border-radius: var(--sms-radius); border: 0; background: """ + NAVY_BG + r"""; box-shadow: none; }
.sms-booking .sms-booking__help { border-radius: var(--sms-radius); }

/* ---------- Page hero (inner pages): a small bento ---------- */
.sms-phero { padding: clamp(0.75rem, 0.5rem + 1vw, 1.5rem) 0 0; }
.sms-phero .sms-phero__inner { width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-phero .sms-phero__grid { display: grid; grid-template-columns: minmax(0, 1fr); gap: var(--sms-gap); }
.sms-phero .sms-phero__main { display: flex; flex-direction: column; justify-content: center; padding: clamp(1.5rem, 1rem + 2.6vw, 3.5rem); }
.sms-phero .sms-phero__crumb { min-width: 0; margin-bottom: 1.75rem; color: var(--sms-ink-soft); font-size: var(--sms-step--1); font-weight: 500; }
.sms-phero .sms-phero__crumb-link { color: var(--sms-ink); font-weight: 700; text-underline-offset: 4px; }
.sms-phero .sms-phero__title { min-width: 0; max-width: 13em; margin: 0 0 1.25rem; color: var(--sms-title); font-size: clamp(2.3rem, 1.3rem + 3.6vw, 4.5rem); font-weight: 800; line-height: 1.02; letter-spacing: -0.045em; }
.sms-phero .sms-phero__sub { min-width: 0; margin-bottom: 0.5rem; color: var(--sms-accent); font-weight: 700; }
.sms-phero .sms-phero__lead { min-width: 0; max-width: 38rem; color: var(--sms-ink); font-size: var(--sms-step-1); font-weight: 500; line-height: 1.55; }
.sms-phero .sms-phero__lead p { margin: 0 0 0.75rem; }
.sms-phero .sms-phero__actions { display: flex; flex-wrap: wrap; gap: 0.75rem; min-width: 0; margin-top: 1.5rem; }
.sms-phero .sms-phero__kicker { min-width: 0; }
.sms-phero .sms-phero__photo { aspect-ratio: 4 / 3; background: var(--sms-navy); }
.sms-phero .sms-phero__img { position: absolute; inset: 0; z-index: -1; display: block; width: 100%; height: 100%; object-fit: cover; }
.sms-phero .sms-phero__chips { display: flex; flex-direction: column; justify-content: flex-end; gap: 0.9rem; padding: clamp(1.25rem, 1rem + 1vw, 1.75rem); }
.sms-phero .sms-phero__tile--navy { border-color: transparent; background: """ + NAVY_BG + r"""; }
.sms-phero .sms-phero__list { display: grid; gap: 0.6rem; min-width: 0; margin: 0; padding: 0; list-style: none; }
.sms-phero .sms-phero__item { display: flex; align-items: center; gap: 0.75rem; min-width: 0; color: var(--sms-title); font-weight: 600; line-height: 1.35; }
.sms-phero .sms-phero__item-icon { width: 2.25rem; height: 2.25rem; padding: 0.5rem; border-radius: 0.8rem; background: var(--sms-mint); color: var(--sms-accent); }
.sms-phero .sms-phero__item-text { min-width: 0; }
.sms-phero .sms-tile__label { color: var(--sms-ink-soft); }
@media (min-width: 60em) {
  .sms-phero .sms-phero__grid { grid-template-columns: repeat(12, minmax(0, 1fr)); }
  .sms-phero .sms-phero__main { grid-column: 1 / 8; grid-row: 1 / 3; min-height: 32rem; }
  .sms-phero .sms-phero__photo { grid-column: 8 / 13; grid-row: 1; aspect-ratio: auto; min-height: 18rem; }
  .sms-phero .sms-phero__chips { grid-column: 8 / 13; grid-row: 2; }
}

/* ---------- CTA: a wide navy tile ---------- */
.sms-bcta { padding: 0; }
.sms-bcta .sms-bcta__inner { width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-bcta .sms-bcta__box { position: relative; display: grid; gap: 2rem; align-items: center; overflow: hidden; padding: clamp(1.75rem, 1rem + 3.5vw, 4rem); border-radius: var(--sms-radius); background: """ + NAVY_BG + r"""; }
.sms-bcta .sms-bcta__shield { position: absolute; right: -3rem; bottom: -4rem; width: 16rem; height: auto; opacity: 0.05; pointer-events: none; }
.sms-bcta .sms-bcta__copy { position: relative; min-width: 0; }
.sms-bcta .sms-bcta__title { margin: 0 0 1rem; color: var(--sms-title); font-size: clamp(2rem, 1.3rem + 2.6vw, 3.4rem); font-weight: 800; line-height: 1.04; letter-spacing: -0.04em; }
.sms-bcta .sms-bcta__text { max-width: 36rem; color: var(--sms-ink-soft); font-size: var(--sms-step-1); line-height: 1.55; }
.sms-bcta .sms-bcta__text p { margin: 0; }
.sms-bcta .sms-bcta__side { position: relative; display: grid; gap: 1rem; justify-items: start; min-width: 0; }
.sms-bcta .sms-bcta__actions { display: flex; flex-wrap: wrap; gap: 0.75rem; min-width: 0; }
.sms-bcta .sms-bcta__call { min-width: 0; color: var(--sms-ink-soft); font-size: var(--sms-step--1); }
.sms-bcta .sms-bcta__call a { color: var(--sms-title); font-weight: 700; text-underline-offset: 4px; }
@media (min-width: 60em) {
  .sms-bcta .sms-bcta__box { grid-template-columns: minmax(0, 1.5fr) minmax(0, 1fr); }
  .sms-bcta .sms-bcta__side { justify-items: end; text-align: right; }
}

/* ---------- Home: hero bento ---------- */
.sms-bento { padding: clamp(0.75rem, 0.5rem + 1vw, 1.5rem) 0 0; }
.sms-bento .sms-bento__inner { width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-bento .sms-bento__grid { display: grid; grid-template-columns: minmax(0, 1fr); gap: var(--sms-gap); }
.sms-bento .sms-bento__tile--navy { border-color: transparent; background: """ + NAVY_BG + r"""; }
.sms-bento .sms-bento__hero { display: flex; flex-direction: column; justify-content: flex-end; gap: 1.5rem; min-height: 26rem; padding: clamp(1.5rem, 1rem + 2.6vw, 3.5rem); }
.sms-bento .sms-bento__shield { position: absolute; right: -2.5rem; top: -3rem; z-index: -1; width: clamp(12rem, 8rem + 12vw, 20rem); height: auto; opacity: 0.06; pointer-events: none; }
.sms-bento .sms-bento__kicker { min-width: 0; margin: 0; }
.sms-bento .sms-bento__title { min-width: 0; max-width: 11em; margin: 0; color: var(--sms-title); font-size: clamp(2.5rem, 1.3rem + 4vw, 5rem); font-weight: 800; line-height: 0.99; letter-spacing: -0.05em; }
.sms-bento .sms-bento__lead { min-width: 0; max-width: 31rem; color: var(--sms-ink-soft); font-size: var(--sms-step-1); line-height: 1.55; }
.sms-bento .sms-bento__lead p { margin: 0; }
.sms-bento .sms-bento__actions { display: flex; flex-wrap: wrap; gap: 0.75rem; min-width: 0; }
.sms-bento .sms-bento__photo { aspect-ratio: 4 / 3; background: var(--sms-navy); }
.sms-bento .sms-bento__photo-img { position: absolute; inset: 0; z-index: -1; display: block; width: 100%; height: 100%; object-fit: cover; }
.sms-bento .sms-bento__chip { position: absolute; left: 1rem; bottom: 1rem; display: inline-flex; align-items: center; gap: 0.5rem; padding: 0.5rem 0.95rem 0.5rem 0.55rem; border-radius: 999px; background: rgba(6, 30, 53, 0.86); color: #ffffff; font-size: var(--sms-step--1); font-weight: 700; -webkit-backdrop-filter: blur(10px); backdrop-filter: blur(10px); }
.sms-bento .sms-bento__chip-icon { width: 1.6rem; height: 1.6rem; padding: 0.3rem; border-radius: 50%; background: rgba(130, 208, 110, 0.18); color: #82d06e; }
.sms-bento .sms-bento__chip-text { min-width: 0; }

/* Service tiles */
.sms-bento .sms-bento__svc { display: flex; flex-direction: column; padding: 0.55rem; }
.sms-bento .sms-bento__svc-media { display: grid; min-width: 0; overflow: hidden; border-radius: var(--sms-inner-r); background: var(--sms-pale); }
.sms-bento .sms-bento__svc-img { grid-area: 1 / 1; display: block; min-width: 0; width: 100%; height: auto; aspect-ratio: 16 / 10; object-fit: cover; transition: transform 1.1s var(--sms-ease); }
.sms-bento .sms-bento__svc-list { grid-area: 1 / 1; align-self: end; z-index: 1; min-width: 0; margin: 0.55rem; padding: 0.8rem 1rem; border-radius: 1rem; background: rgba(6, 30, 53, 0.92); color: #ffffff; font-size: var(--sms-step--1); font-weight: 600; line-height: 1.35; list-style: none; transform: translateY(calc(100% + 1rem)); transition: transform 0.6s var(--sms-ease); }
.sms-bento .sms-bento__svc-item { display: flex; align-items: center; gap: 0.55rem; min-width: 0; padding: 0.2rem 0; }
.sms-bento .sms-bento__svc-item-icon { width: 1.05rem; height: 1.05rem; color: #82d06e; }
.sms-bento .sms-bento__svc-item-text { min-width: 0; }
.sms-bento .sms-bento__svc:hover .sms-bento__svc-img,
.sms-bento .sms-bento__svc:focus-within .sms-bento__svc-img { transform: scale(1.06); }
.sms-bento .sms-bento__svc:hover .sms-bento__svc-list,
.sms-bento .sms-bento__svc:focus-within .sms-bento__svc-list { transform: none; }
.sms-bento .sms-bento__svc-body { display: flex; flex: 1 1 auto; flex-direction: column; min-width: 0; padding: 1.1rem 0.9rem 0.9rem; }
.sms-bento .sms-bento__svc-top { display: flex; align-items: center; justify-content: space-between; gap: 1rem; min-width: 0; }
.sms-bento .sms-bento__svc-icon { width: 2.75rem; height: 2.75rem; padding: 0.65rem; border-radius: 0.95rem; background: var(--sms-mint); color: var(--sms-accent); }
.sms-bento .sms-bento__svc-go { display: grid; place-items: center; min-width: 0; width: 2.4rem; height: 2.4rem; border-radius: 50%; box-shadow: inset 0 0 0 1px var(--sms-line); color: var(--sms-ink); transition: background-color 0.4s, color 0.4s, transform 0.5s var(--sms-ease); }
.sms-bento .sms-bento__svc-go-icon { width: 1.1rem; height: 1.1rem; }
.sms-bento .sms-bento__svc:hover .sms-bento__svc-go,
.sms-bento .sms-bento__svc:focus-within .sms-bento__svc-go { background: var(--sms-navy); color: #ffffff; transform: rotate(-45deg); }
.sms-bento .sms-bento__svc-title { min-width: 0; margin: 1rem 0 0.4rem; font-size: clamp(1.2rem, 1.08rem + 0.45vw, 1.5rem); font-weight: 800; line-height: 1.18; letter-spacing: -0.03em; }
.sms-bento .sms-bento__svc-link { color: var(--sms-title); text-decoration: none; }
.sms-bento .sms-bento__svc-link::after { content: ""; position: absolute; inset: 0; z-index: 2; border-radius: inherit; }
.sms-bento .sms-bento__svc-link:focus-visible { outline: none; }
.sms-bento .sms-bento__svc:has(.sms-bento__svc-link:focus-visible) { outline: 3px solid var(--sms-green); outline-offset: 3px; }
.sms-bento .sms-bento__svc-text { min-width: 0; margin: 0; color: var(--sms-ink-soft); font-size: var(--sms-step--1); line-height: 1.55; }
.sms-bento .sms-bento__svc-more { min-width: 0; margin-top: auto; padding-top: 1rem; color: var(--sms-accent); font-size: var(--sms-step--1); font-weight: 700; }
.sms-bento .sms-bento__svc:hover .sms-arrow { transform: translateX(5px); }
@media (hover: none) {
  .sms-bento .sms-bento__svc-list { grid-area: 2 / 1; margin: 0; border-radius: 0; background: var(--sms-navy); transform: none; }
}

/* Small fact tiles */
.sms-bento .sms-bento__qual { display: flex; align-items: center; gap: 1.1rem; padding: clamp(1.25rem, 1rem + 1vw, 1.75rem); }
.sms-bento .sms-bento__qual-badge { display: block; flex: 0 0 auto; min-width: 0; width: 4.75rem; height: auto; padding: 0.35rem; border-radius: 1rem; background: #ffffff; box-shadow: inset 0 0 0 1px var(--sms-line); }
.sms-bento .sms-bento__qual-body { min-width: 0; }
.sms-bento .sms-bento__qual-name { margin: 0; color: var(--sms-title); font-size: var(--sms-step-1); font-weight: 800; line-height: 1.2; letter-spacing: -0.02em; }
.sms-bento .sms-bento__qual-no { margin: 0.25rem 0 0; color: var(--sms-ink-soft); font-size: var(--sms-step--1); font-weight: 600; font-variant-numeric: tabular-nums; }
.sms-bento .sms-bento__claim { display: flex; align-items: center; gap: 1.1rem; padding: clamp(1.25rem, 1rem + 1.4vw, 2.25rem); border-color: transparent; background: var(--sms-mint); }
.sms-bento .sms-bento__claim-icon { width: 3rem; height: 3rem; padding: 0.7rem; border-radius: 50%; background: #ffffff; color: var(--sms-green); }
.sms-bento .sms-bento__claim-text { min-width: 0; margin: 0; color: var(--sms-navy); font-size: clamp(1.15rem, 0.95rem + 0.8vw, 1.6rem); font-weight: 700; line-height: 1.3; letter-spacing: -0.025em; }
.sms-bento .sms-bento__area { display: flex; flex-direction: column; justify-content: flex-end; gap: 0.25rem; min-height: 12rem; padding: clamp(1.25rem, 1rem + 1vw, 1.75rem); }
.sms-bento .sms-bento__rings { position: absolute; right: -4.5rem; top: -4.5rem; z-index: -1; width: 15rem; height: 15rem; pointer-events: none; }
.sms-bento .sms-bento__ring { position: absolute; inset: 0; border-radius: 50%; box-shadow: inset 0 0 0 1px var(--sms-line-green); }
.sms-bento .sms-bento__ring--2 { inset: 2.5rem; }
.sms-bento .sms-bento__ring--3 { inset: 5rem; background: var(--sms-mint); box-shadow: none; }
.sms-bento .sms-bento__area-icon { position: absolute; right: 2.4rem; top: 2.4rem; width: 2.2rem; height: 2.2rem; color: var(--sms-green); }
.sms-bento .sms-bento__area-text { min-width: 0; max-width: 30rem; margin: 0; color: var(--sms-title); font-size: var(--sms-step-1); font-weight: 700; line-height: 1.4; letter-spacing: -0.015em; }
.sms-bento .sms-bento__contact { display: flex; flex-direction: column; justify-content: space-between; gap: 1.25rem; padding: clamp(1.25rem, 1rem + 1vw, 1.75rem); }
.sms-bento .sms-bento__contact-title { min-width: 0; margin: 0; color: var(--sms-title); font-size: var(--sms-step-1); font-weight: 800; line-height: 1.25; letter-spacing: -0.02em; }
.sms-bento .sms-bento__contact-head { min-width: 0; }
.sms-bento .sms-bento__contact-links { display: grid; gap: 0.5rem; min-width: 0; }
.sms-bento .sms-bento__contact-link { position: relative; z-index: 4; display: flex; align-items: center; gap: 0.75rem; min-width: 0; padding: 0.8rem 1rem; border-radius: 1rem; background: var(--sms-pale); color: var(--sms-ink); font-weight: 700; text-decoration: none; overflow-wrap: anywhere; transition: background-color 0.3s; }
.sms-bento .sms-bento__contact-link:hover { background: var(--sms-mint); }
.sms-bento .sms-bento__contact-icon { width: 2.25rem; height: 2.25rem; padding: 0.5rem; border-radius: 50%; background: var(--sms-surface); color: var(--sms-green); }
.sms-bento .sms-bento__contact-text { min-width: 0; font-variant-numeric: tabular-nums; }
.sms-bento .sms-bento__photo { order: 1; }
.sms-bento .sms-bento__qual,
.sms-bento .sms-bento__claim,
.sms-bento .sms-bento__area,
.sms-bento .sms-bento__contact { order: 2; }
@media (min-width: 46em) {
  .sms-bento .sms-bento__grid { grid-template-columns: repeat(6, minmax(0, 1fr)); }
  .sms-bento .sms-bento__photo,
  .sms-bento .sms-bento__qual,
  .sms-bento .sms-bento__claim,
  .sms-bento .sms-bento__area,
  .sms-bento .sms-bento__contact { order: 0; }
  .sms-bento .sms-bento__hero { grid-column: span 4; grid-row: span 2; min-height: 30rem; }
  .sms-bento .sms-bento__photo { grid-column: span 2; grid-row: span 2; min-height: 18rem; aspect-ratio: auto; }
  .sms-bento .sms-bento__svc { grid-column: span 2; }
  .sms-bento .sms-bento__qual { grid-column: span 2; flex-direction: column; align-items: flex-start; justify-content: space-between; }
  .sms-bento .sms-bento__claim { grid-column: span 4; }
  .sms-bento .sms-bento__area,
  .sms-bento .sms-bento__contact { grid-column: span 3; }
}
@media (min-width: 64em) {
  .sms-bento .sms-bento__grid { grid-template-columns: repeat(12, minmax(0, 1fr)); }
  .sms-bento .sms-bento__hero { grid-column: span 7; min-height: 34rem; }
  .sms-bento .sms-bento__photo { grid-column: span 5; }
  .sms-bento .sms-bento__svc { grid-column: span 4; }
  .sms-bento .sms-bento__qual { grid-column: span 4; flex-direction: row; align-items: center; justify-content: flex-start; }
  .sms-bento .sms-bento__claim { grid-column: span 8; }
  .sms-bento .sms-bento__area { grid-column: span 6; }
  .sms-bento .sms-bento__contact { grid-column: span 6; }
}

/* ---------- Course finder (radio inputs, works without JavaScript) ---------- */
.sms-finder { padding: var(--sms-gap) 0 0; }
.sms-finder.sms-finder--page { padding: calc(var(--sms-section) * 0.55) 0 0; }
.sms-finder .sms-finder__inner { width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-finder .sms-finder__tile { padding: 0.55rem; }
.sms-finder .sms-finder__radio { position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0); clip-path: inset(50%); white-space: nowrap; }
.sms-finder .sms-finder__grid { display: grid; gap: 0.55rem; }
.sms-finder .sms-finder__pick { min-width: 0; padding: clamp(1rem, 0.6rem + 1.8vw, 2.5rem) clamp(0.75rem, 0.4rem + 1.6vw, 2.25rem); }
.sms-finder .sms-finder__title { margin: 0 0 0.75rem; color: var(--sms-title); font-size: clamp(1.9rem, 1.2rem + 2.4vw, 3.1rem); font-weight: 800; line-height: 1.05; letter-spacing: -0.045em; }
.sms-finder .sms-finder__lead { max-width: 34rem; margin-bottom: 1.5rem; color: var(--sms-ink-soft); }
.sms-finder .sms-finder__lead p { margin: 0; }
.sms-finder .sms-finder__chips { display: flex; flex-wrap: wrap; gap: 0.5rem; min-width: 0; }
.sms-finder .sms-finder__chip { display: inline-flex; align-items: center; gap: 0.5rem; min-width: 0; padding: 0.5rem 1rem 0.5rem 0.5rem; border: 1px solid var(--sms-line); border-radius: 999px; background: var(--sms-surface); color: var(--sms-ink); cursor: pointer; font-size: var(--sms-step--1); font-weight: 600; line-height: 1.3; transition: background-color 0.3s, color 0.3s, border-color 0.3s, transform 0.3s var(--sms-ease); }
.sms-finder .sms-finder__chip:hover { border-color: var(--sms-green); transform: translateY(-2px); }
.sms-finder .sms-finder__chip-icon { width: 1.75rem; height: 1.75rem; padding: 0.35rem; border-radius: 50%; background: var(--sms-mint); color: var(--sms-green); transition: background-color 0.3s, color 0.3s; }
.sms-finder .sms-finder__chip-text { min-width: 0; }
.sms-finder .sms-finder__out { position: relative; display: flex; flex-direction: column; min-width: 0; min-height: 21rem; overflow: hidden; padding: clamp(1.25rem, 0.9rem + 1.8vw, 2.5rem); border-radius: var(--sms-inner-r); background: """ + NAVY_BG + r"""; }
.sms-finder .sms-finder__panel { min-width: 0; }
.sms-finder .sms-finder__panel-icon { width: 3.25rem; height: 3.25rem; padding: 0.75rem; border-radius: 1rem; background: var(--sms-mint); color: var(--sms-accent); }
.sms-finder .sms-finder__label { margin-top: 1.5rem; color: var(--sms-accent); font-size: 0.75rem; font-weight: 700; letter-spacing: 0.14em; text-transform: uppercase; }
.sms-finder .sms-finder__name { margin: 0.35rem 0 1rem; color: var(--sms-title); font-size: clamp(1.6rem, 1.2rem + 1.6vw, 2.5rem); font-weight: 800; line-height: 1.06; letter-spacing: -0.04em; }
.sms-finder .sms-finder__meta { display: flex; align-items: flex-start; gap: 0.6rem; min-width: 0; color: var(--sms-ink); font-weight: 600; }
.sms-finder .sms-finder__meta-icon { width: 1.3rem; height: 1.3rem; margin-top: 0.15rem; color: var(--sms-accent); }
.sms-finder .sms-finder__meta-text { min-width: 0; }
.sms-finder .sms-finder__text { margin-top: 0.75rem; color: var(--sms-ink-soft); }
.sms-finder .sms-finder__text p { margin: 0; }
.sms-finder .sms-finder__actions { display: flex; flex-wrap: wrap; gap: 0.75rem; min-width: 0; margin-top: auto; padding-top: 2rem; }
""" + _finder_css() + r"""
@media (min-width: 60em) {
  .sms-finder .sms-finder__grid { grid-template-columns: minmax(0, 1.3fr) minmax(0, 1fr); }
  .sms-finder .sms-finder__out { min-height: 26rem; }
}

/* ---------- Home: why Streamline bento ---------- */
.sms-why { padding: var(--sms-section) 0 calc(var(--sms-section) * 0.45); }
.sms-why .sms-why__inner { width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-why .sms-why__head { display: grid; gap: 1rem 3rem; align-items: end; margin-bottom: clamp(1.5rem, 1rem + 2vw, 2.5rem); }
.sms-why .sms-why__heading { min-width: 0; }
.sms-why .sms-why__title { margin: 0; color: var(--sms-title); font-size: clamp(1.9rem, 1.2rem + 2.6vw, 3.3rem); font-weight: 800; line-height: 1.06; letter-spacing: -0.04em; }
.sms-why .sms-why__lead { min-width: 0; max-width: 30rem; color: var(--sms-ink-soft); font-size: var(--sms-step-1); line-height: 1.55; }
.sms-why .sms-why__lead p { margin: 0; }
.sms-why .sms-why__grid { display: grid; grid-template-columns: minmax(0, 1fr); gap: var(--sms-gap); }
.sms-why .sms-why__trust { display: flex; flex-direction: column; gap: 0.5rem; padding: clamp(1.25rem, 1rem + 1vw, 1.75rem); }
.sms-why .sms-why__icon { width: 2.75rem; height: 2.75rem; margin-bottom: 1.5rem; padding: 0.65rem; border-radius: 0.95rem; background: var(--sms-mint); color: var(--sms-accent); }
.sms-why .sms-why__name { min-width: 0; margin: 0; color: var(--sms-title); font-size: var(--sms-step-1); font-weight: 800; line-height: 1.25; letter-spacing: -0.025em; }
.sms-why .sms-why__text { min-width: 0; margin: 0; color: var(--sms-ink-soft); font-size: var(--sms-step--1); line-height: 1.55; }
.sms-why .sms-why__tile--navy { border-color: transparent; background: """ + NAVY_BG + r"""; }
.sms-why .sms-why__quote { display: grid; gap: 0.55rem; margin: 0; padding: 0.55rem; }
.sms-why .sms-why__quote-media { position: relative; min-width: 0; min-height: 16rem; overflow: hidden; border-radius: var(--sms-inner-r); }
.sms-why .sms-why__quote-img { position: absolute; inset: 0; display: block; width: 100%; height: 100%; object-fit: cover; }
.sms-why .sms-why__quote-body { display: flex; flex-direction: column; min-width: 0; padding: clamp(1rem, 0.6rem + 1.6vw, 2.25rem); }
.sms-why .sms-why__quote-icon { width: 2.75rem; height: 2.75rem; padding: 0.6rem; border-radius: 0.95rem; background: var(--sms-mint); color: var(--sms-accent); }
.sms-why .sms-why__quote-text { min-width: 0; margin: 1.5rem 0 1.75rem; color: var(--sms-title); font-size: clamp(1.2rem, 1rem + 0.8vw, 1.6rem); font-weight: 600; line-height: 1.42; letter-spacing: -0.02em; }
.sms-why .sms-why__quote-text p { margin: 0; }
.sms-why .sms-why__cite { display: grid; gap: 0.1rem; min-width: 0; margin-top: auto; }
.sms-why .sms-why__cite-name { min-width: 0; color: var(--sms-title); font-weight: 800; }
.sms-why .sms-why__cite-role { min-width: 0; color: var(--sms-accent); font-size: var(--sms-step--1); font-weight: 600; }
.sms-why .sms-why__side { display: flex; flex-direction: column; gap: 0.5rem; padding: clamp(1.25rem, 1rem + 1vw, 1.9rem); }
.sms-why .sms-why__side-top { display: flex; align-items: center; justify-content: space-between; gap: 1rem; min-width: 0; margin-bottom: 1.25rem; }
.sms-why .sms-why__side-top .sms-why__icon { margin-bottom: 0; }
.sms-why .sms-why__tag { min-width: 0; color: var(--sms-ink-soft); font-size: 0.75rem; font-weight: 700; letter-spacing: 0.14em; text-transform: uppercase; }
.sms-why .sms-why__side .sms-arrowlink { position: relative; z-index: 4; align-self: flex-start; margin-top: auto; padding-top: 1rem; font-size: var(--sms-step--1); }
@media (max-width: 45.99em) {
  .sms-why .sms-why__trust { display: grid; grid-template-columns: auto minmax(0, 1fr); gap: 0.2rem 1rem; align-items: start; }
  .sms-why .sms-why__trust .sms-why__icon { grid-row: span 2; margin-bottom: 0; }
}
@media (min-width: 46em) {
  .sms-why .sms-why__grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
  .sms-why .sms-why__quote { grid-column: 1 / -1; grid-template-columns: minmax(0, 0.85fr) minmax(0, 1.15fr); }
}
@media (min-width: 60em) {
  .sms-why .sms-why__head { grid-template-columns: minmax(0, 1.3fr) minmax(0, 1fr); }
  .sms-why .sms-why__lead { justify-self: end; }
}
@media (min-width: 64em) {
  .sms-why .sms-why__grid { grid-template-columns: repeat(12, minmax(0, 1fr)); }
  .sms-why .sms-why__trust { grid-column: span 3; min-height: 15rem; }
  .sms-why .sms-why__quote { grid-column: span 8; grid-row: span 2; }
  .sms-why .sms-why__side { grid-column: span 4; }
}

/* ---------- Risk & Needs Consultancy: tiles that open ---------- */
.sms-cbento { padding: 0; }
.sms-cbento .sms-cbento__inner { width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-cbento .sms-cbento__head { display: grid; gap: 1rem 3rem; align-items: end; margin-bottom: clamp(1.5rem, 1rem + 2vw, 2.5rem); }
.sms-cbento .sms-cbento__heading { min-width: 0; }
.sms-cbento .sms-cbento__title { margin: 0; color: var(--sms-title); font-size: clamp(1.9rem, 1.2rem + 2.6vw, 3.3rem); font-weight: 800; line-height: 1.06; letter-spacing: -0.04em; }
.sms-cbento .sms-cbento__hint { min-width: 0; margin: 0; color: var(--sms-ink-soft); }
.sms-cbento .sms-cbento__grid { display: grid; grid-template-columns: minmax(0, 1fr); gap: var(--sms-gap); }
.sms-cbento .sms-cbento__tile { display: flex; flex-direction: column; padding: clamp(1.4rem, 1rem + 1.4vw, 2.25rem); }
.sms-cbento .sms-cbento__tile:has(.sms-cbento__more[open]) {""" + light.ISLAND + r"""  --sms-hl: rgba(255, 255, 255, 0.1); border-color: transparent; background-color: #061e35; }
.sms-cbento .sms-cbento__top { display: flex; align-items: center; justify-content: space-between; gap: 1rem; min-width: 0; }
.sms-cbento .sms-cbento__icon { width: 3rem; height: 3rem; padding: 0.7rem; border-radius: 1rem; background: var(--sms-mint); color: var(--sms-accent); }
.sms-cbento .sms-cbento__num { min-width: 0; color: var(--sms-ink-soft); font-size: var(--sms-step--1); font-weight: 800; letter-spacing: 0.06em; font-variant-numeric: tabular-nums; }
.sms-cbento .sms-cbento__name { min-width: 0; margin: 1.5rem 0 0.5rem; color: var(--sms-title); font-size: clamp(1.25rem, 1.1rem + 0.6vw, 1.65rem); font-weight: 800; line-height: 1.18; letter-spacing: -0.03em; }
.sms-cbento .sms-cbento__text { min-width: 0; max-width: 40rem; margin: 0; color: var(--sms-ink-soft); }
.sms-cbento .sms-cbento__more { min-width: 0; margin-top: auto; padding-top: 1.5rem; }
.sms-cbento .sms-cbento__toggle { display: inline-flex; align-items: center; gap: 0.6rem; padding: 0.6rem 0.75rem 0.6rem 1.1rem; border: 1px solid var(--sms-line); border-radius: 999px; color: var(--sms-ink); cursor: pointer; font-size: var(--sms-step--1); font-weight: 700; list-style: none; transition: background-color 0.3s, border-color 0.3s; }
.sms-cbento .sms-cbento__toggle::-webkit-details-marker { display: none; }
.sms-cbento .sms-cbento__toggle:hover { border-color: var(--sms-accent); }
.sms-cbento .sms-cbento__toggle-text { min-width: 0; }
.sms-cbento .sms-cbento__plus { width: 1.6rem; height: 1.6rem; padding: 0.3rem; border-radius: 50%; background: var(--sms-mint); color: var(--sms-accent); transition: transform 0.4s var(--sms-ease); }
.sms-cbento .sms-cbento__more[open] .sms-cbento__plus { transform: rotate(45deg); }
.sms-cbento .sms-cbento__body { padding-top: 1.1rem; color: var(--sms-ink-soft); }
.sms-cbento .sms-cbento__more[open] .sms-cbento__body { animation: sms-drop 0.45s var(--sms-ease) both; }
.sms-cbento .sms-cbento__body p { margin: 0 0 1rem; }
.sms-cbento .sms-cbento__list { display: grid; gap: 0.5rem; margin: 0; padding: 0; list-style: none; }
.sms-cbento .sms-cbento__item { display: flex; gap: 0.6rem; min-width: 0; color: var(--sms-ink); font-weight: 600; line-height: 1.45; }
.sms-cbento .sms-cbento__check { width: 1.2rem; height: 1.2rem; margin-top: 0.1rem; color: var(--sms-accent); }
.sms-cbento .sms-cbento__item-text { min-width: 0; }
@media (min-width: 46em) {
  .sms-cbento .sms-cbento__grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
}
@media (min-width: 60em) {
  .sms-cbento .sms-cbento__head { grid-template-columns: minmax(0, 1.4fr) minmax(0, 1fr); }
  .sms-cbento .sms-cbento__hint { justify-self: end; }
}
@media (min-width: 64em) {
  .sms-cbento .sms-cbento__grid { grid-template-columns: repeat(12, minmax(0, 1fr)); }
  .sms-cbento .sms-cbento__tile { grid-column: span 5; min-height: 17rem; }
  .sms-cbento .sms-cbento__tile--0,
  .sms-cbento .sms-cbento__tile--3,
  .sms-cbento .sms-cbento__tile--4 { grid-column: span 7; }
}
"""

RISE = [".sms-bento .sms-bento__hero", ".sms-phero .sms-phero__main"]
ENTRANCE = [".sms-bento .sms-bento__kicker", ".sms-bento .sms-bento__lead", ".sms-bento .sms-bento__actions",
            ".sms-phero .sms-phero__lead", ".sms-phero .sms-phero__actions"]
REVEAL = [".sms-bcta .sms-bcta__box", ".sms-why .sms-why__head", ".sms-cbento .sms-cbento__head"]
LOOP = [".sms-page .sms-tile--in", ".sms-page .sms-tile--in-t"] + [".sms-finder .sms-finder__p%d" % i for i in range(len(COURSES["items"]))]
TRANS = [".sms-page .sms-tile", ".sms-page .sms-glare", ".sms-bento .sms-bento__svc-img", ".sms-bento .sms-bento__svc-list",
         ".sms-bento .sms-bento__svc-go", ".sms-bento .sms-bento__contact-link", ".sms-finder .sms-finder__chip", ".sms-finder .sms-finder__chip-icon",
         ".sms-cbento .sms-cbento__toggle", ".sms-cbento .sms-cbento__plus"]
OPEN = [".sms-cbento .sms-cbento__more[open] .sms-cbento__body"]

SKIP = {"medical-training": [0], "risk-needs-consultancy": [0, 1]}


def _shield(ctx, cls):
    return '<img class="%s" src="%s" alt="" width="378" height="399" aria-hidden="true">' % (cls, ctx.asset("streamline-shield-white.png"))


# ---------------------------------------------------------------------------
# Chrome, page hero, CTA
# ---------------------------------------------------------------------------

def chrome_top(ctx):
    return header(ctx, "blue")


def chrome_bottom(ctx):
    return footer(ctx, "white")


def page_hero(ctx, h):
    sub = '<div class="sms-phero__sub">%s</div>' % e(h["sub"]) if h.get("sub") else ""
    acts = '<div class="sms-phero__actions">%s</div>' % buttons(ctx, h["buttons"]) if h.get("buttons") else ""
    chips_html = "".join('<li class="sms-phero__item">%s<span class="sms-phero__item-text">%s</span></li>' % (icon(ic, "sms-phero__item-icon"), e(t)) for ic, t in h.get("chips", []))
    return """<section class="sms-phero">
  <div class="sms-phero__inner">
    <div class="sms-phero__grid">
      <div class="sms-tile sms-phero__main">
        <div class="sms-phero__crumb"><a class="sms-phero__crumb-link" href="%s">Home</a> / %s</div>
        <div class="sms-kicker sms-phero__kicker">%s</div>
        <h1 class="sms-phero__title">%s</h1>
        <div class="sms-phero__lead">%s%s</div>
        %s
      </div>
      <div class="sms-tile sms-tile--in-t sms-phero__photo" style="--sms-i: 1" data-sms-tilt>%s</div>
      <div class="sms-tile sms-tile--in sms-phero__chips sms-phero__tile--navy" style="--sms-i: 2" data-sms-tilt>
        <p class="sms-tile__label">At a glance</p>
        <ul class="sms-phero__list">%s</ul>
      </div>
    </div>
  </div>
</section>
""" % (ctx.href("home"), e(LABEL[ctx.slug]), e(h["eyebrow"]), e(h["title"]), sub, paras(h["body"]), acts,
       photo_img(ctx, h["photo"], "sms-phero__img", lazy=False), chips_html)


def cta(ctx, d):
    btns = [(l, t) for l, t in d["buttons"] if t != "tel"]
    return """<section class="sms-bcta">
  <div class="sms-bcta__inner">
    <div class="sms-bcta__box">
      %s
      <div class="sms-bcta__copy"><h2 class="sms-bcta__title">%s</h2><div class="sms-bcta__text">%s</div></div>
      <div class="sms-bcta__side"><div class="sms-bcta__actions">%s</div><div class="sms-bcta__call">Or call us on <a href="tel:%s">%s</a></div></div>
    </div>
  </div>
</section>
""" % (_shield(ctx, "sms-bcta__shield"), e(d["title"]), paras(d["text"]), buttons(ctx, btns) if btns else "", PHONE_TEL, PHONE)


# ---------------------------------------------------------------------------
# Signature pieces
# ---------------------------------------------------------------------------

def finder(ctx, page=False):
    items = COURSES["items"]
    radios = "".join('<input class="sms-finder__radio sms-finder__r%d" type="radio" name="sms-course" id="sms-course-%d"%s>' % (
        i, i, " checked" if i == 0 else "") for i in range(len(items)))
    chips_html = "".join('<label class="sms-finder__chip sms-finder__chip--%d" for="sms-course-%d">%s<span class="sms-finder__chip-text">%s</span></label>' % (
        i, i, icon(it.get("icon", "check"), "sms-finder__chip-icon"), e(it["title"])) for i, it in enumerate(items))
    panels = ""
    for i, it in enumerate(items):
        meta = '<div class="sms-finder__meta">%s<span class="sms-finder__meta-text">%s</span></div>' % (icon("clock", "sms-finder__meta-icon"), e(it["meta"])) if it.get("meta") else ""
        text = '<div class="sms-finder__text"><p>%s</p></div>' % e(it["text"]) if it.get("text") else ""
        panels += '<div class="sms-finder__p%d"><div class="sms-finder__panel">%s<div class="sms-finder__label">Selected course</div><h3 class="sms-finder__name">%s</h3>%s%s</div></div>' % (
            i, icon(it.get("icon", "check"), "sms-finder__panel-icon"), e(it["title"]), meta, text)
    btns = [("Book your next training session", "book:training"), ("View our training catalogue of courses", C.CATALOGUE)]
    return """<section class="sms-finder%s" id="courses">
  <div class="sms-finder__inner">
    <div class="sms-tile sms-finder__tile" data-sms-rise>
      %s
      <div class="sms-finder__grid">
        <div class="sms-finder__pick">
          <div class="sms-kicker">Course finder</div>
          <h2 class="sms-finder__title">%s</h2>
          <div class="sms-finder__lead"><p>%s</p></div>
          <div class="sms-finder__chips" role="group" aria-label="Choose a course">%s</div>
        </div>
        <div class="sms-finder__out" aria-live="polite">
          %s
          <div class="sms-finder__actions">%s</div>
        </div>
      </div>
    </div>
  </div>
</section>
""" % (" sms-finder--page" if page else "", radios, e(COURSES["title"]), e(COURSES["lead"][0]), chips_html, panels, buttons(ctx, btns))


def consult(ctx):
    tiles = ""
    for i, it in enumerate(CONSULT["items"]):
        first, rest = split_first(it["text"])
        lst = "".join('<li class="sms-cbento__item">%s<span class="sms-cbento__item-text">%s</span></li>' % (icon("check", "sms-cbento__check"), e(x)) for x in it["list"])
        body = ("<p>%s</p>" % e(rest) if rest else "") + '<ul class="sms-cbento__list">%s</ul>' % lst
        tiles += """<article class="sms-tile sms-cbento__tile sms-cbento__tile--%d" data-sms-rise>
        <div class="sms-cbento__top">%s<span class="sms-cbento__num" aria-hidden="true">%02d</span></div>
        <h3 class="sms-cbento__name">%s</h3>
        <p class="sms-cbento__text">%s</p>
        <details class="sms-cbento__more"><summary class="sms-cbento__toggle"><span class="sms-cbento__toggle-text">%s</span>%s</summary><div class="sms-cbento__body">%s</div></details>
      </article>""" % (i, icon(it["icon"], "sms-cbento__icon"), i + 1, e(it["title"]), e(first), e(it["list_title"]), icon("plus", "sms-cbento__plus"), body)
    return """<section class="sms-cbento" id="services">
  <div class="sms-cbento__inner">
    <div class="sms-cbento__head">
      <div class="sms-cbento__heading"><h2 class="sms-cbento__title">%s</h2></div>
      <p class="sms-cbento__hint">Open a service to see what it includes.</p>
    </div>
    <div class="sms-cbento__grid">%s</div>
  </div>
</section>
""" % (e(CONSULT["title"]), tiles)


def inner_extra(ctx, slug):
    if slug == "medical-training":
        return finder(ctx, page=True)
    if slug == "risk-needs-consultancy":
        # keep the page order: the "Safety Starts by Recognising Danger" feature, then the services bento
        return SHARED_RENDERERS["feature"](ctx, C.PAGES[slug]["sections"][0][1]) + consult(ctx)
    return ""


# ---------------------------------------------------------------------------
# Homepage
# ---------------------------------------------------------------------------

def hero_bento(ctx):
    svcs = ""
    for i, s in enumerate(C.SERVICES):
        lst = "".join('<li class="sms-bento__svc-item">%s<span class="sms-bento__svc-item-text">%s</span></li>' % (icon(ic, "sms-bento__svc-item-icon"), e(t)) for ic, t in s["list"])
        svcs += """<article class="sms-tile sms-tile--in sms-bento__svc" style="--sms-i: %d" data-sms-tilt>
        <div class="sms-bento__svc-media">%s<ul class="sms-bento__svc-list">%s</ul></div>
        <div class="sms-bento__svc-body">
          <div class="sms-bento__svc-top">%s<span class="sms-bento__svc-go" aria-hidden="true">%s</span></div>
          <h2 class="sms-bento__svc-title"><a class="sms-bento__svc-link" href="%s">%s</a></h2>
          <p class="sms-bento__svc-text">%s</p>
          <span class="sms-bento__svc-more" aria-hidden="true">Find out more&nbsp;<span class="sms-arrow">&rarr;</span></span>
        </div>
      </article>
""" % (i + 2, photo_img(ctx, s["photo"], "sms-bento__svc-img", lazy=False), lst, icon(s["icon"], "sms-bento__svc-icon"),
           icon("arrow", "sms-bento__svc-go-icon"), ctx.href(s["slug"]), e(s["title"]), e(s["text"]))
    return """<section class="sms-bento">
  <div class="sms-bento__inner">
    <div class="sms-bento__grid">
      <div class="sms-tile sms-bento__hero sms-bento__tile--navy">
        %s
        <div class="sms-kicker sms-bento__kicker">%s</div>
        <h1 class="sms-bento__title">Clinician-led safety and <span class="sms-mark">medical support</span></h1>
        <div class="sms-bento__lead"><p>%s</p></div>
        <div class="sms-bento__actions">%s</div>
      </div>
      <div class="sms-tile sms-tile--in-t sms-bento__photo" style="--sms-i: 1" data-sms-tilt>
        %s
        <span class="sms-bento__chip">%s<span class="sms-bento__chip-text">Clinician-led</span></span>
      </div>
      %s
      <div class="sms-tile sms-tile--in sms-bento__qual" style="--sms-i: 5" data-sms-tilt>
        <img class="sms-bento__qual-badge" src="%s" alt="" width="1000" height="982" loading="lazy">
        <div class="sms-bento__qual-body"><p class="sms-bento__qual-name">Qualsafe Registered Centre</p><p class="sms-bento__qual-no">Centre No. 908578</p></div>
      </div>
      <div class="sms-tile sms-tile--in sms-bento__claim" style="--sms-i: 6" data-sms-tilt>
        %s<p class="sms-bento__claim-text">%s</p>
      </div>
      <div class="sms-tile sms-tile--in sms-bento__area" style="--sms-i: 7" data-sms-tilt>
        <span class="sms-bento__rings" aria-hidden="true"><span class="sms-bento__ring"></span><span class="sms-bento__ring sms-bento__ring--2"></span><span class="sms-bento__ring sms-bento__ring--3"></span></span>
        %s
        <p class="sms-tile__label">Where we work</p>
        <p class="sms-bento__area-text">%s</p>
      </div>
      <div class="sms-tile sms-tile--in sms-bento__contact" style="--sms-i: 8" data-sms-tilt>
        <div class="sms-bento__contact-head"><p class="sms-tile__label">Contact Us</p><p class="sms-bento__contact-title">Have any questions? We&rsquo;re here to help.</p></div>
        <div class="sms-bento__contact-links">
          <a class="sms-bento__contact-link" href="tel:%s">%s<span class="sms-bento__contact-text">%s</span></a>
          <a class="sms-bento__contact-link" href="mailto:%s">%s<span class="sms-bento__contact-text">%s</span></a>
        </div>
      </div>
    </div>
  </div>
</section>
""" % (_shield(ctx, "sms-bento__shield"), e(C.STRAP), e(C.INTRO2), buttons(ctx, [("Book online", "book"), ("Contact Us", "contact")]),
       photo_img(ctx, "team", "sms-bento__photo-img", lazy=False), icon("heart", "sms-bento__chip-icon"), svcs,
       ctx.asset("whatsapp-image-2026-07-20-at-12.27.35.jpeg"), icon("heart", "sms-bento__claim-icon"), e(C.CLAIM_15),
       icon("pin", "sms-bento__area-icon"), e(C.AREA),
       PHONE_TEL, icon("phone", "sms-bento__contact-icon"), PHONE, EMAIL, icon("mail", "sms-bento__contact-icon"), EMAIL)


def why(ctx):
    trust = "".join('<div class="sms-tile sms-why__trust" data-sms-tilt data-sms-rise>%s<h3 class="sms-why__name">%s</h3><p class="sms-why__text">%s</p></div>' % (
        icon(ic, "sms-why__icon"), e(t), e(x)) for ic, t, x in C.TRUST)
    rec = C.PAGES["recruitment"]["hero"]
    return """<section class="sms-why">
  <div class="sms-why__inner">
    <div class="sms-why__head">
      <div class="sms-why__heading"><div class="sms-kicker">Why Streamline</div><h2 class="sms-why__title">%s</h2></div>
      <div class="sms-why__lead"><p>%s</p></div>
    </div>
    <div class="sms-why__grid">
      %s
      <figure class="sms-tile sms-why__quote sms-why__tile--navy" data-sms-rise>
        <div class="sms-why__quote-media">%s</div>
        <div class="sms-why__quote-body">
          %s
          <blockquote class="sms-why__quote-text"><p>%s</p></blockquote>
          <figcaption class="sms-why__cite"><span class="sms-why__cite-name">%s</span><span class="sms-why__cite-role">Director</span></figcaption>
        </div>
      </figure>
      <div class="sms-tile sms-why__side" data-sms-tilt data-sms-rise>
        <div class="sms-why__side-top">%s<span class="sms-why__tag">Career support</span></div>
        <h3 class="sms-why__name">%s</h3>
        <p class="sms-why__text">%s</p>
        <a class="sms-arrowlink" href="%s">%s&nbsp;<span class="sms-arrow" aria-hidden="true">&rarr;</span></a>
      </div>
      <div class="sms-tile sms-why__side" data-sms-tilt data-sms-rise>
        <div class="sms-why__side-top">%s<span class="sms-why__tag">%s</span></div>
        <h3 class="sms-why__name">%s</h3>
        <p class="sms-why__text">%s</p>
        <a class="sms-arrowlink" href="%s">Visit Recruitment&nbsp;<span class="sms-arrow" aria-hidden="true">&rarr;</span></a>
      </div>
    </div>
  </div>
</section>
""" % (e(C.WORKING_WITH["title"]), e(C.WORKING_WITH["body"][1]), trust,
       photo_img(ctx, "directors", "sms-why__quote-img"), icon("quote", "sms-why__quote-icon"), e(C.MATHEW_QUOTE), e(C.DIRECTORS[0]["name"]),
       icon(C.CAREERS["icon"], "sms-why__icon"), e(C.CAREERS["title"]), e(C.CAREERS["text"]), ctx.href(C.CAREERS["slug"]), e(C.CAREERS["cta"]),
       icon("users", "sms-why__icon"), e(rec["eyebrow"]), e(rec["title"]), e(rec["body"][0]), ctx.href("recruitment"))


def home(ctx):
    ctx.notes.append("Image-only copy used: \"Clinician-led safety and medical support\" (clinician-led-safety.png)")
    ctx.notes.append("Image-only copy used: \"Mathew and Tom bring over 15 years of ambulance experience...\" (why-choose-us.png - use approved)")
    out = hero_bento(ctx)
    out += finder(ctx)
    out += why(ctx)
    picks = ["Where is Streamline based?", "Who runs Streamline?", "Can Streamline provide more than one service?", "Do you offer a free initial discussion?", "Are you insured?", "How can I contact Streamline?"]
    allf = dict(C.faqs("home"))
    out += SHARED_RENDERERS["faq"](ctx, {"eyebrow": C.STRAP, "title": "General Streamline [[FAQs]]",
                                        "lead": ["Answers to common questions about Streamline Safety & Medical Solutions, our team, services, bookings and how we work."],
                                        "items": [(q, allf[q]) for q in picks], "show": 6})
    out += cta(ctx, {"title": "Have any questions? We’re here to help.",
                     "text": ["We offer an initial discussion to understand your requirements, and our risk and needs consultancy includes a free initial consultation before any chargeable work is agreed."],
                     "buttons": [("Book online", "book"), ("Contact Us", "contact")]})
    return out


# ---------------------------------------------------------------------------
# Script: staggered tile assembly on scroll, pointer tilt with a soft glare
# ---------------------------------------------------------------------------

JS = """<script>
(function () {
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var fine = window.matchMedia('(hover: hover) and (pointer: fine)').matches;
  var each = function (sel, fn) { Array.prototype.forEach.call(document.querySelectorAll(sel), fn); };

  /* Tiles below the fold assemble in a short stagger as they scroll in */
  if (!reduce && 'IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      var n = 0;
      entries.forEach(function (en) {
        if (!en.isIntersecting) { return; }
        var t = en.target;
        io.unobserve(t);
        t.style.transitionDelay = (Math.min(n, 5) * 80) + 'ms';
        n += 1;
        t.classList.remove('is-armed');
        window.setTimeout(function () { t.style.transitionDelay = ''; }, 1500);
      });
    }, { rootMargin: '0px 0px -6% 0px', threshold: 0.1 });
    var vh = window.innerHeight;
    each('[data-sms-rise]', function (t) {
      if (t.getBoundingClientRect().top < vh * 0.94) { return; }
      t.classList.add('is-armed');
      io.observe(t);
    });
  }

  /* Pointer tilt (transform only, fine pointers, never with reduced motion) */
  if (!fine || reduce) { return; }
  each('[data-sms-tilt]', function (el) {
    var glare = document.createElement('span');
    glare.className = 'sms-glare';
    glare.setAttribute('aria-hidden', 'true');
    el.appendChild(glare);
    var tx = 0, ty = 0, cx = 0, cy = 0, gx = 0, gy = 0, max = 6, raf = 0, inside = false;
    var tick = function () {
      cx += (tx - cx) * 0.16;
      cy += (ty - cy) * 0.16;
      var done = Math.abs(tx - cx) < 0.002 && Math.abs(ty - cy) < 0.002;
      if (!inside && done) {
        el.style.transform = '';
        el.classList.remove('is-tilting');
        raf = 0;
        return;
      }
      el.style.transform = 'perspective(1100px) rotateX(' + (-cy * max).toFixed(2) + 'deg) rotateY(' + (cx * max).toFixed(2) + 'deg)';
      glare.style.transform = 'translate3d(' + gx.toFixed(1) + 'px, ' + gy.toFixed(1) + 'px, 0)';
      raf = done ? 0 : window.requestAnimationFrame(tick);
    };
    var kick = function () { if (!raf) { raf = window.requestAnimationFrame(tick); } };
    el.addEventListener('pointerenter', function (ev) {
      if (ev.pointerType && ev.pointerType !== 'mouse') { return; }
      var r = el.getBoundingClientRect();
      max = Math.max(1.5, Math.min(6, 6 * 380 / Math.max(r.width, r.height, 1)));
      inside = true;
      el.classList.add('is-tilting', 'is-hover');
    });
    el.addEventListener('pointermove', function (ev) {
      if (!inside) { return; }
      var r = el.getBoundingClientRect();
      var px = (ev.clientX - r.left) / r.width, py = (ev.clientY - r.top) / r.height;
      tx = Math.max(-1, Math.min(1, px * 2 - 1));
      ty = Math.max(-1, Math.min(1, py * 2 - 1));
      gx = ev.clientX - r.left;
      gy = ev.clientY - r.top;
      kick();
    }, { passive: true });
    el.addEventListener('pointerleave', function () {
      inside = false;
      tx = 0;
      ty = 0;
      el.classList.remove('is-hover');
      kick();
    });
  });
})();
</script>
"""


def scripts(ctx, main):
    return JS if ("data-sms-tilt" in main or "data-sms-rise" in main) else ""
