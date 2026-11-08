# The SEP gap class and death: no signal

*Local, L1595, 8 November 2026, 16:10 UTC. My pull from L1585, at the owner's word. COMPUTED, self-check, except where marked. Probes: [`tests/probes/sepgap/`](../tests/probes/sepgap/).*

**The question.** S-04 (`Q01_iff_sep_and`, Lean Verified as R30-20261108-752db6) shows that under SEP, Q01 can fail only through a finitely supported constrained start whose free bits meet two adjacent whites (00) infinitely often. I asked whether 00 pairs in the free bits are where finite rows die. If they were, the class might be mortal by a local argument, and SEP would imply Q01.

**Verdict: no.** The local route is ruled out by an argument, and the statistical one finds nothing.

1. **No local lemma can exist** (PROOF-SKETCH, hand, single-party). Every free-bit prefix, with or without 00, belongs to some `Theta f`. Its truncation at depth d is a finite start that keeps depth 1 black at the even ticks until about tick d, by the kit's light cone (`zrow_light_cone`) and the truncation results (`truncation_death`, `trunc_survives`). So no statement of the form "a 00 at step s kills a finite row within k steps" holds, for any k.
2. **Within the free horizon the hazard is a fair coin** ([`death_pairs.py`](../tests/probes/sepgap/death_pairs.py), [output](../tests/probes/sepgap/death_pairs.out); exhaustive, every start of exact width 8 to 22, 2.1 million starts).
   - The hazard of death at the next check is 0.500 after each of 00, 01, 10 and 11, within noise at every width.
   - The last pair before death is 00 a quarter of the time, as are all pairs.
   - The champions do not avoid 00: at width 22 their late 00 rate is 0.63 against 0.30 for all survivors.

   This is what the kit's `count_constrained` bijection implies: within the horizon, the checks are independent of the free bits. It is known in kind, and the data only confirm it.
3. **Beyond the horizon there is no 00 effect** ([`late_hazard.py`](../tests/probes/sepgap/late_hazard.py), [output](../tests/probes/sepgap/late_hazard.out); every check past step ⌈w/2⌉, widths 16 to 22 pooled, about 1,430 checks per pair). The hazards are 0.505 (00), 0.529 (01), 0.479 (10) and 0.474 (11), each ±0.013. The largest gap, 01 against 11, is 2.9 standard errors, and 00 is not the highest. A weak tilt (a black previous free bit looks safer) is below the 3σ bar I set, and is not claimed.

All three preregistered predictions of step 1 and both of step 2 failed; they are kept in the scripts.

**What it teaches.** Finite death statistics are blind to the SEP gap class, as they must be. That class is a property of the infinite tail, and in the free regime the checks carry no information about the free bits. The gap between SEP and Q01 is not visible in finite starts.

**Where the gap lives instead** (a pull, not a claim). In stream language, Q01 is BinaryCTS (`rule30-open`'s `binaryCTS_iff_Q01`), the constant-tail separator for every binary stream, and SEP is the same separator restricted to hard-core streams (no 1,1). So SEP ⇒ Q01 is exactly the question whether excluding eventually constant inverse diagonals for hard-core streams excludes them for all binary streams. The kit's lift and normalization tools (`liftWord`, `normalizeSym`, `prependTwos`, `rotated_iterate`) act on that side. A map that removes 1,1 pairs and preserves eventual constancy of the inverse would prove SEP ⇒ Q01; a structural reason no such map exists would show the gap is real. INSTINCT.md, L1595.

**Record searched:** `record_find` on free bits with 00, two adjacent white, no00, golden, death with free bits and free bit with death (hits: the kit's `free_bits_no00_no11111`, Theorem B on zero runs, L942's free-bit information-loss stage; none on 00 and death); S-03's first-check bound; the kit's `count_constrained`.

## Stream side, step 1: the finite hard-core class is a thinned copy (L1596)

*Local, 16:44 UTC, at the owner's word ("Yes, start it"). COMPUTED, self-check. [`hardcore_death.py`](../tests/probes/sepgap/hardcore_death.py), [output](../tests/probes/sepgap/hardcore_death.out).*

Through S-04's chart, "SEP ⇒ BinaryCTS" is the same statement as "QN ⇒ Q01". The stream language changes the tools, not the question. A finite separation would be a difference in horizon. So I compared D(w), the latest death among all starts of exact width w, with D_N(w), the latest death among starts whose free bits up to death have no 00. These are the rows whose endpoint stream is hard-core up to death. The comparison is exhaustive for w = 8 to 26, 33.5 million starts.

- **The longest life at every width needs a 00.** For every w from 8 to 26 the overall champion's free bits contain a 00.
- **The class-N champion lives shorter.** D_N < D at 18 of 19 widths, equal only at w = 10. D_N/D lies between 0.67 and 0.86 for w ≥ 16, and D_N grows with w at the same rate (36 to 38 at w = 25, 26 against D = 44).
- **Predictions:** "D_N < D at most widths" (0.65) held; "D_N/D ≥ 0.7 at every w ≥ 16" (0.6) failed narrowly at w = 16 (0.667).
- **The deficit is mostly entropy.** Forbidding 00 thins the free prefixes over a horizon of h = ⌈w/2⌉ steps by F(h+2)/2^h. With the fair-coin hazard found above, that shortens the longest life by about 2(h − log₂ F(h+2)) ticks. The model predicts a mean of 6.1 ticks over w = 16 to 26; the observed mean is 8.2. The extra 2 ticks are not tested for significance: the model is crude, with no error model for maxima. They are not claimed.

**What it teaches.** In finite form the hard-core side is not easier in kind. Its horizon grows linearly like the general one and falls short by roughly the entropy of the golden-mean constraint. So SEP is Q01 restricted to free bits in the golden-mean shift (no 00): a positive-entropy subclass, not a degenerate one. A proof of SEP would have to work on most of the same ground as a proof of Q01. Conversely, SEP ⇒ Q01 cannot come from finite horizons; it needs an argument about infinite tails.

**What the kit's finiteness-preserving maps do.** The two maps on constrained rows that keep a row finite and in the class are the two-step shift (`two_step_shift`), which shifts the free bits, and the late twin (S-02), which changes only the first free bits and keeps the future. Neither removes 00 pairs infinitely often. A reduction of SEP ⇒ Q01 would need a new map of that kind. This is a remark on these two maps, not a claim that no other exists.

**Next, if continued.** Look for an invariant of finite immortal rows (a hypothetical object) that the golden-mean restriction would change. Or test the reduction in a relaxed model where immortal finite rows are known to exist, for example the free-input layers of S-04's `LR1`, which realize every no-11 word.
