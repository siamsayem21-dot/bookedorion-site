#!/usr/bin/env python3
"""Builds /pricing/ for bookedorion.com.

Standalone on purpose: it borrows the head, header and footer from the published
/about/ page, so it always matches the live site without running the full build.
Run from the repo root:  python3 _source/pricing.py
Every number here comes from 00_LOCKED_RULEBOOK.md and the Terms page.
"""
import json, os, re

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
URL = 'https://bookedorion.com/pricing/'
TITLE = 'AI Receptionist Pricing for HVAC | BookedOrion'
DESC = ('BookedOrion pricing: $79 a month plus $29 per booked job, never more than $449, '
        'or $249 flat with unlimited bookings. 14-day free trial, no setup fee.')

BASE, PER_JOB, CAP, FLAT, NIGHT = 79, 29, 449, 249, 49

def ppj(n):
    return min(BASE + PER_JOB * n, CAP)

CHECK = ('<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" '
         'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12l5 5L20 7"/></svg>')
CROSS = ('<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" '
         'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"/></svg>')

def li(items, icon=CHECK):
    return ''.join(f'<li>{icon}<span>{t}</span></li>' for t in items)

# ---------- content ----------
INCLUDED = [
    'Answers the calls your team misses, and every call at night, on weekends and holidays',
    'Books jobs straight onto your Google or Outlook calendar',
    'A text summary after every call, with one-tap confirm',
    'A recording and transcript of every call',
    'A call-back list of callers who didn’t book',
    'A short report every Monday',
    'Google review requests after each finished job',
    'Setup done for you. Changes by text, done by the next business day',
]

COUNTS = [
    'A new appointment from a call Molly handled',
    'You confirm it with one tap in the text summary',
    'No reply within 48 hours counts as booked',
    'A no-show, or a customer who says no at the door',
]
NOT_COUNTS = [
    'Spam and wrong-number calls',
    'Duplicates, or callers outside your service area',
    'Calls that weren’t a real job',
    'Cancellations with a record, made before the visit and within 7 days',
]

EXAMPLES = [0, 3, 5, 6, 10, 13]

FAQ = [
    ('How much does BookedOrion cost?',
     'Two plans. Pay-per-Job is $79 a month plus $29 for each booked job, and never more than $449 in a month. '
     'Flat is $249 a month with unlimited booked jobs. Both include 400 call minutes a month and start with a free 14-day trial.'),
    ('Is there a setup fee or a contract?',
     'No. Setup is free and we do it for you. Plans are month to month, and you can cancel at any time. '
     'Cancellation takes effect at the end of the current billing month.'),
    ('How does the free trial work?',
     'We set Molly up for your shop and run her free for 14 days. After the trial, you choose a plan or stop. '
     'There’s nothing to cancel if you stop.'),
    ('What if Molly books nothing in my first month?',
     'On Pay-per-Job, if Molly books no jobs in your first paid month, that month is free.'),
    ('What counts as a booked job?',
     'A new appointment from a call Molly handled. You confirm it with one tap in the text summary. '
     'If you don’t reply within 48 hours, it counts as booked. The call recording and summary are the record.'),
    ('What if a customer cancels or doesn’t show up?',
     'Cancellations are free when there’s a record: the customer called or texted Molly, or you send us the call recording '
     'or a screenshot of the text. It must be before the appointment and within 7 days. A no-show still counts, '
     'because the appointment was made.'),
    ('Do spam and wrong-number calls count?',
     'Never. They don’t count as booked jobs and they’re never billed.'),
    ('What happens if we use more than 400 minutes?',
     'We text you at 80% (320 minutes). One busy month is fine. If you go over two months in a row, '
     'we agree on a bigger plan together. No surprise bills.'),
    ('Which plan should I pick?',
     'Not sure? Start with Pay-per-Job. Each month we show you which plan would have cost you less, '
     'and you can switch.'),
    ('We only need nights and weekends. Is there a plan for that?',
     'Yes. Night-only is $49 a month plus $29 per booked job. Your own team answers during the day, '
     'and Molly covers nights, weekends and holidays.'),
    ('How do I pay?',
     'By a secure invoice link each month. Molly never takes card numbers or payment details on a call.'),
]

