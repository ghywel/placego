# site/wolframcollatzmahler: the clean entry point, www.wolframcollatzmahler.com

The public site the owner asked for on 2026-10-11 (CHAT-LEDGER.md CL366, CL367): a true original entry point that
explains to anyone what we learned, how close we are, what we lack and what we need; states the Rule 30 / Collatz /
Mahler relationship; carries images and animations; and holds a clean, searchable trove of our data. The older
`site/wolframrule30/` pages (cadencevideoplayer.com/wolframrule30) are a linked annex only. The owner named the site and its
domain on 2026-10-11: www.wolframcollatzmahler.com, served from the root of that domain.

## Files

| File | What it is |
|---|---|
| `index.html` | The entry: the problem in one breath, where we stand in one breath, three doors, the trio, the trove, why we ask. |
| `learn.html` | For anyone: the rule, the pyramid, the three questions as a coin, why it is hard. |
| `stand.html` | Where we stand: proved, measured, closed routes, the one missing statement, with sources. |
| `trio.html` | Rule 30, Collatz and Mahler's 3/2 side by side: the shared skeleton and where each is open. |
| `need.html` | What we need: seven asks in plain and exact words, and how a contribution is checked. |
| `trove.html` | The searchable catalogue; reads `data/manifest.json`. |
| `join.html` | Where to start reading, the standards, how to send something. |
| `style.css`, `r30.js` | The shared style and the small Rule 30 drawing engine (no dependencies). |
| `build_manifest.py` | Generates `data/manifest.json` from a curated list; run it after a data file changes. |
| `content/` | Markdown written by the other workers (GPT: `problems.md`, `trio-technical.md`), rendered into pages by Cloud. |

## Standards (CL366)

Every factual claim traces to the record and names its source on the page. Proof distance is stated plainly.
Prior art is credited by name. Static files only: no build step, no analytics, no cookies; external loads are Google
Fonts only. Nothing private. Data entries carry a schema, a source, a size, a SHA-256 and, where one exists, a replay
command. Three reading levels on every main page: plain words, the picture, the exact statement with its source.
Every drawing animates only while on screen and stands still under `prefers-reduced-motion`.

## Deploying

Copy the directory as it is (including `data/` and `content/`) to the root of www.wolframcollatzmahler.com so that
`/` serves `index.html`; the pages use relative paths and carry canonical links to that domain. `learn.html` links to the
annex by its absolute address.
