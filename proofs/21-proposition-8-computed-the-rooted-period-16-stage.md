# Proposition 8 (computed): the rooted period-16 stage is finite, with sixteen histories

*The waiting room (not yet verified). Derived from [PROOFS.md](../PROOFS.md), entry "21. Proposition 8 (computed):
the rooted period-16 stage is finite, with sixteen histories"; rebuild with `python3 proofs/build.py`. Edit the
proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** in the waiting room: stated with a proof, not yet checked by a second reader.

## In plain words

Every way the left side can grow through period sixteen has been listed, and there are only sixteen.

**What it says.** Started from the single cell, the left side can branch at a few places while its repeating pattern is sixteen steps long. Following every branch shows exactly fifteen places where it can split, and sixteen ways it can go, each reaching a repeat length of thirty-two after between about 88,000 and 894,000 steps. The single cell's own history gets there first.

**Why it matters.** It replaces a lower bound with a complete list. Every possible history is now known to take at least 87,867 steps to double its repeat length to thirty-two, and at most 894,235.

**An everyday picture.** A family tree drawn out to the last cousin: instead of guessing how many lines there are, every line has been followed until it ends.

## The formal statement and proof

*Where:* CLOUD-LOCAL.md, TM5 and TM5b (2026-10-07 14:45 and 14:50), chat L178 and L179; `tests/probes/lexicon/rule30_tm5.py` and `rule30_tm5b.py`. *Bears on:* PERIOD-TWO.md Q7, gap 2 (the record of $R_5$ and $\lambda_4$); G184, G200, G204. *Status:* certified by computation (Local, 2026-10-07); second reader wanted.

**Proposition 8 (computed).** Identify rooted histories (G165) up to temporal rotation. The period-16 stage of the
rooted tree, from the entry $N_4 = 400$ to the entries to period 32, has exactly fifteen genuine branch nodes, at
depths 53,207, 58,286, 72,575, 165,748, 174,449, 179,399, 243,767, 350,243, 445,474, 482,608, 485,619, 537,692, 563,842,
603,582 and 760,454. It has exactly sixteen histories, entering period 32 at

```math
N_5 \in \{87\,867,\ 183\,184,\ 196\,189,\ 229\,338,\ 253\,537,\ 271\,596,\ 291\,257,\ 527\,724,\ 551\,910,\ 555\,813,\ 575\,211,\ 634\,886,\ 645\,655,\ 667\,052,\ 770\,532,\ 894\,235\}.
```

So every rooted history has $87{,}867 \le N_5 \le 894{,}235$, that is $2{,}745.8 \le R_5 \le 27{,}944.8$. The minimum is
attained only by the single cell's own history.

*Proof (certificate).* The walk is exact, for three reasons.
- A nonzero driver $b$ has exactly one 16-periodic child: at a time $t_0$ with $b(t_0) = 1$ the equation gives
  $c(t_0 + 1) = a(t_0) + 1$ whatever $c(t_0)$ is, and the rest of $c$ follows round the cycle. At a zero driver
  $(a, 0)$ the integration $c(t + 1) = c(t) + a(t)$ closes, with the two children $c$ and $c + 1$, exactly when $a$
  has even parity; with odd parity the history leaves period 16. Following every child therefore enumerates the tree.
- The rule commutes with temporal rotation. When the two children are rotations of each other, so are the whole
  suffixes they start, and one is followed; otherwise both are.
- Every transition is checked by the literal equation $Sc = a + (b \vee c)$ at all 16 times, separately from the
  constructor.

`rule30_tm5b.py` followed every history from the root to its first odd zero or to depth $10^6$. No history was alive
at the bound and no cap fired, so the enumeration is complete.

Two independent codes agree. TM6's C program (`rule30_tm6.c`, common period 32) found the same fifteen branches and
saw the same sixteen exits as doublings. The single cell's left side computed directly from Rule 30
(`rule30_leftside_million.py`) and its three flipped sides realise four of the histories, exiting period 16 at
87,866, 183,183, 229,337 and 291,256. Every history's excursion lengths sum to its own $N_5 - 400$, every branch
driver has even parity and every exit driver odd. $\square$