ADDONS = [
    ('Tune-up reminders', 'Before summer and winter, past customers who agreed to hear from you get a reminder to book their check.', '$49', '/month'),
    ('Estimate follow-up', 'Gave a price and heard nothing? A short, polite follow-up on day 2, 5 and 10, then it stops.', '$49', '/month'),
    ('Google Business Profile tune-up', 'Photos, services, hours, service area and help replying to reviews. Google decides rankings, so we never promise a position.', '$199', 'one time'),
    ('A website for your shop', 'A fast, mobile-first site on your own domain. You see a free design preview before you pay anything.', '$600', '+ $49/month'),
]

# ---------- sections ----------
def hero():
    return f'''<section class="bhero"><div class="wrap prh">
<div class="eyebrow">Pricing</div>
<h1>AI receptionist pricing for HVAC shops</h1>
<p>$79 a month plus $29 per booked job, or $249 a month flat. Every plan starts with a free 14-day trial. We set it up for you. No setup fee, no contract.</p>
<div class="prh-cta"><a class="btn" href="/#start">Start free trial</a><a class="prh-call" href="tel:+15705219710">Or call Molly: (570) 521-9710</a></div>
</div></section>'''

def plans():
    return f'''<section class="blk" id="plans"><div class="bh"><div class="eyebrow dk">Plans</div><h2>Two plans. Same Molly on both.</h2>
<p>The only difference is how you pay. Everything else is the same: setup, features and support.</p></div>
<div class="prp">
<article class="prc is-main">
<div class="prc-top"><h3>Pay-per-Job</h3><span class="prc-tag">Start here</span></div>
<p class="prc-sub">Low base, then pay per booked job</p>
<div class="prc-price"><b>${BASE}</b><span>a month + ${PER_JOB} per booked job</span></div>
<ul class="prc-facts">{li([f'Never more than ${CAP} in a month', 'No jobs booked in your first paid month? That month is free', 'Best for quieter months and slow seasons'])}</ul>
<a class="btn" href="/#start">Start free trial</a>
</article>
<article class="prc">
<div class="prc-top"><h3>Flat</h3></div>
<p class="prc-sub">One price, unlimited bookings</p>
<div class="prc-price"><b>${FLAT}</b><span>a month</span></div>
<ul class="prc-facts">{li(['Unlimited booked jobs', 'No per-job charge, however many she books', 'Best for busy months'])}</ul>
<a class="btn btn-line" href="/#start">Start free trial</a>
</article>
</div>
<p class="prn"><b>Only need nights and weekends?</b> Night-only is ${NIGHT} a month plus ${PER_JOB} per booked job. Your team answers by day, Molly covers nights, weekends and holidays.</p>
<p class="prn">Both plans include 400 call minutes a month. Spam and wrong-number calls are never counted.</p>
</section>'''

def calculator():
    rows = ''.join(f'<tr><th scope="row">{n}{"+" if n == 13 else ""}</th><td>${ppj(n)}{'<small class="prz">$0 in your first paid month</small>' if n == 0 else ""}</td><td>${FLAT}</td></tr>' for n in EXAMPLES)
    return f'''<section class="blk" id="calculator"><div class="bh"><div class="eyebrow dk">Your bill</div><h2>What would you pay in a month?</h2>
<p>Move the slider to the number of jobs Molly books for you in a month.</p></div>
<div class="prcalc" data-base="{BASE}" data-job="{PER_JOB}" data-cap="{CAP}" data-flat="{FLAT}">
<label class="prcalc-l" for="jobs">Booked jobs this month: <output id="jobs-out" for="jobs">4</output></label>
<input id="jobs" type="range" min="0" max="20" step="1" value="4">
<div class="prcalc-r">
<div class="prcalc-b" data-k="ppj"><span>Pay-per-Job</span><b data-v="ppj">$195</b><small data-m="ppj">$79 + 4 × $29</small><i class="prbar"><i data-w="ppj" style="width:43%"></i></i></div>
<div class="prcalc-b" data-k="flat"><span>Flat</span><b data-v="flat">$249</b><small>Same every month</small><i class="prbar"><i data-w="flat" style="width:55%"></i></i></div>
</div>
<p class="prcalc-s" data-s aria-live="polite">Pay-per-Job costs $54 less this month.</p>
</div>
<div class="prtbl"><table><caption>Example monthly bills</caption><thead><tr><th scope="col">Booked jobs</th><th scope="col">Pay-per-Job</th><th scope="col">Flat</th></tr></thead><tbody>{rows}</tbody></table></div>
<p class="prn">Pay-per-Job stops at ${CAP}, however many jobs she books. Each month we show you which plan would have cost you less.</p>
</section>'''

