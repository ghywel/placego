# wolframrule30: the Rule 30 page for cadencevideoplayer.com/wolframrule30

Built by Cloud on 2026-10-09 at the owner's request, to be deployed by Local. The owner will send the page to
Stephen Wolfram, so it is written for a reader with no background, and every claim on it is taken from the record
(STATE-OF-THE-PROOF.md, RULE30-PRIZE.md, PROOFS.md) or from Wolfram's own 2019 prize announcement.

## What is here

| File | What it is |
|---|---|
| `index.html` | The landing page: from "what is Rule 30" to where Problem 1 stands. |
| `vitruvian.html` | Vitruvian Rule 30: pyramid, square, prize column, wheel, clocks, wall run. |
| `heartbeat.html` | Frontier Heartbeat: four acts on what a repeating centre would demand. |
| `necklace.html` | The All-S Necklace: GPT's 84-cell ring that keeps the clock for ever. |
| `sieve.html` | The Edge-Event Sieve: the forced left side, interactive (linked, not embedded). |

The landing page has two visuals of its own, the growing pyramid with its centre column read off and the rule applied
one cell at a time, and embeds three of the renders.

The four render pages are full pages in their own right, with a link back to the story. Opened with `?embed`, a page
hides its prose and shows only its toolbar and stage; that is how `index.html` embeds three of them in iframes. Each
render is the same page as its Claude artifact of 2026-10-09, wrapped in a full HTML document.

## Deploying (Local)

- Static files only: no build step, no server code, no analytics, no cookies. Copy the five `.html` files into the
  site's `/wolframrule30/` directory so that `/wolframrule30/` serves `index.html`. `README.md` need not be copied.
- Keep the five files together: the landing page loads the others by relative path.
- External loads: Google Fonts (stylesheets and font files) only. Links go out to GitHub (the public record),
  writings.stephenwolfram.com, wolframscience.com and arxiv.org.

## Checks after deploying

- `/wolframrule30/` opens on the title and the growing pyramid, and its tally counts up.
- The three embedded renders (plate, heartbeat, necklace) show their toolbar and animation with no prose inside the
  frame, and each "Open ... on its own page" link opens the full page with its notes and a working back link.
- On a phone-width window nothing scrolls sideways.
- The browser console shows no errors. (Cloud's checks before handover: none at 1440 and 400 pixels wide, in light
  and dark mode, on all five pages.)

## Editing

The text of `index.html` is meant to stay faithful to the record. If a result changes, change the page from
STATE-OF-THE-PROOF.md, not from memory, and keep its plain-language register: the owner asked for visuals first and
no dense mathematics.
