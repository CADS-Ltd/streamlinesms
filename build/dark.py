"""Shared cinematic structure for concepts 10-12 (first written for the dark round-4 concepts, since removed).

Restyles the shared sections from common.py through the semantic tokens
(--sms-ink, --sms-surface, --sms-accent ...). Each dark concept sets its own
token values and display font on top of this.
"""

CSS = r"""
/* ===== Cinematic base (light.py sets the colours for concepts 10-12) ===== */
.sms-page {
  --sms-bg: #050c16;
  --sms-surface: #0c1929;
  --sms-pale: #08131f;
  --sms-pale-2: rgba(255, 255, 255, 0.06);
  --sms-mint: rgba(130, 208, 110, 0.12);
  --sms-ink: #e9eff5;
  --sms-ink-soft: #aebccb;
  --sms-line: rgba(170, 195, 220, 0.16);
  --sms-line-green: rgba(130, 208, 110, 0.22);
  --sms-accent: #82d06e;
  --sms-field: #07111c;
  --sms-field-line: rgba(170, 195, 220, 0.38);
  --sms-glow: rgba(130, 208, 110, 0.35);
  --sms-shadow: 0 0 0 1px var(--sms-line);
  --sms-shadow-lg: 0 30px 70px rgba(0, 0, 0, 0.45);
  --sms-hw: 300;
  --sms-sw: 700;
  --sms-title: #ffffff;
  --sms-on-accent: #04121f;
  --sms-header-bg: rgba(5, 12, 22, 0.72);
  --sms-card-pale: #0d1c2d;
  --sms-footer-bg: #03080f;
  --sms-seg-on-bg: #f2f6f9;
  --sms-seg-on-fg: #04121f;
  --sms-btn-line: rgba(233, 239, 245, 0.32);
  --sms-error: #ff9e96;
  --sms-warn: #ffcf66;
  --sms-hair: rgba(255, 255, 255, 0.05);
  --sms-ring-line: rgba(255, 255, 255, 0.35);
  --sms-shade: 5, 12, 22;
  font-weight: 300;
  color-scheme: dark;
}
.sms-page ::selection { background: var(--sms-accent); color: var(--sms-bg); }
.sms-page a:focus-visible,
.sms-page button:focus-visible,
.sms-page summary:focus-visible,
.sms-page input:focus-visible,
.sms-page select:focus-visible,
.sms-page textarea:focus-visible { outline-color: var(--sms-accent); }
.sms-page .sms-skip { background: var(--sms-accent); color: var(--sms-bg); }

/* Buttons: bright green pill with navy text (high contrast on dark) */
.sms-page .sms-btn { font-weight: 600; letter-spacing: 0.01em; }
.sms-page .sms-btn--primary { border-color: var(--sms-accent); background: var(--sms-accent); color: var(--sms-on-accent); box-shadow: none; transition: transform 0.4s var(--sms-ease), box-shadow 0.6s var(--sms-ease); }
.sms-page .sms-btn--primary:hover { box-shadow: 0 12px 40px var(--sms-glow); }
.sms-page .sms-btn--outline { border-color: var(--sms-btn-line); color: var(--sms-ink); }
.sms-page .sms-btn--outline:hover { border-color: var(--sms-ink); background: transparent; color: var(--sms-ink); }

/* Header: glass over the page */
.sms-header { border-bottom: 1px solid var(--sms-line); background: var(--sms-header-bg); }
.sms-header .sms-header__link { color: var(--sms-ink-soft); font-weight: 400; }
.sms-header .sms-header__link:hover,
.sms-header .sms-header__link[aria-current="page"] { color: var(--sms-ink); }
.sms-header .sms-header__link::after { background: var(--sms-accent); }
.sms-header .sms-header__summary { background: var(--sms-pale-2); color: var(--sms-ink); box-shadow: inset 0 0 0 1px var(--sms-line); }
.sms-header .sms-header__panel { background: var(--sms-surface); box-shadow: 0 0 0 1px var(--sms-line), 0 24px 60px rgba(0, 0, 0, 0.55); }
.sms-header .sms-header__panel-link { color: var(--sms-ink); font-weight: 400; }
.sms-header .sms-header__panel-link:hover,
.sms-header .sms-header__panel-link[aria-current="page"] { background: var(--sms-pale-2); }
.sms-header .sms-header__panel-icon { color: var(--sms-accent); }

/* Section heads: light display type, one bold or accented phrase */
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
.sms-booking .sms-booking__eyebrow { gap: 0.75rem; margin-bottom: 1.25rem; color: var(--sms-accent); font-weight: 500; letter-spacing: 0.22em; }
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
.sms-booking .sms-booking__eyebrow::before { width: 0.45rem; height: 0.45rem; border-radius: 50%; background: var(--sms-accent); box-shadow: 0 0 12px var(--sms-glow); }
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
.sms-booking .sms-booking__title { margin-bottom: 1.25rem; font-size: clamp(2rem, 1.3rem + 2.8vw, 3.6rem); font-weight: var(--sms-hw); line-height: 1.08; letter-spacing: -0.03em; color: var(--sms-title); }
.sms-feature .sms-feature__lead,
.sms-cards .sms-cards__lead,
.sms-steps .sms-steps__lead,
.sms-checklist .sms-checklist__lead,
.sms-people .sms-people__lead,
.sms-links .sms-links__lead,
.sms-faq .sms-faq__lead { color: var(--sms-ink-soft); font-weight: 300; }

/* Tones: white = page background, pale = a slightly lifted band */
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
.sms-feature .sms-watermark,
.sms-cards .sms-watermark,
.sms-steps .sms-watermark,
.sms-quotes .sms-watermark,
.sms-people .sms-watermark,
.sms-claim .sms-watermark,
.sms-checklist .sms-watermark { opacity: 0.035; filter: brightness(0) invert(1); }

/* Panels: hairline borders instead of shadows */
.sms-page .sms-photo { background: var(--sms-surface); }
.sms-page .sms-chips__item { background: var(--sms-surface); box-shadow: inset 0 0 0 1px var(--sms-line); font-weight: 400; }
.sms-page .sms-chips__icon { background: var(--sms-mint); color: var(--sms-accent); }
.sms-page .sms-more__toggle { color: var(--sms-accent); font-weight: 500; }
.sms-feature.sms-tone-white .sms-chips__item { background: var(--sms-surface); box-shadow: inset 0 0 0 1px var(--sms-line); }
.sms-feature .sms-feature__frame { box-shadow: var(--sms-shadow-lg); }
.sms-feature .sms-feature__blob { border-radius: 50%; background: radial-gradient(circle, rgba(130, 208, 110, 0.22), transparent 65%); }
.sms-feature .sms-feature__lead { color: var(--sms-ink); font-weight: 300; }
.sms-feature .sms-feature__strap { background: var(--sms-mint); color: var(--sms-ink); font-weight: 500; box-shadow: inset 0 0 0 1px var(--sms-line-green); }
.sms-feature .sms-feature__strap-icon { color: var(--sms-accent); }
.sms-feature .sms-feature__chips-title { font-weight: 500; }

.sms-cards .sms-cards__item,
.sms-cards.sms-tone-white .sms-cards__item { background: var(--sms-surface); box-shadow: inset 0 0 0 1px var(--sms-line); }
.sms-cards.sms-tone-pale .sms-cards__item { background: var(--sms-card-pale); }
.sms-cards .sms-cards__item:hover { box-shadow: inset 0 0 0 1px var(--sms-line-green), 0 20px 50px rgba(0, 0, 0, 0.35); }
.sms-cards .sms-cards__icon,
.sms-cards.sms-tone-white .sms-cards__icon { background: var(--sms-mint); color: var(--sms-accent); }
.sms-cards .sms-cards__num { color: var(--sms-accent); font-weight: 300; }
.sms-cards .sms-cards__name { font-weight: 500; color: var(--sms-title); }
.sms-cards .sms-cards__meta,
.sms-cards.sms-tone-white .sms-cards__meta { background: var(--sms-pale-2); color: var(--sms-ink); font-weight: 400; }
.sms-cards .sms-cards__meta-icon,
.sms-cards .sms-cards__check,
.sms-cards .sms-cards__link { color: var(--sms-accent); }
.sms-cards .sms-cards__list-title { color: var(--sms-ink); font-weight: 600; }

.sms-steps .sms-steps__badge { background: var(--sms-surface); color: var(--sms-accent); box-shadow: 0 0 0 6px var(--sms-bg), inset 0 0 0 1px var(--sms-line-green); }
.sms-steps.sms-tone-pale .sms-steps__badge { box-shadow: 0 0 0 6px var(--sms-pale), inset 0 0 0 1px var(--sms-line-green); }
.sms-steps .sms-steps__line-fill { background: linear-gradient(90deg, var(--sms-accent), rgba(130, 208, 110, 0.4)); }
.sms-steps .sms-steps__num { background: var(--sms-accent); color: var(--sms-on-accent); }
.sms-steps .sms-steps__name { font-weight: 500; color: var(--sms-title); }
.sms-steps .sms-steps__note,
.sms-steps.sms-tone-white .sms-steps__note { background: var(--sms-surface); box-shadow: inset 0 0 0 1px var(--sms-line); }

.sms-checklist .sms-checklist__item { background: var(--sms-surface); box-shadow: inset 0 0 0 1px var(--sms-line); font-weight: 400; }
.sms-checklist .sms-checklist__icon { background: var(--sms-mint); color: var(--sms-accent); }

.sms-notice .sms-notice__box { background: var(--sms-surface); box-shadow: inset 0 0 0 1px var(--sms-line); }
.sms-notice .sms-notice__badge { background: var(--sms-mint); color: var(--sms-accent); }
.sms-notice .sms-notice__title { font-weight: 500; }

.sms-faq .sms-faq__item,
.sms-faq.sms-tone-white .sms-faq__item { background: var(--sms-surface); box-shadow: inset 0 0 0 1px var(--sms-line); }
.sms-faq .sms-faq__q { font-weight: 400; }
.sms-faq .sms-faq__q:hover { color: var(--sms-title); }
.sms-faq .sms-faq__q::after { background: var(--sms-mint); color: var(--sms-accent); }
.sms-faq .sms-faq__a a { color: var(--sms-accent); }
.sms-faq .sms-faq__all-toggle { border-color: var(--sms-btn-line); font-weight: 500; }
.sms-faq .sms-faq__search-label { font-weight: 500; }

.sms-quotes .sms-quotes__item { background: var(--sms-surface); box-shadow: inset 0 0 0 1px var(--sms-line); }
.sms-quotes .sms-quotes__icon { background: var(--sms-mint); color: var(--sms-accent); }
.sms-quotes .sms-quotes__label { color: var(--sms-accent); font-weight: 500; }
.sms-quotes .sms-quotes__text { font-weight: 300; color: var(--sms-title); }

.sms-people .sms-people__person,
.sms-people.sms-tone-white .sms-people__person { background: var(--sms-surface); box-shadow: inset 0 0 0 1px var(--sms-line); }
.sms-people .sms-people__role { background: var(--sms-mint); color: var(--sms-ink); font-weight: 500; }
.sms-people .sms-people__name { font-weight: 500; color: var(--sms-title); }
.sms-people .sms-people__tags { color: var(--sms-accent); font-weight: 400; }
.sms-people .sms-people__shared { background: linear-gradient(135deg, rgba(130, 208, 110, 0.12), rgba(130, 208, 110, 0.02)); box-shadow: inset 0 0 0 1px var(--sms-line-green); color: var(--sms-ink); }
.sms-people .sms-people__shared-label { color: var(--sms-accent); font-weight: 500; }
.sms-people .sms-people__shared-title { font-weight: 500; }
.sms-people .sms-people__shared-text { color: var(--sms-ink-soft); }
.sms-people .sms-people__shared .sms-more__toggle { color: var(--sms-accent); }
.sms-people .sms-people__shared .sms-more__body { color: var(--sms-ink-soft); }

.sms-links .sms-links__link { background: var(--sms-surface); box-shadow: inset 0 0 0 1px var(--sms-line); color: var(--sms-ink); }
.sms-links .sms-links__link:hover { box-shadow: inset 0 0 0 1px var(--sms-line-green), 0 20px 50px rgba(0, 0, 0, 0.35); }
.sms-links .sms-links__icon { background: var(--sms-mint); color: var(--sms-accent); }
.sms-links .sms-links__name { font-weight: 500; }
.sms-links .sms-links__go { color: var(--sms-accent); font-weight: 500; }

.sms-claim .sms-claim__icon,
.sms-claim.sms-tone-pale .sms-claim__icon { background: var(--sms-mint); color: var(--sms-accent); }
.sms-claim .sms-claim__text { font-weight: 300; color: var(--sms-title); }

.sms-marquee .sms-marquee__item,
.sms-marquee.sms-tone-white .sms-marquee__item { background: var(--sms-surface); box-shadow: inset 0 0 0 1px var(--sms-line); font-weight: 400; }
.sms-marquee .sms-marquee__icon { color: var(--sms-accent); }

.sms-contact .sms-contact__detail { background: var(--sms-surface); box-shadow: inset 0 0 0 1px var(--sms-line); }
.sms-contact .sms-contact__icon { background: var(--sms-mint); color: var(--sms-accent); }
.sms-contact .sms-contact__value { color: var(--sms-title); font-weight: 500; }
.sms-contact .sms-contact__value:hover { color: var(--sms-accent); }
.sms-contact .sms-contact__label { font-weight: 500; }
.sms-contact .sms-contact__form { background: var(--sms-surface); box-shadow: inset 0 0 0 1px var(--sms-line), var(--sms-shadow-lg); }
.sms-contact .sms-contact__form-title { font-weight: 500; }
.sms-contact .sms-contact__booklink { background: var(--sms-mint); box-shadow: inset 0 0 0 1px var(--sms-line-green); }
.sms-contact .sms-contact__booklink a { color: var(--sms-accent); }
.sms-contact .sms-contact__field-label { font-weight: 500; }
.sms-contact .sms-contact__status { color: var(--sms-accent); }

/* Booking demo */
.sms-booking .sms-booking__step-title { color: var(--sms-title); font-weight: 300; letter-spacing: -0.02em; }
.sms-booking .sms-booking__summary-title,
.sms-booking .sms-booking__help-title { font-weight: 500; }
.sms-booking .sms-booking__summary { background: linear-gradient(160deg, rgba(130, 208, 110, 0.12), rgba(130, 208, 110, 0.02)); box-shadow: inset 0 0 0 1px var(--sms-line-green); color: var(--sms-ink); }
.sms-booking .sms-booking__summary-icon,
.sms-booking .sms-booking__summary-list dt { color: var(--sms-accent); }
.sms-booking .sms-booking__input.is-invalid { border-color: var(--sms-error); box-shadow: 0 0 0 3px rgba(255, 138, 128, 0.16); }
.sms-booking .sms-booking__error { color: var(--sms-error); }
.sms-booking .sms-booking__soon { background: rgba(255, 200, 90, 0.1); box-shadow: inset 0 0 0 1px rgba(255, 200, 90, 0.3); }
.sms-booking .sms-booking__soon-icon { color: var(--sms-warn); }
.sms-booking .sms-booking__soon a { color: var(--sms-warn); }

/* Footer */
.sms-footer { border-top: 1px solid var(--sms-line); background: var(--sms-footer-bg); color: var(--sms-ink-soft); }
.sms-footer .sms-footer__heading { color: var(--sms-ink); font-weight: 600; letter-spacing: 0.22em; }
.sms-footer .sms-footer__tag { color: var(--sms-ink); font-weight: 400; }
.sms-footer .sms-footer__link { color: var(--sms-ink-soft); }
.sms-footer .sms-footer__link:hover { color: var(--sms-accent); }
.sms-footer .sms-footer__base { border-color: var(--sms-line); }

/* Shared helpers for the dark concepts' own sections */
.sms-page .sms-kicker { display: inline-flex; align-items: center; gap: 0.75rem; min-width: 0; margin: 0 0 1.25rem; color: var(--sms-accent); font-size: var(--sms-step--1); font-weight: 500; letter-spacing: 0.22em; text-transform: uppercase; }
.sms-page .sms-kicker::before { content: ""; flex: 0 0 auto; width: 0.45rem; height: 0.45rem; border-radius: 50%; background: var(--sms-accent); box-shadow: 0 0 12px var(--sms-glow); }
.sms-page .sms-arrowlink { display: inline-flex; align-items: center; gap: 0.6rem; min-width: 0; color: var(--sms-accent); font-weight: 500; text-underline-offset: 6px; }
.sms-page .sms-arrowlink .sms-arrow { text-decoration: none; }
.sms-page .sms-pill { display: inline-flex; align-items: center; min-width: 0; padding: 0.4rem 0.9rem; border-radius: 999px; box-shadow: inset 0 0 0 1px var(--sms-line); color: var(--sms-ink-soft); font-size: var(--sms-step--1); font-weight: 400; }
.sms-page .sms-pills { display: flex; flex-wrap: wrap; gap: 0.5rem; margin: 0; padding: 0; list-style: none; }
.sms-page .sms-pills__item { min-width: 0; }
.sms-page .sms-caption { margin: 0.9rem 0 0; color: var(--sms-ink-soft); font-size: 0.8125rem; }

/* Segmented control built from radio inputs (works without JavaScript) */
.sms-page .sms-seg { display: inline-flex; flex-wrap: wrap; gap: 0.25rem; min-width: 0; margin: 0 0 1rem; padding: 0.3rem; border-radius: 999px; background: var(--sms-pale-2); box-shadow: inset 0 0 0 1px var(--sms-line); }
.sms-page .sms-seg__label { display: inline-flex; align-items: center; min-width: 0; padding: 0.55rem 1.1rem; border-radius: 999px; color: var(--sms-ink-soft); cursor: pointer; font-size: var(--sms-step--1); font-weight: 500; transition: background-color 0.3s, color 0.3s; }
.sms-page .sms-seg__label:hover { color: var(--sms-title); }
.sms-page .sms-seg__radio { position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0); clip-path: inset(50%); white-space: nowrap; }
"""

