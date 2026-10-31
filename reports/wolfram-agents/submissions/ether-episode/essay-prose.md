---
Template: ComputationalEssay
Name: The longest ether-pair episode behind a black right edge of rule 30
Author: Gareth Herbert - with Claude (Anthropic) and GPT (OpenAI)
Date: 2026-10-31
Description: A partial result proved in core Lean: for every k ≥ 1, two adjacent depths k, k + 1 behind a black right edge of rule 30 follow the ether of kit pull request 69 (period 4 in depth, 8 in time) for at most floor(2k/3) + 4 - [k ≡ 0 or 2 mod 6] consecutive ticks, whatever the edge code, phase and onset, and an explicit code with no black bit beyond k + 1 attains this
Abstract: Read rule 30 from its rightmost black cell, bit $j$ of the edge code $x$ being the cell $j$ places to its left; $T$ is the kit's edge map. Kit pull request 69 (Troy Lowry, `Rule30EtherGrounding`) defines an ether $\mathrm{ether}(i,t)$ of period 4 in depth and 8 in time, and proves that no two adjacent depths of a black-edge code follow it eventually. Let $L(k)=\lfloor2k/3\rfloor+4-[k\equiv0,2\pmod{6}]$. For every code $x$ with $x_0=1$, every $k\ge1$, phase $(i,q)$ and onset $s$, bits $k$ and $k+1$ of $T^tx$ equal $\mathrm{ether}(i,t+q)$ and $\mathrm{ether}(i+1,t+q)$ on at most $L(k)$ consecutive ticks $t\ge s$ (an episode), and an explicit code $w$ attains $L(k)$, also when cut after bit $k+1$ (`Rule30Submission.episode_max`, `Rule30Submission.episode_bound`, `Rule30Submission.wit_episode`, `Rule30Submission.episode_witness_finite`). If $s+q+2i+6k\equiv7\pmod{8}$, an episode of $L(k)$ ticks forces bits $0,\dots,k+1$ of $T^sx$ to be those of $w$ (`Rule30Submission.witness_unique`). The kit has the frame (`Rule30FrozenRuler`) and a front-and-potential method for the period-three ether (`Rule30EtherThreeErosion`); we found no stated episode bound in the kit, its open pull requests or the submissions. Phillips (2004) explored periodic-background boundary growth experimentally. The front (the deepest mismatch with the ether) at depth $R$ and phase $\psi$ moves by 32 local rules keeping $2R+g(\psi)-3t$ constant from tick 1 on, for a fixed weight $g$, so it advances $3/2$ depth per tick on average. From a floor at tick 1, or along the explicit front of $w$, it reaches depth $k$ by tick $L(k)$. Nothing is claimed for the centre column, the Prize problems, $k=0$, or uniqueness without the congruence.
Keywords: [rule 30, Rule 30 Prize, right edge, edge map, ether, episode, front, potential, Lean 4, LeanLink, partial result]
Sources: ["[The Rule 30 Prize kit](https://github.com/WolframInstitute/Rule30PrizeKit)", "[The Wolfram · Collatz · Mahler record](https://github.com/ghywel/placego)"]
Links: ["[Rule 30 Prizes](https://rule30prize.org/)", "[Kit pull request 69: Rule30EtherGrounding](https://github.com/WolframInstitute/Rule30PrizeKit/pull/69)", "[Kit pull request 71: Rule30EtherEpisode](https://github.com/WolframInstitute/Rule30PrizeKit/pull/71)", "[Rule30EtherThreeErosion (R30-20261024-1fc962)](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261024-1fc962)", "[Phillips, Growth of the boundaries of simple cellular automata (2004)](https://www.wolframscience.com/conference/2004/presentations/material/rphillips-growth.nb)"]
---

## The question

Rule 30 updates each cell from itself and its two neighbours: the new colour is *left* XOR (*centre* OR *right*).
From a single black cell it grows the pattern below. The three Rule 30 Prize problems ask about its centre column, in
red: whether it is eventually periodic, whether its two colours have density 1/2, and whether computing its $n$th cell
takes effort of at least order $n$.

```wl
pattern = CellularAutomaton[30, {{1}, 0}, 60];
ArrayPlot[ReplacePart[pattern, {t_, 61} :> 2 pattern[[t, 61]]], ColorRules -> {0 -> White, 1 -> GrayLevel[0.15], 2 -> StandardRed}, ImageSize -> 480]
```

The first 40 cells of the centre column:

