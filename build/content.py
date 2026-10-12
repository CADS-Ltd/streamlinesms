"""Page content for every concept, taken word for word from the live site
(see reference/content.md and reference/*.html). [[text]] marks a brand highlight.
FAQs are parsed straight from the saved live pages so the wording is exact.

Long passages are split automatically: the first sentence or paragraph shows,
the rest sits behind a "Read more" toggle, so nothing from the live site is lost.
"""
import html
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
REF = os.path.join(HERE, "..", "reference")


def faqs(page):
    """Return [(question, answer_html)] from a saved live page's FAQ block."""
    s = open(os.path.join(REF, page + ".html"), encoding="utf-8").read()
    out = []
    for q, a in re.findall(r'<details[^>]*>\s*<summary[^>]*>((?:(?!</summary>).)*)</summary>\s*<div class="sl-faq__answer">((?:(?!</details>).)*?)</div>\s*</details>', s, re.S):
        q = html.unescape(re.sub(r"<[^>]+>", "", q)).strip()
        a = re.sub(r"\s+", " ", a).strip()
        a = re.sub(r"<(p|ul|li|strong)\b[^>]*>", r"<\1>", a)
        a = re.sub(r'<a\b[^>]*href="([^"]+)"[^>]*>', r'<a href="\1">', a)
        a = re.sub(r"</?(span|em|br)[^>]*>", "", a)
        out.append((q, a))
    return out


# Photos: the client's own images from the live site, cropped to the photographic
# area (no navy fades, no baked-in text). key -> (file, width, height, focus, alt)
PHOTOS = {
    "festival": ("event-medics-festival.jpg", 742, 614, "50% 30%", "Two Streamline medics in uniform at a music festival"),
    "team": ("team-at-event.jpg", 1052, 777, "50% 30%", "The Streamline team smiling together at an outdoor event"),
    "fete": ("medic-at-village-fete.jpg", 632, 668, "50% 30%", "A Streamline medic overlooking a village fete"),
    "cpr-room": ("cpr-training-room.jpg", 526, 849, "50% 40%", "A trainer demonstrating CPR on a manikin in a training room"),
    "phone": ("office-phone.jpg", 852, 941, "40% 30%", "A member of the Streamline team taking a call at a desk"),
    "jacket": ("branded-jacket-warehouse.jpg", 662, 690, "50% 40%", "The Streamline logo on the back of a uniform jacket in a warehouse"),
    "session": ("training-session.jpg", 912, 777, "60% 40%", "A Streamline clinician running a practical training session"),
    "directors": ("directors.jpg", 762, 756, "50% 20%", "Directors Mathew Stones and Tom Wilkes"),
    "cpr-outdoor": ("cpr-outdoor.jpg", 486, 354, "50% 50%", "A learner practising CPR on a manikin with a Streamline trainer"),
    "stall": ("event-stall.jpg", 486, 356, "50% 45%", "The Streamline team at a community event stand"),
    "assessor": ("assessor-hi-vis.jpg", 840, 1086, "45% 30%", "A Streamline advisor in a hi-vis vest assessing a workplace"),
}

# ---------------------------------------------------------------- shared bits
AREA = "Based in Swadlincote and serving Derbyshire, Staffordshire, Leicestershire, Nottinghamshire and the wider UK."
INTRO = "Streamline Safety & Medical Solutions provides professional event medical cover, accredited first aid training and practical safety consultancy for businesses, workplaces, construction sites and events across the East Midlands and throughout the UK."
INTRO2 = "Our experienced frontline clinicians help organisations stay compliant, reduce risk and protect the people who matter most."
CLAIM_15 = "Mathew and Tom bring over 15 years of ambulance experience between them, with even more expertise across our wider team."
STRAP = "Protecting People. Supporting Business."

SERVICES = [
    {"slug": "event-medical-cover", "key": "event", "title": "Event Medical Cover", "icon": "heart", "photo": "festival",
     "text": "From small local events to large-scale public gatherings, we provide professional, reliable and proportionate medical cover that gives you peace of mind.",
     "cta": "Book us for your medical cover",
     "list": [("tent", "Community events, village fetes and charity events"), ("briefcase", "Business showcases and corporate events"), ("trophy", "Sports and combat-sports events"), ("music", "Small festivals and outdoor activities")]},
    {"slug": "medical-training", "key": "training", "title": "Medical Training", "icon": "cap", "photo": "cpr-room",
     "text": "Accredited first aid and workplace safety training delivered by real frontline professionals in Swadlincote and beyond.",
     "cta": "Book your next training session",
     "list": [("firstaid", "Emergency First Aid at Work"), ("firstaid", "First Aid at Work and requalification"), ("school", "Paediatric and emergency paediatric first aid"), ("heart", "FREC 3 and FREC 4")]},
    {"slug": "risk-needs-consultancy", "key": "consultancy", "title": "Risk & Needs Consultancy", "icon": "clipboard", "photo": "assessor",
     "text": "We help businesses and event organisers understand their risks, meet their legal obligations, and ensure they have the right plans, people and equipment in place.",
     "cta": "Book a free consultation for your business",
     "list": [("clipboard", "First Aid Needs Assessment"), ("file", "Risk Assessment Writing"), ("route", "Event Medical Plans"), ("fire", "Fire Safety Assessment")]},
]
CAREERS = {"slug": "pre-hospital-career-support", "key": "careers", "title": "Pre-Hospital Career Support", "icon": "compass",
           "text": "Take your next step in a pre-hospital career with tailored interview preparation, mock assessments and honest, practical feedback.",
           "cta": "Explore career support"}

