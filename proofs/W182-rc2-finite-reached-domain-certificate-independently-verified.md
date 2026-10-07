# RC2 finite reached-domain certificate independently verified

*The waiting room (not yet verified). Derived from [PROOFS.md](../PROOFS.md), entry "GPT G182 — RC2 finite
reached-domain certificate independently verified (2026-10-07)"; rebuild with `python3 proofs/build.py`. Edit the
proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** in the waiting room: stated with a proof, not yet checked by a second reader.

## In plain words

The small-period reached timing certificate passes independent verification.

**What it says.** At period caps one, two, four and eight, supplied potentials pay every reached edge. The largest doubled timing budget is fourteen at cap eight. Parent paths, complete successor lists and all numerical inequalities were checked independently.

**Why it matters.** This closes the finite RC2 audit, while retaining its limitation: 398 labels represent 411 edges, so it barely compresses the state. No bound at all periods follows.

**An everyday picture.** Every entry in a small route ledger balances, but the ledger lists almost every journey separately. That does not give a short rule for a larger network.

## The formal statement and proof

**Finite certificate theorem, second reader pending.** On the clock-aligned root-reached graphs at common caps q1,2,4,8, the exported RC2 certificate supplies nonnegative original vertex potentials h satisfying h(s)>=2*delay(s,t)-5+h(t) on every retained edge, with maxima0,0,1,14 respectively. Therefore every finite path segment remaining in the corresponding reached domain has doubled slope-5/2 reward at most that maximum, by telescoping. The q8 upper budget is14, or7 in undoubled arithmetic. This proves neither minimality nor any uniform all-period bound. A cap exit has reward-5 but the ensuing larger-period stage is outside this certificate.

**Artifact and provenance.** The static artifact `rc2-certificate.json` has56,232 bytes and SHA-256 f8d57126f5601ec41295db803ba13271ac54523e4b39a6c5a749b3f30e76a2a7. Local produced it with exporter commit c5d24a0, after regenerating the arrays because the original RC2 run retained none; L143 records that limitation and matching counts/maxima. The numerical data remains outside Git in the shared scratch. Git holds the producing source, checksum, independent checker and this conclusion. No claimed provenance relies on a flag's note.

**Independent verification of coverage and values.** GPT's `tests/probes/lexicon/rule30_rc2_certificate_check.py` imports no Local code and performs no Bellman iteration, potential search or graph-generation traversal. For each supplied vertex it validates the supplied parent chain to the constant root, and every supplied edge by literal compatibility, rotation and reset scans. It enumerates scalar candidate child words at each supplied state to verify successor closedness against the edge list; reachability plus closedness certifies the exact finite reached graph. A no-child state must be a zero driver with odd source parity, whose cap exit costs0/reward-5. Features use scalar resets, least pair period and independent binomial substitution at X=1 for temporal difference order.

Every K row is nonnegative, every actual consecutive-edge inequality holds, and every edge label is represented, terminal labels included. The G179 lift is computed explicitly and every original edge inequality checked. Confirmed counts (vertices/edges/context labels/actual arcs) are3/2/2/1,9/9/9/9,31/32/32/33,409/411/398/413. Confirmed K and h maxima are0,0,1,14 at the four caps. The checker verifies the artifact's summary against these computed values, not merely its printed assertions.

**Controls retained from G181.** Zero K fails a known positive actual context arc; deleting the known(143,26)->(134,186) edge fails successor closedness. Terminal labels are present. The identified unexpected strict-bound guard passes: q8 hmax14 is strictly below Kmax+11, so the checker does not mistake the reserve bound for an equality. Parent coverage, successor closedness and numerical inequalities all pass separately. GPT Intel static audit CPU0.1287 s/RSS14.4 MiB; Local's regeneration CPU0.01 s/RSS12.2 MiB is a separate run. CV-C1/C2 expectations hold; no failed check or partial stop is counted as a pass.

**Scope and closure of this block.** RC-P1's finite success is now independently verified, while its398/411-label caveat remains unchanged. This does not establish a small context family, bounded degree-independent memory, linear certificate magnitude at unbounded periods, period growth, arbitrary interior clocks or birth-clamped bounds. The gap-1 candidate-refinement loop stops here following CL011's coordination steer. Next GPT work is a reasoning synthesis of the compression failures, then the open period-growth obligation of G165; no new candidate family or larger-period job is launched.
