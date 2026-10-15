"""Concept 6 - Concierge. Warm, conversational and very readable. The site talks to
you: the homepage greets you with "How can we help?" and you answer in a sentence
("I'm looking for [Event Medical Cover] for [Sports and combat-sports events].")
built from two styled native selects. The page answers with the right service, its
list, one matching question and answer from that service's own FAQs, and the next
step. Big friendly Figtree type, lots of white, mint and pale-green fields, navy
for the footer and one island. Inner pages open with a greeting-card hero whose
chips become speech-bubble tags, and close with a chat-style prompt."""
import re

from common import *  # noqa: F401,F403
import content as C

NAME = "Concierge"
FONTS = "https://fonts.googleapis.com/css2?family=Figtree:wght@300;400;500;600;700;800&display=swap"

# ---------------------------------------------------------------------------
# Data for the sentence builder (all copy from content.py)
# ---------------------------------------------------------------------------
_EVENT = C.PAGES["event-medical-cover"]["sections"]
_TRAIN = C.PAGES["medical-training"]["sections"]
_CONS = C.PAGES["risk-needs-consultancy"]["sections"]
_CAREER = C.PAGES["pre-hospital-career-support"]["sections"]
EV_FEATURE = _EVENT[0][1]
EV_BOOK = _EVENT[2][1]
TR_FEATURE = _TRAIN[1][1]
CO_FEATURE = _CONS[0][1]
CA_FEATURE = _CAREER[0][1]
CA_CARDS = _CAREER[1][1]["items"]
CONTACT_LINKS = C.PAGES["contact"]["sections"][1][1]

S_EVENT, S_TRAIN, S_CONS = C.SERVICES

# Each service: what the answer card shows. "faqs" are exact questions from that
# service page's FAQ block; "omap" picks which one answers each option of the
# second list (index into faqs). The first FAQ is the one shown without JS.
SVCS = [
    {"key": "event", "title": S_EVENT["title"], "icon": S_EVENT["icon"], "text": S_EVENT["text"], "list": S_EVENT["list"],
     "photo": "fete", "page": S_EVENT["slug"], "book": "book:event", "cta": S_EVENT["cta"],
     "chips_title": EV_FEATURE["chips_title"], "chips": EV_FEATURE["chips"], "faqpage": "event-medical-cover",
     "faqs": ["How do you decide how many medical staff are required?", "Can you provide one medic?",
              "What is the minimum clinical grade you provide?", "Can you cover multi-day or overnight events?"],
     "omap": [1, 0, 2, 0, 3]},
    {"key": "training", "title": S_TRAIN["title"], "icon": S_TRAIN["icon"], "text": S_TRAIN["text"], "list": S_TRAIN["list"],
     "photo": "session", "page": S_TRAIN["slug"], "book": "book:training", "cta": S_TRAIN["cta"],
     "chips_title": TR_FEATURE["chips_title"], "chips": TR_FEATURE["chips"], "faqpage": "medical-training",
     "faqs": ["Can you deliver training at our workplace?", "Do you train care-home staff?", "Do you provide private group training?",
              "Do you train schools and nurseries?", "Can training reflect our workplace risks?"],
     "omap": [1, 2, 3, 0, 4]},
    {"key": "consultancy", "title": S_CONS["title"], "icon": S_CONS["icon"], "text": S_CONS["text"], "list": S_CONS["list"],
     "photo": "jacket", "page": S_CONS["slug"], "book": "book:consultancy", "cta": S_CONS["cta"],
     "chips_title": CO_FEATURE["chips_title"], "chips": CO_FEATURE["chips"], "faqpage": "risk-needs-consultancy",
     "faqs": ["Do you offer a free initial consultation?", "Can you help decide how many first aiders we need?",
              "What is a safe system of work?", "Can you help with event planning?"],
     "omap": [1, 1, 2, 2, 2, 1, 0, 0, 0, 3]},
    {"key": "careers", "title": C.CAREERS["title"], "icon": C.CAREERS["icon"], "text": C.CAREERS["text"],
     "list": [(it["icon"], it["title"]) for it in CA_CARDS],
     "photo": "cpr-outdoor", "page": C.CAREERS["slug"], "book": "book:careers", "cta": C.PAGES["pre-hospital-career-support"]["hero"]["buttons"][0][0],
     "chips_title": CA_FEATURE["chips_title"], "chips": CA_FEATURE["chips"], "faqpage": "pre-hospital-career-support",
     "faqs": ["Is the service suitable if I have no experience?", "Can you help me progress from FREC 3?",
              "Can you explain the difference between ambulance roles?", "Can you help with ambulance service interviews?",
              "Can you help a newly qualified paramedic find work?", "Can you help me choose a qualification?",
              "Can you help if I keep being rejected?"],
     "omap": [0, 1, 2, 3, 4, 5, 6]},
]
for _s in SVCS:
    assert len(_s["omap"]) == len(_s["chips"]), _s["key"]

SHIELD = "streamline-shield-blue.png"


def _faq_lookup(page, q):
    return dict(C.faqs(page))[q]


def _faq_html(ctx, a):
    return a.replace(SITE + "/contact-us", ctx.href("contact"))


def _strip(h):
    return re.sub(r"<[^>]+>", "", h).strip()


# ---------------------------------------------------------------------------
# CSS
# ---------------------------------------------------------------------------
EYEBROWS = ["feature", "cards", "steps", "checklist", "faq", "quotes", "people", "contact", "links", "marquee", "booking"]
TITLES = EYEBROWS


def _helpdesk_css(n):
    out = ""
    for i in range(n):
        r = ".sms-helpdesk .sms-helpdesk__r%d" % i
        out += "%s:checked ~ .sms-helpdesk__choices .sms-helpdesk__choice--%d { border-color: var(--sms-green); background: var(--sms-pale); box-shadow: 0 10px 24px rgba(64, 127, 54, 0.14); }\n" % (r, i)
        out += "%s:checked ~ .sms-helpdesk__choices .sms-helpdesk__choice--%d .sms-helpdesk__choice-icon { background: var(--sms-green); color: #ffffff; }\n" % (r, i)
        out += "%s:checked ~ .sms-helpdesk__choices .sms-helpdesk__choice--%d .sms-helpdesk__choice-tick { opacity: 1; transform: scale(1); }\n" % (r, i)
        out += "%s:focus-visible ~ .sms-helpdesk__choices .sms-helpdesk__choice--%d { outline: 3px solid var(--sms-green); outline-offset: 3px; }\n" % (r, i)
        out += "%s:checked ~ .sms-helpdesk__panels .sms-helpdesk__panel--%d { display: grid; }\n" % (r, i)
    return out


