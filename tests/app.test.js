const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const root = path.resolve(__dirname, '..');
test('demo includes required GSAP and ScrollTrigger scripts', () => {
  const html = fs.readFileSync(path.join(root, 'index.html'), 'utf8');
  assert.match(html, /gsap@3\.12\.5\/dist\/gsap\.min\.js/);
  assert.match(html, /ScrollTrigger\.min\.js/);
});
test('animation code registers ScrollTrigger and respects reduced motion', () => {
  const js = fs.readFileSync(path.join(root, 'app.js'), 'utf8');
  assert.match(js, /registerPlugin\(ScrollTrigger\)/);
  assert.match(js, /prefers-reduced-motion/);
});
test('page includes responsive viewport and accessible interactive control', () => {
  const html = fs.readFileSync(path.join(root, 'index.html'), 'utf8');
  assert.match(html, /name="viewport"/);
  assert.match(html, /id="pulse-button"[^>]+type="button"/);
});
