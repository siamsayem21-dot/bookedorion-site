"""Homepage v3: premium redesign on the shared BookedOrion design system."""
import os, json, html
import build_blog as B

ROOT = os.path.join(os.path.dirname(__file__), '..')
HEAD_META = open(os.path.join(ROOT, 'v3_head.html')).read()

PH = '<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.91.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92z"/>'
CHK = '<path d="M5 12l5 5L20 7"/>'
X = '<path d="M18 6L6 18M6 6l12 12"/>'
CAL = '<rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/>'
MSG = '<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>'
MIC = '<rect x="9" y="2" width="6" height="12" rx="3"/><path d="M5 10a7 7 0 0 0 14 0M12 17v5"/>'
ARR = '<path d="M5 12h14M13 6l6 6-6 6"/>'
WARN = '<path d="M12 9v4M12 17h.01"/><path d="M10.3 3.9L1.8 18a2 2 0 0 0 1.7 3h17a2 2 0 0 0 1.7-3L13.7 3.9a2 2 0 0 0-3.4 0z"/>'
LIST = '<path d="M9 6h11M9 12h11M9 18h11M4 6h.01M4 12h.01M4 18h.01"/>'

def ic(d, s=18, w=2.2, c='currentColor'):
    return f'<svg width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="{c}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{d}</svg>'

FAQ = [
 ('How is Molly different from other AI receptionists?', 'Most AI receptionist apps are built for any business and you set them up yourself. Molly is built only for HVAC, a real person sets her up for your shop, and your team can still answer first.'),
 ('Can my team still answer first?', 'Yes. Your phone rings as usual. If nobody picks up in about 10–15 seconds, or the line is busy, the call goes to Molly. After hours, she can answer every call. You choose, and you can switch anytime.'),
 ('Will callers know it’s an AI?', 'Yes. Molly says she’s an AI assistant and that the call may be recorded.'),
 ('Do I change my phone number?', 'No. You keep your number and your Google listing. Unanswered calls forward to Molly.'),
 ('What if a caller has a real emergency?', 'You pick the emergency words. When Molly hears one, she tells the caller how to stay safe and rings your phone first.'),
 ('What does it cost to try?', 'Nothing. The first 14 days are free, with no setup fee and no contract. On Pay-per-Job, if Molly books no jobs in your first paid month, that month is free too.'),
 ('What counts as a booked job?', 'A new appointment from a call Molly handled, which you confirm with one tap in the text summary. Spam and wrong-number calls never count. If the customer cancels and there’s a record of it, you aren’t charged.'),
 ('Does it work with ServiceTitan, Jobber or Housecall Pro?', 'Every booking is sent to you by text and email with all the details, ready to add. There’s no direct integration yet.'),
 ('What if Molly gets something wrong?', 'Tell us and we fix her script by the next business day. If she isn’t sure, she takes a message and you call back.'),
]

def faq_ld():
    return json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]})

def coverage(mode):
    segs = ''
    for h in range(24):
        day = 7 <= h < 18
        c = ('tm' if day else 'mo') if mode == 'porch' else ('bk' if day else 'mo')
        segs += f'<i class="cv-{c}"></i>'
    lg = ('<span><i class="cv-mo"></i>Molly</span><span><i class="cv-tm"></i>Your office</span>' if mode == 'porch'
          else '<span><i class="cv-mo"></i>Molly</span><span><i class="cv-bk"></i>Team first, Molly backup</span>')
    return f'<div class="cv" aria-hidden="true"><div class="cv-bar">{segs}</div><div class="cv-ax"><span>12a</span><span>6a</span><span>12p</span><span>6p</span><span>12a</span></div><div class="cv-lg">{lg}</div></div>'