CSS = r"""
/* ===== Concept 6 theme: Concierge ===== */
.sms-page { --sms-font: "Figtree", "Montserrat", Arial, sans-serif; --sms-radius: 1.75rem; --sms-radius-sm: 1rem; --sms-max: 76rem;
  --sms-step-2: clamp(1.85rem, 1.3rem + 2.1vw, 3.05rem); --sms-step-3: clamp(2.4rem, 1.45rem + 3.8vw, 4.7rem);
  --sms-shadow: 0 1px 2px rgba(6, 30, 53, 0.04), 0 14px 34px rgba(6, 30, 53, 0.07);
  --sms-shadow-lg: 0 2px 6px rgba(6, 30, 53, 0.04), 0 30px 64px rgba(6, 30, 53, 0.12);
  font-size: clamp(1.0625rem, 1rem + 0.25vw, 1.1875rem); line-height: 1.65; }
.sms-page .sms-mark { color: var(--sms-green); }
.sms-page .sms-btn { padding: 0.95rem 1.45rem; font-size: 0.95rem; letter-spacing: 0.005em; }
.sms-page .sms-btn--primary { box-shadow: 0 10px 24px rgba(64, 127, 54, 0.26); }
.sms-page .sms-more__toggle { font-size: 0.95rem; }

/* ---------- Header ---------- */
.sms-header { border-bottom: 0; background: rgba(255, 255, 255, 0.92); box-shadow: 0 1px 0 rgba(6, 30, 53, 0.06); }
.sms-header .sms-header__link { padding: 0.55rem 0.95rem; font-size: 0.95rem; font-weight: 600; transition: background-color 0.25s, color 0.25s; }
.sms-header .sms-header__link::after { display: none; }
.sms-header .sms-header__link:hover { background: var(--sms-pale-2); }
.sms-header .sms-header__link[aria-current="page"] { background: var(--sms-mint); }
.sms-header .sms-header__summary { background: var(--sms-mint); }
.sms-header .sms-header__panel { border-radius: 1.5rem; }

/* ---------- Footer (navy, rounded top) ---------- */
.sms-footer { border-radius: clamp(1.75rem, 1rem + 3vw, 3rem) clamp(1.75rem, 1rem + 3vw, 3rem) 0 0; background: var(--sms-navy); color: rgba(255, 255, 255, 0.84); }
.sms-footer .sms-footer__heading { color: #ffffff; font-size: 0.95rem; letter-spacing: 0; text-transform: none; }
.sms-footer .sms-footer__tag { color: #ffffff; font-size: 1.05rem; }
.sms-footer .sms-footer__link { color: rgba(255, 255, 255, 0.84); }
.sms-footer .sms-footer__link:hover { color: var(--sms-green-on-navy); }
.sms-footer .sms-footer__base { border-color: rgba(255, 255, 255, 0.16); color: rgba(255, 255, 255, 0.7); }

/* ---------- Shared section heads ---------- */
""" + ",\n".join(".sms-%s .sms-%s__eyebrow" % (b, b) for b in EYEBROWS) + r""" {
  gap: 0.5rem; padding: 0.35rem 0.9rem 0.35rem 0.7rem; border-radius: 999px; background: var(--sms-mint); color: var(--sms-navy);
  font-size: 0.875rem; font-weight: 600; letter-spacing: 0; text-transform: none; }
""" + ",\n".join(".sms-%s .sms-%s__eyebrow::before" % (b, b) for b in EYEBROWS) + r""" { width: 0.5rem; height: 0.5rem; border-radius: 50%; }
""" + ",\n".join(".sms-%s .sms-%s__title" % (b, b) for b in TITLES) + r""" { font-weight: 700; line-height: 1.1; letter-spacing: -0.03em; text-wrap: balance; }
.sms-cards .sms-cards__lead,
.sms-steps .sms-steps__lead,
.sms-checklist .sms-checklist__lead,
.sms-people .sms-people__lead,
.sms-links .sms-links__lead,
.sms-faq .sms-faq__lead { font-size: var(--sms-step-1); }

/* Chips: soft pills */
.sms-page .sms-chips__item { padding: 0.5rem 1rem 0.5rem 0.5rem; border: 1px solid var(--sms-line); background: #ffffff; box-shadow: none; font-size: 0.95rem; }
.sms-feature.sms-tone-white .sms-chips__item { border-color: transparent; background: var(--sms-pale); }

/* Feature: photo on a tilted mint card */
.sms-feature .sms-feature__frame { border-radius: 2rem; box-shadow: none; }
.sms-feature .sms-feature__blob { inset: 1rem -0.75rem -1rem 1.25rem; right: -0.75rem; bottom: -1rem; width: auto; aspect-ratio: auto; border-radius: 2rem; background: var(--sms-mint); transform: rotate(2.5deg); animation: none; }
.sms-feature.sms-tone-pale .sms-feature__blob { background: #ffffff; }
.sms-feature .sms-feature__lead { font-weight: 500; }
.sms-feature .sms-feature__chips-title { font-size: 1.05rem; }
.sms-feature .sms-feature__strap { border-radius: 1.25rem 1.25rem 1.25rem 0.35rem; }
@media (min-width: 56em) {
  .sms-feature.sms-feature--flip .sms-feature__blob { left: -0.75rem; right: 1.25rem; transform: rotate(-2.5deg); }
}

/* Cards */
.sms-cards .sms-cards__item { border: 1px solid var(--sms-line); border-radius: 1.75rem; box-shadow: none; transition: transform 0.35s var(--sms-ease), border-color 0.3s; }
.sms-cards .sms-cards__item:hover { transform: translateY(-4px); border-color: var(--sms-line-green); }
.sms-cards.sms-tone-white .sms-cards__item { border-color: transparent; background: var(--sms-pale); }
.sms-cards .sms-cards__icon { border-radius: 50%; }
.sms-cards .sms-cards__name { letter-spacing: -0.01em; }
.sms-cards .sms-cards__num { font-weight: 800; }
.sms-cards .sms-cards__list-title { letter-spacing: 0; text-transform: none; font-size: 0.95rem; }

/* Steps: each step is a speech bubble */
.sms-steps .sms-steps__body { padding: 1rem 1.2rem 1.1rem; border-radius: 1.4rem 1.4rem 1.4rem 0.35rem; background: var(--sms-pale); }
.sms-steps.sms-tone-pale .sms-steps__body { background: #ffffff; }
.sms-steps .sms-steps__note { border-radius: 1.25rem; }
@media (min-width: 60em) {
  .sms-steps .sms-steps__body { padding-top: 0.9rem; }
}

/* Checklist */
.sms-checklist .sms-checklist__item { border-radius: 1.5rem; }

/* Notice */
.sms-notice .sms-notice__box { border: 1px solid var(--sms-line); border-radius: 2rem; box-shadow: none; }

/* FAQ: question pills, answers as reply bubbles */
.sms-faq .sms-faq__item { border: 1px solid var(--sms-line); border-radius: 1.5rem; background: #ffffff; box-shadow: none; transition: border-color 0.3s; }
.sms-faq.sms-tone-white .sms-faq__item { border-color: transparent; background: var(--sms-pale); }
.sms-faq .sms-faq__item[open] { border-color: var(--sms-line-green); }
.sms-faq .sms-faq__q { padding: 1.15rem 3.9rem 1.15rem 1.4rem; font-weight: 600; }
.sms-faq .sms-faq__q:hover { color: var(--sms-green); }
.sms-faq .sms-faq__a { margin: 0 0.6rem 0.6rem; padding: 1rem 1.2rem; border-radius: 1.25rem 1.25rem 1.25rem 0.35rem; background: var(--sms-pale); }
.sms-faq.sms-tone-white .sms-faq__a { background: #ffffff; }
.sms-faq .sms-faq__a > :last-child { margin-bottom: 0; }
.sms-faq .sms-faq__a a { color: var(--sms-green); }
.sms-faq .sms-faq__all-toggle { border-color: var(--sms-navy); }

/* Quotes: big speech bubbles */
.sms-quotes .sms-quotes__item { border-radius: 2rem 2rem 2rem 0.5rem; }
.sms-quotes .sms-quotes__icon { border-radius: 50%; }
.sms-quotes .sms-quotes__label { letter-spacing: 0.04em; }
.sms-quotes .sms-quotes__text { font-weight: 500; }

/* People */
.sms-people .sms-people__frame { border-radius: 2rem; box-shadow: none; }
.sms-people .sms-people__person { border: 1px solid var(--sms-line); box-shadow: none; }
.sms-people.sms-tone-white .sms-people__person { border-color: transparent; }
.sms-people .sms-people__shared { border-radius: 2rem; }

/* Links */
.sms-links .sms-links__link { border: 1px solid var(--sms-line); box-shadow: none; }
.sms-links .sms-links__icon { border-radius: 50%; }

/* Claim */
.sms-claim .sms-claim__text { letter-spacing: -0.02em; }

/* Contact */
.sms-contact .sms-contact__detail { border-radius: 1.5rem; }
.sms-contact .sms-contact__label { letter-spacing: 0.02em; text-transform: none; font-size: 0.875rem; }
.sms-contact .sms-contact__form { border: 1px solid var(--sms-line); border-radius: 2rem; box-shadow: var(--sms-shadow); }
.sms-contact .sms-contact__booklink { border-radius: 1.25rem; }

/* Booking wizard */
.sms-booking .sms-booking__form { border: 1px solid var(--sms-line); border-radius: 2rem; box-shadow: var(--sms-shadow); }
.sms-booking .sms-booking__service-card { border-radius: 1.5rem; }
.sms-booking .sms-booking__service-icon { border-radius: 50%; }
.sms-booking .sms-booking__summary,
.sms-booking .sms-booking__help { border-radius: 1.75rem; }

/* ---------- Page hero: a greeting card ---------- */
.sms-greeting { position: relative; padding: clamp(1rem, 0.5rem + 2vw, 2.25rem) 0 clamp(1.5rem, 1rem + 2vw, 3rem); background: linear-gradient(180deg, var(--sms-pale-2) 0, var(--sms-pale-2) 74%, #ffffff 74%); }
.sms-greeting .sms-greeting__inner { width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-greeting .sms-greeting__card { position: relative; display: grid; gap: clamp(1.75rem, 1rem + 3vw, 3.5rem); align-items: center; padding: clamp(1.25rem, 0.5rem + 3.2vw, 3.75rem); border-radius: clamp(1.75rem, 1.2rem + 2vw, 3rem); background: #ffffff; box-shadow: var(--sms-shadow-lg); }
.sms-greeting .sms-greeting__copy { min-width: 0; }
.sms-greeting .sms-greeting__crumb { margin-bottom: 1.25rem; color: var(--sms-ink-soft); font-size: 0.9rem; }
.sms-greeting .sms-greeting__crumb-link { color: var(--sms-navy); font-weight: 600; text-underline-offset: 3px; }
.sms-greeting .sms-greeting__eyebrow { display: inline-flex; align-items: center; gap: 0.5rem; padding: 0.35rem 0.9rem 0.35rem 0.7rem; border-radius: 999px; background: var(--sms-mint); color: var(--sms-navy); font-size: 0.9rem; font-weight: 600; }
.sms-greeting .sms-greeting__eyebrow::before { content: ""; flex: 0 0 auto; width: 0.5rem; height: 0.5rem; border-radius: 50%; background: var(--sms-green); }
.sms-greeting .sms-greeting__title { margin: 1rem 0 1.25rem; font-size: var(--sms-step-3); font-weight: 700; line-height: 1.04; letter-spacing: -0.035em; text-wrap: balance; }
.sms-greeting .sms-greeting__sub { margin-bottom: 0.6rem; font-size: var(--sms-step-1); font-weight: 600; line-height: 1.45; }
.sms-greeting .sms-greeting__lead { max-width: 34rem; color: var(--sms-ink-soft); font-size: var(--sms-step-1); line-height: 1.55; }
.sms-greeting .sms-greeting__lead p { margin: 0 0 0.75rem; }
.sms-greeting .sms-greeting__actions { display: flex; flex-wrap: wrap; gap: 0.75rem; margin-top: 1.75rem; }
.sms-greeting .sms-greeting__media { position: relative; min-width: 0; padding-bottom: 1.75rem; }
.sms-greeting .sms-greeting__frame { aspect-ratio: 4 / 3.4; border-radius: clamp(1.25rem, 1rem + 1vw, 2rem); }
.sms-greeting .sms-greeting__tags { margin: 0; padding: 0; list-style: none; }
.sms-greeting .sms-greeting__tag { position: absolute; z-index: 2; display: inline-flex; align-items: center; gap: 0.55rem; min-width: 0; max-width: calc(100% - 1.5rem); padding: 0.55rem 1.05rem 0.55rem 0.55rem; border-radius: 1.4rem; background: #ffffff; box-shadow: var(--sms-shadow-lg); color: var(--sms-navy); font-size: 0.95rem; font-weight: 700; line-height: 1.3; animation: sms-bob 6s ease-in-out infinite; }
.sms-greeting .sms-greeting__tag::after { content: ""; position: absolute; width: 0.9rem; height: 0.9rem; border-radius: 0.15rem; background: #ffffff; transform: rotate(45deg); }
.sms-greeting .sms-greeting__tag--1 { left: 0.75rem; top: 0.75rem; border-bottom-left-radius: 0.35rem; }
.sms-greeting .sms-greeting__tag--1::after { left: 1.4rem; bottom: -0.3rem; }
.sms-greeting .sms-greeting__tag--2 { right: 0.75rem; bottom: 0; border-bottom-right-radius: 0.35rem; animation-delay: -3s; }
.sms-greeting .sms-greeting__tag--2::after { right: 1.4rem; bottom: -0.3rem; }
.sms-greeting .sms-greeting__tag-icon { width: 2rem; height: 2rem; padding: 0.42rem; border-radius: 50%; background: var(--sms-mint); color: var(--sms-green); }
.sms-greeting .sms-greeting__tag-text { position: relative; z-index: 1; min-width: 0; overflow-wrap: anywhere; }
.sms-greeting .sms-greeting__tag-link { color: var(--sms-navy); text-decoration: none; }
.sms-greeting .sms-greeting__tag-link:hover { text-decoration: underline; }
@media (min-width: 56em) {
  .sms-greeting .sms-greeting__card { grid-template-columns: minmax(0, 1.1fr) minmax(0, 0.9fr); }
  .sms-greeting .sms-greeting__frame { aspect-ratio: 4 / 4.2; }
  .sms-greeting .sms-greeting__tag--1 { left: -1.5rem; top: 1.75rem; }
  .sms-greeting .sms-greeting__tag--2 { right: -1rem; bottom: 3rem; }
}

/* ---------- CTA: a chat-like prompt ---------- */
.sms-chatcta { padding: var(--sms-section) 0; }
.sms-chatcta .sms-chatcta__inner { width: 100%; max-width: 60rem; margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-chatcta .sms-chatcta__window { padding: clamp(1.1rem, 0.6rem + 2.2vw, 2.5rem); border-radius: clamp(1.75rem, 1.2rem + 2vw, 2.5rem); background: var(--sms-pale-2); }
.sms-chatcta .sms-chatcta__bar { display: flex; align-items: center; gap: 0.75rem; margin-bottom: 1.5rem; padding-bottom: 1rem; border-bottom: 1px solid var(--sms-line-green); font-size: 0.95rem; font-weight: 700; }
.sms-chatcta .sms-chatcta__bar-name { min-width: 0; }
.sms-chatcta .sms-chatcta__avatar { flex: 0 0 auto; min-width: 0; width: 2.5rem; height: 2.5rem; padding: 0.45rem; border-radius: 50%; background: #ffffff; box-shadow: var(--sms-shadow); object-fit: contain; }
.sms-chatcta .sms-chatcta__thread { display: grid; gap: 0.9rem; }
.sms-chatcta .sms-chatcta__row { display: flex; align-items: flex-end; gap: 0.6rem; min-width: 0; }
.sms-chatcta .sms-chatcta__row--you { justify-content: flex-end; }
.sms-chatcta .sms-chatcta__bubble { min-width: 0; max-width: 42rem; margin: 0; padding: 1rem 1.35rem 1.1rem; border-radius: 1.5rem 1.5rem 1.5rem 0.4rem; background: #ffffff; box-shadow: var(--sms-shadow); }
.sms-chatcta .sms-chatcta__bubble--you { border-radius: 1.5rem 1.5rem 0.4rem 1.5rem; background: var(--sms-navy); color: #ffffff; }
.sms-chatcta .sms-chatcta__title { margin: 0; font-size: clamp(1.5rem, 1.1rem + 1.6vw, 2.4rem); font-weight: 700; line-height: 1.15; letter-spacing: -0.025em; text-wrap: balance; }
.sms-chatcta .sms-chatcta__text { color: var(--sms-ink-soft); font-size: var(--sms-step-1); line-height: 1.55; }
.sms-chatcta .sms-chatcta__text p { margin: 0; }
.sms-chatcta .sms-chatcta__gap { flex: 0 0 auto; min-width: 0; width: 2.5rem; }
.sms-chatcta .sms-chatcta__bubble--first { border-bottom-left-radius: 1.5rem; }
.sms-chatcta .sms-chatcta__thread .sms-chatcta__row:not(.sms-chatcta__row--you) + .sms-chatcta__row { margin-top: -0.35rem; }
.sms-chatcta .sms-chatcta__replies { display: flex; flex-wrap: wrap; justify-content: flex-end; gap: 0.6rem; min-width: 0; margin-top: 0.75rem; }
.sms-chatcta .sms-chatcta__replies .sms-btn--outline { background: #ffffff; border-color: var(--sms-line-green); }
.sms-chatcta .sms-chatcta__replies .sms-btn--outline:hover { border-color: var(--sms-navy); background: var(--sms-navy); color: #ffffff; }
@supports (animation-timeline: view()) {
  .sms-chatcta .sms-chatcta__thread .sms-chatcta__row:nth-child(2) { animation-range: entry 15% entry 100%; }
  .sms-chatcta .sms-chatcta__thread .sms-chatcta__replies { animation-range: entry 25% entry 100%; }
}

/* ---------- Home hero: the concierge ---------- */
.sms-concierge { position: relative; overflow: hidden; padding: clamp(2.25rem, 1.25rem + 4vw, 5rem) 0 clamp(3rem, 2rem + 4vw, 6rem); background: radial-gradient(46rem 30rem at 92% -8%, #ffffff 0, rgba(255, 255, 255, 0) 70%), radial-gradient(30rem 22rem at -6% 104%, var(--sms-mint) 0, rgba(220, 239, 214, 0) 70%), var(--sms-pale-2); }
.sms-concierge .sms-concierge__inner { position: relative; width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-concierge .sms-concierge__greet { display: flex; align-items: flex-end; gap: 0.75rem; margin-bottom: clamp(1.25rem, 0.9rem + 1.4vw, 2.25rem); }
.sms-concierge .sms-concierge__avatar { flex: 0 0 auto; min-width: 0; width: 3.1rem; height: 3.1rem; padding: 0.55rem; border-radius: 50%; background: #ffffff; box-shadow: var(--sms-shadow); object-fit: contain; }
.sms-concierge .sms-concierge__title { position: relative; min-width: 0; margin: 0; padding: 0.6rem 1.3rem 0.7rem; border-radius: 1.6rem 1.6rem 1.6rem 0.35rem; background: var(--sms-navy); color: #ffffff; font-size: clamp(1.3rem, 1rem + 1.1vw, 1.85rem); font-weight: 700; line-height: 1.25; letter-spacing: -0.015em; }
.sms-concierge .sms-concierge__title .sms-mark { color: var(--sms-green-on-navy); }

/* ---------- Sentence builder ---------- */
.sms-ask { position: relative; }
.sms-ask .sms-ask__sentence { margin: 0; color: var(--sms-navy); font-size: clamp(2rem, 1.1rem + 3.6vw, 4.2rem); font-weight: 500; line-height: 1.18; letter-spacing: -0.035em; text-wrap: pretty; }
.sms-ask .sms-ask__fixed { font-weight: 700; }
.sms-ask .sms-ask__pick { position: relative; }
.sms-ask .sms-ask__select { max-width: 100%; margin: 0; padding: 0 1.1em 0 0.1em; border: 0; border-bottom: 0.07em solid var(--sms-green); border-radius: 0; background: transparent url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23407f36' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M6 9l6 6 6-6'/%3E%3C/svg%3E") no-repeat right 0.1em center / 0.6em; color: var(--sms-green); font: inherit; font-weight: 700; letter-spacing: inherit; cursor: pointer; -webkit-appearance: none; appearance: none; text-overflow: ellipsis; }
.sms-ask .sms-ask__face { display: none; }
.sms-ask.is-js .sms-ask__pick { display: inline-block; max-width: 100%; }
.sms-ask.is-js .sms-ask__select { position: absolute; inset: 0; z-index: 1; width: 100%; height: 100%; padding: 0; border: 0; background: none; opacity: 0; font-size: 1rem; }
.sms-ask.is-js .sms-ask__face { display: inline; padding: 0 0.06em; border-radius: 0.18em; background-image: linear-gradient(#ffffff, #ffffff); background-repeat: no-repeat; background-position: 0 100%; background-size: 100% 0; color: var(--sms-green); font-weight: 700; text-decoration: underline; text-decoration-color: rgba(64, 127, 54, 0.5); text-decoration-thickness: 0.07em; text-underline-offset: 0.14em; -webkit-box-decoration-break: clone; box-decoration-break: clone; transition: background-size 0.35s var(--sms-ease), text-decoration-color 0.3s; }
.sms-ask .sms-ask__pick:hover .sms-ask__face,
.sms-ask .sms-ask__pick:focus-within .sms-ask__face { background-size: 100% 100%; text-decoration-color: var(--sms-green); }
.sms-ask .sms-ask__pick:focus-within .sms-ask__face { outline: 3px solid var(--sms-green); outline-offset: 4px; }
.sms-ask .sms-ask__chev { display: inline-block; width: 0.5em; height: 0.5em; margin-left: 0.08em; vertical-align: 0.1em; stroke-width: 3; transition: transform 0.3s var(--sms-ease); }
.sms-ask .sms-ask__pick:hover .sms-ask__chev { transform: translateY(0.08em); }
.sms-ask .sms-ask__stop { display: inline-block; color: var(--sms-navy); font-weight: 500; }
.sms-ask .sms-ask__stop[hidden],
.sms-ask:not(.is-js) .sms-ask__stop,
.sms-ask:not(.is-js) .sms-ask__hint { display: none; }
.sms-ask .sms-ask__below { display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 0.75rem 1.5rem; margin-top: clamp(1rem, 0.8rem + 0.8vw, 1.5rem); }
.sms-ask .sms-ask__hint { display: inline-flex; align-items: center; gap: 0.5rem; min-width: 0; margin: 0; color: var(--sms-ink-soft); font-size: 0.95rem; font-weight: 500; }
.sms-ask .sms-ask__hint-icon { width: 1.25rem; height: 1.25rem; color: var(--sms-green); }
.sms-ask .sms-ask__jump { display: flex; flex-wrap: wrap; align-items: center; gap: 0.4rem; min-width: 0; margin: 0; padding: 0; list-style: none; font-size: 0.9rem; }
.sms-ask .sms-ask__jump-label { min-width: 0; margin-right: 0.25rem; color: var(--sms-ink-soft); }
.sms-ask .sms-ask__jump-item { min-width: 0; }
.sms-ask .sms-ask__jump-link { display: inline-block; padding: 0.35rem 0.85rem; border-radius: 999px; background: #ffffff; color: var(--sms-navy); font-weight: 600; text-decoration: none; transition: background-color 0.25s, color 0.25s; }
.sms-ask .sms-ask__jump-link:hover { background: var(--sms-navy); color: #ffffff; }

/* Answer stage + cards */
.sms-ask .sms-ask__stage { position: relative; margin-top: clamp(1.75rem, 1rem + 2.5vw, 3rem); transition: height 0.5s var(--sms-ease); }
.sms-ask .sms-ask__stage.is-sizing { overflow: hidden; }
.sms-ask .sms-ask__card { display: grid; gap: clamp(1.5rem, 1rem + 2vw, 3rem); padding: clamp(1.1rem, 0.5rem + 2.4vw, 2.75rem); border-radius: clamp(1.5rem, 1rem + 1.6vw, 2.25rem); background: #ffffff; box-shadow: var(--sms-shadow-lg); }
.sms-ask .sms-ask__card[hidden] { display: none; }
.sms-ask:not(.is-js) .sms-ask__card + .sms-ask__card { margin-top: 1.25rem; }
.sms-ask .sms-ask__card.is-out { position: absolute; top: 0; left: 0; right: 0; pointer-events: none; animation: sms-c6-out 0.36s var(--sms-ease) both; }
.sms-ask .sms-ask__card.is-in { animation: sms-c6-in 0.6s var(--sms-ease) both; }
.sms-ask .sms-ask__main { min-width: 0; }
.sms-ask .sms-ask__picked { display: inline-flex; flex-wrap: wrap; align-items: center; gap: 0.35rem 0.6rem; max-width: 100%; margin-bottom: 1.25rem; padding: 0.35rem 0.4rem 0.35rem 0.95rem; border-radius: 1.25rem; background: var(--sms-pale); font-size: 0.9rem; line-height: 1.35; }
.sms-ask .sms-ask__picked[hidden] { display: none; }
.sms-ask .sms-ask__picked-label { min-width: 0; color: var(--sms-ink-soft); font-weight: 500; }
.sms-ask .sms-ask__picked-val { display: inline-flex; align-items: center; gap: 0.35rem; min-width: 0; padding: 0.25rem 0.8rem 0.25rem 0.35rem; border-radius: 999px; background: var(--sms-green); color: #ffffff; font-weight: 700; }
.sms-ask .sms-ask__picked-icon { width: 1.15rem; height: 1.15rem; }
.sms-ask .sms-ask__picked-text { min-width: 0; }
.sms-ask .sms-ask__top { display: flex; align-items: center; gap: 0.9rem; margin-bottom: 0.9rem; }
.sms-ask .sms-ask__icon { width: 3.25rem; height: 3.25rem; padding: 0.75rem; border-radius: 50%; background: var(--sms-mint); color: var(--sms-green); }
.sms-ask .sms-ask__name { min-width: 0; margin: 0; font-size: clamp(1.6rem, 1.2rem + 1.5vw, 2.5rem); font-weight: 700; line-height: 1.1; letter-spacing: -0.03em; }
.sms-ask .sms-ask__text { max-width: 38rem; color: var(--sms-ink-soft); font-size: var(--sms-step-1); line-height: 1.55; }
.sms-ask .sms-ask__text p { margin: 0 0 0.75rem; }
.sms-ask .sms-ask__text > p:last-child { margin-bottom: 0; }
.sms-ask .sms-ask__list { display: grid; gap: 0.55rem; margin: 1.5rem 0 0; padding: 0; list-style: none; }
.sms-ask .sms-ask__item { display: flex; align-items: center; gap: 0.75rem; min-width: 0; padding: 0.6rem 0.9rem 0.6rem 0.6rem; border-radius: 1.1rem; background: var(--sms-pale); font-size: 0.98rem; font-weight: 600; line-height: 1.35; }
.sms-ask .sms-ask__item-icon { width: 2.2rem; height: 2.2rem; padding: 0.5rem; border-radius: 50%; background: #ffffff; color: var(--sms-green); }
.sms-ask .sms-ask__item-text { min-width: 0; }
.sms-ask .sms-ask__actions { display: flex; flex-wrap: wrap; gap: 0.75rem; margin-top: 1.75rem; }
.sms-ask .sms-ask__side { position: relative; min-width: 0; }
.sms-ask .sms-ask__frame { aspect-ratio: 4 / 3; border-radius: 1.5rem; }
.sms-ask .sms-ask__source { position: absolute; z-index: 1; left: 0.75rem; top: 0.75rem; display: inline-flex; align-items: center; gap: 0.4rem; padding: 0.3rem 0.8rem 0.3rem 0.4rem; border-radius: 999px; background: #ffffff; color: var(--sms-navy); font-size: 0.85rem; font-weight: 700; box-shadow: var(--sms-shadow); }
.sms-ask .sms-ask__source-text { min-width: 0; }
.sms-ask .sms-ask__source-icon { width: 1.4rem; height: 1.4rem; padding: 0.25rem; border-radius: 50%; background: var(--sms-mint); color: var(--sms-green); }
.sms-ask .sms-ask__chat { position: relative; z-index: 1; min-width: 0; margin: -2.75rem 0.5rem 0; }
.sms-ask .sms-ask__faq { display: grid; gap: 0.6rem; }
.sms-ask .sms-ask__faq[hidden] { display: none; }
.sms-ask .sms-ask__faq.is-in { animation: sms-c6-in 0.5s var(--sms-ease) both; }
.sms-ask .sms-ask__q { justify-self: end; min-width: 0; max-width: 92%; margin: 0; padding: 0.8rem 1.1rem; border-radius: 1.3rem 1.3rem 0.35rem 1.3rem; background: var(--sms-navy); color: #ffffff; font-weight: 600; line-height: 1.4; box-shadow: var(--sms-shadow); }
.sms-ask .sms-ask__a { display: flex; align-items: flex-end; gap: 0.55rem; min-width: 0; }
.sms-ask .sms-ask__avatar { flex: 0 0 auto; min-width: 0; width: 2.3rem; height: 2.3rem; padding: 0.4rem; border-radius: 50%; background: #ffffff; box-shadow: var(--sms-shadow); object-fit: contain; }
.sms-ask .sms-ask__a-body { min-width: 0; padding: 0.9rem 1.1rem; border: 1px solid var(--sms-line); border-radius: 1.3rem 1.3rem 1.3rem 0.35rem; background: #ffffff; color: var(--sms-ink-soft); font-size: 0.98rem; line-height: 1.55; box-shadow: var(--sms-shadow); }
.sms-ask .sms-ask__a-body p { margin: 0 0 0.5rem; }
.sms-ask .sms-ask__a-body > :last-child { margin-bottom: 0; }
.sms-ask .sms-ask__a-body ul { margin: 0 0 0.5rem; padding-left: 1.1rem; }
.sms-ask .sms-ask__a-body a { color: var(--sms-green); font-weight: 700; }
.sms-ask .sms-ask__live { position: absolute; width: 1px; height: 1px; overflow: hidden; clip-path: inset(50%); white-space: nowrap; }
@media (min-width: 40em) {
  .sms-ask .sms-ask__list { grid-template-columns: repeat(2, minmax(0, 1fr)); }
}
@media (min-width: 40em) and (max-width: 59.99em) {
  .sms-ask .sms-ask__side { display: grid; grid-template-columns: minmax(0, 0.8fr) minmax(0, 1.2fr); gap: 1rem; align-items: center; }
  .sms-ask .sms-ask__frame { aspect-ratio: 4 / 4.6; }
  .sms-ask .sms-ask__chat { margin: 0; }
}
@media (min-width: 60em) {
  .sms-ask .sms-ask__card { grid-template-columns: minmax(0, 1.2fr) minmax(0, 1fr); align-items: start; }
  .sms-ask .sms-ask__chat { margin: -3.25rem 1rem 0 -1.5rem; }
}

/* Have these ready (event page) */
.sms-ask .sms-ask__ready-title { margin: 1.75rem 0 0.2rem; font-size: var(--sms-step-1); font-weight: 700; line-height: 1.3; }
.sms-ask .sms-ask__ready-sub { margin: 0 0 0.85rem; color: var(--sms-ink-soft); font-size: 0.95rem; }
.sms-ask .sms-ask__ready { display: grid; gap: 0.5rem; margin: 0; padding: 0; list-style: none; }
.sms-ask .sms-ask__ready-item { min-width: 0; }
.sms-ask .sms-ask__tick-label { display: flex; align-items: center; gap: 0.8rem; min-width: 0; padding: 0.7rem 0.95rem; border-radius: 1.1rem; background: var(--sms-pale); cursor: pointer; font-size: 0.98rem; font-weight: 600; line-height: 1.35; transition: background-color 0.25s; }
.sms-ask .sms-ask__tick-label:hover { background: var(--sms-pale-2); }
.sms-ask .sms-ask__tick-label:has(.sms-ask__tick:checked) { background: var(--sms-mint); }
.sms-ask .sms-ask__tick { display: grid; flex: 0 0 auto; place-items: center; min-width: 0; width: 1.6rem; height: 1.6rem; margin: 0; border: 2px solid #6b7c8b; border-radius: 50%; background: #ffffff; cursor: pointer; -webkit-appearance: none; appearance: none; transition: background-color 0.25s, border-color 0.25s; }
.sms-ask .sms-ask__tick::after { content: ""; width: 0.42rem; height: 0.78rem; margin-top: -0.15rem; border: solid #ffffff; border-width: 0 0.18rem 0.18rem 0; transform: rotate(45deg) scale(0); transition: transform 0.25s var(--sms-ease); }
.sms-ask .sms-ask__tick:checked { border-color: var(--sms-green); background: var(--sms-green); }
.sms-ask .sms-ask__tick:checked::after { transform: rotate(45deg) scale(1); }
.sms-ask .sms-ask__tick-text { min-width: 0; }
.sms-ask .sms-ask__count { margin: 0.75rem 0 0; color: var(--sms-navy); font-size: 0.95rem; font-weight: 700; }
.sms-ask .sms-ask__count[hidden] { display: none; }
.sms-ask .sms-ask__body { margin-top: 1.5rem; color: var(--sms-ink-soft); }
.sms-ask .sms-ask__body p { margin: 0 0 0.75rem; }
@media (min-width: 40em) {
  .sms-ask .sms-ask__ready { grid-template-columns: repeat(2, minmax(0, 1fr)); }
}

/* Event page wrapper */
.sms-askpage { padding: var(--sms-section) 0; background: var(--sms-pale-2); }
.sms-askpage .sms-askpage__inner { width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-askpage .sms-askpage__head { margin-bottom: clamp(1.25rem, 1rem + 1vw, 2rem); }
.sms-askpage .sms-askpage__eyebrow { display: inline-flex; align-items: center; gap: 0.5rem; margin-bottom: 0.9rem; padding: 0.35rem 0.9rem 0.35rem 0.7rem; border-radius: 999px; background: #ffffff; color: var(--sms-navy); font-size: 0.875rem; font-weight: 600; }
.sms-askpage .sms-askpage__eyebrow::before { content: ""; flex: 0 0 auto; width: 0.5rem; height: 0.5rem; border-radius: 50%; background: var(--sms-green); }
.sms-askpage .sms-askpage__title { margin: 0; font-size: var(--sms-step-2); font-weight: 700; line-height: 1.1; letter-spacing: -0.03em; }
.sms-askpage .sms-ask__sentence { font-size: clamp(1.8rem, 1rem + 3.2vw, 3.8rem); }

/* ---------- Who we work with ---------- */
.sms-whoroll { padding: clamp(3rem, 2rem + 4vw, 6rem) 0 0; }
.sms-whoroll .sms-whoroll__inner { width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-whoroll .sms-whoroll__band { position: relative; padding: clamp(2rem, 1.1rem + 3.5vw, 4.5rem) clamp(1.25rem, 0.8rem + 3vw, 4rem); border-radius: clamp(1.75rem, 1.2rem + 2vw, 3rem); background: var(--sms-mint); text-align: center; }
.sms-whoroll .sms-whoroll__title { display: inline-block; margin: 0 0 1.1rem; padding: 0.35rem 0.95rem; border-radius: 999px; background: #ffffff; font-size: 0.9rem; font-weight: 600; line-height: 1.4; }
.sms-whoroll .sms-whoroll__line { margin: 0; font-size: clamp(2rem, 1.1rem + 3.6vw, 4.2rem); font-weight: 600; line-height: 1.15; letter-spacing: -0.035em; }
.sms-whoroll .sms-whoroll__word { display: inline-block; max-width: 100%; padding: 0 0.32em 0.06em; border-radius: 0.3em; background: #ffffff; color: var(--sms-green); text-transform: lowercase; box-shadow: 0 0.08em 0 rgba(6, 30, 53, 0.07); }
.sms-whoroll .sms-whoroll__word[hidden] { display: none; }
.sms-whoroll .sms-whoroll__word.is-out { animation: sms-c6-roll-out 0.32s var(--sms-ease) both; }
.sms-whoroll .sms-whoroll__word.is-in { animation: sms-c6-roll-in 0.45s var(--sms-ease) both; }
.sms-whoroll .sms-whoroll__list { display: flex; flex-wrap: wrap; justify-content: center; gap: 0.5rem; margin: 1.5rem auto 0; padding: 0; list-style: none; }
.sms-whoroll .sms-whoroll__item { min-width: 0; padding: 0.45rem 1rem; border-radius: 999px; background: #ffffff; font-size: 0.95rem; font-weight: 600; }
.sms-whoroll.is-rolling .sms-whoroll__list { position: absolute; width: 1px; height: 1px; margin: 0; overflow: hidden; clip-path: inset(50%); white-space: nowrap; }
.sms-whoroll .sms-whoroll__area { max-width: 40rem; margin: 1.5rem auto 0; color: var(--sms-ink-soft); }
.sms-whoroll .sms-whoroll__area p { margin: 0; }

/* ---------- Services menu ---------- */
.sms-svcmenu { padding: var(--sms-section) 0; }
.sms-svcmenu .sms-svcmenu__inner { width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-svcmenu .sms-svcmenu__head { max-width: 50rem; margin-bottom: clamp(2rem, 1.5rem + 2vw, 3.5rem); }
.sms-svcmenu .sms-svcmenu__eyebrow { display: inline-flex; align-items: center; gap: 0.5rem; margin-bottom: 0.9rem; padding: 0.35rem 0.9rem 0.35rem 0.7rem; border-radius: 999px; background: var(--sms-mint); font-size: 0.875rem; font-weight: 600; }
.sms-svcmenu .sms-svcmenu__eyebrow::before { content: ""; flex: 0 0 auto; width: 0.5rem; height: 0.5rem; border-radius: 50%; background: var(--sms-green); }
.sms-svcmenu .sms-svcmenu__title { margin: 0 0 1rem; font-size: var(--sms-step-2); font-weight: 700; line-height: 1.1; letter-spacing: -0.03em; text-wrap: balance; }
.sms-svcmenu .sms-svcmenu__lead { color: var(--sms-ink-soft); font-size: var(--sms-step-1); line-height: 1.55; }
.sms-svcmenu .sms-svcmenu__lead p { margin: 0; }
.sms-svcmenu .sms-svcmenu__list { position: relative; border-top: 1px solid var(--sms-line); }
.sms-svcmenu .sms-svcmenu__row { border-bottom: 1px solid var(--sms-line); }
.sms-svcmenu .sms-svcmenu__sum { display: grid; grid-template-columns: auto minmax(0, 1fr) auto; gap: 0.25rem clamp(0.85rem, 0.5rem + 1vw, 1.5rem); align-items: center; margin: 0.5rem 0; padding: clamp(1rem, 0.7rem + 1vw, 1.6rem) clamp(0.5rem, 0.2rem + 1vw, 1.1rem); border-radius: 1.5rem; cursor: pointer; list-style: none; transition: background-color 0.3s; }
.sms-svcmenu .sms-svcmenu__sum::-webkit-details-marker { display: none; }
.sms-svcmenu .sms-svcmenu__sum:hover,
.sms-svcmenu .sms-svcmenu__row[open] .sms-svcmenu__sum { background: var(--sms-pale); }
.sms-svcmenu .sms-svcmenu__num { align-self: start; min-width: 0; padding-top: 0.5em; color: var(--sms-green); font-size: 0.95rem; font-weight: 800; font-variant-numeric: tabular-nums; }
.sms-svcmenu .sms-svcmenu__label { min-width: 0; }
.sms-svcmenu .sms-svcmenu__name { display: block; margin: 0; font-size: clamp(1.55rem, 1.05rem + 2.1vw, 3rem); font-weight: 600; line-height: 1.1; letter-spacing: -0.035em; transition: color 0.3s, transform 0.4s var(--sms-ease); }
.sms-svcmenu .sms-svcmenu__line { display: block; max-width: 34rem; margin-top: 0.4rem; color: var(--sms-ink-soft); font-size: 0.98rem; line-height: 1.5; }
.sms-svcmenu .sms-svcmenu__go { display: grid; place-items: center; min-width: 0; width: 3rem; height: 3rem; border-radius: 50%; background: #ffffff; box-shadow: inset 0 0 0 1px var(--sms-line); color: var(--sms-navy); transition: transform 0.45s var(--sms-ease), background-color 0.3s, color 0.3s; }
.sms-svcmenu .sms-svcmenu__go-icon { width: 1.3rem; height: 1.3rem; }
.sms-svcmenu .sms-svcmenu__sum:hover .sms-svcmenu__name { transform: translateX(0.3rem); }
.sms-svcmenu .sms-svcmenu__row[open] .sms-svcmenu__name { color: var(--sms-green); }
.sms-svcmenu .sms-svcmenu__row[open] .sms-svcmenu__go { background: var(--sms-green); box-shadow: none; color: #ffffff; transform: rotate(90deg); }
.sms-svcmenu .sms-svcmenu__panel { display: grid; gap: 1.25rem; padding: 0.5rem clamp(0.5rem, 0.2rem + 1vw, 1.1rem) 1.75rem; }
.sms-svcmenu .sms-svcmenu__row[open] .sms-svcmenu__panel { animation: sms-c6-in 0.55s var(--sms-ease) both; }
.sms-svcmenu .sms-svcmenu__frame { aspect-ratio: 16 / 10; border-radius: 1.5rem; }
.sms-svcmenu .sms-svcmenu__body { min-width: 0; }
.sms-svcmenu .sms-svcmenu__items { display: grid; gap: 0.5rem; margin: 0; padding: 0; list-style: none; }
.sms-svcmenu .sms-svcmenu__item { display: flex; align-items: center; gap: 0.7rem; min-width: 0; font-weight: 600; line-height: 1.35; }
.sms-svcmenu .sms-svcmenu__item-icon { width: 2.1rem; height: 2.1rem; padding: 0.48rem; border-radius: 50%; background: var(--sms-mint); color: var(--sms-green); }
.sms-svcmenu .sms-svcmenu__item-text { min-width: 0; }
.sms-svcmenu .sms-svcmenu__actions { display: flex; flex-wrap: wrap; gap: 0.75rem; margin-top: 1.5rem; }
.sms-svcmenu .sms-svcmenu__extra { display: grid; gap: 1rem; margin: clamp(2rem, 1.5rem + 2vw, 3rem) 0 0; padding: 0; list-style: none; }
.sms-svcmenu .sms-svcmenu__extra-item { min-width: 0; }
.sms-svcmenu .sms-svcmenu__extra-link { display: grid; grid-template-columns: auto minmax(0, 1fr) auto; gap: 0.25rem 1rem; align-items: center; height: 100%; padding: 1.25rem 1.4rem; border-radius: 1.5rem; background: var(--sms-pale); color: var(--sms-navy); text-decoration: none; transition: transform 0.35s var(--sms-ease), background-color 0.3s; }
.sms-svcmenu .sms-svcmenu__extra-link:hover { transform: translateY(-3px); background: var(--sms-pale-2); }
.sms-svcmenu .sms-svcmenu__extra-icon { width: 3rem; height: 3rem; padding: 0.7rem; border-radius: 50%; background: #ffffff; color: var(--sms-green); }
.sms-svcmenu .sms-svcmenu__extra-body { min-width: 0; }
.sms-svcmenu .sms-svcmenu__extra-name { display: block; font-size: 1.1rem; font-weight: 700; line-height: 1.3; }
.sms-svcmenu .sms-svcmenu__extra-text { display: block; margin-top: 0.2rem; color: var(--sms-ink-soft); font-size: 0.95rem; line-height: 1.5; }
.sms-svcmenu .sms-svcmenu__extra-go { min-width: 0; color: var(--sms-green); font-size: 1.3rem; font-weight: 700; }
@media (max-width: 39.99em) {
  .sms-svcmenu .sms-svcmenu__go { width: 2.5rem; height: 2.5rem; }
  .sms-svcmenu .sms-svcmenu__line { font-size: 0.95rem; }
}
@media (min-width: 46em) {
  .sms-svcmenu .sms-svcmenu__extra { grid-template-columns: repeat(2, minmax(0, 1fr)); }
}
@media (min-width: 40em) and (max-width: 61.99em) {
  .sms-svcmenu .sms-svcmenu__panel { grid-template-columns: minmax(0, 0.9fr) minmax(0, 1.1fr); align-items: center; gap: 1.5rem; }
  .sms-svcmenu .sms-svcmenu__frame { aspect-ratio: 4 / 3.4; }
}
@media (min-width: 62em) {
  .sms-svcmenu .sms-svcmenu__list { min-height: 39rem; border-top: 0; }
  .sms-svcmenu .sms-svcmenu__row { width: 54%; }
  .sms-svcmenu .sms-svcmenu__row:first-child { border-top: 1px solid var(--sms-line); }
  .sms-svcmenu .sms-svcmenu__panel { position: absolute; top: 0; right: 0; width: 42%; padding: 0; background: #ffffff; }
}
@media (min-width: 80em) {
  .sms-svcmenu .sms-svcmenu__items { grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 0.75rem 1rem; }
}

/* ---------- What makes Streamline different (TRUST) ---------- */
.sms-promises { padding: var(--sms-section) 0; background: var(--sms-pale); }
.sms-promises .sms-promises__inner { width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-promises .sms-promises__head { display: grid; gap: 1rem 3rem; align-items: end; margin-bottom: clamp(2rem, 1.5rem + 2vw, 3rem); }
.sms-promises .sms-promises__eyebrow { display: inline-flex; align-items: center; gap: 0.5rem; margin-bottom: 0.9rem; padding: 0.35rem 0.9rem 0.35rem 0.7rem; border-radius: 999px; background: var(--sms-mint); font-size: 0.875rem; font-weight: 600; }
.sms-promises .sms-promises__eyebrow::before { content: ""; flex: 0 0 auto; width: 0.5rem; height: 0.5rem; border-radius: 50%; background: var(--sms-green); }
.sms-promises .sms-promises__heading { min-width: 0; }
.sms-promises .sms-promises__title { margin: 0; font-size: var(--sms-step-2); font-weight: 700; line-height: 1.1; letter-spacing: -0.03em; text-wrap: balance; }
.sms-promises .sms-promises__lead { min-width: 0; color: var(--sms-ink-soft); font-size: var(--sms-step-1); line-height: 1.55; }
.sms-promises .sms-promises__lead p { margin: 0; }
.sms-promises .sms-promises__grid { display: grid; gap: 1rem; margin: 0; padding: 0; list-style: none; }
.sms-promises .sms-promises__item { min-width: 0; padding: clamp(1.4rem, 1rem + 1.2vw, 2rem); border-radius: 1.75rem; background: #ffffff; transition: transform 0.35s var(--sms-ease); }
.sms-promises .sms-promises__item:hover { transform: translateY(-4px); }
.sms-promises .sms-promises__icon { width: 3.25rem; height: 3.25rem; margin-bottom: 1.1rem; padding: 0.75rem; border-radius: 50%; background: var(--sms-mint); color: var(--sms-green); }
.sms-promises .sms-promises__name { margin: 0 0 0.4rem; font-size: 1.2rem; font-weight: 700; line-height: 1.3; }
.sms-promises .sms-promises__text { color: var(--sms-ink-soft); }
.sms-promises .sms-promises__text p { margin: 0; }
@media (min-width: 40em) {
  .sms-promises .sms-promises__grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
}
@media (min-width: 60em) {
  .sms-promises .sms-promises__head { grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); }
}
@media (min-width: 68em) {
  .sms-promises .sms-promises__grid { grid-template-columns: repeat(4, minmax(0, 1fr)); }
}

/* ---------- Working with you: the navy island ---------- */
.sms-alongside { padding: var(--sms-section) 0; }
.sms-alongside .sms-alongside__inner { width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-alongside .sms-alongside__box { display: grid; overflow: hidden; border-radius: clamp(1.75rem, 1.2rem + 2vw, 3rem); background: var(--sms-navy); color: #ffffff; }
.sms-alongside .sms-alongside__media { position: relative; min-width: 0; }
.sms-alongside .sms-alongside__frame { height: 100%; min-height: 16rem; aspect-ratio: 4 / 3; border-radius: 0; }
.sms-alongside .sms-alongside__body { min-width: 0; padding: clamp(1.6rem, 1rem + 3vw, 4rem); }
.sms-alongside .sms-alongside__title { margin: 0 0 1.25rem; color: #ffffff; font-size: var(--sms-step-2); font-weight: 700; line-height: 1.1; letter-spacing: -0.03em; text-wrap: balance; }
.sms-alongside .sms-alongside__title .sms-mark { color: var(--sms-green-on-navy); }
.sms-alongside .sms-alongside__text { color: rgba(255, 255, 255, 0.86); font-size: var(--sms-step-1); line-height: 1.6; }
.sms-alongside .sms-alongside__text p { margin: 0; }
.sms-alongside .sms-more__toggle { color: var(--sms-green-on-navy); }
.sms-alongside .sms-more__body { color: rgba(255, 255, 255, 0.86); }
.sms-alongside .sms-alongside__quote { margin: 2rem 0 0; }
.sms-alongside .sms-alongside__bubble { margin: 0; padding: 1.2rem 1.4rem; border-radius: 1.5rem 1.5rem 1.5rem 0.4rem; background: var(--sms-navy-2); color: #ffffff; font-size: 1.02rem; font-weight: 500; line-height: 1.6; }
.sms-alongside .sms-alongside__bubble p { margin: 0; }
.sms-alongside .sms-alongside__cite { display: flex; align-items: center; gap: 0.6rem; margin-top: 0.8rem; color: var(--sms-green-on-navy); font-size: 0.95rem; font-style: normal; font-weight: 700; }
.sms-alongside .sms-alongside__cite-avatar { flex: 0 0 auto; min-width: 0; width: 2.2rem; height: 2.2rem; padding: 0.38rem; border-radius: 50%; background: #ffffff; object-fit: contain; }
.sms-alongside .sms-alongside__cite-text { min-width: 0; }
@media (min-width: 60em) {
  .sms-alongside .sms-alongside__box { grid-template-columns: minmax(0, 0.9fr) minmax(0, 1.1fr); }
  .sms-alongside .sms-alongside__frame { aspect-ratio: auto; }
}

/* ---------- Contact: mini concierge ---------- */
.sms-helpdesk { padding: var(--sms-section) 0; background: var(--sms-pale-2); }
.sms-helpdesk .sms-helpdesk__inner { width: 100%; max-width: var(--sms-max); margin: 0 auto; padding: 0 var(--sms-gutter); }
.sms-helpdesk .sms-helpdesk__title { margin: 0 0 clamp(1.25rem, 1rem + 1vw, 2rem); font-size: var(--sms-step-2); font-weight: 700; line-height: 1.1; letter-spacing: -0.03em; }
.sms-helpdesk .sms-helpdesk__box { position: relative; min-width: 0; margin: 0; padding: clamp(1.1rem, 0.6rem + 2.2vw, 2.5rem); border: 0; border-radius: clamp(1.75rem, 1.2rem + 2vw, 2.5rem); background: #ffffff; box-shadow: var(--sms-shadow-lg); }
.sms-helpdesk .sms-helpdesk__legend { display: flex; float: left; align-items: flex-end; gap: 0.6rem; width: 100%; margin: 0 0 1.5rem; padding: 0; }
.sms-helpdesk .sms-helpdesk__avatar { flex: 0 0 auto; min-width: 0; width: 2.6rem; height: 2.6rem; padding: 0.45rem; border-radius: 50%; background: #ffffff; box-shadow: var(--sms-shadow); object-fit: contain; }
.sms-helpdesk .sms-helpdesk__ask { min-width: 0; padding: 0.6rem 1.2rem 0.7rem; border-radius: 1.4rem 1.4rem 1.4rem 0.35rem; background: var(--sms-navy); color: #ffffff; font-size: clamp(1.15rem, 1rem + 0.6vw, 1.45rem); font-weight: 700; line-height: 1.3; }
.sms-helpdesk .sms-helpdesk__radio { position: absolute; width: 1px; height: 1px; margin: 0; opacity: 0; pointer-events: none; }
.sms-helpdesk .sms-helpdesk__choices { display: grid; clear: both; gap: 0.6rem; }
.sms-helpdesk .sms-helpdesk__choice { position: relative; display: flex; align-items: center; gap: 0.8rem; min-width: 0; padding: 0.9rem 1rem; border: 2px solid var(--sms-line); border-radius: 1.4rem; background: #ffffff; cursor: pointer; font-weight: 700; line-height: 1.3; transition: border-color 0.25s, background-color 0.25s, transform 0.3s var(--sms-ease); }
.sms-helpdesk .sms-helpdesk__choice:hover { border-color: var(--sms-green); transform: translateY(-3px); }
.sms-helpdesk .sms-helpdesk__choice-icon { width: 2.6rem; height: 2.6rem; padding: 0.6rem; border-radius: 50%; background: var(--sms-mint); color: var(--sms-green); transition: background-color 0.25s, color 0.25s; }
.sms-helpdesk .sms-helpdesk__choice-text { min-width: 0; padding-right: 1.25rem; }
.sms-helpdesk .sms-helpdesk__choice-tick { position: absolute; right: 0.75rem; top: 0.75rem; width: 1.3rem; height: 1.3rem; padding: 0.18rem; border-radius: 50%; background: var(--sms-green); color: #ffffff; opacity: 0; transform: scale(0.4); transition: opacity 0.25s, transform 0.3s var(--sms-ease); }
.sms-helpdesk .sms-helpdesk__panels { margin-top: 1.25rem; }
.sms-helpdesk .sms-helpdesk__panel { display: none; gap: 1.25rem; padding: clamp(1.1rem, 0.8rem + 1.4vw, 2rem); border-radius: 1.75rem 1.75rem 1.75rem 0.4rem; background: var(--sms-pale); animation: sms-c6-in 0.5s var(--sms-ease) both; }
.sms-helpdesk .sms-helpdesk__panel-main { min-width: 0; }
.sms-helpdesk .sms-helpdesk__panel-name { margin: 0 0 0.5rem; font-size: clamp(1.35rem, 1.1rem + 1vw, 1.9rem); font-weight: 700; line-height: 1.15; letter-spacing: -0.02em; }
.sms-helpdesk .sms-helpdesk__panel-text { max-width: 40rem; color: var(--sms-ink-soft); font-size: var(--sms-step-1); line-height: 1.55; }
.sms-helpdesk .sms-helpdesk__panel-text p { margin: 0; }
.sms-helpdesk .sms-helpdesk__panel-actions { display: flex; flex-wrap: wrap; gap: 0.75rem; margin-top: 1.25rem; }
.sms-helpdesk .sms-helpdesk__direct { display: grid; gap: 0.5rem; align-content: start; min-width: 0; }
.sms-helpdesk .sms-helpdesk__direct-label { min-width: 0; color: var(--sms-ink-soft); font-size: 0.95rem; font-weight: 600; }
.sms-helpdesk .sms-helpdesk__direct-link { display: flex; align-items: center; gap: 0.7rem; min-width: 0; padding: 0.7rem 0.9rem; border-radius: 1.1rem; background: #ffffff; color: var(--sms-navy); font-weight: 700; text-decoration: none; overflow-wrap: anywhere; transition: transform 0.3s var(--sms-ease); }
.sms-helpdesk .sms-helpdesk__direct-link:hover { transform: translateX(4px); }
.sms-helpdesk .sms-helpdesk__direct-icon { width: 2.2rem; height: 2.2rem; padding: 0.5rem; border-radius: 50%; background: var(--sms-mint); color: var(--sms-green); }
.sms-helpdesk .sms-helpdesk__direct-text { min-width: 0; }
""" + _helpdesk_css(5) + r"""
@media (min-width: 40em) {
  .sms-helpdesk .sms-helpdesk__choices { grid-template-columns: repeat(2, minmax(0, 1fr)); }
}
@media (min-width: 64em) {
  .sms-helpdesk .sms-helpdesk__choices { grid-template-columns: repeat(5, minmax(0, 1fr)); }
  .sms-helpdesk .sms-helpdesk__choice { flex-direction: column; align-items: flex-start; padding: 1.1rem; }
  .sms-helpdesk .sms-helpdesk__panel { grid-template-columns: minmax(0, 1.4fr) minmax(0, 1fr); align-items: start; }
}

@keyframes sms-c6-in { from { opacity: 0; transform: translateY(14px) scale(0.985); } to { opacity: 1; transform: none; } }
@keyframes sms-c6-out { from { opacity: 1; transform: none; } to { opacity: 0; transform: translateY(-10px) scale(0.99); } }
@keyframes sms-c6-roll-out { from { opacity: 1; transform: none; } to { opacity: 0; transform: translateY(-0.45em); } }
@keyframes sms-c6-roll-in { from { opacity: 0; transform: translateY(0.45em); } to { opacity: 1; transform: none; } }
"""

