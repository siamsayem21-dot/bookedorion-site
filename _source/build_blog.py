#!/usr/bin/env python3
"""Builds the BookedOrion blog (static pages) into ../site/blog."""
import json, os, html

OUT = os.path.join(os.path.dirname(__file__), '..', 'site')
SITE = 'https://bookedorion.com'
DATE = '2026-10-21'
DATE_H = 'Oct 21, 2026'
AUTHOR = 'Siam Ahmed'
CSSV = '10'
FONTS = '<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">'

LOGO = ('<a href="/" class="logo" aria-label="BookedOrion home"><span>Booked</span>'
        '<svg width="22" height="22" viewBox="0 0 64 64" aria-hidden="true"><circle cx="32" cy="32" r="26" fill="none" stroke="#2BD9A0" stroke-width="8"/>'
        '<path d="M21 33 L29 41 L44 23" fill="none" stroke="#FFFFFF" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/></svg><span>rion</span></a>')

BANNER = ''
HEADER = BANNER + f'''<header class="top"><div class="wrap topin">{LOGO}
<nav><a class="nav" href="/how-it-works/">How it works</a><a class="nav" href="/#pricing">Pricing</a><a class="nav" href="/about/">About</a><a class="nav on" href="/blog/">Blog</a><a class="ncall" href="tel:+15705219710" aria-label="Call Molly at (570) 521-9710"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#2BD9A0" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.91.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92z"/></svg><span>(570) 521-9710</span></a><a class="btn" href="/#start">Start free trial</a></nav></div></header>'''

FOOTER = '''<footer class="foot"><div class="wrap footin">
<div class="fb"><div class="flogo">Booked<svg width="20" height="20" viewBox="0 0 64 64" aria-hidden="true"><circle cx="32" cy="32" r="26" fill="none" stroke="#2BD9A0" stroke-width="8"/><path d="M21 33 L29 41 L44 23" fill="none" stroke="#FFFFFF" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/></svg>rion</div>
<p>Every missed call answered, day or night. The AI receptionist made for HVAC shops.</p>
<a class="fcall" href="tel:+15705219710">Call Molly: (570) 521-9710</a><a class="btn" href="/#start">Start free trial</a></div>
<div class="fcols"><div class="fcol"><div class="fh">PRODUCT</div><a href="/#demo">Hear Molly</a><a href="/how-it-works/">How it works</a><a href="/#pricing">Pricing</a><a href="/getting-started/">Getting started</a></div><div class="fcol"><div class="fh">COMPANY</div><a href="/about/">About</a><a href="/blog/">Blog</a><a href="mailto:siam@bookedorion.com">Contact</a><a href="/#start">Free trial</a></div><div class="fcol"><div class="fh">LEGAL</div><a href="/privacy/">Privacy</a><a href="/terms/">Terms</a><a href="/sms-terms/">SMS terms</a></div></div>
</div><div class="wrap copy"><span>© 2026 BookedOrion. All rights reserved.</span><span>AI receptionist for HVAC shops</span></div></footer>'''

CTA = '''<aside class="cta"><div class="ctak">FREE 14-DAY TRIAL</div>
<h2>Let Molly catch the calls your team misses.</h2>
<p>She answers when you can’t, books the visit on your calendar and texts you the details. Free for 14 days. No setup fee, no contract.</p>
<div class="ctab"><a class="btn big" href="/#start">Start free trial</a><a class="ghost" href="tel:+15705219710">Call Molly: (570) 521-9710</a></div></aside>'''

def head(title, desc, path, extra=''):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{SITE}{path}">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:type" content="{'article' if path != '/blog/' else 'website'}">
<meta property="og:url" content="{SITE}{path}">
<meta property="og:image" content="https://bookedorion.com/og-image.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0B0A24">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
{FONTS}
<link rel="stylesheet" href="/blog/blog.css?v={CSSV}">
{extra}
</head>
<body>
'''

# ---------------- articles ----------------
POSTS = [
 dict(
  slug='missed-calls-after-hours',
  cat='Phones & calls',
  title='What really happens when your HVAC shop misses a call after hours',
  desc='A homeowner with a dead AC rarely leaves a voicemail. Here is what happens to that call, what it costs, and four ways to stop losing it.',
  read='5 min read',
  body='''
