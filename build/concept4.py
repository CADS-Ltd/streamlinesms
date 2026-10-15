"""Concept 4 - Lifeline. Friendly but precise, in Streamline's own colours. A heartbeat
(ECG) trace, drawn in inline SVG, is the visual thread of the whole site: it draws
itself across the hero and carries the client's photos on its peaks, runs down the
homepage as a scroll-filled lifeline, beats inside the service "monitor" cards, maps
the event booking journey, and frames the inner-page heroes, CTA bands and footer.
Mostly white and pale-green pages, with navy kept for one feature island and the footer."""
import math
import re

from common import *  # noqa: F401,F403
import content as C

NAME = "Lifeline"
FONTS = "https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap"


# ---------------------------------------------------------------------------
# ECG geometry: polyline traces built in Python so the travelling dots, the
# photo "beats" and the scroll markers can be timed to the exact peaks.
# ---------------------------------------------------------------------------

def _bump(x0, x1, base, h, n=7):
    return [(x0 + (x1 - x0) * i / n, base - h * math.sin(math.pi * i / n)) for i in range(1, n + 1)]


def ecg(width, base, beats, s=1.0):
    """beats: [(centre x, amplitude)]. Returns (path d, list of tip fractions along the path)."""
    pts = [(0.0, base)]
    tips = []
    for cx, amp in beats:
        pts.append((cx - 62 * s, base))
        pts += _bump(cx - 62 * s, cx - 38 * s, base, amp * 0.12)
        pts.append((cx - 14 * s, base))
        pts.append((cx - 8 * s, base + amp * 0.1))
        tips.append(len(pts))
        pts.append((cx, base - amp))
        pts.append((cx + 9 * s, base + amp * 0.3))
        pts.append((cx + 17 * s, base))
        pts.append((cx + 32 * s, base))
        pts += _bump(cx + 32 * s, cx + 74 * s, base, amp * 0.22)
    pts.append((float(width), base))
    cum = [0.0]
    for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
        cum.append(cum[-1] + math.hypot(x1 - x0, y1 - y0))
    total = cum[-1]
    d = "M" + " L".join("%.1f %.1f" % p for p in pts)
    return d, [cum[i] / total for i in tips]


def _glow(gid):
    return ('<defs><radialGradient id="%s"><stop offset="0" stop-color="currentColor" stop-opacity="0.55"></stop>'
            '<stop offset="1" stop-color="currentColor" stop-opacity="0"></stop></radialGradient></defs>') % gid


def sweep(cls, gid, w, h, base, beats, s, dur):
    """A small live monitor trace: a sweeping gap and a glowing write-head."""
    d, _ = ecg(w, base, beats, s)
    return ('<svg class="sms-lfsweep %s" viewBox="0 0 %d %d" style="--sms-lf-dur: %.1fs" aria-hidden="true" focusable="false">%s'
            '<path class="sms-lfsweep__ghost" d="%s"></path><path class="sms-lfsweep__line" d="%s" pathLength="1"></path>'
            '<g class="sms-lfsweep__head" style="offset-path: path(\'%s\')"><circle r="10" fill="url(#%s)"></circle><circle class="sms-lfsweep__core" r="3.2"></circle></g></svg>') % (
        cls, w, h, dur, _glow(gid), d, d, d, gid)


def drawn(cls, w, h, base, beats, s, ratio="xMidYMid meet", extra=""):
    """A static trace that draws itself (on load or on scroll, depending on cls)."""
    d, _ = ecg(w, base, beats, s)
    return ('<svg class="sms-lfdraw %s" viewBox="0 0 %d %d" preserveAspectRatio="%s" aria-hidden="true" focusable="false">'
            '<path class="sms-lfdraw__line" d="%s" pathLength="1"></path>%s</svg>') % (cls, w, h, ratio, d, extra)


# Hero trace (desktop): photo beats sit on three peaks.
HERO_W, HERO_H, HERO_BASE = 1440, 250, 196
HERO_BEATS = [(140, 34), (450, 132), (625, 30), (800, 132), (975, 44), (1150, 132), (1330, 40)]
HERO_D, HERO_TIPS = ecg(HERO_W, HERO_BASE, HERO_BEATS, 1.25)
HERO_PHOTO_TIPS = [HERO_TIPS[1], HERO_TIPS[3], HERO_TIPS[5]]
HERO_NARROW = ecg(400, 84, [(80, 26), (200, 62), (320, 26)], 0.62)[0]
DRAW_S, DRAW_DELAY, LOOP_S = 2.4, 0.2, 7.0

# Booking journey: four beats, one per real booking-information sentence.
BOOKING = C.PAGES["event-medical-cover"]["sections"][2][1]
JOURNEY_LABELS = ["Your quotation", "Terms to review", "Booking confirmed", "If details change"]
JOURNEY_ORDER = [0, 3, 1, 2]
JOURNEY_D, JOURNEY_TIPS = ecg(1200, 86, [(150, 60), (450, 60), (750, 60), (1050, 60)], 1.0)
J_START, J_END = 22.0, 58.0

COURSES = C.PAGES["medical-training"]["sections"][0][1]

ECG_MASK = ("url(\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 40 16'%3E%3Cpath d='M0 9h11l2-3 2 3h3l2 3 3-11 3 13 2-5h12' fill='none' stroke='%23000' stroke-width='2' stroke-linejoin='round' stroke-linecap='round'/%3E%3C/svg%3E\")")
ECG_TILE = ("url(\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 160 64'%3E%3Cpath d='M0 40h52l5-6 5 6h12l4 5 7-36 7 44 5-13h63' fill='none' stroke='%23407f36' stroke-opacity='0.22' stroke-width='2' stroke-linejoin='round'/%3E%3C/svg%3E\")")


def _beat_css():
    out = ""
    for i, f in enumerate(HERO_PHOTO_TIPS, 1):
        out += ".sms-lfhero .sms-lfhero__beat--%d .sms-lfhero__beat-photo { animation-delay: %.2fs; }\n" % (i, DRAW_DELAY + DRAW_S * f * 0.82)
        out += ".sms-lfhero .sms-lfhero__beat--%d .sms-lfhero__beat-label { animation-delay: %.2fs; }\n" % (i, DRAW_DELAY + DRAW_S * f * 0.82 + 0.25)
        out += ".sms-lfhero .sms-lfhero__beat--%d .sms-lfhero__beat-ring { animation-delay: %.2fs; }\n" % (i, DRAW_DELAY + DRAW_S + LOOP_S * f - 0.15)
    return out


def _journey_css():
    out = "@supports (animation-timeline: view()) {\n  @media (min-width: 60em) {\n"
    for i, f in enumerate(JOURNEY_TIPS, 1):
        at = J_START + (J_END - J_START) * f
        out += "    .sms-lfjourney .sms-lfjourney__step:nth-child(%d) .sms-lfjourney__beat-on { animation-range: cover %.1f%% cover %.1f%%; }\n" % (i, at - 2, at + 1)
    out += "  }\n}\n"
    return out


