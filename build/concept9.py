"""Concept 9 - Blueprint. A precise, calm planning aesthetic for a safety and medical
planning company: light grid-paper backgrounds, navy line drawings, IBM Plex Mono
reference labels, measurement ticks and crosshair corner marks on every frame.

Signature pieces: an interactive event site plan that draws itself line by line and
opens callouts from numbered hotspots (homepage and Event Medical Cover), services
as technical spec sheets that outline themselves on hover, and a workplace floor
plan for the First Aid Needs Assessment (Risk & Needs Consultancy). Every hotspot
has a plain list twin, so all of it works without JavaScript and on small screens.
"""
from common import *  # noqa: F401,F403
import content as C

NAME = "Blueprint"
FONTS = "https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=Space+Grotesk:wght@400;500;600;700&display=swap"

NAVY = "#061e35"
GREEN = "#407f36"
INK = "#405365"
MINT = "#dcefd6"

# ---------------------------------------------------------------------------
# Content pulled straight from content.py
# ---------------------------------------------------------------------------
EVENT = C.PAGES["event-medical-cover"]
BOOKING = EVENT["sections"][2][1]                       # "Book Your Event Medical Cover" feature
QUOTE = BOOKING["chips"]                                 # What information is needed for a quote?
CONSULT_CARDS = C.PAGES["risk-needs-consultancy"]["sections"][1][1]["items"]
FANA = CONSULT_CARDS[0]                                  # First Aid Needs Assessment
EMP = CONSULT_CARDS[3]                                   # Event Medical Plans


def _factors():
    """The eight factors named in the First Aid Needs Assessment card, verbatim."""
    part = FANA["text"].split("We consider ", 1)[1].rstrip(".")
    bits = part.split(", ")
    bits = bits[:-1] + bits[-1].split(" and ", 1)
    return [b[0].upper() + b[1:] for b in bits]


FACTORS = _factors()
VISIT = {it["link"]: it["go"] for it in C.PAGES["contact"]["sections"][1][1]["items"]}


# ---------------------------------------------------------------------------
# CSS helpers: crosshair corner marks and grid paper
# ---------------------------------------------------------------------------
def cross(c, a=9):
    """Background layers that draw a small crosshair on each corner of a box
    whose pseudo element is inset by -a px."""
    g = "linear-gradient(%s, %s)" % (c, c)
    d = 2 * a
    parts = [
        "%s 0 %dpx / %dpx 1px" % (g, a, d), "%s %dpx 0 / 1px %dpx" % (g, a, d),
        "%s 100%% %dpx / %dpx 1px" % (g, a, d), "%s calc(100%% - %dpx) 0 / 1px %dpx" % (g, a, d),
        "%s 0 calc(100%% - %dpx) / %dpx 1px" % (g, a, d), "%s %dpx 100%% / 1px %dpx" % (g, a, d),
        "%s 100%% calc(100%% - %dpx) / %dpx 1px" % (g, a, d), "%s calc(100%% - %dpx) 100%% / 1px %dpx" % (g, a, d),
    ]
    return ", ".join(p + " no-repeat" for p in parts)


def grid(major, minor, base, big=96, small=24):
    return ("linear-gradient(%s 1px, transparent 1px) 0 0 / %dpx %dpx, linear-gradient(90deg, %s 1px, transparent 1px) 0 0 / %dpx %dpx, "
            "linear-gradient(%s 1px, transparent 1px) 0 0 / %dpx %dpx, linear-gradient(90deg, %s 1px, transparent 1px) 0 0 / %dpx %dpx, %s") % (
        major, big, big, major, big, big, minor, small, small, minor, small, small, base)


GRID_LIGHT = grid("rgba(217, 226, 231, 0.85)", "rgba(220, 239, 214, 0.75)", "#ffffff")
GRID_PALE = grid("rgba(217, 226, 231, 0.9)", "rgba(217, 226, 231, 0.42)", "#f4f8f3")
GRID_NAVY_SOFT = grid("rgba(130, 208, 110, 0.07)", "rgba(255, 255, 255, 0.03)", "transparent")
GRID_NAVY = grid("rgba(130, 208, 110, 0.12)", "rgba(255, 255, 255, 0.045)", "transparent")

EYEBROWS = [".sms-feature .sms-feature__eyebrow", ".sms-cards .sms-cards__eyebrow", ".sms-steps .sms-steps__eyebrow", ".sms-checklist .sms-checklist__eyebrow",
            ".sms-faq .sms-faq__eyebrow", ".sms-quotes .sms-quotes__eyebrow", ".sms-people .sms-people__eyebrow", ".sms-contact .sms-contact__eyebrow",
            ".sms-links .sms-links__eyebrow", ".sms-marquee .sms-marquee__eyebrow", ".sms-booking .sms-booking__eyebrow",
            ".sms-bphero .sms-bphero__eyebrow", ".sms-bpage .sms-bpage__eyebrow", ".sms-bpspec .sms-bpspec__eyebrow", ".sms-bpplan .sms-bpplan__eyebrow",
            ".sms-bpvalues .sms-bpvalues__eyebrow"]
TITLES = [".sms-feature .sms-feature__title", ".sms-cards .sms-cards__title", ".sms-steps .sms-steps__title", ".sms-checklist .sms-checklist__title",
          ".sms-faq .sms-faq__title", ".sms-quotes .sms-quotes__title", ".sms-people .sms-people__title", ".sms-contact .sms-contact__title",
          ".sms-links .sms-links__title", ".sms-marquee .sms-marquee__title", ".sms-booking .sms-booking__title",
          ".sms-bpspec .sms-bpspec__title", ".sms-bpplan .sms-bpplan__title", ".sms-bpvalues .sms-bpvalues__title"]

