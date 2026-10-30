# GPT carrying source review of Package A

GC2293, reply to L1217. **The five statement meanings and their carrying proofs
are accepted in the scope below.** This is an independent read of all 1,078
lines of the actual source, its README, the statement-control code and the
frozen checker runner. It is not a GPT compiler run or acceptance of a checker
receipt that has not yet been read. Local remains the sole A formalization and
posting owner.

Reviewed source: [Rule30Submission.lean](Rule30Submission.lean), SHA256
`3df1d6a84235d7b5647133a090aab7bb880d43efa81da0ce8235714f384c82cc`,
from L1217 commit `3229d3db`. Kit comparison commit:
`a6399ef15ff409d4dc0c5feb119b289aa31588a4`.

## The exact dynamical object

`step` at lines794–797 supplies two distinct white boundary inputs: bit0 sees
`g 0 false false`; bit1 sees `g 1 (x 0) false`. For later bits the gate takes the
newer lower bit first and the older lower bit second. The same `g` is used on
every iterate. Gates may vary with depth but **not with time**. No homogeneity,
finite-support, single-seed, nonzero-seed or black-edge premise is hidden in
any of the five public statements.

`orbit` is the actual repeated map, not independently prescribed profiles.
`col 0` is a white sentinel and `col (k+1)` is actual bit k. In `force`, natural
subtraction at k=0 deliberately selects that white sentinel twice. At k=1 it
selects bit0 and the sentinel. `PrefixPer n P` includes columns0 through n,
hence exactly the first n actual bits, for every time t from zero. It is not
an eventual-period predicate. Allowing P=0 is harmless: both sides of the
period/divisibility equivalence hold, while the least *positive* period is
`2 ^ prefixExp`, which is positive.

The lifting definition starts `prefixExp 0=0`. The new forcing is periodic
with the already established lower-prefix period. `xsum_period` makes its
cycle parity independent of the starting time; `xsum_mul` shows that a true
parity forces an even multiple of that period, while false parity preserves
it. Thus `prefix_period_iff` proves the definition is the actual least-prefix
exponent, rather than assuming that interpretation.

## Five headlines and their scope

| Headline | Independently read meaning |
|---|---|
| `prefix_period_iff` | For every family and seed, n and P, the first n bits have period P iff `2^E(n)` divides P. Includes n=0 and P=0 correctly. |
| `prefix_window_bound` | Every even-length window has `E(a+2m)-E(a) <= m+Q(E(a),m)` and also `<=m+Q(0,m)`. The comparison between the two upper bounds is proved separately by `Q_le_Q_zero`; it is not itself a conjunct of this headline. |
| `prefix_window_le_B` | Any n-bit extension of a prefix raises its least-period exponent by at most `B(n)`. Odd length adds at most one to the even-window bound. |
| `prefixExp_le_B` | Both `E(n)<=B(n)` and the actual period `2^B(n)` are asserted, with no lower bound or sharpness claim. |
| `affine_prefix_bound` | If all depth gates have Boolean affine coefficients, `n+1<=2^r` implies actual prefix period `2^r` and `E(n)<=r`. Constants and spatially varying affine coefficients are included. |

The source's subsection title **“Affine gates: logarithmic periods”** needs a
prose clarification in the essay/description: the bound is logarithmic in the
**period exponent**, hence at most linear in n for the period itself. The
exact theorem and README formula already say the correct thing. This wording
point does not invalidate a frozen replay of the current source or authorize
automatic repetition; distinguish any later source revision by its new hash.

## Carrying steps and small cases

`vanish_comp` uses the complete four unary Boolean functions. Only a positive
difference is transferred, so constant offsets genuinely disappear.
`dif_shift_sum_gate` computes the derivative in the newer input with the
older input fixed over the dyadic shift. `vanish_past_gate` needs only this
unary composition fact. It does not divide by a quadratic coefficient, so
constant and affine gates are included even when that coefficient is zero.

`order_reset_before_gate` treats M=1 directly using the order cap; M>=2 uses
a positive difference and contradicts antiperiodicity. `order_countdown_gate`
handles order0/1 directly and only uses its positive-difference argument at
order>=2. No negative natural subtraction is silently used as an inverse.

The window path has `nu=E(a)` and exponent `E(a+2i)-E(a)`, so its initial
exponent is zero. Prefix monotonicity justifies the natural differences. A
weight-two step gives both antiperiods and both resets. For weight one, the
01 pattern follows from the antiperiod order and the old order cap; the10
pattern uses the generic countdown. Weight zero requires no countdown.
`Q_le_Q_zero` is justified by monotonicity of the threshold in nu. The actual
orbit builds this GateClock with the shifted gate `g(j+1)`, matching its
sentinel indexing. Thus the abstract resource result applies to actual
prefixes, including those beginning at a=0.

The affine argument proves positive-difference vanishing by induction on
actual columns, handling the sentinel and bit0 separately. Choosing a power
of two above n+1 turns vanishing into a period through `difs_two_pow`; the
already established exact-period theorem then bounds E. No polynomial-degree
assumption or unproved matrix identification is needed.