TRUST = [
    ("heart", "Frontline Experience", "Our services are shaped by current, real-world ambulance and safety experience."),
    ("target", "Proportionate Solutions", "Advice and support matched to the people, activities and risks involved."),
    ("shield", "Professional Standards", "Fully insured, carefully planned and professionally delivered."),
    ("chat", "Personal Service", "Clear communication and dependable support from enquiry to completion."),
]

ABOUT_HOME = [
    "At Streamline Safety & Medical Solutions, we combine current frontline ambulance experience with practical safety expertise to provide professional, dependable support for organisations, workplaces and events across the East Midlands and throughout the UK.",
    "We recognise that every organisation and event is different. That is why we do not take a one-size-fits-all approach. Our recommendations are proportionate to the people, activities and risks involved, helping you put appropriate arrangements in place without unnecessary complexity or expense.",
    "Whether you require support for a single event, a training course for your team or an ongoing safety partnership, you can expect honest advice, clear communication and a service tailored around your organisation.",
]

WORKING_WITH = {
    "title": "Working With You, Not Simply For [[You.]]",
    "body": ["At Streamline Safety & Medical Solutions, we are passionate about working alongside our clients to provide support that is fair, proportionate and genuinely tailored to their needs. We believe in honest advice, practical solutions and professional communication that helps you make the right decisions with confidence.",
             "If you need four first aiders trained, we will not try to sell you more than you need. Our approach is simple: clear guidance, realistic recommendations and support that is never over-sold."],
}
MATHEW_QUOTE = "“We truly care about the people and organisations we support. We will always communicate fairly, recommend proportionately and focus on what is genuinely right for you — not what is easiest to sell. That is what makes us different.”"

WHO = ["Individuals", "Businesses", "Schools", "Nurseries", "Care providers", "Construction and industrial workplaces", "Charities", "Community groups", "Sports clubs", "Security providers", "Event organisers"]

DIRECTORS = [
    {"name": "Mathew Stones", "tags": "Frontline Ambulance Experience · Mentoring · Training",
     "bio": ["Mathew is a Director of Streamline Safety & Medical Solutions and continues to work on the frontline within the ambulance service. His ongoing clinical experience allows him to bring current, real-world knowledge into the training, medical cover and consultancy services delivered by Streamline.",
             "With experience supporting, mentoring and developing people in frontline ambulance environments, Mathew understands the importance of confidence, clear communication and practical decision-making when responding to real emergencies. His approach focuses on making training realistic, relevant and easy to apply in high-pressure situations."]},
    {"name": "Thomas Wilkes", "tags": "Industrial Rescue · Workplace Safety · Training",
     "bio": ["Thomas, known as Tom, is one of the Directors of Streamline Safety & Medical Solutions. Having previously worked on the frontline within the ambulance service, he now works as an Industrial Rescue Operative, bringing experience in workplace safety, rescue environments and risk assessment.",
             "Tom brings strong experience in both practical safety operations and classroom-based training. His background includes mentoring and developing others, with a particular focus on delivering clear, structured and engaging training that helps learners build confidence and competence."]},
]

CATALOGUE = "https://drive.google.com/file/d/1k82wcwQwJq7KmyQy4cUvaI-Ub998ElZr/view?usp=sharing"

# ---------------------------------------------------------------- inner pages
PAGES = {}

