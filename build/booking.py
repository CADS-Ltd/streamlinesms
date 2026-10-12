"""Interactive booking request form (demo).

Without JavaScript it is one long form with every section visible. With
JavaScript it becomes a four-step wizard: choose a service, tell us about it,
your details, review and send. Nothing is sent anywhere - the last step shows a
demo confirmation. Field choices come from the live site (the "What information
is needed for a quote?" FAQ, the course list, the consultancy services and the
career support areas).
"""
from common import e, icon, PHONE, PHONE_TEL, EMAIL
import content as C

EVENT_TYPES = ["Community event, village fete or charity event", "Business showcase or corporate event", "Sports or combat-sports event",
               "School event or private function", "Small festival or outdoor activity", "Something else"]
COURSES = ["Emergency First Aid at Work", "First Aid at Work", "First Aid at Work requalification", "Paediatric First Aid",
           "CPR, AED and basic life support", "FREC 3", "FREC 4", "Bespoke Course"]
CONSULT = ["First Aid Needs Assessment", "Risk Assessment Writing", "Gap Assessment", "Event Medical Plans",
           "Safe System of Work (SSoW) Advice", "Fire Safety Assessment", "Not sure yet"]
INDUSTRIES = ["Office", "Retail", "Warehousing", "Construction", "Manufacturing", "Hospitality", "Education", "Care",
              "Community organisation", "Sports, leisure or events", "Something else"]
ROLES = ["Event medic", "Ambulance Care Assistant", "Emergency Care Assistant", "Ambulance Technician", "Associate Ambulance Practitioner",
         "Student paramedic", "Paramedic", "Not sure yet"]
SUPPORT = ["Interview preparation", "Mock assessments", "Feedback & development", "Career direction"]

SERVICE_OPTIONS = [
    ("event", "heart", "Event Medical Cover", "Medical cover for your event, from small local events to large-scale public gatherings."),
    ("training", "cap", "Medical Training", "First aid and pre-hospital training for you or your team."),
    ("consultancy", "clipboard", "Risk & Needs Consultancy", "A free initial consultation about your workplace, event or organisation."),
    ("careers", "compass", "Pre-Hospital Career Support", "Interview preparation, mock assessments and honest feedback."),
]


def _opts(items, placeholder="Please choose"):
    return '<option value="">%s</option>' % placeholder + "".join('<option>%s</option>' % e(i) for i in items)


def _chipset(name, items, label):
    return ('<fieldset class="sms-booking__group"><legend class="sms-booking__label">%s</legend><div class="sms-booking__chips">%s</div></fieldset>' % (
        label, "".join('<label class="sms-booking__chip"><input class="sms-booking__chip-input" type="checkbox" name="%s" value="%s" data-label="%s"><span class="sms-booking__chip-text">%s%s</span></label>' % (
            name, e(i), label, icon("check", "sms-booking__chip-icon"), e(i)) for i in items)))


def _field(id_, label, control, hint="", cls=""):
    h = '<span class="sms-booking__hint" id="%s-hint">%s</span>' % (id_, hint) if hint else ""
    return '<div class="sms-booking__field%s"><label class="sms-booking__label" for="%s">%s</label>%s%s<span class="sms-booking__error" data-error-for="%s"></span></div>' % (
        (" " + cls) if cls else "", id_, label, h, control, id_)