PLANS = [
 ('0', 'Pay-per-Job', 'Low base, then pay per booked job', '79', '/month + $29 per booked job', 'Never more than $449 a month', 'full', ['Your team rings first, Molly answers what you miss', 'Nights, weekends and holidays answered', 'Jobs booked on your calendar', 'Emergencies ring you first', 'Text summary after every call, one-tap confirm', '400 call minutes a month included', 'No jobs booked in your first month? That month is free']),
 ('1', 'Flat', 'One price, unlimited bookings', '249', '/month', 'Unlimited booked jobs', 'full', ['Everything in Pay-per-Job', '400 call minutes a month included', 'No per-job charge, however many she books', 'Usually the better deal at 6+ booked jobs a month', 'Same setup, same rules, same support']),
]

CMP = [('Monthly price','$79 + $29 per booked job','$249'),('Most you can pay in a month','$449','$249'),('Booked jobs','Charged per job','Unlimited'),('Call minutes included','400','400'),('Answers when your team misses a call by day','y','y'),('Answers nights, weekends, holidays','y','y'),('Books jobs on your calendar','y','y'),('Emergencies ring your cell first','y','y'),('Text summary after each call, one-tap confirm','y','y'),('Recordings and transcripts','y','y'),('Upset callers passed to you','y','y'),('Call-back list of callers who didn’t book','y','y'),('Short report every Monday','y','y'),('Spam and wrong-number calls billed','Never','Never'),('Setup done for you','y','y'),('Setup fee','$0','$0'),('Contract','None','None')]

def plans_html():
    cols = ''
    for k, name, sub, price, per, day, mode, feats in PLANS:
        rec = k == '0'
        flw = ''.join(f'<li>{ic(CHK, 16, 3)}<span>{f}</span></li>' for f in feats)
        cols += f'''<div class="pl{' is-rec' if rec else ''}" data-plan="{k}">
          <div class="pl-tag">Recommended</div>
          <h3>{name}</h3><p class="pl-sub">{sub}</p>
          <div class="pl-price"><b>${price}</b><span>{per}</span></div>
          <p class="pl-day">{day}</p>
          {coverage(mode)}
          <ul>{flw}</ul>
          <a class="b {'b-mint' if rec else 'b-line'}" href="#start">Start free trial</a>
        </div>'''
    def cell(v):
        if v == 'y': return '<td><span class="ok" aria-label="Included">✓</span></td>'
        if v == 'n': return '<td><span class="no" aria-label="Not included">–</span></td>'
        return f'<td>{v}</td>'
    rows = ''.join(f'<tr><th scope="row">{r[0]}</th>{cell(r[1])}{cell(r[2])}</tr>' for r in CMP)
    return cols, rows