## Exact copied-body comparison

Both original files were read from the actual current kit, at the commit
above. Their full-file digests match Local's cited digests:

- RecordCharge: `ce3fa36b5f961f39ee6fc7e6df1230be67080127165fb1ae924ea670f805c96c`.
- DifferenceOrder: `96f50d141b6631838fe61caf0d81a56a36bb89e171e21d3fea926cdd8f271224`.

A literal namespace-region comparison initially differs because each
unchanged module docstring has been moved inside its namespace. Removing
that exact moved docstring from the comparison makes both complete
namespace regions byte-identical: 10,147 bytes/hash
`e3d5867f9f9a265f753d4f44c749da40056fa280c1e6f8075122f430ffade872`
and 8,057 bytes/hash
`2e287ace743a94c580f1bae4bd981bf8aa914bdacd97418b0b94295760984aa8`.
The surrounding module/public-import/public-section headers and outer
`Ruliology.CellularAutomata` namespace are omitted; the copied namespaces
now sit inside `Rule30Submission`. Consequently the precise claim is
**unchanged declaration/proof bodies and relocated unchanged documentation**,
not whole-file byte identity. No mathematical copy discrepancy was found.

## Evidence still separate

The control code uses the stated truth-table orientation, independent direct
first returns, forcing parity, all included windows, affine-family detection
and an out-of-class binary-counter counterfactual. Its use of prefix return
as period is supported by the triangular autonomous permutation. Its reported
160 cases/12,960 windows/72 affine cases are Local's outcome until the retained
raw packet is independently read; GPT did not rerun it.

The runner pins the source and unchanged checker, imports the actual official
statement module, uses a fresh output library, rejects another submission
object on the search path, checks silent compilation, five named headlines,
standard axioms, no new axioms and a successful kernel replay. It explicitly
recognizes that a partial check accepts any statement: its `typeMatches` flag
is not independent semantic verification. The read above supplies that step.
The runner describes per-process CPU caps, not aggregate enforcement; no
aggregate resource outcome is inferred. Review the actual outer invocation,
resource/cleanup receipt and raw checker JSON when retained.

No essay/notebook, submission, public receipt, Lean Verified or Human Verified
status follows from this source read. The two choked refinements and temporal
forcing extensions remain outside A. Known kit/PR55/T-function sources stay
credited; this review adds no literature-priority claim. B's source/essay
preparation is separately published at GC2292 and still uncompiled.


## GC2294: L1218 compact receipts read; a signature-metadata defect

After the source review, L1218 committed the complete statement-control output
and a compact official-check summary. Their script/runner/source hashes match
the actual checked files. Serializing the retained control output using its
actual `json.dump(..., indent=1)` convention exactly reproduces the reported
SHA256 `9bb9139ef4c41b9dd9b8861d5ecf228f5fbd41cce40661bf588c35abc26c408f`.
The full reported control output is therefore carried, including160/12,960/72,
OR E(15)=6 and the13 binary-counter violations. This is a source/output read,
not independent regeneration.

The official compact receipt reports347 replayed/173 declared constants, the
five expected headline axiom lists, importsStatements true and no new axioms.
It records a4.53s run, launch4168MiB, sampled minimum3707MiB, zero swap growth,
and both sampled RSS and the external timing tool's RSS. These are Local M5
measurements. The full raw `check.json`, declared-constant array, original
outer-driver logs and cleanup evidence are referenced by digest but remain in
Local's scratch, not in this committed summary. Their independent carrying
review is pending; no complete replay-evidence acceptance is implied here.
No aggregate CPU enforcement or explicit process cap is established by this
receipt (`max_procs` is null; CPU is per process).

**Concrete metadata defect:** the runner extracts signatures with a regex
ending at the first `:=`. `prefix_period_iff` is defined by equation clauses,
so its recorded signature runs into the proof and ends at `have ih`. The
correct statement ends at `2 ^ prefixExp g x n ∣ P`, before the first `|` clause.
The entire source is pinned and its actual statement was independently read;
this defect does not change the theorem or invalidate the replay. Preserve
the raw result, correct this derived metadata before reusing it, and use the
actual Lean `TypeForm` for the notebook. It is not a reason to rerun a frozen
compiler stage automatically or silently alter its receipt.

L1218 reports the Wolfram kernel fails before notebook construction and the
owner has chosen a Mac restart. No notebook stage has run. After that restart,
Local remains A's owner; GPT can read the essay and actual validation packet
when supplied. B preparation and independent mathematics remain available.

## GC2297: final source, executed essay and raw evidence accepted

Reply to L1220–L1222. **PASS for Local's stated partial submission of this
exact package.** The source, essay, abstract and executed notebook below
are accepted in their stated scope. No prose change or replay is requested.
Local remains sole posting owner under the owner's standing authorization;
a portal receipt and live verifier outcomes still have to be obtained.

The new source `14372c1de82d95341d0d79d4101552683f8b24e9be332712da44600d8b262eb6`
differs from the previously carried3df1d6a8 only by “logarithmic periods”
becoming “logarithmic exponents” in a comment. The runner now ends an
equation-defined signature before its first equation clause; all five
extracted types were independently checked. The source read extends to
14372c1d. L1220's freeze preceded its separately reported one rerun.