```wl
Take[CellularAutomaton[30, {{1}, 0}, {100, {{0}}}], 40]
```

This essay is about the right edge of each row instead, and proves nothing about the centre column. The rightmost
black cell moves one place to the right at every step. Read each row from it, as the kit's
`Rule30FrozenRuler` does: bit $j$ of the **edge code** is the cell $j$ places to the left of the edge cell, at **depth**
$j$. For every row with a rightmost black cell, a step of rule 30 is then the **edge map** $T$ (`edge_evol`):

$$(Tx)_0 = x_0, \qquad (Tx)_1 = x_1 \oplus x_0, \qquad (Tx)_j = x_j \oplus (x_{j-1} \lor x_{j-2}) \quad (j \ge 2).$$

Write $x_j(t)$ for bit $j$ of $T^t x$, the code after $t$ steps, or **ticks**; it is `iter t x j` in Lean. Bit 0 stays
black, and bit $j$ reads only bits $j - 2$, $j - 1$ and $j$, so the first $n$ bits evolve on their own (`iter_agree`).
Row 11 of the pattern read from its edge, its image under $T$, and row 12 read from its edge, each padded with white to
30 bits:

```wl
edgeMap[x_List] := Join[{x[[1]], BitXor[x[[2]], x[[1]]]}, BitXor[x[[3 ;;]], BitOr[x[[2 ;; -2]], x[[1 ;; -3]]]]];
edgeCode[row_List, n_] := PadRight[Reverse[Take[row, Last[Flatten[Position[row, 1]]]]], n];
bits[x_List] := StringJoin[ToString /@ x];
rows = CellularAutomaton[30, {{1}, 0}, 12];
<|"row 11 from its edge" -> bits[edgeCode[rows[[12]], 30]], "T applied to it" -> bits[edgeMap[edgeCode[rows[[12]], 30]]],
  "row 12 from its edge" -> bits[edgeCode[rows[[13]], 30]], "equal" -> edgeMap[edgeCode[rows[[12]], 30]] === edgeCode[rows[[13]], 30]|>
```

**The ether.** Kit pull request 69 (`Rule30EtherGrounding`, by Troy Lowry) introduced in this frame an ether of four
columns, each periodic in time with period 8:

$$\mathrm{ether}(i, t) = \text{bit } (t \bmod 8) \text{ of } (43, 202, 178, 172)_{i \bmod 4}.$$

Bits count from the least significant, so in time, for $t = 0, \dots, 7$, the four columns read $11010100$,
$01010011$, $01001101$ and $00110101$. It is a two-sided solution of the edge rule, with no edge and $i$ read modulo 4
(`ether_step`):

$$\mathrm{ether}(i, t+1) = \mathrm{ether}(i, t) \oplus \bigl(\mathrm{ether}(i-1, t) \lor \mathrm{ether}(i-2, t)\bigr).$$

In the fixed frame it is a periodic background of rule 30 whose rows alternate between one black cell in four and three
in four. On the left are its columns 23 to 0 as the edge frame sees them, and on the right rule 30 on a ring of 24 cells
started from $1000\,1000\cdots$. The first entry checks that the two are one pattern, column $i$ at tick $t$ being
position $t - i$:

```wl
ether[i_, t_] := BitGet[{43, 202, 178, 172}[[Mod[i, 4] + 1]], Mod[t, 8]];
ring = CellularAutomaton[30, Flatten[ConstantArray[{1, 0, 0, 0}, 6]], 15];
{ring === Table[ether[t - p, t], {t, 0, 15}, {p, 0, 23}],
 GraphicsRow[{ArrayPlot[Table[ether[i, t], {t, 0, 15}, {i, 23, 0, -1}], Mesh -> All, PlotLabel -> "columns 23 to 0 in the edge frame"],
   ArrayPlot[ring, Mesh -> All, PlotLabel -> "rule 30 on a ring of 24 cells"]}, ImageSize -> 560]}
```

Pull request 69 proved that no two adjacent depths of a code with a black edge follow the ether *eventually*
(`no_eventual_ether_pair`): for every code with $x_0 = 1$ and all $k, i, q$ there is no onset $s$ with

$$x_k(t) = \mathrm{ether}(i, t + q) \quad\text{and}\quad x_{k+1}(t) = \mathrm{ether}(i + 1, t + q) \qquad \text{for all } t \ge s.$$

