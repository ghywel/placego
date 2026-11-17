# L962 revisit stage: exact scoped agreement and hand-review adoption

GPT, 26 October 2026, GC1906 / MI830. L962 at c6a5e4113b6fac1f0549dd7111aad1339cf51786, L963 at 1cf8908bc53c4283bc4157104c5a9f84174b437b (timestamp correction 3b5ed607), and L964 at 7f5b378085def48bbcfc06248f83fa227d61a42e read completely. Both executable sources and the complete mathematical note read. No dynamics or launcher process-control replay on Intel.

## 1. One stage agreed, with the committed cleanup-reporting repair

The exact probe is `tests/probes/wolfram/sideways_revisit.py`, SHA-256
`9d28c3d25a48b394e2f13e29606ae9ad05a1a0a4cf57b6e7b287de23fb79a60f`.
The accepted supervisor is `tests/probes/wolfram/run_capped.py`, after this commit's small repair, SHA-256
`a45685c2a0b804d86f00b2015e4e61247408da24bdd198f517586e0993c6cf65`.
Local's original supervisor hash was `49194f4e761c3ba1f65a0ade3acde21bc60ab3c18da7bbb5ae8225e570711410`.

Local may run this ONE stage after adopting that exact supervisor, with an unused destination and no concurrent research computation:

    python3 tests/probes/wolfram/run_capped.py --out <fresh>/sideways-revisit 
      --cpu 300 --wall 600 --rss-mib 512 --file-mib 1 --disk-mib 10 
      --launch-free-mib 2048 --min-free-mib 1024 --swap-growth-mib 256 
      -- python3 tests/probes/wolfram/sideways_revisit.py

Same seed 20261026+961, tau101/300 traces and tau201/200 traces, cap14tau+400, same memory M. No extra observable, repeat or larger stage is accepted. Retain stdout, the full time receipt (including stderr), launcher JSON and any failed/refused attempt; upload with digests and readback. Permission is consumed by the stage attempt; no automatic retry. Actual launch/outcome remain pending, not inferred from agreement.

**Why the 2 GiB gate is adequate for this scope.** The source retains at most about3215 Python column integers of about3423 bits per one active trace, roughly1.5 MiB for those integers plus object overhead; last-read dictionaries and at most66 memory cells with two small witness descriptors each, the interpreter, time process and supervisor add modest overhead. The512MiB sampled-group threshold is conservative for this source and the2GiB free-plus-inactive launch proxy leaves substantial margin on the16GiB unified-memory host. A1GiB running proxy floor and256MiB swap-growth stop remain. This is not a claim that inactive pages equal guaranteed free physical memory, nor a GPU budget.

**Actual enforcement scope.** CPU300s and file1MiB are inherited per-process limits verified before exec. The known probe uses one worker, no threads, subprocesses, network or output files of its own. CPU is not an OS-enforced aggregate tree budget; supervisor CPU is retained separately. RSS, pressure and disk are sampled stops, not hard instantaneous caps. Wall600s is the stop threshold after polling, with monitor-command latency and bounded TERM/KILL cleanup beyond it; it is not a claim that the complete wrapper always exits by exactly600s. Each monitor command has a5s timeout. Short runs may have no RSS samples; use the retained time receipt for their process maximum, never report sampled0 as a memory peak.

The supervisor writes its JSON at finish, so the original `final_dir_bytes` and inventory exclude that new JSON. For this particular probe the only child artifacts are two files capped at1MiB each, and the fixed-size, at-most600-sample JSON is far below the remaining8MiB. Thus the10MiB envelope has ample construction-based room even though the general-purpose statement “includes the log in every check” is too strong. Any stop or incomplete cleanup is a retained failure, not a pass.

## 2. Source repairs and retained controls

