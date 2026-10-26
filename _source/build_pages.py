#!/usr/bin/env python3
"""How it works, legal pages and 404 for bookedorion.com (reuses the blog shell)."""
import os, json, html
import build_blog as B
import how_v2 as H2
import getting_started as GS
import about as AB

OUT = B.OUT
UPDATED = 'October 27, 2026'

def page(path, title, desc, inner, extra=''):
    hdr = B.HEADER.replace('class="nav on"','class="nav"')
    if path in ('/how-it-works/','/about/'): hdr = hdr.replace('class="nav" href="'+path+'"','class="nav on" href="'+path+'"')
    if False: hdr = hdr.replace('class="nav" href="/how-it-works/"','class="nav on" href="/how-it-works/"')
    return B.head(title, desc, path, extra) + hdr + f'<main>{inner}</main>' + B.FOOTER + '\n</body>\n</html>\n'

def hero(kicker, h1, sub):
    return f'<section class="bhero"><div class="wrap"><div class="eyebrow">{kicker}</div><h1>{h1}</h1><p>{sub}</p></div></section>'

CHK = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#0B7A57" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12l5 5L20 7"/></svg>'
NO = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#C2410C" stroke-width="3" stroke-linecap="round" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"/></svg>'

# ---------------- How it works ----------------
def how():
    modes = [
        ('Porchlight', '$197/mo', 'After hours only', 'Your office answers during the day as usual. When you close, calls forward to Molly. Nights, weekends and holidays are covered.'),
        ('Full Desk', '$397/mo', 'After hours + daytime overflow', 'Your team still answers first. If nobody picks up in about 20 seconds, or the line is busy, Molly takes the call. A good place to start.'),
        ('Revenue Desk', '$797/mo', 'Everything + follow-ups', 'Full Desk, plus follow-up emails for estimates that never booked, tune-up reminder campaigns and a monthly booked-jobs report.'),
    ]
    mode_html = ''.join(f'<div class="mode{" pop" if i==1 else ""}"><div class="mtop"><b>{n}</b><span>{p}</span></div><div class="mk">{k}</div><p>{d}</p></div>' for i,(n,p,k,d) in enumerate(modes))

    steps = [
        ('Greets and discloses', '“Thanks for calling ABC Heating &amp; Air. This is Molly, the AI assistant. This call may be recorded. How can I help?”'),
        ('Listens to the problem', 'The caller explains in their own words: no cooling, no heat, a noise, a leak, a quote. Molly asks a follow-up if something is unclear.'),
        ('Checks for an emergency', 'If the caller says one of your emergency words (gas, smoke, CO alarm, no heat with an elderly person), Molly follows your rules. For gas or CO she tells the caller to get outside and call 911, then rings you.'),
        ('Takes the details', 'Name, callback number, service address and ZIP, what kind of system it is, and whether anyone at home is at risk from the heat or cold.'),
        ('Checks your service area', 'If the ZIP is outside your area, Molly says so politely instead of booking a job you can’t take.'),
        ('Mentions your fee', 'If you charge a diagnostic or trip fee, Molly states it before booking, so there are no surprises at the door.'),
        ('Books the visit', 'She offers open slots from your calendar and books the one the caller picks.'),
        ('Reads it back', '“So that’s Maria at 214 Oak Lane, AC blowing warm air, Wednesday at 8 AM. Did I get that right?”'),
        ('Texts you', 'Seconds after the call, you get a summary by text and email. The recording and transcript are saved.'),
    ]
    step_html = ''.join(f'<li><span class="sn">{i+1}</span><div><b>{t}</b><p>{d}</p></div></li>' for i,(t,d) in enumerate(steps))

    setup = [
        ('Day 1', 'Short form', 'Name, company and email. That’s all we need to start.'),
        ('Within 1 business day', 'Setup questions', 'Your hours, service area ZIPs, fees, emergency words, on-call number and which calendar to book on.'),
        ('Next', 'We build and test', 'We write Molly’s script for your shop, then you hear a test call. Nothing goes live until you say it sounds right.'),
        ('Go live', 'Forward your calls', 'You set your phone to forward missed or after-hours calls to Molly. We walk you through it on the phone. Your number stays the same.'),
        ('Day 14', 'You decide', 'If Molly didn’t book a job, you pay nothing. If she did, pick a plan or walk away.'),
    ]
    setup_html = ''.join(f'<li><div class="sk">{a}</div><b>{t}</b><p>{d}</p></li>' for a,t,d in setup)

    always = ['Says she’s an AI assistant','Mentions the call may be recorded','Follows your emergency rules','Passes upset or tricky callers to you','Texts you every call']
    never = ['Takes card numbers over the phone','Diagnoses a system or promises a repair','Quotes prices you didn’t approve','Makes sales calls or sends marketing texts','Pretends to be a person']
    rules = (f'<div class="rules"><div><div class="rk ok">MOLLY ALWAYS</div>' + ''.join(f'<div class="ri">{CHK}<span>{t}</span></div>' for t in always) +
             f'</div><div><div class="rk no">MOLLY NEVER</div>' + ''.join(f'<div class="ri">{NO}<span>{t}</span></div>' for t in never) + '</div></div>')

    faq = [
        ('Do I need new software?', 'No. Bookings go on the Google or Outlook calendar you already use, and details come to you by text and email.'),
        ('What if I use ServiceTitan, Jobber or Housecall Pro?', 'Every booking arrives with all the details, ready for your team to add in seconds. Ask us about a direct integration.'),
        ('What if Molly isn’t sure?', 'She takes a clear message and tells the caller you’ll call back. You get it by text right away.'),
        ('Can I change the script later?', 'Yes. Email us what to change and we update it, usually the same day.'),
        ('Can I hear every call?', 'Yes. Every call has a summary, a recording and a transcript.'),
    ]
    faq_html = ''.join(f'<details class="fq"><summary>{q}<span aria-hidden="true">+</span></summary><p>{a}</p></details>' for q,a in faq)
    ld = {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faq]}

    inner = hero('HOW IT WORKS', 'Exactly what Molly does on every call.',
                 'A plain, step-by-step look at how BookedOrion answers, books and reports on the calls your team misses. No jargon.') + f'''
<div class="wrap pg">
<section class="blk"><div class="bh"><div class="eyebrow dk">THREE WAYS TO USE MOLLY</div><h2>Pick how much of your phone she covers.</h2></div>
<div class="modes">{mode_html}</div></section>

<section class="blk"><div class="bh"><div class="eyebrow dk">ONE CALL, STEP BY STEP</div><h2>What happens when a homeowner calls at 9:47 PM.</h2>
<p>This is the order Molly follows on a normal service call. We set up every step with you before she goes live.</p></div>
<ol class="steps">{step_html}</ol></section>

<section class="blk two"><div><div class="eyebrow dk">WHAT YOU GET</div><h2>After every call, it’s on your phone.</h2>
<p>You don’t log in to anything. Each call sends you a short summary. Recordings and transcripts are there whenever you want to check her work.</p>
<div class="ri">{CHK}<span><b>Text + email summary</b> of every call</span></div>
<div class="ri">{CHK}<span><b>Calendar booking</b> with the address and problem</span></div>
<div class="ri">{CHK}<span><b>Recording and transcript</b> of each call</span></div>
<div class="ri">{CHK}<span><b>Instant call</b> to you for emergencies</span></div></div>
<div class="phone"><div class="pscreen"><div class="ph">Text from BookedOrion · 9:49 PM</div>
<div class="bub"><b>New job booked ✓</b><br><b>Customer:</b> Maria G.<br><b>Problem:</b> AC blowing warm air<br><b>Area:</b> In your service area ✓<br><b>Visit:</b> Wed 8:00 AM<br><span class="dim">Told about the diagnostic fee.</span></div>
<div class="bub urg"><b>Urgent call · 9:12 PM</b><br>No heat, elderly caller. Molly is ringing you now.</div>
<div class="ph">Example text for illustration</div></div></div></section>

<section class="blk"><div class="bh"><div class="eyebrow dk">SETUP</div><h2>We do the setup. You answer a few questions.</h2></div>
<ol class="setup">{setup_html}</ol></section>

<section class="blk"><div class="bh"><div class="eyebrow dk">MOLLY’S RULEBOOK</div><h2>Clear rules, set with you.</h2>
<p>Read more in our <a href="/blog/hvac-emergency-call-triage/">emergency call triage guide</a>.</p></div>{rules}</section>

<section class="blk"><div class="bh"><div class="eyebrow dk">QUESTIONS</div><h2>Setup questions owners ask</h2></div><div class="fqs">{faq_html}</div></section>
{B.CTA}
</div>'''
    return page('/how-it-works/', 'How BookedOrion Works | AI Receptionist for HVAC', 'Step by step: how Molly answers, triages, books and reports on your HVAC calls, and how setup works in a few days.', inner, f'<script type="application/ld+json">{json.dumps(ld)}</script>')

