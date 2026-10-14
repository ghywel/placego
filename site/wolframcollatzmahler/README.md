# site/wolframcollatzmahler: the clean entry point, www.wolframcollatzmahler.com

The public site the owner asked for on 2026-10-11 (CHAT-LEDGER.md CL366, CL367): a true original entry point that
explains to anyone what we learned, how close we are, what we lack and what we need; states the Rule 30 / Collatz /
Mahler relationship; carries images and animations; and holds a clean, searchable trove of our data. The older
`site/wolframrule30/` pages are included as `rule30/`, the worked Rule 30 problem. The owner named the site and its
domain on 2026-10-11: www.wolframcollatzmahler.com, served from the root of that domain.

## Files

| File | What it is |
|---|---|
| `index.html` | The entry: the problem in one breath, where we stand in one breath, three doors, the trio, the trove, why we ask. |
| `learn.html` | For anyone: the rule, the pyramid, the three questions as a coin, why it is hard. |
| `stand.html` | Where we stand: proved, measured, closed routes, the one missing statement, with sources. |
| `trio.html` | Rule 30, Collatz and Mahler's 3/2 side by side: the shared skeleton and where each is open. |
| `need.html` | What we need: seven asks in plain and exact words, and how a contribution is checked. |
| `trove.html` | The searchable catalogue; the catalogue is embedded in the page by `build_manifest.py` (fetching `data/manifest.json` is only a fallback), so it works from the file system too. |
| `join.html` | Where to start reading, the standards, how to send something. |
| `problems.html`, `trio-technical.html` | For mathematicians (on the toolbar): the open statements exactly, typeset with KaTeX; the three problems with their theorems. On 2026-10-14 Cloud's record comb (RULE30-PRIZE.md 8.104) corrected problems.html's Data line. It had said "at least 18 for 125..138" beside "exact 17 at 132", and it lacked 125, 143, 147 and the upper bounds. It now matches stand.html and RECORD-MAP.md. |
| `vendor/katex/` | KaTeX 0.16.11 (MIT, licence included): stylesheet, script, auto-render, woff2 fonts; vendored so that the site makes no external loads beyond Google Fonts. |
| `index.html` (2026-10-14) | Front and centre: "The one missing method" (the four problems' shared missing step, with a table of what is known and each exact missing statement), and the counters updated (314 proved with a second reader: 306 proof pages plus eight results of 14 October; 697 research probes in lexicon/ and mahler/; 1 missing method, four statements). Rule 30's missing statement is kept as its instance. `problems.html` gained sections 9 (Mahler's exact form, G293, G294, the ladders, the census and existence results) and 10 (Erdős's ternary question). Record depths updated on `stand.html`, `need.html`, `record.html` and `wolfram.html` (exact at 125, 132, 139, 142, 143 and 147).  Corrected the same day by Cloud's record comb (RULE30-PRIZE.md 8.104). The 306 had counted every .md file in proofs/, including README.md, README-intro.md, picture-pass.md and summaries.md. There are 302 proof pages, and one (W283) is in the waiting room, so 301 + 8 = 309. The probe count is 701 with the four probes of the afternoon. |
| `wolfram.html`, `collatz.html`, `mahler.html` | One page per problem (the owner, 2026-10-14: "separate pages like this for wolfram / collatz / mahler in the top toolbar"), each in three levels with a live exact picture and check: Rule 30's three questions and where Question 1 stands (with a centre-column counter); Collatz, the conjecture, what is known, our counting form, an exact orbit plot (BigInt); Mahler, the exact form, what is in print, our census and ladder, the exact best-candidate plot and the 5 mod 8 game. The toolbar now reads Learn, Wolfram, Collatz, Mahler, Where we stand, How they connect (was "Rule 30, Collatz, Mahler"), What we need, For mathematicians, The trove, Join; "Rule 30, worked" is reached from the Wolfram page, and `rule30/index.html` marks Wolfram as current. |
| `mahler-census.html` | The Mahler census (2026-10-14): no Z-number below 2^63, the negative half to -2^63, a live exact horizon checker (BigInt), the records chart, and the cost of going further; linked from `stand.html` and `trio.html`. Sources: MAHLER.md sections 1 and 2, `tests/probes/mahler/`. Its share image was rendered without the real faces (`--fonts` absent); re-render with `build_share.py --fonts DIR` for the house typeface. |
| `cones.html`, `wheelcentre.html`, `record.html`, `ring.html` | Live pictures with inputs, linked from the pages they illustrate (`record.html` embeds `data/records.json`, written by `data/build_data.py`). |
| `style.css`, `r30.js` | The shared style and the small Rule 30 drawing engine (no dependencies). |
| `build_manifest.py` | Generates `data/manifest.json` from a curated list and embeds it in `trove.html`; run it after a data file changes. |
| `share/`, `build_share.py` | One share image per page (1200 x 630, flat colours, about 50 KB each) and the Open Graph and Twitter card tags in every page's head that point at it, so that a link to any page unfurls with its headline beside the Rule 30 pyramid. `python3 build_share.py` re-renders them with a headless Chromium (`CHROME=...` or `--chrome`); `--tags-only` refreshes the tags without a browser. The real faces need `--fonts DIR` with a `local.css` of `@font-face` rules and the latin woff2 files of Source Serif 4 and Inter beside it (download them from Google Fonts; nothing in that directory is committed); without it the renderer falls back to the system serif and sans. Re-run after a page's title, headline or description changes. |
| `data/build_data.py`, `data/replay.py` | Build the clean exports (records, forbidden words, rings) and embed the records in `record.html`; replay every record row in seconds. |
| `rule30/` | The Wolfram Rule 30 page, the worked problem: the nine HTML files of `site/wolframrule30/` copied verbatim (the owner, 2026-10-11: "perfect as it is"); served at `/rule30/`. Keep the nine files together; they load one another by relative path. |
| `content/` | Markdown written by the other workers (GPT: `problems.md`, `trio-technical.md`), rendered into pages by Cloud. |
| `COMB-2026-10-14.md` | Intel's record comb (RULE30-PRIZE.md 8.106): 41 corrections on eleven pages, quoted from both sides; four findings in generated data (records JSON, trove manifest) left for their builders; and a note that `content/` is no longer in git, so `problems.html` and `trio-technical.html` are now edited directly. |

## Standards (CL366)

Every factual claim traces to the record and names its source on the page. Proof distance is stated plainly.
Prior art is credited by name. Static files only: no build step, no analytics, no cookies; external loads are Google
Fonts only (KaTeX is vendored). Nothing private. Data entries carry a schema, a source, a size, a SHA-256 and, where one exists, a replay
command. Three reading levels on every main page: plain words, the picture, the exact statement with its source.
Every drawing animates only while on screen and stands still under `prefers-reduced-motion`.
Keyboard and screen readers: a skip link to the content on every page (including the worked page), a labelled site
navigation landmark, a visible focus ring on every link, card and control, every labelled drawing marked as an image,
scoped table headers, and the text-sized uses of the working colours (links, kickers, labels, status pills) darkened to
at least 4.5:1 against the paper in both light and dark modes (`--link`, `--teal-text`, `--green-text`, `--gold-text`
in `style.css`); the large and decorative uses keep the full colours.

## Deploying

Copy the directory as it is (including `data/` and `content/`) to the root of www.wolframcollatzmahler.com so that
`/` serves `index.html`; the pages use relative paths and carry canonical links to that domain. `rule30/` is served beside the pages at `/rule30/`.