REVEAL = []
TRANS = [".sms-page .sms-seg__label"]


def seg(name, labels, checked=0, legend=""):
    """Radio-driven segmented control. Returns (radios, labels) HTML: put the radios
    directly inside the component root, before everything they switch, and the
    labels anywhere inside it. Pair with seg_css()."""
    radios = "".join('<input class="sms-seg__radio sms-%s__r%d" type="radio" name="sms-%s" id="sms-%s-%d"%s>' % (
        name, i, name, name, i, " checked" if i == checked else "") for i in range(len(labels)))
    labs = "".join('<label class="sms-seg__label sms-%s__l%d" for="sms-%s-%d">%s</label>' % (name, i, name, i, l) for i, l in enumerate(labels))
    aria = ' role="group" aria-label="%s"' % legend if legend else ""
    return radios, '<div class="sms-seg"%s>%s</div>' % (aria, labs)


def seg_css(root, name, n, panel=None, show="display: block;", hide="display: none;"):
    """CSS for seg(): checked label style, focus ring and (optionally) which panel shows.
    `root` is the section root class, `panel` a class suffix numbered 0..n-1."""
    out = []
    for i in range(n):
        r = "%s .sms-%s__r%d" % (root, name, i)
        out.append("%s:checked ~ * .sms-%s__l%d,\n%s:checked ~ .sms-seg .sms-%s__l%d { background: var(--sms-seg-on-bg); color: var(--sms-seg-on-fg); }" % (r, name, i, r, name, i))
        out.append("%s:focus-visible ~ * .sms-%s__l%d,\n%s:focus-visible ~ .sms-seg .sms-%s__l%d { outline: 3px solid var(--sms-accent); outline-offset: 2px; }" % (r, name, i, r, name, i))
        if panel:
            out.append("%s:checked ~ * .%s%d,\n%s:checked ~ .%s%d { %s }" % (r, panel, i, r, panel, i, show))
    if panel:
        out.insert(0, ", ".join("%s .%s%d" % (root, panel, i) for i in range(n)) + " { %s }" % hide)
    return "\n".join(out) + "\n"