# ---------------- Legal ----------------
def legal(path, title, kicker, desc, body):
    inner = hero(kicker, title, f'Last updated {UPDATED}') + f'<div class="wrap art legal"><div class="prose">{body}</div></div>'
    return page(path, f'{title} | BookedOrion', desc, inner)

PRIVACY = '''
<p class="lede">This policy explains what information BookedOrion collects, how we use it and the choices you have. Questions: <a href="mailto:siam@bookedorion.com">siam@bookedorion.com</a>.</p>
<h2>Who we are</h2>
<p>BookedOrion provides an AI receptionist service (“Molly”) for HVAC and home-service businesses. In this policy, “we” means BookedOrion and “you” means a visitor to this website or a business that uses our service.</p>
<h2>What we collect</h2>
<ul class="list">
<li><b>From this website:</b> the name, company and email you enter when you request a trial or contact us.</li>
<li><b>From our business customers:</b> setup details such as business hours, service area, fees, calendar access and the phone numbers to alert.</li>
<li><b>From calls Molly answers for our customers:</b> the caller’s name, phone number, service address, the problem they describe, call recordings and transcripts. We process this on behalf of the HVAC business the caller contacted.</li>
<li><b>Basic technical data:</b> our hosting provider may log standard information such as IP address and browser type to keep the site running and secure.</li>
</ul>
<h2>How we use it</h2>
<ul class="list">
<li>To set up, run and improve the service for our customers.</li>
<li>To book appointments and send call summaries and alerts to the business that owns the call.</li>
<li>To reply to your questions and provide support.</li>
<li>To meet legal requirements.</li>
</ul>
<h2>Text messages</h2>
<p>We send text messages only to business owners and staff who sign up to receive call summaries and alerts. See our <a href="/sms-terms/">SMS terms</a>.</p>
<p><b>No mobile information will be shared with third parties/affiliates for marketing/promotional purposes.</b> Text messaging originator opt-in data and consent will not be shared with any third parties.</p>
<h2>Who processes data for us</h2>
<p>We use service providers for hosting, telephony, email and calendar functions, only as needed to run the service. They may use the data only to provide their services to us. We do not sell personal information.</p>
<h2>Call recordings</h2>
<p>Molly tells callers at the start of each call that the call may be recorded. Recordings and transcripts are available to the business that received the call.</p>
<h2>How long we keep it</h2>
<p>We keep information for as long as needed to provide the service and meet legal obligations. Business customers can ask us to delete their call data when they leave.</p>
<h2>Your choices</h2>
<p>You can ask to see, correct or delete your information by emailing <a href="mailto:siam@bookedorion.com">siam@bookedorion.com</a>. You can stop text messages at any time by replying STOP.</p>
<h2>Security</h2>
<p>We use reasonable safeguards to protect information. No system is perfectly secure, so we cannot guarantee absolute security.</p>
<h2>Children</h2>
<p>This website and service are for businesses. We do not knowingly collect information from children under 13.</p>
<h2>Changes</h2>
<p>We may update this policy. The date at the top shows the latest version.</p>
'''