# ---------------------------------------------------------------------------
# CSS
# ---------------------------------------------------------------------------
CSS = r"""
/* ===== Concept 4: Lifeline ===== */
.sms-page {
  --sms-font: "Plus Jakarta Sans", "Montserrat", Arial, sans-serif;
  --sms-radius: 1.5rem;
  --sms-radius-sm: 0.875rem;
  --sms-step-2: clamp(1.75rem, 1.25rem + 1.9vw, 2.875rem);
  --sms-step-3: clamp(2.4rem, 1.4rem + 4vw, 4.6rem);
  --sms-shadow: 0 1px 2px rgba(6, 30, 53, 0.04), 0 14px 34px rgba(6, 30, 53, 0.06);
  --sms-shadow-lg: 0 2px 4px rgba(6, 30, 53, 0.04), 0 30px 70px rgba(6, 30, 53, 0.12);
  --sms-lf-line: #d9e2e7;
  --sms-lf-grid: rgba(64, 127, 54, 0.075);
  --sms-field-line: #8796a3;
  letter-spacing: -0.003em;
}
.sms-page .sms-mark { color: var(--sms-accent); }
.sms-page .sms-lfstop { margin-left: -0.07em; color: var(--sms-green); }
.sms-lfisland .sms-lfstop { color: var(--sms-green-on-navy); }
.sms-page .sms-btn { padding: 0.95rem 1.45rem; font-weight: 700; letter-spacing: 0; }
.sms-page .sms-btn--primary { box-shadow: 0 1px 0 rgba(255, 255, 255, 0.25) inset, 0 10px 24px rgba(64, 127, 54, 0.24); }
.sms-page .sms-btn--primary:hover { box-shadow: 0 1px 0 rgba(255, 255, 255, 0.25) inset, 0 16px 30px rgba(64, 127, 54, 0.3); }
.sms-page .sms-btn--outline { border-color: rgba(6, 30, 53, 0.22); }
.sms-page .sms-btn--outline:hover { border-color: var(--sms-navy); background: var(--sms-navy); color: var(--sms-white); }
.sms-page .sms-chips__item { border: 1px solid var(--sms-lf-line); box-shadow: none; }
.sms-page .sms-chips__icon { background: var(--sms-pale-2); }
.sms-page .sms-more__toggle { color: var(--sms-green); }
.sms-page .sms-photo { border-radius: 1.75rem; }
.sms-page .sms-lfsweep,
.sms-page .sms-lfdraw { display: block; min-width: 0; overflow: visible; }

/* Shared eyebrow: a tiny heartbeat instead of a dash */
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
.sms-page .sms-lfkick::before { content: ""; flex: 0 0 auto; width: 2rem; height: 0.85rem; border-radius: 0; background: currentColor; -webkit-mask: """ + ECG_MASK + """ center / contain no-repeat; mask: """ + ECG_MASK + """ center / contain no-repeat; }
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
.sms-page .sms-lfkick { gap: 0.6rem; font-size: 0.78rem; letter-spacing: 0.14em; }
.sms-page .sms-lfkick { display: inline-flex; align-items: center; margin-bottom: 1rem; color: var(--sms-green); font-weight: 700; line-height: 1.3; text-transform: uppercase; }
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
.sms-booking .sms-booking__title,
.sms-page .sms-lftitle { margin: 0 0 1rem; font-size: var(--sms-step-2); font-weight: 800; line-height: 1.1; letter-spacing: -0.032em; }
.sms-page .sms-lflead { color: var(--sms-ink-soft); font-size: var(--sms-step-1); line-height: 1.6; }
.sms-page .sms-lflead p { margin: 0 0 0.75rem; }
.sms-feature.sms-tone-pale,
.sms-cards.sms-tone-pale,
.sms-steps.sms-tone-pale,
.sms-checklist.sms-tone-pale,
.sms-notice.sms-tone-pale,
.sms-faq.sms-tone-pale,
.sms-quotes.sms-tone-pale,
.sms-people.sms-tone-pale,
.sms-contact.sms-tone-pale,
.sms-links.sms-tone-pale,
.sms-claim.sms-tone-pale,
.sms-marquee.sms-tone-pale,
.sms-booking.sms-tone-pale { background: var(--sms-pale); }

/* ---------- Header ---------- */
.sms-header { border-bottom: 1px solid rgba(217, 226, 231, 0.8); background: rgba(255, 255, 255, 0.9); }
.sms-header .sms-header__link { font-weight: 600; }
.sms-header .sms-header__link::after { height: 2px; bottom: 0.15rem; }
.sms-header .sms-header__summary { border: 1px solid var(--sms-lf-line); background: var(--sms-white); }
.sms-header .sms-header__panel { border: 1px solid var(--sms-lf-line); }

/* ---------- Footer: navy, with a quiet light-green trace along the top ---------- */
.sms-footer { position: relative; background: var(--sms-navy); color: rgba(255, 255, 255, 0.82); }
.sms-footer .sms-footer__trace { position: absolute; left: 0; right: 0; top: -1px; height: 2.5rem; color: var(--sms-green-on-navy); opacity: 0.55; pointer-events: none; }
.sms-footer .sms-lfdraw { width: 100%; height: 100%; }
.sms-footer .sms-footer__heading,
.sms-footer .sms-footer__tag { color: var(--sms-white); }
.sms-footer .sms-footer__heading { letter-spacing: 0.14em; }
.sms-footer .sms-footer__link { color: rgba(255, 255, 255, 0.82); }
.sms-footer .sms-footer__link:hover { color: var(--sms-green-on-navy); }
.sms-footer .sms-footer__link:focus-visible { outline-color: var(--sms-green-on-navy); }
.sms-footer .sms-footer__base { border-color: rgba(255, 255, 255, 0.14); color: rgba(255, 255, 255, 0.72); }
.sms-footer .sms-footer__inner { padding-top: 1.5rem; }

/* ---------- Trace primitives ---------- */
.sms-page .sms-lfdraw__line { fill: none; stroke: currentColor; stroke-width: 2.2; stroke-linecap: round; stroke-linejoin: round; vector-effect: non-scaling-stroke; stroke-dasharray: 1; stroke-dashoffset: 0; }
.sms-page .sms-lfsweep { color: var(--sms-green); }
.sms-page .sms-lfsweep__ghost { fill: none; stroke: currentColor; stroke-opacity: 0.12; stroke-width: 2; stroke-linejoin: round; }
.sms-page .sms-lfsweep__line { fill: none; stroke: currentColor; stroke-width: 2.4; stroke-linecap: round; stroke-linejoin: round; animation: sms-lf-sweep var(--sms-lf-dur, 3s) linear infinite; }
.sms-page .sms-lfsweep__head { opacity: 0; offset-rotate: 0deg; animation: sms-lf-head var(--sms-lf-dur, 3s) linear infinite; }
.sms-page .sms-lfsweep__core { fill: currentColor; }
.sms-page .sms-lfdraw--load .sms-lfdraw__line { animation: sms-lf-draw 2.2s cubic-bezier(0.55, 0.1, 0.3, 1) 0.3s both; }
@keyframes sms-lf-draw { from { stroke-dashoffset: 1; } to { stroke-dashoffset: 0; } }
@keyframes sms-lf-sweep { from { stroke-dasharray: 0.86 0.14; stroke-dashoffset: 0.86; } to { stroke-dasharray: 0.86 0.14; stroke-dashoffset: -0.14; } }
@keyframes sms-lf-head { from { offset-distance: 0%; opacity: 1; } to { offset-distance: 100%; opacity: 1; } }
@keyframes sms-lf-pop { from { opacity: 0; transform: scale(0.4); } 70% { opacity: 1; transform: scale(1.06); } to { opacity: 1; transform: none; } }
@keyframes sms-lf-in { from { opacity: 0; transform: translateX(-10px); } to { opacity: 1; transform: none; } }
@keyframes sms-lf-ring { 0% { opacity: 0.7; transform: scale(1); } 22% { opacity: 0; transform: scale(1.55); } 100% { opacity: 0; transform: scale(1.55); } }
@keyframes sms-lf-travel { 0% { offset-distance: 0%; opacity: 0; } 4% { opacity: 1; } 93% { opacity: 1; } 100% { offset-distance: 100%; opacity: 0; } }
@keyframes sms-lf-spark { 0% { stroke-dashoffset: 0.07; opacity: 0; } 4% { opacity: 1; } 93% { opacity: 1; } 100% { stroke-dashoffset: -0.93; opacity: 0; } }
@keyframes sms-lf-live { 0%, 100% { box-shadow: 0 0 0 0 rgba(64, 127, 54, 0.45); } 50% { box-shadow: 0 0 0 7px rgba(64, 127, 54, 0); } }

/* ---------- Home hero ---------- */
.sms-lfhero { position: relative; overflow: hidden; padding: clamp(2.75rem, 1.8rem + 4vw, 5.5rem) 0 clamp(2.5rem, 1.5rem + 3vw, 4rem); background: var(--sms-white); }
.sms-lfhero .sms-lfhero__grid,
.sms-lfphero .sms-lfphero__grid { position: absolute; inset: 0; z-index: 0; background-image: linear-gradient(var(--sms-lf-grid) 1px, transparent 1px), linear-gradient(90deg, var(--sms-lf-grid) 1px, transparent 1px); background-size: 28px 28px; -webkit-mask-image: radial-gradient(70% 65% at 50% 70%, #000 20%, transparent 75%); mask-image: radial-gradient(70% 65% at 50% 70%, #000 20%, transparent 75%); pointer-events: none; }
.sms-lfhero .sms-lfhero__inner { position: relative; z-index: 1; width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-lfhero .sms-lfhero__copy { min-width: 0; }
.sms-page .sms-lfpill { display: inline-flex; align-items: center; gap: 0.65rem; max-width: 100%; margin-bottom: 1.5rem; padding: 0.45rem 1rem 0.45rem 0.6rem; border: 1px solid var(--sms-lf-line); border-radius: 999px; background: var(--sms-white); color: var(--sms-navy); font-size: var(--sms-step--1); font-weight: 600; line-height: 1.35; }
.sms-page .sms-lfpill__dot { flex: 0 0 auto; min-width: 0; width: 0.6rem; height: 0.6rem; margin-left: 0.25rem; border-radius: 50%; background: var(--sms-green); animation: sms-lf-live 2s ease-in-out infinite; }
.sms-page .sms-lfpill__text { min-width: 0; }
.sms-lfhero .sms-lfhero__title { max-width: 15em; margin: 0; font-size: clamp(2.6rem, 1.2rem + 5.4vw, 5.6rem); font-weight: 800; line-height: 1.0; letter-spacing: -0.04em; }
.sms-lfhero .sms-lfhero__title .sms-mark { display: inline-block; }
.sms-lfhero .sms-lfhero__row { display: grid; gap: 1.5rem; align-items: end; margin-top: clamp(1.25rem, 0.8rem + 1.5vw, 2rem); }
.sms-lfhero .sms-lfhero__lead { min-width: 0; max-width: 36rem; color: var(--sms-ink-soft); font-size: var(--sms-step-1); line-height: 1.6; }
.sms-lfhero .sms-lfhero__lead p { margin: 0; }
.sms-lfhero .sms-lfhero__actions { display: flex; flex-wrap: wrap; gap: 0.75rem; min-width: 0; }
.sms-lfhero .sms-lfhero__stage { position: relative; z-index: 1; width: 100%; max-width: 100rem; margin: clamp(1.5rem, 1rem + 2vw, 2.5rem) auto 0; container-type: inline-size; }
.sms-lfhero .sms-lfhero__svg { width: 100%; height: auto; color: var(--sms-green); }
.sms-lfhero .sms-lfhero__svg--wide { display: none; }
.sms-lfhero .sms-lfhero__svg--narrow { padding: 0 var(--sms-gutter); }
.sms-lfhero .sms-lfhero__ghost { fill: none; stroke: var(--sms-mint); stroke-width: 2; stroke-linejoin: round; }
.sms-lfhero .sms-lfhero__line { fill: none; stroke: currentColor; stroke-width: 2.6; stroke-linecap: round; stroke-linejoin: round; stroke-dasharray: 1; stroke-dashoffset: 0; animation: sms-lf-draw 2.4s cubic-bezier(0.5, 0.05, 0.35, 1) 0.2s both; }
.sms-lfhero .sms-lfhero__spark { fill: none; stroke: #82d06e; stroke-width: 4.5; stroke-linecap: round; stroke-linejoin: round; stroke-dasharray: 0.07 0.93; opacity: 0; animation: sms-lf-spark 7s linear 2.6s infinite both; }
.sms-lfhero .sms-lfhero__dot { opacity: 0; offset-rotate: 0deg; animation: sms-lf-travel 7s linear 2.6s infinite both; }
.sms-lfhero .sms-lfhero__dot-core { fill: var(--sms-green); stroke: var(--sms-white); stroke-width: 2.5; }
.sms-lfhero .sms-lfhero__beats { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 0.75rem; margin: 1.5rem 0 0; padding: 0 var(--sms-gutter); list-style: none; }
.sms-lfhero .sms-lfhero__beat { min-width: 0; }
.sms-lfhero .sms-lfhero__beat-link { display: flex; flex-direction: column; align-items: center; gap: 0.6rem; min-width: 0; color: var(--sms-navy); text-align: center; text-decoration: none; border-radius: 1rem; }
.sms-lfhero .sms-lfhero__beat-photo { position: relative; display: block; flex: 0 0 auto; min-width: 0; width: clamp(4.5rem, 3rem + 7vw, 6.5rem); aspect-ratio: 1; border-radius: 50%; animation: sms-lf-pop 0.7s var(--sms-ease) both; }
.sms-lfhero .sms-lfhero__beat-img { position: absolute; inset: 0; display: block; width: 100%; height: 100%; border: 4px solid var(--sms-white); border-radius: 50%; object-fit: cover; box-shadow: 0 0 0 2px var(--sms-green), 0 14px 30px rgba(6, 30, 53, 0.18); transition: transform 0.4s var(--sms-ease); }
.sms-lfhero .sms-lfhero__beat-ring { position: absolute; inset: -2px; border: 2px solid var(--sms-green); border-radius: 50%; opacity: 0; animation: sms-lf-ring 7s ease-out infinite; }
.sms-lfhero .sms-lfhero__beat-label { display: flex; flex-direction: column; align-items: center; gap: 0.1rem; min-width: 0; animation: sms-lf-in 0.6s var(--sms-ease) both; }
.sms-lfhero .sms-lfhero__beat-name { min-width: 0; font-size: 0.8125rem; font-weight: 700; line-height: 1.25; }
.sms-lfhero .sms-lfhero__beat-go { display: inline-flex; align-items: center; gap: 0.3rem; min-width: 0; color: var(--sms-green); font-size: 0.75rem; font-weight: 700; }
.sms-lfhero .sms-lfhero__beat-link:hover .sms-lfhero__beat-img,
.sms-lfhero .sms-lfhero__beat-link:focus-visible .sms-lfhero__beat-img { transform: scale(1.06); }
.sms-lfhero .sms-lfhero__beat-link:hover .sms-lfhero__beat-name { color: var(--sms-green); }
.sms-lfhero .sms-lfhero__note { margin: 1.25rem auto 0; padding: 0 var(--sms-gutter); max-width: var(--sms-max); color: var(--sms-ink-soft); font-size: var(--sms-step--1); }
.sms-lfhero .sms-lfhero__note p { margin: 0; }
@media (min-width: 52em) {
  .sms-lfhero .sms-lfhero__row { grid-template-columns: minmax(0, 1fr) auto; column-gap: 3rem; }
  .sms-lfhero .sms-lfhero__actions { justify-content: flex-end; }
}
@media (min-width: 64em) {
  .sms-lfhero { padding-bottom: clamp(2rem, 1rem + 2vw, 3rem); }
  .sms-lfhero .sms-lfhero__svg--wide { display: block; }
  .sms-lfhero .sms-lfhero__svg--narrow { display: none; }
  .sms-lfhero .sms-lfhero__beats { position: absolute; inset: 0; display: block; margin: 0; padding: 0; }
  .sms-lfhero .sms-lfhero__beat { position: absolute; left: calc(var(--x) - 3.7cqw); top: calc(var(--y) - 3.7cqw); }
  .sms-lfhero .sms-lfhero__beat-link { flex-direction: row; align-items: center; gap: 0.9rem; text-align: left; }
  .sms-lfhero .sms-lfhero__beat-photo { width: 7.4cqw; }
  .sms-lfhero .sms-lfhero__beat-label { align-items: flex-start; max-width: 11.5cqw; padding: 0.55rem 0.85rem; border: 1px solid var(--sms-lf-line); border-radius: 0.9rem; background: rgba(255, 255, 255, 0.92); box-shadow: 0 10px 24px rgba(6, 30, 53, 0.07); }
  .sms-lfhero .sms-lfhero__beat-name { font-size: clamp(0.78rem, 0.6rem + 0.3vw, 0.9375rem); }
  .sms-lfhero .sms-lfhero__note { margin-top: 0.5rem; }
}

/* ---------- Vertical lifeline (homepage, wide screens) ---------- */
.sms-lifeline { position: relative; }
.sms-lifeline .sms-lifeline__rail,
.sms-lifeline .sms-lifeline__mark { display: none; }
@supports (animation-timeline: view()) {
  @media (min-width: 80em) {
    .sms-lifeline .sms-lifeline__rail { position: absolute; z-index: 2; top: 5.5rem; bottom: 6rem; left: calc(max(0px, (100% - var(--sms-max)) / 2) + var(--sms-gutter) - 2.75rem); display: block; width: 2px; border-radius: 2px; background: var(--sms-lf-line); pointer-events: none; view-timeline: --sms-lfrail block; }
    .sms-lifeline .sms-lifeline__fill { position: absolute; inset: 0; display: block; border-radius: 2px; background: linear-gradient(180deg, #82d06e, var(--sms-green) 30%); transform-origin: top; animation: sms-lf-grow linear both; animation-timeline: --sms-lfrail; animation-range: cover 50vh cover calc(100% - 50vh); }
    .sms-lifeline .sms-lifeline__track { position: absolute; inset: 0; display: block; animation: sms-lf-track linear both; animation-timeline: --sms-lfrail; animation-range: cover 50vh cover calc(100% - 50vh); }
    .sms-lifeline .sms-lifeline__dot { position: absolute; left: 50%; bottom: 0; display: block; width: 0.75rem; height: 0.75rem; margin: 0 0 -0.375rem -0.375rem; border-radius: 50%; background: var(--sms-green); box-shadow: 0 0 0 5px rgba(64, 127, 54, 0.16), 0 0 18px rgba(64, 127, 54, 0.5); }
    .sms-lifeline .sms-lifeline__mark { position: absolute; z-index: 3; left: -2.75rem; top: 0.1rem; display: block; width: 1.4rem; height: 1.4rem; margin-left: calc(-0.7rem + 1px); border: 2px solid var(--sms-green); border-radius: 50%; background: var(--sms-white); pointer-events: none; }
    .sms-lifeline .sms-lifeline__mark--island,
    .sms-lifeline .sms-lifeline__mark--cta { left: calc(-2.75rem - var(--sms-lf-pad)); }
    .sms-lifeline .sms-lifeline__mark-on { position: absolute; inset: 3px; display: block; border-radius: 50%; background: var(--sms-green); animation: sms-lf-mark linear both; animation-timeline: view(); animation-range: cover 46% cover 50%; }
    .sms-lifeline .sms-lifeline__mark-ring { position: absolute; inset: -2px; display: block; border: 2px solid var(--sms-green); border-radius: 50%; opacity: 0; animation: sms-lf-markring linear both; animation-timeline: view(); animation-range: cover 48% cover 58%; }
    .sms-lifeline .sms-lfmon__heading,
    .sms-lifeline .sms-lfjourney__head,
    .sms-lifeline .sms-lfisland__copy,
    .sms-lifeline .sms-faq__head,
    .sms-lifeline .sms-lfcta__copy { position: relative; }
    .sms-lifeline .sms-faq__head { position: sticky; }
  }
}
@keyframes sms-lf-grow { from { transform: scaleY(0); } to { transform: scaleY(1); } }
@keyframes sms-lf-track { from { transform: translateY(-100%); } to { transform: translateY(0); } }
@keyframes sms-lf-mark { from { opacity: 0; transform: scale(0.3); } to { opacity: 1; transform: none; } }
@keyframes sms-lf-markring { 0% { opacity: 0; transform: scale(1); } 20% { opacity: 0.8; transform: scale(1.2); } 100% { opacity: 0; transform: scale(2.6); } }

/* ---------- Home: services as monitors ---------- */
.sms-lfmon { position: relative; padding: var(--sms-section) 0; background: var(--sms-pale); }
.sms-lfmon .sms-lfmon__inner { width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-lfmon .sms-lfmon__head { display: grid; gap: 0.5rem 3rem; align-items: end; margin-bottom: clamp(2rem, 1.5rem + 2vw, 3.25rem); }
.sms-lfmon .sms-lfmon__heading,
.sms-lfmon .sms-lfmon__lead { min-width: 0; }
.sms-lfmon .sms-lfmon__lead p { margin: 0; }
.sms-lfmon .sms-lfmon__lead { font-size: clamp(1.0625rem, 1rem + 0.35vw, 1.25rem); }
.sms-lfmon .sms-lfmon__grid { display: grid; gap: clamp(1rem, 0.6rem + 1.5vw, 1.5rem); margin: 0; padding: 0; list-style: none; }
.sms-lfmon .sms-lfmon__item { display: flex; min-width: 0; }
.sms-lfmon .sms-lfmon__card { position: relative; display: flex; flex-direction: column; flex: 1 1 auto; min-width: 0; padding: 0.75rem 0.75rem 1.75rem; border: 1px solid var(--sms-lf-line); border-radius: 1.75rem; background: var(--sms-white); box-shadow: var(--sms-shadow); transition: transform 0.45s var(--sms-ease), box-shadow 0.45s var(--sms-ease), border-color 0.45s var(--sms-ease); }
.sms-lfmon .sms-lfmon__card:hover,
.sms-lfmon .sms-lfmon__card:focus-within { transform: translateY(-6px); border-color: #b9d6b2; box-shadow: var(--sms-shadow-lg); }
.sms-lfmon .sms-lfmon__screen { position: relative; min-width: 0; padding: 1.1rem 0.6rem 0.9rem; overflow: hidden; border-radius: 1.2rem; background-color: var(--sms-pale); background-image: linear-gradient(var(--sms-lf-grid) 1px, transparent 1px), linear-gradient(90deg, var(--sms-lf-grid) 1px, transparent 1px); background-size: 16px 16px; background-position: -1px -1px; transition: background-color 0.45s var(--sms-ease); }
.sms-lfmon .sms-lfmon__num { position: absolute; left: 0.7rem; top: 0.55rem; padding: 0 0.2rem; background: var(--sms-pale); color: var(--sms-green); font-size: 0.72rem; font-weight: 800; letter-spacing: 0.14em; }
.sms-lfmon .sms-lfmon__screen .sms-lfsweep { width: 100%; height: auto; }
.sms-lfmon .sms-lfmon__body { display: flex; flex-direction: column; flex: 1 1 auto; min-width: 0; padding: 0 1rem; }
.sms-lfmon .sms-lfmon__icon { width: 3.25rem; height: 3.25rem; margin: -1.6rem 0 1rem 0.25rem; padding: 0.75rem; border: 3px solid var(--sms-white); border-radius: 50%; background: var(--sms-green); color: var(--sms-white); box-shadow: 0 8px 18px rgba(64, 127, 54, 0.28); position: relative; }
.sms-lfmon .sms-lfmon__name,
.sms-lfmon .sms-lfmon__text,
.sms-lfmon .sms-lfmon__list { min-width: 0; }
.sms-lfmon .sms-lfmon__name { margin: 0 0 0.5rem; font-size: clamp(1.25rem, 1.1rem + 0.5vw, 1.5rem); font-weight: 800; line-height: 1.2; letter-spacing: -0.025em; }
.sms-lfmon .sms-lfmon__name-link { color: var(--sms-navy); text-decoration: none; }
.sms-lfmon .sms-lfmon__name-link:hover { color: var(--sms-green); }
.sms-lfmon .sms-lfmon__text { margin: 0 0 1.1rem; color: var(--sms-ink-soft); }
.sms-lfmon .sms-lfmon__list { display: grid; gap: 0.1rem; margin: 0 0 1.5rem; padding: 0.4rem 0 0; border-top: 1px solid var(--sms-lf-line); list-style: none; font-size: var(--sms-step--1); }
.sms-lfmon .sms-lfmon__li { display: flex; align-items: center; gap: 0.65rem; min-width: 0; padding: 0.5rem 0; border-bottom: 1px dashed var(--sms-lf-line); font-weight: 600; line-height: 1.4; }
.sms-lfmon .sms-lfmon__li-icon { width: 1.2rem; height: 1.2rem; color: var(--sms-green); }
.sms-lfmon .sms-lfmon__li-text { min-width: 0; }
.sms-lfmon .sms-lfmon__actions { display: flex; flex-wrap: wrap; align-items: center; gap: 0.75rem 1.25rem; min-width: 0; margin-top: auto; }
.sms-lfmon .sms-lfmon__cta { font-size: 0.875rem; }
.sms-lfmon .sms-lfmon__more { min-width: 0; color: var(--sms-navy); font-size: var(--sms-step--1); font-weight: 700; text-decoration-color: var(--sms-green); text-decoration-thickness: 2px; text-underline-offset: 4px; }
.sms-lfmon .sms-lfmon__more:hover { color: var(--sms-green); }
.sms-lfmon .sms-lfmon__minor { display: grid; gap: clamp(1rem, 0.6rem + 1.5vw, 1.5rem); margin: clamp(1rem, 0.6rem + 1.5vw, 1.5rem) 0 0; padding: 0; list-style: none; }
.sms-lfmon .sms-lfmon__mitem { display: flex; min-width: 0; }
.sms-lfmon .sms-lfmon__mcard { display: grid; grid-template-columns: auto minmax(0, 1fr); gap: 0.25rem 1.1rem; align-items: start; flex: 1 1 auto; min-width: 0; padding: 1.4rem 1.5rem; border: 1px solid var(--sms-lf-line); border-radius: 1.5rem; background: rgba(255, 255, 255, 0.7); color: var(--sms-navy); text-decoration: none; transition: transform 0.4s var(--sms-ease), background-color 0.4s var(--sms-ease); }
.sms-lfmon .sms-lfmon__mcard:hover { transform: translateY(-4px); background: var(--sms-white); }
.sms-lfmon .sms-lfmon__micon { grid-row: span 3; width: 2.9rem; height: 2.9rem; padding: 0.65rem; border-radius: 50%; background: var(--sms-mint); color: var(--sms-green); }
.sms-lfmon .sms-lfmon__mname { min-width: 0; margin: 0; font-size: var(--sms-step-1); font-weight: 800; line-height: 1.3; letter-spacing: -0.02em; }
.sms-lfmon .sms-lfmon__mtext { min-width: 0; margin: 0; color: var(--sms-ink-soft); font-size: var(--sms-step--1); }
.sms-lfmon .sms-lfmon__mgo { min-width: 0; margin-top: 0.35rem; color: var(--sms-green); font-size: var(--sms-step--1); font-weight: 700; }
.sms-lfmon .sms-lfmon__tag { display: inline-block; margin-left: 0.4rem; padding: 0.1rem 0.5rem; border-radius: 999px; background: var(--sms-pale-2); color: var(--sms-ink-soft); font-size: 0.7rem; font-weight: 700; letter-spacing: 0.08em; text-transform: uppercase; vertical-align: middle; }
@media (min-width: 52em) {
  .sms-lfmon .sms-lfmon__head { grid-template-columns: minmax(0, 1.05fr) minmax(0, 0.95fr); }
  .sms-lfmon .sms-lfmon__minor { grid-template-columns: repeat(2, minmax(0, 1fr)); }
}
@media (min-width: 64em) {
  .sms-lfmon .sms-lfmon__grid { grid-template-columns: repeat(3, minmax(0, 1fr)); }
}

/* ---------- Booking journey (home + event medical cover) ---------- */
.sms-lfjourney { position: relative; padding: var(--sms-section) 0; background: var(--sms-white); view-timeline: --sms-lfj block; }
.sms-lfjourney .sms-lfjourney__inner { width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-lfjourney .sms-lfjourney__head { max-width: 44rem; margin-bottom: clamp(2rem, 1.5rem + 2vw, 3.5rem); }
.sms-lfjourney .sms-lfjourney__track { position: relative; container-type: inline-size; }
.sms-lfjourney .sms-lfjourney__svg { display: none; }
.sms-lfjourney .sms-lfjourney__list { position: relative; z-index: 1; display: grid; gap: 1.75rem; margin: 0; padding: 0; list-style: none; counter-reset: sms-lfj; }
.sms-lfjourney .sms-lfjourney__rail { position: absolute; z-index: 0; left: 1.45rem; top: 1.5rem; bottom: 1.5rem; width: 2px; margin-left: -1px; background: var(--sms-lf-line); }
.sms-lfjourney .sms-lfjourney__rail-fill { display: block; width: 100%; height: 100%; background: var(--sms-green); transform-origin: top; }
.sms-lfjourney .sms-lfjourney__step { position: relative; display: grid; align-content: start; grid-template-columns: 2.9rem minmax(0, 1fr); gap: 0 1.1rem; min-width: 0; }
.sms-lfjourney .sms-lfjourney__beat { position: relative; display: grid; place-items: center; grid-row: span 2; min-width: 0; width: 2.9rem; height: 2.9rem; border: 2px solid var(--sms-green); border-radius: 50%; background: var(--sms-white); color: var(--sms-green); font-size: 0.85rem; font-weight: 800; box-shadow: 0 0 0 6px var(--sms-white); }
.sms-lfjourney .sms-lfjourney__beat-on { position: absolute; inset: -2px; display: grid; place-items: center; border-radius: 50%; background: var(--sms-green); color: var(--sms-white); box-shadow: 0 0 0 6px rgba(64, 127, 54, 0.14); }
.sms-lfjourney .sms-lfjourney__name { min-width: 0; margin: 0.35rem 0 0.35rem; font-size: var(--sms-step-1); font-weight: 800; line-height: 1.3; letter-spacing: -0.02em; }
.sms-lfjourney .sms-lfjourney__text { min-width: 0; margin: 0; color: var(--sms-ink-soft); }
.sms-lfjourney .sms-lfjourney__foot { display: grid; gap: 1.5rem 3rem; align-items: start; margin-top: clamp(2.5rem, 2rem + 2vw, 3.5rem); padding-top: clamp(2rem, 1.5rem + 1.5vw, 2.75rem); border-top: 1px solid var(--sms-lf-line); }
.sms-lfjourney .sms-lfjourney__foot-main { min-width: 0; }
.sms-lfjourney .sms-lfjourney__foot-title { margin: 0 0 1rem; font-size: var(--sms-step-0); font-weight: 800; }
.sms-lfjourney .sms-chips__item { background: var(--sms-pale); border-color: transparent; }
.sms-lfjourney .sms-lfjourney__actions { display: flex; flex-wrap: wrap; gap: 0.75rem; min-width: 0; }
@media (min-width: 60em) {
  .sms-lfjourney .sms-lfjourney__svg { display: block; width: 100%; height: auto; }
  .sms-lfjourney .sms-lfjourney__svg-base { fill: none; stroke: var(--sms-lf-line); stroke-width: 2; stroke-linejoin: round; stroke-linecap: round; }
  .sms-lfjourney .sms-lfjourney__svg-fill { fill: none; stroke: var(--sms-green); stroke-width: 2.6; stroke-linejoin: round; stroke-linecap: round; stroke-dasharray: 1; stroke-dashoffset: 0; }
  .sms-lfjourney .sms-lfjourney__rail { display: none; }
  .sms-lfjourney .sms-lfjourney__list { grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 0; margin-top: calc(-10cqw + 2.1667cqw - 1.45rem); }
  .sms-lfjourney .sms-lfjourney__step { grid-template-columns: minmax(0, 1fr); justify-items: center; padding: 0 1.25rem; text-align: center; }
  .sms-lfjourney .sms-lfjourney__beat { grid-row: auto; margin-bottom: calc(10cqw - 2.1667cqw - 1.45rem + 1.5rem); box-shadow: 0 0 0 7px var(--sms-white); }
  .sms-lfjourney .sms-lfjourney__foot { grid-template-columns: minmax(0, 1fr) auto; align-items: end; }
}
@supports (animation-timeline: view()) {
  .sms-lfjourney .sms-lfjourney__svg-fill { animation: sms-lf-draw linear both; animation-timeline: --sms-lfj; animation-range: cover 22% cover 58%; }
  .sms-lfjourney .sms-lfjourney__beat-on { animation: sms-lf-mark linear both; animation-timeline: view(); animation-range: cover 38% cover 46%; }
  .sms-lfjourney .sms-lfjourney__rail-fill { animation: sms-lf-grow linear both; animation-timeline: view(); animation-range: cover 50vh cover calc(100% - 50vh); }
  @media (min-width: 60em) {
    .sms-lfjourney .sms-lfjourney__beat-on { animation-timeline: --sms-lfj; }
  }
}

/* ---------- Home: about island (the one navy feature) ---------- */
.sms-lfisland { --sms-lf-pad: clamp(1.5rem, 0.6rem + 4vw, 4.5rem); position: relative; padding: var(--sms-section) 0; background: var(--sms-white); }
.sms-lfisland .sms-lfisland__inner { width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-lfisland .sms-lfisland__box { position: relative; padding: max(6rem, calc(var(--sms-lf-pad) + 1.5rem)) var(--sms-lf-pad) var(--sms-lf-pad); border-radius: 2.25rem; background: radial-gradient(60rem 30rem at 85% 0%, #0b3152, var(--sms-navy) 70%); color: rgba(255, 255, 255, 0.86); }
.sms-lfisland .sms-lfisland__trace { position: absolute; left: 0; right: 0; top: 1.25rem; height: 4rem; color: var(--sms-green-on-navy); opacity: 0.45; }
.sms-lfisland .sms-lfdraw { width: 100%; height: 100%; }
.sms-lfisland .sms-lfisland__grid { position: relative; display: grid; gap: clamp(2rem, 1.5rem + 3vw, 4.5rem); align-items: center; }
.sms-lfisland .sms-lfisland__copy { min-width: 0; }
.sms-lfisland .sms-lfkick { color: var(--sms-green-on-navy); }
.sms-lfisland .sms-lftitle { color: var(--sms-white); }
.sms-lfisland .sms-lftitle .sms-mark { color: var(--sms-green-on-navy); }
.sms-lfisland .sms-lfisland__text { max-width: 36rem; font-size: var(--sms-step-1); line-height: 1.6; color: rgba(255, 255, 255, 0.9); }
.sms-lfisland .sms-lfisland__text p { margin: 0; }
.sms-lfisland .sms-more__toggle { color: var(--sms-green-on-navy); }
.sms-lfisland .sms-more__body { color: rgba(255, 255, 255, 0.8); }
.sms-lfisland .sms-more__toggle:focus-visible,
.sms-lfisland .sms-btn:focus-visible { outline-color: var(--sms-green-on-navy); }
.sms-lfisland .sms-lfisland__actions { display: flex; flex-wrap: wrap; gap: 0.75rem; margin-top: 1.75rem; }
.sms-lfisland .sms-btn--outline { border-color: rgba(255, 255, 255, 0.35); color: var(--sms-white); }
.sms-lfisland .sms-btn--outline:hover { border-color: var(--sms-white); background: var(--sms-white); color: var(--sms-navy); }
.sms-lfisland .sms-btn--primary { border-color: var(--sms-green-on-navy); background: var(--sms-green-on-navy); color: var(--sms-navy); box-shadow: none; }
.sms-lfisland .sms-lfisland__media { position: relative; min-width: 0; }
.sms-lfisland .sms-lfisland__frame { aspect-ratio: 4 / 3.3; border-radius: 1.75rem; }
.sms-lfisland .sms-lfisland__claim { position: relative; margin: -2.5rem 0.75rem 0; display: flex; gap: 1rem; align-items: flex-start; padding: 1.25rem 1.4rem; border-radius: 1.25rem; background: var(--sms-white); color: var(--sms-navy); box-shadow: 0 24px 50px rgba(0, 0, 0, 0.3); }
.sms-lfisland .sms-lfisland__claim-icon { width: 2.75rem; height: 2.75rem; padding: 0.6rem; border-radius: 50%; background: var(--sms-green); color: var(--sms-white); }
.sms-lfisland .sms-lfisland__claim-text { min-width: 0; font-weight: 700; line-height: 1.45; }
.sms-lfisland .sms-lfisland__claim-text p { margin: 0; }
.sms-lfisland .sms-lfisland__trust { display: grid; gap: 0; margin: clamp(2.5rem, 2rem + 2vw, 4rem) 0 0; padding: 0; border-top: 1px solid rgba(255, 255, 255, 0.14); list-style: none; }
.sms-lfisland .sms-lfisland__value { display: grid; align-content: start; grid-template-columns: auto minmax(0, 1fr); gap: 0.2rem 1rem; min-width: 0; padding: 1.5rem 0; border-bottom: 1px solid rgba(255, 255, 255, 0.14); }
.sms-lfisland .sms-lfisland__value-icon { grid-row: span 2; width: 2.75rem; height: 2.75rem; padding: 0.6rem; border: 1px solid rgba(130, 208, 110, 0.4); border-radius: 50%; color: var(--sms-green-on-navy); }
.sms-lfisland .sms-lfisland__value-name { min-width: 0; margin: 0.2rem 0 0.25rem; color: var(--sms-white); font-size: var(--sms-step-0); font-weight: 800; letter-spacing: -0.01em; }
.sms-lfisland .sms-lfisland__value-text { min-width: 0; margin: 0; color: rgba(255, 255, 255, 0.78); font-size: var(--sms-step--1); }
@media (min-width: 56em) {
  .sms-lfisland .sms-lfisland__grid { grid-template-columns: minmax(0, 1.05fr) minmax(0, 0.95fr); }
  .sms-lfisland .sms-lfisland__media { padding-bottom: 3rem; }
  .sms-lfisland .sms-lfisland__claim { position: absolute; left: 1.5rem; right: 1.5rem; bottom: 0; margin: 0; }
  .sms-lfisland .sms-lfisland__trust { grid-template-columns: repeat(2, minmax(0, 1fr)); column-gap: 2.5rem; }
}
@media (min-width: 72em) {
  .sms-lfisland .sms-lfisland__trust { grid-template-columns: repeat(4, minmax(0, 1fr)); border-bottom: 1px solid rgba(255, 255, 255, 0.14); }
  .sms-lfisland .sms-lfisland__value { grid-template-columns: minmax(0, 1fr); padding: 1.75rem 0 0.5rem; border-bottom: 0; }
  .sms-lfisland .sms-lfisland__value-icon { grid-row: auto; margin-bottom: 0.75rem; }
  .sms-lfisland .sms-lfisland__value-text { padding-bottom: 1.25rem; }
}

/* ---------- Inner page hero ---------- */
.sms-lfphero { position: relative; overflow: hidden; padding: clamp(2.5rem, 1.5rem + 4vw, 5rem) 0 clamp(5rem, 4rem + 3vw, 6.5rem); background: var(--sms-white); }
.sms-lfphero .sms-lfphero__grid { -webkit-mask-image: radial-gradient(60% 70% at 75% 55%, #000 15%, transparent 75%); mask-image: radial-gradient(60% 70% at 75% 55%, #000 15%, transparent 75%); }
.sms-lfphero .sms-lfphero__inner { position: relative; z-index: 1; display: grid; gap: clamp(2.5rem, 1.5rem + 4vw, 5rem); align-items: center; width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-lfphero .sms-lfphero__copy { min-width: 0; }
.sms-lfphero .sms-lfphero__crumb { display: flex; flex-wrap: wrap; gap: 0.4rem; margin-bottom: 1.25rem; color: var(--sms-ink-soft); font-size: var(--sms-step--1); }
.sms-lfphero .sms-lfphero__crumb-link { min-width: 0; color: var(--sms-ink-soft); text-underline-offset: 3px; }
.sms-lfphero .sms-lfphero__crumb-link:hover { color: var(--sms-green); }
.sms-lfphero .sms-lfphero__crumb-sep,
.sms-lfphero .sms-lfphero__crumb-here { min-width: 0; }
.sms-lfphero .sms-lfphero__title { margin: 0 0 1.25rem; font-size: var(--sms-step-3); font-weight: 800; line-height: 1.04; letter-spacing: -0.04em; }
.sms-lfphero .sms-lfphero__sub { margin-bottom: 0.75rem; color: var(--sms-navy); font-size: var(--sms-step-1); font-weight: 700; line-height: 1.45; }
.sms-lfphero .sms-lfphero__body { max-width: 34rem; color: var(--sms-ink-soft); font-size: var(--sms-step-1); line-height: 1.6; }
.sms-lfphero .sms-lfphero__body p { margin: 0; }
.sms-lfphero .sms-lfphero__actions { display: flex; flex-wrap: wrap; gap: 0.75rem; margin-top: 1.9rem; }
.sms-lfphero .sms-lfphero__media { position: relative; min-width: 0; width: 100%; max-width: 32rem; margin: 0 auto; }
.sms-lfphero .sms-lfphero__visual { position: relative; min-width: 0; padding-bottom: 2.5rem; }
.sms-lfphero .sms-lfphero__frame { aspect-ratio: 4 / 4.2; border-radius: 2rem; box-shadow: var(--sms-shadow-lg); }
.sms-lfphero .sms-lfphero__monitor { position: absolute; z-index: 2; left: 0.75rem; bottom: 0; width: min(15rem, 62%); padding: 0.7rem 0.8rem 0.55rem; border: 1px solid var(--sms-lf-line); border-radius: 1.1rem; background: var(--sms-white); box-shadow: var(--sms-shadow-lg); }
.sms-lfphero .sms-lfphero__monitor .sms-lfsweep { width: 100%; height: auto; }
.sms-lfphero .sms-lfphero__chips { position: relative; z-index: 2; display: flex; flex-wrap: wrap; gap: 0.5rem; margin: 1.25rem 0 0; padding: 0; list-style: none; }
.sms-lfphero .sms-lfphero__chip { display: inline-flex; align-items: center; gap: 0.5rem; min-width: 0; padding: 0.5rem 0.95rem 0.5rem 0.5rem; border: 1px solid var(--sms-lf-line); border-radius: 999px; background: var(--sms-white); box-shadow: 0 12px 28px rgba(6, 30, 53, 0.12); font-size: var(--sms-step--1); font-weight: 700; line-height: 1.3; }
.sms-lfphero .sms-lfphero__chip-icon { width: 1.9rem; height: 1.9rem; padding: 0.4rem; border-radius: 50%; background: var(--sms-mint); color: var(--sms-green); }
.sms-lfphero .sms-lfphero__chip-text { min-width: 0; overflow-wrap: anywhere; }
.sms-lfphero .sms-lfphero__trace { position: absolute; z-index: 0; left: 0; right: 0; bottom: 1rem; height: 4.5rem; color: var(--sms-mint); }
.sms-lfphero .sms-lfdraw { width: 100%; height: 100%; }
.sms-lfphero .sms-lfdraw__line { stroke-width: 2.4; }
@media (min-width: 56em) {
  .sms-lfphero .sms-lfphero__inner { grid-template-columns: minmax(0, 1.1fr) minmax(0, 0.9fr); }
  .sms-lfphero .sms-lfphero__media { max-width: none; }
  .sms-lfphero .sms-lfphero__monitor { left: -2rem; }
  .sms-lfphero .sms-lfphero__chips { position: absolute; right: -1.25rem; top: 1.25rem; display: grid; justify-items: end; max-width: 80%; margin: 0; }
}

/* ---------- CTA band with a trace ---------- */
.sms-lfcta { padding: var(--sms-section) 0; background: var(--sms-white); }
.sms-lfcta .sms-lfcta__inner { width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-lfcta { --sms-lf-pad: clamp(2rem, 1.2rem + 3.5vw, 4.25rem); }
.sms-lfcta .sms-lfcta__box { position: relative; display: grid; gap: 2rem; align-items: center; padding: var(--sms-lf-pad); padding-bottom: clamp(5rem, 4rem + 3vw, 6.5rem); border: 1px solid #d3e4cf; border-radius: 2.25rem; background: var(--sms-pale-2); }
.sms-lfcta .sms-lfcta__trace { position: absolute; left: 0; right: 0; bottom: 1.25rem; height: 4.5rem; overflow: hidden; border-radius: 0 0 2.25rem 2.25rem; color: var(--sms-green); opacity: 0.5; pointer-events: none; }
.sms-lfcta .sms-lfdraw { width: 100%; height: 100%; }
.sms-lfcta .sms-lfcta__copy { position: relative; min-width: 0; }
.sms-lfcta .sms-lfcta__icon { width: 3.25rem; height: 3.25rem; margin-bottom: 1.25rem; padding: 0.75rem; border-radius: 50%; background: var(--sms-green); color: var(--sms-white); box-shadow: 0 0 0 8px rgba(64, 127, 54, 0.12); }
.sms-lfcta .sms-lfcta__title { margin: 0 0 0.85rem; font-size: clamp(1.85rem, 1.2rem + 2.4vw, 3.25rem); font-weight: 800; line-height: 1.08; letter-spacing: -0.035em; }
.sms-lfcta .sms-lfcta__text { max-width: 38rem; color: var(--sms-ink-soft); font-size: var(--sms-step-1); line-height: 1.6; }
.sms-lfcta .sms-lfcta__text p { margin: 0; }
.sms-lfcta .sms-lfcta__side { position: relative; display: grid; gap: 1rem; justify-items: start; min-width: 0; }
.sms-lfcta .sms-lfcta__actions { display: flex; flex-wrap: wrap; gap: 0.75rem; min-width: 0; }
.sms-lfcta .sms-lfcta__call { min-width: 0; color: var(--sms-ink-soft); font-size: var(--sms-step--1); }
.sms-lfcta .sms-lfcta__call a { color: var(--sms-navy); font-weight: 700; text-decoration-color: var(--sms-green); text-decoration-thickness: 2px; text-underline-offset: 4px; }
@media (min-width: 60em) {
  .sms-lfcta .sms-lfcta__box { grid-template-columns: minmax(0, 1.4fr) minmax(0, 1fr); column-gap: 3rem; }
  .sms-lfcta .sms-lfcta__side { justify-items: end; text-align: right; }
  .sms-lfcta .sms-lfcta__actions { justify-content: flex-end; }
}
@supports (animation-timeline: view()) {
  .sms-lfcta .sms-lfdraw__line,
  .sms-lfisland .sms-lfdraw__line,
  .sms-footer .sms-lfdraw__line { animation: sms-lf-draw linear both; animation-timeline: view(); animation-range: entry 10% cover 45%; }
}

/* ---------- Medical training: course readout on a navy monitor ---------- */
.sms-lfread { position: relative; padding: var(--sms-section) 0; background: var(--sms-white); }
.sms-lfread .sms-lfread__inner { display: grid; gap: clamp(2rem, 1.5rem + 3vw, 4rem); align-items: start; width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-lfread .sms-lfread__copy { min-width: 0; }
.sms-lfread .sms-lfread__actions { display: flex; flex-wrap: wrap; gap: 0.75rem; margin-top: 1.75rem; }
.sms-lfread .sms-lfread__panel { min-width: 0; overflow: hidden; border-radius: 2rem; background: linear-gradient(170deg, #0b3152, var(--sms-navy) 55%); color: rgba(255, 255, 255, 0.86); box-shadow: var(--sms-shadow-lg); }
.sms-lfread .sms-lfread__screen { position: relative; padding: 1.25rem 1.25rem 0.75rem; border-bottom: 1px solid rgba(255, 255, 255, 0.1); background-image: linear-gradient(rgba(130, 208, 110, 0.07) 1px, transparent 1px), linear-gradient(90deg, rgba(130, 208, 110, 0.07) 1px, transparent 1px); background-size: 18px 18px; }
.sms-lfread .sms-lfread__screen .sms-lfsweep { width: 100%; height: auto; color: var(--sms-green-on-navy); }
.sms-lfread .sms-lfread__label { display: flex; justify-content: space-between; gap: 1rem; margin-bottom: 0.5rem; color: var(--sms-green-on-navy); font-size: 0.72rem; font-weight: 800; letter-spacing: 0.16em; text-transform: uppercase; }
.sms-lfread .sms-lfread__label-text { min-width: 0; padding: 0 0.25rem; background: #0b3152; }
.sms-lfread .sms-lfread__rows { margin: 0; padding: 0.5rem clamp(1rem, 0.5rem + 2vw, 2rem) 1rem; list-style: none; counter-reset: sms-lfread; }
.sms-lfread .sms-lfread__row { position: relative; display: grid; grid-template-columns: auto minmax(0, 1fr); gap: 0.35rem 1rem; align-items: start; min-width: 0; padding: 1.15rem 0; border-bottom: 1px solid rgba(255, 255, 255, 0.1); transition: transform 0.35s var(--sms-ease); }
.sms-lfread .sms-lfread__row:last-child { border-bottom: 0; }
.sms-lfread .sms-lfread__row:hover { transform: translateX(4px); }
.sms-lfread .sms-lfread__icon { grid-row: span 3; width: 2.6rem; height: 2.6rem; padding: 0.55rem; border: 1px solid rgba(130, 208, 110, 0.35); border-radius: 50%; color: var(--sms-green-on-navy); transition: background-color 0.35s var(--sms-ease), color 0.35s var(--sms-ease); }
.sms-lfread .sms-lfread__row:hover .sms-lfread__icon { background: var(--sms-green-on-navy); color: var(--sms-navy); }
.sms-lfread .sms-lfread__name { min-width: 0; margin: 0.35rem 0 0; color: var(--sms-white); font-size: var(--sms-step-0); font-weight: 800; line-height: 1.35; letter-spacing: -0.01em; }
.sms-lfread .sms-lfread__meta { display: flex; align-items: flex-start; gap: 0.45rem; min-width: 0; color: var(--sms-green-on-navy); font-size: var(--sms-step--1); font-weight: 600; line-height: 1.45; }
.sms-lfread .sms-lfread__meta-icon { width: 1rem; height: 1rem; margin-top: 0.15rem; }
.sms-lfread .sms-lfread__meta-text { min-width: 0; }
.sms-lfread .sms-lfread__text { min-width: 0; margin: 0; color: rgba(255, 255, 255, 0.75); font-size: var(--sms-step--1); }
@media (min-width: 60em) {
  .sms-lfread .sms-lfread__inner { grid-template-columns: minmax(0, 0.8fr) minmax(0, 1.2fr); }
  .sms-lfread .sms-lfread__copy { position: sticky; top: 7.5rem; }
  .sms-lfread .sms-lfread__row { grid-template-columns: auto minmax(0, 1fr) minmax(0, 14rem); }
  .sms-lfread .sms-lfread__icon { grid-row: span 2; }
  .sms-lfread .sms-lfread__meta { grid-column: 3; grid-row: 1 / span 2; justify-content: flex-end; padding-top: 0.4rem; text-align: right; }
  .sms-lfread .sms-lfread__text { grid-column: 2; }
}

/* ---------- Shared sections, restyled for Lifeline ---------- */
.sms-feature .sms-feature__frame { aspect-ratio: 4 / 3.5; border-radius: 1.75rem; box-shadow: var(--sms-shadow-lg); }
.sms-feature .sms-feature__blob { right: -1.5rem; bottom: -1.5rem; width: 82%; aspect-ratio: 16 / 10; border-radius: 1.75rem; background-color: var(--sms-pale-2); background-image: """ + ECG_TILE + """; background-size: 160px 64px; background-position: 0 50%; animation: none; }
.sms-feature.sms-tone-pale .sms-feature__blob { background-color: var(--sms-mint); }
.sms-feature.sms-feature--flip .sms-feature__blob { left: -1.5rem; right: auto; }
.sms-feature .sms-feature__lead { font-weight: 500; }
.sms-feature .sms-feature__strap { border: 1px solid #c6dfc0; background: var(--sms-pale-2); }
.sms-feature .sms-feature__chips-title { font-weight: 800; }
.sms-feature.sms-tone-white .sms-chips__item { border-color: transparent; background: var(--sms-pale); }

.sms-cards .sms-cards__item { border: 1px solid var(--sms-lf-line); border-radius: 1.5rem; background: var(--sms-white); box-shadow: none; }
.sms-cards.sms-tone-white .sms-cards__item { border-color: transparent; background: var(--sms-pale); }
.sms-cards .sms-cards__item:hover { box-shadow: var(--sms-shadow-lg); }
.sms-cards .sms-cards__item::before { content: ""; position: absolute; left: 1.6rem; right: 1.6rem; top: -1px; height: 3px; border-radius: 0 0 3px 3px; background: var(--sms-green); transform: scaleX(0); transform-origin: left; transition: transform 0.45s var(--sms-ease); }
.sms-cards .sms-cards__item:hover::before { transform: scaleX(1); }
.sms-cards .sms-cards__icon { border-radius: 50%; background: var(--sms-pale-2); }
.sms-cards.sms-tone-white .sms-cards__icon { background: var(--sms-white); }
.sms-cards .sms-cards__item:hover .sms-cards__icon { transform: scale(1.08); }
.sms-cards .sms-cards__num { font-size: 0.85rem; font-weight: 800; letter-spacing: 0.14em; }
.sms-cards .sms-cards__name { font-weight: 800; letter-spacing: -0.02em; }
.sms-cards .sms-cards__meta { border: 1px solid var(--sms-lf-line); background: var(--sms-white); }
.sms-cards .sms-cards__list-title { font-size: 0.75rem; letter-spacing: 0.12em; }

.sms-steps .sms-steps__line { background: var(--sms-lf-line); }
.sms-steps .sms-steps__badge { border: 2px solid var(--sms-green); background: var(--sms-white); color: var(--sms-green); }
.sms-steps .sms-steps__num { background: var(--sms-green); }
.sms-steps .sms-steps__name { font-size: var(--sms-step-1); font-weight: 800; letter-spacing: -0.015em; }
.sms-steps .sms-steps__note { border: 1px solid var(--sms-lf-line); background: var(--sms-white); }
.sms-steps.sms-tone-white .sms-steps__note { border-color: transparent; }

.sms-checklist .sms-checklist__item { border: 1px solid var(--sms-lf-line); background: var(--sms-white); font-weight: 700; }
.sms-checklist .sms-checklist__icon { background: var(--sms-pale-2); }

.sms-notice .sms-notice__box { border: 1px solid var(--sms-lf-line); border-radius: 1.75rem; box-shadow: none; }
.sms-notice .sms-notice__badge { background: var(--sms-pale-2); }
.sms-notice .sms-notice__title { font-weight: 800; letter-spacing: -0.015em; }

.sms-faq .sms-faq__item { border: 1px solid var(--sms-lf-line); border-radius: 1.1rem; background: var(--sms-white); box-shadow: none; transition: border-color 0.3s var(--sms-ease); }
.sms-faq.sms-tone-white .sms-faq__item { border-color: transparent; background: var(--sms-pale); }
.sms-faq .sms-faq__item[open] { border-color: #b9d6b2; }
.sms-faq .sms-faq__q { font-weight: 700; }
.sms-faq .sms-faq__q::after { background: var(--sms-pale-2); color: var(--sms-green); }
.sms-faq .sms-faq__item[open] .sms-faq__q::after { background: var(--sms-green); color: var(--sms-white); }
.sms-faq .sms-faq__all-toggle { border: 2px solid rgba(6, 30, 53, 0.22); }
.sms-faq .sms-faq__input { border-color: var(--sms-field-line); }

.sms-quotes .sms-quotes__item { border: 1px solid var(--sms-lf-line); border-radius: 1.75rem; background: var(--sms-pale); }
.sms-quotes .sms-quotes__icon { border-radius: 50%; }
.sms-quotes .sms-quotes__text { font-weight: 600; letter-spacing: -0.01em; }

.sms-people .sms-people__person { border: 1px solid var(--sms-lf-line); background: var(--sms-white); box-shadow: none; }
.sms-people.sms-tone-white .sms-people__person { border-color: transparent; background: var(--sms-pale); }
.sms-people .sms-people__role { background: var(--sms-pale-2); }
.sms-people .sms-people__name { font-weight: 800; letter-spacing: -0.02em; }
.sms-people .sms-people__frame { border-radius: 1.75rem; }
.sms-people .sms-people__shared { border: 1px solid #c6dfc0; background: var(--sms-pale); color: var(--sms-navy); }
.sms-people .sms-people__shared-label { color: var(--sms-green); }
.sms-people .sms-people__shared-title { font-weight: 800; }
.sms-people .sms-people__shared-text,
.sms-people .sms-people__shared .sms-more__body { color: var(--sms-ink-soft); }
.sms-people .sms-people__shared .sms-more__toggle { color: var(--sms-green); }

.sms-links .sms-links__link { border: 1px solid var(--sms-lf-line); box-shadow: none; }
.sms-links .sms-links__link:hover { box-shadow: var(--sms-shadow-lg); }
.sms-links .sms-links__icon { border-radius: 50%; background: var(--sms-pale-2); }
.sms-links .sms-links__name { font-weight: 800; letter-spacing: -0.02em; }

.sms-claim .sms-claim__icon { background: var(--sms-green); color: var(--sms-white); box-shadow: 0 0 0 8px rgba(64, 127, 54, 0.12); }
.sms-claim.sms-tone-pale .sms-claim__icon { background: var(--sms-green); }
.sms-claim .sms-claim__text { font-weight: 800; letter-spacing: -0.03em; }

.sms-marquee .sms-marquee__item { border: 1px solid var(--sms-lf-line); box-shadow: none; }

.sms-contact .sms-contact__detail { border: 1px solid transparent; }
.sms-contact .sms-contact__form { border: 1px solid var(--sms-lf-line); border-radius: 1.75rem; }
.sms-contact .sms-contact__booklink { border: 1px solid #c6dfc0; background: var(--sms-pale-2); }
.sms-contact .sms-contact__form-title { font-weight: 800; }

.sms-booking .sms-booking__form { border: 1px solid var(--sms-lf-line); border-radius: 1.75rem; box-shadow: var(--sms-shadow); }
.sms-booking .sms-booking__service-card { border-width: 1px; border-radius: 1.25rem; }
.sms-booking .sms-booking__service-input:checked + .sms-booking__service-card { box-shadow: 0 0 0 1px var(--sms-green); }
.sms-booking .sms-booking__service-icon { border-radius: 50%; background: var(--sms-pale-2); }
.sms-booking .sms-booking__step-title { font-weight: 800; letter-spacing: -0.025em; }
.sms-booking .sms-booking__chip-text { border-width: 1px; }
.sms-booking .sms-booking__summary { border-radius: 1.5rem; }
.sms-booking .sms-booking__help { border: 1px solid #c6dfc0; background: var(--sms-pale-2); }
""" + _beat_css() + _journey_css()