CSS = r"""
/* ===== Concept 9 theme: Blueprint ===== */
.sms-page { --sms-font: "Space Grotesk", "Montserrat", Arial, sans-serif; --sms-mono: "IBM Plex Mono", ui-monospace, "SFMono-Regular", Menlo, Consolas, monospace; --sms-radius: 0.375rem; --sms-radius-sm: 0.25rem; --sms-shadow: none; --sms-shadow-lg: none; --sms-ease: cubic-bezier(0.2, 0.7, 0.2, 1); --sms-step-2: clamp(1.75rem, 1.3rem + 1.7vw, 2.75rem); letter-spacing: -0.003em; }
.sms-page .sms-mark { color: var(--sms-green); }
.sms-page .sms-btn { padding: 0.9rem 1.3rem; border-width: 1.5px; border-radius: 0.25rem; font-weight: 600; letter-spacing: 0.005em; transition: transform 0.25s var(--sms-ease), background-color 0.25s, border-color 0.25s, color 0.25s; }
.sms-page .sms-btn:hover { transform: translateY(-2px); }
.sms-page .sms-btn--primary { box-shadow: none; }
.sms-page .sms-btn--primary:hover { border-color: var(--sms-navy); background: var(--sms-navy); }
.sms-page .sms-chips__item { padding: 0.45rem 0.85rem 0.45rem 0.5rem; border: 1px solid var(--sms-line); border-radius: 0.25rem; background: var(--sms-white); box-shadow: none; font-weight: 500; }
.sms-page .sms-chips__icon { border-radius: 0.2rem; }
.sms-feature.sms-tone-white .sms-chips__item { background: var(--sms-white); }
.sms-page .sms-photo { border-radius: 0.25rem; }
.sms-page .sms-more__toggle { font-family: var(--sms-mono); font-size: 0.8125rem; font-weight: 500; letter-spacing: 0.08em; text-transform: uppercase; }
.sms-page .sms-watermark { display: none; }

/* Header */
.sms-header { border-bottom: 1px solid var(--sms-line); background: rgba(255, 255, 255, 0.96); }
.sms-header .sms-header__link { border-radius: 0.25rem; font-weight: 500; }
.sms-header .sms-header__link::after { bottom: 0.15rem; height: 1px; border-radius: 0; }
.sms-header .sms-header__summary { border: 1px solid var(--sms-line); border-radius: 0.25rem; background: var(--sms-white); font-family: var(--sms-mono); font-weight: 500; letter-spacing: 0.08em; text-transform: uppercase; }
.sms-header .sms-header__panel { border: 1px solid var(--sms-line); border-radius: 0.375rem; box-shadow: 0 18px 40px rgba(6, 30, 53, 0.1); }
.sms-header .sms-header__panel-link { border-radius: 0.25rem; font-weight: 500; }

/* Section heads (shared and Blueprint blocks) */
@EYEBROWS@ { display: inline-flex; align-items: center; gap: 0.6rem; margin-bottom: 1rem; color: var(--sms-ink-soft); font-family: var(--sms-mono); font-size: 0.8125rem; font-weight: 500; letter-spacing: 0.12em; line-height: 1.4; text-transform: uppercase; }
@EYEBROWS_BEFORE@ { content: ""; flex: 0 0 auto; width: 1.4rem; height: 9px; border-left: 1px solid var(--sms-green); border-right: 1px solid var(--sms-green); border-radius: 0; background: linear-gradient(var(--sms-green), var(--sms-green)) center / 100% 1px no-repeat; }
@TITLES@ { font-weight: 600; line-height: 1.12; letter-spacing: -0.028em; }

/* ---------- Shared sections restyled ---------- */
.sms-feature .sms-feature__frame { box-shadow: none; }
.sms-feature .sms-feature__media::after { content: ""; position: absolute; z-index: 2; inset: -9px; background: @CROSS_NAVY@; pointer-events: none; }
.sms-feature .sms-feature__blob { inset: 0.75rem -0.75rem -0.75rem 0.75rem; width: auto; aspect-ratio: auto; border: 1px solid var(--sms-line); border-radius: 0; background: @GRID_LIGHT@; animation: none; }
.sms-feature.sms-feature--flip .sms-feature__blob { inset: 0.75rem 0.75rem -0.75rem -0.75rem; }
.sms-feature .sms-feature__lead { font-weight: 400; }
.sms-feature .sms-feature__strap { border: 1px solid var(--sms-line-green); border-radius: 0.25rem; background: var(--sms-pale-2); font-weight: 600; }
.sms-feature .sms-feature__chips-title { font-weight: 600; }
@media (min-width: 56em) {
  .sms-feature .sms-feature__blob { inset: 1.25rem -1.25rem -1.25rem 1.25rem; }
  .sms-feature.sms-feature--flip .sms-feature__blob { inset: 1.25rem 1.25rem -1.25rem -1.25rem; }
}

.sms-cards .sms-cards__item { border: 1px solid var(--sms-line); border-radius: var(--sms-radius); background: var(--sms-white); box-shadow: none; transition: border-color 0.3s; }
.sms-cards.sms-tone-white .sms-cards__item { background: var(--sms-white); }
.sms-cards .sms-cards__item:hover { border-color: var(--sms-green); transform: none; }
.sms-cards .sms-cards__icon { width: 2.75rem; height: 2.75rem; padding: 0.6rem; border-radius: 0.25rem; }
.sms-cards.sms-tone-white .sms-cards__icon { background: var(--sms-mint); }
.sms-cards .sms-cards__item:hover .sms-cards__icon { transform: none; }
.sms-cards .sms-cards__num { color: var(--sms-ink-soft); font-family: var(--sms-mono); font-size: 0.875rem; font-weight: 500; letter-spacing: 0.08em; }
.sms-cards .sms-cards__name { font-weight: 600; letter-spacing: -0.015em; }
.sms-cards .sms-cards__meta { border: 1px solid var(--sms-line); border-radius: 0.2rem; background: var(--sms-pale); font-family: var(--sms-mono); font-size: 0.75rem; font-weight: 500; }
.sms-cards.sms-tone-white .sms-cards__meta { background: var(--sms-pale); }
.sms-cards .sms-cards__list-title { font-family: var(--sms-mono); font-size: 0.75rem; font-weight: 500; letter-spacing: 0.1em; }
.sms-cards .sms-cards__list-item { border-top: 1px solid var(--sms-line); }

.sms-steps .sms-steps__line { width: 1px; background: var(--sms-line); }
.sms-steps .sms-steps__line-fill { border-radius: 0; }
.sms-steps .sms-steps__badge { border: 1.5px solid var(--sms-navy); border-radius: 0.25rem; background: var(--sms-white); color: var(--sms-green); }
.sms-steps .sms-steps__num { border-radius: 0.2rem; font-family: var(--sms-mono); font-weight: 500; }
.sms-steps .sms-steps__name { font-weight: 600; }
.sms-steps .sms-steps__note { border: 1px solid var(--sms-line); border-radius: 0.25rem; background: var(--sms-white); }
.sms-steps.sms-tone-white .sms-steps__note { background: var(--sms-pale); }
@media (min-width: 60em) {
  .sms-steps .sms-steps__line { width: auto; height: 1px; }
}

.sms-checklist .sms-checklist__item { border: 1px solid var(--sms-line); border-radius: var(--sms-radius); background: var(--sms-white); font-weight: 500; }
.sms-checklist .sms-checklist__item:hover { border-color: var(--sms-green); transform: none; }
.sms-checklist .sms-checklist__icon { border-radius: 0.25rem; background: var(--sms-mint); }

.sms-notice .sms-notice__box { border: 1px solid var(--sms-line); border-radius: var(--sms-radius); box-shadow: none; }
.sms-notice .sms-notice__badge { border-radius: 0.25rem; }
.sms-notice .sms-notice__label { color: var(--sms-ink-soft); font-family: var(--sms-mono); font-weight: 500; }
.sms-notice .sms-notice__title { font-weight: 600; }

.sms-faq .sms-faq__list { counter-reset: sms-bpq; }
.sms-faq .sms-faq__item { margin-bottom: 0.5rem; border: 1px solid var(--sms-line); border-radius: 0.25rem; background: var(--sms-white); box-shadow: none; counter-increment: sms-bpq; transition: border-color 0.3s; }
.sms-faq.sms-tone-white .sms-faq__item { background: var(--sms-white); }
.sms-faq .sms-faq__item[open] { border-color: var(--sms-navy); }
.sms-faq .sms-faq__q { display: flex; gap: 0.9rem; padding: 1.05rem 3.5rem 1.05rem 1.1rem; font-weight: 500; }
.sms-faq .sms-faq__q::before { content: "Q" counter(sms-bpq, decimal-leading-zero); flex: 0 0 auto; padding-top: 0.2rem; color: var(--sms-ink-soft); font-family: var(--sms-mono); font-size: 0.75rem; font-weight: 500; letter-spacing: 0.06em; }
.sms-faq .sms-faq__q::after { border: 1px solid var(--sms-line); border-radius: 0.2rem; background: var(--sms-pale); color: var(--sms-navy); font-family: var(--sms-mono); font-size: 1.1rem; }
.sms-faq .sms-faq__a { padding: 0 1.25rem 1.25rem 3.85rem; }
.sms-faq .sms-faq__input { border-radius: 0.25rem; }
.sms-faq .sms-faq__all-toggle { border-width: 1.5px; border-radius: 0.25rem; font-family: var(--sms-mono); font-weight: 500; letter-spacing: 0.08em; text-transform: uppercase; }

.sms-quotes .sms-quotes__item { border: 1px solid var(--sms-line); border-radius: var(--sms-radius); background: var(--sms-white); }
.sms-quotes .sms-quotes__item::after { content: ""; position: absolute; inset: -9px; background: @CROSS_LINE@; pointer-events: none; }
.sms-quotes .sms-quotes__icon { border-radius: 0.25rem; background: var(--sms-mint); }
.sms-quotes .sms-quotes__label { color: var(--sms-ink-soft); font-family: var(--sms-mono); font-weight: 500; }
.sms-quotes .sms-quotes__text { font-weight: 500; }

.sms-people .sms-people__frame { box-shadow: none; }
.sms-people .sms-people__person { border: 1px solid var(--sms-line); border-radius: var(--sms-radius); box-shadow: none; }
.sms-people.sms-tone-white .sms-people__person { background: var(--sms-white); }
.sms-people .sms-people__role { border-radius: 0.2rem; font-family: var(--sms-mono); font-size: 0.75rem; font-weight: 500; letter-spacing: 0.08em; text-transform: uppercase; }
.sms-people .sms-people__name { font-weight: 600; }
.sms-people .sms-people__shared { position: relative; isolation: isolate; overflow: hidden; border-radius: var(--sms-radius); }
.sms-people .sms-people__shared::before { content: ""; position: absolute; z-index: -1; inset: 0; background: @GRID_NAVY@; pointer-events: none; }
.sms-people .sms-people__shared-label { font-family: var(--sms-mono); font-weight: 500; }

.sms-links .sms-links__link { border: 1px solid var(--sms-line); border-radius: var(--sms-radius); box-shadow: none; transition: border-color 0.3s; }
.sms-links .sms-links__link:hover { border-color: var(--sms-green); transform: none; }
.sms-links .sms-links__icon { border-radius: 0.25rem; }
.sms-links .sms-links__name { font-weight: 600; }
.sms-links .sms-links__go { font-family: var(--sms-mono); font-weight: 500; letter-spacing: 0.04em; }

.sms-claim .sms-claim__icon { border-radius: 0.25rem; }
.sms-claim .sms-claim__text { font-weight: 500; letter-spacing: -0.02em; }

.sms-marquee .sms-marquee__item { border: 1px solid var(--sms-line); border-radius: 0.25rem; box-shadow: none; font-weight: 500; }

.sms-contact .sms-contact__detail { border: 1px solid var(--sms-line); border-radius: var(--sms-radius); background: var(--sms-white); }
.sms-contact .sms-contact__detail:hover { border-color: var(--sms-green); transform: none; }
.sms-contact .sms-contact__icon { border-radius: 0.25rem; background: var(--sms-mint); }
.sms-contact .sms-contact__label { font-family: var(--sms-mono); font-weight: 500; }
.sms-contact .sms-contact__value { font-weight: 600; }
.sms-contact .sms-contact__form { border: 1px solid var(--sms-line); border-radius: var(--sms-radius); box-shadow: none; }
.sms-contact .sms-contact__form::after { content: ""; position: absolute; inset: -9px; background: @CROSS_NAVY@; pointer-events: none; }
.sms-contact .sms-contact__form { position: relative; }
.sms-contact .sms-contact__form-title { font-weight: 600; }
.sms-contact .sms-contact__booklink { border-radius: 0.25rem; background: var(--sms-pale); border: 1px solid var(--sms-line); }
.sms-contact .sms-contact__input { border-radius: 0.25rem; }

/* Booking wizard */
.sms-booking { isolation: isolate; }
.sms-booking::before { content: ""; position: absolute; z-index: -1; inset: 0; background: @GRID_LIGHT@; -webkit-mask-image: linear-gradient(180deg, #000, transparent 70%); mask-image: linear-gradient(180deg, #000, transparent 70%); pointer-events: none; }
.sms-booking .sms-booking__form { border: 1px solid var(--sms-line); border-radius: var(--sms-radius); box-shadow: none; }
.sms-booking .sms-booking__progress-step { font-family: var(--sms-mono); font-size: 0.75rem; font-weight: 500; letter-spacing: 0.06em; text-transform: uppercase; }
.sms-booking .sms-booking__progress-dot { border-width: 1.5px; border-radius: 0.25rem; font-family: var(--sms-mono); font-weight: 500; }
.sms-booking .sms-booking__bar { height: 2px; border-radius: 0; background: var(--sms-line); }
.sms-booking .sms-booking__bar-fill { border-radius: 0; }
.sms-booking .sms-booking__step-title { font-weight: 600; letter-spacing: -0.025em; }
.sms-booking .sms-booking__service-card { border-width: 1px; border-radius: var(--sms-radius); }
.sms-booking .sms-booking__service-icon { border-radius: 0.25rem; }
.sms-booking .sms-booking__service-tick { border-radius: 0.2rem; }
.sms-booking .sms-booking__service-name { font-weight: 600; }
.sms-booking .sms-booking__label { font-weight: 600; }
.sms-booking .sms-booking__input { border-radius: 0.25rem; }
.sms-booking .sms-booking__chip-text { border-width: 1px; border-radius: 0.25rem; font-weight: 500; }
.sms-booking .sms-booking__toggle { border: 1px solid var(--sms-line); border-radius: 0.3rem; background: var(--sms-pale); }
.sms-booking .sms-booking__toggle-opt span { border-radius: 0.2rem; font-weight: 600; }
.sms-booking .sms-booking__stepper { border-radius: 0.25rem; }
.sms-booking .sms-booking__review { border: 1px solid var(--sms-line); border-radius: 0.25rem; }
.sms-booking .sms-booking__done-badge { border-radius: 0.375rem; }
.sms-booking .sms-booking__summary { position: relative; isolation: isolate; overflow: hidden; border-radius: var(--sms-radius); }
.sms-booking .sms-booking__summary::before { content: ""; position: absolute; z-index: -1; inset: 0; background: @GRID_NAVY@; pointer-events: none; }
.sms-booking .sms-booking__summary-list dt { font-family: var(--sms-mono); font-weight: 500; }
.sms-booking .sms-booking__help { border: 1px solid var(--sms-line); border-radius: var(--sms-radius); background: var(--sms-white); }

/* Footer: navy blueprint */
.sms-footer { position: relative; isolation: isolate; background: var(--sms-navy); color: rgba(255, 255, 255, 0.84); }
.sms-footer::before { content: ""; position: absolute; z-index: -1; inset: 0; background: @GRID_NAVY_SOFT@; pointer-events: none; }
.sms-footer .sms-footer__heading { color: var(--sms-green-on-navy); font-family: var(--sms-mono); font-weight: 500; }
.sms-footer .sms-footer__tag { color: var(--sms-white); font-weight: 500; }
.sms-footer .sms-footer__link { color: rgba(255, 255, 255, 0.84); }
.sms-footer .sms-footer__link:hover { color: var(--sms-green-on-navy); }
.sms-footer .sms-footer__badge { border-radius: 0.25rem; }
.sms-footer .sms-footer__base { border-color: rgba(255, 255, 255, 0.16); font-family: var(--sms-mono); font-size: 0.75rem; letter-spacing: 0.04em; }

/* ---------- Frame: photo with crosshairs, ruler ticks and dimension lines ---------- */
.sms-bpframe { position: relative; min-width: 0; padding: 1.25rem 1.6rem 0 0.6rem; }
.sms-bpframe .sms-bpframe__box { position: relative; min-width: 0; }
.sms-bpframe .sms-bpframe__box::after { content: ""; position: absolute; z-index: 3; inset: -9px; background: @CROSS_NAVY@; pointer-events: none; }
.sms-bpframe .sms-bpframe__photo { aspect-ratio: 4 / 3.4; border-radius: 0.2rem; }
.sms-bpframe .sms-bpframe__photo .sms-photo__img { animation: sms-zoom 1.8s var(--sms-ease) both; }
.sms-bpframe .sms-bpframe__ruler { position: absolute; left: 0; right: 0; top: -1.1rem; height: 9px; background: repeating-linear-gradient(90deg, rgba(64, 83, 101, 0.55) 0 1px, transparent 1px 12px) left bottom / 100% 4px no-repeat, repeating-linear-gradient(90deg, rgba(64, 83, 101, 0.7) 0 1px, transparent 1px 60px) left bottom / 100% 9px no-repeat; transform-origin: left; animation: sms-bp-drawx 1.2s var(--sms-ease) 0.35s both; }
.sms-bpframe .sms-bpframe__vdim { position: absolute; top: 0; bottom: 0; right: -1.25rem; width: 9px; border-top: 1px solid var(--sms-ink-soft); border-bottom: 1px solid var(--sms-ink-soft); background: linear-gradient(var(--sms-ink-soft), var(--sms-ink-soft)) center / 1px 100% no-repeat; transform-origin: top; animation: sms-bp-drawy 1.1s var(--sms-ease) 0.6s both; }
.sms-bpframe .sms-bpframe__dim { position: relative; display: flex; justify-content: center; min-width: 0; margin-top: 1rem; }
.sms-bpframe .sms-bpframe__dim-line { position: absolute; left: 0; right: 0; top: 50%; height: 9px; margin-top: -5px; border-left: 1px solid var(--sms-ink-soft); border-right: 1px solid var(--sms-ink-soft); background: linear-gradient(var(--sms-ink-soft), var(--sms-ink-soft)) center / 100% 1px no-repeat; transform-origin: center; animation: sms-bp-drawx 1.1s var(--sms-ease) 0.5s both; }
.sms-bpframe .sms-bpframe__dim-label { position: relative; min-width: 0; max-width: 85%; padding: 0.1rem 0.7rem; background: var(--sms-white); color: var(--sms-ink-soft); font-family: var(--sms-mono); font-size: 0.75rem; font-weight: 500; letter-spacing: 0.1em; line-height: 1.5; text-align: center; text-transform: uppercase; }
.sms-bpframe .sms-bpframe__tags { position: absolute; z-index: 2; inset: 0; margin: 0; padding: 0; list-style: none; pointer-events: none; }
.sms-bpframe .sms-bpframe__tag { position: absolute; display: flex; align-items: center; gap: 0.5rem; min-width: 0; max-width: min(17rem, 78%); padding: 0.45rem 0.7rem 0.45rem 0.45rem; border: 1px solid var(--sms-navy); border-radius: 0.2rem; background: var(--sms-white); color: var(--sms-navy); font-family: var(--sms-mono); font-size: 0.75rem; font-weight: 500; letter-spacing: 0.02em; line-height: 1.35; }
.sms-bpframe .sms-bpframe__tag--0 { left: -0.6rem; bottom: 1rem; }
.sms-bpframe .sms-bpframe__tag--1 { right: 0.9rem; top: 0.9rem; }
.sms-bpframe .sms-bpframe__tag::before { content: ""; position: absolute; top: 50%; width: 1.4rem; height: 1px; background: var(--sms-navy); }
.sms-bpframe .sms-bpframe__tag--0::before { left: 100%; }
.sms-bpframe .sms-bpframe__tag--1::before { right: 100%; }
.sms-bpframe .sms-bpframe__tag::after { content: ""; position: absolute; top: 50%; width: 7px; height: 7px; margin-top: -3px; border: 1px solid var(--sms-navy); border-radius: 50%; background: var(--sms-white); }
.sms-bpframe .sms-bpframe__tag--0::after { left: calc(100% + 1.4rem); }
.sms-bpframe .sms-bpframe__tag--1::after { right: calc(100% + 1.4rem); }
.sms-bpframe .sms-bpframe__tag-icon { width: 1.6rem; height: 1.6rem; padding: 0.3rem; border-radius: 0.15rem; background: var(--sms-mint); color: var(--sms-green); }
.sms-bpframe .sms-bpframe__tag-text { min-width: 0; }
.sms-bpframe .sms-bpframe__tag { animation: sms-bp-fade 0.8s var(--sms-ease) 1s both; }
@media (min-width: 52em) {
  .sms-bpframe { padding-left: 0; }
  .sms-bpframe .sms-bpframe__photo { aspect-ratio: 4 / 4.3; }
  .sms-bpframe .sms-bpframe__tag--0 { left: -1.75rem; }
}

/* ---------- Home hero ---------- */
.sms-bphero { position: relative; isolation: isolate; overflow: hidden; padding: clamp(2.5rem, 1.5rem + 4vw, 5.5rem) 0 0; }
.sms-bphero::before { content: ""; position: absolute; z-index: -1; inset: 0; background: @GRID_LIGHT@; -webkit-mask-image: linear-gradient(180deg, #000 55%, transparent); mask-image: linear-gradient(180deg, #000 55%, transparent); pointer-events: none; }
.sms-bphero .sms-bphero__inner { display: grid; gap: clamp(2.5rem, 1.5rem + 4vw, 5rem); align-items: center; width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-bphero .sms-bphero__copy { min-width: 0; }
.sms-bphero .sms-bphero__eyebrow { min-width: 0; padding: 0.35rem 0.7rem; border: 1px solid var(--sms-line); border-radius: 0.2rem; background: var(--sms-white); color: var(--sms-navy); }
.sms-bphero .sms-bphero__title { max-width: 12em; min-width: 0; margin: 0 0 1.5rem; font-size: clamp(2.4rem, 1.2rem + 4.4vw, 4.6rem); font-weight: 600; line-height: 1.02; letter-spacing: -0.045em; }
.sms-bphero .sms-bphero__line { display: block; }
.sms-bphero .sms-bphero__lead { max-width: 34rem; min-width: 0; color: var(--sms-ink-soft); font-size: var(--sms-step-1); line-height: 1.55; }
.sms-bphero .sms-bphero__lead p { margin: 0; }
.sms-bphero .sms-bphero__actions { display: flex; flex-wrap: wrap; gap: 0.75rem; min-width: 0; margin-top: 2rem; }
.sms-bphero .sms-bphero__media { min-width: 0; width: 100%; max-width: 32rem; margin: 0 auto; }
.sms-bphero .sms-bphero__index { position: relative; margin-top: clamp(3rem, 2rem + 4vw, 5rem); border-top: 1px solid var(--sms-line); background: var(--sms-white); }
.sms-bphero .sms-bphero__index-inner { display: grid; width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-bphero .sms-bphero__index-label { min-width: 0; padding: 1rem 0 0.25rem; color: var(--sms-ink-soft); font-family: var(--sms-mono); font-size: 0.75rem; font-weight: 500; letter-spacing: 0.12em; text-transform: uppercase; }
.sms-bphero .sms-bphero__list { display: grid; min-width: 0; margin: 0; padding: 0; list-style: none; }
.sms-bphero .sms-bphero__item { min-width: 0; border-bottom: 1px solid var(--sms-line); }
.sms-bphero .sms-bphero__item:last-child { border-bottom: 0; }
.sms-bphero .sms-bphero__link { display: grid; grid-template-columns: auto minmax(0, 1fr) auto; gap: 0.15rem 0.9rem; align-items: center; padding: 1.1rem 0; color: var(--sms-navy); text-decoration: none; }
.sms-bphero .sms-bphero__icon { grid-row: span 2; width: 2.6rem; height: 2.6rem; padding: 0.6rem; border: 1px solid var(--sms-line); border-radius: 0.2rem; color: var(--sms-green); transition: background-color 0.3s, color 0.3s, border-color 0.3s; }
.sms-bphero .sms-bphero__ref { min-width: 0; color: var(--sms-ink-soft); font-family: var(--sms-mono); font-size: 0.75rem; font-weight: 500; letter-spacing: 0.1em; }
.sms-bphero .sms-bphero__name { grid-column: 2; min-width: 0; font-size: var(--sms-step-1); font-weight: 600; letter-spacing: -0.015em; line-height: 1.25; }
.sms-bphero .sms-bphero__go { grid-column: 3; grid-row: 1 / span 2; min-width: 0; color: var(--sms-green); font-size: 1.2rem; transition: transform 0.3s var(--sms-ease); }
.sms-bphero .sms-bphero__link:hover .sms-bphero__icon { border-color: var(--sms-green); background: var(--sms-green); color: var(--sms-white); }
.sms-bphero .sms-bphero__link:hover .sms-bphero__go { transform: translateX(4px); }
@media (min-width: 52em) {
  .sms-bphero .sms-bphero__inner { grid-template-columns: minmax(0, 1.15fr) minmax(0, 0.85fr); }
  .sms-bphero .sms-bphero__media { max-width: none; }
}
@media (min-width: 60em) {
  .sms-bphero .sms-bphero__index-inner { grid-template-columns: 9rem minmax(0, 1fr); align-items: stretch; }
  .sms-bphero .sms-bphero__index-label { padding: 1.6rem 0; border-right: 1px solid var(--sms-line); }
  .sms-bphero .sms-bphero__list { grid-template-columns: repeat(3, minmax(0, 1fr)); }
  .sms-bphero .sms-bphero__item { border-bottom: 0; border-right: 1px solid var(--sms-line); }
  .sms-bphero .sms-bphero__item:last-child { border-right: 0; }
  .sms-bphero .sms-bphero__link { padding: 1.4rem 1.5rem; }
}

/* ---------- Inner page hero ---------- */
.sms-bpage { position: relative; isolation: isolate; overflow: hidden; padding: clamp(2.5rem, 1.5rem + 4vw, 5rem) 0 clamp(3rem, 2rem + 4vw, 5.5rem); border-bottom: 1px solid var(--sms-line); }
.sms-bpage::before { content: ""; position: absolute; z-index: -1; inset: 0; background: @GRID_LIGHT@; -webkit-mask-image: linear-gradient(180deg, #000 50%, rgba(0, 0, 0, 0.25)); mask-image: linear-gradient(180deg, #000 50%, rgba(0, 0, 0, 0.25)); pointer-events: none; }
.sms-bpage .sms-bpage__inner { display: grid; gap: clamp(2.5rem, 1.5rem + 4vw, 5rem); align-items: center; width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-bpage .sms-bpage__copy { min-width: 0; }
.sms-bpage .sms-bpage__crumb { display: flex; flex-wrap: wrap; gap: 0.5rem; min-width: 0; margin-bottom: 1.75rem; color: var(--sms-ink-soft); font-family: var(--sms-mono); font-size: 0.75rem; font-weight: 500; letter-spacing: 0.1em; text-transform: uppercase; }
.sms-bpage .sms-bpage__crumb-link { min-width: 0; color: var(--sms-navy); text-underline-offset: 3px; }
.sms-bpage .sms-bpage__crumb-sep,
.sms-bpage .sms-bpage__crumb-here { min-width: 0; }
.sms-bpage .sms-bpage__title { min-width: 0; margin: 0 0 1.25rem; font-size: clamp(2.3rem, 1.3rem + 3.6vw, 4.1rem); font-weight: 600; line-height: 1.04; letter-spacing: -0.042em; }
.sms-bpage .sms-bpage__sub { min-width: 0; margin-bottom: 0.75rem; font-size: var(--sms-step-1); font-weight: 500; line-height: 1.4; }
.sms-bpage .sms-bpage__lead { max-width: 36rem; min-width: 0; color: var(--sms-ink-soft); font-size: var(--sms-step-1); line-height: 1.55; }
.sms-bpage .sms-bpage__lead p { margin: 0 0 0.75rem; }
.sms-bpage .sms-bpage__actions { display: flex; flex-wrap: wrap; gap: 0.75rem; min-width: 0; margin-top: 1.75rem; }
.sms-bpage .sms-bpage__media { min-width: 0; width: 100%; max-width: 31rem; margin: 0 auto; }
@media (min-width: 52em) {
  .sms-bpage .sms-bpage__inner { grid-template-columns: minmax(0, 1.1fr) minmax(0, 0.9fr); }
  .sms-bpage .sms-bpage__media { max-width: none; }
}

/* ---------- Services as spec sheets ---------- */
.sms-bpspec { padding: var(--sms-section) 0; }
.sms-bpspec .sms-bpspec__inner { width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-bpspec .sms-bpspec__head { display: grid; gap: 0.5rem 3rem; align-items: end; margin-bottom: clamp(2rem, 1.5rem + 2vw, 3.25rem); }
.sms-bpspec .sms-bpspec__heading { min-width: 0; }
.sms-bpspec .sms-bpspec__title { margin: 0; font-size: var(--sms-step-2); }
.sms-bpspec .sms-bpspec__lead { max-width: 36rem; min-width: 0; color: var(--sms-ink-soft); }
.sms-bpspec .sms-bpspec__lead p { margin: 0; }
.sms-bpspec .sms-bpspec__grid { display: grid; gap: clamp(1.25rem, 0.8rem + 1.5vw, 1.75rem); margin: 0; padding: 0; list-style: none; }
.sms-bpspec .sms-bpspec__item,
.sms-bpspec .sms-bpspec__mini { position: relative; display: flex; flex-direction: column; min-width: 0; border: 1px solid var(--sms-line); border-radius: 0.25rem; background: var(--sms-white); }
.sms-bpspec .sms-bpspec__edge { position: absolute; z-index: 2; background: var(--sms-green); pointer-events: none; transition: transform 0.28s var(--sms-ease); }
.sms-bpspec .sms-bpspec__edge--t { left: -1px; right: -1px; top: -1px; height: 2px; transform: scaleX(0); transform-origin: left; transition-delay: 0.21s; }
.sms-bpspec .sms-bpspec__edge--r { top: -1px; bottom: -1px; right: -1px; width: 2px; transform: scaleY(0); transform-origin: top; transition-delay: 0.14s; }
.sms-bpspec .sms-bpspec__edge--b { left: -1px; right: -1px; bottom: -1px; height: 2px; transform: scaleX(0); transform-origin: right; transition-delay: 0.07s; }
.sms-bpspec .sms-bpspec__edge--l { top: -1px; bottom: -1px; left: -1px; width: 2px; transform: scaleY(0); transform-origin: bottom; transition-delay: 0s; }
.sms-bpspec .sms-bpspec__item:hover .sms-bpspec__edge,
.sms-bpspec .sms-bpspec__item:focus-within .sms-bpspec__edge,
.sms-bpspec .sms-bpspec__mini:hover .sms-bpspec__edge,
.sms-bpspec .sms-bpspec__mini:focus-within .sms-bpspec__edge { transform: none; }
.sms-bpspec .sms-bpspec__item:hover .sms-bpspec__edge--t,
.sms-bpspec .sms-bpspec__mini:hover .sms-bpspec__edge--t { transition-delay: 0s; }
.sms-bpspec .sms-bpspec__item:hover .sms-bpspec__edge--r,
.sms-bpspec .sms-bpspec__mini:hover .sms-bpspec__edge--r { transition-delay: 0.07s; }
.sms-bpspec .sms-bpspec__item:hover .sms-bpspec__edge--b,
.sms-bpspec .sms-bpspec__mini:hover .sms-bpspec__edge--b { transition-delay: 0.14s; }
.sms-bpspec .sms-bpspec__item:hover .sms-bpspec__edge--l,
.sms-bpspec .sms-bpspec__mini:hover .sms-bpspec__edge--l { transition-delay: 0.21s; }
.sms-bpspec .sms-bpspec__top { display: flex; justify-content: space-between; gap: 1rem; min-width: 0; padding: 0.7rem 1rem; border-bottom: 1px solid var(--sms-line); color: var(--sms-ink-soft); font-family: var(--sms-mono); font-size: 0.75rem; font-weight: 500; letter-spacing: 0.1em; text-transform: uppercase; }
.sms-bpspec .sms-bpspec__ref { min-width: 0; color: var(--sms-navy); }
.sms-bpspec .sms-bpspec__sheet { min-width: 0; }
.sms-bpspec .sms-bpspec__media { position: relative; min-width: 0; margin: 1rem 1rem 0; }
.sms-bpspec .sms-bpspec__media::after { content: ""; position: absolute; z-index: 2; inset: -6px; background: @CROSS_INK6@; pointer-events: none; }
.sms-bpspec .sms-bpspec__photo { aspect-ratio: 16 / 10; border-radius: 0.15rem; }
.sms-bpspec .sms-bpspec__body { display: flex; flex: 1 1 auto; flex-direction: column; min-width: 0; padding: 1.25rem 1.25rem 1.4rem; }
.sms-bpspec .sms-bpspec__name-row { display: flex; align-items: center; gap: 0.75rem; min-width: 0; margin-bottom: 0.75rem; }
.sms-bpspec .sms-bpspec__icon { width: 2.4rem; height: 2.4rem; padding: 0.5rem; border-radius: 0.2rem; background: var(--sms-mint); color: var(--sms-green); }
.sms-bpspec .sms-bpspec__name { min-width: 0; margin: 0; font-size: var(--sms-step-1); font-weight: 600; letter-spacing: -0.02em; line-height: 1.2; }
.sms-bpspec .sms-bpspec__name-link { color: var(--sms-navy); text-decoration: none; }
.sms-bpspec .sms-bpspec__name-link:hover { color: var(--sms-green); }
.sms-bpspec .sms-bpspec__text { min-width: 0; margin: 0 0 1.1rem; color: var(--sms-ink-soft); font-size: var(--sms-step--1); line-height: 1.6; }
.sms-bpspec .sms-bpspec__table { min-width: 0; margin: 0 0 1.4rem; padding: 0; border-bottom: 1px solid var(--sms-line); list-style: none; }
.sms-bpspec .sms-bpspec__row { display: grid; grid-template-columns: 2.9rem minmax(0, 1fr); gap: 0.6rem; min-width: 0; padding: 0.55rem 0; border-top: 1px solid var(--sms-line); font-size: var(--sms-step--1); line-height: 1.45; }
.sms-bpspec .sms-bpspec__key { min-width: 0; padding-top: 0.1rem; color: var(--sms-ink-soft); font-family: var(--sms-mono); font-size: 0.75rem; font-weight: 500; }
.sms-bpspec .sms-bpspec__val { min-width: 0; font-weight: 500; }
.sms-bpspec .sms-bpspec__actions { display: flex; flex-wrap: wrap; align-items: center; gap: 0.75rem 1.25rem; min-width: 0; margin-top: auto; }
.sms-bpspec .sms-bpspec__go { min-width: 0; color: var(--sms-navy); font-family: var(--sms-mono); font-size: 0.8125rem; font-weight: 500; letter-spacing: 0.02em; text-underline-offset: 4px; }
.sms-bpspec .sms-bpspec__go:hover { color: var(--sms-green); }
.sms-bpspec .sms-bpspec__minor { display: grid; gap: clamp(1.25rem, 0.8rem + 1.5vw, 1.75rem); margin: clamp(1.25rem, 0.8rem + 1.5vw, 1.75rem) 0 0; padding: 0; list-style: none; }
.sms-bpspec .sms-bpspec__mini { display: grid; grid-template-columns: minmax(0, 1fr); }
.sms-bpspec .sms-bpspec__mini-body { display: grid; gap: 0.5rem 1.25rem; align-items: center; min-width: 0; padding: 1.25rem; }
.sms-bpspec .sms-bpspec__mini-copy { min-width: 0; }
.sms-bpspec .sms-bpspec__mini .sms-bpspec__name-row { margin-bottom: 0.4rem; }
.sms-bpspec .sms-bpspec__mini .sms-bpspec__text { margin: 0; }
@media (min-width: 46em) {
  .sms-bpspec .sms-bpspec__minor { grid-template-columns: repeat(2, minmax(0, 1fr)); }
}
@media (min-width: 60em) {
  .sms-bpspec .sms-bpspec__head { grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); }
  .sms-bpspec .sms-bpspec__lead { justify-self: end; }
}
@media (min-width: 64em) {
  .sms-bpspec .sms-bpspec__grid { grid-template-columns: repeat(3, minmax(0, 1fr)); }
}

/* ---------- Interactive plans (event site plan, workplace floor plan) ---------- */
.sms-bpplan { position: relative; isolation: isolate; padding: var(--sms-section) 0; background: var(--sms-pale); border-top: 1px solid var(--sms-line); border-bottom: 1px solid var(--sms-line); }
.sms-bpplan.sms-bpplan--white { background: var(--sms-white); }
.sms-bpplan .sms-bpplan__inner { width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-bpplan .sms-bpplan__head { display: grid; gap: 1rem 3rem; align-items: start; margin-bottom: clamp(2rem, 1.5rem + 2vw, 3rem); }
.sms-bpplan .sms-bpplan__heading,
.sms-bpplan .sms-bpplan__intro { min-width: 0; }
.sms-bpplan .sms-bpplan__title { margin: 0; font-size: var(--sms-step-2); }
.sms-bpplan .sms-bpplan__lead { max-width: 38rem; color: var(--sms-ink-soft); }
.sms-bpplan .sms-bpplan__lead p { margin: 0; }
.sms-bpplan .sms-bpplan__heading .sms-bpplan__lead { margin-top: 1rem; }
.sms-bpplan .sms-bpplan__actions { display: flex; flex-wrap: wrap; gap: 0.75rem; min-width: 0; margin-top: 1.5rem; }
.sms-bpplan .sms-bpplan__includes-title { margin: 0 0 0.5rem; color: var(--sms-navy); font-family: var(--sms-mono); font-size: 0.75rem; font-weight: 500; letter-spacing: 0.1em; text-transform: uppercase; }
.sms-bpplan .sms-bpplan__includes { margin: 0; padding: 0; border-bottom: 1px solid var(--sms-line); list-style: none; }
.sms-bpplan .sms-bpplan__include { display: grid; grid-template-columns: 2.4rem minmax(0, 1fr); gap: 0.5rem; min-width: 0; padding: 0.6rem 0; border-top: 1px solid var(--sms-line); font-size: var(--sms-step--1); font-weight: 500; }
.sms-bpplan .sms-bpplan__include-key { min-width: 0; color: var(--sms-ink-soft); font-family: var(--sms-mono); font-size: 0.75rem; }
.sms-bpplan .sms-bpplan__include-text { min-width: 0; }
.sms-bpplan .sms-bpplan__board { display: grid; gap: clamp(1.5rem, 1rem + 2vw, 2.5rem); align-items: start; }
.sms-bpplan .sms-bpplan__fig { min-width: 0; margin: 0; }
.sms-bpplan .sms-bpplan__stage { position: relative; min-width: 0; }
.sms-bpplan .sms-bpplan__canvas { position: relative; isolation: isolate; min-width: 0; border: 1px solid var(--sms-line); border-radius: 0.2rem; background: var(--sms-white); }
.sms-bpplan .sms-bpplan__canvas::before { content: ""; position: absolute; z-index: -1; inset: 0; background: @GRID_LIGHT@; pointer-events: none; }
.sms-bpplan .sms-bpplan__canvas::after { content: ""; position: absolute; inset: -9px; background: @CROSS_NAVY@; pointer-events: none; }
.sms-bpplan .sms-bpplan__svg { display: block; width: 100%; height: auto; }
.sms-bpplan .sms-bpplan__txt { display: none; font-family: var(--sms-mono); font-size: 13px; font-weight: 500; letter-spacing: 0.12em; }
.sms-bpplan .sms-bpplan__spot { position: absolute; z-index: 3; left: var(--x); top: var(--y); display: grid; place-items: center; width: 1.85rem; height: 1.85rem; margin: 0; padding: 0; border: 1.5px solid var(--sms-navy); border-radius: 50%; background: var(--sms-white); color: var(--sms-navy); cursor: pointer; font: 500 0.8125rem/1 var(--sms-mono); transform: translate(-50%, -50%); transition: transform 0.35s var(--sms-ease), opacity 0.35s, background-color 0.25s, color 0.25s, box-shadow 0.25s; }
.sms-bpplan .sms-bpplan__spot-num { min-width: 0; }
.sms-bpplan .sms-bpplan__spot:disabled { cursor: default; opacity: 1; }
.sms-bpplan .sms-bpplan__spot:not(:disabled):hover { box-shadow: 0 0 0 5px rgba(64, 127, 54, 0.18); }
.sms-bpplan .sms-bpplan__spot.is-active { border-color: var(--sms-green); background: var(--sms-green); color: var(--sms-white); box-shadow: 0 0 0 6px rgba(64, 127, 54, 0.2); }
.sms-bpplan .sms-bpplan__tip { position: relative; z-index: 4; min-width: 0; margin-top: 1rem; padding: 0.9rem 1rem 1rem; border: 1px solid var(--sms-navy); border-radius: 0.25rem; background: var(--sms-white); box-shadow: 0 16px 34px rgba(6, 30, 53, 0.12); animation: sms-bp-tip 0.35s var(--sms-ease) both; }
.sms-bpplan .sms-bpplan__tip[hidden] { display: none; }
.sms-bpplan .sms-bpplan__tip-head { display: flex; align-items: center; justify-content: space-between; gap: 1rem; min-width: 0; margin-bottom: 0.5rem; padding-bottom: 0.5rem; border-bottom: 1px solid var(--sms-line); }
.sms-bpplan .sms-bpplan__tip-ref { min-width: 0; color: var(--sms-green); font-family: var(--sms-mono); font-size: 0.75rem; font-weight: 500; letter-spacing: 0.1em; }
.sms-bpplan .sms-bpplan__tip-close { display: grid; place-items: center; min-width: 0; width: 1.9rem; height: 1.9rem; margin: -0.3rem -0.4rem -0.3rem 0; padding: 0; border: 1px solid transparent; border-radius: 0.2rem; background: transparent; color: var(--sms-navy); cursor: pointer; }
.sms-bpplan .sms-bpplan__tip-close:hover { border-color: var(--sms-line); }
.sms-bpplan .sms-bpplan__tip-x { width: 1.1rem; height: 1.1rem; transform: rotate(45deg); }
.sms-bpplan .sms-bpplan__tip-group { margin: 0 0 0.3rem; color: var(--sms-ink-soft); font-family: var(--sms-mono); font-size: 0.75rem; font-weight: 500; letter-spacing: 0.04em; line-height: 1.4; }
.sms-bpplan .sms-bpplan__tip-text { display: flex; gap: 0.6rem; align-items: flex-start; margin: 0; font-size: var(--sms-step-0); font-weight: 600; letter-spacing: -0.01em; line-height: 1.35; }
.sms-bpplan .sms-bpplan__tip-icon { width: 1.6rem; height: 1.6rem; padding: 0.3rem; border-radius: 0.15rem; background: var(--sms-mint); color: var(--sms-green); }
.sms-bpplan .sms-bpplan__tip-copy { min-width: 0; }
.sms-bpplan .sms-bpplan__cap { display: flex; flex-wrap: wrap; justify-content: space-between; gap: 0.25rem 1rem; margin-top: 1.1rem; color: var(--sms-ink-soft); font-family: var(--sms-mono); font-size: 0.75rem; font-weight: 500; letter-spacing: 0.08em; text-transform: uppercase; }
.sms-bpplan .sms-bpplan__cap-note,
.sms-bpplan .sms-bpplan__hint { min-width: 0; }
.sms-bpplan .sms-bpplan__hint[hidden] { display: none; }
.sms-bpplan .sms-bpplan__key { min-width: 0; }
.sms-bpplan .sms-bpplan__list + .sms-bpplan__key-title { margin-top: 1.75rem; }
.sms-bpplan .sms-bpplan__key-title { margin: 0 0 0.75rem; font-size: var(--sms-step-0); font-weight: 600; letter-spacing: -0.01em; }
.sms-bpplan .sms-bpplan__list { margin: 0; padding: 0; border-top: 1px solid var(--sms-line); list-style: none; }
.sms-bpplan .sms-bpplan__row { min-width: 0; border-bottom: 1px solid var(--sms-line); }
.sms-bpplan .sms-bpplan__row,
.sms-bpplan .sms-bpplan__rowbtn { display: grid; grid-template-columns: 2.2rem minmax(0, 1fr); gap: 0.75rem; align-items: start; }
.sms-bpplan .sms-bpplan__row { padding: 0.75rem 0.25rem; }
.sms-bpplan .sms-bpplan__row.is-live { display: block; padding: 0; }
.sms-bpplan .sms-bpplan__rowbtn { width: 100%; min-width: 0; margin: 0; padding: 0.75rem 0.25rem; border: 0; border-radius: 0.2rem; background: transparent; color: var(--sms-navy); cursor: pointer; font: inherit; text-align: left; transition: background-color 0.25s; }
.sms-bpplan .sms-bpplan__rowbtn:hover { background: rgba(220, 239, 214, 0.55); }
.sms-bpplan .sms-bpplan__num { display: grid; place-items: center; min-width: 0; width: 1.7rem; height: 1.7rem; border: 1.5px solid var(--sms-navy); border-radius: 50%; background: var(--sms-white); color: var(--sms-navy); font-family: var(--sms-mono); font-size: 0.75rem; font-weight: 500; transition: background-color 0.25s, color 0.25s, border-color 0.25s; }
.sms-bpplan .sms-bpplan__row-body { display: grid; gap: 0.15rem; min-width: 0; padding-top: 0.1rem; }
.sms-bpplan .sms-bpplan__row-text { min-width: 0; font-size: var(--sms-step--1); font-weight: 500; line-height: 1.45; }
.sms-bpplan .sms-bpplan__row.is-active .sms-bpplan__num { border-color: var(--sms-green); background: var(--sms-green); color: var(--sms-white); }
.sms-bpplan .sms-bpplan__row.is-active .sms-bpplan__rowbtn { background: var(--sms-white); box-shadow: inset 2px 0 0 var(--sms-green); }
.sms-bpplan .sms-bpplan__key-foot { margin-top: 1.5rem; }
/* Draw-in (only once the script has armed it; arming itself is instant) */
.sms-bpplan.is-armed .sms-bpplan__ln { stroke-dasharray: 1 1; stroke-dashoffset: 1; }
.sms-bpplan.is-armed .sms-bpplan__fade,
.sms-bpplan.is-armed .sms-bpplan__fill,
.sms-bpplan.is-armed .sms-bpplan__labels { opacity: 0; }
.sms-bpplan.is-armed .sms-bpplan__spot { opacity: 0; transform: translate(-50%, -50%) scale(0.5); transition: none; }
.sms-bpplan.is-armed.is-drawn .sms-bpplan__ln { stroke-dashoffset: 0; transition: stroke-dashoffset 1.5s var(--sms-ease) calc(var(--d, 0) * 0.15s); }
.sms-bpplan.is-armed.is-drawn .sms-bpplan__fade,
.sms-bpplan.is-armed.is-drawn .sms-bpplan__fill { opacity: 1; transition: opacity 0.9s ease calc(0.5s + var(--d, 0) * 0.13s); }
.sms-bpplan.is-armed.is-drawn .sms-bpplan__labels { opacity: 1; transition: opacity 0.9s ease 1.1s; }
.sms-bpplan.is-armed.is-drawn .sms-bpplan__spot { opacity: 1; transform: translate(-50%, -50%); transition: transform 0.45s var(--sms-ease) calc(1.2s + var(--i, 0) * 0.08s), opacity 0.45s ease calc(1.2s + var(--i, 0) * 0.08s), background-color 0.25s, color 0.25s, box-shadow 0.25s; }
.sms-bpplan.is-armed.is-drawn.is-settled .sms-bpplan__spot { transition: transform 0.35s var(--sms-ease), background-color 0.25s, color 0.25s, box-shadow 0.25s; }
@media (min-width: 40em) {
  .sms-bpplan .sms-bpplan__txt { display: inline; }
  .sms-bpplan .sms-bpplan__spot { width: 2.1rem; height: 2.1rem; font-size: 0.875rem; }
}
@media (min-width: 48em) {
  .sms-bpplan .sms-bpplan__tip { --tx: 1.5rem; --ty: -1.4rem; position: absolute; left: var(--x); top: var(--y); width: 16.5rem; margin: 0; transform: translate(var(--tx), var(--ty)); }
  .sms-bpplan .sms-bpplan__tip--l { --tx: calc(-100% - 1.5rem); }
  .sms-bpplan .sms-bpplan__tip--up { --ty: calc(-100% + 1.4rem); }
}
@media (min-width: 64em) {
  .sms-bpplan .sms-bpplan__head { grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); }
  .sms-bpplan .sms-bpplan__board { grid-template-columns: minmax(0, 1.75fr) minmax(0, 1fr); }
  .sms-bpplan .sms-bpplan__key { position: sticky; top: 6.5rem; }
}

/* ---------- Home: values as a numbered spec list ---------- */
.sms-bpvalues { padding: var(--sms-section) 0; }
.sms-bpvalues .sms-bpvalues__inner { display: grid; gap: clamp(2.5rem, 1.5rem + 4vw, 5rem); width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-bpvalues .sms-bpvalues__head { min-width: 0; }
.sms-bpvalues .sms-bpvalues__title { margin: 0 0 1.25rem; font-size: var(--sms-step-2); }
.sms-bpvalues .sms-bpvalues__lead { max-width: 36rem; color: var(--sms-ink-soft); }
.sms-bpvalues .sms-bpvalues__lead p { margin: 0; }
.sms-bpvalues .sms-bpvalues__claim { position: relative; max-width: 34rem; margin-top: 2.25rem; padding: 1.5rem 1.5rem 1.4rem; border: 1px solid var(--sms-line); border-radius: 0.2rem; background: var(--sms-pale); }
.sms-bpvalues .sms-bpvalues__claim::after { content: ""; position: absolute; inset: -9px; background: @CROSS_NAVY@; pointer-events: none; }
.sms-bpvalues .sms-bpvalues__claim-label { margin-bottom: 0.6rem; color: var(--sms-navy); font-family: var(--sms-mono); font-size: 0.75rem; font-weight: 500; letter-spacing: 0.1em; text-transform: uppercase; }
.sms-bpvalues .sms-bpvalues__claim-text { margin: 0 0 1.1rem; font-size: var(--sms-step-1); font-weight: 500; letter-spacing: -0.015em; line-height: 1.4; }
.sms-bpvalues .sms-bpvalues__list { min-width: 0; margin: 0; padding: 0; border-top: 1px solid var(--sms-navy); list-style: none; }
.sms-bpvalues .sms-bpvalues__row { position: relative; display: grid; grid-template-columns: 2.5rem 2.6rem minmax(0, 1fr); gap: 1rem; align-items: start; min-width: 0; padding: 1.5rem 0; border-bottom: 1px solid var(--sms-line); }
.sms-bpvalues .sms-bpvalues__row::after { content: ""; position: absolute; left: 0; bottom: -1px; width: 100%; height: 1px; background: var(--sms-green); transform: scaleX(0); transform-origin: left; transition: transform 0.5s var(--sms-ease); }
.sms-bpvalues .sms-bpvalues__row:hover::after { transform: none; }
.sms-bpvalues .sms-bpvalues__num { min-width: 0; padding-top: 0.55rem; color: var(--sms-ink-soft); font-family: var(--sms-mono); font-size: 0.8125rem; font-weight: 500; }
.sms-bpvalues .sms-bpvalues__icon { width: 2.6rem; height: 2.6rem; padding: 0.6rem; border-radius: 0.2rem; background: var(--sms-mint); color: var(--sms-green); }
.sms-bpvalues .sms-bpvalues__body { min-width: 0; }
.sms-bpvalues .sms-bpvalues__name { margin: 0 0 0.3rem; font-size: var(--sms-step-1); font-weight: 600; letter-spacing: -0.015em; line-height: 1.25; }
.sms-bpvalues .sms-bpvalues__text { margin: 0; color: var(--sms-ink-soft); }
@media (min-width: 60em) {
  .sms-bpvalues .sms-bpvalues__inner { grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); align-items: start; }
}

/* ---------- CTA: navy blueprint panel ---------- */
.sms-bpcta { padding: var(--sms-section) 0; }
.sms-bpcta .sms-bpcta__inner { width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-bpcta .sms-bpcta__box { position: relative; isolation: isolate; display: grid; gap: 2rem; align-items: center; overflow: hidden; padding: clamp(2rem, 1.2rem + 3.5vw, 4.25rem); border-radius: 0.25rem; background: var(--sms-navy); color: var(--sms-white); }
.sms-bpcta .sms-bpcta__box::before { content: ""; position: absolute; z-index: -1; inset: 0; background: @GRID_NAVY@; pointer-events: none; }
.sms-bpcta .sms-bpcta__box::after { content: ""; position: absolute; z-index: -1; inset: 0.9rem; background: @CROSS_GON@; pointer-events: none; }
.sms-bpcta .sms-bpcta__mark { position: absolute; z-index: -1; right: -7rem; bottom: -9rem; width: 22rem; height: 22rem; color: rgba(130, 208, 110, 0.2); pointer-events: none; }
.sms-bpcta .sms-bpcta__copy { min-width: 0; }
.sms-bpcta .sms-bpcta__ref { margin-bottom: 1rem; color: var(--sms-green-on-navy); font-family: var(--sms-mono); font-size: 0.75rem; font-weight: 500; letter-spacing: 0.12em; text-transform: uppercase; }
.sms-bpcta .sms-bpcta__title { margin: 0 0 1rem; font-size: clamp(1.9rem, 1.3rem + 2.4vw, 3.2rem); font-weight: 600; line-height: 1.08; letter-spacing: -0.035em; }
.sms-bpcta .sms-bpcta__text { max-width: 36rem; color: rgba(255, 255, 255, 0.84); }
.sms-bpcta .sms-bpcta__text p { margin: 0; }
.sms-bpcta .sms-bpcta__side { display: grid; gap: 1.1rem; justify-items: start; min-width: 0; }
.sms-bpcta .sms-bpcta__actions { display: flex; flex-wrap: wrap; gap: 0.75rem; min-width: 0; }
.sms-bpcta .sms-btn--outline { border-color: rgba(255, 255, 255, 0.75); color: var(--sms-white); }
.sms-bpcta .sms-btn--outline:hover { border-color: var(--sms-white); background: var(--sms-white); color: var(--sms-navy); }
.sms-bpcta .sms-btn--primary:hover { border-color: var(--sms-white); background: var(--sms-white); color: var(--sms-navy); }
.sms-bpcta .sms-bpcta__call { display: flex; flex-wrap: wrap; gap: 0.25rem 1.25rem; min-width: 0; color: rgba(255, 255, 255, 0.84); font-family: var(--sms-mono); font-size: 0.8125rem; }
.sms-bpcta .sms-bpcta__call-link { min-width: 0; color: var(--sms-white); text-underline-offset: 4px; overflow-wrap: anywhere; }
.sms-bpcta .sms-bpcta__call-link:hover { color: var(--sms-green-on-navy); }
.sms-bpcta .sms-bpcta__box a:focus-visible { outline-color: var(--sms-green-on-navy); }
@media (min-width: 60em) {
  .sms-bpcta .sms-bpcta__box { grid-template-columns: minmax(0, 1.4fr) minmax(0, 1fr); }
  .sms-bpcta .sms-bpcta__side { justify-items: end; }
  .sms-bpcta .sms-bpcta__actions { justify-content: flex-end; }
  .sms-bpcta .sms-bpcta__call { justify-content: flex-end; }
}

.sms-footer a:focus-visible,
.sms-people .sms-people__shared a:focus-visible,
.sms-people .sms-people__shared summary:focus-visible { outline-color: var(--sms-green-on-navy); }

@keyframes sms-bp-drawx { from { transform: scaleX(0); } to { transform: scaleX(1); } }
@keyframes sms-bp-drawy { from { transform: scaleY(0); } to { transform: scaleY(1); } }
@keyframes sms-bp-fade { from { opacity: 0; } to { opacity: 1; } }
@keyframes sms-bp-tip { from { opacity: 0; scale: 0.97; } to { opacity: 1; scale: 1; } }
"""

