#!/usr/bin/env python3
"""Final build step for bookedorion.com (run after home_v3.py, build_blog.py, build_pages.py).

1. Loads /premium.css last on every page, so the premium layer wins over page styles.
2. Turns shouting ALL-CAPS section labels into sentence case.
3. Drops the trailing arrow from text links ("Read article →" becomes "Read article").
"""
import os, re

OUT = os.path.join(os.path.dirname(__file__), '..', 'site')
PREMIUM_V = '1'
LINK = f'<link rel="stylesheet" href="/premium.css?v={PREMIUM_V}">'

LABELS = {
    'LEGAL': 'Legal', 'PRODUCT': 'Product', 'COMPANY': 'Company', 'FREE 14-DAY TRIAL': 'Free 14-day trial',
    'QUESTIONS': 'Questions', 'YOUR CONTACT': 'Your contact', 'WHY WE EXIST': 'Why we exist',
    'WHAT WE NEED FROM YOU': 'What we need from you', 'TWO WAYS TO USE MOLLY': 'Two ways to use Molly',
    'TRY IT': 'Try it', 'THE PLAN': 'The plan', 'THE BOOKEDORION BLOG': 'The BookedOrion blog',
    'TALK TO US': 'Talk to us', 'SETUP': 'Setup', 'OUR PROMISES': 'Our promises', 'OUR FOCUS': 'Our focus',
    'ONE CALL, STEP BY STEP': 'One call, step by step', 'MOLLY’S RULEBOOK': 'Molly’s rulebook',
    'HOW IT WORKS': 'How it works', 'GO-LIVE DAY': 'Go-live day', 'GETTING STARTED': 'Getting started',
    'ABOUT BOOKEDORION': 'About BookedOrion', 'A NOTE FROM THE FOUNDER': 'A note from the founder',
    'IN THIS ARTICLE': 'In this article', 'YOU': 'You', 'BOOKEDORION': 'BookedOrion', 'RESULT': 'Result',
    'CALLER SAYS': 'Caller says', 'RECOMMENDED': 'Recommended', 'MOLLY DOES': 'Molly does',
}
LABEL_RE = re.compile(r'(<(?:div|p|span)\s+class="(?:eyebrow[^"]*|ctak|kicker|fh|toch|glab|slab|badge)"[^>]*>)([^<]+)(<)')

def fix(html):
    if LINK not in html:
        html = html.replace('</head>', LINK + '\n</head>', 1)
    html = LABEL_RE.sub(lambda m: m.group(1) + LABELS.get(m.group(2).strip(), m.group(2)) + m.group(3), html)
    html = re.sub(r'([A-Za-z.’)])\s*→(\s*</a>)', r'\1\2', html)
    html = html.replace('</svg> BOOKEDORION</div>', '</svg> BookedOrion</div>').replace('<span>MOLLY DOES</span>', '<span>Molly does</span>')
    return html

def main():
    n = 0
    for root, _, files in os.walk(OUT):
        if '/_' in root or '/.git' in root:
            continue
        for f in files:
            if f.endswith('.html'):
                p = os.path.join(root, f)
                t = open(p).read()
                u = fix(t)
                if u != t:
                    open(p, 'w').write(u); n += 1
    print(f'finish: {n} pages updated')

if __name__ == '__main__':
    main()
