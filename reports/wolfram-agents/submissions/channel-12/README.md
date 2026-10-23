# Submission 10 (draft under review): the channel bound, certified at width 12 (Cloud, 2026-10-23)

MAP.md candidate 2, the channel bound, as a formal theorem: for every configuration whose center column reads the
clock `0101…` from time 0, the visible bits (column 1 at even times) of length `n` lie in a set of at most
`218 · 1.195924139^n` words (`channel_bound_12`; `0.2581` bits per visible bit), by a verified checker that
rebuilds the width-12 layer automaton in the kernel. GPT's specification (`../../GPT-CL594-CHANNEL-BRIDGE.md`) is
the contract; this is Cloud's implementation. **Ready for Local's build (CL597); GPT's second read requested in CL596.**

- `Rule30Submission.lean`: the module (built and checked in the kit at `cc1e0e0`). Sections: 1 the kernel
  computation (`nxt`, `step2`, `img4`, `pos64`, `wordLoop`, `sweep`, `imageSets`, `edge`, `run`, `check`,
  `wcheck`); 2 what it establishes (`pos64_spec`, `wordLoop_spec`, `sweep_spec`, `imageSets_spec`, `edge_sound`,
  `run_sound`, `check_sound`); 3 the physical window (`win`, `win_testBit`, `win_succ`, `win_step2`, `Clock`);
  4 the walk and the count (`st_inv`, `AccF`, `cntA`, `visFrom`, `visFrom_mem`, `wcheck_sound`, `weight_bound`);
  5 the certificate (`Cert`, `Cert.Valid`, `Cert.bound`, `Cert.ncard_bound`); 6 width 12 (`succ12`, `weights12`,
  `check12`, `wcheck12`, `cert12_valid`, `channel_bound_12`, `channel_ncard_12`).
- `check.json`: the kit's `Check.lean` output on the final module: verdict `pass`, 234 constants, nine headlines
  (`channel_bound_12`, `channel_bound_12_eventually`, `channel_ncard_12`, `Cert.bound`, `check_sound`,
  `weight_bound`, `win_step2`, `visFrom_mem`, `cert12_valid`) on `propext`, `Classical.choice`, `Quot.sound` only
  (`cert12_valid` on `propext`). Build 114 s, replay 107 s in Cloud's container; no double quote or backslash.
- `essay-template.md` + `assemble.py` -> `essay.md` (77,092 characters), fast cell order: three display cells with the
  one `Open` set, `Axioms`, `CallGraph`, `KernelCheck` last. `abstract.md`: the API abstract (Markdown with TeX,
  ASCII outside the math, four parts), to go through the `utf8` wrapper with every text parameter.
- `expected_numbers.py`: every number the essay's Wolfram Language cells print, computed in Python first (below).
- `build_dfa.py`: the automaton by the C program's BFS (same order, same numbering); at width 16 it reproduces
  GPT's graph exactly. `cert.py`: the integer Collatz-Wielandt certificates (widths 12 and 14 computed here; 16 is
  GPT's, verified exactly).

## What the kernel does

The source carries only the graph (402 successor pairs, `DEAD` for a dead edge) and the weights. `check` walks the
states in BFS order: state 0 is the full bitset `2^4096 − 1`; for each state it sweeps its bitset in 64-bit words
(`Nat.shiftRight`, `Nat.land`), extracts members by their top bit (`pos64`, six comparisons: `Nat.log2` is not
kernel-accelerated and unfolds in thousands of steps on a big number), computes the four two-step images of each
member and ORs `2^image` into the half of a packed accumulator selected by the member's low bit. The two halves are
the image sets of the two labels. A new target state is defined as that image; an old one must contain it (`Nat.land`
equality); a dead edge must have an empty image; at the end every discovered state must have been processed. Every
loop variable is forced to a literal before the recursive call (`force`, a `Nat.casesOn`), because the kernel is lazy
and would otherwise stack unevaluated expressions. `wcheck` is the weight inequality per state.

## Expected outputs of the essay's cells (`expected_numbers.py`)

- Widths 6 and 8 automaton cell: `{{6, 31, 18, 1.358}, {8, 56, 29, 1.28006}}` (growth by 300 power iterations;
  Python gives 1.358001 and 1.280057).
- Certificate cell: `{402, 251, True}`.
- Growth cell: `{1.19568, 0.25813, {2, 3, 5, 8, 12, 17, 25, 36, 50, 68, 91, 119}, 1866.}` (Python: growth 1.1956850,
  `log2(R/D) = 0.25813`, the bound `218 (R/D)^12 = 1866.0`).

## Numbers (computed by `cert.py` and `build_dfa.py`)

Width 12: 402 states, 48,190 row occurrences (root 4,096), 251 dead edges; growth rate 1.1956850, certified ratio
`R/D = 1195924139/10^9`, `log2 = 0.2581` bits per visible bit; `wmin = 803714697`, `w0 = 174869380839`, `C = 218`.
Width 14: 919 states, 193,314 rows, ratio 1.184655442 (0.2445 bits), C = 300. Width 16 (GPT's certificate):
2,260 states, 820,089 rows, ratio 1.159107281 (0.2131 bits), C = 10310. Kernel time here is about 0.8 ms per row
occurrence: width 12 about 40 s, width 16 about 11 minutes.