For a while they can. Call a run of consecutive ticks $s, s + 1, \dots$ on which both equations hold an **episode** at
depths $k, k + 1$ with phase $(i, q)$ and onset $s$. How long can an episode be?

**The result.** Let

$$L(k) = \lfloor 2k/3 \rfloor + 4 - [k \equiv 0 \text{ or } 2 \pmod 6],$$

where $[P]$ is 1 if $P$ holds and 0 otherwise. It is `Lw k` in Lean, and $L(1), \dots, L(12)$ are
$4, 4, 6, 6, 7, 7, 8, 8, 10, 10, 11, 11$. For every $k \ge 1$ the longest episode at depths $k, k + 1$, over every code
with a black edge (finite or not), every phase and every onset, has exactly $L(k)$ ticks (`episode_max`). The bound is
`episode_bound`. An explicit code, the witness below, attains it (`wit_episode`), and still does when cut after bit
$k + 1$ (`episode_witness_finite`); in the witness's phase class every episode of $L(k)$ ticks starts from the
witness's bits 0 to $k + 1$ (`witness_unique`).

## Exploration

### The witness

The witness $w$ has $w_0 = 1$ and $w_j = \mathrm{ether}(j + 3, 1)$ for $j \ge 1$: a black edge cell followed by the
period $1110$. At depths $j \ge 1$ it is the ether at tick 1, with column $j + 3$ at depth $j$, so for every $k \ge 1$
its pair at depths $k, k + 1$ follows the ether with phase $(k + 3, 1)$ from tick 0. Its first 21 bits, and its episodes
at depths 6, 7 and 9, 10:

```wl
lw[k_] := Floor[2 k/3] + 4 - Boole[MemberQ[{0, 2}, Mod[k, 6]]];
wit = Prepend[Table[ether[j + 3, 1], {j, 40}], 1];
witOrbit = NestList[edgeMap, wit, 16];
follows[k_, t_] := witOrbit[[t + 1, {k + 1, k + 2}]] === {ether[k + 3, t + 1], ether[k + 4, t + 1]};
Column[{bits[Take[wit, 21]],
  Grid[Prepend[Table[{k, lw[k], StringJoin[If[follows[k, #], "1", "0"] & /@ Range[0, lw[k]]], SelectFirst[Range[0, 16], ! follows[k, #] &]}, {k, {6, 9}}],
    {"depth k", "Lw k", "follows at ticks 0 to Lw k", "first failing tick"}], Frame -> All]}, Spacings -> 1]
```

Each episode lasts $L(k)$ ticks and fails at tick $L(k)$. The picture shows why. It shows the witness on ticks 0 to 14,
from the top down, with depth 20 at the left and the edge cell, depth 0, just left of the dashed line; the four columns
right of that line are white cells beyond the edge. A cell is red where it differs from the ether that the witness
follows at every depth, $\mathrm{ether}(j + 3, t + 1)$ at depth $j$. The deepest red cell of a row is the **front**. The
blue boxes are the two episodes.

```wl
mismatch[j_, t_] := BitXor[If[j < 0, 0, witOrbit[[t + 1, j + 1]]], ether[j + 3, t + 1]];
field = Table[Which[mismatch[j, t] == 1, 2, j < 0, 0, True, witOrbit[[t + 1, j + 1]]], {t, 0, 14}, {j, 20, -4, -1}];
box[k_] := Line[{{19 - k, 15 - lw[k]}, {21 - k, 15 - lw[k]}, {21 - k, 15}, {19 - k, 15}, {19 - k, 15 - lw[k]}}];
ArrayPlot[field, ColorRules -> {0 -> White, 1 -> GrayLevel[0.35], 2 -> StandardRed}, Mesh -> All, Frame -> True, ImageSize -> 520,
 Epilog -> {Thick, StandardBlue, box[6], box[9], Black, Dashed, Line[{{21, 0}, {21, 15}}]},
 FrameTicks -> {{Table[{t + 1, t}, {t, 0, 14, 2}], None}, {Table[{21 - j, j}, {j, 20, -4, -4}], None}}, FrameLabel -> {"tick", "depth"}]
```

At tick 0 the witness differs from the ether only at the edge cell and at white cells beyond it; at tick 1 it agrees
with the ether at every depth from $-3$ inwards. From then on the disagreement spreads into the row, six depths every
four ticks, and each episode ends when the front reaches its pair.

### Every code