def page():
    cols, rows = plans_html()
    faqs = ''.join(f'<details><summary><span>{q}</span><i aria-hidden="true">+</i></summary><p>{a}</p></details>' for q, a in FAQ)
    header = B.HEADER.replace('class="nav on" href="/blog/"', 'class="nav" href="/blog/"').replace('href="/#pricing"', 'href="#pricing"')
    return HEAD_META + f'''<meta name="theme-color" content="#0B0A24">
<title>BookedOrion · AI receptionist for HVAC companies</title>
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
{B.FONTS}
<link rel="stylesheet" href="/blog/blog.css?v={B.CSSV}">
<link rel="stylesheet" href="/home.css?v={B.CSSV}">
<script type="application/ld+json">{faq_ld()}</script>
</head>
<body class="home">
<a class="skip" href="#main">Skip to content</a>
{header}
<main id="main">

<!-- HERO -->
<section class="hero" id="top">
  <div class="wrap hero-in">
    <div class="hero-copy">
      <p class="kicker">AI receptionist for HVAC shops</p>
      <h1>You fix the AC.<br><span>Molly answers the phone.</span></h1>
      <p class="hero-lede">When your team can’t pick up, Molly answers, books the visit on your calendar and texts you the details. Nights, weekends and busy days.</p>
      <div class="hero-cta">
        <a class="b b-mint b-lg" href="#start">Start free trial {ic(ARR, 18, 2.6)}</a>
        <a class="b b-ghost b-lg" href="tel:+15705219710">{ic(PH, 18)}Hear Molly</a>
      </div>
      <ul class="hero-facts"><li>{ic(CHK,15,3)}Free 14-day trial</li><li>{ic(CHK,15,3)}Keep your number</li><li>{ic(CHK,15,3)}No contract</li></ul>
      <p class="hero-call">Hear her live anytime: <a href="tel:+15705219710">(570) 521-9710</a></p>
    </div>

    <figure class="console" aria-label="Demo: how one missed call becomes a booked job">
      <div class="con-bar"><span class="con-dots" aria-hidden="true"><i></i><i></i><i></i></span><span class="con-title">Molly · call log</span><span class="con-demo">Demo · sample data</span></div>
      <ol class="con-steps">
        <li class="cs cs-call">
          <time>9:47 PM</time><span class="cs-dot">{ic(PH,14)}</span>
          <div class="cs-body"><b>Incoming call</b><p>Maria G. · Homeowner</p><span class="cchip cchip-warn">Office closed</span></div>
        </li>
        <li class="cs cs-call">
          <time>9:47 PM</time><span class="cs-dot">{ic(MIC,14)}</span>
          <div class="cs-body"><b>Molly answers</b>
            <p class="tx"><em>Molly</em>Thanks for calling ABC Heating &amp; Air. This is Molly, the AI assistant.</p>
            <p class="tx"><em>Caller</em>My AC is running but blowing warm air.</p></div>
        </li>
        <li class="cs cs-book">
          <time>9:48 PM</time><span class="cs-dot">{ic(CAL,14)}</span>
          <div class="cs-body"><b>Visit booked</b><div class="slot"><span>WED</span><div><b>8:00–10:00 AM</b><small>AC repair · 214 Oak Ln</small></div></div></div>
        </li>
        <li class="cs cs-note">
          <time>9:48 PM</time><span class="cs-dot">{ic(MSG,14)}</span>
          <div class="cs-body"><b>Owner notified</b><div class="sms">New job booked: Maria G., 214 Oak Ln. AC blowing warm air. Wed 8–10 AM.</div></div>
        </li>
      </ol>
      <figcaption>Sample call for illustration. Not live customer data.</figcaption>
    </figure>
  </div>
</section>

<!-- PROBLEM -->
<section class="sec sec-paper" id="problem">
  <div class="wrap">
    <div class="split">
      <div class="split-l">
        <p class="eyebrow-d">The problem</p>
        <h2>A missed call is a job your competitor books.</h2>
        <p class="lead">When the AC dies, most homeowners don’t leave a voicemail. They call the next shop on Google.</p>
      </div>
      <div class="vs" role="group" aria-label="The same call, two ways">
        <div class="vs-col vs-no"><p class="vs-h">Without Molly</p>
          <ol><li>Rings while your team is on a job</li><li>Goes to voicemail</li><li>Caller hangs up</li><li>Books with another shop</li></ol>
          <p class="vs-r">{ic(X,15,2.6)}Job lost</p></div>
        <div class="vs-col vs-yes"><p class="vs-h">With Molly</p>
          <ol><li>Answered in seconds, with your company name</li><li>Gets name, address and problem</li><li>Books a time on your calendar</li><li>You get a text</li></ol>
          <p class="vs-r">{ic(CHK,15,3)}Job booked</p></div>
      </div>
    </div>

    <div class="mc" aria-labelledby="mc-h">
      <div class="mc-in">
        <h3 id="mc-h">What are missed calls costing you?</h3>
        <label class="rng" for="calls"><span>Missed calls per week</span><output id="callsV">8</output></label>
        <input id="calls" type="range" min="1" max="40" step="1" value="8">
        <label class="rng" for="ticket"><span>Average job value</span><output>$<span id="ticketV">350</span></output></label>
        <input id="ticket" type="range" min="100" max="2000" step="25" value="350">
        <label class="rng" for="rate"><span>Callers who would have booked</span><output><span id="rateV">40</span>%</output></label>
        <input id="rate" type="range" min="10" max="80" step="5" value="40">
      </div>
      <div class="mc-out" aria-live="polite">
        <p class="est">Estimate</p>
        <p class="mc-big">$<span id="monthly">4,850</span><small>/month</small></p>
        <p class="yr">$<span id="yearly">58,200</span> a year</p>
        <p class="how">Missed calls × 4.33 weeks × booking rate × job value. Your numbers, not a promise.</p>
        <a class="b b-mint" href="#start">Win these calls back</a>
      </div>
    </div>
  </div>
</section>

<!-- HOW MOLLY HANDLES A CALL -->
<section class="sec" id="how">
  <div class="wrap">
    <div class="sec-head"><p class="eyebrow-d">How it works</p><h2>How Molly handles a call.</h2><p class="lead">Same phone number. Nothing new to install. Here’s one call from ring to booked job.</p></div>
    <ol class="flow">
      <li class="flw fl-call"><span class="fl-n">1</span><p class="fl-k">Call handling</p><h3>Answer</h3><p>Your phone rings first. No answer in about 10–15 seconds, busy, or after hours? Molly picks up with your company name.</p>
        <div class="frag"><span class="frag-ic">{ic(PH,14)}</span><span>“Thanks for calling ABC Heating &amp; Air…”</span></div></li>
      <li class="flw fl-call"><span class="fl-n">2</span><p class="fl-k">Call handling</p><h3>Qualify</h3><p>She asks what’s wrong, gets the name, address and ZIP, and checks you serve that area.</p>
        <div class="frag frag-list"><span>Name</span><span>Address</span><span>Problem</span><span>ZIP ✓</span></div></li>
      <li class="flw fl-book"><span class="fl-n">3</span><p class="fl-k">Scheduling</p><h3>Book</h3><p>She offers open times from your calendar, the caller picks one, and she reads it back.</p>
        <div class="frag"><span class="frag-ic">{ic(CAL,14)}</span><span>Wed · 8:00–10:00 AM</span></div></li>
      <li class="flw fl-note"><span class="fl-n">4</span><p class="fl-k">Owner notification</p><h3>Notify</h3><p>You get a text and email in seconds. The recording and transcript are saved.</p>
        <div class="frag"><span class="frag-ic">{ic(MSG,14)}</span><span>New job booked · Maria G.</span></div></li>
    </ol>
    <div class="emerg">{ic(WARN,20)}<p><b>Emergencies skip the line.</b> Gas smell, CO alarm, smoke or sparks: Molly tells the caller to get safe and calls your cell right away.</p></div>
    <p class="more-link"><a href="/how-it-works/">See every step in detail →</a></p>
  </div>
</section>

<!-- DEMO -->
<section class="sec sec-navy" id="demo">
  <div class="wrap demo">
    <div class="demo-l">
      <p class="eyebrow-l">Hear Molly</p>
      <h2>Test her yourself in 60 seconds.</h2>
      <p class="lead">Call the demo line and talk like a homeowner. No sign-up.</p>
      <ol class="steps3"><li><b>Call the demo line.</b> Any hour. She answers as a sample HVAC shop.</li><li><b>Say what’s wrong.</b> Try “My AC is blowing warm air.”</li><li><b>Listen to her book it.</b> She asks the right questions and offers a time.</li></ol>
      <a class="b b-mint b-lg" href="tel:+15705219710">{ic(PH,18)}Call (570) 521-9710</a>
      <p class="fine">It’s a demo line, so no real visit gets booked. She’ll tell you she’s an AI.</p>
    </div>
    <div class="demo-r">
      <div class="dm-top"><span class="dm-av">{ic(CHK,14,3)}</span><div><b>Molly</b><small>Sample conversations</small></div><span class="con-demo">Demo</span></div>
      <label class="dm-lbl" for="biz">Type your company name to hear Molly’s greeting</label>
      <input id="biz" type="text" placeholder="e.g. ABC Heating &amp; Air" autocomplete="organization">
      <p class="dm-greet"><b>Molly:</b> “Thanks for calling <span id="bizShown">ABC Heating &amp; Air</span>. This is Molly, the AI assistant. This call may be recorded. How can I help?”</p>
      <div class="dm-tabs" role="tablist" aria-label="Sample calls" id="tabs"></div>
      <div id="lines" class="dm-lines" aria-live="polite"></div>
      <p class="dm-out">{ic(CHK,16,3)}<span id="outcome"></span></p>
      <p class="fine">Sample conversations for illustration.</p>
    </div>
  </div>
</section>

<!-- CAPABILITIES & BOUNDARIES -->
<section class="sec sec-paper" id="capabilities">
  <div class="wrap">
    <div class="sec-head"><p class="eyebrow-d">What you get</p><h2>What Molly does, and what she never does.</h2></div>
    <div class="cap">
      <div class="cap-col"><h3>Molly will</h3><ul class="cap-yes">
        <li>{ic(CHK,16,3)}Answer missed, after-hours and busy-line calls</li>
        <li>{ic(CHK,16,3)}Say she’s an AI and that the call may be recorded</li>
        <li>{ic(CHK,16,3)}Book visits only into times you leave open</li>
        <li>{ic(CHK,16,3)}Quote only the fees you approve</li>
        <li>{ic(CHK,16,3)}Ring your cell for emergencies and upset callers</li>
        <li>{ic(CHK,16,3)}Send a summary, recording and transcript of every call</li>
        <li>{ic(CHK,16,3)}Send a call-back list of callers who didn’t book</li>
        <li>{ic(CHK,16,3)}Send you a short report every Monday</li></ul></div>
      <div class="cap-col"><h3>Molly won’t</h3><ul class="cap-no">
        <li>{ic(X,16,2.6)}Take card numbers over the phone</li>
        <li>{ic(X,16,2.6)}Diagnose a system or promise a repair</li>
        <li>{ic(X,16,2.6)}Pretend to be a person</li>
        <li>{ic(X,16,2.6)}Make sales calls or send marketing texts</li>
        <li>{ic(X,16,2.6)}Sell or share your customers’ details</li></ul></div>
    </div>
    <div class="works"><p>Works with what you already use</p><ul><li>Your current number</li><li>AT&amp;T · Verizon · T-Mobile</li><li>Google Calendar</li><li>Outlook Calendar</li><li>Text and email alerts</li></ul><a href="/privacy/">How we handle data →</a></div>
  </div>
</section>

<!-- PRICING -->
<section class="sec" id="pricing">
  <div class="wrap">
    <div class="sec-head center"><p class="eyebrow-d">Pricing</p><h2>Two simple plans.</h2><p class="lead">$79 a month plus $29 per booked job, or $249 a month flat. Both start with a free 14-day trial. We set it up. No setup fee, no contract.</p></div>
    <div class="finder" role="group" aria-label="Find your plan"><span>Jobs Molly could book you each month?</span>
      <button type="button" data-plan="0" aria-pressed="true" class="on">Up to 5</button>
      <button type="button" data-plan="1" aria-pressed="false">6 or more</button></div>
    <div class="plans two">{cols}</div>
    <p class="pl-note"><b>Only need nights and weekends?</b> Night-only: $49 a month + $29 per booked job. Spam and wrong-number calls are never counted. <a href="/terms/">What counts as a booked job →</a></p>
    <details class="cmp"><summary>Compare all features <i aria-hidden="true">+</i></summary>
      <div class="cmp-wrap"><table><thead><tr><th></th><th>Pay-per-Job<small>$79 + $29/job</small></th><th>Flat<small>$249/mo</small></th></tr></thead><tbody>{rows}</tbody></table></div></details>
  </div>
</section>

<!-- FOUNDER + TRIAL -->
<section class="sec sec-navy" id="start">
  <div class="wrap pilot">
    <div class="pilot-l">
      <p class="eyebrow-l">Free 14-day trial</p>
      <h2>Try Molly free for 14 days.</h2>
      <div class="founder">
        <img src="/siam-2.jpg" alt="Siam Ahmed, founder of BookedOrion" width="96" height="96">
        <div><p class="fd-q">“I set up every shop myself and check Molly’s calls with you in week one.”</p><p class="fd-n"><b>Siam Ahmed</b> · Founder, BookedOrion</p></div>
      </div>
      <ol class="pilot-steps"><li><b>Day 1</b><span>Send your details. We reply within one business day.</span></li><li><b>Days 2–3</b><span>We build Molly for your shop. You hear a test call.</span></li><li><b>Day 14</b><span>Keep her, or walk away. No setup fee, no contract.</span></li></ol>
      <a class="link-l" href="/getting-started/">See the full setup plan →</a>
    </div>
    <form id="pilotForm" class="form" aria-label="Start your free trial" novalidate>
      <h3>Start your free trial</h3>
      <label for="f-name">Your name</label><input id="f-name" type="text" autocomplete="name" required>
      <label for="f-company">Company</label><input id="f-company" type="text" autocomplete="organization" required>
      <label for="f-email">Email</label><input id="f-email" type="email" autocomplete="email" required>
      <label for="f-phone">Phone <span>(optional)</span></label><input id="f-phone" type="tel" autocomplete="tel" inputmode="tel">
      <input type="checkbox" name="botcheck" id="f-bot" tabindex="-1" autocomplete="off" aria-hidden="true" hidden>
      <p class="f-err" id="fieldErr" role="alert" hidden></p>
      <button type="submit" id="f-submit" class="b b-ink b-lg">Start my free trial</button>
      <div id="formOk" class="f-ok" role="status" hidden><b>You’re in. ✓</b> Siam will email you within one business day with your setup questions.</div>
      <div id="formErr" class="f-bad" role="alert" hidden></div>
      <div id="formDone" class="f-ok" hidden><b>One last step.</b> Send these details to <b>siam@bookedorion.com</b> and we’ll set up your trial. <button type="button" id="copyBtn">Copy details</button><pre id="formText"></pre></div>
      <p class="f-fine">We reply within one business day. No sales calls unless you ask. We never sell your details. Prefer email? <a href="mailto:siam@bookedorion.com">siam@bookedorion.com</a></p>
    </form>
  </div>
</section>

<!-- FAQ -->
<section class="sec sec-paper" id="faq">
  <div class="wrap faq">
    <div class="faq-l"><p class="eyebrow-d">FAQ</p><h2>Questions owners ask.</h2><p class="lead">Still unsure? Email <a href="mailto:siam@bookedorion.com">siam@bookedorion.com</a> or call Molly and hear her for yourself.</p><a class="more-link" href="/how-it-works/">More answers on How it works →</a></div>
    <div class="faq-r">{faqs}</div>
  </div>
</section>

<!-- FINAL CTA -->
<section class="sec">
  <div class="wrap"><div class="final"><h2>Tonight’s calls can be tomorrow’s booked jobs.</h2><p>We set it all up. Free for 14 days.</p>
    <div class="hero-cta"><a class="b b-mint b-lg" href="#start">Start free trial {ic(ARR,18,2.6)}</a><a class="b b-ghost b-lg" href="tel:+15705219710">{ic(PH,18)}Hear Molly</a></div></div></div>
</section>
</main>
{B.FOOTER}
<div class="mcta" aria-label="Quick actions"><a class="b b-ghost" href="tel:+15705219710">{ic(PH,16)}Hear Molly</a><a class="b b-mint" href="#start">Start free trial</a></div>
<script src="/home.js?v={B.CSSV}" defer></script>
</body>
</html>
'''

def main():
    open(os.path.join(ROOT, 'site', 'index.html'), 'w').write(page())
    print('home built')

if __name__ == '__main__':
    main()
