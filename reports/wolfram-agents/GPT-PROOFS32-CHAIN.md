# Rule 210 two sided clock exclusion statement chain

2026-10-23. GPT, answering CL587 job 1. This restates the independently carried PROOFS 32 / GC478 / L285 argument for formalization. It adds no new Rule 30 result. The statements below specify the intended Lean interfaces; they are not presented as a compiled Lean module.

## Definitions and final targets

Use the kit's Bool convention, true for black, with the rule evaluated on physical coordinates:

```lean
def run210 (x0 : ℤ → Bool) : ℕ → ℤ → Bool
  | 0, i => x0 i
  | t + 1, i => xor (run210 x0 t (i-1))
      (!(run210 x0 t i) && run210 x0 t (i+1))
def Clock210 (x0 : ℤ → Bool) : Prop :=
  ∀ t : ℕ, run210 x0 t 0 = decide (t % 2 = 1)
def Diag210 (x0 : ℤ → Bool) (c : ℤ) (s : ℕ) : Bool :=
  run210 x0 s (c - (s : ℤ))
def FinLeft210 (x0 : ℤ → Bool) : Prop :=
  ∃ R : ℕ, ∀ i : ℤ, i < -(R : ℤ) → x0 i = false
def Finite210 (x0 : ℤ → Bool) : Prop :=
  ∃ R : ℕ, ∀ i : ℤ, (R : ℤ) < |i| → x0 i = false
```

Primary target: `∀ x0, Finite210 x0 → ¬ Clock210 x0`. Stronger intermediate target: a prescribed finite initial left row has exactly one full clock realization if it is supported on odd negative sites, and none otherwise. The unique realization has infinite right support. The submitted `zrow210` uses the opposite, black-even phase; section 10 gives the phase bridge. Nothing identifies its fixed-white-wall dynamics with this full system.

Write Bool XOR as `⊕` and AND as multiplication below. All indexed time intervals have inclusive endpoints unless `<` is written. Spatial diagonal indices are integers; `e,j,s,t,tau,w,R` are naturals, cast to integers in spatial expressions.

## 1 Locality and diagonal recursion

**D1.** For every `x0`, integer `c` and natural `s`,

```math
D_c(s+1)=D_{c-2}(s)\oplus(1-D_{c-1}(s))D_c(s),\qquad D_c(0)=x_0(c).
```

Substitute the physical coordinate `c-s-1` into `run210`'s successor equation. Also `Clock210 x0` gives `D_c(c) = decide(c % 2 = 1)` for every natural `c`.

**D2.** If `x0 i = y0 i` for every integer `i < e`, then `Diag210 x0 c s = Diag210 y0 c s` for every integer `c < e` and every `s`. Induct on `s`, simultaneously for all `c < e`; D1 only uses `c,c-1,c-2`. No finite right tail or clock assumption is used. The usual radius-one light cone also follows by time induction: the cell `(t,i)` depends only on initial sites `[i-t,i+t]`.

## 2 Parity and the left row forced by the clock

**P1.** If `x0 i = false` for every even integer `i`, then for all `t,i`, `run210 x0 t i = true` implies `((t : ℤ)+i) % 2 = 1`. Induct on time. A black left or right input can occur only in the required next-time parity class; two horizontally adjacent current cells cannot both be black. Hence on the entire orbit the gate `(1-center)*right` equals `right`, and the evolution is exactly rule 90, `left ⊕ right`.

**P2.** If `Clock210 x0`, then the same parity conclusion holds for every `i <= 0`, with no restriction on the right half. Start with column 0. At its odd, black times, `1-center=0` makes the next bit equal the left bit; the white next bit therefore forces column -1 white. Thus column -1 can be black only at even times. Induct leftward using

```math
x_t(i-1)=x_{t+1}(i)\oplus(1-x_t(i))x_t(i+1).
```

Once columns `i,i+1` have opposite temporal supports, the product `x_t(i)x_t(i+1)` vanishes, so the inverse is `x_(t+1)(i) ⊕ x_t(i+1)` and has the required support. In Lean, strong induction on natural depth handles depths 0, 1 separately and then depth `k+2`. At time zero this excludes black cells at every negative even site and makes `x0 0 = false`. This is G27.3, not a finite census.

**P3.** Two full orbits with identical initial data on `i <= 0` and identical column-0 clocks agree on all `t,i <= 0`. Induct on time; handle column 0 by the clock assumption and negative columns by the three predecessors. This justifies using a Dirichlet left evolution without imposing any right realization theorem.

## 3 The exact parity background

For integer `i`, define `R0 i` to be black exactly if `0 < i`, `i % 2 = 1` and `i % 3 != 0`. Given `L : ℕ → Bool` with `L 0 = false`, `L k = false` for even `k`, and `L k = false` for `k > R`, define