RISE = [".sms-concierge .sms-ask__sentence", ".sms-greeting .sms-greeting__title"]
ENTRANCE = [".sms-concierge .sms-concierge__greet", ".sms-greeting .sms-greeting__eyebrow", ".sms-concierge .sms-ask__below", ".sms-greeting .sms-greeting__lead",
            ".sms-concierge .sms-ask__stage", ".sms-greeting .sms-greeting__actions", ".sms-greeting .sms-greeting__media"]
REVEAL = [".sms-whoroll .sms-whoroll__band", ".sms-svcmenu .sms-svcmenu__head", ".sms-svcmenu .sms-svcmenu__list", ".sms-svcmenu .sms-svcmenu__extra-item",
          ".sms-promises .sms-promises__head", ".sms-promises .sms-promises__item", ".sms-alongside .sms-alongside__box",
          ".sms-chatcta .sms-chatcta__bar", ".sms-chatcta .sms-chatcta__row", ".sms-chatcta .sms-chatcta__replies",
          ".sms-helpdesk .sms-helpdesk__title", ".sms-helpdesk .sms-helpdesk__box", ".sms-askpage .sms-askpage__head", ".sms-askpage .sms-ask"]
LOOP = [".sms-greeting .sms-greeting__tag", ".sms-ask .sms-ask__card.is-out", ".sms-ask .sms-ask__card.is-in", ".sms-ask .sms-ask__faq.is-in",
        ".sms-whoroll .sms-whoroll__word.is-out", ".sms-whoroll .sms-whoroll__word.is-in", ".sms-helpdesk .sms-helpdesk__panel"]