PAGES["event-medical-cover"] = {
    "doc": "Event Medical Cover",
    "desc": "Professional, proportionate event medical cover from Swadlincote across Derbyshire, Leicestershire, Staffordshire and the wider East Midlands.",
    "hero": {"eyebrow": "Event Medical Support", "title": "Tailored [[Event Medical Cover]]",
             "body": ["From small local events to large-scale public gatherings, we provide professional, reliable and proportionate medical cover that gives you peace of mind."],
             "buttons": [("Book us for your medical cover", "book:event"), ("Call 01283 358789", "tel")],
             "photo": "festival", "chips": [("shield", "Skilled. Proportionate. Reliable."), ("heart", "Clinician-led")]},
    "sections": [
        ("feature", {"eyebrow": "What type of medical support do we offer?", "title": "Medical Support Built Around [[Your Event]]", "photo": "fete",
                     "body": ["We deliver high-quality medical support across a wide range of events and environments, from community gatherings and sporting events to concerts, public events and planned workplace operations.",
                              "Our services are flexible, scalable and tailored to the specific risks, audience profile, venue layout and operational needs of your event. Whether you require a small first aid presence or a more structured medical plan, we provide professional, reliable and safe support designed around your event."],
                     "chips_title": "What events can Streamline cover?",
                     "chips": [("tent", "Community events, village fetes and charity events"), ("briefcase", "Business showcases and corporate events"), ("trophy", "Sports and combat-sports events"), ("school", "School events and private functions"), ("music", "Small festivals and outdoor activities")]}),
        ("cards", {"tone": "pale", "eyebrow": "Our Process", "title": "Skilled. Proportionate. [[Reliable.]]", "cols": 3, "watermark": True,
                   "items": [
                       {"icon": "users", "title": "Skilled", "text": "Our medical teams are made up of trained responders and clinicians with real experience in event & frontline environments. From first responders through to registered clinicians, we ensure the right level of skill is matched to the needs of your event. This allows us to provide safe, confident and effective care, whether dealing with minor injuries, medical concerns or supporting emergency escalation."},
                       {"icon": "target", "title": "Proportionate", "text": "We do not believe in a one-size-fits-all approach. Every event is assessed based on its size, audience, location, activities, risks and access to emergency services. This means we provide a level of medical cover that is suitable, sensible and aligned with current guidance, helping organisers remain safe, compliant and well prepared without overcomplicating the provision."},
                       {"icon": "check", "title": "Reliable", "text": "Event organisers need medical support they can trust. We focus on clear planning, professional communication and dependable delivery from the first enquiry through to post-event reporting. Our team arrives prepared, equipped and ready to support the event, giving organisers confidence that medical arrangements are in safe hands."}]}),
        ("feature", {"eyebrow": "Booking information", "title": "Book Your Event Medical Cover", "photo": "stall", "flip": True,
                     "body": ["When booking Streamline Safety & Medical Solutions, we will provide you with a clear quotation based on your event requirements.",
                              "Your booking will be confirmed once this has been agreed and any required booking information has been completed.",
                              "If your event details change, such as timings, attendance or activities, please let us know so we can make sure the medical provision remains suitable.",
                              "Full Medical Cover Booking Terms & Conditions will be provided when you choose to book with us, so you can review everything before confirming your booking."],
                     "chips_title": "What information is needed for a quote?",
                     "chips": [("calendar", "Event type, date, times, venue and postcode"), ("users", "Expected attendance and age range"), ("music", "Activities and alcohol arrangements"), ("file", "Previous incidents and existing provision"), ("route", "Risk assessment, site plan and emergency access"), ("clipboard", "Any organiser or venue requirements")],
                     "buttons": [("Book us for your medical cover", "book:event")]}),
        ("faq", {"tone": "pale", "eyebrow": "Skilled. Proportionate. Reliable.", "title": "Event Medical Cover FAQs",
                 "lead": ["Answers about professional event medical cover, staffing, equipment, planning, quotations and organiser responsibilities."],
                 "items": faqs("event-medical-cover")}),
    ],
    "image_text": ["\"Book Your Event Medical Cover\" heading (book-your-medical-cover.png)"],
    "cta": {"title": "How early should I book?", "text": ["Contact us as early as possible. Larger, higher-risk or multi-day events require more planning. For an event within one month, contact us directly as well as submitting any online enquiry."],
            "buttons": [("Book us for your medical cover", "book:event"), ("Call 01283 358789", "tel")]},
}

