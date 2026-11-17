# Submission 11 (submitted, R30-20261023-4d1a54): the channel bound at width 14, explicit states, one kernel theorem per state (Cloud, 2026-10-23)

MAP.md candidate 2, the second rung: GPT's design GPT-CL601-WIDTHS.md (GC1708) implemented. The bitset of each of the 919
states is explicit data (`T14`, a binary tree of literals, about 4.5 MB of decimal), and each state's closure is its own
theorem `s14_i` by `decide +kernel`, so the kernel's caches, which live for one declaration, stay bounded. The width-6
pilot (`Pilot6.lean`, 31 states) passes with its negative controls: a false dead edge, swapped labels and a dropped image
are each rejected. The full width-14 module passes `lake env lean` in 256 s on Cloud's machine (the single-declaration
version of the width-12 design was unfinished after 53 minutes at 10 GB). The kit build and `Check.lean` receipt, the
module and the assembled essay are being added (12:55 BST).

- `Rule30Submission.lean`: the module (3,929 lines, 4.8 MB, of which 4.5 MB is `T14`); built and checked in the kit at
  `cc1e0e0`; no double quote or backslash; SHA256 `7559970244b025c1733a9fc98f1f16a2583366ff8d70edb5cfda50bd71f42fd7`.
- `check.json`: the kit's `Check.lean` output: verdict `pass`, **3,961 constants** (the 919 state theorems and the
  range tree among them), eight headlines (`channel_bound_14`, `bound_of`, `explicit_sound`, `stateCheck_spec`,
  `weight_bound`, `win_step2`, `visFrom_mem`, `all14`) on `propext`, `Classical.choice`, `Quot.sound` only (`all14` on
  two). On Cloud's machine: `lake env lean` 256 s, `lake build` 330 s, replay 245 s, memory bounded (about 6 GB in the
  elaborator for the whole module). The verifier will take longer than four minutes; the maintainer path applies.
- `essay-template.md` + `assemble.py` -> `essay.md` (the notebook will be about 5 MB because of the data); `abstract.md`; `expected_numbers.py` (below); `cert.py`,
  `build_dfa.py` (the certificate and the automaton, as before); `Pilot6.lean` (the pilot with its negatives).

## Expected outputs of the essay's cells (`expected_numbers.py`)

- Widths 6 and 8 automaton cell: `{{6, 31, 18, 1.358}, {8, 56, 29, 1.28006}}`.
- Certificate cell: `{919, 614, True}`.
- Growth cell: `{1.18442, 0.24447, {2, 3, 5, 8, 12, 17, 25, 36, 50, 68, 91, 119, 156, 199, 251, 316, 393, 488, 601, 735}, 8891.2}`
  (Python: growth 1.1844186).

## Numbers

Width 14: 919 states, 193,314 row occurrences (root 16,384), 614 dead edges; growth rate 1.1844186, certified ratio
`R/D = 1184655442/10^9`, `log2 = 0.24447` bits per visible bit asymptotically; `wmin = 653189453`,
`w0 = 195955063994`, `C = 300`.

## Review and corrections (2026-10-23, GPT GC1709)

GPT's carrying read of section 7 and `channel_bound_14`: **PASS** (`../../GPT-CL603-REVIEW.md`; the three pilot negatives
confirmed by literal witnesses). Two essay corrections before submission, applied: the prefactor in "The idea of the
proof" is 300 (a stale 218 from the width-12 text); the provenance now says the notebook regenerates the width-6/8
automata and computes width-14 diagnostics from the supplied graph, not that it regenerates the width-14 graph. The
pilot's fourth control is renamed `pos_root` (a positive test, not a negative). The Lean module is unchanged.

## Submitted (2026-10-23 13:50 BST)

Submitted by Local at 13:46 BST on the owner's standing permission as **R30-20261023-4d1a54** (L778; on the M5: build
171 s, check 115 s, essay built in 260 s, 5.5 MB). Lean Unverified, queued: the automatic check will exceed four minutes
and the maintainer path applies, by the owner's word. The verdict will be recorded here when it comes.

