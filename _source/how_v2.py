"""Visual version of the How it works page. Imported by build_pages.py."""
import json
import build_blog as B

def ic(paths, size=22, color='currentColor', sw=2.2):
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="{sw}" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{paths}</svg>')

P = {
 'phone': '<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.91.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92z"/>',
 'chat': '<path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/>',
 'alert': '<path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/><path d="M12 9v4M12 17h.01"/>',
 'user': '<path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/>',
 'pin': '<path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/>',
 'dollar': '<path d="M12 1v22M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/>',
 'cal': '<rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18M9 16l2 2 4-4"/>',
 'repeat': '<path d="M17 1l4 4-4 4M3 11V9a4 4 0 0 1 4-4h14M7 23l-4-4 4-4M21 13v2a4 4 0 0 1-4 4H3"/>',
 'msg': '<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>',
 'form': '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6M8 13h8M8 17h5"/>',
 'q': '<circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3M12 17h.01"/>',
 'tool': '<path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/>',
 'fwd': '<path d="M15 3h6v6M14 10l7-7"/><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.91.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92z"/>',
 'flag': '<path d="M4 15s1-1 4-1 5 2 8 2 4-1 4-1V3s-1 1-4 1-5-2-8-2-4 1-4 1zM4 22v-7"/>',
 'check': '<path d="M5 12l5 5L20 7"/>',
 'x': '<path d="M6 6l12 12M18 6L6 18"/>',
 'moon': '<path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/>',
 'sun': '<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/>',
 'mail': '<rect x="2" y="4" width="20" height="16" rx="2"/><path d="M22 6l-10 7L2 6"/>',
 'mic': '<rect x="9" y="2" width="6" height="12" rx="3"/><path d="M19 10v1a7 7 0 0 1-14 0v-1M12 18v4"/>',
}
MOLLY = ('<svg width="26" height="26" viewBox="0 0 64 64" aria-hidden="true"><circle cx="32" cy="32" r="20" fill="none" stroke="#FFFFFF" stroke-width="7"/>'
         '<path d="M23.5 32.5 L30 39 L41.5 25.5" fill="none" stroke="#2BD9A0" stroke-width="6.5" stroke-linecap="round" stroke-linejoin="round"/></svg>')
ARROW = '<div class="farr" aria-hidden="true"><span></span></div>'

def flow():
    nodes = [
        ('phone','Homeowner calls','9:47 PM · AC blowing warm air','c1'),
        (None,'Molly answers','In seconds, any hour','c2'),
        ('cal','Job booked','Wed 8:00 AM on your calendar','c3'),
        ('msg','You get a text','Name, address, problem, time','c4'),
    ]
    out=[]
    for i,(k,t,s,c) in enumerate(nodes):
        icon = MOLLY if k is None else ic(P[k],24)
        out.append(f'<div class="fnode {c}"><div class="fic">{icon}</div><b>{t}</b><span>{s}</span></div>')
        if i < len(nodes)-1: out.append(ARROW)
    return '<div class="flow" role="img" aria-label="A homeowner calls, Molly answers, the job is booked on your calendar, and you get a text.">' + ''.join(out) + '</div>'

def bar(kind):
    # 24h strip: 0-8 night, 8-18 office, 18-24 evening
    if kind=='porch':
        segs=[('m',8,'Molly'),('t',10,'Your team'),('m',6,'Molly')]
    else:
        segs=[('m',8,'Molly'),('h',10,'Team first'),('m',6,'Molly')]
    s=''.join(f'<span class="seg {c}" style="flex:{w}"><em>{lbl}</em></span>' for c,w,lbl in segs)
    return f'<div class="dbar" aria-hidden="true">{s}</div><div class="dlab" aria-hidden="true"><span>12a</span><span>6a</span><span>12p</span><span>6p</span><span>12a</span></div>'