The state at any tick is again a code with a black edge, and $T^{s+u}x = T^u(T^s x)$ (`iter_add`), so an episode with
onset $s$ and phase $(i, q)$ is an episode with onset 0 and phase $(i, q + s)$ of the state at tick $s$. Bits 0 to
$k + 1$ evolve on their own, and the ether has period 4 in $i$ and 8 in $t$. So the longest episode at depths
$k, k + 1$ is a finite question: the $2^{k+1}$ prefixes of length $k + 2$ with bit 0 black, the 32 phases
$(i \bmod 4, q \bmod 8)$, onset 0. The computation answers it for $k = 0, \dots, 10$. The **phase class** of an episode, $c = (s + q + 2i + 6k) \bmod 8$, says which shift of the ether
its pair follows once the onset is moved to 0 (step 1 below). The fourth column counts, for each class that attains the
maximum, the prefixes that attain it, and the last checks that in class 7 that prefix is the witness's.

```wl
longest[k_] := Module[{codes = Prepend[#, 1] & /@ Tuples[{0, 1}, k + 1], orbit, runs, m, best},
  orbit = NestList[edgeMap, Transpose[codes], 4 k + 8];
  runs = Flatten[Table[Module[{alive = 1, last = 1, t = 0},
      While[Max[alive] == 1 && t <= 4 k + 8,
       last = alive;
       alive = alive (1 - BitXor[orbit[[t + 1, k + 1]], ether[i, t + q]]) (1 - BitXor[orbit[[t + 1, k + 2]], ether[i + 1, t + q]]);
       t++];
      {Mod[q + 2 i + 6 k, 8], t - 1, last}], {i, 0, 3}, {q, 0, 7}], 1];
  m = Max[runs[[All, 2]]];
  best = Select[runs, #[[2]] == m &];
  {k, m, lw[k], AssociationMap[Count[Total[Cases[best, {#, _, v_} :> v]], _?Positive] &, Union[best[[All, 1]]]],
   If[k == 0, "-", Pick[codes, Total[Cases[best, {7, _, v_} :> v]], _?Positive] === {Take[wit, k + 2]}]}];
Grid[Prepend[longest /@ Range[0, 10], {"k", "longest episode", "Lw k", "number of optimal prefixes, by phase class", "class 7: the witness's prefix"}], Frame -> All]
```

The longest episode is $L(k)$ for $k = 1, \dots, 10$. In these cases class 7 always attains it, class 5 at even $k$ and
class 3 at $k = 8$, each with a single optimal prefix. At $k = 0$ the longest episode has 2 ticks, one fewer than
$L(0) = 3$.

## The idea of the proof

The proof compares the code with the ether and follows the deepest disagreement, the front of the picture above. Each
step names the lemmas of the module that prove it.

**1. The wave and the mismatch.** The ether is one wave, $\mathrm{ether}(i, t) = e(t + 2i)$ with
$e = (1, 1, 0, 1, 0, 1, 0, 0)$ of period 8 (`ether_eq`). So an episode compares its depths $j = k, k + 1$ with the wave
$e(t + 2j + c)$, where $c$ is its phase class once the onset is moved to 0, and the proof compares every depth with the
same wave. Let $X_j(t)$ be bit $j$ of the code at tick $t$, with
$X_j = 0$ at the white depths $j < 0$, and let $D_j(t) = X_j(t) \oplus e(t + 2j + c)$ be the **mismatch**. The code and
the wave obey the same rule, so the mismatch obeys

$$D_j(t + 1) = D_j(t) \oplus F_\varphi\bigl(D_{j-1}(t), D_{j-2}(t)\bigr), \qquad \varphi = (t + 2j + c) \bmod 8,$$

with a gate $F_\varphi$ that depends only on the phase $\varphi$ (`D_step`). Every gate maps $(0, 0)$ to 0. The gates,
computed from $e$:

```wl
e[p_] := BitGet[43, Mod[p, 8]];
gate[phi_, a_, b_] := BitXor[BitOr[BitXor[e[phi - 2], a], BitXor[e[phi - 4], b]], BitOr[e[phi - 2], e[phi - 4]]];
<|"ether(i, t) = e(t + 2 i)" -> And @@ Flatten[Table[ether[i, t] == e[t + 2 i], {i, 0, 3}, {t, 0, 7}]],
  "gate at phase 0 to 7" -> AssociationMap[Replace[Table[gate[#, a, b], {a, 0, 1}, {b, 0, 1}],
     {{{0, 1}, {1, 1}} -> "a OR b", {{0, 1}, {0, 0}} -> "(NOT a) AND b", {{0, 0}, {1, 0}} -> "a AND (NOT b)", {{0, 0}, {0, 1}} -> "a AND b"}] &, Range[0, 7]]|>
```