<p class="lede">It’s 9:47 PM in July. A homeowner in Plano walks into a hot house, finds the AC blowing warm air and calls the first HVAC shop on Google. Your phone rings. Nobody answers. What happens next decides whether you get that job.</p>

<h2>Most people don’t leave a voicemail</h2>
<p>When a call goes to voicemail, most callers hang up. One call-handling company looked at call data from 10,000 businesses and found that <strong>69% of callers who reach voicemail don’t leave a message</strong> (Moneypenny, 2016). The same report found that a third of small businesses surveyed didn’t answer incoming calls at all.</p>
<p>That data is a few years old and isn’t HVAC-specific. But ask any homeowner with no cooling what they do when a shop doesn’t pick up. They don’t wait. They call the next number.</p>

<h2>The after-hours call is usually a real job</h2>
<p>Nobody calls an HVAC company at 9 PM to chat. After-hours calls tend to be the urgent ones: no cooling, no heat, a strange noise, water under the air handler. These callers are ready to book. That’s exactly why losing them hurts.</p>

<h2>What one missed call costs you</h2>
<p>Do the math with your own numbers. Take the calls you miss in a normal week, multiply by how many would have booked, then by your average ticket.</p>
<div class="calc">
<div><span>Missed calls a week</span><b>8</b></div>
<div><span>Share that would book</span><b>40%</b></div>
<div><span>Average job value</span><b>$350</b></div>
<div class="tot"><span>Lost per month (about)</span><b>$4,850</b></div>
</div>
<p class="note">Example numbers only: 8 × 4.33 weeks × 40% × $350. Plug in yours with the calculator on our <a href="/#start">home page</a>.</p>

<h2>Four ways to stop losing these calls</h2>
<h3>1. Forward to your own cell</h3>
<p>Free, and it works until you’re on a roof, under a house or asleep. It also means you never really clock out.</p>
<h3>2. A live answering service</h3>
<p>A person answers, which callers like. Many services take a message instead of booking the job, and per-minute pricing climbs fast in summer. We compare costs in <a href="/blog/answering-service-vs-ai-receptionist/">this guide</a>.</p>
<h3>3. A night-shift CSR</h3>
<p>The best experience, and the most expensive. Most small shops can’t justify a full-time person for nights and weekends.</p>
<h3>4. An AI receptionist</h3>
<p>Answers every call in seconds, any hour, and can book straight onto your calendar. It should say it’s an AI, follow your rules for emergencies and hand tricky callers to a human. That’s how Molly works.</p>

<h2>A simple fix you can do tonight</h2>
<ul class="list">
<li>Change your voicemail greeting to name your company and say when you’ll call back.</li>
<li>Write down which calls count as emergencies (start with our <a href="/blog/hvac-emergency-call-triage/">triage list</a>).</li>
<li>Count how many calls you miss this week. Your phone’s call log has the answer.</li>
</ul>
''',
  sources=[('Moneypenny: Small business call report (2016)','https://moneypenny.com/us/resources/news/small-business-call-report/')],
 ),
 dict(
  slug='answering-service-vs-ai-receptionist',
  art=('vs','Answering service','AI receptionist'),
  cat='Guides',
  title='Answering service vs. AI receptionist: an honest comparison for HVAC shops',
  desc='Live answering services and AI receptionists both answer your phone. Here is how they compare on cost, booking, emergencies and caller experience.',
  read='6 min read',
  body='''
<p class="lede">If your phone goes unanswered on nights, weekends or busy afternoons, you have two common options: pay a live answering service, or use an AI receptionist. Both have a place. Here’s a straight comparison.</p>

<h2>How each one works</h2>
<p><strong>A live answering service</strong> routes your calls to a shared team of receptionists. They follow your script, take messages and, on some plans, book appointments.</p>
<p><strong>An AI receptionist</strong> is software that answers in a natural voice, asks the caller questions and can book directly onto your calendar. A good one says it’s an AI and hands off to a human when needed.</p>

<h2>Cost: per minute vs. flat monthly</h2>
<p>Many live services charge by the minute. As one example, published pricing for one well-known US virtual receptionist service ranged from <strong>$245 a month for 50 minutes</strong> to <strong>$705 a month for 200 minutes</strong>, with extra minutes billed at roughly $4–5 each (as reported in December 2025; check current prices with the provider).</p>
<p>That matters for HVAC because call volume isn’t steady. When the first heat wave hits, calls jump, and a per-minute bill jumps with them.</p>
<p>AI receptionists are usually priced per month with a call allowance, so a busy week costs about the same as a quiet one.</p>

