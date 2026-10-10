# wolframrule30: the Rule 30 page for cadencevideoplayer.com/wolframrule30

Built by Cloud on 2026-10-09 at the owner's request, to be deployed by Local. The owner will send the page to
Stephen Wolfram, so it is written for a reader with no background, and every claim on it is taken from the record
(STATE-OF-THE-PROOF.md, RULE30-PRIZE.md, PROOFS.md) or from Wolfram's own 2019 prize announcement.

## What is here

| File | What it is |
|---|---|
| `index.html` | The whole story on one page, from "what is Rule 30" to where Problem 1 stands, every visual embedded. |
| `vitruvian.html` | Vitruvian Rule 30: pyramid, square, prize column, wheel, clocks, wall run. |
| `heartbeat.html` | Frontier Heartbeat: a starting frame and four labelled acts on a repeating centre's cost. |
| `necklace.html` | The All-S Necklace: GPT's 84-cell ring that keeps the clock for ever. |
| `sieve.html` | The Edge-Event Sieve: the forced left side, interactive, with the counterexample wedge. |
| `centre.html` | Make the Centre Say Anything: build a start so the centre spells the primes, Fibonacci, pi or a word; watch a finite start run out. |
| `sierpinski.html` | Sierpinski Everywhere: the whole pyramid as odd overlaps of Sierpinski triangles, one per kick. |
| `bricks.html` | Bricks, Rulers and Fronts: the left front, the edge ruler, the crystals and the turning ring. |

The landing page walks a reader with no background to the current state of Problem 1, in eight chapters: the rule;
why it matters; order at the edges (the left front, the edge ruler); the whole picture (the plate); assume the
opposite (making the centre say anything, the crystals, Sierpinski triangles, Sierpinski Everywhere, the sieve, the heartbeat); what we found (the necklace, the turning
ring); a twin in arithmetic (Collatz: the Gray code worked through on one number, then Rule 30 beside the powers of
3); how it was done. It has five visuals of its own (the growing pyramid, the rule one cell at a time, the
Sierpinski figure, the Gray-code example, and the twin) and embeds every render: fifteen visuals, ten of them in
frames. The Collatz chapter's claims come from COLLATZ-PRIZE.md (its honest summary, §3, §5, §8 and the edge-ruler
addendum) and RULE30-PRIZE.md §8.45. Three renders have a Sound button, off by default (Web Audio, started only by a
click): the edge ruler (each triangle an octave note), the left front (one gliding tone) and the necklace (a music
box, one bar of six beats). Each keeps its own time on the audio clock, so it plays on while its frame is out of
view, until paused or switched off. `bricks.html` is embedded four times, one view
per frame, chosen by the hash (`#front`, `#ruler`, `#crystals`, `#ring`).

The seven render pages are full pages in their own right, with a link back to the story. Opened with `?embed`, a page
hides its prose and shows only its toolbar and stage; that is how `index.html` embeds them in iframes. Each
render is the same page as its Claude artifact of 2026-10-09, wrapped in a full HTML document.

Every visual animates only while it is on screen. The landing page watches its own two canvases and each frame with an
IntersectionObserver and tells each frame by `postMessage({r30: "visibility", visible})` as it scrolls in and out of
view (a hidden tab counts as off screen). A short snippet in the head of each render, the same in all seven, holds the
page's animation frames and skips its interval ticks while it is told it is out of view, and asks once as it starts.
Opened on its own, a render always runs.

## Deploying (Local)

- Static files only: no build step, no server code, no analytics, no cookies. Copy the eight `.html` files into the
  site's `/wolframrule30/` directory so that `/wolframrule30/` serves `index.html`. `README.md` need not be copied.
- Keep the eight files together: the landing page loads the others by relative path.
- External loads: Google Fonts (stylesheets and font files) only. Links go out to GitHub (the public record),
  writings.stephenwolfram.com, wolframscience.com and arxiv.org.

## Checks after deploying

- `/wolframrule30/` opens on the title and the growing pyramid, and its tally counts up.
- The ten frames (left front, edge ruler, plate, the centre saying anything, crystals, Sierpinski Everywhere,
  sieve, heartbeat, necklace, turning ring) show their toolbar and picture with no prose inside the frame, and each "Open ... on its own page"
  link opens the full page with its notes and a working back link.
- A frame scrolled out of view stops, and carries on from the same place when it comes back.
- On a phone-width window nothing scrolls sideways.
- The browser console shows no errors. (Cloud's checks before handover: none at 1440 and 400 pixels wide, in light
  and dark mode, on all five pages. On 2026-10-09, for the one-page version: no page errors at 1440 and 390 pixels
  wide, light and dark, with all eight frames loaded, and every frame checked to stop off screen and carry on when
  back; the sandbox blocked the font loads and served no favicon, which is all the console showed.)

## Editing

The text of `index.html` is meant to stay faithful to the record. If a result changes, change the page from
STATE-OF-THE-PROOF.md, not from memory, and keep its plain-language register: the owner asked for visuals first and
no dense mathematics.

`ruler-chord.m4a` and `ruler-chord.webm`, played by the ruler's "Hear it as a chord" button in `bricks.html`, are rendered by
`site/render_ruler_chord.py` (not published) and live beside the pages on the site: in the Cadence tree's `Site/wolframrule30/`,
which `publish-site.sh` merges with this folder. Audio is kept out of this repository (no data files in git). Re-render with
`python3 site/render_ruler_chord.py <Cadence>/Site/wolframrule30` and bump the `?v=` on the two sources.