**2. A clean tail and the front.** Bits $k$ and $k + 1$ never read deeper bits, so replacing the code beyond depth
$k + 1$ by the wave changes no episode at depths $k, k + 1$ (`tail`, `iter_agree`). Then the mismatch vanishes beyond
depth $k + 1$ at tick 0, and during an episode it vanishes at $k$ and $k + 1$; since every gate maps $(0, 0)$ to 0, it
vanishes at every depth $\ge k$ throughout the episode (`tail_inv`). It never vanishes everywhere, because the wave is
black at one of the white depths $-4, \dots, -1$ (`low_one`). So the deepest mismatch, the front $R(t)$, exists at
every tick (`front_zero`, `front_succ`), and an episode needs $R(t) < k$ on all its ticks.

**3. Lemma A: how the front moves.** Every cell deeper than the front is clean, so the next front depends only on the
front phase $\psi = (t + 2R + 2 + c) \bmod 8$, the phase of the next deeper cell, and on the mismatches
$a = D_{R-1}(t)$ and $b = D_{R-2}(t)$ of the two next shallower cells. In the 32 cases (`table`, `step`) the front moves
$+2$ at $\psi \in \{2, 4, 6, 7\}$, $+1$ at $\psi = 0$, $+1$ at $\psi = 3$ if $a = 0$ and $+1$ at $\psi = 5$ if $a = 1$,
and otherwise stays, except that at $\psi = 1$ with $a = b = 1$ it retreats. Every move that is not a retreat keeps the
potential, doubled to keep it an integer,

$$P = 2R + g(\psi) - 3t, \qquad g = (-3, 0, 3, -2, 1, -4, -1, 2).$$

The 32 cases, computed from the gates, with the checks of the potential and of Lemma B below:

```wl
g2 = {-3, 0, 3, -2, 1, -4, -1, 2};
move[psi_, a_, b_] := Which[gate[psi + 2, 0, 1] == 1, 2, gate[psi, 1, a] == 1, 1, gate[psi - 2, a, b] == 0, 0, True, "retreat"];
moves = Flatten[Table[{psi, a, b, move[psi, a, b]}, {psi, 0, 7}, {a, 0, 1}, {b, 0, 1}], 2];
<|"move at psi = 0 to 7, for (a, b) = 00, 01, 10, 11" -> GroupBy[moves, First -> Last],
  "retreats {psi, a, b}" -> Cases[moves, {psi_, a_, b_, "retreat"} :> {psi, a, b}],
  "every other move keeps 2R + g(psi) - 3t" -> AllTrue[Cases[moves, {_, _, _, _Integer}], 2 #[[4]] + g2[[Mod[#[[1]] + 1 + 2 #[[4]], 8] + 1]] == g2[[#[[1]] + 1]] + 3 &],
  "moves onto phase 1 {psi, move}" -> Union[Cases[moves, {psi_, _, _, d_Integer} /; Mod[psi + 1 + 2 d, 8] == 1 :> {psi, d}]],
  "mismatch one shallower after that move" -> Union[Table[gate[4, 1, a], {a, 0, 1}]]|>
```

**4. Lemma B: no retreat after tick 1.** A retreat starts from front phase 1, which is odd, so it lands on an even
front phase: $t + c$ changes parity and $2R$ is even. The only move onto phase 1 is the $+2$ move from phase 4, and it
leaves the cell one shallower than the new front clean, so $a = 0$ there and the next move is not a retreat. So from tick
1 on the front never retreats and $P$ is constant (`step`, `front_succ`; the module carries forward only the floor of
step 5, `pot_inv`). Then $R(t) = \bigl(3t + P - g(\psi)\bigr)/2$: the front advances $3/2$ depth per tick on average.
The witness, from tick 1:

```wl
front[t_] := Max[Select[Range[-4, 40], mismatch[#, t] == 1 &]];
Grid[{Prepend[Range[14], "tick t"], Prepend[front /@ Range[14], "front R(t)"],
  Prepend[Table[Mod[t + 2 front[t] + 9, 8], {t, 14}], "front phase psi"],
  Prepend[Table[2 front[t] + g2[[Mod[t + 2 front[t] + 9, 8] + 1]] - 3 t, {t, 14}], "2R + g(psi) - 3t"]}, Frame -> All]
```

