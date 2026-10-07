# backward period doublings cannot be consecutive

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT151. backward period
doublings cannot be consecutive (second-read by Local, 2026-10-07)"; rebuild with `python3 proofs/build.py`. Edit
the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

A backward period doubling creates a 010 reset in the predecessor row. The next backward row must therefore keep the same period: doublings cannot be consecutive. A nonconstant tail turning zero within 2k physical steps consequently has period at most three times 2 to the power k minus one, improving the previous bound. This does not bound the delays between doublings, guarantee that the bound is attained, or classify the silver code’s initial tail.

## The formal statement and proof

### G151. Backward period doublings cannot be consecutive (2026-10-07)

**Status and target.** Symbolic tail-period refinement, independent review pending; G150 independently verified by Local L106. No experiment. Uses G150's two-label criterion and reviewed G13/G124. Prediction: a doubled predecessor necessarily acquires a reset, forcing the next backward step to preserve its period. Counterfactual: the bound p or 2p permits doubling at every backward nonconstant row. The reset argument excludes that possibility; it gives no upper bound on the delays between doublings or a wall-support conclusion.

Let y be a nonconstant periodic ordinary Rule30 row of least period p, and suppose its predecessor x has least period 2p. Then x contains a cyclic factor 010. Consequently x has exactly one whole-line predecessor z, with least period 2p. In particular no periodic backward chain has consecutive doublings between nonconstant rows.

**Proof.** By G150, y has no resetting zero gap, and an odd number of its cyclic runs of ones have length 2 modulo3. Choose one such run, whose length is at least two. At the cut just after the preceding zero the inverse recurrent pair set is C={00,11} or A={00,01}. Label 00 as zero and the other state as one. One p-period interchanges the labels. Thus in the doubled predecessor x, the selected cut takes both labels one p apart. At the occurrence with label zero, the actual adjacent input pair is 00. The first two driver ones give

    00 --1--> 01 --1--> 10.

The consecutive reconstructed input symbols are therefore 0,1,0. Reversing the spatial reading direction leaves 010 unchanged. Since x is a whole-line periodic row there is also a following symbol, so G13's reset factor 010z occurs. G150's reset case now gives exactly one predecessor of x, of the same least period 2p. This proves the claim without assuming any particular finite head or boundary bit.

**Improved zero-basin time bound.** If a nonconstant periodic pattern first reaches zero at physical time T>=2, the last two backward states are the all-one row and a period-three phase of 001. That period-three pattern has a cyclic 010 reset, so the next earlier pattern, if present, must also have period three. Beyond it, no two consecutive steps can double. Thus if the original least period is 3*2^a,

    a <= floor((T-2)/2),
    period <= 3*2^floor((T-2)/2).

This is stronger than G124/G149's a<=T-2 cap. In G149's setting, a compatible row becoming finite after k two-step iterates has a nonconstant zero-reaching eventual tail with

    a <= k-1,    period <= 3*2^(k-1),    k>=1.

If its periodic tail reaches zero earlier, apply the first-hit statement with that earlier T<=2k. Constant tails retain least period one. The former 3*4^(k-1) bound remains true but is superseded by this stronger bound; no reviewed text is invalidated.

**Independent control and unexpected sharpness guard.** The literal six-site trajectory extends G124 as

    101011 -> 001010 -> 011011 -> 010010 -> 111111 -> 000000.

The first arrow is checked by its six ordinary left-to-right triples, which give 0,0,1,0,1,0. The first two words have least period six; 011011 and 010010 have least period three. Read backward, the 3-to-6 doubling is followed by a 6-to-6 preservation, exactly as proved. Moreover 101011 itself has cyclic factor 010 (at positions 1,2,3), so its predecessor again preserves period six. The control prevents claiming that the upper bound is automatically attained by doubling every other step. No such matching all-depth construction is supplied.

**Scope.** This sharpens the periodic spatial zero basin and the conditional ancestors of finite compatible rows in G149. G123's canonical periods still have unbounded growth, and this theorem does not bound the gaps between their increases. It does not prove that the phase-zero silver tail is periodic, zero-reaching, finite or infinite. A new multi-row invariant or an actual all-depth tail classification is still required. No new computation, full right extension or prize conclusion follows.

*Second reader's note on G151 (Local, 2026-10-07; chat L107).* Correct, read jointly with G150. In the doubled case the
selected residue-two run sees both labels one period apart, and at the label-zero occurrence the pair is $00$; two
driver ones give $00 \to 01 \to 10$, so the reconstructed inputs read $0, 1, 0$, a run of one 1 between zeros, which is
G150's reset case for $x$. The time indexing is right: below the all-one row and the period-three phase of $001$ (which
itself contains $010$, forcing the next row back to period three) there remain $T - 3$ backward steps, so at most
$\lceil (T-3)/2 \rceil = \lfloor (T-2)/2 \rfloor$ non-consecutive doublings, and $a \le k - 1$ in G149's setting.
Checked (`rule30_audit_g99_g100.py`, S46): for all 672 doubling outputs of least period at most 12, both period-$2p$
predecessors (found by the descending recursion and confirmed forward) contain $010$ and have exactly one predecessor on
rings of size $2p$ and $4p$; on every ring up to size 24 (all 3,168 rows first reaching zero at time 2 or later; the
per-size cap was never hit) the period obeys $a \le \lfloor (T-2)/2 \rfloor$; and the six-site trajectory, with
$101011$'s own $010$.
