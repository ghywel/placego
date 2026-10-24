# CL624 / L894: nesting scope and a finite CQ01 compatibility definition

GPT, 2026-10-24; GC1804 / MI737. Source and mathematical specification review, no physical enumeration, Lean replay or job launch.

**Verdict:** D8 asks a well-defined descriptive question after fixing the alignment below. Its negative counterfactual is too broad. Job 2's finite compatibility predicate is writable now using the existing kit; the exact finite-support census and the relaxed channel-language intersection must remain different objects. Finish the accepted W76 and W8 work, then keep W78 held without a new idea and an exact new agreement. CL623 task 6 is already completed in GC1796, with the narrower Sparse16 follow-up in GC1798; those reviews are not reopened.

## Sources actually read

- Full CL624 at `b69239ad5130b628e4a4c0fd9710b5aae85b2217`, L893 at `87d7e4e3aaa39031575764aa539235826da32b7c`, L894 at `2e8488fad463a6b980d0cc3379b38973ce3ab589`.
- Full `tests/probes/wolfram/d8_maximizer_nesting.py`, SHA256 `35b472a83790969a3e04a1f02e3ea6dc3b9ff58ee40b4565db53ac4381af6dc3`; `p1_lane_engine.py`'s `trace_bits`, `recon`, `index_of`.
- Kit `2f63afda261888e04ec57237290e723190914a1d` sources retained for GC1796: `Rule30ZeroBoundary` (SHA256 `95279579b7a51d750a87db786ade44cf55627bd805e6a4d369126adc91d1004d`), reconstruction, locality, light-cone and Theta interfaces; `Rule30PeriodTwoSideways` (`d08b1d0d0ea35051855323fbf1e8a88f01ab39a89ad0361b76f161437c206b54`), gluing and finite exact-death proof; full `Rule30DrivenPrefix` (`7be112c4105a8f94196eb8fe08335238df415d53176146ffcd847e6cd3b988dc`). No new formal theorem is claimed.
- GC1775's Job 2 scope, GPU-METAL-JOBS sections Job 2 and J.4, MAP section 7, GC1794/1796/1798 reviewed first. Record search `finite.horizon.*compatib|d8_maximizer|nested.*prefix` returned 20 hits in 11 files; the directly relevant reports were read separately. RECORD-MAP read fully after compaction. Older startup simulations were not repeated under the current no-duplicate-compute instruction.

## 1. D8: exact alignment, limited inference

Let M_W be the complete set of maximizing lane indices at width W and n=W/2. D8 projects j in M_(W+2) to j mod 2^n, then compares the top k bits of this **projected** index with the top k bits of M_W. These are the same absolute odd trace times W-2k+1, W-2k+3, ..., W-1. It drops the new bit at time W+1. It is not comparing the newest k trace bits at each width, which would shift the time window by two. The chosen comparison is appropriate for the extension question; label it explicitly.

The identity is carried by `index_of` and reconstruction locality: a low-n-bit trace projection determines the same initial depths 1 through W. It does not preserve the zero tail beyond W, the lifetime, or maximizing status. Thus Q_k subset P_k is a valid finite observation, not an implication of the coordinate identity.

Correct the counterfactual in CL624 and D8: non-nesting refutes the policy that **only extensions of the previous width's maximizing k-bit blocks need be searched** at that tested step. It does not kill incremental exact search in general: a method may retain nonmaximizing blocks or use sound upper bounds. Conversely, nesting at six measured steps supplies neither a pruning certificate nor a law for W78. The question also does not establish that late bits alone determine death; D5's within-block spread remains relevant.

Two small adversarial readings of the actual code:

- With A={0}, B={0,2^n}, there are two B maximizers projecting to one A index. `projected_that_are_width_W_maximizers` returns 1, the number of **distinct projected coincidences**, not the number of B rows (2). Keep that label precise; add a separate multiplicity count if wanted.
- With A={0}, B={0,2^(n-1)}, the longest shared top-bit run is n although nesting fails at every positive k. A maximum over pairs cannot describe the typical pair. Report both, as D8 does; do not use the maximum to test an unstated typical-pair prediction.

Before retained-data execution, validate positive even widths in the intended 64..76 list, unique width arguments, nonempty maximizer lists and 0<=index<2^(W/2), and refuse an occupied output destination. Current `load` checks completeness and count/uniqueness but not these domains; out-of-range values can produce meaningless negative shared-prefix lengths. Bind the selected input digests and keep explicit analysis caps and small literal controls. This is a source/math verdict, not acceptance of an unbounded pairwise run or a new physical job. No need to rerun the census.

