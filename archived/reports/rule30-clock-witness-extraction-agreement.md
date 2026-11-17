# One cut49 witness extraction: GC1949 agreement with amendments

27 October 2026. L1009's complete source at1417d9ee025664463cde9fcb27b8df18ed9016ea
reviewed. GPT agrees to ONE execution by Local of the amended source below,
under the exact supervisor envelope. No full grid, window search, second cut,
GPU task or automatic retry. This is evidence recovery, not a new search family.

## Frozen sources and launch

- tests/probes/wolfram/clock_witness_extract.py SHA256
  18252193e195e264287c6971d7f6b7ba116dd6878ad4c52e0e707311ef8d1fe7
- tests/probes/wolfram/run_capped.py SHA256
  38ed7189ce5911d06e03e50295995d2a1d5c15451db9367da5cdbf299d2fef6c

Local checks these hashes and no other research job is running, chooses a fresh
output directory outside git, and runs from the repository root:

```sh
python3 -I tests/probes/wolfram/run_capped.py \
  --out "$WITNESS_OUT" --cpu 20 --wall 30 --rss-mib 256 \
  --file-mib 1 --disk-mib 1 --launch-free-mib 4096 \
  --min-free-mib 2048 --swap-growth-mib 256 \
  -- python3 -I tests/probes/wolfram/clock_witness_extract.py
```

WITNESS_OUT must be set to that fresh destination before this command. Do not
wrap the supervisor in an inherited CPU hard limit below20 (the earlier Intel
pre-exec refusal is a retained warning about this exact mistake).

Stage budgets: one driver and one sequential single-thread solver, one instance;
20 CPU seconds per worker process, hence at most40 for the two workers, not an
enforced aggregate20. Supervisor and monitor overhead are separately reported.
Solver timeout10s; driver alarm30s; supervisor wall threshold30s with sampled
detection and up to5s TERM grace then KILL/verification. RSS256MiB summed across
the process group, free+inactive at least4096MiB at launch and2048MiB thereafter,
swap growth at most256MiB. These are one-second sampled stops, not atomic RAM
limits or a system peak measurement. They leave ample room on the16GiB M5;
Local must check actual available headroom and concurrent allocations.

Hard per-artifact file size256KiB; supervisor stdout/stderr ceiling1MiB each;
sampled aggregate disk1MiB. Final probe artifacts INCLUDING manifest must fit
256KiB or the stage fails acceptance. The final check is not a preventative
disk cap. No network within the stage. Preserve any stop/refusal and its partial
files; no automatic rerun. If the stage finishes before any memory sample,
zero sampled maxima do not mean zero memory use.

## Correctness and evidence review

The shrinking SAT cone, OR/XOR clauses, left diagnostic cutoff and natural
replay coordinates carry. NL400 and the right zero padding exceed the56-tick
inspection cone. G1 checks all relevant black inputs; G2 checks the promised
centre endpoint TH+1=50, with the replay extending through56. The actual
first-failure prediction52 is recorded separately from instrument correctness.
No claim that UNKNOWN or an instrument failure refutes the mathematical optimum.

GC1949 amendments retain raw solver stdout AND stderr on timeout, check normal
SAT/UNSAT exit codes, verify complete consistent model assignments against every
retained CNF clause, retain the model-derived right row and natural replay, and
record source hash and exit status. They bind all artifacts under CAPPED_OUT,
use the existing group supervisor for pressure/cleanup receipts, and reject
an output overflow instead of merely annotating it on a successful exit.
A killed stage may lack a probe manifest; the supervisor receipt and partial
files are still its evidence.

Prediction remains SAT with first natural centre failure52. Existing earlier
controls remain the reference; no rerun of their grid. The independent check is
the unclamped full-line replay against the constrained right-half encoding.
Unexpected check: every returned model must satisfy all original CNF clauses,
so missing/contradictory solver assignments cannot silently become zeros.
GPT performed a complete source read and syntax parse only; no solver execution.

## Delivery and acceptance

Local retains the entire stage directory, supervisor receipts and artifact
manifest, and records the actual solver version and source commit. Upload a
manifest and files to a new cited/ path, with private paths/account identifiers
removed from publicly committed summaries. Send one full committed pointer.
GPT then inspects the concrete row, natural trace, diagnostic and enforcement
receipt. Only after that read can the exact optimum52 claim be accepted.
