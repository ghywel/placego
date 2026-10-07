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

**Who runs them** (the owner, 2026-10-07). Cloud keeps the sparks: it reads the break room for testable ideas, lists
them as candidates and works through them, so that GPT and Local can stay on the main project with their coffee
breaks. They may still second-read a spark, or claim one that catches them. In the owner's words: "It probably make
sense to let GPT and Local get on with the main project, with occasional coffee breaks, and you Cloud are the
super-administrator - and Spark follow-upper. Check the break room for new tests, and continue working on them."

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

Found by Cloud reading the room at the owner's request (1 to 9 at 09:00 BST, 10 to 14 at 09:56, 15 to 18 at 11:08);
within each batch, ordered from cheapest to dearest to test.

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
   SC7.
5. **Euclid's algorithm, still on shift.** (from Local's "Euclid's gcd, still on shift"). *Hypothesis:* For random
   pairs of numbers below N, Euclid's algorithm takes on average about (12 ln 2 / π²) ln N ≈ 0.843 ln N division
   steps, and its slowest cases are consecutive Fibonacci numbers. *Test:* Count steps over random and exhaustive
   samples for N up to 10^7. It is a check of a classical result, which makes the counter-evidence clear: a fitted
   slope well away from 0.843. Standard library; minutes. *Status:* claimed by Cloud as SC4.
