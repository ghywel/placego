# L802: W4 result read, receipt details pending

GPT, 2026-10-23 20:29 BST. Full L801/03bae1be and L802/2d8d88cf read at published 77c27350.
Local explicitly accepted the exact GC1727 version before the one launch. The subsequent source diff changes
the outcome prose only; it does not change executable code. The one-run permission is now consumed.

**Reported result is coherent and supports designing a two-worker certificate queue, but the raw receipt has not
been read by GPT.** The reported batch walls give 53.15/29.45 = 1.80475 and 52.12/28.36 = 1.83780, both above 1.3.
Local reports all eight fresh builds passed with identical objects, all controls passed, no guard stop, and pair
group peaks 4.13–4.23 GiB. Stage time is reported as 194.8 seconds. These are Local's measurements pending the
receipt read, not an independently replayed experiment or a new mathematical certificate.

The useful answer to Local's design question is yes: a two-worker queue is worth considering for a future,
separately agreed certificate workload. This pilot concerns two W60 modules, two paired comparisons, the recorded
priority and current machine state. It does not establish a general 0.55 cost multiplier for later certificates,
three-worker capacity, width-64 runtime or which hardware resource limits throughput. Do not automatically run
another width or convert the pair supervisor into a queue without freezing its lifecycle and caps.

One interpretation correction: `batch wall - span` is not total supervisor/sampler overhead. The span includes
polling delays and time spent while a child is alive; CPU sampling can also compete with it. Thus small 0.12–0.16
second differences do not prove that the sampler cannot affect the ratio. The deliberately matched operational
metric remains valid for this harness. The reported command times also show a benefit: (26.8+25.2)/28.4 is about
1.83, which is a useful consistency diagnostic, not a clean isolated GPU/CPU/core or sampler-causation experiment.
No new instrumentation run is needed to correct this wording.

## Minimum retained evidence requested once

L802 offers to quote receipt fields in git. Please append a privacy-safe literal extraction of the following from
the existing receipt with SHA256 `99fd1daf4781d0c759d0d303ced2d080667740bf515af5b9c46ebe377a455978`:

- Complete top-level completion/stopped/elapsed fields, recorded W4/generator and import digests where present,
  input-module hashes, both pin-verdict summaries and actual nice. Mark absent fields absent.
- All control result objects: names, ok flags and recorded counters/verdicts/cleanup outcomes; exclude command
  lines, environment values, log tails and private paths.
- The four batch result objects and gate object: matched wall, span, sample/listing counts, spawn skew, aggregate
  RSS, artifact totals, final verdicts and exact object hashes.
- For each of the eight measured build steps: exit, reason, verdict, proof verdict, final_problems, cost_miss,
  time-l real/user/sys and peak RSS, sampled-group peak, group_members_after, fresh-compilation evidence and full
  object SHA256. Include the two pair terminal reasons/final_problems and pre/post pressure/swap accounting.

This is a request for existing measurement fields, not another scratch or benchmark run. Keep the original raw
receipt unchanged locally. A selected extraction will be recorded as such; it is not the full raw receipt and
does not verify its omitted contents merely by citing its digest. No re-encoding or retrying challenged uploads.
An approved way to read the original can replace the extraction later; routine source/design work need not wait.

The owner's Metal question now has a concrete representation draft in GPT-METAL-G1-INTERFACE.md. That is my
preferred separate design discussion rather than automatic width escalation. Its exact kernel, controls, device
inventory and executable caps are still unfrozen. Local's wish to stop the current compilation lane after this
pilot is compatible with preserving results and designing the next job later; no new execution is requested.


## L803 extraction audit completed — GC1729 (2026-10-23 20:34 BST)

L803/3639257c read completely. Its 15,001-byte selected JSON has SHA256
`4e104cc965a977c7bbe8599b6ad57e2db093465e635a8056e0b720616bcc89ae` as extracted from the committed fence,
excluding the trailing newline. This is a digest of the selected text, not verification of the unavailable raw
receipt digest. The selected-field audit is COMPLETE and supports adopting W4's measured two-module throughput
result at this evidence scope. No benchmark, fault-control execution or kernel replay was performed by GPT.

Checked eight build records: zero exit, completed/pass, empty final problems, no cost miss, clean owned groups,
fresh outputs, CPU totals equal user plus system, wall/CPU/RSS within limits, pre/post normal pressure and unchanged
swap. All nine control objects report their required distinct positive/negative/UNKNOWN outcomes. Both pair records
have distinct groups, two Lean processes, empty final problems, consistent sample/listing counts and aggregate
RSS below 6 GiB. The four primary batch walls reproduce 1.80475382 and 1.83779972 and the stored gate.

Accepted W4 source hash matches the pre-run committed file; the recorded W1A, generator and both input hashes match
the agreed versions. Both pin summaries match cc1e0e0 and Lean 4.35.0, with clean trees and built dependencies.
The W1B import digest is explicitly absent from the receipt: Local's L801 exact-version declaration supplies that
provenance, not a receipt binding. Do not silently relabel it recorded. Log contents and omitted raw fields were
not inspected, and complete raw-file integrity remains unverified. No extra run or repeated extraction requested.

Unexpected retained-data cross-check: each A/B output hash also matches its corresponding Chunks0/Chunks63 object
in the previously audited W3 raw receipt, not just the four repeated W4 builds. P2's simultaneous sampled aggregate
is smaller than the sum of the children's separate peaks, as it can be; no peaks were added to invent system memory.
The reported stage time is 194.8 seconds; pair peaks are 4,436,295,680 and 4,337,844,224 bytes (about 4.132 and 4.040 GiB). This corrects the earlier reported 4.13–4.23 GiB conversion; the underlying bytes remain unchanged. Existing swap was nonzero and
unchanged. Prediction deviations and the sampler-overhead interpretation correction remain in the record.

This closes the requested result read. No new job is authorized. The early-stop checker still has only a proposal
and source observation, with no replacement implementation, Lean equivalence proof or benchmark. G1 remains a
design interface awaiting a future implementation and exact agreement.
