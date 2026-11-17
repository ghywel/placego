# Rule 150 with the AND on even cells: the single seed's two-step orbit is exactly Rule 90, and its centre is white from time 2

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT265. Rule 150 with the AND on even
cells: the single seed's two-step orbit is exactly Rule 90, and its centre is white from time 2 (second-read,
2026-10-09)"; rebuild with `python3 proofs/build.py`. Edit the proof in PROOFS.md and this summary in
[summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

A Rule 150 variant with the extra AND applied only on even cells grows from a single black cell exactly like the simpler Rule 90, and its centre goes white for good.

**What it says.** Split the cells into even and odd. Every two steps, the even cells follow Rule 90's famous triangle pattern and the odd cells blank out. The extra AND does fire on the in-between steps, but over each pair of steps its effect reduces to a product of neighbouring even cells, and Rule 90's pattern never lights two neighbouring even cells at once, so that product is always zero. The centre of Rule 90's triangle is white after the start, so this variant's centre is black only at the first two steps.

**Why it matters.** It turns a measured curiosity from an experiment into a proof: here the centre's silence is permanent, not just observed for a while. It also shows how a carefully placed AND can cancel itself out over two steps instead of breaking the pattern.

**An everyday picture.** A correction that is applied and then exactly undone a moment later, because the lights it depends on always come on in alternating seats.

## The formal statement and proof

*Where:* RULE30-GPT.md GC835. *Credit:* GPT's proof of a pattern Local measured (AS, L455: white to row 16,383).
Independently read by Local (chat L458). A literal check of the exact description against direct simulation
agrees at every t < 3000. *Status:* hand proof verified by a second reader. Not a prize claim; an inhomogeneous
rule, not Rule 30. *Filed by:* Local, at GPT's request (GC835).

**Statement.** Let $x'(i) = x(i-1) \oplus x(i) \oplus x(i+1) \oplus [i \text{ even}]\, x(i) x(i+1)$, started from a
single black cell at 0. Then:
- at time 2n the odd sites are white and the even sites carry the nth row of Rule 90's single-seed orbit;
- at time 2n + 1 the even sites are unchanged and each odd site is the XOR of its two even neighbours;
- the centre is black exactly at times 0 and 1.

**Proof.**
1. With $a_i = x(2i)$ and $b_i = x(2i+1)$, the update reads $a_i' = b_{i-1} \oplus a_i \oplus b_i \oplus a_i b_i$ and
   $b_i' = a_i \oplus b_i \oplus a_{i+1}$.
2. If b = 0, one step gives a' = a and $b_i' = a_i \oplus a_{i+1}$. A second step gives b'' = 0 and
   $a_i'' = a_{i-1} \oplus a_{i+1} \oplus a_i a_{i+1}$.
3. Rule 90's single-seed rows are supported on one spatial parity, so the product vanishes and the coarse orbit is
   exactly Rule 90, by induction.
4. Its centre at coarse time n > 0 is 0. For odd n the central index is not an integer; for n = 2r,
   $\binom{2r}{r} = 2\binom{2r-1}{r-1}$ is even. ∎

*Scope (GC835).*
- On arbitrary rows the induced coarse map is not Rule 90: with a_0 = a_1 = 1 the product is 1.
- The m = 6 whitening AS observed is not covered.
- AS's other sparse-mask verdicts remain finite-window evidence.

*Near-entry gate (Local, at filing).* `--near G265` gives 31, 29 and G229 (all <= 0.10 on the formal text), read; none
is restated. Hard checks pass.
