"""Concept 9 - Heartbeat. Concept 6's layouts, motion and interactive pieces (the
heartbeat-line heroes, the which-service chooser, the event-types rail, the stacking
cards, the qualification timeline and the recruitment pathway) in Streamline's
original colour scheme: green top bar, white and pale-green sections, navy text and
brand green, with a navy event rail, navy cards, call-to-action panel and footer."""
from concept6 import *  # noqa: F401,F403
import concept6 as base
import light

NAME = "Heartbeat"
DARK = False
CINE = True

CSS = base.CSS + light.css([
    ".sms-rail", ".sms-stack .sms-stack__card", ".sms-pcta .sms-pcta__box", ".sms-pulse .sms-pulse__chip",
    ".sms-phero6 .sms-phero6__badge", ".sms-footer",
]) + r"""
/* ===== Concept 9: light details ===== */
.sms-page { background: radial-gradient(90rem 50rem at 85% -10%, rgba(64, 127, 54, 0.1), transparent 60%), var(--sms-bg); }
.sms-page .sms-mark { background: none; -webkit-background-clip: border-box; background-clip: border-box; color: var(--sms-accent); }
.sms-topbar { border-bottom: 0; background: #407f36; color: #ffffff; }
.sms-topbar .sms-topbar__text,
.sms-topbar .sms-topbar__link { color: #ffffff; font-weight: 600; }
.sms-topbar .sms-topbar__icon { color: #ffffff; }
.sms-page .sms-ecg__line { stroke: #407f36; }
.sms-page .sms-ecg__glow { stroke: rgba(64, 127, 54, 0.16); }
.sms-page .sms-ecg__scan { background: linear-gradient(90deg, transparent, rgba(64, 127, 54, 0.14), transparent); }
.sms-phero6 .sms-phero6__frame,
.sms-pulse .sms-pulse__main { box-shadow: 0 0 0 1px var(--sms-line-green), 0 30px 70px rgba(6, 30, 53, 0.16), 0 0 60px rgba(64, 127, 54, 0.16); }
.sms-pulse .sms-pulse__small { border-color: var(--sms-bg); box-shadow: 0 20px 50px rgba(6, 30, 53, 0.2); }
.sms-choose .sms-choose__opt { box-shadow: inset 0 0 0 1px var(--sms-line), 0 6px 18px rgba(6, 30, 53, 0.04); }
.sms-choose .sms-choose__panel { background: radial-gradient(80% 120% at 100% 0%, rgba(64, 127, 54, 0.1), transparent 60%), var(--sms-surface); box-shadow: inset 0 0 0 1px var(--sms-line-green), var(--sms-shadow-lg); }
.sms-valid .sms-valid__m,
.sms-valid .sms-valid__m--r,
.sms-valid .sms-valid__swatch { background: rgba(64, 127, 54, 0.22); }
.sms-valid .sms-valid__swatch--r { background: var(--sms-accent); }
.sms-path .sms-path__dot { background: var(--sms-bg); }
"""


def chrome_bottom(ctx):
    return footer(ctx, "white")


def chrome_top(ctx):
    return topbar(ctx, C.STRAP) + header(ctx, "blue")
