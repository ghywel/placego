---
Template: ComputationalEssay
Name: The closing law of prefix doublings on Rule 30's right edge
Author: Gareth Herbert - with Claude (Anthropic) and GPT (OpenAI)
Date: 2026-11-03
Description: A partial result proved in core Lean: on the kit's gate clocks, including Rule 30's right edge, the difference order drops by exactly one across each pair of letters 10 (a doubling, then a keep), so after a doubling at period q0 (the period before that doubling) an alternating run has at most q0 - 1 pairs and closes with a doubling exactly at that length. Corollaries: 1101011 never occurs among the doubling letters, and five consecutive letters hold at most three doublings once the period is at least 4.
Abstract: See abstract.txt.
Keywords: [rule 30, Rule 30 Prize, right edge, prefix periods, difference order, gate clocks, doubling letters, Lean 4, LeanLink, partial result]
Sources: ["[The Rule 30 Prize kit](https://github.com/WolframInstitute/Rule30PrizeKit)", "[The Wolfram · Collatz · Mahler record](https://github.com/ghywel/placego)"]
Links: ["[Rule 30 Prizes](https://rule30prize.org/)", "[Kit pull request 55, the right-edge prefix clocks](https://github.com/WolframInstitute/Rule30PrizeKit/pull/55)", "[Rowland, On the right edge of Rule 30, section 5](https://arxiv.org/abs/math/0612058)"]
---

## The question

Read in the frame that moves with it, the right edge of Rule 30 is a map on bits: bit $j$ is XORed, at each step, with
the OR of bits $j - 1$ and $j - 2$. The kit's `Rule30GateClocks` allows any gate $g_j$ in place of OR. The first $n$ bits
of any seed are periodic in time, with least period $2^{E_n}$, and the exponent $E_n$ grows by $0$ or $1$ as one bit is
added. Write the growth flags as a word of **doubling letters**: letter $n$ is $1$ when adding bit $n$ doubles the
period, and $0$ when it does not.

Which words of doubling letters can occur? The kit and earlier work show that three doublings in a row are rare and that
the period grows at most like half the number of bits. This essay proves an exact rule for one family of words, the
alternating runs, for every gate with a quadratic term.

## The exact countdown

For a stream $f$ of period $M = 2^v$, the kit's `order f M` measures how many differences of $f$ vanish below the full
period: in polynomial terms, the multiplicity of the factor $1 + z$ in $\sum_{t < M} f(t) z^t$ over $\mathbb{F}_2$.

The step that matters is a pair of letters $10$. Take three consecutive streams: $s$ with period $M = 2^v \ge 2$; the
next one, $b$, which has just doubled, so that it is antiperiodic at $M$; and $h$, which integrates the gate,
$h(t + 1) = h(t) \oplus g(b(t), s(t))$, and keeps the period $2M$. In this setting the kit proves that the order drops
by **at most** one: $\mathrm{order}\, s\, M \le \mathrm{order}\, h\, (2M) + 1$ (`order_countdown_gate`). Here it is
shown that for a gate whose derivative in its newer input, $g(1, s) \oplus g(0, s)$, depends on $s$ (OR is such a gate),
it drops by **exactly** one. Past the $M$-th difference, the new stream's differences are exactly those of the older
input:

$$\Delta^{k + 2 + M} h = \Delta^{k + 1} s,$$

so the first vanishing difference of $h$ lies exactly $M + 1$ beyond that of $s$ (`order_countdown_exact`). The guards
are exactly those of this setting: the periods and the antiperiod above, $M \ge 2$, and
$\mathrm{order}\, s\, M + 1 < M$. The last one is needed because the order is capped at $M - 1$: a constant stream,
the zero stream included, has every difference vanishing and so the capped order $M - 1$, and the equality fails there.
This is a statement about a $10$ pair, not about an arbitrary step without a doubling.

## The closing law

Suppose the doubling letters, from position $n$, read

$$1\,(10)^m\,1,$$

