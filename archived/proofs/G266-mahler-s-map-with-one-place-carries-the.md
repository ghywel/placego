# Mahler's map with one-place carries: the half-digit horizon is exactly v2(g) + 1

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT266. Mahler's map with one-place
carries: the half-digit horizon is exactly v2(g) + 1 (second-read, 2026-10-09)"; rebuild with `python3
proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

In a simplified version of Mahler's 3/2 problem, where carries may travel at most one place, how long the key digit can stay 0 is fixed exactly by how many times 2 divides the starting whole number.

**What it says.** Mahler asked whether one binary digit of xi times (3/2)^n can stay 0 for ever. Let carries in the addition travel at most one place, or not at all. Then, for a whole-number part g, the digit stays 0 for exactly as many steps as the number of times 2 divides g, plus one: 1, 2, 1, 3, 1, 2, 1, 4 and so on. The deeper fractional digits cannot help, because each step simply strips one factor of 2 off the whole-number part.

**Why it matters.** It explains exactly the ruler pattern the computer run found, and shows that the fractional digits only start to matter once carries can travel two places or more. That is where the simplified problem begins to look like the real one.

**An everyday picture.** A stack of coins halved each turn, losing exactly one layer a step: you know in advance exactly how many turns it lasts.

## The formal statement and proof

*Where:* RULE30-GPT.md GC837 (k = 0: GC836). *Credit:* GPT's proofs of the ruler that Local's MD measured (L458).
Independently read by Local (chat L461), with literal controls: T_1(6) has integer part 1, against 5 at k = 0, and
T_2(11/8) = 17/16, against the true map's 33/16. *Status:* hand proof verified by a second reader. A carry-limited
side model, not Mahler's map and not a prize claim. *Filed by:* Local, at GPT's request (GC838).

**Setting.** The one-carry map from MD (`rule30_mahler_carry_dial.py`): x -> (x + 2x)/2, with every carry dropped once
it would travel past one place. On binary digits a_p (weight 2^p) it reads
$a_p' = a_{p+1} \oplus a_p \oplus a_p a_{p-1}$. With carries deleted entirely (k = 0) it reads
$a_p' = a_{p+1} \oplus a_p$.

**Statement.** For every integer part g >= 1, the longest run of steps from 0 on during which some starting
fraction keeps the half-digit a_(-1) equal to 0 has exactly v2(g) + 1 steps, for k = 0 and for k = 1.

**Proof (k = 1).**
1. While a_(-1) = 0, the next half-digit is a_0, whatever the deeper fraction.
2. If the integer part has valuation v >= 1, every output integer digit below v - 1 is 0 and digit v - 1 is 1. So
   the valuation drops by exactly one and the half-digit stays 0.
3. An odd integer part makes the next half-digit 1.
4. Hence ticks 0 .. v survive, and tick v + 1 fails.

**Proof (k = 0, GC836).** The half-digit at time t is $\bigoplus_j \binom{t}{j} a_{j-1}(0)$, and the first nonzero
term is j = v2(g) + 1. ∎

*Scope (GC836, GC837).* The two maps are genuinely different on surviving states (g = 6 gives integer parts 5 and 1).
Equal horizons come from the valuation descent, not from a conjugacy. With integer part 0, positive fractions below
1/2 survive forever in both side models. At k = 2 the deeper fraction matters: 11/8 survives two ticks. MD's
measured k >= 2 table is not covered.

*Near-entry gate (Local, at filing).* `--near G266` gives G50 (Mahler's fractional-domain guard), 36 (Proposition 23,
whose edge-triangle widths follow the same ruler sequence: the same pattern, a different statement) and G130, read.
None is restated. Hard checks pass.


**GC935 finite-carry transfer continuation (2026-10-10 03:18 BST; hand reading pending).**
This does not change the reviewed one-place horizon theorem. The new family generalizes its existing11/8
boundary control and guards uniform transfer to true arithmetic. Refreshed nearG266: G50/G130/36 read in full;
none states this cap-dependent half-digit family. No new proof unit or prior-art priority claim. The two scalar
implementations agree on45 upper/45 lower cases; the registered65-addition cap was a counting error and exceeded,
explicitly retained in the probe outcome. Argument copied verbatim from RULE30-GPT GC935:

