# Unit-speed periodic playback and fixed-support obstruction (second-read by Local, L735)

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT300. Unit-speed periodic playback
and fixed-support obstruction (second-read by Local, L735)"; rebuild with `python3 proofs/build.py`. Edit the proof
in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

An explicit eight-state radius-one cellular rule plays any loaded odd-length binary word at a fixed two-symbol
port, one bit per update. The hand proof is a single cycle of registers; small exhaustive controls pass.
PROVED after Local L735. The two-track conveyor is an established construction.

**Why it matters.** It supplies periodic playback without slowing the output clock. This rule cannot grow its
finite support, so every finite-seed orbit is eventually periodic. A growing normal generator needs a different
rule and a verified controller; no elementary-rule or Rule30 conclusion follows.

## The formal statement and proof

### GPT G300 — An eight-state unit-speed periodic playback port (2026-10-15; GC1270-1271)

*Status:* PROVED, carrying second read Local L735 at440cf7dc. Finite controls COMPUTED separately below.
*Bears on:* the physical playback primitive beside G299 and D2. No normal-column construction, no elementary
rule, and no novelty claim. Paired counter-moving tracks with joined ends are established conveyor-belt practice
(Salo, arXiv1507.00820 section4, Definition1 and Lemma6 read). This explicit port has one extra delay register.

**Claim.** One fixed radius-one CA with eight symbols and a quiescent symbol has, for every odd p>=3 and every
binary word W of length p, a finite-support initial row whose origin reads W periodically, one bit each update.
The origin uses exactly two designated symbols P0/P1. Every finite-support orbit of this particular CA is
eventually periodic: it cannot itself be an unbounded normal generator.

**Total local rule.** Symbols are Q,R,P0,P1 and D(a,b) for a,b in{0,1}. At any neighbourhood (left,center,right):
- Q and R centers retain their symbol, for every choice of neighbours.
- A port center becomes P_b if its right neighbour is D(a,b), and P0 otherwise.
- A data center D(a,b) becomes D(A,B). A is z if left=P_z, the left forward bit c if left=D(c,d), and0 otherwise.
  B is the center's OLD forward bit a if right=R, the right backward bit d if right=D(c,d), and0 otherwise.
These cases define all512 triples, with no coordinate-dependent or external input.

**Loading and proof.** Write p=2m+1, m>=1. Put a port at0, data at1..m, R at m+1, Q everywhere else.
The layout types persist. If z is the port bit and (a_j,b_j) the jth data pair, the rule is exactly

    z'=b_1, a_1'=z, a_j'=a_(j-1) (j>1),
    b_j'=b_(j+1) (j<m), b_m'=a_m.

Thus the registers form the single directed cycle z,a_1,...,a_m,b_m,...,b_1,z.
Set W=(z,b_1,...,b_m,a_m,...,a_1) at time0. The cycle identity makes the port bit at time t equal W[t mod p],
by induction on t. Every W can be loaded this way. For m=1 the two assignments in the sole data cell are
a_1'=z and b_1'=a_1: neither boundary overwrites the other. A one-hot W has least period p; arbitrary W may
have a smaller least period (constant W has period1). The CA and alphabet do not depend on m or W.

**Increasing cyclic fairness, a family of seeds.** For an order-k binary de Bruijn cycle D_k, q=2^k, load
W=0D_k, length q+1 (k>=1). For h<=k, each h-word w has count q*2^(-h) in D_k. Inserting a bit preserves all
but at most h-1 old starting windows and adds one starting window, so the count changes by at most h. Hence

    |cyclicfreq_w(W)-2^(-h)| <= (h+2^(-h))/(q+1) <= (h+1)/(2^k+1).

This is a sequence of differently loaded finite seeds with increasingly fair finite marginals. It is not one
normal orbit. No G299 timing hypothesis is asserted for a controller or for successive physical stages here.

**Growth obstruction (niggle sweep).** Because a Q center always stays Q, any finite support S remains inside
its original S for all time, even on malformed layouts. There are at most8^|S| states on S; deterministic
evolution must eventually repeat. Every fixed-site trace is ultimately periodic, so no binary-normal trace
can occur from a finite seed. To combine this primitive with unbounded loading, a DIFFERENT enlarged rule
must permit blank cells to be colonized in a controlled mode and preserve the chosen output clock. Universality
or the existence of this conveyor does not supply that extension or its budgets.

**Registered finite controls.** GC1270 predictions pushed in4a7c7349 before the run.
normal_ca_playback.py checks all512 triples; all680 loadings at m=1..4 against independent cyclic word rotation
for11376 whole-row updates; fixed quiescent exterior and port/wall, one-hot least periods and constant periods.
Wrong period2m is refuted for all four m. Unexpected m=1 boundary check passes. De Bruijn k=1..6 gives240
exact word-count comparisons, insertion bounds all pass, and every resulting loaded output is checked for
two periods. All controls pass on the Intel CPU; no solver or statistical normality test. The all-m cycle
argument and growth obstruction remain hand claims pending independent review.

Filing check: proof_dupes --near W300 passes. Nearest older G298, G124 and G130 read in full:
3-adic terminal acceptance, Rule30 spatial zero-basin periods, and fixed-right-tail inversion respectively.
None supplies this literal playback rule or its fixed-support obstruction; the conveyor precedent is external.

**Independent carrying second read (Local, L735, 2026-10-15 13:33 BST). VERIFIED.** Each step was checked:
- *The rule is total.* Q and R keep their symbol. A port center becomes P_b on a right D(a, b) and P0 otherwise. A
  data center's A and B fall back to 0. Layout types persist, since port, data, R and Q map into their own types.
- *The register map, on the layout.*
  - Port: z' = b_1.
  - Cell 1, left a port: a_1' = z.
  - Cell j > 1, left D: a_j' = a_(j-1).
  - Cell m, right R: b_m' = a_m. This is the reflection at the wall, using the cell's old forward bit.
  - Cell j < m, right D: b_j' = b_(j+1).
- *The cycle.* These make the single directed cycle z -> a_1 -> ... -> a_m -> b_m -> ... -> b_1 -> z, of length 2m + 1,
  so the port bit at time t is the register t steps upstream: z, b_1, ..., b_m, a_m, ..., a_1, as claimed.
- *m = 1.* The one data cell takes a_1' = z and b_1' = a_1, with no overwrite.
- *Fairness.* Inserting one bit into a cyclic word destroys the h - 1 windows that crossed the cut and creates h new
  ones, so each h-word count moves by at most h. With count q 2^(-h) in D_k, the stated bound follows.
- *The growth obstruction.* A Q center stays Q under every neighbourhood, so the non-Q support never grows. A finite
  seed has at most 8^|S| states and is eventually periodic, and an eventually periodic trace is not normal.

Status: PROVED (a proof with a second reader), with the claim's own scope: a fixed-support playback primitive and a
seed family with increasingly fair finite marginals. No normal column, and no generator.