RISE = [".sms-lfhero .sms-lfhero__title", ".sms-lfphero .sms-lfphero__title"]
ENTRANCE = [".sms-page .sms-lfpill", ".sms-lfphero .sms-lfphero__crumb", ".sms-lfhero .sms-lfhero__lead", ".sms-lfhero .sms-lfhero__actions",
            ".sms-lfphero .sms-lfphero__sub", ".sms-lfphero .sms-lfphero__body", ".sms-lfphero .sms-lfphero__actions", ".sms-lfphero .sms-lfphero__media"]
REVEAL = [".sms-lfmon .sms-lfmon__head", ".sms-lfmon .sms-lfmon__item", ".sms-lfmon .sms-lfmon__mitem",
          ".sms-lfjourney .sms-lfjourney__head", ".sms-lfjourney .sms-lfjourney__text", ".sms-lfjourney .sms-lfjourney__foot",
          ".sms-lfisland .sms-lfisland__copy", ".sms-lfisland .sms-lfisland__media", ".sms-lfisland .sms-lfisland__value",
          ".sms-lfcta .sms-lfcta__copy", ".sms-lfcta .sms-lfcta__side", ".sms-lfread .sms-lfread__copy", ".sms-lfread .sms-lfread__panel"]
LOOP = [".sms-page .sms-lfpill__dot", ".sms-page .sms-lfsweep__line", ".sms-page .sms-lfsweep__head", ".sms-page .sms-lfdraw--load .sms-lfdraw__line",
        ".sms-lfhero .sms-lfhero__line", ".sms-lfhero .sms-lfhero__spark", ".sms-lfhero .sms-lfhero__dot", ".sms-lfhero .sms-lfhero__beat-photo",
        ".sms-lfhero .sms-lfhero__beat-ring", ".sms-lfhero .sms-lfhero__beat-label",
        ".sms-lifeline .sms-lifeline__fill", ".sms-lifeline .sms-lifeline__track", ".sms-lifeline .sms-lifeline__mark-on", ".sms-lifeline .sms-lifeline__mark-ring",
        ".sms-lfjourney .sms-lfjourney__svg-fill", ".sms-lfjourney .sms-lfjourney__beat-on", ".sms-lfjourney .sms-lfjourney__rail-fill",
        ".sms-lfcta .sms-lfdraw__line", ".sms-lfisland .sms-lfdraw__line", ".sms-footer .sms-lfdraw__line"]
