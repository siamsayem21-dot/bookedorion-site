#!/usr/bin/env python3
"""Builds /services/ and the home-page "Everything we do" block for bookedorion.com.

Standalone like pricing.py: borrows head, header and footer from the published /about/ page.
Run from the repo root:  python3 _source/services.py
Services, prices and rules come from 00_LOCKED_RULEBOOK.md (C11-C14). All visuals are
HTML product sketches with sample data, labelled as samples. No emergency-transfer claim (C6).
"""
import json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pricing import ROOT

PATH = '/services/'
URL = 'https://bookedorion.com' + PATH
TITLE = 'Services for HVAC Shops | BookedOrion'
DESC = ('Molly answers your calls and books jobs. Review requests, reminders, follow-ups, '
        'Google profile help and websites for HVAC shops. 14-day free trial.')

def ic(d, s=20):
    return (f'<svg width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{d}</svg>')
I = {
 'phone': '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.9.6 2.8.7a2 2 0 0 1 1.7 2z"/>',
 'chat': '<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>',
 'bell': '<path d="M18 8a6 6 0 0 0-12 0c0 7-3 9-3 9h18s-3-2-3-9M13.7 21a2 2 0 0 1-3.4 0"/>',
 'star': '<path d="M12 2l3.1 6.3 6.9 1-5 4.9 1.2 6.8L12 17.8 5.8 21l1.2-6.8-5-4.9 6.9-1z"/>',
 'cal': '<rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/>',
 'mail': '<rect x="2" y="4" width="20" height="16" rx="2"/><path d="M22 6l-10 7L2 6"/>',
 'pin': '<path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/>',
 'web': '<rect x="2" y="3" width="20" height="14" rx="2"/><path d="M8 21h8M12 17v4"/>',
 'chart': '<path d="M3 3v18h18"/><path d="M7 15l4-4 3 3 5-6"/>',
 'check': '<path d="M5 12l5 5L20 7"/>',
}
CHK = ic(I['check'], 14)

# (anchor, icon, name, one-line, price-tag, tag-kind)
SVCS = [
 ('molly', 'phone', 'Molly, AI receptionist', 'Answers missed and after-hours calls and books the job', 'Your plan', 'plan'),
 ('chat', 'chat', 'Website chat and DM replies', 'Replies to people who message your site or Facebook page', 'Included', 'inc'),
 ('reminders', 'bell', 'Appointment reminders', 'A text the day before every visit', 'Included', 'inc'),
 ('reviews', 'star', 'Google review requests', 'A thank-you with your review link after each job', 'Included', 'inc'),
 ('tuneups', 'cal', 'Tune-up reminders', 'Past customers hear from you before summer and winter', '$49/mo', 'add'),
 ('estimates', 'mail', 'Estimate follow-up', 'A polite nudge on day 2, 5 and 10, then it stops', '$49/mo', 'add'),
 ('gbp', 'pin', 'Google Business Profile tune-up', 'Photos, services, hours and area, set up right', '$199 once', 'add'),
 ('website', 'web', 'A website for your shop', 'Fast, mobile-first, with tap-to-call and booking', '$600 + $49/mo', 'add'),
 ('report', 'chart', 'Monthly report', 'Calls, jobs and reviews, in real numbers', 'Included', 'inc'),
]
S = {k: v for k, *v in [(s[0],) + s[1:] for s in SVCS]}

def tag(a):
    _, _, _, _, p, k = next(s for s in SVCS if s[0] == a)
    return f'<span class="sv-tag sv-{k}">{p}</span>'

SAMPLE = '<span class="sv-sample">Sample</span>'

# ---------- product sketches ----------
def v_molly():
    return f'''<div class="vz vz-call" aria-hidden="true">{SAMPLE}
<div class="vz-row"><span class="vz-live"></span><b>Incoming call</b><span class="vz-t">9:47 PM</span></div>
<p class="vz-q">“Hi, my AC is running but blowing warm air.”</p>
<p class="vz-a">“Sorry about that. I have Wednesday at 8 AM open. Does that work?”</p>
<div class="vz-ticket"><span class="vz-ok">{CHK}</span><div><b>Visit booked</b><span>Wed 8:00 AM · Maria G. · 214 Oak Ln</span></div></div>
</div>'''