def booked():
    return f'''<section class="blk" id="booked-job"><div class="bh"><div class="eyebrow dk">The $29</div><h2>What counts as a booked job</h2>
<p>You only see the $29 for real appointments, and every one has a call recording behind it.</p></div>
<div class="prbk">
<div class="prbk-c yes"><h3>Counts</h3><ul>{li(COUNTS)}</ul></div>
<div class="prbk-c no"><h3>Never counts</h3><ul>{li(NOT_COUNTS, CROSS)}</ul></div>
</div>
<p class="prn">Mark a booking as “not booked” in the text and pick a reason. We check the recording before removing the charge. Full rules are in our <a href="/terms/">Terms</a>.</p>
</section>'''

def included():
    return f'''<section class="blk" id="included"><div class="bh"><div class="eyebrow dk">Included</div><h2>Included on every plan</h2></div>
<ul class="princ">{li(INCLUDED)}</ul>
<p class="prn">Texts to your customers start once your number is registered for business texting. We handle that during setup.</p>
</section>'''

def addons():
    items = ''.join(f'<div class="prao"><div><b>{t}</b><p>{d}</p></div><div class="prao-p"><b>{p}</b><span>{u}</span></div></div>' for t, d, p, u in ADDONS)
    return f'''<section class="blk" id="add-ons"><div class="bh"><div class="eyebrow dk">Optional</div><h2>Add-ons</h2>
<p>Add any of these to either plan. Take both tune-up reminders and estimate follow-up for $79 a month.</p></div>
<div class="praos">{items}</div>
<p class="prn">The website price is our founding price for the first shops.</p>
</section>'''

def compare():
    return '''<section class="blk"><div class="bh"><div class="eyebrow dk">Other options</div><h2>How this compares to an answering service</h2>
<p>Many answering services bill by the minute or by the call, whether or not a job gets booked. With Pay-per-Job, you pay a $79 base, and the rest only for jobs that land on your calendar.</p>
<p><a href="/blog/answering-service-vs-ai-receptionist/">Read the full comparison: answering service vs AI receptionist</a></p></div>
</section>'''

def faq():
    qs = ''.join(f'<details class="fq"><summary>{q}<i aria-hidden="true">+</i></summary><p>{a}</p></details>' for q, a in FAQ)
    return f'''<section class="blk" id="faq"><div class="bh"><div class="eyebrow dk">Questions</div><h2>Pricing questions</h2></div>
<div class="prfaq">{qs}</div></section>'''

def cta():
    return '''<section class="blk"><div class="prend"><h2>Try Molly free for 14 days</h2>
<p>We set her up for your hours, fees and service area. You keep your number and learn no new software.</p>
<div class="prh-cta"><a class="btn" href="/#start">Start free trial</a><a class="prh-call" href="tel:+15705219710">Call Molly: (570) 521-9710</a></div></div></section>'''

JS = '''<script>
(function(){var c=document.querySelector('.prcalc');if(!c)return;
var B=+c.dataset.base,J=+c.dataset.job,C=+c.dataset.cap,F=+c.dataset.flat,r=document.getElementById('jobs'),o=document.getElementById('jobs-out');
function q(s){return c.querySelector(s)}
function u(){var n=+r.value,p=Math.min(B+J*n,C),mx=Math.max(C,F);o.textContent=n;
q('[data-v=ppj]').textContent='$'+p;
q('[data-m=ppj]').textContent=(B+J*n>C)?'Capped at $'+C:'$'+B+' + '+n+' × $'+J;
q('[data-w=ppj]').style.width=(p/mx*100)+'%';q('[data-w=flat]').style.width=(F/mx*100)+'%';
c.querySelector('[data-k=ppj]').classList.toggle('lo',p<F);c.querySelector('[data-k=flat]').classList.toggle('lo',F<p);
var s=q('[data-s]');
if(p<F)s.textContent='Pay-per-Job costs $'+(F-p)+' less this month.'+(n===0?' In your first paid month, it would be $0.':'');
else if(F<p)s.textContent='Flat costs $'+(p-F)+' less this month.';
else s.textContent='Both plans cost the same this month.';}
r.addEventListener('input',u);u();})();
</script>'''