<div class="tablewrap"><table>
<thead><tr><th></th><th>Live answering service</th><th>AI receptionist</th></tr></thead>
<tbody>
<tr><td>Pricing</td><td>Often per minute</td><td>Usually flat monthly</td></tr>
<tr><td>Answers</td><td>Yes, by a person</td><td>Yes, in seconds, any hour</td></tr>
<tr><td>Books the job</td><td>Often takes a message</td><td>Can book on your calendar</td></tr>
<tr><td>Summer rush</td><td>Hold times and higher bills</td><td>Answers many calls at once</td></tr>
<tr><td>Knows HVAC</td><td>Depends on the script and agent</td><td>Depends on how it’s set up</td></tr>
<tr><td>Upset callers</td><td>Human empathy</td><td>Should hand off to you</td></tr>
</tbody></table></div>

<h2>Where a live service still wins</h2>
<ul class="list">
<li>Callers who strongly prefer a human from the first second.</li>
<li>Complicated situations that don’t fit any script.</li>
<li>Businesses that only need messages taken, not jobs booked.</li>
</ul>

<h2>Where an AI receptionist wins</h2>
<ul class="list">
<li>Every call answered right away, even when ten come in at once.</li>
<li>The job gets booked, not just written down for tomorrow.</li>
<li>Predictable monthly cost, even in July.</li>
<li>A text summary of every call on your phone.</li>
</ul>

<h2>Five questions to ask any provider</h2>
<ol class="list">
<li>Does it book the appointment, or only take a message?</li>
<li>What happens on a gas smell or no-heat call with an elderly caller?</li>
<li>How does it pass an upset caller to a real person?</li>
<li>What does a 2× busier month cost me?</li>
<li>Can I listen to recordings and read summaries of every call?</li>
</ol>

<h2>Our take</h2>
<p>We built BookedOrion because most HVAC shops don’t need a message taker. They need the job booked. Molly answers when your team can’t, follows your emergency rules and texts you every booking. Try it free for 14 days and judge it on real calls.</p>
''',
  sources=[('Vida: virtual receptionist pricing guide (Dec 2025)','https://vida.io/blog/ruby-receptionists-pricing')],
 ),
 dict(
  slug='hvac-emergency-call-triage',
  art=('3','Levels of','call urgency'),
  cat='Guides',
  title='Emergency or not? A simple call triage list for HVAC shops',
  desc='A plain triage list for HVAC calls: what needs action right now, what can be booked for tomorrow, and what to tell callers about gas and carbon monoxide.',
  read='4 min read',
  body='''
<p class="lede">Not every after-hours call is an emergency, and treating them all the same either burns out your techs or leaves a family in danger. Here’s a simple list you can give your office, your answering service or your AI receptionist.</p>

<div class="warn"><b>Safety first.</b> For a gas smell or a carbon monoxide alarm, the caller’s first step is never “wait for a tech.” Tell them to get out of the house and call 911 from outside.</div>

<h2>Level 1: Life safety. Act now.</h2>
<h3>Gas smell</h3>
<p>Tell the caller to leave the area right away, then call 911 and their gas company from a safe distance. In most of North Texas that’s Atmos Energy, whose 24-hour emergency line is 866-322-8667. Then alert the owner or on-call tech.</p>
<h3>Carbon monoxide alarm sounding</h3>
<p>The U.S. Consumer Product Safety Commission says never ignore a CO alarm: get outside immediately and call 911 from fresh air. Don’t go back in until responders say it’s safe.</p>
<h3>Burning smell, smoke or sparks from equipment</h3>
<p>Tell the caller to turn the system off at the thermostat and call 911 if there is smoke or fire. Alert the on-call tech.</p>

<h2>Level 2: Urgent. Same night or first thing.</h2>
<ul class="list">
<li><b>No heat in freezing weather</b>, especially with elderly people, babies or someone who is ill in the home.</li>
<li><b>No cooling during extreme heat</b> with vulnerable people inside. Texas health officials list older adults, young children and people with chronic illness as most at risk from heat, and say air conditioning is the best protection.</li>
<li><b>Water leaking</b> from the unit onto floors or ceilings.</li>
</ul>
<p>Your rule here is a business choice: ring the on-call tech now, or book the first slot in the morning. Write it down so everyone handles it the same way.</p>

