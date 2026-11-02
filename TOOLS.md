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
| **Local** | Claude Fable 5.1 (Claude Code desktop; Opus 5.5 until 1 November 2026 23:05 GMT, L1284) | M5 MacBook Pro: 10 cores, 16 GiB unified memory shared by CPU and GPU | Holds the Wolfram side (§6); current-kit Lean and portal builds; SAT with verified certificates; Metal on the M5 | Runs only while the owner has a session open; memory is shared with the owner's other apps |
| **GPT** | GPT (Codex) | Intel MacBook Pro: i9, 8 cores / 16 threads, 16 GiB RAM; RX 6600 eGPU with its own 8 GiB VRAM (measured, GPT-OVERNIGHT-20261029) | Hand mathematics and carrying reads; CPU and RX 6600 compute; long scheduled blocks when the owner turns them on | No Wolfram (owner, 2026-11-01); Lean 4.35 verified (GC2343); the GPU also drives a display, so keep headroom |
| **Cloud** | Claude Fable 5.1 | Cloud sandbox, always on | Long reads and reviews, record rewriting and rotation, closing summaries, portal reading; a different reasoning style from Local's | HTTPS only (the shared store works; no SSH or home network); cannot reach the kit's pull-request index (CL670); no heavy compute |

## 3. Inventory: who has which tool (snapshot 2026-11-01)

Local's column was checked on the machine on 2026-11-01 (L1275), and again after the owner's installs the same day,
with a smoke test of each new tool (L1276), and once more after the fixes (L1277). GPT verified the Intel column after installation in GC2343; Cloud confirmed the sandbox column in CL675 (4 cores, 15 GB, Ubuntu 24.04, ephemeral).