**5. Floors at tick 1, and the witness.** The cells at depths $\le 0$ never change: white beyond the edge, black at it.
So their mismatch at tick 1 is known. In phase classes 0, 1, 3, 5 and 6 it bounds the front at tick 1 from below. In
classes 2, 4 and 7 the bound needed is depth 1, which holds unless the row has no mismatch at any depth $\ge 1$ at
tick 1. Either bound gives $P \ge P_c$ from tick 1 on, with floors $P_c = (-5, -2, 1, -4, -1, -6, -3, 0)$ for
$c = 0, \dots, 7$ (`lb`, `floor_arith`). A row with no mismatch at depth $\ge 1$ at tick 1 is forced, depth by depth,
at tick 0. In classes 2 and 4 its mismatch is then periodic and never ends (`heal2`, `heal4`), which a clean tail
excludes. In class 7 its mismatch vanishes at every depth $\ge 1$: the row is the witness's (`heal7`). So every
clean-tail row keeps $P \ge P_c$ from tick 1 on, except the witness's row in class 7 (`floor_case`, `dichotomy`). This
exception matters for the bound itself, not only for uniqueness: the witness's row is below the floor, and its front is
forced instead, along the **witness's lane**: front phases $2 \to 7 \to 4 \to 1$, moves $+2, +2, +2, 0$, and
$R(t) = 6\lfloor t/4 \rfloor - 4 + 2\max(t \bmod 4 - 1, 0)$ for $t \ge 1$ (`Rw`, `wit_front`); at tick 0 its front is at
depth 0, and the move to tick 1 is a retreat. Every row with a 9-bit prefix and the wave beyond it, in every class, for
20 ticks:

```wl
F2 = {-5, -2, 1, -4, -1, -6, -3, 0};
potentials[x_, c_] := Module[{orbit = NestList[edgeMap, x, 20], d, r},
   Table[d = BitXor[Join[{0, 0, 0, 0}, orbit[[t + 1]]], e[t + 2 Range[-4, Length[x] - 1] + c]];
    r = Last[Flatten[Position[d, 1]]] - 5;
    2 r + g2[[Mod[t + 2 r + 2 + c, 8] + 1]] - 3 t, {t, 20}]];
rowsP = Flatten[Table[With[{x = Join[{1}, IntegerDigits[m, 2, 8], e[2 Range[9, 70] + c]]},
     {c, potentials[x, c], c == 7 && Rest[x] === e[2 Range[70] + 7]}], {c, 0, 7}, {m, 0, 255}], 1];
<|"rows" -> Length[rowsP], "potential constant on ticks 1 to 20" -> AllTrue[rowsP, Equal @@ #[[2]] &],
  "the witness's row {class, potential}" -> Cases[rowsP, {c_, p_, True} :> {c, First[p]}],
  "least potential of the other rows, classes 0 to 7" -> Table[Min[Cases[rowsP, {c, p_, False} :> First[p]]], {c, 0, 7}],
  "floors" -> F2|>
```

Every floor is attained by one of these rows.

**The comparison.** Suppose an episode had $L(k) + 1$ ticks, $0, \dots, L(k)$. If $P \ge P_c$, then at tick $L(k)$ the
potential puts the front at depth $\ge k$ (`final_arith`, a check of every front phase and class). On the witness's lane
the front is at depth $\ge k$ at tick $L(k)$ as well, at $k$ or $k + 1$ (`wit_arith2`). Either way step 2 is
contradicted (`core`, `episode_bound`). For $k \ge 1$ the lane also has $R(t) < k$ for $t < L(k)$, so the witness's pair
follows the ether on ticks 0 to $L(k) - 1$ (`wit_arith1`, `wit_episode`), and cutting the witness after bit $k + 1$
changes none of its bits 0 to $k + 1$ at any tick (`episode_witness_finite`). In class 7 every other row has $P \ge 0$,
which brings the front to depth $\ge k$ already at tick $L(k) - 1$. So an episode of $L(k)$ ticks in class 7 forces the
witness's row, that is, the witness's bits 0 to $k + 1$ at the onset (`uniq_arith`, `core7`, `witness_unique`).

The rate $3/2$ is the potential's $3t$ against its $2R$, so the front needs about $2k/3$ ticks to reach depth $k$; the
floors and the witness's lane fix the constant.

## The formal proof

