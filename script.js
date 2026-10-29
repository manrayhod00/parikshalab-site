// ParikshaLab site behaviour. No libraries; everything degrades to a readable static page.

// The user counter. Raise this number as the user base grows; every [data-count="users"] follows it.
var USER_COUNT = 1000;

var reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
var fine = matchMedia('(hover: hover) and (pointer: fine)').matches;
// Crawlers snapshot the page mid-animation, so they get the final numbers straight away.
var bot = navigator.webdriver || /bot|crawl|spider|slurp|google|bing|lighthouse|headless/i.test(navigator.userAgent);

// nav: glass on scroll, burger, scroll progress
var nav = document.getElementById('nav');
var bar = document.querySelector('.progress');
function onScroll() {
  nav.classList.toggle('stuck', scrollY > 10);
  if (bar) {
    var h = document.documentElement.scrollHeight - innerHeight;
    bar.style.transform = 'scaleX(' + (h > 0 ? scrollY / h : 0) + ')';
  }
}
addEventListener('scroll', onScroll, { passive: true });
onScroll();

// theme: light by default; the choice is remembered (the <head> script applies it before paint)
var root = document.documentElement, themeBtn = document.getElementById('theme');
function paintTheme() {
  var dark = root.getAttribute('data-theme') === 'dark';
  themeBtn.setAttribute('aria-label', dark ? 'Switch to light theme' : 'Switch to dark theme');
  var m = document.querySelector('meta[name="theme-color"]');
  if (m) m.setAttribute('content', dark ? '#060913' : '#f7f8fc');
}
themeBtn.addEventListener('click', function () {
  var dark = root.getAttribute('data-theme') !== 'dark';
  if (dark) root.setAttribute('data-theme', 'dark'); else root.removeAttribute('data-theme');
  try { localStorage.setItem('pl-theme', dark ? 'dark' : 'light'); } catch (e) {}
  paintTheme();
});
paintTheme();

var burger = document.getElementById('burger');
var links = document.getElementById('links');
burger.addEventListener('click', function () {
  var open = links.classList.toggle('open');
  burger.classList.toggle('open', open);
  burger.setAttribute('aria-expanded', open);
});

// counters
function runCount(el) {
  var target = el.dataset.count === 'users' ? USER_COUNT : +el.dataset.count;
  var suffix = el.dataset.suffix || '';
  var fmt = function (n) { return Math.round(n).toLocaleString('en-IN') + suffix; };
  if (reduce || bot) { el.textContent = fmt(target); return; }
  var run = el._run = (el._run || 0) + 1;   // a newer run cancels an older one
  var start = performance.now(), dur = 1800;
  (function tick(now) {
    if (run !== el._run) return;
    var t = Math.min(1, (now - start) / dur), e = 1 - Math.pow(1 - t, 4);
    el.textContent = fmt(target * e);
    if (t < 1) requestAnimationFrame(tick);
  })(start);
}
document.querySelectorAll('[data-count]').forEach(function (el) {
  var target = el.dataset.count === 'users' ? USER_COUNT : +el.dataset.count;
  el.textContent = target.toLocaleString('en-IN') + (el.dataset.suffix || '');
});

// reveal on scroll; [data-stagger] children get increasing delays
document.querySelectorAll('[data-stagger]').forEach(function (g) {
  Array.prototype.forEach.call(g.children, function (c, i) {
    if (!c.hasAttribute('data-reveal')) c.setAttribute('data-reveal', '');
    c.style.setProperty('--d', (i * 0.09) + 's');
  });
});
// Animations replay: an element plays when it comes into view and resets once it has
// fully left the screen, so scrolling back up or down plays it again.
var enter = new IntersectionObserver(function (entries) {
  entries.forEach(function (en) {
    if (!en.isIntersecting || en.target.classList.contains('in')) return;
    en.target.classList.add('in');
    en.target.querySelectorAll('[data-count]').forEach(runCount);
    en.target.dispatchEvent(new CustomEvent('reveal'));
  });
}, { threshold: 0.12, rootMargin: '0px 0px -60px 0px' });
var leave = new IntersectionObserver(function (entries) {
  entries.forEach(function (en) { if (!en.isIntersecting) en.target.classList.remove('in'); });
}, { threshold: 0 });
document.querySelectorAll('[data-reveal]').forEach(function (el) { enter.observe(el); if (!reduce) leave.observe(el); });