Cloud's prediction concerns the first five steps through W74; Local's concerns all six through W76. Retain both denominators. A complete negative result is useful, with the narrowed interpretation above.

## 2. Exact finite-support language for Job 2

Use the kit's phase: center c(t)=1 at even t and 0 at odd t. For a word v of length n define its right-visible meaning by

`v(s) = drv altCol R (2s+1) 1`, for 0<=s<n.

The corresponding left-neighbor trace a_v has a_v(2s)=1 and a_v(2s+1)=not v(s). It is specified for 0<=t<2n. Define F_v(k)=recon(a_v,k,0) only for 1<=k<=2n. `recon_local` makes this independent of every extension of a_v outside those times. More generally recon(a_v,k,t) is determined when t+k<=2n. The finite recurrence is the kit's recurrence, not a new engine.

Let R(B,n) be the set of distinct words v produced by right starts supported at positions 1..B, with all positions >B white, driven by altCol. Define

`J(L,B,n) = { v in R(B,n) : F_v(k)=0 for every L<k<=2n }`.

**Hand specification lemma:** J(L,B,n) is exactly the distinct right-visible words of finite configurations with black center, left support through L and right support through B whose center alternates at every time 0..2n. This is finite-horizon compatibility, not an infinite CQ01 counterexample criterion.

Carrying argument:

1. Fix a right witness R. The kit's Psi R has trace a_v through time 2n-1, so Psi R agrees with F_v at depths 1..2n.
2. `alternates_iff_meets`, `history_eq_recon` and `recon_local` imply that a left row compatible through time 2n agrees with Psi R at those depths. Hence its white tail beyond L forces the displayed zero tests. Alternatively, a first discrepancy d<=2n makes the center fail at time d by `exact_death_center`.
3. Conversely, when the tests hold, choose the left row equal to F_v through min(L,2n) and zero elsewhere. It agrees with Psi R through depth 2n. The left light cone gives `Meets` for every t<2n; `evol_glue_upto` supplies the genuine whole-line evolution and center alternation through 2n. The chosen row has finite support through L. The same R witnesses its visible word.

There is no need to guess future visible bits for this definition. If a proposed test reaches depth K>2n from an n-bit word, its additional trace observations must instead be existentially quantified and tied to the **same** right witness/extension. Fixing unknown future visible bits to zero is not that quantifier. Testing a finite zero strip never establishes an infinite zero tail of Psi.

