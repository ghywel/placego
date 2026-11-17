---
Template: ComputationalEssay
Name: Nested record thresholds for every two-input gate clock
Author: Gareth Herbert - with Claude (Anthropic) and GPT (OpenAI)
Date: 2026-10-31
Description: A partial result proved in core Lean: for every two-input gate at each depth and every seed, the first 2m bits of the edge map have period dividing 2^(m+2) for all m below 2058, where the record-charge bound allowed 2^(m+3) from m = 19
Abstract: For gates g_j, one per depth, and any seed, bit j of the edge map evolves by x_j(t+1) = x_j(t) XOR g_j(x_(j-1)(t), x_(j-2)(t)), missing bits white; with g = OR this is the right edge of Rule 30. Our earlier submission R30-20261030-7b0d12 proved that the first 2m bits have period 2^E(2m) with E(2m) <= m + Q_0(m), the kit's record-charge bound, which allows the excess E(2m) - m to reach 3 from m = 19. We prove it cannot do so before 2058: E(2m) <= m + 2 for every m < 2058, every gate family and every seed (`Rule30Submission.prefixExp_le_add_two`, `Rule30Submission.first_excess_three`). Three new laws hold for every gate: no three consecutive doublings once the period is at least 2 (`Rule30Submission.no_three`); after a pair whose second bit alone doubles, the next bit doubles exactly when the gate is quadratic and the pair's first bit has odd weight (`Rule30Submission.after01_double_iff`); and after two doublings from period M, the next bit's difference order is at least M - 2 (`Rule30Submission.after11_order`). Choosing the stretch after the last visit to excess 1 before excess 3 first appears, these force two countdowns, of the first bits' order and then of the last bits' resource, which cost at least 2058 pairs together. A computed family, found by search, attains excess 2 from m = 3. Nothing is claimed about excess 3 being reached, about later thresholds or about the centre column.
Keywords: [rule 30, Rule 30 Prize, right edge, T-functions, prefix periods, record charge, finite differences, Boolean gates, Lean 4, LeanLink, partial result]
Sources: ["[The Rule 30 Prize kit](https://github.com/WolframInstitute/Rule30PrizeKit)", "[The Wolfram · Collatz · Mahler record](https://github.com/ghywel/placego)"]
Links: ["[Rule 30 Prizes](https://rule30prize.org/)", "[Half-rate prefix clocks for every two-input gate (R30-20261030-7b0d12)](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261030-7b0d12)", "[Kit pull request 62: Rule30GateClocks](https://github.com/WolframInstitute/Rule30PrizeKit/pull/62)"]
---

## The question

Take a gate $g_j : \{0,1\}^2 \to \{0,1\}$ for each depth and a seed, and let

$$x_j(t+1) = x_j(t) \oplus g_j\bigl(x_{j-1}(t),\, x_{j-2}(t)\bigr), \qquad x_{-1} = x_{-2} = 0.$$

With OR at every depth this is the right edge of Rule 30. The first $n$ bits evolve on their own, with least period
$2^{E(n)}$, and each new bit keeps the period or doubles it. Our earlier submission (R30-20261030-7b0d12) proved the
kit's half-rate bound for every such family, $E(2m) \le m + Q_0(m)$, where $Q_0$ comes from the record-charge
thresholds $1, 3, 19, 2^{21} + 19, \dots$. So the excess $E(2m) - m$ may be 2 from $m = 3$ and 3 from $m = 19$.

Is that second threshold real? An exact search over all gate families, to 9 bits, and a beam search, to 38 bits, never
found excess 3. They did find excess 2 sustained by a rigid pattern. This essay proves why: excess 3 needs at least
2058 pairs of bits, for every gate family and every seed.

## Three laws for every gate

Read the bits in pairs, pair $i$ being bits $2i$ and $2i+1$, and write a pair as $11$, $10$, $01$ or $00$ according
to which of its bits double. Write a gate as $g(b,s) = \lambda bs \oplus \alpha b \oplus \beta s \oplus \gamma$.

**No three in a row** (`no_three`). If two consecutive bits both double, from a prefix of period $M \ge 2$, then
over the new period $4M$ the two inputs of the next gate have even weight, and so does their AND: pairing each time
with its partner half a period later, the AND has the weight of the older input over $2M$, which is $M$. Every term of
every gate is even, so the next bit cannot double.

**The test after a $01$ pair** (`after01_double_iff`). If a pair's first bit keeps the period $P \ge 2$ and its second
doubles, the next bit doubles exactly when $\lambda = 1$ and the first bit has odd weight over $P$. Odd weight is
order 0 in the kit's difference order (`order_zero_iff`, from $\Delta^{2^v - 1} f(t) = \sum_{k < 2^v} f(t+k)$).

**A start after $11$** (`after11_order`). After two doublings from period $M = 2^e \ge 4$, the next bit has order at
least $M - 2$ at length $4M$. The bit's difference is its forcing, and the newer input $b$ is complemented by a shift
of $2M$, so the bit's $\Delta^{2M+1}$ is $\lambda s \oplus \alpha$ (`vanish_past_gate`). The older input $s$ is
complemented by a shift of $M$, so $\Delta^{M+1} s = 0$. Hence $\Delta^{3M+2}$ of the bit vanishes.

Two laws come from the earlier submission: within a run of $01$ pairs the first bits' order drops by at most one per
pair, and through a $10$ pair the last bit's resource does too (both `order_countdown_gate`). A $01$ leaves its last
bit with resource $2^{E-1} - 1$, half its period minus one (`order_of_antiperiod`), and a $11$ needs resource 0
before it (`order_reset_before_gate`).

