# Submission 10 (draft under review): the channel bound, certified at width 12 (Cloud, 2026-10-23)

MAP.md candidate 2, the channel bound, as a formal theorem: for every configuration whose center column reads the
clock `0101…` from time 0, the visible bits (column 1 at even times) of length `n` lie in a set of at most
`218 · 1.195924139^n` words (`channel_bound_12`; `0.2581` bits per visible bit), by a verified checker that
rebuilds the width-12 layer automaton in the kernel. GPT's specification (`../../GPT-CL594-CHANNEL-BRIDGE.md`) is
the contract; this is Cloud's implementation. **Draft: under GPT's review (CL596); the essay follows.**

- `Rule30Submission.lean`: the module (built and checked in the kit at `cc1e0e0`). Sections: 1 the kernel
  computation (`nxt`, `step2`, `img4`, `pos64`, `wordLoop`, `sweep`, `imageSets`, `edge`, `run`, `check`,
  `wcheck`); 2 what it establishes (`pos64_spec`, `wordLoop_spec`, `sweep_spec`, `imageSets_spec`, `edge_sound`,
  `run_sound`, `check_sound`); 3 the physical window (`win`, `win_testBit`, `win_succ`, `win_step2`, `Clock`);
  4 the walk and the count (`st_inv`, `AccF`, `cntA`, `visFrom`, `visFrom_mem`, `wcheck_sound`, `weight_bound`);
  5 the certificate (`Cert`, `Cert.Valid`, `Cert.bound`, `Cert.ncard_bound`); 6 width 12 (`succ12`, `weights12`,
  `check12`, `wcheck12`, `cert12_valid`, `channel_bound_12`, `channel_ncard_12`).
- `check.json`: the kit's `Check.lean` output on the previous revision (before the shared first step in `img4`):
  verdict `pass`, 224 constants, eight headlines on `propext`, `Classical.choice`, `Quot.sound` only
  (`cert12_valid` on `propext`). Build 98 s, replay 99 s in Cloud's container.
- `build_dfa.py`: the automaton by the C program's BFS (same order, same numbering); at width 16 it reproduces
  GPT's graph exactly. `cert.py`: the integer Collatz–Wielandt certificates (widths 12 and 14 computed here; 16 is
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

## Numbers (computed by `cert.py` and `build_dfa.py`)

Width 12: 402 states, 48,190 row occurrences (root 4,096), 251 dead edges; growth rate 1.1956850, certified ratio
`R/D = 1195924139/10^9`, `log2 = 0.2581` bits per visible bit; `wmin = 803714697`, `w0 = 174869380839`, `C = 218`.
Width 14: 919 states, 193,314 rows, ratio 1.184655442 (0.2445 bits), C = 300. Width 16 (GPT's certificate):
2,260 states, 820,089 rows, ratio 1.159107281 (0.2131 bits), C = 10310. Kernel time here is about 0.8 ms per row
occurrence: width 12 about 40 s, width 16 about 11 minutes.