PAGES["medical-training"] = {
    "doc": "Medical Training",
    "desc": "Clinician-led first aid and pre-hospital training in Swadlincote and beyond, delivered through our Qualsafe registered centre.",
    "hero": {"eyebrow": "Medical Training", "title": "First Aid Training in [[Swadlincote]]",
             "sub": "Clinician-Led First Aid and Pre-Hospital Training",
             "body": ["Accredited first aid and workplace safety training delivered by real frontline professionals in Swadlincote and beyond."],
             "buttons": [("Book your next training session", "book:training"), ("View our training catalogue of courses", CATALOGUE)],
             "photo": "cpr-room", "chips": [("award", "Qualsafe Registered Centre"), ("users", "Practical, hands-on training")]},
    "sections": [
        ("cards", {"eyebrow": "Medical Training", "title": "What medical training courses do you [[provide?]]", "cols": 3, "compact": True,
                   "lead": ["Availability may vary, so please contact us for current dates and options."],
                   "items": [
                       {"icon": "firstaid", "title": "Emergency First Aid at Work", "meta": "Usually one day"},
                       {"icon": "firstaid", "title": "First Aid at Work", "meta": "Usually three days"},
                       {"icon": "check", "title": "First Aid at Work requalification", "meta": "Usually two days"},
                       {"icon": "school", "title": "Paediatric First Aid", "meta": "Usually two days", "text": "Paediatric and emergency paediatric first aid."},
                       {"icon": "heart", "title": "FREC 3", "meta": "Usually five classroom-based training days with assessments", "text": "FREC 3 is the Level 3 Award in First Response Emergency Care."},
                       {"icon": "award", "title": "FREC 4", "meta": "Usually five classroom-based training days, alongside completion of a portfolio and workbooks"},
                       {"icon": "heart", "title": "CPR, AED and basic life support"},
                       {"icon": "briefcase", "title": "Bespoke workplace medical training"},
                       {"icon": "school", "title": "Bespoke school training packages", "text": "Including support for requirements arising from Benedict’s Law."}]}),
        ("feature", {"tone": "pale", "eyebrow": "Group Bookings", "title": "Group & Bespoke [[Training]]", "photo": "session", "watermark": True,
                     "body": ["Booking training as a group is a great way to support your workplace, club or organisation with practical training tailored to the people, risks and situations your team may face.",
                              "Streamline Safety & Medical Solutions is a Qualsafe Registered Centre – Centre No. 908578, allowing us to deliver nationally recognised, regulated qualifications alongside bespoke in-house training. We can deliver training at your venue or arrange a suitable training location for your group.",
                              "If you would like a tailored package, simply select “Bespoke Course” on the booking form and tell us what you would like the training to cover. Our team will then get in touch to discuss your requirements and build a suitable training package for your organisation."],
                     "chips_title": "Examples of bespoke training",
                     "chips": [("heart", "Care Homes & Social Care"), ("trophy", "Sports Clubs & Activity Providers"), ("school", "Schools & Education"), ("briefcase", "Workplaces & Businesses"), ("sparkle", "Something Specific?")],
                     "buttons": [("Book your next training session", "book:training")]}),
        ("cards", {"eyebrow": "Your training experience", "title": "What to expect", "cols": 4, "compact": True,
                   "lead": ["Practical training designed to help you build confidence, apply skills and respond effectively in real-world situations."],
                   "items": [
                       {"icon": "users", "title": "Practical, hands-on training", "text": "Develop your skills through practical activities and guided practice, not just classroom theory."},
                       {"icon": "target", "title": "Realistic scenarios", "text": "Put your knowledge into practice through realistic medical and trauma-based training scenarios."},
                       {"icon": "heart", "title": "Experienced instructors", "text": "Learn from instructors with real pre-hospital and frontline clinical experience."},
                       {"icon": "award", "title": "Recognised qualifications", "text": "Our regulated courses are delivered through our Qualsafe registered training centre."}]}),
        ("notice", {"tone": "pale", "label": "Upcoming public training sessions", "title": "No public courses currently scheduled",
                    "text": ["We do not currently have any upcoming public course dates planned, but we intend to offer more courses in the future. Please check back soon or register your interest in the section below to hear about new dates when they are released."],
                    "buttons": [("Register your interest", "book:training"), ("View our training catalogue of courses", CATALOGUE)]}),
        ("steps", {"tone": "pale", "eyebrow": "Register Your Interest", "title": "What Happens Next?",
                   "lead": ["Can’t see a date for the course you’re looking for? Registering your interest lets us know exactly what training you need and helps us plan future courses around genuine demand."],
                   "items": [
                       {"icon": "chat", "title": "Tell Us What You Need", "text": "Register your interest in the course or qualification you’re looking for. This helps our training team understand current demand and what learners would like us to run next."},
                       {"icon": "mail", "title": "We’ll Keep You Informed", "text": "When suitable dates become available, we can get in touch and let you know about the opportunity without you having to continually check the website."},
                       {"icon": "compass", "title": "We’ll Help With Your Options", "text": "Where appropriate, we can discuss alternative course dates, group bookings, bespoke training or other qualifications that may suit what you’re trying to achieve."}],
                   "note": ["No obligation to book. Registering your interest does not commit you to a course or require payment."]}),
        ("faq", {"eyebrow": "Clinician-led, practical training", "title": "Medical Training FAQs",
                 "lead": ["Answers about first aid training in Swadlincote, workplace group courses, qualifications, assessments and bookings."],
                 "items": faqs("medical-training")}),
    ],
    "image_text": ["\"Group Bookings\" eyebrow (streamline-group-bookings.png)", "\"Examples of bespoke training\" list title (examples-of-streamline-s-bespoke-training.png)"],
    "cta": {"title": "Not Sure Which Course Is Right for You?", "text": ["Our Pre-Hospital Career Support service can help you understand possible routes, qualifications and next steps based on where you are now and where you want to go."],
            "buttons": [("Book your next training session", "book:training"), ("Explore career support", "pre-hospital-career-support")]},
}