def v_chat():
    return f'''<div class="vz vz-msg" aria-hidden="true">{SAMPLE}
<div class="vz-bub in">Do you service Allen? Heater’s making a loud noise.</div>
<div class="vz-bub out">Yes, we cover Allen. I can book a visit Thursday at 10 AM or 2 PM. Which works?</div>
<div class="vz-bub in">2 PM please</div>
<div class="vz-chip">{CHK} Booked · Thu 2:00 PM</div>
</div>'''

def v_remind():
    return f'''<div class="vz vz-sms" aria-hidden="true">{SAMPLE}
<span class="vz-from">ABC Heating &amp; Air</span>
<div class="vz-bub in">Reminder: your visit is tomorrow, 8–10 AM. Reply here to cancel or change.</div>
<span class="vz-meta">Sent the day before</span>
</div>'''

def v_review():
    return f'''<div class="vz vz-sms" aria-hidden="true">{SAMPLE}
<div class="vz-row"><span class="vz-done">{CHK} Job done</span><span class="vz-t">2:10 PM</span></div>
<div class="vz-bub in">Thanks for choosing ABC Heating &amp; Air, Maria. If you have a minute, a Google review would mean a lot: <u>g.page/abc-heating/review</u></div>
<span class="vz-meta">Same message to every customer</span>
</div>'''

def v_tuneup():
    return f'''<div class="vz vz-mail" aria-hidden="true">{SAMPLE}
<span class="vz-from">From ABC Heating &amp; Air</span>
<b class="vz-subj">Time for your heating check</b>
<p>Cold nights are coming. Book your furnace tune-up before the first freeze.</p>
<span class="vz-btn">Book a tune-up</span>
</div>'''

def v_estimate():
    steps = [('Day 0', 'Estimate sent', ''), ('Day 2', 'Short follow-up', ''), ('Day 5', 'Second note', ''), ('Day 10', 'Last note, then it stops', 'end')]
    li = ''.join(f'<li class="{c}"><time>{d}</time><span>{t}</span></li>' for d, t, c in steps)
    return f'<div class="vz vz-steps" aria-hidden="true">{SAMPLE}<ol>{li}</ol></div>'

def v_gbp():
    items = ['Photos of real jobs and trucks', 'Every service you offer', 'Hours and service area', 'Replies to recent reviews']
    li = ''.join(f'<li>{CHK}<span>{t}</span></li>' for t in items)
    return f'''<div class="vz vz-gbp" aria-hidden="true">{SAMPLE}
<div class="vz-gh"><span class="vz-av">A</span><div><b>ABC Heating &amp; Air</b><span>HVAC contractor</span></div></div>
<ul>{li}</ul></div>'''

def v_web():
    return f'''<div class="vz vz-phone" aria-hidden="true">{SAMPLE}
<div class="vz-scr"><div class="vz-nav"><b>ABC Heating &amp; Air</b><span>☰</span></div>
<p class="vz-h">AC and heating repair in your area</p>
<span class="vz-cta">Call now</span><span class="vz-cta2">Book a visit</span>
<p class="vz-small">Licensed · Upfront diagnostic fee</p></div></div>'''

def v_report():
    rows = [('Calls answered', '42'), ('Jobs booked', '11'), ('Review requests sent', '9'), ('Answered after hours', '17')]
    li = ''.join(f'<li><span>{a}</span><b>{b}</b></li>' for a, b in rows)
    return f'''<div class="vz vz-rep" aria-hidden="true">{SAMPLE}
<div class="vz-row"><b>October report</b><span class="vz-t">ABC Heating &amp; Air</span></div>
<ul>{li}</ul></div>'''

