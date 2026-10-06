# Generates the static ParikshaLab pages with one shared head, header and footer.
# Edit page content here, then run: python tools/build_pages.py (overwrites the *.html pages and sitemap.xml).
import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = 'https://parikshalab.in/'
WA = 'https://wa.me/918088158012?text=Hello%20ParikshaLab%2C%20I%20would%20like%20a%20demo%20for%20my%20institution.'
WA_STU = {'NEET': 'https://wa.me/918088158012?text=Hi%20ParikshaLab%2C%20I%20am%20a%20NEET%20aspirant.%20Please%20add%20me%20to%20early%20access%20for%20the%20free%20NEET%20mock%20tests.',
          'JEE': 'https://wa.me/918088158012?text=Hi%20ParikshaLab%2C%20I%20am%20a%20JEE%20aspirant.%20Please%20add%20me%20to%20early%20access%20for%20the%20free%20JEE%20Main%20mock%20tests.'}

P = {
 'arrow': '<path d="M5 12h14M13 6l6 6-6 6"/>',
 'left': '<path d="M19 12H5M11 6l-6 6 6 6"/>',
 'monitor': '<rect x="3" y="4" width="18" height="12" rx="2"/><path d="M8 20h8M12 16v4"/>',
 'layers': '<path d="M12 3l9 5-9 5-9-5z"/><path d="M3 13l9 5 9-5"/>',
 'chart': '<path d="M4 20V10M10 20V4M16 20v-7M22 20H2"/>',
 'devices': '<rect x="2" y="5" width="13" height="10" rx="1.5"/><path d="M5 19h7"/><rect x="17" y="8" width="5" height="11" rx="1.2"/>',
 'clock': '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
 'shield': '<path d="M12 3l8 3v6c0 5-3.4 8.4-8 9.8C7.4 20.4 4 17 4 12V6z"/><path d="M9 12l2 2 4-4"/>',
 'cloud': '<path d="M7 18a4.5 4.5 0 0 1-.5-9 6 6 0 0 1 11.5 1.5A3.8 3.8 0 0 1 17.5 18z"/><path d="M9.5 13.5l2 2 3.5-3.5"/>',
 'refresh': '<path d="M20 11a8 8 0 1 0-2.3 5.7"/><path d="M20 4v7h-7"/>',
 'grid': '<rect x="3" y="3" width="7" height="7" rx="1.5"/><rect x="14" y="3" width="7" height="7" rx="1.5"/><rect x="3" y="14" width="7" height="7" rx="1.5"/><rect x="14" y="14" width="7" height="7" rx="1.5"/>',
 'zoom': '<circle cx="11" cy="11" r="7"/><path d="M20 20l-4-4M11 8v6M8 11h6"/>',
 'lock': '<rect x="4" y="11" width="16" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/>',
 'phone': '<rect x="6" y="2" width="12" height="20" rx="2.5"/><path d="M11 18h2"/>',
 'tablet': '<rect x="4" y="2" width="16" height="20" rx="2.5"/><path d="M11 18h2"/>',
 'laptop': '<rect x="4" y="4" width="16" height="11" rx="1.5"/><path d="M2 19h20"/>',
 'globe': '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a14 14 0 0 1 0 18M12 3a14 14 0 0 0 0 18"/>',
 'sigma': '<path d="M18 5H6l6 7-6 7h12"/>',
 'camera': '<rect x="3" y="6" width="18" height="14" rx="2"/><circle cx="12" cy="13" r="3.5"/><path d="M8 6l1.5-2h5L16 6"/>',
 'pen': '<path d="M4 20h4L19 9l-4-4L4 16z"/><path d="M13 7l4 4"/>',
 'tag': '<path d="M3 12V4h8l10 10-8 8z"/><circle cx="7.5" cy="8.5" r="1.3"/>',
 'spark': '<path d="M12 3v4M12 17v4M3 12h4M17 12h4M6 6l2.5 2.5M15.5 15.5L18 18M6 18l2.5-2.5M15.5 8.5L18 6"/>',
 'users': '<circle cx="9" cy="8" r="3.2"/><path d="M3 20c0-3.3 2.7-5.5 6-5.5s6 2.2 6 5.5"/><circle cx="17" cy="9" r="2.5"/><path d="M16 14.6c2.9.2 5 2.2 5 5.4"/>',
 'brush': '<path d="M14 4l6 6-8 8H6v-6z"/><path d="M4 20l2-2"/>',
 'target': '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1.5"/>',
 'file': '<path d="M7 3h7l5 5v13H7z"/><path d="M14 3v5h5M10 13h6M10 17h6"/>',
 'mail': '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M4 7l8 6 8-6"/>',
 'call': '<path d="M5 4h3l2 5-2 1a11 11 0 0 0 5 5l1-2 5 2v3a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2z"/>',
 'check': '<path d="M5 12.5l4.5 4.5L19 7"/>',
 'home': '<path d="M3 11l9-7 9 7"/><path d="M5 10v10h14V10"/>',
 'pdf': '<path d="M7 3h7l5 5v13H7z"/><path d="M14 3v5h5"/><path d="M12 11v6M9.5 14.5L12 17l2.5-2.5"/>',
}
def svg(n, extra=''):
    return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"{extra}>{P[n]}</svg>'
WA_SVG = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5.1-1.3A10 10 0 1 0 12 2zm5.8 14.2c-.2.7-1.4 1.3-2 1.4-.5.1-1.1.1-1.8-.1-.4-.1-1-.3-1.7-.6-3-1.3-4.9-4.3-5-4.5-.2-.2-1.2-1.6-1.2-3s.7-2.1 1-2.4c.2-.3.5-.4.7-.4h.5c.2 0 .4 0 .6.5l.8 2c.1.2.1.4 0 .5l-.3.5-.4.4c-.1.1-.3.3-.1.6.2.3.8 1.3 1.7 2.1 1.2 1 2.1 1.4 2.4 1.5.3.1.4.1.6-.1l.9-1c.2-.2.4-.2.6-.1l2 1c.2.1.4.2.4.3.1.2.1.7-.1 1.4z"/></svg>'

def shot(name, alt, eager=False, cls=''):
    load = 'eager" fetchpriority="high' if eager else 'lazy'
    c = f' class="{cls}"' if cls else ''
    return (f'<img{c} src="assets/shots/b-{name}-1600.webp" srcset="assets/shots/b-{name}-900.webp 900w, assets/shots/b-{name}-1600.webp 1600w" '
            f'sizes="(max-width: 1080px) 94vw, 720px" width="1600" height="1000" alt="{alt}" loading="{load}" decoding="async">')
def laptop(name, alt, url='cbt.yourinstitute.in', eager=False):
    return f'<div class="laptop"><div class="bar"><i></i><i></i><i></i><span>{url}</span></div><div class="scr">{shot(name, alt, eager)}</div></div>'
def phone(name, alt, eager=False):
    return f'<div class="phone"><img src="assets/shots/p-{name}.webp" width="560" height="1206" alt="{alt}" loading="{"eager" if eager else "lazy"}" decoding="async"></div>'
def arrow_link(href, text):
    return f'<a class="link-arrow" href="{href}">{text} {svg("arrow")}</a>'
def cta(title, text):
    return f'''
<section style="padding-top:40px">
  <div class="wrap">
    <div class="cta" data-reveal="zoom">
      <h2>{title}</h2>
      <p>{text}</p>
      <div class="hero-cta">
        <a class="btn btn-primary" href="contact.html">Book a campus demo {svg("arrow")}</a>
        <a class="btn btn-ghost" href="{WA}" target="_blank" rel="noopener">Chat on WhatsApp</a>
      </div>
    </div>
  </div>
</section>'''