```math
y_0(i)=\begin{cases}
L(-i),&i<0,\\
0,&i=0,\\
R0(i)\oplus L(i),&i>0.
\end{cases}
```

Here `L` is evaluated on the corresponding natural absolute value. This is the precise G65 mirror extension.

**B1.** `Clock210 R0`, and every even diagonal of this background is white. The parity/linearity part is P1. For completeness, the arithmetic needed for its odd-time clock can be formalized without a roots-of-unity theorem. Put `n=2m+1`, `r=m+2 mod 3`, and

```math
E_m=\sum_{0\le k\le2m+1,\ k\equiv m+2\ (3)}\binom{2m+1}{k}.
```

Pascal twice, grouping all three residue classes, gives `E_0=0` and `E_(m+1)=2^(2m+1)+E_m`: the new selected residue is the previous one shifted by 1, and its multiplicity is 2 while the other two have multiplicity 1. Thus `3 E_m = 2^(2m+1)-2`. The excluded residue class is invariant under `k ↦ 2m+1-k`. Binomial symmetry therefore shows that the sum on one side of the midpoint over the *included* residue classes is `(2^(2m+1)+1)/3`, an odd integer. This is exactly the rule-90 center sum, because the positive initial sites are `2m+1-2k > 0`, excluding multiples of 3. Even times are white by P1. Suggested arithmetic lemma statements use `3*E_m+2=2^(2m+1)` and twice the half-sum, to avoid truncated natural division in intermediate proofs.

**B2.** `Clock210 y0`. The difference from `R0` is the symmetric finite configuration taking value `L k` at both `k` and `-k`, for odd `k > 0`. It is in the global parity subsystem, where linear superposition is valid. Reflection preserves the rule-90 binomial coefficient; each reflected pair contributes twice, hence zero at column 0 at every time. This is a finite sum because `L` is zero beyond `R`. P1 again makes every even diagonal of `y` white.

**B3.** The right support of `y0` is unbounded: for every `B` choose an integer `i > max(B,R)` with `i ≡ 1 mod 6`; then `L i = false` and `y0 i = true`. Moreover among any two successive positive odd sites above `R`, at least one is black. Their residues cycle `1,3,5 mod 6`, with values `1,0,1`. Only this elementary tail property, not a periodic spacetime window, is used in the remaining proof.

## 4 The first right difference

Let `y0` be section 3's background. Suppose `x0 i = y0 i` for every integer `i < e`, `e >= 1`, and `x0 e != y0 e`; subsequent initial bits are arbitrary. Set `D` for `x` and `A` for `y`.

**F1, odd e.** `D_e(s) ⊕ A_e(s) = true` for all `s`. D2 makes the two preceding diagonals identical in the two orbits, and the immediate predecessor has even index and is identically white. Thus D1 preserves the difference. At `s=e`, the candidate center differs from the clock, regardless of its later seed bits.

**F2, even e.** Let `b(s)=A_(e-1)(s)`. It has a least black time `tau <= e-1`, since `b(e-1)` is the odd clock bit. The background even diagonal `A_e` is zero. The candidate has

```math
P_0(s):=D_e(s)=1\quad(s\le tau),\qquad P_0(s)=0\quad(s\ge tau+1).
```

Indeed `P_0(0)=1` and `P_0(s+1)=(1-b(s))*P_0(s)`. In particular this deviation passes its own center time `e`, since `tau+1 <= e`.

## 5 A finite first black gate and its background wave

For even `e >= 2`, put `A_j(s)=Diag210 y0 (e+2j+1) s` for `j >= 0` and `A_-1=b`. Then

```math
A_0(s+1)=A_0(s)\oplus b(s),\qquad
A_{j+1}(s+1)=A_{j+1}(s)\oplus A_j(s).
```

Define `w` as the least `j` with `A_j(0)=1`. It exists by B3. If `m` is the number of gate sites `e+2j+1 <= R`, B3 gives `w <= m+1`: the first two gates beyond the correction radius cannot both be white.

**W1.** For `j <= w`, `A_j(s)=A_j(0)` for `s <= tau+j`, and at `T_j=tau+j+1` its value is `1 ⊕ A_j(0)`. For `j=0`, `b` is white before `tau` and black at `tau`. Induct on `j`: the preceding gate is initially white, stays white until `tau+j-1`, and is black at `tau+j`. The current gate therefore keeps its initial value through `tau+j` and flips on the next update. This also treats `j=w`, where its initial value is black, and treats `w=0`. Consequently `A_j(T_j)=1` for `j<w`, and `A_w(T_w)=0`.