CSS = '''.prh{display:flex;flex-direction:column;gap:16px}
.prh-cta{display:flex;flex-wrap:wrap;align-items:center;gap:12px 20px;margin-top:8px}
.prh-call{color:var(--ink);font-weight:600;text-decoration:none;border-bottom:1px solid var(--line)}
.prh-call:hover{border-color:var(--ink)}
.btn-line{background:#fff!important;color:var(--ink)!important;border:1px solid var(--line)!important;box-shadow:none!important}
.prp{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:20px}
.prc{background:#fff;border:1px solid var(--line);border-radius:20px;padding:28px;display:flex;flex-direction:column;gap:14px}
.prc.is-main{border-color:var(--ink);box-shadow:var(--lift)}
.prc-top{display:flex;justify-content:space-between;align-items:center;gap:12px}
.prc h3{margin:0;font-size:22px;font-weight:600}
.prc-tag{font-size:13px;font-weight:600;color:var(--mintdk);background:var(--mintsoft);border-radius:999px;padding:4px 10px}
.prc-sub{margin:0;color:var(--muted)}
.prc-price{display:flex;align-items:baseline;flex-wrap:wrap;gap:8px}
.prc-price b{font-size:48px;line-height:1;font-weight:600;letter-spacing:-.03em;font-variant-numeric:tabular-nums}
.prc-price span{color:var(--muted)}
.prc ul,.prbk ul,.princ{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:10px}
.prc li,.prbk li,.princ li{display:flex;gap:10px;align-items:flex-start;line-height:1.5}
.prc li svg,.princ li svg,.prbk .yes li svg{flex:none;margin-top:4px;color:var(--mintdk)}
.prbk .no li svg{flex:none;margin-top:4px;color:var(--soft)}
.prc .btn{margin-top:auto;align-self:flex-start}
.prn{margin:0;color:var(--muted);line-height:1.6;max-width:760px}
.prn a,.bh p a{color:var(--indigo)}
.prcalc{background:#fff;border:1px solid var(--line);border-radius:20px;padding:28px;display:flex;flex-direction:column;gap:18px}
.prcalc-l{font-weight:600}
.prcalc-l output{font-variant-numeric:tabular-nums}
.prcalc input[type=range]{width:100%;accent-color:var(--indigo);height:28px}
.prcalc-r{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px}
.prcalc-b{border:1px solid var(--line);border-radius:14px;padding:18px;display:flex;flex-direction:column;gap:4px;transition:border-color .2s}
.prcalc-b span{color:var(--muted);font-weight:600}
.prcalc-b b{font-size:36px;font-weight:600;letter-spacing:-.02em;font-variant-numeric:tabular-nums}
.prcalc-b small{color:var(--soft);font-variant-numeric:tabular-nums}
.prbar{display:block;height:6px;border-radius:6px;background:var(--paper);margin-top:10px;overflow:hidden}
.prbar i{display:block;height:100%;background:var(--soft);border-radius:6px;transition:width .2s}
.prcalc-b.lo{border-color:var(--mintdk)}
.prcalc-b.lo .prbar i{background:var(--mint)}
.prcalc-s{margin:0;font-weight:600}
.prtbl{overflow-x:auto;border:1px solid var(--line);border-radius:16px;background:#fff}
.prtbl table{width:100%;min-width:0;border-collapse:collapse;font-variant-numeric:tabular-nums}
.prtbl caption{text-align:left;padding:16px 20px 4px;font-weight:600}
.prtbl th,.prtbl td{padding:12px 20px;text-align:left;border-top:1px solid var(--line)}
.prtbl thead th{color:var(--muted);font-weight:600;font-size:14px}
.prtbl small{color:var(--soft)}
.prz{display:block;font-size:13px}
.prtbl tbody th{background:none;font-weight:600}
.prbk{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:20px}
.prbk-c{background:#fff;border:1px solid var(--line);border-radius:20px;padding:24px;display:flex;flex-direction:column;gap:14px}
.prbk-c h3{margin:0;font-size:18px;font-weight:600}
.princ{display:grid!important;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px 28px!important}
.praos{display:flex;flex-direction:column;border:1px solid var(--line);border-radius:20px;background:#fff}
.prao{display:flex;justify-content:space-between;gap:24px;padding:20px 24px;border-top:1px solid var(--line)}
.prao:first-child{border-top:0}
.prao p{margin:4px 0 0;color:var(--muted);line-height:1.5}
.prao-p{text-align:right;flex:none;display:flex;flex-direction:column}
.prao-p b{font-size:20px;font-weight:600;font-variant-numeric:tabular-nums}
.prao-p span{color:var(--soft);font-size:14px}
.prfaq{display:flex;flex-direction:column;gap:10px;max-width:860px}
.prfaq .fq p{margin:12px 0 0;color:var(--muted);line-height:1.65}
.prfaq .fq summary i{font-style:normal;color:var(--soft);transition:transform .2s}
.prfaq .fq[open] summary i{transform:rotate(45deg)}
.prend{background:var(--paper);border:1px solid var(--line);border-radius:24px;padding:40px;display:flex;flex-direction:column;gap:12px;margin-bottom:56px}
.prend h2{margin:0;font-size:clamp(26px,3.2vw,36px);font-weight:600;letter-spacing:-.02em}
.prend p{margin:0;color:var(--muted)}
@media (max-width:760px){.prtbl th,.prtbl td{padding:10px 12px}.prtbl caption{padding:14px 12px 4px}.prp,.prcalc-r,.prbk,.princ{grid-template-columns:1fr}.prc,.prcalc,.prend{padding:22px}.prao{flex-direction:column;gap:8px}.prao-p{text-align:left;flex-direction:row;gap:6px;align-items:baseline}.prc-price b{font-size:40px}}
@media (prefers-reduced-motion:reduce){.prbar i,.prcalc-b,.prfaq .fq summary i{transition:none}}
'''

