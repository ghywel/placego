# Odd factors do not enlarge the rooted edge-history tree

*The waiting room (not yet verified). Derived from [PROOFS.md](../PROOFS.md), entry "G157. Odd factors do not
enlarge the rooted edge-history tree (2026-10-07)"; rebuild with `python3 proofs/build.py`. Edit the proof in
PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** in the waiting room: stated with a proof, not yet checked by a second reader.

## In plain words

Odd factors in a chosen common period add no histories to the rooted edge tree. Restricting to the power of two dividing that period preserves every branch and its length, so the first two exact bounds apply to infinitely many common periods. This does not bound settling times.

## The formal statement and proof

**Statement.** Let P>=1 and Q=2^v, where v is the exponent of two dividing P. The common-period-P rooted tree of G7 is isomorphic to the common-period-Q tree: repeat each Q-bit temporal word P/Q times. This preserves depth, the predecessor B, zero hits and temporal rotation classes. In particular its maximum prefix length K is identical, and G156 sharpens to

```math
K+1\le N_4(Q)=\frac1Q\sum_{d\mid Q}\varphi(d)4^{Q/d}.
```

Every odd P has exact maximum K=3; every P with v=1 has exact maximum K=8. These are finite-tree statements, not a bound on physical transient lengths.

**Proof.** A child c of the adjacent pair (a,b) obeys

```math
c(t+1)=a(t)\oplus\bigl(b(t)\vee c(t)\bigr).
```

Suppose a and b have a common dyadic period d. If b has a one, a reset at t0 fixes c(t0+1)=a(t0) XOR1 independently of c(t0). The same reset occurs at t0+d, so c agrees with its d-shift immediately after the reset and thereafter by the recurrence. For any integer t choose an earlier reset; hence the entire periodic word c has period d. If b is zero, summing d steps gives c(t+d)=c(t) XOR sigma, where sigma is the parity of one d-block of a; in particular c has period 2d. Starting from the constant root, induction makes every profile's least period a power of two. Each profile is also P-periodic, so its least period divides P and therefore divides Q.

Restrict every profile to its first Q letters. Since all have period Q, restriction commutes with shift, OR, XOR and B. Conversely repetition embeds any Q-periodic rooted history in the P-periodic tree. The two maps are inverse on every node and edge, and a rotation by t on either side depends only on t modulo Q. Thus the entire rooted trees and their rotation quotients agree. Apply G156 at Q. Its literal Q=1 and Q=2 controls supply the asserted exact maxima. Square.

**Controls and identified unexpected check (symbolic, no run).** Local L114's P=3,5,7 maxima3 and P=6 maximum8 follow exactly, rather than merely fitting a pattern. At P=6 the necklace upper bound drops from700 to10; excluding the known nonabsorbing class gives exact K=8. The rooted hypothesis is essential: the ambient period-three pair (0,100), with the cyclic word written in temporal order, has least pair period3 and cannot be reduced to Q=1. It is excluded by the rooted induction, not by an assertion that all periodic B-states are dyadic. This is the unexpected scope guard.

**Prior art and limits.** This is an explicit finite-tree corollary of the reset/integration mechanism in Nersissian, section4, Theorems10-12 (read directly); that source attributes dyadic diagonal periods to Jen. No novelty is claimed for period doubling or the reset proof. The source's initialized physical tails do not alone establish equality of our arbitrary-phase rooted trees, so the two-sided periodic argument above supplies that transfer. This does not identify maximum K at Q>=4, control actual settling times, establish an upper period-growth law, or solve a prize problem. No computational experiment was launched.
