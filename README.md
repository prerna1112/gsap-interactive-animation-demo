# Signal Motion — GSAP + ScrollTrigger capability demo

An application-specific prototype demonstrating a smooth, responsive scroll narrative for a small dashboard starter task. It uses GSAP timelines, ScrollTrigger, staggered reveals, SVG path drawing, counters, parallax, and a small interaction—without a backend or client data.

## Live demo

https://gsap-interactive-animation-demo.vercel.app

Case study: [docs/signal-motion-gsap-case-study.pdf](docs/signal-motion-gsap-case-study.pdf)

## What it demonstrates

- ScrollTrigger progress rail, hero parallax, and one-time progressive reveals.
- A sequenced SVG chart line/area reveal with data points.
- Animated metric counters and progress bars.
- Responsive layout with mobile-friendly touch targets.
- A “Pulse the data” control with immediate feedback.
- `prefers-reduced-motion` fallback that renders the content without animation.

## Architecture

This is intentionally a dependency-light static page: semantic HTML provides the content, CSS owns layout and visual states, and `app.js` owns animation orchestration. GSAP and ScrollTrigger are loaded from jsDelivr for the demo; production work can pin/bundle them through the client’s existing build system.

## Run locally

```bash
npm test
python3 -m http.server 4175
```

Open http://localhost:4175. Scroll through the page and use “Pulse the data”.

## Tests

The Node test file checks that the GSAP/ScrollTrigger assets, reduced-motion guard, plugin registration, viewport metadata, and accessible button are present. Visual behavior was verified in Chromium at desktop and mobile widths.

## Trade-offs and limitations

The chart uses realistic dummy values and an inline SVG so there is no API dependency. The CDN scripts require network access; a production implementation should bundle and version them. This prototype focuses on one polished interaction sequence rather than a full product dashboard.

## Honest context

This is a new prototype created to demonstrate the requested GSAP/ScrollTrigger capability. It is not represented as previous paid client work.
