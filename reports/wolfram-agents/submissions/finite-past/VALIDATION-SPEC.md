# Package B: validation specification, not an execution freeze

GC2302 current state: [full review and selected source](README.md#gc2302-frozen-development-accepted-plain-submission-form-selected).
The frozen L1229 module development stage is accepted PASS; earlier failures
remain retained. The selected plain submission source is33c82f32, with all
five mathematical bodies unchanged. L1230's two form probes remain exploratory.
Local alone freezes the next official check and notebook; no GPT compiler.
The historical GC2295 input pins below are superseded by current assembly.json
and README. Original module guards stay tied to0072d264and are not asserted to
have compiled against the plain form. No routine owner permission is needed.

## Exact interface to review

The source order is:

1. `Rule30FinitePastDraft.lean`: physical `Span`, finite-nonzero domain, root,
   endpoint growth, injectivity and simultaneous root/age decomposition.
2. `FiniteParentCriterionDraft.lean`: actual predecessor, white at every i>=R,
   finite iff the target and parent both have a black cell at L+1.
3. `NormalizedFinitePastDraft.lean`: translation covariance, normalized n-step
   injection and exact range, including n=0 and width zero.
4. `FinitePastCountDraft.lean`: exhaustive duplicate-free row and image lists,
   and exact all-width counts, using the existing Jen Boolean-word enumeration.
5. `SubmissionHeadlinesDraft.lean`: seven public wrapper statements. This imports
   the official `Ruliology.CellularAutomata.Rule30Prize` module but also the local draft files; it
   is NOT yet a self-contained verifier module.

The current [source comparison and provenance](../../../GPT-PROOF-DELIVERY-RESUMPTION-20261030.md#gc2290-normalized-source-actual-counts-and-older-external-provenance)
credits G121/G122/L077, actual kit ingredients and Karttunen's 2016 OEIS records.
The age-distribution, three/four-black bounds and mixed-driver infinite tails
are outside this proposed delivery scope. No new mathematical priority claim.

The public wrappers are:

- `Rule30Submission.finite_root_age`
- `Rule30Submission.finite_parent_test`
- `Rule30Submission.normalized_ancestor_bijection`
- `Rule30Submission.finite_word_enumeration`
- `Rule30Submission.finite_parent_enumeration`
- `Rule30Submission.finite_parent_count`
- `Rule30Submission.finite_parent_small_widths`

## Prepared source assembly

[Rule30Submission.lean](Rule30Submission.lean), SHA256
`8664d9e306f508edf8b83d56a90c63be2bb11ba6fa993bf07c7cf1916d438235`,
is now a 30,692-byte single-file preparation artifact, still **UNCOMPILED**.
The deterministic [assembler](../../../../tests/probes/wolfram/assemble_finite_past.py)
pins all five inputs, permits removal only of their exact listed module/import/
public-section lines, and retains every remaining body byte. [assembly.json](assembly.json)
binds the five body hashes and their byte offsets. It adds the actual official
Prize and Realization imports once. No namespace or theorem-body rewrite occurs.
This is text assembly and a byte-binding check, not a compiler stage or a
replacement for carrying review. A final accepted assembly still needs the
validation stages below.

## Controls required before a passing development verdict

The [positive guard module](FinitePastValidationGuard.lean) now implements these
controls against the actual assembled module, including the inherited endpoint
and small-root guards. It uses independent literal rows for image orientation,
width-three/four membership, the sole finite-parent word1101, and the infinite
half-line counterexample. The [negative control](FinitePastExpectedRejection.lean)
is deliberately ill-typed and separate. Neither has run. The older
`FinitePastGuard.lean` remains retained with the closed GC2287 stage; do not
import it alongside the assembled source, which already carries its dependency
namespace. A new stage compiles the assembled source, then the positive guards,
then requires rejection at the deliberately false declaration. An import or
positive-control failure is never counted as that expected rejection.

| Control | Required result and purpose |
|---|---|
| All-white | Fixed by physical evolution; outside `FiniteNonzero` and `Root`. Detects a vacuous zero-root decomposition. |
| Width 1 and 2 | Literal singleton and adjacent pair are roots; neither has a nonzero finite parent. |
| Physical versus normalized image | A singleton at0 evolves to black sites -1,0,1; its normalized image is black at0,1,2. Check the translation sign against literal supports. |
| n=0 | Normalized image is the original row; zero-step past is finite nonzeroness. No accidental positive-age assumption. |
| Width zero | `Normal 0` has no inhabitants and `allRows 0=[]`; no subtraction convention manufactures a zero-width ancestor. |
| Width 3 | Literal111 has parent1; literal101 has no finite parent. There are2 words and1 parent-word. |
| Width 4 | The four words1001,1011,1101,1111 are enumerated once each; only1101 has finite parent11. Both `mem` directions and `Nodup` matter. |
| Right boundary | Exercise `finite_parent_test` on an actual white-right predecessor with the boundary starting at R. For11 at0,1, the step row p(i)=[i>=1] makes both test bits black but is not finite: it must not satisfy the white-right premise. |
| Image enumeration | Show membership and duplicate-freeness of the image list, not only its length. |
| Expected rejection | A separate ill-typed control must fail, such as trying to discharge `False` with the zero-exclusion theorem. Its failure is required; never interpret a failed positive compile as this control's success. |

The right-boundary countercontrol is hand-checkable: take target11 at0,1
and p(i)=0 for i<=0, otherwise1. Its physical output is11; both uniform
exteriors map to white. Here y(1)=p(1)=1 but p is infinite and p(R)=p(1)=1, so the
omitted boundary hypothesis would make the statement false. This is a control
of the conditional statement's meaning, not a newly compiled counterexample.

Inspect the complete actual compiler output and axiom closures. Standard
axioms may be a subset of `propext`, `Classical.choice`, `Quot.sound`; do not
invent an expected exact set or declaration count before seeing the actual
successful source. Any `sorryAx`, new axiom, unsafe kernel-skip option or native
decision tactic is disallowed. Module compilation and kernel replay remain
separate checks.

## Environment and stage boundaries

Live portal instructions1.17.3 were read at this checkpoint, SHA256
`1e702976f3bdd169350a7cc034161775e335d35f4badce457c03872c82bc6709`.
The live environment at21:03:37UTC reports verifier commit
`19540bfb974ef743bf98818e768c1ee94f62eecf`, Lean4.35.0,
Mathlib`56a005855ea17e0b0958f73ec801ae140b0a1679`, LeanLink1.2.1,
image`rule30-verifier:11`. This differs from research main a6399ef1. Bind the
actual relevant dependency and `Check.lean` hashes; never treat main's newer
modules as installed in the verifier. Re-read the environment before a real
validation/submission stage.

Direct reads at the verifier commit confirm byte-identical Jen, Realization,
Prize, unchanged checker, toolchain and Lake configuration compared with
research main. The root `Rule30PrizeKit.lean` differs only in its catalogue-count
comment (136 versus168). Its actual imports include `Rule30Equivalents`, so a
small core proof does not by itself imply a cheap whole submission import.
GC2295 removes that unnecessary root import. The unchanged verifier checker
sets `statementModule` to `Ruliology.CellularAutomata.Rule30Prize` and tests
that exact module's presence; its diagnostic suggests Rule30PrizeKit but does
not require the root. Direct Prize and Realization imports both depend on Jen,
which has no explicit import. This gives the needed core source closure at the
retained verifier commit. It is a source dependency audit, not compiler success
or a measured memory bound. The prior55024c94assembly stays in git history;
the new8664d9e3 changes imports and preparation comments, with all four proof
modules and all seven public theorem bodies/types unchanged. Re-budget the
actual chosen host and retain the complete validation outcome.

1. **Compatible-toolchain development.** A new stage is possible only after
   locating or deliberately provisioning4.35 and freezing the complete changed
   source, driver and controls. The Intel's earlier4.33.1 dependency failure is
   not repaired by repeatedly invoking it or patching official source.
2. **Single-module assembly.** Carry the four source bodies and public wrappers
   in `Rule30Submission.lean`, with actual official imports only. Remove local
   draft imports and intermediate module headers by an explicit, reviewed
   assembly procedure. Compare each retained body and all seven types to its
   reviewed source. Namespace changes, if any, require renewed type/source
   binding. No dependency file can be silently omitted because it compiled in
   another checkout.
3. **Official check.** Freeze the assembled source and unchanged checker at
   the current verifier commit. Run the exact partial-headline check for all
   seven wrappers. Retain exit codes and raw JSON, replay count, declared count,
   source/toolchain/checker digests and each actual axiom set. A development
   `#print axioms` is not a replay verdict.
4. **Notebook validation.** A separate freeze binds the checked single source,
   assembled essay, metadata, abstract, illustration controls and validator.
   Use a plain kernel and MarkdownToNotebook with `UseCache -> False`, not a
   hidden front end. The embedded UTF-8 source must match byte-for-byte, the
   source literal may remain uniconized (GC2303, as in A), `rule30Submission` must be the actual imported environment,
   all seven `TypeForm`/axiom entries must exist, and the final replay must have
   the exact count observed in the official stage. `IncludeInternal -> True`
   avoids the previously demonstrated LeanLink name-filter omission.
5. **Delivery.** Independent carrying/source/artifact review, final current
   prior-art check, required core-catalogue PR, and one assigned posting owner
   precede upload. Owner authorization already covers posting after these
   checks; no new routine consent round is needed. Retain the submitted source,
   notebook, abstract, public receipt and live status. Human review is separate.

No stage is launched by this document. Before any actual stage, measure current
host load/headroom and publish prediction, counterfactual, source hashes,
controls and enforcement details. Intel defaults remain one job, nice10, at
most2threads, pilot120aggregate CPU seconds/300wall/768MiB RSS; any separately
justified larger stage stays within1200aggregate CPU/1800wall/1536MiB/4threads.
Use `run_capped.py`, tree tracking and a real aggregate CPU monitor. Launch
headroom4096MiB, floor3072MiB, swap-growth64MiB,16MiB/file/128MiB/stage.
Pressure/thermal/monitor failure stops the job and preserves the receipt; no
automatic retry or cap increase. Earlier M5 notebook caps do not transfer to
this Intel host. No simultaneous job with another stage and no assumed M5
allocation. A stage that cannot fit these constraints stays unlaunched.

## Essay controls and expected illustrative values

`essay-prose-draft.md` contains a literal local-rule illustration and independent
integer-map cross-check, not an executed notebook. Its expected rows at times
0..4 are1,111,11001,1101111,110010001. Their centre bits are1,1,0,1,1.
The count table, columns(width,total,parent,root), is expected to be:

```
1  1  0  1
2  1  0  1
3  2  1  1
4  4  1  3
5  8  2  6
6 16  4 12
7 32  8 24
8 64 16 48
```

Those are mathematical expectations, not copied runtime outputs. Every future
notebook check must refuse a missing or duplicate headline, a wrong width-three
count, a changed translation orientation, mismatched source bytes, unevaluated
symbolic output and a forged/replaced replay result. The final source marker
must be absent, its replacement must contain the exact source bytes, and no private local path,
account ID or credential may be embedded. The numerical illustration validates
its presentation only; it cannot establish the universal theorem or its novelty.


## Coordination after L1219/L1220

Local's L1219 review accepts consistency of the seven headline statements,
not yet the definitions or proof bodies. Its proposed compatible4.35 B
**development** stage after confirmed resumption is welcome, with A's notebook
first and exactly one compiler owner. It still needs its own committed source,
guard, driver, control and resource freeze; this specification does not start
it or assign posting. GPT keeps B source preparation and will not start a
competing B compiler stage. L1220's restart pause was superseded by Local's
explicit L1221 resumption; no B stage has yet been announced as started.
A compilation pass cannot substitute for the pending definition/carrying read.
