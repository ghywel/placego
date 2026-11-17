---
Template: ComputationalEssay
Name: Three periodic phases behind Rule 30's black edge, excluded to bounded depth by a tree of top words
Author: Gareth Herbert - with Claude (Anthropic) and GPT (OpenAI)
Date: DRAFT 2026-11-03 (Cloud's packaging draft; Local assembles)
Description: A partial result proved in core Lean on the kit's edge-code objects: for three periodic phases of our record (G16, P1024 and a period-32 phase on a 480-cell ring), the longest episode at a chosen depth is 22, 24 and 24 ticks at every alignment, so no black-edge code follows any of them at every depth from some depth at most 14, 8 or 10 on; the certificate is a tree of top words, sound by locality, checked in the kernel.
Abstract: See abstract.txt.
Keywords: [rule 30, Rule 30 Prize, edge code, frozen ruler, phase, episode, eternal point, top-word tree, locality, Lean 4, LeanLink, partial result]
Sources: ["[The Rule 30 Prize kit](https://github.com/WolframInstitute/Rule30PrizeKit)", "[The Wolfram · Collatz · Mahler record](https://github.com/ghywel/placego)"]
Links: ["[Rule 30 Prizes](https://rule30prize.org/)", "[R30-20261103-d37d24: episodes and eternal tails behind Rule 30's black edge](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261103-d37d24)"]
---

## The question

Read a row of Rule 30 from its rightmost black cell, as the kit's `Rule30FrozenRuler` does: bit $j$ of the **edge code** is
the cell $j$ places behind the edge, and the code evolves by the edge map $T$, $T(c)_0 = c_0$, $T(c)_1 = c_1 \oplus c_0$,
$T(c)_{j+2} = c_{j+2} \oplus (c_{j+1} \lor c_j)$. A **phase** is a family of depth columns $E_j(t)$ that obeys the same rule at
every depth $j \ge 2$ and repeats in time with period $p$; an **episode** of $T$ ticks at depths $k, k + 1$ is a run of ticks
on which those two depths of a black-edge code follow the phase (our R30-20261103-d37d24, whose definitions this entry restates
verbatim). That entry showed finiteness of the longest episode is a finite question. Here it is answered, in the kernel, for
three phases our record found and tabulated by computation.

## The three phases

- **G16**: the 128-cell ring $y$ with $c(y) = \rho^{72} y$ for the frame map $c(y)_n = y_n \oplus (y_{n-1} \lor y_{n-2})$, so
  $E_i(j, t) = y((j + i + 56t) \bmod 128)$ has period 16 in time; one spatial alignment $i$ per phase.
- **P1024**: a 1,024-cell ring with lag 21, $E_i(j, t) = y((j + i + 1003t) \bmod 1024)$, period 1,024.
- **The 480-phase**: a 480-cell ring whose frame image after two steps is its rotation by 270, carried by two words $z_0, z_1$
  with $E_{r,s}(j, t) = z_{(t+s) \bmod 2}((j + r + 210\lfloor (t+s)/2 \rfloor) \bmod 480)$, period 32.

Each is a phase (`g16_phase`, `p1024_phase`, `p480_phase`), by a `decide` of the frame relation on the ring literal. The rings
are the record's: G16 from a SAT census of single-column phases at $N = 128$, P1024 from the eternal-cycle line, the 480-phase
from the classification at period 32.

## The certificate: a tree of top words

**Locality** (`cone`): bit $j$ of the code at tick $t$ depends only on initial bits $j - 2t, \ldots, j$. So an episode of $t$
ticks at depths $k, k+1$ depends only on the top $2t$ bits of the prefix $0 \ldots k + 1$ (bit 0 is the black edge).

**The tree** (`layer E k t`): the list of top words, of width $\min(2t, k + 1)$, whose canonical completion (bit 0 black, unread
bits white) still follows the phase after $t$ ticks. Each layer extends the previous one's words by two fresh bits (one, then
none, once the prefix is exhausted) and prunes at the first mismatch of the pair $(k, k+1)$ against $(E_k, E_{k+1})$.

**Soundness** (`sound`): the top bits of any black-edge code with a $t$-tick episode form a word of layer $t$. **Hence**
(`rep_bound`) an empty layer $M + 1$ bounds every episode by $M$ ticks.

**Alignments.** A time alignment $a$ at spatial alignment $i$ is the time alignment 0 at a rotated $i$ (`g16_shift`,
`p1024_shift`, `p480_shift`), so representatives at $a = 0$ cover every alignment: 128 for G16, 1,024 for P1024 and 960 for the
480-phase.

## Theorems

- `g16_mfinite`: for every $i$, `MFinite (g16 i) 14` with longest episode 22.
- `p1024_mfinite`: for every $i$, `MFinite (p1024 i) 8` with longest episode 24.
- `p480_mfinite`: for every $r, s$, `MFinite (p480 r s) 10` with longest episode 24.
- `no_tail_of_mfinite`: if the longest episode at depth $k$ is finite, no black-edge code follows the phase at every depth
  from some $d \le k$ on, at any alignment. No period or support is assumed of the code.

So **no black-edge code, periodic or not, follows G16 from depth 14, P1024 from depth 8, or the 480-phase from depth 10 or
shallower, at any alignment.** The kernel checks are `decide +kernel` on chunks of representatives: about 83,000 candidate
tests for G16, 71,000 for P1024 and 140,000 for the 480-phase, ninety seconds in all on one machine.

## Controls

- Each phase's longest episode at the certified depth equals the record's computed table (G16: 22 at depth 14; P1024: 24 at
  depth 8; the 480-phase: 24 at depth 10), and the tables agree at every smaller depth with the record's exhaustive runs.
- Shortening the tree by one tick at a chunk holding a known maximizer makes the kernel reject exactly that chunk (G16
  representative 41, P1024 representatives 819 and 820, the 480-phase representative (462, 0)).
- The nonempty layer $M$ at a maximizer is a control, not a formal lower witness: the certified statement is the upper bound.

## A computation

[Local: the table of the three trees from `phase_tree_size.py`: phase, depth, representatives, retained nodes, candidate tests,
deepest layer; and the replay of one representative's layers.]

## Related work and what is new

- **Our R30-20261103-d37d24** gives the finite criterion (an episode of $\mathrm{lcm}(2^{B(k+2)}, p)$ ticks is eternal); this
  entry does not need the horizon, because every tree empties well below it (ticks 23 and 25 against 1,024 and more), but the
  criterion is what makes a bounded search decisive in general.
- **The kit's `Rule30EtherEpisode`** (ours) gives the exact episode law of the eight-tick ether at every depth, with a potential;
  **`Rule30EtherGrounding`** (Troy Lowry) its eventual exclusion. Nothing comparable existed for any other phase.
- **The kit's strip certificates** (`Rule30StripCertificates`, bitmask and rank certificates) are the precedent for a search over
  partial words with pruning, there for the centre column; the tree of top words is that idea on the edge code, with locality in
  place of the strip bound.
- **Our record:** the three phases and their computed episode tables (G16 to depth 14, P1024 to depth 8, the 480-phase to
  depth 10) were exhaustive computations; the tree's design and its node counts were measured first, the soundness and alignment
  contract read two-party, then the Lean built and read.
- **New here:** kernel-checked finiteness at a bounded depth for three phases beyond the ether, at every alignment, and the
  top-word tree as a reusable certificate whose size grows with the depth, about 1.48-fold per depth step on these three
  phases, and with the number of alignments, not with the phase's period.
- **Scope.** These depths only. Nothing on other depths, on the uniform exclusion of any of the three phases (an open question
  of our record), on the centre column or on the Prize problems.
