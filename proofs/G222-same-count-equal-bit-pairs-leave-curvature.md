# same-count equal-bit pairs leave curvature

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT222. same-count equal-bit pairs
leave curvature (second-read by Local, 2026-10-08)"; rebuild with `python3 proofs/build.py`. Edit the proof in
PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

Interior two-step00 and11 occurrences at the same count pair to a second difference.

**What it says.** Match their minimum multiplicity. The matched coefficient is curvature divided by2, while each mixed word contributes negative curvature divided by4. Unmatched equal-bit and boundary contributions remain explicit.

**Why it matters.** It names a second mechanism for temporal cancellation, beyond individual mixed paths. The actual class allocation and residual terms still need control.

**An everyday picture.** Two opposite changes can shed their shared trend while leaving curvature; matching the wrong labels breaks that bookkeeping.

## The formal statement and proof

**Where:** RULE30-GPT.md GC440 at a02b6c5; statement and proof copied verbatim below. Local L260 at cbee024 checks all four path coefficients, minimum-multiplicity regrouping, intermediate admission, zero-extension kills, boundary residual and both hand guards. This refines G80's two-step accounting, distinct from G91's next-state coalescence.

Fix t+2<=T and an actual admitted parent occurrence with count a satisfying a>=ell_(t+1). Both first-bit alternatives are admitted. Put F_j=f_(t+2)(a+j), using killed-state zero extension, and K_a=F_0-2*F_1+F_2. Its two-step fair potential is (F_0+2*F_1+F_2)/4. Thus actual00 and11 contributions are respectively

    U_a=(3*F_0-2*F_1-F_2)/4,
    V_a=(3*F_2-2*F_1-F_0)/4,
    U_a+V_a=K_a/2.

Either mixed path contributes -K_a/4, as G80 proves. For actual interior occurrences at count a, retain the full two-bit word before final admission, and let n_00,n_01,n_10,n_11 be its four multiplicities. Set M_a=min(n_00,n_11). The exact sum for this class is

    (2*M_a-n_01-n_10)*K_a/4
      +(n_00-M_a)*U_a+(n_11-M_a)*V_a.

**Proof.** Subtract M_a from the00 and11 counts, collect M_a*(U_a+V_a), and add both mixed counts. Substitution of the displayed coefficients gives the formula. Each parent retains its multiplicity; no same terminal state, swapped orbit, fair actual word frequencies or independence assumption is used. An interior00 path can fail the final barrier; its endpoint potential is then F_0=0 and its negative drop remains in U_a. First-step failures and all parents with a<ell_(t+1) stay in G80's separate literal boundary residual, never in this formula. Adding those residuals and any last unpaired step gives G80's exact global accounting.

**Scope:** the nonzero equal-bit pair and mismatched-count guards remain in GC440. Neither actual matched mass nor unmatched equal-bit, mixed or boundary allocation has a uniform estimate. No count-ratio conclusion follows.

**Duplicate guard for G222:** actual nearest G80,G91,G92 read in full. G80 supplies mixed-path curvature and literal two-step residual accounting. G91 matches next-state labels; G92 closes its coarse maximum-curvature bootstrap. G222 instead matches00/11 multiplicities at the same count and exposes the combined signed curvature coefficient, retaining all unmatched and boundary terms. No new smoothing or bootstrap estimate is claimed.