// cursor spotlight on cards
if (fine) document.addEventListener('pointermove', function (e) {
  var c = e.target.closest && e.target.closest('.card');
  if (!c) return;
  var r = c.getBoundingClientRect();
  c.style.setProperty('--mx', (e.clientX - r.left) + 'px');
  c.style.setProperty('--my', (e.clientY - r.top) + 'px');
});

// gentle 3D tilt on device stages
if (fine && !reduce) document.querySelectorAll('[data-tilt]').forEach(function (el) {
  var t = el.querySelector('.laptop') || el;
  el.addEventListener('pointermove', function (e) {
    var r = el.getBoundingClientRect();
    var x = (e.clientX - r.left) / r.width - 0.5, y = (e.clientY - r.top) / r.height - 0.5;
    t.style.transform = 'rotateY(' + (x * 7) + 'deg) rotateX(' + (-y * 6) + 'deg)';
  });
  el.addEventListener('pointerleave', function () { t.style.transform = ''; });
});

// guided tour: the step nearest the middle of the screen picks the screenshot
var steps = document.querySelectorAll('.tstep');
if (steps.length) {
  var shots = document.querySelectorAll('.tour-stage .scr img');
  var dots = document.querySelectorAll('.tour-dots i');
  var url = document.querySelector('.tour-stage .bar span');
  var tio = new IntersectionObserver(function (entries) {
    entries.forEach(function (en) {
      if (!en.isIntersecting) return;
      var i = +en.target.dataset.i;
      steps.forEach(function (s, k) { s.classList.toggle('on', k === i); });
      shots.forEach(function (s, k) { s.classList.toggle('on', k === i); });
      dots.forEach(function (s, k) { s.classList.toggle('on', k === i); });
      if (url && en.target.dataset.url) url.textContent = en.target.dataset.url;
    });
  }, { rootMargin: '-45% 0px -45% 0px' });
  steps.forEach(function (s, i) { s.dataset.i = i; tio.observe(s); });
}

// tabs
document.querySelectorAll('[data-tabs]').forEach(function (box) {
  var btns = box.querySelectorAll('.tabs button'), panels = box.querySelectorAll('.tab-panel');
  btns.forEach(function (b, i) {
    b.addEventListener('click', function () {
      btns.forEach(function (x, k) { x.classList.toggle('on', k === i); x.setAttribute('aria-selected', k === i); });
      panels.forEach(function (p, k) { p.classList.toggle('on', k === i); });
    });
  });
});

// phone carousel: buttons + drag to scroll on desktop
document.querySelectorAll('[data-carousel]').forEach(function (wrap) {
  var track = wrap.querySelector('.carousel');
  var step = function () { var f = track.querySelector('figure'); return f ? f.offsetWidth + 28 : 300; };
  wrap.querySelectorAll('[data-dir]').forEach(function (b) {
    b.addEventListener('click', function () { track.scrollBy({ left: step() * +b.dataset.dir, behavior: 'smooth' }); });
  });
  var down = false, sx = 0, sl = 0;
  track.addEventListener('pointerdown', function (e) {
    if (e.pointerType !== 'mouse') return;
    down = true; sx = e.clientX; sl = track.scrollLeft; track.classList.add('drag');
  });
  addEventListener('pointerup', function () { down = false; track.classList.remove('drag'); });
  track.addEventListener('pointermove', function (e) { if (down) track.scrollLeft = sl - (e.clientX - sx); });
  track.addEventListener('dragstart', function (e) { e.preventDefault(); });
});

