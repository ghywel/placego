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
rule30Submission = LeanImportString[(*Iconize["Lean source"]*)"import Ruliology.CellularAutomata.Rule30Prize
import Ruliology.CellularAutomata.Rule30FrozenRuler

/-!
# Rule 30: the longest ether-pair episode behind a black right edge

Read a row of rule 30 from its rightmost black cell, as in `Rule30FrozenRuler`: bit `k` of the
edge code is the cell `k` places behind the edge cell, and `iter t x` is the code at time `t`
(the edge map `T`). Kit pull request #69 (`Rule30EtherGrounding`) introduced in this frame the four-column,
eight-tick ether `ether i t` (a two-sided solution, `ether_step`) and proved that no two adjacent
depths of a black-edge code can follow it *eventually*. This module computes how long they can
follow it. An **episode** at depths `k, k + 1` with phase `(i, q)` and onset `s` is a run of
consecutive ticks `t ≥ s` with `iter t x k = ether i (t + q)` and
`iter t x (k + 1) = ether (i + 1) (t + q)`.

* `episode_bound`: for every code `x` with a black edge (`x 0 = true`; finite or not), every depth
  `k ≥ 1`, every phase `(i, q)` and every onset `s`, no episode has `Lw k + 1` ticks, where
  `Lw k = floor(2k/3) + 4 - [k ≡ 0 or 2 (mod 6)]` (`episode_bound_all`: the bound for every `k`).
* `episode_witness`: the witness `wit` (`x 0 = 1`, `x j = ether (j + 3) 1` for `j ≥ 1`) has an
  episode of `Lw k` ticks at depths `k, k + 1` for every `k ≥ 1`.
* `episode_max`: together, **the longest episode is `M(k) = Lw k` for every `k ≥ 1`**.
* `wit_episode` names the witness, and `episode_witness_finite` cuts it after bit `k + 1`: a code with
  no black bit beyond `k + 1` attains `Lw k` too (prefix autonomy). Through the kit's `code` and
  `edge_evol` such a code is the edge code of a finite row; that translation is not restated here.
* `witness_unique`: at phase class `7` (`s + q + 2i + 6k ≡ 7 (mod 8)`, the witness's class) every
  code with an episode of `Lw k` ticks has the witness's prefix (bits `0 .. k + 1`) at its onset.
  Bits beyond `k + 1` are free, and other phase classes may also attain `Lw k`.

Scope: a moving black right edge, in the frame of `Rule30FrozenRuler`. Nothing here concerns a fixed wall, the center
column or densities.

**The argument** (a front with a potential). `ether i t = e (t + 2 i)` with
`e = (1,1,0,1,0,1,0,0)` (`ether_eq`), so an episode's reference at depth `j` is the wave
`e (t + 2 j + c)` for one of 8 phase classes `c`, and `iter_add` moves the onset to `0`.

1. *Two-sided frame* (`X`, `E`, `D`). Depth `n : Nat` stands for edge depth `n - 8`; the cells
   beyond the edge are white. The black-edge state and the wave obey
   `X_n(t+1) = X_n(t) ⊕ (X_(n-1)(t) ∨ X_(n-2)(t))` at every `n ≥ 2` (`X_step`, `E_step`), so the
   mismatch `D = X ⊕ E` obeys `D_n(t+1) = D_n(t) ⊕ F_φ(D_(n-1)(t), D_(n-2)(t))`, `φ = t + 2n + c`
   (`D_step`), with `F` OR at `φ ∈ {0, 6}`, `¬a ∧ b` at `{1, 4}`, `a ∧ ¬b` at `{2, 3}`, AND at
   `{5, 7}`; `F(0, 0) = 0`.
2. *Clean tail* (`tail`, `tail_inv`). Replace the code beyond depth `k + 1` by the wave at time `0`.
   Prefix autonomy (`iter_agree`) keeps the pair; during an episode no mismatch reaches depth `k`.
   The mismatch is bounded above, and some white depth `-4 .. -1` mismatches, so the **front**
   (top mismatch) exists at every time (`low_one`, `top_exists`, `front_succ`).
3. *Lemma A* (`table`, `step`; 32 local cases): with front phase `ψ = t + 2R + 2 + c`, the front
   moves `+2` at `ψ ∈ {2, 4, 6, 7}`, `+1` at `ψ = 0`, `+1` at `ψ = 3` iff `D_(R-1) = 0`, `+1` at
   `ψ = 5` iff `D_(R-1) = 1`, else `0`, or retreats at `ψ = 1` when `D_(R-1) = D_(R-2) = 1`; every
   non-retreat move keeps the doubled potential `2R + g2(ψ) - 3t`,
   `g2 = (-3, 0, 3, -2, 1, -4, -1, 2)` (here `G = g2 + 4` and offset depths).
4. *Lemma B*: a retreat lands on an even phase and the only move onto phase `1` is the `+2` move
   from phase `4`, which leaves the cell below the new front clean; so nothing retreats from time
   `1` on and the potential is constant (`pot_inv`).
5. *Floors at time 1* (`floor_case`, `floor_arith`). The cells at depths `≤ 0` are fixed, which
   bounds the front at time `1` below. At `c = 2, 4` the only row healing every depth `≥ 1` at time
   `1` never becomes clean (`heal2`, `heal4`), which a clean tail does; at `c = 7` that row is the
   witness's (`heal7`) and every other row has potential `≥ 0`.
6. *Front comparison* (`final_arith`, `wit_front`, `wit_arith2`): at time `Lw k` the front is at
   depth `≥ k` — through the potential floor, or along the witness lane, whose moves are forced
   (front phases `2 → 7 → 4 → 1`, moves `+2, +2, +2, 0`, front `Rw`). That contradicts step 2.

**Sources.** The finite tables mirror a separate certificate of the same 32 cases. The method, a
front state with a potential certified on local patterns, is that of the kit's
`Rule30EtherThreeErosion` (period-three ether). The ether and `ether_step` are from kit pull
request #69 (`Rule30EtherGrounding`, by Troy Lowry), which is not in the verifier's kit build:
`ether` is copied here verbatim.
-/

namespace Rule30Submission

set_option autoImplicit false

open Ruliology.CellularAutomata
open Ruliology.CellularAutomata.Rule30FrozenRuler

/-! ### The ether and the wave -/

/-- The ether of PR #69 (`Rule30EtherGrounding.ether`), copied verbatim: four spatial columns of the
one-in-four ether, bit `t` read in time order. -/
def ether (i t : Nat) : Bool :=
  (match i % 4 with
   | 0 => 43 | 1 => 202 | 2 => 178 | _ => 172).testBit (t % 8)

/-- The episode length `floor(2k/3) + 4 - [k = 0, 2 (mod 6)]`. -/
def Lw (k : Nat) : Nat := 2 * k / 3 + 4 - (if k % 6 = 0 ∨ k % 6 = 2 then 1 else 0)

/-- The wave `e = (1,1,0,1,0,1,0,0)`, period 8. -/
def e (p : Nat) : Bool := (43 : Nat).testBit (p % 8)

theorem e_mod (p : Nat) : e p = e (p % 8) := by
  simp only [e, Nat.mod_mod]

theorem e_congr {p q : Nat} (h : p % 8 = q % 8) : e p = e q := by
  simp only [e, h]

theorem ether_table : ∀ i, i < 4 → ∀ t, t < 8 → ether i t = e (t + 2 * i) := by decide

/-- `ether i t = e (t + 2 i)`. -/
theorem ether_eq (i t : Nat) : ether i t = e (t + 2 * i) := by
  have h := ether_table (i % 4) (Nat.mod_lt _ (by decide)) (t % 8) (Nat.mod_lt _ (by decide))
  have h1 : ether i t = ether (i % 4) (t % 8) := by
    simp only [ether, Nat.mod_mod]
  rw [h1, h]
  exact e_congr (by omega)

theorem wave_table : ∀ r, r < 8 → e (r + 5) = xor (e (r + 4)) (e (r + 2) || e r) := by decide

/-- The wave obeys the edge rule: `e (p + 1) = e p ⊕ (e (p - 2) ∨ e (p - 4))`. -/
theorem wave (p : Nat) : e (p + 5) = xor (e (p + 4)) (e (p + 2) || e p) := by
  have h := wave_table (p % 8) (Nat.mod_lt _ (by decide))
  rw [e_congr (show (p + 5) % 8 = (p % 8 + 5) % 8 by omega),
    e_congr (show (p + 4) % 8 = (p % 8 + 4) % 8 by omega),
    e_congr (show (p + 2) % 8 = (p % 8 + 2) % 8 by omega), e_mod p, h]

/-- The `ether_step` of PR #69 (positive control): the ether is a two-sided solution of the edge rule. -/
theorem ether_step (i t : Nat) :
    ether i (t + 1) = xor (ether i t) (ether (i + 3) t || ether (i + 2) t) := by
  rw [ether_eq, ether_eq, ether_eq, ether_eq]
  have h := wave (t + 2 * i + 4)
  rw [e_congr (show (t + 2 * i + 4 + 5) % 8 = (t + 1 + 2 * i) % 8 by omega),
    e_congr (show (t + 2 * i + 4 + 4) % 8 = (t + 2 * i) % 8 by omega),
    e_congr (show (t + 2 * i + 4 + 2) % 8 = (t + 2 * (i + 3)) % 8 by omega),
    e_congr (show (t + 2 * i + 4) % 8 = (t + 2 * (i + 2)) % 8 by omega)] at h
  exact h

/-! ### The mismatch increment -/

/-- The mismatch increment at a cell of phase `φ`: OR at `φ ∈ {0, 6}`, `¬a ∧ b` at `{1, 4}`,
`a ∧ ¬b` at `{2, 3}`, AND at `{5, 7}`. -/
def F (φ : Nat) (a b : Bool) : Bool :=
  match φ with
  | 0 => a || b
  | 1 => !a && b
  | 2 => a && !b
  | 3 => a && !b
  | 4 => !a && b
  | 5 => a && b
  | 6 => a || b
  | _ => a && b

theorem F_zero (φ : Nat) : F φ false false = false := by
  unfold F; split <;> rfl

theorem F_table : ∀ r, r < 8 → ∀ a b : Bool,
    F ((r + 4) % 8) a b = xor ((xor (e (r + 2)) a) || (xor (e r) b)) (e (r + 2) || e r) := by
  decide

theorem F_spec (p : Nat) (a b : Bool) :
    F ((p + 4) % 8) a b = xor ((xor (e (p + 2)) a) || (xor (e p) b)) (e (p + 2) || e p) := by
  have h := F_table (p % 8) (Nat.mod_lt _ (by decide)) a b
  rw [show (p + 4) % 8 = (p % 8 + 4) % 8 by omega,
    e_congr (show (p + 2) % 8 = (p % 8 + 2) % 8 by omega), e_mod p, h]

/-! ### The two-sided frame (depth `n` stands for edge depth `n - 8`) -/

/-- The black-edge state at offset depth `n` (edge depth `n - 8`; white at negative depths). -/
def X (x : Nat → Bool) (n t : Nat) : Bool := if n < 8 then false else iter t x (n - 8)

/-- The reference wave of phase class `c` at offset depth `n`. -/
def E (c n t : Nat) : Bool := e (t + 2 * n + c)

/-- The mismatch. -/
def D (x : Nat → Bool) (c n t : Nat) : Bool := xor (X x n t) (E c n t)

theorem X_step (x : Nat → Bool) (n t : Nat) (hn : 2 ≤ n) :
    X x n (t + 1) = xor (X x n t) (X x (n - 1) t || X x (n - 2) t) := by
  unfold X
  by_cases h8 : n < 8
  · have h1 : n - 1 < 8 := by omega
    have h2 : n - 2 < 8 := by omega
    simp [h8, h1, h2]
  · by_cases h9 : n = 8
    · subst h9; simp [iter, T]
    · by_cases h10 : n = 9
      · subst h10; simp [iter, T]
      · obtain ⟨m, rfl⟩ : ∃ m, n = m + 10 := ⟨n - 10, by omega⟩
        have a1 : m + 10 - 8 = m + 2 := by omega
        have a2 : m + 10 - 1 - 8 = m + 1 := by omega
        have a3 : m + 10 - 2 - 8 = m := by omega
        have b1 : ¬ (m + 10 - 1 < 8) := by omega
        have b2 : ¬ (m + 10 - 2 < 8) := by omega
        simp only [h8, b1, b2, ite_false, a1, a2, a3]
        rfl

theorem E_step (c n t : Nat) (hn : 2 ≤ n) :
    E c n (t + 1) = xor (E c n t) (E c (n - 1) t || E c (n - 2) t) := by
  unfold E
  have h := wave (t + 2 * (n - 2) + c)
  rw [show t + 1 + 2 * n + c = t + 2 * (n - 2) + c + 5 by omega,
    show t + 2 * n + c = t + 2 * (n - 2) + c + 4 by omega,
    show t + 2 * (n - 1) + c = t + 2 * (n - 2) + c + 2 by omega]
  exact h

theorem F_E (c n t : Nat) (hn : 2 ≤ n) (a b : Bool) :
    F ((t + 2 * n + c) % 8) a b =
      xor ((xor (E c (n - 1) t) a) || (xor (E c (n - 2) t) b))
        (E c (n - 1) t || E c (n - 2) t) := by
  unfold E
  rw [show t + 2 * n + c = t + 2 * (n - 2) + c + 4 by omega,
    show t + 2 * (n - 1) + c = t + 2 * (n - 2) + c + 2 by omega]
  exact F_spec _ a b

theorem bool_step (Xn Xa Xb En Ea Eb : Bool) :
    xor (xor Xn (Xa || Xb)) (xor En (Ea || Eb)) =
      xor (xor Xn En) (xor ((xor Ea (xor Xa Ea)) || (xor Eb (xor Xb Eb))) (Ea || Eb)) := by
  cases Xn <;> cases Xa <;> cases Xb <;> cases En <;> cases Ea <;> cases Eb <;> rfl

/-- **The mismatch rule.** `D_n(t+1) = D_n(t) ⊕ F_φ(D_(n-1)(t), D_(n-2)(t))`, `φ = t + 2n + c`. -/
theorem D_step (x : Nat → Bool) (c n t : Nat) (hn : 2 ≤ n) :
    D x c n (t + 1) =
      xor (D x c n t) (F ((t + 2 * n + c) % 8) (D x c (n - 1) t) (D x c (n - 2) t)) := by
  unfold D
  rw [X_step x n t hn, E_step c n t hn, F_E c n t hn]
  exact bool_step _ _ _ _ _ _

theorem D_step' (x : Nat → Bool) (c n t n1 n2 φ : Nat) (hn : 2 ≤ n) (h1 : n1 = n - 1)
    (h2 : n2 = n - 2) (hφ : φ = (t + 2 * n + c) % 8) :
    D x c n (t + 1) = xor (D x c n t) (F φ (D x c n1 t) (D x c n2 t)) := by
  subst h1 h2 hφ; exact D_step x c n t hn

theorem D_low (x : Nat → Bool) (c n t : Nat) (hn : n < 8) : D x c n t = e (t + 2 * n + c) := by
  simp [D, X, E, hn]

theorem D_eight (x : Nat → Bool) (hx : x 0 = true) (c t : Nat) :
    D x c 8 t = ! e (t + 16 + c) := by
  simp [D, X, E, iter_zero, hx]

theorem X_ge (x : Nat → Bool) (n t : Nat) (hn : 8 ≤ n) : X x n t = iter t x (n - 8) := by
  simp [X, show ¬ n < 8 by omega]

theorem xor_false_eq {p q : Bool} (h : xor p q = false) : p = q := by
  cases p <;> cases q <;> simp_all

/-! ### The front -/

/-- `R` is the front at time `t`: the top mismatch. -/
abbrev FrontAt (x : Nat → Bool) (c t R : Nat) : Prop :=
  D x c R t = true ∧ ∀ n, R < n → D x c n t = false

theorem top_exists (f : Nat → Bool) (m : Nat) (hm : f m = true) :
    ∀ d, (∀ n, m + d ≤ n → f n = false) → ∃ R, m ≤ R ∧ f R = true ∧ ∀ n, R < n → f n = false := by
  intro d
  induction d with
  | zero =>
    intro h
    have h' := h m (by omega)
    rw [hm] at h'
    exact absurd h' (by decide)
  | succ d ih =>
    intro h
    cases hfd : f (m + d) with
    | true => exact ⟨m + d, by omega, hfd, fun n hn => h n (by omega)⟩
    | false =>
      apply ih
      intro n hn
      by_cases hnd : n = m + d
      · rw [hnd]; exact hfd
      · exact h n (by omega)

theorem front_ge {x : Nat → Bool} {c t R : Nat} (hF : FrontAt x c t R) {m : Nat}
    (hm : D x c m t = true) : m ≤ R := by
  by_cases h : m ≤ R
  · exact h
  · have h' := hF.2 m (by omega)
    rw [hm] at h'
    exact absurd h' (by decide)

theorem low_table :
    ∀ r, r < 8 → (e (r + 8) || (e (r + 10) || (e (r + 12) || e (r + 14)))) = true := by
  decide

/-- Among the white depths `-4 .. -1` some cell mismatches the wave: the front is at least `-4`. -/
theorem low_one (x : Nat → Bool) (c t : Nat) : ∃ m, 4 ≤ m ∧ m ≤ 7 ∧ D x c m t = true := by
  have h := low_table ((t + c) % 8) (Nat.mod_lt _ (by decide))
  have h4 : D x c 4 t = e ((t + c) % 8 + 8) := by
    rw [D_low x c 4 t (by decide)]; exact e_congr (by omega)
  have h5 : D x c 5 t = e ((t + c) % 8 + 10) := by
    rw [D_low x c 5 t (by decide)]; exact e_congr (by omega)
  have h6 : D x c 6 t = e ((t + c) % 8 + 12) := by
    rw [D_low x c 6 t (by decide)]; exact e_congr (by omega)
  have h7 : D x c 7 t = e ((t + c) % 8 + 14) := by
    rw [D_low x c 7 t (by decide)]; exact e_congr (by omega)
  rw [← h4, ← h5, ← h6, ← h7] at h
  simp only [Bool.or_eq_true] at h
  rcases h with h | h | h | h
  · exact ⟨4, by decide, by decide, h⟩
  · exact ⟨5, by decide, by decide, h⟩
  · exact ⟨6, by decide, by decide, h⟩
  · exact ⟨7, by decide, by decide, h⟩

/-! ### The clean tail -/

/-- The code with everything beyond depth `k + 1` replaced by the reference wave at time `0`. -/
def tail (x : Nat → Bool) (k c : Nat) : Nat → Bool :=
  fun j => if j ≤ k + 1 then x j else e (2 * j + c)

theorem tail_agree (x : Nat → Bool) (k c : Nat) : AgreeBelow (k + 2) x (tail x k c) := by
  intro i hi
  simp [tail, show i ≤ k + 1 by omega]

theorem tail_clean (x : Nat → Bool) (k c : Nat) :
    ∀ n, k + 10 ≤ n → D (tail x k c) c n 0 = false := by
  intro n hn
  have h2 : ¬ (n - 8 ≤ k + 1) := by omega
  rw [D, X_ge _ n 0 (by omega)]
  simp only [iter, tail, h2, ite_false, E]
  rw [e_congr (show (2 * (n - 8) + c) % 8 = (0 + 2 * n + c) % 8 by omega)]
  exact Bool.xor_self _

/-- During an episode on ticks `0 .. L`, the clean tail stays clean: no mismatch at depth `≥ k`. -/
theorem tail_inv (x : Nat → Bool) (c k L : Nat)
    (h0 : ∀ n, k + 10 ≤ n → D x c n 0 = false)
    (hp : ∀ u, u ≤ L → D x c (k + 8) u = false ∧ D x c (k + 9) u = false) :
    ∀ u, u ≤ L → ∀ n, k + 8 ≤ n → D x c n u = false := by
  intro u
  induction u with
  | zero =>
    intro hu n hn
    by_cases h8 : n = k + 8
    · rw [h8]; exact (hp 0 hu).1
    · by_cases h9 : n = k + 9
      · rw [h9]; exact (hp 0 hu).2
      · exact h0 n (by omega)
  | succ u ih =>
    intro hu n hn
    by_cases h8 : n = k + 8
    · rw [h8]; exact (hp _ hu).1
    · by_cases h9 : n = k + 9
      · rw [h9]; exact (hp _ hu).2
      · rw [D_step x c n u (by omega), ih (by omega) n (by omega), ih (by omega) (n - 1) (by omega),
          ih (by omega) (n - 2) (by omega), F_zero]
        rfl

theorem front_zero (x : Nat → Bool) (c k : Nat) (h0 : ∀ n, k + 10 ≤ n → D x c n 0 = false) :
    ∃ R, 4 ≤ R ∧ FrontAt x c 0 R := by
  obtain ⟨m, hm4, _, hm⟩ := low_one x c 0
  obtain ⟨R, hmR, hR, hR'⟩ :=
    top_exists (fun n => D x c n 0) m hm (k + 10) (fun n hn => h0 n (by omega))
  exact ⟨R, by omega, hR, hR'⟩

/-! ### Lemma A: the front's moves (32 local cases), and the potential -/

/-- Doubled potential weights, shifted: `G = 2 g + 4` with
`g = (-3/2, 0, 3/2, -1, 1/2, -2, -1/2, 1)`. -/
def G (ψ : Nat) : Nat :=
  match ψ with
  | 0 => 1 | 1 => 4 | 2 => 7 | 3 => 2 | 4 => 5 | 5 => 0 | 6 => 3 | _ => 6

/-- The front's move at front phase `ψ` (the phase of the cell above the front) with
`a = D_(R-1)`: `+2` at `ψ ∈ {2, 4, 6, 7}`, `+1` at `ψ = 0`, at `ψ = 3` iff `a = 0` and at `ψ = 5`
iff `a = 1`; otherwise `0` (or a retreat, at `ψ = 1` with `a = b = 1`). -/
def dR (ψ : Nat) (a : Bool) : Nat :=
  if F ((ψ + 2) % 8) false true = true then 2 else if F ψ true a = true then 1 else 0

/-- The front's moves as in the hand proof's table. -/
theorem dR_table (a : Bool) :
    dR 0 a = 1 ∧ dR 1 a = 0 ∧ dR 2 a = 2 ∧ dR 3 a = (if a then 0 else 1) ∧ dR 4 a = 2 ∧
      dR 5 a = (if a then 1 else 0) ∧ dR 6 a = 2 ∧ dR 7 a = 2 := by
  cases a <;> decide

/-- The finite table behind Lemma A, the potential and Lemma B. -/
abbrev TableOK (ψ : Nat) (a b : Bool) : Prop :=
  (¬ (ψ = 1 ∧ a = true ∧ b = true) →
    dR ψ a ≤ 2 ∧
    (dR ψ a = 2 → F ((ψ + 2) % 8) false true = true) ∧
    (dR ψ a = 1 → F ψ true a = true ∧ F ((ψ + 2) % 8) false true = false) ∧
    (dR ψ a = 0 → xor true (F ((ψ + 6) % 8) a b) = true ∧ F ψ true a = false ∧
      F ((ψ + 2) % 8) false true = false) ∧
    2 * dR ψ a + G ((ψ + 1 + 2 * dR ψ a) % 8) = G ψ + 3 ∧
    ((ψ + 1 + 2 * dR ψ a) % 8 = 1 → dR ψ a = 2 ∧ F ψ true a = false)) ∧
  ((ψ = 1 ∧ a = true ∧ b = true) →
    xor true (F ((ψ + 6) % 8) a b) = false ∧ F ψ true a = false ∧
      F ((ψ + 2) % 8) false true = false)

set_option synthInstance.maxSize 4096 in
set_option synthInstance.maxHeartbeats 400000 in
theorem table : ∀ ψ, ψ < 8 → ∀ a b : Bool, TableOK ψ a b := by decide

/-- **Lemma A.** One step of a front `R` with front phase `ψ`, `a = D_(R-1)`, `b = D_(R-2)`. Without
a retreat the new front is `R + dR ψ a`, the doubled potential `2R + G ψ - 3t` is unchanged, and
when the new front phase is `1` the cell below the new front is clean (Lemma B). A retreat (`ψ = 1`,
`a = b = 1`) clears every depth `≥ R`. -/
theorem step (x : Nat → Bool) (c t R ψ : Nat) (a b : Bool) (hR : 4 ≤ R) (hF : FrontAt x c t R)
    (hψ : (t + 2 * R + 2 + c) % 8 = ψ) (ha : D x c (R - 1) t = a) (hb : D x c (R - 2) t = b) :
    (¬ (ψ = 1 ∧ a = true ∧ b = true) →
      FrontAt x c (t + 1) (R + dR ψ a) ∧
      2 * (R + dR ψ a) + G ((t + 1 + 2 * (R + dR ψ a) + 2 + c) % 8) = 2 * R + G ψ + 3 ∧
      ((t + 1 + 2 * (R + dR ψ a) + 2 + c) % 8 = 1 → D x c (R + dR ψ a - 1) (t + 1) = false)) ∧
    ((ψ = 1 ∧ a = true ∧ b = true) → ∀ n, R ≤ n → D x c n (t + 1) = false) := by
  have hψ8 : ψ < 8 := by omega
  have v3 : ∀ n, R + 3 ≤ n → D x c n (t + 1) = false := by
    intro n hn
    rw [D_step x c n t (by omega), hF.2 n (by omega), hF.2 (n - 1) (by omega),
      hF.2 (n - 2) (by omega), F_zero]
    rfl
  have v2 : D x c (R + 2) (t + 1) = F ((ψ + 2) % 8) false true := by
    rw [D_step' x c (R + 2) t (R + 1) R ((ψ + 2) % 8) (by omega) (by omega) (by omega) (by omega),
      hF.2 (R + 2) (by omega), hF.2 (R + 1) (by omega), hF.1, Bool.false_xor]
  have v1 : D x c (R + 1) (t + 1) = F ψ true a := by
    rw [D_step' x c (R + 1) t R (R - 1) ψ (by omega) (by omega) (by omega) (by omega),
      hF.2 (R + 1) (by omega), hF.1, ha, Bool.false_xor]
  have v0 : D x c R (t + 1) = xor true (F ((ψ + 6) % 8) a b) := by
    rw [D_step' x c R t (R - 1) (R - 2) ((ψ + 6) % 8) (by omega) rfl rfl (by omega), hF.1, ha, hb]
  obtain ⟨Tm, Tr⟩ := table ψ hψ8 a b
  have hph : ∀ d, (t + 1 + 2 * (R + d) + 2 + c) % 8 = (ψ + 1 + 2 * d) % 8 := by
    intro d; omega
  refine ⟨fun hnr => ?_, fun hr => ?_⟩
  · obtain ⟨hle, h2, h1, h0, hpot, hph1⟩ := Tm hnr
    refine ⟨⟨?_, ?_⟩, ?_, ?_⟩
    · rcases (by omega : dR ψ a = 0 ∨ dR ψ a = 1 ∨ dR ψ a = 2) with h | h | h
      · rw [h, Nat.add_zero, v0]; exact (h0 h).1
      · rw [h, v1]; exact (h1 h).1
      · rw [h, v2]; exact h2 h
    · intro n hn
      by_cases hn3 : R + 3 ≤ n
      · exact v3 n hn3
      · rcases (by omega : dR ψ a = 0 ∨ dR ψ a = 1 ∨ dR ψ a = 2) with h | h | h
        · rcases (by omega : n = R + 1 ∨ n = R + 2) with rfl | rfl
          · rw [v1]; exact (h0 h).2.1
          · rw [v2]; exact (h0 h).2.2
        · have hn2 : n = R + 2 := by omega
          subst hn2; rw [v2]; exact (h1 h).2
        · omega
    · rw [hph]; omega
    · rw [hph]; intro h1'
      obtain ⟨_, hFa⟩ := hph1 h1'
      rw [show R + dR ψ a - 1 = R + 1 by omega, v1]; exact hFa
  · intro n hn
    obtain ⟨r0, r1, r2⟩ := Tr hr
    by_cases hn3 : R + 3 ≤ n
    · exact v3 n hn3
    · rcases (by omega : n = R ∨ n = R + 1 ∨ n = R + 2) with rfl | rfl | rfl
      · rw [v0]; exact r0
      · rw [v1]; exact r1
      · rw [v2]; exact r2

/-- The front exists at the next time, with the guard of Lemma B: a retreat lands on an even
phase, and the only move onto phase `1` is the `+2` move from phase `4`, which leaves the cell
below the new front clean. -/
theorem front_succ (x : Nat → Bool) (c t R : Nat) (hR : 4 ≤ R) (hF : FrontAt x c t R) :
    ∃ R', 4 ≤ R' ∧ FrontAt x c (t + 1) R' ∧
      ((t + 1 + 2 * R' + 2 + c) % 8 = 1 → D x c (R' - 1) (t + 1) = false) := by
  obtain ⟨Sm, Sr⟩ := step x c t R ((t + 2 * R + 2 + c) % 8) (D x c (R - 1) t) (D x c (R - 2) t)
    hR hF rfl rfl rfl
  by_cases hr : ((t + 2 * R + 2 + c) % 8 = 1 ∧ D x c (R - 1) t = true ∧ D x c (R - 2) t = true)
  · have hcl := Sr hr
    obtain ⟨m, hm4, _, hm⟩ := low_one x c (t + 1)
    obtain ⟨R', hmR, hR', hR''⟩ := top_exists (fun n => D x c n (t + 1)) m hm R
      (fun n hn => hcl n (by omega))
    refine ⟨R', by omega, ⟨hR', hR''⟩, fun h => ?_⟩
    have h1 := hr.1
    exfalso; omega
  · obtain ⟨hF', _, hph⟩ := Sm hr
    exact ⟨_, by omega, hF', hph⟩

/-! ### The potential from time 1 on -/

/-- The invariant from time `1` on: a front, the guard of Lemma B, and the potential floor. -/
abbrev Good (x : Nat → Bool) (c Kc t R : Nat) : Prop :=
  4 ≤ R ∧ FrontAt x c t R ∧ ((t + 2 * R + 2 + c) % 8 = 1 → D x c (R - 1) t = false) ∧
    3 * t + Kc ≤ 2 * R + G ((t + 2 * R + 2 + c) % 8)

/-- No retreat from time `1` on, so the potential never drops. -/
theorem pot_inv (x : Nat → Bool) (c Kc : Nat) (h1 : ∃ R, Good x c Kc 1 R) :
    ∀ u, ∃ R, Good x c Kc (u + 1) R := by
  intro u
  induction u with
  | zero => exact h1
  | succ u ih =>
    obtain ⟨R, hR4, hF, hg, hpot⟩ := ih
    obtain ⟨Sm, _⟩ := step x c (u + 1) R ((u + 1 + 2 * R + 2 + c) % 8) (D x c (R - 1) (u + 1))
      (D x c (R - 2) (u + 1)) hR4 hF rfl rfl rfl
    have hnr : ¬ ((u + 1 + 2 * R + 2 + c) % 8 = 1 ∧ D x c (R - 1) (u + 1) = true ∧
        D x c (R - 2) (u + 1) = true) := by
      rintro ⟨h1, h2, _⟩
      rw [hg h1] at h2
      exact absurd h2 (by decide)
    obtain ⟨hF', hpot', hph'⟩ := Sm hnr
    refine ⟨_, by omega, hF', hph', ?_⟩
    omega

/-! ### Floors at time 1 -/

/-- Lower bounds on the front at time `1` (offset depths; `9` is edge depth `1`). -/
def lb (c : Nat) : Nat :=
  match c with
  | 0 => 6 | 1 => 8 | 2 => 9 | 3 => 8 | 4 => 9 | 5 => 8 | 6 => 8 | _ => 9

/-- The doubled potential floors `F2_c`, shifted by `20`: `-5, -2, 1, -4, -1, -6, -3, 0`. -/
def K (c : Nat) : Nat :=
  match c with
  | 0 => 15 | 1 => 18 | 2 => 21 | 3 => 16 | 4 => 19 | 5 => 14 | 6 => 17 | _ => 20

theorem G_cases (p : Nat) :
    (p % 8 = 0 ∧ G (p % 8) = 1) ∨ (p % 8 = 1 ∧ G (p % 8) = 4) ∨ (p % 8 = 2 ∧ G (p % 8) = 7) ∨
    (p % 8 = 3 ∧ G (p % 8) = 2) ∨ (p % 8 = 4 ∧ G (p % 8) = 5) ∨ (p % 8 = 5 ∧ G (p % 8) = 0) ∨
    (p % 8 = 6 ∧ G (p % 8) = 3) ∨ (p % 8 = 7 ∧ G (p % 8) = 6) := by
  have h : p % 8 < 8 := Nat.mod_lt _ (by decide)
  generalize p % 8 = r at h ⊢
  revert r; decide

theorem c_cases (c : Nat) (hc : c < 8) :
    c = 0 ∨ c = 1 ∨ c = 2 ∨ c = 3 ∨ c = 4 ∨ c = 5 ∨ c = 6 ∨ c = 7 := by omega

/-- The floor: a front at time `1` at or above `lb c` has doubled potential at least `F2_c`. -/
theorem floor_arith (c : Nat) (hc : c < 8) (R : Nat) (hR : lb c ≤ R) :
    3 * 1 + K c ≤ 2 * R + G ((1 + 2 * R + 2 + c) % 8) := by
  rcases G_cases (1 + 2 * R + 2 + c) with ⟨h1, h2⟩ | ⟨h1, h2⟩ | ⟨h1, h2⟩ | ⟨h1, h2⟩ |
      ⟨h1, h2⟩ | ⟨h1, h2⟩ | ⟨h1, h2⟩ | ⟨h1, h2⟩ <;>
    rw [h2] <;>
    rcases c_cases c hc with rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl <;>
    simp only [lb, K] at hR ⊢ <;> omega

theorem Lw_cases (k : Nat) : ((k % 6 = 0 ∨ k % 6 = 2) ∧ Lw k = 2 * k / 3 + 3) ∨
    (¬ (k % 6 = 0 ∨ k % 6 = 2) ∧ Lw k = 2 * k / 3 + 4) := by
  unfold Lw
  split
  · next h => left; exact ⟨h, by omega⟩
  · next h => right; exact ⟨h, by omega⟩

/-- **Front comparison at the end of the episode.** At time `Lw k` a front carrying the floor
potential is at depth `≥ k`. (The `(4, 6)` periodicity of the potential is absorbed by `omega`.) -/
theorem final_arith (c : Nat) (hc : c < 8) (k : Nat) (R : Nat)
    (h : 3 * Lw k + K c ≤ 2 * R + G ((Lw k + 2 * R + 2 + c) % 8)) : k + 8 ≤ R := by
  have hL := Lw_cases k
  rcases G_cases (Lw k + 2 * R + 2 + c) with ⟨h1, h2⟩ | ⟨h1, h2⟩ | ⟨h1, h2⟩ | ⟨h1, h2⟩ |
      ⟨h1, h2⟩ | ⟨h1, h2⟩ | ⟨h1, h2⟩ | ⟨h1, h2⟩ <;>
    rw [h2] at h <;>
    rcases c_cases c hc with rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl <;>
    simp only [K] at h <;> omega

/-! ### The witness lane at phase class 7 -/

/-- The witness front (offset depths): `6n + 4, 6n + 4, 6n + 6, 6n + 8` at `t = 4n .. 4n + 3`,
i.e. edge depths `R_w(t) = 6n - 4, 6n - 4, 6n - 2, 6n`. -/
def Rw (t : Nat) : Nat := 6 * (t / 4) + 4 + 2 * (t % 4 - 1)

theorem wit_move (t : Nat) (a : Bool) (ha : (t + 2 * Rw t + 2 + 7) % 8 = 1 → a = false) :
    Rw t + dR ((t + 2 * Rw t + 2 + 7) % 8) a = Rw (t + 1) := by
  have hd : ∀ a : Bool, dR 2 a = 2 ∧ dR 7 a = 2 ∧ dR 4 a = 2 := by decide
  have hd1 : dR 1 false = 0 := by decide
  rcases (by omega : t % 4 = 0 ∨ t % 4 = 1 ∨ t % 4 = 2 ∨ t % 4 = 3) with h | h | h | h
  · have hψ : (t + 2 * Rw t + 2 + 7) % 8 = 1 := by unfold Rw; omega
    rw [hψ, ha hψ, hd1]; unfold Rw; omega
  · have hψ : (t + 2 * Rw t + 2 + 7) % 8 = 2 := by unfold Rw; omega
    rw [hψ, (hd a).1]; unfold Rw; omega
  · have hψ : (t + 2 * Rw t + 2 + 7) % 8 = 7 := by unfold Rw; omega
    rw [hψ, (hd a).2.1]; unfold Rw; omega
  · have hψ : (t + 2 * Rw t + 2 + 7) % 8 = 4 := by unfold Rw; omega
    rw [hψ, (hd a).2.2]; unfold Rw; omega

/-- **The witness front.** At phase class `7`, a row whose mismatch vanishes at every edge depth
`≥ 1` heals at times `1, 2` and then has the forced front `Rw t` (cycle of front phases
`2 → 7 → 4 → 1`, moves `+2, +2, +2, 0`). -/
theorem wit_front (x : Nat → Bool) (hx : x 0 = true) (h9 : ∀ n, 9 ≤ n → D x 7 n 0 = false) :
    ∀ u, FrontAt x 7 (u + 1) (Rw (u + 1)) ∧
      ((u + 1 + 2 * Rw (u + 1) + 2 + 7) % 8 = 1 → D x 7 (Rw (u + 1) - 1) (u + 1) = false) := by
  intro u
  induction u with
  | zero =>
    have d8 : D x 7 8 0 = true := by rw [D_eight x hx]; decide
    have d7 : D x 7 7 0 = true := by rw [D_low x 7 7 0 (by decide)]; decide
    have q9 : D x 7 9 1 = false := by
      rw [D_step' x 7 9 0 8 7 1 (by decide) rfl rfl (by decide), h9 9 (by decide), d8, d7]; decide
    have q10 : D x 7 10 1 = false := by
      rw [D_step' x 7 10 0 9 8 3 (by decide) rfl rfl (by decide), h9 10 (by decide),
        h9 9 (by decide), d8]; decide
    have qn : ∀ n, 11 ≤ n → D x 7 n 1 = false := by
      intro n hn
      rw [D_step x 7 n 0 (by omega), h9 n (by omega), h9 (n - 1) (by omega), h9 (n - 2) (by omega),
        F_zero]; rfl
    have hR1 : Rw (0 + 1) = 4 := by decide
    rw [hR1]
    refine ⟨⟨?_, ?_⟩, ?_⟩
    · rw [D_low x 7 4 (0 + 1) (by decide)]; decide
    · intro n hn
      by_cases hn11 : 11 ≤ n
      · exact qn n hn11
      · rcases (by omega : n = 5 ∨ n = 6 ∨ n = 7 ∨ n = 8 ∨ n = 9 ∨ n = 10) with
          rfl | rfl | rfl | rfl | rfl | rfl
        · rw [D_low x 7 5 (0 + 1) (by decide)]; decide
        · rw [D_low x 7 6 (0 + 1) (by decide)]; decide
        · rw [D_low x 7 7 (0 + 1) (by decide)]; decide
        · rw [D_eight x hx]; decide
        · exact q9
        · exact q10
    · intro h; exact absurd h (by decide)
  | succ u ih =>
    obtain ⟨hF, hg⟩ := ih
    have hR4 : 4 ≤ Rw (u + 1) := by unfold Rw; omega
    obtain ⟨Sm, _⟩ := step x 7 (u + 1) (Rw (u + 1)) ((u + 1 + 2 * Rw (u + 1) + 2 + 7) % 8)
      (D x 7 (Rw (u + 1) - 1) (u + 1)) (D x 7 (Rw (u + 1) - 2) (u + 1)) hR4 hF rfl rfl rfl
    have hnr : ¬ ((u + 1 + 2 * Rw (u + 1) + 2 + 7) % 8 = 1 ∧
        D x 7 (Rw (u + 1) - 1) (u + 1) = true ∧ D x 7 (Rw (u + 1) - 2) (u + 1) = true) := by
      rintro ⟨h1, h2, _⟩
      rw [hg h1] at h2
      exact absurd h2 (by decide)
    obtain ⟨hF', _, hph'⟩ := Sm hnr
    have hmv := wit_move (u + 1) (D x 7 (Rw (u + 1) - 1) (u + 1)) hg
    rw [hmv] at hF' hph'
    exact ⟨hF', hph'⟩

theorem wit_arith1 (k t : Nat) (ht : t < Lw k) : Rw t < k + 8 := by
  have hL := Lw_cases k
  have hk6 : k % 6 = 0 ∨ k % 6 = 1 ∨ k % 6 = 2 ∨ k % 6 = 3 ∨ k % 6 = 4 ∨ k % 6 = 5 := by omega
  have ht4 : t % 4 = 0 ∨ t % 4 = 1 ∨ t % 4 = 2 ∨ t % 4 = 3 := by omega
  unfold Rw
  rcases hk6 with h6 | h6 | h6 | h6 | h6 | h6 <;> rcases ht4 with h4 | h4 | h4 | h4 <;> omega

theorem wit_arith2 (k : Nat) : k + 8 ≤ Rw (Lw k) := by
  have hL := Lw_cases k
  unfold Rw; omega

/-! ### Healing at time 1 (the exclusions at phase classes 2, 4 and the witness at 7) -/

theorem heal_rec (x : Nat → Bool) (c : Nat) (h1 : ∀ n, 9 ≤ n → D x c n 1 = false) :
    ∀ n n1 n2, 9 ≤ n → n1 = n - 1 → n2 = n - 2 →
      D x c n 0 = F ((2 * n + c) % 8) (D x c n1 0) (D x c n2 0) := by
  intro n n1 n2 hn hn1 hn2
  have h := D_step' x c n 0 n1 n2 ((2 * n + c) % 8) (by omega) hn1 hn2 (by omega)
  rw [h1 n hn] at h
  exact xor_false_eq h.symm

theorem pat2_step : ∀ n n1 n2, n1 = n + 1 → n2 = n + 2 →
    F ((2 * n2 + 2) % 8) (n1 % 4 != 0) (n % 4 != 0) = (n2 % 4 != 0) := by
  intro n n1 n2 h1 h2
  subst h1 h2
  rw [show (2 * (n + 2) + 2) % 8 = (2 * (n % 4) + 6) % 8 by omega,
    show (n + 1) % 4 = (n % 4 + 1) % 4 by omega, show (n + 2) % 4 = (n % 4 + 2) % 4 by omega]
  have h : n % 4 < 4 := Nat.mod_lt _ (by decide)
  generalize n % 4 = r at h ⊢
  revert r; decide

theorem pat4_step : ∀ n n1 n2, n1 = n + 1 → n2 = n + 2 →
    F ((2 * n2 + 4) % 8) (n1 % 4 != 3) (n % 4 != 3) = (n2 % 4 != 3) := by
  intro n n1 n2 h1 h2
  subst h1 h2
  rw [show (2 * (n + 2) + 4) % 8 = (2 * (n % 4)) % 8 by omega,
    show (n + 1) % 4 = (n % 4 + 1) % 4 by omega, show (n + 2) % 4 = (n % 4 + 2) % 4 by omega]
  have h : n % 4 < 4 := Nat.mod_lt _ (by decide)
  generalize n % 4 = r at h ⊢
  revert r; decide

/-- At phase class `2`, healing every depth `≥ 1` at time `1` forces the mismatch row
`0, 1, 1, (0, 1, 1, 1)*` at depths `1, 2, ...`. -/
theorem heal2 (x : Nat → Bool) (hx : x 0 = true) (h1 : ∀ n, 9 ≤ n → D x 2 n 1 = false) :
    ∀ m, D x 2 (m + 10) 0 = ((m + 10) % 4 != 0) ∧ D x 2 (m + 11) 0 = ((m + 11) % 4 != 0) := by
  have hr := heal_rec x 2 h1
  have d8 : D x 2 8 0 = true := by rw [D_eight x hx]; decide
  have d7 : D x 2 7 0 = true := by rw [D_low x 2 7 0 (by decide)]; decide
  have d9 : D x 2 9 0 = false := by rw [hr 9 8 7 (by decide) rfl rfl, d8, d7]; decide
  have d10 : D x 2 10 0 = true := by rw [hr 10 9 8 (by decide) rfl rfl, d9, d8]; decide
  have d11 : D x 2 11 0 = true := by rw [hr 11 10 9 (by decide) rfl rfl, d10, d9]; decide
  intro m
  induction m with
  | zero => exact ⟨d10, d11⟩
  | succ m ih =>
    refine ⟨ih.2, ?_⟩
    rw [hr (m + 1 + 11) (m + 11) (m + 10) (by omega) (by omega) (by omega), ih.1, ih.2]
    exact pat2_step (m + 10) (m + 11) (m + 1 + 11) (by omega) (by omega)

/-- At phase class `4` the forced row is `(1, 1, 0, 1)*`. -/
theorem heal4 (x : Nat → Bool) (hx : x 0 = true) (h1 : ∀ n, 9 ≤ n → D x 4 n 1 = false) :
    ∀ m, D x 4 (m + 10) 0 = ((m + 10) % 4 != 3) ∧ D x 4 (m + 11) 0 = ((m + 11) % 4 != 3) := by
  have hr := heal_rec x 4 h1
  have d8 : D x 4 8 0 = true := by rw [D_eight x hx]; decide
  have d7 : D x 4 7 0 = false := by rw [D_low x 4 7 0 (by decide)]; decide
  have d9 : D x 4 9 0 = true := by rw [hr 9 8 7 (by decide) rfl rfl, d8, d7]; decide
  have d10 : D x 4 10 0 = true := by rw [hr 10 9 8 (by decide) rfl rfl, d9, d8]; decide
  have d11 : D x 4 11 0 = false := by rw [hr 11 10 9 (by decide) rfl rfl, d10, d9]; decide
  intro m
  induction m with
  | zero => exact ⟨d10, d11⟩
  | succ m ih =>
    refine ⟨ih.2, ?_⟩
    rw [hr (m + 1 + 11) (m + 11) (m + 10) (by omega) (by omega) (by omega), ih.1, ih.2]
    exact pat4_step (m + 10) (m + 11) (m + 1 + 11) (by omega) (by omega)

/-- At phase class `7` the forced row is clean: it is the witness's. -/
theorem heal7 (x : Nat → Bool) (hx : x 0 = true) (h1 : ∀ n, 9 ≤ n → D x 7 n 1 = false) :
    ∀ n, 9 ≤ n → D x 7 n 0 = false := by
  have hr := heal_rec x 7 h1
  have d8 : D x 7 8 0 = true := by rw [D_eight x hx]; decide
  have d7 : D x 7 7 0 = true := by rw [D_low x 7 7 0 (by decide)]; decide
  have d9 : D x 7 9 0 = false := by rw [hr 9 8 7 (by decide) rfl rfl, d8, d7]; decide
  have d10 : D x 7 10 0 = false := by rw [hr 10 9 8 (by decide) rfl rfl, d9, d8]; decide
  have hm : ∀ m, D x 7 (m + 9) 0 = false ∧ D x 7 (m + 10) 0 = false := by
    intro m
    induction m with
    | zero => exact ⟨d9, d10⟩
    | succ m ih =>
      refine ⟨ih.2, ?_⟩
      rw [hr (m + 1 + 10) (m + 10) (m + 9) (by omega) (by omega) (by omega), ih.1, ih.2, F_zero]
  intro n hn
  have h := (hm (n - 9)).1
  rwa [show n - 9 + 9 = n by omega] at h

/-- **The floor at time 1.** Either the front at time `1` is at least `lb c`, or the phase class
is `7` and the row is the witness's (clean at every edge depth `≥ 1`). The exclusions at `c = 2, 4`
use that the healing rows there never become clean, while the clean tail does. -/
theorem floor_case (x : Nat → Bool) (hx : x 0 = true) (c k : Nat) (hc : c < 8)
    (h0 : ∀ n, k + 10 ≤ n → D x c n 0 = false) (R : Nat) (hF : FrontAt x c 1 R) :
    lb c ≤ R ∨ (c = 7 ∧ ∀ n, 9 ≤ n → D x c n 0 = false) := by
  by_cases h9 : 9 ≤ R
  · left
    have hl : lb c ≤ 9 := by
      rcases c_cases c hc with rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl <;> decide
    omega
  · have h1 : ∀ n, 9 ≤ n → D x c n 1 = false := fun n hn => hF.2 n (by omega)
    rcases c_cases c hc with rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl
    · left
      have hm : D x 0 6 1 = true := by rw [D_low x 0 6 1 (by decide)]; decide
      exact front_ge hF hm
    · left
      have hm : D x 1 8 1 = true := by rw [D_eight x hx]; decide
      exact front_ge hF hm
    · exfalso
      have hp := (heal2 x hx h1 (4 * k + 31)).1
      rw [h0 _ (by omega), show (4 * k + 31 + 10) % 4 = 1 by omega] at hp
      exact absurd hp (by decide)
    · left
      have hm : D x 3 8 1 = true := by rw [D_eight x hx]; decide
      exact front_ge hF hm
    · exfalso
      have hp := (heal4 x hx h1 (4 * k + 31)).1
      rw [h0 _ (by omega), show (4 * k + 31 + 10) % 4 = 1 by omega] at hp
      exact absurd hp (by decide)
    · left
      have hm : D x 5 8 1 = true := by rw [D_eight x hx]; decide
      exact front_ge hF hm
    · left
      have hm : D x 6 8 1 = true := by rw [D_eight x hx]; decide
      exact front_ge hF hm
    · right; exact ⟨rfl, heal7 x hx h1⟩

/-! ### The episode bound -/

/-- Steps 2-5 for a clean-tail row: from time `1` on, either the potential keeps the floor
`K c`, or the phase class is `7` and the row is the witness's. -/
theorem dichotomy (z : Nat → Bool) (c k : Nat) (hz : z 0 = true) (hc : c < 8)
    (h0 : ∀ n, k + 10 ≤ n → D z c n 0 = false) :
    (∀ u, ∃ R, Good z c (K c) (u + 1) R) ∨ (c = 7 ∧ ∀ n, 9 ≤ n → D z c n 0 = false) := by
  obtain ⟨R0, hR0, hF0⟩ := front_zero z c k h0
  obtain ⟨R1, hR1, hF1, hph1⟩ := front_succ z c 0 R0 hR0 hF0
  rcases floor_case z hz c k hc h0 R1 hF1 with hlb | hw
  · exact Or.inl (pot_inv z c (K c) ⟨R1, hR1, hF1, hph1, floor_arith c hc R1 hlb⟩)
  · exact Or.inr hw

/-- The core: no clean-tail row has its pair (offset depths `k + 8, k + 9`, edge depths `k, k + 1`)
free of mismatch on all the ticks `0 .. Lw k`. -/
theorem core (z : Nat → Bool) (c k : Nat) (hz : z 0 = true) (hc : c < 8)
    (h0 : ∀ n, k + 10 ≤ n → D z c n 0 = false)
    (hp : ∀ u, u ≤ Lw k → D z c (k + 8) u = false ∧ D z c (k + 9) u = false) : False := by
  have hcl := tail_inv z c k (Lw k) h0 hp
  have hL1 : 1 ≤ Lw k := by have := Lw_cases k; omega
  suffices hs : ∃ R, k + 8 ≤ R ∧ D z c R (Lw k) = true by
    obtain ⟨R, hR, hD⟩ := hs
    rw [hcl (Lw k) (Nat.le_refl _) R hR] at hD
    exact absurd hD (by decide)
  rcases dichotomy z c k hz hc h0 with hg | ⟨rfl, hw⟩
  · obtain ⟨R, hgR⟩ := hg (Lw k - 1)
    rw [Nat.sub_add_cancel hL1] at hgR
    exact ⟨R, final_arith c hc k R hgR.2.2.2, hgR.2.1.1⟩
  · obtain ⟨hwf, _⟩ := wit_front z hz hw (Lw k - 1)
    rw [Nat.sub_add_cancel hL1] at hwf
    exact ⟨Rw (Lw k), wit_arith2 k, hwf.1⟩

/-- Onset and phase: an episode tick `s + u` of `x` at phase `(i, q)` is a tick `u` at which the
clean-tail row of `iter s x` has no mismatch at the pair, in phase class
`c = (s + q + 2i + 6k) mod 8` (that is, `q + s + 2i - 2k`). -/
theorem pair_clean (x : Nat → Bool) (k i q s c u : Nat) (hcdef : (s + q + 2 * i + 6 * k) % 8 = c)
    (h1 : iter (s + u) x k = ether i (s + u + q))
    (h2 : iter (s + u) x (k + 1) = ether (i + 1) (s + u + q)) :
    D (tail (iter s x) k c) c (k + 8) u = false ∧ D (tail (iter s x) k c) c (k + 9) u = false := by
  rw [iter_add] at h1 h2
  have ag := iter_agree (tail_agree (iter s x) k c) u
  constructor
  · unfold D
    rw [X_ge _ (k + 8) u (by omega), Nat.add_sub_cancel, ← ag k (by omega), h1, ether_eq]
    unfold E
    rw [e_congr (show (s + u + q + 2 * i) % 8 = (u + 2 * (k + 8) + c) % 8 by omega)]
    exact Bool.xor_self _
  · unfold D
    rw [X_ge _ (k + 9) u (by omega), show k + 9 - 8 = k + 1 by omega, ← ag (k + 1) (by omega), h2,
      ether_eq]
    unfold E
    rw [e_congr (show (s + u + q + 2 * (i + 1)) % 8 = (u + 2 * (k + 9) + c) % 8 by omega)]
    exact Bool.xor_self _

/-- The episode bound at every depth (at `k = 0` it is weaker than the truth, `M(0) = 2`). -/
theorem episode_bound_all (x : Nat → Bool) (hx : x 0 = true) (k i q s : Nat) :
    ¬ (∀ t, s ≤ t → t ≤ s + Lw k →
        iter t x k = ether i (t + q) ∧ iter t x (k + 1) = ether (i + 1) (t + q)) := by
  intro hep
  have hy0 : iter s x 0 = true := by rw [iter_zero]; exact hx
  obtain ⟨c, hcdef⟩ : ∃ c, (s + q + 2 * i + 6 * k) % 8 = c := ⟨_, rfl⟩
  have hz : tail (iter s x) k c 0 = true := by simp [tail, hy0]
  apply core (tail (iter s x) k c) c k hz (by omega) (tail_clean (iter s x) k c)
  intro u hu
  obtain ⟨h1, h2⟩ := hep (s + u) (by omega) (by omega)
  exact pair_clean x k i q s c u hcdef h1 h2

/-- **The episode bound.** For every black-edge code `x` (finite or not), every depth `k ≥ 1`,
every phase `(i, q)` and every onset `s`, the pair at depths `k, k + 1` is not the ether pair of PR #69
on the `Lw k + 1` consecutive ticks `s .. s + Lw k`. -/
theorem episode_bound : ∀ (x : Nat → Bool), x 0 = true → ∀ k, 1 ≤ k → ∀ i q s : Nat,
    ¬ (∀ t, s ≤ t → t ≤ s + Lw k →
        iter t x k = ether i (t + q) ∧ iter t x (k + 1) = ether (i + 1) (t + q)) :=
  fun x hx k _ i q s => episode_bound_all x hx k i q s

/-! ### The witness -/

/-- The witness: bit `0` black, `x j = ether (j + 3) 1` for `j ≥ 1`. -/
def wit (j : Nat) : Bool := if j = 0 then true else ether (j + 3) 1

theorem wit_zero : wit 0 = true := rfl

/-- The witness's phase `(i, q, s) = (k + 3, 1, 0)` is in class `7`. -/
theorem wit_class (k : Nat) : (0 + 1 + 2 * (k + 3) + 6 * k) % 8 = 7 := by omega

theorem wit_clean : ∀ n, 9 ≤ n → D wit 7 n 0 = false := by
  intro n hn
  rw [D, X_ge wit n 0 (by omega)]
  simp only [iter, wit, E]
  rw [ite_eq_right (by omega), ether_eq,
    e_congr (show (1 + 2 * (n - 8 + 3)) % 8 = (0 + 2 * n + 7) % 8 by omega)]
  exact Bool.xor_self _

/-- **The witness.** For every `k ≥ 1` the witness `wit` carries the ether pair at depths
`k, k + 1` (phase `i = k + 3`, `q = 1`) on the ticks `0 .. Lw k - 1`. -/
theorem episode_witness : ∀ k, 1 ≤ k → ∃ x : Nat → Bool, x 0 = true ∧
    ∀ t, t < Lw k →
      iter t x k = ether (k + 3) (t + 1) ∧ iter t x (k + 1) = ether (k + 4) (t + 1) := by
  intro k hk
  refine ⟨wit, wit_zero, ?_⟩
  intro t ht
  have hD : D wit 7 (k + 8) t = false ∧ D wit 7 (k + 9) t = false := by
    cases t with
    | zero => exact ⟨wit_clean _ (by omega), wit_clean _ (by omega)⟩
    | succ u =>
      have hw := (wit_front wit wit_zero wit_clean u).1
      have hlt := wit_arith1 k (u + 1) ht
      exact ⟨hw.2 _ (by omega), hw.2 _ (by omega)⟩
  obtain ⟨h1, h2⟩ := hD
  have e1 := xor_false_eq h1
  have e2 := xor_false_eq h2
  rw [X_ge wit (k + 8) t (by omega), Nat.add_sub_cancel] at e1
  rw [X_ge wit (k + 9) t (by omega), show k + 9 - 8 = k + 1 by omega] at e2
  rw [e1, e2, ether_eq, ether_eq]
  unfold E
  exact ⟨e_congr (by omega), e_congr (by omega)⟩

/-- **The maximum.** For every `k ≥ 1`, `M(k) = Lw k = floor(2k/3) + 4 - [k ≡ 0, 2 (mod 6)]` is
the longest ether-pair episode at depths `k, k + 1` behind a black right edge: an episode of
`Lw k` ticks exists, and none has `Lw k + 1` ticks, over every code, phase and onset. -/
theorem episode_max (k : Nat) (hk : 1 ≤ k) :
    (∃ x : Nat → Bool, x 0 = true ∧ ∃ i q s : Nat, ∀ t, s ≤ t → t < s + Lw k →
        iter t x k = ether i (t + q) ∧ iter t x (k + 1) = ether (i + 1) (t + q)) ∧
    (∀ x : Nat → Bool, x 0 = true → ∀ i q s : Nat, ¬ (∀ t, s ≤ t → t ≤ s + Lw k →
        iter t x k = ether i (t + q) ∧ iter t x (k + 1) = ether (i + 1) (t + q))) := by
  refine ⟨?_, fun x hx i q s => episode_bound x hx k hk i q s⟩
  obtain ⟨x, hx, hw⟩ := episode_witness k hk
  exact ⟨x, hx, k + 3, 1, 0, fun t _ ht => hw t (by omega)⟩

/-! ### Uniqueness of the optimal prefix at phase class 7 -/

/-- At time `Lw k - 1` a front carrying the non-witness floor of class `7` is at depth `≥ k`. -/
theorem uniq_arith (k R : Nat)
    (h : 3 * (Lw k - 1) + K 7 ≤ 2 * R + G ((Lw k - 1 + 2 * R + 2 + 7) % 8)) : k + 8 ≤ R := by
  have hL := Lw_cases k
  have hk6 : k % 6 = 0 ∨ k % 6 = 1 ∨ k % 6 = 2 ∨ k % 6 = 3 ∨ k % 6 = 4 ∨ k % 6 = 5 := by omega
  simp only [K] at h
  rcases G_cases (Lw k - 1 + 2 * R + 2 + 7) with ⟨h1, h2⟩ | ⟨h1, h2⟩ | ⟨h1, h2⟩ | ⟨h1, h2⟩ |
      ⟨h1, h2⟩ | ⟨h1, h2⟩ | ⟨h1, h2⟩ | ⟨h1, h2⟩ <;>
    rw [h2] at h <;>
    rcases hk6 with h6 | h6 | h6 | h6 | h6 | h6 <;> omega

/-- At phase class `7`, a clean-tail row whose pair is clean on the ticks `0 .. Lw k - 1` is the
witness's row. -/
theorem core7 (z : Nat → Bool) (k : Nat) (hz : z 0 = true)
    (h0 : ∀ n, k + 10 ≤ n → D z 7 n 0 = false)
    (hp : ∀ u, u ≤ Lw k - 1 → D z 7 (k + 8) u = false ∧ D z 7 (k + 9) u = false) :
    ∀ n, 9 ≤ n → D z 7 n 0 = false := by
  have hcl := tail_inv z 7 k (Lw k - 1) h0 hp
  have hL2 : 2 ≤ Lw k := by have := Lw_cases k; omega
  rcases dichotomy z 7 k hz (by decide) h0 with hg | ⟨_, hw⟩
  · exfalso
    obtain ⟨R, hgR⟩ := hg (Lw k - 2)
    rw [show Lw k - 2 + 1 = Lw k - 1 by omega] at hgR
    have hR := uniq_arith k R hgR.2.2.2
    have hD := hgR.2.1.1
    rw [hcl (Lw k - 1) (Nat.le_refl _) R hR] at hD
    exact absurd hD (by decide)
  · exact hw

/-- **Uniqueness at phase class 7.** If a black-edge code has an episode of `Lw k` ticks at depths
`k, k + 1` with onset `s` and a phase `(i, q)` of the witness's class
(`s + q + 2i + 6k ≡ 7 (mod 8)`), then at time `s` its bits `0 .. k + 1` are the witness's.
(Bits beyond `k + 1` are unconstrained; the statement says nothing about other classes.) -/
theorem witness_unique (x : Nat → Bool) (hx : x 0 = true) (k i q s : Nat)
    (hc : (s + q + 2 * i + 6 * k) % 8 = 7)
    (hep : ∀ t, s ≤ t → t < s + Lw k →
        iter t x k = ether i (t + q) ∧ iter t x (k + 1) = ether (i + 1) (t + q)) :
    ∀ j, j ≤ k + 1 → iter s x j = wit j := by
  have hy0 : iter s x 0 = true := by rw [iter_zero]; exact hx
  have hz : tail (iter s x) k 7 0 = true := by simp [tail, hy0]
  have hL2 : 2 ≤ Lw k := by have := Lw_cases k; omega
  have hw := core7 (tail (iter s x) k 7) k hz (tail_clean (iter s x) k 7) (fun u hu => by
    obtain ⟨h1, h2⟩ := hep (s + u) (by omega) (by omega)
    exact pair_clean x k i q s 7 u hc h1 h2)
  intro j hj
  by_cases hj0 : j = 0
  · subst hj0; rw [hy0]; rfl
  · have e1 := xor_false_eq (hw (j + 8) (by omega))
    rw [X_ge _ (j + 8) 0 (by omega), Nat.add_sub_cancel] at e1
    simp only [iter] at e1
    rw [tail_agree (iter s x) k 7 j (by omega), e1]
    unfold wit E
    rw [ite_eq_right hj0, ether_eq]
    exact e_congr (by omega)

/-! ### Controls (kernel evaluation) -/

/-- `Lw 1 .. Lw 8 = 4, 4, 6, 6, 7, 7, 8, 8`, the longest episodes at depths `1 .. 8` found by an
exhaustive computation over the codes. -/
example : Lw 1 = 4 ∧ Lw 2 = 4 ∧ Lw 3 = 6 ∧ Lw 4 = 6 ∧ Lw 5 = 7 ∧ Lw 6 = 7 ∧ Lw 7 = 8 ∧
    Lw 8 = 8 := by decide

/-- The witness front at times `1 .. 4` is at edge depths `-4, -2, 0, 2` (offset `4, 6, 8, 10`). -/
example : Rw 1 = 4 ∧ Rw 2 = 6 ∧ Rw 3 = 8 ∧ Rw 4 = 10 := by decide

/-- The witness carries the pair at depth `6` on the ticks `0 .. 6` ... -/
example : ∀ t, t < 7 → iter t wit 6 = ether 9 (t + 1) ∧ iter t wit 7 = ether 10 (t + 1) := by
  decide

/-- ... and loses it at tick `Lw 6 = 7`; likewise at depth `5`. -/
example : ¬ (iter (Lw 6) wit 6 = ether 9 (Lw 6 + 1) ∧ iter (Lw 6) wit 7 = ether 10 (Lw 6 + 1)) ∧
    ¬ (iter (Lw 5) wit 5 = ether 8 (Lw 5 + 1) ∧ iter (Lw 5) wit 6 = ether 9 (Lw 5 + 1)) := by
  decide

/-! ### The witness named, and a finite witness -/

/-- `episode_witness` with its witness named: the code `wit` itself carries the pair. -/
theorem wit_episode (k : Nat) (hk : 1 ≤ k) : ∀ t, t < Lw k →
    iter t wit k = ether (k + 3) (t + 1) ∧ iter t wit (k + 1) = ether (k + 4) (t + 1) := by
  intro t ht
  have hD : D wit 7 (k + 8) t = false ∧ D wit 7 (k + 9) t = false := by
    cases t with
    | zero => exact ⟨wit_clean _ (by omega), wit_clean _ (by omega)⟩
    | succ u =>
      have hw := (wit_front wit wit_zero wit_clean u).1
      have hlt := wit_arith1 k (u + 1) ht
      exact ⟨hw.2 _ (by omega), hw.2 _ (by omega)⟩
  obtain ⟨h1, h2⟩ := hD
  have e1 := xor_false_eq h1
  have e2 := xor_false_eq h2
  rw [X_ge wit (k + 8) t (by omega), Nat.add_sub_cancel] at e1
  rw [X_ge wit (k + 9) t (by omega), show k + 9 - 8 = k + 1 by omega] at e2
  rw [e1, e2, ether_eq, ether_eq]
  unfold E
  exact ⟨e_congr (by omega), e_congr (by omega)⟩

/-- The witness cut after bit `k + 1`: its black bits all lie in `0 .. k + 1`. -/
def witCut (k j : Nat) : Bool := if j ≤ k + 1 then wit j else false

/-- **A finite witness.** For every `k ≥ 1` a code with no black bit beyond `k + 1` carries the
ether pair at depths `k, k + 1` on the ticks `0 .. Lw k - 1`. It agrees with `wit`
below `k + 2`, and prefix autonomy (`iter_agree`) keeps the pair. -/
theorem episode_witness_finite (k : Nat) (hk : 1 ≤ k) :
    ∃ x : Nat → Bool, x 0 = true ∧ (∀ j, k + 1 < j → x j = false) ∧
      ∀ t, t < Lw k →
        iter t x k = ether (k + 3) (t + 1) ∧ iter t x (k + 1) = ether (k + 4) (t + 1) := by
  refine ⟨witCut k, ?_, ?_, ?_⟩
  · simp [witCut, wit]
  · intro j hj
    simp only [witCut]
    rw [ite_eq_right (by omega)]
  · intro t ht
    have h0 : AgreeBelow (k + 2) (witCut k) wit := by
      intro i hi
      simp only [witCut]
      rw [ite_eq_left (by omega)]
    have ag := iter_agree h0 t
    rw [ag k (by omega), ag (k + 1) (by omega)]
    exact wit_episode k hk t ht

/-- Control: the cut witness carries the pair at depth `6` on the ticks `0 .. 6`, as `wit` does. -/
example : ∀ t, t < 7 → iter t (witCut 6) 6 = ether 9 (t + 1) ∧ iter t (witCut 6) 7 = ether 10 (t + 1) := by
  decide

end Rule30Submission

", "ProjectDir" -> $Rule30PrizeKit]
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