TERMS = '''
<p class="lede">These terms cover your use of the BookedOrion website and service. By starting a trial or a plan, you agree to them. Questions: <a href="mailto:siam@bookedorion.com">siam@bookedorion.com</a>.</p>
<h2>The service</h2>
<p>BookedOrion provides an AI receptionist (“Molly”) that answers calls for your business, books appointments on your calendar and sends you call summaries and alerts.</p>
<h2>Free 14-day trial</h2>
<p>We set up the service and run it free for 14 days. There is no setup fee. After the trial, you can choose a plan or stop.</p>
<h2>Plans and billing</h2>
<ul class="list">
<li><b>Pay-per-Job:</b> $79 a month plus $29 for each booked job, never more than $449 in a month. If Molly books no jobs in your first paid month, that month is free.</li>
<li><b>Flat:</b> $249 a month with unlimited booked jobs.</li>
<li><b>Night-only:</b> Pay-per-Job with a $49 monthly base, covering nights, weekends and holidays only.</li>
<li>Plans are month to month. There is no long-term contract.</li>
<li>You can cancel at any time. Cancellation takes effect at the end of the current billing month.</li>
<li>Each plan includes 400 call minutes a month. We text you when you reach 80% (320 minutes). One busy month is fine. If you go over two months in a row, we agree on a bigger plan together. No surprise bills.</li>
<li>Spam and wrong-number calls are never counted.</li>
<li>Payment is by a secure invoice link. Molly never takes payment details on a call.</li>
</ul>
<h2>What counts as a booked job</h2>
<ul class="list">
<li>A booked job is a new appointment from a call Molly handled. You confirm it with one tap in the text summary. If you don’t reply within 48 hours, it counts as booked. The call recording and summary are the record.</li>
<li>If you mark a booking as not booked, you pick a reason (spam, duplicate, outside your service area, not a real job, or customer cancelled). We check the recording before removing the charge.</li>
<li>Cancellations are free when there is a record: the customer called or texted Molly, or you send us the call recording or a screenshot of the text. The cancellation must be before the appointment time and within 7 days.</li>
<li>A no-show, or a customer who declines at the door, still counts, because the appointment was made.</li>
</ul>
<h2>Your responsibilities</h2>
<ul class="list">
<li>Give us accurate business information: hours, fees, service area and emergency contacts.</li>
<li>Keep your emergency phone numbers up to date and reachable.</li>
<li>Use the service in line with the laws that apply to your business, including rules on call recording and text messaging.</li>
</ul>
<h2>Limits of an AI receptionist</h2>
<p>Molly is an AI assistant. She can misunderstand callers or make mistakes. She is not an emergency service and does not replace 911, your gas utility or your own judgment. Review your call summaries and tell us about any problem so we can fix the script.</p>
<h2>Payments over the phone</h2>
<p>Molly does not collect card numbers or other payment details by phone.</p>
<h2>Text messaging program</h2>
<p><b>Program name:</b> BookedOrion Alerts. <b>Description:</b> call summaries, booking confirmations and urgent-call alerts sent to business owners and staff who sign up for them.</p>
<ul class="list">
<li>Message frequency varies with your call volume.</li>
<li>Message and data rates may apply.</li>
<li>Text STOP to cancel at any time. After you send STOP, we will send one message to confirm you are unsubscribed.</li>
<li>Text HELP for help, or email <a href="mailto:siam@bookedorion.com">siam@bookedorion.com</a>.</li>
<li>Carriers are not liable for delayed or undelivered messages.</li>
</ul>
<p>Enclosed is a copy of the boilerplate terms of service covering minimum requirements from the carriers. See our full <a href="/sms-terms/">SMS terms</a> and <a href="/privacy/">Privacy Policy</a>.</p>
<h2>Limitation of liability</h2>
<p>To the extent the law allows, BookedOrion is not liable for lost profits or indirect damages, and our total liability is limited to the amount you paid us in the three months before the claim.</p>
<h2>Changes</h2>
<p>We may update these terms. We will tell active customers about important changes by email.</p>
'''