<h2>Level 3: Book it. Next available slot.</h2>
<ul class="list">
<li>AC running but not cooling well, in normal weather</li>
<li>Strange noises with the system still working</li>
<li>Thermostat problems</li>
<li>Tune-ups and maintenance visits</li>
<li>New system quotes</li>
<li>Price questions</li>
</ul>

<h2>Turn this into a one-page rule sheet</h2>
<ol class="list">
<li>List your Level 1 and Level 2 words: “gas,” “smell,” “alarm,” “smoke,” “no heat,” “leak.”</li>
<li>Decide who gets the call for each level, and their number.</li>
<li>Write the exact words to tell the caller for gas and CO.</li>
<li>Share it with everyone who answers your phone.</li>
</ol>
<p>This is the same list we set up with every BookedOrion shop. You choose the emergency words, and Molly rings you first when she hears one.</p>
<p class="note">This article is general information, not professional safety advice. Follow your local gas utility, fire department and code requirements.</p>
''',
  sources=[('Atmos Energy: Recognizing a leak','https://atmosenergy.com/safety/recognizing-leak'),
           ('U.S. CPSC: Carbon monoxide talking points (PDF)','https://www.cpsc.gov/s3fs-public/pdfs/blk_pdf_Talking_Points.pdf'),
           ('Texas DSHS: Hot weather precautions','https://dshs.state.tx.us/news/releases/20130806.aspx')],
 ),
 dict(
  slug='call-forwarding-team-answers-first',
  cat='Phones & calls',
  art=('20s','Your team first','then Molly'),
  title='How to set up call forwarding so your team still answers first',
  desc='Conditional call forwarding lets your phone ring first and sends only missed or busy calls onward. Here is how it works on common carriers and office phone systems.',
  read='4 min read',
  body='''
<p class="lede">You don’t have to choose between answering your own phone and using a backup. Conditional call forwarding lets your phone ring first. Only the calls nobody picks up, or that come in while you’re on another call, move on.</p>

<h2>Unconditional vs. conditional forwarding</h2>
<p><strong>Unconditional</strong> forwarding sends every call somewhere else. Your phone never rings.</p>
<p><strong>Conditional</strong> forwarding only kicks in when a call isn’t answered, the line is busy, or your phone is off. For most HVAC shops this is the one you want: your team gets the first try, and nothing gets lost.</p>

<h2>Common carrier codes</h2>
<p>Many carriers let you turn this on by dialing a short code from the phone itself. Google’s support pages list these, among others:</p>
<div class="tablewrap"><table>
<thead><tr><th>Carrier</th><th>Turn on</th><th>Turn off</th></tr></thead>
<tbody>
<tr><td>AT&amp;T (no answer)</td><td>**61* + number + #</td><td>##61#</td></tr>
<tr><td>AT&amp;T (busy)</td><td>*67* + number + #</td><td>##67#</td></tr>
<tr><td>Verizon</td><td>*71 + number</td><td>*73</td></tr>
<tr><td>T-Mobile</td><td colspan="2">Varies by line. Check with T-Mobile.</td></tr>
</tbody></table></div>
<p class="note">Carriers change codes from time to time. Confirm with your carrier before you rely on them.</p>

<h2>Office phone systems</h2>
<p>If your shop uses a business phone app or VoIP system, forwarding is usually a setting rather than a code. Look for “call forwarding”, “no-answer rule” or “ring group overflow” in your admin settings, and set how many seconds it rings before forwarding.</p>

<h2>How long should it ring?</h2>
<p>About 10 to 15 seconds, or two to three rings, works for most shops. Long enough for someone in the office to grab it, short enough that the caller doesn’t give up.</p>

<h2>Test it before you trust it</h2>
<ol class="list">
<li>Call your business number from a different phone.</li>
<li>Let it ring without answering. Check that it forwards after the time you set.</li>
<li>Call again while the line is busy. Check that it forwards right away.</li>
<li>Write down the “turn off” code and keep it somewhere handy.</li>
</ol>
<p>When we set up Molly, we walk you through this on the phone and test it together. Your number never changes.</p>
''',
  sources=[('Google Voice Help: carrier call forwarding codes','https://support.google.com/voice/answer/165656?hl=en')],
 ),
 dict(
  slug='summer-rush-phone-checklist',
  cat='Guides',
  art=('7','Summer rush','checklist items'),
  title='Summer rush phone checklist for HVAC owners',
  desc='The first heat wave brings more calls than your office can handle. Seven things to set up before it hits, so no booking slips through.',
  read='4 min read',
  body='''
