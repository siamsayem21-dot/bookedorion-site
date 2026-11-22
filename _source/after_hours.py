#!/usr/bin/env python3
"""Builds /after-hours-answering-hvac/ for bookedorion.com.

Standalone like pricing.py: borrows head, header and footer from the published /about/ page.
Run from the repo root:  python3 _source/after_hours.py
Facts come from 00_LOCKED_RULEBOOK.md, the Terms page and /getting-started/.
No emergency-transfer claim (rulebook C6), no competitor names (C7), no made-up stats.
"""
import json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pricing import li, CHECK, ROOT

PATH = '/after-hours-answering-hvac/'
URL = 'https://bookedorion.com' + PATH
TITLE = 'After-Hours Answering Service for HVAC | BookedOrion'
DESC = ('Molly answers your HVAC calls at night, on weekends and holidays, books jobs on your calendar '
        'and texts you. From $49 a month + $29 per booked job.')
LSA = 'https://support.google.com/localservices/answer/7527305?hl=en'

STEPS = [
    ('9:47 PM', 'The call comes in', 'Your office is closed, so the call forwards to Molly. Your number stays the same.'),
    ('9:47 PM', 'Molly answers', '“Thanks for calling ABC Heating & Air. This is Molly, the AI assistant. This call may be recorded.”'),
    ('9:48 PM', 'She takes the details', 'Name, callback number, address, the problem and the type of system. She checks the ZIP is in your area and mentions your diagnostic fee.'),
    ('9:49 PM', 'The job is booked', 'She offers open slots from your calendar. The caller picks Wednesday at 8 AM, and she reads it back.'),
    ('9:50 PM', 'You get a text', 'Name, address, problem and time, with one tap to confirm. The recording and transcript are saved.'),
]

RULES = [
    ('Gas smell or carbon monoxide', 'Safety first. Molly tells the caller to get outside and call 911 and the gas company from outside. She doesn’t book a routine visit.'),
    ('Urgent for your shop', 'You choose the words that make a call urgent, like no heat with an elderly person at home. Molly follows the rule you set and the call is marked urgent in your text.'),
    ('Everything else', 'Booked into the first open slot on your calendar, usually the next morning. You wake up to a list, not a voicemail box.'),
]

FAQ = [
    ('How much does after-hours answering cost?',
     'Night-only is $49 a month plus $29 per booked job, for nights, weekends and holidays. If you also want Molly to pick up '
     'the calls your team misses during the day, Pay-per-Job is $79 a month plus $29 per booked job (never more than $449), '
     'or Flat is $249 a month. Every plan starts with a free 14-day trial, with no setup fee and no contract.'),
    ('Will callers know they’re talking to an AI?',
     'Yes. Molly says she’s an AI assistant and that the call may be recorded, at the start of every call.'),
    ('Do I keep my phone number?',
     'Yes. Your calls forward to Molly when you’re closed. To turn her off, you cancel the forwarding.'),
    ('What does Molly do with a gas smell or carbon monoxide call?',
     'She tells the caller to get outside and call 911 and the gas company from outside. She doesn’t book a routine visit, '
     'and the call is marked urgent in your text.'),
    ('Does she cover weekends and holidays?',
     'Yes. Night-only covers nights, weekends and holidays. You set the hours during setup. To change them later, send us a text and it’s done by the next business day.'),
    ('Which calendar does she book on?',
     'Your Google or Outlook calendar. She doesn’t connect directly to ServiceTitan, Jobber or Housecall Pro yet.'),
    ('Does Molly quote prices?',
     'Only the diagnostic or trip fee you approve. She never guesses a repair price.'),
    ('Does Molly speak Spanish?',
     'Not yet. We’ll only offer it once it passes our tests.'),
    ('Are spam and wrong-number calls billed?',
     'Never.'),
]

def hero():
    return '''<section class="bhero"><div class="wrap prh">
<div class="eyebrow">After-hours answering</div>
<h1>After-hours answering for HVAC shops</h1>
<p>When your office closes, Molly answers. She takes the caller’s details, books the job on your calendar and texts you a summary. Your team keeps the daytime calls.</p>
<div class="prh-cta"><a class="btn" href="/#start">Start free trial</a><a class="prh-call" href="tel:+15705219710">Or call Molly: (570) 521-9710</a></div>
</div></section>'''