def faq(items, title='Frequently asked questions'):
    qs = ''.join(f'<details class="faq-item"><summary>{q}</summary><p>{a}</p></details>' for q, a in items)
    return f'''
<section>
  <div class="wrap" style="max-width:860px">
    <div class="sec-head center" data-reveal><h2>{title}</h2></div>
    <div class="faq" data-reveal>{qs}</div>
  </div>
</section>'''
def faq_ld(items):
    import re
    strip = lambda t: re.sub(r'<[^>]+>', '', t).replace('&amp;', '&').replace('&minus;', '-').replace('&nbsp;', ' ')
    return {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": strip(q), "acceptedAnswer": {"@type": "Answer", "text": strip(a)}} for q, a in items]}

NAV = [('index.html', 'Home'), ('platform.html', 'Platform'), ('qbank.html', 'QBank Studio'), ('reports.html', 'Reports'), ('apps.html', 'Apps'), ('about.html', 'About')]

def page(fname, title, desc, body, ld=None, index=True):
    canon = SITE + ('' if fname == 'index.html' else fname.replace('.html', ''))
    links = ''.join(f'<a href="{h}"{" class=\"active\" aria-current=\"page\"" if h == fname else ""}>{t}</a>' for h, t in NAV)
    ldj = f'<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>\n' if ld else ''
    robots = 'index, follow, max-image-preview:large' if index else 'noindex'
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#f7f8fc">
<script>try{{if(localStorage.getItem("pl-theme")==="dark")document.documentElement.setAttribute("data-theme","dark")}}catch(e){{}}</script>
<meta name="robots" content="{robots}">
<link rel="canonical" href="{canon}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{SITE}assets/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:site_name" content="ParikshaLab">
<meta property="og:locale" content="en_IN">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{SITE}assets/og-image.png">
{ldj}<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'><defs><linearGradient id='g' x1='0' y1='0' x2='1' y2='1'><stop offset='0' stop-color='%235b83ff'/><stop offset='1' stop-color='%239b6bff'/></linearGradient></defs><rect width='32' height='32' rx='9' fill='url(%23g)'/><path d='M10 23V9h6.5a4.5 4.5 0 0 1 0 9H13' stroke='white' stroke-width='2.8' fill='none' stroke-linecap='round' stroke-linejoin='round'/></svg>">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Sora:wght@500;600;700&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="styles.css">
</head>
<body>
<div class="progress" aria-hidden="true"></div>
<header class="nav" id="nav">
  <div class="wrap nav-in">
    <a class="brand" href="index.html" aria-label="ParikshaLab home"><span>Pariksha<b>Lab</b></span></a>
    <nav class="links" id="links" aria-label="Main">{links}</nav>
    <div class="nav-act">
      <button class="theme-btn" id="theme" type="button" aria-label="Switch to dark theme"><svg class="sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg><svg class="moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 14.5A8 8 0 0 1 9.5 4a8 8 0 1 0 10.5 10.5z"/></svg></button>
      <div class="nav-cta"><a class="btn btn-primary btn-sm" href="contact.html">Book a demo</a></div>
      <button class="burger" id="burger" aria-label="Menu" aria-expanded="false" aria-controls="links"><span></span><span></span><span></span></button>
    </div>
  </div>
</header>
<main>
{body}
</main>
<footer>
  <div class="wrap">
    <div class="foot">
      <div>
        <a class="brand" href="index.html"><span>Pariksha<b>Lab</b></span></a>
        <p>CBT mock test platform, NEET and JEE Main question bank and result reports for schools and coaching institutes across India.</p>
      </div>
      <div><h4>Product</h4><ul><li><a href="platform.html">Exam platform</a></li><li><a href="qbank.html">QBank Studio</a></li><li><a href="reports.html">Result reports</a></li><li><a href="apps.html">Apps</a></li></ul></div>
      <div><h4>For students</h4><ul><li><a href="neet-mock-test.html">NEET mock tests</a></li><li><a href="jee-main-mock-test.html">JEE Main mock tests</a></li></ul></div>
      <div><h4>Company</h4><ul><li><a href="about.html">About</a></li><li><a href="contact.html">Contact</a></li><li><a href="contact.html">Book a demo</a></li></ul></div>
      <div><h4>Reach us</h4><ul><li><a href="{WA}" target="_blank" rel="noopener">WhatsApp +91 80881 58012</a></li><li><a href="tel:+918088158012">+91 80881 58012</a></li><li><a href="mailto:admin.parikshalab@gmail.com">admin.parikshalab@gmail.com</a></li></ul></div>
    </div>
    <div class="fine"><span>&copy; <span id="yr">2026</span> ParikshaLab. All rights reserved.</span><span>parikshalab.in</span></div>
  </div>
</footer>
<a class="fab" href="{WA}" target="_blank" rel="noopener" aria-label="Chat on WhatsApp">{WA_SVG}</a>
<script src="script.js"></script>
</body>
</html>
'''
    open(os.path.join(ROOT, fname), 'w', encoding='utf-8', newline='\n').write(html)

AURORA = '<div class="aurora" aria-hidden="true"><i></i><i></i><i></i></div><div class="gridbg" aria-hidden="true"></div>'
def phero(eyebrow, h1, lede, extra=''):
    return f'''
<section class="page-hero">
  {AURORA}
  <div class="wrap z">
    <div class="sec-head center" style="margin-bottom:0" data-stagger>
      <h1><span class="kicker">{eyebrow}</span>{h1}</h1>
      <p class="lede">{lede}</p>
      {extra}
    </div>
  </div>
</section>'''

GROWTH = '''
    <div class="stats s3" data-reveal>
      <div><b><span data-count="21783">21,783</span></b><span>NEET UG questions</span></div>
      <div><b><span data-count="11476">11,476</span></b><span>JEE Main questions</span></div>
      <div><b>Every week</b><span class="live">New questions added</span></div>
    </div>'''

# ---------------------------------------------------------------- HOME
HOME_FAQ = [
 ('What is a CBT mock test platform?', 'A computer based test (CBT) platform lets students sit mock tests on a screen instead of an OMR sheet, with the same layout, buttons, timer and question palette as the NTA exam. ParikshaLab gives your institute that exam screen, a NEET and JEE Main question bank to build tests from, and a result report after every attempt.'),
 ('Can we run tests under our own institute name?', 'Yes. Your logo and colours appear on the login page, the exam screen and every report, and the platform can run on your own web address such as cbt.yourschool.in.'),
 ('Do we need a computer lab?', 'No. Students can take tests on Android or iOS phones, tablets, or any modern browser on Windows, Mac, Chromebook or Linux. If you have a lab, the same tests run there too.'),
 ('Which exams does ParikshaLab cover?', 'NEET UG and JEE Main, on the official paper pattern. The bank has 21,783 NEET UG and 11,476 JEE Main questions with answer keys and explanations, and new questions are added every week.'),
 ('Can teachers add their own questions?', 'Yes. Teachers can add a question from a screenshot or type it in, tag it by subject, chapter and difficulty, and use it in any paper. Your questions stay private to your institute.'),
 ('How long does it take to get started?', 'Usually a few days. We run a free demo test with one of your batches, set up your branded site, and you can start building papers in QBank Studio right away.'),
]
home = f'''
<section class="hero">
  {AURORA}
  <div class="wrap hero-grid z">
    <div>
      <h1 data-reveal="lines"><span class="kicker">CBT mock test platform for NEET &amp; JEE coaching institutes</span><span class="hl"><span>The exam hall,</span></span><span class="hl"><span class="grad">on every screen.</span></span></h1>
      <p class="lede" data-reveal style="--d:.3s">Online test software for schools and coaching institutes: a 33,000+ NEET and JEE Main question bank that grows every week, a studio that builds a full mock test in minutes, and an NTA-style CBT engine that feels exactly like the real exam. On Android, iOS and any browser.</p>
      <div class="hero-cta" data-reveal style="--d:.42s">
        <a class="btn btn-primary" href="contact.html">Book a campus demo {svg("arrow")}</a>
        <a class="btn btn-ghost" href="platform.html">Take the tour</a>
      </div>
      <div class="hero-stats" data-reveal style="--d:.54s">
        <div><b><span data-count="users" data-suffix="+">1,000+</span></b><span class="live">Users on ParikshaLab</span></div>
        <div><b><span data-count="33000" data-suffix="+">33,000+</span></b><span>Questions, growing weekly</span></div>
        <div><b>3</b><span>Android, iOS, web</span></div>
      </div>
    </div>
    <div class="stage" data-tilt data-reveal="zoom" style="--d:.2s">
      <div class="glow-ring"></div>
      {laptop("04_jee_palette_in_use", "JEE Main CBT mock test in progress on a laptop, with a graph based question and the NTA-style colour coded question palette", eager=True)}
      {phone("03_jee_question", "The same JEE Main test on a phone", eager=True)}
      <div class="chip-float" style="left:-34px;bottom:8%"><span class="ic g">{svg("cloud")}</span><div>Sync: Saved<small>Every answer, every click</small></div></div>
    </div>
  </div>
</section>

<div class="marquee" aria-hidden="true"><div class="marquee-track">
  {"".join(f"<span>{t}</span>" for t in ["NEET UG","JEE Main","Physics","Chemistry","Mathematics","Botany","Zoology","Numerical answers","Diagrams and graphs","Typeset equations","Five-state palette","Live timer","Result PDF","Android","iOS","Any browser"]*2)}
</div></div>

<section>
  <div class="wrap">
    <div class="sec-head center" data-reveal>
      <h2>Everything between the syllabus and the <span class="grad">result sheet.</span></h2>
    </div>
    <div class="grid g4" data-stagger>
      <a class="card pillar" href="platform.html"><span class="num">01</span><span class="ic">{svg("monitor")}</span><h3>Exam engine</h3><p>The NTA-style screen your students will face, with a live timer, subject tabs and the question palette.</p><span class="link-arrow">See the tour {svg("arrow")}</span></a>
      <a class="card pillar" href="qbank.html"><span class="num">02</span><span class="ic v">{svg("layers")}</span><h3>QBank Studio</h3><p>33,000+ NEET and JEE questions, with more every week. Build a paper in minutes, or add your own from a screenshot.</p><span class="link-arrow">Open Studio {svg("arrow")}</span></a>
      <a class="card pillar" href="reports.html"><span class="num">03</span><span class="ic c">{svg("chart")}</span><h3>Result reports</h3><p>Score, subject split, where the marks came from and time on every question. One tap PDF.</p><span class="link-arrow">See a report {svg("arrow")}</span></a>
      <a class="card pillar" href="apps.html"><span class="num">04</span><span class="ic g">{svg("devices")}</span><h3>Every device</h3><p>Android, iOS, laptops, lab desktops and any modern browser. Nothing to set up in your lab.</p><span class="link-arrow">See the apps {svg("arrow")}</span></a>
    </div>
  </div>
</section>

<section class="band">
  <div class="wrap split wide">
    <div class="stage" data-tilt data-reveal="zoom">
      <div class="glow-ring"></div>
      {laptop("07_neet_physics", "NEET UG mock test physics question with a logic gate circuit diagram, on the CBT exam screen")}
    </div>
    <div data-reveal>
      <h2>This is what your students see.</h2>
      <p class="lede">A NEET UG full syllabus test, exactly as it runs today. Diagrams stay crisp, equations are typeset, and every answer is saved the moment it is chosen.</p>
      <ul class="ticks">
        <li><span><b>Same controls as the real exam.</b> Save &amp; Next, Mark for Review, Clear Response, Submit.</span></li>
        <li><span><b>Palette with live counts.</b> Answered, not answered, marked and not visited, always in view.</span></li>
        <li><span><b>Zoom when it helps.</b> Text scales up for long statement questions and small screens.</span></li>
      </ul>
      {arrow_link("platform.html", "Walk through a full test")}
    </div>
  </div>
</section>

<section>
  <div class="wrap split">
    <div data-reveal>
      <h2>Android. iOS. <span class="grad">Any browser.</span></h2>
      <p class="lede">Students practise on the phone in their pocket and sit the full mock in your computer lab. Same login, same test, same result.</p>
      <div class="platforms" data-stagger>
        <div class="plat">{svg("phone")}Android app</div>
        <div class="plat">{svg("phone")}iOS app</div>
        <div class="plat">{svg("laptop")}Windows &amp; Mac</div>
        <div class="plat">{svg("globe")}Any browser</div>
      </div>
      {arrow_link("apps.html", "See it on a phone")}
    </div>
    <div class="fan" data-reveal="zoom">
      {phone("06_neet_physics", "NEET physics question on a phone")}
      {phone("04_jee_palette_open", "Question palette open on a phone")}
      {phone("07_neet_zoology", "NEET zoology statement question on a phone")}
    </div>
  </div>
</section>

<section class="band">
  <div class="wrap">
    <div class="sec-head center" data-reveal>
      <h2>A question bank big enough for the <span class="grad">whole year.</span></h2>
      <p class="lede">Every question comes with its answer key and explanation, tagged by subject, chapter and difficulty. New questions are added every week.</p>
    </div>{GROWTH}
    <div class="center">{arrow_link("qbank.html", "Explore QBank Studio")}</div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-head center" data-reveal>
      <h2>Preparing on your own? <span class="grad">Free mocks are coming.</span></h2>
      <p class="lede">We are opening ParikshaLab to students directly: full syllabus NEET and JEE Main mock tests on the real CBT screen, with the first mocks free.</p>
    </div>
    <div class="grid g2" data-stagger>
      <a class="card pillar" href="neet-mock-test.html"><span class="ic g">{svg("target")}</span><h3>NEET mock tests</h3><p>180 questions, 720 marks, Physics, Chemistry, Botany and Zoology on the official pattern.</p><span class="link-arrow">Get early access {svg("arrow")}</span></a>
      <a class="card pillar" href="jee-main-mock-test.html"><span class="ic v">{svg("sigma")}</span><h3>JEE Main mock tests</h3><p>75 questions, 300 marks, MCQ and numerical answers in Physics, Chemistry and Mathematics.</p><span class="link-arrow">Get early access {svg("arrow")}</span></a>
    </div>
  </div>
</section>
{faq(HOME_FAQ, 'Questions institutes ask us')}
{cta("See a live test running in your own lab.", "We run a full mock with one of your batches, then walk your team through the reports it produces. No cost, no commitment.")}
'''
ld = {"@context": "https://schema.org", "@graph": [
  {"@type": "WebSite", "@id": SITE + "#website", "url": SITE, "name": "ParikshaLab", "inLanguage": "en-IN", "publisher": {"@id": SITE + "#org"}},
  {"@type": "Organization", "@id": SITE + "#org", "name": "ParikshaLab", "url": SITE, "email": "admin.parikshalab@gmail.com", "telephone": "+91-8088158012", "areaServed": "IN",
   "description": "Computer based test platform and question bank for NEET and JEE Main, built for schools and coaching institutes in India.",
   "contactPoint": {"@type": "ContactPoint", "telephone": "+91-8088158012", "email": "admin.parikshalab@gmail.com", "contactType": "sales", "areaServed": "IN", "availableLanguage": ["en", "hi"]}},
  {"@type": "SoftwareApplication", "name": "ParikshaLab", "applicationCategory": "EducationalApplication", "operatingSystem": "Android, iOS, Web browser", "url": SITE,
   "description": "NTA-style computer based test engine with a 33,000+ question NEET and JEE Main bank, QBank Studio for building papers, and detailed student result reports.",
   "offers": {"@type": "Offer", "priceCurrency": "INR", "availability": "https://schema.org/InStock"}},
  faq_ld(HOME_FAQ)]}
page('index.html', 'NEET & JEE CBT Mock Test Platform for Coaching Institutes | ParikshaLab',
     'Online CBT mock test software for schools and coaching institutes: NTA-style NEET and JEE Main tests on Android, iOS and web, a 33,000+ question bank, QBank Studio and instant result reports.', home, ld)

# ---------------------------------------------------------------- PLATFORM
TOUR = [
 ('01_login', 'cbt.yourinstitute.in/login', 'Sign in', 'One login, one device.', 'Students sign in with their mobile number and password. A login works on one device at a time, and signing in somewhere else signs the first one out.'),
 ('02_test_list', 'cbt.yourinstitute.in/tests', 'Choose a test', 'Every open test, in one list.', 'Full syllabus mocks, chapter tests and practice papers appear the moment you deploy them. A test left halfway shows Resume.'),
 ('03_jee_first_question', 'JEE Main Full Syllabus Mock', 'Answer', 'The screen from exam day.', 'Candidate name, live timer, subject tabs and the four NTA buttons: Save &amp; Next, Save &amp; Mark for Review, Clear Response, Mark for Review &amp; Next.'),
 ('04_jee_palette_in_use', 'JEE Main Full Syllabus Mock', 'Navigate', 'A palette that tells the truth.', 'Five states with live counts: not visited, not answered, answered, marked for review, and answered and marked. Graphs and figures load right inside the options.'),
 ('07_neet_physics', 'NEET UG Full Syllabus Test 1', 'Read', 'Diagrams stay sharp.', 'Circuit diagrams, graphs and structures appear at full clarity, and text can be zoomed for long questions.'),
 ('09_submit_confirm', 'NEET UG Full Syllabus Test 1', 'Submit', 'No accidental submissions.', 'A clear confirmation before the paper is final. If time runs out, the test submits itself with every saved answer.'),
 ('10_result', 'NEET UG Full Syllabus Test 1', 'Result', 'The score, the moment they submit.', 'The mark appears straight away, with Download result PDF and View my answers one tap away.'),
]
tour_imgs = ''.join(shot(n, h, eager=(i == 0), cls='on' if i == 0 else '') for i, (n, u, k, h, p) in enumerate(TOUR))
tour_steps = ''.join(f'''
      <div class="tstep{' on' if i == 0 else ''}" data-url="{u}">
        <span class="k">{i+1:02d} / {k.upper()}</span>
        <h3>{h}</h3>
        <p>{p}</p>
        {laptop(n, h, u)}
      </div>''' for i, (n, u, k, h, p) in enumerate(TOUR))
SUBJ = [('Physics', '03_jee_first_question', 'Dimensions, vectors and units, typeset the way the paper prints them.'),
        ('Chemistry', '05_jee_chemistry', 'Formulae, charges and ions such as XeF<sub>4</sub> and PF<sub>4</sub><sup>+</sup>, never mangled.'),
        ('Mathematics', '06_jee_mathematics', 'Series, powers and fractions rendered as real mathematics.'),
        ('Biology', '08_neet_botany', 'Clean, readable text for Botany and Zoology, with tabs for each.')]
subj_btns = ''.join(f'<button type="button" role="tab" aria-selected="{"true" if i == 0 else "false"}"{" class=\"on\"" if i == 0 else ""}>{s}</button>' for i, (s, n, t) in enumerate(SUBJ))
subj_panels = ''.join(f'''
      <div class="tab-panel{' on' if i == 0 else ''}" role="tabpanel">
        <div class="stage" style="max-width:960px;margin-inline:auto">{laptop(n, s + " question on the exam screen")}</div>
        <p class="center muted" style="margin-top:24px">{t}</p>
      </div>''' for i, (s, n, t) in enumerate(SUBJ))
platform = phero('NTA-style CBT exam platform', 'An exam engine that behaves <span class="grad">like the real one.</span>',
  'Scroll through a real test, from login to result. Every screen below is taken straight from the platform.') + f'''
<section style="padding-top:40px">
  <div class="wrap tour">
    <div class="tour-stage" data-tilt>
      <div class="glow-ring"></div>
      <div class="laptop"><div class="bar"><i></i><i></i><i></i><span>{TOUR[0][1]}</span></div><div class="scr">{tour_imgs}</div></div>
      <div class="tour-dots" aria-hidden="true">{"".join("<i class=\"on\"></i>" if i == 0 else "<i></i>" for i in range(len(TOUR)))}</div>
    </div>
    <div class="tour-steps">{tour_steps}
    </div>
  </div>
</section>

<section class="band">
  <div class="wrap" data-tabs>
    <div class="sec-head center" data-reveal>
      <h2>Equations, formulae and diagrams, <span class="grad">rendered right.</span></h2>
    </div>
    <div class="center" data-reveal><div class="tabs" role="tablist">{subj_btns}</div></div>
    <div class="tab-panels">{subj_panels}
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-head center" data-reveal>
      <h2>The details that keep a test <span class="grad">fair and calm.</span></h2>
    </div>
    <div class="grid g3" data-stagger>
      <div class="card"><span class="ic">{svg("clock")}</span><h3>Exact timer</h3><p>A live countdown on every screen, and automatic submission when time is up.</p></div>
      <div class="card"><span class="ic g">{svg("cloud")}</span><h3>Saved on every click</h3><p>Answers sync as they are chosen. The screen shows Sync: Saved so students never wonder.</p></div>
      <div class="card"><span class="ic c">{svg("refresh")}</span><h3>Safe resume</h3><p>If a phone dies or a lab machine restarts, the student picks up where they left off.</p></div>
      <div class="card"><span class="ic v">{svg("shield")}</span><h3>Stays on the test</h3><p>Leaving full screen, switching tabs or copying counts as a warning. After four, the test locks until a teacher unlocks it.</p></div>
      <div class="card"><span class="ic">{svg("lock")}</span><h3>One device per student</h3><p>Signing in on a second device signs the first one out. Saved answers are kept.</p></div>
      <div class="card"><span class="ic c">{svg("zoom")}</span><h3>Zoom and palette</h3><p>Text zooms for readability. On phones the palette opens as a sheet with the same five states.</p></div>
    </div>
  </div>
</section>

<section class="band">
  <div class="wrap">
    <div class="sec-head center" data-reveal>
      <h2>Both papers, on the official pattern.</h2>
    </div>
    <div class="spec" data-stagger>
      <div class="card"><span class="tag">NEET UG</span><dl><dt>Questions</dt><dd>180 MCQs</dd><dt>Subjects</dt><dd>Physics, Chemistry, Botany, Zoology</dd><dt>Duration</dt><dd>180 minutes</dd><dt>Marking</dt><dd>+4 / &minus;1</dd><dt>Total</dt><dd>720 marks</dd></dl></div>
      <div class="card"><span class="tag v">JEE Main</span><dl><dt>Questions</dt><dd>75 (60 MCQ + 15 numerical)</dd><dt>Subjects</dt><dd>Physics, Chemistry, Mathematics</dd><dt>Duration</dt><dd>180 minutes</dd><dt>Marking</dt><dd>+4 / &minus;1</dd><dt>Total</dt><dd>300 marks</dd></dl></div>
    </div>
  </div>
</section>
{cta("Put this screen in front of your students.", "We will set up a test for one of your batches and show you the results the same day.")}
'''
page('platform.html', 'NTA-Style CBT Exam Platform for NEET & JEE Main | ParikshaLab', 'A tour of the ParikshaLab computer based test engine for NEET and JEE Main mock tests: NTA-style screen, five-state palette, typeset equations, sharp diagrams, auto-save, safe resume and instant results.', platform)

# ---------------------------------------------------------------- QBANK
qbank = phero('NEET &amp; JEE question bank and test paper generator', 'A big question bank, and a studio to <span class="grad">build from it.</span>',
  'Every institution gets its own QBank Studio. Build a full syllabus mock or a one chapter test in minutes, from our bank, your own questions, or both.') + f'''
<section style="padding-top:30px">
  <div class="wrap">
{GROWTH}
  </div>
</section>

<section style="padding-top:40px">
  <div class="wrap split">
    <div data-reveal="zoom">
      <div class="panel">
        <div class="panel-head"><span class="ic">{svg("grid")}</span>QBank Studio<span class="who">NEET UG &middot; Generate</span></div>
        <div class="st-steps"><span class="done">1 Start</span><span class="done">2 Method</span><span class="on">3 Build</span><span>4 Review</span></div>
        <span class="lbl">Questions per subject</span>
        <div class="st-row"><span>Physics <b>45</b></span><span>Chemistry <b>45</b></span><span>Botany <b>45</b></span><span>Zoology <b>45</b></span></div>
        <span class="lbl">Difficulty mix</span>
        <div class="mix"><i style="--w:35%;background:var(--green)"></i><i style="--w:50%;background:var(--amber)"></i><i style="--w:15%;background:var(--red)"></i></div>
        <div class="mix-key"><span><i style="background:var(--green)"></i>Easy 35%</span><span><i style="background:var(--amber)"></i>Medium 50%</span><span><i style="background:var(--red)"></i>Hard 15%</span></div>
        <div class="qcard">
          <div class="qtags"><span>Current Electricity</span><span class="m">Medium</span><span>Physics</span></div>
          <p>Two identical cells of emf 1.5 V are joined in parallel across a 2.25 &Omega; resistor. If the current is 0.5 A, what is each cell's internal resistance?</p>
          <div class="qopts"><span>A&nbsp; 0.25 &Omega;</span><span class="ok">B&nbsp; 1.5 &Omega;</span><span>C&nbsp; 0.75 &Omega;</span><span>D&nbsp; 3.0 &Omega;</span></div>
          <div class="qwhy"><b>Why:</b> 1.5 V drives 0.5 A, so R + r/2 = 3 &Omega; and r = 1.5 &Omega;.</div>
        </div>
        <div class="st-foot"><span>Paper <b>180 / 180</b></span><span class="pill-btn">Generate paper</span></div>
      </div>
    </div>
    <div data-reveal>
      <h2>Two ways to build. Checked before it goes live.</h2>
      <ul class="ticks">
        <li><span><b>Generate, then refine.</b> Set questions per subject, slide the difficulty mix and fill chapter quotas from past paper weightage. One tap draws the paper; swap anything you don't like.</span></li>
        <li><span><b>Browse and pick.</b> Filter by subject, chapter, difficulty, question type and figures, and read each question with its key and explanation.</span></li>
        <li><span><b>Chapter tests too.</b> Set a quota for one chapter and the paper stays inside it.</span></li>
        <li><span><b>Check before deploy.</b> Chapter coverage, difficulty counts, total marks and answer balance, so the key is not mostly B.</span></li>
      </ul>
    </div>
  </div>
</section>

<section class="band">
  <div class="wrap">
    <div class="sec-head center" data-reveal>
      <h2>From a blank page to a <span class="grad">live test.</span></h2>
    </div>
    <div class="process" data-stagger>
      <div class="card"><span class="ic">{svg("target")}</span><h3>Start</h3><p>Pick NEET UG or JEE Main and name the paper.</p></div>
      <div class="card"><span class="ic v">{svg("spark")}</span><h3>Method</h3><p>Generate automatically, or browse and hand pick.</p></div>
      <div class="card"><span class="ic c">{svg("layers")}</span><h3>Build</h3><p>Tune subjects, difficulty and chapters. Swap any question.</p></div>
      <div class="card"><span class="ic g">{svg("check")}</span><h3>Review and deploy</h3><p>Run the paper check, then publish to students in one tap.</p></div>
    </div>
  </div>
</section>

<section>
  <div class="wrap split rev">
    <div data-reveal="zoom">
      <div class="panel">
        <div class="own-flow">
          <div class="shot"><span class="shot-tag">{svg("camera")} Screenshot</span>
            <div class="paper scan"><i style="width:82%"></i><i style="width:94%"></i><i style="width:60%"></i><div class="fig"></div><i style="width:40%"></i><i style="width:46%"></i></div></div>
          <div class="arrow-dot">{svg("arrow")}</div>
          <div class="qcard" style="margin-top:0">
            <div class="qtags"><span class="y">Your question</span><span>Organic Chemistry</span><span class="h">Hard</span></div>
            <div class="ln"></div><div class="ln" style="width:78%"></div>
            <div class="qopts" style="margin-top:12px"><span>A</span><span>B</span><span class="ok">C</span><span>D</span></div>
            <div style="text-align:right;margin-top:12px"><span class="save">Save to my bank</span></div>
          </div>
        </div>
        <div class="or">or type it in</div>
        <div class="typed" data-type="A particle moves along x = 4t&#178; &#8722; 3t. Its velocity at t = 2 s is"><span class="txt">A particle moves along x = 4t&sup2; &minus; 3t. Its velocity at t = 2 s is</span><span class="caret"></span></div>
      </div>
    </div>
    <div data-reveal>
      <h2>Questions from your teachers, in the same bank.</h2>
      <p class="lede">Every teacher has favourites from books, class notes and old papers. Add them in seconds and use them in any paper, right next to ours.</p>
      <ul class="ticks">
        <li><span><b>From a screenshot.</b> Snap the question from a book, PDF or old paper, figure and all.</span></li>
        <li><span><b>Or type it in.</b> Question, options, answer and explanation in one simple form.</span></li>
        <li><span><b>Tag it once.</b> Subject, chapter and difficulty, so it shows up in filters and quotas.</span></li>
        <li><span><b>Private to you.</b> Your questions are never shared with any other institution.</span></li>
      </ul>
    </div>
  </div>
</section>
{cta("Build your first paper with us, live.", "In a 30 minute call we build a NEET or JEE Main paper from the bank, add one of your own questions, and deploy it to a test batch.")}
'''
page('qbank.html', 'NEET & JEE Question Bank and Test Paper Generator | QBank Studio', 'QBank Studio: 21,783 NEET UG and 11,476 JEE Main questions with keys and explanations, and new questions added every week. Generate a paper in minutes, check it, deploy it, and add your own questions from a screenshot.', qbank)

# ---------------------------------------------------------------- REPORTS
tb = [30, 38, 22, 44, 32, 26, 36, 28, 92, 34, 20, 40, 30, 36, 26]
tbars = ''.join(f'<i style="--h:{h}%"{" class=\"slow\"" if h > 80 else ""}></i>' for h in tb)
reports = phero('Mock test result analysis', 'Every attempt answers one question: <span class="grad">what next?</span>',
  'The moment a student submits, they get a result report to review on screen or download as a PDF. It shows not just the score, but where it came from.') + f'''
<section style="padding-top:40px">
  <div class="wrap split">
    <div class="stage" data-tilt data-reveal="zoom">
      <div class="glow-ring"></div>
      {laptop("10_result", "Test submitted screen showing 441 out of 720 with Download result PDF and View my answers buttons", "NEET UG Full Syllabus Test 1")}
    </div>
    <div data-reveal>
      <h2>No waiting for results day.</h2>
      <p class="lede">Submit, and the score is on screen. The result sheet stays on the test list, so students can come back to it any time.</p>
      <ul class="ticks">
        <li><span><b>Download result PDF.</b> Ready to print, file or send home.</span></li>
        <li><span><b>View my answers.</b> Each question with the student's answer, the correct key and the marks earned.</span></li>
      </ul>
    </div>
  </div>
</section>

<section class="band">
  <div class="wrap split rev">
    <div data-reveal="zoom">
      <div class="panel">
        <div class="panel-head"><span class="ic c">{svg("chart")}</span>Result report<span class="who">NEET UG &middot; Test 1</span></div>
        <div class="kpis">
          <div class="kpi"><small>Score</small><b><span data-count="512">512</span></b><span>of 720</span></div>
          <div class="kpi"><small>Accuracy</small><b><span data-count="81" data-suffix="%">81%</span></b><span>136 of 168</span></div>
          <div class="kpi"><small>Negative</small><b style="color:var(--red)">&minus;32</b><span>32 wrong</span></div>
        </div>
        <span class="lbl">Where the marks came from</span>
        <div class="mix" style="height:12px"><i style="--w:75.6%;background:var(--green)"></i><i style="--w:17.8%;background:var(--red)"></i><i class="seg-left" style="--w:6.6%"></i></div>
        <div class="mix-key"><span><i style="background:var(--green)"></i>136 correct &middot; +544</span><span><i style="background:var(--red)"></i>32 wrong &middot; &minus;32</span><span><i class="seg-left"></i>12 left</span></div>
        <span class="lbl">Subject split, marks of 180</span>
        <div class="bars">
          <div class="bar"><span>Physics</span><span class="track"><i style="--w:62%"></i></span><span class="v">112</span></div>
          <div class="bar"><span>Chemistry</span><span class="track"><i style="--w:71%"></i></span><span class="v">128</span></div>
          <div class="bar"><span>Botany</span><span class="track"><i style="--w:80%"></i></span><span class="v">144</span></div>
          <div class="bar"><span>Zoology</span><span class="track"><i style="--w:71%"></i></span><span class="v">128</span></div>
        </div>
        <span class="lbl">Time per question, Physics &middot; Q9 took 4m 10s</span>
        <div class="tbars" role="img" aria-label="Time spent on each physics question; question 9 took far longer than the rest">{tbars}</div>
        <div class="rep-btns"><span>Review answers</span><span class="p">Download result PDF</span></div>
      </div>
    </div>
    <div data-reveal>
      <h2>A score, and the story behind it.</h2>
      <ul class="ticks">
        <li><span><b>Where the marks came from.</b> Correct, wrong and left, and the marks lost to negative marking.</span></li>
        <li><span><b>Subject split.</b> Marks in each subject, so the weakest one is obvious.</span></li>
        <li><span><b>Time on every question.</b> The four minutes lost on question nine become visible.</span></li>
        <li><span><b>Answer review.</b> Every question with the student's answer and the correct key.</span></li>
      </ul>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-head center" data-reveal>
      <h2>The whole batch, <span class="grad">at a glance.</span></h2>
    </div>
    <div class="grid g3" data-stagger>
      <div class="card"><span class="ic">{svg("file")}</span><h3>All tests</h3><p>Every test with its attempts, average and top score in the admin panel.</p></div>
      <div class="card"><span class="ic c">{svg("users")}</span><h3>Every student</h3><p>Open a test to see each student's score, time taken and status: submitted or in progress.</p></div>
      <div class="card"><span class="ic v">{svg("lock")}</span><h3>Unlock in one tap</h3><p>If a student's test locks mid-exam, unlock it from the same screen and they carry on.</p></div>
    </div>
  </div>
</section>
{cta("See a real report from your own students.", "Run one free mock with a batch and we will walk your team through every report it produces.")}
'''
page('reports.html', 'Mock Test Result Analysis and Reports | ParikshaLab', 'Instant scores and a detailed result analysis after every NEET and JEE mock test: where the marks came from, subject split, time per question, answer review and a one tap PDF.', reports)

# ---------------------------------------------------------------- APPS
PH = [('01_login', 'Sign in', 'Mobile number and password'), ('02_test_list', 'Your tests', 'Start or resume with one tap'),
      ('03_jee_question', 'Exam screen', 'Timer, tabs and all four buttons'), ('04_jee_palette_open', 'Palette sheet', 'Five states with live counts'),
      ('05_jee_mathematics', 'Mathematics', 'Typeset equations on a small screen'), ('06_neet_physics', 'Physics', 'Long questions stay readable'),
      ('07_neet_zoology', 'Zoology', 'Statement questions, clearly laid out'), ('08_neet_zoomed', 'Zoom to 130%', 'Bigger text when it helps')]
figs = ''.join(f'<figure>{phone(n, t + ": " + c)}<figcaption><b>{t}</b><span>{c}</span></figcaption></figure>' for n, t, c in PH)
apps = f'''
<section class="page-hero" style="padding-bottom:40px">
  {AURORA}
  <div class="wrap z split">
    <div data-stagger>
      <h1><span class="kicker">CBT test app for Android, iOS and web</span>Open to <span class="grad">everything.</span></h1>
      <p class="lede">ParikshaLab runs as an app on Android and iOS, and in any modern browser on Windows, Mac, Chromebook or Linux. No lab setup, no special machines.</p>
      <div class="hero-cta"><a class="btn btn-primary" href="contact.html">Get it for your institute {svg("arrow")}</a></div>
    </div>
    <div class="fan" data-reveal="zoom">
      {phone("02_test_list", "Test list on a phone", eager=True)}
      {phone("03_jee_question", "JEE Main question on a phone", eager=True)}
      {phone("05_jee_mathematics", "Mathematics question on a phone", eager=True)}
    </div>
  </div>
</section>

<section style="padding-top:40px">
  <div class="wrap">
    <div class="platforms" data-stagger>
      <div class="plat">{svg("phone")}Android app</div>
      <div class="plat">{svg("phone")}iOS app</div>
      <div class="plat">{svg("tablet")}Tablets</div>
      <div class="plat">{svg("laptop")}Windows &amp; Mac</div>
      <div class="plat">{svg("laptop")}Chromebook &amp; Linux</div>
      <div class="plat">{svg("globe")}Chrome, Edge, Safari, Firefox</div>
    </div>
  </div>
</section>

<section class="band" data-carousel>
  <div class="wrap">
    <div class="sec-head" data-reveal style="margin-bottom:30px">
      <h2>The full exam, <span class="grad">in a pocket.</span></h2>
      <p class="lede">These are real screens from the phone app. Swipe or drag through a test.</p>
    </div>
  </div>
  <div class="car-edge"><button class="round" data-dir="-1" aria-label="Previous">{svg("left")}</button><button class="round" data-dir="1" aria-label="Next">{svg("arrow")}</button></div>
  <div class="carousel" data-reveal>{figs}</div>
</section>

<section>
  <div class="wrap">
    <div class="sec-head center" data-reveal>
      <h2>Practise on the phone. <span class="grad">Sit the mock in the lab.</span></h2>
    </div>
    <div class="grid g3" data-stagger>
      <div class="card"><span class="ic">{svg("users")}</span><h3>Same login everywhere</h3><p>The same test list, the same answers and the same results on every device.</p></div>
      <div class="card"><span class="ic g">{svg("cloud")}</span><h3>Nothing is lost</h3><p>Answers sync as they are chosen, so a dropped connection or a flat battery costs nothing.</p></div>
      <div class="card"><span class="ic v">{svg("lock")}</span><h3>One device at a time</h3><p>A login is active on one device, which keeps every attempt honest.</p></div>
    </div>
  </div>
</section>
{cta("Bring your students onto one platform.", "Android, iOS and the browser, all under your institution's name.")}
'''
page('apps.html', 'CBT Mock Test App for Android, iOS and Web | ParikshaLab', 'ParikshaLab runs as an app on Android and iOS and in any modern browser. See real screens of NEET and JEE Main tests on a phone.', apps)

# ---------------------------------------------------------------- ABOUT
about = phero('About ParikshaLab', 'Built for the institutes that prepare <span class="grad">India\'s doctors and engineers.</span>',
  'NEET and JEE are decided on a screen. We make sure students have seen that screen hundreds of times before the day it counts.') + f'''
<section style="padding-top:30px">
  <div class="wrap">
    <div class="grid g3" data-stagger>
      <div class="card"><span class="ic">{svg("target")}</span><h3>Practice should match the exam</h3><p>Same layout, same buttons, same palette, same pressure. Familiarity on exam day is worth marks.</p></div>
      <div class="card"><span class="ic c">{svg("chart")}</span><h3>A score is not feedback</h3><p>Students need to know where the marks went and where the time went. That is what our reports are for.</p></div>
      <div class="card"><span class="ic v">{svg("users")}</span><h3>Teachers stay in charge</h3><p>Faculty choose every question and every paper. The platform carries the rest.</p></div>
    </div>
  </div>
</section>

<section class="band">
  <div class="wrap split">
    <div data-reveal>
      <h2>Your name on it. <span class="grad">Every screen.</span></h2>
      <p class="lede">Students and parents see your institution, not a vendor. We stay invisible and run the engine underneath.</p>
      <ul class="ticks">
        <li><span><b>Your logo and colours</b> on the login page, the exam screen and every report.</span></li>
        <li><span><b>Your own web address,</b> such as cbt.yourschool.in, with a secure certificate.</span></li>
        <li><span><b>Your questions stay yours.</b> Private to your institution and never shared.</span></li>
      </ul>
    </div>
    <div class="stage" data-tilt data-reveal="zoom">
      <div class="glow-ring"></div>
      {laptop("01_login", "Student login page", "cbt.yourschool.in")}
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-head center" data-reveal>
      <h2>Live in days, <span class="grad">not months.</span></h2>
    </div>
    <div class="process" data-stagger>
      <div class="card"><span class="ic">{svg("call")}</span><h3>Demo</h3><p>We show the platform and run a trial test with one of your batches.</p></div>
      <div class="card"><span class="ic v">{svg("brush")}</span><h3>Your site</h3><p>We set up your branded site with your logo, colours and address.</p></div>
      <div class="card"><span class="ic c">{svg("layers")}</span><h3>Your tests</h3><p>Build papers in QBank Studio, or send us yours and we load them.</p></div>
      <div class="card"><span class="ic g">{svg("chart")}</span><h3>Go live</h3><p>Students sign in on any device, and reports arrive after every test.</p></div>
    </div>
  </div>
</section>
{cta("Let's talk about your batches.", "Tell us how many students you have and which exams they are preparing for. We will take it from there.")}
'''
page('about.html', 'About ParikshaLab | CBT Platform for NEET & JEE Institutes', 'ParikshaLab helps Indian schools and coaching institutes prepare students for NEET and JEE on the same kind of screen they will face on exam day. White labelled and live in days.', about)

# ---------------------------------------------------------------- CONTACT
contact = phero('Book a free demo', 'See a live test in <span class="grad">your own lab.</span>',
  'Book a free demo. We run a full mock with one of your batches, then walk your team through the reports. No cost, no commitment.') + f'''
<section style="padding-top:30px">
  <div class="wrap">
    <div class="contact-cards" data-stagger>
      <a class="card cc" href="{WA}" target="_blank" rel="noopener"><span class="ic g"><svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5.1-1.3A10 10 0 1 0 12 2zm5.8 14.2c-.2.7-1.4 1.3-2 1.4-.5.1-1.1.1-1.8-.1-.4-.1-1-.3-1.7-.6-3-1.3-4.9-4.3-5-4.5-.2-.2-1.2-1.6-1.2-3s.7-2.1 1-2.4c.2-.3.5-.4.7-.4h.5c.2 0 .4 0 .6.5l.8 2c.1.2.1.4 0 .5l-.3.5-.4.4c-.1.1-.3.3-.1.6.2.3.8 1.3 1.7 2.1 1.2 1 2.1 1.4 2.4 1.5.3.1.4.1.6-.1l.9-1c.2-.2.4-.2.6-.1l2 1c.2.1.4.2.4.3.1.2.1.7-.1 1.4z"/></svg></span><div><small>WhatsApp</small><b>+91 80881 58012</b></div></a>
      <a class="card cc" href="tel:+918088158012"><span class="ic">{svg("call")}</span><div><small>Phone</small><b>+91 80881 58012</b></div></a>
      <a class="card cc" href="mailto:admin.parikshalab@gmail.com"><span class="ic v">{svg("mail")}</span><div><small>Email</small><b>admin.parikshalab@gmail.com</b></div></a>
    </div>
  </div>
</section>

<section style="padding-top:20px">
  <div class="wrap" style="max-width:860px">
    <div class="panel" data-reveal>
      <h2 style="font-size:clamp(26px,3vw,36px)">Request a demo</h2>
      <p class="muted" style="margin:10px 0 28px">Fill this in and it opens WhatsApp with your details ready to send.</p>
      <form class="enquiry" id="enquiry">
        <label>Your name<input name="name" required autocomplete="name"></label>
        <label>Institution<input name="institution" required autocomplete="organization"></label>
        <label>City<input name="city" autocomplete="address-level2"></label>
        <label>Phone<input name="phone" type="tel" autocomplete="tel"></label>
        <label>Number of students<select name="students"><option value="">Choose</option><option>Under 100</option><option>100 to 500</option><option>500 to 2,000</option><option>Over 2,000</option></select></label>
        <label>Exams<select name="exams"><option>NEET and JEE Main</option><option>NEET only</option><option>JEE Main only</option></select></label>
        <label class="full">Anything we should know?<textarea name="message"></textarea></label>
        <div class="full" style="display:flex;align-items:center;gap:18px;flex-wrap:wrap"><button class="btn btn-primary" type="submit">Send on WhatsApp {svg("arrow")}</button><span class="form-note">We usually reply within a working day.</span></div>
      </form>
    </div>
  </div>
</section>
'''
page('contact.html', 'Book a Free Demo | ParikshaLab CBT Platform', 'Book a free ParikshaLab demo for your school or coaching institute. WhatsApp or call +91 80881 58012, or email admin.parikshalab@gmail.com.', contact)

# ---------------------------------------------------------------- STUDENT MOCK TEST PAGES
EXAMS = {
 'NEET': dict(file='neet-mock-test.html', name='NEET UG', other=('jee-main-mock-test.html', 'JEE Main mock tests'),
   title='Free NEET Mock Test 2027 in CBT Format, NTA Pattern | ParikshaLab',
   desc='Free full syllabus NEET UG mock tests on an NTA-style computer based test screen: 180 questions, 720 marks, +4/-1 marking, instant results with subject split and time per question. Join early access.',
   kicker='NEET mock test &middot; CBT format',
   h1='NEET mock tests on a <span class="grad">real exam screen.</span>',
   lede='Full syllabus NEET UG mock tests on the official pattern, in an NTA-style computer based test format. Your first mocks are free. Early access is opening now.',
   shot=('07_neet_physics', 'NEET mock test physics question with a circuit diagram on the CBT exam screen', 'NEET UG Full Syllabus Test 1'),
   phone=('07_neet_zoology', 'NEET zoology statement question in the mock test app on a phone'),
   spec='<dt>Questions</dt><dd>180 MCQs</dd><dt>Subjects</dt><dd>Physics, Chemistry, Botany, Zoology</dd><dt>Duration</dt><dd>180 minutes</dd><dt>Marking</dt><dd>+4 / &minus;1</dd><dt>Total</dt><dd>720 marks</dd>',
   bank='21,783 NEET UG questions',
   faq=[
    ('Are the NEET mock tests free?', 'Your first NEET mock tests on ParikshaLab are free. A full test series with more mocks will be available as a paid plan. Join early access on WhatsApp and we will tell you as soon as the free mocks open.'),
    ('Is NEET UG a computer based test?', 'NTA announces the exam mode for each year in the official NEET UG information bulletin, so check neet.nta.nic.in for the current mode. ParikshaLab NEET mocks follow the official paper pattern of 180 questions and 720 marks in a computer based format, so they build your speed and accuracy either way.'),
    ('What is the NEET UG exam pattern?', '180 multiple choice questions across Physics, Chemistry, Botany and Zoology, 180 minutes, +4 for a correct answer and &minus;1 for a wrong one, for a total of 720 marks.'),
    ('Can I take the mock test on my phone?', 'Yes. The mocks run in the Android and iOS apps and in any modern browser, and your answers are saved on every click, so a dropped connection costs nothing.'),
    ('What do I get after each mock test?', 'Your score the moment you submit, a result PDF, every question with your answer and the correct key, marks lost to negative marking, a subject-wise split and the time you spent on each question.'),
   ]),
 'JEE': dict(file='jee-main-mock-test.html', name='JEE Main', other=('neet-mock-test.html', 'NEET mock tests'),
   title='Free JEE Main Mock Test 2027 in CBT Format, NTA Pattern | ParikshaLab',
   desc='Free full syllabus JEE Main mock tests on an NTA-style computer based test screen: 75 questions, MCQ and numerical, 300 marks, instant results with subject split and time per question. Join early access.',
   kicker='JEE Main mock test &middot; CBT format',
   h1='JEE Main mock tests on the <span class="grad">real CBT screen.</span>',
   lede='Full syllabus JEE Main mock tests on the official pattern, with the same timer, subject tabs, buttons and question palette as the NTA computer based test. Your first mocks are free. Early access is opening now.',
   shot=('04_jee_palette_in_use', 'JEE Main CBT mock test with a graph based question and the NTA-style question palette', 'JEE Main Full Syllabus Mock'),
   phone=('05_jee_mathematics', 'JEE Main mathematics question in the mock test app on a phone'),
   spec='<dt>Questions</dt><dd>75 (60 MCQ + 15 numerical)</dd><dt>Subjects</dt><dd>Physics, Chemistry, Mathematics</dd><dt>Duration</dt><dd>180 minutes</dd><dt>Marking</dt><dd>+4 / &minus;1</dd><dt>Total</dt><dd>300 marks</dd>',
   bank='11,476 JEE Main questions',
   faq=[
    ('Are the JEE Main mock tests free?', 'Your first JEE Main mock tests on ParikshaLab are free. A full test series with more mocks will be available as a paid plan. Join early access on WhatsApp and we will tell you as soon as the free mocks open.'),
    ('Is JEE Main a computer based test?', 'Yes. NTA conducts JEE Main as a computer based test (CBT). ParikshaLab mocks use the same kind of screen: candidate details, a live timer, subject tabs, the four NTA buttons and a five-state question palette.'),
    ('What is the JEE Main paper pattern?', '75 questions across Physics, Chemistry and Mathematics, 20 multiple choice and 5 numerical answer questions per subject, in 180 minutes, with +4 for a correct answer and &minus;1 for a wrong one, for a total of 300 marks. Always confirm the latest pattern in the official NTA information bulletin.'),
    ('Can I practise numerical answer questions?', 'Yes. Numerical value questions are entered on screen exactly as in the real CBT, and equations and graphs are typeset so they read the way the paper prints them.'),
    ('What do I get after each mock test?', 'Your score the moment you submit, a result PDF, every question with your answer and the correct key, marks lost to negative marking, a subject-wise split and the time you spent on each question.'),
   ]),
}
def student_cta(e):
    return f'<a class="btn btn-primary" href="{WA_STU[e]}" target="_blank" rel="noopener">Get early access on WhatsApp {svg("arrow")}</a>'
for e, x in EXAMS.items():
    body = phero(x['kicker'], x['h1'], x['lede'],
      f'<div class="hero-cta" style="justify-content:center">{student_cta(e)}<a class="btn btn-ghost" href="#screen">See the exam screen</a></div><p class="form-note" style="margin-top:18px">First mocks free &middot; Android, iOS and any browser</p>') + f'''
<section id="screen" style="padding-top:40px">
  <div class="wrap split">
    <div class="stage" data-tilt data-reveal="zoom">
      <div class="glow-ring"></div>
      {laptop(x['shot'][0], x['shot'][1], x['shot'][2])}
    </div>
    <div data-reveal>
      <h2>Practise on the screen you will face.</h2>
      <p class="lede">Many marks lost in a {x['name']} mock are not about the syllabus. They go to time pressure, unfamiliar buttons and careless negative marking. A computer based mock fixes that before exam day.</p>
      <ul class="ticks">
        <li><span><b>NTA-style interface.</b> Save &amp; Next, Mark for Review, Clear Response and a live timer, exactly where you expect them.</span></li>
        <li><span><b>Five-state question palette.</b> Answered, not answered, marked and not visited, with live counts.</span></li>
        <li><span><b>Questions from a big bank.</b> Drawn from {x['bank']}, each with its answer key and explanation.</span></li>
        <li><span><b>Instant result analysis.</b> Score, subject split, negative marks and time on every question.</span></li>
      </ul>
    </div>
  </div>
</section>

<section class="band">
  <div class="wrap">
    <div class="sec-head center" data-reveal>
      <h2>The {x['name']} pattern, <span class="grad">in every mock.</span></h2>
    </div>
    <div class="spec" data-stagger>
      <div class="card"><span class="tag">{x['name']} mock test</span><dl>{x['spec']}</dl></div>
      <div class="card"><span class="tag v">After you submit</span><dl><dt>Score</dt><dd>Instantly</dd><dt>Result PDF</dt><dd>One tap</dd><dt>Answer review</dt><dd>Every question</dd><dt>Subject split</dt><dd>Yes</dd><dt>Time per question</dt><dd>Yes</dd></dl></div>
    </div>
  </div>
</section>

<section>
  <div class="wrap split rev">
    <div class="fan" data-reveal="zoom">
      {phone(x['phone'][0], x['phone'][1])}
      {phone("04_jee_palette_open", "Question palette open on a phone during a mock test")}
    </div>
    <div data-reveal>
      <h2>Your phone is enough.</h2>
      <p class="lede">Take a full mock on Android, iOS or any browser. Answers are saved on every click, and if your battery dies you pick up exactly where you left off.</p>
      <div class="hero-cta">{student_cta(e)}</div>
      <p class="muted" style="margin-top:22px">Preparing for both? {arrow_link(x['other'][0], 'See ' + x['other'][1])}</p>
    </div>
  </div>
</section>
{faq(x['faq'], x['name'] + ' mock test questions')}
<section style="padding-top:20px">
  <div class="wrap">
    <div class="cta" data-reveal="zoom">
      <h2>Run a coaching institute or school?</h2>
      <p>Give every batch {x['name']} mock tests under your own name, built from our question bank and yours, with reports for every student.</p>
      <div class="hero-cta"><a class="btn btn-primary" href="contact.html">Book a campus demo {svg("arrow")}</a><a class="btn btn-ghost" href="index.html">ParikshaLab for institutes</a></div>
    </div>
  </div>
</section>
'''
    ld = {"@context": "https://schema.org", "@graph": [faq_ld(x['faq']),
      {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE},
        {"@type": "ListItem", "position": 2, "name": x['name'] + " mock test", "item": SITE + x['file'].replace('.html', '')}]}]}
    page(x['file'], x['title'], x['desc'], body, ld)

# ---------------------------------------------------------------- 404
nf = phero('Error 404', 'This page <span class="grad">is not on the paper.</span>', 'The link may be old or mistyped.',
  f'<div class="hero-cta" style="justify-content:center"><a class="btn btn-primary" href="index.html">Back to home {svg("arrow")}</a><a class="btn btn-ghost" href="contact.html">Contact us</a></div>')
nf = nf.replace('class="page-hero"', 'class="page-hero" style="min-height:80vh;display:grid;align-content:center"')
page('404.html', 'Page not found | ParikshaLab', 'This page could not be found.', nf, index=False)

sm = ''.join(f'  <url><loc>{SITE}{p}</loc><lastmod>2026-10-06</lastmod><priority>{pr}</priority></url>\n' for p, pr in
             [('', '1.0'), ('neet-mock-test', '0.9'), ('jee-main-mock-test', '0.9'), ('platform', '0.9'), ('qbank', '0.9'), ('reports', '0.8'), ('apps', '0.8'), ('about', '0.6'), ('contact', '0.7')])
open(os.path.join(ROOT, 'sitemap.xml'), 'w', encoding='utf-8', newline='\n').write(
    '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + sm + '</urlset>\n')
print('built')
