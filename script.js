// nav shadow on scroll
var nav = document.getElementById('nav');
addEventListener('scroll', function () {
  nav.classList.toggle('stuck', scrollY > 8);
}, { passive: true });

// mobile menu
var burger = document.getElementById('burger');
var links = document.getElementById('links');
burger.addEventListener('click', function () { links.classList.toggle('open'); });
links.addEventListener('click', function (e) {
  if (e.target.tagName === 'A') links.classList.remove('open');
});

// reveal on scroll + animate bars once visible
var io = new IntersectionObserver(function (entries) {
  entries.forEach(function (en) {
    if (!en.isIntersecting) return;
    en.target.classList.add('in');
    en.target.querySelectorAll('.fill').forEach(function (f, i) {
      setTimeout(function () { f.style.width = f.dataset.w + '%'; }, 160 + i * 130);
    });
    io.unobserve(en.target);
  });
}, { threshold: 0.14, rootMargin: '0px 0px -40px 0px' });
document.querySelectorAll('.reveal').forEach(function (el) { io.observe(el); });

// live countdown inside the exam mockup
var clock = document.getElementById('clock');
var left = 2 * 3600 + 58 * 60 + 41;
setInterval(function () {
  if (left > 0) left--;
  var h = Math.floor(left / 3600), m = Math.floor(left % 3600 / 60), s = left % 60;
  var p = function (n) { return String(n).padStart(2, '0'); };
  clock.textContent = p(h) + ':' + p(m) + ':' + p(s);
}, 1000);

document.getElementById('yr').textContent = new Date().getFullYear();