The module is core Lean. It imports the official statements (`Rule30Prize`) and the frame (`Rule30FrozenRuler`) at the
verifier's kit commit 842b756f. Pull request 69 is not in that build, so the module copies its `ether` verbatim and
proves `ether_step` again. The finite facts, such as the ether's table, the gates and the 32 cases of Lemma A, are
proved by `decide`, which the kernel evaluates; the rest is induction, rewriting and `omega`. Lean writes depths with an
offset, $n = j + 8$, so that the white depths are natural numbers too, and shifts the weights and floors by constants,
`G` $= g + 4$ (the module's docstring writes the same weights as $2g + 4$ with $g$ halved) and `K` $= P_c + 20$, for
the same reason.

```wl
Needs["Wolfram`LeanLink`"];
$Rule30PrizeKit = Environment["RULE30PRIZE_KIT"];
DirectoryQ[$Rule30PrizeKit]
```

```wl
rule30Submission = LeanImportString[(*Iconize["Lean source"]*)"%%LEAN%%", "ProjectDir" -> $Rule30PrizeKit]
```

## The formal checks

The five headlines, as Lean prints them:

```wl
opens = {"Rule30Submission", "Ruliology.CellularAutomata.Rule30FrozenRuler"};
heads = {"episode_max", "episode_bound", "wit_episode", "episode_witness_finite", "witness_unique"};
show[names_, prop_] := Column[Row[{Style[#, Bold], ":  ", rule30Submission["Rule30Submission." <> #][prop, "Open" -> opens]}] & /@ names, Spacings -> 1];
show[heads, "TypeForm"]
```

Their axioms are standard ones only:

```wl
AssociationMap[rule30Submission["Rule30Submission." <> #]["Axioms"] &, heads]
```

The definitions behind them: the episode length $L(k)$, the wave $e$, the ether of pull request 69, the witness $w$ and
the witness cut after bit $k + 1$. They match `lw`, `e`, `ether` and `wit` above.

```wl
show[{"Lw", "e", "ether", "wit", "witCut"}, "TermForm"]
```

Steps 1 and 3: the ether is the wave, the mismatch rule, and Lemma A for one step of the front, with `dR` the move
computed above and `G` the shifted weights.

```wl
show[{"ether_eq", "D_step", "step"}, "TypeForm"]
```

Steps 4 and 5: the invariant from tick 1 on (`Good`: a front at offset depth $n \ge 4$, that is $j \ge -4$, the guard of
Lemma B and the floor of the potential), its preservation, the dichotomy at tick 1 and the witness's lane.

```wl
Column[{show[{"Good"}, "TermForm"], show[{"pot_inv", "dichotomy", "wit_front"}, "TypeForm"]}, Spacings -> 1]
```

The kernel accepts every declaration of the module again. This is the replay the verifier runs; it comes last because
it resets LeanLink's elaboration state:

```wl
rule30Submission["Rule30Submission.episode_max"]["KernelCheck"]
```

## What is not proved

- Nothing here concerns the centre column of rule 30 or decides a Prize problem. The theorems are about the cells
  behind a moving black right edge and one ether, that of pull request 69; nothing is said about other ethers, fixed
  walls or densities.
- Uniqueness is proved only in phase class 7, and only for bits 0 to $k + 1$ of the state at the onset; the deeper bits
  are free. Other classes can attain $L(k)$ too: in the table above, class 5 at even $k$ and class 3 at $k = 8$; in a
  longer exhaustive computation of ours that is not reproduced here (a computation, not a theorem), class 5 at every
  even $k$ from 2 to 14 and class 3 at $k = 8$ and 14. Those optimal codes are not classified.
- The sharp statement is for $k \ge 1$. At $k = 0$ the longest episode has 2 ticks (the exhaustive computation above,
  not a theorem of the module), and the module's bound for every depth, `episode_bound_all`, gives only 3 there.
- The finite witness is stated for edge codes. Through the kit's `code` and `edge_evol` such a code is the edge code of
  a finite row of rule 30; that translation is not restated in the module.
- Growth of perturbations on periodic backgrounds, including Rule 30, was investigated by Phillips (see Earlier work).
  A linear front and its speed $3/2$ are not claimed as new in themselves, and we do not identify our front, measured
  in edge depth, with the boundaries he measured. What is claimed is the exact length of the longest episode, uniformly
  over edge codes, phases and onsets, its attainment and the uniqueness in class 7, with their proofs.
- Our search for earlier bounds covered the kit at 842b756f and its later main branch e5e1728, its open pull
  requests, the portal's list of submissions, and the boundary-growth literature cited below (Phillips; Brummitt and
  Rowland). That is a statement about our search, not a proof that no such bound exists.

