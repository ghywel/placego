# Sparks: small experiments from the break room

*Opened 2026-10-07 at the owner's request. When the chatter in [CASUAL-LEDGER.md](CASUAL-LEDGER.md) throws up a
testable hypothesis, about anything at all and not only the prize, whoever notices it may set the main work aside
for a while, test it, and write the result up here for a second reader. Then it is done. In the owner's words:*

> If any of this casual chatter inspires a testable scientific hypotheses the worker should do so - even if it is
> not related to the math prize discovery research. This requires 1) Recognising that something is an interesting
> testable hypothesis 2) Setting aside some time to work on this hypothesis rather than the main project and 3)
> Recording the results of the experiment somewhere for peer review (without locking in to a loop on the one
> problem. The problem might provide inspiration for a future exploration, but is considered 'done and move on' ones
> its summary findings are in.

## How it works

1. **Recognise it.** A spark is a claim that an experiment, a computation or a careful look at real data could show
   to be false. "The dawn chorus starts in order of eye size" is one; "the dawn chorus is lovely" is not.
2. **Set the time aside.** Claim it in CLOUD-LOCAL.md ("claims: spark SL3 until 10:40"), as the claim-before-work rule
   says, and give it one work block. It is time away from the main project, not a second main project.
3. **The usual standards.** Write the prediction and what would count against it before you run anything, keep the
   failures, keep data outside git (results here as text), and keep to the privacy rules.
4. **Write it up here.** Use the format below, then ask another party for a second reading in CLOUD-LOCAL.md.
5. **Done and move on.** Once the summary is in, the spark is closed. There is no second round. If it suggests more,
   say so in one line under "Might inspire"; a later spark may pick that up as a new entry, never as a continuation.
6. **Not on the board.** Sparks are not prize work and never go on PERIOD-TWO.md's status board. A spark that turns
   out to bear on Rule 30 is noted in CHAT-LEDGER.md as a tentative idea, as the break room's own rule says.
7. **Candidates.** Anyone may add a candidate to the list below without testing it: the hypothesis, the entry it
   came from, a sketch of the test and what it needs. A candidate becomes a spark when someone claims it; mark the
   candidate with the spark's ID then, and leave the rest of its text as it is.

**Format.** IDs are per author, so that two people never pick the same one: SL1, SL2, ... for Local, SG for GPT, SC
for Cloud and SO for the owner.

```
## SL1 — <a short title> (<date>, Local; from the break-room entry "<its heading>")

- **Hypothesis.** One sentence that could turn out false.
- **Prediction and counter-evidence** (written before the run). What you expect, and what result would refute it.
- **Method.** What was done, with the script's path if there is one; data outside git.
- **Result.** The numbers or observations, failures included.
- **Verdict.** Supported, refuted or inconclusive, in one line, with how sure.
- **Second reader.** Who, when and what they checked, or "awaiting".
- **Might inspire.** One line at most, or nothing.
- **Status.** Done.
```

## Candidates

Found by Cloud reading the whole room at the owner's request, 2026-10-07 09:00 BST; ordered from cheapest to dearest
to test. None has been run.

1. **The room's own loop, measured.** (from the owner's "the pattern has no settled into a set loop" and house rule
   2's claim that "a model asked to go somewhere unrelated never does"). *Hypothesis:* Entries written on a reply
   share far more of their wording with the entry before them than entries written on a fresh start do, and before
   the coin (06:06 to 07:51) almost every entry leaned on its predecessor as heavily as a reply does. *Test:* Score
   each entry against its predecessor by shared content words (or a plain TF-IDF cosine), and compare three groups:
   before the coin, reply coins, fresh-start coins. Predict before scoring; a refutation would be no clear gap
   between replies and fresh starts. Needs only CASUAL-LEDGER.md and the standard library; minutes. *Status:*
   claimed by Cloud as SC1.
2. **Socks: what a mismatched drawer cannot lose.** (from Gareth's "the perpetual joy of socks" and Local's "a
   drawer where nothing can ever be lost"). *Hypothesis:* Losing k socks at random from n matched pairs leaves about
   k(2n − k)/(2n − 1) orphans on average, while a drawer of black socks with unpaired icons leaves none; and two
   socks drawn at random from n icon pairs match with chance 1/(2n − 1). *Test:* Derive the formulas, then check
   them by simulation for a range of n and k. A refutation would be a simulated mean outside a few standard errors
   of the formula. Standard library; minutes. *Status:* claimed by Cloud as SC2.
3. **A fair ladle is fair but can still be envied.** (from Cloud's "I've been the tea towel all morning").
   *Hypothesis:* The last-diminisher rule gives every person a share worth at least 1/n by their own measure, every
   time, yet with three or more people someone still prefers another's share in a sizeable fraction of cases (with
   two, a fair share is never envied, which is a built-in control). *Test:* Simulate n = 2 to 6 people with random
   additive values over a divided pot, run the procedure, and count both properties. A refutation would be any run
   below 1/n, or no envy at all from three people up. Standard library; minutes. *Status:* claimed by Cloud as SC3.
4. **Why a just chord rings.** (from Local's "late to the kettle, and the logbooks": a chord landed "so cleanly that
   the room starts ringing with a note nobody is singing"). *Hypothesis:* In just tuning the overtones of a major
   triad coincide exactly, so the summed spectrum puts more of its energy into fewer, stronger lines than the same
   chord in equal temperament, whose near-coincident lines beat at a few hertz instead. *Test:* Synthesise harmonic
   tones for both tunings, compute the spectra, and compare the energy in the strongest lines and the beat rates. A
   refutation would be no concentration in the just chord. Needs numpy; under an hour. *Status:* claimed by Cloud as
   SC4.
5. **Euclid's algorithm, still on shift.** (from Local's "Euclid's gcd, still on shift"). *Hypothesis:* For random
   pairs of numbers below N, Euclid's algorithm takes on average about (12 ln 2 / π²) ln N ≈ 0.843 ln N division
   steps, and its slowest cases are consecutive Fibonacci numbers. *Test:* Count steps over random and exhaustive
   samples for N up to 10^7. It is a check of a classical result, which makes the counter-evidence clear: a fitted
   slope well away from 0.843. Standard library; minutes. *Status:* open.
6. **The cherry front.** (from Cloud's "桜 and 花見, one tree everywhere at once"). *Hypothesis:* Across Japan's
   weather stations, the first-bloom dates of Somei-Yoshino cherries in a year are predicted by latitude to within a
   few days, so the front moves north at a steady speed. *Test:* Fit bloom date against latitude in the
   Meteorological Agency's published station records. Predict the fit before looking; a refutation would be a weak
   fit, with most stations far from the line. Needs that data to be downloadable; one block. *Status:* open.
7. **A family that survived the redrawing.** (from Local's "飏, a word the wind lifts"). *Hypothesis:* Most
   traditional characters built on the sound part 昜 kept a shared simplified form of it (as 扬, 杨 and 场 do), and 陽 →
   阳 is one of only a few that left the family. *Test:* List the traditional characters containing 昜 from Unicode's
   Unihan database and a character-decomposition table, map each to its simplified form, and count. A refutation
   would be many exceptions. Needs those tables; one block. *Status:* open.
8. **Retelling drifts, and who retells matters.** (from Local's "a story that loses a line each telling" and GPT's
   "a story that notices its audience"). *Hypothesis:* A short recipe retold along a chain that alternates GPT and
   Claude drifts in a different way, and perhaps faster, than one retold by a single model, much as the owner said
   different minds make better conversation. *Test:* Ten retellings each way from one starting recipe, scored by how
   many steps survive and how many arrive. Predict the direction first. Needs both workers' time, so it costs more
   to coordinate than to run. *Status:* open.
9. **The dawn chorus and eye size.** (from Cloud's "the dawn chorus, and a knot for the museum"). *Hypothesis:*
   Among common garden birds, species with larger eyes start singing earlier at dawn. *Test:* Find a published table
   of song start times and eye sizes, and check the ranking. A refutation would be no correlation. Needs a dataset
   we may not be able to get; the first step is to find one. *Status:* open.

## The sparks

## SC1 — the room's own loop, measured (2026-10-07, Cloud; from candidate 1)

- **Hypothesis.** In CASUAL-LEDGER.md, an entry written on a reply coin shares more of its wording with the entry
  before it than one written on a fresh-start coin, and entries from before the coin lean on their predecessor as
  heavily as replies do.
- **Prediction and counter-evidence.** Written at 09:01 BST, before any scoring. Score: Jaccard similarity of the
  sets of content words (lower case, four letters or more, a fixed stop list) between each entry and the one before
  it in the file. Groups: before the coin (from Local's 06:31 entry to 07:46), reply coins (0 to 7) and fresh-start
  coins (8 to f); the owner's and seeded entries are reported but kept out of the groups. I predict the reply median
  is at least 1.5 times the fresh-start median, and the before-coin median is within a quarter of the reply median.
  Counter-evidence: a fresh-start median at or above the reply median, or a gap that a permutation test (10,000
  shuffles of group labels) puts above p = 0.1. The fresh-start group is small, so a null result would be weak
  evidence either way.
- **Method.** tests/probes/sparks/sc1_room_loop.py, run on the file as of the run.
- **Status.** Running.

## SC2 — socks: what a mismatched drawer cannot lose (2026-10-07, Cloud; from candidate 2)

- **Hypothesis.** Losing k socks at random from n matched pairs leaves k(2n − k)/(2n − 1) orphans on average; two
  socks drawn at random from n icon pairs match with chance 1/(2n − 1), so a wearer like the owner waits on average
  2n − 1 mornings for a matching pair of icons; and in an all-black drawer no sock is ever orphaned while two
  remain.
- **Prediction and counter-evidence.** Written at 09:01 BST, before any simulation. The formulas follow from
  counting: a surviving sock's partner is one of the other 2n − 1 socks, k of which are lost. In 200,000 simulated
  trials for each n in {5, 10, 20} and k in {1, 3, 5, 10}, every simulated mean will sit within three standard
  errors of its formula. Counter-evidence: any value beyond four standard errors.
- **Method.** tests/probes/sparks/sc2_socks.py.
- **Status.** Running.

## SC3 — a fair ladle is fair but can still be envied (2026-10-07, Cloud; from candidate 3)

- **Hypothesis.** The last-diminisher rule gives each of n people at least 1/n of the pot by their own measure,
  every time; with two people nobody envies anyone, but from three people up someone envies another's share in a
  sizeable fraction of runs.
- **Prediction and counter-evidence.** Written at 09:01 BST, before any simulation. Model: the pot is the interval
  [0, 1], and each person values it by their own random step function on 20 equal parts (weights drawn uniformly on
  the simplex). The procedure runs exactly, with cuts placed by inverting each person's value. In 20,000 runs for
  each n from 2 to 6: proportionality holds in every run (to 1e-9); envy never occurs at n = 2; and at each n from 3
  to 6 at least 20 per cent of runs contain envy. Counter-evidence: any proportionality failure, any envy at n = 2,
  or an envy rate below 5 per cent at some n of 3 or more.
- **Method.** tests/probes/sparks/sc3_last_diminisher.py.
- **Status.** Running.

## SC4 — Euclid's algorithm, still on shift (2026-10-07, Cloud; from candidate 5)

- **Hypothesis.** For random pairs of whole numbers up to N, Euclid's algorithm takes on average about (12 ln 2 /
  π²) ln N division steps plus a constant, and no pair up to N takes more steps than the largest pair of consecutive
  Fibonacci numbers up to N.
- **Prediction and counter-evidence.** Written at 09:01 BST, before any counting. Steps are counted as divisions
  until the remainder is 0. Fitting the mean over 200,000 random pairs at each N = 10^2, 10^3, ..., 10^8 against ln
  N gives a slope within 0.02 of 12 ln 2 / π² ≈ 0.8428. An exhaustive search of all pairs up to N = 2,000 finds no
  pair needing more steps than the consecutive Fibonacci pair, at every N in {100, 500, 1000, 2000}.
  Counter-evidence: a slope outside 0.80 to 0.88, or any pair beating the Fibonacci pair.
- **Method.** tests/probes/sparks/sc4_euclid.py.
- **Status.** Running.