// typing line in the "type it in" demo, replayed each time its panel is revealed
var typed = document.querySelector('[data-type]');
if (typed && !reduce) {
  var full = typed.dataset.type, out = typed.querySelector('.txt'), typing = 0;
  var box = typed.closest('[data-reveal]') || typed;
  out.textContent = '';
  box.addEventListener('reveal', function () {
    var run = ++typing, n = 0;
    out.textContent = '';
    (function next() {
      if (run !== typing) return;
      out.textContent = full.slice(0, ++n);
      if (n < full.length) setTimeout(next, 38 + Math.random() * 50);
    })();
  });
}

// enquiry form: builds a WhatsApp message (the site has no server)
var form = document.getElementById('enquiry');
if (form) form.addEventListener('submit', function (e) {
  e.preventDefault();
  var d = new FormData(form), lines = ['Hello ParikshaLab, I would like a demo.'];
  [['name', 'Name'], ['institution', 'Institution'], ['city', 'City'], ['phone', 'Phone'], ['students', 'Students'], ['exams', 'Exams'], ['message', 'Message']]
    .forEach(function (f) { var v = (d.get(f[0]) || '').trim(); if (v) lines.push(f[1] + ': ' + v); });
  window.open('https://wa.me/918088158012?text=' + encodeURIComponent(lines.join('\n')), '_blank', 'noopener');
});

var yr = document.getElementById('yr');
if (yr) yr.textContent = new Date().getFullYear();

// Exam chooser (2026-10-30): every "free mock" / "10 mocks" button asks NEET or JEE Main
// first. Without JS the links still work: /free/ and /signup/ ask the same question.
(function () {
  var EXAMS = [
    { code: 'neet', tag: 'NEET', name: 'NEET UG', meta: '180 questions · 720 marks · 3 hours' },
    { code: 'jee', tag: 'JEE', name: 'JEE Main', meta: '75 questions · 300 marks · 3 hours' }
  ];
  var BASE = 'https://test.parikshalab.in';
  var dlg = document.createElement('dialog');
  dlg.className = 'chooser';
  dlg.setAttribute('aria-labelledby', 'chooser-h');
  document.body.appendChild(dlg);
  function open(kind) {
    var free = kind === 'free';
    dlg.innerHTML = '<button class="ch-x" type="button" aria-label="Close">&times;</button>' +
      '<h3 id="chooser-h">Which exam are you preparing for?</h3>' +
      '<p>' + (free ? 'Your free full mock starts right away. No sign-up, just your name.'
                    : 'Pick ONE exam: 10 full mocks with report cards for <s class="was">&#8377;499</s> <b>&#8377;199</b> <span class="off">60% OFF</span>. Want both? Buy each separately.') + '</p>' +
      EXAMS.map(function (e) {
        var href = free ? BASE + '/free/' + e.code + '/' : BASE + '/signup/?exam=' + e.tag;
        return '<a class="ch-exam" href="' + href + '"><span class="t-ic ' + e.code + '">' + e.tag + '</span>' +
          '<span class="t-x"><b>' + e.name + '</b><span>' + e.meta + '</span></span><span class="t-arr">&rarr;</span></a>';
      }).join('');
    dlg.querySelector('.ch-x').onclick = function () { dlg.close(); };
    if (dlg.showModal) dlg.showModal(); else location.href = BASE + (free ? '/free/' : '/signup/');
  }
  dlg.addEventListener('click', function (e) { if (e.target === dlg) dlg.close(); });
  document.addEventListener('click', function (e) {
    var a = e.target.closest && e.target.closest('[data-free],[data-paid]');
    if (!a) return;
    e.preventDefault();
    if (links && links.classList.contains('open')) burger.click();
    open(a.hasAttribute('data-free') ? 'free' : 'paid');
  });
})();