a doubling, then $m \ge 0$ pairs "double, keep", then a doubling, where the period before the first doubling is
$q_0 = 2^{E_n}$. The first doubling makes its stream antiperiodic, which fixes its order at $q_0 - 1$. Each pair "10"
then lowers the order of the pair's first stream by exactly one, and a doubling follows exactly when that order has
reached $0$. Hence (`closing_law`):

- $m + 1 \le q_0$;
- the next letter is $1$ if and only if $m + 1 = q_0$.

A closing run therefore has length one less than a power of two. In particular:

- `no_1101011`: the word $1\,(10)^2\,1\,1$ never occurs, since $3$ is not a power of two;
- `no_three_at`: three doublings in a row need $q_0 = 1$;
- `no_11011_at`: $11011$ closes with a doubling only when $q_0 = 2$;
- `five_letter`: once the period is at least $4$, any five consecutive letters contain at most three doublings.

These hold for every seed, finite or infinite, and every family of quadratic gates; `closing_law_or` states the Rule 30
case.

## A picture: the letters of the single black cell

The gate clock of OR from a single black bit, with bits computed for $2^{E}$ steps as each new bit is added:

```wl
orClock[seed_List, nbits_Integer] := Module[{x = PadRight[seed, nbits + 2], hist, ex = {0}, col, force, acc},
  hist = {x};
  col[k_, t_] := If[k == 0, 0, hist[[t + 1, k]]];
  Do[
    While[Length[hist] < 2^Last[ex],
      With[{y = Last[hist]}, AppendTo[hist, Table[BitXor[y[[j]], If[j == 1, 0, BitOr[y[[j - 1]], If[j == 2, 0, y[[j - 2]]]]]], {j, Length[y]}]]]];
    acc = Mod[Total[Table[BitOr[col[n, t], col[Max[n - 1, 0], t]], {t, 0, 2^Last[ex] - 1}]], 2];
    AppendTo[ex, Last[ex] + acc], {n, 0, nbits - 1}];
  ex];
ex = orClock[{1}, 22];
letters = Differences[ex];
runs = Flatten[Table[With[{n = n0}, Module[{m = 0, out = {}},
  While[n + 2 m + 3 <= Length[letters] && letters[[n + 1]] == 1 && letters[[n + 2 m + 2]] == 1,
    AppendTo[out, {n, m, 2^ex[[n + 1]], letters[[n + 2 m + 3]]}];
    If[letters[[n + 2 m + 3]] == 0, m++, Break[]]];
  out]], {n0, 0, Length[letters] - 3}], 1];
Column[{Row[{"letters: ", StringJoin[ToString /@ letters]}],
  Grid[Prepend[{#[[1]], #[[2]], #[[3]], #[[4]], Boole[#[[2]] + 1 == #[[3]]]} & /@ runs,
    {"start n", "pairs m", "q0", "next letter", "law: m+1 = q0"}], Frame -> All]}]
```

Each row is a run $1\,(10)^m\,1$; the next letter is $1$ exactly in the rows where $m + 1 = q_0$. Within the 22 letters
displayed, a run closes with a doubling only once, the $11011$ at $q_0 = 2$; nothing is claimed here about later
letters.

## Related work and what is new

- **The kit.** `Rule30DifferenceOrder` and `Rule30GateClocks` give the order, the reset law and the countdown
  inequality used here. Kit pull request 55 (the right-edge prefix clocks) already proves, for OR, that $11011$ does not
  occur once the period is at least $4$, using the countdown inequality.
- **The portal.** Earlier gate-clock submissions bound the prefix exponent and prove `no_three` and the "01" doubling
  test, without the exact countdown.
- **Literature.** Rowland, section 5, studies the right edge's periods and their growth.
- **New here.** The countdown as an equality for every quadratic gate, and from it the closing law for every $m$ with
  its exact closing length, kernel-checked. The difference-order mechanism itself is classical.
- **Scope.** Statements about the doubling letters of gate clocks. Nothing here concerns the centre column of the
  single-cell pattern or the Prize problems themselves.