CSS = (CSS.replace("@EYEBROWS@", ",\n".join(EYEBROWS))
       .replace("@EYEBROWS_BEFORE@", ",\n".join(s + "::before" for s in EYEBROWS))
       .replace("@TITLES@", ",\n".join(TITLES))
       .replace("@CROSS_NAVY@", cross("rgba(6, 30, 53, 0.7)"))
       .replace("@CROSS_LINE@", cross("rgba(64, 83, 101, 0.45)"))
       .replace("@CROSS_INK6@", cross("rgba(64, 83, 101, 0.6)", 6))
       .replace("@CROSS_GON@", cross("rgba(130, 208, 110, 0.55)", 10))
       .replace("@GRID_LIGHT@", GRID_LIGHT)
       .replace("@GRID_NAVY_SOFT@", GRID_NAVY_SOFT)
       .replace("@GRID_NAVY@", GRID_NAVY))

RISE = [".sms-bphero .sms-bphero__title", ".sms-bpage .sms-bpage__title"]
ENTRANCE = [".sms-bphero .sms-bphero__eyebrow", ".sms-bpage .sms-bpage__crumb", ".sms-bpage .sms-bpage__eyebrow", ".sms-bphero .sms-bphero__lead",
            ".sms-bpage .sms-bpage__sub", ".sms-bpage .sms-bpage__lead", ".sms-bphero .sms-bphero__actions", ".sms-bpage .sms-bpage__actions",
            ".sms-bphero .sms-bphero__media", ".sms-bpage .sms-bpage__media", ".sms-bphero .sms-bphero__index"]
