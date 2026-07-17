# design.md — Design System

The single source of truth for how everything looks. Reference it in a prompt — "style per `design.md`" — and you get a consistent product without art-directing anything.

The default here is a **white / light, editorial** aesthetic: high contrast, serif display headings, sans body, monospaced numerals, restrained semantic colour. It is a starting point, not a religion. Change the values to taste — but change them **here**, once, rather than in each project.

---

## How to use

1. Paste the Google Fonts `<link>` into `<head>`.
2. Paste the `:root` token block as the first rule in your `<style>`.
3. Style everything with `var(--token)`. Never hard-code a hex that a token already covers.
4. Spread the shared chart `layout` defaults into every chart.
5. If you need a value the system does not have, **add it here first, then use it.** Do not fork silently.

Rule 5 is the one that matters. The moment one project invents its own blue, the system is dead.

---

## Colour tokens

```css
:root {
  /* surfaces */
  --bg: #fafaf8;        /* page background — warm off-white */
  --bg2: #ffffff;       /* cards, raised surfaces */
  --bg3: #f5f5f0;       /* table headers, inset chips */
  --bg4: #eeeee8;       /* progress tracks, deep insets */
  --bg-hover: #f0f0ea;  /* row / cell hover */
  /* borders */
  --bd: #e2e0d8;        /* default hairline */
  --bd2: #d5d3ca;       /* medium */
  --bd-strong: #c0beb5; /* emphasis / axis lines */
  /* text */
  --t1: #1a1a18;        /* primary — near-black */
  --t2: #5c5c56;        /* secondary */
  --t3: #8a8a82;        /* tertiary / labels */
  --t4: #b0b0a8;        /* disabled / faint */
  /* semantic: green = good/up, red = bad/down */
  --g: #1a8754;  --g2: #22a366;  --g-bg: rgba(26,135,84,0.07);  --g-bg2: rgba(26,135,84,0.14);
  --r: #c0392b;  --r2: #e74c3c;  --r-bg: rgba(192,57,43,0.07);  --r-bg2: rgba(192,57,43,0.14);
  /* accents: blue = neutral/baseline, amber = caution, purple, cyan = info, pink = alt */
  --b: #2563eb;  --b2: #3b82f6;  --b-bg: rgba(37,99,235,0.06);  --b-bg2: rgba(37,99,235,0.12);
  --a: #b45309;  --a-bg: rgba(180,83,9,0.07);
  --p: #7c3aed;  --p-bg: rgba(124,58,237,0.06);
  --c: #0891b2;  --c-bg: rgba(8,145,178,0.06);
  --pk: #be185d; --pk-bg: rgba(190,24,93,0.06);
  /* type */
  --serif: 'Instrument Serif', Georgia, serif;
  --sans: 'DM Sans', -apple-system, sans-serif;
  --mono: 'JetBrains Mono', 'SF Mono', 'Menlo', monospace;
  /* elevation */
  --shadow-sm: 0 1px 2px rgba(0,0,0,0.04);
  --shadow: 0 1px 3px rgba(0,0,0,0.06), 0 1px 2px rgba(0,0,0,0.04);
  --shadow-md: 0 4px 6px rgba(0,0,0,0.05), 0 2px 4px rgba(0,0,0,0.04);
  --shadow-lg: 0 10px 15px rgba(0,0,0,0.06), 0 4px 6px rgba(0,0,0,0.04);
  /* radius */
  --radius: 8px;
  --radius-lg: 12px;
}
```

**Semantic discipline.** Green always means good or up; red always means bad or down. Blue is the neutral or baseline series. Never use green or red decoratively — on a page full of numbers they carry meaning, and spending them on decoration makes the page unreadable.

---

## Typography

```html
<link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;0,9..40,600;0,9..40,700;1,9..40,400&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
```

| Role | Family | Where |
|---|---|---|
| Display / masthead | `--serif` | `<h1>` only; italic `<em>` for the subordinate clause |
| Body / UI | `--sans` | everything by default; `line-height:1.5` |
| Numerals / code | `--mono` | figures, table columns, axis ticks |

**Numbers are always monospaced**, so columns align and digits do not jump around as values change. This is the single cheapest thing you can do to make a page look professional.

Labels: `11px`, uppercase, `letter-spacing:0.8–1px`, weight 600–700, colour `--t3`.

---

## Layout

```css
.shell { max-width:1520px; margin:0 auto; padding:20px 32px 60px; }
```

Breakpoints: `1200px`, `768px`, `480px`, plus `@media(pointer:coarse)` for touch — minimum 44px tap targets.

---

## Core components

**Masthead** — serif title with an italic muted clause, 2px solid underline, status pills on the right.

```css
.masthead { padding:28px 0 22px; border-bottom:2px solid var(--t1); display:flex; justify-content:space-between; align-items:flex-end; flex-wrap:wrap; gap:12px; }
.masthead h1 { font-family:var(--serif); font-size:32px; font-weight:400; letter-spacing:-0.5px; }
.masthead h1 em { font-style:italic; color:var(--t3); }
```

**KPI strip** — grid with a hairline gap, wrapped in a rounded border. The gap is the border colour showing through, which is why it is 1px and not a real border on each cell.

```css
.kpi-strip { display:grid; grid-template-columns:repeat(4,1fr); gap:1px; background:var(--bd); border:1px solid var(--bd); border-radius:var(--radius-lg); overflow:hidden; }
.kpi-val { font-family:var(--mono); font-size:24px; font-weight:700; letter-spacing:-0.5px; }
.kpi-val.pos { color:var(--g); } .kpi-val.neg { color:var(--r); }
```

**Cards** — `--bg2`, hairline border, `--radius-lg`, `--shadow`; uppercase `--t2` title in the head.

**Tables** — sticky uppercase header on `--bg3` with a 2px bottom border; rows hover to `--bg-hover`.

---

## Chart defaults

Charts are the core of most dashboards, so their styling is part of the system rather than an afterthought. Spread this into every chart call.

```js
const CHART_LAYOUT = {
  paper_bgcolor: 'transparent',
  plot_bgcolor: '#fafaf8',                                   // = --bg
  font: { family: 'DM Sans', size: 10, color: '#5c5c56' },   // = --sans / --t2
  margin: { t: 10, b: 10, l: 10, r: 10 },
  xaxis: {
    gridcolor: '#eeeee8', linecolor: '#d5d3ca', linewidth: 1, showgrid: false,
    tickfont: { size: 9 }
  },
  yaxis: {
    gridcolor: '#f0f0ea', linecolor: '#d5d3ca', linewidth: 1, showgrid: true,
    tickfont: { size: 9, family: 'JetBrains Mono' }          // monospaced numerals
  },
  showlegend: true,
  legend: { x: 0, y: 1.02, orientation: 'h', font: { size: 9 }, bgcolor: 'transparent' },
  hovermode: 'x unified',                                     // unified crosshair on ALL time series
  hoverlabel: { bgcolor: '#fff', bordercolor: '#d5d3ca', font: { size: 10, family: 'DM Sans' } }
};
```

Conventions, applied to every chart — when you change one, audit its siblings:

- No vertical gridlines. Horizontal only, and faint.
- `hovermode:'x unified'` on all time series. Never leave a chart on the library default.
- Annotation colours follow the semantic palette.

---

## Non-negotiables

- Light theme by default; maximally readable; high contrast.
- Semantic green/red reserved for meaning, never decoration.
- All figures monospaced.
- One change to a shared pattern means applying it to every instance of that pattern.