def render(ctx, d):
    svc = "".join("""<label class="sms-booking__service">
          <input class="sms-booking__service-input" type="radio" name="service" value="%s" data-label="Service" data-name="%s" required>
          <span class="sms-booking__service-card">
            %s
            <span class="sms-booking__service-name">%s</span>
            <span class="sms-booking__service-text">%s</span>
            %s
          </span>
        </label>""" % (k, e(t), icon(ic, "sms-booking__service-icon"), e(t), e(x), icon("check", "sms-booking__service-tick")) for k, ic, t, x in SERVICE_OPTIONS)

    event = """<fieldset class="sms-booking__step" data-step="2" data-service="event">
      <legend class="sms-booking__step-title">Tell us about your event</legend>
      <p class="sms-booking__step-text">This is the information we need for a quote. If you are not sure of something yet, leave it blank.</p>
      <div class="sms-booking__grid">
        %s
        %s
        %s
        %s
        %s
      </div>
      <div class="sms-booking__soon" data-sms-soon hidden>
        %s
        <div class="sms-booking__soon-text"><strong>Your event is less than a month away.</strong> For an event within one month, contact us directly as well as submitting any online enquiry. <a href="tel:%s">Call %s</a></div>
      </div>
      <div class="sms-booking__field sms-booking__field--wide">
        <label class="sms-booking__label" for="bk-attendance">Expected attendance: <output class="sms-booking__output" for="bk-attendance" data-sms-output>500</output></label>
        <input class="sms-booking__range" id="bk-attendance" name="attendance" type="range" min="50" max="10000" step="50" value="500" data-label="Expected attendance">
        <span class="sms-booking__range-scale" aria-hidden="true"><span>50</span><span>10,000+</span></span>
      </div>
      <div class="sms-booking__grid">
        %s
        <fieldset class="sms-booking__group"><legend class="sms-booking__label">Will alcohol be available?</legend>
          <div class="sms-booking__toggle">
            <label class="sms-booking__toggle-opt"><input type="radio" name="alcohol" value="Yes" data-label="Alcohol available"><span>Yes</span></label>
            <label class="sms-booking__toggle-opt"><input type="radio" name="alcohol" value="No" data-label="Alcohol available"><span>No</span></label>
            <label class="sms-booking__toggle-opt"><input type="radio" name="alcohol" value="Not sure yet" data-label="Alcohol available"><span>Not sure</span></label>
          </div>
        </fieldset>
      </div>
      %s
      %s
    </fieldset>""" % (
        _field("bk-event-type", "Event type", '<select class="sms-booking__input" id="bk-event-type" name="event_type" data-label="Event type" required>%s</select>' % _opts(EVENT_TYPES)),
        _field("bk-event-date", "Event date", '<input class="sms-booking__input" id="bk-event-date" name="event_date" type="date" data-label="Event date" required>'),
        _field("bk-venue", "Venue and postcode", '<input class="sms-booking__input" id="bk-venue" name="venue" type="text" autocomplete="off" data-label="Venue and postcode" required placeholder="e.g. Village green, DE11">'),
        _field("bk-start", "Start time", '<input class="sms-booking__input" id="bk-start" name="start" type="time" data-label="Start time">'),
        _field("bk-end", "Finish time", '<input class="sms-booking__input" id="bk-end" name="end" type="time" data-label="Finish time">'),
        icon("alert", "sms-booking__soon-icon"), PHONE_TEL, PHONE,
        _field("bk-age", "Age range of attendees", '<select class="sms-booking__input" id="bk-age" name="age" data-label="Age range">%s</select>' % _opts(["Mostly adults", "Mixed ages, including children", "Mostly children and young people"])),
        _chipset("event_docs", ["Risk assessment", "Site plan", "Emergency access plan", "Existing medical provision"], "Do you already have any of these?"),
        _field("bk-event-notes", "Activities, previous incidents or venue requirements", '<textarea class="sms-booking__input sms-booking__input--area" id="bk-event-notes" name="event_notes" data-label="Event notes"></textarea>', cls="sms-booking__field--wide"),
    )

    training = """<fieldset class="sms-booking__step" data-step="2" data-service="training">
      <legend class="sms-booking__step-title">Which training are you interested in?</legend>
      <p class="sms-booking__step-text">We can deliver training at your venue or arrange a suitable training location for your group.</p>
      <div class="sms-booking__grid">
        %s
        <div class="sms-booking__field">
          <label class="sms-booking__label" for="bk-learners">Number of learners</label>
          <div class="sms-booking__stepper">
            <button class="sms-booking__step-btn" type="button" data-sms-step="-1" data-sms-wizard-only hidden aria-label="One fewer learner">%s</button>
            <input class="sms-booking__input sms-booking__input--num" id="bk-learners" name="learners" type="number" min="1" max="99" value="4" inputmode="numeric" data-label="Number of learners">
            <button class="sms-booking__step-btn" type="button" data-sms-step="1" data-sms-wizard-only hidden aria-label="One more learner">%s</button>
          </div>
        </div>
        %s
      </div>
      <fieldset class="sms-booking__group"><legend class="sms-booking__label">Where should the training take place?</legend>
        <div class="sms-booking__toggle">
          <label class="sms-booking__toggle-opt"><input type="radio" name="location" value="At our venue" data-label="Training location" checked><span>At our venue</span></label>
          <label class="sms-booking__toggle-opt"><input type="radio" name="location" value="A location Streamline arranges" data-label="Training location"><span>A location you arrange</span></label>
          <label class="sms-booking__toggle-opt"><input type="radio" name="location" value="Open course (register interest)" data-label="Training location"><span>Open course</span></label>
        </div>
      </fieldset>
      <div class="sms-booking__reveal" data-sms-bespoke hidden>
        %s
      </div>
      <p class="sms-booking__aside-note">%s No public courses are currently scheduled, so open course requests register your interest and we will let you know when new dates are released.</p>
    </fieldset>""" % (
        _field("bk-course", "Course", '<select class="sms-booking__input" id="bk-course" name="course" data-label="Course" required>%s</select>' % _opts(COURSES)),
        icon("minus"), icon("plus"),
        _field("bk-train-date", "Preferred date", '<input class="sms-booking__input" id="bk-train-date" name="train_date" type="date" data-label="Preferred date">'),
        _field("bk-bespoke", "What would you like the training to cover?", '<textarea class="sms-booking__input sms-booking__input--area" id="bk-bespoke" name="bespoke" data-label="Bespoke topics"></textarea>', hint="For example falls awareness, head injuries, anaphylaxis or a scenario around your workplace risks.", cls="sms-booking__field--wide"),
        icon("calendar", "sms-booking__note-icon"),
    )

    consult = """<fieldset class="sms-booking__step" data-step="2" data-service="consultancy">
      <legend class="sms-booking__step-title">Your free initial consultation</legend>
      <p class="sms-booking__step-text">At this stage, you do not need to know exactly what service you require.</p>
      %s
      <div class="sms-booking__grid">
        %s
        %s
      </div>
      %s
    </fieldset>""" % (
        _chipset("consult", CONSULT, "What would you like help with?"),
        _field("bk-industry", "Type of business, site or event", '<select class="sms-booking__input" id="bk-industry" name="industry" data-label="Type of business" required>%s</select>' % _opts(INDUSTRIES)),
        _field("bk-people", "Number of staff, visitors or attendees", '<select class="sms-booking__input" id="bk-people" name="people" data-label="People involved">%s</select>' % _opts(["Fewer than 10", "10 to 49", "50 to 249", "250 or more"])),
        _field("bk-concerns", "Any concerns around compliance, staffing, equipment or emergency response?", '<textarea class="sms-booking__input sms-booking__input--area" id="bk-concerns" name="concerns" data-label="Concerns"></textarea>', cls="sms-booking__field--wide"),
    )

    careers = """<fieldset class="sms-booking__step" data-step="2" data-service="careers">
      <legend class="sms-booking__step-title">Tell us your goal</legend>
      <p class="sms-booking__step-text">Tell us about your experience, the role you have in mind and any upcoming interview or assessment.</p>
      <div class="sms-booking__grid">
        %s
        %s
      </div>
      %s
      %s
    </fieldset>""" % (
        _field("bk-role", "Role you have in mind", '<select class="sms-booking__input" id="bk-role" name="role" data-label="Role" required>%s</select>' % _opts(ROLES)),
        _field("bk-interview", "Upcoming interview or assessment date", '<input class="sms-booking__input" id="bk-interview" name="interview" type="date" data-label="Interview date">'),
        _chipset("support", SUPPORT, "What support would you like?"),
        _field("bk-position", "Your current position", '<textarea class="sms-booking__input sms-booking__input--area" id="bk-position" name="position" data-label="Current position"></textarea>', cls="sms-booking__field--wide"),
    )

    details = """<fieldset class="sms-booking__step" data-step="3">
      <legend class="sms-booking__step-title">Your details</legend>
      <p class="sms-booking__step-text">So the team can get back to you about your request.</p>
      <div class="sms-booking__grid">
        %s
        %s
        %s
        %s
      </div>
      <fieldset class="sms-booking__group"><legend class="sms-booking__label">How should we contact you?</legend>
        <div class="sms-booking__toggle">
          <label class="sms-booking__toggle-opt"><input type="radio" name="contact_pref" value="Email" data-label="Contact by" checked><span>%s Email</span></label>
          <label class="sms-booking__toggle-opt"><input type="radio" name="contact_pref" value="Phone" data-label="Contact by"><span>%s Phone</span></label>
        </div>
      </fieldset>
    </fieldset>""" % (
        _field("bk-name", "Your name", '<input class="sms-booking__input" id="bk-name" name="name" type="text" autocomplete="name" data-label="Name" required>'),
        _field("bk-org", "Organisation (optional)", '<input class="sms-booking__input" id="bk-org" name="org" type="text" autocomplete="organization" data-label="Organisation">'),
        _field("bk-email", "Email", '<input class="sms-booking__input" id="bk-email" name="email" type="email" autocomplete="email" data-label="Email" required>'),
        _field("bk-phone", "Telephone", '<input class="sms-booking__input" id="bk-phone" name="phone" type="tel" autocomplete="tel" data-label="Telephone" required>'),
        icon("mail", "sms-booking__toggle-icon"), icon("phone", "sms-booking__toggle-icon"),
    )

    review = """<fieldset class="sms-booking__step" data-step="4">
      <legend class="sms-booking__step-title">Check and send</legend>
      <p class="sms-booking__step-text">Our quotation and plan are based on the information provided, so please check everything looks right.</p>
      <dl class="sms-booking__review" data-sms-review hidden></dl>
      <label class="sms-booking__consent"><input class="sms-booking__consent-input" type="checkbox" name="consent" required data-label="Consent"><span>I understand this is a request: a booking is confirmed once Streamline has accepted it and the relevant requirements have been completed.</span></label>
      <span class="sms-booking__error" data-error-for="consent"></span>
    </fieldset>"""

    steps_nav = "".join('<li class="sms-booking__progress-step" data-sms-progress="%d"><span class="sms-booking__progress-dot">%s<span class="sms-booking__progress-num">%d</span></span><span class="sms-booking__progress-label">%s</span></li>' % (
        i, icon("check", "sms-booking__progress-tick"), i, l) for i, l in enumerate(["Service", "Details", "Your details", "Send"], 1))

    return """<section class="sms-booking" id="booking">
  <div class="sms-booking__inner">
    <form class="sms-booking__form" action="#" method="post" novalidate data-sms-booking>
      <div class="sms-booking__top" data-sms-wizard-only hidden>
        <ol class="sms-booking__progress">%s</ol>
        <div class="sms-booking__bar" aria-hidden="true"><span class="sms-booking__bar-fill" data-sms-bar></span></div>
        <p class="sms-booking__status sms-visually-hidden" role="status" aria-live="polite" data-sms-status></p>
      </div>
      <fieldset class="sms-booking__step" data-step="1">
        <legend class="sms-booking__step-title">What would you like to book?</legend>
        <p class="sms-booking__step-text">Choose one to get started.</p>
        <div class="sms-booking__services">%s</div>
        <span class="sms-booking__error" data-error-for="service"></span>
      </fieldset>
      %s
      %s
      %s
      %s
      %s
      %s
      <div class="sms-booking__nav">
        <button class="sms-btn sms-btn--outline sms-booking__back" type="button" data-sms-back hidden>Back</button>
        <button class="sms-btn sms-btn--primary sms-booking__next" type="button" data-sms-next hidden>Continue&nbsp;<span class="sms-arrow" aria-hidden="true">&rarr;</span></button>
        <button class="sms-btn sms-btn--primary sms-booking__submit" type="submit" data-sms-submit disabled>Send booking request&nbsp;<span class="sms-arrow" aria-hidden="true">&rarr;</span></button>
      </div>
      <div class="sms-booking__done" data-sms-done hidden tabindex="-1">
        <div class="sms-booking__done-badge">%s</div>
        <h2 class="sms-booking__done-title">Request received (demo)</h2>
        <p class="sms-booking__done-text">This is a concept, so nothing has been sent. On the live site your request would go straight to the Streamline team and you would get a confirmation email.</p>
        <p class="sms-booking__done-ref">Reference <strong data-sms-ref>SMS-0000</strong></p>
        <button class="sms-btn sms-btn--outline" type="button" data-sms-restart>Start another request</button>
      </div>
    </form>
    <aside class="sms-booking__aside">
      <div class="sms-booking__summary" data-sms-wizard-only hidden>
        <div class="sms-booking__summary-title">%s Your request</div>
        <dl class="sms-booking__summary-list" data-sms-summary><dt>Service</dt><dd>Not chosen yet</dd></dl>
      </div>
      <div class="sms-booking__help">
        <div class="sms-booking__help-title">Prefer to talk?</div>
        <a class="sms-booking__help-link" href="tel:%s">%s %s</a>
        <a class="sms-booking__help-link" href="mailto:%s">%s %s</a>
      </div>
      <div class="sms-booking__demo">%s <span>Demo form for the concept: nothing is sent or stored.</span></div>
    </aside>
  </div>
</section>
""" % (steps_nav, svc, event, training, consult, careers, details, review, icon("check", "sms-booking__done-icon"),
       icon("clipboard", "sms-booking__summary-icon"), PHONE_TEL, icon("phone", "sms-booking__help-icon"), PHONE, EMAIL, icon("mail", "sms-booking__help-icon"), EMAIL,
       icon("shield", "sms-booking__demo-icon"))