PAGES["risk-needs-consultancy"] = {
    "doc": "Risk & Needs Consultancy",
    "desc": "Workplace risk assessments, first aid needs assessments, event medical plans and safety consultancy, with a free initial consultation.",
    "hero": {"eyebrow": "Risk and Needs Consultancy", "title": "Expert Advice, [[Practical Solutions]]",
             "body": ["We help businesses and event organisers understand their risks, meet their legal obligations, and ensure they have the right plans, people and equipment in place."],
             "buttons": [("Request a FREE initial Consultation", "book:consultancy"), ("Call 01283 358789", "tel")],
             "photo": "assessor", "chips": [("chat", "Free initial consultation"), ("shield", "IOSH-qualified advisors")]},
    "sections": [
        ("feature", {"eyebrow": "Our Consultancy Services", "title": "Safety Starts by Recognising [[Danger]]", "photo": "jacket",
                     "body": ["In pre-hospital care, the first step is always to assess for danger. Before treatment begins, we look at the environment, identify risks, protect people from harm, and make sure the right support is in place.",
                              "Our Risk & Needs Consultancy applies that same practical, safety-first mindset to workplaces, events and public environments. Led by IOSH-qualified health and safety advisors with real-world medical and operational experience, we help you identify hazards, understand your responsibilities, and put proportionate plans, people and equipment in place before problems occur.",
                              "From first aid needs assessments to event medical planning and safe systems of work, we help you move from uncertainty to clear, practical and compliant safety arrangements."],
                     "strap": "Assess the risk. Plan the response. Protect your people.",
                     "chips_title": "Which industries do you support?",
                     "chips": [("building", "Offices"), ("briefcase", "Retail"), ("building", "Warehousing"), ("hardhat", "Construction"), ("hardhat", "Manufacturing"), ("users", "Hospitality"), ("school", "Education"), ("heart", "Care"), ("tent", "Community organisations"), ("trophy", "Sports, leisure and events")]}),
        ("cards", {"tone": "pale", "title": "What consultancy services do you [[provide?]]", "cols": 3, "watermark": True,
                   "items": [
                       {"icon": "clipboard", "title": "First Aid Needs Assessment", "text": "We evaluate your workplace to determine the level of first aid provision required. We consider the work undertaken, likely hazards, workforce size, first aid kit levels, kit storage and monitoring, first aider numbers, absence cover and emergency service response arrangements.",
                        "list_title": "What this includes", "list": ["Review of workplace hazards, staffing and operating patterns", "Recommended first aider numbers, competence levels and equipment", "Clear, proportionate actions to strengthen your provision"]},
                       {"icon": "file", "title": "Risk Assessment Writing", "text": "We identify workplace hazards, how they may cause harm, their likelihood and severity, the controls already in place and the residual risk. The result is a clear, practical assessment that helps you manage risk effectively.",
                        "list_title": "What this includes", "list": ["Hazard identification and evaluation of who may be affected", "Review of existing controls, severity, likelihood and residual risk", "Usable documentation with prioritised recommendations"]},
                       {"icon": "search", "title": "Gap Assessment", "text": "We assess your current emergency response capability, identify gaps and advise how to improve training, equipment and processes. Where appropriate, we can run realistic scenarios or practical exercises to test your existing arrangements and highlight areas for improvement.",
                        "list_title": "What this includes", "list": ["Comparison of current arrangements against operational needs", "Scenario testing or practical exercises where appropriate", "Prioritised improvement plan covering people, kit and processes"]},
                       {"icon": "route", "title": "Event Medical Plans", "text": "We help event organisers decide what a suitable event medical plan should include. Using recognised guidance and practical frontline experience, we create proportionate arrangements tailored to the event, venue, audience and identified risks.",
                        "list_title": "What this includes", "list": ["Proportionate medical resources and suitable clinical capability", "Access, communications, escalation and emergency arrangements", "Practical planning informed by recognised event guidance"]},
                       {"icon": "hardhat", "title": "Safe System of Work (SSoW) Advice", "text": "We support industrial, workplace and event clients to build safe systems of work focused on first aid and the activities they undertake. This helps protect teams, clarify responsibilities and keep operations safe, practical and compliant.",
                        "list_title": "What this includes", "list": ["Clear step-by-step safe working methods for relevant activities", "Defined responsibilities, equipment and risk controls", "Practical implementation and review support"]},
                       {"icon": "fire", "title": "Fire Safety Assessment", "text": "We review your premises to identify fire hazards, people who may be at risk and the adequacy of your existing precautions. Our practical assessment considers prevention, detection and warning, escape routes, emergency arrangements, fire-fighting equipment, staff information and training, helping you understand the actions needed to improve fire safety and compliance.",
                        "list_title": "What this includes", "list": ["Review of fire hazards, ignition sources and people at risk", "Assessment of alarms, escape routes, signage and emergency arrangements", "Prioritised recommendations covering equipment, training and routine checks"]}]}),
        ("steps", {"eyebrow": "Free initial consultation", "title": "How Your Free Initial [[Consultation]] Works",
                   "lead": ["This is a no-obligation conversation where we take the time to learn about your current arrangements, any concerns you may have, and what you are hoping to achieve."],
                   "items": [
                       {"icon": "chat", "title": "Tell Us What You Need", "text": "Once you submit your enquiry, we will review the information you have provided and contact you to arrange a suitable time for your free consultation. At this stage, you do not need to know exactly what service you require."},
                       {"icon": "users", "title": "We Discuss Your Current Situation", "text": "During the consultation, we will ask about your workplace, event, venue or activity. This helps us build a clear picture of your risks, responsibilities and current safety arrangements. This conversation is not about catching you out."},
                       {"icon": "search", "title": "We Identify Key Risks and Priorities", "text": "Using a practical safety-first approach, we will help identify the main areas that may need attention."},
                       {"icon": "compass", "title": "We Explain Your Options", "text": "After discussing your needs, we will explain what support may be appropriate. We will be clear about what is necessary, what is advisable, and what may be excessive for your situation."},
                       {"icon": "check", "title": "You Receive Clear Next Steps", "text": "At the end of the consultation, we will summarise what we believe your next steps should be. There is no pressure to proceed."}],
                   "note": ["The free consultation does not usually include full document writing, detailed legal compliance reviews, full risk assessments, event medical plans or formal written reports. These can be provided as part of a paid consultancy service if required."]}),
        ("faq", {"tone": "pale", "eyebrow": "Free initial consultation", "title": "Risk & Needs Consultancy FAQs",
                 "lead": ["Practical answers about workplace assessments, event planning, reports and proportionate safety support."],
                 "items": faqs("risk-needs-consultancy")}),
    ],
    "cta": {"title": "Why We Offer a Free Consultation", "text": ["It gives you the chance to speak with someone who understands both safety planning and practical medical response, so you can make confident decisions about protecting your staff, visitors and the public."],
            "buttons": [("Request a FREE initial Consultation", "book:consultancy"), ("Call 01283 358789", "tel")]},
}

