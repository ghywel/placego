# SW02 carrying review

GPT GC2690, 6 November 2026. **Q01 ⇒ Mortality passes the requested carrying read.** Together with the existing kit arrows, this gives Q01 ⇔ Mortality ⇔ all-length repeat budgets. AM-3's bounded amplification and CT-2's first-check bounds also pass with the corrections below. CP-4's separator converse passes with its one-tick phase repair. These are hand results read by Local and GPT, with a separate finite certificate replay for AM-3. None proves Q01 or a prize statement, and no new Lean verification is claimed.

This completes the requested read of L1563's main proof packet at `3eb5ea93`, beginning with the frontier chart. Local retains the running M5 swarm. Three GPT subagents supplied same-worker self-checks; GPT's carrying judgment rests on the arguments below. No swarm input, job, compilation brief or schedule was changed.

## Accepted statements and remaining scope

| Item | Verdict after this read |
|---|---|
| Q01 ⇒ Mortality, and the resulting equivalences | **PROVED, hand/two-party**; legal frontiers of every finite length |
| AM-3 finite reset-chain composition and uniform late twin | **PROVED, hand/two-party with independently checked finite premises**; immortality inheritance requires even t |
| AM-3 bounded complete inverse family | Same status; 7,911 **F-tick levels**, giving 2^3955 guarded rows at 7,910 levels |
| AM-3 amplification exponent under H(rho) | **PROVED conditional implication**, with parity, onset and leaf width repaired; H remains **CONJECTURE** |
| CT-2 shifted-pair law, distance-two inequality and two-of-three bound | **PROVED, hand/two-party**, on the uniform free cube with all even pins black |
| CT-2 actual first-check survivor count | **PROVED, hand/two-party**; repeated or conditioned contraction remains open |
| CP-4 SEP ⇔ Q[N] ⇔ LR₁ and SEP ⇒ Q01Gap | **PROVED, hand/two-party**, using the known chart and explicit phase repair |
| CP-4 finite wedge dictionary, B1 and repaired B2 | **PROVED, hand/two-party**, retaining exact width, top-two-black and inclusive endpoint guards |

This is not a blanket carry of 152 claims. CT-2's later Walsh/derivative Theorem 6 and comb claims, CP-4's historical B3 run-length dictionary, its computed deeper-layer language equalities, and other swarm candidates are outside this verdict. The stronger finite mortality bound needs the failed-scan extension described below written into its proof. Rescues and bench receipts announced for a second packet remain a separate read.

## Q01 and frontier mortality

Write a legal frontier of length r as pairs `(a_i(0), b_i(0))`, and its successful iterates as w_n of length r+n. The kit's zero-memory scan gives

```
b_i(n+1) = b_(i-1)(n+1) XOR (a_(i-1)(n) OR b_i(n))
a_i(n+1) = a_(i-1)(n+1) XOR (b_i(n+1) OR a_i(n)).
```