OPEN = [".sms-svcmenu .sms-svcmenu__row[open] .sms-svcmenu__panel"]
TRANS = [".sms-header .sms-header__link", ".sms-cards .sms-cards__item", ".sms-faq .sms-faq__item",
         ".sms-ask .sms-ask__face", ".sms-ask .sms-ask__chev", ".sms-ask .sms-ask__stage", ".sms-ask .sms-ask__jump-link",
         ".sms-ask .sms-ask__tick", ".sms-ask .sms-ask__tick::after", ".sms-ask .sms-ask__tick-label",
         ".sms-svcmenu .sms-svcmenu__sum", ".sms-svcmenu .sms-svcmenu__name", ".sms-svcmenu .sms-svcmenu__go", ".sms-svcmenu .sms-svcmenu__extra-link",
         ".sms-promises .sms-promises__item", ".sms-helpdesk .sms-helpdesk__choice", ".sms-helpdesk .sms-helpdesk__choice-icon",
         ".sms-helpdesk .sms-helpdesk__choice-tick", ".sms-helpdesk .sms-helpdesk__direct-link"]

SKIP = {"contact": [1], "event-medical-cover": [2]}


# ---------------------------------------------------------------------------
# Small builders
# ---------------------------------------------------------------------------

def avatar(ctx, cls):
    return '<img class="%s" src="%s" alt="" width="378" height="399" loading="lazy" aria-hidden="true">' % (cls, ctx.asset(SHIELD))