def short():
    return '''<section class="blk"><div class="ahs"><h2>In short</h2>
<p>BookedOrion is an AI receptionist built only for HVAC. After you close, your calls forward to Molly. She says she’s an AI, asks what’s wrong, checks the address is in your service area, books the next open slot on your Google or Outlook calendar and texts you the details. Night-only costs $49 a month plus $29 per booked job, with a free 14-day trial.</p></div></section>'''

def timeline():
    items = ''.join(f'<li><time>{t}</time><div><b>{h}</b><p>{d}</p></div></li>' for t, h, d in STEPS)
    return f'''<section class="blk"><div class="bh"><div class="eyebrow dk">One call</div><h2>A 9:47 PM call, start to finish</h2>
<p>A homeowner’s AC is blowing warm air. Here’s what happens.</p></div>
<ol class="aht">{items}</ol>
<p class="prn">Sample call for illustration. See every step on <a href="/how-it-works/">How it works</a>.</p></section>'''

def rules():
    cards = ''.join(f'<div class="ahr{" ahr-s" if i == 0 else ""}"><h3>{t}</h3><p>{d}</p></div>' for i, (t, d) in enumerate(RULES))
    return f'''<section class="blk"><div class="bh"><div class="eyebrow dk">Your rules</div><h2>You decide what counts as urgent</h2>
<p>Not every late call is an emergency. During setup, you tell us how to handle each kind.</p></div>
<div class="ahrs">{cards}</div>
<p class="prn">Molly is an AI assistant, not an emergency service. She doesn’t replace 911, your gas utility or your judgment.</p></section>'''

def hours():
    return f'''<section class="blk"><div class="bh"><div class="eyebrow dk">Your hours</div><h2>Nights only, or nights plus the calls you miss</h2></div>
<div class="prp">
<article class="prc is-main"><div class="prc-top"><h3>Night-only</h3></div>
<p class="prc-sub">Your office answers by day. Molly takes over when you close.</p>
<div class="prc-price"><b>$49</b><span>a month + $29 per booked job</span></div>
<ul class="prc-facts">{li(['Nights, weekends and holidays', 'Your team keeps every daytime call', 'Best if someone answers the office phone all day'])}</ul>
<a class="btn" href="/#start">Start free trial</a></article>
<article class="prc"><div class="prc-top"><h3>All day, team first</h3></div>
<p class="prc-sub">Your team gets about 10–15 seconds to answer. If nobody picks up, Molly does.</p>
<div class="prc-price"><b>$79</b><span>a month + $29 per booked job, or $249 flat</span></div>
<ul class="prc-facts">{li(['Every after-hours call', 'Plus the calls your team misses on a busy day', 'Best if the owner is also the one answering'])}</ul>
<a class="btn btn-line" href="/pricing/">See both plans</a></article>
</div>
<p class="prn">Same setup and features on every plan. Spam and wrong-number calls are never counted. <a href="/pricing/">Full pricing and bill calculator</a></p></section>'''

def why():
    return f'''<section class="blk"><div class="bh"><div class="eyebrow dk">Why it matters</div><h2>A missed call at night is often a job for someone else</h2>
<p>A homeowner with no heat at 10 PM may not wait for a call back in the morning. If they can’t reach you, the next shop is one tap away.</p>
<p>If you run Google Local Services Ads, Google’s own help page lists your responsiveness as a ranking factor and says <q>Missed calls may negatively affect your responsiveness.</q> Answering after hours is one way to miss fewer. Google decides rankings, so we never promise a position.</p>
<p class="ahsrc">Source: <a href="{LSA}" rel="nofollow noopener" target="_blank">Google Local Services Ads Help, “About ad rankings”</a></p>
<p><a href="/blog/answering-service-vs-ai-receptionist/">Comparing options? Read answering service vs AI receptionist</a></p></div></section>'''

def setup():
    return '''<section class="blk"><div class="bh"><div class="eyebrow dk">Setup</div><h2>About 30 minutes of your time</h2>
<p>We build Molly for your hours, fees, service area and emergency rules, connect your calendar and run test calls. You answer a short checklist, listen to a test call, and turn on call forwarding with one code or setting. We stay on the phone with you while you do it.</p>
<p><a href="/getting-started/">See the setup plan, step by step</a></p></div></section>'''

