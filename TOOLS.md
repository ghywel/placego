# TOOLS: the best tool for each job, and who can run it

*Started 2026-11-01 by Local at the owner's request: "we need to define for all workers which tools we should be using
for which tasks, and add that to our regularly checked workflow documents." AGENTS.md §10 points here, and every
worker reads this page at session start (AGENTS.md §2). Each worker owns and confirms the rows for its own host; a cell
marked **to confirm** is not yet checked by the worker who has that host.*

## 1. The rule

The owner (2026-11-01): "the AI assistants ... have a habit of 'going around the problem' when a requested tool is
unavailable and finding some other solution, but i would always rather we use the best tool for the job."

1. **Use the tool §4 names for the task.**
2. **If it is not on your host, do not go around it.** Either hand the task to a worker who has the tool (§3), or ask
   the owner to install it (§5). Say which in the ledger entry.
3. **A substitute needs the owner's agreement.** The entry then names it as a substitute and says why.
4. **An output has the status of the check behind it** (AGENTS.md §3). A solver's answer without a certificate is
   COMPUTED; a checked certificate or a Lean kernel check is a machine proof of exactly what it states.
5. **Substantial computation runs under `tests/probes/wolfram/run_capped.py`, on any host**, with the caps stated
   beforehand (AGENTS.md §6).
6. **Keep this page true.** When a tool is installed, removed or found missing, update §3 in the same commit.

## 2. The workers

| Worker | Model | Host | Suited to | Limits |
|---|---|---|---|---|
| **Local** | Claude Opus 5.5 (Claude Code desktop) | M5 MacBook Pro: 10 cores, 16 GiB unified memory shared by CPU and GPU | Holds the Wolfram side (§6); current-kit Lean and portal builds; SAT with verified certificates; Metal on the M5 | Runs only while the owner has a session open; memory is shared with the owner's other apps |
| **GPT** | GPT (Codex) | Intel MacBook Pro: i9, 8 cores / 16 threads, 16 GiB RAM; RX 6600 eGPU with its own 8 GiB VRAM (measured, GPT-OVERNIGHT-20261029) | Hand mathematics and carrying reads; CPU and RX 6600 compute; long scheduled blocks when the owner turns them on | No Wolfram (owner, 2026-11-01); Lean 4.33.1 only (§5); the GPU also drives a display, so keep headroom |
| **Cloud** | Claude Fable 5.1 | Cloud sandbox, always on | Long reads and reviews, record rewriting and rotation, closing summaries, portal reading; a different reasoning style from Local's | HTTPS only (the shared store works; no SSH or home network); cannot reach the kit's pull-request index (CL670); no heavy compute |

## 3. Inventory: who has which tool (snapshot 2026-11-01)

Local's column was checked on the machine on 2026-11-01 (L1275). GPT's and Cloud's columns hold only what the record
shows; their workers confirm or correct them.

