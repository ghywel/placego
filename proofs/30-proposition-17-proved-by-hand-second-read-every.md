# Proposition 17 (proved by hand, second-read): every actual Collatz demand law is unimodal

*Siblings, Jen and the squeeze. Derived from [PROOFS.md](../PROOFS.md), entry "30. Proposition 17 (proved by hand,
second-read): every actual Collatz demand law is unimodal"; rebuild with `python3 proofs/build.py`. Edit the proof
in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** second-read (GC469).

## In plain words

The Collatz demand laws always rise to a single peak and then fall, at every horizon.

**What it says.** In GPT's accounting of how Collatz-style survivors are spread over odd-step counts, each time step reshapes a "demand" distribution by one of two averaging moves. One move can create a dip on its own, but in the real schedule it never acts alone: it always follows the other, smoothing move, and that pair keeps any single-peaked shape single-peaked. So every actual demand law has one peak.

**Why it matters.** It supplies the shape condition an earlier comparison (G218) needed, so that comparison holds for every real case, not just the 1,024 horizons checked by computer. It orders the available error bounds; it does not bound the error itself or prove anything about Collatz.

**An everyday picture.** Pouring sand through two sieves in a fixed order: the coarse sieve alone can leave a ridge, but because the fine one always goes first, the pile that comes out still has a single top.

## The formal statement and proof

*Where:* chat L275, L276, L279; GC469; `tests/probes/prizes/collatz_demand_unimodal.py` (DU) and
`collatz_demand_unimodal_proof.py` (UP); GPT's `collatz_gpt_composite_shape_audit.py`.
*Bears on:* PERIOD-TWO.md's Collatz critical-boundary row and Q9; G74 (the demand), G218 (whose shape premise this
supplies), G219 (the opposite operator order), G220 (whose superlevel components become nested single intervals),
L048 (actual log-concavity fails from horizon 65).
*Credit:* the operators B and C and the synthetic guard are GPT's (G94, G219); the run over all laws to 1024, the
isolation argument and the lemma are Local's; the second reading, an elementary replacement for the strong-unimodality
citation and independent controls are GPT's (GC469). *Status:* second-read (GC469).

**Setting.** As in G74 and L048: $\ell_t$ is the least $a$ with $3^a > 2^t$ ($\ell_0 = 0$), and the demand at time
$t$ is the atom sequence $P_j = F_{t+1}(\ell_{t+1} + j) - F_{t+1}(\ell_{t+1} + j - 1)$ of the scaled backward survival
function. Going backward, a critical step ($\ell_{r+1} = \ell_r + 1$) acts by $C(p) = (p_0, p_0 + p_1, p_1 + p_2, \ldots)$
and a flat step by $B(q) = (2q_0 + q_1, q_1 + q_2, q_2 + q_3, \ldots)$.

**Proposition 17.** For every horizon $T$ and every $r < T$, the demand law is unimodal.

*Proof.* (1) $C$ preserves unimodality: with mode $m$ of $p$, $C(p)_{j+1} - C(p)_j = p_{j+1} - p_{j-1}$ is $\ge 0$ for
$j < m$ and $\le 0$ for $j > m$ (GC469's elementary form of Keilson and Gerber's strong unimodality). Applying $C$ twice
shows convolution with $(1, 2, 1)$ preserves unimodality, and a tail of a unimodal sequence is unimodal.
(2) Flat steps are isolated, because $\ell_{r+2} - \ell_r \ge 1$ ($2 \log_3 2 > 1$). So a flat step at $r < T - 1$ acts on
a law made by a critical step, and the law at $r$ is $B(C(p))$ with $p$ the law at $r + 2$; a flat step at $r = T - 1$
turns the terminal atom $(1)$ into $(2)$.
(3) If $p \ge 0$ is unimodal, so is $P = B(C(p))$: $P_0 = 3p_0 + p_1$ and $P_j = p_{j-1} + 2p_j + p_{j+1}$ for $j \ge 1$,
a unimodal tail by (1). If $p$ is nonincreasing, $P_{j+1} - P_j = (p_j - p_{j-1}) + 2(p_{j+1} - p_j) + (p_{j+2} - p_{j+1}) \le 0$ for every $j \ge 1$, so $P$ is unimodal whatever $P_0$ is. Otherwise $p_0 \le p_1$. If $p_1 \le p_2$ then
$P_0 \le P_1$. If $p$ peaks at 1, the tail is nonincreasing from $P_2$ on, and a valley would need $2p_0 > p_1 + p_2$ and
$p_2 + p_3 > p_0 + p_1$, which give $p_2/2 + p_3 > 3p_1/2$, impossible since $p_2 < p_1$ and $p_3 \le p_2$.
Backward induction from the terminal atom completes the proof. $\square$

*Scope.* G218's comparison (optimized centering is no worse than G74's original sum) therefore holds for every actual
law at every horizon. This orders discrepancy bounds; it is not a uniform small bound and not a Collatz statement.
Actual log-concavity still fails (L048), and G219's opposite order still fails on arbitrary input; its input is
$C(p)$ only for the non-unimodal $p = (40, 2, 42, \ldots)$. The same proof covers any binary threshold schedule whose
flat steps are isolated. Checks: every one of the 524,800 actual steps to $T = 1024$ is $C$ or $B(C)$ exactly, and every
actual law there is unimodal (DU, UP).

*Second reader's note (GPT, 2026-10-08; GC469).* Steps 2 and 3 verified, including the time order and the terminal
exception, with an elementary proof of step 1 in place of the citation. Independent pushforward controls pass on all
496 small unimodal vectors and 1,364 composite identities; the wrong order and a non-unimodal input both fail as they
should.
