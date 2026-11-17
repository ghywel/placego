# odd zero returns require logarithmic delay in the entry period

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT189. odd zero returns require
logarithmic delay in the entry period (second-read by Local, 2026-10-07)"; rebuild with `python3 proofs/build.py`.
Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

An odd-length return to an all-white stripe takes longer as the period grows.

**What it says.** For a stripe whose period is a power of two, a first return to all white after an odd number of
steps takes at least twice the number of doublings so far, plus three. Working backwards from the end, each new tick
of the stripe is fixed by a few before it, so an odd return follows a set track. Even-length returns can branch, and
escape the argument.

**Why it matters.** It gives a restriction that grows with the period, though only slowly, and isolates the even
returns as the hard case.

**An everyday picture.** A model railway whose points (the switches where the track divides) are all fixed follows
one set route, and you can count how long a circuit takes; make one set of points free to go either way, and the
count no longer limits the journey.

## The formal statement and proof

### GPT G189 — Odd zero returns require logarithmic delay in the entry period (2026-10-07)

**Odd-return period bound, second reader pending; symbolic, no run.** Let compatible periodic profiles start with0,c,1, where c is nonzero of least period q. Suppose the first subsequent identically zero profile occurs at an ODD position r=2k+3, counting the initial zero as position0. Then

    q <= 2^k; equivalently r >= 2*log2(q)+3.

This applies to a doubled dyadic stage when its first zero return is odd. It does not assert that first returns are always odd, or that logarithmic delay supplies the normalized growth required by G186/G187.

**Prediction and counterfactual before the hand checks.** The backward profile functions at even indices should be affine with coefficient1 in their newest temporal bit, so a constant-one condition determines that bit. At odd indices this coefficient can vanish. The counterfactual that every return constraint is deterministic should fail at G188's return10 branch. The controls below check these three claims without a census or computational job.

**Backward functions and their temporal support.** At the final zero the preceding two profiles must be equal; call them w,w. Define U0(w)=U1(w)=w and, for n>=0,

    U_(n+2)(w) = S U_n(w) + (U_(n+1)(w) OR U_n(w)).

Here S w(t)=w(t+1), addition is XOR, and OR is pointwise. This is exactly the compatibility equation solved for the preceding profile, not a model that drops its background. By induction, U_(2j) and U_(2j+1) depend only on bits w(t)..w(t+j). Moreover

    U_(2j)(w)(t) = w(t+j) + A_j(w(t),...,w(t+j-1))

for a Boolean function A_j (A0=0). For the induction step, S U_(2j) has the new bit w(t+j+1) with coefficient1; the OR term in U_(2j+2) depends only on bits through t+j and cannot cancel it. The odd function U_(2j+3) has support through t+j+1, because it is S U_(2j+1) plus an OR term on that same support. This proves both support and affine claims.

In a return of length r, the profile at position2 is U_(r-3)(w), and the entry at position1 is U_(r-2)(w). Thus odd r=2k+3 forces U_(2k)(w)=1. For k>=1 this fixes

    w(t+k) = 1 + A_k(w(t),...,w(t+k-1)).

The k consecutive bits are therefore a state of a deterministic shift map with2^k states. Because w is periodic, its state sequence is a directed cycle, of length P<=2^k. Its temporal word repeats with period P. Every reconstructed profile, including c=U_(r-2)(w), also repeats with P, since these functions commute with time shift. Hence the least period q of c divides P and q<=2^k. For k=0, U0(w)=1 gives w=1 and q=1, yielding the same bound directly. No root reachability assumption is needed for this necessary bound.

**Independent literal and formula controls.** The first functions are U2=Delta w, U3=w*Delta w and U4=Delta^2 w, where Delta=I+S. Thus the r=5 equation fixes w(t+1)=1+w(t), and the r=7 equation fixes w(t+2)=1+w(t), matching G188's alternating and0011 cycles. The literal first return0,01,11,01,01,0 has q2,r5 and meets the bound exactly. Direct forward substitution checks its four interior triples: the right-hand sides are11,10,10,00, respectively, equal to the shifted children. Its preceding source is constant1, so this also guards the essential q2 exception in G188. The ambient r7 control there has entry1101 of least period4 and also meets the bound exactly, but is not an odd-source doubling. G188's ambient r11 entry has period11<=16, consistent with the bound and inconsistent with a blanket dyadic claim for ambient histories.

**Identified unexpected check: even returns retain branching.** U3(x,y)=x*(1+y) is independent of y when x=0, so the even-index induction does not extend to all U_n. More directly, G188's actual r10 condition admits BOTH next bits from state011, even though its full graph has no periodic cycle. This prevents replacing the even return condition with a deterministic map on the same states. For a nondeterministic graph, a periodic word can revisit states before its least temporal period: even the full binary shift admits words0^(m-1)1 of arbitrary least period m on a fixed finite state graph. That abstract control is not a compatible Rule30 return. It only shows why counting states alone is insufficient for the even case.

**Existing record, scope and next obligation.** This generalizes the deterministic odd-return maps of G188 using the backward identity already present in G7/G159. Finite deterministic maps and their cycle bounds are standard; no literature novelty is claimed. The result is a parity-restricted necessary logarithmic delay, not a growing normalized delay: log2(q)/q tends to0. Even first returns, ancestry restrictions and recurrence of large normalized stage lengths remain open. Local: please second-read the support induction, r-3 indexing and least-period divisibility; no new job or larger cap requested. The saved return12 calculation remains unpublished rather than supplying another fixed-bound increment.

*Second reader's note on G189 (Local, 2026-10-07; chat L154).* Correct. Solving each compatibility triple for its first
profile gives $U_{n+2} = SU_n + (U_{n+1} \lor U_n)$ from the final pair $(w, w)$, so $U_n$ is the profile at position
$r - 1 - n$. Hence position 2 is $U_{r-3}$ and the entry is $U_{r-2}$, as stated. In the induction, $SU_{2j}$ carries
$w(t + j + 1)$ with coefficient 1 and the OR term stops at $t + j$, so $U_{2j+2}$ is affine in its newest bit. A
periodic word driven by a deterministic $k$-bit map lies on one cycle of length $P \le 2^k$, so $w$, and with it every
shift-commuting profile, has period $P$, and the entry's least period divides $P$. Checked (`rule30_audit_g99_g100.py`,
S82). The backward functions were computed directly on all words of length 9: for $n \le 12$ the support and affine
claims hold, and $U_2 = \Delta w$, $U_3 = w\,\Delta w$, $U_4 = \Delta^2 w$. On actual walks, every nonzero $c$ at caps 2
to 11 whose first zero falls at an odd position $r = 2k + 3$ has least period at most $2^k$. The bound is exact at
$r = 5$ and $r = 7$ and loose from $r = 11$ on. The even case is not merely unproved: at cap 12 an even first return at
$r = 8$ has an entry of least period 12, far above what the odd bound would allow at that length, so an even-return
obstruction must use the doubling structure, as G188's position-8 argument does.
