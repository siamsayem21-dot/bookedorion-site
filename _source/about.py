"""About page for bookedorion.com."""
import build_blog as B
from how_v2 import ic, P

def page():
    promises = [
        ('chat', 'Honest with your callers', 'Molly says she’s an AI assistant and that the call may be recorded. She never pretends to be a person.'),
        ('dollar', 'No surprises on your bill', 'No hidden fees, no contract. We text you before you reach your call allowance. Cancel anytime.'),
        ('user', 'A real person behind it', 'I set up every pilot myself and review Molly’s calls with you in week one. You email me, not a ticket queue.'),
        ('flag', 'You only pay if it works', 'If Molly doesn’t book a job in your 14-day pilot, you pay nothing.'),
    ]
    pr = ''.join(f'<div class="apr"><span class="apic">{ic(P[k],22)}</span><b>{t}</b><p>{d}</p></div>' for k, t, d in promises)
    focus = [('One trade', 'HVAC only. Molly knows no-cool, no-heat, tune-up and emergency calls.'),
             ('One region', 'Dallas–Fort Worth. We know the summer rush and the winter freezes.'),
             ('One job', 'Answer the calls your team misses and turn them into booked jobs.')]
    fc = ''.join(f'<div class="afc"><em>0{i+1}</em><b>{t}</b><span>{d}</span></div>' for i, (t, d) in enumerate(focus))
    return f'''<section class="bhero"><div class="wrap ahero">
<div class="atext"><div class="eyebrow">ABOUT BOOKEDORION</div>
<h1>We help HVAC shops stop losing jobs to voicemail.</h1>
<p>BookedOrion builds and runs Molly, an AI receptionist set up for each shop by hand. One trade, one region, one job, done well.</p></div>
<figure class="afig"><img src="/siam-2.jpg" alt="Siam Ahmed, founder of BookedOrion" width="320" height="320"><figcaption><b>Siam Ahmed</b><span>Founder, BookedOrion</span></figcaption></figure>
</div></section>
<div class="wrap pg">
<section class="blk"><div class="bh"><div class="eyebrow dk">WHY WE EXIST</div><h2>The phone rings when your team can’t answer.</h2>
<p>Techs are on roofs and in attics. The office is on another line. After 6 PM, calls go to voicemail, and the homeowner with a dead AC calls the next shop on Google.</p>
<p>Big companies solve this with call centers. Most local shops can’t. BookedOrion gives them a front desk that answers every call, books the job and tells the owner, without hiring anyone.</p></div></section>

<section class="blk"><div class="anote2"><div class="eyebrow dk">A NOTE FROM THE FOUNDER</div>
<p class="aq">“Every HVAC owner I talk to says the same thing: the phone rings when nobody can answer it. I started BookedOrion so a small shop can pick up every call like a big one, without hiring a call center.”</p>
<div class="asig"><img src="/siam-2.jpg" alt="" width="48" height="48"><div><b>Siam Ahmed</b><span>Founder, BookedOrion</span></div></div></div></section>

<section class="blk"><div class="bh"><div class="eyebrow dk">OUR FOCUS</div><h2>We do one thing, for one trade.</h2></div><div class="afocus">{fc}</div></section>

<section class="blk"><div class="amap"><div class="amtx"><div class="eyebrow">WHERE WE WORK</div><h2>Built for shops across Dallas–Fort Worth.</h2><p>We know DFW summers, winter freezes and the calls they bring. Molly is set up for the cities you actually serve.</p>
<div class="amchips"><span>Dallas</span><span>Fort Worth</span><span>Plano</span><span>Frisco</span><span>Arlington</span><span>Irving</span><span>McKinney</span><span>Denton</span><span>+ nearby</span></div></div>
<div class="amvis"><svg class="mp" viewBox="0 0 640 420" role="img" aria-label="Map of cities we serve across Dallas–Fort Worth"><defs><pattern id="mpg" width="32" height="32" patternUnits="userSpaceOnUse"><path d="M32 0H0V32" fill="none" stroke="rgba(255,255,255,.05)"/></pattern></defs><rect width="640" height="420" fill="url(#mpg)"/><ellipse cx="271" cy="277" rx="300" ry="190" fill="rgba(63,55,201,.18)"/><path d="M116 344 Q 271 304 426 331" fill="none" stroke="rgba(255,255,255,.18)" stroke-width="2" stroke-dasharray="4 6"/><g class="mp-c"><circle cx="426" cy="331" r="19" fill="rgba(43,217,160,.12)"/><circle cx="426" cy="331" r="9" fill="#2BD9A0" stroke="#0B0A24" stroke-width="2"/><text x="440" y="336" text-anchor="start" font-size="16" font-weight="700" fill="#FFFFFF">Dallas</text></g><g class="mp-c"><circle cx="116" cy="344" r="19" fill="rgba(43,217,160,.12)"/><circle cx="116" cy="344" r="9" fill="#2BD9A0" stroke="#0B0A24" stroke-width="2"/><text x="102" y="349" text-anchor="end" font-size="16" font-weight="700" fill="#FFFFFF">Fort Worth</text></g><g class="mp-c"><circle cx="483" cy="186" r="16" fill="rgba(43,217,160,.12)"/><circle cx="483" cy="186" r="6" fill="#8F88FF" stroke="#0B0A24" stroke-width="2"/><text x="497" y="191" text-anchor="start" font-size="14" font-weight="600" fill="#FFFFFF">Plano</text></g><g class="mp-c"><circle cx="410" cy="108" r="16" fill="rgba(43,217,160,.12)"/><circle cx="410" cy="108" r="6" fill="#8F88FF" stroke="#0B0A24" stroke-width="2"/><text x="424" y="113" text-anchor="start" font-size="14" font-weight="600" fill="#FFFFFF">Frisco</text></g><g class="mp-c"><circle cx="246" cy="355" r="16" fill="rgba(43,217,160,.12)"/><circle cx="246" cy="355" r="6" fill="#8F88FF" stroke="#0B0A24" stroke-width="2"/><text x="232" y="360" text-anchor="end" font-size="14" font-weight="600" fill="#FFFFFF">Arlington</text></g><g class="mp-c"><circle cx="338" cy="309" r="16" fill="rgba(43,217,160,.12)"/><circle cx="338" cy="309" r="6" fill="#8F88FF" stroke="#0B0A24" stroke-width="2"/><text x="352" y="314" text-anchor="start" font-size="14" font-weight="600" fill="#FFFFFF">Irving</text></g><g class="mp-c"><circle cx="532" cy="81" r="16" fill="rgba(43,217,160,.12)"/><circle cx="532" cy="81" r="6" fill="#8F88FF" stroke="#0B0A24" stroke-width="2"/><text x="546" y="86" text-anchor="start" font-size="14" font-weight="600" fill="#FFFFFF">McKinney</text></g><g class="mp-c"><circle cx="231" cy="70" r="16" fill="rgba(43,217,160,.12)"/><circle cx="231" cy="70" r="6" fill="#8F88FF" stroke="#0B0A24" stroke-width="2"/><text x="217" y="75" text-anchor="end" font-size="14" font-weight="600" fill="#FFFFFF">Denton</text></g><g class="mp-c"><circle cx="465" cy="229" r="16" fill="rgba(43,217,160,.12)"/><circle cx="465" cy="229" r="6" fill="#8F88FF" stroke="#0B0A24" stroke-width="2"/><text x="479" y="234" text-anchor="start" font-size="14" font-weight="600" fill="#FFFFFF">Richardson</text></g><g class="mp-c"><circle cx="518" cy="250" r="16" fill="rgba(43,217,160,.12)"/><circle cx="518" cy="250" r="6" fill="#8F88FF" stroke="#0B0A24" stroke-width="2"/><text x="532" y="255" text-anchor="start" font-size="14" font-weight="600" fill="#FFFFFF">Garland</text></g><g class="mp-c"><circle cx="372" cy="225" r="16" fill="rgba(43,217,160,.12)"/><circle cx="372" cy="225" r="6" fill="#8F88FF" stroke="#0B0A24" stroke-width="2"/><text x="386" y="230" text-anchor="start" font-size="14" font-weight="600" fill="#FFFFFF">Carrollton</text></g><g class="mp-c"><circle cx="499" cy="137" r="16" fill="rgba(43,217,160,.12)"/><circle cx="499" cy="137" r="6" fill="#8F88FF" stroke="#0B0A24" stroke-width="2"/><text x="513" y="142" text-anchor="start" font-size="14" font-weight="600" fill="#FFFFFF">Allen</text></g></svg></div></div></section>



<section class="blk"><div class="bh"><div class="eyebrow dk">OUR PROMISES</div><h2>What you can hold us to.</h2></div><div class="aprs">{pr}</div></section>

<section class="blk"><div class="anote"><div><div class="eyebrow dk">TALK TO US</div><h3>Questions before you start?</h3>
<p>Email <a href="mailto:siam@bookedorion.com">siam@bookedorion.com</a> or call Molly yourself at <a href="tel:+15705219710">(570) 521-9710</a> and hear her answer.</p></div></div></section>
{B.CTA}
</div>'''

