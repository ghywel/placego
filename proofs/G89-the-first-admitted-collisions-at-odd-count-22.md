# the first admitted collisions, at odd count 22

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT89. the first admitted collisions,
at odd count 22 (second-read by Local, 2026-10-06)"; rebuild with `python3 proofs/build.py`. Edit the proof in
PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

Two surviving numbers can meet after all: the first pair appears at 22 odd steps.

**What it says.** The numbers 5,348,744,187 and 5,348,744,191 differ by 4. Each keeps its growth factor at least 1
at every step, each takes 22 odd steps, and after 34 steps both arrive at 9,770,112,830. Adding the same multiple of
2^34 to both gives infinitely many such pairs. With fewer odd steps no pair exists (G83 to G88).

**Why it matters.** It settles the question with a counterexample. The Collatz count's bookkeeping is nearly, but
not exactly, one to one, and the count has to allow for it.

**An everyday picture.** Two hikers who set off four doors apart, both always above their starting height, and meet
on the same summit.

## The formal statement and proof

### G89. Admitted terminal fibres are not always singletons (2026-10-06)

The count-22 run refutes the open all-a injectivity conjecture from L040. One explicit pair is

    n = 5348744187, n' = 5348744191,
    T^34(n) = T^34(n') = 9770112830.

Both starts have width 33. Their parity words, where 1 denotes an odd step of the halved Collatz map, are

    1101101101011011100110110110101101,
    1111111111011100100111011100001100.

Each word has 22 ones and satisfies 3^(prefix odd count) >= 2^(prefix length) at all 34 prefixes. This is checked by exact integer comparisons, separately from the actual trajectories. Their intercepts are B = 166780787837 and B' = 41256549401; their difference is 125524238436 = 4*3^22. The position-sum intercept formula and direct evolutions independently verify

    2^34*9770112830 = 3^22*5348744187 + 166780787837
                      = 3^22*5348744191 + 41256549401.

Thus the meeting is within G73's admitted common-width domain. It does not contradict G72-G73's multiplicity or short-label reconstruction theorems, which allow multiplicity; it refutes the unproved singleton conjecture. Since R_22 < 8, G83 bounds each same-count fibre by two, and this pair attains that bound.

**Infinite lift families.** For every integer k >= 0 add k*2^34 to both starts. The parity bijection preserves both 34-bit words and admission, and the common terminal becomes 9770112830 + k*3^22. For k = 0 their common width is directly checked. For k >= 1 both lie strictly inside the same length-2^34 interval, and every relevant power-of-two width boundary is an endpoint of such an interval; their widths therefore agree. This gives infinitely many admitted meeting pairs at the one horizon 34, not an asymptotic collision density.

Five least-residue pairs were independently validated; exhaustive enumeration of the accepting partition remains under RC3 audit:

| Smaller start | Larger start | Common terminal after 34 steps |
| --- | --- | --- |
| 5348744187 | 5348744191 | 9770112830 |
| 7435082747 | 7435082751 | 13581056558 |
| 11843133435 | 11843133439 | 21632881628 |
| 15231450875 | 15231450879 | 27822043514 |
| 15257926651 | 15257926655 | 27870404645 |

The a <= 20 analytic exclusion and a = 21 audited residue cover show that 22 is the first odd count permitting a same-count admitted collision, subject to independent review of those proofs and the coverage argument. This is a finite structural result, not a Collatz or Rule 30 solution. The failed BN1 prediction is part of its provenance; no novelty claim. Independent Local reading is requested at return.

### G89 accepting-cover outcome and finite classification (2026-10-06)

RC3 passes: 319 rejected residue classes and five accepting singleton residues form a pairwise disjoint cover of all 17179869184 residues modulo 2^34. Independent reasons are 167 admission failures, 132 offset-interval failures and 20 count failures. Every accepted pair passes the direct trajectory, all-prefix admission, odd-position affine and same-width checks, and first meets at step 34. The independent root span is below 8, validating the displacement-four reduction. A corrupted accepting residue is rejected. Predictions and checker at ca9d765; GPT Intel Python, under one second. No control failed. Certificate SHA256: 332752fd9bfb580e89c89722acee44daa9dcebd06507e97ba9bf416289799ace; data outside Git.

Consequently the five rows in G89 give precisely the five lower-start residue families at count 22 and horizon 34. Each family consists of the listed pair plus k*2^34 for k >= 0, with common terminal increased by k*3^22. No shorter admitted horizon with the same odd count can contain a collision: G81 would pad such a meeting pair by zeroes to length 34, producing an accepting code pair that already meets before step 34. Every accepting pair here first meets at 34; equivalently its two last parity bits differ, whereas a proper zero padding would make both last bits zero. This excludes that possibility. The first admitted same-count collision odd count is therefore 22, with the lower-count analytic and residue-cover proofs and this classification still awaiting independent model review. The singleton lead is closed by counterexample; no larger count run was resumed.

Probe: `tests/probes/prizes/collatz_gpt_accepting_cover.py`. This is a finite structural classification, not an all-count density estimate or a prize result.

*Second reader's note on G89 (Local, 2026-10-06; chat L046).* Correct, and confirmed by a different method.
`collatz_fibres.c` enumerates every admitted word (39,993,895 at $a = 22$) and finds every intercept collision mod
$3^a$ with no pruning; each realized pair is re-evolved directly, with the identity $2^t T^t(n) = 3^a n + B$ checked in
128-bit integers. Result: none for $a \le 21$, and at $a = 22$ exactly G89's five pairs (displacement 4, one width,
first meeting at step 34). The displayed identities, words, admission and the lifts $k = 1, 2, 3$ check (K4). The
engine's positive control: without admission, for $a = 3$ to 8, its pairs equal a direct scan of every start below
$2^{t+1}$ (C1). Extension (blind prediction, more pairs than at 22: held): $|W_{23}| = 87{,}986{,}917$, with 20
realized pairs, all of displacement 4, equal widths and exact, and none first meeting at the horizon 36: fifteen
first meet at step 35 and five at step 34. So at 23 every collision is a shorter-horizon meeting padded by shared
later bits; the $a = 22$ property that every pair first meets at its horizon does not persist.
