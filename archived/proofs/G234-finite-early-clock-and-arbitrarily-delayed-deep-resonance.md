# Finite early clock and arbitrarily delayed deep resonance

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT234. Finite early clock and
arbitrarily delayed deep resonance (second-read by Local, 2026-10-09)"; rebuild with `python3 proofs/build.py`. Edit
the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

A finite early clock does not prevent arbitrarily delayed resonance in a deeper white interval.

**What it says.** A fixed finite alternating centre prefix and a deeper odd white interval can be realized together in a finite seed. Independent far-left pivots make the interval midpoint stay white for any prescribed additional finite delay. Second reading pending.

**Why it matters.** An early clock prefix alone cannot exclude the resonant state; the later retained clock samples must interact with it. This is a composition of existing triangular and latch arguments, with no full RR clock witness.

**An everyday picture.** Two preparations occupy disjoint regions, so fixing one leaves the other free until the intervening dynamics brings them together.


**Finite-horizon extension.** If an odd white-block RR cone witness has a black nearer endpoint, its whole clock cone can be retained while outer pivots give any finite midpoint resonance delay. Those pivots first reach the clock strictly after its existing horizon; existence of the original witness is an explicit premise.

## The formal statement and proof

**Promoted from the waiting room, 2026-10-09 (Local L385).** Second reader: Local, chat L385. Waiting-room heading: "G234. Finite early clock and arbitrarily delayed deep resonance (GPT, 2026-10-08; waiting room, GC549.8)". The text below is unchanged, so its *Status:* line and "second reading pending" labels are historical.

*Provenance:* RULE30-GPT.md GC549 checkpoint 8, composing G130 and Cloud-reviewed GC496/GC513/GC515. Pre-filing reading near G130: G129, G60, G50. Candidate-neighbour reading under waiting-room ID W234: G130 and entries 12 and 06. The triangular component reuses G130; entries 12 and 06 require periodic regimes, absent here. The disjoint-clock/deep-resonance composition is not a restatement. No experiment or prize claim. Independent hand reading pending.

**Claim (composition of existing mechanisms, second reader pending).** For any finite h>=0, d>=h+2, m>=1 and K>=1, and either alternating clock phase, there is a finite-support Rule 30 initial row with that clock at column zero through time h, an all-white initial interval at depths d through d+2m-2 with black endpoints, and a resonant white run of exact duration m+K at that interval's midpoint. This is not an E(d,2m-1) witness unless its clock also lasts to d+2m-2, which is not asserted.

**Construction and proof.** Put c=-d-m+1. Set initial sites c-m and c+m black and every site strictly between them white. The nearer black endpoint is c+m=-d+1<=-h-1, so the entire prescribed patch is disjoint from the clock's cone [-h,h]. Choose initial sites in that clock cone to realize the prescribed finite trace, using G130's left-permutive triangular construction with nonnegative initial sites fixed except for the chosen initial centre phase. This fixes only finitely many sites and gives the clock through h independently of the farther-left choices below.

At s=m-1, the midpoint's two neighbours are black and its centre white by the reviewed GC496/GC513 arrival argument. Write b_k=x_s(c-1-k). Then b_0=1. For k>=1 the unique leftmost initial pivot in b_k is c-m-k, with XOR coefficient one. Every other input in its cone has larger initial index. Choose these pivots successively for k=1 through K so that b_k matches black at even depth and white at odd depth for k<K, and differs at k=K. This is the deterministic triangular mechanism used in GC515; no iid assumption is used. It makes the first checkerboard mismatch depth exactly K. Every new pivot is farther left than the black endpoint c-m and outside the clock cone, so it changes neither the initial white interval nor the prescribed clock prefix. Set all other unspecified initial cells to zero, giving finite support. GC513's right latch then gives the midpoint's exact white duration m+K; arbitrary cells to its right, including those chosen for the clock, do not alter this endpoint.

**Controls and scope.** For m=1, K=1, the local sites c-2,c-1,c,c+1 read 1101 and the midpoint trace begins 001, giving duration two. For m=1, K=2, a translated {-1,1} seed gives the known 0001 midpoint trace, duration three; the independent early-clock cone can be adjoined to its right. These reuse recorded hand controls, not a new experiment. The unexpected point is that both a genuine finite clock prefix and an arbitrarily long deep resonant delay coexist in one finite seed. A fixed early prefix alone cannot exclude the resonant state; later clock equations and their interaction with that prefix must do the work. This says nothing about an infinite clock, the full RR horizon or a uniform record bound.


**Conditional finite-horizon extension (GC549 checkpoint 9; second reading pending).** Take any actual E(d,2m-1) cone witness whose nearer initial endpoint at site -d+1 is black, and put T=d+2m-2. Keeping its entire initial cone [-T,T] fixed, it can be extended to a finite seed in which the white interval's midpoint has resonant white duration m+K for any finite K>=1. No claim is made that such a cone witness exists at an arbitrary d,m, or that its clock continues after T.

Put c=-d-m+1 as above. The interval's farther black endpoint c-m=-T-1 is outside the retained cone. Set it black. The arrival-row pivots for mismatch depths k>=1 are c-m-k=-T-1-k, also outside the cone. Choose them successively to give the first mismatch at K, and zero-pad all remaining unspecified cells. Radius-one locality preserves every clock sample through T and every prescribed initial zero in the witness. The same arrival and right-latch proof used in G234 gives exact duration m+K, regardless of the retained right exterior. This proves the conditional extension without any additional SAT run.

**Horizon control.** The added black endpoint first can affect column zero at T+1; the k-th arrival pivot first can affect it at T+1+k. Their coefficient at first arrival is one by left permutivity. For m=1 the white interval is a singleton at depth d, T=d, and its farther endpoint is exactly one site outside the clock cone. This checks the endpoint convention. The full finite RR clock therefore cannot itself constrain these outer resonance pivots. It can constrain the initial prefix inside its cone, and adding later clock samples can constrain newly exposed pivots; these are different obligations. A white interval with an unproved black nearer endpoint is not covered by this extension.

*Independent reading (Local L385, 2026-10-09).* Near-entry gate first (`proof_dupes.py --near W234`: G122, G243, G130, read; G234 reuses G130 by citation and restates none). Verified by hand: the patch sits at sites <= c + m = -d + 1 <= -h - 1, outside the clock cone [-h, h]; b_k = x_s(c - 1 - k) at s = m - 1 has cone c - m - k .. c - k - 2 + m, whose leftmost cell c - m - k enters with coefficient one by left-permutivity while every other input is already fixed, so the pivots can be chosen in turn; GC496/GC513/GC515 then give the exact duration. Checked literally by building the seed from the recipe: 1,344 parameter sets (both phases, h <= 6, d = h + 2 .. h + 5, m <= 4, K <= 6) all hold the clock through h, the white interval with black endpoints, and a midpoint white run of exactly m + K; every pivot flip flips its b_k. Checkpoint 9 checked the same way on 18 actual cone witnesses found by brute force (d = 2 .. 4, m = 1, 2): every extension K = 1 .. 4 keeps the clock through T = d + 2m - 2 and gives duration m + K (72 of 72). Scope as stated: nothing about an infinite clock or a record bound.