SMS = '''
<p class="lede">These terms apply to text messages sent by BookedOrion.</p>
<h2>Program</h2>
<p><b>Program name:</b> BookedOrion Alerts</p>
<p><b>What you receive:</b> call summaries, booking confirmations and urgent-call alerts about calls Molly answers for your business. We do not send marketing texts.</p>
<p><b>Who receives them:</b> business owners and staff who sign up during setup and give consent to receive these texts.</p>
<h2>Opting in</h2>
<p>You opt in during setup by giving us the mobile number(s) to alert and agreeing to receive text messages from BookedOrion. Consent is not a condition of purchase.</p>
<h2>Frequency and cost</h2>
<ul class="list">
<li>Message frequency varies. It depends on how many calls Molly answers for you.</li>
<li>Message and data rates may apply.</li>
</ul>
<h2>Help and opting out</h2>
<ul class="list">
<li>Text <b>HELP</b> for help, or email <a href="mailto:siam@bookedorion.com">siam@bookedorion.com</a>.</li>
<li>Text <b>STOP</b> to cancel. You will receive one final message confirming you are unsubscribed. You can rejoin by texting START.</li>
</ul>
<h2>Carriers</h2>
<p>Carriers are not liable for delayed or undelivered messages.</p>
<h2>Privacy</h2>
<p>No mobile information will be shared with third parties/affiliates for marketing/promotional purposes. Text messaging originator opt-in data and consent will not be shared with any third parties. Read our <a href="/privacy/">Privacy Policy</a>.</p>
'''

