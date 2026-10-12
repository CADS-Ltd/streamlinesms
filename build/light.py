"""Light theme for concepts 7-9: the layouts and motion of concepts 4-6 in
Streamline's original colour scheme (white and pale-green sections, navy text,
brand green #407F36), with navy "islands" where the live site uses navy: photo
heroes, diagram screens, call-to-action panels and the footer.

Goes after a dark concept's CSS, so these token values win. dark.CSS still
supplies the structure (it is token-driven).
"""

LIGHT = """
  --sms-bg: #ffffff;
  --sms-surface: #ffffff;
  --sms-pale: #f4f8f3;
  --sms-pale-2: #eef7ec;
  --sms-mint: #dcefd6;
  --sms-ink: #061e35;
  --sms-ink-soft: #405365;
  --sms-line: #d9e2e7;
  --sms-line-green: #c5dcc0;
  --sms-accent: #407f36;
  --sms-title: #061e35;
  --sms-on-accent: #ffffff;
  --sms-field: #ffffff;
  --sms-field-line: #8a99a6;
  --sms-glow: rgba(64, 127, 54, 0.3);
  --sms-header-bg: rgba(255, 255, 255, 0.92);
  --sms-card-pale: #ffffff;
  --sms-footer-bg: #061e35;
  --sms-seg-on-bg: #061e35;
  --sms-seg-on-fg: #ffffff;
  --sms-btn-line: rgba(6, 30, 53, 0.35);
  --sms-error: #b3261e;
  --sms-warn: #8a5a00;
  --sms-hair: rgba(6, 30, 53, 0.05);
  --sms-ring-line: rgba(6, 30, 53, 0.3);
  --sms-shade: 6, 30, 53;
  --sms-shadow: 0 0 0 1px var(--sms-line);
  --sms-shadow-lg: 0 24px 60px rgba(6, 30, 53, 0.12);
"""

# Brand navy, used for the islands (photo heroes, panels, footer)
ISLAND = """
  --sms-bg: #061e35;
  --sms-surface: #0b2a47;
  --sms-pale: #082540;
  --sms-pale-2: rgba(255, 255, 255, 0.07);
  --sms-mint: rgba(130, 208, 110, 0.14);
  --sms-ink: #eef3f7;
  --sms-ink-soft: #b9c7d4;
  --sms-line: rgba(180, 205, 228, 0.2);
  --sms-line-green: rgba(130, 208, 110, 0.3);
  --sms-accent: #82d06e;
  --sms-title: #ffffff;
  --sms-on-accent: #04121f;
  --sms-field: #071d33;
  --sms-field-line: rgba(180, 205, 228, 0.4);
  --sms-glow: rgba(130, 208, 110, 0.35);
  --sms-card-pale: #0d2f4f;
  --sms-seg-on-bg: #f2f6f9;
  --sms-seg-on-fg: #04121f;
  --sms-btn-line: rgba(238, 243, 247, 0.35);
  --sms-error: #ff9e96;
  --sms-warn: #ffcf66;
  --sms-hair: rgba(255, 255, 255, 0.05);
  --sms-ring-line: rgba(255, 255, 255, 0.35);
  --sms-shade: 6, 30, 53;
  color: var(--sms-ink);
"""

BASE = r"""
/* ===== Light theme: original Streamline colours ===== */
.sms-page {""" + LIGHT + """  font-weight: 400;
  color-scheme: light;
}
.sms-page ::selection { background: var(--sms-accent); color: #ffffff; }
.sms-page .sms-btn--primary { border-color: var(--sms-accent); background: var(--sms-accent); color: var(--sms-on-accent); }
.sms-feature .sms-watermark,
.sms-cards .sms-watermark,
.sms-steps .sms-watermark,
.sms-quotes .sms-watermark,
.sms-people .sms-watermark,
.sms-claim .sms-watermark,
.sms-checklist .sms-watermark { opacity: 0.06; filter: none; }
.sms-cards .sms-cards__item,
.sms-links .sms-links__link,
.sms-faq .sms-faq__item,
.sms-contact .sms-contact__form { box-shadow: inset 0 0 0 1px var(--sms-line), 0 10px 30px rgba(6, 30, 53, 0.05); }
.sms-contact .sms-contact__booklink a { color: var(--sms-ink); }
.sms-cards .sms-cards__item:hover,
.sms-links .sms-links__link:hover { box-shadow: inset 0 0 0 1px var(--sms-line-green), 0 20px 50px rgba(6, 30, 53, 0.1); }
"""


def css(islands):
    """Light tokens plus navy islands for the given section selectors."""
    return BASE + ",\n".join(islands) + " {" + ISLAND + "}\n"