<p class="lede">The first real heat wave in Dallas–Fort Worth changes your phone overnight. Calls double, techs are booked out and the office can’t keep up. A little setup in spring keeps those calls from turning into lost jobs.</p>

<h2>1. Fix your voicemail greeting</h2>
<p>Say your company name, that you got their call, and when you’ll call back. “You’ve reached the voicemail of…” sounds like nobody works there.</p>

<h2>2. Decide what happens after hours</h2>
<p>Forward to an on-call phone, an answering service or an AI receptionist. Pick one and write it down. “We’ll figure it out” means voicemail.</p>

<h2>3. Write your emergency list</h2>
<p>Which calls get someone out tonight? No cooling with an elderly person at home, water leaking through a ceiling, a burning smell. Our <a href="/blog/hvac-emergency-call-triage/">triage guide</a> has a starting list.</p>

<h2>4. Set a callback promise, and keep it</h2>
<p>“We call back within one hour during business hours” is a promise customers remember, especially if you keep it.</p>

<h2>5. Agree on what to say about price</h2>
<p>Everyone answering your phone should give the same diagnostic or trip fee, and nobody should guess a repair price over the phone.</p>

<h2>6. Count your missed calls once a week</h2>
<p>Your phone’s call log shows them. If the number climbs in June, it’s time to add coverage before July.</p>

<h2>7. Make booking easy</h2>
<p>Keep open slots visible to whoever answers, so they can book on the call instead of promising a callback.</p>

<p>If you’d rather not staff the phone through August, that’s exactly what Molly is for. She answers what your team misses, books it, and texts you.</p>
''',
  sources=[],
 ),
 dict(
  slug='questions-before-ai-answers-your-phone',
  cat='AI basics',
  art=('5','Questions to ask','before you buy'),
  title='5 questions to ask before AI answers your business phone',
  desc='AI receptionists are not all the same. Ask these five questions before one talks to your customers.',
  read='4 min read',
  body='''
<p class="lede">An AI receptionist speaks for your company, sometimes at 2 AM with nobody watching. Before you let one answer your phone, ask these five questions. The answers tell you more than any demo.</p>

<h2>1. Does it tell callers it’s an AI?</h2>
<p>Customers notice. An AI that pretends to be a person can damage the trust you’ve built. Look for one that says up front that it’s an AI assistant and that the call may be recorded.</p>

<h2>2. Does it book the job, or just take a message?</h2>
<p>A message means someone still has to call back tomorrow, by which time the homeowner may have called another shop. Ask whether it books straight onto your calendar.</p>

<h2>3. What happens in an emergency?</h2>
<p>Ask exactly what it says to a caller who smells gas, and who it alerts. You want clear safety instructions for the caller and an immediate call to you, not a note in an inbox.</p>

<h2>4. How does a caller reach a real person?</h2>
<p>Some callers are upset, or the situation doesn’t fit a script. Ask how the AI passes them to you, or takes a message when nobody can answer.</p>

<h2>5. Can you check its work, and walk away?</h2>
<p>You should be able to read a summary and listen to every call. And you should be able to cancel without a long contract if it isn’t working for you.</p>