CHEV = '<svg class="sms-ask__chev" viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M6 9l6 6 6-6"/></svg>'


def _faq_block(ctx, s, k, hidden):
    q = s["faqs"][k]
    a = _faq_html(ctx, _faq_lookup(s["faqpage"], q))
    return '<div class="sms-ask__faq" data-sms-ask-faq%s><p class="sms-ask__q">%s</p><div class="sms-ask__a">%s<div class="sms-ask__a-body">%s</div></div></div>' % (
        " hidden" if hidden else "", e(q), avatar(ctx, "sms-ask__avatar"), a)


def _side(ctx, s, lazy):
    faqs = "".join(_faq_block(ctx, s, k, k != 0) for k in range(len(s["faqs"])))
    return """<div class="sms-ask__side">
          <div class="sms-ask__source">%s<span class="sms-ask__source-text">From our FAQs</span></div>
          %s
          <div class="sms-ask__chat">%s</div>
        </div>""" % (icon("chat", "sms-ask__source-icon"), photo(ctx, s["photo"], figcls="sms-ask__frame", lazy=lazy), faqs)


def _picked(s):
    return '<div class="sms-ask__picked" hidden data-sms-ask-picked><span class="sms-ask__picked-label">%s</span><span class="sms-ask__picked-val">%s<span class="sms-ask__picked-text" data-sms-ask-picked-text>%s</span></span></div>' % (
        e(s["chips_title"]), icon("check", "sms-ask__picked-icon"), e(s["chips"][0][1]))


