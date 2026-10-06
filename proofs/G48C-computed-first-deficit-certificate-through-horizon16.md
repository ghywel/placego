# Computed first-deficit certificate through horizon16

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT48C. Computed first-deficit
certificate through horizon16"; rebuild with `python3 proofs/build.py`. Edit the proof in PROOFS.md and this summary
in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

A computer certificate: every number above 1 whose growth factor first dips below 1 within 16 steps really does drop
below itself then.

**What it says.** Every step pattern up to length 16 was checked, together with every number in each pattern's
class, by G48's formula. Apart from the number 1, every number whose growth factor first dips below 1 by step 16
does fall below its start at that same step.

**Why it matters.** It confirms, for short horizons, that the growth factor and actual survival agree once you leave
out the trivial cycle. It is a finite result, not a theorem for all horizons.

**An everyday picture.** Testing every key on a short key-ring: none opens the door except the one marked "1".

## The formal statement and proof

**Where:** RULE30-GPT.md G48 outcome, 2026-10-06; copied verbatim. **Bears on:** PERIOD-TWO.md §7 question9. **Status:** finite-horizon exact computation and affine lifting argument, single-party; awaiting independent reproduction and second reader. Not a general Collatz theorem.

### G48 computed finite-horizon certificate

For every positive integer n>1 whose first coefficient deficit occurs by step16, actual stopping occurs at that same step. This is a finite-horizon statement over all positive starts, not an all-horizon theorem.

**Certificate and argument.** The committed script enumerates every binary word throughlength16, retaining exactly the791 words whose first deficient prefix is the whole word. Its exact gap calculation and census find only one realized positive surviving lift: word10,start1,gap0. G48's affine identity says every positive lift of a residue has gap g-D*m, with D>0. Thus the script's integer enumeration of all m from their positive-domain minimum to floor(g/D) accounts for every possible surviving start in each class, including starts larger than the representatives tested directly. There are no remaining positive survivors except1. Before the first coefficient deficit, the positive affine correction ensures actual survival, so an n>1 with that deficit by16 descends at the deficit itself. The direct controls check2373 lifts independently and retain the zero-residue domain exception. This computed argument depends on the completeness and correctness of the committed enumeration; it awaits independent reproduction and review. No novelty or prize claim.

*Second reader's note on G48 and its certificate (Local, 2026-10-06; chat L018).* The identity is correct: with
$n = r + 2^t m$, $n_t = q + A m$, so $n_t - n = g - Dm$; every proper prefix has coefficient above 1 and so already lifts
any positive start, which makes survival exactly $g - Dm \ge 0$ with the stated $m_{\min}$. The certificate was
reproduced independently with my own code (`collatz_audit_g39_g42.py`, G48 part): exactly 791 first-deficit words
of length at most 16, and over all of them the only surviving positive lift is the word 10 with start 1 and gap 0;
and, separately, a brute-force scan of every start $1 < n < 2^{22}$ finds none whose coefficient deficit comes by
step 16 without its actual stopping at that step. So the finite-horizon statement is replicated, by two methods.
It is the coefficient stopping time conjecture checked to horizon 16, which GPT identifies as known (G014); the
literature verifies it much further, so the value here is the exact gap form, not the horizon.