REVEAL = [".sms-bpspec .sms-bpspec__head", ".sms-bpspec .sms-bpspec__item", ".sms-bpspec .sms-bpspec__mini",
          ".sms-bpplan .sms-bpplan__head", ".sms-bpplan .sms-bpplan__key",
          ".sms-bpvalues .sms-bpvalues__head", ".sms-bpvalues .sms-bpvalues__row", ".sms-bpcta .sms-bpcta__box"]
LOOP = [".sms-bpframe .sms-bpframe__photo .sms-photo__img", ".sms-bpframe .sms-bpframe__ruler", ".sms-bpframe .sms-bpframe__vdim",
        ".sms-bpframe .sms-bpframe__dim-line", ".sms-bpframe .sms-bpframe__tag"]
OPEN = [".sms-bpplan .sms-bpplan__tip"]
TRANS = [".sms-bpspec .sms-bpspec__edge", ".sms-bpplan .sms-bpplan__spot", ".sms-bpplan .sms-bpplan__rowbtn", ".sms-bpplan .sms-bpplan__num",
         ".sms-bpplan.is-armed.is-drawn .sms-bpplan__ln", ".sms-bpplan.is-armed.is-drawn .sms-bpplan__fade", ".sms-bpplan.is-armed.is-drawn .sms-bpplan__fill",
         ".sms-bpplan.is-armed.is-drawn .sms-bpplan__labels", ".sms-bpplan.is-armed.is-drawn .sms-bpplan__spot", ".sms-bpplan.is-armed.is-drawn.is-settled .sms-bpplan__spot", ".sms-bphero .sms-bphero__icon",
         ".sms-bphero .sms-bphero__go", ".sms-bpvalues .sms-bpvalues__row::after", ".sms-faq .sms-faq__item", ".sms-links .sms-links__link"]

