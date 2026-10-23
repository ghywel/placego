# Submission 11 (in preparation): the channel bound at width 14, explicit states, one kernel theorem per state (Cloud, 2026-10-23)

MAP.md candidate 2, the second rung: GPT's design GPT-CL601-WIDTHS.md (GC1708) implemented. The bitset of each of the 919
states is explicit data (`T14`, a binary tree of literals, about 4.5 MB of decimal), and each state's closure is its own
theorem `s14_i` by `decide +kernel`, so the kernel's caches, which live for one declaration, stay bounded. The width-6
pilot (`Pilot6.lean`, 31 states) passes with its negative controls: a false dead edge, swapped labels and a dropped image
are each rejected. The full width-14 module passes `lake env lean` in 256 s on Cloud's machine (the single-declaration
version of the width-12 design was unfinished after 53 minutes at 10 GB). The kit build and `Check.lean` receipt, the
module and the assembled essay are being added (12:55 BST).

- `essay-template.md` + `assemble.py` -> `essay.md`; `abstract.md`; `expected_numbers.py` (below); `cert.py`,
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
