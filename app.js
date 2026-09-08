(function(){
  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const qs = (s) => document.querySelector(s);
  if (!window.gsap || !window.ScrollTrigger || reduceMotion) {
    document.querySelectorAll('.metric-value').forEach((el) => { el.textContent = el.dataset.value; });
    document.querySelectorAll('.metric-bar span').forEach((el) => { el.style.width = '82%'; });
    qs('.chart-line')?.style.setProperty('stroke-dashoffset', '0');
    qs('.chart-area')?.style.setProperty('opacity', '1');
    return;
  }
  gsap.registerPlugin(ScrollTrigger);
  gsap.from('.site-header', { y: -24, opacity: 0, duration: .55, ease: 'power2.out' });
  gsap.from('.title-line', { y: 70, opacity: 0, stagger: .12, duration: .8, ease: 'power3.out', delay: .2 });
  gsap.from('.hero-art', { scale: .86, opacity: 0, rotate: 3, duration: 1, ease: 'power3.out', delay: .35 });
  gsap.utils.toArray('.reveal').forEach((el) => gsap.from(el, { y: 24, opacity: 0, duration: .65, ease: 'power2.out', scrollTrigger: { trigger: el, start: 'top 84%', once: true } }));
  gsap.to('#scroll-progress', { width: '100%', ease: 'none', scrollTrigger: { scrub: .2, start: 0, end: 'max' } });
  gsap.to('.signal-card', { y: -20, rotate: 2, ease: 'none', scrollTrigger: { trigger: '.hero', start: 'top top', end: 'bottom top', scrub: 1 } });
  gsap.to('.orb-one', { y: 120, x: -30, ease: 'none', scrollTrigger: { trigger: '.hero', start: 'top top', end: 'bottom top', scrub: 1.4 } });
  gsap.to('.orb-two', { y: -80, x: 20, ease: 'none', scrollTrigger: { trigger: '.hero', start: 'top top', end: 'bottom top', scrub: 1.2 } });
  document.querySelectorAll('.metric-card').forEach((card, index) => {
    const value = card.querySelector('.metric-value'); const target = Number(value.dataset.value);
    const bar = card.querySelector('.metric-bar span'); const state = { n: 0 };
    gsap.to(state, { n: target, duration: 1.1, ease: 'power2.out', onUpdate: () => { value.textContent = Math.round(state.n); }, scrollTrigger: { trigger: card, start: 'top 80%', once: true } });
    gsap.to(bar, { width: `${78 + index * 7}%`, duration: .9, ease: 'power2.out', scrollTrigger: { trigger: card, start: 'top 80%', once: true } });
    gsap.from(card, { y: 45, opacity: 0, duration: .7, delay: index * .08, ease: 'power3.out', scrollTrigger: { trigger: card, start: 'top 84%', once: true } });
  });
  const chart = gsap.timeline({ scrollTrigger: { trigger: '.chart-frame', start: 'top 72%', end: 'bottom 55%', scrub: 1, once: true } });
  chart.to('.chart-line', { strokeDashoffset: 0, duration: 1.3, ease: 'power2.out' }, 0).to('.chart-area', { opacity: 1, duration: .6 }, .2).to('.chart-points circle', { opacity: 1, stagger: .08, duration: .25 }, .5);
  gsap.from('.sequence-panel', { y: 35, opacity: 0, duration: .75, ease: 'power3.out', scrollTrigger: { trigger: '.sequence-panel', start: 'top 82%', once: true } });
  const pulseButton = qs('#pulse-button');
  pulseButton?.addEventListener('click', () => {
    const tl = gsap.timeline(); tl.to('.chart-points circle', { scale: 1.7, transformOrigin: 'center', stagger: .06, duration: .18, ease: 'power2.out' }).to('.chart-points circle', { scale: 1, stagger: .06, duration: .28, ease: 'elastic.out(1,.5)' });
    qs('#pulse-feedback').textContent = 'signal refreshed / 184ms';
  });
})();
