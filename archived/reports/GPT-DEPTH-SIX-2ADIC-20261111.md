# Depth six follows a signed-derangement profile

GPT, GC2932–GC2933, 11 November 2026. Owner-directed continuation of
[GC2931's error bounds](GPT-HIDDEN-CLOCKS-REVIEW-20261111.md#clouds-2-adic-cascade-with-explicit-error-bounds).
Both schedules remain paused. This is a complete proposed hand proof,
**PROOF-SKETCH pending Cloud's independent carry**. Same-worker reviews
and exact computations are self-checks, not that carry.

The sixth left diagonal of the chosen integer lift follows a fixed
2-adic function, at the inherited phase C−t. The onset remains explicit
for each modulus. A known valuation identity for this function then
determines the diagonal's zero phases and least eventual period.

## Statement and conventions

Use Cloud's lift of the single cell:

    A_(t+1)(j) = A_t(j-1) + A_t(j) + A_t(j+1) + A_t(j) A_t(j+1),
    A_0(j) = 1 if j=0, and 0 otherwise.

Write u_n(t)=1+A_t(n−t). Thus u_n(t)=1 for n<0, u_0(t)=2,
and u_n(0)=1 for n>0. The exact recurrence is

    u_n(t+1) = u_n(t) u_(n-1)(t) + u_(n-2)(t) - 1.

Let C be the 2-adic limit of u_3(t)+t. For k≥1 put

    r_k = min {r≥0 : v_2(r!)≥k},
    N_6(k) = k+2+2r_k.

Define, with the empty product equal to 1,

    F(x) = - sum_(j≥0) product_(1≤i≤j) (x+i),   x in Z_2.

Then the proposed conclusion is

    u_6(t) = F(C-t) mod 2^k,                 t≥N_6(k).       (1)

The onset is sufficient, not asserted optimal. Since r_k≤2k, the
simpler sufficient onset 5k+2 also works. Equivalently,

    v_2(u_6(t)-F(C-t)) ≥ floor((t-2)/5),     t≥7.            (2)

For every fixed k the least eventual period of u_6 modulo 2^k is
**exactly 2^k**. Beyond the stated onset,

    min(v_2(u_6(t)),k) = min(v_2(C+2-t),k).                 (3)

In particular, u_6(t)=0 modulo 2^k precisely at
t=C+2 modulo 2^k. These zero and valuation statements concern **1+A**.
Subtracting 1 gives A_t(6−t), with the same least period.

## Recovering the upstream bounds

This repeats the carrying steps from GC2931 so that the onset can be
checked here without an implicit asymptotic substitution. First,
u_1(t)=2^t and u_2(t)=1+2^(t−1)u_2(t−1) for t≥1. Also

    (u_3(t+1)+t+1) - (u_3(t)+t)
      = 2^(t-1) (u_3(t)u_2(t-1)+2),        t≥1.

The increments tend to zero 2-adically with valuation at least t−1.
Completeness and summation of the tail give the limit C and

    v_2(C-u_3(t)-t)≥t-1,                  t≥1.

Fix k and T=k+1. For all t≥T, modulo 2^k we have u_1=0,
u_2=1, u_3=C−t, and u_3(t+1)=u_3(t)−1. The depth-four recurrence
is therefore homogeneous. Its next r multipliers are consecutive
descending residues. A product of r consecutive integers is divisible
by r!, including for negative starting integers. Hence

    u_4(t)=0 mod 2^k,                     t≥T+r_k.

The next update then gives u_5(t+1)=u_3(t)−1=u_3(t+1).
Consequently, with S_k=k+2+r_k,

    u_5(t)=u_3(t)=C-t mod 2^k,            t≥S_k.            (4)

These are statements at a fixed modulus, with onsets depending on k.

## Construction and uniqueness of the profile

For every integer x, the j-factor product in F(x) is divisible by j!.
By density of the integers and continuity of that polynomial, the
same divisibility holds for every x in Z_2. Since v_2(j!) tends to
infinity, the series converges uniformly. Each summand is an integer
polynomial and is 1-Lipschitz, so F is 1-Lipschitz. In particular, its
residue modulo 2^k depends only on x modulo 2^k. The tail beginning at
j=r_k vanishes modulo 2^k, making every such profile a finite sum.

Removing the first term and factoring the remaining products yields

    F(x) = (x+1)F(x+1)-1,
    F(x-1) = xF(x)-1.                                      (5)

There is only one Z_2-valued function satisfying (5). Indeed, the
difference H of two candidates obeys

    H(x) = product_(1≤i≤r)(x+i) H(x+r).

The right side has valuation at least v_2(r!), because H is
Z_2-valued. Letting r grow proves H(x)=0. Continuity need not be
assumed for this uniqueness argument.

## Transport through the sixth recurrence

By (4) and the depth-four bound, the exact recurrence reduces to

    u_6(t+1) = (C-t)u_6(t)-1 mod 2^k,      t≥S_k.

The comparison sequence F(C−t) satisfies that same update by (5).
Its difference from the physical sequence therefore satisfies

    e(t+1) = (C-t)e(t) mod 2^k,            t≥S_k.

After r_k updates, the difference has acquired r_k consecutive
descending factors. Their product is divisible by r_k! in Z_2.
Thus e(S_k+r_k)=0 modulo 2^k and remains zero at all later ticks.
Since S_k+r_k=N_6(k), this proves (1), including its endpoint.

The argument forgets the incoming value of u_6 after a controlled
number of updates. It preserves the earlier ancestry in C. It does
not replace that phase with a fresh arbitrary clock or interchange
the time and modulus limits.

## Exact valuation, unique zero phase and least period

Only j=0 and j=1 survive in the defining series modulo 2, so
F(x)=x modulo 2. Applying (5) twice gives the useful factorization

    F(x) = (x+2)((x+1)F(x+2)-1).

The parenthesis is odd: modulo 2 it is (x+1)x−1=1. Therefore

    v_2(F(x)) = v_2(x+2),                 x in Z_2,         (6)

with v_2(0)=infinity. This includes x=−2, where F(−2)=0.
Combining (6) with (1) proves the truncated statement (3).

Compatibility of F gives a period 2^k for the tail in (1). To prove
minimality, let Q>0 be any eventual period of the physical sequence.
Choose t beyond both onsets with t=C+2 modulo 2^k. The values at t
and t+Q must both vanish. The unique zero class forces Q=0 modulo
2^k. Thus every eventual period is a multiple of 2^k, proving the
claimed least period.

Over a full eventual period the truncated valuation has exactly
2^(k−a−1) occurrences of a for 0≤a<k, and one occurrence of k.
This is an exact count for this diagonal. The residue distribution
itself is not uniform: at x=0,1,2,3 the profile modulo 4 is

    F(x) mod 4 = 2, 3, 0, 3.

Nor does (3) assert full integer valuation equality at every time
after one universal onset. Such equality at a particular t follows
if an admissible k is larger than v_2(C+2−t); otherwise the conclusion
at that t remains truncated. No centre-column distribution statement
follows from these fixed-depth results.

## Prior art and scope of the contribution

Record searched: GC2931 and CL777; separate record searches for
factorial and 2-adic; actual cached kit lean/equivalents/catalogues and
indexed portal/PR sources at the complete refresh
2026-11-11T19:06:45.230275Z, kit
`72fdf4b4a7b3dfd7a1fb4d956f971cdb69552e18`. The search found no matching
physical depth-six bridge. It does not establish a literature priority
claim. Nersissian's integer lift and Cloud's diagonal recurrence remain
credited in the preceding review.

The function F is **known, reproved here**. O'Desky–Richman,
[Theorem 4.5, equations (48)–(49)](https://arxiv.org/html/2012.04615v4#S4.SS2),
give a_p(y,r)=sum_j r^j j! binomial(y,j). Exactly

    F(x) = -a_2(-x-1,-1),
    F(-n-1) = -(-1)^n D_n,                 n≥0,

where D_n counts derangements. Thus the profile is a signed-derangement
interpolation, not a new special function. The elementary construction
above uses no incomplete-gamma exponential normalization.

The valuation identity is also **known, reproved here**. Miska,
[section 4.1.3, printed page 15](https://arxiv.org/pdf/1508.01987#page=15),
includes 2 among primes with v_p(D_n)=v_p(n−1). The factorization above
is the same derangement recurrence transported to Z_2.

For the broader recurrence context, Buckingham's
[section 2.3, Proposition 2.9](https://arxiv.org/html/2206.12726v2#S2.SS3)
treats continuous solutions of automatically seeded factorial-type
recurrences. Here G(y)=−F(−y−1) obeys G(y)=1−yG(y−1).
The application established by the proposed proof is the physical
tracking (1), its explicit onset, and the resulting exact diagonal
period and zero schedule.

## Exact controls and retained evidence

The source and limits were published before running, in GC2932 at
`6fc6ec606`. [The probe](../tests/probes/gpt_lift_depth_six_check.py)
passed on the Intel host. For k=1 through 12 it checks every residue
of F, its recurrence, valuation and unique zero; compares two full
physical periods beyond N_6(k); and checks compatibility of the
computed C residues. A full spatial integer evolution through t=12
checks the coordinate convention independently. Deliberately replacing
C−t with C+t is rejected. No failing result was discarded.

The declared caps were 15 CPU seconds, 30 wall seconds, tree RSS
768 MiB, three processes, 2 MiB/file, 8 MiB/stage, free-memory floors
4096/1024 MiB and swap-growth stop 4096 MiB. Run completed with rc=0,
0.286594 aggregate CPU seconds and 0.55 wall seconds. The child time
receipt gives maximum RSS 12,029,952 bytes. The process finished before
a periodic tree-memory sample; the receipt's zero sampled maximum
must not be read as zero memory use. Launch free/inactive memory was
5853 MiB, and host thermal/speed controls were normal.

Verified raw files are in the shared store:

| Path | SHA256 |
|---|---|
| `cited/gpt/gc2932-depth-six-check.py` | `4588760a6813a981ffc43b3b97713c4d5557c4a95534a700966b3782fa999605` |
| `cited/gpt/gc2932-depth-six-result.json` | `cf76f651f5a2c81527c42354ffa6922f0536ee3688ea7992763ca52acf46cd25` |
| `cited/gpt/gc2932-depth-six-launcher.json` | `11517e45117086bacf86746777874329fed3f196aacbd6f6e9668b1f1597df25` |
| `cited/gpt/gc2932-depth-six-time.txt` | `7f00ab4df955d102198f7bba34d1b78deaecaa2b25b5f385c0820aa23d53a1c4` |
| `cited/gpt/gc2932-depth-six-aggregate.json` | `fb0221b786d2c426b528508202455045f51526449b77e93bf0bbc31bd0e74f0d` |

The finite checks do not replace the all-k proof or independent carry.
No Lean build, portal submission or external verification is claimed.

## Next executable step

Cloud's carrying read should check the upstream onset S_k, the extra
r_k updates, and the passage from the known profile valuation to the
physical sequence's truncated valuation and least eventual period.
This also carries the upstream 2-adic part of GC2931 if accepted.

My own pull: use depth six's exact zero-phase valuations to control
depth seven's recurrence, u_7(t+1)=F(C−t)u_7(t)+(C−t)−1 modulo 2^k
after N_6(k), with an explicit onset for its response profile. This is
the next proof target, not a completed result or a scheduled job.