CSS = '''
.afig img{width:260px!important;height:300px!important;border-radius:22px!important;border:0!important;box-shadow:0 24px 60px rgba(0,0,0,.35)!important;object-position:50% 28%}
.afc em{background:none!important;-webkit-text-fill-color:var(--ink);color:var(--ink)!important;font-family:var(--fh)}
.afc b{color:var(--ink)!important}
.anote2{background:var(--paper)!important;border-color:var(--line)!important}
.anote2::before{color:rgba(43,217,160,.25)!important}
.aq{font-family:var(--fh);font-weight:600}
.asig img{border-color:var(--line)!important}
.apic{background:var(--mintsoft)!important;color:var(--mintdk)!important}
.apr{background:var(--paper)!important;border:1px solid var(--line)}

.ahero{position:relative}
.afc{position:relative;overflow:hidden;padding:26px!important;transition:transform .25s,box-shadow .25s}
.afc:hover{transform:translateY(-3px);box-shadow:0 18px 40px rgba(15,13,46,.08)}
.afc em{font-style:normal;font-size:48px;font-weight:700;letter-spacing:-.04em;line-height:1;background:linear-gradient(135deg,#3F37C9,#2BD9A0);-webkit-background-clip:text;background-clip:text;color:transparent;margin-bottom:8px}
.anote2{position:relative;border-radius:28px;padding:44px;background:linear-gradient(135deg,#F4F3FF,#EFFCF6);border:1px solid #E4E2F7;display:flex;flex-direction:column;gap:18px}
.anote2::before{content:"“";position:absolute;right:36px;top:-10px;font-size:180px;line-height:1;color:rgba(63,55,201,.10);font-weight:700}
.aq{margin:0;font-size:clamp(21px,2.4vw,28px);line-height:1.45;letter-spacing:-.01em;color:#14123A;font-weight:600;max-width:860px}
.asig{display:flex;align-items:center;gap:12px}.asig img{width:48px;height:48px;border-radius:50%;object-fit:cover;border:2px solid #2BD9A0}.asig b{display:block}.asig span{font-size:14px;color:var(--muted)}
.amap{display:grid;grid-template-columns:1fr 1.2fr;gap:0;border-radius:28px;overflow:hidden;background:#0B0A24;color:#FFFFFF}
.amtx{padding:44px;display:flex;flex-direction:column;gap:14px;justify-content:center}.amtx h2{margin:0;font-size:clamp(26px,3vw,36px);line-height:1.12;letter-spacing:-.02em}.amtx p{margin:0;font-size:17px;line-height:1.6;color:#C9C7EE}
.amchips{display:flex;flex-wrap:wrap;gap:8px;margin-top:6px}.amchips span{font-size:13px;font-weight:600;border:1px solid rgba(255,255,255,.16);border-radius:999px;padding:6px 11px;color:#DCDAF5}
.amvis{background:radial-gradient(70% 70% at 60% 40%,rgba(63,55,201,.35),transparent 70%)}
.mp{width:100%;height:100%;display:block}
.mp-c circle:last-of-type{transition:r .2s}
@media (max-width:860px){.amap{grid-template-columns:1fr}.amtx{padding:30px}.anote2{padding:28px}}

.ahero{flex-direction:row!important;flex-wrap:wrap;align-items:center;gap:40px!important}
.atext{flex:1.4 1 460px;min-width:0;display:flex;flex-direction:column;gap:16px}
.afig{flex:0 1 300px;margin:0 auto;display:flex;flex-direction:column;align-items:center;gap:14px}
.afig img{width:240px;height:240px;max-width:100%;border-radius:50%;object-fit:cover;border:4px solid #2BD9A0;box-shadow:0 0 0 10px rgba(63,55,201,.35)}
.afig figcaption{text-align:center;color:#FFFFFF}.afig b{display:block;font-size:18px}.afig span{font-size:14px;color:#B9B7DC}
.bh p+p{margin-top:12px}
.afocus{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,240px),1fr));gap:14px}
.afc{border:1px solid var(--line);border-radius:20px;padding:22px;display:flex;flex-direction:column;gap:6px}
.afc b{font-size:20px;color:var(--indigo)}.afc span{font-size:15px;line-height:1.55;color:var(--muted)}
.aprs{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,260px),1fr));gap:14px}
.apr{background:var(--wash);border-radius:20px;padding:22px;display:flex;flex-direction:column;gap:8px}
.apr b{font-size:18px}.apr p{margin:0;font-size:15px;line-height:1.55;color:var(--muted)}
.apic{width:46px;height:46px;border-radius:14px;background:#EEEDFB;color:#3F37C9;display:flex;align-items:center;justify-content:center;margin-bottom:4px}
.anote{border:1px solid var(--line);border-radius:24px;padding:28px}.anote h3{margin:4px 0 8px;font-size:24px}.anote p{margin:0;font-size:16px;line-height:1.6;color:var(--muted)}
'''