PAGES["pre-hospital-career-support"] = {
    "doc": "Pre-Hospital Career Support",
    "desc": "Interview preparation, mock assessments and honest feedback for people starting or progressing a pre-hospital career.",
    "hero": {"eyebrow": "Pre-Hospital Career Support", "title": "Practical Support. [[Confident Career Steps.]]",
             "body": ["Take your next step in a pre-hospital career with tailored interview preparation, mock assessments and honest, practical feedback."],
             "buttons": [("Complete this form to get started", "book:careers")],
             "photo": "session", "chips": [("chat", "Honest, frontline-informed support")]},
    "sections": [
        ("feature", {"eyebrow": "Career Support", "title": "Starting Out in a Medical or [[Pre-Hospital Career?]]", "photo": "cpr-outdoor",
                     "body": ["We offer tailored support for aspiring clinicians and pre-hospital professionals, helping you get ready for interviews, assessment days, and the next steps in your career.",
                              "With practical advice, mock assessments, and honest feedback, we help you build confidence and present your best self."],
                     "chips_title": "Support at every starting point",
                     "chips": [("compass", "People considering an ambulance career"), ("firstaid", "First aiders and FREC-qualified medics"), ("users", "Ambulance Care Assistants and Emergency Care Assistants"), ("heart", "Ambulance Technicians and Associate Ambulance Practitioners"), ("cap", "Student and newly qualified paramedics"), ("route", "People returning to pre-hospital care"), ("target", "Applicants struggling to secure their first role")]}),
        ("cards", {"tone": "pale", "eyebrow": "Pre-hospital career support", "title": "Your Next Step. [[Our Practical Support.]]", "cols": 2, "numbered": True, "watermark": True,
                   "items": [
                       {"icon": "chat", "title": "Interview preparation", "text": "Prepare to explain your experience, strengths and motivation clearly in a pre-hospital or ambulance service interview.",
                        "list_title": "What we can help with", "list": ["Understanding the role you are applying for.", "Structuring answers around relevant examples.", "Practising interview questions and discussing your responses.", "Presenting your skills and experience with confidence."]},
                       {"icon": "clipboard", "title": "Mock assessments", "text": "Get familiar with the assessment process and practise your approach in a supportive environment.",
                        "list_title": "What we can help with", "list": ["Discussing the assessment information provided by your prospective employer.", "Mock assessment practice tailored to your preparation needs.", "Developing clear communication and a structured approach.", "Reflecting on your performance before the real assessment."]},
                       {"icon": "star", "title": "Feedback & development", "text": "Understand what you do well and where focused preparation could make a difference.",
                        "list_title": "What we can help with", "list": ["Honest, constructive feedback on your practice.", "Identifying strengths and areas to improve.", "Reflecting on previous interviews or assessments.", "Agreeing practical priorities for your next steps."]},
                       {"icon": "compass", "title": "Career direction", "text": "Explore pre-hospital roles and opportunities that fit your experience, interests and ambitions.",
                        "list_title": "What we can help with", "list": ["Understanding different ambulance and pre-hospital roles.", "Discussing entry routes and career progression.", "Considering relevant opportunities and their requirements.", "Working out where to focus your preparation."]}]}),
        ("steps", {"eyebrow": "Step by step", "title": "How your support [[works]]",
                   "items": [
                       {"icon": "target", "title": "Tell us your goal", "text": "Complete the enquiry form and tell us about your experience, the role you have in mind and any upcoming interview or assessment."},
                       {"icon": "chat", "title": "Agree your focus", "text": "We discuss where you need support and agree the most useful preparation for your next step."},
                       {"icon": "clipboard", "title": "Prepare & practise", "text": "Work through the agreed support, which may include interview practice, mock assessments or career guidance."},
                       {"icon": "star", "title": "Take your next step", "text": "Use constructive feedback and clear priorities to focus your preparation and approach your next opportunity with confidence."}]}),
        ("faq", {"tone": "pale", "eyebrow": "Honest, frontline-informed support", "title": "Pre-Hospital Career Advice FAQs",
                 "lead": ["Answers about ambulance and pre-hospital career routes, applications, interviews and professional progression."],
                 "items": faqs("pre-hospital-career-support")}),
    ],
    "cta": {"title": "How do I book career advice?", "text": ["Contact us through the website and explain your current position, the role you are interested in and the support you would like."],
            "buttons": [("Complete this form to get started", "book:careers"), ("Call 01283 358789", "tel")]},
}