VIS = {'molly': v_molly, 'chat': v_chat, 'reminders': v_remind, 'reviews': v_review, 'tuneups': v_tuneup,
       'estimates': v_estimate, 'gbp': v_gbp, 'website': v_web, 'report': v_report}

COPY = {
 'molly': ('Every call answered, any hour',
           'When your team can’t pick up, Molly answers with your company name, takes the details, checks the ZIP is in your area and books the visit on your calendar. You get a text with everything.'),
 'chat': ('Messages answered like phone calls',
          'Someone messages your website or Facebook page at night. They get a reply in minutes and a time on your calendar.'),
 'reminders': ('Fewer no-shows',
               'Customers get a reminder the day before, and can cancel or change by replying.'),
 'reviews': ('More reviews from the jobs you already did',
             'Tap “Job done” and your customer gets a thank-you with your Google review link. Every customer gets the same request.'),
 'tuneups': ('Fill slow weeks with tune-ups',
             'Before summer and winter, past customers who agreed to hear from you get a reminder to book their check.'),
 'estimates': ('Win back quiet estimates',
               'Gave a price and heard nothing? Three short, polite notes go out, then it stops.'),
 'gbp': ('Look right when they find you on Google',
         'We update your photos, services, hours and service area, and help you reply to reviews. Google decides rankings, so we never promise a position.'),
 'website': ('A site built to make the phone ring',
             'Mobile-first, on your own domain, with tap-to-call and a booking form. You see a free design preview before you pay anything.'),
 'report': ('Know what’s working',
            'One page a month: calls answered, jobs booked and review requests sent. Real counts only.'),
}

PHOTO = {'answer': ('homeowner-call', 'Homeowner smiling while on a phone call at home'),
         'grow': ('front-door-visit', 'Homeowner greeting a visitor at her front door'),
         'show': ('homeowner-phone', 'Man on his sofa looking something up on his phone')}

GROUPS = [
 ('answer', 'Answer', 'Never miss a job', 'Every call and message gets a fast answer and a time on your calendar.', 'molly', ['chat', 'reminders']),
 ('grow', 'Grow', 'Get more from the customers you already have', 'Finished jobs turn into reviews, and past customers come back.', 'reviews', ['tuneups', 'estimates']),
 ('show', 'Show up', 'Look good online and see the numbers', 'Make the first impression count, and know what you got each month.', 'website', ['gbp', 'report']),
]

VZT = {'molly': 'Molly · live call', 'chat': 'Website chat', 'reminders': 'Text to customer', 'reviews': 'After the job',
       'tuneups': 'Email to past customer', 'estimates': 'Estimate follow-up', 'gbp': 'Google profile checklist',
       'website': 'Your new site', 'report': 'Monthly report'}

def chrome(a, html):
    i = html.index('>') + 1
    j = html.rindex('</div>')
    inner = html[i:j].replace(SAMPLE, '', 1)
    open_tag = html[:i]
    return (open_tag + f'<div class="vz-chrome"><i></i><i></i><i></i><b>{VZT[a]}</b><em>Demo · sample data</em></div>'
            + f'<div class="vz-body">{inner}</div></div>')

def card(a, big=False):
    _, icn, name, _, _, _ = next(s for s in SVCS if s[0] == a)
    h, p = COPY[a]
    return f'''<article class="sv-card{' sv-big' if big else ''}" id="{a}">
<div class="sv-txt"><div class="sv-top"><span class="sv-ic">{ic(I[icn])}</span>{tag(a)}</div>
<p class="sv-name">{name}</p><h3>{h}</h3><p>{p}</p></div>
<div class="sv-vis">{chrome(a, VIS[a]())}</div></article>'''

