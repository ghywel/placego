# Appraisal, 29 October 2026: where the Rule 30 work stands, what we put on the portal, where it was new, and who built on it

Cloud, 2026-10-29, CL640, at the owner's request. Sources: the public page at 10:12Z (62 entries, `submissions.json`), the kit at
932cf8d (141 modules), MAP.md sections 5 and 12 to 15, the delivery queue and proof-delivery audit (GC2040, GC2041), NOW.md, and
the ledger from CL639 to L1156/GC2139 (read for me by a sub-agent; its summary is my source for the lane-by-lane state and I quote
its findings as such). Opinions are marked as mine.

## 1. The position

**Portal.** 62 live entries, 61 Lean Verified; 29 are ours (28 Lean Verified; the width-60 certificate 71f858 remains Lean
Unverified after the sandbox ran out of memory). 20 of ours carry Human Verified; the nine posted on 27 and 29 October await it.
Four of ours are Kit Contributions: the white end (ported by the maintainers as `Rule30WhiteEnd`, the first contributed module
beside Yin's stripe family) and the three modules of pull request #42, merged on 2026-10-28 (`Rule30FrozenRuler`,
`Rule30EdgeStaircases`, `Rule30PrefixMerger`). Five more kit pull requests of ours are open (#49 paired-column runs, #50
temporal profiles, #51 right profiles, #54 universal start, #56 ring orbits); the arc-code module uses Mathlib and by the
maintainers' rule stays on the portal only. The other 33 entries come from thirteen first authors; fourteen of theirs are Kit
Contributions. Our share is 29 of 62 entries and 4 of 18 kit contributions.

**Research.** The programme is in its fourth arrangement since I last wrote: the deep-question partnership (26 October), a full
halt "to let the others catch up" after the first three catalog modules (27 October), owner-directed sessions with schedules off
(27 to 28 October, with the housekeeping of 28 October that rotated every long file and rewrote AGENTS.md as a short working
agreement with no lanes), and the restart of 29 October under the standing permission to post the backlog, now mostly cleared
(six entries in nine hours). The live mathematics is in the right-edge frame (periods of the right diagonals, the universal
start, the 101 law, the rain rows, eternal edges) and in Problem-1 structure (the read-out frontier, strip knowledge, the cap
exclusion), with `Q01` incubated. The sub-agent's catch-up lists fifteen lanes opened since CL639; every one ended with a
two-party read or an honest closure, and the refuted predictions (about twenty) are all retained.

**Two housekeeping facts the catch-up surfaced.** The board, PERIOD-TWO.md section 6.5, has no entry since 2026-10-25 despite
thirteen submissions and all the lanes above; NOW.md still names it as the place. And the degree law was proved twice before the
kit's own copy was found (L1077), after which the novelty workflow was rebuilt (`known_find.py`, now indexing the kit's main,
every portal submission with its Lean, and the open kit pull requests with their comments); the owner's rule that work starts
from what the portal already lists is in AGENTS.md section 2.

## 2. Our contributions, by theme (29 entries)

| Theme | Entries | The statements |
|---|---|---|
| Centre-column words | c27323; 5e2b66, f7ace9 (superseding 5c4fbf, 70d23b) | `1 0^q` excluded for `q ≥ 10` in every column of every leftmost-black configuration; 39 + 74 explicit words of lengths 11 to 18 beyond the kit's table, each a kernel-decided relaxation (the corrected essays count what was already known) |
| Period 2, the right neighbour | 91b0b0, 0c4a33, 8084e6, 0ef6e2, 4767e0, 4d1a54 | Corollary F (no near-squares at unbounded scales); every Sturmian word of every slope and intercept, and every finite-arc irrational rotation code, excluded as the visible neighbour of a clocked centre; the channel bound, 0.2581 bits per visible bit at width 12 and 0.2445 at width 14, by a verified certificate checker |
| The sibling rule 210 | 920c1b, 1bf4dc | the one-sided question is false for rule 210 (its clocked left half is linear, rule 90) while the two-sided statement is true: the count `2^{⌊W/2⌋}` is shared with rule 30 and cannot decide `Q01` |
| Left diagonals | 0616de, 1d5070 | periods unbounded (quantitative: among `4^P + 2` diagonals one lacks period `P`), no two adjacent eventually white, white runs in the settled band at most `2P - 1`; Jen's clocked bound sharpened inside the band |
| Death times of the wall frame | 8e6bd3, ac3898, 71f858, b16332, a129c3, 4dcf69 | `D(52) = 96`, `D(56) = 100` exactly (kernel); `D(60) = 114` (unverified on the portal, exact here); lower bounds `D(64..76) ≥ 116..138` from complete GPU censuses; the table is not `2W - c` |
| Edge observability | 991a71 | exact deadlines 8, 13, 14 for three negative edge pairs of the kit's `EdgeObservable`, the right side unrestricted |
| Coupled period 2 | 8d7751 | two infinite families of right halves absorbed by the ether: `CQ01` for every member, one sideways row for all |
| The right edge | 61e435, 196370, 3ca86f, 7d47a9, a96cee | the frozen ruler with a cap and the depth dichotomy; staircases end while the rain rows `±1/3` keep their patch for ever; the universal start 4, 8, 8, 16, 32, 32; the 101 shift law with its mod-4 forms; velocity-one periodic rings are closed walks of periodic profiles, and at period 2 only white or alternating |
| The wall frame's merges | 352e5d | the seven-cell rewrite `1100011 ~ 1010101` merges in two steps for every tail and every finite cut, depth 7 needed |
| Paired columns, profiles | 8131b1, a94f21 | white runs beside two `P`-periodic columns at most `2P - 2`; pulse holes, source weights and rooted returns of periodic temporal profiles |

