# common endpoint segments characterize allocation-bound ties

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT221. common endpoint
segments characterize allocation-bound ties (second-read by Local, 2026-10-08)"; rebuild with `python3
proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

The gap between optimized centering and component allocation is exactly a weighted distance to endpoint segments.

**What it says.** Each demand component gives a real segment joining its cumulative-imbalance endpoint values. The two bounds tie precisely when all those segments share a point; merely touching is enough.

**Why it matters.** It identifies which geometry explains the recorded ties and where a strict improvement must occur. It does not estimate the component bound itself or the final count ratio.

**An everyday picture.** One common meeting point costs nothing extra. Separate acceptable meeting intervals impose an unavoidable travel cost.

## The formal statement and proof

**Where:** RULE30-GPT.md GC434 at 3d5a2cb; statement and proof copied verbatim below. Local L259 at b5e6886 verifies the three-case distance identity, endpoint incidence, tie criterion, strict-gap bound and hand controls. This is elementary real-line distance geometry refining G220, not a bound on the actual interval imbalances.

Use GC432's positive levels and components. Index each component by e=(j,l,r), set w_e=h_j-h_(j-1)>0 and let A_e be the closed real segment with endpoints B_(l-1),B_r. Write dist(c,A_e)=0 inside the segment and the distance to the nearer endpoint outside it. Then, with E the G220 bound and M the G217 optimized bound,

    M-E = min_c sum_e w_e*dist(c,A_e).

In particular, M=E if and only if the segments A_e have a common point. For nonempty demand, write L=max_e min(A_e) and U=min_e max(A_e); the equality criterion is L<=U. Empty demand gives M=E=0 and the empty intersection is understood as the whole real line.

**Proof.** For any two real x,y, the three cases c below, inside or above their segment give

    abs(x-c)+abs(y-c)=abs(x-y)+2*dist(c,[min(x,y),max(x,y)]).

GC432's endpoint incidence gives the exact identity

    (1/2)*sum_a abs(B_a-c)*abs(d_a-d_(a+1))
      = (1/2)*sum_e w_e*(abs(B_(l-1)-c)+abs(B_r-c))
      = E+sum_e w_e*dist(c,A_e).

Minimize over c. For a finite nonempty family, the distance objective tends to infinity as abs(c) tends to infinity and attains its minimum. All summands are nonnegative with positive weights, so this minimum is zero precisely when one c belongs to every segment. Equivalently L<=U. If L>U, choose segments attaining these two extrema; for every c their unweighted distances sum to at least L-U, and the weighted objective is at least min_e(w_e)*(L-U)>0. This also independently checks strict positivity, rather than just invoking failure of a zero minimizer.

**Scope:** the disconnected, touching and translated-prefix hand guards are retained in GC434. The six recorded GC432 total ties imply a common center at every time increment; the width-7 strict gain implies at least one incompatible increment. No new actual-segment classification or population computation has been run, and no count-ratio estimate follows.

**Duplicate guard for G221:** actual nearest G220,G218,G217 read in full. G220 supplies the component endpoint decomposition and both inequalities; G217 defines optimized centering; G218 orders two older bounds conditionally on unimodality. G221 identifies their exact nonnegative gap and a common-segment criterion, without assuming shape or improving the actual imbalance estimate.