SCEN = [
 ('cool','AC not cooling','phone','“My AC is running but blowing warm air.”',
  ['Asks name, address and ZIP','Confirms you serve that area','States your diagnostic fee','Offers open slots on your calendar'],
  'ok','Job booked · Wed 8:00 AM','You get a text with all the details.'),
 ('gas','Gas smell','alert','“I smell gas near my furnace.”',
  ['Tells caller to get outside right away','Tells them to call 911 and the gas company from outside','Rings your on-call phone immediately','Texts you the address'],
  'urgent','You’re called in seconds','Safety first. Molly does not book a routine visit.'),
 ('heat','No heat, elderly caller','user','“The heat’s out and my mother is 82.”',
  ['Flags it as urgent (vulnerable person)','Follows your rule: ring you now or first slot','Takes the address and callback number','Confirms what happens next'],
  'urgent','Urgent alert to you','Your rule decides: tonight or first thing.'),
 ('area','Outside your area','pin','“I’m in Waco. Can you come out?”',
  ['Checks the ZIP against your service area','Politely says it’s outside your area','Doesn’t book a job you can’t take','Logs the call for you'],
  'neutral','No booking, no wasted trip','You still see the call in your summary.'),
 ('price','Price question','dollar','“How much to come look at my unit?”',
  ['Gives only the fee you approved','Never guesses a repair price','Offers to book the diagnostic visit','Books it if the caller agrees'],
  'ok','Diagnostic visit booked','No made-up prices. Ever.'),
 ('human','Wants a real person','chat','“Can I talk to someone?”',
  ['Doesn’t argue or stall','Transfers the call to you','Takes a message if no one picks up','Texts you right away'],
  'neutral','Handed to you','Upset callers never get stuck with a robot.'),
]

def scenarios():
    tabs=''.join(f'<button type="button" class="stab{" on" if i==0 else ""}" data-i="{i}" aria-pressed="{"true" if i==0 else "false"}">{ic(P[k],18)}<span>{t}</span></button>' for i,(sid,t,k,*_) in enumerate(SCEN))
    data=json.dumps([dict(say=say,steps=st,kind=kd,res=res,note=note) for (_,_,_,say,st,kd,res,note) in SCEN])
    first=SCEN[0]
    steps=''.join(f'<li>{ic(P["check"],16,"#3F37C9",3)}<span>{x}</span></li>' for x in first[4])
    return f"""<div class="scen"><div class="stabs" role="group" aria-label="Pick a type of call">{tabs}</div>
<div class="spath" aria-live="polite">
<div class="snode caller"><div class="slab">CALLER SAYS</div><div class="ssay" id="ssay">{first[3]}</div></div>
<div class="sline" aria-hidden="true"></div>
<div class="snode molly"><div class="slab">{MOLLY}<span>MOLLY DOES</span></div><ul id="ssteps">{steps}</ul></div>
<div class="sline" aria-hidden="true"></div>
<div class="snode res ok" id="sres"><div class="slab">RESULT</div><b id="sresb">{first[6]}</b><span id="snote">{first[7]}</span></div>
</div></div>
<script>(function(){{var D={data};var tabs=document.querySelectorAll('.stab');var chk='{ic(P["check"],16,"#3F37C9",3).replace("'","&#39;")}';
function show(i){{var d=D[i];tabs.forEach(function(t,j){{t.classList.toggle('on',j==i);t.setAttribute('aria-pressed',j==i?'true':'false');}});
document.getElementById('ssay').textContent=d.say;var ul=document.getElementById('ssteps');ul.innerHTML='';
d.steps.forEach(function(s){{var li=document.createElement('li');li.innerHTML=chk;var sp=document.createElement('span');sp.textContent=s;li.appendChild(sp);ul.appendChild(li);}});
var r=document.getElementById('sres');r.className='snode res '+d.kind;document.getElementById('sresb').textContent=d.res;document.getElementById('snote').textContent=d.note;
var p=document.querySelector('.spath');p.classList.remove('anim');void p.offsetWidth;p.classList.add('anim');}}
tabs.forEach(function(t){{t.addEventListener('click',function(){{show(+t.dataset.i);}});}});}})();</script>"""