# The site plan replaces the booking-information feature on Event Medical Cover.
# Sections 0 and 1 are re-rendered inside inner_extra so the original order stays.
SKIP = {"event-medical-cover": [0, 1, 2]}


# ---------------------------------------------------------------------------
# Small builders
# ---------------------------------------------------------------------------
def eyebrow(block, text):
    return '<div class="sms-%s__eyebrow">%s</div>' % (block, e(text))


def frame(ctx, key, caption, tags=(), lazy=True, cls=""):
    tag_html = ""
    if tags:
        tag_html = '<ul class="sms-bpframe__tags">%s</ul>' % "".join(
            '<li class="sms-bpframe__tag sms-bpframe__tag--%d">%s<span class="sms-bpframe__tag-text">%s</span></li>' % (i, icon(ic, "sms-bpframe__tag-icon"), e(t))
            for i, (ic, t) in enumerate(tags[:2]))
    return """<div class="sms-bpframe%s">
      <div class="sms-bpframe__box">
        <span class="sms-bpframe__ruler" aria-hidden="true"></span>
        <span class="sms-bpframe__vdim" aria-hidden="true"></span>
        %s
        %s
      </div>
      <div class="sms-bpframe__dim"><span class="sms-bpframe__dim-line" aria-hidden="true"></span><span class="sms-bpframe__dim-label">%s</span></div>
    </div>""" % ((" " + cls) if cls else "", photo(ctx, key, lazy=lazy, parallax=False, figcls="sms-bpframe__photo"), tag_html, e(caption))