TRANS = [".sms-lfhero .sms-lfhero__beat-img", ".sms-lfmon .sms-lfmon__card", ".sms-lfmon .sms-lfmon__screen", ".sms-lfmon .sms-lfmon__mcard",
         ".sms-cards .sms-cards__item::before", ".sms-faq .sms-faq__item", ".sms-lfread .sms-lfread__row", ".sms-lfread .sms-lfread__icon"]

SKIP = {"event-medical-cover": [2], "medical-training": [0]}


# ---------------------------------------------------------------------------
# Shared pieces
# ---------------------------------------------------------------------------

def stops(html_text):
    """Wrap full stops in titles so the wide Jakarta period sits tight and reads as a green beat."""
    return re.sub(r"\.(?=\s|<|$)", '<span class="sms-lfstop">.</span>', html_text)


def mark(cls=""):
    return '<span class="sms-lifeline__mark%s" aria-hidden="true"><span class="sms-lifeline__mark-ring"></span><span class="sms-lifeline__mark-on"></span></span>' % ((" " + cls) if cls else "")


def page_hero(ctx, h, crumb=True):
    crumb_html = ""
    if crumb:
        crumb_html = '<nav class="sms-lfphero__crumb" aria-label="Breadcrumb"><a class="sms-lfphero__crumb-link" href="%s">Home</a><span class="sms-lfphero__crumb-sep" aria-hidden="true">/</span><span class="sms-lfphero__crumb-here" aria-current="page">%s</span></nav>' % (
            ctx.href("home"), e(LABEL[ctx.slug]))
    sub = '<div class="sms-lfphero__sub">%s</div>' % e(h["sub"]) if h.get("sub") else ""
    acts = '<div class="sms-lfphero__actions">%s</div>' % buttons(ctx, h["buttons"]) if h.get("buttons") else ""
    chips_html = "".join('<li class="sms-lfphero__chip">%s<span class="sms-lfphero__chip-text">%s</span></li>' % (icon(ic, "sms-lfphero__chip-icon"), e(t)) for ic, t in h.get("chips", [])[:2])
    monitor = sweep("sms-lfphero__sweep", "sms-lf-g-ph", 220, 64, 42, [(55, 28), (150, 34)], 0.5, 2.8)
    trace = drawn("sms-lfdraw--load", 1440, 72, 50, [(180, 22), (1040, 30), (1250, 18)], 0.85, "none")
    return """<section class="sms-lfphero">
  <div class="sms-lfphero__grid" aria-hidden="true"></div>
  <div class="sms-lfphero__trace" aria-hidden="true">%s</div>
  <div class="sms-lfphero__inner">
    <div class="sms-lfphero__copy">
      %s
      <div class="sms-lfpill"><span class="sms-lfpill__dot" aria-hidden="true"></span><span class="sms-lfpill__text">%s</span></div>
      <h1 class="sms-lfphero__title">%s</h1>
      %s
      <div class="sms-lfphero__body">%s</div>
      %s
    </div>
    <div class="sms-lfphero__media">
      <div class="sms-lfphero__visual">%s
      <div class="sms-lfphero__monitor" aria-hidden="true">%s</div></div>
      <ul class="sms-lfphero__chips">%s</ul>
    </div>
  </div>
</section>
""" % (trace, crumb_html, e(h["eyebrow"]), stops(e(h["title"])), sub, paras(h["body"]), acts,
       photo(ctx, h["photo"], lazy=False, parallax=False, figcls="sms-lfphero__frame"), monitor, chips_html)


