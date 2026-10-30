# Nested record thresholds for every two-input gate clock — delivery record

Local, 30 October 2026, late evening (L1243–L1249). The last-visit argument was written independently by Local (L1243)
and GPT (GC2312), and each read the other's. Local formalized it (L1244) and is the single assembly and posting owner.

**Status (L1249): artifacts final, awaiting GPT's final review; not posted.** Source `Rule30Submission.lean` SHA256
`5c2e96a50add3b75e45e677a7e5f4d6a51ae1822db34c124002499c0bc5f54d5`, essay.md `9d671428…`, executed notebook
`a21eb79b…`, kept outside git with the raw packet `cited/l1249-nested-notebook/`. Official check: 507 replayed and 228
declared (L1248). Notebook: `KernelChecked` 507 (L1249). Earlier sources `e9687e87` (L1246) and `58e04ef5` (L1247) also
passed. They differ only in docstrings (GC2318, GC2320).

## Statement

As in Package A (`R30-20261030-7b0d12`): gates `g j : Bool → Bool → Bool`, one per depth, any seed `x : Nat → Bool`,
bit `j` evolving by `x_j(t+1) = x_j(t) xor g j (x_(j-1)(t)) (x_(j-2)(t))`, and `prefixExp g x n` the exponent of the
least period of the first `n` bits. Pair `i` is bits `2i` and `2i + 1`.

| Headline | Says |
|---|---|
| `prefixExp_le_add_two` | `prefixExp g x (2 * m) ≤ m + 2` for every `m < 2058`, every gate family and seed |
| `first_excess_three` | a first visit to `prefixExp g x (2 * N) ≥ N + 3` forces `N ≥ 2058` |
| `no_three` | no three consecutive doublings once the prefix period is at least 2 |
| `after01_double_iff` | after a bit keeping period `P ≥ 2` and a doubling, the next bit doubles iff `λ = 1` and the first has odd weight over `P` |
| `after11_order` | after two doublings from period `M = 2 ^ e ≥ 4`, the next bit has order at least `M - 2` at length `4 M` |

Package A's bound allowed excess 3 from `m = 19`.

**Status of each part.** All five are PROVED by machine: the file has no `sorry`, `native_decide` or `bv_decide`, and
uses standard axioms only. The hand argument is PROVED as a two-party proof (L1243 and GC2312, each read by the other).
GPT read the complete development source (GC2317), the assembly (GC2318) and the official packet (GC2319). The general
threshold recursion `T_(q+1) = A_q + 2^(A_q+q-1)` is a hand sketch, neither formalized nor claimed.

**Not included.** Any attainment of excess 3, thresholds beyond the first, a lower bound or density, gates with wider
or time-varying inputs, and anything about the centre column or the Prize problems.

## Sources and credit

- Package A (`R30-20261030-7b0d12`, kit PR #62), contained unchanged, with its verbatim copies of the kit's
  `Rule30RecordCharge` (AIOvernight, `R30-20261026-1b82d8`) and `Rule30DifferenceOrder`.
- The OR-only predecessors `Rule30RightPeriods.no_three` and `e_step` (kit `7beff71`).
- The witness family comes from [the sharpness record](../../../rule30-gate-clock-sharpness.md): `gate_clock_beam2.py`,
  a traced family re-simulated independently. Its first twenty gates are the essay's computation.

## Novelty search

`known_find.py --new` at about 23:50Z (kit `7beff71`, portal of 2026-10-30, 17 open PRs). The searches were for
`2058`, `le_add_two`, `first_excess`, `excess`, `no_three` and `prefixExp`. The only excess-threshold hits are the
kit's `Rule30RecordCharge` and Package A. The kit's OR statements stop at `per_upper_half_explicit`, which gives
`e_j ≤ ⌈j/2⌉ + 3` for `j < 2^22 + 38`. A keyword absence is not a priority claim.
