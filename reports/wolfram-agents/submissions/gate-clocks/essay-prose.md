---
Template: ComputationalEssay
Name: Half-rate prefix clocks for every two-input gate
Author: Gareth Herbert - with Claude (Anthropic) and GPT (OpenAI)
Date: 2026-10-30
Description: A partial result proved in core Lean: the half-rate bound on the periods of rule 30's right edge holds with any two-input gate in place of OR, at every depth and from any starting window, and affine gates have logarithmic exponents
Abstract: Rule 30's right edge, read in the frame that moves with it, is the map x_j -> x_j XOR (x_(j-1) OR x_(j-2)) on binary sequences. Its first n bits repeat with period 2^E(n), and the kit proves E(n) <= ceil(n/2) + Q_0(floor(n/2)), where Q_0 grows like an iterated logarithm (`Rule30RightPeriods.per_upper_half`). We prove that this upper bound does not depend on OR. Take any family of two-input gates g_j, one per depth, and any seed, finite or infinite, and let bit j evolve by x_j(t+1) = x_j(t) XOR g_j(x_(j-1)(t), x_(j-2)(t)), missing bits white. The exponent obtained by lifting one bit at a time is exactly that of the least period (`Rule30Submission.prefix_period_iff`), and every window of bits obeys the kit's record-charge bound E(a+2m) - E(a) <= m + Q_(E(a))(m) <= m + Q_0(m) (`Rule30Submission.prefix_window_bound`, `Rule30Submission.prefix_window_le_B`, `Rule30Submission.prefixExp_le_B`). If every gate is affine, the first n bits have period dividing 2^r whenever n + 1 <= 2^r (`Rule30Submission.affine_prefix_bound`). The reason is that a gate's derivative in its newer input is constant, s or NOT s, so one more finite difference removes it, and the kit's reset and countdown laws need nothing else. No lower bound, doubling density or statement about the centre column is claimed.
Keywords: [rule 30, Rule 30 Prize, right edge, T-functions, triangular maps, prefix periods, finite differences, Boolean gates, Lean 4, LeanLink, partial result]
Sources: ["[The Rule 30 Prize kit](https://github.com/WolframInstitute/Rule30PrizeKit)", "[The Wolfram · Collatz · Mahler record](https://github.com/ghywel/placego)"]
Links: ["[Rule 30 Prizes](https://rule30prize.org/)", "[Rule30RecordCharge in the kit](https://github.com/WolframInstitute/Rule30PrizeKit/blob/main/lean/Ruliology/CellularAutomata/Rule30RecordCharge.lean)", "[Kit pull request 55: prefix clocks](https://github.com/WolframInstitute/Rule30PrizeKit/pull/55)"]
---

## The question

Grow rule 30 from a row whose right part is white, and read the cells just behind its right edge in the frame that
moves with the edge. Bit $j$ is the cell $j$ steps behind the edge, and one step of rule 30 becomes

$$x_j(t+1) = x_j(t) \oplus \bigl(x_{j-1}(t) \lor x_{j-2}(t)\bigr),$$

with $x_{-1} = x_{-2} = 0$. Each bit is changed only by the two bits nearer the edge, so the first $n$ bits evolve on
their own, by a permutation of $2^n$ states. Their least period is therefore a power of two, $2^{E(n)}$, and adding
one bit either keeps it or doubles it. The kit proves that the doublings come at half rate at most:
$E(n) \le \lceil n/2 \rceil + Q_0(\lfloor n/2 \rfloor)$, where $Q_0$ is at most $3$ for every $n$ below about
four million and grows like an iterated logarithm (`Rule30RightPeriods.per_upper_half`).

How much of this is about rule 30's OR? For the upper bound, none of it. This essay proves the same bound when the OR
is replaced by any Boolean function of the two nearer bits, chosen independently at every depth.

## The map and its prefix clocks

Fix a gate $g_j : \{0,1\}^2 \to \{0,1\}$ for each depth $j$ and a seed, a binary sequence $x(0)$ that may be
infinite. Let

$$x_j(t+1) = x_j(t) \oplus g_j\bigl(x_{j-1}(t),\, x_{j-2}(t)\bigr), \qquad x_{-1} = x_{-2} = 0.$$

So bit $0$ may toggle, if $g_0(0,0) = 1$, and bit $1$ is driven by bit $0$ alone. OR at every depth is rule 30's edge.
AND is the "nearsighted binary counter" studied by Skirrow. XOR is a linear map.