def how():
    modes = [
        ('Porchlight','$197/mo','After hours only','Your office answers during the day as usual. When you close, Molly answers.', bar('porch'), ''),
        ('Full Desk','$397/mo','After hours + daytime overflow','Your team still answers first. If nobody picks up in about 20 seconds, or the line is busy, Molly takes it.', bar('full'), ''),
        ('Revenue Desk','$797/mo','Everything + follow-ups','Full Desk coverage, plus follow-ups that bring back old estimates and tune-up customers.', bar('full'),
         '<div class="addons"><span>'+ic(P['mail'],15)+' Estimate follow-ups</span><span>'+ic(P['cal'],15)+' Tune-up reminders</span><span>'+ic(P['flag'],15)+' Monthly report</span></div>'),
    ]
    BADGE='<div class="badge">RECOMMENDED</div>'
    mode_html=''.join(f'<div class="mode{" pop" if i==1 else ""}">{BADGE if i==1 else ""}<div class="mtop"><b>{n}</b><span>{p}</span></div><div class="mk">{k}</div>{viz}<p>{d}</p>{extra}</div>' for i,(n,p,k,d,viz,extra) in enumerate(modes))
    legend = f'<div class="legend"><span><i class="lg m"></i>Molly answers every call</span><span><i class="lg h"></i>Your team first, Molly backs up</span><span><i class="lg t"></i>Your team only</span></div>'

    phases = [
        ('Answer', 'First few seconds', [
            ('chat','Greets and discloses','“Thanks for calling ABC Heating &amp; Air. This is Molly, the AI assistant. This call may be recorded.”'),
            ('mic','Listens to the problem','No cooling, no heat, a noise, a leak, a quote. She asks a follow-up if it’s unclear.'),
            ('alert','Checks for an emergency','Hears one of your emergency words? She follows your rules and rings you. Gas or CO: “Please get outside and call 911.”'),
        ]),
        ('Qualify', 'About a minute', [
            ('user','Takes the details','Name, callback number, address, type of system, anyone at risk from heat or cold.'),
            ('pin','Checks your area','ZIP outside your service area? She says so politely instead of booking it.'),
            ('dollar','Mentions your fee','States your diagnostic or trip fee before booking. No surprises at the door.'),
        ]),
        ('Book', 'Before hanging up', [
            ('cal','Books the visit','Offers open slots from your calendar. The caller picks one.'),
            ('repeat','Reads it back','“Maria, 214 Oak Lane in Plano, AC blowing warm air, Wednesday 8 AM. Did I get that right?”'),
            ('msg','Texts you','Seconds later you get the summary. Recording and transcript are saved.'),
        ]),
    ]
    n=0; ph_html=''
    for pi,(name,when,items) in enumerate(phases):
        rows=''
        for k,t,d in items:
            n+=1
            rows+=f'<li><div class="sic">{ic(P[k],20)}</div><div><div class="stt"><span class="snum">{n}</span><b>{t}</b></div><p>{d}</p></div></li>'
        ph_html+=f'<div class="phase p{pi+1}"><div class="phh"><span class="phn">{pi+1}</span><div><b>{name}</b><span>{when}</span></div></div><ol>{rows}</ol></div>'

    # transcript mock next to phases
    convo = [
        ('m','Thanks for calling ABC Heating &amp; Air. This is Molly, the AI assistant. This call may be recorded. How can I help?'),
        ('c','Hi, my AC is running but it’s blowing warm air.'),
        ('m','Sorry about that. Can I get your name and the service address?'),
        ('c','Maria, 214 Oak Lane in Plano.'),
        ('m','Thanks, Maria. Our diagnostic visit has a flat fee, paid to the tech on site. I have Wednesday at 8 AM open. Does that work?'),
        ('c','Yes, perfect.'),
        ('m','You’re booked for Wednesday at 8 AM. You’ll get a text confirmation shortly.'),
    ]
    convo_html=''.join(f'<div class="cb {w}">{t}</div>' for w,t in convo)
    call_mock=f'''<div class="callmock" aria-label="Example call transcript"><div class="cmh"><div class="cma">{MOLLY}</div><div><b>Molly · Live call</b><span>Incoming · 9:47 PM</span></div><em class="live"><i></i>01:24</em></div>
<div class="cmb">{convo_html}</div><div class="cmf">{ic(P['check'],18,'#0B5E44',3)} Job booked · Wed 8:00 AM · owner texted</div><div class="cmn">Sample call for illustration</div></div>'''

    setup = [
        ('form','Day 1','Short form','Name, company and email.'),
        ('q','Within 1 business day','Setup questions','Hours, service-area ZIPs, fees, emergency words, on-call number, calendar.'),
        ('tool','Next','We build and test','You hear a test call. Nothing goes live until you approve it.'),
        ('fwd','Go live','Forward your calls','Missed or after-hours calls forward to Molly. Same number.'),
        ('flag','Day 14','You decide','No job booked? You pay nothing.'),
    ]
    setup_html=''.join(f'<li><div class="tdot">{ic(P[k],20)}</div><div class="sk">{a}</div><b>{t}</b><p>{d}</p></li>' for k,a,t,d in setup)

    always = ['Says she’s an AI assistant','Mentions the call may be recorded','Follows your emergency rules','Passes upset or tricky callers to you','Texts you every call']
    never = ['Takes card numbers over the phone','Diagnoses a system or promises a repair','Quotes prices you didn’t approve','Makes sales calls or sends marketing texts','Pretends to be a person']
    rules = ('<div class="rules"><div class="rok"><div class="rk">'+ic(P['check'],18,'#0B7A57',3)+' MOLLY ALWAYS</div>' + ''.join(f'<div class="ri"><span class="dot ok">{ic(P["check"],14,"#FFFFFF",3.2)}</span><span>{t}</span></div>' for t in always) +
             '</div><div class="rno"><div class="rk">'+ic(P['x'],18,'#C2410C',3)+' MOLLY NEVER</div>' + ''.join(f'<div class="ri"><span class="dot no">{ic(P["x"],14,"#FFFFFF",3.2)}</span><span>{t}</span></div>' for t in never) + '</div></div>')

    gets = [('msg','Text summary','Every call, seconds after it ends'),('cal','Calendar booking','Address, problem and time'),('mic','Recording + transcript','Check her work anytime'),('phone','Instant call','For your emergency words')]
    gets_html=''.join(f'<div class="get"><div class="gic">{ic(P[k],22)}</div><b>{t}</b><span>{d}</span></div>' for k,t,d in gets)

    faq = [
        ('Do I need new software?', 'No. Bookings go on the Google or Outlook calendar you already use, and details come to you by text and email.'),
        ('What if I use ServiceTitan, Jobber or Housecall Pro?', 'Every booking arrives with all the details, ready for your team to add in seconds. Ask us about a direct integration.'),
        ('What if Molly isn’t sure?', 'She takes a clear message and tells the caller you’ll call back. You get it by text right away.'),
        ('Can I change the script later?', 'Yes. Email us what to change and we update it, usually the same day.'),
        ('Can I hear every call?', 'Yes. Every call has a summary, a recording and a transcript.'),
    ]
    faq_html=''.join(f'<details class="fq"><summary>{q}<span aria-hidden="true">+</span></summary><p>{a}</p></details>' for q,a in faq)
    ld={"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faq]}

    inner = f'''<section class="bhero hiwhero"><div class="wrap">
<div class="eyebrow">HOW IT WORKS</div><h1>Exactly what Molly does on every call.</h1>
<p>From the first ring to the text on your phone. Here’s the whole thing, step by step.</p>
{flow()}
</div></section>
<div class="wrap pg">
<section class="blk"><div class="bh"><div class="eyebrow dk">THREE WAYS TO USE MOLLY</div><h2>Pick how much of your day she covers.</h2><p>Each bar is one 24-hour day.</p></div>
{legend}<div class="modes">{mode_html}</div></section>

<section class="blk"><div class="bh"><div class="eyebrow dk">ONE CALL, STEP BY STEP</div><h2>What happens when a homeowner calls at 9:47 PM.</h2></div>
<div class="callgrid"><div class="phases">{ph_html}</div>{call_mock}</div></section>

<section class="blk"><div class="bh"><div class="eyebrow dk">TRY IT</div><h2>Pick a call. See what Molly does.</h2><p>Every shop gets different calls. Tap one to see how Molly handles it.</p></div>
{scenarios()}</section>

<section class="blk"><div class="bh"><div class="eyebrow dk">SETUP</div><h2>We do the setup. You answer a few questions.</h2></div>
<ol class="tline">{setup_html}</ol><a class="gslink" href="/getting-started/">See the full getting-started plan →</a></section>

<section class="blk"><div class="bh"><div class="eyebrow dk">MOLLY’S RULEBOOK</div><h2>Clear rules, set with you.</h2><p>Read more in our <a href="/blog/hvac-emergency-call-triage/">emergency call triage guide</a>.</p></div>{rules}</section>

<section class="blk"><div class="bh"><div class="eyebrow dk">QUESTIONS</div><h2>Setup questions owners ask</h2></div><div class="fqs">{faq_html}</div></section>
{B.CTA}
</div>'''
    return inner, f'<link rel="stylesheet" href="/how-it-works/hiw.css?v=3">\n<script type="application/ld+json">{json.dumps(ld)}</script>'

CSS = '''/* How it works: visual layer */
.hiwhero{padding-block:64px 72px}
.hiwhero .wrap{gap:18px}
.flow{display:flex;align-items:stretch;gap:0;margin-top:28px;flex-wrap:wrap}
.fnode{flex:1 1 180px;min-width:0;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.12);border-radius:20px;padding:22px 20px;display:flex;flex-direction:column;gap:6px;animation:fin .6s ease both}
.fnode b{font-size:18px;color:#FFF}.fnode span{font-size:14px;color:#B9B7DC;line-height:1.45}
.fic{width:48px;height:48px;border-radius:14px;display:flex;align-items:center;justify-content:center;margin-bottom:8px;color:#FFF;background:rgba(255,255,255,.1)}
.c2{background:linear-gradient(160deg,#3F37C9,#2A23A6);border-color:#5B54E0;box-shadow:0 20px 50px rgba(63,55,201,.45)}.c2 .fic{background:rgba(255,255,255,.16)}.c2 span{color:#E1DFFA}
.c3 .fic{background:rgba(43,217,160,.18);color:#2BD9A0}.c4 .fic{background:#2BD9A0;color:#0B0A24}
.c2{animation-delay:.25s}.c3{animation-delay:.5s}.c4{animation-delay:.75s}
.farr{flex:0 0 40px;display:flex;align-items:center;justify-content:center}
.farr span{display:block;width:100%;height:2px;background:repeating-linear-gradient(90deg,#2BD9A0 0 6px,transparent 6px 11px);position:relative;background-size:22px 2px;animation:dash 1s linear infinite}
.farr span::after{content:"";position:absolute;right:-2px;top:-4px;border-left:8px solid #2BD9A0;border-top:5px solid transparent;border-bottom:5px solid transparent}
@keyframes dash{to{background-position:22px 0}}
@keyframes fin{from{opacity:0;transform:translateY(10px)}to{opacity:1;transform:none}}
@media (max-width:900px){.flow{flex-direction:column}.farr{flex-basis:28px}.farr span{width:2px;height:100%;min-height:24px;background:repeating-linear-gradient(180deg,#2BD9A0 0 6px,transparent 6px 11px)}.farr span::after{right:-4px;top:auto;bottom:-2px;border-top:8px solid #2BD9A0;border-left:5px solid transparent;border-right:5px solid transparent;border-bottom:0}}

.legend{display:flex;flex-wrap:wrap;gap:10px 22px;font-size:14px;font-weight:600;color:var(--ink)}
.legend span{display:inline-flex;align-items:center;gap:8px}
.lg{width:16px;height:16px;border-radius:4px;display:inline-block}
.lg.m,.seg.m{background:#3F37C9}.lg.h,.seg.h{background:repeating-linear-gradient(135deg,#C9F7E8 0 7px,#9EEBCF 7px 10px)}.lg.t,.seg.t{background:#E6E5F2}
.mode{position:relative}
.mode .badge{position:absolute;top:-12px;left:24px;background:#2BD9A0;color:#0B0A24;font-size:11px;font-weight:700;letter-spacing:.1em;padding:5px 10px;border-radius:999px}
.dbar{display:flex;height:44px;border-radius:12px;overflow:hidden;margin-top:6px}
.seg{display:flex;align-items:center;justify-content:center;min-width:0;padding:0 4px}
.seg em{font-style:normal;font-size:11px;font-weight:700;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.seg.m em{color:#FFF}.seg.h em{color:#0B5E44}.seg.t em{color:#6B6990}
.pop .seg.t{background:#2A2766}
.dlab{display:flex;justify-content:space-between;font-size:11px;font-weight:600;color:var(--soft);margin-top:-2px}.pop .dlab{color:#8E8CB8}
.addons{display:flex;flex-wrap:wrap;gap:8px}
.addons span{display:inline-flex;align-items:center;gap:6px;font-size:13px;font-weight:600;color:var(--indigo);background:#EEEDFB;padding:6px 10px;border-radius:999px}

.callgrid{display:flex;flex-wrap:wrap;gap:32px;align-items:flex-start}
.phases{flex:1.4 1 520px;min-width:0;display:flex;flex-direction:column;gap:16px}
.phase{border:1px solid var(--line);border-radius:22px;overflow:hidden}
.phh{display:flex;align-items:center;gap:14px;padding:16px 20px;background:var(--wash);border-bottom:1px solid var(--line)}
.phh b{display:block;font-size:18px}.phh span{font-size:13px;color:var(--soft);font-weight:600}
.phn{width:36px;height:36px;border-radius:12px;display:inline-flex;align-items:center;justify-content:center;font-weight:700;color:#FFF;flex-shrink:0}
.p1 .phn{background:#3F37C9}.p2 .phn{background:#6C63FF}.p3 .phn{background:#0B9E6E}
.phase ol{list-style:none;margin:0;padding:6px 20px 10px}
.phase li{display:flex;gap:14px;padding:14px 0;border-bottom:1px solid #F1F0F8}.phase li:last-child{border-bottom:0}
.sic{width:40px;height:40px;border-radius:12px;flex-shrink:0;display:flex;align-items:center;justify-content:center;background:#EEEDFB;color:#3F37C9}
.p3 .sic{background:#E6FBF4;color:#0B7A57}
.stt{display:flex;align-items:center;gap:8px}.stt b{font-size:16px}
.snum{font-size:11px;font-weight:700;color:var(--soft);border:1px solid var(--line);border-radius:6px;padding:1px 6px;font-variant-numeric:tabular-nums}
.phase li p{margin:4px 0 0;font-size:15px;line-height:1.55;color:var(--muted)}
.callmock{flex:1 1 360px;min-width:0;position:sticky;top:96px;background:var(--night);border-radius:26px;padding:8px;box-shadow:0 40px 90px rgba(15,13,46,.3)}
.cmh{display:flex;align-items:center;gap:12px;padding:14px 16px;color:#FFF}
.cmh b{display:block;font-size:15px}.cmh span{font-size:12px;color:#A9A7D4}
.cma{width:40px;height:40px;border-radius:50%;background:linear-gradient(135deg,#3F37C9,#6C63FF);display:flex;align-items:center;justify-content:center;flex-shrink:0}
.live{margin-left:auto;font-style:normal;font-size:13px;font-weight:600;color:#8FF0CF;display:inline-flex;align-items:center;gap:6px;background:rgba(43,217,160,.12);padding:5px 10px;border-radius:999px}
.live i{width:7px;height:7px;border-radius:50%;background:#2BD9A0;animation:pulse 1.8s infinite}
@keyframes pulse{0%{box-shadow:0 0 0 0 rgba(43,217,160,.6)}70%{box-shadow:0 0 0 8px rgba(43,217,160,0)}100%{box-shadow:0 0 0 0 rgba(43,217,160,0)}}
.cmb{display:flex;flex-direction:column;gap:9px;padding:6px 12px 14px}
.cb{max-width:86%;padding:10px 13px;font-size:14px;line-height:1.5;border-radius:16px;animation:fin .5s ease both}
.cb.m{align-self:flex-end;background:#3F37C9;color:#FFF;border-bottom-right-radius:4px}
.cb.c{align-self:flex-start;background:rgba(255,255,255,.09);color:#FFF;border-bottom-left-radius:4px}
.cb:nth-child(2){animation-delay:.3s}.cb:nth-child(3){animation-delay:.6s}.cb:nth-child(4){animation-delay:.9s}.cb:nth-child(5){animation-delay:1.2s}.cb:nth-child(6){animation-delay:1.5s}.cb:nth-child(7){animation-delay:1.8s}
.cmf{display:flex;align-items:center;gap:8px;margin:0 8px;background:#2BD9A0;color:#0B0A24;font-weight:700;font-size:14px;padding:12px 14px;border-radius:14px}
.cmn{font-size:11px;color:#8E8CB8;padding:10px 14px 6px}
@media (max-width:900px){.callmock{position:static}}

.getgrid{display:flex;flex-wrap:wrap;gap:40px;align-items:center}
.gets{flex:1 1 440px;min-width:0;display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px}
@media (max-width:520px){.gets{grid-template-columns:1fr}}
.get{border:1px solid var(--line);border-radius:20px;padding:20px;display:flex;flex-direction:column;gap:6px}
.get b{font-size:17px}.get span{font-size:14px;color:var(--muted);line-height:1.5}
.gic{width:46px;height:46px;border-radius:14px;background:#EEEDFB;color:#3F37C9;display:flex;align-items:center;justify-content:center;margin-bottom:6px}
.get:nth-child(4) .gic{background:#FFF1E8;color:#C2410C}

.tline{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:16px;position:relative}
.tline::before{content:"";position:absolute;left:24px;right:24px;top:24px;height:2px;background:linear-gradient(90deg,#3F37C9,#2BD9A0)}
.tline li{position:relative;display:flex;flex-direction:column;gap:6px}
.tdot{width:48px;height:48px;border-radius:50%;background:#FFF;border:2px solid #3F37C9;color:#3F37C9;display:flex;align-items:center;justify-content:center;margin-bottom:8px;position:relative}
.tline li:last-child .tdot{background:#2BD9A0;border-color:#2BD9A0;color:#0B0A24}
.gslink{align-self:flex-start;font-weight:700;font-size:16px;text-decoration:none;background:#EEEDFB;color:#2A23A6;padding:12px 18px;border-radius:12px}.gslink:hover{background:#E1DFFA}
.tline b{font-size:17px}.tline p{margin:0;font-size:14px;line-height:1.55;color:var(--muted)}
@media (max-width:900px){.tline{grid-template-columns:1fr;gap:22px;padding-left:64px}.tline::before{left:23px;right:auto;top:10px;bottom:10px;width:2px;height:auto;background:linear-gradient(180deg,#3F37C9,#2BD9A0)}.tdot{position:absolute;left:-64px;top:-2px}}

.rules .rok{background:#F2FCF8;border-color:#C9F2E2}.rules .rno{background:#FFF7F2;border-color:#FBD9C5}
.rk{display:inline-flex;align-items:center;gap:8px}.rok .rk{color:#0B7A57}.rno .rk{color:#C2410C}
.dot{width:24px;height:24px;border-radius:50%;display:inline-flex;align-items:center;justify-content:center;flex-shrink:0}.dot.ok{background:#10B981}.dot.no{background:#EA580C}
.rules .ri{align-items:center;font-size:16px}
.scen{display:flex;flex-wrap:wrap;gap:28px;align-items:stretch;background:var(--wash);border-radius:28px;padding:clamp(18px,3vw,32px)}
.stabs{flex:1 1 260px;min-width:0;display:flex;flex-direction:column;gap:8px}
.stab{font:inherit;display:flex;align-items:center;gap:12px;text-align:left;background:#FFF;border:1px solid var(--line);border-radius:14px;padding:14px 16px;min-height:52px;font-size:16px;font-weight:600;color:var(--ink);cursor:pointer;transition:border-color .15s,box-shadow .15s,transform .15s}
.stab svg{color:var(--indigo);flex-shrink:0}.stab:hover{transform:translateX(3px)}
.stab.on{background:var(--night);color:#FFF;border-color:var(--night);box-shadow:0 12px 30px rgba(15,13,46,.2)}.stab.on svg{color:var(--mint)}
.spath{flex:2 1 420px;min-width:0;display:flex;flex-direction:column;align-items:stretch}
.snode{background:#FFF;border:1px solid var(--line);border-radius:18px;padding:18px 20px}
.slab{display:flex;align-items:center;gap:8px;font-size:12px;font-weight:700;letter-spacing:.12em;color:var(--soft);margin-bottom:8px}
.ssay{font-size:20px;font-weight:600;line-height:1.4;color:var(--ink)}
.snode.molly{background:linear-gradient(160deg,#3F37C9,#2A23A6);border-color:#3F37C9;color:#FFF}.molly .slab{color:#C9C5FF}
.molly ul{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,220px),1fr));gap:8px}
.molly li{display:flex;gap:8px;align-items:flex-start;background:rgba(255,255,255,.1);border-radius:10px;padding:10px 12px;font-size:15px;line-height:1.4}
.molly li svg{flex-shrink:0;margin-top:2px;stroke:#2BD9A0}
.sline{width:2px;height:22px;margin:0 auto;background:repeating-linear-gradient(180deg,#3F37C9 0 5px,transparent 5px 9px)}
.snode.res b{display:block;font-size:22px;letter-spacing:-.01em}.snode.res span{font-size:15px;color:var(--muted)}
.res.ok{background:#E6FBF4;border-color:#9EEBCF}.res.ok b{color:#0B5E44}
.res.urgent{background:#FFF1E8;border-color:#FBC9A8}.res.urgent b{color:#9A3412}
.res.neutral{background:#FFF}.res.neutral b{color:var(--ink)}
.spath.anim .snode{animation:fin .45s ease both}.spath.anim .molly{animation-delay:.12s}.spath.anim .res{animation-delay:.24s}
@media (prefers-reduced-motion:reduce){.fnode,.cb,.farr span,.live i{animation:none!important}}
'''
