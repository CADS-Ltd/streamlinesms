"""Build every concept page.

    python3 build/build.py

Writes concept-N.html (homepages) at the repo root and concept-N/<page>.html
for the inner pages. Output is pure ASCII with inline CSS/JS per page.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..")
sys.path.insert(0, HERE)

import common as K  # noqa: E402
import content as C  # noqa: E402
import booking  # noqa: E402
import importlib  # noqa: E402

CONCEPTS = {}
for _n in (1, 2, 3):
    try:
        CONCEPTS[_n] = importlib.import_module("concept%d" % _n)
    except ImportError:
        pass


def render(n, mod, slug):
    ctx = K.Ctx(n, slug)
    css = K.BASE_CSS + booking.CSS + mod.CSS + K.motion_css(mod.REVEAL, mod.RISE, mod.ENTRANCE, mod.LOOP, mod.TRANS + booking.TRANS, booking.ANIM + getattr(mod, 'OPEN', []))
    if slug == "home":
        title = "Streamline Safety & Medical Solutions | Concept %d" % n
        desc = "Clinician-led event medical cover, first aid training and safety consultancy, based in Swadlincote and working across Derbyshire, Nottinghamshire, Leicestershire, Staffordshire and beyond"
        main = mod.home(ctx)
    else:
        page = C.PAGES[slug]
        title = "%s | Streamline Safety & Medical Solutions | Concept %d" % (page["doc"], n)
        desc = page["desc"]
        main = mod.page_hero(ctx, page["hero"])
        for kind, data in page["sections"]:
            main += booking.render(ctx, data) if kind == "booking" else K.SHARED_RENDERERS[kind](ctx, data)
        if page.get("cta"):
            main += mod.cta(ctx, page["cta"])
        ctx.notes += ["Image-only copy used: " + t for t in page.get("image_text", [])]
        if slug == "book":
            ctx.notes.append("Booking form is an interactive demo: nothing is sent or stored")
    body = '<body class="sms-page">\n<a class="sms-skip" href="#main">Skip to content</a>\n'
    body += mod.chrome_top(ctx)
    body += '<main id="main">\n' + main + '</main>\n'
    body += mod.chrome_bottom(ctx)
    if 'data-sms-form' in main:
        body += K.FORM_JS
    if 'data-sms-faq-search' in main:
        body += K.FAQ_JS
    if 'data-sms-booking' in main:
        body += booking.JS
    body += getattr(mod, "scripts", lambda c, m: "")(ctx, main)
    body += "</body>\n</html>\n"
    doc = K.head(ctx, title, desc, css) + body
    doc = doc.replace("%%COMMENT%%", K.comment(n, mod.NAME, slug, ctx))
    return K.ascii_html(doc)


def main():
    count = 0
    for n, mod in CONCEPTS.items():
        os.makedirs(os.path.join(ROOT, "concept-%d" % n), exist_ok=True)
        for slug in ["home"] + [s for s, _ in K.PAGES]:
            out = os.path.join(ROOT, "concept-%d.html" % n) if slug == "home" else os.path.join(ROOT, "concept-%d" % n, slug + ".html")
            with open(out, "w", encoding="ascii", newline="\n") as f:
                f.write(render(n, mod, slug))
            count += 1
    print("wrote", count, "pages")


if __name__ == "__main__":
    main()


INDEX_DESC = {
    1: ("Editorial split", "White and airy with soft mint shapes. Big rounded photos with floating badges, a zig-zag of services with photos, and gentle motion as you scroll."),
    2: ("Centred statement", "Light and friendly. Centred pale-green heroes with a photo collage, photo service cards, rounded everything, green call-to-action bands and a light footer."),
    3: ("Bold brand", "The most branded option. Green top bar, split photo heroes with boxed navy and green headlines, angled brand shapes, booking panels and tabbed services with photos."),
}


def build_index():
    rows = ""
    for n in CONCEPTS:
        name, desc = INDEX_DESC[n]
        links = '<li class="sms-index__page"><a class="sms-index__page-link" href="concept-%d.html">Home</a></li>' % n
        links += "".join('<li class="sms-index__page"><a class="sms-index__page-link" href="concept-%d/%s.html">%s</a></li>' % (n, s, K.e(l)) for s, l in K.PAGES)
        rows += """<li class="sms-index__item">
        <div class="sms-index__num">%02d</div>
        <div class="sms-index__body">
          <h2 class="sms-index__name"><a class="sms-index__name-link" href="concept-%d.html">Concept %d: %s</a></h2>
          <div class="sms-index__desc"><p>%s</p></div>
          <ul class="sms-index__pages">%s</ul>
        </div>
      </li>""" % (n, n, n, name, K.e(desc), links)
    doc = """<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>Streamline Safety &amp; Medical Solutions | Website concepts</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700&amp;display=swap">
