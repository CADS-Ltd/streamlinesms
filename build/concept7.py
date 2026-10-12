"""Concept 7 - Spotlight. Concept 4's layouts, motion and interactive pieces (the
inspection-light hero, the unassessed / assessed site diagram, the pinned-photo
scroll story and the Assess / Plan / Protect ring) in Streamline's original colour
scheme: white and pale-green sections, navy text and brand green, with navy photo
heroes, diagram screen, ring band, call-to-action panel and footer."""
from concept4 import *  # noqa: F401,F403
import concept4 as base
import light

NAME = "Spotlight"
DARK = False
CINE = True

CSS = base.CSS + light.css([
    ".sms-nhero", ".sms-torch", ".sms-scene .sms-scene__card", ".sms-ring", ".sms-ncta .sms-ncta__box", ".sms-footer",
]) + r"""
/* ===== Concept 7: light details ===== */
.sms-story .sms-story__frame { box-shadow: 0 0 0 1px var(--sms-line), var(--sms-shadow-lg); }
.sms-voice .sms-voice__claim { background: var(--sms-pale); }
.sms-facts { background: var(--sms-pale); }
.sms-torch,
.sms-nhero { background: var(--sms-bg); }
.sms-scene .sms-scene__card { background: linear-gradient(180deg, #0b2a47, #061e35); }
.sms-ncta .sms-ncta__box { background: radial-gradient(60% 120% at 20% 110%, rgba(64, 127, 54, 0.5), transparent 70%), linear-gradient(180deg, #0b2a47, #061e35); }
"""


def chrome_top(ctx):
    return header(ctx, "blue")
