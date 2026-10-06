# Exact finite-ensemble parity-tail information budget

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT44. Exact finite-ensemble
parity-tail information budget"; rebuild with `python3 proofs/build.py`. Edit the proof in PROOFS.md and this
summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

A remainder modulo 3^a can imitate only so many fair coin tosses; ask for more and the repetition shows.

**What it says.** If the remainder is uniformly random, the next d odd-or-even steps look like fair coin tosses,
with an exact error formula, as long as 2^d is much smaller than 3^a. Beyond that the steps are fixed by the
remainder and carry no new randomness. GPT also showed one tempting comparison with coin tosses fails for long
patterns.

**Why it matters.** It is an exact information budget: the Collatz state after the free bits can pay for about 1.58
a fair coin tosses and no more.

**An everyday picture.** A deck of cards can fake only so many coin tosses; deal enough and the deck repeats.

## The formal statement and proof

**Where:** RULE30-GPT.md G44, 2026-10-06; copied verbatim. **Bears on:** PERIOD-TWO.md §7 question9 and COLLATZ-PRIZE.md §4. **Status:** complete finite-counting argument and single-party exact controls; second-read by Local, 2026-10-06 (note below). No stopping-time count bound.

### G44 theorem and proof: resolution of a finite residue ensemble

Fix odd M=3^a, a>=1. Let q be uniform on the least representatives0,...,M-1 and y=M+q. For d>=1 put B=2^d. The parity bijection identifies the first d parities of y with y moduloB, through a permutation of the B labels. Therefore its total variation distance from uniform d-bit words equals the variation distance of y moduloB from uniform residues moduloB.

Write M=kB+r with0<=r<B. In any M consecutive integers exactly r residue classes occur k+1 times and the others k times. Hence the variation distance is exactly

    TV = r*(B-r)/(B*M).

Indeed the r excess masses have difference(k+1)/M-1/B=(B-r)/(B*M), and the remaining deficit masses have difference1/B-k/M=r/(B*M); their summed absolute differences divided by2 give the displayed value. It follows that TV<=B/(4M). When B>=M the same formula becomesTV=1-M/B. Thus the approximation improves for coarse binary resolution, but becomes sparse when the requested word population greatly exceeds the initial residue population.

**Information statement.** When B>=M, distinct q give distinct y moduloB, and hence distinct d-parity words. The map is then injective on the entire initial ensemble. For any distribution of q, the Shannon entropy of these words equals H(q); for all d it is at most H(q)<=log2(M), because the words are a deterministic function of q. Uniform q gives entropy exactlylog2(M) once B>=M. This is a finite initial ensemble; it does not make the integer Collatz dynamics an autonomous finite-state system.

More generally, if the q law has support sizeN<=M, its word law has support at mostN and TV from uniform B words is at least1-N/B. Choose that support as the test event: its actual probability is1 and its uniform probability is at mostN/B. For a law uniform on N distinct q and B>=M, the distance is exactly1-N/B and entropylog2(N). Actual endpoint ensembles may have nonuniform terminal-q weights, so they must use their own support and law; uniformity on all M residues is an explicitly idealized comparison.

**Retained counterexample to an overstrong route.** Fix q0 and consider the actual d-parity prefix of y0=M+q0 at each d. For uniform q, once B>=M this cylinder has probability1/M. Its fair-coin probability is2^(-d). Their ratio is2^d/M and is unbounded with d. Thus no constant C can bound every cylinder's probability by C times its coin probability for arbitrarily long tails. No assumption about eventual behaviour of y0 is needed: every integer orbit has finite prefixes. The example refutes only a simultaneous all-cylinder comparison. It neither refutes the specially constrained stopping-time count in COLLATZ-PRIZE.md §1 nor predicts a divergent orbit. That target concerns a selected union of words whose paths stay above their start; some such events may become empty.

*Second reader's note on G44 (Local, 2026-10-06; chat L009).* Correct. Terras's bijection carries the parity-word
law to $y \bmod B$; the count of residue classes among $M$ consecutive integers gives the excess and deficit masses
$(B-r)/(BM)$ and $r/(BM)$ and so $\mathrm{TV} = r(B-r)/(BM) \le B/(4M)$; for $B > M$ ($B \ne M$, one odd and one a
power of two) $k = 0$, $r = M$, $\mathrm{TV} = 1 - M/B$, and the map from $q$ to words is injective; the support and
cylinder statements follow. Checked exactly against parity words computed directly from $y = M + q$ for $a = 1$ to
6 and $d = 1$ to 13 (78 cases, zero failures; `collatz_audit_g39_g42.py`, G44 part).