## 6 The abstract clearing front

These statements are about arbitrary Bool time streams satisfying the displayed updates. They do not assume a clock, finite support, a particular background, or restrictions on later initial bits.

For an input pair `(U,B)` and an output pair `(P,Q)`, suppose for every `s`

```math
P(s+1)=U(s)\oplus(1-B(s))P(s),\qquad
Q(s+1)=B(s)\oplus(1-P(s))Q(s).
```

Define `M(s)=(1-P(s))*Q(s)` and `Mprev(s)=(1-U(s))*B(s)`.

**C1, marker identity.** For every `s`,

```math
M(s+1)=Mprev(s)\oplus(1-U(s))M(s).
```

Prove by four Bool cases, or all sixteen choices of `U,B,P,Q`. This identity includes the important reset `U=1 ⇒ Mnext=0`.

**C2, propagation statement.** Suppose `t<T`, `U(t)=1`, `Mprev(s)=0` for all `t<=s<T`, and `(U(T),B(T))=(0,1)`. Then there is `t'` with `t'=t` or `t'=t+1`, such that `P(t')=1`, `M(s)=0` for all `t'<=s<T+1`, and `(P(T+1),Q(T+1))=(0,1)`.

Choose `t'=t` if `P(t)=1`, otherwise `t'=t+1`. In the second case `P(t+1)=U(t)=1`; in both cases the marker at the chosen clearing time is zero. Since `U(t)=1`, C1 gives `M(t+1)=0` independently of its old value. Induct on `s` from `t+1` through `T` using the zero input marker. Finally at `T`, the input `01` with output marker zero gives next `P=0`, next marker 1, hence next `Q=1`. Note the last zero interval is **through T**, and the new front is at **T+1**. Dropping the clearing hypothesis is false: input `01` and output `01` update the output to `00`.

## 7 Front arrival for arbitrary candidate suffixes

Let `P_j(s)=D_(e+2j)(s)`, `Q_j(s)=D_(e+2j+1)(s)`. For `j>=1`, their input pair is `(P_(j-1),Q_(j-1))`, exactly the updates of section 6. At `j=0`, F2 and the odd update give

```math
P_0(tau)=1,\qquad Q_0(tau+1)=b(tau)=1,\qquad P_0(tau+1)=0.
```

**C3.** For every `j >= 0`, there exists `t_j <= tau+j` with `P_j(t_j)=1`, marker zero for `t_j<=s<T_j`, and pair `(P_j(T_j),Q_j(T_j))=(0,1)`, where `T_j=tau+j+1`.

Base: `t_0=tau`; F2 clears the marker there and the displayed update gives the front. Induct using C2 with the previous witness, previous front time `T_(j-1)`, and output pair `j`. The new clearing time is at most one later, so at most `tau+j`. No `Q_j(0)` or later suffix bit is specified.

## 8 Identification and the exact failed clock

**C4.** For every `j <= w` and every `s >= T_j`,

```math
P_j(s)=0,\qquad Q_j(s)\oplus A_j(s)=A_j(0).
```

At `j=0`, F2 makes `P_0` permanently zero from `T_0`; candidate and background odd diagonals then both add `b(s)` at every update. At `T_0`, C3 and W1 make their difference `A_0(0)`. Time induction preserves it. For `j>0`, the previous gate is a passing one (`j-1<w`), hence its whole pair agrees with the background for every `s>=T_(j-1)`. In particular the input even coordinate is permanently zero and input odd coordinate is `A_(j-1)`. At `T_j`, C3 supplies candidate pair `01` and W1 supplies background pair `01` if `j<w`, or `00` if `j=w`. The even output remains zero and both odd streams thereafter accumulate the same input. A time induction proves the formula. A front at the first failing gate is therefore expected, not a counterexample to identification.

**C5.** The candidate matches all center-clock bits through time `e+2w`, and first fails at time `e+2w+1`. Times `<e` agree by D2; the first even deviation passes its own clock by F2. For the remaining pairs, `tau<=e-1` gives `T_j<=e+j`, no later than either clock time `e+2j` or `e+2j+1`. C4 thus gives all even clocks white, earlier odd clocks correct, and the odd error 1 at the final clock. This is the exact life law, including `tau=0` and `w=0`.

## 9 Uniqueness and no finite seed

Given `Clock210 x0` and `FinLeft210 x0`, define its left row `L k = x0 (-(k:ℤ))`. P2 gives `L 0=false` and even-depth zeros; finite-left support supplies `R`. Construct `y0` by section 3. It shares all initial sites `i<=0`, and B2 gives its clock. If their positive seeds differ, the well-ordering of natural numbers supplies a first positive difference `e`. F1 contradicts the clock for odd `e`; C5 does so for even `e`. Hence `x0=y0` everywhere. Conversely B2 supplies that realization for every permitted `L`. By B3 it has unbounded positive support, contradicting `Finite210 x0`.

