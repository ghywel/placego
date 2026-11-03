---
Template: ComputationalEssay
Name: Episodes and eternal tails behind Rule 30's black edge: a finite criterion
Author: Gareth Herbert - with Claude (Anthropic) and GPT (OpenAI)
Date: 2026-11-03
Description: A partial result proved in core Lean on the kit's edge-code objects: for any periodic phase, every depth's longest episode behind a black right edge is finite if and only if no eternal point of any period follows the phase; an episode of lcm(2^B(k+2), p) ticks lasts for ever, so finiteness is a finite question; and an eventual tail is an eternal one.
Abstract: See abstract.txt.
Keywords: [rule 30, Rule 30 Prize, edge code, frozen ruler, phase, episode, eternal point, gate clock, prefix period, Lean 4, LeanLink, partial result]
Sources: ["[The Rule 30 Prize kit](https://github.com/WolframInstitute/Rule30PrizeKit)", "[The Wolfram · Collatz · Mahler record](https://github.com/ghywel/placego)"]
Links: ["[Rule 30 Prizes](https://rule30prize.org/)", "[R30-20261030-7b0d12: the half-rate bound on gate clocks](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261030-7b0d12)"]
---

## The question

Read a row of Rule 30 from its rightmost black cell, as the kit's `Rule30FrozenRuler` does. Bit $j$ of the **edge code**
is the cell $j$ places behind the edge, and the code evolves by the edge map $T$:

$$T(c)_0 = c_0, \qquad T(c)_1 = c_1 \oplus c_0, \qquad T(c)_{j+2} = c_{j+2} \oplus (c_{j+1} \lor c_j).$$

A **phase** $E$ is a family of depth columns $E_j(t)$ that obeys the same rule at every depth $j \ge 2$ and repeats in
time with period $p > 0$. The kit's eight-tick ether is one. An **episode** of $T$ ticks at depths $k, k + 1$ is a run
$t < T$ on which those two depths of a code follow the phase. How long can an episode behind a black edge be?

The kit answers this exactly for the eight-tick ether (`Rule30EtherEpisode`: the longest episode is
$\lfloor 2k/3 \rfloor + 4 - [k \equiv 0, 2 \bmod 6]$). For other phases the record has computed tables, not proofs.
This essay relates the question to a structural one, for every phase at once.

## The objects

On the kit's `iter` (the edge map's iterates), with $x_0$ = true for a black edge:

- `IsPhase E p`: $0 < p$, the rule at every depth $j + 2$, and $E_j(t + p) = E_j(t)$ for every $j$ and $t$.
- `Episode E k x a T`: for every $t < T$, `iter t x k = E k (t + a)` and `iter t x (k + 1) = E (k + 1) (t + a)`.
- `MFinite E k`: some $L$ bounds every episode at depth $k$ of every black-edge code at every alignment.
- `EternalTail E`: some black-edge code returns to itself after some $P > 0$ ticks and follows $E$ at every depth
  $\ge d$ and every time.

## The finite criterion

Bits $0 \ldots k + 1$ of every code are purely periodic from time 0, with period dividing $2^{B(k+2)}$, where
$B(n) = \lceil n/2 \rceil + Q(0, \lfloor n/2 \rfloor)$ is the kit's half-rate bound (`Rule30GateClocks.prefixExp_le_B`;
the edge map is the gate clock with OR). The phase has period $p$. So the episode condition has period

$$H(k, p) = \operatorname{lcm}\bigl(2^{B(k+2)}, p\bigr)$$

in $t$, for every code at once (`horizon`).

**Theorems.**
- `episode_extend`: an episode of $H(k, p)$ ticks lasts for ever.
- `eternal_of_long`: such an episode gives an eternal point. Keep bits $0 \ldots k + 1$, paste the phase beyond, and
  the code returns to itself after $H(k, p)$ ticks and follows $E$ at every depth $\ge k$.
- `mfinite_iff`: the longest episode at depth $k$ is finite **if and only if** no episode reaches $H(k, p)$ ticks,
  and it is then at most $H(k, p) - 1$.

