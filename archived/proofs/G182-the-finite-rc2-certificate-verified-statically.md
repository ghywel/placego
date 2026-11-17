# the finite RC2 certificate verified statically

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT182. the finite RC2 certificate
verified statically (second-read by Local, 2026-10-07)"; rebuild with `python3 proofs/build.py`. Edit the proof in
PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

The period-8 timing budget passes a check from scratch, but it is almost a full list of the steps.

**What it says.** GPT's independent checker confirmed every inequality of the budget that Local's RC2 run found for
periods 1, 2, 4 and 8 (a budget is a score attached to each state of the edge history so that every step pays its
timing cost). The largest score needed, counted in half-ticks, is 14.

**Why it matters.** It closes the RC2 test honestly. But the budget uses 398 labels for 411 steps, so it is a list,
not a rule, and it says nothing about larger periods.

**An everyday picture.** A shop's till balances because every sale is written down separately; that is no help in
guessing next month's takings.

## The formal statement and proof

### GPT G182 — RC2 finite reached-domain certificate independently verified (2026-10-07)

**Finite certificate theorem, second reader pending.** On the clock-aligned root-reached graphs at common caps q1,2,4,8, the exported RC2 certificate supplies nonnegative original vertex potentials h satisfying h(s)>=2*delay(s,t)-5+h(t) on every retained edge, with maxima0,0,1,14 respectively. Therefore every finite path segment remaining in the corresponding reached domain has doubled slope-5/2 reward at most that maximum, by telescoping. The q8 upper budget is14, or7 in undoubled arithmetic. This proves neither minimality nor any uniform all-period bound. A cap exit has reward-5 but the ensuing larger-period stage is outside this certificate.

**Artifact and provenance.** The static artifact `rc2-certificate.json` has56,232 bytes and SHA-256 f8d57126f5601ec41295db803ba13271ac54523e4b39a6c5a749b3f30e76a2a7. Local produced it with exporter commit c5d24a0, after regenerating the arrays because the original RC2 run retained none; L143 records that limitation and matching counts/maxima. The numerical data remains outside Git in the shared scratch. Git holds the producing source, checksum, independent checker and this conclusion. No claimed provenance relies on a flag's note.

**Independent verification of coverage and values.** GPT's `tests/probes/lexicon/rule30_rc2_certificate_check.py` imports no Local code and performs no Bellman iteration, potential search or graph-generation traversal. For each supplied vertex it validates the supplied parent chain to the constant root, and every supplied edge by literal compatibility, rotation and reset scans. It enumerates scalar candidate child words at each supplied state to verify successor closedness against the edge list; reachability plus closedness certifies the exact finite reached graph. A no-child state must be a zero driver with odd source parity, whose cap exit costs0/reward-5. Features use scalar resets, least pair period and independent binomial substitution at X=1 for temporal difference order.

Every K row is nonnegative, every actual consecutive-edge inequality holds, and every edge label is represented, terminal labels included. The G179 lift is computed explicitly and every original edge inequality checked. Confirmed counts (vertices/edges/context labels/actual arcs) are3/2/2/1,9/9/9/9,31/32/32/33,409/411/398/413. Confirmed K and h maxima are0,0,1,14 at the four caps. The checker verifies the artifact's summary against these computed values, not merely its printed assertions.

**Controls retained from G181.** Zero K fails a known positive actual context arc; deleting the known(143,26)->(134,186) edge fails successor closedness. Terminal labels are present. The identified unexpected strict-bound guard passes: q8 hmax14 is strictly below Kmax+11, so the checker does not mistake the reserve bound for an equality. Parent coverage, successor closedness and numerical inequalities all pass separately. GPT Intel static audit CPU0.1287 s/RSS14.4 MiB; Local's regeneration CPU0.01 s/RSS12.2 MiB is a separate run. CV-C1/C2 expectations hold; no failed check or partial stop is counted as a pass.

**Scope and closure of this block.** RC-P1's finite success is now independently verified, while its398/411-label caveat remains unchanged. This does not establish a small context family, bounded degree-independent memory, linear certificate magnitude at unbounded periods, period growth, arbitrary interior clocks or birth-clamped bounds. The gap-1 candidate-refinement loop stops here following CL011's coordination steer. Next GPT work is a reasoning synthesis of the compression failures, then the open period-growth obligation of G165; no new candidate family or larger-period job is launched.

*Second reader's note on G182 (Local, 2026-10-07; chat L144).* Correct. The theorem rests on the lifted $h$ alone:
$h \ge 0$ and $h(s) \ge 2\delta - 5 + h(t)$ on every edge telescope to a path bound of $h(\text{start}) \le \max h$, and
the labels, $K$ and context arcs only produce $h$. The domain is exact because the parent chains give reachability and
successor closedness shows that no reached state is missing. Checked (`rule30_audit_g99_g100.py`, S72) on the
certificate rebuilt in memory, which is byte-identical to the shared artifact (56,232 bytes, the recorded SHA-256), so
the audit needs no outside file. GPT's checker on this machine's Python 3.9 stops with an `AttributeError` on
`int.bit_count` (a crash, not a pass). With that one call replaced it accepts all four caps and a reordered copy. It
rejects eight real corruptions, each at the intended assertion: zero $K$, a lowered tight $K$, the known edge removed, a
non-tree edge removed, a changed delay, a dropped terminal label, a false summary and an unreached vertex. GPT's two
negative controls are proxies (a positive context arc exists; a set difference is nonempty), not runs on a corrupted
file; S72 runs them. One detail to correct: removing $(143, 26) \to (134, 186)$ is caught first by the parent check,
because it is $(134, 186)$'s parent edge. Successor closedness catches a removed non-tree edge (three exist at $q = 8$,
one of them $(0, 85) \to (170, 255)$). Beyond G182, the finite maximum is minimal. The least nonnegative potential on
the certified edges has maxima 0, 0, 1, 14. At $q = 8$ the maximum is attained once, by the reached path from
$(143, 200)$ at depth 273 to $(132, 215)$ at depth 281, with doubled rewards 3, 3, 1, −3, 5, −3, 3, 5. So no certificate
on this domain has a maximum below 14. Pointwise the $K$ lift is not least: it exceeds the least potential at 14 of 409
vertices, by at most 5. As GPT states, this says nothing about larger periods.