The first $n$ bits again evolve by a permutation of their own. Suppose they have period $P = 2^E$, and consider bit
$n$. Its forcing $f(t) = g_n(x_{n-1}(t), x_{n-2}(t))$ has period $P$, so after $P$ steps bit $n$ has been flipped
$f(0) + \dots + f(P-1)$ times. If that number is even, the first $n+1$ bits have period $P$; if it is odd, bit $n$
is complemented by a shift of $P$ and the period doubles. This is the lifting rule for triangular maps
(Klimov–Shamir; the kit's `TFunctionCycles`). The formal proof defines `prefixExp g x n` by applying it one bit at a
time, and proves that it is exactly the least period's exponent: $P$ is a period of the first $n$ bits if and only if
$2^{\texttt{prefixExp}\ g\ x\ n}$ divides $P$ (`prefix_period_iff`). This holds for every seed, finite or not.

## One more difference

Write $\Delta f(t) = f(t+1) \oplus f(t)$. Over $\mathbb{F}_2$, $\Delta^{2^v} f(t) = f(t + 2^v) \oplus f(t)$. Take
three consecutive bits after a doubling: $s = x_{j-2}$ with period $M = 2^v$, $b = x_{j-1}$ complemented by a shift of
$M$, and $h = x_j$ with $h(t+1) = h(t) \oplus g(b(t), s(t))$. Then

$$\Delta\bigl(h(t+M) \oplus h(t)\bigr) = g\bigl(1 \oplus b(t), s(t)\bigr) \oplus g\bigl(b(t), s(t)\bigr) = \alpha \oplus \lambda\, s(t),$$

where $g(b,s) = \lambda bs \oplus \alpha b \oplus \beta s \oplus \gamma$. The derivative of a two-input gate in its
newer input is a function of the older input alone: constant, $s$ or $\lnot s$. So

$$\Delta^{M+1+r} h = \lambda\, \Delta^r s \qquad (r \ge 1),$$

and whenever a positive difference of $s$ vanishes, so does the corresponding difference of $h$ (`vanish_comp`,
`vanish_past_gate`). For OR, $\lambda = \alpha = 1$, and this is the kit's `dif_shift_sum`.

The kit measures each bit by its *difference order*: for a stream of period $L$, the largest $r \le L - 1$ with
$\Delta^{L-r}$ of the stream identically zero. Its two laws for the half-rate proof are a reset (the order of $s$ is
$0$ just before two doublings in a row) and a countdown (a single doubling lowers it by at most one). Both use only
the implication above, for either value of $\lambda$, and never divide by it. So they hold for every gate
(`order_reset_before_gate`, `order_countdown_gate`).

## The bound

The kit's record-charge count (`Rule30RecordCharge`) turns those laws into the bound, and it never sees the gate. Read
the bits in pairs, from any starting depth $a$, and let the exponent's excess over the number of pairs be charged
against the resource. Two doublings in a row need the resource at zero, and leave it exponentially large. With
thresholds

$$T_\nu(0) = 1, \qquad T_\nu(q+1) = T_\nu(q) + 2^{\nu + T_\nu(q) + q},$$

and $Q_\nu(m)$ the least $q$ with $m < T_\nu(q)$, the result is

$$E(a + 2m) - E(a) \le m + Q_{E(a)}(m) \le m + Q_0(m)$$

for every gate family, seed and window (`prefix_window_bound`). The thresholds $T_0$ are $1, 3, 19, 2^{21} + 19$,
so $Q_0(m) \le 3$ for $m \le 2^{21} + 18$. Any window of $n$ bits raises the exponent by at most
$B(n) = \lceil n/2 \rceil + Q_0(\lfloor n/2 \rfloor)$ (`prefix_window_le_B`), and the first $n$ bits have period
dividing $2^{B(n)}$ (`prefixExp_le_B`).

## Affine gates

If every gate is affine ($\lambda_j = 0$), the derivative is constant and the bound improves to a logarithm. By
induction, bit $k$ has $\Delta^{k+2}$ identically zero. Over $\mathbb{F}_2$ that makes it periodic with period $2^r$
as soon as $k + 2 \le 2^r$. So the first $n$ bits have period dividing $2^r$ whenever $n + 1 \le 2^r$
(`affine_prefix_bound`). This is unitriangular nilpotency, here proved through the difference order instead of
matrices.

## A computation

The theorems need no computation. For illustration, here are the exponents $E(0), \dots, E(12)$ for three gates, next
to the bound $B(n)$, and for a map outside the class. The binary counter flips bit $j$ when all lower bits are $1$, so
it reads every lower bit rather than two.

```wl
gateBit[tab_, b_, s_] := BitGet[tab, 2 b + s];
edgeStep[tab_][x_List] := Table[BitXor[x[[j]], gateBit[tab, If[j > 1, x[[j - 1]], 0], If[j > 2, x[[j - 2]], 0]]], {j, Length[x]}];
counterStep[x_List] := Reverse[IntegerDigits[FromDigits[Reverse[x], 2] + 1, 2, Length[x]]];
prefixExponents[stepper_, start_List] := Module[{orbit = NestList[stepper, start, 2^Length[start]]},
  Table[Log2[SelectFirst[Range[2^k], Take[orbit[[# + 1]], k] === Take[start, k] &]], {k, 0, Length[start]}]];
threshold[nu_, q_] := If[q == 0, 1, threshold[nu, q - 1] + 2^(nu + threshold[nu, q - 1] + q - 1)];
q0[d_] := NestWhile[# + 1 &, 0, ! (d < threshold[0, #]) &];
bound[n_] := Ceiling[n/2] + q0[Floor[n/2]];
seedBits[k_] := PadRight[Reverse[IntegerDigits[k, 2]], 12];
<|"B(n), n = 0..12" -> bound /@ Range[0, 12],
  "OR (gate 14) from seed 1" -> prefixExponents[edgeStep[14], seedBits[1]],
  "AND (gate 8) from seed 3" -> prefixExponents[edgeStep[8], seedBits[3]],
  "XOR (gate 6) from seed 1" -> prefixExponents[edgeStep[6], seedBits[1]],
  "binary counter, which reads every lower bit" -> prefixExponents[counterStep, seedBits[0]]|>
```

A gate is given by its truth table, read at index $2b + s$, so OR is 14, AND is 8 and XOR is 6. The exponents are found
by the first return of the first $k$ bits, without using the lifting rule. OR from a single black cell is rule 30's
edge itself. The three gates stay within $B(n)$, and XOR within
$\lceil \log_2(n+1) \rceil$. The counter's exponent is $n$, which passes $B(n)$ from $n = 4$ on. The two-input
hypothesis is what the proof uses, and this example shows it cannot be dropped. A larger check of the definitions, over
all sixteen gates and four mixtures, eight seeds and sixteen bits, is in our record. It also is a computation, not
evidence for the theorems, which are proved below.

## The formal proof

The module, in core Lean, imports only the official statement module. The kit's `Rule30RecordCharge` and
`Rule30DifferenceOrder` are copied into it unchanged, because the verifier's kit predates them. LeanLink 1.2.2 hides
names containing `.rec` (such as `record_potential` and the field `recurrence`) unless internal names are included, so
the import includes them, to check the whole module.

```wl
Needs["Wolfram`LeanLink`"];
$Rule30PrizeKit = Environment["RULE30PRIZE_KIT"];
DirectoryQ[$Rule30PrizeKit]
```

```wl
rule30Submission = LeanImportString["%%LEAN%%", "ProjectDir" -> $Rule30PrizeKit, "IncludeInternal" -> True]
```

## The formal checks

The headlines, as Lean prints them:

```wl
opens = {"Rule30Submission", "Rule30Submission.Rule30RecordCharge"};
heads = {"prefix_period_iff", "prefix_window_bound", "prefix_window_le_B", "prefixExp_le_B", "affine_prefix_bound"};
Column[rule30Submission["Rule30Submission." <> #]["TypeForm", "Open" -> opens] & /@ heads]
```

Their axioms are standard ones only:

```wl
AssociationMap[rule30Submission["Rule30Submission." <> #]["Axioms"] &, heads]
```

The kernel accepts every declaration of the module again. This is the replay the verifier runs. It comes last because
it resets LeanLink's elaboration state:

```wl
rule30Submission["Rule30Submission.prefix_window_bound"]["KernelCheck"]
```

## What is not proved

- No lower bound. AND fixes every seed with no two adjacent black bits, so a gate need not force any doubling, and
  the exponent of the AND counter from seed 3 grows only logarithmically. For OR the kit's own lower bounds apply.
- No doubling density, limit or comparison between gates beyond the common upper bound.
- Gates that read more than the two nearer bits, or change with time, are outside the theorem; the counter above
  shows the bound fails for the first kind. Our record has sketches for gates with a fixed temporal phase. They are
  not part of this submission, and neither are refinements for particular gates.
- Nothing here concerns the centre column of rule 30 or decides a Prize problem.
- We found no gate-generic statement of this bound in the kit, its open pull requests or the portal's submissions.
  That is a statement about our search, not a proof that none exists.

## Relation to earlier work

The period lifting of triangular maps of the 2-adic integers is Klimov and Shamir's theory of T-functions, in the kit
as `TFunctionCycles`. Anashin's results on periodically switched T-functions concern maximal period. Their
hypotheses need a lower-bit coefficient that two-input gates lack from depth 3 on, so they neither give nor contradict
this bound. The half-rate bound for rule 30 is the kit's `per_upper_half`: its difference order is `Rule30DifferenceOrder`,
and its record-charge count is AIOvernight's `Rule30RecordCharge` (submission R30-20261026-1b82d8). Troy Lowry's kit
pull request 55 extends that proof to the prefix clocks of arbitrary right-edge starts, with OR. Here the gate is a
parameter, and the window may start at any depth. The AND counter from two adjacent black cells is described in
Natalia Skirrow's notes on nearsighted binary counters. The observation that the upper bound survives every gate was
made in our joint record, by Cloud and GPT, and Local formalized it.
