"""Getting started / onboarding page for bookedorion.com."""
import build_blog as B
from how_v2 import ic, P, MOLLY

def page():
    phases = [
        dict(n=1, when='Day 1', title='Kickoff', you='Fill a 3-field form. Pick a 15-minute call or do it all by email.', we='Reply within 1 business day and send your setup questions.', yt='2 min', icon='form'),
        dict(n=2, when='Day 1–2', title='Setup questions', you='Answer a short checklist about your shop (below).', we='Turn your answers into Molly’s script, rules and booking settings.', yt='~15 min', icon='q'),
        dict(n=3, when='Day 2–4', title='Build and test', you='Listen to a test call. Tell us anything to change.', we='Build Molly, connect your calendar, run test calls for every call type.', yt='~10 min', icon='tool'),
        dict(n=4, when='Go-live day', title='Turn on forwarding', you='Dial one code or change one setting. We stay on the phone with you.', we='Watch the first live calls and confirm texts reach you.', yt='~5 min', icon='fwd'),
        dict(n=5, when='Week 1', title='Fine-tune', you='Read the text summaries. Reply with anything that looks off.', we='Review every call with you and adjust the script the same day.', yt='As you like', icon='repeat'),
        dict(n=6, when='Day 14', title='You decide', you='Keep Molly or walk away.', we='Show you every booked job. No job booked? You pay nothing.', yt='1 min', icon='flag'),
    ]
    ph = ''
    for p in phases:
        ph += f'''<li class="gph">
<div class="gnode"><span>{ic(P[p['icon']],20)}</span></div>
<div class="gcard"><div class="gtop"><span class="gwhen">{p['when']}</span><span class="gyt">{ic(P['user'],14)} Your time: {p['yt']}</span></div>
<h3>{p['n']}. {p['title']}</h3>
<div class="gsplit"><div class="gyou"><div class="glab">YOU</div><p>{p['you']}</p></div><div class="gwe"><div class="glab">{MOLLY.replace('width="26" height="26"','width="16" height="16"')} BOOKEDORION</div><p>{p['we']}</p></div></div></div></li>'''

    checklist = [
        ('Business basics','Company name as callers know it, address, website'),
        ('Hours','When your office answers, and when Molly should take over'),
        ('Service area','The cities or ZIP codes you cover'),
        ('Services','What you do and don’t do (repairs, installs, tune-ups, brands)'),
        ('Fees','Diagnostic or trip fee Molly may mention. Nothing else is quoted.'),
        ('Emergencies','Your emergency words and who gets the call, day and night'),
        ('Calendar','Google or Outlook calendar to book on, and slot length'),
        ('Alerts','Mobile numbers and emails that should get call summaries'),
    ]
    cl = ''.join(f'<li><label><input type="checkbox" class="gck"><span class="gbox">{ic(P["check"],14,"#FFFFFF",3.2)}</span><span><b>{t}</b><em>{d}</em></span></label></li>' for t,d in checklist)

    carriers = [
        ('AT&amp;T','Dial <code>*61*</code> + Molly’s number + <code>#</code> for unanswered calls.'),
        ('Verizon','Dial <code>*71</code> + Molly’s number.'),
        ('T-Mobile','We send you the exact code for your line.'),
        ('Office phone','RingCentral, Grasshopper, Google Voice and others: one setting. We send screenshots.'),
    ]
    cr = ''.join(f'<div class="gcar"><b>{n}</b><span>{t}</span></div>' for n,t in carriers)

    faq = [
        ('How long until Molly is live?','Usually a few days after we get your setup answers. The test call step is the only one that waits on you.'),
        ('Do I have to be on a call?','No. You can do everything by email. If you prefer a call, it takes about 15 minutes.'),
        ('What if I’m busy in the middle of summer?','That’s when shops need this most. Your part adds up to about 30 minutes, spread over a few days.'),
        ('Can I turn it off?','Yes. Turning off call forwarding stops Molly right away. Your number never changes.'),
        ('Who do I talk to?','Siam, the founder, sets up every pilot himself. Email siam@bookedorion.com.'),
    ]
    fq = ''.join(f'<details class="fq"><summary>{q}<span aria-hidden="true">+</span></summary><p>{a}</p></details>' for q,a in faq)

    inner = f'''<section class="bhero gshero"><div class="wrap">
<div class="eyebrow">GETTING STARTED</div>
<h1>Live in days.<br><span class="gmint">About 30 minutes of your time.</span></h1>
<p>We do the setup, testing and tuning. You answer a few questions, hear a test call and flip on forwarding. Here’s the whole plan.</p>
<div class="gmeter" role="img" aria-label="Your part is about 30 minutes. BookedOrion does the rest.">
<div class="gmrow"><span class="gmk">Your part</span><div class="gmbar"><i class="gm-you"></i></div><b>~30 min</b></div>
<div class="gmrow"><span class="gmk">Our part</span><div class="gmbar"><i class="gm-us"></i></div><b>Everything else</b></div>
</div>
<div class="gbadges"><span>{ic(P['check'],16,'#2BD9A0',3)} No new software</span><span>{ic(P['check'],16,'#2BD9A0',3)} Same phone number</span><span>{ic(P['check'],16,'#2BD9A0',3)} Nothing goes live until you approve</span></div>
</div></section>
<div class="wrap pg">
<section class="blk"><div class="bh"><div class="eyebrow dk">THE PLAN</div><h2>Six steps. Most of the work is ours.</h2><p>Each step shows what you do, what we do, and how much of your time it takes.</p></div>
<ol class="gplan">{ph}</ol></section>

<section class="blk gtwo"><div class="bh"><div class="eyebrow dk">WHAT WE NEED FROM YOU</div><h2>Have these ready and setup goes fast.</h2>
<p>Don’t have everything? Send what you have. We fill gaps on a quick call.</p>
<div class="gprog"><div class="gpbar"><i id="gpfill"></i></div><span id="gptext">0 of {len(checklist)} ready</span></div></div>
<ul class="gcl">{cl}</ul></section>

<section class="blk"><div class="bh"><div class="eyebrow dk">GO-LIVE DAY</div><h2>Turning Molly on is one setting.</h2>
<p>Your number stays the same. Calls your team misses forward to Molly. To turn her off, cancel forwarding.</p></div>
<div class="gfwd"><div class="gfwdviz" aria-hidden="true">
<div class="gfn"><span>{ic(P['phone'],20)}</span><b>Homeowner calls your number</b></div><div class="gfa"></div>
<div class="gfn"><span>{ic(P['user'],20)}</span><b>Your team gets first try</b><em>~20 seconds</em></div><div class="gfa"></div>
<div class="gfn m"><span>{MOLLY}</span><b>No answer? Molly picks up</b></div></div>
<div class="gcars">{cr}<p class="gnote">Codes come from carrier help pages and can change. We confirm yours with you on go-live day.</p></div></div></section>

<section class="blk"><div class="gcontact"><img class="gav" src="/siam-2.jpg" alt="Siam Ahmed, founder of BookedOrion" width="84" height="84" style="object-fit:cover"><div><div class="eyebrow dk">YOUR CONTACT</div><h3>One person, start to finish.</h3>
<p>Siam, the founder, sets up every pilot and checks Molly’s calls with you in week one. No ticket queue.</p><p>Want to hear Molly first? Call <a href="tel:+15705219710">(570) 521-9710</a>.</p>
<a href="mailto:siam@bookedorion.com">siam@bookedorion.com</a></div></div></section>

<section class="blk"><div class="bh"><div class="eyebrow dk">QUESTIONS</div><h2>Getting started questions</h2></div><div class="fqs">{fq}</div></section>
{B.CTA}
</div>
<script>(function(){{var c=document.querySelectorAll('.gck'),f=document.getElementById('gpfill'),t=document.getElementById('gptext');
function u(){{var n=0;c.forEach(function(x){{if(x.checked)n++;}});f.style.width=(n/c.length*100)+'%';t.textContent=n+' of '+c.length+' ready'+(n===c.length?' ✓':'');}}
c.forEach(function(x){{x.addEventListener('change',u);}});}})();</script>'''
    return inner