def ask_card(ctx, s, lazy):
    items = "".join('<li class="sms-ask__item">%s<span class="sms-ask__item-text">%s</span></li>' % (icon(ic, "sms-ask__item-icon"), e(t)) for ic, t in s["list"])
    acts = buttons(ctx, [(s["cta"], s["book"]), ("Find out more", s["page"])])
    return """<article class="sms-ask__card sms-ask__card--%s" data-sms-ask-card data-name="%s">
        <div class="sms-ask__main">
          %s
          <div class="sms-ask__top">%s<h2 class="sms-ask__name">%s</h2></div>
          <div class="sms-ask__text"><p>%s</p></div>
          <ul class="sms-ask__list">%s</ul>
          <div class="sms-ask__actions">%s</div>
        </div>
        %s
      </article>""" % (s["key"], attr(s["title"]), _picked(s), icon(s["icon"], "sms-ask__icon"), e(s["title"]), e(s["text"]), items, acts, _side(ctx, s, lazy))


def _options(s, si=None):
    out = ""
    for j, (_, t) in enumerate(s["chips"]):
        out += '<option value="%s"%s data-faq="%d">%s</option>' % ("%d-%d" % (si, j) if si is not None else str(j), " selected" if j == 0 and (si in (None, 0)) else "", s["omap"][j], e(t))
    return out


def _pick(sel_id, label_html, select_html, face_text, stop=False):
    st = '<span class="sms-ask__stop" data-sms-ask-stop>.</span>' if stop else ""
    return ('<span class="sms-ask__pick"><label class="sms-visually-hidden" for="%s">%s</label>%s'
            '<span class="sms-ask__face" aria-hidden="true"><span data-sms-ask-face>%s</span>&nbsp;%s</span>%s</span>') % (sel_id, label_html, select_html, e(face_text), CHEV, st)


def concierge(ctx):
    svc_opts = "".join('<option value="%d"%s>%s</option>' % (i, " selected" if i == 0 else "", e(s["title"])) for i, s in enumerate(SVCS))
    svc_sel = '<select class="sms-ask__select" id="sms-ask-svc" data-sms-ask-svc>%s</select>' % svc_opts
    groups = "".join('<optgroup label="%s">%s</optgroup>' % (attr(s["chips_title"]), _options(s, i)) for i, s in enumerate(SVCS))
    for_sel = '<select class="sms-ask__select" id="sms-ask-for" data-sms-ask-for>%s</select>' % groups
    cards = "".join(ask_card(ctx, s, lazy=(i != 0)) for i, s in enumerate(SVCS))
    jump = "".join('<li class="sms-ask__jump-item"><a class="sms-ask__jump-link" href="%s">%s</a></li>' % (ctx.href(s["slug"]), e(s["title"])) for s in C.SERVICES)
    return """<section class="sms-concierge">
  <div class="sms-concierge__inner">
    <div class="sms-concierge__greet">
      <img class="sms-concierge__avatar" src="%s" alt="" width="378" height="399" fetchpriority="high" aria-hidden="true">
      <h1 class="sms-concierge__title">How can we <span class="sms-mark">help?</span></h1>
    </div>
    <div class="sms-ask" data-sms-ask>
      <p class="sms-ask__sentence">I&rsquo;m looking for %s for %s</p>
      <div class="sms-ask__below">
        <p class="sms-ask__hint">%sTap the green words to change them.</p>
        <ul class="sms-ask__jump"><li class="sms-ask__jump-label">Or go straight to</li>%s</ul>
      </div>
      <div class="sms-ask__live" aria-live="polite" data-sms-ask-live></div>
      <div class="sms-ask__stage" data-sms-ask-stage>
      %s
      </div>
    </div>
  </div>
</section>
""" % (ctx.asset(SHIELD), _pick("sms-ask-svc", "Service", svc_sel, SVCS[0]["title"]),
       _pick("sms-ask-for", '<span data-sms-ask-label>Who or what it is for</span>', for_sel, SVCS[0]["chips"][0][1], stop=True),
       icon("sparkle", "sms-ask__hint-icon"), jump, cards)


# ---------------------------------------------------------------------------
# Required hooks
# ---------------------------------------------------------------------------