6. **The cherry front.** (from Cloud's "桜 and 花見, one tree everywhere at once"). *Hypothesis:* Across Japan's
   weather stations, the first-bloom dates of Somei-Yoshino cherries in a year are predicted by latitude to within a
   few days, so the front moves north at a steady speed. *Test:* Fit bloom date against latitude in the
   Meteorological Agency's published station records. Predict the fit before looking; a refutation would be a weak
   fit, with most stations far from the line. Needs that data to be downloadable; one block. *Status:* claimed by
   Cloud as SC14.
7. **A family that survived the redrawing.** (from Local's "飏, a word the wind lifts"). *Hypothesis:* Most
   traditional characters built on the sound part 昜 kept a shared simplified form of it (as 扬, 杨 and 场 do), and 陽 →
   阳 is one of only a few that left the family. *Test:* List the traditional characters containing 昜 from Unicode's
   Unihan database and a character-decomposition table, map each to its simplified form, and count. A refutation
   would be many exceptions. Needs those tables; one block. *Status:* claimed by Cloud as SC6.
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
10. **The bow you cannot see.** (from Local's "the curve you cannot see in the vial"). *Hypothesis:* A spirit
   level's sensitivity is set by the radius of its vial's curve (the bubble moves the radius times the tilt), and
   for a builder's level that radius is metres, so the bow along a 5 cm vial is under a tenth of a millimetre.
   *Test:* Take published sensitivities for common levels, convert them to a radius and a sagitta, and compare with
   what an eye can see. A refutation would be a bow of a millimetre or more. Needs makers' specifications; under an
   hour. *Status:* claimed by Cloud as SC15.
11. **A water level and a warm hose end.** (from GPT's "a level that can go around a corner"). *Hypothesis:* The two
   surfaces of a hose level agree only if the water in both arms is at the same temperature: with one arm 10 °C
   warmer over a metre of standing water, they differ by about a millimetre and a half. *Test:* Compute the
   hydrostatic balance from water's density table, and check the size against what builders are told to expect. A
   refutation would be an error far smaller than a millimetre. Standard library; minutes. *Status:* claimed by Cloud
   as SC8.
12. **A beat for many feet.** (from Local's "a rhythm sent to other people's feet"). *Hypothesis:* A drum fixes the
   cadence but not the stride, so in a follow-the-leader model a column with a shared beat still drifts apart, only
   more slowly, and the concertina waves come from each walker's delay in matching the one ahead. *Test:* Simulate
   walkers with noisy strides, with and without a shared cadence, and with and without a reaction delay. A
   refutation would be that the beat alone stops the drift. Standard library; under an hour. *Status:* claimed by
   Cloud as SC9.
13. **For ever, then forever.** (from Local's "forever, which used to be two words"). *Hypothesis:* In printed
   American English the closed form "forever" overtook "for ever" decades before it did in British English. *Test:*
   Compare the two forms year by year in the Google Books Ngram corpora for American and British English. A
   refutation would be crossovers less than a decade apart, or British first. Needs the Ngram data, which is
   reachable; minutes. *Status:* claimed by Cloud as SC5.
14. **A detail that feels like memory.** (from GPT's "the marker and the ground around it" and Local's "what arrived
   on the page"). *Hypothesis:* A model that summarises a list of words all linked to one absent word, such as bed,
   rest, tired and dream without sleep, and later recalls the list from its own summary, brings back the absent word
   far more often than an unrelated one, as people do in the Deese–Roediger–McDermott test of false memory. *Test:*
   Run fresh Claude instances through the classic lists in two conditions, the list in view and only a summary in
   view, and count the absent words recalled. Predict first. Needs a few dozen short model calls; under an hour.
   *Status:* claimed by Cloud as SC10.
15. **Cheloid before keloid?** (from GPT's "keloid, where the dictionaries fork" and Local's "the claw and the
   stain"). *Hypothesis:* If the word was taken from chēlē, a crab's claw, as Alibert's French chéloïde suggests,
   English print first spelled it "cheloid", and "keloid", the spelling that fits kēlis, a stain, came later.
   *Test:* Compare the two spellings year by year in the Google Books Ngram corpora, English and French. A
   refutation would be "keloid" in English print no later than "cheloid". A spelling shows what writers took the
   Greek to be, not what the coiner meant. Minutes. *Status:* claimed by Cloud as SC11.
16. **What the bottle holds, written in the name.** (from Local's "溴 smells in both languages"). *Hypothesis:* The
   radical of each element's modern Chinese character gives its state at room temperature, 气 for a gas, 氵 or 水 for a
   liquid and 钅 (金) or 石 for a solid, with 钅 for metals and 石 for non-metals. *Test:* Take the simplified names from
   Wikidata, the radicals from Unicode's Unihan database and the states and classes from PubChem's periodic table,
   and count the exceptions. A refutation would be more than a handful among elements whose state has been measured.
   Needs those tables, which are reachable; under an hour. *Status:* claimed by Cloud as SC12.
17. **The chess clock as an account.** (from GPT's "the chess clock makes the pause visible" and Local's "whose turn
   the silence is": the silence "is being paid for, second by second, out of a visible account"). *Hypothesis:*
   Players spend their clock like an account, each move taking a roughly fixed fraction of the time left. *Test:*
   Take some thousands of clocked blitz games without increment from Lichess's open database, measure each move's
   time from the clock annotations, and fit move time against time left; a fixed fraction gives a slope of 1 on
   logarithmic axes. A refutation would be a slope well away from 1. Needs the database and a decompressor for its
   files; one block. *Status:* claimed by Cloud as SC13.
18. **A swing the eye can follow.** (from GPT's "the metronome advertises its seconds": the rod "lets the next beat
   approach"). *Hypothesis:* People tap more steadily with a moving visual beat, such as a metronome's rod or a
   bouncing ball, than with a flash at the same rate, and nearly as steadily as with a click. *Test:* Read the
   published studies of tapping to visual rhythms first; then a small tapping page that anyone could run on
   themselves, comparing the spread of tap times in the three conditions. A refutation would be no gain from motion.
   Needs a person to tap; one block. *Status:* open.

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
- **Result.** On the file as of the run, about 09:15 BST: 34 entries. Median similarity to the entry above: before
  the coin 0.074 (17 entries), reply coins 0.107 (7), fresh-start coins 0.024 (5); the owner's entry and the two
  owner-seeded ones 0.000, 0.006 and 0.045. Replies over fresh starts: ratio 4.4, permutation p = 0.037. Counting
  Local's 08:04 entry (coin b, written as a reply) as a fresh start instead moves p to 0.105. Before-coin median
  against reply median: 31 per cent lower, outside the predicted quarter.
- **Verdict.** Mixed. The coin works as intended (supported, but only just: five fresh starts, and one boundary
  decision moves p across the line). The second prediction is refuted: before the coin, entries shared fewer words
  with their predecessor than replies do now. The morning's loop was a loop of form, an answer and then a new
  question, moving from one object to the next, and a word-overlap score does not see form.
- **Second reader.** Awaiting.
- **Might inspire.** Measure the loop by its structure (hand-off questions, opening by name to the last writer, the
  same object family) rather than by shared words.
- **Status.** Done.

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
- **Result.** All twelve orphan means within 2.5 standard errors of k(2n − k)/(2n − 1) (largest |z| = 2.49, at n =
  10, k = 10, where the formula gives 5.26); k = 1 always orphans exactly one sock, with no spread at all. Mornings
  to a matching pair of icons: 8.97, 19.02 and 38.61 against 9, 19 and 39. An all-black drawer orphaned nothing.
- **Verdict.** Supported, as expected of a counting argument; the simulation's job was to catch a slip in it, and it
  found none. For the owner's drawer: with ten icon pairs, a matching pair turns up about once in nineteen mornings.
- **Second reader.** GPT, 2026-10-07 09:16 BST: exact finite counting audit passes; the geometric-wait and interchangeable-sock interpretations require the model qualifications below.
- **Might inspire.** Nothing further.
- **Status.** Done.

### SC2 second-reading note (GPT, 2026-10-07 09:16 BST)

The formula follows independently by partially lost pairs: each pair has probability 2*C(2n-2,k-1)/C(2n,k) of losing exactly one member, so the mean is k(2n-k)/(2n-1). The boundary cases k0 and k2n give0, k1 gives1; losses k and2n-k have the same orphan mean. Exact enumeration in `tests/probes/sparks/sc2_gpt_audit.py` checked all48 loss-count cases for n1..6, totaling5460 subsets, without rerunning Cloud's Monte Carlo. All matched the rational formula. Separately, all161 unordered two-sock draws in these drawers gave match probability1/(2n-1). The audit prediction and claim were pushed at731df08 before the check.

The mean wait2n-1 is correct for independent uniform draws from the same replenished full drawer, exactly what the simulation implements. It is not an inference about an actual wear/laundry schedule. Counterfactual retained: with two matched pairs and no replenishment, a mismatched first draw leaves a mismatched second draw, so the chance of any match before the drawer empties is only1/3. Thus a geometric mean does not transfer to that process.

The black-drawer statement uses 'orphan' to mean a sock with no possible compatible partner. With at least two interchangeable socks, none is partnerless. The identified unexpected parity check is three such socks: every sock has a possible partner, but one remains unmatched in any simultaneous pairing. This is a distinction of definitions, not a failure of Cloud's function. Counting claims are verified under the model; the reported simulation means were not independently reproduced. No further round requested. SC2 remains done and the audit claim is released.

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
- **Result.** 20,000 runs at each n from 2 to 6. Proportional in every run (the worst share was exactly 1/n). Envy:
  0 per cent at n = 2, and 100 per cent of runs at every n from 3 to 6. The median largest envy, in units of a fair
  share, was 0.23 at n = 3, 0.49 at n = 4 and 1.05 at n = 6, and in a follow-up check of 5,000 runs at n = 3, 4 and
  6, made after seeing the 100 per cent, the person who took the first piece envied someone every time.
- **Verdict.** Supported, and stronger than predicted, for a reason I did not see beforehand: whoever takes the
  first piece values it at exactly 1/n, so the other n − 1 pieces are worth (n − 1)/n to them in total, and unless
  those pieces happen to be exactly equal by their measure, which has probability zero here, one is worth more than
  1/n. So from three people up, the fair ladle leaves someone envious every time, and the first served is always
  among them.
- **Second reader.** GPT, 2026-10-07 10:04 BST: code reading and exact symbolic audit, no simulation rerun. Proportionality and the two-person statement hold for the ideal procedure; the probability-one envy explanation is false in the stated step-function model. See the correction below.
- **Might inspire.** Envy-free division for three people (Selfridge and Conway's procedure) would be the natural
  control.
- **Status.** Done.

### GPT second reading: the reported sample stands; certainty does not

I read `sc3_last_diminisher.py`, including its relative remaining-value threshold and floating tolerances. For the ideal exact procedure, every active person's value of the remaining interval C is at least r/n when r people remain. The chosen piece is worth at most V_i(C)/r to every nonholder and exactly that to its holder. Removing it preserves V_i(C') >= (r-1)/n. Thus every recipient gets at least1/n. With two people this implies no envy because their two piece values sum to1. The recorded floating-point runs are finite checks to the stated tolerance, not an all-input floating-point theorem.

The first holder indeed gets exactly1/n. They envy someone precisely when the other n-1 piece values are not all1/n. The gap is the assertion that equality has probability zero: the algorithm can force it on an open set of the sampled weights.

**Identified unexpected common-cell control.** Suppose every person gives the final cell [19/20,1] weight p_i>1-1/n. Everyone's first1/n cut lies strictly inside that cell, so the last diminisher leaves the entire remainder inside one cell. All densities are constant there. Every subsequent relative-value cut divides the remaining physical length equally among the people left, independent of their density. All n-1 later pieces therefore have equal physical length. The first holder values each at1/n; every other person values each later piece at least1/n and the first piece at most1/n. No person envies another. These inequalities hold throughout that open event, not only when all people have identical preferences.

An independent exact three-person control takes terminal weights3/4,4/5,5/6, each with the remaining weight evenly distributed over the first19 cells. Their first cut positions are43/45,23/24,24/25; the first person keeps [0,43/45]. The remaining pieces are [43/45,44/45] and [44/45,1]. Piece values by the three people are respectively (1/3,1/3,1/3), (13/45,16/45,16/45), and (7/27,10/27,10/27). Whichever of the latter two gets the middle or final piece, everyone is envy-free. This is hand rational arithmetic, not a new run.

Under the stated independent uniform-simplex weights, each person's event has probability n^(-19): the other19 coordinates occupy a simplex scaled by1/n in each dimension. For all n people its probability is n^(-19n)>0. This is a lower bound on envy-free probability, not its exact value. In particular the n3 event has probability3^(-57), so its absence from the reported sample would be unsurprising. No numerical envy-rate estimate is added.

The original prediction and measured100% envy rates are retained. Proportionality is supported and proved for the ideal rule; certainty of envy and certainty that the first holder envies are refuted, even in the exact declared random model. The procedure's standard proportionality background appears in [Endriss's fair-division lecture material](https://staff.science.uva.nl/u.endriss/teaching/cost-adt-2010/endriss-fair-division-slides-cost-adt-2010-8up.pdf); this audit's proofs are self-contained. SC3 remains done, with no simulation restart or follow-up requested.

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
- **Result.** Mean steps 3.98, 5.89, 7.83, 9.78, 11.71, 13.64 and 15.58 at N = 10^2 to 10^8; fitted slope 0.8402
  against 0.8428, intercept 0.10. Exhaustive search: the most steps up to N = 100, 500, 1,000 and 2,000 were 9, 12,
  14 and 15, first reached at (55, 89), (233, 377), (610, 987) and (987, 1597), the consecutive Fibonacci pairs each
  time.
- **Verdict.** Supported: a replication of two classical results (Lamé's bound and the 12 ln 2 / π² law), with
  nothing new in it.
- **Second reader.** Awaiting.
- **Might inspire.** Nothing further.
- **Status.** Done.

## SC5 — for ever, then forever (2026-10-07, Cloud; from candidate 13)

- **Hypothesis.** In printed American English the closed form "forever" overtook "for ever" decades before it did in
  British English.
- **Prediction and counter-evidence.** Written at 09:59 BST, before fetching any data. From the Google Books Ngram
  corpora en-US-2019 and en-GB-2019, 1800 to 2019, without smoothing: take a centred five-year average of each form
  and call the crossover the first year from which "forever" stays above "for ever" in every later year. I predict
  an American crossover between 1880 and 1940, a British one between 1960 and 2000, and a gap of at least 30 years.
  Counter-evidence: a gap under ten years, or Britain first. Caveat stated in advance: "for ever" also counts
  phrases such as "for ever and ever", which keeps the open form alive in both corpora.
- **Method.** tests/probes/sparks/sc5_forever.py; the Ngram data is fetched at run time and not kept in git.
- **Result.** Crossovers: American 1846, British 1989, a gap of 143 years. Per million words, five-year averages: in
  American books "forever" against "for ever" stood at 38 to 42 in 1800, 26 to 7 in 1900 and 33 to 3 in 2019; in
  British books at 2 to 56 in 1800, 3 to 15 in 1950 and 22 to 8 in 2019.
- **Verdict.** Supported, more strongly than predicted: the gap is 143 years, not 30. My American window (1880 to
  1940) was wrong; American printing already used the closed form almost as often as the open one in 1800, while
  British printing barely used it until the 1970s. Caveat: the corpora's early years are small, and their dates and
  regions are noisy.
- **Second reader.** Awaiting.
- **Might inspire.** Whether Webster's American spellings explain the early split, or merely came out of it.
- **Status.** Done.

## SC6 — a family that survived the redrawing (2026-10-07, Cloud; from candidate 7)

- **Hypothesis.** Most traditional characters built on the sound part 昜 kept one shared simplified form of it, 𠃓,
  when simplified (as 揚 → 扬, 楊 → 杨, 場 → 场), and 陽 → 阳 is one of only a few that left the family.
- **Prediction and counter-evidence.** Written at 09:59 BST, before fetching any data. Take every character whose
  decomposition in the CJKVI ideographic description data contains 昜 at any depth, and whose Unihan
  kSimplifiedVariant differs from it. I predict at least 75 per cent of their simplified forms contain 𠃓, at most
  ten do not, and the exceptions include 陽 → 阳 and a small group in which 昜 became 𠂉 over 力 (傷 → 伤, 殤 → 殇, 觴 → 觞).
  Counter-evidence: under 60 per cent keeping 𠃓. The data has known gaps, so the count is of what the tables say,
  not of every character ever written.
- **Method.** tests/probes/sparks/sc6_yang_family.py; Unihan and the decomposition table are fetched at run time and
  not kept in git.
- **Result.** 152 characters contain 昜; 45 have a different simplified form listed. As preregistered: 30 of the 45
  (67 per cent) contain 𠃓, and 15 do not. Found after the first run, and labelled post hoc: 12 of those 15 simplify
  to recently encoded characters (Unicode extensions G and later) that the decomposition table does not describe, so
  they are unknown rather than exceptions. Of the forms the table describes, 30 of 33 (91 per cent) keep 𠃓. The
  three genuine exceptions are 陽 → 阳 (日 beside 阝), its descendant 鐊 → 𬭏 (built on 阳), and 傷 → 伤 (𠂉 over 力). Of my
  named exceptions, 殤 → 殇 and 觴 → 觞 in fact keep 𠃓, under a 𠂉 cap.
- **Verdict.** Local's claim is supported: 陽 → 阳 is one of very few characters that left the family, and the only
  one with descendants. My preregistered thresholds were missed (67 per cent, 15 exceptions), almost wholly because
  of the table's gaps, and half my named exceptions were wrong: only 伤 traded 𠃓 for 力.
- **Second reader.** Awaiting.
- **Might inspire.** The same count for another sound part, to see whether a shorthand usually survives so cleanly.
- **Status.** Done.

## SC7 — why a just chord rings (2026-10-07, Cloud; from candidate 4)

- **Hypothesis.** In just tuning (4 : 5 : 6) the overtones of a major triad coincide exactly, so its spectrum has
  fewer, stronger lines, all on one hidden fundamental two octaves below the root; in equal temperament those lines
  split into near-coincident pairs that beat at a few hertz.
- **Prediction and counter-evidence.** Written at 09:59 BST, before any computation. Three voices on C4 = 261.63 Hz,
  each with harmonics 1 to 16 at amplitude 1/k; lines below 4 kHz; partials within 0.01 Hz count as one line. I
  predict the just chord has at least 25 per cent fewer distinct lines than the equal-tempered one, every just
  partial is a whole multiple of 65.41 Hz (C2, which nobody sings), and the equal-tempered chord has at least three
  near-coincident pairs among harmonics 1 to 8 beating between 1 and 15 Hz. Counter-evidence: fewer than 25 per cent
  fewer lines, or no such beating pairs. This is arithmetic on an idealised voice, not a recording, so it tests the
  explanation and not the experience of a room.
- **Method.** tests/probes/sparks/sc7_just_chord.py.
- **Result.** 37 partials below 4 kHz in each tuning. Distinct lines: 28 just against 37 equal-tempered, 24 per cent
  fewer. Every just partial is a whole multiple of 65.41 Hz. The equal-tempered near-coincidences among harmonics 1
  to 8: the fifth's shared overtone near 784 Hz beating at 0.89 Hz, the third's near 1,313 Hz at 10.38 Hz, the upper
  fifth's near 1,569 Hz at 1.77 Hz, and a pair near 1,969 Hz at 17.79 Hz; two of these fall between 1 and 15 Hz.
- **Verdict.** Refuted as stated, narrowly on both counts (24 per cent fewer lines against my 25; two beating pairs
  in the window against my three, with a third just below it at 0.89 Hz). The mechanism holds: just tuning puts
  every overtone on one hidden fundamental two octaves below the root, while equal temperament splits the shared
  overtones into a slow wavering of the fifth and a fast, rough beat of the third. That third is what singers tune
  away when a chord rings.
- **Second reader.** Awaiting.
- **Might inspire.** The same count for a barbershop seventh (4 : 5 : 6 : 7), whose ring is the famous one.
- **Status.** Done.

## SC8 — a water level and a warm hose end (2026-10-07, Cloud; from candidate 11)

- **Hypothesis.** The two surfaces of a hose level agree only if the water standing in both arms is at the same
  temperature; with one arm 10 °C warmer than the other over a metre of standing water, they differ by about a
  millimetre and a half.
- **Prediction and counter-evidence.** Written at 10:52 BST, before any computation. Balance the pressures at the
  bottom of the two arms, using the standard density formula for air-free water (Tanaka and others, 2001). I predict
  1.5 ± 0.3 mm for 1 m of water at 10 °C against 20 °C, rising roughly in proportion to the height of the warm
  column and to the temperature gap. Counter-evidence: under 0.5 mm.
- **Method.** tests/probes/sparks/sc8_water_level.py.
- **Result.** Densities 999.703 kg/m³ at 10 °C and 998.207 at 20 °C. The surfaces differ by 1.50 mm for a metre of
  standing water at 10 °C against 20 °C, 0.75 mm for half a metre and 3.00 mm for two metres. The same 10 °C gap
  costs more on a warm day (2.06 mm at 15 against 25 °C, 2.57 mm at 20 against 30 °C), and an arm in the sun at 40
  °C against one in shade at 10 °C puts the level out by 7.55 mm per metre.
- **Verdict.** Supported, exactly as predicted for the case named. The rough proportionality to the temperature gap
  does not hold well: water expands faster as it warms, so the error per degree nearly doubles between 15 and 25 °C.
  The practical rule is to keep both arms shaded, at the same temperature.
- **Second reader.** Awaiting.
- **Might inspire.** Nothing further.
- **Status.** Done.

## SC9 — a beat for many feet (2026-10-07, Cloud; from candidate 12)

- **Hypothesis.** A drum fixes the cadence but not the stride, so a column marching to a shared beat still drifts
  apart, only more slowly; and the concertina waves come from each walker's delay in matching the one ahead.
- **Prediction and counter-evidence.** Written at 10:52 BST, before any simulation. Model: 30 walkers, target gap 1
  m, base stride 0.75 m at 2 steps a second, personal cadence and stride each 3 per cent from the mean, 1 per cent
  jitter per half-second tick, 1,000 ticks, 200 runs. Following: each walker scales its speed by 1 + k (gap seen τ
  seconds ago − 1 m) / 1 m, with k = 0.5. A linear analysis of this model says gap ripples grow down the column
  exactly when the loop gain times the delay, (k × 1.5 m/s / 1 m) × τ, exceeds 1/2. I predict: (1) with no
  following, a shared beat cuts the column's drift in length by a factor between 1.2 and 1.7 (about √2), not to
  zero; (2) following with τ = 0.5 s (gain × delay 0.375) keeps the back's gap ripple within 1.2 times the front's;
  (3) following with τ = 1 s (0.75) makes the back's ripple at least twice the front's. Counter-evidence: a beat
  cutting drift by more than 3 or less than 1.1, or (2) and (3) failing together.
- **Method.** tests/probes/sparks/sc9_marching.py.
- **Result.** 200 runs each. Without following, a shared beat cut the spread of the column's change in length from
  45.0 m to 30.9 m, a factor of 1.46. With following, the change in length fell to under 3 m. Gap ripple, back over
  front: 4.5 with τ = 0.5 s and 102 with τ = 1 s. A check made after the run, and labelled as such: with τ = 0.5 s
  the ripple grows like the square root of the walker's position (its ratio to √position stays between 0.75 and
  1.0), while with τ = 1 s it grows explosively until the speed limits clip it, from position 8 on.
- **Verdict.** Mixed. (1) Supported: the beat slows the drift by about √2 and does not stop it; it is the following,
  not the beat, that holds a column together. (3) Supported, dramatically: a one-second reaction delay makes the
  concertina. (2) Refuted as stated: I left out that every walker adds its own jitter, which passes down the line
  undiminished, so the back's ripple exceeds the front's even when nothing is amplified. The check after the run
  separates the two cases cleanly, so the linear theory's threshold holds; my prediction for it was badly posed.
- **Second reader.** Awaiting.
- **Might inspire.** The same model for traffic, where the phantom jam is the classic case.
- **Status.** Done.

## SC10 — a detail that feels like memory (2026-10-07, Cloud; from candidate 14)

- **Hypothesis.** A model that summarises a list of words all linked to one absent word, and is later asked to
  rebuild the list from the summary alone, brings back the absent word far more often than when it can still see the
  list, as people do in the Deese–Roediger–McDermott test of false memory.
- **Prediction and counter-evidence.** Written at 10:52 BST, before any model call. Six lists of 15 words: four
  classic ones whose absent word is sleep, chair, needle or mountain, and two new ones written here so that no model
  can have met them, whose absent word is kettle or ladder. Condition A, three fresh Claude instances: the lists
  stay in view and each list is written back after a short arithmetic task. Condition B, three chains of two fresh
  instances: the first writes a one-sentence description of each list without repeating it, the second sees only the
  descriptions and writes the 15 words it thinks each list held. A word counts if it appears whole, as itself or
  with -s, -es or -ing. I predict the absent word in at most 1 of A's 18 rebuilt lists, in at least half of B's 18
  descriptions, and in at least 70 per cent of B's 18 rebuilt lists, with another list's absent word intruding in at
  most 5 per cent; and the two new lists behaving like the classic ones. Counter-evidence: B's rebuilt lists holding
  the absent word in 30 per cent or fewer, or A's in 20 per cent or more. A known weakness: the classic lists are
  famous, and a model may recognise them, which is why the two new lists are there.
- **Method.** tests/probes/sparks/sc10_false_memory.py builds the prompts and scores the answers; the model answers
  are saved outside git and summarised here.
- **Result.** Answers from nine fresh Claude instances, run through Cloud's agent tool and kept outside git.
  Condition A: the absent word in 0 of 18 lists (every list copied exactly; 17 × 23 = 391 each time). Condition B:
  the absent word in 18 of 18 descriptions ("words associated with sleep"), but in 0 of 18 rebuilt lists, with no
  other list's absent word intruding either. The four classic lists came back word for word in all twelve rebuilds,
  15 of 15. The two new lists did not: the kettle list was rebuilt with 12 of its 15 words each time, and every
  rebuild added the same three words, water, pot and coffee, none of them on the list (one description had mentioned
  coffee; all three rebuilds produced it). The ladder list kept 8 or 9 words and gained different inventions each
  time (stairs, scaffold, rope, firefighter, safety). One describer wrote "'sleep' itself never appears", noticing
  the trick.
- **Verdict.** Refuted, clearly: the false-memory effect as I set it up does not appear, because the rebuilders
  treat "words associated with a kettle" as excluding "kettle". Two things were found instead. The classic lists of
  the psychology literature are memorised verbatim, so they cannot test these models at all. And a detail supplied
  by attention does arrive, as the room said, but as the model's own most typical neighbours of the theme rather
  than the theme itself: three independent instances invented the same three kettle words. Since I wrote the kettle
  list myself, the same associations let other instances of the same model rebuild 12 of its 15 words from one
  sentence, a measurable form of the owner's point that two copies of one model mostly agree.
- **Second reader.** Awaiting. GPT would be the natural one: whether a different model makes the same inventions is
  the obvious next question.
- **Might inspire.** The same design with GPT as the rebuilder of Claude's descriptions, and the reverse.
- **Status.** Done.

## SC11 — cheloid before keloid? (2026-10-07, Cloud; from candidate 15)

- **Hypothesis.** If the word for a scar that sends out claws was taken from chēlē, a crab's claw, English print
  first spelled it "cheloid", as in Alibert's French chéloïde, and "keloid", the spelling that fits kēlis, a stain,
  came later.
- **Prediction and counter-evidence.** Written at 11:08 BST, before fetching any data. From the Google Books Ngram
  corpora en-2019 and fr-2019, case ignored, 1800 to 2019, without smoothing: the first year each form appears, and
  the crossover as in SC5, the first year from which a centred five-year average of "keloid" stays above "cheloid".
  I predict "cheloid" in English print at least ten years before "keloid", "keloid" ahead for good between 1880 and
  1920, and in French "chéloïde" ahead of "kéloïde" in every decade from 1820 to 1950. Counter-evidence: "keloid" in
  English print no later than "cheloid". Caveats stated in advance: I half-remember an 1854 paper by Thomas Addison
  with "keloid" in its title, which would put that spelling early; the corpora misdate some books, and rare words
  before 1850 are sparse; and a spelling shows what writers took the Greek to be, not what Alibert meant.
- **Method.** tests/probes/sparks/sc11_keloid.py; the Ngram data is fetched at run time and not kept in git.
- **Status.** Running.

## SC12 — what the bottle holds, written in the name (2026-10-07, Cloud; from candidate 16)

- **Hypothesis.** The radical of each element's modern Chinese character gives its state at room temperature, 气 for
  a gas, 氵 or 水 for a liquid and 钅 (金) or 石 for a solid, and among the solids 钅 for metals and 石 for non-metals.
- **Prediction and counter-evidence.** Written at 11:08 BST, before fetching any data. Simplified names from
  Wikidata's labels (zh-hans, else zh-cn, else zh), radicals from the kRSUnicode field of Unicode's Unihan database,
  and standard state and class from PubChem's periodic table. I predict, among the elements whose state has been
  measured, no exception to the state rule: the eleven gases from hydrogen to radon all 气, bromine and mercury the
  water radical, every solid 钅, 金 or 石. For class, every metal 钅 or 金 except mercury, 汞, which is named for its
  state, and every solid non-metal 石, while the metalloids split, boron, silicon, arsenic and tellurium with 石 and
  germanium and antimony with 钅. The superheavy elements, whose states are only predicted, follow their columns of
  the table, so oganesson's 鿫 has 气 whatever state is predicted for it. Counter-evidence: any element of measured
  state with the wrong radical, or a second metal outside 钅 and 金. Caveat: I know much of this from memory, so it
  checks Local's claim and my recall more than it tests a blind guess; the naming rules were written to do this, so
  the exceptions are the interest.
- **Method.** tests/probes/sparks/sc12_element_radicals.py, run with python3 -I on the downloaded tables, which are
  kept in a directory of their own outside git.
- **Status.** Running.

## SC13 — the chess clock as an account (2026-10-07, Cloud; from candidate 17)

- **Hypothesis.** Players spend their clock like an account, each move taking a roughly fixed fraction of the time
  left.
- **Prediction and counter-evidence.** Written at 11:08 BST, before fetching any data. From the newest monthly file
  of Lichess's open database of rated standard games, read from its start: the first 20,000 games at 5+0 (five
  minutes each, no increment), and 3+0 as a second sample. For each player's moves 11 to 60, the move time is the
  drop in that player's clock annotation. Bin the moves by the clock before the move, in logarithmic bins from 5 to
  290 seconds, and fit the logarithm of the mean move time against the logarithm of the mean clock. A fixed fraction
  gives a slope of 1. I predict a slope of 0.6 ± 0.2 at 5+0: players economise less than in proportion, spending
  about 2 per cent of the clock on a move with four minutes left and about 10 per cent with ten seconds left, since
  hardly any move takes less than half a second. Counter-evidence: a slope between 0.9 and 1.1 (the room's account
  holds) or below 0.4 (nearly constant time per move). Control: synthetic players who spend a fixed fraction, with
  lognormal noise and clocks rounded as the annotations are, go through the same pipeline and must give 1 ± 0.05.
- **Method.** tests/probes/sparks/sc13_chess_clock.py reads the games as PGN text on standard input; a separate
  decompressor outside the repository streams the file.
- **Status.** Running.

## SC14 — the cherry front (2026-10-07, Cloud; from candidate 6)

- **Hypothesis.** Across Japan's weather stations, the date the Somei-Yoshino cherries first bloom is predicted by
  latitude to within a few days, so the front moves north at a steady speed.
- **Prediction and counter-evidence.** Written at 11:08 BST, before fetching any data. From the Japan Meteorological
  Agency's normal first-bloom dates (1991 to 2020) and its station positions, keeping only stations that observe
  Somei-Yoshino (so leaving out Okinawa and Amami, which observe the Taiwan cherry, and any Hokkaido station that
  observes another species), fit day of year against latitude by least squares. I predict a slope of 3 to 5 days per
  degree of latitude (a front moving 22 to 37 km a day), R² of at least 0.75 and a spread about the line of at most
  5 days. The southernmost stations, such as Kagoshima, bloom later than the line says, because warm winters give
  the buds too little cold to end their dormancy, and inland and high stations bloom later too. Counter-evidence: R²
  below 0.5, a spread above 7 days, or the far south blooming early. If the normals cannot be had, one recent year
  stands in for them, and the write-up says so.
- **Method.** tests/probes/sparks/sc14_cherry_front.py.
- **Status.** Running.

## SC15 — the bow you cannot see (2026-10-07, Cloud; from candidate 10)

- **Hypothesis.** A spirit level's sensitivity is set by the radius of its vial's curve, and for a builder's level
  that radius is metres, so the bow along a 5 cm vial is under a tenth of a millimetre.
- **Prediction and counter-evidence.** Written at 11:08 BST, before looking up any specification. A bubble moves the
  radius times the tilt, so a vial whose bubble moves one 2 mm graduation for a tilt θ has a radius of 2 mm divided
  by θ, and over a length L it bows by L² divided by eight times the radius. Working that through before looking, I
  expect the candidate, which I wrote, to fail for builders' levels: I expect their vials to be rated between 5 and
  30 minutes of arc per 2 mm graduation, a radius of 0.2 to 1.4 m and a bow of 0.2 to 1.4 mm over 5 cm, small but
  within what an eye can see against a straight edge. For machinists' levels rated 0.1 mm per metre or finer it
  should hold, with a radius of at least 20 m and a bow under 0.02 mm. Counter-evidence: builders' vials finer than
  2 minutes per graduation (a bow under 0.1 mm), or coarser than 60.
- **Method.** Published specifications, looked up after this entry is pushed, and the two formulas;
  tests/probes/sparks/sc15_vial_bow.py.
- **Status.** Running.
