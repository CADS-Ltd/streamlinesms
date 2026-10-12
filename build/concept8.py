"""Concept 8 - Studio. Concept 5's layouts, motion and interactive pieces (the
centred hero over a self-sweeping photo comparison, tilting service tiles, the
course-length picker, the Skilled / Proportionate / Reliable diagrams and the
consultation timeline) in Streamline's original colour scheme: white and pale-green
sections, navy text and brand green, with navy diagram and call-to-action panels."""
from concept5 import *  # noqa: F401,F403
import concept5 as base
import light

NAME = "Studio"
DARK = False
CINE = True

CSS = base.CSS + light.css([
    ".sms-spr .sms-spr__card", ".sms-gcta .sms-gcta__box", ".sms-tiles .sms-tiles__item--big", ".sms-footer",
]) + r"""
/* ===== Concept 8: light details ===== */
.sms-page .sms-btn--primary:hover { box-shadow: 0 12px 40px var(--sms-glow); }
.sms-header .sms-header__inner { box-shadow: inset 0 0 0 1px var(--sms-line), 0 18px 50px rgba(6, 30, 53, 0.1); }
.sms-ghero::before,
.sms-ghome::before { background: radial-gradient(closest-side, rgba(64, 127, 54, 0.14), transparent); }
.sms-ghero { background: linear-gradient(180deg, var(--sms-pale), var(--sms-bg) 60%); }
.sms-ghome { background: linear-gradient(180deg, var(--sms-pale), var(--sms-bg) 70%); }
.sms-tiles .sms-tiles__glare { background: radial-gradient(closest-side, rgba(64, 127, 54, 0.12), transparent); }
.sms-tiles .sms-tiles__link { box-shadow: inset 0 0 0 1px var(--sms-line), 0 10px 30px rgba(6, 30, 53, 0.05); }
.sms-course .sms-course__panel { box-shadow: inset 0 0 0 1px var(--sms-line), var(--sms-shadow-lg); }
.sms-course .sms-course__dot { background: rgba(6, 30, 53, 0.15); }
.sms-course .sms-course__day { background: var(--sms-pale); }
.sms-spr .sms-spr__card { background: linear-gradient(180deg, #0b2a47, #061e35); }
.sms-gcta .sms-gcta__box { background: radial-gradient(55% 140% at 25% 120%, rgba(64, 127, 54, 0.45), transparent 70%), linear-gradient(180deg, #0b2a47, #061e35); }
"""


def chrome_top(ctx):
    return header(ctx, "blue")