def page_hero(ctx, h):
    sub = '<div class="sms-greeting__sub">%s</div>' % e(h["sub"]) if h.get("sub") else ""
    acts = '<div class="sms-greeting__actions">%s</div>' % buttons(ctx, h["buttons"]) if h.get("buttons") else ""
    tags = ""
    for i, (ic, t) in enumerate(h.get("chips", [])[:2], 1):
        txt = e(t)
        if ic == "phone":
            txt = '<a class="sms-greeting__tag-link" href="tel:%s">%s</a>' % (PHONE_TEL, e(t))
        elif ic == "mail":
            txt = '<a class="sms-greeting__tag-link" href="mailto:%s">%s</a>' % (EMAIL, e(t))
        tags += '<li class="sms-greeting__tag sms-greeting__tag--%d">%s<span class="sms-greeting__tag-text">%s</span></li>' % (i, icon(ic, "sms-greeting__tag-icon"), txt)
    return """<section class="sms-greeting">
  <div class="sms-greeting__inner">
    <div class="sms-greeting__card">
      <div class="sms-greeting__copy">
        <nav class="sms-greeting__crumb" aria-label="Breadcrumb"><a class="sms-greeting__crumb-link" href="%s">Home</a> <span aria-hidden="true">/</span> %s</nav>
        <div class="sms-greeting__eyebrow">%s</div>
        <h1 class="sms-greeting__title">%s</h1>
        %s
        <div class="sms-greeting__lead">%s</div>
        %s
      </div>
      <div class="sms-greeting__media">
        %s
        <ul class="sms-greeting__tags">%s</ul>
      </div>
    </div>
  </div>
</section>
""" % (ctx.href("home"), e(LABEL[ctx.slug]), e(h["eyebrow"]), e(h["title"]), sub, paras(h["body"]), acts,
       photo(ctx, h["photo"], figcls="sms-greeting__frame", lazy=False), tags)


def _visitor_question(title):
    return title.endswith("?") and title.split(" ", 1)[0] in ("How", "What", "Can", "Do", "Where", "When", "Who")


def cta(ctx, d):
    btns = list(d["buttons"])
    if not any(t == "tel" for _, t in btns):
        btns.append(("Call 01283 358789", "tel"))
    if _visitor_question(d["title"]):
        rows = '<div class="sms-chatcta__row sms-chatcta__row--you"><h2 class="sms-chatcta__bubble sms-chatcta__bubble--you sms-chatcta__title">%s</h2></div>' % e(d["title"])
        rows += '<div class="sms-chatcta__row">%s<div class="sms-chatcta__bubble"><div class="sms-chatcta__text">%s</div></div></div>' % (avatar(ctx, "sms-chatcta__avatar"), paras(d["text"]))
    else:
        rows = '<div class="sms-chatcta__row"><span class="sms-chatcta__gap" aria-hidden="true"></span><div class="sms-chatcta__bubble sms-chatcta__bubble--first"><h2 class="sms-chatcta__title">%s</h2></div></div>' % e(d["title"])
        rows += '<div class="sms-chatcta__row">%s<div class="sms-chatcta__bubble"><div class="sms-chatcta__text">%s</div></div></div>' % (avatar(ctx, "sms-chatcta__avatar"), paras(d["text"]))
    return """<section class="sms-chatcta">
  <div class="sms-chatcta__inner">
    <div class="sms-chatcta__window">
      <div class="sms-chatcta__bar">%s<span class="sms-chatcta__bar-name">Streamline Safety &amp; Medical Solutions</span></div>
      <div class="sms-chatcta__thread">
        %s
        <div class="sms-chatcta__replies">%s</div>
      </div>
    </div>
  </div>
</section>
""" % (avatar(ctx, "sms-chatcta__avatar"), rows, buttons(ctx, btns))


def chrome_top(ctx):
    return header(ctx, "blue")


def chrome_bottom(ctx):
    return footer(ctx, "white")


# ---------------------------------------------------------------------------
# Inner page extras
# ---------------------------------------------------------------------------

def event_builder(ctx):
    s = SVCS[0]
    opts = _options(s)
    sel = '<select class="sms-ask__select" id="sms-ask-for" data-sms-ask-for>%s</select>' % opts
    ready = "".join('<li class="sms-ask__ready-item"><label class="sms-ask__tick-label"><input class="sms-ask__tick" type="checkbox"><span class="sms-ask__tick-text">%s</span></label></li>' % e(t) for _, t in EV_BOOK["chips"])
    body = EV_BOOK["body"]
    card = """<article class="sms-ask__card sms-ask__card--event" data-sms-ask-card data-name="%s">
        <div class="sms-ask__main">
          %s
          <div class="sms-ask__text"><p>%s</p>%s</div>
          <div data-sms-ready>
            <h3 class="sms-ask__ready-title">Have these ready</h3>
            <p class="sms-ask__ready-sub">%s</p>
            <ul class="sms-ask__ready">%s</ul>
            <p class="sms-ask__count" hidden aria-live="polite" data-sms-ready-count></p>
          </div>
          <div class="sms-ask__actions">%s</div>
        </div>
        %s
      </article>""" % (attr(s["title"]), _picked(s), e(body[0]), more(paras(body[1:])), e(EV_BOOK["chips_title"]), ready,
                       buttons(ctx, EV_BOOK["buttons"] + [("Call 01283 358789", "tel")]), _side(ctx, dict(s, photo=EV_BOOK["photo"]), True))
    ctx.notes.append("Event page sentence builder replaces the \"Book Your Event Medical Cover\" section: its text, quote list and button are all inside the answer card")
    return """<section class="sms-askpage">
  <div class="sms-askpage__inner">
    <div class="sms-askpage__head"><div class="sms-askpage__eyebrow">%s</div><h2 class="sms-askpage__title">%s</h2></div>
    <div class="sms-ask" data-sms-ask>
      <p class="sms-ask__sentence">I&rsquo;m looking for <span class="sms-ask__fixed">%s</span> for %s</p>
      <div class="sms-ask__below"><p class="sms-ask__hint">%sTap the green words to change them.</p></div>
      <div class="sms-ask__live" aria-live="polite" data-sms-ask-live></div>
      <div class="sms-ask__stage" data-sms-ask-stage>
      %s
      </div>
    </div>
  </div>
</section>
""" % (e(EV_BOOK["eyebrow"]), e(EV_BOOK["title"]), e(s["title"]),
       _pick("sms-ask-for", '<span data-sms-ask-label>%s</span>' % e(s["chips_title"]), sel, s["chips"][0][1], stop=True),
       icon("sparkle", "sms-ask__hint-icon"), card)


def helpdesk(ctx):
    links = {it["link"]: it for it in CONTACT_LINKS["items"]}
    topics = []
    for s in C.SERVICES:
        it = links[s["slug"]]
        topics.append({"icon": it["icon"], "title": it["title"], "text": it["text"], "go": (it["go"], it["link"]), "book": (s["cta"], "book:" + s["key"])})
    topics.append({"icon": C.CAREERS["icon"], "title": C.CAREERS["title"], "text": C.CAREERS["text"], "go": (C.CAREERS["cta"], C.CAREERS["slug"]),
                   "book": (C.PAGES["pre-hospital-career-support"]["hero"]["buttons"][0][0], "book:careers")})
    rec = links["recruitment"]
    topics.append({"icon": rec["icon"], "title": rec["title"], "text": rec["text"], "go": (rec["go"], rec["link"]), "book": None})
    radios = "".join('<input class="sms-helpdesk__radio sms-helpdesk__r%d" type="radio" name="sms-help" id="sms-help-%d"%s>' % (i, i, " checked" if i == 0 else "") for i in range(len(topics)))
    choices = "".join('<label class="sms-helpdesk__choice sms-helpdesk__choice--%d" for="sms-help-%d">%s<span class="sms-helpdesk__choice-text">%s</span>%s</label>' % (
        i, i, icon(t["icon"], "sms-helpdesk__choice-icon"), e(t["title"]), icon("check", "sms-helpdesk__choice-tick")) for i, t in enumerate(topics))
    direct = """<div class="sms-helpdesk__direct">
            <div class="sms-helpdesk__direct-label">Or speak to us directly</div>
            <a class="sms-helpdesk__direct-link" href="tel:%s">%s<span class="sms-helpdesk__direct-text">%s</span></a>
            <a class="sms-helpdesk__direct-link" href="mailto:%s">%s<span class="sms-helpdesk__direct-text">%s</span></a>
          </div>""" % (PHONE_TEL, icon("phone", "sms-helpdesk__direct-icon"), PHONE, EMAIL, icon("mail", "sms-helpdesk__direct-icon"), EMAIL)
    panels = ""
    for i, t in enumerate(topics):
        btns = ([t["book"]] if t["book"] else []) + [t["go"]]
        panels += """<div class="sms-helpdesk__panel sms-helpdesk__panel--%d">
          <div class="sms-helpdesk__panel-main">
            <h3 class="sms-helpdesk__panel-name">%s</h3>
            <div class="sms-helpdesk__panel-text"><p>%s</p></div>
            <div class="sms-helpdesk__panel-actions">%s</div>
          </div>
          %s
        </div>""" % (i, e(t["title"]), e(t["text"]), buttons(ctx, btns), direct)
    return """<section class="sms-helpdesk">
  <div class="sms-helpdesk__inner">
    <h2 class="sms-helpdesk__title">%s</h2>
    <fieldset class="sms-helpdesk__box">
      <legend class="sms-helpdesk__legend">%s<span class="sms-helpdesk__ask">What can we help with?</span></legend>
      %s
      <div class="sms-helpdesk__choices">%s</div>
      <div class="sms-helpdesk__panels" aria-live="polite">%s</div>
    </fieldset>
  </div>
</section>
""" % (e(CONTACT_LINKS["title"]), avatar(ctx, "sms-helpdesk__avatar"), radios, choices, panels)


def inner_extra(ctx, slug):
    if slug == "contact":
        return helpdesk(ctx)
    if slug == "event-medical-cover":
        return event_builder(ctx)
    return ""


# ---------------------------------------------------------------------------
# Homepage
# ---------------------------------------------------------------------------

def whoroll(ctx):
    items = "".join('<li class="sms-whoroll__item">%s</li>' % e(w) for w in C.WHO)
    return """<section class="sms-whoroll" data-sms-roll>
  <div class="sms-whoroll__inner">
    <div class="sms-whoroll__band">
      <h2 class="sms-whoroll__title">Who does Streamline work with?</h2>
      <p class="sms-whoroll__line">We support <span class="sms-whoroll__word" aria-hidden="true" hidden data-sms-roll-word></span></p>
      <ul class="sms-whoroll__list" data-sms-roll-list>%s</ul>
      <div class="sms-whoroll__area"><p>%s</p></div>
    </div>
  </div>
</section>
""" % (items, e(C.AREA))