def page_hero(ctx, h):
    sub = '<div class="sms-bpage__sub">%s</div>' % e(h["sub"]) if h.get("sub") else ""
    acts = '<div class="sms-bpage__actions">%s</div>' % buttons(ctx, h["buttons"]) if h.get("buttons") else ""
    crumb = '<nav class="sms-bpage__crumb" aria-label="Breadcrumb"><a class="sms-bpage__crumb-link" href="%s">Home</a><span class="sms-bpage__crumb-sep" aria-hidden="true">/</span><span class="sms-bpage__crumb-here" aria-current="page">%s</span></nav>' % (
        ctx.href("home"), e(LABEL[ctx.slug]))
    return """<section class="sms-bpage">
  <div class="sms-bpage__inner">
    <div class="sms-bpage__copy">
      %s
      %s
      <h1 class="sms-bpage__title">%s</h1>
      %s
      <div class="sms-bpage__lead">%s</div>
      %s
    </div>
    <div class="sms-bpage__media">%s</div>
  </div>
</section>
""" % (crumb, eyebrow("bpage", h["eyebrow"]), e(h["title"]), sub, paras(h["body"]), acts,
       frame(ctx, h["photo"], "Fig. 01 \u2013 " + plain(h["eyebrow"]), h.get("chips", []), lazy=False))


REG_MARK = ('<svg class="sms-bpcta__mark" viewBox="0 0 200 200" width="200" height="200" aria-hidden="true" focusable="false">'
            '<g fill="none" stroke="currentColor" stroke-width="1"><circle cx="100" cy="100" r="74"/><circle cx="100" cy="100" r="46"/>'
            '<circle cx="100" cy="100" r="3"/><path d="M100 6 V194 M6 100 H194"/><path d="M100 26 v8 M100 166 v8 M26 100 h8 M166 100 h8"/></g></svg>')


def cta(ctx, d):
    return """<section class="sms-bpcta">
  <div class="sms-bpcta__inner">
    <div class="sms-bpcta__box">
      %s
      <div class="sms-bpcta__copy">
        <div class="sms-bpcta__ref">%s</div>
        <h2 class="sms-bpcta__title">%s</h2>
        <div class="sms-bpcta__text">%s</div>
      </div>
      <div class="sms-bpcta__side">
        <div class="sms-bpcta__actions">%s</div>
        <div class="sms-bpcta__call"><a class="sms-bpcta__call-link" href="tel:%s">T %s</a><a class="sms-bpcta__call-link" href="mailto:%s">E %s</a></div>
      </div>
    </div>
  </div>
</section>
""" % (REG_MARK, e(C.STRAP), e(d["title"]), paras(d["text"]), buttons(ctx, d["buttons"]), PHONE_TEL, PHONE, EMAIL, EMAIL)


def chrome_top(ctx):
    return header(ctx, "blue")


def chrome_bottom(ctx):
    return footer(ctx, "white")


# ---------------------------------------------------------------------------
# Plans (inline SVG drawn for this concept)
# ---------------------------------------------------------------------------
def _ln(d, n, extra=""):
    return '<path class="sms-bpplan__ln" style="--d:%d" pathLength="1" d="%s"%s/>' % (n, d, extra)


def _box(x, y, w, h, n, extra=""):
    return '<rect class="sms-bpplan__ln" style="--d:%d" pathLength="1" x="%d" y="%d" width="%d" height="%d"%s/>' % (n, x, y, w, h, extra)


def _txt(x, y, t, anchor="middle", extra=""):
    return '<text class="sms-bpplan__txt" x="%d" y="%d" text-anchor="%s"%s>%s</text>' % (x, y, anchor, extra, t)


