# GC2004 — alternate ticks explain the inherited-weight exception

28 October 2026. Independent GPT work while Local is offline, authorized by the owner. Hand consequences below are PROOF-SKETCH awaiting a later independent read; finite outputs are COMPUTED with independent implementations within this GPT run, not a second-party review. No novelty claim for the general parity algebra.

## Question and record

GC2002 left inherited-period diagonal weights unresolved. What extra information distinguishes their odd and even weights? The frozen GC2003 specification and source preceded the one completed check. Record search: `record_find.py 'linear complexity|Hasse derivative|even.*forcing|weight parity|binomial.*parity'`; G161's temporal-difference reformulation read. A later targeted search for consecutive doublings recovered GC763 in archive/gpt/RULE30-GPT.6.md, which already uses the OR half-period pairing below to forbid three successive prefix-period doublings. These are existing mechanisms being connected to the reconstruction question.

## 1. The missing bit is the forcing parity on alternate ticks

Write D(t+1)=D(t) XOR g(t), and suppose D has an even period P. Sum the adjacent pairs in one period:

    XOR_(t=0..P-1) D(t)
      = XOR_(j=0..P/2-1) [D(2j) XOR D(2j+1)]
      = XOR_(j=0..P/2-1) g(2j).

Pairing instead across odd ticks, using D(P)=D(0), gives the same answer as XOR g(2j+1). This proof works for every even P. It does not require minimality or a particular starting phase.

Thus the two alternating classes of the forcing have equal parity: either both even or both odd. Both odd gives an odd-weight diagonal, even though the forcing's TOTAL parity is even. This is the explicit criterion behind the inherited-period exception in L1062. It supplies a smaller statistic to understand, not a proven faster way to compute that statistic.

For Rule 30, g_d=D_(d-1) OR D_(d-2). The criterion therefore concerns the timing of the OR events on the two classes of ticks. Globally shifting a closed forcing does not change the answer: even and odd classes swap, but have equal parity. Relative feeder patterns still matter.

## 2. Period information really loses this distinction

Two generic forcing words, in time order, give closed integrals starting at zero:

| g | D | least period of g and D | black count in D |
|---|---|---:|---:|
| 11000000 | 01000000 | 8 | 1 |
| 10100000 | 01100000 | 8 | 2 |

Both have even total forcing parity and inherit period eight. In the first, each alternating class contains one event. In the second, the events share one class and cancel modulo two. These are controls for the generic integrator, not asserted Rule 30 diagonal pairs.

The actual single-seed calculation supplies an analogous distinction: diagonals 10 and 11 both have forcing period 64 and diagonal period 64, but their black counts are 32 and 31. Thus the period labels, including the fact of inheritance, do not determine weight parity even among these actual Rule 30 diagonals.

## 3. Why one doubling sometimes triggers another

Let P=2h. Suppose feeder a complements after h ticks, while feeder b repeats after h ticks. For each t,

    (a(t) OR b(t)) XOR (a(t+h) OR b(t+h)) = 1 XOR b(t).

The P-step forcing parity is consequently

    (h mod 2) XOR parity of b over h ticks.

For dyadic P>=4, h is even. The next diagonal doubles beyond P exactly when b has odd weight over h. If b's least dyadic period is strictly smaller than h, that weight is even, so doubling is impossible. If it is odd, b must have least period h. This is an exact conditional mechanism; it does not assume all diagonal periods are monotone.

Concrete single-seed instances, using the computed words:
- D4 has period 8 and complements at lag 4. Its partner D3 has period 4 and two black cells. The next diagonal D5 does not double beyond 8.
- D6 has period 16 and complements at lag 8. Its partner D5 has period 8 and three black cells. The next diagonal D7 doubles to 32.

GC763 already applies the same pairing: after two consecutive new prefix-period doublings, the shorter feeder is itself half-period complementary and has an even black count, so a third doubling cannot follow (with its stated even-base guard). The current work explains the inherited-weight exception in that same language. It does not re-open the older quantitative growth programme or establish a logarithmic asymptotic law.

## 4. Exact finite verification and resource receipt

Source: tests/probes/wolfram/diagonal_phase_parity.py, frozen at commit 7b7afd51. SHA-256 `f1f06277c33b7235d4dd2f2fd54288646837a9e9b8d568b85e79c0106e8ba7e5`.

- All 276 closed synthetic integrals of lengths 2, 4 and 8, both initial bits, satisfy the alternating-class identity. The P=2 half-period parity exception is retained.
- Diagonals 0 through 29 were generated recursively from complete periodic feeder words. Each forcing word is reduced to its least dyadic period before integration, and the resulting diagonal word is checked for minimality. This gives exact finite period computations by induction, rather than guessing a period from a forward sample.
- A separate forward implementation uses the literal eight-entry Rule 30 truth table as bit-parallel minterms on the full finite row. All 26,834 cell comparisons, covering two periods of each diagonal, match. Maximum computed period: 4096.
- The same-period controls give opposite weights as predicted. No failed assertion or scope widening.

One worker under run_capped.py: 30 s CPU, 45 s wall, 256 MiB sampled group RSS, 2 MiB per file, 4 MiB total artifacts, 1024 MiB launch and 512 MiB ongoing free+inactive headroom thresholds, 128 MiB swap-growth stop. Completed with return code zero. Child time: 0.20 s real, 0.19 s user, 0.01 s system; supervisor wall 1.04 s. Child maximum RSS from time: 14,495,744 bytes, not a system-memory peak. The job finished before the first periodic monitor sample; zero sampled RSS must not be read as zero memory use. CPU/file limits were configured by the standard launcher, launch pressure gate passed, and ongoing sampling thresholds were installed but never sampled during this short run. Final artifacts were under 6 KiB before the manifest.

Retained packet: `cited/gc2003-phase-parity/manifest.json`, SHA-256 `c93a87aeae20a3eb4543e2ea439027cb2a283f4c3830ec37780d6acc999ff767`. Contains source-commit binding and digests of results, output, timing and launcher receipts. Raw-body upload receipts and stored digests matched. No Local message or flag was sent.

## What changed

We now have an explicit alternating-tick criterion for the previously unnamed inherited-weight exception, an actual Rule 30 example showing why period labels alone are insufficient, and a connection to the known obstruction to repeated period doublings. These explain internal structure without claiming a centre-column theorem.

The next precise question is whether the alternating-tick forcing parities can themselves be propagated using a small sufficient collection of feeder statistics, or whether their update necessarily introduces additional correlations. That needs a defined collection and a counterexample/proof; the present identities alone do not establish closure. No further run is launched at this checkpoint.