NOTFOUND = '''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Page not found | BookedOrion</title>
<meta name="robots" content="noindex"><link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png">
''' + B.FONTS + '''<link rel="stylesheet" href="/blog/blog.css?v=''' + B.CSSV + '''"></head>
<body>''' + B.HEADER + '''<main><section class="bhero" style="padding-block:120px"><div class="wrap"><div class="eyebrow">404</div><h1>This page went to voicemail.</h1>
<p>We couldn’t find that page. Molly would have answered, but she only does phones.</p>
<div class="ctab"><a class="btn big" href="/">Go to the home page</a><a class="ghost" href="/blog/">Read the blog</a></div></div></section></main>''' + B.FOOTER + '</body></html>\n'

EXTRA_CSS = '''
/* pages: how it works, legal */
.pg{display:flex;flex-direction:column;gap:72px;padding-block:64px 8px}
.blk{display:flex;flex-direction:column;gap:28px}
.bh{display:flex;flex-direction:column;gap:12px;max-width:760px}
.bh h2,.two h2{margin:0;font-size:clamp(28px,3.6vw,42px);line-height:1.1;letter-spacing:-.025em}
.bh p,.two p{margin:0;font-size:18px;line-height:1.65;color:var(--muted)}
.eyebrow.dk{color:var(--indigo)}
.modes{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,300px),1fr));gap:18px}
.mode{border:1px solid var(--line);border-radius:22px;padding:26px;display:flex;flex-direction:column;gap:10px}
.mode.pop{background:var(--night);color:#FFF;border-color:var(--night)}
.mtop{display:flex;justify-content:space-between;gap:10px;align-items:baseline}.mtop b{font-size:22px}.mtop span{font-weight:700;color:var(--indigo)}.pop .mtop span{color:var(--mint)}
.mk{font-size:14px;font-weight:700;color:var(--mintdk);background:#E6FBF4;align-self:flex-start;padding:5px 10px;border-radius:999px}.pop .mk{color:var(--night);background:var(--mint)}
.mode p{margin:0;font-size:16px;line-height:1.6;color:var(--muted)}.pop p{color:#C9C7EE}
.steps{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,340px),1fr));gap:14px}
.steps li{display:flex;gap:16px;background:var(--wash);border-radius:18px;padding:20px}
.sn{width:34px;height:34px;flex-shrink:0;border-radius:50%;background:var(--indigo);color:#FFF;font-weight:700;display:inline-flex;align-items:center;justify-content:center;font-variant-numeric:tabular-nums}
.steps b{font-size:17px}.steps p{margin:4px 0 0;font-size:15px;line-height:1.6;color:var(--muted)}
.blk.two{flex-direction:row;flex-wrap:wrap;gap:48px;align-items:center}
.two>div:first-child{flex:1 1 420px;min-width:0;display:flex;flex-direction:column;gap:14px}
.ri{display:flex;gap:10px;align-items:flex-start;font-size:16px;line-height:1.5}.ri svg{flex-shrink:0;margin-top:3px}
.phone{flex:0 1 340px;min-width:0;margin:0 auto;background:var(--ink);border-radius:40px;padding:12px;box-shadow:0 30px 70px rgba(15,13,46,.25)}
.pscreen{background:#FFF;border-radius:30px;padding:20px 16px;display:flex;flex-direction:column;gap:12px}
.ph{text-align:center;font-size:12px;color:var(--soft);font-weight:600}
.bub{background:#F1F0F8;border-radius:18px 18px 18px 6px;padding:14px 16px;font-size:15px;line-height:1.6}.bub.urg{background:#FFF1E8;color:#7C2D12}.dim{color:var(--muted)}
.setup{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,200px),1fr));gap:14px}
.setup li{border:1px solid var(--line);border-radius:18px;padding:20px;display:flex;flex-direction:column;gap:6px}
.sk{font-size:12px;font-weight:700;letter-spacing:.08em;color:var(--indigo);text-transform:uppercase}.setup b{font-size:17px}.setup p{margin:0;font-size:15px;line-height:1.55;color:var(--muted)}
.rules{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,300px),1fr));gap:18px}
.rules>div{border:1px solid var(--line);border-radius:22px;padding:24px;display:flex;flex-direction:column;gap:12px}
.rk{font-size:13px;font-weight:700;letter-spacing:.12em}.rk.ok{color:#0B7A57}.rk.no{color:#C2410C}
.fqs{display:flex;flex-direction:column;gap:10px;max-width:860px}
.fq{background:var(--wash);border-radius:16px;padding:18px 22px}
.fq summary{list-style:none;cursor:pointer;font-weight:700;font-size:17px;display:flex;justify-content:space-between;gap:16px}.fq summary::-webkit-details-marker{display:none}
.fq summary span{color:var(--indigo);transition:transform .2s}.fq[open] summary span{transform:rotate(45deg)}
.fq p{margin:10px 0 0;font-size:16px;line-height:1.6;color:var(--muted)}
.legal{padding-block:24px 48px}
'''