def jsonld():
    service = {
        '@context': 'https://schema.org', '@type': 'Service',
        'name': 'AI receptionist for HVAC companies', 'url': URL,
        'provider': {'@type': 'Organization', 'name': 'BookedOrion', 'url': 'https://bookedorion.com/'},
        'offers': [
            {'@type': 'Offer', 'name': 'Pay-per-Job', 'price': str(BASE), 'priceCurrency': 'USD', 'url': URL,
             'description': f'${BASE} per month plus ${PER_JOB} per booked job, never more than ${CAP} a month. 400 call minutes. 14-day free trial.'},
            {'@type': 'Offer', 'name': 'Flat', 'price': str(FLAT), 'priceCurrency': 'USD', 'url': URL,
             'description': f'${FLAT} per month, unlimited booked jobs, 400 call minutes. 14-day free trial.'},
            {'@type': 'Offer', 'name': 'Night-only', 'price': str(NIGHT), 'priceCurrency': 'USD', 'url': URL,
             'description': f'${NIGHT} per month plus ${PER_JOB} per booked job. Nights, weekends and holidays only.'},
        ],
    }
    faqld = {'@context': 'https://schema.org', '@type': 'FAQPage', 'mainEntity': [
        {'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in FAQ]}
    crumbs = {'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': [
        {'@type': 'ListItem', 'position': 1, 'name': 'Home', 'item': 'https://bookedorion.com/'},
        {'@type': 'ListItem', 'position': 2, 'name': 'Pricing', 'item': URL}]}
    return ''.join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in (service, faqld, crumbs))

def build():
    shell = open(os.path.join(ROOT, 'about', 'index.html')).read()
    head_end = shell.index('</head>')
    head = shell[:head_end]
    # page-specific head
    head = re.sub(r'<title>.*?</title>', f'<title>{TITLE}</title>', head)
    head = re.sub(r'(<meta name="description" content=")[^"]*', lambda m: m.group(1) + DESC, head)
    head = re.sub(r'(<meta property="og:title" content=")[^"]*', lambda m: m.group(1) + TITLE, head)
    head = re.sub(r'(<meta property="og:description" content=")[^"]*', lambda m: m.group(1) + DESC, head)
    head = head.replace('content="article"', 'content="website"')
    head = head.replace('https://bookedorion.com/about/', URL)
    head = head.replace('/about/about.css?v=1', '/pricing/pricing.css?v=1')
    head = re.sub(r'<script type="application/ld\+json">.*?</script>', '', head, flags=re.S)
    head += jsonld() + '\n'
    rest = shell[head_end:]
    body_start = rest.index('<main>')
    header = rest[:body_start].replace('class="nav on" href="/about/"', 'class="nav" href="/about/"')
    header = header.replace('class="nav" href="/pricing/"', 'class="nav on" href="/pricing/"')
    footer = rest[rest.index('</main>'):]
    main = ('<main>' + hero() + '<div class="wrap pg">' + plans() + calculator() + booked() + included()
            + addons() + compare() + faq() + cta() + '</div>' + JS)
    html = head + header + main + footer
    os.makedirs(os.path.join(ROOT, 'pricing'), exist_ok=True)
    open(os.path.join(ROOT, 'pricing', 'index.html'), 'w').write(html)
    open(os.path.join(ROOT, 'pricing', 'pricing.css'), 'w').write(CSS)
    print('built pricing/index.html', len(html), 'bytes')

if __name__ == '__main__':
    build()