CSS = '''/* Getting started */
.gshero{padding-block:72px 76px}
.gmint{background:linear-gradient(90deg,#2BD9A0,#8FF0CF);-webkit-background-clip:text;background-clip:text;color:transparent}
.gmeter{margin-top:22px;max-width:640px;display:flex;flex-direction:column;gap:12px;background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.12);border-radius:18px;padding:18px 20px}
.gmrow{display:grid;grid-template-columns:80px 1fr auto;gap:14px;align-items:center;font-size:14px}
.gmk{color:#B9B7DC;font-weight:600}.gmrow b{color:#FFF;font-size:14px;white-space:nowrap}
.gmbar{height:14px;border-radius:999px;background:rgba(255,255,255,.08);overflow:hidden}
.gmbar i{display:block;height:100%;border-radius:999px;animation:grow 1.2s cubic-bezier(.2,.8,.2,1) both}
.gm-you{width:9%;background:#2BD9A0}.gm-us{width:100%;background:linear-gradient(90deg,#3F37C9,#6C63FF);animation-delay:.2s!important}
@keyframes grow{from{width:0}}
.gbadges{display:flex;flex-wrap:wrap;gap:10px 22px;margin-top:8px;font-size:15px;color:#DCDAF5;font-weight:500}
.gbadges span{display:inline-flex;align-items:center;gap:8px}

.gplan{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:18px;position:relative}
.gplan::before{content:"";position:absolute;left:25px;top:30px;bottom:30px;width:2px;background:linear-gradient(180deg,#3F37C9,#6C63FF 60%,#2BD9A0)}
.gph{display:flex;gap:22px;align-items:flex-start;position:relative}
.gnode{flex-shrink:0;width:52px;height:52px;border-radius:50%;background:#FFF;border:2px solid #3F37C9;color:#3F37C9;display:flex;align-items:center;justify-content:center;position:relative;z-index:1}
.gph:last-child .gnode{background:#2BD9A0;border-color:#2BD9A0;color:#0B0A24}
.gcard{flex:1;min-width:0;border:1px solid var(--line);border-radius:22px;padding:22px 24px;display:flex;flex-direction:column;gap:12px;transition:box-shadow .2s,transform .2s;background:#FFF}
.gcard:hover{box-shadow:0 18px 40px rgba(15,13,46,.08);transform:translateY(-2px)}
.gtop{display:flex;flex-wrap:wrap;justify-content:space-between;gap:8px}
.gwhen{font-size:12px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--indigo)}
.gyt{display:inline-flex;align-items:center;gap:6px;font-size:13px;font-weight:700;color:#0B5E44;background:#E6FBF4;padding:4px 10px;border-radius:999px}
.gcard h3{margin:0;font-size:21px;letter-spacing:-.01em}
.gsplit{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,240px),1fr));gap:12px}
.gyou,.gwe{border-radius:14px;padding:14px 16px}
.gyou{background:var(--wash)}.gwe{background:#EEEDFB}
.glab{display:flex;align-items:center;gap:6px;font-size:11px;font-weight:700;letter-spacing:.12em;color:var(--soft);margin-bottom:4px}
.gwe .glab{color:#3F37C9}.gwe .glab svg circle{stroke:#3F37C9}
.gsplit p{margin:0;font-size:15px;line-height:1.55;color:var(--ink)}

.gtwo{flex-direction:row!important;flex-wrap:wrap;gap:40px;align-items:flex-start}
.gtwo .bh{flex:1 1 340px;position:sticky;top:96px}
.gprog{display:flex;align-items:center;gap:12px;margin-top:6px}
.gpbar{flex:1;height:10px;border-radius:999px;background:var(--line);overflow:hidden}
.gpbar i{display:block;height:100%;width:0;background:linear-gradient(90deg,#3F37C9,#2BD9A0);transition:width .35s ease}
#gptext{font-size:14px;font-weight:700;color:var(--ink);white-space:nowrap;font-variant-numeric:tabular-nums}
.gcl{flex:1.3 1 420px;min-width:0;list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,260px),1fr));gap:12px}
.gcl label{display:flex;gap:12px;align-items:flex-start;border:1px solid var(--line);border-radius:16px;padding:16px;cursor:pointer;transition:border-color .15s,background .15s;min-height:44px}
.gcl label:hover{border-color:#B9B6E8}
.gck{position:absolute;opacity:0;width:1px;height:1px}
.gbox{width:24px;height:24px;flex-shrink:0;border-radius:7px;border:2px solid #CFCDE3;display:flex;align-items:center;justify-content:center;transition:background .15s,border-color .15s}
.gbox svg{opacity:0;transition:opacity .15s}
.gck:checked+.gbox{background:#2BD9A0;border-color:#2BD9A0}.gck:checked+.gbox svg{opacity:1}
.gck:focus-visible+.gbox{outline:3px solid #2BD9A0;outline-offset:2px}
.gcl label:has(.gck:checked){background:#F2FCF8;border-color:#9EEBCF}
.gcl b{display:block;font-size:16px}.gcl em{display:block;font-style:normal;font-size:14px;line-height:1.5;color:var(--muted);margin-top:2px}

.gfwd{display:flex;flex-wrap:wrap;gap:28px;align-items:stretch}
.gfwdviz{flex:1 1 360px;min-width:0;background:var(--night);border-radius:24px;padding:26px;display:flex;flex-direction:column;align-items:stretch}
.gfn{display:flex;align-items:center;gap:12px;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.12);border-radius:16px;padding:14px 16px;color:#FFF}
.gfn span{width:40px;height:40px;border-radius:12px;background:rgba(255,255,255,.1);display:flex;align-items:center;justify-content:center;flex-shrink:0}
.gfn b{font-size:16px}.gfn em{margin-left:auto;font-style:normal;font-size:13px;color:#A9A7D4;white-space:nowrap}
.gfn.m{background:linear-gradient(160deg,#3F37C9,#2A23A6);border-color:#5B54E0}.gfn.m span{background:rgba(255,255,255,.16)}
.gfa{width:2px;height:22px;margin:0 auto;background:repeating-linear-gradient(180deg,#2BD9A0 0 5px,transparent 5px 9px)}
.gcars{flex:1 1 360px;min-width:0;display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,200px),1fr));gap:12px;align-content:start}
.gcar{border:1px solid var(--line);border-radius:16px;padding:16px;display:flex;flex-direction:column;gap:6px}
.gcar b{font-size:16px}.gcar span{font-size:14px;line-height:1.55;color:var(--muted)}
.gcar code{font-family:ui-monospace,Menlo,Consolas,monospace;font-size:13px;background:#EEEDFB;color:#2A23A6;padding:1px 6px;border-radius:6px}
.gnote{grid-column:1/-1;margin:0;font-size:13px;color:var(--soft)}

.gcontact{display:flex;flex-wrap:wrap;gap:24px;align-items:center;border:1px solid var(--line);border-radius:24px;padding:28px;background:linear-gradient(135deg,#FFFFFF,#F7F7FC)}
.gav{width:84px;height:84px;border-radius:50%;background:linear-gradient(135deg,#3F37C9,#6C63FF);color:#FFF;font-weight:700;font-size:28px;display:flex;align-items:center;justify-content:center;box-shadow:0 0 0 6px #EEEDFB}
.gcontact>div:last-child{flex:1 1 320px;min-width:0;display:flex;flex-direction:column;gap:6px}
.gcontact h3{margin:0;font-size:24px}.gcontact p{margin:0;font-size:16px;line-height:1.6;color:var(--muted)}
.gcontact a{font-weight:700;font-size:16px}
@media (max-width:640px){.gplan::before{left:21px}.gnode{width:44px;height:44px}.gph{gap:14px}.gtwo .bh{position:static}.gmrow{grid-template-columns:70px 1fr}.gmrow b{grid-column:2}}
@media (prefers-reduced-motion:reduce){.gmbar i{animation:none}}
'''