def event_svg(uid):
    g = []
    # access road and fence
    g += [_ln("M0 452 H800", 0, ' stroke-width="1.5"'), _ln("M0 496 H800", 0, ' stroke-width="1.5"'),
          '<path class="sms-bpplan__fade" style="--d:6" stroke="%s" stroke-width="1.5" stroke-dasharray="14 10" d="M230 474 H800"/>' % INK,
          _ln("M360 420 H160", 1, ' stroke-width="2.5"'), _ln("M120 420 H40 V30 H760 V420 H700", 1, ' stroke-width="2.5"'), _ln("M660 420 H440", 1, ' stroke-width="2.5"'),
          '<g class="sms-bpplan__fade" style="--d:4" fill="%s" stroke="none"><rect x="354" y="414" width="8" height="12"/><rect x="438" y="414" width="8" height="12"/>'
          '<rect x="114" y="414" width="8" height="12"/><rect x="158" y="414" width="8" height="12"/><rect x="654" y="414" width="8" height="12"/><rect x="698" y="414" width="8" height="12"/></g>' % NAVY]
    # stage and arena
    g += ['<rect class="sms-bpplan__fill" style="--d:6" x="320" y="48" width="160" height="56" fill="%s" stroke="none"/>' % MINT,
          _box(320, 48, 160, 56, 2, ' stroke-width="2"'), _ln("M345 104 Q400 126 455 104", 3, ' stroke-width="1.5"'),
          '<rect class="sms-bpplan__fade" style="--d:5" stroke="%s" stroke-width="1.5" stroke-dasharray="6 6" x="270" y="140" width="260" height="140" rx="6"/>' % INK]
    # walkways
    g += [_ln("M400 412 V280", 3, ' stroke="%s" stroke-width="1"' % INK), _ln("M300 330 H520", 4, ' stroke="%s" stroke-width="1"' % INK)]
    # stalls
    g += [_box(x, 60, 36, 26, 2 + i // 2, ' stroke-width="1.5"') for i, x in enumerate([70, 116, 162, 208, 254])]
    g += [_box(60, y, 30, 36, 3 + i, ' stroke-width="1.5"') for i, y in enumerate([120, 166, 212])]
    # food and bar
    g += [_box(600, y, 66, 28, 2 + i // 2, ' stroke-width="1.5"') for i, y in enumerate([60, 98, 136, 174, 212])]
    # car park
    bays = " ".join("M%d 300 V328 M%d 372 V400" % (x, x) for x in range(81, 250, 21))
    g += [_box(60, 300, 190, 100, 2, ' stroke-width="1.5"'),
          '<path class="sms-bpplan__fade" style="--d:5" stroke="%s" stroke-width="1" d="%s"/>' % (INK, bays),
          _ln("M140 452 V420", 2, ' stroke="%s" stroke-width="1"' % INK)]
    # site office
    g += [_box(280, 350, 64, 40, 4, ' stroke-width="1.5"')]
    # first aid point
    g += ['<rect class="sms-bpplan__fill" style="--d:6" x="540" y="300" width="72" height="48" fill="%s" stroke="none"/>' % MINT,
          _box(540, 300, 72, 48, 4, ' stroke="%s" stroke-width="2"' % GREEN),
          _ln("M576 310 V338", 5, ' stroke="%s" stroke-width="4"' % GREEN), _ln("M562 324 H590", 5, ' stroke="%s" stroke-width="4"' % GREEN)]
    # emergency access route
    g += ['<path class="sms-bpplan__fade" style="--d:7" stroke="%s" stroke-width="2.5" stroke-dasharray="9 7" d="M680 474 V330 H614"/>' % GREEN,
          '<path class="sms-bpplan__fade" style="--d:8" stroke="%s" stroke-width="2.5" stroke-dasharray="9 7" d="M680 330 V262 H532"/>' % GREEN]
    # entrance arrow, north arrow
    g += [_ln("M400 492 V436", 5, ' stroke-width="1.5"'), _ln("M392 447 L400 435 L408 447", 6, ' stroke-width="1.5"'),
          '<path class="sms-bpplan__fade" style="--d:6" fill="%s" stroke="none" d="M782 44 L790 72 L782 65 L774 72 Z"/>' % NAVY]
    labels = [_txt(400, 81, "STAGE"), _txt(400, 216, "ARENA"), _txt(180, 50, "STALLS"), _txt(633, 50, "FOOD &amp; BAR"),
              _txt(155, 355, "CAR PARK"), _txt(312, 408, "SITE OFFICE"), _txt(576, 366, "FIRST AID"), _txt(452, 441, "ENTRANCE", "start"),
              _txt(40, 479, "ACCESS ROAD", "start"), _txt(700, 300, "EMERGENCY ACCESS", "middle", ' transform="rotate(-90 700 300)"'), _txt(782, 36, "N")]
    return """<svg class="sms-bpplan__svg" viewBox="0 0 800 520" width="800" height="520" role="img" aria-labelledby="%s-t" focusable="false">
            <title id="%s-t">Illustrated plan of a generic outdoor event: entrance, arena and stage, stalls, food and bar, first aid point, site office, emergency access route, car park and access road</title>
            <g fill="none" stroke="%s" stroke-linecap="round" stroke-linejoin="round">%s</g>
            <g class="sms-bpplan__labels" fill="%s" aria-hidden="true">%s</g>
          </svg>""" % (uid, uid, NAVY, "".join(g), INK, "".join(labels))


EVENT_SPOTS = {"entrance": (400, 420), "arena": (470, 180), "bar": (633, 150), "aid": (576, 324), "gate": (680, 420), "office": (312, 370)}


def floor_svg(uid):
    g = []
    # outer walls (with the main entrance and the loading bay door left open)
    g += [_ln("M180 470 H760 V420", 0, ' stroke-width="4"'), _ln("M760 330 V30 H40 V470 H120", 0, ' stroke-width="4"')]
    # interior walls
    g += [_ln("M300 30 V200", 1, ' stroke-width="2.5"'), _ln("M300 250 V470", 1, ' stroke-width="2.5"'),
          _ln("M40 180 H190", 2, ' stroke-width="2.5"'), _ln("M240 180 H300", 2, ' stroke-width="2.5"'),
          _ln("M40 320 H110", 2, ' stroke-width="2.5"'), _ln("M160 320 H300", 2, ' stroke-width="2.5"')]
    # door swings
    g += ['<path class="sms-bpplan__fade" style="--d:5" stroke="%s" stroke-width="1" d="M120 470 V412 A58 58 0 0 1 178 470"/>' % INK,
          '<path class="sms-bpplan__fade" style="--d:5" stroke="%s" stroke-width="1" d="M190 180 V229 A49 49 0 0 0 239 180"/>' % INK,
          '<path class="sms-bpplan__fade" style="--d:5" stroke="%s" stroke-width="1" d="M300 200 H349 A49 49 0 0 1 300 249"/>' % INK]
    # office: desks and a rota board
    g += [_box(x, y, 50, 26, 3 + (x - 70) // 65, ' stroke-width="1.5"') for y in (70, 120) for x in (70, 135, 200)]
    g += ['<g class="sms-bpplan__fade" style="--d:6" fill="%s" stroke="none">%s</g>' % (INK, "".join(
        '<circle cx="%d" cy="%d" r="5"/>' % (x + 25, y) for y in (106, 156) for x in (70, 135, 200)))]
    g += [_box(46, 80, 8, 60, 4, ' stroke-width="1.5"')]
    # welfare: table, chairs, first aid kit
    g += [_box(150, 230, 90, 50, 3, ' stroke-width="1.5"'),
          '<g class="sms-bpplan__fade" style="--d:6" stroke="%s" stroke-width="1">%s</g>' % (INK, "".join(
              '<rect x="%d" y="%d" width="16" height="10"/>' % (x, y) for y in (216, 284) for x in (162, 187, 212))),
          '<rect class="sms-bpplan__fill" style="--d:6" x="48" y="232" width="28" height="24" fill="%s" stroke="none"/>' % MINT,
          _box(48, 232, 28, 24, 4, ' stroke="%s" stroke-width="2"' % GREEN),
          _ln("M62 237 V251", 5, ' stroke="%s" stroke-width="2.5"' % GREEN), _ln("M55 244 H69", 5, ' stroke="%s" stroke-width="2.5"' % GREEN)]
    # reception desk and the way in
    g += [_ln("M190 360 H270 V400", 3, ' stroke-width="1.5"'), _ln("M150 516 V480", 5, ' stroke-width="1.5"'), _ln("M142 491 L150 479 L158 491", 6, ' stroke-width="1.5"')]
    # warehouse: racking
    for i, y in enumerate((70, 140, 210)):
        g.append(_box(340, y, 260, 24, 3 + i, ' stroke-width="1.5"'))
        g.append('<path class="sms-bpplan__fade" style="--d:6" stroke="%s" stroke-width="1" d="%s"/>' % (INK, " ".join("M%d %d V%d" % (x, y, y + 24) for x in range(392, 600, 52))))
    # wall cabinet for kit storage
    g += ['<rect class="sms-bpplan__fill" style="--d:6" x="306" y="282" width="14" height="38" fill="%s" stroke="none"/>' % MINT,
          _box(306, 282, 14, 38, 4, ' stroke="%s" stroke-width="2"' % GREEN)]
    # loading bay: hatched zone and a hazard sign
    g += ['<defs><pattern id="%s-hatch" width="12" height="12" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><path d="M0 0 V12" stroke="%s" stroke-width="1" opacity="0.45"/></pattern></defs>' % (uid, INK),
          '<rect class="sms-bpplan__fill" style="--d:7" x="600" y="320" width="160" height="150" fill="url(#%s-hatch)" stroke="none"/>' % uid,
          _box(600, 320, 160, 150, 4, ' stroke-width="1.5" stroke-dasharray="none"'),
          _ln("M680 372 L702 412 H658 Z", 6, ' stroke-width="2"'),
          '<path class="sms-bpplan__fade" style="--d:7" stroke="%s" stroke-width="1.5" stroke-dasharray="8 7" d="M600 395 H360"/>' % INK,
          _ln("M796 375 H772", 6, ' stroke-width="1.5"'), _ln("M780 368 L770 375 L780 382", 6, ' stroke-width="1.5"')]
    labels = [_txt(130, 172, "OFFICE"), _txt(232, 308, "WELFARE"), _txt(230, 444, "RECEPTION"), _txt(470, 290, "WAREHOUSE"),
              _txt(680, 310, "LOADING BAY"), _txt(205, 500, "ENTRANCE", "start")]
    return """<svg class="sms-bpplan__svg" viewBox="0 0 800 520" width="800" height="520" role="img" aria-labelledby="%s-t" focusable="false">
            <title id="%s-t">Illustrated floor plan of a generic workplace: office, welfare room with a first aid kit, reception and entrance, warehouse with racking, a kit cabinet and a loading bay</title>
            <g fill="none" stroke="%s" stroke-linecap="round" stroke-linejoin="round">%s</g>
            <g class="sms-bpplan__labels" fill="%s" aria-hidden="true">%s</g>
          </svg>""" % (uid, uid, NAVY, "".join(g), INK, "".join(labels))


FLOOR_SPOTS = [(470, 152), (680, 395), (160, 108), (62, 244), (313, 300), (195, 255), (50, 110), (150, 470)]
FLOOR_ICONS = ["briefcase", "alert", "users", "firstaid", "clipboard", "user", "calendar", "phone"]


def board(ctx, uid, svg, items, key_foot=""):
    """items: [(x, y, group, text, icon)] in viewBox units (800 x 520)."""
    spots, tips, groups = [], [], []
    for i, (x, y, grp, text, ic) in enumerate(items, 1):
        px, py = x / 8.0, y / 5.2
        pos = "--x:%.2f%%;--y:%.2f%%" % (px, py)
        mods = (" sms-bpplan__tip--l" if px > 55 else "") + (" sms-bpplan__tip--up" if py > 50 else "")
        tid = "%s-tip-%d" % (uid, i)
        spots.append('<button class="sms-bpplan__spot" type="button" style="%s;--i:%d" data-sms-spot="%d" aria-expanded="false" aria-controls="%s" disabled>'
                     '<span class="sms-bpplan__spot-num" aria-hidden="true">%d</span><span class="sms-visually-hidden">Point %d: %s</span></button>' % (pos, i, i, tid, i, i, e(text)))
        tips.append('<div class="sms-bpplan__tip%s" id="%s" style="%s" data-sms-tip="%d" hidden>'
                    '<div class="sms-bpplan__tip-head"><span class="sms-bpplan__tip-ref">REF %02d</span>'
                    '<button class="sms-bpplan__tip-close" type="button" data-sms-tip-close aria-label="Close">%s</button></div>'
                    '<p class="sms-bpplan__tip-group">%s</p><p class="sms-bpplan__tip-text">%s<span class="sms-bpplan__tip-copy">%s</span></p></div>' % (
                        mods, tid, pos, i, i, icon("plus", "sms-bpplan__tip-x"), e(grp), icon(ic, "sms-bpplan__tip-icon"), e(text)))
        row = ('<li class="sms-bpplan__row" data-sms-row="%d"><span class="sms-bpplan__num" aria-hidden="true">%d</span>'
               '<span class="sms-bpplan__row-body"><span class="sms-bpplan__row-text">%s</span></span></li>' % (i, i, e(text)))
        if groups and groups[-1][0] == grp:
            groups[-1][2].append(row)
        else:
            groups.append((grp, i, [row]))
    key = "".join('<h3 class="sms-bpplan__key-title">%s</h3><ol class="sms-bpplan__list"%s>%s</ol>' % (e(g), ' start="%d"' % n if n > 1 else "", "".join(r))
                  for g, n, r in groups)
    return """<div class="sms-bpplan__board">
      <figure class="sms-bpplan__fig">
        <div class="sms-bpplan__stage">
          <div class="sms-bpplan__canvas">
            %s
            %s
          </div>
          %s
        </div>
        <figcaption class="sms-bpplan__cap"><span class="sms-bpplan__cap-note">Illustration, not to scale</span><span class="sms-bpplan__hint" data-sms-hint hidden>Select a numbered point to explore</span></figcaption>
      </figure>
      <div class="sms-bpplan__key">%s%s</div>
    </div>""" % (svg, "".join(spots), "".join(tips), key, key_foot)


def plan_home(ctx):
    sp = EVENT_SPOTS
    qt = BOOKING["chips_title"]
    emp = "%s: %s" % (EMP["title"], EMP["list_title"])
    items = [
        sp["entrance"] + (qt, QUOTE[0][1], QUOTE[0][0]),
        sp["arena"] + (qt, QUOTE[1][1], QUOTE[1][0]),
        sp["bar"] + (qt, QUOTE[2][1], QUOTE[2][0]),
        sp["office"] + (qt, QUOTE[4][1], QUOTE[4][0]),
        sp["aid"] + (emp, EMP["list"][0], "firstaid"),
        sp["gate"] + (emp, EMP["list"][1], "route"),
    ]
    first, rest = split_first(EMP["text"])
    head = """<div class="sms-bpplan__heading">%s<h2 class="sms-bpplan__title">Event Medical <span class="sms-mark">Plans</span></h2></div>
      <div class="sms-bpplan__intro"><div class="sms-bpplan__lead"><p>%s</p></div>%s<div class="sms-bpplan__actions">%s</div></div>""" % (
        eyebrow("bpplan", "Risk & Needs Consultancy"), e(first), more("<p>%s</p>" % e(rest)),
        buttons(ctx, [("Book us for your medical cover", "book:event"), ("Visit Risk & Needs Consultancy", "risk-needs-consultancy")]))
    return """<section class="sms-bpplan" id="plan" data-sms-plan>
  <div class="sms-bpplan__inner">
    <div class="sms-bpplan__head">%s</div>
    %s
  </div>
</section>
""" % (head, board(ctx, "sms-plan-home", event_svg("sms-plan-home"), items))


def plan_event(ctx):
    sp = EVENT_SPOTS
    order = ["entrance", "arena", "bar", "aid", "gate", "office"]
    qt = BOOKING["chips_title"]
    items = [sp[k] + (qt, QUOTE[i][1], QUOTE[i][0]) for i, k in enumerate(order)]
    head = """<div class="sms-bpplan__heading">%s<h2 class="sms-bpplan__title">%s</h2></div>
      <div class="sms-bpplan__intro"><div class="sms-bpplan__lead"><p>%s</p></div>%s<div class="sms-bpplan__actions">%s</div></div>""" % (
        eyebrow("bpplan", BOOKING["eyebrow"]), e(BOOKING["title"]), e(BOOKING["body"][0]), more(paras(BOOKING["body"][1:])), buttons(ctx, BOOKING["buttons"]))
    ctx.notes.append("Event site plan: hotspot text is the \"What information is needed for a quote?\" list from the booking section, which this plan replaces")
    return """<section class="sms-bpplan sms-bpplan--white" id="quote-plan" data-sms-plan>
  <div class="sms-bpplan__inner">
    <div class="sms-bpplan__head">%s</div>
    %s
  </div>
</section>
""" % (head, board(ctx, "sms-plan-event", event_svg("sms-plan-event"), items))


def plan_floor(ctx):
    items = [FLOOR_SPOTS[i] + ("We consider", f, FLOOR_ICONS[i]) for i, f in enumerate(FACTORS)]
    first = split_first(FANA["text"])[0]
    inc = "".join('<li class="sms-bpplan__include"><span class="sms-bpplan__include-key" aria-hidden="true">%02d</span><span class="sms-bpplan__include-text">%s</span></li>' % (i, e(t))
                  for i, t in enumerate(FANA["list"], 1))
    head = """<div class="sms-bpplan__heading">%s<h2 class="sms-bpplan__title">%s</h2><div class="sms-bpplan__lead"><p>%s</p></div></div>
      <div class="sms-bpplan__intro"><h3 class="sms-bpplan__includes-title">%s</h3><ul class="sms-bpplan__includes">%s</ul><div class="sms-bpplan__actions">%s</div></div>""" % (
        eyebrow("bpplan", "Our Consultancy Services"), e(FANA["title"]), e(first), e(FANA["list_title"]), inc,
        buttons(ctx, [("Request a FREE initial Consultation", "book:consultancy")]))
    ctx.notes.append("Workplace floor plan: hotspot labels are the factors named in the First Aid Needs Assessment card (\"We consider ...\")")
    return """<section class="sms-bpplan" id="needs-plan" data-sms-plan>
  <div class="sms-bpplan__inner">
    <div class="sms-bpplan__head">%s</div>
    %s
  </div>
</section>
""" % (head, board(ctx, "sms-plan-floor", floor_svg("sms-plan-floor"), items))


def inner_extra(ctx, slug):
    if slug == "event-medical-cover":
        secs = EVENT["sections"]
        return SHARED_RENDERERS["feature"](ctx, secs[0][1]) + SHARED_RENDERERS["cards"](ctx, secs[1][1]) + plan_event(ctx)
    if slug == "risk-needs-consultancy":
        return plan_floor(ctx)
    return ""


# ---------------------------------------------------------------------------
# Homepage
# ---------------------------------------------------------------------------
def spec_sheets(ctx):
    edges = "".join('<span class="sms-bpspec__edge sms-bpspec__edge--%s" aria-hidden="true"></span>' % s for s in "trbl")
    items = ""
    for n, s in enumerate(C.SERVICES, 1):
        rows = "".join('<li class="sms-bpspec__row"><span class="sms-bpspec__key" aria-hidden="true">%02d.%d</span><span class="sms-bpspec__val">%s</span></li>' % (n, j, e(t))
                       for j, (_, t) in enumerate(s["list"], 1))
        items += """<li class="sms-bpspec__item">%s
        <div class="sms-bpspec__top"><span class="sms-bpspec__ref">REF %02d</span><span class="sms-bpspec__sheet">Sheet %d of 3</span></div>
        <div class="sms-bpspec__media">%s</div>
        <div class="sms-bpspec__body">
          <div class="sms-bpspec__name-row">%s<h3 class="sms-bpspec__name"><a class="sms-bpspec__name-link" href="%s">%s</a></h3></div>
          <p class="sms-bpspec__text">%s</p>
          <ul class="sms-bpspec__table">%s</ul>
          <div class="sms-bpspec__actions">%s<a class="sms-bpspec__go" href="%s">%s</a></div>
        </div>
      </li>""" % (edges, n, n, photo(ctx, s["photo"], parallax=False, figcls="sms-bpspec__photo"), icon(s["icon"], "sms-bpspec__icon"),
                  ctx.href(s["slug"]), e(s["title"]), e(s["text"]), rows, buttons(ctx, [(s["cta"], "book:" + s["key"])]),
                  ctx.href(s["slug"]), e(VISIT[s["slug"]]))
    rec = C.PAGES["recruitment"]["hero"]
    minis = [(4, C.CAREERS["icon"], C.CAREERS["title"], C.CAREERS["text"], C.CAREERS["cta"], C.CAREERS["slug"]),
             (5, "users", plain(rec["title"]), rec["body"][0], VISIT["recruitment"], "recruitment")]
    mini = "".join("""<li class="sms-bpspec__mini">%s
        <div class="sms-bpspec__top"><span class="sms-bpspec__ref">REF %02d</span><span class="sms-bpspec__sheet">%s</span></div>
        <div class="sms-bpspec__mini-body">
          <div class="sms-bpspec__mini-copy">
            <div class="sms-bpspec__name-row">%s<h3 class="sms-bpspec__name"><a class="sms-bpspec__name-link" href="%s">%s</a></h3></div>
            <p class="sms-bpspec__text">%s</p>
          </div>
          <a class="sms-bpspec__go" href="%s">%s&nbsp;<span class="sms-arrow" aria-hidden="true">&rarr;</span></a>
        </div>
      </li>""" % (edges, n, e(LABEL[slug]), icon(ic, "sms-bpspec__icon"), ctx.href(slug), e(t), e(x), ctx.href(slug), e(go)) for n, ic, t, x, go, slug in minis)
    return """<section class="sms-bpspec" id="services">
  <div class="sms-bpspec__inner">
    <div class="sms-bpspec__head">
      <div class="sms-bpspec__heading">%s<h2 class="sms-bpspec__title">What We <span class="sms-mark">Provide</span></h2></div>
      <div class="sms-bpspec__lead"><p>%s</p></div>
    </div>
    <ul class="sms-bpspec__grid">%s</ul>
    <ul class="sms-bpspec__minor">%s</ul>
  </div>
</section>
""" % (eyebrow("bpspec", "Our Services"), e(C.INTRO), items, mini)


def values(ctx):
    rows = "".join("""<li class="sms-bpvalues__row"><span class="sms-bpvalues__num" aria-hidden="true">%02d</span>%s<div class="sms-bpvalues__body"><h3 class="sms-bpvalues__name">%s</h3><p class="sms-bpvalues__text">%s</p></div></li>""" % (
        i, icon(ic, "sms-bpvalues__icon"), e(t), e(x)) for i, (ic, t, x) in enumerate(C.TRUST, 1))
    return """<section class="sms-bpvalues" id="about">
  <div class="sms-bpvalues__inner">
    <div class="sms-bpvalues__head">
      %s
      <h2 class="sms-bpvalues__title">Protecting People. <span class="sms-mark">Preparing Organisations.</span></h2>
      <div class="sms-bpvalues__lead"><p>%s</p></div>
      %s
      <div class="sms-bpvalues__claim">
        <div class="sms-bpvalues__claim-label">Why Choose Streamline?</div>
        <p class="sms-bpvalues__claim-text">%s</p>
        <a class="sms-btn sms-btn--outline" href="%s">Meet The Directors</a>
      </div>
    </div>
    <ol class="sms-bpvalues__list">%s</ol>
  </div>
</section>
""" % (eyebrow("bpvalues", "About Streamline"), e(C.ABOUT_HOME[0]), more(paras(C.ABOUT_HOME[1:])), e(C.CLAIM_15), ctx.href("about"), rows)


def home(ctx):
    ctx.notes += ["Image-only copy used: \"Clinician-led safety and medical support\" (clinician-led-safety.png)",
                  "Image-only copy used: \"Mathew and Tom bring over 15 years of ambulance experience...\" (why-choose-us.png - use approved)",
                  "Hero headline is the consultancy strapline \"Assess the risk. Plan the response. Protect your people.\" from the Risk & Needs Consultancy page"]
    idx = "".join('<li class="sms-bphero__item"><a class="sms-bphero__link" href="%s">%s<span class="sms-bphero__ref">REF %02d</span><span class="sms-bphero__name">%s</span><span class="sms-bphero__go" aria-hidden="true">&rarr;</span></a></li>' % (
        ctx.href(s["slug"]), icon(s["icon"], "sms-bphero__icon"), i, e(s["title"])) for i, s in enumerate(C.SERVICES, 1))
    out = """<section class="sms-bphero">
  <div class="sms-bphero__inner">
    <div class="sms-bphero__copy">
      %s
      <h1 class="sms-bphero__title"><span class="sms-bphero__line">Assess the risk.</span> <span class="sms-bphero__line">Plan the response.</span> <span class="sms-bphero__line sms-mark">Protect your people.</span></h1>
      <div class="sms-bphero__lead"><p>%s</p></div>
      <div class="sms-bphero__actions">%s</div>
    </div>
    <div class="sms-bphero__media">%s</div>
  </div>
  <div class="sms-bphero__index">
    <div class="sms-bphero__index-inner">
      <div class="sms-bphero__index-label">Choose a service</div>
      <ul class="sms-bphero__list">%s</ul>
    </div>
  </div>
</section>
""" % (eyebrow("bphero", "Clinician-led safety and medical support"), e(C.INTRO2),
       buttons(ctx, [("Book online", "book"), ("Call 01283 358789", "tel")]),
       frame(ctx, "fete", "Fig. 01 \u2013 Event Medical Cover", lazy=False), idx)
    out += spec_sheets(ctx)
    out += plan_home(ctx)
    out += values(ctx)
    picks = ["Where is Streamline based?", "Who runs Streamline?", "Can Streamline provide more than one service?", "Do you offer a free initial discussion?", "Are you insured?", "How can I contact Streamline?"]
    allf = dict(C.faqs("home"))
    out += SHARED_RENDERERS["faq"](ctx, {"tone": "pale", "eyebrow": C.STRAP, "title": "General Streamline [[FAQs]]",
                                        "lead": ["Answers to common questions about Streamline Safety & Medical Solutions, our team, services, bookings and how we work."],
                                        "items": [(q, allf[q]) for q in picks], "show": 6})
    out += cta(ctx, {"title": "Have any questions? We’re here to help.", "text": ["Speak to our team and we will be happy to help."],
                     "buttons": [("Book online", "book"), ("Contact Us", "contact")]})
    return out


# ---------------------------------------------------------------------------
# Script: hotspots, callouts and the draw-in (progressive enhancement)
# ---------------------------------------------------------------------------
JS = """<script>
(function () {
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var each = function (list, fn) { Array.prototype.forEach.call(list, fn); };
  each(document.querySelectorAll('[data-sms-plan]'), function (sec) {
    var spots = sec.querySelectorAll('[data-sms-spot]');
    var rows = sec.querySelectorAll('[data-sms-row]');
    var hint = sec.querySelector('[data-sms-hint]');
    var current = null;
    if (hint) { hint.hidden = false; }
    var find = function (sel, n) { return sec.querySelector('[' + sel + '="' + n + '"]'); };
    var close = function () {
      if (!current) { return; }
      var b = find('data-sms-spot', current), t = find('data-sms-tip', current), r = find('data-sms-row', current);
      if (b) { b.setAttribute('aria-expanded', 'false'); b.classList.remove('is-active'); }
      if (t) { t.hidden = true; }
      if (r) { r.classList.remove('is-active'); }
      current = null;
    };
    var open = function (n) {
      close();
      var b = find('data-sms-spot', n), t = find('data-sms-tip', n), r = find('data-sms-row', n);
      if (b) { b.setAttribute('aria-expanded', 'true'); b.classList.add('is-active'); }
      if (t) { t.hidden = false; }
      if (r) { r.classList.add('is-active'); }
      sec.classList.add('is-drawn');
      current = n;
    };
    each(spots, function (b) {
      b.disabled = false;
      b.addEventListener('click', function (ev) {
        ev.stopPropagation();
        var n = b.getAttribute('data-sms-spot');
        if (current === n) { close(); } else { open(n); }
      });
    });
    each(rows, function (li) {
      var btn = document.createElement('button');
      btn.type = 'button';
      btn.className = 'sms-bpplan__rowbtn';
      while (li.firstChild) { btn.appendChild(li.firstChild); }
      li.appendChild(btn);
      li.classList.add('is-live');
      btn.setAttribute('aria-controls', sec.querySelector('[data-sms-tip="' + li.getAttribute('data-sms-row') + '"]').id);
      btn.addEventListener('click', function (ev) {
        ev.stopPropagation();
        var n = li.getAttribute('data-sms-row');
        if (current === n) { close(); } else { open(n); }
      });
    });
    each(sec.querySelectorAll('[data-sms-tip-close]'), function (c) {
      c.addEventListener('click', function (ev) {
        ev.stopPropagation();
        var n = current; close();
        var b = n && find('data-sms-spot', n);
        if (b) { b.focus(); }
      });
    });
    each(sec.querySelectorAll('[data-sms-tip]'), function (t) { t.addEventListener('click', function (ev) { ev.stopPropagation(); }); });
    document.addEventListener('click', function () { close(); });
    sec.addEventListener('keydown', function (ev) {
      if (ev.key === 'Escape' && current) {
        var b = find('data-sms-spot', current); close();
        if (b) { b.focus(); }
      }
    });
    sec.addEventListener('focusin', function () { sec.classList.add('is-drawn'); });
    if (!reduce && 'IntersectionObserver' in window) {
      var canvas = sec.querySelector('.sms-bpplan__canvas');
      var box = canvas.getBoundingClientRect();
      if (box.top > window.innerHeight * 0.85) {
        sec.classList.add('is-armed');
        var io = new IntersectionObserver(function (entries) {
          entries.forEach(function (en) {
            if (en.isIntersecting) {
              sec.classList.add('is-drawn');
              window.setTimeout(function () { sec.classList.add('is-settled'); }, 2400);
              io.disconnect();
            }
          });
        }, { threshold: 0.35 });
        io.observe(canvas);
      }
    }
  });
})();
</script>
"""


def scripts(ctx, main):
    return JS if "data-sms-plan" in main else ""