| Tool | Local (M5) | GPT (Intel) | Cloud (sandbox) |
|---|---|---|---|
| Python 3 | `python3` is python.org **3.15.2** (certificate bundle installed): numpy 2.5.4, scipy 1.18.1, sympy 1.14.0, networkx 3.7, gmpy2 2.3.2, mpmath 1.3.0, python-sat 1.9.dev17 (built from source), z3-solver 5.3.3.0, cvc5 1.4.2, certifi. All 1,597 probe files compile under 3.15; six give harmless invalid-escape warnings. The old system 3.9.6 (`/usr/bin/python3`) is no longer the default | **3.14.7**; numpy 2.5.4, scipy 1.18.1, sympy 1.14.0, networkx 3.7, gmpy2 2.3.2, mpmath 1.3.0, python-sat 1.9.dev17, z3-solver 5.3.3.0, cvc5 1.4.2, certifi 2026.10.23. Intel wheels; default HTTPS verified; [pins](tests/requirements-math-intel-py314.txt) | `python3` **3.13.16**: numpy 2.5.3, scipy 1.18.1, python-sat 1.9.dev17 (CaDiCaL 1.9.5 and 1.5.3, Glucose 4, MiniSat 2.2, Lingeling, MapleChrono all pass an UNSAT control), certifi. sympy was absent and installed this session with pip through the proxy (1.14.0); networkx, gmpy2, mpmath, z3-solver, cvc5 absent. **The container is ephemeral**: an install lasts one session unless the environment's setup is changed |
| C | Apple clang; GMP (Homebrew) | Apple clang 17.0.0; GMP 6.3.0 installed (Homebrew); checker C builds pass | gcc 13.3.0 and clang 18.1.3; **no GMP headers** |
| GPU compute | Metal on the M5 GPU (`.metal` kernels in `tests/probes`) | Vulkan 1.4.357/MoltenVK; RX 6600 enumerated explicitly alongside the other GPUs; no new GPU dispatch | none |
| SAT solvers | Kissat, CaDiCaL (command line); python-sat's CaDiCaL 1.9.5, Glucose 4 and MiniSat 2.2 in Python. The CaDiCaL LRAT to `cake_lpr` pipeline passes its controls (a true proof verified, a corrupted one rejected) | Kissat 4.0.4, CaDiCaL 3.0.1; Gimsatul4664fd74 in the private versioned tool cache (1/2/4-thread controls passed GC2376, timing study GC2377); Python CaDiCaL195/Glucose4/MiniSat22 pass PHP(5 pigeons,4 holes) UNSAT and a SAT control | python-sat's solvers (above) in Python; no Kissat or CaDiCaL command line |
| Proof-certificate checkers | `cake_lpr` (verified LRAT checker), `drat-trim` | cake_lpr source033aad53 (upstream checksums pass), drat-trim/lrat-check source2e3b2dc0; compiled for Intel. CaDiCaL LRAT accepted; corrupted hint rejected; DRAT accepted and empty proof rejected | none |
| Lean 4 | `elan` with 4.33.1 and **4.35.0** (the kit's version) | elan **4.35.0** installed and default, plus retained4.33.1; small kernel compile passes. No new full-kit build claimed | **none** (no elan, lean or lake); Lean sources are prepared here and built on Local |
| Wolfram | Wolfram Engine 15.0, `wolframscript`, LeanLink, the Wolfram MCP | **none, by the owner's decision** | none |
| SMT (z3, cvc5) | z3 5.3.3: command line (Homebrew) and Python (z3-solver); cvc5 1.4.2 in Python only, with no command line. All three solved a 16-bit bit-vector test (the inverse of 3 mod 2^16) | z3 **5.3.3** command line and Python; cvc5 **1.4.2** Python; both give inverse3 modulo2^16 =43691 | none |
| PARI/GP | **2.19.0** (PariGP.app), on `PATH` as `gp` through a link in `/opt/homebrew/bin` to the app's `gp-2.19`; remake the link when the app's version changes. It passed a valuation, continued-fraction and modular-inverse test | **2.19.0**, official Intel app, gp on PATH; valuation and modular-inverse controls pass | none |
| Sage | not installed | not installed (not requested) | none |
| `gh` (GitHub CLI) | signed in | 2.102.0; existing authentication verified; command on PATH | none |
| `record_find.py`, `known_find.py --new` | yes | yes (GC2340 complete refresh) | portal only; the kit's PR index is unreachable |
| `run_capped.py` | yes | yes; swap monitoring requires unsandboxed execution in Codex, not a substitute monitor | not applicable |

## 4. Task to tool

| Task | Best tool | Who runs it | Status of the output |
|---|---|---|---|
| Is it already known? | `record_find.py`, then `known_find.py --new`; `gh` for kit PR conversations; then the literature (AGENTS.md §2) | Local or GPT; Cloud for the portal only | — |
| Small exact simulation (a cellular automaton, the 3/2 map, a Collatz trajectory) | Python with numpy, or C; Wolfram for exploration and pictures | anyone; Wolfram by Local | COMPUTED |
| Large census or bit-parallel search | C with bit-sliced lanes; Metal compute for bitwise kernels, after a CPU oracle agrees ([GPU-METAL-JOBS](reports/wolfram-agents/GPU-METAL-JOBS.md)) | Local (M5), GPT (CPU, RX 6600) | COMPUTED or MEASURED |
| A finite "does such a configuration exist?" question | SAT: Kissat or CaDiCaL; for UNSAT, an LRAT proof checked by `cake_lpr`, with `drat-trim` as a second checker | Local or GPT (Intel confirmed GC2343) | SAT: the witness checks itself. UNSAT: a machine proof of that finite case once the certificate checks |
| Guessing a law from exact data (a closed form, recurrence or generating function) | Wolfram `FindSequenceFunction`, `FindLinearRecurrence`, `FindGeneratingFunction`, `FindFormula` | Local | CONJECTURE until proved |
| Exact symbolic work: recurrences and sums, real inequalities, exact intervals, polynomials over GF(2), Boolean normal forms | Wolfram (`RSolve`, `Reduce`, `Resolve`, `CylindricalDecomposition`, `Interval`, `GroebnerBasis[..., Modulus -> 2]`, `BooleanConvert`) | Local | COMPUTED: no certificate; it becomes PROVED through a hand proof or Lean |
| Exact number theory: big integers, 2-adic valuations, residues, continued fractions, lattice reduction | Wolfram to explore; PARI/GP as the fast open cross-check; the replayable probe in Python (sympy, gmpy2) or C with GMP | Local explores; anyone replays | COMPUTED |
| Finite questions about arithmetic with carries (Collatz, Mahler, the 3/2 map) as constraints | SMT over bit-vectors: z3 (command line or Python) or cvc5 (Python); a claim that needs a certificate is re-encoded as SAT with LRAT | Local or GPT (Intel confirmed GC2343) | COMPUTED; certified via SAT and LRAT |
| A formal proof for the kit or the portal | Lean 4.35, core, against a kit checkout at a recorded commit; standard axioms only | Local or GPT (4.35 installed GC2343) | machine proof of the stated theorem |
| A portal notebook build and check | LeanLink in `WolframKernel -script` under `run_capped.py --track-tree` | Local only | — |
| Hand proofs written in TeX | TeX, checked with `mathcheck/check.py FILE` | anyone | PROOF-SKETCH until the second read (AGENTS.md §4) |
| Pictures for the owner | Wolfram (`ArrayPlot`, `Graphics`) or an Artifact page | Local; others describe the picture they want | — |
| Data that does not belong in git | the shared store, cited by digest | anyone | — |
| The record and coordination | `CHAT-LEDGER.md`, shared-store flags, `ledger_check.py`, `doc_links.py` | anyone | — |
| Long reads, reviews, rotation of large documents, closing summaries | any worker; Cloud is always on and suited to it | Cloud first | — |

## 5. Gaps: proposed installs, waiting for the owner

**Local's set is complete** (L1276, L1277). The owner installed Python 3.15.2 with the modules in §3, the
certificate bundle, z3 and its Python package, cvc5 and PARI/GP, and removed a wrong pip package named `z3` (an
unrelated ZFS-to-S3 backup tool) and its boto. Every tool passed a known-answer test, and §3 records the versions.
What is left:

1. **Intel complete and verified (GC2343).** Lean4.35, matching Python library versions on Python3.14,
   z3/cvc5, certificate checkers and PARI/GP are installed. Wolfram remains Local-only. Sage was not requested.
   Homebrew has no Intel PARI bottle; the official Intel2.19.0 DMG was used with the publisher's SHA256 checked.
2. **Cloud confirmed its column** (CL675, answered in L1278). Every column of §3 is now confirmed by its own worker.

### Intel installation and verification (GC2343)

Replay: `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 tests/probes/toolchain_smoke.py`.
This tests package arithmetic, three SAT backends with SAT/UNSAT controls, both Python SMT solvers,
CaDiCaL-to-cake_lpr LRAT, a corrupted-hint rejection, DRAT and empty-proof rejection, Lean4.35 and gp.
It is a small known-answer installation check, not a research result or a full kit rebuild.
Python requirements also pass `pip check`. Python's installer certificate script was run and a default
urllib HTTPS request succeeded with certificate verification enabled. The existing3.14 interpreter
was retained; no move to3.15 was needed because the requested versions have Intel3.14 wheels.

Upstream checker sources: [cake_lpr033aad53](https://github.com/tanyongkiam/cake_lpr/tree/033aad53d1733bd4b8ca41cf6f1b5fb5d84f8de2)
(all four release checksums match) and [drat-trim2e3b2dc0](https://github.com/marijnheule/drat-trim/tree/2e3b2dc0ecf938addbd779d42877b6ed69d9a985).
PARI Intel DMG SHA256: `18614a90cd5ce59dd8ebc2578b11eacb43dc4e363e3bc21fab0b3cfe16c87814`,
matching the [official download page](https://pari.math.u-bordeaux.fr/download.html).
Command links expose installed user tools on the app's existing PATH; future login shells also get the
user tool directories. Full research runs still need the current resource freeze and capped runner.

### Intel parallel SAT addition (GC2376–GC2377)

Pinned [Gimsatul4664fd74](https://github.com/arminbiere/gimsatul/tree/4664fd74c97f87e30e7f907181707679b6fa49f2)
compiled from upstream C with Apple clang, sanitized build metadata and pthreads.
Binary SHA-256 `7d254115f5d895eeb6ac8312492b0ef93e0981a3c42dbfb903b629aa0b9e69b0`;
source, license and executable retained in the private versioned tool cache.
No global PATH change. Set `GIMSATUL_BINARY` to that executable for
[the bounded benchmark driver](tests/probes/intel_parallel_bench.py).
Known SAT models, unit UNSAT/DRAT checks and certified D40 answers pass at1/2/4 threads.
[Exact freezes, measurements and scope](reports/GPT-T33-INTEL-20261102.md#gc2377-controls-passed-repeated-parallel-benchmark-frozen).
The driver records wait4 CPU for all threads, wall time and RSS, and enforces
aggregate work alongside run_capped's memory/pressure/disk monitoring. It does not
make the existing single-thread solvers parallel, or certify arbitrary UNSAT answers
without a checked proof. More threads are an option to measure per workload.

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
