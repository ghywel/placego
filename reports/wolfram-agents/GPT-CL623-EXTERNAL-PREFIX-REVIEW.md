# CL623 task 6: external results and the missing prefix bound

GPT, 2026-10-24; GC1796 / MI729. **Requested statement/proof-shape review complete, with the Sparse16 source limitation below. No Lean, GPU or orbit replay.**

The useful imports are the generic masked-periodicity exclusion, exact forced-row/death interfaces, parametric strip certificates, and existing controlled-response/dependency modules. None of the reviewed results supplies a general cheap bound for L885's deep-free-bit branches. Sparse16 does give a precise *conditional sparse-branch test*; proving its spatial-weight premise cheaply is the missing bridge. Do not change the running W74 census or drop lanes using the Psi constraints.

## Evidence and scope

- External submission [R30-20261024-9d92a2 Lean source](https://www.wolframcloud.com/obj/rule-30-prize/Agents/api/file?id=R30-20261024-9d92a2&kind=lean), 145,345 bytes, SHA256 `57bd19e546495805c816437239133c694a9ef5ed43a1163b3ad6246f7fe9d1cb`. Read all five families at the requested depth, with detailed reading of the period-2 arguments. The official public receipt reports Lean Verified, 653 replayed constants, standard axioms only, kit `2f63afda261888e04ec57237290e723190914a1d`. Its checker lists 20 headline entries; the abstract's 74 is not that receipt count.
- Pinned kit sources: `Rule30PeriodTwoSideways`, `Rule30PeriodTwoWidth6`, `Rule30ZeroBoundary`, `Rule30ZeroBoundarySmall`, `Rule30FiniteClockSixteen`, `Rule30ControlledResponse`, `Rule30DrivenPrefix`, at that same commit. Relevant definitions, statements and carrying interfaces read; this is not an independent kernel verification.
- Existing literal tables: `submissions/channel-14/Pilot6.lean` and `submissions/words-A/Rule30Submission.lean`, `words-B/Rule30Submission.lean`, relative to this report's directory. Pure string/graph checks below, no new physical census.
- Record searched for Psi/paramStripCert/Sparse16/prefix pruning; existing GC1772, GC1775, GC1794 and MAP scope used. Old closed cell-recovery/skeleton routes were not reopened.

## 6a(i–ii): Psi is a proper restricted interface, not the census domain

Using the kit's conventions,

`Theta f = lam (alt f)`, with `alt f (2s)=true`, `alt f (2s+1)=f(s)`;

`u R s = drv altCol R (2s+1) 1`, and `Psi R = Theta (fun s => !u R s)`.

Thus Psi takes a right half driven by an alternating centre and constructs its uniquely compatible forced left half. Its free bits are the **complement** of the right column at the white times. Keep the phase shift: `altCol` is black at even times here; the channel certificate's displayed clock is white at even times. An odd time shift aligns those observations.

Q01 concerns *every* finite left half, equivalently the absence of finite `Theta f` for arbitrary f. CQ01 concerns coupling finite halves; the kit identifies it with the absence of finite `Psi R` for finite R. Arbitrary free choices in P1 are not already certified to be a Psi image. The distinction is essential, not a notation change.

`isR30_bad_or_periodic` uses monotone finite ranks: either the evolution enters the bad rank, or its column 1 is eventually periodic **at the white phases** with a period compatible with the driver/certificate. It does not assert full-row periodicity. For finite Psi the periodic branch is excluded using the already-known impossibility of eventually periodic free bits. The bad branch remains; this is not a solution of CQ01 or Q01.

`Psi_free_constraints_width6_of_finSupp` assumes `FinSupp (Psi R)` and returns an existential settling time S0, followed by exclusion of the listed patterns. It supplies no computable S0 bound for a free prefix. In contrast, `u_golden` and `u_black_among_five` hold for arbitrary R from s=0: u has no 11 or 00000, so its complementary free bits have no 00 or 11111.

`Psi_even_first_defect_le_10` says each even row first differs from the spatial alternating stripe at an even depth in {2,4,6,8,10}. **That defect is not death.** Psi is in InX, so it satisfies every even-time survival condition. A useful adversarial control is `Theta (fun _ => true) = stripe`: it is an InX row but cannot be a Psi image, because its free bits contain 11111. Its finite truncations are valid left-census inputs. Rejecting them by a Psi-only invariant would change the domain being maximized over.

`Psi_black_in_window_16` does bound white runs, but only as follows: for each even row and each d≤16, some black cell has d<k≤33. It is not a length-16 sliding-window result at arbitrary spatial depths. The general wrapper `inX_black_in_window_of_q01` **consumes an already-proved width-W death bound** (<2D) to obtain a black cell in (d,2D−1] for d≤W. Reusing this wrapper with a stronger certified width bound is legitimate; using it to establish the very width bound it consumes would be circular. Neither it nor the shallow stripe defect controls the white run beyond W=74 in GC1772's identity.

The depth-1000 computations are also narrower than the general census: `Psi empty 997=true`; for W≤988, a black cell lies in (W,W+9], and that particular row's truncation fails centre alternation within nine steps of W. Every left half supported through 996 paired with the **empty right half** fails by 997. This is not a D(996) bound for arbitrary free bits, nor all-width CQ01Empty. The period-3 011 counterpart certifies depth999, windows W≤990, and left width≤998 with empty right. These are the exact theorem endpoints, more precise than “up to depth1000.”

## 6a(iii): nine words; the initial channel state matters

The actual kit list has **nine**, not thirteen, words. Traversing the existing 31-state `succ6` table on those literal words gives:

| Right-visible word | Accepted from initial state 0? | Accepted from any state 1..30? |
|---|---|---|
| 11 | No | No |
| 00000 | No | No |
| 100101 | Yes, ends at 11 | No |
| 10010001 | Yes, ends at 4 | No |
| 101001 | No | No |
| 1010100001 | Yes, ends at 4 | No |
| 1010001001 | Yes, ends at 13 | No |
| 10010000101 | Yes, ends at 11 | No |
| 1001000010001 | Yes, ends at 4 | No |

No transition returns to state0. Hence all nine are excluded in this graph after its first visible observation, although six are allowed as initial words. This is a strong consistency check with the eventual exclusion, and shows why silently applying an eventual restriction at time zero is wrong. The graph fact itself needs no finite-Psi assumption; transporting it to a physical statement uses our existing channel soundness and the explicit phase alignment above. We have not proved that avoiding these nine words *characterizes* the whole graph language. The kit's 54-rank bad-class certificate and our 31 subset states are different representations, not interchangeable state labels.

The checks parsed all 31 edge pairs and all nine patterns, tested every start state, rejected 11 and accepted the one-bit positive control 0. These were finite table comparisons, not a new Rule30 experiment. Initial word-table parser assertions failed because list endings were on the same line; parsing was corrected before any overlap count was reported. The corrected check verifies 48/80 distinct words and 22 parametric families. Reproduction script: `tests/probes/wolfram/task6_table_review.py` (external Lean and pinned width6 file supplied as arguments).

## 6a(iv–v): coupled clocks and skeletons

`not_coupled_of_right_masked_periodic` is worth adopting as a generic interface: a periodic driver containing a black phase, together with eventual same-period repetition of the right head on driver-white phases, excludes a finitely supported compatible left half, via FiniteMaskedJen. The right half need not itself be finite. Period2 fits its formal scope, **but proving that masked periodicity is exactly the missing work**, not a consequence of finiteness alone. The kit's period2 eventual-free-periodicity obstruction is already the corresponding door. Rule210 uses a different local map; our two-sided result there does not supply this premise for Rule30.

The period4 empty-right results for 0001/0011/0111, including phases, prove entrance into explicit invariant traps (bounds14/12/16) and then apply that interface. The period3 001 traps enter at1270/1269/1268 by phase. Their empty-right scope is decisive. The all-finite-right versions remain conditional on `Absorption`/`AbsorptionT`; the period2 empty-right result in this file is only the finite997 statement above. No automatic transfer of trap certificates between drivers.

`q001_width_le_12` is a zero-boundary observation statement at times **3j<28**, j≤9; Q01 observes **2j**. It does not establish the period2 condition by changing a name or time unit. Its related InX3 window statement stays in that clock. The skeletons supply eventual masked values of column1 under specified periodic columns: useful intermediate conditions, with existential settling, not unconditional column exclusions or a new D(W) bound. Reuse the modules; do not repeat the already-closed skeleton work.

## 6a(vi): parametric families overlap 48/128 listed words

The 22 tuples cover eight white-pad and fourteen black-pad families of periodic words c^r u, r≥r0. The proof builds an abstract strip set closed under padding, checks the period map and the required forced colour, then invokes the finite masked Jen obstruction. Closure is explicitly checked; soundness does not assume a bounded saturation loop necessarily reaches a fixed point. A fixed r repeated periodically is the scope: arbitrary concatenations with varying r do not follow.

Direct string comparison, permitting cyclic rotation and respecting each r0, gives **25/48 words-A and 23/80 words-B**, total **48/128**. Literal, unrotated matches are22 and16 respectively. This is direct membership in the stated families, not a claim to have exhausted all possible derived consequences or shorter-period identifications. Thus the new families generalize many of our individual exclusions, but do not blanket-subsume the128 table. Cyclic rotation is valid for eventual periodic-column exclusion by shifting the onset.

Our submitted word tables precede this submission; call this overlapping/later parametric generalization, not retroactive prior art against those submissions. For *future* claims these external families and their method must be checked first. The basic white-end family and the 10111-pad family already have kit predecessors, which the external source acknowledges. Adopt `paramStripCert` as reusable machinery without conflating it with a free-prefix survival certificate.

## 6b: one conditional sparse-branch candidate, not a general bound

The [official Sparse16 entry](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261023-60d213) states that survival at even times0..110 forces at least17 black initial cells in depths1..111, with arbitrary farther tail; its receipt reports Lean Verified and a Human Verified tag. **Conditional on that advertised theorem**, a branch B is prunable beyond110 if one certifies `max_{x in B} weight(x[1..111]) <= 16`. For a spatial partial assignment, known black count b plus all still-unknown positions u gives the safe sufficient test b+u≤16. At W74, positions75..111 are already zero. This needs an **upper capacity** over every completion, not a lower weight estimate or the weight of one maximizer. A deep free-bit prefix does not directly fix a spatial prefix: triangular reconstruction depends on earlier free bits, nonlinearly. Clustering alone supplies no capacity certificate. `DrivenPrefix` provides exact dependency and shrinking-cone interfaces for developing such a certificate; `ControlledResponse` quotients right halves under **all** boundary words and helps right-half searches, not arbitrary left branches; finite observed equality is explicitly weaker. `FiniteClockSixteen` assumes an actual full-state 16-cycle and derives head-period rigidity; survival and weight16 do not supply that hypothesis. **Next useful design target:** a sound, cheap spatial-weight upper envelope from a free-bit branch, stopping if it is always >16 or costs essentially full enumeration. No implementation, pruning efficacy or new job is claimed. Sparse16's carrying notebook was not independently read: there is no separate Lean link, and the download exceeded the chosen5MB read cap. That is an evidence limitation, not a mathematical or GPU memory cap.

## 6c: optional directions, explicitly scoped

- XOR rigidity: the advertised theorem forbids nontrivial XOR superposition of finite-seed histories; useful guard against linearizing Rule30, no D(W) pruning mechanism supplied. Public statement/receipt only, not a carrying-source audit or novelty determination.
- TraceEdge: next target is a mechanism showing that one matching trace determines enough of the right response class to force the left edge; full state injectivity is already false. This addresses the unknown-right-half obstruction rather than adding more fixed edge pairs. No new E1/E2 run requested.

## Decision and next work

The scope kill tests tipped against using Psi constraints as P1 pruning; the table comparison supplied a useful initial-transient explanation. Sparse16 offers a sharply stated restricted candidate, whose missing premise is now explicit. No general prefix bound or prize claim is promoted. W74's one accepted attempt was launched in L888; its actual retained outcome remains pending, with no retry or W76 agreement. The newly committed lower74 submission generator/gate at `c171c3cd` is the next accessible source review, while the witness/output dependency remains separate.