## Earlier work

- **The frame.** The edge code, the edge map and `edge_evol` are the kit's `Rule30FrozenRuler`, which the same authors
  contributed earlier. The kit's module identifies $T$ as the 2-adic right-edge map of Coven, Pivato and Yassawi
  (Proc. Amer. Math. Soc. 135, 2007).
- **The ether.** The ether, `ether_step` and the eventual exclusion `no_eventual_ether_pair`, stated in the frame of
  `Rule30FrozenRuler`, are Troy Lowry's kit pull request 69, `Rule30EtherGrounding`. It reached the kit's main branch on
  31 October, after the verifier's build at 842b756f, so this module copies its `ether`. The pull request proves the exclusion through a pair invariant that every ether pair satisfies and a
  descent step, `local_descent`, that reads four consecutive ticks. Run on a finite window, that step would lose three
  ticks per depth, and so would bound an episode by about $3k$ ticks. The pull request does not state that bound, and
  it is not formalized here. The bound proved here has slope $2/3$ and is sharp.
- **The method.** A front state with a potential certified on finitely many local patterns is the method of the kit's
  `Rule30EtherThreeErosion`, by Luis Perez Morales and Claude (submission R30-20261024-1fc962), for the period-three
  ether, where the potential does not increase. Here it is applied to the ether of pull request 69 with 32 local cases,
  the potential is conserved from tick 1 on, and with the witness it gives the longest episode exactly.
- **Boundary growth.** Phillips investigated boundary growth from finite perturbations of periodic backgrounds,
  including Rule 30. Here we determine the sharp duration of a prescribed ether-pair episode behind a moving black edge,
  uniformly over all edge codes, phases and onset times. His study is experimental, and the proof here does not depend
  on it. Brummitt and Rowland's census of boundary growth treats constant backgrounds and points to Phillips for
  periodic ones.

**The kit pull request.** A catalog version of this module, `Ruliology.CellularAutomata.Rule30EtherEpisode`, which
imports the ether from `Rule30EtherGrounding` instead of copying it, is offered to the kit as
[pull request 71](https://github.com/WolframInstitute/Rule30PrizeKit/pull/71). Until the verifier's kit includes it,
this essay's Lean source carries the whole proof.

## References

- The Rule 30 Prize kit, [WolframInstitute/Rule30PrizeKit](https://github.com/WolframInstitute/Rule30PrizeKit), at
  commit 842b756f: the modules `Rule30Prize`, `Rule30FrozenRuler` and `Rule30EtherThreeErosion`.
- T. Lowry, kit pull request 69, `Rule30EtherGrounding`:
  [WolframInstitute/Rule30PrizeKit/pull/69](https://github.com/WolframInstitute/Rule30PrizeKit/pull/69).
- G. Herbert, Claude and GPT, kit pull request 71, `Rule30EtherEpisode`, the catalog form of this module:
  [WolframInstitute/Rule30PrizeKit/pull/71](https://github.com/WolframInstitute/Rule30PrizeKit/pull/71).
- L. Perez Morales and Claude, Rule 30 Prize submission
  [R30-20261024-1fc962](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261024-1fc962), in the kit as
  `Rule30EtherThreeErosion`: the period-three ether erodes, so it has no wall of any width.
- R. Phillips, *Growth of the boundaries of simple cellular automata*, Wolfram Science Conference 2004,
  [notebook](https://www.wolframscience.com/conference/2004/presentations/material/rphillips-growth.nb) (a conference
  notebook of computer experiments).
- C. D. Brummitt and E. Rowland, *Boundary growth in one-dimensional cellular automata*,
  [arXiv:1204.2172](https://arxiv.org/abs/1204.2172) (2012).
- E. M. Coven, M. Pivato and R. Yassawi, *Prevalence of odometers in cellular automata*, Proc. Amer. Math. Soc. 135
  (2007), [arXiv:math/0511030](https://arxiv.org/abs/math/0511030), as cited by the kit's `Rule30FrozenRuler` for the
  edge map.
- The record of this work, [ghywel/placego](https://github.com/ghywel/placego).
- [Rule 30 Prizes](https://rule30prize.org/), and S. Wolfram,
  [Announcing the Rule 30 Prizes](https://writings.stephenwolfram.com/2019/10/announcing-the-rule-30-prizes/) (2019).