def cta(ctx, d, lifeline=False):
    btns = [(l, t) for l, t in d["buttons"] if t != "tel"]
    trace = drawn("sms-lfcta__svg", 1200, 110, 70, [(240, 44), (560, 62), (900, 40)], 1.0, "none")
    return """<section class="sms-lfcta">
  <div class="sms-lfcta__inner">
    <div class="sms-lfcta__box">
      <div class="sms-lfcta__trace" aria-hidden="true">%s</div>
      <div class="sms-lfcta__copy">%s%s<h2 class="sms-lfcta__title">%s</h2><div class="sms-lfcta__text">%s</div></div>
      <div class="sms-lfcta__side"><div class="sms-lfcta__actions">%s</div><div class="sms-lfcta__call">Or call us on <a href="tel:%s">%s</a></div></div>
    </div>
  </div>
</section>
""" % (trace, mark("sms-lifeline__mark--cta") if lifeline else "", icon("heart", "sms-lfcta__icon"), e(d["title"]), paras(d["text"]), buttons(ctx, btns) if btns else "", PHONE_TEL, PHONE)


def chrome_top(ctx):
    return header(ctx, "blue")


def chrome_bottom(ctx):
    trace = '<div class="sms-footer__trace" aria-hidden="true">%s</div>' % drawn("sms-footer__svg", 1440, 40, 26, [(300, 16), (1120, 20)], 0.6, "none")
    return footer(ctx, "white").replace('<footer class="sms-footer">', '<footer class="sms-footer">\n  ' + trace, 1)