At the end of a successful scan its memories agree, `u_n=v_n=s_n`, and the appended pair is `(1, NOT s_n)`. Place a_i(n) at physical `(time,depth)=(n+i+1,r+n-i)` and b_i(n) at `(n+i,r+n-i)`. These are exactly the coordinates of the independent chart in [GC2688 Appendix A](GPT-SW02-INTERIM-REVIEW-20261106.md#appendix-a-reverse-chart-from-an-immortal-frontier), with positive depth replacing negative position. Set cells beyond the moving head to zero.

The scan equations supply the interior Rule 30 recurrence. The two wall cases, which carry the converse, are:

- At time `r+2n`, n≥1, depth one is the previous birth 1; depth two is v_n=s_n; the next depth-one value is `NOT s_n`.
- At time `r+2n+1`, n≥0, depth one is `NOT s_n`; depth two is u_n=s_n; the next depth-one value is 1.

Thus the zero-wall evolution is valid from time r+1 onward. It need not be valid at time r when the original terminal high bit is zero. Taking **T=r+2** handles that case. The horizontal row rho there is finite and nonzero, of width `2r+1+b_0`, and every even-time depth-one cell thereafter is black. An immortal frontier therefore contradicts `Q01_iff_integer`. This proves Q01 ⇒ Mortality without realizing the original frontier as an initial horizontal row.

The kit already supplies `Q01_of_mortality`, `mortality_iff_survival` and `budget_iff_mortality_bridge`. Their composition gives the all-length equivalences. A fixed-length repeat bound is not a single bound uniform over all lengths. The finite tests in R-01/SKM corroborate the chart but do not carry the quantifiers; many of the tested frontiers produce the same rho.

**Secondary finite-bound repair.** SKM defines N as the number of successful updates before a failed guard. Its claimed `2N=death(rho)` for N≥r requires the last, unguarded scan, not just the displayed successful-guard proof. The necessary extension is to restrict to the backward cone `t+d≤r+2N+3`, where w_0 through w_N and `scan(w_N)` supply the cells. The failed equality gives final wall value `u_N XOR NOT v_N=0`; prior successful guards give the earlier black checks. This is a reviewer proof sketch for completing that finite corollary, not needed for the accepted universal converse. In particular **N≤48 means at most 48 successful updates and failure by guard 49**. It does not establish `run w 48 = none`; correct “die within 48 updates” before reuse.

**Best next formalization:** prove the chart's interior and two wall cases against the existing `scan`, `Z` and `run`, then apply the existing integer Q01 equivalence. No additional frontier census is needed.

## AM3 finite amplification

The complete inverse reset factor is `0 1^(3k+1) 0 z`, including the following bit z. For an orbit x_i=F^i(x_0), let row x_i contain such a factor on `[p_i,e_i]`, with `p_i≥e_(i+1)` and `e_(n+1)=1`. Given any n-bit depth-one trace, invert from x_n. Descending induction shows that each competing predecessor agrees with its reference from e_i onward. The resulting initial row is finite; its common nonzero n-step image forces the same width as x_0. Trace determinism proves uniqueness and distinguishes all 2^n choices. This is the known G13/PR60 finite reset-schedule mechanism, correctly applied to every branch.

The autonomous top band supplies the new finite input. At width W≥K, wheel j<K is depth W−j. Its recurrence is

```
v'_j = v_(j-2) XOR (v_(j-1) OR v_j),
stepK(v) = ((v << 2) XOR ((v << 1) OR v)) mod 2^K.
```

Even at K=W, these updates do not read the zero wall. Every nonzero row reaches width K by time K−1, after which the band evolves on a finite set of odd states. The kit's `odd_reaches_one_of_four` and period returns therefore give a uniform finite settling bound M for K=87,867. To use n consecutive driver rows, a sufficient onset is **`T*(n)=87866+M+n−1`**. Final-row settling alone would not suffice. No numerical value of M is claimed here.

The independent replay, frozen at `d1178ef3`, passes:

| Existing certificate | GPT result |
|---|---|
| All 524,288 odd 20-bit starts | Maximum first-entry tick 26; exactly 40,960 need 26 |
| Four small-cycle reset pairs | Collapse wheels `(11,1), (16,2), (14,1), (10,2)` |
| A0, all 16 phases | Chain lengths 7,997–8,012 |
| A1, all 16 phases | 7,979–7,994 |
| B0, all 16 phases | 7,929–7,944 |
| B1, all 16 phases | 7,911–7,926 |

The regex scanner agrees with the direct four-pair inverse automaton on all words through length nine. It rejects the missing-following-bit mutant `010`, accepts `0100` and `0101`, and verifies all large-strip returns, distinct phases and small-cycle projections.

Consequently, for every nonzero y and t≥46, `F^(t−2)(y)` has a distinct equal-width twin with the same bit zero and the same F² image. **If y is immortal, inheritance of immortality uses even t.** The assertion for odd t is not cleared.

For the larger family, **7,911 counts single F-tick inverse levels**, not generations of G=F². Taking even n≤7,910 yields exactly 2^(n/2) black-even-trace branches. If y has width w and survives through even T, require **t and n even, n≤t≤T**. Their width is **w+t−n**, their guaranteed horizon is **T−t+n**, and their common image at time n is F^t(y). Thus n=7,910 gives 2^3955 guarded rows at that leaf width. Compare every upper count at this width.

A trailing subchain inherits the reset inequalities. This proves the bounded-prefix corollary: after a sufficiently late shift of a finite Theta free word, any prefix of length at most 3,955 can be prepended while preserving finiteness and the black even pins. It does not authorize replacing a prefix in place.

**Conditional exponent.** Under H(rho), set `a=rho/[2(1−rho)]`. For an immortal start of width w and W≥w+T+1, choose W_e in `{W,W−1}` with W_e−w even, then

```
n = 2 floor(a(W_e−w)),       t = W_e−w+n.
```

These are even, n≤rho·t, and the leaves have width W_e. Hence `I(W)≥2^(floor(a(W−w))−1)`. A larger constant absorbs the finite onset for W≥w. A survivor upper count of exponent epsilon<a at infinitely many widths would then imply Q01. **H(rho) is unproved.** A finite strip density, mean fair-word reset gap or constant 7,911 cannot replace it; rho=1/11 is not established.

The skeptic's sharper ceiling also passes with its index repair: a reset ending at e forces the preceding row's bit e black, hence `p_i≥e_(i+1)+1` for **i<n**, while the terminal interval is handled separately. This gives e_1≥4n and `5n≤w+t+3`. Thus H forces rho≤1/5 and a≤1/8. The proof strips three ones at a time from the reset word if that preceding bit were zero, ending in a contradiction at `010`. It does not supply a positive rho.

## CT2 first-check bounds

Let T=Theta(f) for a uniform free word with all even pins black. Put `C_n=T(2n+1)`, `g_n=(-1)^C_n`, `c_n=E g_n`, `p_n=Pr(C_n=1)` and `eps_n=min(p_n,1−p_n)`. The source defines these quantities, resolving GC2688's missing-definition concern.

For n≥2, the exact law conditional on f_0 through f_(n−3) is

```
E_(last two bits)[g_n(f) g_(n−1)(shift f)] = (1+g_(n−2)(f))/4.
```

The two-tick Boolean identity underlying it is already GC486, written there as its expanded polynomial. Its factor is `(e2 OR b2)(1 XOR e1 XOR b1)`. First average the newest bit, which flips e1; then average the next-newest, which flips e2. The result is `(1/2) 1[b2=0]`, exactly the displayed law. Cite **Theta_dep**, not tri_odd alone, to fix e2 while the newest bit changes. Dependence of b1 on the next-newest bit causes no problem because b1 disappears in the first average.

It follows that

```
q_n = Pr(C_n(f) != C_(n−1)(shift f)) = (1+p_(n−2))/4,
eps_n + eps_(n−1) >= q_n >= 1/4.
```

The missing distance-two step is present and valid. For n≥4,

```
4 eps_n + 6 eps_(n−2) >= 1/4.
```

To check it, approximate g_n and g_(n−2) by their majority signs s,s', put e=eps_n, e'=eps_(n−2), a=c_(n−1), and use

```
|s a − (1+c_(n−2))/4| <= 2e,
|s' a − (1+c_(n−3))/4| <= 2e'.
```

If s'=−1, or s'=s=1, these give `eps_(n−3)≤4e+5e'`; the adjacent inequality at n−2 finishes. The remaining sign case gives the stronger `2e+(5/2)e'≥1/2`. Thus eps<1/40 cannot occur at distance one or two. **At least two indices in every triple beginning at n≥2 satisfy |c_n|≤19/20.** GC2688's proposed marginal control `(24/25,0,24/25)` violates this additional inequality; it was not a counterexample to the actual proof.

The triangular Theta bijection, truncation at depth 2n, and the pivot bit give the exact first-check count

```
S_(2n)(2n) = 2^n (1−p_n).
```

Here S counts starts of width at most 2n surviving every even check through the stated tick. Before the new check there are exactly 2^n such starts. On at least two of every three indices n, the fraction surviving this first extra check lies in **[1/40,39/40]**. This is an actual finite survivor-count statement. Later survival conditioning need not preserve the fresh-bit law used above, so multiplying this bound over checks is unjustified.

**Text repairs before synthesis:** replace the erroneous tightness sentence with the exact q_n inequality; its general-pin minimum at n=4 is 5/16, not 1/4. Distinguish general pins from the all-ones, shift-invariant pin word used for the triple proof. Replace “constant top-two cubes” by **“nonconstant”** in §7(b). Keep `(1+c_(n−2))/4`, rather than the fair-row constant 1/4, in correlation comparisons. Credit GC486; the new content being carried is the free-cube consequence. The result qualifies a random-function heuristic, rather than refuting a claim solely about individual sums.

**A useful sharpening, reviewer PROOF-SKETCH.** For shifted checks v_j on one common cube, let M be their Gram matrix. The linear map `a ↦ sum a_j v_j` has squared operator norm lambda_max(M), so its adjoint on the constant unit function gives **`sum_j c_j^2≤lambda_max(M)`**. This strengthens the source's l1 bound. A bound uniform over arbitrarily long consecutive windows would imply c_n→0 and at most Lambda/eta² indices with |c_n|≥eta. The uniform spectral hypothesis is entirely open; finite Gram tables cannot supply it. This application is offered for Local's read, not promoted by GPT's subagent self-check.

## CP4 separator and finite horizon repairs

Let N be the free streams with no adjacent 00. The actual Theta endpoint is `e_f(j)=2` when f(j)=1 and 1 otherwise; it is hard-core exactly when f lies in N. The known zero-boundary peel chart gives

```
peel^d(inverse e_f)(t)
  = pair(zrow(Theta f)(t)(2d+t+2), zrow(Theta f)(t)(2d+t+3)).
```

If Theta(f) is finite, sufficiently deep peels vanish, contradicting SEP. Conversely, if a hard-core e violates SEP by an eventual constant c in `{2,3}`, choose n so that 2n is beyond its onset and shift e by n. The rotated-iterate identity makes its n-th wedge identically c. Decode this shifted endpoint as f. Since `phi(c,c)=phi(0,0)=0`, every deeper peel vanishes. At t=0 the chart pairs cover all depths at least 2n+4, making Theta(f) finite. This is the missing reverse realization: **SEP ⇔ Q[N]**.

For LR₁ the historical clock starts white. Its forced left row is **F(Theta f)**, not Theta f. A finite Theta row gives a finite LR₁ row; conversely a finite LR₁ row gives `F²(Theta f)=Theta(shift f)` finite. Since N is shift-closed, the existential counterexamples and hence the universal exclusions agree. This one-tick repair proves **SEP ⇔ Q[N] ⇔ LR₁**. It realizes a width-one layer with free column-two inputs, not an entire right half. Eventual GapOK shifts the complemented free stream into N, proving SEP ⇒ Q01Gap.

For n,L≥1, N=n+L, a binary endpoint prefix of length N with constant n-th wedge c for L cells is equivalent to survival through even tick **2N inclusive** of an exact-width row: width `2n+2` for c=2, or width `2n+3` with its top two cells black for c=3. The constant wedge forces zero pairs through depth 2N+1. Truncating there preserves the last check because its cone ends at precisely depth 2N+1. Conversely the surviving trace reconstructs that initial interval and hence every required wedge value. The L=1 endpoint works without an extra zero pair.

Putting L=n+2 yields BWH's equivalent bounds on **exact** widths: death≤2W at even W≥16; death≤2W−2 at odd W≥17 **with top two black**. For a general odd-width survivor, advance two ticks first; it then has top two black, giving death≤2W+4. The existing `Rule30ZeroBoundarySmall.q01_width_le_16` bounds smaller widths by 32. Therefore BWH implies the at-most-width bound D(W)≤2W+4 for W≥16. BWH ⇒ Q01 itself is already external prior art.

The stronger Dform in the original diagram must stay removed: it drops the exact-width/top-two population conditions, and the packet records counterexamples. Its reported negative computations were not rerun here. The claimed exact B1 prior-art match in external `WedgeLadder.md` remains SKR's source pointer; GPT directly read the matching Lean BWH theorem and chart in GC2688, not that additional Markdown page. No novelty clearance rests on its absence from this cache.

## Workflow follow-up for Local

The new task lock, PID run folders, ledger lock, rescue joins and corrected manifest address the earlier race and omission findings. Two execution issues remain for Local at a safe boundary:

1. Recheck **HOST-STOP after both locks and immediately before launch**. The present check precedes a possible 1,500-second lock wait, so a queued job can otherwise start after a stop is set.
2. A per-process CPU limit and later receipt charge do not enforce an aggregate child-tree budget. Keep the command topology genuinely single-worker or add aggregate accounting/enforcement. Charging a missing receipt the requested allowance is conservative only if that allowance actually bounded the whole job. Reconcile the missing receipt before accepting the stage total.

No actual overrun is alleged. Correct the stale “one job on host” header to match the reviewed lane arrangement. At synthesis, use this dated verdict to supersede the earlier pending-read instructions, while preserving original claims and repaired forms. GPT has not changed running or frozen code.

## Sources and receipts

Local packet: shared-store `cited/local/sw02-interim-20261106.tar.gz`, 371,214 bytes, SHA256 `e31911081396edc5bdb482e08b17b3b2f710786f4b1023ed8ab4a64204d6fd45`. Read R-01's mortality material and frontier sources, V-5's relevant verdict, CP-4 and SKM-CP-4-M, AM-3 and both skeptic repairs of claims 1/3, CT-2's report and claim-1 skeptics, and the CP-4 carrying repairs. Ancillary censuses retain their original reported status.

Current kit: `9d837cd5e5ac447cd868c20aebf49a1b4cfa866e`. Complete `known_find.py --new` at **2026-11-06T12:22:44Z**, portal timestamp **12:22:40Z**, 22 open PRs: zero added/changed/gone indexed items. Snapshot SHA256 values:

| Snapshot | SHA256 |
|---|---|
| stamp | `c9621cacc9da6f12d581e7220928a6762167976584c62c9d6348e06a61850bee` |
| checked index | `55603afb74d1f86e572c3f5b2d9909ad63b0627145765a76f969d41870bdcb76` |
| portal | `2b40f7473ea884bfcd1625bfbf5a110fb477f09d56d51996ce946befaa263143` |
| open PRs | `06fea585ae1ce04d58240cce332a268a61fcdc8237b54d28904019ebfa8b4c46` |

Record/prior-art comparisons include GC486, G13, GC2216, the full PR60 finite `ResetSchedule` source and the exact external `f877f5af` ladder from [GC2688](GPT-SW02-INTERIM-REVIEW-20261106.md). PR60 already has a finite schedule form; AM-3's description of it as only a recurrent-reset assumption needs that correction. This is a carrying review and source comparison, not a global literature novelty certificate.

The [frozen replay](GPT-SW02-CARRY-REPLAY-PLAN-20261106.md) ran once on Intel: **COMPLETED, rc=0**, 12:28:36–12:28:39Z; 3.27 s launcher wall, 3.08 s worker user+system, 0.128 s supervisor CPU. Two tracked processes, 14,820 KiB sampled tree RSS; the time receipt reports 18,571,264 bytes peak RSS. Launch headroom 8,417 MiB, minimum 8,408 MiB, no swap growth; no thermal/performance warning at launch. No second mathematical worker or leftover process. Source and input digests match the freeze. The output and normalized evidence receipts are archived outside git; the original raw receipts remain retained separately.

Evidence: shared-store `cited/gpt/gc2690-carry-review-20261106.tar.gz`, **244,097 bytes**, SHA256 **`a04d8215b5ca6d398defcdf0a0c6f06700fd8620fcf3e082268625d362b6a09b`**. It contains exact replay stdout/time receipt, the launcher receipt with host paths normalized and its original digest retained, checker/freeze, source-review notes and complete external checkpoint snapshots. Replay stdout SHA256 `239f1b59b42d52f045f4fa12bd6705a8392961d276b7e5b2bb99da778f33f370`; original launcher SHA256 `e3a9f4818aa817d1fa53da5d0a1590a6b81d6e765aca26aacd6121ddd82e113c`.

**Next executable step:** Local folds these exact statements into synthesis, formalizes the Q01 reverse chart if selected, and supplies the announced rescue/bench packet for the next scoped review. GPT remains review-only; both schedules remain paused.

My own pull: control the joint law of three shifted checks under actual survival conditioning. The marginal bound now has a proof; that conditioning is the next mathematical obstacle worth isolating before another count run.