CSS = r"""
/* ---------- Booking wizard ---------- */
.sms-booking .sms-booking__inner { display: grid; gap: clamp(1.5rem, 1rem + 2vw, 2.5rem); align-items: start; }
.sms-booking .sms-booking__form { position: relative; min-width: 0; padding: clamp(1.25rem, 0.8rem + 2vw, 2.5rem); border-radius: var(--sms-radius); background: var(--sms-surface); box-shadow: var(--sms-shadow-lg); }
.sms-booking .sms-booking__top { min-width: 0; margin-bottom: 2rem; }
.sms-booking .sms-booking__top[hidden] { display: none; }
.sms-booking .sms-booking__progress { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 0.5rem; margin: 0 0 1rem; padding: 0; list-style: none; }
.sms-booking .sms-booking__progress-step { display: flex; flex-direction: column; align-items: center; gap: 0.4rem; min-width: 0; color: var(--sms-ink-soft); font-size: var(--sms-step--1); font-weight: 600; text-align: center; }
.sms-booking .sms-booking__progress-dot { position: relative; display: grid; place-items: center; width: 2.4rem; height: 2.4rem; border: 2px solid var(--sms-line); border-radius: 50%; background: var(--sms-surface); color: var(--sms-ink-soft); font-weight: 700; transition: transform 0.3s var(--sms-ease); }
.sms-booking .sms-booking__progress-tick { display: none; width: 1.2rem; height: 1.2rem; }
.sms-booking .sms-booking__progress-num { min-width: 0; }
.sms-booking .sms-booking__progress-label { min-width: 0; }
.sms-booking .sms-booking__progress-step.is-current { color: var(--sms-ink); }
.sms-booking .sms-booking__progress-step.is-current .sms-booking__progress-dot { border-color: var(--sms-green); color: var(--sms-accent); transform: scale(1.12); }
.sms-booking .sms-booking__progress-step.is-done .sms-booking__progress-dot { border-color: var(--sms-green); background: var(--sms-green); color: var(--sms-white); }
.sms-booking .sms-booking__progress-step.is-done .sms-booking__progress-tick { display: block; }
.sms-booking .sms-booking__progress-step.is-done .sms-booking__progress-num { display: none; }
.sms-booking .sms-booking__bar { height: 6px; overflow: hidden; border-radius: 6px; background: var(--sms-pale-2); }
.sms-booking .sms-booking__bar-fill { display: block; width: 100%; height: 100%; border-radius: 6px; background: var(--sms-green); transform: scaleX(0.25); transform-origin: left; transition: transform 0.5s var(--sms-ease); }
.sms-booking .sms-booking__step { min-width: 0; margin: 0 0 2rem; padding: 0; border: 0; }
.sms-booking .sms-booking__step[hidden] { display: none; }
.sms-booking .sms-booking__form.is-wizard .sms-booking__step:not([hidden]) { animation: sms-slide-in 0.45s var(--sms-ease) both; }
.sms-booking .sms-booking__step-title { margin: 0 0 0.35rem; padding: 0; font-size: var(--sms-step-2); font-weight: 700; line-height: 1.2; }
.sms-booking .sms-booking__step-text { margin: 0 0 1.5rem; color: var(--sms-ink-soft); }
.sms-booking .sms-booking__services { display: grid; gap: 0.85rem; }
.sms-booking .sms-booking__service { position: relative; display: block; min-width: 0; cursor: pointer; }
.sms-booking .sms-booking__service-input { position: absolute; opacity: 0; pointer-events: none; }
.sms-booking .sms-booking__service-card { position: relative; display: grid; grid-template-columns: auto minmax(0, 1fr); gap: 0.25rem 1rem; align-items: center; height: 100%; padding: 1.25rem 3rem 1.25rem 1.25rem; border: 2px solid var(--sms-line); border-radius: var(--sms-radius); background: var(--sms-surface); transition: transform 0.25s var(--sms-ease); }
.sms-booking .sms-booking__service:hover .sms-booking__service-card { transform: translateY(-3px); border-color: var(--sms-green); }
.sms-booking .sms-booking__service-icon { grid-row: span 2; width: 3rem; height: 3rem; padding: 0.7rem; border-radius: 1rem; background: var(--sms-mint); color: var(--sms-accent); }
.sms-booking .sms-booking__service-name { min-width: 0; font-weight: 700; }
.sms-booking .sms-booking__service-text { min-width: 0; color: var(--sms-ink-soft); font-size: var(--sms-step--1); line-height: 1.45; }
.sms-booking .sms-booking__service-tick { position: absolute; right: 1rem; top: 1rem; width: 1.5rem; height: 1.5rem; padding: 0.2rem; border-radius: 50%; background: var(--sms-green); color: var(--sms-white); opacity: 0; transform: scale(0.4); transition: transform 0.3s var(--sms-ease), opacity 0.3s var(--sms-ease); }
.sms-booking .sms-booking__service-input:checked + .sms-booking__service-card { border-color: var(--sms-green); background: var(--sms-pale-2); }
.sms-booking .sms-booking__service-input:checked + .sms-booking__service-card .sms-booking__service-tick { opacity: 1; transform: scale(1); }
.sms-booking .sms-booking__service-input:focus-visible + .sms-booking__service-card { outline: 3px solid var(--sms-green); outline-offset: 3px; }
.sms-booking .sms-booking__grid { display: grid; gap: 1rem 1.25rem; margin-bottom: 1rem; }
.sms-booking .sms-booking__field { display: grid; gap: 0.35rem; align-content: start; min-width: 0; margin-bottom: 1rem; }
.sms-booking .sms-booking__grid .sms-booking__field { margin-bottom: 0; }
.sms-booking .sms-booking__label { min-width: 0; padding: 0; font-size: var(--sms-step--1); font-weight: 700; }
.sms-booking .sms-booking__hint { min-width: 0; color: var(--sms-ink-soft); font-size: var(--sms-step--1); }
.sms-booking .sms-booking__input { width: 100%; min-width: 0; padding: 0.85rem 1rem; border: 1px solid var(--sms-field-line); border-radius: var(--sms-radius-sm); background: var(--sms-field); color: var(--sms-ink); font: inherit; }
.sms-booking .sms-booking__input--area { min-height: 6.5rem; resize: vertical; }
.sms-booking .sms-booking__input.is-invalid { border-color: #b3261e; box-shadow: 0 0 0 3px rgba(179, 38, 30, 0.12); }
.sms-booking .sms-booking__error { display: block; min-width: 0; min-height: 0; color: #b3261e; font-size: var(--sms-step--1); font-weight: 600; }
.sms-booking .sms-booking__group { min-width: 0; margin: 0 0 1rem; padding: 0; border: 0; }
.sms-booking .sms-booking__group .sms-booking__label { display: block; margin-bottom: 0.5rem; }
.sms-booking .sms-booking__chips { display: flex; flex-wrap: wrap; gap: 0.5rem; }
.sms-booking .sms-booking__chip { position: relative; min-width: 0; cursor: pointer; }
.sms-booking .sms-booking__chip-input { position: absolute; opacity: 0; pointer-events: none; }
.sms-booking .sms-booking__chip-text { display: inline-flex; align-items: center; gap: 0.35rem; padding: 0.55rem 0.95rem; border: 2px solid var(--sms-line); border-radius: 999px; background: var(--sms-surface); font-size: var(--sms-step--1); font-weight: 600; transition: transform 0.2s var(--sms-ease); }
.sms-booking .sms-booking__chip:hover .sms-booking__chip-text { transform: translateY(-2px); }
.sms-booking .sms-booking__chip-icon { display: none; width: 1rem; height: 1rem; }
.sms-booking .sms-booking__chip-input:checked + .sms-booking__chip-text { border-color: var(--sms-green); background: var(--sms-green); color: var(--sms-white); }
.sms-booking .sms-booking__chip-input:checked + .sms-booking__chip-text .sms-booking__chip-icon { display: inline-block; }
.sms-booking .sms-booking__chip-input:focus-visible + .sms-booking__chip-text { outline: 3px solid var(--sms-green); outline-offset: 2px; }
.sms-booking .sms-booking__toggle { display: inline-flex; flex-wrap: wrap; gap: 0.25rem; padding: 0.25rem; border-radius: 999px; background: var(--sms-pale-2); }
.sms-booking .sms-booking__toggle-opt { position: relative; min-width: 0; cursor: pointer; }
.sms-booking .sms-booking__toggle-opt input { position: absolute; opacity: 0; pointer-events: none; }
.sms-booking .sms-booking__toggle-opt span { display: inline-flex; align-items: center; gap: 0.35rem; padding: 0.55rem 1rem; border-radius: 999px; font-size: var(--sms-step--1); font-weight: 700; }
.sms-booking .sms-booking__toggle-opt input:checked + span { background: var(--sms-surface); color: var(--sms-accent); box-shadow: 0 4px 12px rgba(6, 30, 53, 0.1); }
.sms-booking .sms-booking__toggle-opt input:focus-visible + span { outline: 3px solid var(--sms-green); outline-offset: 2px; }
.sms-booking .sms-booking__toggle-icon { width: 1rem; height: 1rem; }
.sms-booking .sms-booking__output { color: var(--sms-accent); font-weight: 700; }
.sms-booking .sms-booking__range { width: 100%; min-width: 0; accent-color: var(--sms-green); }
.sms-booking .sms-booking__range-scale { display: flex; justify-content: space-between; color: var(--sms-ink-soft); font-size: 0.75rem; }
.sms-booking .sms-booking__stepper { display: flex; align-items: stretch; min-width: 0; border: 1px solid var(--sms-field-line); border-radius: var(--sms-radius-sm); overflow: hidden; }
.sms-booking .sms-booking__step-btn { display: grid; place-items: center; min-width: 0; width: 3rem; border: 0; background: var(--sms-pale-2); color: var(--sms-accent); cursor: pointer; }
.sms-booking .sms-booking__step-btn[hidden] { display: none; }
.sms-booking .sms-booking__input--num { border: 0; border-radius: 0; text-align: center; -moz-appearance: textfield; }
.sms-booking .sms-booking__soon { display: flex; gap: 0.75rem; min-width: 0; margin: 0 0 1.25rem; padding: 1rem 1.25rem; border-radius: var(--sms-radius-sm); background: #fff6e0; color: var(--sms-ink); font-size: var(--sms-step--1); }
.sms-booking .sms-booking__soon[hidden] { display: none; }
.sms-booking .sms-booking__soon:not([hidden]) { animation: sms-drop 0.4s var(--sms-ease) both; }
.sms-booking .sms-booking__soon-icon { color: #8a5a00; }
.sms-booking .sms-booking__soon-text { min-width: 0; }
.sms-booking .sms-booking__soon-text a { color: var(--sms-ink); font-weight: 700; }
.sms-booking .sms-booking__reveal[hidden] { display: none; }
.sms-booking .sms-booking__reveal:not([hidden]) { animation: sms-drop 0.4s var(--sms-ease) both; }
.sms-booking .sms-booking__aside-note { display: flex; gap: 0.6rem; margin: 0.5rem 0 0; color: var(--sms-ink-soft); font-size: var(--sms-step--1); }
.sms-booking .sms-booking__note-icon { color: var(--sms-accent); }
.sms-booking .sms-booking__review { display: grid; grid-template-columns: minmax(0, 0.8fr) minmax(0, 1.2fr); gap: 0; margin: 0 0 1.5rem; border-radius: var(--sms-radius-sm); background: var(--sms-pale); overflow: hidden; }
.sms-booking .sms-booking__review[hidden] { display: none; }
.sms-booking .sms-booking__review dt,
.sms-booking .sms-booking__review dd { min-width: 0; margin: 0; padding: 0.7rem 1rem; border-bottom: 1px solid var(--sms-line); font-size: var(--sms-step--1); overflow-wrap: anywhere; }
.sms-booking .sms-booking__review dt { color: var(--sms-ink-soft); font-weight: 600; }
.sms-booking .sms-booking__review dd { font-weight: 700; }
.sms-booking .sms-booking__consent { display: flex; gap: 0.75rem; align-items: flex-start; font-size: var(--sms-step--1); cursor: pointer; }
.sms-booking .sms-booking__consent-input { flex: 0 0 auto; width: 1.25rem; height: 1.25rem; margin-top: 0.1rem; accent-color: var(--sms-green); }
.sms-booking .sms-booking__nav { display: flex; flex-wrap: wrap; justify-content: space-between; gap: 0.75rem; padding-top: 1.5rem; border-top: 1px solid var(--sms-line); }
.sms-booking .sms-booking__nav [hidden] { display: none; }
.sms-booking .sms-booking__nav[hidden] { display: none; }
.sms-booking .sms-booking__next,
.sms-booking .sms-booking__submit { margin-left: auto; cursor: pointer; font: inherit; font-size: var(--sms-step--1); font-weight: 700; }
.sms-booking .sms-booking__back { cursor: pointer; font: inherit; font-size: var(--sms-step--1); font-weight: 700; }
.sms-booking .sms-booking__done { padding: clamp(1rem, 0.5rem + 2vw, 2rem) 0; text-align: center; }
.sms-booking .sms-booking__done[hidden] { display: none; }
.sms-booking .sms-booking__done-badge { display: grid; place-items: center; width: 5rem; height: 5rem; margin: 0 auto 1.25rem; border-radius: 50%; background: var(--sms-green); color: var(--sms-white); animation: sms-tick 0.7s var(--sms-ease) both; }
.sms-booking .sms-booking__done-icon { width: 2.5rem; height: 2.5rem; }
.sms-booking .sms-booking__done-title { margin: 0 0 0.75rem; font-size: var(--sms-step-2); }
.sms-booking .sms-booking__done-text { max-width: 32rem; margin: 0 auto 1rem; color: var(--sms-ink-soft); }
.sms-booking .sms-booking__done-ref { margin: 0 0 1.5rem; }
.sms-booking .sms-booking__aside { display: grid; gap: 1rem; min-width: 0; }
.sms-booking .sms-booking__summary { min-width: 0; padding: 1.5rem; border-radius: var(--sms-radius); background: var(--sms-navy); color: var(--sms-white); }
.sms-booking .sms-booking__summary[hidden] { display: none; }
.sms-booking .sms-booking__summary-title { display: flex; align-items: center; gap: 0.5rem; margin-bottom: 1rem; font-weight: 700; }
.sms-booking .sms-booking__summary-icon { color: var(--sms-green-on-navy); }
.sms-booking .sms-booking__summary-list { margin: 0; }
.sms-booking .sms-booking__summary-list dt { color: var(--sms-green-on-navy); font-size: 0.75rem; font-weight: 700; letter-spacing: 0.1em; text-transform: uppercase; }
.sms-booking .sms-booking__summary-list dd { margin: 0 0 0.75rem; font-weight: 600; overflow-wrap: anywhere; animation: sms-fade-up 0.35s var(--sms-ease) both; }
.sms-booking .sms-booking__help { display: grid; gap: 0.5rem; min-width: 0; padding: 1.5rem; border-radius: var(--sms-radius); background: var(--sms-mint); }
.sms-booking .sms-booking__help-title { font-weight: 700; }
.sms-booking .sms-booking__help-title,
.sms-booking .sms-booking__progress-dot,
.sms-booking .sms-booking__demo > span { min-width: 0; }
.sms-booking .sms-booking__help-link { display: inline-flex; align-items: center; gap: 0.5rem; min-width: 0; color: var(--sms-ink); font-size: var(--sms-step--1); font-weight: 700; text-decoration: none; overflow-wrap: anywhere; }
.sms-booking .sms-booking__help-link:hover { color: var(--sms-accent); }
.sms-booking .sms-booking__help-icon { color: var(--sms-accent); }
.sms-booking .sms-booking__demo { display: flex; gap: 0.5rem; min-width: 0; padding: 0 0.5rem; color: var(--sms-ink-soft); font-size: var(--sms-step--1); }
.sms-booking .sms-booking__demo-icon { color: var(--sms-accent); }
@media (min-width: 40em) {
  .sms-booking .sms-booking__services { grid-template-columns: repeat(2, minmax(0, 1fr)); }
  .sms-booking .sms-booking__grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
  .sms-booking .sms-booking__field--wide { grid-column: 1 / -1; }
}
@media (min-width: 64em) {
  .sms-booking .sms-booking__inner { grid-template-columns: minmax(0, 1fr) minmax(0, 20rem); }
  .sms-booking .sms-booking__aside { position: sticky; top: 7rem; }
}
"""