## The last visit

The excess increases only at a $11$ pair, and a $00$ pair lowers it. Suppose it first reaches 3 at pair-count $N$,
and let $K$ be the last pair-count before that with excess at most 1. This choice isolates a stretch of constant
excess 2 between two bounding $11$ pairs: pair $K$ is $11$, the pairs strictly between are $01$ or $10$, and the last
pair is $11$. Losses and recoveries before $K$ do not matter. They are outside the stretch.

- $K \ge 2$, since excess 2 at pair-count 1 or 2 would need $E(2) = 3$, which is impossible, or $E(4) = 4$, four
  doublings in a row, which breaks no-three. So the period before pair $K$ is $M = 2^{K+1} \ge 8$.
- Pair $K+1$ is $01$, by no-three, and its first bit has order at least $M - 2$.
- No first bit can double until that order has counted down to 0, which takes at least $M - 1$ pairs of $01$.
- After the last $01$ pair, at index $\ell \ge K + M - 1$, the resource is $2^{\ell+2} - 1$. Only $10$ pairs follow,
  each lowering it by at most one, and the final $11$ needs it at 0.

So $N \ge \ell + 1 + 2^{\ell + 2} \ge 9 + 1 + 2^{11} = 2058$ (`first_excess_three`), and therefore
$E(2m) \le m + 2$ for every $m < 2058$ (`prefixExp_le_add_two`). Our hand sketch of the same argument at every level
puts each threshold about two exponentials above the previous one, against one for the record charge. It is neither
formalized nor claimed here: only the step to excess 3 is.

## A computation

The first twenty gates of a family found by our beam search, in truth-table notation (index $2b + s$, so 1 is NOR, 2
is $\lnot b \land s$, 4 is $b \land \lnot s$ and 3 is $\lnot b$), from the all-zero seed:

```wl
familyGates = {1, 1, 1, 1, 4, 2, 1, 1, 1, 1, 2, 4, 1, 1, 1, 1, 1, 1, 1, 3};
gateBit[tab_, b_, s_] := BitGet[tab, 2 b + s];
edgeStep[x_List] := Table[BitXor[x[[j]], gateBit[familyGates[[j]], If[j > 1, x[[j - 1]], 0], If[j > 2, x[[j - 2]], 0]]], {j, Length[x]}];
orbit = NestList[edgeStep, ConstantArray[0, 20], 2^12];
exponent[n_] := SelectFirst[Range[0, 12], Take[orbit[[2^# + 1]], n] === Take[First[orbit], n] &];
pairs = Table[StringJoin[ToString /@ {exponent[2 i + 1] - exponent[2 i], exponent[2 i + 2] - exponent[2 i + 1]}], {i, 0, 9}];
<|"E(2m), m = 0..10" -> Table[exponent[2 m], {m, 0, 10}],
  "m + 2" -> Table[m + 2, {m, 0, 10}],
  "pairs (first bit, last bit doubles)" -> pairs|>
```

Prefix periods are powers of two, so each exponent is the least $e$ at which the first $n$ bits return after $2^e$
steps. From $m = 3$ the exponent is exactly $m + 2$, the bound. The pairs are $11, 10, 11$ and then seven $01$
pairs. That is the first countdown of the last-visit argument with $K = 2$ and $M = 8$, and it is as short as the
argument allows, $M - 1 = 7$ pairs. In our search the family continues to 38 bits with nine $10$ pairs, the start of
the second countdown, which needs $2^{11} - 1$ of them. That is a computation; the theorem is below.

## The formal proof

The module, in core Lean, imports only the official statement module. It contains our earlier submission unchanged,
including its copies of the kit's `Rule30RecordCharge` and `Rule30DifferenceOrder`, and then the new section. LeanLink
1.2.2 hides names containing `.rec` unless internal names are included, so the import includes them.

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
opens = {"Rule30Submission", "Rule30Submission.Rule30RecordCharge", "Rule30Submission.Rule30DifferenceOrder"};
heads = {"prefixExp_le_add_two", "first_excess_three", "no_three", "after01_double_iff", "after11_order"};
Column[rule30Submission["Rule30Submission." <> #]["TypeForm", "Open" -> opens] & /@ heads]
```

Their axioms are standard ones only:

```wl
AssociationMap[rule30Submission["Rule30Submission." <> #]["Axioms"] &, heads]
```

The kernel accepts every declaration of the module again. This is the replay the verifier runs. It comes last because
it resets LeanLink's elaboration state:

```wl
rule30Submission["Rule30Submission.prefixExp_le_add_two"]["KernelCheck"]
```

## What is not proved

- That excess 3 is ever reached, at pair 2058 or later. The bound is a lower bound on the time, not an attainment.
- The thresholds beyond the first. A hand sketch repeats the argument, but only the step to excess 3 is formalized.
- Anything about the limiting rate: the leading half-rate term is unchanged. No lower bound or density is claimed.
- Gates that read more than the two nearer bits, or change with time.
- Anything about the centre column of Rule 30 or a Prize problem.

## Relation to earlier work

The record-charge count is AIOvernight's `Rule30RecordCharge` (R30-20261026-1b82d8), and the difference order is the
kit's `Rule30DifferenceOrder`. The OR-specific predecessors of no-three and the doubling rule are the kit's
`Rule30RightPeriods.no_three` and `e_step`, and the prefix-clock organization is Troy Lowry's kit pull request 55. The
gate-generic bound this sharpens is our R30-20261030-7b0d12, also kit pull request 62. The last-visit argument was
written independently by Claude and by GPT in our joint record, and each read the other's. The search that found the
witness family is in the same record.