| Tool | Local (M5) | GPT (Intel) | Cloud (sandbox) |
|---|---|---|---|
| Python 3 | system 3.9.6 with numpy 2.0.2 and scipy 1.13.1 only (no sympy, networkx, python-sat, gmpy2, z3); Homebrew 3.12 and 3.14 and `uv` present but unused by the probes | to confirm | to confirm |
| C | Apple clang; GMP (Homebrew) | to confirm (record: C probes run) | to confirm |
| GPU compute | Metal on the M5 GPU (`.metal` kernels in `tests/probes`) | RX 6600, selected explicitly (record); API to confirm | none |
| SAT solvers | Kissat, CaDiCaL | to confirm (record: one Intel certificate replay, GC2333) | to confirm |
| Proof-certificate checkers | `cake_lpr` (verified LRAT checker), `drat-trim` | to confirm | none |
| Lean 4 | `elan` with 4.33.1 and **4.35.0** (the kit's version) | **4.33.1 only** (record) | to confirm |
| Wolfram | Wolfram Engine 15.0, `wolframscript`, LeanLink, the Wolfram MCP | **none, by the owner's decision** | none |
| SMT (z3, cvc5) | not installed (§5) | to confirm | to confirm |
| PARI/GP, Sage | not installed | to confirm | to confirm |
| `gh` (GitHub CLI) | signed in | to confirm | none |
| `record_find.py`, `known_find.py --new` | yes | yes (GC2340 complete refresh) | portal only; the kit's PR index is unreachable |
| `run_capped.py` | yes | yes (record) | not applicable |

## 4. Task to tool

| Task | Best tool | Who runs it | Status of the output |
|---|---|---|---|
| Is it already known? | `record_find.py`, then `known_find.py --new`; `gh` for kit PR conversations; then the literature (AGENTS.md §2) | Local or GPT; Cloud for the portal only | — |
| Small exact simulation (a cellular automaton, the 3/2 map, a Collatz trajectory) | Python with numpy, or C; Wolfram for exploration and pictures | anyone; Wolfram by Local | COMPUTED |
| Large census or bit-parallel search | C with bit-sliced lanes; Metal compute for bitwise kernels, after a CPU oracle agrees ([GPU-METAL-JOBS](reports/wolfram-agents/GPU-METAL-JOBS.md)) | Local (M5), GPT (CPU, RX 6600) | COMPUTED or MEASURED |
| A finite "does such a configuration exist?" question | SAT: Kissat or CaDiCaL; for UNSAT, an LRAT proof checked by `cake_lpr`, with `drat-trim` as a second checker | Local; GPT once §3 is confirmed | SAT: the witness checks itself. UNSAT: a machine proof of that finite case once the certificate checks |
| Guessing a law from exact data (a closed form, recurrence or generating function) | Wolfram `FindSequenceFunction`, `FindLinearRecurrence`, `FindGeneratingFunction`, `FindFormula` | Local | CONJECTURE until proved |
| Exact symbolic work: recurrences and sums, real inequalities, exact intervals, polynomials over GF(2), Boolean normal forms | Wolfram (`RSolve`, `Reduce`, `Resolve`, `CylindricalDecomposition`, `Interval`, `GroebnerBasis[..., Modulus -> 2]`, `BooleanConvert`) | Local | COMPUTED: no certificate; it becomes PROVED through a hand proof or Lean |
| Exact number theory: big integers, 2-adic valuations, residues, continued fractions, lattice reduction | Wolfram to explore; the replayable probe in Python (sympy or gmpy2, §5) or C with GMP | Local explores; anyone replays | COMPUTED |
| Finite questions about arithmetic with carries (Collatz, Mahler, the 3/2 map) as constraints | SMT over bit-vectors (z3 or cvc5) once installed (§5); a claim that needs a certificate is re-encoded as SAT with LRAT | Local, GPT | COMPUTED; certified via SAT and LRAT |
| A formal proof for the kit or the portal | Lean 4.35, core, against a kit checkout at a recorded commit; standard axioms only | Local; GPT for development only until 4.35 is installed | machine proof of the stated theorem |
| A portal notebook build and check | LeanLink in `WolframKernel -script` under `run_capped.py --track-tree` | Local only | — |
| Hand proofs written in TeX | TeX, checked with `mathcheck/check.py FILE` | anyone | PROOF-SKETCH until the second read (AGENTS.md §4) |
| Pictures for the owner | Wolfram (`ArrayPlot`, `Graphics`) or an Artifact page | Local; others describe the picture they want | — |
| Data that does not belong in git | the shared store, cited by digest | anyone | — |
| The record and coordination | `CHAT-LEDGER.md`, shared-store flags, `ledger_check.py`, `doc_links.py` | anyone | — |
| Long reads, reviews, rotation of large documents, closing summaries | any worker; Cloud is always on and suited to it | Cloud first | — |

## 5. Gaps: proposed installs, waiting for the owner

Nothing in this list is installed yet. Each item says what it would replace.

1. **A pinned Python environment on Local and Intel**, with exact versions in a requirements file: sympy, networkx,
   python-sat, gmpy2 and z3-solver beside numpy and scipy. Today's system Python 3.9.6 has only numpy and scipy, which
   pushes probes towards hand-rolled substitutes.
2. **An SMT solver (z3, or cvc5) on Local and Intel**, for constraints with carries. Today these get hand-encoded as
   SAT, which is the "going around" this page exists to stop.
3. **Lean 4.35 on Intel**, so that GPT can validate against the kit's version. Until then, current-kit validation is
   Local's.
4. **GPT and Cloud confirm their columns in §3.**
5. Optional: **PARI/GP** as a fast open-source cross-check for Wolfram's number theory.

## 6. Wolfram (the owner, 2026-11-01)

- **Wolfram stays off the Intel. Local holds the Wolfram side.** GPT and Cloud design or suggest Wolfram tasks for Local
  to run. Put the request in the ledger with the code or its intent, the prediction, and the output you want back.
- **The results matter, not the workings, and they must translate.** In the owner's words: "the precise working of
  wolfram doesn't matter, the results it can produce matter, which must always be translatable into a different
  language anyway." Every Wolfram result that carries a status is restated in plain mathematics. If it is a
  computation, the entry gives the Wolfram code and a replay in Python, C or Lean, so that a worker without Wolfram can
  check it.
- **Use it for:** guessing laws from data, exact symbolic algebra, exploration and pictures, and LeanLink builds.
  **Not for:** certified UNSAT (Wolfram's SAT functions give no certificate, as far as we know), large censuses (C and
  Metal are much faster), or anything another worker must replay without a translation.
- **Operations.** The MCP kernel is for small evaluations only. Heavy builds run as `WolframKernel -script` under
  `run_capped.py`. After a fault, ask the owner to restart Wolfram before debugging. Never print licence, machine or
  account identifiers (AGENTS.md §7).
- **First use, for the record.** On 2026-11-01, from the first 20 values of M(k) alone, `FindLinearRecurrence`,
  `FindGeneratingFunction` and `FindSequenceFunction` returned a recurrence, a generating function and a closed form
  that agree with the proved formula through k = 40, in about a second (L1275). That is the step done by eye on
  31 October, and it shows the guessing row of §4 working.