def faq():
    qs = ''.join(f'<details class="fq"><summary>{q}<i aria-hidden="true">+</i></summary><p>{a}</p></details>' for q, a in FAQ)
    return f'<section class="blk"><div class="bh"><div class="eyebrow dk">Questions</div><h2>After-hours answering questions</h2></div><div class="prfaq">{qs}</div></section>'

def cta():
    return '''<section class="blk"><div class="prend"><h2>Stop sending night calls to voicemail</h2>
<p>Try Molly free for 14 days. You keep your number and learn no new software.</p>
<div class="prh-cta"><a class="btn" href="/#start">Start free trial</a><a class="prh-call" href="tel:+15705219710">Call Molly: (570) 521-9710</a></div></div></section>'''

CSS = '''.ahs{background:#fff;border:1px solid var(--line);border-left:4px solid var(--mint);border-radius:16px;padding:24px 28px;display:flex;flex-direction:column;gap:10px;max-width:860px}
.ahs h2{margin:0;font-size:20px;font-weight:600}
.ahs p{margin:0;font-size:18px;line-height:1.65;color:var(--ink)}
.aht{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;max-width:860px}
.aht li{display:grid;grid-template-columns:88px 1fr;gap:20px;padding:18px 0;border-top:1px solid var(--line)}
.aht li:first-child{border-top:0}
.aht time{font-weight:600;color:var(--indigo);font-variant-numeric:tabular-nums;padding-top:2px}
.aht b{font-size:18px;font-weight:600}
.aht p{margin:4px 0 0;color:var(--muted);line-height:1.6}
.aht li:last-child time{color:var(--mintdk)}
.ahrs{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px}
.ahr{background:#fff;border:1px solid var(--line);border-radius:18px;padding:22px;display:flex;flex-direction:column;gap:8px}
.ahr h3{margin:0;font-size:18px;font-weight:600}
.ahr p{margin:0;color:var(--muted);line-height:1.6}
.ahr-s{border-color:var(--amber);background:var(--ambersoft)}
.ahr-s h3{color:var(--amber)}
.ahsrc{font-size:15px!important}
q{quotes:"“" "”"}
@media (max-width:760px){.ahrs{grid-template-columns:1fr}.aht li{grid-template-columns:1fr;gap:4px}.ahs{padding:20px}}
'''

def jsonld():
    service = {'@context': 'https://schema.org', '@type': 'Service', 'name': 'After-hours answering for HVAC companies',
               'serviceType': 'After-hours answering service', 'url': URL,
               'provider': {'@type': 'Organization', 'name': 'BookedOrion', 'url': 'https://bookedorion.com/'},
               'description': 'An AI receptionist that answers HVAC calls at night, on weekends and holidays, books jobs on the shop’s calendar and texts the owner a summary.',
               'offers': {'@type': 'Offer', 'name': 'Night-only', 'price': '49', 'priceCurrency': 'USD', 'url': 'https://bookedorion.com/pricing/',
                          'description': '$49 per month plus $29 per booked job. Nights, weekends and holidays. 14-day free trial.'}}
    faqld = {'@context': 'https://schema.org', '@type': 'FAQPage', 'mainEntity': [
        {'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in FAQ]}
    crumbs = {'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': [
        {'@type': 'ListItem', 'position': 1, 'name': 'Home', 'item': 'https://bookedorion.com/'},
        {'@type': 'ListItem', 'position': 2, 'name': 'After-hours answering', 'item': URL}]}
    return ''.join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in (service, faqld, crumbs))

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
                        '<link rel="stylesheet" href="/pricing/pricing.css?v=1">\n<link rel="stylesheet" href="/after-hours-answering-hvac/ah.css?v=1">')
    head = re.sub(r'<script type="application/ld\+json">.*?</script>', '', head, flags=re.S) + jsonld() + '\n'
    rest = shell[he:]
    header = rest[:rest.index('<main>')].replace('class="nav on" href="/about/"', 'class="nav" href="/about/"')
    footer = rest[rest.index('</main>'):]
    main = ('<main>' + hero() + '<div class="wrap pg">' + short() + timeline() + rules() + hours() + why()
            + setup() + faq() + cta() + '</div>')
    out = os.path.join(ROOT, PATH.strip('/'))
    os.makedirs(out, exist_ok=True)
    open(os.path.join(out, 'index.html'), 'w').write(head + header + main + footer)
    open(os.path.join(out, 'ah.css'), 'w').write(CSS)
    print('built', PATH, len(DESC), 'char desc')

if __name__ == '__main__':
    build()