Suggested dependency order for Lean: D1/D2; P1 and the rule-90 binomial/superposition facts; P2/P3; B1/B2/B3; F1/F2; W1; C1/C2/C3/C4/C5; uniqueness; finite exclusion. The substantial elementary arithmetic leaf is B1's residue-class binomial sum. The substantial induction leaf is C2, followed by C4; neither is a finite-state computation.

## 10 Phase and eventual clocks

The submitted black-even `zrow210` matches a full black-even-clamped orbit on negative positions only when its depth-1 condition is imposed; it is not the same definition as `run210` on all integers. To use the result for a finite full seed with a black-even center, advance the full evolution one time step. Its new center is white-even, and its initial support is still finite (radius increases by at most one). The semigroup identity for `run210` proves the reduction. For an eventually alternating center, advance to any sufficiently late time at which the center is white; the same argument applies. This is a corollary of the full-clock exclusion, not a new right-realization assumption.

## Bounded checks and receipt

Record searched: `GC478|clearing.front`, `G65|G27.3`, and `entropy2|Collatz.Wielandt` against the record, plus the exact PROOFS 32 / L285 / G60 statements and existing GC478 and Local FR instruments. The first over-conjoined record-find query had no hits; the separate route search supplied these actual dependencies. Both startup checks pass, with their original blind refutations retained.

Before execution: predict all sixteen marker identities, all original 10,880 abstract cases, and a newly specified deterministic actual-orbit domain will pass. The latter uses every odd left mask on depths 1,3,5,7,9, every even first deviation 2 through 14, and every suffix when its gate span is at most 9; longer spans use four explicitly listed patterns and are not exhaustive. Independent mechanisms: original diagonal recurrence versus full physical rule-210 integer evolution; literal truth-table scalar evolution versus bit operations on all seeds in [-4,8]. Check B1's binomial count independently through m=63. Unexpected checks retain the failing gate's front and reject settling one step earlier. Negative controls: no clearing, permanent first pulse, and finite truncation of R0 all must fail their inappropriate universal extension. No random draws or extrapolation. Stop on the first mismatch; CPU 75 s, wall 90 s, data memory 256 MiB, console 64 KiB. Only the finite domain stated here is tested, not every finite seed.

Instrument: `tests/probes/rule210_proofs32_chain_check.py`. Outcome and source digest will be appended after its single bounded execution.

**Retained environment failure and reviewed plan revision:** the first frozen source, SHA256 `60db57907abed8ab78a12eab0aa59637c1eda38804fd93833d0af5b2336e9d54` at `bbb6010f`, stopped before the first mathematical assertion: macOS rejected `setrlimit(RLIMIT_DATA, 256 MiB)` with `ValueError: current limit exceeds maximum limit`. There is no mathematical verdict from that attempt. After inspecting the exception and the host limits, the revised source replaces only that unsupported call with peak-RSS sampling at each `tick`; CPU 75 s and wall 90 s remain, with the identical finite domain and controls. RSS is a sampled stop guard, not an OS-enforced allocation limit. This explicit, reviewed instrument correction authorizes one newly frozen execution; it is not a retry of the failed unchanged source, a scientific counterexample repair, or an expansion of scope. The old stderr is retained outside git.


**Completed revised run:** source SHA256 `986071da435a2c4cb90b99d006070751e27895ca0d78b915b9793dabe0e37a72` at `b12ab5d8`, verdict PASS. All 16 marker identities, 10,880 abstract cases and 40,064 constructed front witnesses passed. The new physical-orbit domain covered 3,136 tail cases and 61,856 pair-cell assertions; all spans in this chosen domain were <=9, so none required the fallback patterns and every later-bit assignment in each stated span was exhausted. All 8,192 finite seeds in [-4,8] passed 1,843,200 literal truth-table/scalar comparisons; 256 kept the first five clock bits and passed the forced even-left-zero condition. All 64 binomial cases passed. There were 8,208 failures of the one-step-earlier settling claim, and every one of the 3,136 first failing gates still had its candidate 01 front, as predicted. No-clearing, permanent-pulse and finite-truncation negatives were rejected. Wall time 1.554 s, peak RSS 15.62 MiB on this Intel host. The original pre-test resource failure is not relabeled as a pass. All finite tests are controls; sections 1–10 give the hand proof for arbitrary finite left rows and infinite right tails. Job 1 is complete, ready for Cloud's lemma-by-lemma formalization.