def svcmenu(ctx):
    rows = ""
    for i, s in enumerate(C.SERVICES):
        items = "".join('<li class="sms-svcmenu__item">%s<span class="sms-svcmenu__item-text">%s</span></li>' % (icon(ic, "sms-svcmenu__item-icon"), e(t)) for ic, t in s["list"])
        rows += """<details class="sms-svcmenu__row" name="sms-services"%s>
        <summary class="sms-svcmenu__sum"><span class="sms-svcmenu__num" aria-hidden="true">%02d</span><span class="sms-svcmenu__label"><h3 class="sms-svcmenu__name">%s</h3><span class="sms-svcmenu__line">%s</span></span><span class="sms-svcmenu__go" aria-hidden="true">%s</span></summary>
        <div class="sms-svcmenu__panel">
          %s
          <div class="sms-svcmenu__body">
            <ul class="sms-svcmenu__items">%s</ul>
            <div class="sms-svcmenu__actions">%s</div>
          </div>
        </div>
      </details>""" % (" open" if i == 0 else "", i + 1, e(s["title"]), e(s["text"]), icon("arrow", "sms-svcmenu__go-icon"),
                       photo(ctx, s["photo"], figcls="sms-svcmenu__frame"), items, buttons(ctx, [(s["cta"], "book:" + s["key"]), ("Find out more", s["slug"])]))
    rec = C.PAGES["recruitment"]["hero"]
    extra = [(C.CAREERS["icon"], C.CAREERS["title"], C.CAREERS["text"], C.CAREERS["slug"]),
             ("users", plain(rec["title"]), rec["body"][0], "recruitment")]
    extras = "".join('<li class="sms-svcmenu__extra-item"><a class="sms-svcmenu__extra-link" href="%s">%s<span class="sms-svcmenu__extra-body"><span class="sms-svcmenu__extra-name">%s</span><span class="sms-svcmenu__extra-text">%s</span></span><span class="sms-svcmenu__extra-go" aria-hidden="true">&rarr;</span></a></li>' % (
        ctx.href(sl), icon(ic, "sms-svcmenu__extra-icon"), e(t), e(tx)) for ic, t, tx, sl in extra)
    return """<section class="sms-svcmenu" id="services">
  <div class="sms-svcmenu__inner">
    <div class="sms-svcmenu__head">
      <div class="sms-svcmenu__eyebrow">Our Services</div>
      <h2 class="sms-svcmenu__title">Clinician-Led Medical Cover, First Aid Training &amp; <span class="sms-mark">Safety Consultancy</span></h2>
      <div class="sms-svcmenu__lead"><p>%s</p></div>
    </div>
    <div class="sms-svcmenu__list" data-sms-menu>
      %s
    </div>
    <ul class="sms-svcmenu__extra">%s</ul>
  </div>
</section>
""" % (e(C.INTRO), rows, extras)


def promises(ctx):
    lead = dict(C.faqs("home"))["What makes Streamline different?"]
    items = "".join('<li class="sms-promises__item">%s<h3 class="sms-promises__name">%s</h3><div class="sms-promises__text"><p>%s</p></div></li>' % (
        icon(ic, "sms-promises__icon"), e(t), e(tx)) for ic, t, tx in C.TRUST)
    return """<section class="sms-promises">
  <div class="sms-promises__inner">
    <div class="sms-promises__head">
      <div class="sms-promises__heading"><div class="sms-promises__eyebrow">%s</div><h2 class="sms-promises__title">What makes Streamline <span class="sms-mark">different?</span></h2></div>
      <div class="sms-promises__lead">%s</div>
    </div>
    <ul class="sms-promises__grid">%s</ul>
  </div>
</section>
""" % (e(C.STRAP), lead, items)


def alongside(ctx):
    w = C.WORKING_WITH
    return """<section class="sms-alongside">
  <div class="sms-alongside__inner">
    <div class="sms-alongside__box">
      <div class="sms-alongside__media">%s</div>
      <div class="sms-alongside__body">
        <h2 class="sms-alongside__title">%s</h2>
        <div class="sms-alongside__text"><p>%s</p></div>
        %s
        <figure class="sms-alongside__quote">
          <blockquote class="sms-alongside__bubble"><p>%s</p></blockquote>
          <figcaption class="sms-alongside__cite">%s<span class="sms-alongside__cite-text">Mathew Stones, Director</span></figcaption>
        </figure>
      </div>
    </div>
  </div>
</section>
""" % (photo(ctx, "team", figcls="sms-alongside__frame"), e(w["title"]), e(w["body"][0]), more(paras(w["body"][1:])), e(C.MATHEW_QUOTE),
       avatar(ctx, "sms-alongside__cite-avatar"))


def home(ctx):
    ctx.notes.append("Homepage hero heading \"How can we help?\" and the interface labels in the sentence builder are concept UI copy")
    ctx.notes.append("Services heading uses the live homepage H1: \"Clinician-Led Medical Cover, First Aid Training & Safety Consultancy\"")
    ctx.notes.append("Sentence builder: second-list options are the feature chip lists from each service page; the question and answer shown is verbatim from that page's FAQs")
    out = concierge(ctx)
    out += whoroll(ctx)
    out += svcmenu(ctx)
    out += promises(ctx)
    out += alongside(ctx)
    allf = dict(C.faqs("home"))
    picks = ["What services does Streamline provide?", "Who does Streamline work with?", "Can Streamline provide more than one service?",
             "Do you offer a free initial discussion?", "Where is Streamline based?", "How quickly will Streamline respond?"]
    out += SHARED_RENDERERS["faq"](ctx, {"tone": "pale", "eyebrow": "FAQs", "title": "General Streamline [[FAQs]]",
                                        "lead": ["Answers to common questions about Streamline Safety & Medical Solutions, our team, services, bookings and how we work."],
                                        "items": [(q, allf[q]) for q in picks], "show": 6})
    disc = _strip(allf["Do you offer a free initial discussion?"])
    disc = disc[len("Yes. "):] if disc.startswith("Yes. ") else disc
    out += cta(ctx, {"title": "Have any questions? We’re here to help.", "text": [disc],
                     "buttons": [("Book online", "book"), ("Contact Us", "contact")]})
    return out


# ---------------------------------------------------------------------------
# Script (vanilla, progressive enhancement)
# ---------------------------------------------------------------------------
JS = r"""<script>
(function () {
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  function each(list, fn) { Array.prototype.forEach.call(list, fn); }

  /* Sentence builder: the page answers with the right service */
  each(document.querySelectorAll('[data-sms-ask]'), function (root) {
    var svc = root.querySelector('[data-sms-ask-svc]');
    var pick = root.querySelector('[data-sms-ask-for]');
    var stage = root.querySelector('[data-sms-ask-stage]');
    var cards = root.querySelectorAll('[data-sms-ask-card]');
    var live = root.querySelector('[data-sms-ask-live]');
    var label = root.querySelector('[data-sms-ask-label]');
    var stop = root.querySelector('[data-sms-ask-stop]');
    if (!pick || !stage || !cards.length) return;
    var groups = [];
    var gs = pick.querySelectorAll('optgroup');
    if (gs.length) {
      each(gs, function (g) { groups.push({ label: g.label, opts: Array.prototype.slice.call(g.querySelectorAll('option')) }); });
    } else {
      groups.push({ label: label ? label.textContent : '', opts: Array.prototype.slice.call(pick.options) });
    }
    var current = -1;
    var timer = 0;
    root.classList.add('is-js');
    function setFace(sel) {
      var f = sel.parentNode.querySelector('[data-sms-ask-face]');
      var o = sel.options[sel.selectedIndex];
      if (f && o) f.textContent = o.text;
    }
    function fill(i) {
      while (pick.firstChild) pick.removeChild(pick.firstChild);
      groups[i].opts.forEach(function (o) { pick.appendChild(o); });
      pick.selectedIndex = 0;
      if (label) label.textContent = groups[i].label;
    }
    function update(animate) {
      var i = svc ? svc.selectedIndex : 0;
      var changed = i !== current;
      if (changed && svc) fill(i);
      var o = pick.options[pick.selectedIndex];
      var k = parseInt(o.getAttribute('data-faq') || '0', 10);
      var card = cards[i];
      var from = stage.offsetHeight;
      var prev = current;
      current = i;
      each(cards, function (c, j) { c.hidden = j !== i; c.classList.remove('is-in', 'is-out'); });
      var faqs = card.querySelectorAll('[data-sms-ask-faq]');
      var faqChanged = false;
      each(faqs, function (f, j) {
        var show = j === k;
        if (show && f.hidden) faqChanged = true;
        f.hidden = !show;
        f.classList.remove('is-in');
      });
      var picked = card.querySelector('[data-sms-ask-picked]');
      if (picked) {
        picked.hidden = false;
        var pt = picked.querySelector('[data-sms-ask-picked-text]');
        if (pt) pt.textContent = o.text;
      }
      if (stop) stop.hidden = /\?\s*$/.test(o.text);
      if (svc) setFace(svc);
      setFace(pick);
      if (live && animate) live.textContent = 'Showing ' + card.getAttribute('data-name') + ': ' + o.text;
      if (!animate || reduce) return;
      if (changed && prev >= 0) {
        var old = cards[prev];
        old.hidden = false;
        old.classList.add('is-out');
        setTimeout(function () {
          if (old.classList.contains('is-out')) { old.classList.remove('is-out'); old.hidden = true; }
        }, 380);
        card.classList.add('is-in');
      } else if (faqChanged && faqs[k]) {
        faqs[k].classList.add('is-in');
      }
      var to = card.offsetHeight;
      stage.style.height = from + 'px';
      stage.classList.add('is-sizing');
      void stage.offsetHeight;
      stage.style.height = to + 'px';
      clearTimeout(timer);
      timer = setTimeout(function () { stage.style.height = ''; stage.classList.remove('is-sizing'); }, 560);
    }
    if (svc) svc.addEventListener('change', function () { update(true); });
    pick.addEventListener('change', function () { update(true); });
    update(false);
  });

  /* Have these ready: a small tally */
  each(document.querySelectorAll('[data-sms-ready]'), function (box) {
    var ticks = box.querySelectorAll('input[type="checkbox"]');
    var out = box.querySelector('[data-sms-ready-count]');
    if (!out || !ticks.length) return;
    out.hidden = false;
    function count() {
      var n = 0;
      each(ticks, function (t) { if (t.checked) n++; });
      out.textContent = n === ticks.length ? 'All ' + n + ' ready' : n + ' of ' + ticks.length + ' ready';
    }
    each(ticks, function (t) { t.addEventListener('change', count); });
    count();
  });

  /* Who we work with: a gentle vertical roll */
  each(document.querySelectorAll('[data-sms-roll]'), function (root) {
    if (reduce) return;
    var word = root.querySelector('[data-sms-roll-word]');
    var items = root.querySelectorAll('[data-sms-roll-list] li');
    if (!word || !items.length) return;
    var words = Array.prototype.map.call(items, function (li) { return li.textContent; });
    var i = 0;
    var visible = false;
    var busy = false;
    root.classList.add('is-rolling');
    word.hidden = false;
    word.textContent = words[0];
    function next() {
      if (!visible || document.hidden || busy) return;
      busy = true;
      word.classList.remove('is-in');
      word.classList.add('is-out');
      setTimeout(function () {
        i = (i + 1) % words.length;
        word.textContent = words[i];
        word.classList.remove('is-out');
        void word.offsetWidth;
        word.classList.add('is-in');
        busy = false;
      }, 320);
    }
    if ('IntersectionObserver' in window) {
      new IntersectionObserver(function (en) { visible = en[0].isIntersecting; }, { threshold: 0.2 }).observe(root);
    } else {
      visible = true;
    }
    setInterval(next, 2300);
  });

  /* Services menu: opens on hover / keyboard focus on wide screens, one at a time */
  each(document.querySelectorAll('[data-sms-menu]'), function (menu) {
    var rows = menu.querySelectorAll('details');
    var wide = window.matchMedia('(min-width: 62em)');
    var fine = window.matchMedia('(hover: hover) and (pointer: fine)');
    function fit() {
      menu.style.minHeight = '';
      if (!wide.matches) return;
      var p = menu.querySelector('details[open] .sms-svcmenu__panel');
      if (p && p.offsetHeight > menu.offsetHeight) menu.style.minHeight = p.offsetHeight + 'px';
    }
    function openRow(r) {
      each(rows, function (x) { if (x !== r) x.open = false; });
      r.open = true;
      fit();
    }
    each(rows, function (r) { r.addEventListener('toggle', fit); });
    window.addEventListener('resize', fit, { passive: true });
    fit();
    each(rows, function (r) {
      var s = r.querySelector('summary');
      var t = 0;
      r.addEventListener('mouseenter', function () {
        if (!fine.matches || !wide.matches) return;
        clearTimeout(t);
        t = setTimeout(function () { openRow(r); }, 140);
      });
      r.addEventListener('mouseleave', function () { clearTimeout(t); });
      s.addEventListener('focus', function () {
        var kb = true;
        try { kb = s.matches(':focus-visible'); } catch (err) { kb = true; }
        if (wide.matches && kb) openRow(r);
      });
      s.addEventListener('click', function (ev) {
        if (!wide.matches) return;
        ev.preventDefault();
        openRow(r);
      });
    });
  });
})();
</script>
"""


def scripts(ctx, main):
    if "data-sms-ask" in main or "data-sms-roll" in main or "data-sms-menu" in main:
        return JS
    return ""