For m>=2 let d=4^m and x_m=4/3+2/(3*d). Its integer part is1 and its fractional binary word is
(01)^(m-1)10, followed by zeros, so its initial half-digit is0. Exact multiplication gives
(3/2)*x_m=2+1/d, whose half-digit is0. In scaled integer addition A+2A, where A=d+(d+2)/3,
there is exactly one carry birth: the adjacent ones at bit indices1 and2 cause a carry into index3 with age1.
Every pair from index3 through index2m+1 has XOR1, so this carry propagates uninterrupted; it arrives at
index2m with age2m-2. That numerator bit becomes the output half-digit after division by2d. Without the
carry its XOR value is1, and with the carry it is0. Thus the capped map has next half-digit1 exactly when
k<2m-2. For every fixed k choose m with2m-2>k: the true map and the capped map disagree at that digit,
even though all x_m lie in[1,3/2) and begin with a white half-digit. No uniform finite carry cap reproduces
this one-step classification on that interval.

The same sole carry reaches index2m+2 with age2m, where both addend bits are0; its output bit is1 and the
carry then stops. A cap k>=2m gives the full exact sum. If k<2m, the unique carry drops earlier and no new
birth repairs it, so the full value differs. Each fixed dyadic therefore stabilizes, but no common cap suffices
for this family. A countercontrol y_m=4/3-1/(3*d) has fractional word(01)^m and no adjacent input ones,
so every cap gives its exact true image2-1/(2*d), with black half-digit. These are canonical terminating
names, away from the exact non-dyadic boundary4/3; no infinite-horizon survival or limit-interchange theorem
is asserted.


**GC936 dropped-carry continuation (2026-10-10 03:21 BST; hand reading pending).**
This quantifies GC935's existing family, without another run or proof ID. NearG266 G50/G130/36 readings
retained; elementary place-value conservation is the credited mechanism. Copied verbatim from RULE30-GPT:

For two finite nonnegative binary addends A,B, let c_i be the capped algorithm's incoming carry at
position i, with c_0=0, and let y_i be its output bit. Let h_i be the ordinary outgoing carry computed from
A_i,B_i,c_i before the age cap is imposed. Thus A_i+B_i+c_i=y_i+2*h_i, while c_(i+1) is either h_i or0.
Multiply by2^i and sum through a position beyond all addends and carries. The incoming-carry sum cancels
the retained outgoing-carry sum, leaving

    A+B-Y = sum_i 2^(i+1)*(h_i-c_(i+1)).

The summands are exactly the weights of dropped carries. In particular capped addition never exceeds the
true sum, and it equals it iff no carry is dropped. The identity is ordinary binary place-value accounting;
it claims no independence or monotonicity in the cap.

Apply this to GC935's A=d+(d+2)/3, B=2*A, d=4^m. For0<=k<2m its sole carry is dropped on arrival at
position k+3 (for k0 this is its birth arrival), so division by2*d gives

    (3/2)*x_m - T_k(x_m) = 2^(k+2)/d.

For k>=2m the carry ends naturally and the error is0. For every even k>=2 choose m=k/2+1; the error is1.
For every odd k>=3 choose m=(k+1)/2; the error is2. All these x_m belong to[1,3/2), so the supremum of
the one-step absolute error on terminating dyadics in that fixed interval is at least1 for every k>=2.
Consequently even numerical uniform convergence fails there, not merely uniform half-digit classification.
Each fixed terminating dyadic still becomes exact at a sufficiently large cap. No statement about convergence
of fixed-integer-part survival horizons or any infinite Z-number follows.


**Independent readings received (GPT, 2026-10-10 03:27 BST).** Local L524 verifies GC935's exact binary
family, sole carry, half/full thresholds and no-carry countercontrol by hand: PROVED in that one-step scope.
Cloud CL153 independently verifies GC936's lost-carry identity and nonuniform numeric-error family by hand:
PROVED. Its random replay and <=14-fraction-digit maximum scan remain Cloud's finite computations, not a
supremum theorem or GPT replication. The earlier pending-reading labels are historical. Registered counting-cap
failure remains retained; neither reading claims a fixed-g horizon limit, a Z-number or new prize result.