TRANS = [".sms-booking .sms-booking__progress-dot", ".sms-booking .sms-booking__bar-fill", ".sms-booking .sms-booking__service-card",
         ".sms-booking .sms-booking__service-tick", ".sms-booking .sms-booking__chip-text"]
ANIM = [".sms-booking .sms-booking__form.is-wizard .sms-booking__step:not([hidden])", ".sms-booking .sms-booking__soon:not([hidden])",
        ".sms-booking .sms-booking__reveal:not([hidden])", ".sms-booking .sms-booking__done-badge", ".sms-booking .sms-booking__summary-list dd"]

JS = """<script>
(function () {
  var form = document.querySelector('[data-sms-booking]');
  if (!form) return;
  var steps = Array.prototype.slice.call(form.querySelectorAll('.sms-booking__step'));
  var back = form.querySelector('[data-sms-back]');
  var next = form.querySelector('[data-sms-next]');
  var submit = form.querySelector('[data-sms-submit]');
  if (submit) submit.disabled = false;
  var done = form.querySelector('[data-sms-done]');
  var bar = form.querySelector('[data-sms-bar]');
  var status = form.querySelector('[data-sms-status]');
  var review = form.querySelector('[data-sms-review]');
  var summary = document.querySelector('[data-sms-summary]');
  var current = 1;
  var names = { 1: 'Choose a service', 2: 'Tell us more', 3: 'Your details', 4: 'Check and send' };

  form.classList.add('is-wizard');
  Array.prototype.forEach.call(document.querySelectorAll('[data-sms-wizard-only]'), function (el) { el.hidden = false; });
  if (review) review.hidden = false;

  function service() { var r = form.querySelector('input[name="service"]:checked'); return r ? r.value : ''; }
  function visibleStep(n) { return steps.filter(function (s) { return s.getAttribute('data-step') === String(n) && (!s.hasAttribute('data-service') || s.getAttribute('data-service') === service()); })[0]; }

  function show(n) {
    current = n;
    steps.forEach(function (s) { s.hidden = s !== visibleStep(n); });
    back.hidden = n === 1;
    next.hidden = n === 4;
    submit.hidden = n !== 4;
    if (bar) bar.style.transform = 'scaleX(' + (n / 4) + ')';
    Array.prototype.forEach.call(form.querySelectorAll('[data-sms-progress]'), function (p) {
      var i = parseInt(p.getAttribute('data-sms-progress'), 10);
      p.classList.toggle('is-current', i === n);
      p.classList.toggle('is-done', i < n);
    });
    if (status) status.textContent = 'Step ' + n + ' of 4: ' + names[n];
    if (n === 4) buildReview();
  }

  function clearErrors(scope) {
    Array.prototype.forEach.call(scope.querySelectorAll('.is-invalid'), function (el) { el.classList.remove('is-invalid'); el.removeAttribute('aria-invalid'); });
    Array.prototype.forEach.call(scope.querySelectorAll('[data-error-for]'), function (el) { el.textContent = ''; });
  }

  function validate(scope) {
    clearErrors(scope);
    var ok = true, first = null;
    Array.prototype.forEach.call(scope.querySelectorAll('[required]'), function (el) {
      var bad;
      if (el.type === 'radio') { bad = !scope.querySelector('input[name="' + el.name + '"]:checked'); }
      else if (el.type === 'checkbox') { bad = !el.checked; }
      else { bad = !el.value.trim() || !el.checkValidity(); }
      if (bad) {
        ok = false;
        var key = (el.type === 'radio' || el.type === 'checkbox') ? el.name : el.id;
        var msg = scope.querySelector('[data-error-for="' + key + '"]');
        if (msg) msg.textContent = el.type === 'radio' ? 'Please choose one option.' : el.type === 'checkbox' ? 'Please tick to continue.' : el.type === 'email' && el.value ? 'Please enter a valid email address.' : 'Please fill this in.';
        if (el.type !== 'radio' && el.type !== 'checkbox') { el.classList.add('is-invalid'); el.setAttribute('aria-invalid', 'true'); }
        if (!first) first = el;
      }
    });
    if (first) first.focus();
    return ok;
  }

  function values(scope) {
    var out = [];
    var seen = {};
    Array.prototype.forEach.call(scope.querySelectorAll('[data-label]'), function (el) {
      var label = el.getAttribute('data-label');
      if (label === 'Consent') return;
      var v = '';
      if (el.type === 'radio') { if (!el.checked) return; v = el.getAttribute('data-name') || el.value; }
      else if (el.type === 'checkbox') { if (!el.checked) return; v = el.value; }
      else v = el.value.trim();
      if (!v) return;
      if (el.id === 'bk-attendance') v = Number(v).toLocaleString('en-GB') + (v === el.max ? '+' : '');
      if (el.type === 'date') { var d = new Date(v + 'T12:00:00'); if (!isNaN(d)) v = d.toLocaleDateString('en-GB', { day: 'numeric', month: 'long', year: 'numeric' }); }
      if (seen[label] !== undefined) { out[seen[label]][1] += ', ' + v; return; }
      seen[label] = out.length;
      out.push([label, v]);
    });
    return out;
  }

  function dl(target, pairs) {
    target.innerHTML = '';
    pairs.forEach(function (p) {
      var dt = document.createElement('dt'); dt.textContent = p[0];
      var dd = document.createElement('dd'); dd.textContent = p[1];
      target.appendChild(dt); target.appendChild(dd);
    });
  }

  function activeScopes() { return [visibleStep(1), visibleStep(2), visibleStep(3)].filter(Boolean); }

  function buildReview() {
    var pairs = [];
    activeScopes().forEach(function (s) { pairs = pairs.concat(values(s)); });
    dl(review, pairs);
  }

  function updateSummary() {
    if (!summary) return;
    var pairs = [];
    activeScopes().forEach(function (s) { pairs = pairs.concat(values(s)); });
    if (!pairs.length) pairs = [['Service', 'Not chosen yet']];
    dl(summary, pairs.slice(0, 7));
  }

  next.addEventListener('click', function () {
    var scope = visibleStep(current);
    if (!validate(scope)) return;
    show(current + 1);
    form.scrollIntoView({ behavior: 'smooth', block: 'start' });
  });
  back.addEventListener('click', function () { show(current - 1); });

  form.addEventListener('submit', function (ev) {
    ev.preventDefault();
    if (!validate(visibleStep(4))) return;
    steps.forEach(function (s) { s.hidden = true; });
    form.querySelector('.sms-booking__nav').hidden = true;
    form.querySelector('.sms-booking__top').hidden = true;
    form.querySelector('[data-sms-ref]').textContent = 'SMS-' + String(Math.floor(1000 + Math.random() * 9000));
    done.hidden = false;
    done.focus();
  });

  form.querySelector('[data-sms-restart]').addEventListener('click', function () {
    form.reset();
    done.hidden = true;
    form.querySelector('.sms-booking__nav').hidden = false;
    form.querySelector('.sms-booking__top').hidden = false;
    updateSummary();
    show(1);
  });

  form.addEventListener('change', function (ev) {
    if (ev.target.name === 'service' && current === 1) { updateSummary(); setTimeout(function () { show(2); }, 250); }
    if (ev.target.id === 'bk-course') { form.querySelector('[data-sms-bespoke]').hidden = ev.target.value !== 'Bespoke Course'; }
    if (ev.target.id === 'bk-event-date') {
      var d = new Date(ev.target.value + 'T12:00:00');
      var days = (d - new Date()) / 86400000;
      form.querySelector('[data-sms-soon]').hidden = !(days >= -1 && days < 31);
    }
    updateSummary();
  });
  form.addEventListener('input', function (ev) {
    if (ev.target.id === 'bk-attendance') {
      var o = form.querySelector('[data-sms-output]');
      o.textContent = Number(ev.target.value).toLocaleString('en-GB') + (ev.target.value === ev.target.max ? '+' : '');
    }
    updateSummary();
  });
  Array.prototype.forEach.call(form.querySelectorAll('[data-sms-step]'), function (b) {
    b.addEventListener('click', function () {
      var input = form.querySelector('#bk-learners');
      var v = Math.min(99, Math.max(1, (parseInt(input.value, 10) || 1) + parseInt(b.getAttribute('data-sms-step'), 10)));
      input.value = v;
      updateSummary();
    });
  });

  var pre = (new URLSearchParams(window.location.search)).get('service');
  var preInput = pre && form.querySelector('input[name="service"][value="' + pre + '"]');
  if (preInput) { preInput.checked = true; updateSummary(); show(2); } else { show(1); }
})();
</script>
"""