def hero():
    j = [('9:47 PM', 'phone', 'Molly answers and books Wednesday 8 AM'),
         ('Tue', 'bell', 'Reminder text the day before'),
         ('Wed', 'star', 'Job done, review request sent'),
         ('Next fall', 'cal', 'Tune-up reminder goes out')]
    li = ''.join(f'<li><span class="hj-ic">{ic(I[k], 16)}</span><div><time>{t}</time><b>{d}</b></div></li>' for t, k, d in j)
    return f'''<section class="sv-hero"><div class="wrap sv-hin">
<div class="sv-htx">
<p class="eyebrow">Services</p>
<h1>One call, handled from first ring to five-star review</h1>
<p class="sv-lead">Molly answers your phone and books the job. Then reminders, review requests and follow-ups keep that customer coming back. We set it all up for you.</p>
<div class="sv-ctas"><a class="btn" href="/#start">Start the 14-day free trial</a><a class="sv-call" href="tel:+15705219710">Hear Molly: (570) 521-9710</a></div>
</div>
<figure class="sv-journey" aria-label="Sample: one customer, from first call to tune-up reminder">
<div class="hj-head"><span>One customer, Maria G.</span>{SAMPLE}</div>
<ol>{li}</ol>
</figure>
</div></section>'''

def index():
    cols = ''
    for gid, kick, title, _, big, small in GROUPS:
        items = ''.join(f'<li><a href="#{a}"><span class="si-ic">{ic(I[next(s for s in SVCS if s[0]==a)[1]], 18)}</span><span class="si-n">{next(s for s in SVCS if s[0]==a)[2]}</span>{tag(a)}</a></li>' for a in [big] + small)
        cols += f'<div class="si-col"><p class="si-k">{kick}</p><ul>{items}</ul></div>'
    return f'<section class="sv-index" aria-label="All nine services"><div class="wrap"><div class="si">{cols}</div></div></section>'

def groups():
    out = ''
    for n, (gid, kick, title, sub, big, small) in enumerate(GROUPS):
        out += f'''<section class="sv-group{' alt' if n % 2 == 0 else ''}" id="{gid}"><div class="wrap">
<div class="sv-gh"><p class="eyebrow dk">{kick}</p><h2>{title}</h2><p>{sub}</p></div>
<div class="sv-grid">{card(big, True)}{''.join(card(a) for a in small)}</div>
</div></section>'''
    return out

def included():
    inc = [s for s in SVCS if s[5] == 'inc']
    add = [s for s in SVCS if s[5] == 'add']
    li1 = ''.join(f'<li>{CHK}<span>{s[2]}</span></li>' for s in inc)
    li2 = ''.join(f'<li><span>{s[2]}</span><b>{s[4]}</b></li>' for s in add)
    return f'''<section class="sv-price"><div class="wrap">
<div class="sv-gh"><p class="eyebrow dk">Pricing</p><h2>Most of it comes with your plan</h2>
<p>Molly is $79 a month plus $29 per booked job, or $249 a month flat. Everything on the left is included on both.</p></div>
<div class="sp">
<div class="sp-c"><h3>Included on every plan</h3><ul class="sp-inc">{li1}</ul></div>
<div class="sp-c"><h3>Add when you want them</h3><ul class="sp-add">{li2}</ul><p class="sp-n">Take tune-up reminders and estimate follow-up together for $79 a month.</p></div>
</div>
<p class="sp-foot">Texts to customers start once your number is registered for business texting. We handle that during setup. <a href="/pricing/">See full pricing</a></p>
</div></section>'''

FAQ = [
 ('Do I have to use all of them?', 'No. Molly is the core. Turn on the included services you want, and add the paid ones only if they fit your shop.'),
 ('Who sets it up?', 'We do. You answer a short checklist and listen to a test call. Changes are a text away and done by the next business day.'),
 ('When do customer texts start?', 'Once your number is registered for business texting, which we handle during setup. Until then, Molly still answers and books calls.'),
 ('Do you text people who never contacted me?', 'Never. Reminders and follow-ups only go to your own customers, and tune-up reminders only to customers who agreed to hear from you.'),
]

def faq():
    qs = ''.join(f'<details class="fq"><summary>{q}<i aria-hidden="true">+</i></summary><p>{a}</p></details>' for q, a in FAQ)
    return f'<section class="sv-faq"><div class="wrap"><div class="sv-gh"><h2>Questions</h2></div><div class="prfaq">{qs}</div></div></section>'

