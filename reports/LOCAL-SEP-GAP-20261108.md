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