# ---------------------------------------------------------------------------
# Signature sections
# ---------------------------------------------------------------------------

def journey(ctx, full=False, lifeline=False):
    sentences = BOOKING["body"]
    steps = ""
    for n, idx in enumerate(JOURNEY_ORDER, 1):
        steps += ('<li class="sms-lfjourney__step"><span class="sms-lfjourney__beat" aria-hidden="true">%02d<span class="sms-lfjourney__beat-on">%02d</span></span>'
                  '<h3 class="sms-lfjourney__name">%s</h3><p class="sms-lfjourney__text">%s</p></li>') % (n, n, e(JOURNEY_LABELS[n - 1]), e(sentences[idx]))
    svg = ('<svg class="sms-lfjourney__svg" viewBox="0 0 1200 120" aria-hidden="true" focusable="false"><path class="sms-lfjourney__svg-base" d="%s"></path>'
           '<path class="sms-lfjourney__svg-fill" d="%s" pathLength="1"></path></svg>') % (JOURNEY_D, JOURNEY_D)
    foot = ""
    if full:
        foot = """<div class="sms-lfjourney__foot">
        <div class="sms-lfjourney__foot-main"><h3 class="sms-lfjourney__foot-title">%s</h3>%s</div>
        <div class="sms-lfjourney__actions">%s</div>
      </div>""" % (e(BOOKING["chips_title"]), chips(BOOKING["chips"]), buttons(ctx, BOOKING["buttons"]))
    else:
        foot = """<div class="sms-lfjourney__foot">
        <div class="sms-lfjourney__foot-main"><p class="sms-lfjourney__text">%s</p></div>
        <div class="sms-lfjourney__actions">%s</div>
      </div>""" % (e(C.SERVICES[0]["text"]), buttons(ctx, [(C.SERVICES[0]["cta"], "book:event"), ("Event Medical Cover", "event-medical-cover")]))
    return """<section class="sms-lfjourney" id="booking-journey">
  <div class="sms-lfjourney__inner">
    <div class="sms-lfjourney__head">%s<div class="sms-lfkick">%s</div><h2 class="sms-lftitle">From enquiry to <span class="sms-mark">your event</span></h2></div>
    <div class="sms-lfjourney__track">
      %s
      <div class="sms-lfjourney__rail" aria-hidden="true"><span class="sms-lfjourney__rail-fill"></span></div>
      <ol class="sms-lfjourney__list">%s</ol>
    </div>
    %s
  </div>
</section>
""" % (mark() if lifeline else "", e(BOOKING["eyebrow"]), svg, steps, foot)