<style>
.sms-page { --sms-navy: #061e35; --sms-green: #407f36; --sms-pale: #f4f8f3; --sms-white: #ffffff; --sms-ink-soft: #405365; --sms-line: #d9e2e7; margin: 0; background: var(--sms-white); color: var(--sms-navy); font-family: "Montserrat", Arial, sans-serif; font-size: clamp(1rem, 0.96rem + 0.2vw, 1.0625rem); line-height: 1.6; }
.sms-page *,
.sms-page *::before,
.sms-page *::after { box-sizing: border-box; }
.sms-page a:focus-visible { outline: 3px solid var(--sms-green); outline-offset: 3px; }
.sms-index .sms-index__inner { width: 100%%; max-width: 56rem; margin: 0 auto; padding: clamp(3rem, 2rem + 4vw, 6rem) clamp(1rem, 0.6rem + 2vw, 2.5rem); }
.sms-index .sms-index__logo { display: block; width: clamp(11rem, 9rem + 6vw, 14rem); height: auto; margin-bottom: 2.5rem; }
.sms-index .sms-index__title { margin: 0 0 0.75rem; font-size: clamp(1.75rem, 1.4rem + 1.5vw, 2.5rem); font-weight: 700; line-height: 1.2; }
.sms-index .sms-index__intro { margin-bottom: 2.5rem; color: var(--sms-ink-soft); }
.sms-index .sms-index__intro p { margin: 0 0 0.75rem; }
.sms-index .sms-index__list { margin: 0; padding: 0; border-top: 1px solid var(--sms-line); list-style: none; }
.sms-index .sms-index__item { display: grid; grid-template-columns: 3rem minmax(0, 1fr); gap: 0.25rem 1rem; padding: 1.75rem 0; border-bottom: 1px solid var(--sms-line); }
.sms-index .sms-index__num { min-width: 0; color: var(--sms-green); font-weight: 700; }
.sms-index .sms-index__body { min-width: 0; }
.sms-index .sms-index__name { margin: 0 0 0.35rem; font-size: clamp(1.125rem, 1.06rem + 0.3vw, 1.3125rem); font-weight: 700; }
.sms-index .sms-index__name-link { color: var(--sms-navy); }
.sms-index .sms-index__name-link:hover { color: var(--sms-green); }
.sms-index .sms-index__desc { margin-bottom: 0.9rem; color: var(--sms-ink-soft); }
.sms-index .sms-index__desc p { margin: 0; }
.sms-index .sms-index__pages { display: flex; flex-wrap: wrap; gap: 0.5rem; margin: 0; padding: 0; list-style: none; }
.sms-index .sms-index__page { min-width: 0; }
.sms-index .sms-index__page-link { display: inline-block; padding: 0.3rem 0.75rem; border: 1px solid var(--sms-line); border-radius: 999px; color: var(--sms-navy); font-size: 0.875rem; font-weight: 600; text-decoration: none; }
.sms-index .sms-index__page-link:hover { border-color: var(--sms-green); color: var(--sms-green); }
.sms-index .sms-index__note { margin-top: 2.5rem; color: var(--sms-ink-soft); font-size: 0.875rem; }
.sms-index .sms-index__note p { margin: 0; }
</style>
</head>
<body class="sms-page">
<main class="sms-index">
  <div class="sms-index__inner">
    <img class="sms-index__logo" src="assets/streamline-s-m-sol-logo-blue-long.png" alt="Streamline Safety &amp; Medical Solutions" width="2500" height="443">
    <h1 class="sms-index__title">Website concepts</h1>
    <div class="sms-index__intro"><p>Three directions for the new Streamline Safety &amp; Medical Solutions website, each shown across all nine pages. The logo, colours and wording are the same in all three; the layout and how strongly the brand comes through are what change.</p><p>Every concept includes an interactive booking form demo (Book Online). Photos are the client&rsquo;s own images from the current site, used for the concepts only.</p></div>
    <ul class="sms-index__list">%s</ul>
    <div class="sms-index__note"><p>Pitch concepts by CADS. Not for indexing.</p></div>
  </div>
</main>
</body>
</html>
""" % rows
    with open(os.path.join(ROOT, "index.html"), "w", encoding="ascii", newline="\n") as f:
        f.write(K.ascii_html(doc))


if __name__ == "__main__":
    build_index()