**Unexpected endpoint control, by hand:** for n=1, F_v(1)=1 and F_v(2)=v(0). Thus L=1 admits v(0)=0. The physical initial row with black cells exactly at -1,0,1 realizes this: the center is 1,0,1 through time 2. If one also fixes the next even left trace value to 1, reconstruction gives F_v(3)=not v(0)=1. Rejecting on depth 3 would wrongly exclude the stated horizon-2 witness; it tests time 3 as well (the witness's center then remains 1). This catches both the complement and the extra-step error. For n=0 the unique empty word has no left tests.

For a finite right seed, use `packed_sound` with its exact integer encoding and retain expansion; do not clamp each row back to B bits. At white time 1 first apply `step true`; subsequent white observations apply `double = step true (step false ...)`. Starting `double` at time 0 would use the wrong driver phase. In a finite-prefix implementation the last observation at time 2n-1 needs initial positions only through 2n; repeated `step_agree` gives this cone. For white-time states, `iterate_mod_bit` provides the corresponding two-step shrinking cone. Keep the strict inequality in that lemma. Use the existing packed reconstruction module when implementing; this review establishes scalar semantics, not a fresh audit of that module or an executable design.

## 3. Relaxed channel mode is a different census

If A_m(n) is a sound width-m right-channel automaton language with explicitly matched phase and initial-state semantics, define instead

`J_rel(L,m,n) = A_m(n) intersect {v : F_v(k)=0 for L<k<=2n}`.

It counts distinct words accepted by a relaxation. Acceptance is not evidence for a right start of support B, or even one finite right start producing an infinite accepted path. A_m is not interchangeable with R(B,n).

Disabling the left test recovers the exact chosen right-only language by definition. Also L>=2n makes this test vacuous, giving an explicit large-L control. The old channel tables use the opposite displayed phase and their own initial state; do not demand their numeric counts from the black-phase packed engine until the phase/onset/state map is established. An odd time shift changes the initial right-state population; it is not an automatic equality of support-bounded word counts.

Before any executable pilot: choose exact finite-support or relaxed mode; freeze L/B or m/n, phase, terminal horizon, initial state and deduplication; compare with independent tiny whole-line finite-start enumeration and existential completion; test complement, one-step, artificial-tail-clamp and path-multiplicity mutants; retain missing-word witnesses. Then set total stage wall/CPU/memory/output/disk/concurrency caps and stops. This report authorizes no new census or automatic benchmark.

## 4. Coordination dispositions

L893 reports submission 17, R30-20261024-a129c3, **Lean Verified, passed/pass**. Adopt that as Local's reported external status; GPT has not independently received its raw status response, and the earlier login-only API failure is not contrary evidence. L894 reports W76 at 279/512 with all checks passing; its earlier partial best 138 is not D(76). W8 remains accepted and unlaunched as reported. The header correction is for a later outward copy, preserving the accepted measurement pin.

On L894's bundling question: the already-planned W76 submission may finish this block after its actual-output review; it is not a precedent for one submission per later width. Prefer a bundle if that is already ready without another run or delaying the agreed block. No independent publication permission is being invented here; the owner's standing pipeline authorization remains the governing permission.

Gut verdict: the useful next step is the coupled specification, not another width doubling. D8 can guide attention after its finite-data controls; neither sign of its result decides CQ01. The specification above is a hand consequence of read kit lemmas, awaiting independent review before it carries an implementation. No prize claim or new all-width theorem.


## GC1805 / MI738: D8 revision 2 source repairs complete

Fresh git supplied `1664d4fc68db32bc775bab9c4b8f4915f7dd00cd` before a new flag or L895 narrative. The complete revised file was read; SHA256 `4db7064531d0009da758a1c52c8fda98d52c8844361ea5f6931121333d7e153d`. **Source repairs PASS in scope.** Projection labels and counterfactual now match section 1; distinct coincidences and row multiplicities are separate; empty/out-of-range lists, duplicate/disallowed width arguments and occupied outputs are refused. A one-million pair cap applies before each pairwise reduction. With the seven admitted widths there can be at most six such comparisons, hence at most six million pair scores, not an unlimited search. The retained census was not run here.

The four committed literal controls were executed and all passed: two rows/one projection, maximum versus non-nesting, disjoint top bit, low-bit change preserving top-20 nesting. These are file/integer fixtures, not physical Rule 30 computations, and do not substitute for operational limits or input identity.

**Unexpected statistic clarification:** `best[len(best)//2]` is the upper middle order statistic for an even row count. In the supplied two-row example the sorted best-match lengths are [0,32], so it returns 32 (the arithmetic midpoint convention would return 16). It is a valid upper-median convention; label it that way when interpreting the output, and keep the row-best rather than all-pairs population explicit. No numerical result has been seen and no need to change the computational convention after this disclosure. The original vague prediction “usually under 12” must not be silently reinterpreted as a prediction about every pair or every row.

For the intended six-step result, require all seven widths 64,66,68,70,72,74,76 and all six consecutive output rows. The CLI intentionally permits a subset and will otherwise silently omit missing pairs; a partial output must not score the full six-step prediction. Keep Cloud's five-step denominator separate.

Source correction review is complete. The production input manifest and a bounded invocation (wall/CPU/memory/output/disk/concurrency/pressure stops) remain necessary before an exact execution agreement. The pair cap is not a JSON read-size cap, a wall-time cap, or a retained failure receipt. Existing accepted W76/W8 jobs are unchanged, and no new job or retry is authorized by this source verdict. Next useful input is Local's actual frozen D8 invocation or W76 terminal packet, not another review of these repaired lines.


## GC1806 / MI739: D8 revision 3 stage review — input binding needs repair

Read the complete revision at `fc6bddade332ab49355f68b7d6c7b5cff338af73`, SHA256 `a76b34c45ad7940852bebf488642cd0ddc29a22cb23fba37e66c4f8ca1abd567`, and the reused W1A supervisor's initialization, sampling, final accounting, artifact counting and preflight. This closes the source read, **with corrections required before an execution agreement**. The manifest itself remains unavailable until W76 finishes. L894 is still the last fully read Local narrative; L895 appears in the source docstring only.

The changes requested in GC1805 are present: upper-median naming, all seven input widths and all six consecutive output steps, pinned W1A, 300-second stage/step wall and step CPU limits, sampled group RSS stop at 2 GiB and artifacts/logs at 10 MiB. W1A also retains 256 MiB swap-growth, 5 GiB free-disk, pressure and bounded monitoring stops, final CPU/wall/RSS accounting and group cleanup. The single analysis child is sequential. These are process/group measurements, not a system-memory peak certificate. The direct subset CLI remains outside this complete-stage contract.

**Carrying defect: the final matcher checks only exit code and width pairs.** It never compares the seven output `inputs[W].sha256` values with the manifest. Prechecking paths does not bind bytes read later by a child. Isolated execution of the actual AST matcher, on literal JSON fixtures, gave:

| Fixture | Required | Actual |
|---|---|---|
| Six steps, seven matching digests | pass | pass |
| Six steps, W76 digest changed | FAIL | pass |
| Six steps, `inputs` absent | FAIL | pass |
| Last step absent | FAIL | FAIL |
| Nonzero child exit | FAIL | FAIL |

This is a gate countercontrol, not evidence that any real census changed. Require exactly the seven canonical input keys and exact digest equality in the final matcher; a missing/malformed digest must fail. Also bind parsing and hashing to **one byte buffer** in `load`: it currently calls `json.load(open(path))` and then opens the file again for its digest. The unexpected control supplied D=116 in the first read and D=120 in the second: the returned record combined D=116 with the D=120 file's digest. `raw = bounded_read(path); d = json.loads(raw); sha = sha256(raw)` removes that discrepancy. The final manifest comparison then detects replacement between parent precheck and child load.

**Complete the invocation contract in the same repair:** require absolute regular input paths (or resolve them once before passing to the child). Currently a relative path is checked in the caller's directory but reopened with the child's working directory set to the new output folder. This can pass precheck and fail at execution. Read the manifest itself once for both JSON and digest. Pin bounded manifest/input byte sizes before unsupervised preparation; the current full-file prehashes occur before `Supervisor` starts its clock and RSS sampling. A small explicit preparation size bound plus the existing supervised analysis is sufficient here; no supervisor redesign is requested. Retain any preparation refusal as such, never a completed analysis.

The literal controls used only extracted source functions and synthetic JSON, with no W1A stage, retained-census analysis, Rule 30 evolution or Lean execution. Five matcher outcomes and the two-read control are retained locally as one JSON receipt; it was not uploaded because this private client's write interface permits GPT flags only. All failing outcomes are fully stated above. No production result or timing is inferred.

Reasoned/gut verdict: the finite statistic and six-step coverage are ready; the new wrapper still needs one coherent input-binding repair, then its frozen seven-file manifest can carry a bounded agreement. Do not rerun old mathematical controls or redesign the notebook supervisor. W76/W8 agreements and W78 hold stay unchanged. The independent CQ01 specification read remains pending; no new census is opened.


## GC1807 / MI740: D8 revision 4 binding corrections closed

Full source at `7f392f46e363a2640dca76b6e43029286469fdd9`, SHA256 `965f9b16fc233464c344540d78217a2027e485756d3f4ec0c62765bae40ab861`, read after fresh git/flag coordination. **Source/design review PASS in the stated seven-width scope.** GC1806's carrying defects are repaired: the final matcher binds exactly the manifest's seven keys and hashes, and `load` parses and hashes one byte buffer. The stage separately fixes the canonical keys to 64,66,68,70,72,74,76. The manifest is read/hashed once with a 64 KiB bound; each absolute regular nonsymlink input is read with a 16 MiB bound. Seven serial preparation reads therefore have a 112 MiB total byte ceiling; the supervised child retains the reviewed 300-second/2-GiB/10-MiB caps and W1A stops. These byte ceilings do not assert a decoded JSON memory bound; that work is inside the supervised child. The direct CLI is not a substitute for the supervised invocation.

All **11 committed literal controls PASS**. Seven additional pure-file checks PASS: one-buffer identity under an injected second-read replacement; exact byte-cap boundary; cap-plus-one refusal; symlink refusal; extra input key refusal; missing digest refusal; extra width-pair refusal. The replacement check offers D=116 bytes on the first read and D=120 on any later read: `load` makes exactly one read and returns D=116 with that buffer's hash. This strengthens the committed ordinary unchanged-file check. No retained census analysis, Rule 30 evolution, W1A stage, GPU or Lean execution occurred here.

The executable review is now closed; do not repeat the repaired control review. The remaining launch input is the actual frozen seven-file manifest including the terminal W76 result. Review that manifest against retained census identities/completeness and retain the exact invocation and preparation log before recording a one-stage agreement. No D8 launch has yet been accepted or observed. Preparation refusals are not analysis outcomes. W76 and W8 keep their existing agreements; W78 remains held.

The CL624 addendum at `35d905302b9e0eeafb00beb1f6b886e7ddda69a9` was also read in full. The owner's emphasis is adopted: the completed GPU census, engine, fixtures and digests are useful reusable data; the stop concerns the marginal cost of another width here, not the worth of the completed work. This review makes no independent global-record claim about the table. Gut: the binding issue is resolved, and the next useful evidence is the terminal packet, not more wrapper refinement.


## GC1811 / MI744: L898 adopted; exact meaning of the capped horizon

L898 at `9b639796383db7d74e828be3bd4182c22e4dda01` independently carries the
three steps of section 2 against the kit statements. **The finite-horizon
specification is now PROVED (hand, independently second-read).** This promotes
only that characterization, not CQ01 or an executable implementation. GPT's source
pin remains `2f63afda261888e04ec57237290e723190914a1d`; Local reports the same
nonpacked lemmas in its newer read-only kit. No new Lean replay was performed.

The sufficiency argument includes both possibilities: a first discrepancy beyond
2n, and no discrepancy at all. In the latter case `Psi_col` supplies `Meets` for
every time, hence `alternates_iff_meets` gives perpetual alternation. Excluding
that case by assuming a finite row must differ from Psi would assume the question
under investigation. The existing argument by finite light cones needs no such
assumption. Rechecked carrying statements: `history_eq_recon`, `recon_local`,
`alternates_iff_meets` and `exact_death_center` in the retained source files.

Local's proposed n*(L,B) is a useful output, with this precise definition:

`n*(L,B) = sup { n in N : J(L,B,n) is nonempty }`, taking values in `N union {infinity}`.

Include n=0: the empty word is always admitted. Prefix restriction sends every
member of J(L,B,n+1) into J(L,B,n), using the same right witness; reconstruction
at depths <=2n is unchanged. Thus nonemptiness is downward closed, and emptiness
persists at every later horizon. This statement does not imply that the numbers
of distinct words are nonincreasing: one prefix can have multiple extensions.

For fixed L,B there are exactly 2^(L+B) possible black-center starts. If each
fails alternation at a finite time, the maximum of those finitely many first
failure times is finite. Conversely, if arbitrarily large horizons are admitted,
at least one of those finitely many starts survives arbitrarily long, hence
forever. This is the finite-family quantifier argument; it does not establish
that every start fails. Claiming finiteness for all supports would still require
the missing CQ01 argument.

Keep the unit explicit. If tau(x) is the first time the center disagrees with
altCol, and T=max_x tau(x) is finite, then

`n*(L,B) = floor((T-1)/2)`.

It counts completed two-step horizons, not physical ticks. Exact n*=m pins T only
to {2m+1,2m+2}; the longest inclusive agreement horizon is T-1. A census capped at
N that still has survivors reports **n* >= N, right-censored**, not n*=N and not
infinity. Nonempty J at m and empty J at m+1 certify exact m. An incomplete
right-start enumeration cannot certify emptiness or that maximum.

**Unexpected endpoint check, by hand:** at L=0, F_v(1)=1 for every n>=1, so the
required zero at depth 1 fails regardless of B. Therefore n*(0,B)=0. Physically,
the initially white left neighbor and black center give rule(0,1,r)=1 at time 1,
failing the required white center. This checks the empty horizon and the odd
failure-time convention without a census. The prior {-1,0,1} control still
survives through time 2 and fails at 3, as section 2 states.

The proposed scalar enumeration, reconstruction and independent whole-line
comparison have the right mathematical scope. Next input is Local's frozen
executable, exact grid/horizon limits, control and mutation expectations,
source pins and stage-wide resource contract. The whole-line control must
compare distinct visible-word sets, not just counts. Retain an actual compatible
start for each reported nonempty case and distinguish exact/censored/refused
outputs. If packed modules enter, their source/soundness interface needs its own
read; this adoption is not acceptance of an unseen implementation or a launch.
No new computation, review request or all-support theorem is created here.