<p>Molly answers yes to all five. Call her at <a href="tel:+15705219710">(570) 521-9710</a> and test her yourself.</p>
''',
  sources=[],
 ),

]

def article(p):
    path = f"/blog/{p['slug']}/"
    ld = {"@context":"https://schema.org","@type":"BlogPosting","headline":p['title'],"description":p['desc'],
          "datePublished":DATE,"dateModified":DATE,"author":{"@type":"Person","name":AUTHOR},
          "publisher":{"@type":"Organization","name":"BookedOrion","url":SITE},"mainEntityOfPage":SITE+path}
    extra = f'<script type="application/ld+json">{json.dumps(ld)}</script>'
    others = [o for o in POSTS if o is not p]
    def _cv(o,i):
        a=o.get('art',('','',''))
        return f'<div class="ccov v{i%3}" aria-hidden="true"><b>{a[0]}</b><span>{a[1]}</span><em>{a[2]}</em></div>'
    more = ''.join(f'<a class="card" href="/blog/{o["slug"]}/">{_cv(o,i)}<div class="cbody"><div class="meta"><span class="cat">{o["cat"]}</span><span>{o["read"]}</span></div><h3>{html.escape(o["title"])}</h3><span class="rm">Read article →</span></div></a>' for i,o in enumerate(others[:3]))
    src = ''.join(f'<li><a href="{u}" rel="noopener" target="_blank">{html.escape(t)}</a></li>' for t,u in p['sources'])
    return head(p['title']+' | BookedOrion', p['desc'], path, extra) + '<div class="rp" aria-hidden="true"></div>' + HEADER + f'''
<header class="ahero"><div class="wrap ahin">
<a class="back" href="/blog/">← All articles</a>
<div class="meta"><span class="cat">{p['cat']}</span><span>{DATE_H}</span><span>{p['read']}</span></div>
<h1>{html.escape(p['title'])}</h1>
<p class="adesc">{html.escape(p['desc'])}</p>
<div class="by2"><img src="/siam-2.jpg" alt="Siam Ahmed" width="44" height="44"><div><b>{AUTHOR}</b><span>Founder, BookedOrion</span></div></div>
</div></header>
<main>
<div class="wrap alay">
<article class="art2">
<div class="prose">{p['body']}
<div class="src"><h2>Sources</h2><ul>{src}</ul></div>
</div>
<div class="author"><img src="/siam-2.jpg" alt="" width="64" height="64"><div><b>Written by {AUTHOR}</b><p>Founder of BookedOrion. I set up Molly, our AI receptionist, for HVAC shops, and review her calls with every owner.</p></div></div>
</article>
<aside class="toc" aria-label="On this page"><div class="tocin">
<div class="toch">IN THIS ARTICLE</div><nav id="toc"></nav>
<button type="button" class="copyl" id="copyl">Copy link</button>
<a class="tcta" href="/#demo"><b>Hear Molly answer</b><span>Call (570) 521-9710 and talk like a homeowner.</span></a>
</div></aside>
</div>
<div class="wrap">{CTA}
<section class="more2"><h2>Keep reading</h2><div class="cards">{more}</div></section>
</div>
</main>
<script>
(function(){{var pr=document.querySelector('.prose'),toc=document.getElementById('toc'),bar=document.querySelector('.rp');
var hs=[].slice.call(pr.querySelectorAll('h2')).filter(function(h){{return !h.closest('.src');}});
hs.forEach(function(h,i){{h.id=h.id||('s'+(i+1));var a=document.createElement('a');a.href='#'+h.id;a.textContent=h.textContent;toc.appendChild(a);}});
var links=[].slice.call(toc.querySelectorAll('a'));
function on(){{var y=scrollY+140,cur=0;hs.forEach(function(h,i){{if(h.offsetTop<=y)cur=i;}});links.forEach(function(l,i){{l.classList.toggle('on',i===cur);}});
var st=pr.offsetTop,en=st+pr.offsetHeight-innerHeight,pc=Math.min(1,Math.max(0,(scrollY-st)/Math.max(1,en-st)));bar.style.transform='scaleX('+pc+')';}}
addEventListener('scroll',on,{{passive:true}});on();
var c=document.getElementById('copyl');c.addEventListener('click',function(){{try{{navigator.clipboard.writeText(location.href);c.textContent='Link copied ✓';setTimeout(function(){{c.textContent='Copy link';}},2000);}}catch(e){{}}}});
}})();
</script>
''' + FOOTER + '\n</body>\n</html>\n'

def index():
    feat = POSTS[0]
    def cover(p,i):
        a=p.get('art',('','',''))
        return f'<div class="ccov v{i%3}" aria-hidden="true"><b>{a[0]}</b><span>{a[1]}</span><em>{a[2]}</em></div>'
    cards = ''.join(f'''<a class="card" data-cat="{p['cat']}" href="/blog/{p['slug']}/">{cover(p,i)}<div class="cbody"><div class="meta"><span class="cat">{p['cat']}</span><span>{DATE_H}</span><span>{p['read']}</span></div>