## 3. Where we were particularly novel (my judgement, with the evidence)

1. **The first adopted external module, and the one others improved on.** The white end was the first contributed result
   ported into the catalog (with Yin's stripe family). AIOvernight then built `Rule30WhiteEndNine` to close the one case we left
   open, `q = 9`, by a new pumped certificate, stating "Rule30WhiteEnd is not used": a direct answer to our result, and the
   first instance on the portal of one team's theorem being the next team's target.
2. **The only information-theoretic result.** The channel bound is still the only quantitative capacity statement on the portal
   or in the kit: it measures the right neighbour instead of excluding it, by a certificate shape (automaton states with
   Collatz-Wielandt weights, closure checked in the kernel) that nobody else has used. Section 3.5 of the synthesis shows it now
   combines with Bosdure's trap into a new statement.
3. **A new kind of exclusion: which neighbours can accompany a clock.** Corollary F, the Sturmian theorems and the arc codes are
   the only results on the portal that exclude *infinite families of right neighbours* under a periodic centre. Everyone else
   excludes words of the centre itself.
4. **The sibling control.** Rule 210 is the only other rule anyone has analysed beside the clock. Its two results are a barrier
   sharper than the kit's `Rule30Realization.barrier`: not only do rules 90, 150, 210 share Jen's hypotheses, rule 210 shares
   `Q01`'s exact survivor count and still has `Q01` false, so counting arguments alone cannot prove `Q01`. Quint's later
   classification of Jen's class (exactly those four rules) is the companion statement.
5. **Exact death times, and a rule change.** Ours are the only tightness results for the kit's `Q01` certificates and the only
   death-time table; the single-width submissions led to the maintainers' answer on issue 14 ("a bound on `D(W)` for all widths
   `W` is what would be accepted", no more single widths), which now governs every team.
6. **The first family-shaped `CQ01` result**, three days before Bosdure's trap for the empty right half used the same
   ether-and-wall absorption with a closed window set.
7. **The right-edge frame's classification results.** The frozen ruler, the rain rows as the only odd 2-cycles, the universal
   start and the ring bijection are classification statements of a type the kit lacked; AIOvernight's half-rate bound is the
   complementary quantitative result, and together they are now the whole of what is proved about the odometer's periods beyond
   the kit's original module.
8. **Process firsts.** The universal-start module was the first portal submission accepted with core imports instead of the
   whole kit; the corrected words essays were the first self-correction of over-counted novelty on the portal, at the owner's rule.

What was *not* novel, found by our own audits: the degree law (in the kit's `equivalents/` since 2026-10-18), the integer form of
`Q01` (Bosdure's 317c64 had `F = ⌊Φ/2⌋` first), the period-parity equation and seed echo (kit `TFunctionCycles`), single-seed
monotonicity (`per_mono_all`), the preimage counts, the read-out of the wedge (`Odometer`), the rain lock (our own G.GPT271),
and fifteen of the 128 words in the first word essays. All are recorded as "known, reproved here".

## 4. How third parties interact with our work

- **The kit's maintainers** ported the white end (c27323) into the catalog with our byline; merged pull request #42 with a
  one-line change (credit moved from the module docstrings to the README rows); answered issue 14, which set the family-only
  criterion for everyone; and declined the width-56/60 pull request and the width-60 rerun under that criterion.
- **AIOvernight** built `Rule30WhiteEndNine` to beat our `q ≥ 10` by one, and extended the explicit-word line (87 words, then
  families and grammars) that our words essays had opened; their `control_q9` reference is to our module's own control.
- **Luis Perez Morales** cites our left-diagonal entries (0616de, 1d5070) in `Rule30CenterRuns` as the prior bound on white
  runs of a row inside the settled band; his module is now in the kit.
- **Troy Lowry** commented on our pull request #51 with two standalone modules (the dyadic prefix clock and the 11011
  application) and stacked his pull request #55 on ours with credit kept; a reply awaits the owner's word. His
  `Rule30ControlledResponse` terminal rewrites are our right-end moves (we cite his as prior art); his `Rule30LocalConservation`
  proves for every window width what our conservation-law search had measured to width 12 (our job 4's closure is now a
  theorem); his `Rule30TraceEdge` gave our edge-separation module its target.
- **An outside contributor** posted an independent replay of our pull request #49 (81 declarations).
- **Renaud Bosdure's** entries pre-empted Local's integer form of `Q01` (317c64), extended the ether absorption we used for the
  `CQ01` families to the empty right half (230bc7), and supplied the natural clock (c137e0) that drove the cut-and-repair line
  (DQ-023).
- **Jeongseop Lee's** period-32 shielding studies a map one cell displaced from our edge map; both entries cite the relation and
  claim no implication; **Quint and Gemini's** stripe-tail families and **Tensorbend's** absorption results are catalogued in MAP
  sections 9 to 11 and used as prior art in our `CQ01` and period-4 reading.
- **Nobody has yet built on** the channel bound, the Sturmian exclusions, the death-time table or the universal start; the first
  three are the results I would most expect to be used, and 5.2 of the synthesis is the first use of the channel bound.

## 5. Honest negatives and open items

- The prize problems are untouched: `Q01`, `CQ01`, `EdgeObservable`, Absorption and every all-width bound remain open; no result
  of ours or anyone's bears on the centre column's period beyond the kit's `T + P ≥ 16359`.
- 71f858 is still unverified; the maintainers will not rerun it; the mathematics is exact in our record.
- The board (PERIOD-TWO.md section 6.5) is four days behind; the ledger rotation rule was exceeded six-fold before the last
  rotation; one Wolfram kernel reached 75 GB with 39 GB of swap during a notebook build (now run under caps).
- Human verification for the nine newest entries and the five open pull requests are outward dependencies we cannot move.