def main():
    css_path = os.path.join(OUT,'blog','blog.css')
    css = open(css_path).read()
    if '/* pages: how it works' not in css:
        open(css_path,'w').write(css + EXTRA_CSS)
    open(os.path.join(OUT,'how-it-works','hiw.css'),'w').write(H2.CSS) if os.makedirs(os.path.join(OUT,'how-it-works'),exist_ok=True) is None else None
    files = {
        'how-it-works/index.html': page('/how-it-works/', 'How BookedOrion Works | AI Receptionist for HVAC', 'Step by step: how Molly answers, triages, books and reports on your HVAC calls, and how setup works in a few days.', *H2.how()),
        'about/index.html': page('/about/', 'About BookedOrion | AI Receptionist for HVAC', 'BookedOrion helps HVAC shops stop losing jobs to voicemail. Meet the founder and our promises.', AB.page(), '<link rel="stylesheet" href="/about/about.css?v=1">'),
        'getting-started/index.html': page('/getting-started/', 'Getting Started with BookedOrion | Live in Days', 'The six-step plan to get Molly live for your HVAC shop: what you do, what we do, what we need from you and how long it takes.', GS.page(), '<link rel="stylesheet" href="/getting-started/gs.css?v=1">'),
        'privacy/index.html': legal('/privacy/','Privacy Policy','LEGAL','How BookedOrion collects, uses and protects information, including call data and text messages.',PRIVACY),
        'terms/index.html': legal('/terms/','Terms of Service','LEGAL','Terms for the BookedOrion website, free trial, plans and text messaging program.',TERMS),
        'sms-terms/index.html': legal('/sms-terms/','SMS Terms','LEGAL','Terms for BookedOrion Alerts text messages: frequency, cost, HELP and STOP.',SMS),
        '404.html': NOTFOUND,
    }
    for rel,txt in files.items():
        p=os.path.join(OUT,rel); os.makedirs(os.path.dirname(p),exist_ok=True); open(p,'w').write(txt)
    os.makedirs(os.path.join(OUT,'getting-started'),exist_ok=True); open(os.path.join(OUT,'getting-started','gs.css'),'w').write(GS.CSS)
    os.makedirs(os.path.join(OUT,'about'),exist_ok=True); open(os.path.join(OUT,'about','about.css'),'w').write(AB.CSS)
    # sitemap
    urls=['/','/how-it-works/','/getting-started/','/about/','/blog/']+[f"/blog/{p['slug']}/" for p in B.POSTS]+['/privacy/','/terms/','/sms-terms/']
    sm='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join(f'  <url><loc>{B.SITE}{u}</loc><lastmod>{B.DATE}</lastmod></url>\n' for u in urls)+'</urlset>\n'
    open(os.path.join(OUT,'sitemap.xml'),'w').write(sm)
    print('pages built')

if __name__=='__main__':
    main()