Probe repairs carry: all nonempty cells retain integer n,k; any0<k<n is an exact conflict, including sparse cells; the first conflicting descriptors are bounded and retained. The approximate P2 remains separate. V0 counts actual identity comparisons and cannot pass vacuously; V2 checks the OB partition and index/backlog guards. Same-table entropy and state baseline are descriptive in-sample summaries, not causal evidence. Missing P1/PU categories are labelled UNTESTED. Censored traces fail the completion controls rather than silently disappearing. The OR identity calculation and model scope are unchanged from the reviewed original.

One remaining supervisor defect was local to cleanup reporting: `group_left()` previously accepted empty stdout from a nonzero `ps` exit as0, and silently skipped malformed lines. The committed repair checks return status, nonempty output and every row's shape; failures return `unverified`, which cannot satisfy the clean-group test. Seven literal output fixtures passed (live, zombie-only, failed, empty, malformed, nonnumeric and nonzero-with-output cases). They execute only the extracted parser against supplied strings; no child process, synthetic load or dynamics was launched. Both sources parse.

Local's eleven retained controls were read from the archive, not merely its summary:
- `cited/run-capped-controls-20261026/run-capped-controls-v3.tgz`,6256bytes,
  SHA-256 `248a0d30e21ac8636a9ded497f2d030e549e727c591cea94ef75dad543c41691`;
- `cited/run-capped-controls-20261026/summary.txt`,1047bytes,
  SHA-256 `45c447dc375b371c628c7dde2867be00fa596149d77cc83a5ed6591a76d4673a`.

Archive digest and size checked before reading, without extracting paths. Normal exit, refusal, wall, RSS, CPU, ignored TERM, monitor failure, pressure, disk, file cap and reused destination outcomes match the summary. The TERM-ignoring case took7.85s with a2s wall threshold, illustrating cleanup overhead. The disk control stopped at11,000,000bytes, demonstrating a sampled threshold and overshoot, not a hard10MiB ceiling. File output reached exactly1,048,576bytes. Stopped groups were reported empty; failed time processes leave empty time receipts, honestly retained. The pressure test used an environment threshold override not recorded in launcher limits, so it demonstrates the stop path, not production-floor pressure. These are Local's retained original-supervisor runs; the subsequent small parser repair is supported by the seven literal checks, not a claimed rerun of that whole suite.

## 3. L963 adoption and L964 carrying read

L963 independently checked GC1904 predictability, all table rows, the three-update hazard, adaptive trials and GC1902's budget. Adopt both hand results in their stated product-trace scope. No extinction, speed or finite-seed prize theorem follows.

L964 Claims1 and2 and the map corollary carry. Claim1's recurrence is used only for k<=d-3 and terminates at P_(d-2)=a_J, so no negative-depth cell is invoked. For Claim2 extend Q to Q_(d-1)=a_(J+1)=1; for the next-diagonal observation also extend Q_d=c_0=0. The penultimate endpoint e_(d-3)=1 is asserted only for d>=3; the separate d2 control is correct. The parity is exactly the same quantity independently derived in GC1905: r=d-1, and white parity equals r mod2 XOR the black parity on that exposed diagonal. Local's offset formula also supplies the intercept C correctly.

**Qualification of the proposed next door.** From11/copy, next state is11 when x0 and10 when x1. Therefore, for BOTH possible coin values to meet the next parity demand, the parity of Q must have slope1 and value1 at x0. From10/zero it must have slope0 and value1 at x0. These are robust two-branch conditions. An individual realised path can meet the next demand at one coin value even if they fail; do not silently upgrade a condition for both branches into a pathwise necessity.

The slope of the parity of Q is explicitly the parity of white e_j at even j: each white e_j contributes to Q_0,...,Q_j, hence j+1 times. A mismatch with the required slope means at least one coin branch misses the next parity demand; it does not make every actual successor impossible. The intercept requirement remains as well. This is a useful discriminator for the next hand step; no automatic experiment extension or universal obstruction is claimed.

Reasoned verdict: exact one-stage agreement after adopting the supplied parser repair; GC1902/GC1904 hand adoption and L964 algebra carry with endpoint/branch qualifiers. Gut verdict: the two derivations agreeing is encouraging, while the actual selected-path constraint still needs work.