def readout(ctx):
    d = COURSES
    rows = ""
    for it in d["items"]:
        meta = '<div class="sms-lfread__meta">%s<span class="sms-lfread__meta-text">%s</span></div>' % (icon("clock", "sms-lfread__meta-icon"), e(it["meta"])) if it.get("meta") else ""
        text = '<p class="sms-lfread__text">%s</p>' % e(it["text"]) if it.get("text") else ""
        rows += '<li class="sms-lfread__row">%s<h3 class="sms-lfread__name">%s</h3>%s%s</li>' % (icon(it["icon"], "sms-lfread__icon"), e(it["title"]), meta, text)
    screen = sweep("sms-lfread__sweep", "sms-lf-g-rd", 640, 84, 54, [(90, 38), (250, 44), (410, 36), (560, 42)], 0.7, 4.2)
    hero_btns = C.PAGES["medical-training"]["hero"]["buttons"]
    return """<section class="sms-lfread" id="courses">
  <div class="sms-lfread__inner">
    <div class="sms-lfread__copy">
      <div class="sms-lfkick">%s</div>
      <h2 class="sms-lftitle">%s</h2>
      <div class="sms-lflead">%s</div>
      <div class="sms-lfread__actions">%s</div>
    </div>
    <div class="sms-lfread__panel">
      <div class="sms-lfread__screen" aria-hidden="true"><div class="sms-lfread__label"><span class="sms-lfread__label-text">Courses</span><span class="sms-lfread__label-text">Duration</span></div>%s</div>
      <ul class="sms-lfread__rows">%s</ul>
    </div>
  </div>
</section>
""" % (e(d["eyebrow"]), e(d["title"]), paras(d["lead"]), buttons(ctx, hero_btns[:1]), screen, rows)


def inner_extra(ctx, slug):
    if slug == "event-medical-cover":
        return journey(ctx, full=True)
    if slug == "medical-training":
        return readout(ctx)
    return ""


# ---------------------------------------------------------------------------
# Homepage
# ---------------------------------------------------------------------------