PAGES["recruitment"] = {
    "doc": "Recruitment",
    "desc": "Join Streamline: we welcome expressions of interest from clinicians, trainers and health & safety professionals.",
    "hero": {"eyebrow": "Recruitment", "title": "Interested in [[Working With Us?]]",
             "body": ["We are looking to hear from experienced professionals who can support our growing services."],
             "buttons": [("Expression of Interest form", "contact")],
             "photo": "team", "chips": [("users", "Clinicians, trainers and health & safety professionals")]},
    "sections": [
        ("checklist", {"title": "We are looking to hear from [[experienced professionals]]",
                       "items": [("cap", "Training roles delivering first aid and clinical courses"), ("hardhat", "Safety operatives with health & safety experience"), ("heart", "Clinicians for event, medical, and business cover")]}),
        ("feature", {"tone": "pale", "eyebrow": "Recruitment form – Stage One", "title": "Expression of [[Interest]]", "photo": "stall", "watermark": True,
                     "body": ["We welcome expressions of interest from clinicians, trainers and health & safety professionals who may be able to support our event medical services, workplace and business cover, first aid and pre-hospital training, health & safety consultancy, and other operational requirements.",
                              "Submitting this form is not a formal application or offer of employment or engagement. Where your experience and availability appear suitable for our current or developing requirements, we will contact you to discuss the next stage of the process.",
                              "We are particularly interested in people who share our commitment to care, integrity, teamwork, safety and supporting the communities and organisations we work with."],
                     "chips_title": "Our values",
                     "chips": [("heart", "Care"), ("shield", "Integrity"), ("users", "Teamwork"), ("check", "Safety"), ("tent", "Community")],
                     "buttons": [("Expression of Interest form", "contact")]}),
        ("steps", {"eyebrow": "Our recruitment pathway", "title": "A clear [[process]]",
                   "lead": ["Our recruitment pathway is designed to ensure that everyone representing Streamline meets the professional, clinical and operational standards we expect."],
                   "items": [{"icon": "file", "title": "Expression of Interest"}, {"icon": "chat", "title": "Interview"}, {"icon": "clipboard", "title": "Clinical Assessment or Teaching Demonstration"}, {"icon": "user", "title": "Onboarding"}, {"icon": "star", "title": "Uniform & Welcome to the Team"}]}),
    ],
    "image_text": ["\"A clear process\" heading and the values list Care / Integrity / Teamwork / Safety / Community (step-by-step-recruitment-process.png)"],
    "cta": {"title": "If this sounds like you, get in touch", "text": ["Get in touch and we will continue the conversation."],
            "buttons": [("Expression of Interest form", "contact"), ("Email us", "mail")]},
}