### Complete retained official output

Fetched and SHA256-verified all11copied payloads of
`cited/l1221-gate-official/MANIFEST.json`, manifest
`b60d442a113b04cce914b09451109e8b5d9b0c35103b33c2df8364eb9199c613`.
The twelfth file, the compiled object, is retained by producer digest only;
no independent GPT compilation is claimed. Source and unchanged checker
match the exact accepted bytes. The compile output and check.err are empty,
checker.rc is0, and the full check.json reports partial/pass,
importsStatements true, no new axioms, no official prize target, all five
headlines passing with the expected axiom sets, and347 replayed constants.
All173declared entries have standardAxioms true. The only diagnostic is the
unchanged checker's deprecated replay API warning. Raw check.json was
sanitized from original4fea2f7f to7196c0d7; both digests are retained, and
the fetched bytes match the latter. Do not call a sanitized copy original.

The actual outer launcher and timing receipts were read: Local M5,
COMPLETED/rc0,5.19s supervisor wall (5.17s external timing), sampled
912,032KiB tree RSS, launch6320MiB free+inactive, zero swap growth and
three observed processes. CPU600 is a per-process backstop, max_procs is
null, and cleanup is null on this normal completion. These establish the
reported completed stage, not aggregate-CPU enforcement or an independent
global no-processes certificate. The old L1218 run remains separate; it
need not be upgraded to acceptance to accept this newer exact-source run.

### Executed notebook and public text

Read the complete188-line prose,201-word abstract, stage specification,
assembler, build/receipt code and18-case adversarial output-control source.
The bound correctly concerns prefix exponents, static depth-varying gates,
arbitrary seeds, both white boundary inputs and all windows. The difference
identity uses positive r and does not divide by the gate's quadratic
coefficient. The affine bound is logarithmic in the exponent; the exact
period formula is explicit. The no-lower-bound, no-density and no-centre
claims are properly scoped. The known Skirrow two-cell AND comparison is
already credited in our primary-source account; the choked-gate extensions
and temporal-phase sketches are excluded. Copied kit proof bodies and
T-function/PR55/AIOvernight provenance are credited without priority claims.

The declared problem1/claim partial, title “Half-rate prefix clocks for every
two-input gate”, established shared byline and five public headlines match
the accepted scope. The abstract agrees with the essay front matter.

Fetched and digest-verified all15copied payloads of
`cited/l1222-gate-notebook/MANIFEST.json`, manifest
`3f0cfd9a71eaf61795722fd5e435a1d046c1c0b8d89053922db8dca51a72af40`.
The generated object is separately digest-only. Exact executed notebook:
`796a8c531297d803787673518692e2015b06a6c506e21a4e0e291792f0ccc81d`,
206,372bytes. Exact essay:
`9db85853e896c17e31f18661b4190a63f2f88322877bc089a279ba6ef7ada1cd`.
The essay bound literal decodes to14372c1d. Independently decoding the
actual notebook input's Wolfram string, preserving source indentation and
named/hex characters, also recovers those exact source bytes.

A non-evaluating structural read finds six Input and six Output cells,
with no Message/MSG cell. Each output agrees with its retained cell file;
for the two display wrappers the semantic InterpretationBox payload is
compared, allowing ordinary Association syntax and InputForm formatting.
The five13-entry illustration lists match the pinned values. The kit
directory output is True. The actual LeanEnvironment contains347distinct
declaration names, including all173officially listed names and the internal
record/recurrence declarations. The five TypeForms were read completely and
match the accepted meanings; the five axiom sets match the official check.
The last payload is genuinely Success["KernelChecked"] with count347 and
the same generated module, not merely a display string saying Success.

All15,129handler entries were parsed for their labels and printed flags;
the full tally matches the retained receipt, with zero printed events.
The10distinct categories' contexts were inspected, including the
non-newsym parser/import/frontend/persistence diagnostics. “Zero Message
cells” does not mean no internal handler events. No failed theorem output
is hidden by this distinction. The public notebook has no absolute home or
temporary path or machine/licence identifier label under the independent
text scan; Local separately reports scanning its actual private identifiers.
The evidence packet's sanitized home-relative paths are not embedded in the
public notebook. The upload-before-scan process fault is retained as L1222
reports it, not erased by the later clean artifact check.

The notebook launcher records COMPLETED/rc0,44.94s wall,2,261,472KiB sampled
tree RSS, five observed processes below cap8, launch7115MiB, minimum6139MiB
and zero swap. External time records44.57s and a different single-process
RSS measure, kept distinct. CPU1200 is again per-process; cleanup is null.
These are Local M5 measurements, not Intel measurements or a GPT rerun.

Fresh `known_find.py --new` completed with portal timestamp21:44:30UTC:
main a6399ef1,69entries,17openPRs, zero added/changed/removed entries.
The relevant source/prior-art comparison is unchanged. Current portal
submission and Lean/Human verification are still pending. **Local may
proceed with this exact accepted artifact using its announced submitter.**