def hero(ctx):
    beats = ""
    for i, (s, ph) in enumerate(zip(C.SERVICES, ["festival", "cpr-room", "assessor"]), 1):
        cx = HERO_BEATS[2 * i - 1][0]
        tip = HERO_BASE - HERO_BEATS[2 * i - 1][1]
        beats += """<li class="sms-lfhero__beat sms-lfhero__beat--%d" style="--x: %.3f%%; --y: %.3f%%">
          <a class="sms-lfhero__beat-link" href="%s">
            <span class="sms-lfhero__beat-photo">%s<span class="sms-lfhero__beat-ring" aria-hidden="true"></span></span>
            <span class="sms-lfhero__beat-label"><span class="sms-lfhero__beat-name">%s</span><span class="sms-lfhero__beat-go" aria-hidden="true">Explore&nbsp;&rarr;</span></span>
          </a>
        </li>""" % (i, cx / HERO_W * 100, tip / HERO_H * 100, ctx.href(s["slug"]), photo_img(ctx, ph, "sms-lfhero__beat-img", lazy=False, decorative=True), e(s["title"]))
    wide = ('<svg class="sms-lfhero__svg sms-lfhero__svg--wide" viewBox="0 0 %d %d" aria-hidden="true" focusable="false">%s'
            '<path class="sms-lfhero__ghost" d="%s"></path><path class="sms-lfhero__line" d="%s" pathLength="1"></path>'
            '<path class="sms-lfhero__spark" d="%s" pathLength="1"></path>'
            '<g class="sms-lfhero__dot" style="offset-path: path(\'%s\')"><circle r="22" fill="url(#sms-lf-g-hero)"></circle><circle class="sms-lfhero__dot-core" r="6"></circle></g></svg>') % (
        HERO_W, HERO_H, _glow("sms-lf-g-hero"), HERO_D, HERO_D, HERO_D, HERO_D)
    narrow = ('<svg class="sms-lfhero__svg sms-lfhero__svg--narrow" viewBox="0 0 400 120" aria-hidden="true" focusable="false">%s'
              '<path class="sms-lfhero__ghost" d="%s"></path><path class="sms-lfhero__line" d="%s" pathLength="1"></path>'
              '<path class="sms-lfhero__spark" d="%s" pathLength="1"></path>'
              '<g class="sms-lfhero__dot" style="offset-path: path(\'%s\')"><circle r="14" fill="url(#sms-lf-g-hero2)"></circle><circle class="sms-lfhero__dot-core" r="4.5"></circle></g></svg>') % (
        _glow("sms-lf-g-hero2"), HERO_NARROW, HERO_NARROW, HERO_NARROW, HERO_NARROW)
    return """<section class="sms-lfhero">
  <div class="sms-lfhero__grid" aria-hidden="true"></div>
  <div class="sms-lfhero__inner">
    <div class="sms-lfhero__copy">
      <div class="sms-lfpill"><span class="sms-lfpill__dot" aria-hidden="true"></span><span class="sms-lfpill__text">Clinician-led safety and medical support</span></div>
      <h1 class="sms-lfhero__title">%s</h1>
      <div class="sms-lfhero__row">
        <div class="sms-lfhero__lead"><p>%s</p></div>
        <div class="sms-lfhero__actions">%s</div>
      </div>
    </div>
  </div>
  <div class="sms-lfhero__stage">
    %s
    %s
    <ul class="sms-lfhero__beats" aria-label="Our main services">%s</ul>
  </div>
</section>
""" % (stops(e("Protecting People. [[Supporting Business.]]")), e(C.INTRO2), buttons(ctx, [("Book online", "book"), ("Contact Us", "contact")]), wide, narrow, beats)


def monitors(ctx):
    rhythms = [([(60, 40), (165, 46), (268, 36)], 2.9), ([(85, 46), (225, 40)], 3.6), ([(55, 34), (150, 44), (250, 38)], 3.2)]
    cards = ""
    for i, s in enumerate(C.SERVICES):
        beats, dur = rhythms[i]
        items = "".join('<li class="sms-lfmon__li">%s<span class="sms-lfmon__li-text">%s</span></li>' % (icon(ic, "sms-lfmon__li-icon"), e(t)) for ic, t in s["list"])
        cards += """<li class="sms-lfmon__item">
        <article class="sms-lfmon__card" data-sms-quicken>
          <div class="sms-lfmon__screen" aria-hidden="true"><span class="sms-lfmon__num">%02d</span>%s</div>
          <div class="sms-lfmon__body">
            %s
            <h3 class="sms-lfmon__name"><a class="sms-lfmon__name-link" href="%s">%s</a></h3>
            <p class="sms-lfmon__text">%s</p>
            <ul class="sms-lfmon__list">%s</ul>
            <div class="sms-lfmon__actions"><a class="sms-btn sms-btn--primary sms-lfmon__cta" href="%s">%s&nbsp;<span class="sms-arrow" aria-hidden="true">&rarr;</span></a></div>
          </div>
        </article>
      </li>""" % (i + 1, sweep("sms-lfmon__sweep", "sms-lf-g-m%d" % i, 320, 96, 62, beats, 0.55, dur), icon(s["icon"], "sms-lfmon__icon"),
                  ctx.href(s["slug"]), e(s["title"]), e(s["text"]), items, link(ctx, "book:" + s["key"]), e(s["cta"]))
    rec = C.PAGES["recruitment"]["hero"]
    minor = [(C.CAREERS["icon"], C.CAREERS["title"], C.CAREERS["text"], C.CAREERS["cta"], C.CAREERS["slug"]),
             ("users", "Recruitment", rec["body"][0], "Interested in Working With Us?", "recruitment")]
    minors = "".join("""<li class="sms-lfmon__mitem"><a class="sms-lfmon__mcard" href="%s">%s<h3 class="sms-lfmon__mname">%s</h3><p class="sms-lfmon__mtext">%s</p><span class="sms-lfmon__mgo">%s&nbsp;<span class="sms-arrow" aria-hidden="true">&rarr;</span></span></a></li>""" % (
        ctx.href(slug), icon(ic, "sms-lfmon__micon"), e(t), e(x), e(go)) for ic, t, x, go, slug in minor)
    return """<section class="sms-lfmon" id="services">
  <div class="sms-lfmon__inner">
    <div class="sms-lfmon__head">
      <div class="sms-lfmon__heading">%s<div class="sms-lfkick">Our Services</div><h2 class="sms-lftitle">What We <span class="sms-mark">Provide</span></h2></div>
      <div class="sms-lfmon__lead sms-lflead"><p>%s</p></div>
    </div>
    <ul class="sms-lfmon__grid">%s</ul>
    <ul class="sms-lfmon__minor">%s</ul>
  </div>
</section>
""" % (mark(), e(C.INTRO), cards, minors)


def island(ctx):
    vals = "".join('<li class="sms-lfisland__value">%s<h3 class="sms-lfisland__value-name">%s</h3><p class="sms-lfisland__value-text">%s</p></li>' % (
        icon(ic, "sms-lfisland__value-icon"), e(t), e(x)) for ic, t, x in C.TRUST)
    trace = drawn("sms-lfisland__svg", 1200, 64, 40, [(170, 26), (500, 32), (830, 24), (1080, 30)], 0.8, "none")
    return """<section class="sms-lfisland" id="about">
  <div class="sms-lfisland__inner">
    <div class="sms-lfisland__box">
      <div class="sms-lfisland__trace" aria-hidden="true">%s</div>
      <div class="sms-lfisland__grid">
        <div class="sms-lfisland__copy">
          %s
          <div class="sms-lfkick">About Streamline</div>
          <h2 class="sms-lftitle">%s</h2>
          <div class="sms-lfisland__text"><p>%s</p></div>
          %s
          <div class="sms-lfisland__actions"><a class="sms-btn sms-btn--primary" href="%s">Meet The Directors&nbsp;<span class="sms-arrow" aria-hidden="true">&rarr;</span></a><a class="sms-btn sms-btn--outline" href="%s">Contact Us</a></div>
        </div>
        <div class="sms-lfisland__media">
          %s
          <div class="sms-lfisland__claim">%s<div class="sms-lfisland__claim-text"><p>%s</p></div></div>
        </div>
      </div>
      <ul class="sms-lfisland__trust">%s</ul>
    </div>
  </div>
</section>
""" % (trace, mark("sms-lifeline__mark--island"), stops(e(C.PAGES["about"]["hero"]["title"])), e(C.ABOUT_HOME[0]), more(paras(C.ABOUT_HOME[1:])),
       ctx.href("about"), ctx.href("contact"), photo(ctx, "team", figcls="sms-lfisland__frame"), icon("heart", "sms-lfisland__claim-icon"), e(C.CLAIM_15), vals)


def home(ctx):
    ctx.notes += ["Image-only copy used: \"Clinician-led safety and medical support\" (clinician-led-safety.png)",
                  "Image-only copy used: \"Mathew and Tom bring over 15 years of ambulance experience...\" (why-choose-us.png - use approved)",
                  "Booking journey steps use the four booking-information sentences from the Event Medical Cover page verbatim; the short step labels are interface labels"]
    out = hero(ctx)
    out += '<div class="sms-lifeline">\n<div class="sms-lifeline__rail" aria-hidden="true"><span class="sms-lifeline__fill"></span><span class="sms-lifeline__track"><span class="sms-lifeline__dot"></span></span></div>\n'
    out += monitors(ctx)
    out += journey(ctx, lifeline=True)
    out += island(ctx)
    picks = ["What services does Streamline provide?", "Where is Streamline based?", "Who runs Streamline?", "Are your services tailored?",
             "Do you offer a free initial discussion?", "Are you insured?"]
    allf = dict(C.faqs("home"))
    faq = SHARED_RENDERERS["faq"](ctx, {"tone": "pale", "eyebrow": C.STRAP, "title": "General Streamline [[FAQs]]",
                                        "lead": ["Answers to common questions about Streamline Safety & Medical Solutions, our team, services, bookings and how we work."],
                                        "items": [(q, allf[q]) for q in picks], "show": 6})
    out += faq.replace('<div class="sms-faq__head">', '<div class="sms-faq__head">' + mark(), 1)
    out += cta(ctx, {"title": "Have any questions? We’re here to help.", "text": ["Speak to our team and we will be happy to help."],
                     "buttons": [("Book online", "book"), ("Contact Us", "contact")]}, lifeline=True)
    out += "</div>\n"
    return out


def scripts(ctx, main):
    if "data-sms-quicken" not in main:
        return ""
    return """<script>
(function () {
  var reduce = window.matchMedia ? window.matchMedia('(prefers-reduced-motion: reduce)') : { matches: false };
  function rate(card, r) {
    if (reduce.matches || !card.getAnimations) return;
    card.getAnimations({ subtree: true }).forEach(function (a) {
      if (!a.animationName || a.animationName.indexOf('sms-lf-') !== 0) return;
      if (a.updatePlaybackRate) a.updatePlaybackRate(r); else a.playbackRate = r;
    });
  }
  Array.prototype.forEach.call(document.querySelectorAll('[data-sms-quicken]'), function (card) {
    card.addEventListener('mouseenter', function () { rate(card, 1.75); });
    card.addEventListener('mouseleave', function () { if (!card.contains(document.activeElement)) rate(card, 1); });
    card.addEventListener('focusin', function () { rate(card, 1.75); });
    card.addEventListener('focusout', function (ev) { if (!card.contains(ev.relatedTarget)) rate(card, 1); });
  });
})();
</script>
"""
