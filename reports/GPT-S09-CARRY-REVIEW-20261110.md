# S09: exact counting algebra and the five-column ceiling

GPT GC2810, 10 November 2026. **Worker carrying read PASS for P2-3.1(a)-(e), with the scope below.** The hand implications are now PROVED two-party (Local's swarm source, independently read here); the fixed finite certificate was independently replayed. No new Lean module, notebook or submission is claimed. The n=6..10 graph table and additional measure/eigenvalue claims are not carried by this read.

## Sources read and disposition

Complete P2-3 report and claims, SKM-P2-3-1 report/verdict, SKR-P2-3-1 report/verdict and the original 32-value certificate were read from `cited/local/sw02-all-20261106.tar.gz`, archive SHA256 `c231157f6daeb1433d2c8aaf2e0190f78b5c4723009fdcc32ee8842a5c11d94c`. P2-3 report SHA256 `329fa8c0caf8b50c65fd7e3c036c29d91c79e3b544fc59d50c2e9cd4a4041e1b`; certificate `ad07d69b1fba2eab7ed71796f4166b80a78b6c2b2a91a7821c0d01cb0334e6fb`.

The deliverable should lead with the sharp **five-column bound**, and credit the earlier counting algebra as context. It must not present a new proof of Problem 2, a single-column density bound, a positive black-density floor, or a general window-table classification.

| Source | Actual hypotheses and conclusion | Comparison |
|---|---|---|
| [G4.1/G4.2](../archive/gpt/RULE30-GPT.1.md#g41-what-balance-means-algebraically) | Pointwise spin rule; space-time correlation identity with boundary errors; period-five density-3/5 travelling orbit | Same counting algebra in another basis and same sharpness orbit. Known, reproved here; no new extremality proof was in G4.2. |
| [GC2296](rule30-finite-mass-parent-count.md) | Nonzero finite physical row, white exterior; image count `r+2+2h` | Equivalent finite-row count after run/gap bookkeeping. Its further ancestry/counting claims are not upgraded by this read. |
| [Cappallo, OEIS A070952](https://oeis.org/A070952), Mathematica line dated 1 May 2021 | Program comment counts `10` plus twice `001` in the preceding seed row | Same one-step count with white padding. The displayed comment does not specify padding or prove the arbitrary-row statement. Credit it as an earlier counting formula. |
| [`Columns.ColumnTransfer`](https://github.com/lhallee/rule30-open/blob/1ddcd41186e245d6a001604e15b584981990591a/Rule30Open/Columns/ColumnTransfer.lean) | Actual `N` uses the singleton orbit, times `0..n-1`; transfer/dual transfer and iterates bound counts in different columns by factors 3 or 2 | Same local-bound summation idea, different inequalities. No absolute five-column ceiling or exact two-row count appears in this complete source. Its local proofs generalize, but that generalization is not a theorem already stated there. |
| [PR253](https://github.com/WolframInstitute/Rule30PrizeKit/pull/253), head `0cc954b55415f8102db6ba7fa46e8717e3f1b0a5` | Arbitrary streams with two neighboring updates: `3*C(T) <= T+5*A(T)+3`, where A counts run-end sources; separate eight-observation decoder | Actual entire head module, description, conversation/reviews/inline comments read (none at snapshot). Same bounded-potential method, different observable and source-dependent right side. No source-frequency estimate or five-column count. |
| [Fuks, local structure maps](https://arxiv.org/html/1304.8035), section 5, eqs113-114 | Exact update of block probabilities; then explicitly separate Bayesian approximations | Standard framework for the stationary cylinder identity. This section does not assert this Rule30 ceiling; approximations are not used in our proof. |

Primary `ColumnTransfer` at current external head `1ddcd41186e245d6a001604e15b584981990591a`: Lean SHA256 `2bf8a5786a9f46c809711f1cb56b424fbfde139448178a9f4d4ab4ec19cddbce`, note `3ee14bce4904ddec672d33e36538f86fa39d0a52e0d7be2c96f0f30eec304114`. The actual source also contains rightward/dual/iterated theorems omitted by the older Cloud summary; these were included in this comparison.

Record searched: `record_find` ColumnTransfer/P2-3.1; G4.1/G4.2/GC2296; actual current kit lean/equivalents and catalogs, portal sources and open PR sources for five adjacent/five-column/3T+2/three-fifths/count/density. Exact matching numbers in ClosingLaw are clock exponents; TraceEdge is a spatial offset in period exclusion; 0554f7 bounds a single black **run**, all different conclusions. Current external CATALOG and Berzai paper density hits were inspected. Targeted primary web searches found no matching five-column theorem. This is a bounded prior-art comparison, not a claim of literature priority or exhaustive absence.

## Conventions and carrying proof

Physical whole-line Rule30 is `F(x)(i) = x(i-1) XOR (x(i) OR x(i+1))`. Bits are integers 0 or 1 for counting. Windows read left to right; time count includes the initial row and excludes the final endpoint.

### Local identity and finite rows: valid, credited algebra

Set `g(a,b)=a-b+a*b`, with values `0,-1,1,1` on `00,01,10,11`. The identity is

```text
2*rule(a,b,c) + 3*b + [abc=101] + 3*[abc=000] - 3
  = g(b,c)-g(a,b).
```

The common values on `000,001,010,011,100,101,110,111` are respectively `0,-1,2,2,-1,-2,0,0`. This checks the complete local rule without an averaging assumption.

For a nonzero finite row with hull `[L,R]`, let `B` count black cells, `w=R-L+1`, `s` count internal one-cell white gaps, and `z` count `000` centers inside the hull. Sum the identity at positions `L-2..R+2`. Both flux endpoints vanish; the image support lies in `L-1..R+1`; exactly two extra `000` centers occur outside the hull. Thus

```text
2*B(Fx) + 3*B(x) = 3*w + 6 - s - 3*z.
```

This direct proof avoids depending on a solo earlier theorem. The nonzero guard matters: plugging width0 into this formula gives the wrong constant6. It is equivalent to GC2296's run formula using `s+h=r-1` and `w-B=s+2h+z`.

For the singleton trajectory `w(t)=2t+1`, since both support edges advance each tick. For `N(T)=sum_(t<T) B(t)` and analogous `S,Z`, summing gives

```text
5*N(T) = 3*T*T + 6*T + 2 - 2*B(T) - S(T) - 3*Z(T).
```

It also holds at T0; at positive T it yields triangle limsup at most3/5. The statement that triangle density1/2 is equivalent to `(S+3Z)/T^2 -> 1/2` uses `B(T)=O(T)` and is a restatement, not a transfer to one column.

### Invariant measures: valid elementary consequence, no new measure module required

For a probability measure invariant under both spatial shift and F, integrate the local identity. The spatial coboundary has mean0; time invariance gives

```text
5*mu[1] = 3 - mu[101] - 3*mu[000].
```

Both invariances are used. Therefore `mu[1] <=3/5`, with equality iff both indicated cylinders have measure0. Shift consistency also rewrites this as `mu[1]=mu[101]+3*mu[100]`. The uniform measure on the five translates of `(00111)^infinity` is invariant under F (a shift by2 there) and attains3/5. This is credited one-block stationarity/sign-definite rewriting of known algebra, rather than the main new headline.

### Five columns: independent certificate and exact telescope

For `u=(u0,u1,u2,u3,u4)`, put

```text
H(u) = max(0, 2 - (u1+u2+u3+u4)).
```

It is exactly the original certificate on all32 words, range0..2. For any seven input cells, let u be the middle five and v their five physical updates. The finite carrying inequality is

```text
pop(u)-3 <= H(v)-H(u).
```

A hand check reduces the cases further. If the right four cells have population0 or1, the right side needed of H(v) is nonpositive. If that population is at least2, H(u)=0, so population at most3 is immediate. If u has four black cells, at most one of the right four output cells is black: checking the five possible positions of the zero suffices, with the right exterior still free. If u is all black, those four outputs are all white, independent of exterior cells. These give H(v)>=1 or2 as needed. The separately replayed128 edges retain both exterior inputs and handedness.

For every actual trajectory, any starting time A, any five adjacent physical columns and every T>=0, sum along its actual window words:

```text
C5(A,T) <= 3*T + H(u_(A+T)) - H(u_A) <= 3*T+2.
```

No recurrence hypothesis on a fictitious window walk is substituted for an actual orbit: every orbit supplies a legal edge, which is all the upper bound needs. Equivalently the five columns contain at least `2*T-2` white cells (trivial when this lower bound is negative).

Constant2 is minimal already at T1 on a real row whose window is all black; it can be a finite row. Slope3 is minimal: the fixed alternating row with window10101 has three black cells every tick; the known period-five orbit also gives three black cells per tick in every five-column window. Neither is the singleton and neither is a counterexample to a prize claim.

## Fixed independent replay

Source [s09_read_check.py](../tests/probes/swarm/sw02/block12/s09_read_check.py), SHA256 `224bfba6363f37b48679f674f9aa4978e70732b71115366e112d2164955cd318`, private-plan digest `10ee25fb7fb9a5b6385413766150567df21fd9569f8d9a165770406342742867`, committed freeze `c687f664`.

One fixed Intel scalar job **COMPLETED/PASS**: 8 identities,32 certificate entries,128 edges,70 tight edges; mirror8/damage3/rule15016 violations as predicted. Literal finite rows1..1023 and singleton endpoints0..30 agree with the credited formulas. The period-five ring returns after five steps with counts `[3,3,3,3,3]` in its columns. No Karp run, seed horizon enlargement, Lean or Wolfram run.

Aggregate CPU including outer monitor0.273142s, wall0.54s; child self peak RSS12,455,936bytes (wait4 peak12,541,952bytes), free-memory launch5605MiB, swap growth0, normal thermal controls. The job was too short for a live tree sample: recorded sampledRSS0 is not a claim of zero memory use. Freeze:8 aggregateCPU/45stagewall, child5CPU20wall, outer15CPU60wall, tree768MiB/max6, launch4096/running1024MiB, swapgrowth4096MiB,4MiBfile16MiBstage. No job remains.

## Small formalization scope and exact next step

Local should add, when its current build is free, one small core module using the official rule/evolution definitions:

1. `potential` H, its bounds, and the local seven-bit inequality (finite Boolean check).
2. The endpoint telescope for arbitrary trajectories/windows, then `C5<=3T+2` and the white-count corollary. Preserve arbitrary starting time and T0.
3. Sharp constant at T1 and sharp slope using an explicit fixed alternating row or the credited five-cycle.
4. Optionally the eight-word sign-definite identity as credited context; finite-row support bookkeeping is useful but should not delay this small module. No new abstract probability or limit library is needed.

The n6..10 graph means, all-width optimality, n2/n4 realizability claims, eigenvalue/entropy extension and seed-only density question remain outside this release. Their computations were not rerun or independently certified here. Standard graph-potential/Karp methodology, ColumnTransfer, PR253 and known count formulas must be credited. No further exploratory census is requested. GPT next reads returned release packets; new module/notebook/source/essay still need their ordinary release read before posting.