PAGES["about"] = {
    "doc": "About Us",
    "desc": "Clinician-led, practical and professional: meet the directors and values behind Streamline Safety & Medical Solutions.",
    "hero": {"eyebrow": "About Us", "title": "Clinician-Led. Practical. [[Professional.]]",
             "sub": "Protecting People. Supporting Businesses.",
             "body": ["Streamline Safety & Medical Solutions brings frontline clinical experience to medical training, event medical cover and workplace safety consultancy."],
             "buttons": [("Contact Streamline", "contact")],
             "photo": "directors", "chips": [("heart", "Frontline Experience"), ("chat", "Personal Service")]},
    "sections": [
        ("quotes", {"items": [
            {"label": "Our Mission", "icon": "target", "text": "“To deliver practical, clinician-led medical training, event medical support, and safety consultancy that helps organisations act with confidence, reduce risk, and create safer environments.”"},
            {"label": "Our Vision", "icon": "star", "text": "“To set the standard for clinician-led medical training, workplace safety, and first aid risk needs assessment consultancy by delivering streamlined, real-world solutions that empower organisations to act with confidence, reduce risk, and save lives.”"}]}),
        ("cards", {"tone": "pale", "eyebrow": "Our Values In Practice", "title": "The Standards We Share. [[The Support You Can Expect.]]", "cols": 3, "watermark": True, "compact": True,
                   "items": [
                       {"icon": "briefcase", "title": "Professionalism", "text": "Careful preparation, clear communication and attention to detail throughout our work."},
                       {"icon": "shield", "title": "Integrity", "text": "Honest advice, realistic expectations and dependable support, so you can make informed decisions."},
                       {"icon": "check", "title": "Practicality", "text": "Clear guidance shaped by frontline experience, ready to apply in real situations."},
                       {"icon": "heart", "title": "Safety", "text": "Protecting people through thoughtful planning, suitable arrangements and an understanding of risk."},
                       {"icon": "star", "title": "Confidence", "text": "Helping people feel prepared through knowledge, practice and supportive learning."},
                       {"icon": "compass", "title": "Proactive Support", "text": "Identifying gaps early and helping you prepare before an incident happens."}]}),
        ("people", {"eyebrow": "Our Leadership Team", "title": "Meet The [[Directors.]]", "photo": "festival",
                    "lead": ["At Streamline Safety & Medical Solutions, our leadership team brings together frontline ambulance experience, clinical knowledge, training expertise, and practical health and safety insight."],
                    "items": DIRECTORS,
                    "shared": {"label": "Stronger Together", "title": "A Shared Frontline Approach",
                               "text": ["Together, Mathew and Tom combine clinical experience, ambulance service knowledge, industrial safety expertise, and hands-on training experience.",
                                        "Having both worked in frontline ambulance environments, they understand the realities of emergency care, risk management, and supporting people under pressure. Their combined experience allows Streamline to deliver training and safety solutions that are practical, realistic and built around real-world challenges.",
                                        "This shared approach helps ensure that every course, assessment and service delivered by Streamline is grounded in experience, focused on safety, and designed to give people the confidence to act when it matters most."]}}),
        ("claim", {"tone": "pale", "text": CLAIM_15, "watermark": True, "image_text": "\"Mathew and Tom bring over 15 years of ambulance experience...\" (why-choose-us.png - use approved)"}),
    ],
    "cta": {"title": "Protecting People. Supporting Businesses.", "text": ["Speak to our team and we will be happy to help."],
            "buttons": [("Contact Streamline", "contact"), ("Book online", "book")]},
}

PAGES["contact"] = {
    "doc": "Contact Us",
    "desc": "Contact Streamline Safety & Medical Solutions: call 01283 358789 or email hello@streamlinesms.co.uk.",
    "hero": {"eyebrow": "Contact Us", "title": "Contact [[Streamline]]",
             "sub": "Have any questions? We’re here to help.",
             "body": ["For general enquiries about Streamline Safety & Medical Solutions, please get in touch using the details below or complete our enquiry form."],
             "buttons": [("Call 01283 358789", "tel"), ("Book online", "book")],
             "photo": "phone", "chips": [("phone", "01283 358789"), ("mail", "hello@streamlinesms.co.uk")]},
    "sections": [
        ("contact", {"eyebrow": "General contact details", "title": "Streamline Safety & Medical Solutions Ltd",
                     "body": ["We aim to respond as quickly as possible. Detailed quotations or service plans may take longer where we need to assess event information, workplace risks or training requirements."],
                     "form_title": "Use our form below to contact us"}),
        ("links", {"tone": "pale", "title": "Need a Specific [[Service?]]",
                   "items": [
                       {"icon": "heart", "title": "Event Medical Cover", "text": "For event medical cover enquiries, including small event cover and medical planning.", "go": "Visit Medical Cover", "link": "event-medical-cover"},
                       {"icon": "cap", "title": "Medical Training", "text": "For first aid training, workplace training or medical education enquiries.", "go": "Visit Medical Training", "link": "medical-training"},
                       {"icon": "clipboard", "title": "Risk & Needs Consultancy", "text": "For risk assessments, event safety advice, medical planning reviews or compliance support.", "go": "Visit Risk & Needs Consultancy", "link": "risk-needs-consultancy"},
                       {"icon": "users", "title": "Recruitment", "text": "Interested in joining the team? View current opportunities and application information.", "go": "Visit Recruitment", "link": "recruitment"}]}),
    ],
    "image_text": ["Need a Specific Service? card descriptions (ChatGPT-named card images on the live Contact page)"],
    "cta": None,
}

HOME_FAQ = dict(faqs("home"))

PAGES["book"] = {
    "doc": "Book Online",
    "desc": "Request event medical cover, training, a free consultation or career support online.",
    "hero": {"eyebrow": "Book with Streamline", "title": "Book [[online]]",
             "body": ["A booking is confirmed once Streamline has accepted it and the relevant requirements have been completed. This may include accepting the terms, supplying required information and paying a deposit or invoice."],
             "buttons": [("Call 01283 358789", "tel")],
             "photo": "stall", "chips": [("shield", "Demo form: nothing is sent"), ("phone", "01283 358789")]},
    "sections": [
        ("booking", {}),
        ("faq", {"tone": "pale", "eyebrow": STRAP, "title": "Booking questions",
                 "items": [(q, HOME_FAQ[q]) for q in ["When is my booking confirmed?", "Do you require a deposit?", "Can a service be changed after booking?", "What happens if important information changes or was not disclosed?", "Do you have terms and conditions?", "How quickly will Streamline respond?"]],
                 "show": 6, "search": False}),
    ],
    "image_text": [],
    "cta": None,
}