def cta():
    return '''<section class="sv-end"><div class="wrap"><div class="sv-endin">
<h2>Start with Molly. Add the rest when you’re ready.</h2>
<p>Free for 14 days. We set it up, you keep your number.</p>
<div class="sv-ctas"><a class="btn" href="/#start">Start the 14-day free trial</a><a class="sv-call" href="tel:+15705219710">Call Molly: (570) 521-9710</a></div>
</div></div></section>'''

def home_block():
    tiles = ''.join(f'<a class="hs-t" href="/services/#{a}"><span class="si-ic">{ic(I[icn], 18)}</span><b>{name}</b><span class="hs-d">{d}</span>{tag(a)}</a>' for a, icn, name, d, _, _ in SVCS)
    return f'''<section class="sec" id="services"><div class="wrap">
<div class="sec-head"><p class="eyebrow-d">Everything we do</p><h2>Molly answers. The rest keeps customers coming back.</h2><p class="lead">One setup, nine ways to book more work. Most of it is included on your plan.</p></div>
<div class="hs">{tiles}</div>
<a class="hs-more" href="/services/">See every service</a>
</div></section>'''

CSS = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'services.css')).read() if os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'services.css')) else ''

def jsonld():
    svc = {'@context': 'https://schema.org', '@type': 'ItemList', 'name': 'BookedOrion services for HVAC shops', 'url': URL,
           'itemListElement': [{'@type': 'ListItem', 'position': i + 1, 'item': {'@type': 'Service', 'name': s[2], 'description': s[3],
                                'provider': {'@type': 'Organization', 'name': 'BookedOrion', 'url': 'https://bookedorion.com/'}, 'url': URL + '#' + s[0]}}
                               for i, s in enumerate(SVCS)]}
    faqld = {'@context': 'https://schema.org', '@type': 'FAQPage', 'mainEntity': [
        {'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in FAQ]}
    crumbs = {'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': [
        {'@type': 'ListItem', 'position': 1, 'name': 'Home', 'item': 'https://bookedorion.com/'},
        {'@type': 'ListItem', 'position': 2, 'name': 'Services', 'item': URL}]}
    return ''.join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in (svc, faqld, crumbs))

def build():
    shell = open(os.path.join(ROOT, 'about', 'index.html')).read()
    he = shell.index('</head>')
    head = shell[:he]
    head = re.sub(r'<title>.*?</title>', f'<title>{TITLE}</title>', head)
    for k in ('name="description"', 'property="og:description"'):
        head = re.sub(rf'(<meta {k} content=")[^"]*', lambda m: m.group(1) + DESC, head)
    head = re.sub(r'(<meta property="og:title" content=")[^"]*', lambda m: m.group(1) + TITLE, head)
    head = head.replace('content="article"', 'content="website"').replace('https://bookedorion.com/about/', URL)
    head = head.replace('<link rel="stylesheet" href="/about/about.css?v=1">',
                        '<link rel="stylesheet" href="/pricing/pricing.css?v=1">\n<link rel="stylesheet" href="/services/services.css?v=1">')
    head = re.sub(r'<script type="application/ld\+json">.*?</script>', '', head, flags=re.S) + jsonld() + '\n'
    rest = shell[he:]
    header = rest[:rest.index('<main>')].replace('class="nav on" href="/about/"', 'class="nav" href="/about/"')
    header = header.replace('class="nav" href="/services/"', 'class="nav on" href="/services/"')
    footer = rest[rest.index('</main>'):]
    main = '<main class="svp">' + hero() + index() + groups() + included() + faq() + cta()
    out = os.path.join(ROOT, 'services')
    os.makedirs(out, exist_ok=True)
    open(os.path.join(out, 'index.html'), 'w').write(head + header + main + footer)
    open(os.path.join(out, 'services.css'), 'w').write(CSS)
    open(os.path.join(ROOT, '_source', 'home_services_block.html'), 'w').write(home_block())
    print('built /services/')

if __name__ == '__main__':
    build()
