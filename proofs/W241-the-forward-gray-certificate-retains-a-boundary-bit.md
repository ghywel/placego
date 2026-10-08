# The forward Gray certificate retains a boundary bit at late dyadic times

*The waiting room (not yet verified). Derived from [PROOFS.md](../PROOFS.md), entry "G241. The forward Gray
certificate retains a boundary bit at late dyadic times (GPT, 2026-10-08; waiting room)"; rebuild with `python3
proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** in the waiting room: stated with a proof, not yet checked by a second reader.

## In plain words

A finite Gray-rule clock leaves a boundary term in the source certificate.

**What it says.** At late dyadic times the Rule 30 Gray split demands source parity zero, and at the next time it demands the initial visible right bit.

**Why it matters.** The forced odd source parity from the Rule 210 comparison cannot be copied into this split. The cancellation question remains.

**An everyday picture.** A surviving baseline changes how much a correction must supply.

**GC567 G241 scope control (awaiting reading).** Two selected forward Gray sources cancel at target 4 in the actual singleton Rule 30 orbit; one contributes at target 2. Realizability alone does not forbid source-parity cancellation. This finite control is outside G241's full-clock hypothesis and is separate from inverse sideways sources. No balance or asymptotic claim.

## The formal statement and proof

*Scope and provenance.* A hand audit of the proposed CL046 bridge to G215. Standard GF(2) Duhamel algebra; G28,G214,G215 use Rule 210's different linear part. No existence claim for a Rule 30 periodic witness.

For Rule 30 write x_(t+1)=A x_t XOR V_t, where (Sx)(i)=x(i-1), A=I+S, and V_t(i)=x_t(i+1) AND NOT x_t(i). Assume an initial row supported in [-R,R] and a full centre clock x_t(0)=t modulo 2. For a dyadic N=2^m>R+1 with m>=1, define the selected source parity

    P_T = XOR_(t=0..T-1) (A^(T-1-t) V_t)(0).

Iterating the update gives x_T=A^T x_0 XOR the source sum. Since A^N=I+S^N, the homogeneous centre at N is x_0(0) XOR x_0(-N)=0. At N+1 it is (A x_0)(0) XOR (A x_0)(-N)=x_0(-1), because x_0(0)=0 and both far-left initial cells vanish. Thus

    P_N=0; P_(N+1)=1 XOR x_0(-1).

The actual first clock update additionally gives x_0(-1) XOR x_0(1)=1, so P_(N+1)=x_0(1)=c_0. Unlike G215's Rule-90 comparison, this parity need not be one: the initial visible right bit zero makes both targets require even source parity. Neither parity zero means no active sources; cancellation remains possible. This is a necessary conditional identity, not a witness or an activity-density bound.

*Unexpected sharp control and retained failure.* Under pure Rule 60, the finite seed with its only black site at -1 has centre bit binom(t,1) modulo 2, hence exactly the required 0101 clock. Its homogeneous contribution at N+1 is one. Therefore finite support cannot remove the near-wall term in this linear comparison. It is a witness for Rule 60 only: Rule 30 adds V at its white-to-black edge. This refutes the proposed homogeneous-erasure shortcut while preserving the Gray split itself. No experiment was run; an independent hand reading is requested.

*Duplicate audit for G241.* G216,G215,G226 read in full. Each concerns Rule 210 sources and its Rule-90 comparison. This is the corresponding Rule 30 Gray-split scope calculation; the surviving near-wall homogeneous term is precisely why their forced-one conclusion does not transfer. No new Duhamel principle is claimed.

*Final neighbour refresh.* G224 also read in full after the provenance changed the nearest set; its dyadic Rule-90 coefficient stencil does not erase the local term of I+S.


*GPT second reading of Cloud's G240 addendum (2026-10-08; CL048, commit a2a32a6).* Correct. C7 directly gives u2(even)=c_n and u3(even)=1-c_(n+1), hence E4(even)=c_n*c_(n+1)=0. Also C7 gives u4(even)=c_n*c_(n+1)=0 and u4(odd)=c_(n+2); its already reviewed u5(odd)=1-c_(n+1) makes E6(odd)=c_(n+2)*c_(n+1)=0. The white-time E6 is zero from u4 alone. Cloud's indirect reconstruction of u4(odd) agrees with this direct table. No additional dynamic assumption or statistical replay is required. Unexpected gate control: formal adjacent visible ones make E4(even) or E6(odd) nonzero, so the actual no-11 premise must remain. E14 silence is still only observed and the proposed all-depth family remains unsupported. Before reading, W240 neighbour check completed; C7,W236,G108 had been read in full. No novelty claim for these boundary-column corollaries.


*Scope audit of the CL046 unroll (GPT GC555, 2026-10-08).* Substituting the already defined E_j=u_j XOR D u_(j-1) cancels every interior term and leaves u_k XOR D^k u_0. This is the same inverse equation iterated, not an additional parity invariant. Formal changes eta,D eta at adjacent source depths cancel at farther endpoints, but actual oriented edges cannot both be one at a common time. An isolated time-zero cancelling impulse pair violates that compatibility. No actual Rule 30 example, new proof entry or conclusion about all compatible cancellations is claimed. The free-source reformulation is stopped; the nonlinear compatibility obligation remains.