So finiteness at a fixed depth is a finite question, with an explicit horizon. No pigeonhole over prefixes is needed;
the uniform prefix period replaces it.

## The bridge

**Theorem (`episode_bridge`).** For every phase,

$$\bigl(\forall k,\ \texttt{MFinite}\ E\ k\bigr) \iff \neg\, \texttt{EternalTail}\ E .$$

An eternal point gives an infinite episode at its own depth, and conversely an episode of $H(k, p)$ ticks gives an
eternal point. **`eternal_of_eventual`**: a pair that follows $E$ from some onset on, for ever, also gives an eternal
point. Behind a black edge, "eventually follows the phase" and "eternally follows it" are the same question.

## Two controls

- **The eight-tick ether, both ways.** `g8_mfinite` takes the kit's `episode_bound_all`, and `g8_no_eternal` takes the
  kit's `no_eventual_ether_pair`. `g8_mfinite_of_grounding` derives finiteness from grounding alone through the
  bridge, with the weaker bound $H(k, 8) - 1$.
- **A phase with an eternal tail.** The kit's rain code `rainA` returns after two ticks (`period_two_iff`), so its
  orbit is a phase whose episodes are unbounded at some depth (`rain_not_mfinite`). The bridge's other side is not
  vacuous.

## A computation

The longest episode of the eight-tick ether at depths $k, k + 1$, found by brute force over every black-edge prefix
(prefix autonomy makes bits beyond $k + 1$ irrelevant) and every phase alignment, against the kit's formula:

```wl
etherBit[i_, t_] := BitGet[{43, 202, 178, 172}[[Mod[i, 4] + 1]], Mod[t, 8]];
edgeStep[c_List] := Table[Which[j == 1, c[[1]], j == 2, BitXor[c[[2]], c[[1]]], True, BitXor[c[[j]], BitOr[c[[j - 1]], c[[j - 2]]]]], {j, Length[c]}];
lw[k_] := Floor[2 k/3] + 4 - Boole[MemberQ[{0, 2}, Mod[k, 6]]];
episode[c0_, k_, i_, q_, tmax_] := Module[{c = c0, t = 0},
  While[t < tmax && c[[k + 1]] == etherBit[k + i, t + q] && c[[k + 2]] == etherBit[k + 1 + i, t + q], c = edgeStep[c]; t++]; t];
longest[k_] := Max[Table[episode[Join[{1}, IntegerDigits[m, 2, k + 1]], k, i, q, lw[k] + 5], {m, 0, 2^(k + 1) - 1}, {i, 0, 3}, {q, 0, 7}]];
Grid[Prepend[Table[{k, longest[k], lw[k]}, {k, 1, 8}], {"k", "longest episode, brute force", "the kit's formula"}], Frame -> All]
```

The two columns agree. This reproduces a known result, and is shown as an illustration of finite episodes.

## Related work and what is new

- **The bridge** was proposed in our record by Cloud (CL676; the genealogy §38.2), and carried there by hand. Here it is
  a formal theorem on the kit's objects.
- **The kit.**
  - `Rule30EtherEpisode` gives the exact longest episode for the eight-tick ether. Its ether is Troy Lowry's, from kit
    PR 69.
  - `Rule30EtherGrounding` proves that no black-edge code follows that ether eventually.
  - `Rule30FrozenRuler` supplies the edge map and prefix autonomy.
  - `Rule30GateClocks` supplies the uniform prefix period. It is our earlier submission
    [R30-20261030-7b0d12](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261030-7b0d12).
- **New here, as a scoped comparison:** the formal statement for every periodic phase, the finite criterion with the
  explicit horizon $\operatorname{lcm}(2^{B(k+2)}, p)$, and "eventual is eternal".
- **Scope.** No finiteness is decided for any new phase. The record's other phases (period 16, the 480-state phase,
  period 1024) have computed episode tables, and the horizon makes their finiteness a finite question, but nothing
  here computes it. Nothing here concerns the centre column of the single-cell pattern or the Prize problems
  themselves.