<h3>{html.escape(p['title'])}</h3><p>{html.escape(p['desc'])}</p><span class="rm">Read article →</span></div></a>''' for i,p in enumerate(POSTS[1:]))
    cats=['All']+sorted({p['cat'] for p in POSTS})
    chips=''.join(f'<button type="button" class="chip{" on" if c=="All" else ""}" data-f="{c}" aria-pressed="{"true" if c=="All" else "false"}">{c}</button>' for c in cats)
    desc = 'Practical advice for HVAC owners: missed calls, after-hours answering, emergency triage and growing your shop.'
    ld = {"@context":"https://schema.org","@type":"Blog","name":"BookedOrion Blog","url":SITE+'/blog/',
          "blogPost":[{"@type":"BlogPosting","headline":p['title'],"url":f"{SITE}/blog/{p['slug']}/","datePublished":DATE} for p in POSTS]}
    return head('HVAC Owner Blog | BookedOrion', desc, '/blog/', f'<script type="application/ld+json">{json.dumps(ld)}</script>') + HEADER + f'''
<main>
<section class="bhero"><div class="wrap">
<div class="eyebrow">THE BOOKEDORION BLOG</div>
<h1>Practical advice for HVAC owners who hate missed calls.</h1>
<p>Short, honest guides on phones, after-hours calls and booking more jobs. Written for busy HVAC shop owners.</p>
<label class="bsearch"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="M21 21l-4.3-4.3"/></svg><input id="bq" type="search" placeholder="Search articles, e.g. after-hours, emergency, forwarding" aria-label="Search articles"></label>
<div class="bstats"><span><b>{len(POSTS)}</b> guides</span><span><b>5 min</b> average read</span><span><b>HVAC</b> only</span></div>
</div></section>
<section class="wrap list-area">
<div class="chips" role="group" aria-label="Filter articles">{chips}</div>
<a class="feat" data-cat="{feat['cat']}" href="/blog/{feat['slug']}/">
<div class="featart" aria-hidden="true"><div class="ring"></div><div class="t1">9:47 PM</div><div class="t2">Missed call</div><div class="t3">→ Booked by Molly</div></div>
<div class="feattx"><div class="meta"><span class="cat">{feat['cat']}</span><span>{DATE_H}</span><span>{feat['read']}</span></div>
<h2>{html.escape(feat['title'])}</h2><p>{html.escape(feat['desc'])}</p><span class="rm">Read article →</span></div></a>
<div class="cards">{cards}</div>
</section>
<p class="nores" id="nores" hidden>No articles match that search yet.</p>
<script>(function(){{var b=[].slice.call(document.querySelectorAll('.chip')),it=[].slice.call(document.querySelectorAll('.list-area [data-cat]')),q=document.getElementById('bq'),nr=document.getElementById('nores'),f='All';
function run(){{var s=(q.value||'').toLowerCase().trim(),n=0;it.forEach(function(x){{var ok=(f==='All'||x.dataset.cat===f)&&(!s||x.textContent.toLowerCase().indexOf(s)>-1);x.hidden=!ok;if(ok)n++;}});nr.hidden=n>0;}}
b.forEach(function(x){{x.addEventListener('click',function(){{f=x.dataset.f;b.forEach(function(y){{y.classList.toggle('on',y===x);y.setAttribute('aria-pressed',y===x?'true':'false');}});run();}});}});q.addEventListener('input',run);}})();</script>
<div class="wrap">{CTA}</div>
</main>
''' + FOOTER + '\n</body>\n</html>\n'

def main():
    os.makedirs(os.path.join(OUT,'blog'), exist_ok=True)
    open(os.path.join(OUT,'blog','index.html'),'w').write(index())
    for p in POSTS:
        d=os.path.join(OUT,'blog',p['slug']); os.makedirs(d, exist_ok=True)
        open(os.path.join(d,'index.html'),'w').write(article(p))
    urls=['/','/blog/']+[f"/blog/{p['slug']}/" for p in POSTS]
    sm='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join(f'  <url><loc>{SITE}{u}</loc><lastmod>{DATE}</lastmod></url>\n' for u in urls)+'</urlset>\n'
    open(os.path.join(OUT,'sitemap.xml'),'w').write(sm)
    open(os.path.join(OUT,'robots.txt'),'w').write(f'User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n')
    print('built', len(POSTS), 'posts')

if __name__=='__main__':
    main()
