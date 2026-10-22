# RULE30-GPT, volume 4: GC387 to GC548; G208 (2026-10-07 to 2026-10-08)

*A frozen volume of [RULE30-GPT.md](../../RULE30-GPT.md), rotated out of it unchanged on 2026-10-22 in the documentation spring clean. New entries go in the live file; the list of volumes is at its top.*

## GC387 — width15 source audit and the reviewed local identity filed (2026-10-07)

L236 LK source second reading and bounded replication completed. Direct encoding
uses reverse-order integer rows, checks column1's successor explicitly, decodes
columns2..m and deduplicates identical exterior successors. Its simultaneous
trim and singleton-word tests implement the stated complete graph. My own lift
chain reconstructed widths13/14/15 as836/1273/1239 vertices and1174/1810/1760
edges. Every retained edge agrees with a literal scalar Rule30 update. Both
reported column5/6 words reproduced exactly. Expected controls PASS; no rerun
of Local's widths16..18 or the complete million-state width15 graph.

Unexpected radius audit: LK's96-round loop tests ONLY column5. Therefore193
observations certify column5 at the centre; that loop alone does not certify
column6 there. Full width15 stabilization is Local's reported110 rounds, giving
221 rows for all core-forced columns; my cumulative lift bound is151 rounds,
giving an independently derived sufficient303-row bound, not a new minimum.
L237 subsequently reports separate column6 radius102, giving205 rows. These
statements have different premises and must not be collapsed into a193-row
claim about every column2..6. Eventual forcing for an infinite forward strip
follows after entering the finite core and does not prove such a strip exists.

L237 verified: GC385's local identity and conservative145-row transfer second-read.
Filed that identity verbatim as PROOFS G207, with its scope and premise control;
nearest G142,14,C1 read and distinguished, and G205 cited rather than duplicated.
The measured width15 certificate is audit-ready for a separate master filing;
its word/radius statement and finite-window bounds must be written separately.
Source execution used the existing core/lift functions, transcript outside Git.
CL031 read: the finite last-witness comparisons do not exclude other periods
or a different eventually periodic object farther right; no such universal
exclusion is inferred from the phrase 'nothing beyond6 repeats'.

### G208 — Computed width15 forcing next to the recorded wheel (2026-10-07)

**Provenance and scope.** Local's RV2 and LK (`rule30_locked_core_review.py`,
`rule30_locked_core_lock.py`, L236 at f127657) find the exact width15 core by a
direct reverse-bit-order encoding. GPT's GC387 independently executed the
previously validated core lift through widths13..15, reproducing the core counts,
edges and words and checking every retained edge by scalar Rule30 evaluation.
The setting is column0(t)=t mod2 and column1(t)=U((t-d) mod56), with d even and
U the recorded wheel. Exterior column16 is unrestricted. This is a computed
finite certificate with a soundness argument, not a prize solution.

**Computed core.** Width14 has1273 vertices and1810 edges and still fixes only
columns2..4. Width15 has1239 vertices and1760 edges and fixes columns2..6 at
all56 phases. Columns2..4 have G205's words; the additional words, from phase0,
are

    column5: 10000001011000000101100000010110000001011010101110000101
    column6: 00111111000011111100001111110000111111010110100101111100

**Exactness of the lift.** For a finite phase graph, simultaneous in/out trimming
keeps exactly the vertices on bi-infinite walks. Every wider such walk projects
wholly into the narrower core. Add both choices of the next column bit above
every old core vertex; keep edges only when the old final column updates with
that specific new bit and the new column updates with some free exterior bit.
A surviving lifted walk is a valid wider walk, and every wider core walk lifts.
Thus trimming this graph gives exactly the complete wider core, including
bridges between recurrent components. Direct RV2/LK vertex AND edge comparisons
agree with the lift at widths13,14,15. GPT replication independently reproduces
those counts, both words, and literal retained-edge tests at all three widths.

**Finite forcing.** G205's path induction transfers singleton survivor bits to
an actual strip vertex whose distances from the two endpoints are at least
the number of trimming rounds. Local's complete width15 calculation finds
column5 single-valued at every phase after96 rounds. Consequently193 consecutive
wheel observations force column5 at their centre to its displayed word's bit.
That96-round test concerns column5 alone, not column6.

An independently derived sufficient bound for all columns2..6 uses the lift
rounds: width12 stabilizes after71; the successive lifts13,14,15 need15,12,53
rounds. Projection under simultaneous trimming puts complete wider survivors
inside the narrower core before the extra lift rounds, so complete width15
stabilizes by at most151 rounds. Hence a303-observation wheel window forces
columns2..6 at its centre. This conservative bound is not minimal. Local reports
complete stabilization after110 rounds and separate earlier bit radii, but
those sharper counts are not required for the303-row conclusion.

**Infinite forward consequence and boundary guard.** If the wall-compatible
wheel persists on a forward ray, every time at least151 steps after its start
has a303-row window inside that ray, so columns2..6 then follow the fixed words.
The transient prefix is not claimed forced. A nonempty relaxed core or a periodic
strip with free exterior does not prove that an actual global right half can
follow the wheel forever. No column beyond6, spatial growth rate or finite-left
prize conclusion follows. The width13 replacement word1 is compatible at that
width but cannot extend as such through the width15 constraints.

**Controls and retained limits.** Local's direct encoding and GPT's lift are
independent graph constructions; GPT's new execution of the lift reproduces
reported outputs, not a third independent encoder. No GPT rerun of Local's
widths16..18 or complete million-state width15 graph is claimed. The193-row
column5 radius is Local's checked source and reported computation, not a fresh
GPT replication of the96 full trimming rounds. G207 explains the earlier paired
ambiguity, while this certificate settles its common value only under the wider
constraints.

### GC401 — Two unconditional four-update black-output patterns (hand proof proposed)

Setting: Rule30 update x'_j = x_(j-1) XOR (x_j OR x_(j+1)). Positions1..9 below are a translated local interval, not an assumption of a prescribed wall. All unspecified initial cells are arbitrary. Independent second reading pending.

Claim: after four updates, position5 is1 if initially either (A) positions1..7 are0101110, or (B) positions1,2,3,4,6 are1,1,1,0,1 (position5 and positions7..9 arbitrary). This is a local lemma; no wheel, long preparation or prize statement.

Proof A: let initial positions8,9 be d,e. After one update, positions2..8 are1,0,1,0,0,1-d,d OR e. After two, positions3..7 are0,1,1,1-d,1: the last entry is (1-d) OR d OR e. After three, positions4..6 are1,0,0. Hence the fourth update at5 is1 XOR (0 OR0)=1.

Proof B: write initial position5=b, a=x7 OR x8, q=x7 XOR (x8 OR x9). After one update, positions2..8 are0,0,1-b,1,1-b,1-a,q. After two, positions3..7 are1-b,1,b,b AND a,z, where z=(1-b) XOR ((1-a) OR q). After three, positions4..6 are b,1-b,b XOR ((b AND a) OR z). If b=0, the first two entries are0,1 and the next output is1 regardless of the third. If b=1, z=(1-a) OR q, so (b AND a) OR z = a OR (1-a) OR q =1 and the third entry is0; the first two are1,0, again giving output1. This proves B.

Controls: all20 assignments to the free positions of these two nine-cell patterns scalar-evolved to output1. Radius-one locality uses only positions1..9, so no wall value or exterior enters this four-update proof. The earlier eight wall values are needed to establish the reached cut restrictions from GC397's initial anchor, not for this local lemma.

Connection: GC400's32 reached time8 rows satisfy a seven-clause correlation certificate. With their antecedent x6=1, those clauses imply either pattern A or B. Reachability of the certificate is still established by the finite census, not by this short hand proof. A second reader is requested for the hand lemma and the separation of these obligations.


GC401 review receipt (2026-10-08): Local L244 at48480a9 second-read both hand cases line by line and independently checked all20 assignments. GPT replay of Local's gc401 mode PASS:1504 of4096 anchored runs have the antecedent and all1504 match A or B. Filed the unconditional lemma verbatim as G209, retaining the original pending sentence with a dated review resolution. The direct bridge is still computed; the seven-clause abstraction is optional, not necessary to this proof decomposition.

### GC403 — A short time4 anchor relation loses essential correlations (2026-10-08)

Preregistered P1: the time4 relation derived below alone forces every time8 row with column6=1 into G209's A or B, confidence0.5. Counterfactual: the initial anchor retains omitted correlations. No wall or width sweep.

Let a be initial column1 under GC397's anchor2..6=11100 and alternating wall. Direct scalar updates give:

    time1 columns1..5: 1,1-a,0,0,1
    time2 columns1..5: 0,a,1-a,1,1
    time3 columns1..5: a,1,1-a,a,0
    time4 columns1..6: 0,1-a,0,1,h,k
    h=a XOR v, k=v OR w; v=column6(time3), w=column7(time3).

All4096 original assignments verify this relation. It allows six triples(a,h,k), not eight; however freeing everything to its right admits768 time4 rows on columns1..13. After four updates392 have the antecedent and28 fail both A and B. P1 REFUTED. Scalar and packed Rule30 expressions agree at every step. Unexpected release of h,k independently admits1024 rows,512 positive and84 failing the cover: the relation helps but does not suffice.

A retained failing time4 row on columns1..13 is0001101000100; its time8 columns1..9 are010111110. Post hoc scope control (not preregistered): all28 restricted cover failures also evolve to column5=0 at time12. Thus the shortcut fails the anchored implication itself, not merely the chosen sufficient-pattern cover. This is not a counterexample to GC397: these relaxed rows cannot have the entire prescribed earlier history. The missing information sits in correlations with the omitted exterior, not in an erroneous four-update hand lemma.

Instrument: tests/probes/lexicon/rule30_gpt_gate_bridge.py, under0.1 seconds. Transcript outside Git. Stop this time4 shortcut; next inspect which earlier exterior relation excludes the retained failing row, or use a distinct open reasoning lead if no short invariant emerges. No long preparation, death127 or prize conclusion.

### GC404 — One exterior constraint repairs only part of the shortcut (2026-10-08)

P1 preregistered: a single necessary one-update exterior condition excludes all28 GC403 failures (0.6). Counterfactual: excluding the first witness does not repair the entire bridge. With time3 column5=0, let v,w,z,u be columns6..9. Time4 columns6..8 are k=v OR w, l=v XOR(w OR z), r=w XOR(z OR u). Hence k=0 implies v=w=0 and l=z<=z OR u=r. This is a hand-derived necessary condition.

Adding only k=0 implies column7<=column8 to GC403's time4 relation removes12 of28 failures, including the first retained witness. P1 REFUTED:704 relaxed rows remain,328 have the antecedent and16 still fail A/B. The first remaining time4 row on1..13 is0001110010000. All4096 original assignments and16 local input choices satisfy the condition; scalar/packed controls PASS. Unexpected check counts every failure rather than declaring success after excluding one row.

Premise-negative local control: dropping time3 column5=0 permits inputs(column5,v,w,z,u)=(1,1,0,0,0), giving next columns6..8=0,1,0. Thus the inequality is conditional, not an unconditional Rule30 law. This local control makes no wall-compatible trajectory claim.

Instrument: tests/probes/lexicon/rule30_gpt_gate_exterior.py, under0.1 seconds; transcript outside Git. No full symbolic bridge or death127 result. Next consider the complete one-update relation from time3 column5=0, rather than collecting individual clauses without an explanatory invariant. Stop if it merely expands into another reachability table; colleague KC, RR, KT2 remain separate.

### GC405 — Complete local image closes the bridge; hand proof proposed (2026-10-08)

P1 preregistered: the complete one-update image of time3 columns1..9=a,1,1-a,a,0,v,w,z,u suffices for the time8 A/B cover (0.6). It HELD:18 distinct(a,h,k,l,r) states yield576 time4 completions,232 antecedent-positive, zero cover failures. Every original4096 run lies in this image; independent reverse-bit steps agree with scalar. Unexpected exactness check: the image equals GC403's relation plus GC404's inequality plus(h=a and k=1 implies l=1). No further clauses needed.

**Proposed hand bridge.** Assume time3 columns1..5=a,1,1-a,a,0 and wall0(t)=t mod2 through time7. All right exterior cells are arbitrary. Then if column6(time8)=1, time8 matches G209 A or B. The following proof is proposed for independent second reading, not yet catalogued.

Time4 columns1..8 are0,1-a,0,1,h,k,l,r, where

    h=a XOR v, k=v OR w, l=v XOR(w OR z), r=w XOR(z OR u).

If a=0, time5 columns1..4=1,1,0,1; time6 columns1..4=0,0,0,1; time7 columns1..4=0,0,1,1. Consequently time8 columns1..4=1,1,1,0, independently of all later entries. With antecedent1 this is B.

Let a=1. Put H=1-(h OR k), K=h XOR(k OR l), L=k XOR(l OR r), R=l XOR(r OR s), where s is time4 column9. Time5 columns1..8=0,0,1,1,H,K,L,R. Since h=1-v and k=v OR w, H=0. Put J=1-K, M=K OR L, N=K XOR(L OR R), and let O be time6 column8. Time6 columns1..7=1,1,1,0,J,M,N. Time7 columns4..7 are

    P=1-J, Q=J OR M, V=J XOR(M OR N), W=M XOR(N OR O).

The time8 antecedent is F=Q XOR(V OR W). If K=1, then J=0,M=1,V=1,Q=1, so F=0. Thus F=1 requires K=0. Now J=1,M=L,N=L OR R,Q=1,V=1-(L OR R). F=1 requires V=W=0. If L=0, V=0 forces R=1, but W=R OR O=1, contradiction. Hence L=1.

K=0 implies v=0: if v=1 then h=0,k=1,K=1. With v=0 we have h=1,k=w,l=w OR z and K=1 XOR(w OR z); thus w OR z=1. If w=1 then k=l=1 and L=0, contradiction. Therefore w=0,z=1, giving h,k,l,r=1,0,1,1.

Write S for time5 column9 and Y for time5 column10. In this branch time5 columns5..9=0,0,1,0,S. Time6 columns5..9=1,1,1,1-S,S OR Y. Therefore time7 columns4..7=0,1,0,0 and column8=1 XOR((1-S) OR(S OR Y))=0. Updating once more gives time8 columns1..7=0,1,0,1,1,1,0, namely A. This proves the proposed bridge.

**Anchor connection.** GC403's first three hand updates derive this time3 prefix from initial2..6=11100, with initial1=a, under wall times0..2=0,1,0. Combining that propagation, the proposed bridge, and independently reviewed G209 proves GC397's anchored implication without a reachability census, if the new hand case analysis receives second reading. The576/4096 computations are controls, not substitutes for the displayed proof. Eight wall values0..7 remain premises; no wall is needed for G209's last four steps. No long wheel preparation or death127 conclusion.

Instrument: tests/probes/lexicon/rule30_gpt_gate_image.py, under0.1 seconds. GC403 and GC404 failures retained. Next independent review of this hand bridge; no further relational, wall or width sweep.

GC405 resolved review (2026-10-08): Local L245 at shared main a9b5fde rederived every update, the a=0 and a=1 cases, and the initial anchor propagation by hand. Its separate controls cover1024 arbitrary time3 rows,408 with antecedent, and128 anchor completions; GPT replay PASS. Filed bridge and anchored implication as G210 with G209 cited. Reachability census is now a control, not an outstanding proof obligation. No death127 or prize result.

### GC407 — G210 forces one front defect, without a self-renewing anchor (2026-10-08)

Prediction: under the reported anchor at s-14, G210 and observed column5(s-2)=0 force column6(s-6)=0. Hand translation sets G210 time0=s-14, time8=s-6 and time12=s-2. G210 excludes(1,0), hence the conclusion by contraposition. No other tail observations, initial column1, or distant exterior choices enter. The alternating wall starts white because s-14 is even in the normalized recorded witness. Initial columns2..6=11100 at that time were independently verified in L240/L242.

The reference phase at s-14 is54. Its reference pair(column6(s-6),column5(s-2)) is(1,1), whereas the observed pair is(0,0). Thus the later column5 defect forces this particular earlier column6 defect under the short anchor. This is a logical dependency through a forward implication, not backward physical propagation. It does not explain the first column6 defect at s-13.

Tiny reference audit: even phases with spatial2..6=11100 are8,18,28,38,54. Their reference eight/twelve-step pairs are(1,1),(1,1),(1,1),(0,0),(1,1), all satisfying G210. Independent indexing by zipped spatial words agrees. Unexpected composition check: twelve steps after these anchors, spatial2..6 is01110,01110,01110,00101,01110; none is11100. Even the exact reference does not regenerate the same anchor at the end of the implication. Therefore this lemma alone is not a repeatable twelve-step barrier or a preparation-length bound. This check excludes that particular immediate iteration, not every conceivable composition.

Counterfactual that G210 alone fixes the whole exterior path is unsupported: at GC393's relaxed-path level, fixing6(s-6)=0 leaves eight histories. The full GC395 preparation census selected one; these eight are not asserted globally extendable. No census rerun and no new uniqueness claim. Existing failures GC403/GC404 and proofs G209/G210 remain distinct. Instrument tests/probes/lexicon/rule30_gpt_gate_application.py, under0.1 seconds; transcript outside Git.

Next main-line reasoning should seek an anchor-renewal mechanism or a different open lead, rather than more finite completion variants. KT2L, KC and RR stay colleagues' computational lanes.

### GC408 — RR scope and a blocked imported-threshold application (2026-10-08)

L247 and RR source read, RR2 stays Local. Write E(d,L) for an initial row with zero cells at depths d..d+L-1 and alternating column0 through T=d+L-1, exactly RR's stated finite-cone predicate. Every genuine infinite alternating-wall configuration restricts to an E(d,L) witness whenever it has that zero block. Thus UNSAT soundly excludes such a block in any infinite extension. A SAT cone, even when its zero-padded finite seed replays the finite trace, does not assert that the same seed keeps alternating forever. This is a scope clarification of the source's finite predicate, not a correction of Local's solver or numerical counts.

**Useful target from the existing ladder principle.** It suffices to prove that arbitrarily large depths d each have some finite L(d) with E(d,L(d)) impossible; no uniform bound20, linear growth estimate, or decision at every depth is logically required for this sufficient criterion. For a hypothetical finite-left-support alternating-wall seed, choose such a d beyond its leftmost black cell: all d..d+L(d)-1 cells are zero, contradicting that exclusion. An eventually alternating wall can be rebased to its onset; a finite initial seed still has finite left support then. This does not supply the unbounded-depth theorem. Finite measured depths through81 cannot replace its cofinal quantifier. The argument applies even when the hypothetical right half is infinite, a stronger class than finite full seeds. This is elementary use of the ladder/finite-support reduction in sections8.11 and8.62, not a novelty claim.

**Unexpected compactness qualification.** For fixed d, if E(d,L) is SAT for every L, its closed cylinder conditions on infinite binary initial rows form a nested nonempty family. Binary-tree compactness then gives a single infinite initial row, zero at every depth>=d, whose wall alternates forever (one of the two phases). Its right half can be infinite. The property 'finite full support' is not preserved by this limiting argument; zero-padding each finite witness does not fix one common support bound. No finite-seed prize counterexample follows from SAT at all finite horizons.

**Toolkit application attempt retained.** Imported175c is trusted at catalogue level A, with its increasing-family hypothesis. RR's membership event is not increasing in initial black cells, even with the initial wall bit and white block fixed. For d2,L1,T2, phase0, row on-2..2=01000 has wall trace010. Adding black at+1 gives01010 with trace000, so membership is lost. Conversely00000 fails and adding black at-1 gives01000 and passes. All8 free assignments agree under scalar XOR-OR and independent literal Rule30 table. Thus the family is neither increasing nor decreasing. Directly applying175c to these initial-row events is blocked by a proved missing hypothesis, not by doubt about Cloud's imported theorem. An upward closure would contain invalid wall witnesses; any useful monotone certificate family needs a separate construction and soundness argument.

Instrument tests/probes/lexicon/rule30_gpt_records_scope.py, under0.1 seconds, transcript outside Git. No SAT run, RR2 duplicate, general record bound or new catalogue entry. Next reasoning question: a composable obstruction family at cofinally many depths, preserving actual local dynamics rather than pretending the initial-row event is monotone.

### GC409 — Open zero-block precursors are rigid, but do not strengthen RR alone (2026-10-08)

Existing record: G105 proves the whole-ring zero-row precursor rigidity, including asynchronous scope; G121 explains finite-root failure of predecessor descent. The following is their synchronous finite-open-block counterpart, not a novelty claim or an all-depth exclusion. Proposed local proof awaits independent reading.

**Claim.** L consecutive zero outputs of synchronous Rule30 have exactly four input words on their L+2-cell backward interval:

    0^(L+2), 1^L01, 1^(L+1)0, 1^(L+2).

**Proof.** Index the old input0..L+1 and new zero outputs1..L. Each equation is x_(j-1)=x_j OR x_(j+1). If x0=0, the first equation gives x1=x2=0; induction gives every input zero. If x0=1 and a first zero occurs at i<L, then i>=1 and equation j=i+1 forces x_(i+1)=0; equation j=i now says x_(i-1)=0, contradicting its being1. Thus x0..x_(L-1) are all1. The remaining equation j=L requires(x_L OR x_(L+1))=1, giving terminal pairs01,10,11. Every listed word satisfies every equation, proving necessity and sufficiency for all L>=1.

Preregistered controls L1..8 inspect2040 inputs, scalar XOR-OR versus independent decoded Rule30 truth table: exactly4 precursors at each length. Unexpected endpoint guard retains both nonconstant terminal patterns. A claim that the entire precursor interval is constant would be false: the last two cells are essential open-boundary exceptions.

**Application failure / scope.** RR pins a zero block at time0, not in the output of an assumed earlier finite row. Introducing all four permitted unrestricted precursor branches alone supplies no additional obstruction: each zero block has these local predecessors, and full-shift predecessor existence does not enforce finite support. Dropping the black-prefix branches to insist on a finite-left-support predecessor would require a separate premise. G121's single black cell is already a finite root: every nonzero finite image has span at least3, so that seed has no finite predecessor. Its unrestricted infinite predecessors cannot be silently substituted for finite-seed history. Hence this local rigidity is usable at genuinely updated rows, but does not justify a new RR initial-row constraint or the cofinal exclusion target of GC408.

Instrument tests/probes/lexicon/rule30_gpt_zero_block_precursors.py, under0.1 seconds; transcript outside Git. No SAT run, no RR2 duplication, no new cofinal bound. Next reasoning should retain actual time or ancestor membership in any certificate chain; stop if a proposed relation is merely another form of the known finite-root descent.

GC409 resolved review (2026-10-08): Local L248 at495f2ab checks the proof and L1 endpoints, and gives an equivalent direct right-to-left inversion from each of the four boundary pairs. The count itself is general left permutivity; the zero word's precursor shapes are the specialized content. Filed as G211, with scope and no-novelty guard. GC408 finite-horizon/cofinal target accepted; RR2 values through66 remain Local measurements, not an unbounded-depth proof.

### GC411 — Owner-requested Navier-Stokes translation audit (2026-10-08)

**Sources and bounded scope.** Read the concrete comparisons in sections3.1–3.2 of [Bastounis, Circelli and Hansen](https://arxiv.org/html/2610.08144v1), then checked [OpenAI Lemma8.6 and equation10.19](https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf) against the cited fixed Lean commit f9e8bc5. This is a source and local mathematical audit, not compilation or a full blow-up proof review. The critique explicitly does not decide whether the prose proof is correct. No toolkit import or Cloud verification is revoked by this audit.

**Confirmed mismatch.** The prose inverse estimate requests m+4 torus derivatives; [norm_derivativeWord_inverse_le](https://github.com/openai/NavierStokesAndEuler/blob/f9e8bc5b38b6e212696e8a30e3e91517af887bbd/NavierStokes/SmoothFamilyTorusInverse.lean#L1059-L1080) bounds pure coordinate input jets at w.length+5. The cited formal declaration therefore does not certify that precise stronger estimate. The pressure-flux [formal bound](https://github.com/openai/NavierStokesAndEuler/blob/f9e8bc5b38b6e212696e8a30e3e91517af887bbd/NavierStokes/R3/PressureFlux.lean#L576) contains a dissipationRoot term as well as cutoffL6, whereas prose10.19 expresses the bound using B_R alone. Different statements must be distinguished from false statements, and a different valid argument can still prove the intended final theorem.

**Independent hand check of the four-derivative estimate.** Set v=(sqrt2-1,1) and k=(a,b), nonzero integer pair, r=max(abs(a),abs(b))>=1. The product of v dot k=sqrt2*a+(b-a) with its conjugate is the nonzero integer (b-a)^2-2*a^2: if a=0 it is b^2>0; if a is nonzero equality would make sqrt2 rational. Consequently 1/abs(v dot k) <= abs(b-a-sqrt2*a) <= (2+sqrt2)*r.

For a smooth periodic F, integrate its Fourier coefficient m+4 times in a coordinate whose frequency has magnitude r. Periodicity cancels the boundary terms, giving abs(Fhat(k)) <= (2*pi*r)^(-(m+4))*norm(F,C^(m+4)). An output derivative of total order n<=m multiplies the inverse coefficient by at most (2*pi*r)^n, with a further inverse divisor factor bounded above by a constant times r. Thus each differentiated term is bounded by a constant depending on m times norm(F,C^(m+4))*r^(-3). The max-norm shell r has exactly8*r lattice points. The total majorant is8*sum r^(-2), finite. Uniform absolute convergence bounds every derivative through order m; using arbitrary m gives smoothness. The zero mode is set to zero, and every nonzero multiplier is nonzero, giving uniqueness among zero-mean solutions. This verifies the estimate component by ordinary Fourier reasoning; it does not audit the rest of Lemma8.6 or the construction.

**Controls and retained failure.** Prediction was registered in CLOUD-LOCAL before this check. Direct enumeration versus shell formula agrees exactly for64 shells; decay3 majorant partial sum13.0354440112711. Unexpected check: replacing the four input derivatives with three gives only r^(-2), hence shell sum8*sum1/r, divergent. This absolute-majorant argument then fails; that is not a proof that a sharper operator estimate is false. Transcript outside Git. No experiment on PDE solutions, no Lean compilation, no prize claim.

**Application to our work.** Maintain the boundary between a correct certificate and its asserted meaning: GC408's finite-horizon SAT does not certify an infinite orbit, and G211 does not certify initial finite ancestry. Accept imported tools at their recorded review level, while checking that our hypotheses and conclusions actually match. The paper's broad computability discussion has not been independently audited here; it is unnecessary for this concrete conclusion.

### GC412 — Toolkit119 gives marginal ceilings, not a trace decomposition (2026-10-08)

**Scope and prediction.** Imported119 is accepted at recorded level B; its checked domain includes every n3 Boolean function. Use that finite domain to audit an application to Q1, without revisiting Cloud's verification. No comparable application or synergy argument found in the existing GPT record. Preregistered in CLOUD-LOCAL: successive fair-row observations are independent unconditionally but not conditional on a noisy initial row at noise1/4. Predicted positive joint-minus-marginal information, with zero at noise0 and1/2 as an unexpected endpoint check.

Let X=(a,b,c) be independent fair bits at positions-1,0,1. The first two centre observations are F0=b and F1=a XOR(b OR c). Let Y be X passed through independent bit flips with probability q. These are actual successive synchronous observations, not a replacement noise process inside Rule30. Since a is a fresh fair pivot, F1 is fair independently of (b,c), so F0 and F1 are independent.

**Hand identity and strictness.** Entropy expansion gives

    I((F0,F1);Y) - I(F0;Y) - I(F1;Y)
      = I(F0;F1 given Y) - I(F0;F1)
      = I(F0;F1 given Y) >= 0.

At q=1/4, conditional on Y=000, a,b,c are independent Bernoulli(1/4). If b=1, F1=1-a and P(F1=1)=3/4; if b=0, F1=a XOR c and P(F1=1)=3/8. Both b cases have positive probability, and Y=000 has probability1/8. Thus F0 and F1 are not conditionally independent, so the conditional information and displayed gap are strictly positive. This establishes the sign without relying on rounded entropy computations.

**Finite controls.** Exact rational probability tables enumerate8 initial words and8 flip masks per q. XOR-OR agrees with the independent decoded Rule30 table. Direct relative-entropy computation agrees with the entropy chain and conditional-information identity. At q=1/4, I(F0;Y)=0.18872187554086717, I(F1;Y)=0.07223675472190724, joint=0.3058658118488182 bits; gap=0.04490718158604379 bits. All four observation pairs have probability1/4. Unexpected endpoints: q0 gives marginal1,1 and joint2; q1/2 gives all information0. Both gaps are0. Controls PASS. Instrument tests/probes/lexicon/rule30_gpt_toolkit_information.py; probability transcript outside Git.

**What fails and what remains.** Summing actual marginal information values as though they equalled or upper-bounded the trace information is false even for two genuine Rule30 observations. Imported119 correctly bounds each individual readout by1-h(q), but does not bound the missing conditional term by that argument: conditioning on another observation destroys the uniform-input premise. This example does not refute a possible two-bit ceiling2*(1-h(q)); indeed its measured joint information is below that ceiling. Proving such a ceiling requires a separate vector/conditional argument. Nor does a noisy fair-ensemble information ceiling force deterministic count loss or exclude one selected seed. Q1 remains OPEN; useful application guard, no new prize theorem.

### GC413 — Fresh pivots prove a vector noise ceiling without a marginal shortcut (2026-10-08; second reading requested)

**Existing basis and prediction.** G97's reviewed fresh-pivot argument makes fixed-centre observations of an iid fair initial row iid fair. GC412 shows actual marginal information does not sum to the trace information. The positive follow-up, preregistered in CLOUD-LOCAL, uses conditional entropy of the fresh initial pivots instead. This proves the candidate vector ceiling in this special dynamical setting by elementary reasoning; it does not upgrade imported119's general level-B theorem.

**Claim.** Let X be iid fair on the initial cone[-(T-1),T-1], let F=(F0,...,F_(T-1)) be the centre samples of synchronous Rule30 at times0..T-1, and let Y be those initial bits independently flipped with probability q,0<=q<=1. With h(q) the binary entropy,

    I(F;Y) <= T*(1-h(q)).

If G is the same centre trace obtained by evolving initial row Y, then also

    I(F;G) <= I(F;Y) <= T*(1-h(q)).

**Proof.** Left permutivity under iteration gives F_t=X_(-t) XOR g_t of the other initial cone bits. No earlier F_s uses X_(-t), because its leftmost input is at-s>-t. Let E_t be the vector of all initial cone bits except X_(-t). Then the earlier observed prefix is determined by E_t. Conditional on Y and E_t, the pivot still has its binary symmetric-channel posterior: its probability of disagreeing with Y_(-t) is q. Indeed the original bits and channel noises are independent, and observing all other inputs or their noisy copies provides no information about this pivot beyond Y_(-t). Once E_t is fixed, g_t is fixed; XOR does not change entropy. Therefore

    H(F_t given F_<t,Y,E_t)=h(q),
    H(F_t given F_<t,Y)>=h(q).

Summing the conditional-entropy chain yields H(F given Y)>=T*h(q). G97's independent fresh fair pivots give H(F)=T, proving the first bound. G is a deterministic function of Y, so data processing gives the second. Endpoint q0 or q1 yields an invertible input channel and q1/2 an independent one; the proof includes them. This is a fair-input ensemble theorem, not a statement about a fixed initial seed, repeated asynchronous races, or noisy updates introduced during evolution.

**Controls and unexpected check.** Exact rational input/mask tables for T1..4 and q0,1/4,1/2 give12 passing cases. Independent literal versus XOR-OR evolution agrees; trace marginals are exactly uniform. Relative-entropy versus entropy-chain controls agree within1e-12. At q1/4 the full-input information for T1..4 is0.188721875541,0.305865811849,0.409959079384,0.508011779645 bits, below ceilings0.188721875541,0.377443751082,0.566165626623,0.754887502163. Unexpected second-copy check gives0.188721875541,0.276579827772,0.345309580017,0.400009225752 bits, all below the corresponding full-input information. Endpoint q0 gives exactlyT and q1/2 gives0. The earlier two-observation synergy remains; this ceiling is established despite it, rather than by discarding it. Instrument tests/probes/lexicon/rule30_gpt_noise_vector.py; transcript outside Git.

**Scope and next step.** This supplies a sound multibit analogue for this fresh-pivot trace and links the imported information toolkit to an actual Rule30 observation process. It still supplies an ensemble ceiling, not Q1's single-orbit lower bound on distinct window contents or a cofinal obstruction. Request an independent hand second reading before filing; Q1 remains OPEN.

GC413 resolved review (GC414,2026-10-08): Local L249 at4365e6d checks all hand steps, including the fair-input posterior premise, and independently reproduces12 cases. Filed G212 verbatim with that premise emphasized. Actual nearest G108,G119,G205 read in full and distinguished; no new general information theorem or selected-seed complexity claim.

### GC415 — A critical step need not repair a generic absorbing-edge defect (2026-10-08)

Distinct main-line follow-up to Collatz critical-boundary count loss. Read G91-G95 and Local L048's real-schedule failure before proposing a shape repair. No actual demand sweep repeated. G95's isolated-flat schedule condition might suggest that an adjacent critical step washes out G94's edge defect. The following exact synthetic guard rules out that generic induction from log-concavity alone. It does not settle the shape of the actual demand laws.

Index an input probability law q by excess demand j>=0, with missing entries zero. A flat threshold step B folds the fair decrement at zero:

    (Bq)_0=q_0+q_1/2,
    (Bq)_j=(q_j+q_(j+1))/2 for j>=1.

A critical threshold step C adds a fair Bernoulli increment:

    (Cq)_0=q_0/2,
    (Cq)_j=(q_(j-1)+q_j)/2 for j>=1.

These follow by conditioning on the first fair bit in J=max(0,d-bit+J_suffix), d0 or1. Thus prefix10 applies C B to the suffix demand law; this has no adjacent flat steps. Ordinary C alone preserves log-concavity, but C B need not.

**Hand counterexample.** Take q_j=10^j/11111 for j0..4 and zero elsewhere. It is log-concave with connected support: all its nontrivial interior inequalities are equalities. After B then C the first four masses have numerators12,122,1210,12100 over44444. At j2,

    1210^2 - 122*12100 = -12100 < 0.

This is an interior log-concavity failure, not the original edge triple. The critical step therefore can move a generic edge defect into the interior rather than repair it. The input distribution is synthetic and is not claimed to be a suffix law generated by the Collatz threshold schedule, so it does not contradict Local's absence of interior violations in actual profiles.

**Controls and unexpected check.** Prediction and counterexample registered in CLOUD-LOCAL before the rational control. Independent explicit branching sends each mass at j to max(0,j+d-bit), each bit with probability1/2. It reproduces all displayed masses, preserves total1, and gives deficit-12100/44444^2 exactly. Unexpected critical-only guard Cq stays log-concave. Transcript outside Git. No fitted shape rate, actual population, new sweep or count theorem.

**Consequence.** A future proof of the actual near-edge shape needs more than “log-concave future law plus isolated flat steps”; even a two-step restoration shortcut is unavailable at that level of abstraction. Actual signed allocation in G91 remains the main gap. This closes only the named generic repair, leaving the actual threshold law and count-loss row PART.

### GC416 — Cumulative parity allocation pairs with demand gradients (2026-10-08; hand review requested)

**Question and prior scope.** G74's exact signed demand sum and G91's unmatched allocation remain available after GC415's generic shape repair fails. Existing record searched for Abel summation or cumulative parity imbalance; no such formulation found. The following is ordinary finite summation by parts applied to G74, without a novelty claim. It names a different actual allocation object, not a new fairness assumption.

At fixed t and final T, write I_a=I_w(t,a) and d_a=Delta_t(a), extending both by zero outside their finite support. Set B_a=sum_(b<=a) I_b; include its zero left tail and constant right tail. Then the exact increment is

    H_(t+1)-H_t = (1/2)*sum_a B_a*(d_a-d_(a+1)).

Proof: substitute I_a=B_a-B_(a-1) in G74 and shift the second finite sum. The lower support jump must be retained. The gradient coefficients sum to0, so one may subtract any constant from B. Choosing the midpoint of its maximum and minimum gives

    abs(H_(t+1)-H_t) <= osc(B)*TV(d)/4,
    osc(B)=max_a B_a-min_a B_a,
    TV(d)=sum_a abs(d_a-d_(a+1)).

Telescoping yields the sufficient bound abs(C_w(T)-Q_w(T)) <= sum_(t=m)^(T-1) osc(B_t)*TV(Delta_t)/4. No unimodality or log-concavity is needed; full demand variation includes every interior reversal and both endpoint jumps. Actual signed cancellation may be retained in the identity rather than bounded by the oscillation. A uniform ratio would still require this sum to be O(Q_w(T)), or a sharper signed estimate; neither is proved here.

**Controls and retained scope.** Preregistered reuse of widths2..5,horizons m..9 checks100 exact increments, retaining21 empty-parent cases. The Abel sum, original weighted sum and literal backward-weighted H increments agree. Range bound and zero-sum gradients PASS. Unexpected synthetic guard I=(1,-1), d=(3/4,1/4) has zero total imbalance yet contribution1/4: knowing total parity balance alone is insufficient. A single demand spike has total variation2, including its lower jump; omitting that jump would break the centered bound.

The new absolute bound is not uniformly better than G74's: with synthetic I=(1,1) and d=(1,0), it gives1 versus the original absolute bound1/2. Those are algebraic guards, not actual population laws. Any advantage must come from the actual prefix allocation and demand placement, not the coordinate change itself. Instrument tests/probes/prizes/collatz_gpt_prefix_allocation.py; transcript outside Git. No larger start scan, actual-law shape sweep or asymptotic fit. Collatz critical-boundary count loss remains PART; review the identity and boundary convention, then target actual prefix allocation.

GC416 resolved review (GC417,2026-10-08): Local L250 at3a54850 checks Abel summation, full boundary convention, centering and both guards. Filed G213 verbatim; actual nearest G74,G77,G92 read in full. No uniform estimate follows; the actual allocation target remains open.

### GC418 — The coarse prefix-range bound loses in all seven preregistered actual cases (2026-10-08)

G213's identity remains sound, but its range-times-variation estimate needs a practical check before further development. Preregistered widths2..8 at T=8*m,m=w-1, with exactly seven cases and no rate fit. Blind prediction: at least one actual case improves on G74's original absolute weighted imbalance sum. This prediction is REFUTED in the stated scope.

Ratios of the new total bound to the old total bound at widths2..8 are respectively1.263157895,1.406967937,1.934035315,1.751903299,1.713561807,1.252198858,1.776800519. Every ratio exceeds1. All original signed increments agree exactly with the literal backward-weighted H increments, and the final signed sum equals C-Q. Both absolute bounds hold. Controls PASS; the failed prediction is retained rather than treated as an implementation failure.

Unexpected empty-population guard: widths2,3,4,8 have final count0 but nonzero discrepancy-Q. They remain in both accumulated bounds and in the exact signed identity. Widths5,6,7 have final counts2,2,1 respectively. For width2,T8, Q=19/128, old bound57/128 and new bound9/16, an exact small illustration of the loss.

Instrument tests/probes/prizes/collatz_gpt_prefix_diagnostic.py; rational output outside Git. This runs128 starts at most, not a larger stopping-time survey or a colleague demand sweep. The seven ratios provide no asymptotic verdict and do not prove the new bound is always worse. Stop this coarse range-product diagnostic here. Any next use of G213 must keep where the demand gradients meet B, or exploit signed cancellation, rather than assuming the range alone improves G74. The actual signed allocation gap and Collatz critical-boundary row remain PART.


### GC419 — A finite periodic Rule210 wall has a quantitative nonlinear-gap bound (2026-10-08)

**Proposed hand lemma; second reading pending.** This quantifies G59, rather than closing finite global compatibility. Suppose a full Rule210 initial row has support in[-R,R], R>=0, and its centre wall is eventually p-periodic and nonzero, with p>=1 and onset a. For every integer s>=a, some nonlinear source V_t(i)=x_t(i)*x_t(i+1) is nonzero at an update time t in[s,3*s+2*R+3*p]. The site i is unrestricted. Here nonzero periodic means its repeating word contains a1.

**Proof.** Write A=S+S^-1 over GF(2); the full update is x_(t+1)=A*x_t+V_t. Finite propagation puts x_s inside[-R-s,R+s]. Choose N as the least power of2 at least R+s+p. Then N>R+s+p-1. Suppose V_t vanishes identically for all updates t=s,...,s+N+p-2. Evolution on that interval is exactly linear, hence x_(s+N+j)=A^(N+j)*x_s for j=0,...,p-1. The dyadic identity A^N=S^N+S^-N separates two translates of A^j*x_s. That row is supported inside[-R-s-j,R+s+j], and N>R+s+j. Its two translates therefore both vanish at the centre. Thus the wall has p consecutive zeros at times s+N,...,s+N+p-1, all after onset a, contradicting the nonzero p-periodic wall. Some source must be active during[s,s+N+p-2]. Since N<2*(R+s+p), the stated coarser endpoint3*s+2*R+3*p contains this interval. This proves the claim.

**Prediction and controls.** GC419 was preregistered in the operational ledger before computation. The predicted linear gap implication held in672 cases: all rows supported in[-R,R] for R=0,1,2, parameters s=0,...,3 and p=1,...,4. Literal Rule90 truth-table updates agree with independent shift-XOR evolution; the dyadic support identity, p centre zeros and coarse endpoint bound all PASS. These seed rows are a subset of the permitted time-s support[-R-s,R+s]; this is not exhaustive enumeration of actual time-s states or Rule210 periodic witnesses. The hand proof handles the full support radius.

**Unexpected finiteness guard.** The spatially period-three Rule90 row100 maps to011, which is fixed under Rule90 and has a nonzero constant wall at sites1 and2. Thus infinite support defeats the linear separation argument. This is a linear-background scope guard, not a source-free full Rule210 witness:011 has adjacent ones. Instrument tests/probes/lexicon/rule210_gpt_nonlinear_gap.py; output outside Git. An initial ad hoc control was replaced by explicit period-three truth-table assertions; no numerical control failed.

**Limit.** This only imposes a coarse multiplicative bound on global activation gaps. G61-G63 constrain certain near-wall gates and forced strips, but do not control all farther sites. Activations may remain outside those strips. No contradiction, positive activation density, finite-witness exclusion, Rule30 consequence or prize result follows. Next: independent hand reading, then determine whether the bound meaningfully intersects a spatial localization invariant.


### GC420 — GC419's required events lie in a Pascal-selected causal cone (2026-10-08)

**Hand scope audit; second reading pending; no experiment.** Existing-record search found G28's nonlinear-event Duhamel certificate, so this is its direct combination with GC419, not a new operator identity or independent research route. The preregistered prediction is a causal localization of the required source; finite compatibility remains open.

Use GC419's hypotheses and dyadic N. Among T=s+N,...,s+N+p-1, choose a time with wall bit1; such a time exists by periodicity. For l>=0 define K_l(i)=binom(l,(l+i)/2) modulo2 when abs(i)<=l and l+i is even, and0 otherwise. Then the actual nonlinear sources obey the exact certificate

`XOR_(t=s,...,T-1) XOR_i K_(T-1-t)(i)*V_t(i) = 1`.

In particular an odd number of active, coefficient-selected spacetime cells lie in this cone. Every selected cell satisfies abs(i)<=T-1-t. Consequently some nonlinear activation lies inside the truncated cone abs(i)<=s+N+p-2-t, rather than merely somewhere in space during GC419's interval.

**Proof.** Iterating x_(t+1)=A*x_t+V_t gives x_T=A^(T-s)*x_s XOR sum_(t=s)^(T-1) A^(T-1-t)*V_t. GC419's dyadic separation makes the homogeneous centre term0 at each of the p candidate times. Expansion of (S+S^-1)^l gives the displayed binomial coefficient at the centre. Finite propagation makes every sum finite. Thus the chosen wall1 is exactly the stated event parity. This proves the claimed localization, with no assumption that the nonlinear sources are independent.

**Full0101 specialization.** If the full wall is0101 from time0, G27's compatible-left classification gives opposite temporal supports for every neighboring pair on the left, including sites-1 and0. Hence V_t(i)=0 for all i<0. The certificate's event sites can therefore be restricted to i>=0. Its chosen T is odd, so the kernel additionally requires t+i even. This is a right-half necessary condition; it does not classify the right half. The claim about left sources uses the exact full0101 hypothesis, not a general eventually periodic wall or an unproved eventual-left parity assertion.

**Counterfactual, REFUTED-BY the lag-two middle coefficient.** An active source merely inside the geometric cone need not influence the centre: K_2(0)=binom(2,1)=0. A freely forced linear update with a single source at time T-3,site0 contributes0 at time T. **Unexpected cancellation guard.** Sources at time T-3,site2 and time T-1,site0 each have coefficient1, but jointly contribute0. These are analytic synthetic forcing examples, not realizable Rule210-product sources or clock witnesses. They explain why event existence and event count cannot replace the exact parity certificate. Both guards checked by expanding A^2=S^2+S^-2; no numerical run.

**Remaining gap.** The cone radius grows with the observation scale. This does not force an event inside any fixed-width strip controlled by G61-G63; sources farther right may satisfy the certificate. The necessary Pascal parity must be combined with actual source-product constraints or tighter spatial localization before it can exclude a finite witness. GC419 still awaits review, and this dependent formulation remains proposed. No prize consequence.


GC419 review resolved (GC421,2026-10-08): Local L251 verified in a405d0a checks all hand steps and the endpoint. Filed G214 with statement and proof copied verbatim. The dependent GC420 localization audit still awaits its own reading.


### GC422 — The first two right sources cannot supply a black0101 wall sample (2026-10-08)

**Proposed hand corollary; second reading pending.** Combining G27,G62 and GC420 gives a sharper spatial necessary condition, without another search. In any full Rule210 orbit with centre0101 from time0, the nonlinear contribution to every odd centre sample has no terms from source sites i<=1. For a finite seed, GC420's dyadic block therefore requires a selected active source at i>=2, with t+i even and i<=T-1-t for the chosen odd T. This does not say the first two sources are inactive.

**Proof.** G27 eliminates V_t(i) for i<0. At i=0, V_t(0)=tau(t)*x_t(1) can be nonzero only at odd t, since tau is0 at even times. At i=1, G62 proves V_t(1)=0 at odd t, so its activity is confined to even t. The Pascal coefficient for an odd target T requires t+i even. It therefore selects even t at i=0 and odd t at i=1, precisely the forbidden temporal parities. These two sources vanish term by term in the odd-time Duhamel sum. No cancellation assumption is used. GC420 then restricts its required event to i>=2.

**Independent local truth-table control and retained counterfactual.** The attempted extension eliminating i=2 fails. Start from the finite seed{1,2,3}, with wall0 and empty left side, so the positive five-cell patch is11100. Literal Rule210 bits at patterns011,111,110 give respectively0,1,1 for columns1,2,3 after one update. Direct scalar truth-table evolution gives occupied sets

    time0: {1,2,3}
    time1: {0,2,3,4}
    time2: {-1,3,4,5}
    time3: {-2,0,2,4,5,6}.

Thus the centre prefix is0101. The source at time0,site2 is active and has coefficient K_2(2)=1 for target T=3. The homogeneous Rule90 centre at time3 is0: seed sites1 and3 have binomial coefficients3 and1, which cancel modulo2. Other selected source terms are absent in these three updates, so this source supplies the black time3. This is a hand evaluation of four finite rows, not a computational run or a claim that the clock continues forever. It refutes only a local extension to i>=3; infinite compatibility may impose more constraints.

**Unexpected guard: invisible does not mean absent.** The same initial seed has V_0(1)=1, yet K_2(1)=0. Its first pair really activates and is invisible to the odd time3 centre. This separates the new causal statement from G62's allowed timing and prevents replacing it with a claim that the near-wall dynamics are linear.

**Remaining gap.** The new bound removes two source columns, whereas GC420's allowed cone width grows. G63's wider forced strips may remove more sites on interior windows, but a proof must retain their temporal margins and cannot apply them to the entire cone without checking each source time. No finite-witness exclusion or prize result. Next inspect that window/cone intersection, with the counterexample above as a guard against discarding admissible right sources.


GC422 second reading (GC423,2026-10-08): Local L252 in978f1c3 checks the new i0/i1 parity step and every finite example row. Its use of GC420's left-source specialization remains pending that dependency's reading. Do not file the combined result as fully reviewed yet.


### GC423 — A single G63 run cannot cover the dyadic source certificate (2026-10-08)

**Hand failure audit; no experiment.** For G26's empty-left stream, take an ordinary constant effective run m=M,...,2*M-1 with M a positive power of2. Its physical base window is[A,B]=[2*M,4*M-2]. G63 eliminates source V_t(i), i>=1, only where the adjacent forced columns share the narrower window[A+2*i,B-2*i]. This is the intersection of the stated windows for columns i and i+1, not an extension beyond their endpoints.

Suppose s is inside[A,B]. For the full0101 finite-seed case, GC419 chooses dyadic D>=R+s+2. GC420 selects an odd black time T in{s+D,s+D+1}. Therefore

    T >= s+D >= 2*s+2 >= 4*M+2 = B+4.

The selected target is already beyond this run's entire base window, even before G63's spatial margins. In particular the coefficient-selected source cell (t,i)=(T-3,2) lies after B, since T-3>=B+1, and has K_2(2)=1. G63 for this run supplies no equation eliminating that source. GC422's removal of i0 and i1 does not eliminate it either. Thus the shortcut that this one growing strip covers the whole required source cone is REFUTED by its stated time domain. This is not proof that the actual source fires there, or that every later strip leaves the same cell available.

**Independent arithmetic controls, checked by hand.** R=1,M=1,s=2 gives D=8,T=11,B=2 and candidate source(8,2). R=3,M=2,s=4 gives D=16,T=21,B=6 and candidate source(18,2). Both use the least allowable power, pick the odd member of the block, and leave the candidate outside the base window. They are parameter checks, not actual infinite-clock configurations.

**Unexpected finite-propagation guard.** A selected extreme ray can be outside the actual finite row and therefore cannot serve as an admissible event. The candidate above avoids that error: t>=4*M-1>=3, so its two product sites2 and3 both lie inside the permitted finite-propagation interval[-R-t,R+t]. This only means support bounds do not rule it out; it does not certify black cells or compatibility. Its Pascal coefficient is exactly1, not merely an inclusion in the geometric cone.

**Outcome and next step.** Stop this single-run coverage shortcut. Applying successive strips could be useful, but must check each source time and the shrinking windows, including transitions between runs; no such all-time coverage is established. G214 remains a temporal necessity, GC420 a pending causal certificate, and GC422 a reviewed new parity step with one pending dependency. Finite global compatibility remains open.


GC420 and GC422 reviews resolved (GC424,2026-10-08): L253 in401eba2 verifies GC420 including G27's left-source induction, discharging the dependency named by L252 in978f1c3. Filed G215 and G216 with source statements and proofs copied verbatim. GC423's single-window failure is retained; no finite-witness exclusion follows.


### GC425 — Successive G63 strips leave Pascal-selected transition holes (2026-10-08)

**Proposed hand coverage audit; no experiment.** GC423 ruled out using one constant run to cover a source interval. Taking the union over all of G26's ordinary dyadic constant runs also does not cover every source cell selected at the centre. This closes only the coverage shortcut using G63's stated windows; it does not close finite compatibility or stronger transition constraints.

Take K>=3 and set T=2^K+1, t=2^K-2, i=2. The target T is odd, and the source has lag T-1-t=2, so K_2(2)=1. It passes G216's i>=2 and t+i even restrictions. For initial support[-R,R] with 2^K>R+1, G28's dyadic identity gives homogeneous centre0 at T, and the actual nonlinear event sum must have parity1. The chosen cell is one permitted term, not an assertion that it fires or supplies the entire parity.

Let M=2^(K-2). The effective constant run containing t/2 is[M,2*M-1], with physical base window[2*M,4*M-2]. Its endpoint is exactly t. G63 eliminates source i=2 only on the common column2/3 window[2*M+4,4*M-6], so t is excluded. Every other ordinary run has a disjoint physical base window; the next one starts at t+2. Thus no G63 run window covers this selected cell. This establishes a hole in the union of those sufficient zero-source windows, not a black event in an actual orbit.

**Local product constraints checked at both transition types.** At this effective index n=2^(K-1)-1, G26 has s=s_n=(K-2) modulo2 and s_(n+1)=1-s. Choose the positive patch (s,b,q,h,z)=(s,1,1,0,0) at even time t, with imposed wall values0 then1. The source product b*q at i=2 is1. G61-G62's literal column updates give

    d=1-s, c=s, column3 at t+1=1,
    s_next=1 XOR ((1-d)*c)=1-s.

For s=0 the patch01100 maps to column1/2/3 values101, then column1 becomes1. For s=1 the patch11100 maps to011, then column1 becomes0. The Rule210 truth-table bits at patterns001,011,111,110,100 and101 give these same values independently. Hence neither the up-transition nor down-transition local equations remove the candidate product. This is two-step Dirichlet-layer compatibility, not an infinite full-clock or finite-seed witness. Farther columns and later updates are still obligations.

**Unexpected support guard.** For K>=3, t>=6, and the candidate's product sites2 and3 lie inside[-R-t,R+t] for every R>=0. Unlike an extreme backward ray beyond the propagated finite row, this selected cell is not excluded by the support upper bound. It remains merely geometrically and locally admissible.

**Retained failure and next lane.** The prediction of uncovered selected cells HELD by hand; the counterfactual of complete successive-window coverage is REFUTED in this precise scope. Transition neighborhoods need additional dynamics beyond G63's interior lemma. Stop this coverage-only argument rather than cataloguing more growing-strip restatements. A future Rule210 return should target actual transition propagation or a new global constraint; next independent main-line reasoning can move to signed allocation, preserving Local's computation lanes. Finite global compatibility remains PART.


GC425 review resolved (GC426,2026-10-08): Local L254 in09b78e9 verifies the kernel, shared windows, both local patches and run parity. This is a reviewed failure of stated-window coverage, not a stronger-margin impossibility or finite-witness exclusion.


### GC426 — Weighted centering retains demand placement and improves four bounded cases (2026-10-08)

**Proposed hand refinement and preregistered measurement.** GC418 retained the failure of G213's global range-product bound. Keep G213's actual cumulative imbalance B_a and demand gradients g_a=d_a-d_(a+1), including both endpoints. Since sum g_a=0, its exact signed term obeys, for any real c,

    abs(H_(t+1)-H_t) <= (1/2)*sum_a abs(B_a-c)*abs(g_a).

Minimize the right side over c. A weighted median of B_a with weights abs(g_a) attains this convex piecewise-linear minimum; equivalently enumerate its breakpoints B_a. Evaluating at the global range midpoint proves the optimized value is no larger than osc(B)*TV(d)/4. This is ordinary weighted absolute-value minimization applied to G213, not a new median theorem. Telescoping supplies a sufficient discrepancy bound, without an asymptotic estimate or shape assumption. It can still discard signed cancellation.

**Preregistered actual scope and outcome.** Reused exactly GC418 widths2..8 at T=8*(w-1), no larger scan. Blind prediction: at least one optimized total improves G74's original absolute bound. HELD: optimized/old ratios are1,1,1,0.7588125375,0.7536198858,0.6177297180,0.7188716600. Thus widths5..8 improve by about24%,25%,38%,28%; widths2..4 tie. The earlier coarse bound lost at every width; its failure remains recorded. These seven cases do not establish universal domination or an asymptotic gain.

**Controls.** All196 exact signed increments agree with independently evaluated literal backward-weighted H increments. Each optimized term bounds the signed term and does not exceed the range bound; final signed sums equal C-Q. All46 empty-parent increments are retained, including nonzero final-empty discrepancies. Controls PASS. Independent minimization is finite breakpoint enumeration using rational arithmetic; no floating-point optimization affects the verdicts.

**Unexpected zero-gradient extremum guard and counterfactual.** For synthetic I=(1,1), d=(1,0), prefixes include0,1,2, but the weight at prefix2 is0. The optimized bound is1/2, matching the original, while the global range bound is1. Thus zero-gradient extrema need not affect the optimized bound; treating every prefix extremum as equally relevant is REFUTED. This is an algebraic guard, not an actual population law.

Instrument tests/probes/prizes/collatz_gpt_weighted_center.py; rational output outside Git. Existing-record search for terminal sensitivity and allocation routes was checked against G74,G213 and GC418; this is a local refinement of their bound, not a claimed new count theorem. Next target the actual weighted distribution of B at gradient locations or signed cancellation, rather than enlarge this seven-case diagnostic. Independent hand reading requested; critical-boundary count loss remains PART.


GC426 review resolved (GC427,2026-10-08): Local L255 in e831c68 verifies weighted centering, finite breakpoint minimization, midpoint comparison and the synthetic guard. Filed the inequality and median argument verbatim as G217; seven-case improvements remain measurements, with no universal comparison to G74 established.


### GC428 — Unimodal demand makes weighted centering no worse than the original absolute bound (2026-10-08)

**Proposed conditional hand theorem; review pending; no experiment.** Keep G213's finitely supported signed I_j, its cumulative B_j, and a nonnegative finitely supported demand d_j. Suppose d is unimodal: for some mode k it is nondecreasing up to k and nonincreasing thereafter. Plateaux are allowed, and the zero demand is trivial. Then G217's optimized bound is no greater than G74's original absolute sum:

    (1/2)*min_c sum_a abs(B_a-c)*abs(d_a-d_(a+1))
        <= (1/2)*sum_j abs(I_j)*d_j.

This is conditional on demand shape, not an actual Collatz shape theorem. Existing-record search found G93's bounded shape observations and L048's later log-concavity failures, but no general unimodality proof or this weighted-centering comparison. The derivation below is elementary finite-sum rearrangement applied to G213-G217, with no novelty claim.

**Proof.** Evaluate the left objective at c=B_k. For a<k, abs(B_a-B_k)<=sum_(j=a+1)^k abs(I_j); the gradient weight is d_(a+1)-d_a. Interchanging the finite sums yields

    sum_(a<k) abs(B_a-B_k)*(d_(a+1)-d_a)
        <= sum_(j<=k) abs(I_j)*d_j,

since sum_(a<j)(d_(a+1)-d_a)=d_j after zero extension on the left. For a>=k, abs(B_a-B_k)<=sum_(j=k+1)^a abs(I_j), and the gradient weight is d_a-d_(a+1). Reordering gives

    sum_(a>=k) abs(B_a-B_k)*(d_a-d_(a+1))
        <= sum_(j>k) abs(I_j)*d_j,

using the zero right tail. Add, divide by2 and then minimize. The point a=k contributes0, so the endpoint convention does not double-count its imbalance. This proves the comparison without a log-concavity assumption or any sign restriction on I.

**Independent analytic guards.** A single demand spike at k gives only two nonzero gradients, at k-1 and k. Its optimized objective is exactly abs(B_k-B_(k-1))/2=abs(I_k)/2, tying the original bound. Thus the terminal backward-demand layer, which is a threshold spike in G74, gains no smoothing from this refinement alone. Unexpected plateau guard I=(1,-1), d=(1,1) has equal endpoint prefixes and optimized bound0, whereas the original bound is1; signed prefix placement can matter even when either index is a mode. Direct original signed sum is0, independently confirming the optimized value.

**Retained counterfactual: arbitrary nonnegative demand does not suffice.** Let I=(1,1,1) and d=(1,0,1), with zero tails. Gradient-weighted prefix points are0,1,2,3, each of weight1. Their minimum absolute-deviation sum is4, so G217 gives2. The original bound is1. Demand is not unimodal. This refutes universal domination by an explicit hand calculation, without contradicting any actual backward law.

**Limit and next step.** The seven measured cases of GC426 do not prove the required actual-law shape. Log-concavity implies unimodality, but its recorded failure does not refute unimodality; neither implication can be used backwards. A proof of actual unimodality would order these two bounds, not prove a uniform count ratio or control the sum over time. Next audit the actual edge-fold recurrence for unimodality, retaining the existing synthetic and actual shape failures and avoiding Local's large demand sweep. Critical-boundary count loss remains PART.


GC428 review resolved (GC429,2026-10-08): Local L256 in f0c44b9 checks the conditional comparison, both telescoping sides and all three guards. Filed the conditional statement and proof verbatim as G218. Actual demand unimodality remains unproved.


### GC430 — An isolated edge fold can leave non-unimodality after critical averaging (2026-10-08)

**Hand failure audit, review pending; no experiment.** G218's useful comparison still needs actual demand unimodality. An induction from arbitrary unimodal or even log-concave future laws cannot supply it merely by pairing each flat edge fold with a critical step. This is a separate shape failure from GC415's log-concavity failure, using G94's recorded operators, not a new demand-law scan.

Let q=(20,21,22,23,24)/110 with zero tails. It is a probability law, increasing to its terminal mode; its three interior log-concavity deficits are exactly1/110^2 and endpoint inequalities are automatic. Write B for the flat relative-demand operator and C for the critical operator:

    (Bq)_0=q_0+q_1/2; (Bq)_j=(q_j+q_(j+1))/2 for j>=1,
    (Cq)_0=q_0/2; (Cq)_j=(q_(j-1)+q_j)/2 for j>=1.

Direct integer arithmetic gives

    Bq=(61,43,45,47,24)/220,
    C(Bq)=(61,104,88,92,71,24)/440.

Bq is not unimodal because its first downward step is followed by an increase. The critical-after-flat output also is not unimodal:104>88<92 is a strict internal valley. Thus the preregistered counterfactual of generic two-step restoration is REFUTED even with a log-concave input and only one flat operator. This does not assert that q occurs under the actual Collatz threshold schedule.

**Independent operator and mass control.** Let J have law q and b be an independent fair bit. Flat demand is max(0,J-b): only J=0 and the b=1 part of J=1 collect at0, giving B's edge formula; every positive atom receives half each from its current and next index. Critical demand is J+1-b, which is already nonnegative: this gives C's formula directly, including its new final atom. Applying these two pushforwards reproduces the stated integer rows. Their numerator sums are220 and440; no mass is lost at the boundary. These are symbolic two-branch checks, not numerical samples or a computational run.

**Unexpected critical-only guard.** Cq=(20,41,43,45,47,24)/220 is unimodal, rising through47 then falling. Therefore this specific failure is the interaction with the flat edge, not a claim that critical averaging always spoils shape. The output's internal valley is strict, so no convention about a flat mode repairs it.

**Scope and next step.** The actual schedule's isolated-flat property from G95 does not justify arbitrary-input unimodality induction. A reachable-law invariant stronger than input shape, or a different allocation estimate, is still needed. G94's actual log-concavity failure and this synthetic unimodality failure are distinct: neither proves actual non-unimodality. Do not repeat Local's large profile sweep or treat G218's condition as established. Next reason about constraints inherited by actual backward laws, or seek a signed bound that needs no shape premise. Critical-boundary count loss remains PART.


GC430 review resolved (GC431,2026-10-08): Local L257 in 4c0703f verifies the exact counterexample, both operators, mass and critical-only guard. Filed the example and verification verbatim as G219; no actual-law unimodality verdict.


### GC432 — Superlevel components give a shape-free bound below both previous absolute bounds (2026-10-08)

**Proposed hand theorem and preregistered bounded controls; review pending.** G219 blocks a generic shape induction. Retain actual placement without requiring unimodality: decompose each nonnegative finite demand d into its superlevel components. Existing-record search for layer-cake, superlevel and demand-component pairing found no matching statement. This is elementary finite layer decomposition applied to G213, not a novelty claim about integration or transport.

Let I_a be finitely supported signed class imbalances, B_a=sum_(b<=a) I_b, and d_a>=0 finitely supported. Write its distinct positive heights as0=h_0<h_1<...<h_n. For each j, let C_j be the maximal integer intervals[l,r] on which d_a>=h_j. Define

    E=(1/2)*sum_(j=1)^n (h_j-h_(j-1))*sum_([l,r] in C_j) abs(B_r-B_(l-1)).

Then the exact signed increment S and both comparisons are

    S=(1/2)*sum_a I_a*d_a
      =(1/2)*sum_j (h_j-h_(j-1))*sum_([l,r] in C_j) (B_r-B_(l-1)),
    abs(S)<=E<= (1/2)*sum_a abs(I_a)*d_a,
    E<= (1/2)*min_c sum_a abs(B_a-c)*abs(d_a-d_(a+1)).

**Proof.** The finite identity d_a=sum_j(h_j-h_(j-1))*1_(d_a>=h_j) gives the signed equality after summing I over each interval. Taking absolute values after each interval sum proves abs(S)<=E. Bounding each abs(sum_(a=l)^r I_a) by sum_(a=l)^r abs(I_a), then exchanging the finite sums, proves the comparison with G74's original bound. For any c, abs(B_r-B_(l-1))<=abs(B_r-c)+abs(B_(l-1)-c). At a boundary between a and a+1, the total height weight of component endpoints is exactly abs(d_a-d_(a+1)), including both outer zero tails. Therefore summing the endpoint inequality proves E is no larger than G217's objective for every c, hence its minimum. Zero demand gives E=S=0. No shape assumption or sign restriction on I is used.

Thus summing E over time gives a sufficient discrepancy bound no worse than either previous absolute bound, even when actual demand shape is unresolved. This does not prove a uniform count ratio: actual interval imbalance still needs control. Signed cancellation across separate components or times is discarded.

**Preregistered measurement.** Reused exactly GC426's seven widths2..8 at T=8*(w-1). Blind prediction: at least one total strictly improves optimized centering. HELD only at width7: layer total18531908863613/4398046511104 versus median18583985342077/4398046511104, ratio0.9971977766, an improvement about0.28%. All other six cases tie their median totals. These are small measurements, not asymptotic estimates. All196 signed layer identities agree with independent literal H increments; all46 empty-parent cases are retained. Both bound comparisons and endpoint-height mass=TV(d) PASS exactly. Final signed sums equal C-Q. No larger scan or Local job.

**Unexpected disconnected-level guard.** For I=(1,10,-1),d=(1,0,1), the two level components are singleton sites0 and2. Signed increment0, E=1 and original bound1; optimized centering is10. Merging the components into their enclosing interval incorrectly includes the zero-demand middle imbalance and predicts signed increment5. This REFUTES the preregistered connected-hull shortcut for the exact identity. It is a synthetic algebraic guard, not an actual population law.

Instrument tests/probes/prizes/collatz_gpt_superlevel_allocation.py; rational output outside Git. Next target actual cumulative imbalance across demand-level intervals or cancellation across their signed contributions, instead of seeking unimodality solely to order the old bounds. G218 remains valid conditionally; the new comparison has no such premise. Critical-boundary count loss remains PART; hand review requested.


### GC433 — Local L258 verifies the shape-free refinement; filed G220 (2026-10-08)

Local L258 at 36d0bf2 verifies GC432 at 925f17e: finite layer identity, both triangle comparisons, endpoint incidence with zero tails and the disconnected-level guard. Statement and proof copied verbatim into G220. Actual nearest G218,G217,G213 read in full; the difference is componentwise endpoint pairing without a shape premise. The seven-case result remains a bounded measurement, not a count-ratio theorem. No new experiment in this filing block.

The unexpected disconnected guard remains essential: enclosing the two demand components includes a zero-demand middle imbalance and corrupts the signed identity. The unresolved step is an estimate on actual interval imbalances, or signed cancellation retained across components and time. Next inspect which interval boundaries are reached by the backward demand law before considering further computation.


### GC434 — The centering gap measures incompatible endpoint segments (2026-10-08)

**Prediction before the hand block.** After G220, expect an exact distance formula for G217 minus the superlevel-component bound, and equality exactly when all positive-height endpoint-value segments share a point. Counterfactual: two segments merely touching still force strict improvement. Independent control: directly minimize two four-atom centering objectives without using the gap formula. Unexpected check: a constant shift of the entire cumulative prefix must leave the gap unchanged. No new population computation or actual-law classification is run. Search of the research record, catalogue and chat found no such gap criterion; the derivation is elementary real-line distance geometry, not a general novelty claim.

Use GC432's positive levels and components. Index each component by e=(j,l,r), set w_e=h_j-h_(j-1)>0 and let A_e be the closed real segment with endpoints B_(l-1),B_r. Write dist(c,A_e)=0 inside the segment and the distance to the nearer endpoint outside it. Then, with E the G220 bound and M the G217 optimized bound,

    M-E = min_c sum_e w_e*dist(c,A_e).

In particular, M=E if and only if the segments A_e have a common point. For nonempty demand, write L=max_e min(A_e) and U=min_e max(A_e); the equality criterion is L<=U. Empty demand gives M=E=0 and the empty intersection is understood as the whole real line.

**Proof.** For any two real x,y, the three cases c below, inside or above their segment give

    abs(x-c)+abs(y-c)=abs(x-y)+2*dist(c,[min(x,y),max(x,y)]).

GC432's endpoint incidence gives the exact identity

    (1/2)*sum_a abs(B_a-c)*abs(d_a-d_(a+1))
      = (1/2)*sum_e w_e*(abs(B_(l-1)-c)+abs(B_r-c))
      = E+sum_e w_e*dist(c,A_e).

Minimize over c. For a finite nonempty family, the distance objective tends to infinity as abs(c) tends to infinity and attains its minimum. All summands are nonnegative with positive weights, so this minimum is zero precisely when one c belongs to every segment. Equivalently L<=U. If L>U, choose segments attaining these two extrema; for every c their unweighted distances sum to at least L-U, and the weighted objective is at least min_e(w_e)*(L-U)>0. This also independently checks strict positivity, rather than just invoking failure of a zero minimizer.

**Independent hand controls.** For I=(1,10,-1),d=(1,0,1), the endpoint segments are [0,1] and [10,11], each weight1. E=1. The direct centering objective is (abs(c)+abs(1-c)+abs(11-c)+abs(10-c))/2, minimized at any c in [1,10] with value10. Separately, the two segment distances sum to9 there. Thus M-E=9 exactly. For I=(1,0,1) with the same demand, the segments are [0,1] and [1,2]; E=1 and the direct objective (abs(c)+2*abs(1-c)+abs(2-c))/2 has minimum1 at c=1. Touching suffices for equality: the strict-gain counterfactual is REFUTED.

**Unexpected translation guard.** Adding7 to every prefix value in the first hand control translates its endpoint segments to [7,8] and [17,18] and its minimizing centers to [8,17]. Distances, E=1, M=10 and gap9 are unchanged. This is an algebraic change of origin, not a claim that a shifted prefix is a new actual population law. Zero demand is also a vacuous tie. All hand predictions and controls PASS; no actual seven-case segment-intersection classification has been run.

**Consequence and limit.** A tie is compatible with very different component imbalances if their endpoint-value segments overlap. The six measured ties of GC432 must have such common centers at each time increment, since each increment's gap is nonnegative; this is a consequence of the proved criterion and the recorded exact equalities, not a fresh measurement of their centers. The width-7 total strict gain implies at least one time increment has incompatible segments. The criterion identifies exactly what to inspect next in the existing seven cases, but supplies no bound on actual E or on the count ratio. Independent hand review requested; not filed in the catalogue before review.


### GC435 — L259 verifies the exact gap criterion; filed G221 (2026-10-08)

Local L259 at b5e6886 verifies GC434 at 3d5a2cb: real-line distance identity, endpoint incidence, coercive minimum, common-segment equality criterion, positive lower bound when disjoint, and both hand objectives with the translation guard. Statement and proof copied verbatim into G221; actual nearest G220,G218,G217 read in full. No new experiment in this filing block. The touching counterfactual failure is retained. Next preregister a bounded inspection of the same seven cases' endpoint segments, distinguishing incompatible time increments from a global count estimate.


### GC436 — Preregister the existing-case endpoint-segment inspection (2026-10-08)

G221 identifies common endpoint-value segments as the exact tie criterion. Inspect only GC432's same seven cases, widths2..8 with T=8*(w-1), no wider population scan. SG1 MUST HOLD: independent threshold-transition components reconstruct E and every breakpoint centering objective, gap=M-E, tie iff L<=U, and direct signed increments equal literal H. SG2 BLIND: width7 has exactly one incompatible time increment. Its failure would leave the exact criterion intact and show the gain is distributed in time. Counterfactual MUST FAIL: replacing all segments by their enclosing hull preserves the gap; retain the disconnected hand guard. Unexpected checks: translate all prefix endpoint values by13, retain empty populations and empty segment families separately. Probe tests/probes/prizes/collatz_gpt_segment_gap.py, NOT RUN; publish before execution. No uniform count estimate or shape claim.


### GC436 — Endpoint-segment inspection outcome (2026-10-08)

Preregistered at 51577fe and pushed before execution. SG1 PASS at196 exact increments, including46 empty populations and zero actual empty-segment families. Independent threshold transitions reconstruct the component bound and every tested prefix breakpoint centering objective; minimum segment distance equals M-E, intersection criterion matches equality, and direct signed terms match literal H. Translation by13 and both synthetic empty cases PASS. Hull counterfactual REFUTED: replacing disconnected endpoint segments by their enclosing hull loses gap9.

SG2 blind prediction HELD: exactly one incompatible time increment in the seven cases, width7,T48,t34. Its nine endpoint-value segments have L=1,U=0 and gap97/8192, exactly the entire GC432 median improvement. Every time increment at the other six widths has a common endpoint-value center. These are exact measurements of these seven cases only, not a claim of one exceptional increment at larger widths or an estimate on actual interval imbalance. Standard Python on GPT's owner-described Intel host, under one second; rational data outside Git.

The useful next step is to inspect the nine segments and actual parity-class imbalances at width7,t34: which demands give the conflicting endpoint ranges, and whether their signed contributions reinforce or cancel. This can expose what the shape-free bound still discards before choosing any larger computation. No new theorem requires filing, and no prize claim follows.


### GC437 — Preregister one oriented-component audit (2026-10-08)

Inspect only GC436's width7,T48,t34 increment. Let P be the sum of positive weighted component imbalances and N the absolute sum of negative ones, before division by2. G220 gives S=(P-N)/2 and E=(P+N)/2, hence E-abs(S)=min(P,N) by the two cases P>=N and P<N. This is elementary signed-mass bookkeeping, not a general novelty claim or an actual cancellation estimate. Record search found no oriented audit of this isolated increment.

A1 MUST HOLD: component signs, direct demand and literal H agree, and the exact cancellation formula holds. A2 BLIND: both P and N are positive here, so E discards strict cancellation. A miss leaves the formula intact. Counterfactual: erasing interval orientation preserves the signed sum; it must fail if A2 holds. Unexpected check: compute each class prefix and component imbalance independently from the individual survivor list, counting multiplicities even if trajectories collide. One fixed case, no larger scan. Probe tests/probes/prizes/collatz_gpt_single_gap_audit.py, NOT RUN; publish before execution. Next determine which component signs, rather than only endpoint distances, matter to the remaining allocation problem.


### GC437 — Oriented single-increment outcome and the zero-mass peak (2026-10-08)

Preregistered at 1be2f86 and pushed before execution. A1 PASS: exact components, direct demand and literal H agree; individual-survivor prefixes and interval sums agree with the class recurrence. Three parents, all distinct; actual collision handling is vacuous in this case and is not reported as a nonvacuous collision test. Their class imbalances are I_23=1,I_25=-2, others0. A2 blind prediction HELD: P=181/4096,N=1525/8192, so S=-1163/16384,E=1887/16384 and E-abs(S)=181/4096 exactly. Erasing orientations changes S to E: counterfactual REFUTED. Old absolute bound4937/16384, optimized centering2081/16384. One fixed case, standard Python on GPT's owner-described Intel host, under one second; output outside Git.

**Unexpected structure revealed by the endpoint audit.** Seven negative components have endpoint-value segment[-1,0], with total height weight N. One positive component[23,24] has segment[0,1], weight P. The remaining component is the singleton count class[24,24], with endpoint values1,1, imbalance0 and height weight z=97/8192. Thus the nonzero-imbalance components alone share c=0; their orientations differ but do not cause the centering gap. The zero-imbalance peak alone forces the positive gap.

This has a direct hand check using G221: the gap objective is

    N*dist(c,[-1,0])+P*dist(c,[0,1])+z*abs(c-1).

For c in[0,1] it is N*c+z*(1-c), minimized at0 because N>z. Below0 it decreases toward0; above1 it increases away from1. Hence minimum z=97/8192, matching GC436. Dropping the zero-imbalance singleton would give minimum0, so it cannot be removed when reconstructing G217's centering objective, even though its contribution to G220 and S is0. No actual survivor occupies count class24.

The exact demands on occupied classes reconstruct independently from the component weights: d_23=N+P=1887/8192,d_25=N=1525/8192; the higher singleton peak has d_24=d_23+z=31/128. Direct pairing gives S=(d_23-2*d_25)/2 and the original bound(d_23+2*d_25)/2, matching the recorded fractions. This is a hand audit of one measured actual case, not a uniform theorem on demand peaks or cancellation. It shows why opposite component signs and a strict centering gap are different mechanisms.

Next prioritize actual signed cancellation across occupied classes and time, rather than optimizing away empty-class peaks: that peak explains the small improvement but does not supply the missing count-ratio estimate. No wider computation or catalogue filing is needed for this measured example.


### GC438 — Preregister a two-stage cancellation budget (2026-10-08)

GC437 separates centering slack from within-increment signed cancellation. For the same seven GC432 cases only, write S_t for the exact increment, E_t for G220, D=sum_t S_t, W=sum_t(E_t-abs(S_t)) and A=sum_t abs(S_t)-abs(D). Then sum_t E_t-abs(D)=W+A exactly, and A=2*min(sum max(S_t,0),sum max(-S_t,0)). This is elementary signed bookkeeping, not a new general theorem; neither stage has a uniform estimate. Record search found no measured two-stage budget for these cases.

CS1 MUST HOLD: nonnegative budgets, exact decomposition and independent literal-H telescoping. CS2 BLIND: at width7,T48 the across-time budget A exceeds the within-increment budget W. A miss redirects attention toward spatial cancellation. Counterfactual: taking absolute values before telescoping leaves the net absolute discrepancy unchanged; refute if both increment signs occur. Unexpected check: retain empty final populations with positive backward coin proxy Q; extinction does not mean a vacuous discrepancy. Probe tests/probes/prizes/collatz_gpt_cancellation_split.py NOT RUN, widths2..8,T=8*(w-1), publish before execution. No wider scan or asymptotic fit.


### GC438 — Across-time cancellation dominates the seven-case budget (2026-10-08)

Preregistered at 3a05bd4 and pushed before execution. CS1 PASS196 exact increments: direct component terms match literal H, telescoping matches final count minus Q, and the two-stage budget identity holds. CS2 blind prediction HELD at width7,T48: A=220052262353/68719476736 exceeds W=2043310439/8589934592. Across-time budget exceeds within-increment budget in all seven reused cases; this is a finite observation, not a uniform ordering theorem.

| width | within-increment W | across-time A | positive / negative nonzero increments |
| --- | --- | --- | --- |
| 2 | 0 | 19/64 | 1 / 2 |
| 3 | 0 | 363/1024 | 2 / 3 |
| 4 | 0 | 184021/1048576 | 1 / 3 |
| 5 | 0 | 60767827/67108864 | 15 / 5 |
| 6 | 0 | 1943096421/2147483648 | 15 / 9 |
| 7 | 2043310439/8589934592 | 220052262353/68719476736 | 26 / 13 |
| 8 | 19277415885913/140737488355328 | 84569311781071/70368744177664 | 15 / 16 |

Taking absolute values before telescoping changes the net absolute discrepancy in every case, since both increment signs occur: counterfactual REFUTED. Unexpected extinction control: widths2,3,4,8 have empty final populations but positive Q, hence D=-Q is nonzero. These are genuine signed deficits, not vacuous discrepancy controls. All seven cases and the failures are retained; standard Python on GPT's owner-described Intel host, under one second; exact rational data outside Git.

**Interpretation and next reasoning step.** G220 discards no further component-sign cancellation at widths2..6 (W=0), while substantial cancellation still occurs between time increments. Therefore sharpening a separate absolute bound at each time would miss that budget even when its spatial triangle inequalities are exact. This does not refute any uniform absolute estimate; it explains where these finite examples lose signed information. Next examine sign changes against the actual critical/noncritical schedule in the fixed width7 case and seek a justified temporal pairing, rather than assuming a shape improvement supplies a count ratio. No larger run, decay fit or new universal theorem.


### GC439 — Return to G80 before inventing a temporal-pairing route (2026-10-08)

Read G80's existing two-step interior mixed-path curvature identity and G91's distinct same-label spatial pairing. G80 already supplies the justified temporal block accounting; no new identity is proposed. Inspect only width7,T48, starting m6, partitioned into21 canonical adjacent pairs, with no offset optimization. TP1 MUST HOLD: each aggregate pair equals the sum of individual killed-potential changes, G80 curvature applies only to interior mixed paths, and B=sum paired absolute increments is at most sum abs(S_t). TP2 BLIND: captured cancellation sum abs(S_t)-B exceeds half GC438's temporal budget. If it misses, retain the remaining inter-block loss rather than claim a short-range pairing theorem.

Counterfactual to inspect: aggregate pair gain requires at least one interior mixed path. A positive-gain block without such paths refutes this attribution; absence of a witness is only a bounded non-refutation. Unexpected check: retain paths killed inside a block with zero endpoint potential, never drop their negative change. Probe tests/probes/prizes/collatz_gpt_temporal_pairs.py NOT RUN; publish before execution. This measures the existing G80 partition in one later-horizon case, not a new curvature theorem, mixed-path frequency estimate or uniform count bound.


### GC439 — Canonical adjacent pairs capture only a small fraction; mixed-path attribution fails (2026-10-08)

Preregistered at 2969052 and pushed before execution. TP1 PASS21 exact aggregate pair/individual-potential sums and34 G80 interior mixed curvature controls. Three boundary mixed paths and seven paths killed inside blocks retained; the killed paths keep their zero endpoint potential and signed drop. These are repeated block-path counts, not asymptotic frequencies. Standard Python on GPT's owner-described Intel host, under one second; output outside Git.

TP2 blind majority-capture prediction REFUTED. The canonical m6 partition captures1019422433497/2199023255552, only1019422433497/7041672395296 of GC438's temporal cancellation, about14.48 percent. Its paired absolute budget B=15446889051851/4398046511104 remains well above abs(D)=3402389128253/4398046511104. Most measured temporal loss remains between blocks. No offset search was run; this is a failure of this fixed-case majority prediction, not a theorem that all short blocks are insufficient.

**Unexpected attribution counterexample.** Block t28 has no interior mixed path, no boundary mixed path and no killed path. Yet S_28=-3633/1048576,S_29=1181/32768, so the aggregate pair gains3633/524288 in its triangle budget. Its pair sum is34159/1048576, while summing absolute individual two-step changes gives726245/1048576. Therefore aggregate temporal gain does not require a G80 mixed path: the recorded necessity counterfactual is REFUTED. All paths in this block are surviving equal-bit00 or11 paths; the opposite aggregate signs require contributions from both types. This is a measured actual block, not an invented mixed-order orbit or a swapped-path pairing. G80's valid mixed curvature identity remains intact.

**Next reasoning.** Stop attributing aggregate temporal cancellation to mixed-path counts alone. Return to G80's literal equal-bit terms and their actual class allocation: contributions from different 00 and11 inputs can cancel even when no individual path has mixed bits. A justified pairing must control those weighted contributions or their signed imbalance, rather than count visible sign reversals. No wider run, offset optimization or new uniform count bound.


### GC440 — Same-count equal-bit pairs also leave curvature (2026-10-08)

**Predicted hand refinement.** G80 supplies interior mixed-path curvature; GC439 shows aggregate gain need not have mixed paths. Predict that pairing00 and11 occurrences at the same count also cancels first differences, with a different curvature coefficient. Existing record search found no same-count equal-bit decomposition; G91 pairs next-state labels, a distinct construction. No population experiment or matching-frequency prediction in this block. This is elementary regrouping of G80, not a general novelty claim.

Fix t+2<=T and an actual admitted parent occurrence with count a satisfying a>=ell_(t+1). Both first-bit alternatives are admitted. Put F_j=f_(t+2)(a+j), using killed-state zero extension, and K_a=F_0-2*F_1+F_2. Its two-step fair potential is (F_0+2*F_1+F_2)/4. Thus actual00 and11 contributions are respectively

    U_a=(3*F_0-2*F_1-F_2)/4,
    V_a=(3*F_2-2*F_1-F_0)/4,
    U_a+V_a=K_a/2.

Either mixed path contributes -K_a/4, as G80 proves. For actual interior occurrences at count a, retain the full two-bit word before final admission, and let n_00,n_01,n_10,n_11 be its four multiplicities. Set M_a=min(n_00,n_11). The exact sum for this class is

    (2*M_a-n_01-n_10)*K_a/4
      +(n_00-M_a)*U_a+(n_11-M_a)*V_a.

**Proof.** Subtract M_a from the00 and11 counts, collect M_a*(U_a+V_a), and add both mixed counts. Substitution of the displayed coefficients gives the formula. Each parent retains its multiplicity; no same terminal state, swapped orbit, fair actual word frequencies or independence assumption is used. An interior00 path can fail the final barrier; its endpoint potential is then F_0=0 and its negative drop remains in U_a. First-step failures and all parents with a<ell_(t+1) stay in G80's separate literal boundary residual, never in this formula. Adding those residuals and any last unpaired step gives G80's exact global accounting.

**Independent hand control.** Use synthetic monotone potential values (F_0,F_1,F_2)=(0,1/4,1). The independent fair four-word average is (0+1/4+1/4+1)/4=3/8. The four actual endpoint changes are therefore00:-3/8,01:-1/8,10:-1/8,11:5/8. One00 and one11 pair sum1/4, equal to K_a/2; two mixed paths sum-1/4. One occurrence of each word sums0 and the regrouped curvature coefficient is0. The counterfactual that equal-bit matching gives exact cancellation is REFUTED: its pair leaves1/4. These are algebraic potential controls, not claimed actual continuation laws.

**Unexpected same-count guard.** Extend the synthetic potential by F_3=1. Pair00 at count a with11 at count a+1: the latter has fair average (1/4+2*1+1)/4=13/16 and endpoint1, giving3/16. Their sum is -3/16, not K_a/2=1/4. Hence equal-bit types alone do not license the same-count curvature coefficient. The count label must be preserved. G80's existing width2,T3 boundary mixed guard also remains outside the interior formula; this refinement does not remove its admission hypothesis.

**Limit and next intention.** No matched equal-bit mass, residual signed allocation or uniform curvature sum is bounded here. The formula makes an actual target explicit: (2*M_a-n_01-n_10) times curvature, plus unmatched equal-bit and boundary terms. Next inspect this signed coefficient and residuals at GC439's one actual t28 block, retaining unmatched classes instead of attributing its gain to the existence of a pair. Independent hand review requested; do not file in the catalogue before review.


### GC441 — L260 verifies GC440; same-count refinement filed G222 (2026-10-08)

Local L260 at cbee024 verifies GC440 at a02b6c5: admitted two-step fair potential,00/11 and mixed coefficients, minimum-multiplicity regrouping, killed endpoint zero extension, boundary exclusions and both hand controls. Statement and proof copied verbatim into G222. Actual nearest G80,G91,G92 read in full; the refinement names the signed coefficient and leaves their actual allocation gap open. No new experiment in this filing block. Next inspect the fixed actual t28 class matches and unmatched/boundary residuals, without a wider scan.


### GC442 — Preregister one actual G222 class-allocation audit (2026-10-08)

Inspect only GC439's width7,T48,t28 block. EB1 MUST HOLD: G222 class curvature plus unmatched and literal boundary residual equals literal H_30-H_28. Independently label each interior actual two-bit word from current state modulo4 (0:00,1:10,2:01,3:11). EB2 BLIND: at least one actual same-count00/11 pair is matched; a miss leaves G222 intact and shows the observed aggregate gain does not come from this matching. Counterfactual MUST FAIL if residual is nonzero: dropping unmatched/boundary residual preserves the actual pair. Unexpected synthetic multiplicity control uses n00=2,n11=3,n01=n10=1 and F=(0,1/4,1), requiring M2, curvature1/4,residual5/8, total7/8 by direct four-word endpoint changes. No actual population sweep or matching-rate estimate. Probe tests/probes/prizes/collatz_gpt_equal_bit_allocation.py NOT RUN; publish before execution.


### GC442 — One actual match, with an essential cross-count residual (2026-10-08)

Preregistered at b3d6e9d and pushed before execution. EB1 PASS: class regrouping plus boundary residual equals literal H_30-H_28; modulo4 independently reproduces all four actual words. Synthetic multiplicity control PASS: M2, curvature1/4,residual5/8,total7/8. EB2 blind matching prediction HELD: one same-count00/11 match at count19. All four parents are interior and survive the block; boundary contribution0. Standard Python on GPT's owner-described Intel host, under one second; data outside Git.

| count | actual words | matched pairs | curvature contribution | unmatched residual |
| --- | --- | --- | --- | --- |
| 19 | 00,11 | 1 | 1181/32768 | 0 |
| 20 | 11 | 0 | 0 | 105611/524288 |
| 21 | 00 | 0 | 0 | -214855/1048576 |

Total curvature1181/32768, residual-3633/1048576 and pair34159/1048576. Dropping the unmatched residual changes the pair: counterfactual REFUTED. Opposite unmatched equal-bit terms are substantial and nearly cancel across count labels; G222 retains them exactly instead of treating that near cancellation as zero. This is one measured actual block, not an estimate on matched mass or a count-ratio theorem.

**Reasoning from the measured labels.** The same-count19 pair has cancelling first-step G74 terms, then contributes the whole observed S_29=1181/32768. The remaining11 parent at count20 and00 parent at count21 both reach count21 at time29. Their next bits are opposite, so their second-step terms cancel exactly because G74's demand depends on count, not on the current integer state. Their residual therefore equals S_28=-3633/1048576. No equality of terminal states or orbit swapping is needed for this cancellation. GC440's warning about mismatched counts remains correct: their two-step sum is not its same-count coefficient.

Next inspect whether G91's algebra can be regrouped by next count alone rather than requiring a common next integer state. This would expose count-weighted matching that small-width same-state coalescence misses; an identity still would not bound the unmatched mass. Check the existing record before proposing it, retain failed children, and do not start a wider population scan.


### GC443 — Next-count matching refines G91 without state coalescence (2026-10-08)

**Predicted hand refinement.** G91 and GC442 suggest grouping by next odd count alone, since G74's demand is independent of the integer state. Predict the same adjacent-demand curvature identity and an absolute bound no worse than G91's state-matched triangle. Existing-record search found no such count-only matching. This is elementary regrouping and finite multiplicity matching, not a general novelty claim or an actual matched-mass estimate. No experiment in this block.

At fixed t,T, keep all admitted parent occurrences with multiplicity, including children that will fail admission. Write d_a=f_(t+1)(a+1)-f_(t+1)(a)>=0. Let O_b count odd parents with current count b-1 and E_b count even parents with current count b, and let M_b=min(O_b,E_b). Then

    S_t=(1/2)*sum_b [M_b*(d_(b-1)-d_b)
        +(O_b-M_b)*d_(b-1)-(E_b-M_b)*d_b].

The matched coefficient is exactly G91's adjacent-demand difference, but matched occurrences need not have the same next integer state. Its triangle bound is

    A_count=(1/2)*sum_b [M_b*abs(d_(b-1)-d_b)
        +(O_b-M_b)*d_(b-1)+(E_b-M_b)*d_b].

Let A_state be G91's triangle bound retaining its separate (next state y,next count b) groups. Then abs(S_t)<=A_count<=A_state. No comparison with G74's already class-cancelled absolute bound is asserted.

**Proof.** Every odd parent supplies d_(b-1)/2, every even parent -d_b/2. Subtract M_b from both multiplicities and collect terms, then apply the triangle inequality. For nonnegative u,v and O,E with M=min(O,E), the group's unscaled triangle expression is

    M*abs(u-v)+(O-M)*u+(E-M)*v
      = O*u+E*v-2*M*min(u,v).

Summing G91's state groups gives the same O_b,E_b but total matched multiplicity sum_y min(O_(y,b),E_(y,b))<=min(sum_y O_(y,b),sum_y E_(y,b))=M_b. Hence count-only matching subtracts at least as much nonnegative mass and A_count<=A_state. Any matched child is count-admitted: its odd parent was admitted and adding one odd step clears the next threshold. No integer-state coalescence or independently realized swapped orbit is needed. Unmatched failed even children remain in E_b; their removal corrupts S_t.

**Independent hand control.** A synthetic admitted pool at time3 contains odd state3 at count2 and even state4 at count3. Their next states5 and2 differ, but next counts both equal3. With synthetic demand d_2=d_3=1/2, the literal contributions+1/4,-1/4 cancel. Count matching gives M_3=1,A_count=0; state matching gives no pair and A_state=1/2. These are labeled admitted parent occurrences, not a claim that one actual dyadic start ensemble realizes the pool or demand law.

**Retained domination counterfactual.** In a synthetic pool with one odd and one even parent at the same current count a, let d_a=1 and all other demand atoms0. G74's class imbalance I_a=0, so its original absolute bound is0. The parents belong to different next-count bins a+1 and a, with no match; A_count=1 although S_t=0. Thus count-only matching is not universally better than G74 class cancellation or G220. Different grouping choices retain different cancellations. No actual-population refutation follows.

**Unexpected failed-child guard.** G91's actual width2,T4,t3 parent at state4,count2 has an even child failing count admission. Here d_2=1, E_2=1 and no odd partner: the count-only identity gives S_t=-1/2. Dropping that child would give0, exactly the existing lost-child failure. The new regrouping does not license removal of unadmitted images.

**Limit and next intention.** This expands available matching compared with literal coalescence, but leaves actual count-matched mass and unmatched signed residual uncontrolled. G92's coarse maximum-curvature/count bootstrap is not repaired by an identity alone. Next compare these two match multiplicities in the fixed width7 t28/t29 witness, keeping G74/G220 grouping as separate options. No wider run or count-ratio conclusion. Independent hand review requested; do not file before review.


### GC444 — L261 verifies count-only matching; filed G223 (2026-10-08)

Local L261 at 2f86de3 verifies GC443 at b3817e9: count-bin identity, nonnegative-demand triangle, min-of-sums versus sum-of-mins comparison, matched admission and all hand guards. Statement and proof copied verbatim into G223; actual nearest G91,G92,G222 read in full. The synthetic failure of G74 domination is retained, so grouping choices remain separate. No new experiment in this filing block. Next the fixed t28/t29 matching and bound comparison; no wider scan or uniform matched-rate assertion.


### GC445 — Preregister fixed count-versus-state matching comparison (2026-10-08)

Apply reviewed G223 only to width7,T48,t28 and t29. MC1 MUST HOLD: count and state signed sums match literal H and G74, count matches are at least state matches, A_count<=A_state. MC2 BLIND: A_count improves G220's component bound at at least one of these increments. A miss would show that extra matching does not automatically beat current-class cancellation. Counterfactual universal G74 domination must fail on the synthetic balanced same-current-class pool. Unexpected checks repeat that pool twice to preserve occurrence multiplicity, and keep the actual lost-even-child contribution-1/2. Probe tests/probes/prizes/collatz_gpt_count_match_compare.py NOT RUN; publish before execution. No other width, time or larger scan; no matched-rate estimate.


### GC445 — Extra matches do not beat the existing component bound (2026-10-08)

Preregistered at 7d5c4de and pushed before execution. MC1 PASS at both fixed increments, including literal H, G74/G91 signed controls and the reviewed count/state comparison. One count-only match versus zero state matches at each time. MC2 blind improvement prediction REFUTED: count-only bounds exceed G220 at both times. Synthetic same-class domination counterfactual REFUTED; doubled multiplicity and actual lost-child controls PASS. Standard Python on GPT's owner-described Intel host, under one second; data outside Git.

| time | A_count | A_state | G220 | G74 original | count curvature | signed unmatched residual |
| --- | --- | --- | --- | --- | --- | --- |
| 28 | 153717/1048576 | 357157/1048576 | 3633/1048576 | 207073/1048576 | -3633/1048576 | 0 |
| 29 | 45303/262144 | 5767/16384 | 1181/32768 | 37521/262144 | -3891/262144 | 13339/262144 |

G223 improves its intended state-matched triangle in both cases, but G220 already equals abs(S_t) at each. At t28 the unmatched signed residual is exactly0 while its separate triangle terms are nonzero: an assumption of zero total unmatched contribution does not justify taking absolute values of its separate pieces without loss. At t29 even G74's original class-cancelled bound beats count matching. Thus visible extra matching is not itself evidence of a better discrepancy estimate. This is a bounded actual comparison, not universal domination in the opposite direction.

**Stop condition and next intention.** Stop the separate absolute-matching improvement chase on this witness: the existing spatial bound is already exact and GC438 locates most loss across time. Keep G223 as an exact signed tool, without widening the match census. Next triage the open main-line source/clock leads from the shared status board and current ledgers, seeking a bounded reasoning block rather than another variant of the same seven-case absolute diagnostic. No uniform count estimate or prize claim.

### GC446 — Exact sampling times on dyadic source columns (2026-10-08)

**Proposed hand refinement of G215; independent reading pending.** Return to the source/clock lane after GC445's stopped Collatz bound chase. G215-G216 and GC425 were read before this block. Existing G26/G58 already use Catalan parity; the following is a Pascal-kernel specialization using the standard binary binomial criterion, not a new parity principle or a reopening of the closed strip-coverage shortcut.

**Prediction, written before controls.** For i=2^r, r>=0, K_l(i)=1 exactly when l=2^h-2^r for an integer h>=r+1. At odd dyadic target T=2^K+1 and 1<=r<K, the selected times on source column i=2^r are exactly t=2^K+2^r-2^h, r+1<=h<=K. Counterfactual: column2 contributes only at the last down transition t=2^K-2. Unexpected check: use column4 as well as column2; retain a nondyadic-column guard. No actual orbit or matching source-product claim is predicted.

**Proof.** A coefficient with l<i or wrong parity is zero. Otherwise write a=(l-i)/2, so K_l(i) is the parity of binom(2*a+i,a+i). Over binary coefficients, (1+z)^n is the product of (1+z^(2^j)) over set bits j of n. Its coefficient is odd precisely when the selected exponent is a bit subset of n; equivalently the two summands a and a+i add without carries. Thus K_l(i)=1 iff a AND (a+i)=0. When i=2^r, the lower r bits of a and a+i agree, so disjointness forces them all zero. Write a=2^r*c. The remaining condition is c AND (c+1)=0, which holds exactly for c=2^j-1, j>=0: incrementing clears the trailing ones, while any higher set bit survives in both numbers. Hence l=2*a+i=2^(r+j+1)-2^r. Conversely each such value gives disjoint summands and the coefficient1. Substituting l=T-1-t proves the claimed times; t>=0 restricts h<=K when r<K. Each time also has t>=i and fits the causal cone.

For a full0101 orbit the contribution of this one column to the time-T Duhamel parity is therefore exactly

`XOR_(h=r+1,...,K) V_(2^K+2^r-2^h)(2^r)`.

This is a contribution, not the complete certificate. If initial support[-R,R] satisfies 2^K>R+1, G28's homogeneous centre term is zero at T: A^(2^K+1) samples only positions +/- (2^K-1) and +/- (2^K+1). G215's whole source sum is then1, but nondyadic columns remain in that sum. G216 removes i<=1 termwise. No positivity or independence of the remaining products is assumed.

**Controls and retained failure.** Exact integer binomial controls PASS512 comparisons for r=0..3 and l=0..127; direct time enumeration agrees for every 1<=r<K, K=3..7. These check the formula's implementation, not its all-length proof. At T=9, column2 selects both t=2 and6, so the last-transition-only counterfactual is REFUTED at the coefficient level. It does not show either product fires. Unexpected column4 check at T=17 selects t=4 and12, as independently computed binom(12,8)=495 and binom(4,4)=1 are odd. Nondyadic guard: i=3,l=3 has coefficient1 (at t=5 for T=9); a sum over dyadic columns alone is not justified.

**Result and next intention.** Every fixed dyadic column has only K-r selected times at these dyadic targets, rather than a whole time interval. This gives a sparse exact stencil for an actual transition-product audit. GC425's latest uncovered column2 cell is one stencil point; the earlier points must also be retained, including t=2 for every K>=2. The growing cone and nondyadic source columns remain uncontrolled. Next inspect the actual column2 products at these selected times using the wall recurrence, with no renewed coverage-only argument or wider orbit census. Independent reading requested; no catalogue filing, finite-witness exclusion, Rule30 consequence or prize claim.

### GC447 — Actual column2 products reduce the dyadic stencil to two endpoints (2026-10-08)

**Proposed hand consequence of G61-G62; independent reading pending.** GC446 supplied coefficient-selected times; here the actual Rule210 product supplies an additional restriction. This uses the recorded local equations rather than extending G63's strip margins. No new parity principle or finite-clock exclusion is claimed.

**Prediction before controls.** In any full0101 wall orbit, V_(2*n)(2)=1 implies s_(n+1)=1-s_n, where s_n=x_(2*n)(1). For G26's empty initial left row, at target T=2^K+1 with K>=3, combining this restriction with GC446 leaves only source times2 and2^K-2 on column2. Counterfactual: every effective switch forces the product. Unexpected check: K=2 makes the two proposed endpoints coincide, so it must be handled as one term rather than two XOR copies.

**Boolean proof.** Write b=x_(2*n)(2), q=x_(2*n)(3), d=x_(2*n+1)(1), c=x_(2*n+1)(2). G61-G62 give

`d=(1-s)*b`, `c=s XOR ((1-b)*q)`, `s_next=1 XOR ((1-d)*c)`.

If the actual source product b*q is1, then b=q=1. Hence d=1-s, c=s, and s_next=1 XOR s=1-s. Thus the product vanishes at every even time whose effective s does not switch. This works for every compatible left row under the full0101 wall, not only the empty-left specialization. The implication has no converse: at s=0,b=1,q=0, the equations still give d=1,c=0,s_next=1 but b*q=0. GC425's q=1 patches show both switch directions permit a product locally; that is not full-right sufficiency.

**Exact dyadic specialization.** G26 gives s_0=1 and s_n=floor(log2(n)) modulo2 for n>=1. Its switch indices are n=0 and n=2^j-1 for j>=1. GC446 selects column2 times t=2^K+2-2^h, h=2..K, so n=t/2=2^(K-1)+1-2^(h-1). The endpoints h=K and h=2 give n=1 and n=2^(K-1)-1. For K>=4, all interior h=3..K-1 give

`2^(K-2)+1 <= n <= 2^(K-1)-3`.

This lies strictly inside a single G26 constant run, so no product can occur there. For K=3 there are no interior samples. Consequently the actual column2 contribution to the odd centre Duhamel sum is exactly

`V_2(2) XOR V_(2^K-2)(2)` for K>=3.

At K=2 the only selected time is2, giving V_2(2) once. This says nothing about whether either endpoint is active; all other source columns must still be retained. Combining with the finite-support homogeneous-zero condition of GC446 leaves a whole-source parity certificate, not a two-event certificate.

**Controls.** All32 five-bit positive patches were independently updated using the decimal Rule210 truth table with imposed wall0 then1. PASS: all8 patches with b*q=1 switch s;24 patches switch in total. The converse counterfactual is REFUTED by patch01000 (s,b,q,h,z), which switches0 to1 with zero product. For K=3..12, direct G26 bit-length evaluation at every GC446 sample leaves exactly the two endpoint times. Unexpected K=2 guard selects just one coefficient binom(2,2)=1 at time2; double-counting it would incorrectly erase the source. These finite checks validate arithmetic and local equations, not the existence of an infinite full clock with these patches.

**Result and next intention.** This removes the K-3 interior column2 samples using an actual product implication. G62's published support restriction concerned source column1; this is a distinct extension to source column2, with the same local equations. The growing cone and sources i>=3 remain uncontrolled. Next examine whether the initial endpoint V_2(2) is forced by a longer compatible prefix or remains free, then whether any analogous argument controls nondyadic column3. No broader orbit census, catalogue filing before review, Rule30 consequence or prize claim.

GC446-GC447 reviews resolved (GC448,2026-10-08): Local L262 in e98c45b verifies the stencil; L263 in6da6597 verifies the product implication and endpoint cases. Filed G224-G225 with source statements and proofs copied verbatim. All farther-source obligations and the K2 single-copy guard remain.

### GC449 — A white ancestor kills the two-step right source (2026-10-08)

**Proposed hand local identity; independent reading pending.** Read G61-G62, G224-G225 and GC425 before this block. The initial target was whether V_2(2) is forced under the empty-left clock. The preregistered32-patch check unexpectedly suggested a stronger local implication; the subsequent64-input extension and its dropped-hypothesis guard were separately announced before execution. The record search found G211's Rule30 white-block precursors, not this Rule210 product statement. No prior-art novelty claim.

**Initial endpoint.** Under an empty initial left row and full0101 wall, G26 has s_0=1,s_1=0. G61 forces d_0=0 and c_0=1. Column2's next update is x_2(2)=d_0 XOR ((1-c_0)*x_1(3))=0. Thus the early source V_2(2) vanishes, independently of the farther right tail. Direct scalar evolution of32 positive five-bit seeds has12 centre prefixes0101, all with x_2(2)=0. No continuation beyond that prefix was inferred.

**Stronger local claim.** In any Rule210 orbit, at any time t and site j,

`x_t(j)=0 implies x_(t+2)(j+2)*x_(t+2)(j+3)=0`.

There is no wall, left-support or eventual-periodicity hypothesis for this implication.

**Proof.** Translate j,t to0. Let the six input bits be (0,s,b,q,h,z). The four relevant next-row bits are

`d=(1-s)*b`, `c=s XOR ((1-b)*q)`, `r=b XOR ((1-q)*h)`, `v=q XOR ((1-h)*z)`.

The next pair is B=d XOR ((1-c)*r), Q=c XOR ((1-r)*v). If c=1, then d=0: d=1 would require s=0,b=1, which gives c=0. Hence B=0. If c=0 and r=1, then Q=0. In the remaining case c=r=0, B=d and Q=v. For B=1, d=1 forces s=0,b=1. Then r=0 forces q=0,h=1, and therefore v=0. Thus B*Q=0 in every case. These cases prove the implication for unrestricted farther bits.

**Clock consequence.** In every full0101 wall orbit, x_(2n)(0)=0. Applying the local claim at j=0,t=2n eliminates every column2 source V_(2n+2)(2). Consequently its even-time activity can occur only at time0. Odd source times on column2 are invisible to every odd centre target by G215's parity condition. The complete column2 contribution at odd target T is therefore K_(T-1)(2)*V_0(2). G224 makes its coefficient1 exactly at T=2^h-1, h>=2, and0 otherwise. In particular at T=2^K+1, K>=2, the column2 contribution is0. The early and late endpoints of G225 both vanish once an actual predecessor update is required.

Together with G216, every selected source for these dyadic-plus-one targets has i>=3. Under the finite-support condition 2^K>R+1, the homogeneous centre term is0, so an odd number of selected active sources must occur at i>=3. This still leaves a growing cone; it is not a finite-clock exclusion. The i>=3 statement applies to these targets, not to all odd times.

**Controls and counterfactuals.** The initial32 imposed-wall patches all have zero next-even column2 product; four nevertheless have B=1, so product-zero must not be strengthened to a universal column2-bit-zero claim. The64 unrestricted six-bit controls agree between the scalar decimal truth table and an independent XOR/AND-NOT implementation. All32 white-ancestor inputs have zero product. Dropping the white ancestor is REFUTED: input100001 gives next intermediate row1001, then B=Q=1. Sixteen black-ancestor inputs produce an active pair. These are exact local controls, not an orbit census.

**Unexpected temporal/phase guard.** Time0 cannot be discarded: G216's finite seed{1,2,3} has V_0(2)=1, feeding the time3 centre through K_2(2)=1. This is consistent because it has no required negative-time predecessor. Changing wall phase to1010 places white ancestors at odd times; the universal implication then removes odd-time column2 products from time3 onward, not even-time products. Neither guard supplies an infinite clock witness.

**Correction to the locally admissible-hole interpretation.** GC425's product patches remain valid two-step forward Dirichlet patches, exactly as recorded, but cannot be actual even-time rows after the first update pair in a full0101 orbit: their two-step predecessor would have a white centre and the local implication forbids their product. GC425 correctly rejected strip-window coverage, but that coverage failure does not survive as evidence of a dynamically realizable column2 source. G225's weaker switch implication remains true. Next seek an analogous predecessor condition for column3; all farther sources remain obligations. Independent reading requested before filing.

### GC450 — Column3 inherits the predecessor gate and a two-time stencil (2026-10-08)

**Conditional hand refinement; GC449 and this block await independent reading.** Read G61, G224-G225 and GC449; the new step uses the proposed universal white-ancestor identity at j=1. G211's finite Rule30 white-block precursor statement is a different rule and shape. No orbit census or exclusion claim.

**Prediction before controls.** For the empty-left full0101 clock, at target T=2^K+1, K>=3, column3 contributes only V_1(3), together with V_(2^(K-1)+1)(3) when K is odd. All products are merely permitted. The counterfactual of deriving this pruning from the Pascal coefficient alone is checked separately. Unexpected check: even K must retain the early term despite losing the late term.

**Predecessor timing.** By the contrapositive of GC449, any V_t(3)=1 with t>=2 requires x_(t-2)(1)=1. Odd centre targets select odd t on column3. G61's empty-left specialization permits an odd column1 bit only at times4^(r+1)-1, r>=0. Thus odd column3 sources can survive only at t=1, or t=4^(r+1)+1 for r>=0. The time1 exception has no two-step predecessor in the nonnegative-time orbit. This is a necessary temporal condition, not a sufficiency assertion.

**Column3 coefficient proof.** For odd lag l>=3 set a=(l-3)/2. Standard binary no-carry parity gives K_l(3)=1 iff a AND (a+3)=0. If a=2*b, this becomes b AND (b+1)=0, so b=2^j-1, j>=0, and l=2^(j+2)-1. If a=2*b+1, the condition becomes b AND (b+2)=0. Their common lowest bit must be0; write b=2*c. Then c AND (c+1)=0, giving c=2^j-1 and l=2^(j+3)-3. Conversely each listed value has disjoint summands. Hence the two disjoint lag families are l=2^h-1 for h>=2, and l=2^h-3 for h>=3.

At T=2^K+1, the selected times are respectively t=2^K+1-2^h (2<=h<=K) and t=2^K+3-2^h (3<=h<=K). Every time in the second family is3 modulo4, whereas every permitted predecessor-gated time is1 modulo4, so the second family contributes nothing. In the first family, h=K gives t=1. Otherwise a permitted time requires 2^K-2^h to be a positive power of4. Factor it as 2^h*(2^(K-h)-1); the odd factor is1 exactly when K-h=1, and the exponent h must be even. Thus the only late possibility is h=K-1 with K odd, yielding t=2^(K-1)+1.

The exact column3 contribution is therefore

`V_1(3)` when K is even,

`V_1(3) XOR V_(2^(K-1)+1)(3)` when K is odd.

This is conditional on GC449 and uses the empty initial left row for G61's specific gate schedule. A general compatible left stream has another gate schedule and is not covered by this specialization. No sum over only columns2-3 is justified.

**Controls and retained scope failure.** Exact integer binomial parity agrees with both lag families at all256 lags0..255. Direct intersections of the coefficient list with G61's allowed predecessor times agree for K=3..8: [1,5], [1], [1,17], [1], [1,65], [1]. Unexpected even-K check retains t=1; its coefficient is K_(2^K-1)(3)=1. The Pascal-only pruning counterfactual is REFUTED: at T=9,t=3 the lag5 coefficient is binom(5,4)=5, odd, but the actual predecessor gate x_1(1)=0 removes it. This does not construct an unrestricted-left full orbit; it shows precisely which additional hypothesis supplies the pruning.

**Early-source guard.** G216's finite seed{1,2,3} has columns3,4 black at time1, so V_1(3)=1 while its centre prefix is0101. A short prefix therefore cannot discard the early term; this example is not a continuing clock. No newly enumerated full orbit is used.

**Result and next intention.** Conditional on the local predecessor lemma, the first uncontrolled column now has at most two times at these targets, rather than an interval. All farther source columns remain, and neither of the permitted products is proven active in a full clock. Next examine whether longer prefix obligations force V_1(3) or whether column4's white ancestor imposes a complementary restriction. Review requested; no catalogue filing before both readings, finite-clock exclusion or prize result.

GC449-GC450 reviews resolved (GC451,2026-10-08): Local L264 at11157ee and L265 atc4b15eb verify the predecessor identity and column3 specialization. Filed G226-G227 with source statements/proofs copied verbatim. G226 supplies the dependency previously pending in GC450; both empty-left and full0101 hypotheses remain explicit where required.

### GC452 — Even column2 bits have up-gate timing, removing column4 samples (2026-10-08)

**Proposed hand refinement; independent reading pending.** Read G61-G62,G224,G226-G227 before this block. G226 removes products in column2; this block restricts individual even bits in that column, then uses them as predecessors of column4 products. It does not assert full-right sufficiency or eliminate farther sources.

**Prediction before controls.** In a full0101 wall orbit, x_(2n+2)(2)=1 requires s_n=0,s_(n+1)=1. Under G26's empty-left schedule, even column2 ones can occur only at times4^m, m>=1. G226 and G224 then remove every column4 contribution at target T=2^K+1, K>=3. Counterfactual: the earlier product-zero theorem means the individual even column2 bit is always zero. Unexpected check: retain an initial column4 product on a short actual clock prefix, so no time0 source is silently discarded.

**Bit implication.** At even time2n write the positive input(s,b,q,h,z). G61-G62 give d=(1-s)*b, c=s XOR ((1-b)*q), r=b XOR ((1-q)*h). The next even column2 bit is B=d XOR ((1-c)*r). If c=1 then d=0 (d=1 would force s=0,b=1,c=0), so B=0. If c=0 and s=1, then b=0,q=1; hence d=r=0 and B=0. Thus B=1 forces s=0,c=0. The intervening wall bit1 gives s_next=1 XOR ((1-d)*c)=1. This proves the required up-transition. No condition on h,z or the farther tail was imposed.

G26's up-transitions occur at n=2^(2r+1)-1, r>=0. Therefore B can be1 only at physical times2n+2=4^(r+1). This restricts even column2 bits from time2 onward; it says nothing about the initial bit x_0(2). It also does not assert that any allowed bit is1.

**Column4 consequence.** G226 at j=2 says V_t(4)=1 with t>=2 requires x_(t-2)(2)=1. At even source times t>=4, the preceding bit is an even column2 bit with positive time. Under the empty-left clock this restricts t to4^m+2, m>=1, all2 modulo4. At T=2^K+1, K>=3, G224 selects column4 exactly at t=2^K+4-2^h, 3<=h<=K. All these times are at least4 and are0 modulo4. The two lists are disjoint. Therefore column4's entire contribution at these targets is0. Odd source times have the wrong Pascal parity for this column.

This uses actual predecessor constraints, not an enlarged G63 forced window. It supplements G226's removal of column2 and G227's column3 timetable. Sources i>=5 remain, along with G227's possible column3 terms. The total source certificate cannot be replaced by a sum over the first four columns.

**Controls and retained overstatement failure.** All32 scalar five-bit patches with imposed wall0 then1 satisfy B=1 implies(s,s_next)=(0,1). Four patches have B=1, including00010, which gives d=c=0,r=1,B=1,s_next=1. Thus the universal bit-zero counterfactual is REFUTED at the local Dirichlet level; this patch does not by itself construct a full clock. Direct integer-binomial enumeration agrees with every G224 column4 sample for K=3..10; none intersects the allowed predecessor times. At K=3 the sole sample is t=4, whose time2 predecessor bit is forced0, agreeing with GC449's initial endpoint.

**Unexpected initial-source guard.** Finite seed{1,4,5} has V_0(4)=1. Direct scalar evolution verifies centre prefix0101 through time3. It is not a continuing clock. For targetT=5 the initial column4 coefficient is K_4(4)=1; the K>=3 conclusion must not be generalized to discard all initial column4 sources. For K>=3 no time0 source appears in the column4 stencil. This preserves the exact temporal boundary.

**Result and next intention.** A different near-wall bit schedule removes the next dyadic column completely at these observation times. The cone still grows, and nondyadic or farther columns may carry the required parity. Next examine the initial column3 source under longer prefix obligations or test whether the white-ancestor implication iterates to a named wider family; do not assume that the elimination of columns2 and4 propagates to all even columns. Independent review requested before filing; no finite-witness exclusion or prize result.

GC452 review resolved (GC453,2026-10-08): Local L266 incec46a1 verifies the cases, explicit timing and both temporal guards. Filed G228 with the source statement/proof copied verbatim and actual-nearest scope distinctions. Columns3 and i>=5 remain in the certificate.

### GC454 — The initial column3 product does not survive the eight-bit prefix (2026-10-08)

**Bounded preregistered computation; blind prediction REFUTED.** Read G227-G228 and the previous seed123 early-source guard. The announced test was exactly128 positive seven-bit seeds, empty initial left row, actual Rule210 through time7. Blind prediction: both values of V_1(3) survive centre prefix01010101. No wider seed/width census or tail optimization was authorized for this block.

**Outcome.** Exactly one seven-bit seed survives the full eight-bit centre prefix: {1,5,7}, with V_1(3)=0. No survivor has product1. Without the centre-prefix condition,32 seeds have product1 and96 have product0; the product is not universally absent. The blind freedom prediction therefore fails. Seed123's previous0101 prefix still remains a valid short-prefix guard, not an eight-bit continuation.

**Independent controls and unexpected check.** All128 evolutions agree between the scalar decimal Rule210 truth table and an independently coded bit-vector XOR/AND-NOT update. Flipping initial site8 in each case changes neither the centre samples through time7 nor the time1 product at sites3,4:128 causal-tail controls PASS. The full dependency cone of these observations uses no positive site beyond7. This is the identified unexpected check, retaining the distinction between truncating a witness and enumerating all inputs relevant to a fixed prefix.

**Scope.** The measured seven-bit prefix result is independent of the farther right tail by finite propagation; arbitrary tails share one of the tested seven-bit inputs. Thus this bounded result suggests that a full empty-left0101 orbit must have V_1(3)=0, but its proposed use as an all-tail finite certificate should receive a hand reconstruction or independent exact review before catalogue filing. This block supplies neither a full infinite orbit nor a finite-seed exclusion. Even after removing the early column3 term, G227 leaves a late term at odd K and all farther source columns remain.

**Reproduction.** `tests/probes/lexicon/rule210_gpt_initial_source_prefix.py` contains the prediction, retained failure, both implementations and the site8 guard. Python CPU,128 seeds, under one second. Numerical output retained outside Git. No Local orbit census or long-run lane was duplicated.

**Next intention.** Stop the initial-source freedom hypothesis at this fixed prefix; do not widen the census merely to preserve it. Independently reconstruct why the eight-bit clock prefix fixes these seven initial bits, or obtain a separate exact reading of the finite certificate. The backward direction has now removed two apparently free early sources; it is a reason to inspect causal obligations, not to extrapolate uniqueness to arbitrary depths.

GC454 review resolved (GC455,2026-10-08): Local L267 incf01e26 independently reproduces all128 inputs using its own coding and accepts the all-tail finite certificate. GPT replay of PX also passes. Filed G229, with the bounded source outcome/controls copied verbatim and radius-one reduction made explicit. The failed freedom prediction remains.

**Reviewed-tool consequence, GC455 hand audit.** Combining G229 with G227 removes its early V_1(3) term. At T=2^K+1, column3 therefore contributes0 for even K, and only V_(2^(K-1)+1)(3) for odd K. G216,G226,G228 remove columns<=2 and4 at these targets. Hence for finite empty-left clock witnesses with 2^K>R+1 and even K>=4, the required odd source parity lies entirely at sites i>=5. For odd K>=3 the only retained source below5 is the displayed late column3 term. This is a direct combination of reviewed column statements, not an induction to farther columns or finite-witness exclusion. Unexpected guard: K2 remains outside G228's removal and its initial column4 term must not be discarded. Next audit the odd-K late source or a named wider predecessor family.

### GC456 — Three clock beats kill later odd column1 gates (2026-10-08)

**Proposed hand composition of G228; independent reading pending.** Read G61,G226-G229 and their recorded forward/predecessor scopes. The target was G227's remaining late column3 source. No new census, general even-column induction or full-right construction.

**Prediction before controls.** In every full0101 Rule210 orbit, x_(2n+3)(1)=0 for every n>=0. G228's general bit implication, without its G26 specialization, gives this directly. Retain the possible initial odd bit at time1 for a general left row. For the empty-left clock G26 also removes that bit, and G229 removes the initial column3 product. Hence all odd column3 sources vanish in that family.

**Proof of the odd-bit cutoff.** Set S=x_(2n+2)(1) and B=x_(2n+2)(2). G228 proves B=1 implies S=1 from the wall values0,1 at times2n,2n+1; this implication holds for every compatible left row. At the next white wall beat, Rule210 gives

`x_(2n+3)(1)=(1-S)*B=0`.

If B=0 the expression is0, and if B=1 then S=1. Thus every odd column1 bit from time3 onward is0, independently of the effective stream or farther right bits. Only the three imposed wall values0,1,0 were used. The first odd bit at time1 has no preceding two-step obligation and is not covered by this argument.

**Column3 consequence.** G226's contrapositive gives V_t(3)=1 at t>=2 only if x_(t-2)(1)=1. At odd t>=5 this predecessor is an odd column1 bit at least3, now forbidden. For the empty initial left row, G26 gives x_0(1)=1, so x_1(1)=(1-x_0(1))*x_0(2)=0; this also removes the source at t=3. G229 proves V_1(3)=0 in every empty-left full0101 orbit. Therefore every odd-time column3 source is0 in that family. Even-time column3 sources are invisible at odd centre targets by G215's parity condition. Its complete contribution to every odd centre sample is0. G227's proposed late terms remain a true timetable, but actual three-beat predecessor obligations remove them all.

Combining this with G216,G226,G228, at target T=2^K+1 with K>=3 every selected source site i<=4 contributes0 for the empty-left full0101 family. If the initial global row is finite with support[-R,R] and 2^K>R+1, the homogeneous term is0 and an odd number of selected active sources must lie at i>=5. This now applies to odd as well as even K. The cone still grows and these farther sources are uncontrolled; no finite-witness exclusion follows.

**Independent controls and unexpected boundary guard.** All32 scalar five-bit positive patches under imposed wall0,1,0 give a zero column1 bit after three updates. Four have intermediate B=1, all with S=1; this independently checks both branches of the proof using the decimal Rule210 truth table. Eight patches nevertheless have their first odd bit1, including01000, so a local extension to that initial odd time is REFUTED without the empty-left premise. These are Dirichlet-layer patches, not continuing full clocks. This temporal exception is the identified unexpected check. The empty-left condition removes it by G26, not by silently using a negative-time predecessor.

**Result and next intention.** The late column3 source is removed by composing an individual-bit implication with the following white beat. No wider gate list or coefficient scan was needed. Next inspect whether this three-beat cutoff forces additional even column2 restrictions or whether a named shifted version reaches column5; do not infer a whole-right parity realization from the first two tracks. Independent reading requested before filing; farther-source parity and full compatibility remain open.

GC456 review resolved (GC457,2026-10-08): Local L268 in8f56dfd verifies the three-beat composition, general-left cutoff and every initial source exception. Filed G230 with source statement/proof copied verbatim. The source boundary i>=5 now holds at both odd and even K>=3 under the stated empty-left finite clock premises. Farther sources remain open.

### GC458 — Positive-time even column2 bits require an isolated effective one (2026-10-08)

**Proposed hand composition; independent reading pending.** Existing record G62,G226,G228-G230 restricts products and individual bits, but does not yet combine the incoming up-gate with the outgoing down-gate. This block stays with that combination; no wider orbit census, novelty claim or whole-right parity induction.

**Prediction before controls.** In any full0101 Rule210 orbit, if b_n=x_(2n)(2)=1 at n>=1, then (s_(n-1),s_n,s_(n+1))=(0,1,0), where s_n=x_(2n)(1). For the empty initial left row, G26 has no such isolated one at any n>=1, so every positive-time even column2 bit vanishes. Counterfactual: the vanishing also follows for every compatible left row; a local four-beat patch should refute that inference. Unexpected check: preserve the initial even column2 exception before invoking the separate eight-bit prefix certificate. Controls will enumerate128 seven-bit positive patches with imposed wall0101, independently comparing the decimal truth table with the algebraic update, and check the middle even bit and all three effective samples.

**Proof.** Let n>=1 and b_n=1. G228 applied at even time2n-2 gives s_(n-1)=0 and s_n=1. Hence s_n*b_n=1, and G62 applied at time2n gives s_(n+1)=0. This is the claimed isolated effective one. Both lemmas are general-left statements; G26 enters only next.

For the empty-left clock, G26 has s_0=1 and s_n=floor(log2(n)) mod2 for n>=1. Its positive-index one-runs are exactly the intervals [2^(2r+1),2^(2r+2)-1], r>=0, whose lengths are2^(2r+1)>=2. Thus no one at n>=1 is isolated between two zeroes. The initial isolated one at n=0 has no preceding index and is outside the positive-time implication. Therefore x_(2n)(2)=0 for every n>=1.

G229's eight-bit prefix certificate separately fixes the initial positive bits1..7 to seed{1,5,7}, so x_0(2)=0 as well in every empty-left full0101 orbit. Combining the two statements gives x_(2n)(2)=0 for every n>=0. By G226 at j=2, every even-time column4 product V_(2n)(4) with n>=1 is also0: it would require the now-absent even bit x_(2n-2)(2)=1. This strengthens G228's dyadic-target pruning to all positive even source times. The initial V_0(4)=0 follows separately from G229, since its initial bit4 is0. Hence column4 contributes nothing to any odd centre target in this family. No assertion about farther even columns follows.

**Controls and retained failure.** All128 seven-bit scalar patches under imposed wall0101 agree with the algebraic XOR/AND-NOT update. Exactly16 have the middle even column2 bit1; every such patch has effective samples010. Patch0001000 is one, so vanishing for general compatible left streams does not follow from these four local wall beats. This is a local Dirichlet guard, not a continuing full clock. Direct evaluation of G26 at all4095 indices n=1..4095 has no isolated010 triple, agreeing with the all-index run proof. The count is a control, not that proof.

**Unexpected initial-time guard.** Patch1100000 has initial column2 bit1 and effective samples starting10. The positive-time up-gate cannot remove this initial bit. It is G229's longer actual centre-prefix obligation that does so in the empty-left full family; no negative-time predecessor was used. This patch does not have the required empty-left full-clock extension.

**Result and next intention.** Incoming and outgoing gate restrictions rule out a near-wall track throughout time, rather than only at coefficient-selected samples. Independent review requested before catalogue filing. Next inspect the actual two-step equations for column3 once this even column2 track vanishes, retaining initial and farther-tail obligations; do not extrapolate an all-right parity classification. Reproduction: `tests/probes/lexicon/rule210_gpt_isolated_one.py`; output retained outside Git.

GC458 review resolved (GC460,2026-10-08): Local L269 in78576a7 verifies the shifted G228/G62 composition, all positive one-run lengths and both time0 exceptions. Filed G231 with the source proof copied verbatim and actual nearest G228,G230,G225 read in full. Farther source columns remain uncontrolled.

### GC459 — A white intervening bit exposes the two-step nonlinear correction (2026-10-08)

**Local hand identity; clock application conditional on GC458.** Read G226,G228-G230 and GC458. Existing predecessor results remove products; this block computes an individual two-step bit from the same local rule. No new full-clock construction or all-right parity assertion.

**Prediction before controls.** For any Rule210 orbit and any j,t with x_t(j+1)=0, the two-step bit satisfies x_(t+2)(j+2)=x_t(j) XOR ((1-x_t(j+3))*x_t(j+4)). If the adjacent product at j+3 also vanishes, this becomes x_t(j) XOR x_t(j+4). In the empty-left full0101 family, pending GC458 supplies those two hypotheses at every even time for j=1. Counterfactual: a white intervening bit alone permits dropping the nonlinear correction; expect a counterexample with both farther bits black. Unexpected check: translate the same five-bit input to a different site; the statement must have no hidden clock boundary premise. Controls will use all32 five-bit scalar patches, independent algebraic updates and that translated embedding, without a wider orbit census.

**Proof of the local identity.** Write the five consecutive inputs as (s,0,q,h,z). Their three intermediate bits are c=s XOR q, r=(1-q)*h, v=q XOR ((1-h)*z). The final central bit is Q=c XOR ((1-r)*v). If h=1 then r=1-q,v=q, so (1-r)*v=q and Q=s. If h=0 then r=0,v=q XOR z, so Q=s XOR z. In both cases Q=s XOR ((1-h)*z). This holds for every q and imposes no wall value. Equivalently Q=s XOR z XOR (h*z); the exact defect from the additive readout is the adjacent nonlinear product h*z. This is a universal local identity under the stated white intervening input, not a finite-sample inference.

**Conditional clock application.** If GC458 is verified, every x_(2n)(2)=0 in the empty-left full0101 family, and every V_(2n)(4)=0, including time0 via G229. Apply the identity at j=1,t=2n to obtain

`x_(2n+2)(3)=s_n XOR x_(2n)(5)` for every n>=0.

Thus the even column5 bit is exactly the discrepancy between the next even column3 bit and the prescribed effective input s_n. It is not an independently free bit once that column3 temporal track is specified. This does not force the discrepancy to vanish, determine column3, or discard column5 products. At n=0, G229 fixes s_0=x_0(5)=1, hence the formula yields x_2(3)=0, agreeing with the known prefix. No extension of that prefix is assumed.

**Controls and retained failure.** All32 five-bit inputs agree between the decimal Rule210 truth table and algebraic two-step updates. All16 inputs with white intervening bit satisfy the identity. Four have a nonzero h*z correction, including00011: the two-step central bit is0 whereas s XOR z=1. The counterfactual of dropping the nonlinear product with only the white-input premise is REFUTED. Those guards are local inputs, not continuing full clocks. Each of the32 inputs was also embedded at a translated site with exterior bits10 on the left and01 on the right; the two-step central output was unchanged. This identified unexpected check confirms that no boundary wall was hidden in the identity's use. Reproduction: `tests/probes/lexicon/rule210_gpt_two_step_readout.py`.

**Next intention.** Request independent reading of the universal identity and the explicitly conditional application. The output is a small local toolkit relation that identifies precisely which already-controlled product linearizes the column3 readout. Next seek a bound or causal obligation on that discrepancy using actual predecessors, rather than declaring the remaining column5 bit zero. No prize claim or full-clock exclusion.

### GC461 — The white track makes column3 a switch detector (2026-10-08)

**Hand consequence of reviewed G231; farther readout conditional on GC459.** Read Local's TS preregistration in657ed9c and leave its actual-prefix census to Local. Existing G61 equations plus G231 now determine the first unresolved individual temporal track; no new orbit construction or all-right parity induction.

**Prediction before controls.** In every empty-left full0101 orbit, q_n=x_(2n)(3)=1 XOR s_n XOR s_(n+1), including n=0. Thus q_n is white exactly at effective switches. Conditional on GC459, z_n=x_(2n)(5)=1 XOR s_n XOR s_(n+1) XOR s_(n+2). Counterfactual: the next track is always white once the nearer even column2 track is white. Test it against the first effective triple101. Unexpected check: initial n=0 is an isolated effective one; it must remain in these formulae despite being excluded from G231's positive-time gate argument. Controls:16 five-bit inputs with b=0, scalar Rule210 through two updates under imposed wall01, checking q=1 XOR s XOR s_next; no actual-orbit census.

**Proof of the column3 formula.** In G61 notation put b_n=x_(2n)(2), d_n=x_(2n+1)(1), c_n=x_(2n+1)(2). G231 proves b_n=0 at every n>=0 in this family, including time0 through G229. Hence d_n=(1-s_n)*b_n=0 and c_n=s_n XOR q_n. G61's next-white-time equation is s_(n+1)=1 XOR ((1-d_n)*c_n)=1 XOR s_n XOR q_n. Solving over the two-element field gives q_n=1 XOR s_n XOR s_(n+1). Therefore q_n=0 exactly when s_n differs from s_(n+1), and otherwise q_n=1. No condition on farther right bits was imposed. This determines the track uniquely from the known effective stream, but says nothing about existence or uniqueness of an entire right realization.

**Conditional column5 formula.** GC459's proposed readout is q_(n+1)=s_n XOR z_n. Combining it with the just-proved formula at n+1 gives z_n=1 XOR s_n XOR s_(n+1) XOR s_(n+2). This use of GC459 remains pending its independent reading. It cannot be obtained merely by declaring the nonlinear correction zero without G231's product conclusion.

**Boundary and failure.** G26 starts(s_0,s_1,s_2)=(1,0,1). The formula gives q_0=0 and the conditional readout gives z_0=1, agreeing with G229's initial seed{1,5,7}. The all-white farther-track counterfactual is therefore already REFUTED by that initial obligation. The initial isolated one causes no exception to the column3 identity: only the earlier incoming-gate argument started at n=1. At a constant effective triple000, the conditional column5 value is1; at111 it is0. Thus even after the near-wall white track is known, the next odd-position track need not be white. These are evaluations of necessary formulae, not constructions of arbitrary full clocks.

**Independent controls.** All16 five-bit patches(s,0,q,h,z) under imposed wall01 satisfy the column3 identity using the decimal Rule210 truth table, agreeing with independently substituted G61 equations. The explicit initial101 evaluations retain both q_0=0 and z_0=1. Reproduction: `tests/probes/lexicon/rule210_gpt_switch_detector.py`. Local's TS real-orbit census remains separate and unduplicated.

**Next intention.** Request independent reading of the exact column3 track and conditional column5 formula. The switch detector should let us intersect column5's source predecessor times with explicit dyadic switches, while keeping initial products and all farther columns. Do not infer a uniform right parity classification from these two tracks.

GC459 and GC461 reviews resolved (GC463,2026-10-08): Local L270 at e4f4ff9 verifies the universal local identity and its G231 application; L271 at4ff97a2 verifies the exact column3 and column5 tracks including n=0. L272 at572eb5e preserves both readings while correcting the separate existence claim back to G60. The GC459 translated embedding is a locality restatement, not an independent test of a hidden wall premise. The facts s_0=x_0(1)=1 and x_0(5)=1 are separate initial-prefix facts. Catalogue filing queued; GC462 now depends on reviewed results but awaits its own second reading.

GC459/GC461 catalogue filing (GC464,2026-10-08): filed G232/G233 with source proofs copied verbatim and L270/L271 provenance. The conditional language is retained in the source copies, with the now-reviewed dependencies resolved explicitly in the catalogue. The locality-only translated control and separate initial facts remain identified.

### GC462 — The next even track has incompatible incoming and occupancy gates (2026-10-08)

**Conditional hand refinement, pending GC459/GC461 review.** Existing G231 makes every even column2 bit b_n=0 and every even column4 product h_n*z_n=0, where q,h,z,w denote even-time columns3,4,5,6. This block uses GC461's proposed q,z formulae, not an all-right parity induction or a new actual-orbit census.

**Prediction before controls.** Under b=0,h*z=0, the next even column4 bit is H=(1-q)*(1-z)*w. A black H thus requires both q and z white. Conditional on GC459/GC461 and G26, this incoming requirement permits h_n=1 only at n=4^r,r>=1, but z_n=1 at all those indices, contradicting h_n*z_n=0. Hence every even column4 bit vanishes; G229 supplies time0. Counterfactual: white intervening column2 alone makes every even column4 bit white; retain a local patch permitting H=1. Unexpected check: initial effective switch n=0 is followed immediately by another switch; its z_0=1 must remove it separately. Controls:12 local five-bit patches(0,q,h,z,w) with h*z=0, scalar two-step Rule210 versus independently derived expression. No larger search.

**Local incoming identity.** The five inputs at sites2..6 are(0,q,h,z,w). Intermediate sites3..5 are r=(1-q)*h, v=q XOR ((1-h)*z), a=h XOR ((1-z)*w), and the next column4 bit is H=r XOR ((1-v)*a). If h=0, this is (1-(q XOR z))*(1-z)*w=(1-q)*(1-z)*w. If h=1, the premise h*z=0 forces z=0, so r=1-q,v=q,a=1 XOR w and H=(1-q) XOR ((1-q)*(1 XOR w))=(1-q)*w. This again equals the proposed expression. Thus H=1 requires q=z=0, independent of w's other neighbours.

**Conditional elimination.** Let h_n=1 at n>=1 and put m=n-1. The incoming identity gives q_m=z_m=0. GC461 gives q_m=1 XOR s_m XOR s_(m+1), so m is an effective switch. At m=0 the effective triple is101, whose proposed z_m value is1, contradicting z_m=0. At a later up-switch, the effective triple is011 because every positive one-run has length at least2; again z_m=1. The only remaining switches are down-switches m=4^r-1,r>=1. Their effective triple is100 and z_m=0. Hence h_n=1 requires n=4^r,r>=1.

But at each n=4^r the effective zero-run has length4^r>=4, so (s_n,s_(n+1),s_(n+2))=000. GC461 gives z_n=1. This contradicts G231's h_n*z_n=0. Thus every positive-time even column4 bit is0. G229 supplies h_0=x_0(4)=0 separately. The argument is conditional on the proposed GC459/GC461 readout; the gate calculation itself is unconditional under its local two premises.

**Conditional source consequence.** Since every h_n=0, Rule210 makes every odd column3 bit x_(2n+1)(3)=(1-q_n)*h_n=0. G226 at j=3 therefore removes all odd column5 products from time3 onward. At time1, G229 fixes initial sites4,5,6 to010, giving x_1(5)=0 independently of farther cells, so that source also vanishes. G226 at j=4 removes every even column6 product from time2 onward, and G229's initial bit6=0 removes its time0 product. With G216,G226,G230,G231, every selected source at sites i<=6 is thus0 at every odd centre target. For finite support[-R,R], T=2^K+1,K>=3 and2^K>R+1, the homogeneous term vanishes, so selected active sources must have i>=7 with odd total parity. This remains a growing farther cone, not a finite-clock exclusion.

**Controls and retained failure.** All12 product-free white-input patches agree with the decimal Rule210 truth table and the independently derived gate expression. Two have H=1, including00001 at sites2..6, so the universal local bit-zero shortcut is REFUTED. The global conclusion uses the incoming and occupancy requirements at different times. The initial101 effective triple gives z_0=1 despite its adjacent switches; this is the identified unexpected temporal guard. Reproduction: `tests/probes/lexicon/rule210_gpt_column4_gate.py`.

**Next intention.** Independent reading requested for the conditional gate intersection and all early source exceptions. Next resolve GC459/GC461 dependencies and then inspect a named further track; do not assert an even-column induction from this single additional step. Local retains TS actual-prefix work.

### GC465 — A general incoming-gate shortcut needs a no-three-white invariant (2026-10-08)

**Bounded mechanism audit, not a full-right induction.** Read L271's general gate question, G232/G233 and GC462's local identity. Local retains CL/GG actual-orbit census and review. The translated incoming identity would say H=(1-q)*(1-z)*w wherever the preceding even bit is white and the target's adjacent product vanishes. A black target at its arrival also requires z_next=0. Thus closing this gate needs exclusion of q=z=z_next=0, plus a separate initial-time argument.

**Prediction and counterfactual before the check.** On G60's explicit coprime-to6 member, in odd-grid coordinates a_j(n)=x_(2n)(2j+1), Rule90 gives a_(j+1)(n+1)=a_j(n) XOR a_(j+2)(n). Hence q=z=z_next=0 is exactly a_j=a_(j+1)=a_(j+2)=0 at the preceding cut. Blind prediction: none occurs for0<=n<=63,0<=j<=63. Counterfactual: the same no-triple property holds on the empty initial left side; it must fail at negative positions. Unexpected check: compute each tested cell independently by exact integer-binomial parity, not just the recurrence. The test is one64-by64 linear pattern block, no wider actual-seed census or tail search. Failure would close only this universal no-triple shortcut, not Rule210 uniqueness or the earlier named column4 proof.

**Outcome: blind no-triple prediction REFUTED.** The fixed4096 triple positions contain364 all-white triples. The first in time-then-position order is n=6,j=2: actual sites5,7,9 are white at physical time12 in G60's explicit member. Their middle track remains white at the next cut because a_3(7)=a_2(6) XOR a_4(6)=0. Hence the proposed universal incoming/occupancy gate exclusion already fails for the candidate even column6 bit at physical time14. This is an allowed necessary gate pattern, not an active parity defect in the actual member; its even columns remain white.

**Exact hand witness.** At n=6, binomial coefficients are odd precisely at k=0,2,4,6. Thus a_j(6)=a_(j+6)(0) XOR a_(j+2)(0) XOR a_(j-2)(0) XOR a_(j-6)(0). G60's explicit seed has a_j(0)=1 iff j>=0 and j is not1 modulo3. For j=2 the four bits are1,0,1,0; for j=3 they are1,1,0,0; for j=4 they are0,1,1,0. Each XOR is0. Rule90 then gives the next middle bit0 as well. This is a verified explicit obstruction to the gate-only generalization, not just a numerical failure.

**Controls and retained boundary guard.** All4224 cells required by the fixed triple block agree with independently calculated exact integer-binomial parity. The initial negative positions-3,-2,-1 are allwhite, so extending the hoped-for no-triple statement to the empty left side also fails, as predicted. No additional widths, depths or seed families were scanned. Reproduction: `tests/probes/lexicon/rule210_gpt_three_white_gate.py`. The first right-side failure at sites5,7,9 is the unexpected result, with the independent binomial controls checking the instrument.

**Result and next intention.** Close the universal no-three-white shortcut to an all-column version of GC462. Retain the named column4 proof, whose two explicit tracks have the stronger property needed there. Any general uniqueness proof must add a real predecessor or downstream compatibility obligation at the permitted column6/time14 gate, or use another mechanism. Local's CL decision-lag/periodic-tail work is a separate possible mechanism and remains unduplicated. No mixed-parity orbit or finite witness was constructed.

### GC466 — Independent audit of Local's diagonal-deviation reduction (2026-10-08)

**Proof audit in progress, not a uniqueness verdict.** Read the hand argument and explorer in `rule210_uniqueness_automaton.py` throughcae7658. The diagonal recurrence D_c(s+1)=D_(c-2)(s) XOR ((1-D_(c-1)(s))*D_c(s)) follows by substituting i=c-s-1 in Rule210. A zero deviation on an even diagonal persists beyond the finite window if the preceding even deviation is zero there. On an odd diagonal, both preceding deviations zero and the background's even diagonal white make the deviation constant beyond the window. These two inductions appear to justify the finite endpoint tests; the base prefix and finite graph must still be checked independently.

**Predictions before finite controls.** Independently rebuild window L48 using integer time vectors and the decimal Rule210 truth table, with six possible first-deviation residues. Expect exactly9 reachable surviving deviated states, no even endpoint irregularity, no return to zero, no cycle, and longest surviving life3. Counterfactual: a background shifted by one site is accepted by this same certificate; the control must reject it or change the graph. Unexpected check: verify the background update itself at every step using the decimal truth table, so the graph cannot silently depend on an incorrect periodic formula. This block does not rerun Local's actual-orbit census or claim that the required finite base prefix has already passed.

**Independent finite outcome.** The integer-vector/decimal-rule explorer finds exactly9 reachable surviving deviated states, zero irregular even endpoints, no zero return, no deviated cycle, and longest life3, matching Local's finite conclusion. The shifted-background control has15 irregular endpoints under this explorer's counting and is rejected. Every background update also agrees with decimal Rule210 during every evaluated transition. Local's larger irregular count includes additional tail-control traversals; only positivity is used here. Reproduction: `tests/probes/lexicon/rule210_gpt_deviation_audit.py`. This is an independent finite-graph check, not an independent actual-orbit census.

**Remaining proof obligation and next intention.** The graph starts with two entirely zero predecessor deviations. To conclude uniqueness it needs a certified initial prefix beyond the periodic-window threshold, not just agreement on a finite plot. A depth121 prefix is sufficient for L48: every cone through s=48 on diagonals c>=122 lies entirely in positive initial sites (c-2s>=26), and the next diagonal's clock is after the window. Next independently certify the unique depth121 prefix and its all-tail causal reduction, or audit Local's supplied finite base certificate. Until that passes, retain this as a verified finite component and plausible hand reduction, not a completed uniqueness proof. GC465's permitted local gate does not contradict the longer diagonal mechanism.

### GC467 — Completion of L274's empty-left Rule210 uniqueness audit (2026-10-08)

**Bears on:** the Rule210 empty-left full0101 family only; no Rule30 prize conclusion and no result for a nonempty initial left row. Local's L274 supplies the proposition and hand proof; GC466 independently checks its finite deviation graph. This block checks the necessary finite base leaf and closes the causal reduction.

**Preregistered bounded certificate.** Enumerate only prefixes through121 under the full centre clock, using decimal Rule210 minterm masks. Predict the unique survivor equals R(i)=[i>=1 and gcd(i,6)=1]. Independent scalar-list evolution must agree on every256 eight-bit seed through time8. Counterfactual: depth120 already has a unique survivor; this must fail. Unexpected check: distant initial tails at sites122 and beyond must leave centre times0..121 unchanged. No extension of Local's1200-depth census is run.

**Outcome.** Exactly one prefix survives at121, equal to R restricted to1..121; depth120 has two survivors, retaining the counterfactual failure. All256 scalar controls and three distant-tail controls pass. The instrument is `tests/probes/lexicon/rule210_gpt_base_certificate.py`. The finite enumeration is exhaustive by induction: at depth d it extends every surviving (d-1)-prefix by both bit choices, retaining exactly those with centre t mod2 for0<=t<=d. This is a computer-assisted finite certificate, not a proof inferred from an observed count pattern.

**All-tail reduction.** At centre time t, the nearest-neighbour causal cone uses only initial sites[-t,t]. Therefore tails beyond d cannot affect any clock condition through d. The fixed integer strip in the certificate has two initial sites of padding beyond both endpoints of[-121,121]; zero values outside the strip cannot reach any tested centre. Initial sites<=0 are prescribed zero. Thus every infinite full-clock member has the certified121-prefix, regardless of its tail. The three tail controls check this argument's implementation; the cone argument establishes it for every tail.

**Induction order in L274.** Suppose a different member first differs at e>=122. Every preceding diagonal D_c(s)=x_s(c-s), c<e, agrees with R for every s, since its initial cone ends at c. For each new diagonal, its two predecessors have already been processed. For s<=48 and c>=e the cone starts at c-2s>=26, so R's periodic far-field formula applies throughout the finite update window. For even c, R's entire diagonal is white; if its deviation is zero at48 and the preceding even deviation is zero thereafter, recurrence keeps it zero thereafter. For odd c, both predecessor deviations zero thereafter and R's preceding even diagonal white make its deviation constant thereafter. An odd endpoint1 consequently violates the clock at s=c>48; an even endpoint1 would be an irregular state requiring separate treatment.

**Finite obstruction and verdict.** GC466 explores both choices of every next initial bit from all six first-deviation residues, verifies no reachable irregular endpoint, no return to zero and no cycle, and bounds every surviving deviated path by three vertices. Any proposed first deviation therefore dies after finitely many diagonals. The base certificate excludes earlier deviations. Together these verify L274's uniqueness proposition as a computer-assisted proof: the full empty-left0101 Rule210 family is exactly R. Existence is G60, with Local's explicit closed form. Since R has infinitely many black sites, no finite seed with an empty initial left half can realize this clock. Question B for nonempty finite left rows remains open. This reading verifies L274; catalogue filing belongs to the finder, with these certificate dependencies and scope retained.

### GC468 — Terminal-generated schedule guard for L275 (2026-10-08)

**Bears on:** question9's demand-shape premise, not a uniform count estimate. Local L275 found actual demand laws through1024 unimodal and proposed using the absence of consecutive noncritical steps. Read Local's prior-art note first; the supplementary searches `random walk running minimum distribution unimodality non identically distributed Bernoulli steps theorem` and `site.arxiv.org maximum Bernoulli random walk log concavity distribution nonhomogeneous` found no applicable theorem. Search summaries only were read; no result imported.

**Exact folds and scope.** In coordinates measured from the current admission edge, let p be the integer atom sequence of backward survival demand. At a noncritical step N(p)=(2p_0+p_1,p_1+p_2,...); at a critical step C(p)=(p_0,p_0+p_1,p_1+p_2,...), with zeros beyond the final atom. These follow directly by differencing the backward survival equation and shifting the edge by0 or1. The terminal law is(1). Both folds double total mass. This is a terminal-generated family, narrower than arbitrary unimodal input; neither generic unimodality nor GC430's synthetic failure decides it.

**Predictions and outcome.** Before running, predict every terminal-generated law from words of length1..14 without consecutive N is unimodal. The generic-N preservation counterfactual must fail on(10,13,16,18); unexpectedly also check exact total mass2^n after each n folds. The bounded exhaustive word check passes2581 laws with no nonunimodal law; every mass control passes. The generic guard folds to(33,29,34,18), a genuine dip, as expected. Reproduction: `tests/probes/prizes/collatz_gpt_schedule_shape_guard.py`. This is not Local's actual-schedule census and not a proof beyond14 folds.

**Minimum indexing audit.** G74 already states Delta_t(a)=Pr(J=a+1), with J=max over j=t+1..T of ell_j-Z_(j-t-1). Therefore the running-minimum version is min(Z_(j-t-1)-ell_j)=-a-1, with Z_0=0 at j=t+1 and fair bits only for steps t+2..T. L275's walk interpretation is correct with that starting-time convention; adding a fresh coin at t+1 would change the law. The generic fold failure remains evidence that a theorem must use terminal reachability or schedule structure, not unimodality of its arbitrary input alone. Next seek a reachable-law invariant or a counterexample before enlarging the scan.

### GC469 — Independent verification of L276's all-horizon demand unimodality proof (2026-10-08)

**Bears on:** question9's demand-shape premise. Local L276 and the UP proof atb491e17 are the source. G94/G95/G218 read fully after the nearest-entry check for G219; these concern respectively the log-concavity edge, isolated flats and the conditional bound comparison. None proves this actual all-horizon unimodality statement. The following is an independent hand audit, with an elementary substitute for the external convolution citation.

**Critical averaging without an external theorem.** Extend a nonnegative finite unimodal p by zeros and choose a mode m. Write q_j=p_j+p_(j-1)=C(p)_j. Then q_(j+1)-q_j=p_(j+1)-p_(j-1). This is nonnegative for j<m and nonpositive for j>m; only j=m can have either sign. Hence C(p) has a mode at m or m+1. This includes plateaux, leading zeros, trailing zeros and the zero vector. Apply C twice to obtain unimodality of convolution with(1,2,1); restricting it to a tail preserves unimodality.

**Flat-after-critical lemma.** P=B(C(p)) has P_0=3p_0+p_1 and P_j=p_(j-1)+2p_j+p_(j+1) for j>=1. Its tail is the preceding unimodal convolution, shifted. If p is nonincreasing, every tail difference is nonpositive, including P_2-P_1; any choice of P_0 therefore leaves a unimodal sequence. Otherwise p_0<=p_1. If p_1<=p_2, then P_0-P_1=2p_0-p_1-p_2<=0, so prepending P_0 to the unimodal tail cannot introduce a valley. In the remaining case p peaks at1, and the tail from P_2 onward is nonincreasing. A valley would require both P_0>P_1 and P_2>P_1. These inequalities are2p_0>p_1+p_2 and p_2+p_3>p_0+p_1, implying p_2/2+p_3>3p_1/2. This contradicts p_2<p_1 and p_3<=p_2. Thus B(C(p)) preserves unimodality. No random or bounded evidence is used in this lemma.

**Actual schedule and endpoint.** For beta=log_3(2), 1/2<beta<1, the barrier ell_r=ceil(beta*r) has increments0 or1 and ell_(r+2)-ell_r>=1. This remains true at r=0, with the recorded ell_0=0 convention. A flat at r<T-1 therefore has a critical step at r+1, so its backward law is B(C(p)) for the law at r+2. A terminal flat at T-1 acts on(1) and produces(2), still one atom. Strong backward induction from terminal(1) applies C at critical steps and B(C) at flat steps. Consequently every actual backward demand law is unimodal at every finite horizon. The same proof covers every binary threshold schedule with isolated flat steps, explaining GC468 without extrapolating its measurements.

**Preregistered independent controls and outcome.** Predict C and B(C) preserve all unimodal vectors of lengths1..5 with entries0..3. Use independent integer pushforwards J -> J+1-bit and J -> max(0,J-bit), rather than UP's row construction, to check the explicit composite. All496 unimodal vectors pass preservation and all1364 vectors pass the composite identity. The wrong-order counterfactual C(B(20,21,22,23,24)) equals(61,104,88,92,71,24) and retains its valley. Dropping the input-shape premise also fails: p=(1,0,0,1) gives B(C(p))=(3,1,1,2,1). Unexpected guards verify terminal B(1)=(2), the zero law, and a plateau input giving(5,7,7,4,1). Reproduction: `tests/probes/prizes/collatz_gpt_composite_shape_audit.py`; no actual-law sweep or random UP sample duplicated.

**Verdict and limit.** L276 steps2–3 are verified, including the time ordering and terminal exception. G218's optimized-centering comparison now applies to every actual demand at every finite horizon. G219 still refutes the opposite operator order on arbitrary input, and actual log-concavity failures remain. This establishes an ordering of discrepancy bounds, not a uniform small bound or the Collatz conjecture. Local may file the proof with this second-reading provenance; no prize candidate follows.

### GC470 — Independent verification of L278's six-site-left corollary (2026-10-08)

**Bears on:** Rule210 full0101 compatibility for initial left support inside[-6,-1]. Local L278 atbd45bc9 is the proposed corollary, using entry29 and G65. This audit supplies smaller independent finite base leaves, not a duplicate of LB's depth300 census. The disclosed LB preregistration-push slip remains in its source; no prediction is rescored here.

**Predictions and bounded outcome.** Predict that each of the seven nonempty odd-supported left rows has a unique compatible right prefix through121, equal to R XOR the reflected left mask. Independently reject all56 rows containing an even black site by depth6. Independent scalar-list evolution must match decimal-mask traces for all256 eight-bit right seeds with each of the seven odd left masks. Counterfactual: prefix reflection commutes already at depth3 for left{-3}; it must fail. Unexpected threshold check: at first possible deviation e122, the L48 window begins at initial site26, already beyond every mirrored correction. All seven bases are unique as predicted; all56 even-containing rows have no depth6 survivor;1792 scalar controls pass. The depth3 actual survivor set for{-3} is{5}, versus reflected empty-left set{3,5,7}, retaining LB-I1's failure by a smaller exact witness. Reproduction: `tests/probes/lexicon/rule210_gpt_left_base_audit.py`.

**Background and window transfer.** G65 prescribes positive odd bits R(i) XOR L(-i), every positive even bit zero, and the given odd left bits. The added finite pairs at opposite odd sites evolve under Rule90; binomial symmetry cancels their centre contribution at every time. Therefore this background has the clock, every even diagonal white globally, and initial agreement with R on all sites>6. For s<=48 and c>=122 its initial cone[c-2s,c] lies in sites>=26, so the entire computed background window equals GC466's same periodic field. Its behaviour near the wall can differ; the beyond-window induction only needs its globally white even diagonals, not near-wall periodicity.

**Completion of the corollary.** Every full member has one of the independently certified121-prefixes by the same all-tail causal argument as GC467. If it differs from the corresponding reflected background, its first differing right site is e>=122. All earlier diagonals agree exactly for every time. The increasing-diagonal induction of GC467 and identical GC466 finite graph then kill that deviation. This establishes uniqueness for each of the seven odd-supported left rows. The empty row is entry29; the56 other nonempty rows are excluded by the finite depth6 certificates. Every permitted background agrees with infinite R beyond6, so it is infinite. Consequently no finite Rule210 seed with left support inside[-6,-1] realizes the full0101 clock. L278 is verified as a computer-assisted corollary, with this independent base and inherited finite graph.

**Limits and next intention.** Nothing here covers unbounded left radius. The near-wall census does not commute with reflection, and the above121-prefix leaves cover only the specified masks. A general finite-left proof still needs a uniform base argument or a bound and certificates for each larger radius; increasing this census is not an all-radius proof. Catalogue filing belongs to Local with these dependencies and scope. GC469 all-horizon demand review remains verified on the GPT branch pending main integration.

### GC471 — A uniform late-first-deviation exclusion for finite odd left rows (2026-10-08)

**Bears on:** Rule210 question B's arbitrary finite left radius. This is a hand reduction using G65 and the verified GC466-GC467 graph, not a uniform base certificate. GC470's per-row bases remain restricted to radius6. Before the audit, predict that e>=R+99 suffices for the unchanged L48 graph on a first deviation at e, including both predecessor windows. Counterfactual: clearing only the target window automatically clears both predecessors; retain the missing-margin example below. Unexpected check: agreement with the parity background is a premise; no injectivity theorem for two arbitrary nonlinear members follows.

**Statement.** Fix R>=0 and a finite initial left row L supported on odd sites inside[-R,-1]. Let y be G65's Rule210 full0101 parity-sparse realization, with right seed R_0 XOR mirror(L), where R_0(i)=[i>=1 and gcd(i,6)=1]. If any full0101 realization x with this same initial left row agrees with y on initial right sites1..R+98, then x=y everywhere. Equivalently, any different full realization must first differ at a positive site e<=R+98. Here the radius R and the background R_0 are distinct objects.

**Proof.** G65 makes every even diagonal of y white for all time. Its initial row equals R_0 at every site>R. Suppose x first differs at e>=R+99. Diagonals with index c<e agree with y for all times because their initial cones end at c. For c>=e and s<=48, all background cones on c,c-1,c-2 have lower initial endpoints at least e-2-96>=R+1. Thus all three windows equal the same period-six background used in GC466, independently of the particular left mask. The two predecessor deviations initially vanish entirely. Apply the same increasing-diagonal induction: an even zero endpoint stays zero after48; an odd deviation is constant after48 and a nonzero endpoint fails its later clock condition. GC466's exhaustive graph has no reachable irregular endpoint, no return to zero and no cycle, so every first deviation dies in finitely many diagonals. This contradicts the full clock. Hence no such first deviation exists. The argument uses the verified finite graph as a computer-assisted component; it is otherwise uniform in radius and mask.

**Boundary guard and what remains.** At e=R+97 the current window's lower initial site is R+1, but the c=e-2 predecessor's full window reaches R-1. For example R=5 and e=102, a left black site-5 flips background site+5. The odd predecessor c=101 at s=48 has cone[5,101]; its cell at53 receives the+5 correction with endpoint binomial coefficient1, while the-5 correction cannot reach it. It therefore differs from the periodic background. Clearing the current cone alone does not establish periodicity of all three complete windows. The conservative threshold R+99 avoids the issue; no minimal threshold is claimed. This is a failed geometric shortcut, not a counterexample to uniqueness.

A finite seed matching the full clock must differ somewhere from y, since y equals infinite R_0 beyond R. This theorem forces its first difference into1..R+98. To exclude all finite seeds, one still needs a uniform near-wall argument ruling out those early differences. There are2^ceil(R/2) possible odd left masks at radius R; separately checking any finite collection does not settle all radii. Two hypothetical nonlinear members could both differ early, so the theorem also does not say that arbitrary members agreeing with each other on a prefix are equal. Next coordinate this exact remaining obligation with Local; do not widen the LB census as a substitute for proof.

### GC472 — The first nonlinear deviation is an even-site pulse (2026-10-08)

**Bears on:** the uniform near-wall obligation in GC471, not a complete finite-left exclusion. Fix any finite odd-supported left row and its G65 full0101 parity background y. Let x be another full0101 realization with that same left row, and e its first differing positive initial site. Every diagonal with index below e agrees exactly with y at every time; later initial sites cannot affect D_e(s)=x_s(e-s).

**Hand lemma.** Write delta(s)=D_e(x,s) XOR D_e(y,s), and b(s)=D_(e-1)(y,s). Subtracting the diagonal Rule210 recurrence while both predecessor diagonals agree gives delta(s+1)=(1-b(s))*delta(s), with delta(0)=1. If e is odd, e-1 is even and y's entire predecessor diagonal is white, so delta(s)=1 for every s. At s=e this flips the required centre bit; therefore an odd first difference is impossible for a full clock.

Hence any first difference is at an even e, where y_0(e)=0 and x_0(e)=1. The preceding odd diagonal has b(e-1)=1 by y's clock. Let tau be its first black time;0<=tau<=e-1. The exact recurrence gives delta(s)=1 for0<=s<=tau and delta(s)=0 for s>=tau+1. Thus the first deviation is a finite pulse of length tau+1 in diagonal coordinates. In particular it vanishes before its own clock test at s=e. Every earlier clock is unchanged by locality. A single even flip therefore passes the clock through its own site e, whatever later bits are chosen; later diagonal compatibility is essential.

**Predictions and independent outcome.** Before running, predict the odd constant error and even pulse formula for all64 combinations of eight odd-left masks on[-5,-1] and first flips e1..8. Compute the periodic-plus-reflection background by literal decimal Rule210, with independent exact integer-binomial parity for all queried diagonal cells. All64 flip controls and352 binomial comparisons pass. All32 odd first flips fail their own clock as predicted; the32 even flips pass their own clock after their error pulse has died. The unexpected initial-black-predecessor case occurs20 times and gives a one-sample pulse. Reproduction: `tests/probes/lexicon/rule210_gpt_first_pulse.py`. These are local proof controls, not a prefix census or a radius expansion; the analytic recurrence establishes the result for arbitrary later tails and arbitrary finite odd left radius.

**Consequences and retained failure.** Combining with GC471, an alternative full member must start with a0-to1 deviation at an even site2<=e<=R+98. There is no odd first-deviation branch to eliminate in the remaining near-wall argument. But the tempting own-clock test cannot remove the even branch: that clock is automatically satisfied. The next useful question is whether the pulse necessarily forces a later diagonal failure for every near-wall parity background, rather than widening the census or assuming the period-six window there. The duration can depend on the left row; no uniform small duration or all-radius uniqueness follows.

GC471 independent reading resolved: Local L280 at5207f25 verifies all three cone endpoints, global-parity induction and the exact boundary kernel witness. GC472 remains pending its own reading.

### GC473 — The first pulse has an exact following-odd clock gate (2026-10-08)

**Bears on:** the even first-deviation branch remaining in GC472 and the uniform near-wall obligation. Fix the same odd-left G65 background y and an even first differing site e. Let E(s) be the first diagonal's deviation, equal to1 through tau and0 thereafter, where tau is the first black time on background diagonal e-1. Put a(s)=D_(e+1)(y,s), b(s)=D_(e-1)(y,s), and O(s)=D_(e+1)(x,s) XOR a(s). The initial next-bit deviation O(0)=d is freely0 or1. Initial sites beyond e+1 cannot influence these diagonals.

**Exact reset-and-freeze calculation.** The background has a(s+1)=b(s) XOR a(s), because its intervening even diagonal is white. The candidate's recurrence is D_(e+1)(x,s+1)=b(s) XOR ((1-E(s))*D_(e+1)(x,s)). Subtracting gives

    O(s+1)=(1-E(s))*O(s) XOR E(s)*a(s).

For0<=s<=tau, E=1 and hence O(s+1)=a(s), independent of O(s). For s>=tau+1, E=0 and O is constant. Consequently O(1..tau+1) records a(0..tau), and O(s)=a(tau) for every s>=tau+1. The initial choice d is erased at the very first update. Since tau<=e-1, the clock time e+1 lies strictly after the pulse: the next odd clock holds if and only if a(tau)=0. If a(tau)=1, neither next initial-bit choice can repair it. If a(tau)=0, both choices pass this clock; this is a necessary local gate, not full-tail compatibility.

**Predictions and controls.** Before running, predict this entire error-vector formula for eight odd-left masks on[-5,-1], even e2,4,6,8 and both next-bit choices. Check a(tau) independently by exact binomial parity of the mirrored seed; the wrong repair-by-next-bit counterfactual must fail on a blocked gate. Unexpected check: both initial choices must have identical deviation vectors from time1 on. All64 gate/vector controls pass, split32 passing and32 blocked next-clock cases. All32 background binomial gate comparisons pass, and all32 paired choices are erased after the first update. Reproduction: `tests/probes/lexicon/rule210_gpt_next_odd_gate.py`. No Local symmetric-background enumeration or extended census is repeated.

**Retained obstruction to a one-gate proof.** Empty left row, e=2 has tau=0 because initial site1 is black, and a(0)=initial site3=0. Thus both choices at site3 pass the next clock; not every first even pulse is killed at the immediately following odd diagonal. For empty left row e=4, predecessor diagonal3 first turns black at time1 and a(1)=y_1(4)=1, so both site5 choices fail at time5. These are exact hand witnesses for the two branches, not empirical all-radius classifications.

**Next analytic obligation.** The survivors have O eventually zero, while their initial next-bit choice has been hidden in an early transient. The following even diagonal receives both this transient and the original pulse. Any uniform exclusion must control their coupled propagation, or rule out the background gate pattern for all relevant symmetric corrections. The initial e=2 witness shows that the gate pattern itself is realizable, so simply asserting a(tau)=1 universally is closed. No uniform exclusion, all-radius uniqueness or Rule30 consequence is claimed; independent reading requested.

GC472 independent reading resolved: Local L281 at6cad044 verifies the recurrence, odd exclusion and even pulse endpoint by hand. L281 independently derives the following-odd gate of GC473; GPT verifies that proposed lemma by the reset-and-freeze calculation above. These are matching independent derivations; the uniform coupled-transient obligation remains open.

### GC474 — The coupled next-even transient passes its clock (2026-10-08)

**Bears on:** GC473's gate-surviving branch, not uniform exclusion. Keep its notation: even first site e, pulse E(s), next odd background a(s), and next odd error O(s). The following background diagonal e+2 is identically white. Let V(s)=D_(e+2)(x,s), with new initial bit V(0)=v freely0 or1. The exact candidate recurrence therefore reads

    V(s+1)=E(s) XOR ((1 XOR a(s) XOR O(s))*V(s)).

This is an affine recurrence over binary bits, receiving both earlier transients. In particular, the early odd-bit choice can still affect V even though GC473 erased it from the odd diagonal itself. Erasure on one diagonal must not be mistaken for erasure from all descendants.

**Hand clock implication.** If GC473's gate passes, O(s)=0 for s>=tau+1, while E(s)=0 there as well. Thus beyond that time V(s+1)=(1-a(s))*V(s). At s=e+1, a(e+1) is y's centre at an odd time and equals1. Since tau+1<=e, both errors have already vanished. Consequently V(e+2)=0, independently of V(0), the initial odd choice and all farther initial sites. The next even clock is automatic once the preceding odd gate passes. This closes the proposed use of that even clock alone to kill a gate survivor; it does not make the entire V transient vanish or decide diagonal e+3.

**Preregistered controls and outcome.** Before running, predict the full affine error vector and this conditional clock implication for eight odd-left masks on[-5,-1], e2,4,6,8 and both new bits at e+1 and e+2. Exact integer-binomial parity independently checks the gate cell and the black predecessor centre; the scalar evolution uses decimal Rule210. All128 vectors and64 binomial controls pass. All64 passing odd-gate cases pass the even clock. The wrong counterfactual that this clock kills a gate survivor is rejected in all64 cases. Unexpected check:32 paired even initial choices converge to zero at clock time despite starting differently. Reproduction: `tests/probes/lexicon/rule210_gpt_next_even_gate.py`. These controls do not duplicate Local SB2 or SB3's tail census.

A small unregistered follow-up queried the64 already-blocked odd-gate cases from the same sample and found their next even centre also zero. This was not a preregistered test of a stronger theorem. The analytic argument above still assumes the odd gate passes; no unconditional theorem is inferred from the extra sample. Retain that distinction if this stronger pattern is investigated later.

**Next.** Supply this exact transient to Local's invited e+3 odd-link derivation. An early initial choice may be hidden in descendants even after its own error vector is reset. The uniform exclusion still needs a mechanism controlling that propagation, not just consecutive centre clocks. Local's SB2 unique-prefix observations and SB3 life exploration remain separate bounded evidence.

### GC475 — Independent E3 audit reduces both odd gates to initial cells (2026-10-08)

**Bears on:** Local's E3 proposed hand calculation at83468d5, with GC472-GC474 fixed. This independent audit does not import Local's simulator or repeat its SB/E3 census. The piecewise E3 final-error formula is correct, but the special first-pulse background makes it simpler: passage through clock e+3 is equivalent to both initial background cells at e+1 and e+3 being white. Conditional on this pair, all eight choices of the new bits pass these clocks. No claim about a complete continuation follows.

**First gate simplification.** Write b=D_(e-1)(y), a=D_(e+1)(y), c=D_(e+3)(y). The parity background gives a(s+1)=b(s) XOR a(s) and c(s+1)=a(s) XOR c(s). By definition b(s)=0 for s<tau, so a(tau)=a(0). Thus GC473's first odd gate simply reads initial background site e+1. If it passes, a(s)=0 for0<=s<=tau, a(tau+1)=1, and c(s)=c(0) for0<=s<=tau+1. Moreover O(0)=d, while O(s)=0 for every s>=1: its entire error is now a possible initial sample, not a longer transient. GC474's even error Z then satisfies Z(0)=f and Z(1)=1 XOR ((1 XOR d)*f). It may toggle during the pulse, but it vanishes from tau+2 onwards, because the first black a after the pulse is exactly at tau+1.

**Second gate simplification, independent of g.** For the next odd error Q, subtraction gives

    Q(s+1)=O(s) XOR ((1-Z(s))*Q(s)) XOR Z(s)*c(s), Q(0)=g.

At s=0, Q(1)=d XOR ((1-f)*g) XOR f*c(0). If Z(1)=0, its displayed formula forces f=1,d=0, whence Q(1)=c(0). If Z(1)=1, the next update resets Q(2)=c(1)=c(0), since O(1)=0. Thus in both cases Q(2)=c(0). From time2 through tau+2 every update either preserves this value or resets it to the same c(0), since c is constant through tau+1 and O is zero. From tau+2 onwards Z=O=0, so Q freezes. This also covers tau=0: Q(2) is already its final value. Hence Q(e+3)=c(0), for every d,f,g. The e+3 clock passes exactly when initial background site e+3 is white.

This verifies Local's recurrence, erased g and piecewise final-error lemma, while removing its last-reset sum on the actual first-pulse family. In its branch Z(tau+1)=1, s_d=tau+1 and c(s_d)=c(0); in the other branch the same value follows from the two-step reset argument. Generic externally supplied a,O,Z histories would not justify this reduction.

**Predictions, independent controls and unexpected check.** Before running, predict a(tau)=a(0), and Q_final=c(0) on passing first gates, for16 odd-left masks on[-7,-1], e2,4,6,8 and all8 new-bit choices. The literal decimal Rule210 simulator is GPT's GC472 instrument; exact integer-binomial parity independently checks the first gate and each final odd background centre.64 initial-gate comparisons and320 gate-passing E3 choices pass, split192 blocked and128 surviving. No choice repairs a black c(0), rejecting the stated counterfactual. Unexpected check: Local SB's witness L={-5,-7},e=2 has both initial cells3 and5 white, so all8 choices pass through e+3, as verified. Reproduction: `tests/probes/lexicon/rule210_gpt_e3_initial_gate.py`. The background's zero odd stretch explains these early surviving branches without turning them into full members.

**Next.** Supply the two initial-cell gates to Local's life exploration. Uniform exclusion still requires eventual elimination; no fixed-radius sample or finite number of initial white cells proves that. A subsequent analytic block can ask how a longer initial white odd stretch governs pulse survival, after reading Local's SB3 outcome and avoiding its claimed computation.

### GC476 — Gate transport and a finite white-run bound (2026-10-08)

**Bears on:** Local L282-L283's proposed life-law induction, not its proof. The requested full induction is still unresolved in this block: constancy after predecessor errors die does not determine the value inherited from their early transients. Instead establish an exact background lemma removing the moving-time gate parameter.

Let A_j(s)=D_(e+2j+1)(y,s) for j>=0, and A_(-1)=b=D_(e-1)(y). The parity background obeys A_j(s+1)=A_j(s) XOR A_(j-1)(s). Let tau be the first black time of b, and w the length of the initial white odd run: A_j(0)=0 for j<w, A_w(0)=1.

**Hand transport lemma.** For every0<=j<=w, A_j(s)=A_j(0) for0<=s<=tau+j. For every j<w its first black time is exactly tau+j+1. Proof: b is zero before tau and black at tau. Hence A_0 remains its initial value through tau; if that value is zero, its first black occurs at tau+1. Inductively the preceding white A_(j-1) stays zero through tau+j-1 and first turns black at tau+j. The accumulation recurrence keeps A_j at its initial value through tau+j and, if initially white, turns it black at the next update. This proves both statements, including tau0 and the failing gate j=w. In particular A_j(tau)=A_j(0) through the first black gate. Thus Local's white run in row tau has exactly the initial white-run length; no tail dynamics is involved in finding w.

**Finite bound.** Let R be any bound on the finite odd initial-left support, and m the number of gate sites e+1,e+3,... not exceeding R:

    m=max(0, floor((R-e-1)/2)+1).

Beyond R, G65's initial right row is R_0: among successive odd sites its bits are a rotation of1,0,1. There cannot be two successive white odd sites beyond R. Therefore w<=m+1, and the first black gate always exists. If the life law is eventually proved, it would imply failure by clock e+2w+1<=e+2m+3 (in particular at most max(e+3,R+4)). That failure bound is conditional on the life law; the background bound alone does not exclude a nonlinear continuation.

**Preregistered independent controls.** Before running, predict matching initial/time-tau gates through the first black and w<=m+1 for16 odd-left masks through radius7 and even e2,4,6,8. Compare literal decimal scalar Rule210 with exact binomial parity; the counterfactual first black shifts under transport must fail. All64 transport/bound controls and128 binomial gate comparisons pass. After stating the first-black-wave prediction in the probe header,64 additional first-black-time controls also pass. Unexpected guard:20 positive-tau cases have a passing first gate, so the check is not confined to instantaneous pulses. Reproduction: `tests/probes/lexicon/rule210_gpt_gate_transport.py`. No candidate tail census, Local PL/SB3/FV run or radius enlargement is duplicated.

**Next analytic obligation.** Use this exact first-black wave alongside the candidate transients to prove or refute the value at tau+1+2j in L283. Endpoints and eventual constancy alone remain insufficient induction hypotheses. The hand lemma above is a background result for arbitrary finite odd left row, while the general life law remains conjectural.

### GC477 — An abstract pulse-circuit guard for the unresolved induction (2026-10-08)

**Bears on:** the stronger induction hypotheses required after GC476, not a general proof. Replace the actual G65 predecessor diagonal by any binary history b that is zero before tau, black at tau and arbitrary afterwards. Prescribe background even diagonals zero and accumulate its odd diagonals by A_jnext=A_j XOR A_(j-1). Their initial gates are white for j<w and black at j=w. The candidate has first even initial bit1 and every subsequent initial bit freely chosen. Its first diagonal is the exact E pulse; every later diagonal obeys decimal Rule210 with the shared left boundary b. This abstract system contains actual first-deviation prefixes but also histories not known to occur in G65. A counterexample here could require a stronger actual-background premise; success in finitely many abstract cases is still only evidence.

**Predictions before the run.** For tau0..3, w0..3, all16 choices of the next4 b bits and all2^(2w+1) candidate suffixes, predict that odd deviation at index2j+1 equals its initial background gate for every s>=tau+1+2j, j<=w. Predict also that even candidate diagonal2j vanishes for every s>=tau+2j,1<=j<=w. Run to tau+2w+6. The even settling statement is a stronger proposed induction invariant than FV's own-clock check. Counterfactual: replace the finite first pulse by a permanent even1; some settling claim must fail. Unexpected check: histories b after tau may be non-G65, so label the experiment abstract.

**Retained instrument failure and correction.** The first implementation supplied0, instead of b, as the left input for diagonal1. It falsely reported an even failure at tau0,w1,all-zero suffix. All8 truth-table controls passed: they checked the rule, not which diagonal supplied an input. The exact recurrence identifies that left input as D_(e-1)=b. Corrected this indexing before interpreting the output. This was an instrument error, not a refutation of the proposed invariant. Then preregistered and ran32 actual causal-prefix controls on mirrored backgrounds: both candidate and background vectors agree with GPT's independent coordinate scalar simulator through the represented b history. That new control specifically exercises the boundary which the truth-table check missed.

**Corrected outcome.** All10,880 abstract cases satisfy both predictions over the tested time interval; no odd or even mismatch remains. All8 truth-table and32 actual causal-vector controls pass. The permanent-pulse counterfactual fails already at tau0,w1,all-zero suffix (odd j0 at time2 and even j1 at time2). Reproduction: `tests/probes/lexicon/rule210_gpt_abstract_pulse.py`. This is an independently coded abstract circuit guard, not a duplicate of Local's actual-orbit FV/PL/SB3 tail census. Its history cuts to zero after the four varied post-tau bits; it does not quantify over all infinite histories.

**Next.** The successful stronger even-settling guard suggests pairing an odd frozen-value induction with an even zero-after-time bound. But the finite circuit controls do not establish either invariant for all j, tau or later histories. The current proof gap is still inherited transient value, not eventual constancy. Derive a two-diagonal invariant or retain a failure and switch to another authorized reasoning lead; do not promote the abstract test to a life-law theorem.

### GC478 — Candidate hand proof: a clearing front proves the full pulse life law (2026-10-08)

**Status and scope.** Proposed hand proof, requesting Local's independent reading. This would close Rule210 B for the full0101 centre clock at every finite initial-left radius; it is not a Rule30 theorem or a prize claim. The proof uses the exact local Rule210 equation and G27/G65; it does not require entry29's finite graph or the radius-dependent prefix certificates. The controls below support the argument but are not its logical basis.

**Pair variables.** Write candidate diagonal pairs as P_j(s)=D_(e+2j)(x,s), Q_j(s)=D_(e+2j+1)(x,s). For j>=1 their updates, with U=P_(j-1), B=Q_(j-1), are

    P_j(s+1)=U(s) XOR ((1-B(s))*P_j(s)),
    Q_j(s+1)=B(s) XOR ((1-P_j(s))*Q_j(s)).

Define the marker M_j=(1-P_j)*Q_j, which means the pair is01. Direct binary algebra gives the key identity

    M_j(s+1)=(1-U(s))*(B(s) XOR M_j(s))
              =M_(j-1)(s) XOR ((1-P_(j-1)(s))*M_j(s)).

If U=1, the next marker is zero. If the input pair is01 and the current marker is zero, the output pair is01: Pnext=0, Mnext=1. This is a clearing pulse followed by a front, not a statement about the candidate's literal first black cell.

**Clearing-front propagation lemma.** Suppose an input pair has a time t with Pprev(t)=1, has Mprev(s)=0 for t<=s<T, and is01 at time T>t. Then the output pair has some clearing witness t' in{t,t+1}, has P(t')=1 and M(s)=0 for t'<=s<T+1, and is01 at T+1.

Proof: choose t'=t if P(t)=1, and t'=t+1 otherwise. In the latter case the first update has P(t+1)=1 because U(t)=1 and P(t)=0. In either case M(t')=0. Since U(t)=1, M(t+1)=0 independently of all prior values. From t+1 through T-1 the input marker vanishes, so Mnext=(1-U)*M preserves zero. Thus M(T)=0. At T the input pair is01, so the next output pair is01. The same argument proves every asserted intermediate zero; no unmentioned initial-tail restriction is used.

**Base front and induction.** Let e be a first even initial deviation from G65, and tau the preceding odd diagonal's first black time. GC472 gives P_0(s)=1 through tau and0 afterwards. At s=tau its own next odd update resets Q_0(tau+1)=b(tau)=1. Thus pair0 has a clearing witness t_0=tau, marker zero through tau, and is01 at T_0=tau+1. Iterating the propagation lemma yields, for every j, a witness t_j<=tau+j with P_j(t_j)=1, marker zero from t_j through T_j-1, and pair01 at

    T_j=tau+j+1.

This candidate front statement alone holds for arbitrary later suffixes; it does not yet identify their background errors.

**Identification with the parity background.** Let w be the first initially black odd background gate: A_j(0)=0 for j<w and A_w(0)=1, where A_j=D_(e+2j+1)(y). GC476 proves that A_j stays at its initial value through tau+j and flips at T_j. Hence A_j(T_j)=1 for j<w and A_w(T_w)=0. Every background even diagonal is white.

For j=0, after T_0 the candidate first even diagonal is zero, and candidate/background odd diagonals accumulate the same b. Their error is therefore constant, equal to A_0(0). Induct on j<=w. When j>0, the preceding pair is a passing gate and already equals the background from T_(j-1) onwards. At T_j the candidate pair is01. If j<w this agrees with the background pair01; thereafter both obey the same recurrence and remain equal, with P_j=0. If j=w the background pair is00, so the odd error is1. The preceding even input is zero forever; the current P_w stays zero and both odd tracks accumulate the same preceding odd input. The error remains1 forever. Thus, for every j<=w and every s>=T_j,

    P_j(s)=0,  Q_j(s) XOR A_j(s)=A_j(0).

This is stronger than the tested tau+1+2j settling bound. Its proof covers tau0, w0 and arbitrary later b histories.

**Clock consequence and finite-left exclusion.** Since tau<=e-1, T_j<=e+j<=e+2j+1, and for j>=1 also T_j<=e+2j. All earlier clocks agree by first-difference locality. The first even pulse passes its own clock; every later even clock up to e+2w is white, and every odd clock before e+2w+1 passes. At e+2w+1 the frozen error is1, so that clock fails, regardless of every subsequent initial bit. This proves the exact2w life law.

For any finite odd-supported initial-left row, G65's parity background has R_0 beyond its left radius, so GC476 proves w is finite for every even e. An alternative full0101 member has a first right difference. An odd first difference is impossible by GC472; an even first difference now fails at a later odd clock. Hence the G65 background is the unique full0101 realization of that left row. G27.3 proves that any full0101 left system has initial ones only at odd depths, so all finite initial-left rows are covered. G65's right seed is infinite beyond the left radius; therefore no finite global initial seed has a full0101 centre clock. No assumption of near-wall periodicity, fixed radius or tail truncation enters this conclusion.

**Predictions and controls.** Before running, predict the sharper front/settling times on GC477's abstract cases. The initial sharpened query found no failure. After deriving the clearing-marker identity and witnesses, check all16 input/output pair choices by literal decimal Rule210 and each constructed witness on all10880 abstract cases:40064 front witnesses pass, as do the sharper settling values. Unexpected: the first failing background gate also has the candidate01 front; it fails by its error, not by absence of a front. Omitting the clearing premise fails: input01 with target01 outputs00, not01. Reproduction: `tests/probes/lexicon/rule210_gpt_clearing_front.py`. These are proof controls, not a substitute for the quantified propagation lemma. GC477's earlier indexing failure remains retained.

**Next.** Request immediate independent reading of the clearing-front lemma, the background identification and G27 scope before treating Rule210 B as closed or filing the proof. The result would strengthen the existing auxiliary Rule210 line; Rule30 still requires its own argument.

## GC481 — Problems 2 and 3: implication audit and a signed balance target (2026-10-08)

**Owner request.** Fresh eyes on the proposed domino effect among the three Rule 30 prizes. This is a bounded hand-reasoning block, not a computation or a solution. Read the official prize page and Wolfram's announcement, G4's selected-orbit correlation gap, G98's velocity-dynamics guard, and the imported toolkit 119/186 scopes. Both handover startup probes print ALL CHECKS PASS; merge probe retains its existing refuted blind predictions.

**Logical scope.** The prizes concern the one-black-cell orbit. A positive Problem 3 answer implies positive Problem 1: an eventually periodic trace has a fixed finite prefix and period and admits logarithmic-in-n indexing in an ordinary bit model. Problem 2 excludes odd eventual periods, since their rational black frequency cannot equal one-half; balanced even periods remain. Neither aperiodicity nor balance supplies a computational lower bound. As a sequence-level control, Thue-Morse is aperiodic, balanced and indexed by binary digit parity in O(log n) work. Aperiodicity proof: if a period p were eventual, take sufficiently large k with 2^k>p and evaluate at 2^k-p and 2^k; the first bit is k minus the digit sum of p-1 modulo 2, whereas the second is 1. Varying k gives a contradiction. Balance follows from each consecutive even/odd pair being complementary. These are controls for a proposed logical inference, not Rule 30 counterexamples.

**Prediction and counterfactual before the hand audit.** Grouping adjacent signed centre bits must leave only non-flipping pairs. The counterfactual that one-half flip frequency suffices for centre balance must fail. Unexpected check: the Rule 210 velocity evaluated on Rule 30 rows must not be treated as an autonomous Rule 210 orbit; G98 already supplies the explicit failure. No Rule 210 closure transfers by this identity alone.

**Exact elementary reduction.** Let c_t be the centre bit, s_t=1-2c_t and v_t=c_t XOR c_(t+1). Then s_(t+1)=s_t(1-2v_t). Thus

    S(2N) := sum(t=0..2N-1) s_t
           = 2 sum(k=0..N-1) s_(2k) [v_(2k)=0].

The identity follows by pairing each even sample with its successor. An odd prefix adds one spin of absolute value 1. Therefore Problem 2 is exactly the assertion that the signed sum on the right is o(N) on the single-cell orbit. All flipping pairs cancel without an independence assumption. This is a reduction, not a bound, and is elementary rather than a novelty claim. A promising next question is whether the diagonal forcing tools give a bounded or sublinear signed potential for these remaining pairs, retaining reachable-state conditions. G4's biased cycles preclude a universal cancellation claim for arbitrary Rule 30 configurations.

**Hand controls and failure.** Pairs 00,01,10,11 contribute respectively 2,0,0,-2 to both sides. The repeating word 0001 has an even-sample flip at exactly half its pairs, but all non-flipping pairs are 00: S(4)=2 and black density 1/4. The counterfactual is refuted. This arbitrary binary trace need not be a finite Rule 30 orbit. The zero fixed row also forbids a bounded telescoping spin potential on the unrestricted Rule 30 state space; any useful potential must retain the selected orbit or a proved domain restriction.

**Problem 3 lane.** An n-step dependency cone or a difficult inversion problem with variable initial data gives no lower bound for indexing this fixed orbit. The input n has only O(log n) bits; its initial row is fixed. Every prefix also has an O(log N)-length description (fixed simulator plus N), so unbounded description complexity cannot establish the required time lower bound. Imported toolkit 119 limits information through noisy Boolean observations and 186 bounds influence under symmetric ensembles. Both may help formulate restricted models, but neither removes this fixed-input/time-bound gap. First useful work: distinguish a proved lower bound for a named evaluation model from any claim about all algorithms; simultaneously inspect exact skip-ahead recurrences as possible negative answers.

**Prior art read.** Official definitions and model discussion: https://rule30prize.org/ and https://writings.stephenwolfram.com/2019/10/announcing-the-rule-30-prizes/ . Wolfram explicitly separates universality for variable initial conditions from prediction of one selected initial condition. Existing G4/G98 retain the ensemble and autonomous-velocity obstructions. No new large scan, general hardness theorem, or prize submission is proposed.

### GC478 review incorporated and GC479 transfer audit completed (2026-10-08)

Local L285 at 60865af independently verifies the full hand proof and its G27 scope; filed as PROOFS entry 32, Proposition 19, crediting Local's conjecture/evidence and GPT's proof. The candidate label above preserves publication history. Rule 210 B for the full 0101 clock is closed.

GC479's preregistered decimal-patch control passes all 16 Rule 210 pair identities, while Rule 30 disagrees on 6. In particular patch(U,B,P,Q)=(1,1,0,0) produces pair 01 under Rule 30, violating the clearing conclusion. This rules out verbatim unrestricted transfer; it is not an actual Rule 30 full-clock counterexample. Both zero rows stay fixed, retaining the period 1 scope guard. Probe rule210_gpt_transfer_scope.py.

Hand corollary from the verified closure: no finite Rule 210 seed has an eventually nonconstant period 2 trace at any fixed column. Finite support persists because the 000 neighbourhood stays white. Advance the finite orbit to a white phase after the eventual onset and translate that column to 0; its future trace is full 0101, contradicting Proposition 19. This does not exclude eventually constant traces or other periods.

**GC482 filing audit.** Duplicate guard finds no repeated formal text among 241 entries. Nearest entries 32-to 29/31 are the same auxiliary question at empty-left/radius 6;32 strictly generalizes both and replaces finite certificates by the hand front. Entry 09 concerns Rule 30 edge-band period doubling, a different rule and conclusion. Read all three rather than infer duplication from vocabulary. Catalogue rebuild and updated status math PASS (0 TeX errors,0 loose dollars). No new independent review is claimed for the elementary GC479 corollary or transfer control. Next: Problems 2 selected-orbit signed cancellation; keep the Rule 210 closure as an auxiliary tool with its rule scope attached.

## GC483 — A four-neighbourhood balance target and a finite-seed potential obstruction (2026-10-08)

**Scope.** Bounded Problem 2 reasoning after GC481, using G4's already verified biased seven-cell cycle. The finite-propagation and telescoping arguments below are elementary; prior graph-potential methods are recorded in PRIOR-ART's G8/G9 audit. No claim of a new general dynamical principle, no asymptotic experiment, and no Rule 30 prize result. Startup checks from GC481 remain current; Local is paused and its detached jobs are undisturbed.

**Signed local target.** For a physical neighbourhood (l,c,r), Rule 30 gives cnext=l XOR(c OR r). The contribution g=(1-2c)[cnext=c] is +1 exactly on 000 and 101, -1 exactly on 010 and 011, and 0 on the other four triples. Thus on the one-black-cell orbit, if N_abc(N) counts triple abc at the centre at times 0,2,...,2N-2, GC481 becomes

    S(2N)=2(N_000(N)+N_101(N)-N_010(N)-N_011(N)).

Problem 2 asks precisely for the parenthesized signed difference to be o(N). This retains sign and actual-orbit conditioning, and separates it from total non-flipping-pair frequency. It is an exact identity, not an estimate.

**Finite-seed obstruction theorem (hand proof, second reading pending).** There is no bound b(T)=o(T) for |S(T)| that holds uniformly over all nonzero finite Rule 30 seeds, even when the initial centre is black. Consequently no bounded state potential H can satisfy s_0(x)=H(Fx)-H(x) on all nonzero finite configurations (including every intermediate row); in particular no fixed-radius finite-valued local potential can do so. The analogous two-step representation of g as a bounded potential difference also fails uniformly. This does not exclude potentials restricted to the selected orbit or a proved smaller domain.

Proof: G4's seven-cell ring cycle is 1,67,100,63, repeating. Its centre bits are 1,1,0,1, with spin sum-2 per four steps. For any T=4m, periodically repeat initial ring row 1 on the full line and truncate it to [-T,T], setting all other cells white. This is a genuine finite seed, including a black centre. A radius-one automaton's backward cone for the centre at time t lies in [-t,t]; induction therefore reproduces the periodic orbit's centre through time T. Its prefix sum is -T/2. Since m is arbitrary, a uniform sublinear b(T) is impossible. A bounded potential with |H|<=M would instead telescope to |S(T)|<=2M, a contradiction for large T. Two-step g sums equal S(T)/2=-T/4, giving the same contradiction. For fixed-radius finite-valued potentials the bound M is automatic.

**Quantifiers matter.** These finite seeds change with T. The result does not produce one finite seed with a biased limiting frequency, does not refute a seed-width-dependent transient budget, and does not say the single-cell orbit reaches the biased cycle. A potential whose size grows linearly with the expanding row width would also leave an O(T) boundary term and hence would not by itself prove Problem 2. The useful next obligation is a domain restricted by the selected seed, or a signed estimate whose boundary term is proved sublinear along that orbit.

**Preregistered controls and retained counterfactual.** Probe rule30_gpt_balance_local.py states its predictions before execution. Eight decimal-rule/OR identities and signed weights PASS; four ring steps agree with G4. Separate full-line set evolution reproduces 60 centre samples across T4,8,16,32, with spin sums-2,-4,-8,-16 and signed pair sums-1,-2,-4,-8. The counterfactual uniform unit discrepancy bound is refuted. Unexpected guard: every constructed seed is finite and has centre 1, avoiding the weaker zero-row objection. These controls check the finite-cone construction; arbitrary-T coverage comes from the hand induction, not the samples. No broad core scan or detached Local job is duplicated.

## GC484 — Actual single-cell orbit blocks short exact telescoping potentials (2026-10-08)

**Question.** GC483 rules out universal bounded potentials, but leaves a selected-orbit domain. Test only the pointwise exact proposal g_t=H(W_(t+2),t+2 mod q)-H(W_t,t mod q) at even times, where W_t is a fixed-radius centre window and g_t is GC481's signed non-flipping weight. This is a restriction on one proof form, not a claim against balance, approximate cancellation, growing windows, longer memory or eventual-onset identities. Finite constraints may be sufficient to reject a proposed exact potential; successful finite fitting would not prove an infinite identity.

**Preregistered block.** Probe rule30_gpt_selected_potential.py specifies radii 0..3, phases q2,4,8 and the first 128 two-step transitions before execution. Blind P1 expects radius 1,q2 inconsistent. Independent literal decimal-set evolution must agree with integer XOR/OR rows through 256 ticks, and pair rewards must match their signed spin sums. Counterfactual: zeroed rewards still yield inconsistency, must fail. Unexpected check: retain explicit phase 4 and 8 rather than attribute contradictions solely to forgotten parity. Synthetic feasible three-node and infeasible self-loop controls check the potential solver. No census, horizon enlargement or Local detached job is duplicated.

**Hand obstruction for radius<=2, phases 2 or 4 (second reading pending).** The initial five black-site sets are {0}, {-1,0,1}, {-2,-1,2}, {-3,-2,0,1,2,3}, {-4,-3,0,4}. Direct substitution of the eight Rule 30 triples gives each step. On[-2,2], row 0 and row 4 are identical (only the centre is black), and their phase agrees modulo 2 or 4. The first two pair rewards are g_0=-1 (centre 11) and g_2=0 (centre 01). The proposed two differences telescope from row 0 to row 4, so would sum 0, but these rewards sum-1. Contradiction. Radius 0 and 1 inherit the same return. This is already an exact finite witness on the selected one-black-cell orbit, without introducing a biased ring or a varying seed.

**Finite audit outcome.** All 12 radius/phase choices are inconsistent on the declared sampled transitions. Radius 3,q2/q4 witnesses use constraint times 0,2,36,78,80,84,86,188,248; radius 3,q8 uses 0,38,40,42,44,76,78,80,220. Radius 2,q8 uses 0,2,4,6,146,240. These are constraint cycles in the quotient graph; they need not be contiguous return segments of the actual orbit. Any exact H on all sampled transitions would nevertheless satisfy them, so inconsistency is decisive for this proposed model. No omitted edge or unrestricted configuration was used. Full contradiction data is printed by the reproducible probe.

Independent rows PASS 257; pair identities PASS 1536; all 12 zero-reward counterfactual controls remain feasible, as required; synthetic controls PASS. P1 HELD. The scalar hand five-row witness is an additional independent audit of the earliest radius 2 contradiction. Standard Python and exact integers, under one second on GPT's owner-described Intel host. These are finite instrument results; no infinite density conclusion follows.

**Failure retained and next step.** Restricting the domain to the actual orbit does not rescue these short exact potentials from time 0. An identity permitted only after some onset is not excluded: the listed witnesses use early times, and arbitrary onset remains open. Do not infer that a larger radius always fails from radii 0..3. Next useful block should test a fixed later interval or formulate a controlled residual term, rather than enlarge the window until the finite trace becomes uniquely encoded.

## GC485 — Fixed later intervals still reject short exact potentials (2026-10-08)

**Predeclared scope.** Retain GC484's end time 256, radii 0..3 and phases 2/4/8. Test starts 16,64,128 without changing the horizon in response to results. Blind prediction: radius 1/phase 2 remains inconsistent for all three starts. Literal-set/integer evolution must agree on all 257 rows; zero-reward constraints must fit. Synthetic control: one feasible early edge becomes inconsistent when a later parallel edge has a different reward, rejecting the counterfactual that finite fitting proves an eventual identity. Unexpected: explicitly check whether discarding data or retaining more window information merely removes constraints. Probe rule30_gpt_late_potential.py has these predictions before execution; Local's jobs remain separate.

**Outcome.** All 36 radius/phase/start choices are inconsistent. P1 HELD at starts 16,64,128. Independent row comparison PASS 257; all 36 zero-reward controls remain feasible (constant potential 0); synthetic extension counterfactual fails as required. There were no fitted nonzero-reward potentials to validate. The exact solver and its constraint-cycle proof are GC484's, reused without treating quotient walks as literal orbit segments. No adaptive onset chase occurred.

**A particularly short actual-orbit witness.** The sampled row at time 192 restricted to [-5,5] is 01010101000, with coordinates written left to right. Its radius 3 window is 0101010. At time 193 the radius 3 window is 0101011; at 194 it is 0101010 again. The centre is black at all three times. Consequently g_192=-1, while any radius<=3 window state, even with phase 2, has returned after two ticks. An exact potential difference must be 0. The radius 5 patch determines the entire radius 3 output after two updates, so this local return is directly verifiable from the 11-bit patch by the decimal Rule 30 table. The claim that this patch is on the actual singleton orbit is certified by the 257 independent set/integer row comparisons; it is a finite computation, not a hand claim about unbounded time.

**Residual implication (elementary, second reading pending).** For g_t=H(state_(t+2))-H(state_t)+e_t in the radius<=3/phase 2 model, the actual time 192 return forces e_192=-1. Thus no pointwise bound |e_t|<1 can hold on an interval containing 192, whatever H is. This does not obstruct cancellation between residuals, which is the quantity Problem 2 needs. Adding larger phase, longer memory or a bigger window changes the state and is not rejected by this one-loop argument. The other declared models are rejected by their printed finite constraint witnesses.

**What closes and what stays open.** The failed exact-potential shortcut is not solely an initial four-tick anomaly: it survives the three fixed later starts. Nothing here excludes an identity that begins after 256, an arbitrary eventual onset, every finite radius, or controlled cumulative residuals. Stop this bounded fitting lane rather than raise the horizon until another contradiction appears. Next useful reasoning should address the signed sum of residuals or a structurally different cancellation pairing. No balance or computational-hardness conclusion, no prize claim.

## GC486 — Problem 3: generic dyadic dilation fails, with the fixed-seed guard (2026-10-08)

**Lane change.** Stop GC484/485's bounded exact-potential fitting. Take a bounded Problem 3 algebra audit: the cheap linear-rule skip-ahead mechanism, compared with Rule 30's actual composition. Existing record: Rule 30 is Rule 150 plus the centre/right product (RULE30-PRIZE8.50; PRIOR-ART Boole audit), and the linear Frobenius mechanism is already used in G59/G66. Wolfram's official prize announcement explicitly uses Rule 150 as a fast-indexing contrast. No novelty is claimed for Boolean ANF, composition or characteristic-two dilation.

**Predictions before execution.** Probe rule30_gpt_dyadic_anf.py fixes times 1,2,4 and Rules 30/90/150, evaluating every cone input (8,32,512). Decimal-rule evolution and ANF reconstruction must agree. Blind prediction: Rule 30 degree increases strictly across these three times. Counterfactual: two steps of Rule 30 are the same rule on neighbours at distance 2; must fail. Independent linear controls require exactly that dilation for Rules 90/150. Unexpected: verify affine dependence with coefficient 1 on the leftmost input while retaining that it varies the initial seed, which the prize fixes. No larger ANF or time search.

**Exact two-step formula.** For initial sites a,b,c,d,e at offsets-2,-1,0,1,2, the centre after two Rule 30 updates is, over the Boolean ring (squares equal themselves),

    a+d+e+bd+cd+be+ce+de+bde+cde.

Directly expand F(F(a,b,c),F(b,c,d),F(c,d,e)), where F(l,c,r)=l+c+r+cr. The 32-row truth control independently verifies this polynomial. It is not F(a,c,e). The singleton row c=1,a=b=d=e=0 gives actual output 0, while the proposed dilation gives 1: even the earliest selected-seed instance rejects that particular shortcut. This is not a refutation of other selected-seed dyadic recurrences.

**Finite outcome.** Rule 30 has ANF degrees 2,3,7 and term counts 4,10,122 at times 1,2,4. Rules 90 and 150 remain degree 1, with 2 and 3 terms respectively at each time. All 1656 truth reconstructions and affine-left-input controls PASS. The Rule 30 dilation has 16 mismatches among 32 inputs; the two linear dilation controls have none. P1 HELD; counterfactual rejected. These are finite exact profiles, not a degree-growth theorem or computational-time lower bound.

**Restricted lower-bound scope (elementary, not separately second-read).** A Boolean circuit of fan-in at most 2 and depth d has algebraic degree at most 2^d: inputs have degree 1, and any two-input Boolean gate is a polynomial of degree at most 2 in its arguments, so the output degree is at most the sum of the two input degrees. Induction gives the bound. The generic time 4 Rule 30 function therefore needs depth at least 3 in this model, because its degree is 7. This concerns variable input rows, circuit depth and a tiny fixed time. It supplies no linear work bound and no lower bound for the one-black-cell orbit, whose initial bits are fixed constants. High degree can also be computed by short compositions; expanding the entire ANF is not required of a predictor.

**Next.** Keep the exact composition failure as a guard, rather than infer that dyadic indexing is impossible. A useful skip-ahead proposal must provide a selected-orbit representation whose size and update cost are controlled; a generic causal formula with a growing polynomial is not yet that representation. Next inspect trace decimation or a finite-state kernel only with explicit size and selected-seed scope, rather than expand ANFs to larger cones. No prize claim or Local job duplicated.

## GC487 — Selected-trace binary kernel: a finite state-size certificate (2026-10-08)

**Literature first.** Read the binary-kernel definition and finite-kernel characterization in Jeffrey Shallit's Automatic Sequences slides, pages 16-17 (https://cs.uwaterloo.ca/~shallit/Talks/cant22-m.pdf). The characterization is stated there; its proof was not imported. Existing record covers automatic-word exclusions and Walnut (PRIOR-ART G137), not this finite trace state-size certificate. Standard automatic-sequence theory supplies a restricted skip-ahead model, not the prize's full algorithm class.

**Model and hand size lemma (second reading pending).** For the actual singleton centre trace a(n), take decimations a_(d,r)(n)=a(2^d*n+r), with 0<=r<2^d. Suppose a deterministic finite automaton with output reads canonical binary n from least significant digit to most significant digit, with no extra arithmetic memory, and returns a(n). If K decimations differ pairwise at positive test indices, it needs at least K states. Proof: after consuming the d low bits of r, padded to exactly d digits, its state determines the output for every common positive continuation n. Appending the canonical digits of positive n makes a canonical whole input for 2^d*n+r. Equal prefix states would therefore make the two decimations agree at every positive n. A distinguishing continuation forces unequal states. The d0 prefix is empty. No leading-zero convention or output at n0 is needed for this lower bound. It concerns this LSB-first model only; no same numerical bound on MSB-first machines is claimed.

If the full binary kernel were finite and its transitions were explicitly known, it would give a logarithmic indexing algorithm: on a digit b replace current sequence g by n->g(2n+b), and at the end output g(0). These transitions preserve the kernel, and induction through the low-order digits proves correctness. This is a conditional algorithm, not a constructed Rule 30 kernel.

**Predeclared finite test.** D4,M32, all 31 pairs(d,r) with d0..4 and r<2^d; use positive n1..32. Maximum required index 527. Independent decimal-set/integer Rule 30 evolution must agree throughout. Thue-Morse's signatures must have exactly 2 values. Blind prediction: all 31 Rule 30 signatures differ. Counterfactual inference that finite distinct signatures prove an infinite kernel must be rejected by an eventually zero sequence agreeing with every sampled bit. Unexpected: positive-only continuations make the automaton convention explicit. Probe rule30_gpt_kernel_prefix.py states these before its first run; no deeper census or asymptotic fit.

**Outcome.** PASS 528 independent rows. Rule 30 has 31 distinct signatures versus Thue-Morse's2. All 465 pairs have explicit differing positive continuations, each at n<=9 within the predeclared 32 tests. Thus any exact canonical-binary LSB-first DFAO for this Rule 30 trace needs at least 31 states, by the hand lemma. The finite controls certify these sample bits, not a new nonautomaticity theorem.

**Counterfactual and scope.** Define b(n)=a(n) for n<=527 and b(n)=0 thereafter. It agrees with every sampled decimation value but has finite support and is automatic: a finite trie recognizes the finitely many canonical binary words for its black indices, with all other words rejected. The same construction works on their reversed words in the LSB model. Hence the sample cannot prove an infinite kernel. Even an independently proved infinite kernel would exclude finite automata, not every sublinear algorithm. State count 31 is a restricted description-size lower bound; it is not a linear-time lower bound. No claim that these states persist in a finite-state approximation for all future indices, or that any approximate predictor is exact.

**Next.** Keep this finite certificate rather than chase larger sampled state counts. Useful continuation would require an analytic family of distinguishable decimations or an explicit closed representation and its cost; otherwise switch back to a signed cancellation mechanism for Problem 2. No Local computation requested and no prize claim.

## GC488 — Conditional domino mechanism: indexing and balance from a proved decimation representation (2026-10-08)

**Bears on.** The owner's shared-lever question for Problems 2/3, after GC487's restricted size certificate. This is an elementary conditional theorem, second reading pending; it does not assert a finite Rule 30 kernel, a contraction bound or a prize solution. Prior art is the standard finite-kernel model read in Shallit's slides and recorded in GC487; finite matrix representations and geometric-series estimates are standard, with no novelty claim. No experiment, larger kernel census or Local job runs in this block.

**Predictions and hand checks chosen first.** A finite decimation model should give an exact all-prefix recurrence, not only dyadic balance. A contraction on the span of reachable output vectors should imply sublinear signed prefix sums. Counterfactual: finite kernel alone forces balance, must fail on the constant sequence. Unexpected: the contraction criterion need not be necessary; test the balanced alternating sequence, whose kernel includes two biased constant states. Thue-Morse supplies the positive independent control, with an explicitly known two-state representation.

**Setting.** Let g_1,...,g_q be a finite family of spin sequences, each taking values in {-1,1}, containing the selected centre spin trace and closed under even/odd decimation. Define T_b g(n)=g(2n+b). The q-by-q integer matrix A counts each state's two children: row i has one contribution for T_0 g_i and one for T_1 g_i, with multiplicity 2 if they coincide. Put b(n)=(g_i(n))_i and S(N)=(sum(n=0..N-1)g_i(n))_i. Let W be the real linear span of the reachable vectors b(n), n>=0. Then

    A b(n)=b(2n)+b(2n+1),
    S(2n)=A S(n),
    S(2n+1)=A S(n)+b(2n).

These follow by partitioning an ordinary prefix into even and odd indices. W is A-invariant and contains every S(N). The invariant subspace matters: A always has row sums 2, so a bound on its full operator cannot contract below 2.

**Conditional all-prefix balance theorem.** Suppose there are fixed C>0 and 1<rho<2 such that, on W with the inherited sup norm, ||A^k w||<=C*rho^k*||w|| for every k>=0 and w in W. Then every state satisfies

    |sum(n=0..N-1) g_i(n)| <= C*rho/(rho-1)*N^(log_2 rho),  N>=1.

Proof: apply the even/odd prefix recurrence repeatedly to floor(N/2). Starting from S(0)=0 leaves at most one vector b(2n) of sup norm 1 at each binary level. All are in W. If L=floor(log_2 N), bound the sum by C*sum(k=0..L)rho^k <= C*rho^(L+1)/(rho-1) <= C*rho/(rho-1)*N^(log_2 rho). The exponent is below 1. Thus the selected trace has limiting black frequency one-half, for every prefix length rather than just powers of two. Finite dimension also implies such a power bound for any rho strictly between the spectral radius of A restricted to W and 2, when that spectral radius is below 2; the explicit power bound above is the actual hypothesis used.

**Indexing consequence and direction.** The same proved finite closed family, with explicit transitions and outputs g_i(0), gives GC487's O(log N) digit-reading algorithm. Thus if this representation and contraction were proved for Rule 30, it would establish positive Problem 2 while giving a negative answer to the proposed linear-work claim of Problem 3. This is a concrete example of a shared proof mechanism whose conclusions move in different directions. Finite kernel without contraction says nothing by itself about the colour frequency.

**Hand controls and failure.** For Thue-Morse spin g(n)=(-1)^popcount(n), the family(g,-g) has A=[[1,1],[1,1]], and W is spanned by(1,-1), so A vanishes on W. The recurrence gives |S_i(N)|<=1 directly, and its digit-parity indexer is logarithmic. For constant spin 1, q1,A=(2),S(N)=N: the finite-kernel-implies-balance counterfactual fails. For alternating spin(-1)^n, use family(g,1,-1). Its matrix rows are (0,1,1),(0,2,0),(0,0,2). Its reachable span contains vector(0,1,-1) with eigenvalue 2, so the stated contraction fails, although the root's prefix sum has absolute value<=1. This unexpected guard retains the criterion as sufficient, not necessary; it also prevents assuming all kernel states must be balanced because the selected trace is.

**Next obligation.** Rule 30's31 finite signatures are not a proved finite closed family, and no contraction on a reachable output subspace is known. Do not apply this theorem to a graph obtained by merging finite signatures without infinite transition identities. A next useful route could allow an increasing family with a separately bounded representation cost and an actual signed norm estimate, but both bounds are open; do not substitute an empirical spectral fit.

## GC489 — Root-visible quotient removes a false balance obligation (2026-10-08)

**Bears on.** Problems 2/3 and GC488's conditional mechanism. Elementary linear-algebra refinement of that block, not a Rule 30 representation or prize result; independent reading pending. This uses the same finite-kernel setting and prior-art provenance as GC487/488. An invariant quotient and Cayley-Hamilton are standard tools, not a novelty claim. No experiment or Local computation.

**Chosen checks before derivation.** Predict that GC488's alternating root loses its biased eigenvalue 2 mode when only root-visible modes are retained, while the constant root retains it. Thue-Morse is the independent positive control. Counterfactual: small sums at powers of two alone force all-prefix balance, must fail. Unexpected check: the balance quotient need not inherit the separate binary digit transitions, so its smaller dimension must not be advertised as an indexing automaton.

**Hand theorem.** Retain GC488's finite family, matrix A, reachable span W and vectors b(n), S(N). Let ell(w) be the coordinate of the selected root. Define

    U = {w in W : ell(A^k w)=0 for every k>=0}.

This is A-invariant: shifting k proves A U is contained in U. In ambient dimension q it equals the intersection of the kernels for k=0,...,q-1, by Cayley-Hamilton and induction for the later powers. Let V=W/U, with the quotient of the inherited sup norm, and let Abar be the induced operator. The functional ell descends to ellbar and has norm at most 1: ell(w+u)=ell(w), and |ell(w)| is bounded by the norm of every representative w+u. Also the quotient norm of each b(n) is at most 1.

If ||Abar^k v||<=C*rho^k*||v|| on V, for fixed C>0 and 1<rho<2, GC488's binary-prefix expansion now gives for the root alone

    |ell(S(N))| <= C*rho/(rho-1)*N^(log_2 rho), N>=1.

Indeed project each term A^k b(2n) into V and apply ellbar. Thus spectral radius below 2 on this quotient is sufficient, using the same finite-dimensional power bound as GC488. This is weaker than contraction on all of W: kernel states other than the root may have biased sums. No assertion of necessity, and no actual Rule 30 W, U or spectral bound supplied.

**Independent hand controls.** For alternating spin, W is spanned by (1,0,0) and v=(0,1,-1), with A(1,0,0)=0 and A v=2v. For the root ell(w)=w_1, U is exactly span(v). Consequently Abar=0 and the recurrence yields root prefix sums bounded by 1. The biased constant kernel states remain biased; they merely cancel in this observable. Thue-Morse already has A=0 on W, so the refinement preserves its bound. Constant spin 1 has U=0 and Abar=2, rejecting contraction as required.

**Dyadic-only counterexample.** Define a spin sequence h by h(0)=1,h(1)=-1. For each k>=1, on [2^k,2^(k+1)) put +1 on its first half and -1 on its second half. Every such whole block sums to 0, so S_h(2^k)=0 for k>=1. Yet at N=3*2^(k-1), the preceding complete blocks sum to 0 and the new first half contributes 2^(k-1), giving S_h(N)/N=1/3. Hence controlling only ell(A^k b(0)), the dyadic totals, does not supply the all-prefix theorem. The required bound covers all reachable b(n), not just the initial output vector. This example is a hand scope guard, not a Rule 30 orbit.

**Unexpected digit-transition guard.** Write B_0 for the matrix selecting each state's even child, so b(2n)=B_0 b(n). In the alternating family (g,1,-1), B_0 v=(1,1,-1), which is not in U because its root coordinate is 1. Thus U, although A-invariant, is not B_0-invariant. The quotient supports the aggregate prefix argument but cannot in general serve as a digit-reading state representation. GC488's logarithmic indexer still follows from the original finite family, not from this quotient alone. This keeps balance cancellation and indexing cost separate even within a shared representation.

**Next.** A finite sample cannot certify W or the infinitely quantified invisibility condition. With a proved closed family, q exact power tests do certify U by the stated lemma; without such a family, fitting a matrix or quotient to trace signatures remains insufficient. The remaining useful Rule 30 obligation is still an analytic selected-orbit representation or signed cancellation bound. This refinement prevents demanding balance of irrelevant kernel modes, but supplies no new Rule 30 dynamics.

## GC490 — Analytic infinite-kernel control with cheap arithmetic indexing (2026-10-08)

**Bears on.** Problem 3's scope after GC487. This gives a hand counterexample to inferring linear indexing cost from an infinite binary kernel, even together with balance and aperiodicity. It is not a Rule 30 trace. Independent reading pending; no novelty claimed. Prior-art query `automatic sequence "floor" "sqrt" squares nonautomatic` returned no relevant primary-source treatment of this particular parity sequence in the bounded search. NOT FOUND, not a novelty conclusion. The finite-state prefix lemma is GC487's; everything else below is proved directly. No experiment or Local run.

**Checks chosen first.** For h(n)=(-1)^floor(sqrt(n)), predict all-prefix signed discrepancy at most sqrt(N), infinitely many distinct decimations h(4^d*n), and polynomial-in-input-bit-length exact indexing. Constant spin is the independent negative balance control; Thue-Morse is the finite-kernel positive balance control from GC488. Counterfactual infinite kernel forces linear indexing must fail. Unexpected: distinguish the decimations by explicit square-plus-one positive continuations, without a sampled signature census or floating-point square root.

**Balance and nonperiodicity (hand proof).** On the integer interval [k^2,(k+1)^2), h has constant sign (-1)^k and length 2k+1. For N>=1 write K=floor(sqrt(N)), r=N-K^2, so 0<=r<=2K. The complete blocks telescope:

    sum(k=0..K-1) (-1)^k*(2k+1) = (-1)^(K-1)*K,
    S_h(N) = (-1)^K*(r-K),
    |S_h(N)| <= K <= sqrt(N).

Thus black bits (1-h)/2 have limiting density one-half. Constant spin instead has discrepancy N. The runs of h have unbounded lengths and both signs recur infinitely often. An eventually periodic sequence containing both signs has bounded constant runs (at most twice its period); an eventually constant sequence cannot change sign infinitely often. Therefore h is not eventually periodic.

**Infinite decimation family (hand proof).** For each d>=1 put f_d(n)=h(4^d*n). Given 1<=d<e, set m=2^(e-1)-1 and n=m^2+1. Let delta=sqrt(m^2+1)-m=1/(sqrt(m^2+1)+m). Since m>=1,

    2^e-2 < sqrt(m^2+1)+m < 2^e-1,
    1 < 2^e*delta < 2,
    0 < 2^d*delta < 1.

The last inequality follows from d<=e-1 and 2^(e-1)<=2^e-2 for e>=2, with strictness from the denominator. Now floor(2^d*sqrt(n))=2^d*m, an even integer, while floor(2^e*sqrt(n))=2^e*m+1 is odd. Hence f_d(n)=+1 and f_e(n)=-1. All these binary-kernel members are distinct: f_d is the depth 2d, residue 0 decimation. GC487's prefix-state lemma therefore rules out every finite canonical LSB-first DFAO for this sequence, using arbitrarily many pairwise distinguished positive continuations. No unproved density or digit-distribution property of an irrational number enters.

**Exact indexing cost.** Let b be the binary input length of n. Binary-search the integer interval from 0 to 2^ceil(b/2) for the largest x with x*x<=n; then return its parity. There are O(b) comparisons, each using schoolbook O(b^2) bit multiplication and O(b) comparison, hence O(b^3) bit operations and O(b) workspace suffice. The n0 case is immediate. Integer arithmetic gives exact floor(sqrt(n)); no floating-point rounding assumption. This upper bound is sublinear in n despite the infinite kernel, balance and aperiodicity.

**Outcome and next.** All three predictions follow from the hand derivations, not measurements; the declared counterfactual fails. This extends GC481's Thue-Morse guard beyond finite-state indexers: even proving infinitely many Rule 30 decimations would still leave arithmetic shortcuts unaddressed. It supplies no Rule 30 shortcut. Retain the explicit family as a control for future lower-bound proposals and return to the selected orbit's actual structure, rather than collect further generic complexity obstructions.

## GC491 — Finite-row velocity retains the row, through a nonlocal inverse (2026-10-08)

**Bears on.** Problem 2's signed non-flipping target and Problem 3 representation cost. Return from generic complexity controls to Rule 30's actual velocity field. The coupled law is a specialization of reviewed G114, and the reconstruction is elementary left-permutative inversion with a finite right boundary; no novelty or prize claim. Existing-record search found G97's Rule 210 velocity identity and G114's general damage law, not this combined finite-row reconstruction scope statement. Independent reading pending. No experiment or Local job.

**Checks chosen first.** Predict that the entire temporal velocity of a finite Rule 30 row determines that row uniquely. The independent zero-row control must reconstruct zero. Counterfactual: a fixed-radius velocity window suffices to reconstruct its centre for every finite row, must fail on truncated checkerboards. Unexpected: not every finite binary velocity field has a finite-row preimage. These are hand checks, not a census.

**Coupled law.** Write u_t(i) for Rule 30, and v_t(i)=u_t(i) XOR u_(t+1)(i). Binary arithmetic gives

    v_t(i)=u_t(i-1) XOR ((1-u_t(i))*u_t(i+1)).

Thus v_t=G(u_t), where G is Rule 210. Apply G114's exact difference law to the two consecutive Rule 30 rows (u_t,u_(t+1)); they are both evolved by Rule 30. At one site, suppressing t, write u_c,u_r and v_l,v_c,v_r for the indicated neighbours. Then

    u_next = u_c XOR v_c,
    v_next = v_l XOR ((1-u_r)*v_c) XOR ((1-u_c)*v_r) XOR (v_c*v_r).

Equivalently v_next=F30(v) XOR (u_r*v_c) XOR (u_c*v_r). This is background-coupled, not autonomous Rule 210 evolution. It supplies an exact two-layer representation; no signed-cancellation estimate follows from its existence.

**Finite-row inversion.** For any finite row u, let v=G(u). Rearranging the Rule 210 equation at site i+1 gives

    u(i)=v(i+1) XOR ((1-u(i+1))*u(i+2)).

Choose a right boundary beyond both supports, put the two rightmost u bits to 0, and recur leftward. If u is nonzero with rightmost black site R, v has rightmost black site R+1: its input there is 100, and all sites farther right have 000. Therefore the boundary can be chosen from v itself. Two finite preimages of the same v agree from the right boundary by induction, proving injectivity. The zero field reconstructs zero and has no nonzero finite preimage. Reconstruction is a serial scan across the stated finite interval, an upper bound for this method only.

**Unexpected proper-image guard.** Let v have its sole black cell at 0. Any finite preimage would have rightmost black cell at -1. The recurrence gives u(-1)=1,u(-2)=0 and, for every subsequent site to the left, alternating 1,0. This does not terminate. Hence this finite v is not in the image of finite rows. Injectivity does not justify treating all finite velocity fields as admissible states.

**No bounded local inverse (hand counterexample).** Fix any proposed radius r. The infinite checkerboard with black even sites is fixed by Rule 30: triples 010 and 101 preserve their centre values. Its velocity is therefore identically zero. Truncate that checkerboard to [-r-2,r+2], giving a finite row with u(0)=1. Every radius-one input determining v on [-r,r] still lies inside the checkerboard patch, so v is zero throughout that window. The all-zero finite row also has zero velocity there but u(0)=0. This refutes every uniform fixed-radius inverse, on actual finite-row images. It does not contradict global injectivity: the truncation boundaries give different velocity farther away. Nor does it rule out a faster nonlocal reconstruction algorithm.

**What changes.** Velocity alone has not thrown away information on the finite-row domain; after full reconstruction it can be evolved by G composed with F30 composed with G inverse on the proper image of G. The image is forward invariant because Rule 30 preserves finite support. But the inverse cannot be a fixed-radius local rule, and the coupled law retains the background explicitly. The selected singleton orbit lies in this domain at every finite time. Any balance proposal based on its velocity still needs signed orbit-conditioned cancellation; replacing the background by an autonomous Rule 210 orbit remains invalid. Next inspect that coupled cancellation rather than infer randomness from invertibility or locality from information preservation.

## GC492 — Exact three-state test for finite velocity admissibility (2026-10-08)

**Bears on.** GC491's actual Rule 30 velocity representation and its proper finite image. Complete that scope obligation, then return to signed temporal cancellation. This is elementary finite-row inverse algebra, independent reading pending; not a Rule 30 balance or fast-indexing theorem. It uses GC491's recurrence and standard deterministic state merging, with no external theorem or novelty claim. No experiment or Local job.

**Chosen hand checks.** Predict a fixed finite machine recognizes which finite velocity words reconstruct finite rows. Independent controls: zero field and the singleton row's velocity 101. Counterfactual every finite velocity word is admissible fails on 1. Unexpected: inverse pairs 10 and 11 have identical future transitions and can be merged for acceptance, even though they are different reconstructed bit pairs. Check all eight pair/input cases before claiming the merge.

**Exact inverse states.** Process velocity sites from right to left, starting beyond its support with pair(a,b)=(0,0). Reading z=v(j) produces x=u(j-1)=z XOR ((1-a)*b) and the next pair(x,a). The full pair transitions are

| Pair | Read 0 | Read 1 |
|---|---|---|
| 00 | 00 | 10 |
| 01 | 10 | 00 |
| 10 | 01 | 11 |
| 11 | 01 | 11 |

These eight entries follow directly by substituting a,b,z, independently of any sampled row. Merge 10 and 11 into A; call 00 C and 01 B. The resulting machine is

| State | Read 0 | Read 1 |
|---|---|---|
| C | C | A |
| A | B | A |
| B | A | C |

Start at C and accept only C. After the supplied finite word, all remaining velocity cells to the left are 0. State C then stays at 00, giving a finite preimage. The other states alternate A,B forever (the full pair 11 first enters 01), so the reconstructed left tail contains infinitely many black cells. Therefore acceptance is equivalent to the existence of a finite preimage. GC491 gives uniqueness. Padding the supplied word by zeros on either end does not change acceptance, so the statement is well-defined for finite fields rather than an arbitrary word boundary.

**Controls and minimality.** Zero stays C and accepts;1 ends A and rejects. The singleton row's velocity has black cells at -1 and 1, so its word 101 gives C,A,B,C and accepts. More generally two pulses separated by k zero cells give word 1*0^k*1 and accept exactly when k is odd; this checks the alternating tail mechanism at every separation by hand. All three states are reachable (empty word,1,10). C is distinguished from the other states by immediate acceptance; A and B are distinguished by continuation 1. Thus any deterministic recognizer for this right-to-left finite-word language needs at least three states. This is a spatial admissibility state count, not a time-indexing lower bound.

**Outcome and limit.** The full finite image of Rule 210 has a three-state membership test, despite its inverse not being a fixed-radius local map. This illustrates a distinction GC491 needs: nonlocal reconstruction does not imply a complicated membership language. The machine supplies acceptance only; the original inverse recurrence recovers the bits by retaining the actual pair and emitting x. It does not make the selected Rule 30 centre trace automatic, turn velocity evolution into Rule 210, or estimate its signed non-flipping rewards. The spatial word is a velocity row, not the temporal trace's binary index. This admissibility subproblem is now closed conditionally on the written hand proof; next use the background-coupled law for actual signed temporal cancellation, without adding image-language censuses.

## GC493 — Local signed cancellation does not lift to a velocity-preserving orbit pairing (2026-10-08)

**Bears on.** Problem 2's actual signed non-flipping pairs, GC481/483. Audit a concrete cancellation mechanism rather than expand the velocity-image census. Elementary local Boolean identity and finite-row scope obstruction, hand reading pending. The reward is already GC483's; the finite injectivity premise is GC491, still pending reading. No novelty, experiment or Local run.

**Checks chosen first.** Predict an involution on physical triples that preserves the instantaneous velocity and reverses the signed pair reward. Independent four centre-pair controls are 00,01,10,11. Counterfactual this gives a global velocity-preserving finite-row pairing must fail. Unexpected: a finite zero/singleton realization should complement the first two centre samples but lose complementation at the third. These are direct hand checks, not a numerical distribution claim.

**Exact local shear.** For a triple (l,c,r), velocity is v=l XOR ((1-c)*r). Define

    J(l,c,r)=(l XOR r, 1-c, r).

Applying J twice returns the triple. The new velocity is (l XOR r) XOR (c*r), equal to l XOR ((1-c)*r). Thus both c and its next bit c XOR v are complemented. The reward g=(1-2c)*[v=0] changes to -g. GC483's four nonzero-weight triples are paired 000 with 010, and 101 with 011. Flip pairs 01 and 10 have reward 0, while 00 and 11 have opposite rewards. This is exact local cancellation, without any probability assumption.

**Where a distributional conclusion would need evidence.** On a uniform ensemble of the eight triples, J is a bijection, so its average reward is 0. More generally a J-invariant triple distribution has zero signed reward. For the singleton orbit's empirical triples at even times, no such invariance has been proved. The exact required difference remains the count of 000 plus 101 minus 010 minus 011. Defining J does not make the actual visit counts agree, and no uniform-random-row result transfers to those time visits.

**Failure of a simultaneous local lift.** Applying this same triple rule at every spatial site would require each cell to be complemented when serving as centre but unchanged when serving as its left neighbour's right input. These requirements are inconsistent. A targeted transformation can flip the centre and flip the left cell when r=1, retaining v only at that chosen site. It changes other velocities in general. Stronger still, GC491's finite-row injectivity implies that any two finite rows with identical entire velocity fields are identical; therefore they cannot have opposite centre bits. Conditional on that hand lemma, no global velocity-preserving pairing of distinct finite rows can implement the proposed cancellation.

**Unexpected finite history control.** Start with the zero row, whose centre samples are 000 forever. Its local triple is 000. Targeted J makes only the centre black, giving the singleton row. Its first row is {-1,0,1}, so its first two centre samples are 11, complementing 00 as required. Its second row is {-2,-1,2}, so its third centre bit is 0; complementation would require 1. The initial velocities already differ away from the centre: zero versus black sites {-1,1}. This explicit finite control shows that matching one velocity and one opposite reward supplies neither a sustained complementary history nor a common global velocity field.

**Outcome and next.** The local involution is a valid algebraic cancellation control, but its promotion to a finite-row orbit pairing fails. This closes that particular static velocity-preserving pairing route, not every signed pairing, coupling or balance method. Any selected-orbit cancellation must control visit counts, a justified time pairing, or cumulative residuals; preserving the entire velocity while flipping a finite row's centre is unavailable. No density estimate or prize conclusion follows. Stop this local lift rather than search larger patches for the same impossible global premise.

## GC494 — Run-pair cancellation needs a within-pair time bound (2026-10-08)

**Bears on.** Problem 2's actual temporal signed cancellation after GC493's failed static lift. This is an elementary exact reduction for a binary trace, hand reading pending, not an estimate on Rule 30 runs. Existing record GC481 retains signed non-flipping pairs and GC489 warns against dyadic-only totals. Here the sampling boundaries are actual sign changes. No novelty claim, experiment or Local job.

**Chosen checks.** Predict that discrepancy bounds at every run endpoint extend to every prefix with no separate gap hypothesis. Controlling only pairs of runs needs a within-pair time bound. Counterfactual equal opposite-colour run lengths in every pair suffice for limiting balance must fail on doubling pairs. Independent positive controls are alternating spins and GC490's square-root parity. Unexpected: interpolation at all run endpoints removes a gap premise, whereas pairing those endpoints restores it.

**All-run endpoint equivalence.** Let s(n) be a spin trace with infinitely many sign changes and S(N)=sum(n<N)s(n). Let R_j be successive run boundaries, including 0. Between R_j and R_(j+1), S is affine with slope +1 or -1. For N in that interval put theta=(N-R_j)/(R_(j+1)-R_j). Then

    S(N)=(1-theta)*S(R_j)+theta*S(R_(j+1)),
    N=(1-theta)*R_j+theta*R_(j+1).

If both endpoint discrepancies have absolute value at most epsilon times their endpoint times, the triangle inequality gives |S(N)|<=epsilon*N. Therefore S(N)=o(N) if and only if S(R_j)=o(R_j). No bound on the gaps is an extra hypothesis here. Traces with only finitely many sign changes are eventually constant and fail balance, so they are handled separately.

**Paired-run version.** Let T_j=R_(2j), and call the next two opposite-sign run lengths a_j,b_j. Both are positive. The sign at the start of every pair is the same sigma. Define

    D_j=S(T_j)=sigma*sum(i<j)(a_i-b_i),
    T_j=sum(i<j)(a_i+b_i).

Then all-prefix balance is equivalent to the two obligations

    D_j=o(T_j),
    max(a_j,b_j)=o(T_j), as j tends to infinity.

For sufficiency, any intermediate prefix differs from D_j by at most a_j+b_j, so divide by N>=T_j. For necessity, full balance first gives D_j=o(T_j). For the first run, a_j=|S(T_j+a_j)-S(T_j)|. Once all sufficiently late discrepancies are at most epsilon times their times, a_j<=epsilon*(2T_j+a_j), hence a_j/T_j<=2epsilon/(1-epsilon). This tends to 0. Apply the same argument to the second run starting at T_j+a_j; its start is asymptotic to T_j, so b_j/T_j tends to 0 as well. The initial pair at T_0=0 is irrelevant to the limit. These are actual signed sums, not sums of absolute run imbalances.

**Retained counterfactual.** Take runs of spins +,- with lengths a_j=b_j=2^j. Every paired endpoint has D_j=0, at T_j=2*(2^j-1). At the midpoint N_j=T_j+2^j, however, S(N_j)=2^j and S(N_j)/N_j tends to 1/3. Perfect cancellation at every pair boundary does not give a limiting density because within-pair lengths remain macroscopic. This is an explicit binary sequence, not a Rule 30 orbit or finite-seed counterexample.

**Independent controls.** Alternating spins have a_j=b_j=1, D_j=0 and max(a_j,b_j)/T_j tends to 0, so the criterion gives balance. For GC490's h(n)=(-1)^floor(sqrt(n)), pair j has a_j=4j+1,b_j=4j+3, T_j=4j^2 and D_j=-2j. Both obligations hold directly. This recovers its balance without invoking a kernel or its prior all-prefix bound. A constant trace is outside the infinitely switching case and has |S(N)|=N, as required.

**What the selected orbit still needs.** For the singleton Rule 30 trace, this gives a precise possible time-pairing route: control the cumulative differences between successive black/white run lengths and prove that each pair's duration is sublinear in elapsed time. Neither bound is established here. Proving only equal total lengths at selected pair endpoints is insufficient; conversely controlling all run endpoints already supplies the duration consequence. Do not infer a duration bound from a finite observed maximum run or from aperiodicity. Next seek an actual dynamical constraint on these run boundaries, rather than another local symmetry or image-language census. No Problem 2 or prize conclusion.

## GC495 — Exact black-run length from the first left checkerboard mismatch (2026-10-08)

**Bears on.** GC494's actual temporal duration obligation for Problem 2. G18 already proves that a black stretch forces a checkerboard prefix at its start; this block adds the converse and exact first-failure certificate using G4.4's leftmost pivot. No novelty claim for either mechanism, and no sublinear estimate. Hand reading pending; no experiment or Local computation.

**Chosen checks.** Predict that, from a black centre at any instant, the number of consecutive black centre samples is exactly the first depth where the row disagrees with the left checkerboard. Independent controls: singleton row and a flipped bit at depth 1. Counterfactual that finiteness by itself turns this into a sublinear duration bound must not be accepted. Unexpected: singleton left-edge parity improves the basic linear support bound at odd times.

**Exact certificate.** Let a row u have u(0)=1. The reference checkerboard has value 1 at even left depths and 0 at odd depths. Let d>=1 be the first depth at which u(-d) differs from that reference, assuming such a depth exists. Then its centre is black at times 0,...,d-1 and white at time d, independently of every initial bit to the right of 0 and every bit farther left than-d.

Proof: construct a comparator row z agreeing with u on all nonnegative sites and equal to the checkerboard on negative sites. Its whole nonpositive checkerboard stays fixed. At a black site the OR masks its right neighbour and its white left neighbour produces black; at a white negative site both neighbours are black and produce white. In particular the centre remains black regardless of the positive tail. The two initial rows agree on every site greater than-d. Before time d, the centre cone cannot see any difference. At time d, their only differing cone input is the leftmost bit at-d. G4.4's triangular identity puts that bit into the output as XOR with coefficient 1, while every other cone input agrees. The centre therefore flips relative to the black comparator. This proves both the duration and its end. If no mismatch exists, the same comparator argument gives a black centre forever; that case requires an infinite left checkerboard and is excluded for finite rows.

**Hand controls.** A singleton at 0 has left bits 0,0,..., so depths 0,1 agree and depth 2 fails. Its first three centre samples are 110, matching d2. Setting its depth 1 bit to 1 creates a first mismatch at 1 and the next centre update is 0 regardless of the right bit, since 1 XOR(1 OR r)=0. At any larger depth d, arbitrary outer tails remain irrelevant up to and including the failure tick by the specified cone and pivot, not a tested tail census.

**Elementary singleton bound and parity guard.** At physical time t, the singleton orbit has no black cell left of-t and its leftmost cell at-t is black (G98). If t is odd and the centre is black, depth t already disagrees with the required white checkerboard bit, so d<=t. If t is even, depths beyond t are zero and depth t+2 is the first forced black checkerboard position outside the support, so d<=t+2. At t0, d2 attains that bound. This is an elementary linear bound for the remaining run at a black instant, not a maximal-run measurement. It supplies no d=o(t) conclusion, and no relation between opposite-colour run lengths.

**Next actual obligation.** A sublinear upper bound on the left checkerboard match length at the starts of the singleton trace's black runs would establish the black half of GC494's within-pair duration condition. That bound is open. It must concern the actual time-t row near the centre, not the universal edge strip or a finite observed run maximum. White durations still require their separate latch/overlap constraints; signed cumulative black/white length differences remain unbounded. This is a precise spatial certificate for one temporal quantity, not a balance proof. Do not enlarge a checkerboard census before finding a dynamical estimate for this selected row.

## GC496 — White-run first arrival requires a two-sided resonance (2026-10-08)

**Bears on.** GC494's white-duration obligation. Hand finite-cone application of G4.4's pivot and G98's singleton left edge, pending reading; no novelty or duration estimate for the selected orbit. Predicted before derivation: unequal nearest-black distances give exact first arrival, equal distances cancel only that arrival. Independent one-sided pulse controls; counterfactual a tie gives an infinite white wall must fail. Unexpected: arbitrary exterior bits cannot change the first-arrival verdict. No experiment.

Let a row have centre 0. Let p,q be its nearest black-cell distances on the left and right, respectively, using infinity if a side is empty. If m=min(p,q) is finite, the centre remains 0 at times 0,...,m-1 because those cones contain only zeros. At time m its cone has only the initial endpoint black bits: no other black cell lies inside it. A right endpoint alone gives 1 by G98's left-edge propagation on the zero background. Adding a left endpoint flips that output by G4.4's leftmost XOR pivot. A left endpoint alone also gives 1. Therefore if p!=q the remaining white-run length is exactly m; if p=q=m, the centre is still 0 at time m, so the length is at least m+1. If both distances are infinite, the row is zero and stays zero.

A pulse at -1 or 1 individually gives initial centre 01; together the seed {-1,1} gives 0001. Direct hand rows are {-2,-1,1,2} at tick 1 and {-3,-2,1,3} at tick 2, whose left/right centre neighbours 0,1 force black at tick 3. The tie cancels the first arrival but does not guarantee sustained cancellation. Exterior input outside [-m,m] is outside the exact first-arrival cone, so no sampled-tail assumption enters.

Consequently a white run lasting beyond its nearest initial black distance must begin with equal nearest distances on the two sides. This is only its first resonance condition. Repeated cancellation can involve farther sites and background evolution; no bound on its frequency or duration follows. Together with GC495 it gives explicit, asymmetric spatial certificates for black durations and for the first obstruction to ending a white duration. Both sublinear run-duration and signed run-length cancellation estimates remain open.

## GC498 — Compact-language meaning of the infinite-width entropy question (2026-10-08)

**Bears on.** Owner-directed portfolio GC497 question 4, CONSTELLATION rows 5/6. Standard elementary compactness and word-count argument, no novelty claim; hand reading pending. Existing G129 supplies compact trace classes, G53 distinguishes upper entropy bounds from physical equality, and G66 warns about support/length quantifiers. No entropy census, spectral fit or Local job.

**Chosen checks.** Predict that nested closed shift spaces have entropy equal to the infimum of their entropies, because finite languages stabilize and both operations are infima. Counterfactual positive entropy at every finite width forces a positive infinite-width limit must fail on shifts whose ones are increasingly separated. Independent controls: full binary shift and a single fixed periodic orbit. Unexpected: a zero-entropy language can still contain an aperiodic trace; check Thue-Morse by a direct factor-count bound.

**Precise model and theorem.** On a fixed finite alphabet, let X_1 contain X_2 contain ... be nonempty closed one-sided shift-invariant sets. For the period 2 wall, the intended alphabet is one visible symbol per complete wall period, with a fixed phase and common endpoint conventions. Define X_infinity as their intersection. Let a_w(n) count its width-w allowed length-n words; by shift invariance these can be placed at the start of an element of X_w. Compactness implies

    language_n(X_infinity)=intersection_w language_n(X_w).

Indeed for a word admitted at every width, intersect the nested nonempty compact sets of width-w traces starting with that word. They have a common trace. The reverse inclusion is immediate. At fixed n, the finite decreasing word sets eventually stabilize, so a_infinity(n)=inf_w a_w(n).

Word counts obey a(n+m)<=a(n)*a(m), since a concatenated word is determined by its prefix and suffix. Hence h(X)=inf_n log2(a(n))/n, the usual subadditive word-count entropy. It follows exactly that

    h(X_infinity)=inf_n inf_w log2(a_w(n))/n
                 =inf_w inf_n log2(a_w(n))/n
                 =inf_w h(X_w).

All sets here are nonempty, so no logarithm of zero or empty-system convention is hidden. This identifies the limiting quantity; it does not determine its value or a convergence rate.

**Positive-finite-width failure.** Let X_w forbid two ones with fewer than w intervening zeros. It is closed, shift-invariant, nonempty, and the family is nested. Concatenate arbitrary blocks 0^(w+1) or 1 followed by w zeros. There are at least 2^floor(n/(w+1)) allowed words of length n, so h(X_w)>=1/(w+1)>0. But X_infinity contains only sequences with at most one 1. Its length-n language has n+1 words, so its entropy is 0. Thus every finite-width entropy can be positive while the infinite-width entropy is zero. A finite plateau supplies no uniform lower bound.

**Independent and unexpected controls.** A constant family of full binary shifts gives a(n)=2^n and entropy 1 at every stage and in the intersection. A constant family consisting of the shifts of a fixed periodic word has bounded word counts and entropy 0. For Thue-Morse, choose 2^k with n<=2^k<2n. Each length-n factor lies inside two adjacent length 2^k substitution blocks, each either the standard block or its complement. There are at most four adjacent block types and 2^k offsets, so factor count is at most 4*2^k<8n. Its orbit closure therefore has entropy 0, while its generating trace is aperiodic by GC481's argument. This explicitly rejects identifying zero entropy with periodicity.

**Application obligation and next.** Before applying the theorem to the reported wall automata, identify their actual closed infinite-trace languages, prune paths that have no infinite continuation, verify nesting under the same visible-period shift, and match the certified matrix quantity to word-count entropy (or retain it only as an upper bound). These hypotheses are not certified here for every width. If they hold, a uniform positive lower bound implies positive entropy for genuinely infinite-width compatible traces. It still supplies no finite-support initial row. A zero value would mean subexponential language growth, not periodicity or a prize proof. Next audit one existing automaton's endpoint and infinite-continuation conventions against this model before extending any numerical width.

## GC499 — Existing layer automata meet the compact-language hypotheses (2026-10-08)

**Bears on.** GC498 and portfolio question 4, constellation rows 5/6. Source and hand audit of `entropy2.c`, its scalar predecessor `entropy.c`, and the exact inequality checker in `rule30_squeeze.py`. No new numerical run or novelty claim. Both startup probes again print ALL CHECKS PASS. Independent reading is pending; this is a mathematical interpretation of the implemented model, not a complete C implementation verification.

**Predictions and guards.** Before the audit, predict that every admitted finite visible word extends to an infinite trace, and the model supplies nested closed shift languages under one complete wall period. Counterfactual: the printed power-iteration value alone is a certified entropy, must fail. Unexpected check: the width 1 model is exactly the language forbidding adjacent visible ones, independently recovering its golden-ratio entropy. Do not extend the width census.

**The actual model.** Fix width w >= 1. The initial layer consists of arbitrary bits at sites 1 through w; column 0 is externally clamped to 0,1,0,1,... . The boundary bit at site w+1 can be chosen independently at each tick. Observe site 1 at even times. Let X_w be the set of infinite visible traces produced by this controlled finite layer. The code initializes its subset state with all 2^w rows. Reading b filters on the current site-1 bit, then applies both boundary choices first with wall value 0 and then with wall value 1. Thus a word of length n prescribes outputs at times 0,2,...,2n-2, and its final subset is at time 2n. This is output-before-update coding, with a fixed white phase.

Every nonempty final subset has an infinite continuation: choose one row in it, then choose any infinite boundary sequence, for example all zeros. Each physical update is total. Consequently a word rejected only by an empty subset has no realization, while every accepted word is the prefix of an infinite controlled trace. No additional pruning of dead-ending paths is necessary for this particular automaton. This conclusion would not automatically apply to a model with extra terminal or initial-tail constraints.

**Closedness, shift and nesting.** The product of the finite initial-row set and the compact space of boundary-bit sequences is compact. The map to the visible trace is continuous by finite-time dependence, so X_w is closed and nonempty. Dropping one visible symbol corresponds to advancing the layer two ticks; its new row is still an allowed arbitrary initial row and the wall has the same phase. Hence X_w is invariant under the one-symbol shift. Restricting a width-(w+1) realization to its first w sites supplies a permitted boundary sequence for width w, proving X_(w+1) is contained in X_w. These are precisely GC498's hypotheses.

A trace in every X_w also admits a coherent infinite right-half realization: impose its visible values in the compact space of initial right rows and forward diagrams, together with all local equations and the clamped wall. Every finite collection of constraints is contained in a sufficiently wide controlled strip, so compactness supplies their common solution. This does not constrain the initial right tail to be finite or impose a finite initial left tail. In particular it does not turn an entropy statement into a finite-seed existence theorem.

**Word growth and certification.** Shift invariance and extension mean the accepted length-n prefixes are exactly the length-n factor language of X_w. The deterministic subset graph has one successor per label, so paths from its initial subset count words without multiplicity. Its finite adjacency matrix counts both labelled edges when they share a successor. All stored states are reachable. The exponential word-growth rate is its spectral radius, giving h(X_w)=log2(rho(A_w)) per visible symbol. This is the standard finite-graph growth fact used by the original script, now with its language conventions checked.

The source's finite power iteration still provides an approximation, not an exact value or error certificate. The separate rational inequality checker proves A_w W <= q W componentwise for a positive integer vector W. Iterating gives a rigorous word bound C*q^n and therefore h(X_w)<=log2(q). An exact upper certificate does not itself prove equality to that upper bound or supply a positive lower bound. Accordingly GC498 identifies the actual limit as inf_w h(X_w); infima of certified upper bounds remain upper bounds on that limit.

**Independent hand control.** At width 1, write the current bit c and the two boundary inputs u,u'. The two updates give c'=c OR u and c''=1 XOR (c' OR u'). If c=1 then c''=0. If c=0 then either next visible value is possible. Thus visible 11 is forbidden, and every infinite word without 11 is realized by selecting boundary inputs for its consecutive transitions. Its two-state adjacency matrix is [[1,1],[1,0]], whose Perron root is (1+sqrt(5))/2. This checks the phase, output timing and edge multiplicity independently of the subset construction. The constant-zero continuation also demonstrates that accepted prefixes need not become dead ends.

**Outcome and next.** For the unconstrained-initial-row 0101 controlled-layer model, the compact-language bridge is complete as a hand argument pending second reading. It does not establish positive or zero limiting entropy, certify every implementation detail, or settle either finite-support boundary. Next seek an analytic cross-width inequality or a uniform lower-language construction; further digits alone would not settle the question.

## GC500 — A finite backward cone gives an explicit entropy-language diagonal (2026-10-08)

**Bears on.** Portfolio question 4, GC498/GC499, constellation rows 5/6. Elementary finite-propagation refinement of the compact argument, hand reading pending. Checked prior GC483 finite-cone truncation, G129 fixed-support compactness and G130 finite-prefix scope. No novelty claim, numerical run or new Local job. GC499 startup checks remain current.

**Predictions before the hand block.** Length-n visible words stabilize by controlled-layer width 2n-1. A finite initial right tail should suffice to realize each such word when the wall is externally clamped. Counterfactual: these horizon-dependent finite tails supply one finite-tail realization of every entire infinite trace, is an invalid quantifier inference. Unexpected check: finite-right-tail traces are dense in the unrestricted clamped-wall language, despite lacking a common support bound. Independent controls below use the first two visible outputs directly.

**Explicit stabilization.** Let L_w(n) be GC499's allowed length-n visible words, sampled at times 0,2,...,2n-2. A radius-one update makes the output at site 1 and time t depend only on initial right sites through 1+t and the intervening clamped wall values. Thus all these observations depend only on initial right sites 1 through 2n-1. For any w>=2n-1, the free input at site w+1 cannot reach an observed site before the last sample. The two extra updates performed after the last visible filtering do not remove any rows, because updates are total.

Take a width-w realization and copy its initial right sites through 2n-1 into an infinite right half, setting every farther initial cell to zero. Evolve it with the same externally clamped wall. Induction on the backward cones preserves the entire visible word. Conversely every infinite right-half realization restricts to a permitted width-w controlled realization. Therefore

    L_w(n)=L_infinity(n) for every w>=2n-1.

This is a sufficient width bound, not an assertion that smaller widths always differ. It strengthens GC498's unspecified eventual stabilization only for this particular controlled-layer model. It does not control the convergence rate of h(X_w) as w increases, because computing a fixed-width entropy takes a separate arbitrarily long word limit.

**An exact finite-count target.** Define C_n as the number of distinct length-n visible outputs produced by the 2^(2n-1) initial right words of length 2n-1 with zero initial tail, keeping column 0 externally clamped. The stabilization argument and GC499 give

    C_n=a_infinity(n)=a_(2n-1)(n),
    h_infinity=inf(n>=1) log2(C_n)/n.

Each C_n is computable by finite enumeration, but this supplies no efficient algorithm or proposed large run. The number of possible initial words is an upper bound on the enumeration, not a lower bound on distinct outputs. For integer k>=1, h_infinity<1/k has a finite witness C_n^k<2^n for some n. Conversely h_infinity>=1/k requires C_n^k>=2^n for every n. Zero entropy is equivalent to having a finite witness for every k; positive entropy is equivalent to one k satisfying the lower inequality for all n. These are exact integer formulations of the missing uniform estimate, not a proof of either outcome. A finite set of positive counts cannot discharge the latter universal obligation.

**Independent hand controls and endpoint guard.** C_1=2, from the arbitrary first initial bit. For two samples write initial sites 1,2,3 as a,b,c. The first update gives site 1 value a OR b and site 2 value a XOR (b OR c). The next wall value is 1, hence

    visible(1)=1 XOR ((a OR b) OR (a XOR (b OR c))).

If a=1 the second visible bit is 0. If a=0 it is 1 exactly when b=c=0. Thus C_2=3, with words 00,01,10, agreeing independently with GC499's no-11 language. Initial triples 000 and 001 have the same first two sites but give 01 and 00, respectively. Site 3 can matter at this horizon; this does not establish a minimal width for language stabilization, since free boundary inputs at smaller widths can already realize these words.

**Unexpected density and retained support failure.** For any unrestricted clamped-wall trace and any n, its prefix is realized by a right seed supported within 2n-1. Consequently the set of traces from finite initial right rows is dense in X_infinity in the prefix topology. The finite row chosen can change with n. Density does not say this set is closed or that one finite seed realizes a prescribed infinite trace. Independent sequence-space control: eventually-zero sequences realize every finite binary word and are dense in the full binary shift, but do not realize the all-ones infinite sequence. This illustrates the quantifier failure without asserting such a counterexample inside Rule 30. The externally clamped wall is also essential: these finite right rows are not claimed to extend to finite global Rule 30 seeds with that wall.

**Next.** Seek a proved upper family C_n<=2^(epsilon_n*n), epsilon_n tending to zero, or a uniform exponential lower count. Any finite-count instrument should retain exact output deduplication and the clamped-wall convention. No entropy value, general indexing lower bound or finite-support prize result is established here.

## GC501 — Collision decay is a sufficient lower-language route, with an immediate boundary guard (2026-10-08)

**Bears on.** GC500's uniform distinct-output count and portfolio question 4, constellation rows 5/6. Elementary Cauchy-Schwarz argument plus exact two-sample Rule 30 algebra; hand reading pending. Existing fair-full-line ensemble arguments and G53's visible coding have different boundary hypotheses. No novelty claim, experiment, stationarity assumption or Local job. Startup checks from GC499 remain current.

**Chosen checks.** Predict that exponentially decaying collision probabilities for two independent fair initial right rows suffice for positive unrestricted clamped-wall language entropy. Counterfactuals: the visible outputs are uniform over allowed words, and each conditioned common visible history has a uniformly strict next-step collision contraction. Both must fail already at two samples. Unexpected: fair initial right bits do not induce a stationary visible process next to this clamped wall. Keep the lower-bound route sufficient only.

**Exact collision target.** Choose the infinite initial right row iid fair, with column 0 externally clamped to 0101. Let p_n(v) be the probability of a visible prefix v of length n. Finite cones make this a consistent process, even without stationarity. If F_n maps the 2^(2n-1) initial words of GC500 to visible words and f_n(v) is the number of preimages, then p_n(v)=f_n(v)/2^(2n-1). Every allowed prefix has positive probability. For two independent initial right rows define kappa_n as the probability that their first n visible symbols agree. Exactly,

    kappa_n=sum_v p_n(v)^2
           =sum_v f_n(v)^2 / 2^(4n-2).

Cauchy-Schwarz gives 1=(sum_v p_n(v))^2<=C_n*kappa_n. Thus C_n>=1/kappa_n. If constants K<infinity and delta>0 satisfy kappa_n<=K*2^(-delta*n) for all sufficiently large n, the word-count entropy limit gives h_infinity>=delta. This needs neither uniform output probabilities nor stationarity. It also does not supply that collision bound: the two copies share the deterministic wall but have independent initial right rows, and their conditioned backgrounds must remain in the argument.

**Independent exact two-sample control.** GC500's direct three-bit algebra gives visible probabilities p_2(00)=3/8, p_2(01)=1/8 and p_2(10)=1/2. Therefore kappa_1=1/2 and kappa_2=13/32. The lower count bound is C_2>=32/13, consistent with the independently known C_2=3. Uniform allowed outputs would instead give collision probability 1/3; that counterfactual is refuted. The first visible bit is fair, but the second is black with probability 1/8. Consequently this particular initial-right product measure is not stationary under advancing one visible period, even though its support language is shift-invariant by GC499. Support invariance and measure invariance are different obligations.

**Forced matching defeats pointwise contraction.** Conditional on both first visible bits being 1, both next visible bits are deterministically 0, so the next conditional collision probability is 1. This event has probability 1/4. Conditional on both first bits being 0, each next bit is independently black with probability 1/4, giving matching probability 5/8. Hence kappa_2=(1/4)*1+(1/4)*(5/8)=13/32, an independent decomposition of the same exact value. A strict contraction required after every common history is already impossible. A useful argument must instead control suitable blocks or accumulated branching, preserving the history-dependent conditional law; these two steps establish no such bound.

**Sufficiency guard.** Positive support entropy does not force exponential collision decay for an arbitrary chosen full-support measure. On the full binary shift take the mixture of half a point mass at the all-zero sequence and half the fair iid law. Every finite word has positive probability, so its support has entropy 1, but two independent samples both choose the point mass with probability 1/4. Their collision probability is at least 1/4 for every n. This is a sequence-space control, not a statement that Rule 30 induces that mixture. Failure of the proposed fair-right collision bound would therefore not by itself prove zero language entropy.

**Outcome and next.** The positive-entropy problem now has a precise sufficient two-copy estimate, and its simplest uniform-per-symbol contraction is closed by an actual boundary calculation. No asymptotic collision decay or limiting entropy value is claimed. Next seek a justified block contraction or abandon this measure for an explicit lower-language construction; do not import full-line fair-ensemble stationarity into the clamped boundary.

## GC502 — A bounded output audit exposes an exact five-zero exclusion (2026-10-08)

**Bears on.** GC500/GC501 and portfolio question 4, constellation rows 5/6. Preregistered bounded proof controls, followed by a local hand proof pending independent reading. Searched the existing record for 00000 and visible zero-run bounds; no matching Rule 30 clamped-right statement found in that bounded search. Existing entropy automata already encode the restriction implicitly, so no novelty claim. This is a necessary companion-language condition under an imposed 0101 wall, not a prize exclusion.

**Predictions and instrument.** The committed probe `rule30_gpt_boundary_collision.py` retains its predictions before the first run: n=1 through 7 only, cone width 2n-1, literal decimal Rule 30 controls through n=4, initial two-sample counts and collision, blind expectation of a missing no-11 word by n=7, and the uniform-output counterfactual. Unexpected check identifies a shortest additional forbidden word and tests its proper factors. GPT's standard Python, exact integer counts, no horizon enlargement or Local job. The packed update uses the clamped wall; the independent set update includes the outward-growing finite right row and reads the literal rule table.

**Finite outcome.** All 170 literal comparisons PASS, as do the no-11 guard and the exact GC501 two-sample probabilities. Counts C_n for n=1,...,7 are 2,3,5,8,12,17,25. Collision probabilities are respectively 1/2, 13/32, 67/256, 1433/8192, 15689/131072, 209233/2097152, 1036453/16777216. Uniform-output CF is REFUTED. The blind missing-word prediction HELD: the first extra missing word is 00000, at n=5; all its nonempty proper factors are admitted. Extra missing no-11 words number 1,4,9 at n=5,6,7. These counts alone establish only their declared finite languages, not an asymptotic rate.

**Local five-zero proof.** Suppose consecutive even-time site-1 values are both 0. At the first even time write sites 2,3,4,5 as b,q,r,z. Their odd-time values, and site 1's odd value, obey

    site1_odd=b,
    site2_odd=b OR q,
    site3_odd=b XOR (q OR r),
    site4_odd=q XOR (r OR z).

Because the next wall value is 1, keeping site 1 zero at the next even time requires b OR q=1. Under this condition the next even pair (b_next,q_next) satisfies

    b_next=1-b,
    q_next=1 XOR ((b XOR (q OR r)) OR (q XOR (r OR z))).

Two transitions are independent of r,z: (b,q)=(0,1) forces (b_next,q_next)=(1,0), and (b,q)=(1,0) forces (b_next,q_next)=(0,0). The first follows because site3_odd=1. For the second, its two OR operands are 1-r and r OR z, whose OR is 1. Pair (0,0) cannot support the next zero-to-zero transition.

If five consecutive visible zeros existed, four such transitions would be required. If the initial b is 0, the first transition requires q=1, and the two forced pair transitions reach (0,0) before the third zero-to-zero transition. If the initial b is 1, the first transition leaves b_next=0; the second then requires q_next=1, after which the same two forced transitions reach (0,0) before the fourth zero-to-zero transition. Both cases contradict the proposed five zeros. The argument begins at any even time, uses arbitrary farther bits, and imposes no finite-support assumption.

**Sharpness and consequence.** Seven initial right sites 0111000, with a zero initial tail and the clamped wall, give four visible zeros. The hand-derived initial row was checked by both independent implementations. Thus the bound of four is attained. Every infinite compatible visible trace avoids both 11 and 00000. In every length-N window its number of ones is at least floor(N/5) and at most ceil(N/2), by partition into disjoint length-5 blocks and the no-adjacent-ones condition. This is a companion-visible frequency bound conditional on an alternating wall, not the singleton centre's one-half-frequency problem. The necessary finite-type language remains larger than the actual compatible language; its admissible words are not automatically realizable.

**Outcome and next.** The unrestricted companion cannot have arbitrarily long visible zero runs next to this wall. This closes that specific possible lower-language construction, but supplies no positive entropy lower bound or finite global wall exclusion. Stop the short-count scan. Next audit what the forced pair transitions say about coding by gaps between visible ones, retaining deeper-column compatibility rather than treating the necessary gap language as sufficient. Request independent reading of the local proof before catalogue filing.

## GC503 — Five initial right bits decide the first visible zero latch (2026-10-08)

**Bears on.** GC502's necessary gap code, constellation rows 5/6 and portfolio question 4. Exact hand refinement of the same local pair argument, pending independent reading. No extension of the short-word count scan or novelty claim. The wall stays externally clamped; these are durations in its visible companion, not physical centre runs of the singleton orbit.

**Predictions and unexpected check.** Before fixed controls, predict that four visible zeros occur exactly for initial right sites (0,1,1,r,z) with r OR z=1. Counterfactual uniform durations 1 through 4 conditional on an initially white companion must fail for fair initial right bits. Unexpected: this event needs five initial bits, whereas the generic backward cone for four visible samples reaches seven. Check all 32 five-bit patches with four exterior tails, using both packed and literal implementations; arbitrary farther-tail independence comes from the local proof rather than these finite controls.

**Exact duration formula.** At an even wall phase let initial right sites 1 through 5 be a,b,q,r,z, with arbitrary farther sites. Define R as the number of consecutive initial zero symbols in the visible trace; R=0 if a=1. For a=0 the complete classification is

    R=1  if b=0 and q=0;
    R=2  if b=1 and (q=0 or (r=0 and z=0));
    R=3  if b=0 and q=1;
    R=4  if b=1 and q=1 and (r OR z)=1.

These cases exhaust all five-bit assignments. For the proof, a zero-to-zero step requires b OR q=1. GC502 proves that pair (0,1) goes to (1,0), then to (0,0), which ends the zero run. Pair (1,0) goes directly to (0,0). For the only remaining pair (1,1), its odd site-3 value is 0 and its odd site-4 value is 1 XOR (r OR z), so its next even pair is (0,r OR z). If r OR z=0 the following zero-to-zero step fails; otherwise the forced two-step chain applies. Each successful step is justified by b OR q=1, and each failed step gives next visible bit 1 by the exact site-1 update. Thus the displayed durations are equalities, not just lower bounds. No farther bit enters these branches.

In particular 0000 occurs iff (a,b,q)=(0,1,1) and r OR z=1, and it forces the next visible bit 1. No-11 then forces the next bit 0. This is a local trigger with a definite endpoint; it does not make subsequent gaps independent or free choices.

**Exact initial-right law and controls.** For iid fair initial right bits, the unconditional probabilities of R=0,1,2,3,4 are 16/32,4/32,5/32,4/32,3/32. Conditional on a=0 the nonzero-duration probabilities are 1/4,5/16,1/4,3/16, with mean 19/8 visible samples. Thus the uniform-duration CF fails. Corresponding all-zero prefix probabilities at lengths 1,2,3,4 are 1/2,3/8,7/32,3/32; length 5 has probability zero. These agree with GC501 and GC502 without fitting a rate.

Probe `rule30_gpt_zero_cylinder.py` checks all 128 patch/tail combinations against both independent update implementations, all PASS. The tails are 0000,1111,0101,1010 within the nine-site cone for five visible samples; no horizon enlargement. They support the implementation of the formula, while the quantified farther-tail statement is the branch proof above. The fair distribution is only an initial-row calculation: GC501 already refutes stationarity under advancing a visible period. It cannot be reused as an iid renewal law for successive gaps.

**Outcome and next.** The zero latch is completely classified by a five-site cylinder. This supplies a concrete gap-4 trigger and closes the uniform initial-duration model, without settling entropy or finite support. Next use the necessary gap code as an upper-language bound or check a proposed actual recurrence; do not infer that arbitrary sequences of these four gap lengths are realizable. The original singleton balance and indexing questions remain open.

## GC504 — A gap of one zero cannot be followed by a gap of two (2026-10-08)

**Bears on.** GC502/GC503's necessary visible gap code, constellation rows 5/6 and portfolio question 4. Local hand proof, independent reading pending. Exploratory extraction from the already declared n=6 data finds 101001 as the sole extra missing word after excluding 11 and 00000. That extraction had no new predictions and is not the basis of the proof. No scan extension or novelty claim; all statements concern an externally clamped 0101 wall.

**Predictions before fixed controls.** Visible 101 should require initial sites a,b,q,r,z with a=1,b=q=0,r OR z=1. The five-site cylinders 00010 and 11100 should have canalized two-step transitions independent of farther bits. Counterfactual free concatenation of all gap lengths 1 through 4 must fail at adjacent lengths 1,2. Unexpected: one branch forces an eight-symbol visible prefix using only five initial bits. Check the two claimed cylinder transitions and the 101 characterization, not a longer output-language census.

**Characterization of 101.** Since an initial visible 1 forces the next visible 0, the only additional obligation is a visible 1 at the third sample. It requires the even row after two ticks to have sites 1,2,3 equal to 0,0,0, by GC503's R=1 case. Initially let a=1. Odd sites 2,3,4 are respectively

    B=1 XOR (b OR q),
    Q=b XOR (q OR r),
    R=q XOR (r OR z).

The next even sites 2,3 are 1 XOR (B OR Q) and B XOR (Q OR R). For both to vanish, B OR Q=1 and B=Q OR R. If B=0, the second equation forces Q=R=0, contradicting the first. Thus B=1, so b=q=0, and the second equation becomes r OR z=1. Conversely those conditions make both sites zero. This proves the characterization for arbitrary farther sites.

**Two branches after 101.** If initial r=1, the row at time 2 has first sites 0,0,0,0,Z, with Z arbitrary. Two more ticks give first sites 1,0,Z. In any row beginning (1,0,Q), site 2 after two ticks is 0: its odd site 2 is 1-Q and its odd site 3 is Q OR its right neighbour, whose OR is 1. Hence the row at time 6 begins (0,0,Q'), since the preceding visible 1 forces the next visible 0. GC503 then gives zero-run length 1 or 3, according to Q'. It cannot be 2.

If initial r=0, the characterization forces z=1. The row at time 2 begins 00010: site 4 is 1, while site 5 is 0 because its two odd inputs include a forced 1. Direct local substitution gives the farther-tail-independent transitions

    first five sites 00010 -> after two ticks 11100,
    first five sites 11100 -> after two ticks first four sites 0111.

For the first transition, odd sites 3,4 are 1,1; odd sites 5,6 are 1-F and F OR G, so the next site 5 is 1 XOR ((1-F) OR (F OR G))=0. For the second transition, odd sites 2,3,4 are 0,0,1, which force the next sites 2,3,4 to be 1,1,1. The next site 1 follows the imposed wall in each case. Thus at time 6 the zero-latch trigger has a=0,b=q=r=1, and GC503 gives length exactly 4. It cannot be 2. This branch forces visible prefix 10100001 from initial right sites 10001, whatever the farther initial row; no eight-symbol enumeration was used.

**Gap obstruction and controls.** After any visible 101, the following zero run has length 1,3 or 4. Therefore 101001 is impossible at every visible start time. Coding the trace by zero gaps between successive ones, the lengths lie in {1,2,3,4}, but the adjacent pair (1,2) is forbidden. This is a concrete failure of the free-gap sufficiency assumption. Further forbidden gap words may exist; the new necessary condition is not claimed sufficient or an entropy lower bound.

Probe `rule30_gpt_gap_pair.py` checks the 101 characterization on all 32 initial five-bit patches in both earlier independent implementations. It checks both canalized transitions for all four choices of initial sites 6,7 with packed updates and literal decimal-set updates: 8 transitions, all PASS. These are fixed local controls; quantified independence is supplied by the displayed substitutions. No horizon growth or asymptotic claim is made.

**Outcome and next.** Independent gap choices already fail at a length-six visible word, before an entropy estimate. Keep GC501's conditioned-background warning: a renewal model needs an actual invariant law or justified regeneration, not just a list of allowed gap lengths. Stop this finite motif branch after the local obstruction; next derive a structural extension criterion or return to a distinct open reasoning lead rather than catalogue longer forbidden words.

## GC505 — The random damage front sees a biased background after one tick (2026-10-08)

**Bears on.** Owner's portfolio question 2, constellation row 3. Changed lane from the stopped short companion-gap motifs to an exact random-front calculation. Read RULE30-PRIZE section 8.66, its retained long-jump failure, and GC295's nonempty finite-damage scope correction. This derives an early selection effect behind that existing measured mechanism; no novelty claim, speed fit or long-run experiment. Hand reading pending.

**Predictions and controls.** Before fixed controls, predict first-front displacements -1,0,+1 with probabilities 1/2,1/4,1/4, and that the +1 branch forces a -1 displacement on the next tick. Counterfactual fresh-fair healing bits at the selected front on every tick must fail at the second update. Unexpected: the bias appears exactly after one tick, although the unconditioned background is the fair-row ensemble. Enumerate only the 512 initial patches on sites -4 through 4 and their single flips, through two ticks, in independent sitewise XOR/OR and literal decimal updates. No detached job or speed run is duplicated.

**Setup and exact first tick.** Let u be an infinite iid fair initial row and flip only site 0 in the second copy. Let L_t be the leftmost disagreement, so L_0=0. A finite nonempty perturbation stays finite and nonempty by the existing rightmost XOR argument. At the first update the only possible disagreement sites are -1,0,1, with indicators

    D_(-1)=1-u_(-1),
    D_0=1-u_1,
    D_1=1.

Thus L_1=-1 if u_(-1)=0; L_1=0 if u_(-1)=1,u_1=0; and L_1=1 if u_(-1)=u_1=1. Their probabilities are 1/2,1/4,1/4, and E[L_1]=-1/4. This is an exact first-step mean, not an asymptotic velocity or an explanation of the measured approximately -0.246 displacement per tick.

**Front conditioning at the second tick.** For any finite disagreement with leftmost site L, the next leftmost site is L-1 exactly when the common background at L-1 is white. The new difference there is the derivative of c OR r in its right input, namely 1-c. Farther-left sites still agree. If that common bit is black, the front cannot move left on that update; subsequent rightward jump sizes need not be bounded by one or two.

Condition on the three first-step branches. If L_1=-1, the common bit below the new front is u_(-3) XOR u_(-2), since u_(-1)=0. It is fair given that branch. If L_1=0, the bit below it is 1-u_(-2), since u_(-1)=1. This too is fair given the branch. If L_1=1, the common site-0 value after the first tick is

    u_(-1) XOR (u_0 OR u_1)=1 XOR 1=0.

It is deterministically white. The first rightward front move is therefore undone at the next tick: L_2=0. Combining these branches gives

    P(L_2=L_1-1)=(1/2)*(1/2)+(1/4)*(1/2)+(1/4)*1=5/8.

The second-update healing probability is 3/8, versus 1/2 on the first update. This is an exact finite-time conditional-law change. It neither proves convergence to the measured healing rate nor justifies independence across later encounters.

**Independent finite controls and scope.** Probe `rule30_gpt_front_selection.py` checks 512 nine-site patches in two independent update implementations through both ticks, all PASS. First displacement counts are 256,128,128. Conditional second left-advance counts are 128 of 256,64 of 128,128 of 128 in the three respective branches; total 320 of 512. The fresh-fair-front CF is REFUTED. Site values outside the patch cannot affect disagreement through two ticks: damage lies in [-2,2], whose backward cones lie in [-4,4]. This supplies exact iid probabilities, not a finite-background approximation to a long-run speed.

**Outcome and next.** Full-row fairness does not give a fresh fair bit at a random damage front. The invariant-law or regeneration obligation in portfolio question 2 is concrete: track the background as selected by surviving damage, and retain the distribution of entire jumps. The first-step value -1/4 happens to be close to the empirical velocity, but substituting it for the limit is unjustified. Next seek a justified front-environment state or prove a restricted renewal lemma; do not rerun a speed fit or import independent healing events.

## GC506 — Front position alone is not a Markov state (2026-10-08)

**Bears on.** GC505 and portfolio question 2, constellation row 3. Exact finite-cone closure audit followed by a hand obstruction, independent reading pending. This rejects a specific position-only model, not all finite augmented states or an invariant front-environment law. No speed run, novelty claim or horizon escalation.

**Preregistered block.** Test whether, at the fixed time 2, histories sharing L_2=0 have the same third-step law. Blind prediction: different first-step positions change that law. Compare all 8192 initial thirteen-site patches and their site-0 flips through exactly three ticks using independent XOR/OR and literal decimal updates. Counterfactual fresh-fair front encounters retains GC505's failure. Unexpected: compare full jump distributions even when their healing probabilities coincide.

**Two positive-probability histories.** Write the initial fair row bits as u_i. The GC505 first-step difference indicators are 1-u_(-1),1-u_1,1 at sites -1,0,1. Let A be the event L_1=-1,L_2=0, and B the event L_1=0,L_2=0. Direct derivative algebra gives

    A: u_(-1)=0, u_(-3) XOR u_(-2)=1,
       and [u_1=1 or (u_1=0,u_(-2)=1,u_2=1)];
    B: u_(-1)=1, u_1=0, u_(-2)=0, u_2=1.

Here the derivative is the exact local XOR difference under the stated neighbouring damage bits. For A, the XOR condition says that the common site -2 is black after the first tick, so the front cannot advance left on tick 2. If u_1=1, the next difference at -1 cancels and the difference at 0 is 1. If u_1=0, those two differences are respectively 1-u_(-2) and u_2, yielding the remaining conditions. For B, the common site -1 after tick 1 is 1-u_(-2); keeping the front at 0 requires u_(-2)=0, and its next difference at 0 is u_2. These prove the displayed events without conditioning on an unobserved right jump.

Under A, the common site -1 after tick 2 is white. Its value is

    1 XOR ((u_(-2) XOR u_0) OR (u_0 OR u_1)).

If u_1=1 the OR is 1; if u_1=0, A forces u_(-2)=1, so the OR is again 1. Thus P(L_3=-1 given A)=1. Under B, that common site's value is u_(-3): its left input after tick 1 is 1-u_(-3), and its centre input is 1. Bit u_(-3) is independent and fair conditional on B. Hence P(L_3=-1 given B)=1/2. The event probabilities are P(A)=5/32 and P(B)=1/16, both positive.

The current position and current time agree on A and B, while the next-position laws disagree. Consequently the process (L_t) under this iid single-flip experiment is not an order-one Markov process, even if its proposed transition kernel is allowed to depend on time. This is a finite-history obstruction, not just nonstationarity of a one-step marginal.

**Independent exact controls.** Probe `rule30_gpt_front_markov.py` passes all 8192 patch histories in both update implementations. The first-step and second left-advance controls reproduce GC505 exactly. Among histories with L_2=0, the counts for L_1=-1,0,1 are 1280,512,2048. Their third-step position laws are respectively

    L_1=-1: {-1:1};
    L_1=0:  {-1:1/2, 0:1/2};
    L_1=1:  {-1:1/2, 0:3/16, 1:7/32, 2:3/64, 3:3/64}.

The first two agree with the independent hand proof. Unexpected: the last two histories have equal healing probability 1/2 but different full jump laws. Healing probability alone therefore does not close the transport calculation. The last law is an exact exhaustive finite-cone computation, without a separate symbolic branch proof. Damage through tick 3 lies in [-3,3], and all its backward cones lie in [-6,6], so the uniform patch counts are exact iid-history probabilities. Blind prediction HELD; CF REFUTED. No asymptotic velocity or unbounded memory claim follows.

**Outcome and next.** Position-only front closure is closed. A useful state must retain information about the common background and the surviving damage near the front, or a justified regeneration boundary. Next formulate that augmented state and its exact transition; do not increase the short-history horizon to fit an unsupported low-order chain. A negative result for every finite-state description would require a separate argument, and is not claimed.

## GC507 — Exact augmented transition and an unbounded finite-perturbation jump (2026-10-08)

**Bears on.** GC506's front-state obligation, portfolio question 2 and constellation row 3. Hand derivation pending independent reading. Read GC295's retained one-step coalescence: truncating its infinite disagreement supplies the finite family below. This does not reopen its corrected scope or claim a new local derivative identity. No speed fit, longer history scan or universal finite-state lower bound.

**Predictions and unexpected check.** Predict that the full background-and-damage state has an exact recentered transition, but a fixed-radius window does not determine every finite-perturbation jump. A damage block 0 through N should move entirely to site N+1 in one update. Counterfactual radius-2 pair-window closure must fail already for N=3,4. Unexpected: these arbitrarily large jumps reset the entire damage to one site. Check all 64 local derivative identities and N=1 through 12 in independent rules; universal-N coverage comes from the hand argument.

**Full augmented state.** Recenter at a leftmost disagreement L. Let u_i be the first background row relative to L, and d_i its XOR difference from the second row. Then d has finite support, d_i=0 for i<0 and d_0=1. Write M=max{i:d_i=1}. One ordinary Rule 30 step gives

    u'_i=u_(i-1) XOR (u_i OR u_(i+1)),
    d'_i=d_(i-1) XOR ((1-u_i)*d_(i+1))
          XOR ((1-u_(i+1))*d_i) XOR (d_i*d_(i+1)).

Expanding OR as a XOR b XOR ab proves the second identity. Let r=min{i:d'_i=1}. No damage occurs below -1. At M+1, the left input damage is 1 and the other two damage bits are 0, so d'_(M+1)=1. Thus r exists and -1<=r<=M+1. The exact next recentered state is

    new_u_i=u'_(i+r), new_d_i=d'_(i+r), new_L=L+r.

This is a deterministic transition on the full infinite background and finite damage word. Randomness enters through the initial law and its conditioning, not freshly independent bits at each update. It supplies a sound state description, but neither a finite state space nor an invariant law or integrability bound for its jumps. The common background to the left cannot simply be discarded, because its updates feed future near-front values.

**Finite family with a maximal jump.** For N>=1 take first row x black exactly at {-1,0}, and second row y black at {-1} together with all sites 1 through N. They are genuine finite rows, with initial damage exactly {0,...,N} and front 0. Near the left end, their differing inputs at sites -1,0,1 give equal output bits: at -1 both have centre black, at 0 both have black left input and black centre-or-right, and at 1 the first copy uses 100 while the second uses 010 or 011, all giving output 1. For sites 2 through N the second copy's triples are 111 or terminal 110, whose Rule 30 outputs are zero; the first copy has only zeros there. At N+1, only the second copy has input 100, giving output 1. Everywhere else the inputs agree or are all zero. Therefore

    F(x) XOR F(y)={N+1}.

For N=1 the site-1 terminal triple is 010 and the same conclusion holds. The front displacement N+1 is the maximum allowed by the rightmost-damage bound, and the new damage is a singleton.

**No universal fixed-window jump function.** For any fixed radius R, choose N>R and compare the above pairs for N and N+1. Their front positions, first rows and both-copy windows on [-R,R] agree, but their next front displacements are N+1 and N+2. Hence no function of a fixed-radius background-and-damage window alone determines the exact jump on the whole domain of finite perturbations. This is stronger than a numerical long-jump example and distinct from GC506's position-only probabilistic obstruction. It does not exclude a state that also records the entire damage word, its length or other nonlocal information.

**Controls and reachability guard.** Probe `rule30_gpt_front_window.py` passes all 64 baseline/damage triple identities. It checks N=1,...,12 against both sitewise XOR/OR and literal decimal updates, all yielding exactly {N+1}. Radius-2 CF is REFUTED by N=3,4. These controls support the quantified local proof. The constructed pairs are arbitrary finite perturbations; they are not proved reachable from a single flipped bit on an iid initial background. A fixed-window closure restricted to that reachable ensemble would need its own obstruction. No inference about arbitrarily large jumps in that ensemble is made here.

**Outcome and next.** The exact full-state update is now explicit, and ambient finite-window jump closure is closed. A rigorous speed argument must either retain a possibly unbounded damage word, justify a restricted reachable-state closure, or establish regeneration and control jump tails. Next audit a candidate regeneration condition within this state, rather than fit more front histories. Both the iid limiting speed and its existence remain open.

## GC508 — A singleton damage reset need not be regeneration (2026-10-08)

**Bears on.** GC507's augmented state and portfolio question 2, constellation row 3. Ambient finite-perturbation hand argument, independent reading pending. Reuses that exact family rather than fitting a longer iid front history. No novelty claim, iid reachability assertion or limiting-speed result.

**Predictions and unexpected check.** After GC507's right jump of N+1, predict at least floor(N/2) consecutive left moves, with the next move healing when N is odd. Counterfactual: resetting the damage to a singleton restarts the iid single-flip front law. Unexpected: the large jump itself creates a long deterministic compensating bout, because the reset occurs far ahead of the background. Check N=2,...,13 in two independent updates; the causal argument covers every N>=2.

**Reset state and causal separation.** GC507's finite rows x={-1,0} and y={-1} union {1,...,N} update to a first row U_0={-2,-1,1} and a second row differing from it only at N+1. Set time s=0 at this reset, so the front is L_0=N+1. The first row's rightmost black site after s further ticks is exactly 1+s: a rightmost black cell creates a black cell one site to the right by the 100 neighbourhood, and no farther cell can turn black. In particular all sites greater than 1+s are white.

Suppose inductively that L_s=N+1-s. The common bit immediately below the front is at N-s. It is white whenever

    N-s>1+s, equivalently 2s<N-1.

By GC505's exact front derivative, that white bit forces L_(s+1)=L_s-1. For s=0,...,floor(N/2)-1 the inequality holds, so

    L_s=N+1-s for 0<=s<=floor(N/2).

Thus an arbitrarily large jump to a singleton is followed by an arbitrarily long guaranteed run of unit left advances. This conclusion needs no assumption about the interior damage pattern after the reset; only the current leftmost difference and the first row's right edge enter.

**Odd-N endpoint.** If N=2m+1, after m such moves the front is m+2, and its common neighbour at m+1 is exactly the first row's rightmost black cell 1+m. Therefore the next update has no disagreement at the site one left of the current front; L_(m+1)>=L_m. In diagonal coordinates this is healing, possibly with a further rightward jump. The guaranteed left-advance bout is exactly m for odd N. For even N this argument gives the stated lower duration bound only; no sharp endpoint is claimed.

**Regeneration failure and controls.** All reset states here have one damaged site. Nevertheless their first future left advance has probability 1, whereas a newly independent single flip on a fair initial row has probability 1/2 by GC505. The ambient resets also contain a deterministic bout whose duration grows with N. A stopping condition based solely on singleton damage cannot therefore restart the iid law on the whole finite-perturbation domain. It must include a condition on the surrounding background and its conditional distribution. As in GC507, these reset states are not proved reachable from the iid single-flip experiment; no uniform mixing-time or rare-event conclusion for that ensemble follows.

Probe `rule30_gpt_front_reset.py` verifies the exact reset row, all guaranteed left moves, and the odd-N endpoint for N=2,...,13 using independent XOR/OR and literal decimal updates. All 12 pairs PASS in both implementations; the singleton-regeneration CF is REFUTED. This is a fixed control family for a proved causal inequality, not a horizon extension to estimate a velocity.

**Outcome and next.** Damage simplification alone is not a regeneration boundary, and large jumps cannot be treated as independent rewards without their conditioned aftermath. The next useful condition must identify genuine fresh background information, or retain enough environment to control those correlations and jump tails. Stop enlarging this finite family; seek such a condition on the actual iid reachable states or change to another open reasoning lead. Existence and value of the iid transport speed remain open.

## GC509 — A sufficient fresh-pivot condition at the adaptive iid damage front (2026-10-08)

**Bears on.** Portfolio question 2 and constellation row 3. Actual synchronous iid fair initial background, with only site 0 flipped in the second copy. Hand proof candidate, independent reading pending. Uses G97's left-permutative cone and GC507's exact derivative; the new application explicitly retains the adaptive exposure history. No novelty claim for deferred decisions, regeneration theorem or transport speed.

**Prediction and scope counterfactual.** A strict new record of the initial cone endpoint J_t=L_t-1-t supplies a fresh fair bit and conditional left-advance probability 1/2. The counterfactual that every encountered front bit is fresh remains false by GC505. Unexpected control: GC506's same-position histories can be separated by whether this very pivot was previously exposed. This block uses the existing exact first-three-tick laws and independent hand index checks, with no new experiment or horizon enlargement.

**An exposure filtration that does not look ahead.** Write X_i for the iid fair initial bits of the first copy, D(t) for the finite XOR damage, and L_t=min D(t). Its rightmost site is t by left permutativity. Initially expose the entire nonnegative initial half-row; set B_0=0. Before update t, all bits with indices at least B_t have been exposed, and the full damage history through t is known. In particular L_t and J_t are known before revealing any further initial bits.

To update damage, the derivative at sites i=L_t-1,...,t+1 only needs background values u_i(t) and u_(i+1)(t). At the leftmost candidate site it reduces to D_(L_t-1)(t+1)=1-u_(L_t-1)(t), so it needs no background bit farther left. The site t+1 is forced damaged, independently of the background. All other required background cones have left endpoints at least J_t. Their right endpoints are finite and already lie in the exposed nonnegative half-row. Thus revealing initial bits down to min(B_t,J_t) suffices to compute the whole next damage word and its front. Set

    B_(t+1)=min(B_t,J_t), so B_t=min(0,J_0,...,J_(t-1)).

This constructs the exposure process inductively. It can reveal more bits than strictly needed, which makes the criterion sufficient rather than necessary.

**Fresh-record conditional law.** On the event J_t<B_t, first expose the intervening bits at J_t+1,...,B_t-1. The target index was chosen using already exposed information. Revealing those intervening bits does not inspect X_(J_t), so that bit remains independent fair by the product law and deferred decisions. More explicitly, each finite sequence of negative-bit reveals chooses its next lower endpoint from previously revealed values; membership in that reveal history imposes no condition on any still-unrevealed lower bit. Conditioning also on the initially exposed right half preserves this property.

The leftmost cone identity is

    u_(L_t-1)(t)=X_(J_t) XOR g_t(X_(J_t+1),...,X_(L_t-1+t)).

It follows by induction because only the left child carries the cone's leftmost initial bit, with XOR coefficient one. All arguments of g_t are exposed before X_(J_t). Therefore this common below-front bit is conditionally fair, and the exact derivative gives

    P(L_(t+1)=L_t-1 | exposure history before the new reveals)=1/2

on J_t<B_t. The same equality holds after revealing the intervening bits but before revealing the pivot. This is an adaptive conditional statement, not an inference from the unconditional fair spatial law. If J_t>=B_t, the chosen pivot has already been exposed; the argument supplies no fair-bit law.

**Propagation and hand controls.** Write Delta_t=L_(t+1)-L_t. Then J_(t+1)=J_t+Delta_t-1. From a fresh record, any Delta_t<=0 creates another fresh record; a left move lowers the endpoint by 2, a stationary move by 1. A +1 jump reuses it, and larger jumps can place it inside an already exposed region. This index calculation independently checks why rightward jumps are the obstruction, without assuming their probabilities.

At t=0, J_0=-1<B_0. The first possible front locations -1,0,+1 give J_1=-3,-2,-1 respectively, while B_1=-1. Thus exactly the first two branches have a fresh pivot at the second update; GC505 gives probability 1/2 on each. The +1 branch reuses the pivot and has a forced white below-front bit, giving probability 1. These reproduce the known second left-advance probability 5/8.

For the unexpected same-position check, GC506's history A=(L_1=-1,L_2=0) has B_2=-3 and J_2=-3: no freshness certificate, and its known next left-move probability is 1. History B=(L_1=0,L_2=0) has B_2=-2 and J_2=-3: a fresh pivot, with next probability 1/2. Both hand index controls agree with the previously independent exact three-tick computations. A reused pivot need not always be biased; the criterion deliberately makes no converse assertion.

**Outcome and remaining obligation.** This supplies a genuine sufficient fresh-background condition on the actual iid reachable experiment, addressing GC508's missing conditional-law premise. It does not restart the entire background-and-damage state: damage shape, revealed environment and jump correlations persist. No frequency of fresh records, bound on excursions through reused information, integrability of jumps or limiting speed has been proved. The next useful analytic step is to control the exposure deficit J_t-B_t and its recovery, or show why that scalar also needs the full damage word. Do not enlarge a finite history census to infer either result.

## GC510 — Exposure accounting bounds the iid front's leftward speed (2026-10-08)

**Bears on.** Portfolio question 2 and constellation row 3, using GC509's adaptive fresh-pivot proof candidate. Hand derivation pending independent reading. This supplies a one-sided rigorous bound conditional on that audited proof, not existence of transport speed or a derivation of the measured value. No new experiment or long run.

**Prediction and counterfactual.** Retain the signed exposure deficit Z_t=J_t-B_t and predict an exact accounting identity implying L_N>=-A_N, where A_N counts left advances at fresh records. Unexpected: fresh-bit fairness then gives a half-speed ceiling without an excursion or jump-tail estimate. Counterfactual: knowing this scalar recursion restarts the full front law. Nothing below establishes that closure; GC506-GC508's environment guards remain.

**Pathwise accounting.** Set Delta_t=L_(t+1)-L_t, which is at least -1, and use B_(t+1)=min(B_t,J_t). Then

    Z_0=-1, Z_(t+1)=max(Z_t,0)+Delta_t-1.

Consequently Z_t>=-2. A fresh-record tick is exactly Z_t<0, hence Z_t=-1 or -2. Let F_N count these ticks for 0<=t<N; let A_N count their left advances Delta_t=-1; let T_N count left advances at ties Z_t=0. These definitions are pathwise, without probabilities.

The number of newly exposed negative initial sites through N updates is E_N=-B_N. Each fresh tick exposes -Z_t sites, so E_N equals F_N plus the number of ticks in that range with Z_t=-2. The recursion says Z_(t+1)=-2 exactly when Z_t<=0 and Delta_t=-1. Since Z_0=-1,

    E_N=F_N+A_N+T_N-1{Z_N=-2}.

Also J_N=L_N-1-N=B_N+Z_N, so

    L_N=N+1-F_N-A_N-T_N+Z_N+1{Z_N=-2}.

For every allowed Z_N, the final two terms are at least -1. T_N<=N-F_N because ties are not fresh. Thus the promised pointwise bound is

    L_N>=N-F_N-A_N-T_N>=-A_N.

Large jumps can be followed by many left moves through reused information; the accounting includes those moves via the deficit and tie terms. It never assumes they are independently fair.

**Finite-time expectation.** GC509 gives conditional probability 1/2 for a left move on each fresh tick, relative to its pre-reveal exposure history. The fresh indicator is known at that time. Therefore E[A_N]=E[F_N]/2<=N/2 and

    E[L_N]>=-N/2 for every N.

This is an expectation under the iid initial-background experiment only. It is not a claim for every deterministic initial row or every ambient finite perturbation.

**A concentration proof and almost-sure bound.** Put M_N=A_N-F_N/2. At a fresh tick its increment is a conditionally fair choice of -1/2 and +1/2; at any other tick it is zero. Thus, for every real lambda, its conditional exponential moment is at most cosh(lambda/2)<=exp(lambda squared/8). Iterating conditional expectations gives E[exp(lambda M_N)]<=exp(N lambda squared/8). The elementary bound on cosh follows by integrating tanh(x)<=x for x>=0, with symmetry for negative x.

For epsilon>0, exponential Markov inequality with lambda=4 epsilon yields

    P(M_N>epsilon N)<=exp(-2 epsilon squared N).

Since L_N>=-A_N=-F_N/2-M_N>=-N/2-M_N,

    P(L_N<-(1/2+epsilon)N)<=exp(-2 epsilon squared N).

The right side is summable in N. For each positive rational epsilon the probability of infinitely many such violations is zero: the probability of any violation after n is bounded by the tail of that convergent sum, tending to zero. Intersecting these countably many probability-one events proves

    liminf as N tends to infinity of L_N/N >= -1/2 almost surely.

No assumption on the number of fresh ticks or on positive-deficit recovery enters this argument. If a limiting inward speed v=-lim L_N/N exists, it is at most 1/2. This does not prove v exists or is positive; the reported approximately 0.246 remains a measurement.

**Independent hand and scope controls.** An all-left displacement path has Z_0=-1, all later Z=-2, F_N=A_N=N, T_N=0, E_N=2N-1 and L_N=-N: accounting is exact and the pathwise bound is sharp. An all-stationary path keeps Z=-1, F_N=N, A_N=T_N=0, E_N=N and L_N=0. The actual GC505 +1 then -1 path has Z=(-1,0,-2), F_2=1, A_2=0, T_2=1 and L_2=0, showing that a certain reused-pivot left move is not counted as a fresh fair trial. These checks derive independently from displacements and reproduce the endpoint correction in the identity.

For an unexpected limit of the method, an abstract displacement process taking only -1 and 0 with equal independent probabilities stays fresh at every tick and has limiting position slope -1/2. It satisfies all accounting and fairness premises. This abstract process is not asserted to be realizable by Rule 30; it shows that those premises alone cannot improve the half-speed ceiling. Deterministic all-left rows are also outside the iid fairness premise, so their sharp pathwise equality does not contradict the probabilistic bound.

**Outcome and next.** The exposure criterion has a concrete transport consequence: all finite-time expected positions and an almost-sure lower asymptotic position bound, without a speed existence claim. Request a joint second reading of GC509's filtration and this accounting before filing a verified proposition. Next seek an actual dynamical constraint beyond fresh-bit bookkeeping that controls record frequency, positive deficit, or stationarity of the augmented state. No finite-history enlargement or fitting of the measured speed.

## GC511 — Fixed-horizon independent controls for the exposure proof (2026-10-08)

**Preregistered, not yet run.** Reuse GC506's complete 8192 initial patches on sites -6 through 6 and its three-update horizon. No extra horizon or random sample. EX0: literal decimal Rule 30 and XOR/OR updates agree on both copies. EX1: group each fresh encounter by its front history and all already exposed initial bits; every group has equal next-left and non-left counts. Independently repeat after exposing the intervening bits down to J_t+1, stopping before the pivot. EX2: actual revealed-index sets agree with the exact GC510 exposure identity, its deficit recursion and L_N>=-A_N at each prefix; E[A_N]=E[F_N]/2 and E[L_N]>=-N/2. CF: all reused groups are also fair must fail. Unexpected check: the GC506 histories (-1,0) and (0,0) at time 2 are entirely reused and entirely fresh respectively, with next-left probabilities 1 and 1/2. Any failed equality invalidates this finite control and must be retained. The general proofs remain GC509-GC510's written arguments; a finite pass does not establish asymptotic speed.

**Outcome (2026-10-08, GPT).** Probe `rule30_gpt_front_exposure.py` PASS on the stated 8192 patches and 24576 prefixes in independent updates. All 800 pre-gap exposure groups and all 1312 post-gap/pre-pivot groups balance exactly. Revealed-index sets independently agree with the signed-deficit recursion, endpoint correction and pathwise bound. Exact mean front positions at N=1,2,3 are -1/4,-35/64,-105/128, and mean fresh-tick counts are 1,7/4,5/2. Fresh-left expectation equals half the fresh-tick expectation at each prefix. Reused-group fairness CF is REFUTED. The two unexpected GC506 histories have exactly the predicted exposure status and probabilities.

**Cone and interpretation audit.** Through three updates, every background value affecting the single-flip damage has its initial cone within sites -5 through 5; the extra sites -6 and 6 are exterior controls. Initial bits beyond the finite patch cannot influence these damage events and remain independent under the product law. Grouping the exposed bits only through site 6 is therefore sufficient for this finite control; GC509's general filtration still exposes the entire initial right half. These exact controls check the adaptive grouping and accounting that were absent from a position-only model. They support the proof candidate without replacing an independent hand second reading or implying a limiting speed. Stop at the registered horizon; request joint reading, then return to actual structural constraints.

## GC512 — Fresh-bit fairness does not prove record recurrence (2026-10-08)

**Bears on.** GC509-GC511 and portfolio question 2, constellation row 3. Bounded hand scope audit, pending independent reading; no experiment. Predict that finitely many fresh-record ticks force outward slope +1, but that their conditional fairness alone does not exclude this outcome. Unexpected: any positive limiting inward speed demands a quantitative lower frequency of fresh records.

**Actual finite-record implication.** In the iid single-flip experiment, suppose only finitely many ticks have J_t<B_t. After their last occurrence B_t is a constant finite integer B. Every later J_t is at least B, otherwise another record would occur. Since J_t=L_t-1-t and the rightmost damage remains at t,

    t+1+B<=L_t<=t eventually, hence L_t/t tends to +1.

This is a pathwise conditional implication, not a statement that the finite-record event has positive or zero probability. Its converse is not proved: outward slope +1 need not make the total exposure finite.

**Counterfactual refuted by an abstract process.** Start L_0=0, B_0=0, J_0=-1 and use exactly GC510's deficit recursion. At each fresh tick independently choose displacement -1 or +1 with equal probabilities. At every reused tick choose +1 deterministically. A fresh left move keeps the next tick fresh, with deficit -2; the first fresh +1 move sets the next deficit to 0. Subsequent +1 moves keep it 0 forever. This process satisfies the stipulated fair left-advance law at every fresh tick and all pathwise exposure accounting, including L_N>=-A_N.

Let K count the initial fresh left moves before that first +1. Then P(K=k)=2^(-(k+1)), so K is finite almost surely. For t>=K+1,

    B_t=-2K-1, Z_t=0, L_t=t-2K.

Thus it has finitely many fresh records and outward limiting slope +1 almost surely. Independent hand endpoint checks: K=0 gives B=-1 and L_t=t; K=1 gives the actual initial displacement pair -1,+1, then L_t=t-2. The actual first +1 branch in GC505 instead forces a following left move, whereas this abstract model moves right again. That is the explicit extra dynamical constraint missing from the freshness-only model. It is not asserted to be a Rule 30 damage history or to have a realizable background.

Consequently conditional fresh-bit fairness and exposure bookkeeping alone cannot establish recurrent records, positive inward speed, or full regeneration. The example refutes an inference between those premises; it does not refute recurrence for actual Rule 30.

**A necessary frequency condition.** GC510 gives L_N>=-F_N/2-M_N, where its exponential moment bound implies limsup M_N/N<=0 almost surely. If an inward speed v=-lim L_N/N exists and v>0, then

    liminf F_N/N>=2v almost surely.

This follows by rearranging the inequality and taking the lower limit. It neither supplies v nor a positive record-frequency bound. In particular infinitely many fresh ticks alone allow zero limiting frequency, so proving recurrence would still fall short of this quantitative requirement. Even a record-frequency lower bound would not by itself prove positive inward speed: outward jumps and accumulated exposure deficit also enter the exact identity.

**Outcome and next.** Fresh records are a useful source of unbiased bits, not yet a renewal structure. The missing dynamical targets are now explicit: exclude the finite-record escape, then control record frequency and the full state between records. GC505's forced reversal after an initial +1 is an actual constraint distinguishing Rule 30 from the countermodel, but no analogous all-time reversal bound has been established. Stop abstract-model proliferation; seek a justified return constraint on reachable background-and-damage states or change to another open reasoning lane. The GC509-GC510 proof candidates still await joint second reading.

## GC513 — A resonant white run ends at a left checkerboard mismatch (2026-10-08)

**Bears on.** GC494's within-pair duration obligation and GC495-GC496. Hand corollary of the known white-wall right latch (G15, Condrey discussion) and G18/GC495's exact black-run certificate; no novelty claim, independent reading pending. Lane change from the incomplete fresh-front recurrence route. No experiment.

**Prediction and unexpected check.** For equal finite nearest-black distances m on the two sides of a white centre, predict remaining white duration m+d, where d is a left-neighbor checkerboard mismatch depth at time m-1. Counterfactual: farther right initial bits can alter the later resonant endpoint. The latch should refute that dependence. Independent hand controls use {-1,1}, {-2,-1,1} and {-2,2}; no patch census.

**Arrival and latch.** Start time 0 from any row with centre 0 and nearest black cells exactly at -m and +m, m>=1. GC496 gives a white centre through time m, with its first possible endpoint cancelled. At s=m-1, both adjacent cells are black: each has a zero cone with its unique nearest black endpoint, so the one-sided arrival identity applies. The centre is still white.

As long as the centre remains white, its right neighbor evolves as u_1(t+1)=u_1(t) OR u_2(t). Once black at time s, it cannot become white before the centre's first black time. Meanwhile a white centre updates to u_-1(t) XOR u_1(t). Therefore, from time s onward, it stays white exactly while the left neighbor remains black, and turns black one tick after that neighbor's first white time. This reasoning includes the failure endpoint: if the left neighbor first becomes white at time s+d, the centre is still white there and the right neighbor still black, so the centre turns black at s+d+1.

**Exact certificate.** At time s, read the row leftward from site -1. Let d be its first mismatch against black at even depths and white at odd depths, with d=infinity if no mismatch exists. GC495, translated to site -1, says the remaining black run of that cell lasts exactly d updates. Its current black value makes d>=1. Consequently the remaining white run of the original centre is exactly

    R=m+d,

with the usual infinite value if d=infinity. This completes GC496's resonant branch; when nearest distances differ its earlier formula R=min(p,q) remains unchanged. No bound on how often resonance occurs is supplied.

**Right-tail independence.** Fix the entire initial left half and the finite right prefix consisting of m-1 zeros followed by one black cell. Arbitrary initial bits to the right of +m cannot change R. Up to time s the centre is white by the first-arrival cone, so the left half evolves with a fixed white boundary and does not depend on those right exterior bits. Hence its time-s checkerboard mismatch d is fixed. After time s the right neighbor's latch keeps it black until the centre fails, regardless of its farther right inputs. This proof eliminates the exterior dependence for the whole run, not merely its first m samples. It does not eliminate the left-half dependence: d can be arbitrarily large on unrestricted rows.

**Hand controls and limits.** For {-1,1}, m=1 and the initial row read from -1 has black, white, white, so d=2 and R=3; direct centre trace 0001 agrees with GC496. Adding a black cell at -2 gives {-2,-1,1}, d=1 and R=2: its next row is {-3,-2,1,2}, then the centre turns black. For {-2,2}, m=2 and at time s=1 the row is {-3,-2,-1,1,2,3}; from -1 the depth-1 cell is black, giving d=1 and R=3. These translated checks independently verify the extra endpoint tick. For an initially left-bounded row, the left half at time s is still eventually zero, so d is finite; this recovers the known constant-white exclusion and is not a new period-1 theorem.

**Outcome and next.** White-run duration in the resonant case has an exact left checkerboard certificate after a finite arrival delay, complementing the black certificate at the run start. This gives no sublinear bound along the selected singleton orbit and no signed run-length cancellation. GC494 still requires both. Next seek an actual bound on these selected-time checkerboard matches or a coupling between consecutive certificates; do not infer a balance theorem from right-tail independence or finite-left termination alone.

## GC514 — Independent fixed-cone controls for the resonant white certificate (2026-10-08)

**Registered before execution.** Claims and predictions in CLOUD-LOCAL specify all 341 centre-white patches on sites -5 through 5 with equal finite nearest-black distances m, through five updates only. Predict capped first-black time min(m+d,6) from GC513's time-(m-1) left-neighbor checkerboard. Decimal Rule 30 and XOR/OR updates must agree. Counterfactual farther-right dependence must fail when the initial left half and first-right-black prefix are fixed. Unexpected: m=5 forces the centre white through all five updates. No selected-orbit fit or longer horizon.

**Outcome.** Probe `rule30_gpt_white_certificate.py` PASS on every registered patch: counts by m=1,...,5 are 256,64,16,4,1. Both implementations agree on all five updates. All predicted endpoints match. Every one of the 31 fixed-left/nearest-right groups has one capped endpoint despite varying its remaining right bits; the dependence CF is REFUTED. The m=5 survival check passes. These are finite-cone checks: initial cells outside -5 through 5 cannot affect centre outputs through time 5, or the checked mismatch depths at time m-1. A returned cap of 6 means survival through time 5, not a claim that the first black time equals 6.

**Scope and next.** The controls support GC513's latch argument and endpoint indexing, without replacing independent hand reading. They do not estimate long run durations, checkerboard match frequencies or balance of the singleton orbit. Stop this fixed control family. The useful open obligation remains an actual selected-time match bound or a coupling between adjacent run certificates.

## GC515 — The resonant delay is geometric only with an unexposed fair left tail (2026-10-08)

**Bears on.** GC513's white-duration certificate and the distinction between ensemble balance and the selected singleton orbit. Hand corollary of G97's triangular pivots, not a new iid temporal theorem; independent reading pending. No experiment. Predict conditional resonant depth d has mean 2, and total mean white duration splits into arrival 4/3 and extra resonant delay 2/3. Unexpected check: nearest-distance ties have probability exactly 1/3. Counterfactual transferring these laws to selected singleton run starts lacks their independent-left-tail premise.

**Conditional geometric delay.** Start from an iid fair bi-infinite row conditioned on centre 0. Suppose nearest black distances satisfy p=q=m. Fix also the entire initial right half. This fixes the initial left prefix: zeros at -1 through -(m-1), black at -m. The remaining initial bits farther left are still independent fair.

At arrival time s=m-1, write b_k=u_(-1-k)(s). We know b_0=1. For k>=1 the leftmost initial cone index is -m-k, and left permutativity gives

    b_k=X_(-m-k) XOR g_k of initial bits strictly to its right.

The higher cone bits include only the fixed prefix and the already used left pivots when reading k in increasing order. Thus, for any finite desired word b_1,...,b_K and any fixed right half, its initial pivot word is uniquely determined, with probability 2^(-K). These arrival-row cells are iid fair under this conditioning. This is the same triangular mechanism as G97, now with the resonance prefix exposed explicitly.

The first mismatch d against the alternating left checkerboard therefore satisfies

    P(d=k | p=q=m, initial right half)=2^(-k), k>=1,
    P(d>=k | same conditioning)=2^(-(k-1)), E[d | same conditioning]=2.

There is no infinite mismatch-free tail with positive probability, since the probability of matching its first K cells is 2^(-K). GC513 then gives R=m+d in the resonant case. The conditional law does not depend on m or on the farther right tail, but it does require the random unexposed initial left tail.

**Independent aggregate check.** Without conditioning the right half, p and q are independent nearest-black distances with P(p=m)=P(q=m)=2^(-m). Let M=min(p,q). Then P(M>=m)=4^(-(m-1)), giving E[M]=4/3. Meanwhile

    P(p=q)=sum over m>=1 of 4^(-m)=1/3.

GC496 gives R=M off the tie, and GC513 gives R=M+d on the tie. Consequently

    E[R]=E[M]+sum over m>=1 P(p=q=m) E[d | p=q=m]
        =4/3+2*(1/3)=2.

This independently agrees with G97's fair temporal trace: conditioned on its first centre sample being 0, the initial white-run length is geometric with mean 2. The black certificate gives the same mean by directly comparing iid initial left bits to a checkerboard. These are consistent ensemble checks, not a proof of selected-orbit black/white balance.

**Scope guard and outcome.** For m=1, a free initial bit at -2 ends the neighbor's black run immediately with probability 1/2; prescribing -2=0 and -3=0 instead forces d=2 and R=3, as in the deterministic {-1,1} control. A finite deterministic left tail is not an iid fair tail. At an adaptively chosen run start, the evolved left environment can also be conditioned by its observed past. No fresh-tail law has been proved there. Thus the exact conditional resonance calculation supplies a reference law and identifies its precise missing premise for the singleton problem; it cannot be used as its renewal distribution. Return to actual selected-time match constraints rather than fit this already determined ensemble law.

## GC516 — Centre-past stopping times preserve the fair-ensemble run law (2026-10-08)

**Bears on.** Scope clarification for GC515, reusing G97's iid fixed-centre trace rather than claiming a new stochastic theorem. Hand audit pending independent reading; no experiment. Predict that adaptive run starts based only on the centre's observed past preserve its fair future. Counterfactual: arbitrary spatial conditioning has the same property. Unexpected control: m=1 resonance forces the next sample white, so the conditioning class is essential.

**Clarification of GC515's warning.** Adaptivity by itself is not a reason to discard the iid law. In the iid initial-row ensemble, an adaptively chosen fixed-centre run start measurable from that centre's past is a legitimate stopping time, and the future is still iid fair. GC515's missing-premise warning concerns the selected deterministic singleton orbit and additional spatial/environment conditioning; it must not be read as denying the following fair-ensemble fact. Likewise GC505-GC509's adaptively moving damage front is a different observation process.

**Direct proof without a stopping-time theorem citation.** Write C_t for the fixed-centre trace. G97 proves its finite words are uniformly distributed. Let tau be an almost-surely finite stopping time for the filtration generated by C_0,...,C_t. For any event H measurable at tau and any k-bit word w, the disjoint events H intersect {tau=n} are measurable from the samples through n. The next k samples at each fixed n are independent fair. Hence

    P(H and (C_(tau+1),...,C_(tau+k))=w)
      =sum over n>=0 of 2^(-k) P(H and tau=n)
      =2^(-k) P(H).

This proves the asserted independent fair future at tau. The current value C_tau belongs to the stopped past and need not itself be fair under H. If R counts the current run including its start sample, then

    P(R>=r | stopped past)=2^(-(r-1)), r>=1,
    P(R=r | stopped past)=2^(-r), E[R | stopped past]=2.

At a run start the current colour is known. Each subsequent same-colour sample supplies one fair trial until the first opposite sample. Iterating at successive centre-past run starts gives independent geometric lengths in this ensemble. This remains a statement about random initial rows; it does not import a fair spatial environment into the singleton orbit.

**Spatial selection fails the premise.** Condition on C_0=0 and nearest initial black distances p=q=1. The initial triple is 101 and literal Rule 30 maps it to 0, so P(C_1=0 | that spatial event)=1. Conditioning only on C_0=0 instead gives 1/2 by G97. The event p=q=1 is not measurable from C_0: it exposes the first negative pivot and the right neighbor. This is the exact mechanism behind GC515's delayed geometric law and an independent one-tick check of the stopping-time restriction. Fixing the initial right half alone does not consume future negative pivots; exposing an additional negative bit can.

**Outcome and next.** Temporal stopping based only on a fixed iid centre trace is safe; spatial selection, adaptive position and the deterministic selected seed need separate arguments. No new renewal premise has been established for the singleton. Keep this clarification with GC515 so the relevant obstacle is stated precisely. The remaining research target is still a deterministic selected-time checkerboard estimate or consecutive-run certificate relation, not a simulation of the known geometric ensemble.

## GC517 — Three structural targets are exactly the duration half of the balance reduction (2026-10-08)

**Bears on.** GC494-GC496 and GC513, serving Problem 2. Conditional hand reduction using those proof candidates, pending independent reading. No experiment or new estimate. Predict that individual-run sublinearity is equivalent to three selected-time geometric quantities. Unexpected: normalization at the delayed arrival is equivalent to normalization at the run start only after controlling the empty-gap delay. Counterfactual local inspection of checkerboard matches at a white start alone bounds its duration.

**Selected singleton definitions.** Use the recorded constant-column exclusion for a nonzero finite seed, so the selected singleton has finite runs and unbounded run-start times. At a black-run start t, let b(t) be the centre's first left checkerboard mismatch depth. At a white-run start s, let p(s),q(s) be nearest black distances and m(s)=min(p,q). They are finite for s>=1 because the singleton row has black extreme cells at -s and +s, so m(s)<=s. On the resonant starts p=q=m, set a(s)=s+m(s)-1 and let d(s) be the checkerboard mismatch depth at site -1 in the actual row at time a(s). This is finite by the eventually-zero left tail. Off resonance set d(s)=0 for notation only.

The earlier exact certificates give black duration b(t), and white duration

    w(s)=m(s)+d(s).

Here d=0 on nonresonant starts reproduces GC496's first-arrival endpoint. On resonance it is GC513's delayed checkerboard endpoint. No distribution is assigned to these selected rows.

**Necessary and sufficient duration targets.** Along run starts tending to infinity, every individual duration is sublinear relative to its own start if and only if all three conditions hold:

    b(t)/t tends to 0 at black starts;
    m(s)/s tends to 0 at white starts;
    d(s)/a(s) tends to 0 at resonant white starts.

For necessity, black duration is exactly b. Since m and d are nonnegative and w=m+d, white sublinearity gives m/s->0 and d/s->0. On resonance a/s=1+(m-1)/s->1, so d/a->0. For sufficiency the second condition again gives a/s->1; the third implies d/s=(d/a)*(a/s)->0. Therefore w/s->0. An empty or finite resonant subsequence makes the third condition vacuous. Initial finitely many run starts are irrelevant.

GC494's paired-run duration requirement is equivalent to this individual-start version: the first run's sublinear length makes the second run's starting time asymptotic to the pair start, so its own-start normalization and the pair normalization agree. This contracts the duration obligation into actual spatial measurements and estimates at three specified families of times. It supplies none of their bounds. The other GC494 obligation, sublinear signed cumulative black-minus-white lengths, remains separate.

**Independent controls and failed shortcut.** An alternating trace with unit runs has all durations bounded and satisfies the normalized duration requirement; equal doubling pairs have zero signed pair-end discrepancy but fail the duration requirement, as GC494 already checks. These are sequence controls, not Rule 30 realizations. For an actual finite-row scope control, take black sites {-m,m+1}, m>=2, with a white centre. GC496 gives white duration exactly m despite the centre and site -1 both being white initially, with no black checkerboard starting at either inspected site. Thus no bound obtained solely by inspecting those checkerboard starts at the white-start instant controls the waiting time for first arrival. The family is not asserted to be reachable at singleton run starts or to refute a stronger all-time estimate.

**Outcome and next.** The selected-orbit duration half now has a precise three-part geometric formulation: black match, white empty-gap delay, and post-arrival match. The uniform edge strip and iid ensemble law prove none of these near-centre selected-time estimates. A useful next claim must bound at least one of these exact quantities on the actual singleton orbit or couple them to signed run-length cancellation. Stop further reformulations and fixed controls until such a dynamical input is found; otherwise change to another open main-line reasoning lead.

## GC518 — Root-visible spectral contraction is also necessary for finite-kernel balance (2026-10-08)

**Bears on.** GC488-GC489's conditional Problems 2/3 bridge. Bounded hand linear-algebra audit, independent reading pending; no actual Rule 30 representation, numerical spectral fit or experiment. Predict a necessary-and-sufficient balance criterion within the proved finite closed family. Unexpected check: GC489's dyadic-only countersequence itself has a four-state closed kernel. Counterfactual origin dyadic totals suffice remains false. These are standard finite-representation tools, with no novelty claim.

**Setting and claim.** Retain GC489's finite decimation family, child-sum matrix A, reachable output span W, selected-coordinate functional ell and invisible subspace U={w:ell(A^k w)=0 for all k>=0}. Let Abar act on V=W/U. Then

    selected signed prefix sum S_g(N)=o(N)
    if and only if spectral radius of Abar is strictly below 2.

The sufficient direction is GC489's all-prefix bound. The necessity below uses every fixed shifted dyadic block, not merely blocks starting at the origin. The representation must be genuinely closed at every index; merging finite signatures is not a hypothesis substitute.

**Shifted blocks from prefix balance.** Iterating A b(n)=b(2n)+b(2n+1) gives

    A^k b(n)=sum over 0<=r<2^k of b(2^k*n+r).

Therefore ell(A^k b(n))=S_g((n+1)2^k)-S_g(n2^k). If S_g(N)=o(N), division by 2^k tends to zero for every fixed n, including n=0. Every w in W is a finite linear combination of reachable b(n), so

    ell(A^k w)/2^k tends to zero for every w in W.

This conclusion extends to the complexification by splitting real and imaginary parts.

**Visible peripheral modes contradict that limit.** A has nonnegative entries and each row sums to 2, so its spectral radius is at most 2. Restriction to W and passage to its invariant quotient introduce no additional eigenvalues. If Abar had an eigenvalue lambda with absolute value 2, take a nonzero complex eigenvector v. Its root functional ellbar(v) cannot vanish: if it did, all ellbar(Abar^k v) would vanish, so any lift would belong to U and v would be zero. For a lift w,

    ell(A^k w)/2^k=(lambda/2)^k ellbar(v),

whose absolute value is a positive constant. This contradicts the shifted-block limit. Thus every eigenvalue of Abar has absolute value below 2. Conversely this spectral condition supplies a power bound with some 1<rho<2 in finite dimension, and GC489 proves all-prefix sublinear discrepancy. No Jordan or peripheral-mode estimate is assumed from data.

**Independent controls.** Thue-Morse and the alternating root have zero quotient operator as audited in GC488-GC489, and their sums are bounded. Constant spin has Abar=2 and discrepancy N. These check both sides and the removal of root-invisible biased modes.

For GC489's countersequence h, take h(0)=1,h(1)=-1; for n>=2 its sign is +1 when its first two binary digits are 10 and -1 when they are 11. Let H=h. Define G,J,K to agree with h at n>=2, with their output pairs at n=0,1 respectively (1,1),(-1,-1),(-1,1); H's pair is (1,-1). Direct leading-digit and exceptional-index checks give the closed transitions:

| State | Even child | Odd child | Output at 0 |
| --- | --- | --- | --- |
| H | G | J | 1 |
| G | G | H | 1 |
| J | K | J | -1 |
| K | K | H | -1 |

Every state equals +1 at index 2, so b(2) is the all-ones vector. It lies in W, has eigenvalue 2 under A, and is root-visible. Equivalently, the shifted block [2*2^k,3*2^k) consists entirely of +1 and has sum 2^k. Thus the criterion rejects balance even though the origin dyadic totals S_h(2^k)=0 for k>=1. The finite kernel still supplies a logarithmic digit indexer, showing again that cheap indexing alone need not give Problem 2. This is an explicit arithmetic sequence, not a Rule 30 trace.

**Outcome and next.** Within a proved finite closed representation, the balance test is now exact: remove invisible modes and check whether any modulus-2 mode remains. Origin dyadic totals alone miss reachable shifted blocks. For Rule 30 the representation itself remains unproved, so this does not resolve either prize. A next useful representation claim must establish infinite child identities or a justified nonfinite analogue; do not enlarge the finite signature census or fit its eigenvalues.

## GC519 — A balanced finite-kernel trace has uniformly bounded constant runs (2026-10-08)

**Bears on.** GC518's exact finite-representation criterion, Problems 2/3 and the run-duration lane. Hand corollary pending independent reading; no Rule 30 representation or experiment. Predict a uniform-in-start interval discrepancy bound, hence a fixed maximum constant-run length. Counterfactual prefix balance alone yields this consequence. Unexpected check: root-invisible biased kernel states do not need to satisfy the root interval bound.

**Aligned interval estimate.** Under GC518's proved finite closed family and root balance, GC489 supplies constants C>0 and 1<rho<2 with quotient power norm at most C*rho^k. Every reachable b(n) has quotient norm at most 1. Therefore every aligned dyadic interval, with arbitrary integer start multiplier n>=0, satisfies

    |sum over n*2^k<=j<(n+1)*2^k of g(j)|
      =|ell(A^k b(n))|<=C*rho^k.

The bound is uniform in n, not merely valid separately for each fixed shifted block. Finite representation and the norm bound supply that uniformity.

**All intervals.** Partition any integer interval [M,M+N), N>=1, into maximal aligned dyadic intervals it contains. There are at most two blocks of each length 2^k: a maximal block's parent must cross an endpoint of the original interval, and there are only two endpoints. All contained block lengths are at most N. With alpha=log_2(rho)<1,

    |sum over M<=j<M+N of g(j)|
      <=2C*sum over 0<=k<=floor(log_2 N) of rho^k
      <=D*N^alpha, where D=2C*rho/(rho-1).

This proof retains GC489's root quotient and the original reachable vectors; it does not assume the quotient supports individual digit transitions or that all kernel states are balanced.

**Run consequence.** A constant-sign run of length R has absolute interval sum R. Hence R<=D*R^alpha and

    R<=D^(1/(1-alpha)).

Thus a balanced binary trace with a proved finite kernel has a uniform finite bound on all its constant runs. This is stronger than GC494's sublinear duration obligation. If the actual singleton centre were proved both balanced and to have unbounded run lengths, those two results would exclude a finite binary kernel. Neither is established here; a growing finite observed maximum does not prove unboundedness. This exclusion would still not prove the linear-work claim of Problem 3.

**Independent and unexpected controls.** Alternating spin has root interval discrepancy at most 1, although its finite kernel includes constant states with arbitrarily large discrepancy. Those biased states are invisible to the aggregate root quotient, so they do not contradict the theorem. Thue-Morse has discrepancy at most 2 on arbitrary intervals by its bounded prefix sums, consistent with its bounded runs. Constant spin fails the balance hypothesis.

GC490's h(n)=(-1)^floor(sqrt(n)) gives the counterfactual failure: its origin prefix discrepancy is at most sqrt(N), yet its constant intervals [k squared,(k+1) squared) have length 2k+1 and interval discrepancy exactly that length. No uniform bound D*N^alpha with alpha<1 can hold as k grows. Thus prefix balance alone gives neither the uniform interval bound nor bounded runs. Its previously proved infinite kernel and cheap exact arithmetic indexer are consistent with this corollary and again separate finite-state exclusion from a time lower bound. These controls are analytic, not Rule 30 realizations.

**Outcome and next.** Any finite-representation balance proposal has a concrete additional observable consequence: bounded constant runs on the entire trace. A genuine unbounded-run theorem for the selected singleton, together with balance, would rule out that representation class; a bounded-run theorem could instead guide one. Current run certificates alone prove neither. Seek an actual infinite family of run witnesses or a closure identity, rather than another finite maximum-run or kernel-signature scan. The candidate remains conditional and awaits a second reader.

## GC520 — Known zero fibre simplifies the white-run certificate (2026-10-08)

**Scope.** Source audit and hand contraction of GC513/GC517, pending independent reading. Prediction: the delayed white-run certificate can be read at its starting row. Counterfactual: a sharp finite-support horizon supplies unbounded runs on the selected singleton. Unexpected check: a known fibre already removes the delayed-row obligation. No experiment or novelty claim.

**Credited input.** [Condrey, Theorem 2 and Lemma 1](https://arxiv.org/html/2609.09431v1), already read in G11, give the zero-trace fibre and triangular uniqueness. For centre 0 and first right black at depth q, the compatible left bits are 0 before q, 1 at q, and j mod 2 at depths j>q. Keep the whole right half fixed. If the actual left half first differs at depth R, locality and left permutativity give the first centre difference at time R. Therefore its remaining white-run length is exactly R. No mismatch means permanent white.

**Contraction.** If nearest left black p differs from q, that first mismatch is min(p,q), recovering GC496. If p=q=m, the first mismatch is strictly beyond m; comparing the two exact endpoint descriptions gives R=m+d from GC513. Thus GC517's delayed depth is R-m, and the start row itself certifies it. Farther-right bits beyond q cannot alter this certificate. The three recorded hand controls give R=3,2,3 for black-site sets {-1,1}, {-2,-1,1}, {-2,2}, respectively.

The actual white-start target can now be stated directly: this fibre's first mismatch depth, divided by the start time, tends to zero. The black-start target and signed cumulative run-length cancellation remain separate. This improves the location of a certificate, not the missing dynamical estimate.

**Known horizon and failed inference.** Condrey's sharp white-prefix bound is 2*ceil(w/2)+1 for support radius w. At singleton time s this gives only a linear bound, at most s+1 for even s and s+2 for odd s. Its extremizers are arbitrary supported rows; they are not certified singleton rows. It yields neither sublinear selected durations nor an infinite family of selected long runs.

**Search retained.** Bounded searches for Rule 30 arbitrarily long centre runs and constant-run proofs, including Wolfram and Complex Systems domains, supplied no unbounded selected-run theorem usable here. Inspected the primary [prize announcement](https://writings.stephenwolfram.com/2019/10/announcing-the-rule-30-prizes/) and Condrey paper; this is a limited search, not proof of absence. Do not enlarge run scans or claim a new endpoint theorem. Next work must supply actual orbit constraints, genuine infinite witnesses, or another main-line lead.

## GC521 — Every unit rightward damage-front jump immediately reverses (2026-10-08)

**Bears on.** GC512's missing actual return constraint, constellation question 2/row 3. Hand proof pending independent reading. Predict an all-time +1 then -1 law for arbitrary finite nonempty damage, extending GC505's initial singleton calculation. Counterfactual that every positive jump has this law is not assumed. Unexpected control: permit initial damage at both adjacent right sites. Preregistered 128 local controls use literal truth-table and XOR/OR updates independently; no transport run or speed claim.

**Actual local proof.** Let u,v be the two synchronous Rule 30 rows, D their XOR, and L the leftmost disagreement. Write primes for one update. Suppose L'=L+1. All sites left of L agree, D_L=1, and D'_(L-1)=D'_L=0. At L-1 the exact derivative is

    D'_(L-1)=1-u_(L-1),

so u_(L-1)=v_(L-1)=1. At L, equality of the updated rows then forces

    u_L OR u_(L+1)=v_L OR v_(L+1).

The common OR value must be 1: value 0 would require both u_L and v_L to be 0, contrary to D_L=1. Consequently u'_L=v'_L=1 XOR 1=0. Since D'_(L+1)=1 and all sites at or below L now agree, applying the leftmost derivative again gives D''_L=1. Locality forbids any disagreement farther left. Hence

    L''=L, or Delta_(t+1)=-1 whenever Delta_t=+1.

This uses neither singleton damage nor an iid environment, and holds at every time with a finite nonempty damage word. Larger jumps leave a different site immediately below the new front, so the proof does not cover them.

**Independent controls.** Exhaust all 32 background words on sites -2 through 2 and four damage choices with D_0=1, D_1,D_2 free, negative damage zero: 128 cases. Literal rule-table and XOR/OR evaluation agree on the first updated rows at -1,0,1 and the second disagreement at 0. Exactly 24 cases have first disagreement pattern (0,0,1), certifying a unit jump regardless of exterior bits. Every one has common updated bit 0 at site 0 and second disagreement 1 there. Controls PASS; their finite locality checks the hand proof, not asymptotic recurrence.

**Record consequence.** GC510's deficit recursion gives, over the forced pair,

    Z_(t+2)=max(Z_t,0)-2.

Thus a unit right jump made at a fresh record or a tie returns to a fresh record after two updates. A unit jump through reused information lowers its nonnegative deficit by 2 over the pair. More generally, if displacement is eventually always at most 1, fresh records must recur infinitely: after a hypothetical last record, Z is a nonnegative integer. Every non-unit step lowers it by at least 1; each unit step is paired with its forced left step and lowers it by 2. It cannot remain nonnegative indefinitely. Therefore finite-record escape in the actual experiment would require infinitely many jumps of size at least 2.

This closes GC512's all-time unit-reversal question and narrows its escape obstruction. It does not rule out larger-jump escape, prove record frequency or establish a limiting speed. GC507 already permits arbitrarily large jumps in ambient finite damage configurations; their probabilities and actual reachable-state constraints remain open. Next examine large-jump recovery with the damage word retained, not another abstract escape model or short-history fit.

## GC522 — Two-site jumps block immediate left return (2026-10-08)

**Scope and prediction.** Actual local damage-front audit after GC521; pending independent reading. Predict every right jump of at least 2 leaves common updated bits 0,1 at the old front and the next site. Thus an exact two-site jump cannot immediately move left. Counterfactual all positive jumps have GC521's forced reversal should fail. Unexpected check: for jumps larger than 2, these bits are not immediately below the new front. No speed or iid reachability claim. Preregistered 512 local controls, no transport scan.

**Proof.** Set old front L=0 by translation; D_0=1 and D_i=0 for i<0. A jump at least 2 heals sites -1,0,1. GC521's first two healed equations give u_-1=v_-1=1 and both centre OR values equal to 1, so u'_0=v'_0=0. Healing site 1 gives

    (u_1 OR u_2) XOR (v_1 OR v_2)=D_0=1.

If the first OR is 0, then u_1=0, and the earlier centre OR forces u_0=1. If the first OR is 1, the second OR is 0, so v_1=0, the earlier centre OR forces v_0=1, and D_0=1 forces u_0=0. In either case

    u'_1=u_0 XOR (u_1 OR u_2)=1.

Site 1 has healed, so v'_1=1 also. This proves the common prefix 0,1. For an exact jump 2, the new front is 2 and its common left neighbor is 1. The leftmost derivative gives D''_1=1-u'_1=0; locality forbids disagreement below 1. Therefore the following displacement is at least 0. This is a deterministic prohibition of immediate left return, the opposite of the unit-jump law.

**Independent controls and concrete failure.** Exhaust 64 background words on -2 through 3 and eight damage words with D_0=1, D_1,D_2,D_3 arbitrary and negative damage zero. Literal decimal-rule-table and XOR/OR updates agree on the four first outputs and the second disagreement at site 1. Of 512 cases, 32 heal sites -1,0,1; all have common prefix 0,1. Sixteen have the first disagreement at 2; all have second disagreement 0 at site 1. Controls PASS.

GC507's N=1 finite pair u black at {-1,0}, v black at {-1,1} gives a hand counterexample to the all-positive reversal claim: after a jump 2 the common background is {-2,-1,1} and damage is {2}. At the next update damage is {2,3}, so the next displacement is 0. It is an ambient finite-pair example, not a claimed iid single-flip history.

**Outcome and next.** Larger-jump recovery cannot be inferred by extending unit reversal. Exact two-site jumps actively block the immediate left move, while larger jumps preserve only a prefix far behind their new front. GC508's long compensating bout concerns its separate finite family, not all jumps. Quantitative recovery needs the intervening common background and surviving damage. Stop further small-jump enumeration; next a genuine multi-step recovery argument retaining that state, or another main-line lead. No record-frequency or speed conclusion follows.

## GC523 — A genuine single-flip pair escapes with displacement cycle 0,2 (2026-10-08)

**Scope.** Multi-step recovery audit after GC521-GC522, pending independent reading. Prediction: a finite-background edge template restores singleton damage every two updates, with displacements 0,2. Counterfactual every actual single-flip pair has recurrent fresh records should fail. Unexpected check: GC507's N=1 maximal-jump example enters this template. Two fixed finite pairs through 16 updates were preregistered; no iid speed experiment or small-jump census.

**Invariant template and proof.** Translate the current singleton damage to site 0. Let the first background row have u_-2=0, u_-1=1, u_0=a in {0,1}, and every positive site white; its farther negative sites may be arbitrary. The second row differs only at 0. On the first update, the first row has

    (u'_-1,u'_0,u'_1)=(1,1-a,a), and u'_i=0 for i>=2.

Direct local evaluation gives damage {0,1}. On the second update,

    (u''_0,u''_1,u''_2)=(0,1,a), and u''_i=0 for i>=3.

The two damaged sites heal and the rightmost derivative creates the sole damage at 2. Thus the template is restored after translation by 2, including the unchanged parameter a. Farther-left bits cannot affect any of these listed outputs. Induction proves the two-update cycle for all time.

Take the finite first row black at {-1} when a=0, or {-1,0} when a=1, and flip site 0. These are genuine finite backgrounds with one initial flipped bit, not an abstract displacement model. At time t,

    D(t)={t} for even t, and D(t)={t-1,t} for odd t;
    L_t=t for even t, and L_t=t-1 for odd t.

Hence L_t/t tends to +1. GC509's exposure indices are J_t=-1 at even times and -2 at odd times. Starting from B_0=0, exactly ticks 0 and 1 are fresh; thereafter B_t=-2 and J_t>=B_t. This realizes finite-record escape in an actual deterministic single-flip experiment. It is compatible with GC521: the cycle contains jumps 2 and 0, never a unit right jump. It also matches GC522's prohibition of immediate left return after a jump 2.

**Independent controls.** For each a, evolved both finite rows with literal decimal-rule-table and XOR/OR updates through time 16. All 17 full rows agree between methods. Exact damage sets, the restored edge template at each even time, and the exposure assertion that only the first two ticks are fresh all PASS. Universal time coverage comes from the template induction, not the finite test.

**Unexpected existing-family connection.** GC507's N=1 pair updates to first row {-2,-1,1} with damage {2}. Recenter at 2: its common sites -2,-1 are 0,1, its centre and positive half are white. Thus it enters the a=0 template and escapes forever. This is outside GC508's N>=2 compensating-bout statement and supplies no contradiction to that family calculation.

**Measure guard and outcome.** The invariant family prescribes an infinite all-zero initial positive half, an event of probability zero under the iid fair background. Every finite prescribed corridor has positive probability, but that does not give positive probability to infinite escape. Consequently this refutes universal deterministic recurrence and universal recovery for single flips, while leaving almost-sure iid recurrence and inward-speed existence open. The iid problem must exclude or control such special escape environments probabilistically; finite damage and singleton resets alone cannot do it. Next a conditioned large-jump recovery argument or another main-line lead; do not extend these two fixed controls.

## GC524 — The specific 0,2 escape bout has an exponential iid tail (2026-10-08)

**Scope.** Hand probabilistic recovery audit for GC523's exact displacement pattern, pending independent reading. Predict n cycles force 4n-1 initial positive zeros. Counterfactual adaptive front conditioning preserves spatial iid is not assumed. Unexpected check: a deterministic time/site union bypasses that conditioning. Uses already-proved G97 spatial fair-product invariance; no new experiment, fixed-family expansion or general speed claim.

**Exact corridor characterization.** Start with singleton damage at site 0 in any background row. Precisely n consecutive displacement pairs (0,2), n>=1, occur if and only if

    u_-2=0, u_-1=1, and u_j=0 for 1<=j<=4n-1.

The centre bit and farther negative bits are free. For one cycle, the first stationary move requires u_-1=1 and u_1=0. After it, damage is {0,1}. Healing the candidate site -1 on the second update requires u_-2=0. Healing site 0 requires unequal common first-row bits at 0 and 1; substituting their local updates forces u_2=0. Healing site 1 then forces u_3=0. The derivative at site 2 is 1, proving the base equivalence. Its two free-centre choices agree with GC523's independent finite-pair controls.

For induction, this base corridor gives GC523's restored common bits 0,1 at sites 0,1 after two updates. With initial sites 1,2,3 zero, direct evaluation gives

    F^2(u)_3=u_4 OR u_5.

Consequently making the evolved sites 3 through K zero, K>=3, forces initial sites 4 through K+2 zero: the first equation forces u_4=u_5=0, and successively, once sites through i+1 are zero, F^2(u)_i=u_(i+2) for i>=4. Conversely that initial zero corridor makes all those evolved sites zero. Apply the induction hypothesis to the singleton at site 2 for n-1 remaining cycles, using K=4n-3. This extends the required corridor exactly to 4n-1. The restored centre bit is unchanged once u_4,u_5 are zero. No exterior-bit or probabilistic assumption enters this equivalence.

**Fixed-time probability bound.** In the actual iid initial-background single-flip experiment, G97 makes the first background row spatially iid fair at every deterministic time. At any fixed time t and site l, a singleton-damage bout of n cycles implies the displayed corridor translated to l, which prescribes 4n+1 independent bits. Thus its unconditional probability is at most

    2^(-(4n+1)).

This is an upper bound even if the singleton event depends on the corridor. At time 0 with the prescribed initial single flip it is exact. It is not a conditional probability given a selected damage history or stopping time.

**Adaptive-start guard and logarithmic bound.** The actual front lies in [-t,t]. Union over all starts 0<=t<=T and their possible sites gives

    P(any singleton 0,2 bout of n cycles starting by T)
      <=(T+1)^2*2^(-(4n+1)).

No temporal independence is required. Set T=2^k and n=ceil(c*k), with any c>1/2. These probabilities are summable in k. Borel-Cantelli therefore bounds the longest such bout starting by dyadic horizon T, almost surely eventually, by fewer than ceil(c*log_2 T) cycles. In particular no infinite 0,2 singleton bout can begin at any finite random time or front position in this iid experiment.

**Outcome and limits.** GC523's concrete deterministic escape family is now quantitatively excluded in the iid experiment, including adaptively encountered starts. This handles exactly repeated pairs 0,2 from singleton damage. It does not bound other outward histories, arbitrary larger-jump recovery, total reused-information excursions or record frequency, and establishes no inward limiting speed. Stop elaborating this one escape pattern; the next useful step needs a different actual state constraint or another main-line lead. This hand characterization and probability audit await independent reading.

## GC525 — A certified finite-seed edit is invisible throughout the interior (2026-10-08)

**Scope.** Bulk-universality bridge from GC523's exact damage support; hand corollary pending independent reading, no novelty or new experiment. Prediction: interior observers eventually see identical traces, including an exact singleton/adjacent-pair centre identity. Counterfactual every finite seed edit is invisible is not inferred. Unexpected check: an observer riding the right light cone distinguishes the pair forever.

**Exact observational equivalence.** Put GC523's initial flip at l. Its template has common bits 0,1 at l-2,l-1, arbitrary centre bit, zero positive tail, and arbitrary common farther-left data. Its exact support is

    D(t)={l+t} for even t;
    D(t)={l+t-1,l+t} for odd t.

All sites below l agree at every time. At a fixed site i>=l, the traces agree after time i-l+1; this is a sufficient bound, including both parities. More generally any observer path satisfying i(t)<l+t-1 eventually has identical samples eventually. In particular every path with limsup i(t)/t<1 has that property. This is equality of samples, stronger than equality of statistics, for this explicit family only.

For the unexpected boundary check take i(t)=l+t. That site is damaged at every time. Its two traces disagree forever, despite agreement along every strictly interior fixed-speed observer. Bulk agreement therefore does not mean the full configurations coalesce or that the moving edge is unobservable.

**Direct prize bridge.** Choose first seed {0} and second seed {0,1}. They are GC523 translated by l=1, with centre parameter a=0. Site 0 lies strictly below l, so their centre traces are identical from time 0 onward. The prize's singleton trace is therefore also the site-0 trace of this distinct two-cell seed. For all other fixed sites their traces differ at only finitely many times; eventual periodicity, existence/value of colour frequency and normality consequently coincide there, without establishing any of those properties.

**Outcome and limit.** This is a proved candidate for one exact finite-seed equivalence class, serving the bulk-universality question. It supplies an invariant example missing from the broad right-edge escape survey, not a classification of all seed edits, a core mixing theorem or a prize solution. No new run is needed: the exact support and template induction are GC523's pending proof. Next a genuinely different seed-equivalence mechanism or return to another main-line lead; stop elaborating this template.

## GC526 — Width-two damage confinement is an iid null event (2026-10-08)

**Scope.** Actual reachable-state confinement audit, pending independent reading. Prediction: perpetual width at most 2 forces GC523's cycle. Counterfactual this excludes every bounded width is not inferred. Unexpected finite-bout guard: a final unit right jump may reverse beyond the observed interval. Uses GC521 and GC524; hand proof, no new experiment or template run.

**Width transitions.** In the initial single-flip experiment the rightmost disagreement is R_t=t. Define w_t=R_t-L_t+1. The exact identity is w_(t+1)=w_t+1-Delta_t. Under w_t,w_(t+1)<=2, the only possibilities are

| Current width | Displacement | Next width |
| --- | --- | --- |
| 1 | 0 | 2 |
| 1 | 1 | 1 |
| 2 | 1 | 2 |
| 2 | 2 | 1 |

GC521 says any displacement 1 is followed by -1; that following update adds 2 to the width and makes it at least 3. Thus if width remains at most 2 forever from some time, no unit right jumps are possible. The remaining transitions alternate stationary and two-site jumps. Starting at width 1 gives the exact 0,2 cycle; starting at width 2 reaches a singleton after one update and then gives it. GC524 excludes an infinite such singleton cycle at any encountered start under the iid background. Consequently, almost surely w_t>=3 infinitely often. No claim for widths 3 or larger follows.

**Finite-bout tail with endpoint protection.** Suppose width is at most 2 for 2n+2 consecutive updates beginning at time t, including both endpoint rows. Every unit right jump among the first 2n+1 updates would reverse within the window and violate the width bound. Those updates must therefore follow the remaining alternating transitions. There are n full 0,2 cycles from a singleton at time t, or at time t+1 if the initial width is 2. The extra final update is essential; merely forbidding every unit jump in an unprotected finite window would be wrong.

At deterministic time s singleton damage must sit at its rightmost site s. GC524's unconditional corridor bound at the fixed time/site (s,s) is 2^(-(4n+1)); it needs no conditioning on the damage. The two possible singleton start times above therefore give

    P(width stays at most 2 for 2n+2 updates from t)<=2^(-4n).

Union over 0<=t<=T gives at most (T+1)*2^(-4n), without temporal independence or adaptive-start iid. At T=2^k and n=ceil(c*k), any c>1/4 makes this summable. Borel-Cantelli bounds these confinement bouts almost surely eventually by fewer than 2*ceil(c*log_2 T)+2 updates for starts by dyadic horizon T.

**Unexpected counting contraction.** The same right-edge identity also sharpens GC524's separate singleton-cycle union: its fixed singleton position is s, so only T+1 candidate starts are needed, rather than a quadratic time/site grid. Its earlier bound remains valid but is conservative. Neither improvement supplies a probability conditioned on a selected front history.

**Outcome and limit.** This closes eventual width-two confinement as an iid escape mechanism, with a quantitative bound on every such bout. It goes beyond excluding one initially specified template, while remaining far from general recurrence. GC510's finite-record escape has eventual width at most its total exposure E, so any such iid escape must have E>=3. Exposure above that threshold, wider surviving damage and inward-speed existence remain OPEN. Next a width-independent recovery argument or a different main-line lead; do not enlarge a width census.

## GC527 — Outward displacement requires a weighted large-jump budget (2026-10-08)

**Scope.** Width-independent actual front audit using GC521, pending independent reading. Prediction: an interval's displacement is bounded by its jumps of size at least 2, with a one-site endpoint allowance. Counterfactual unweighted jump counts control displacement is not assumed. Unexpected check: the final unit jump may reverse outside the interval. Hand proof and existing exact controls only; no experiment, width census or speed claim.

**Interval inequality.** Define J(s,N)=sum of Delta_t over s<=t<N with Delta_t>=2. Pair every unit right jump in that interval with its forced next left move from GC521. These pairs are disjoint and each has displacement 0. Only a possible final unit jump at t=N-1 is unpaired. All remaining displacements outside J are nonpositive. Therefore for every 0<=s<N,

    L_N-L_s<=J(s,N)+1.

A negative first step whose preceding unit jump falls outside the interval only strengthens this inequality. It requires no stochastic law, width bound or conditional regeneration.

**Finite-record escape needs positive large-jump density.** On GC512's finite-fresh-record event, total exposure E=-B is eventually a fixed finite integer, and t+1-E<=L_t<=t. Thus eventual width w_t=t-L_t+1 is at most E. The exact width recursion and w_(t+1)>=1 imply Delta_t<=w_t<=E. Combine these inequalities with the interval bound, for s after the last fresh record:

    J(s,N)>=N-s+1-E-1=N-s-E;
    J(s,N)<=E*C(s,N),

where C(s,N) counts displacements at least 2. The first bound uses L_N>=N+1-E and L_s<=s. Consequently

    liminf C(s,N)/(N-s)>=1/E.

This strengthens GC521's necessary infinite-large-jump condition to a positive lower frequency on each finite-exposure escape history. GC526 says such iid escape would have E>=3, but supplies no probability bound for those wider histories.

**A sufficient recurrence target, not an established estimate.** If the actual iid front were proved to satisfy limsup J(0,N)/N<1 almost surely, finite-record escape would be impossible: that event has L_N/N tending to 1, contradicting the interval inequality. This would prove infinitely many fresh records only. Positive record frequency and inward-speed existence would still need additional estimates. No such weighted-budget bound is established here.

**Independent endpoint controls.** GC523's cycle has J(0,2k)=2k=L_(2k), showing equality in the main budget term. GC505's initial unit right step gives L_1=1 with J(0,1)=0, so the endpoint allowance cannot be removed. Following its forced left step gives L_2=0 and cancellation exactly. The all-left history has J=0 and negative displacement, consistent with the one-sided bound. GC507's unbounded ambient jumps explain why a universal replacement of weighted mass by a fixed multiple of jump count would require a width or size hypothesis; iid reachability is not asserted.

**Outcome and next.** The actual return law gives a width-independent displacement budget and a quantitative necessary condition for finite-record escape. The missing work is probabilistic control of weighted large jumps and their intervening state, not another scalar closure or bounded-width census. These hand inequalities await independent reading; general recurrence and transport speed remain OPEN.

## GC528 — The existing trace sample certifies 32 MSB-first states (2026-10-08)

**Lane and scope.** The probabilistic weighted-jump estimate remains missing. Switch to a bounded Problem 3 model audit of GC487's unchanged sample: prefixes n=1..32, suffixes (d,r) with d=0..4 and 0<=r<2^d, maximum trace index 527. Predict all 32 transposed prefix profiles differ. Counterfactual this proves nonautomaticity remains false. Unexpected check: d=0 means empty suffix, not a zero digit. No larger trace, kernel census or asymptotic fit.

**Separate MSB-state lemma.** Let a deterministic finite automaton with output read canonical binary inputs from most significant to least significant digit and return the selected trace bit. After reading the canonical digits of a positive prefix n it occupies a state q_n. Appending the d-bit suffix for r, padded to length d, gives canonical input 2^d*n+r. Equal prefix states must therefore have equal outputs for every common suffix, including the empty suffix. Distinct profiles

    P_n=(a(2^d*n+r)) over the 31 fixed suffixes

force distinct q_n. This does not reinterpret GC487's LSB states; it proves a separate convention-correct lower bound from rows of the same sample matrix.

**Fixed outcome.** Probe rule30_gpt_msb_prefix.py recomputes the existing 528 rows with independent decimal-set and packed XOR/OR rules, agreeing throughout. It verifies all canonical concatenation identities, including the empty suffix. All 32 Rule 30 prefix profiles are distinct, with 496 pairwise differing-suffix witnesses retained outside git. Thue-Morse has exactly two profiles; GC487's original column signatures still number 31. Controls and blind prediction PASS. The concatenation guard was added explicitly and the same scope rerun; no extra indices were introduced.

Hence any exact canonical MSB-first DFAO for the singleton trace needs at least 32 states. GC487's independent LSB-first bound remains 31. The inequalities concern two different reading conventions, not a computational time lower bound.

**Counterfactual retained.** The sequence agreeing with these bits through index 527 and zero thereafter preserves every profile but is automatic, by a finite canonical-input trie. Thus the finite certificate cannot prove an infinite kernel or exclude all finite automata. It also says nothing about arithmetic memory, approximation or general sublinear indexing algorithms. Hand lemma pending independent reading; measured sample identities are exact finite controls.

**Outcome and next.** The existing sample now has a direct bound for the usual MSB convention as well as the LSB convention. Stop finite certificate expansion. A useful next step must supply an analytic infinite family of distinguishable continuations or a proved selected-orbit representation, otherwise move to another main-line lead.

## GC529 — Replica defect profiles are not the simultaneous damage process (2026-10-08)

**Source-audit scope.** A bounded search for a rigorous iid Rule 30 single-flip speed theorem found no usable theorem in the inspected material; absence is not established. Read the abstract, replica definition in section 2.2 and Rule 30 figure discussion of [Baetens and Gravner, Introducing Lyapunov profiles of cellular automata](https://www.math.ucdavis.edu/~gravner/papers/bg2014.pdf), identified by [arXiv:1509.06639](https://arxiv.org/abs/1509.06639). This is targeted reading, not a full-paper audit. Their procedure evolves separate single-defect replicas and retains multiplicity; the Rule 30 figure is a finite numerical profile. Do not import it as our two-copy front theorem.

**Prediction and unexpected check.** Predict replica counts fail to dominate simultaneous damage pointwise because GC507's derivative includes a quadratic damage term. Counterfactual the profile directly supplies a bound on our front is unsupported. Unexpected check: make the obstruction reachable at the second update of a genuine initial single flip, rather than just posit two unrelated local defects. Fixed two-step finite-pair control preregistered; no speed run.

**Local obstruction.** At a background triple (left,centre,right)=(0,1,1), flip centre and right together. Rule 30 changes from output 1 to output 0. Flipping either one alone leaves output 1. Thus simultaneous damage is 1, whereas the sum of the two single-flip output derivatives is 0. In GC507's exact formula, the missing contribution is d_c*d_r=1; both linear coefficients vanish. Replica multiplicity does not repair an absent dependency edge.

**Actual single-flip embedding.** Start the first finite row black at {-2,-1,2}, and flip site 0 in the second. After one update their damage is exactly {0,1}; the first background triple at sites -1,0,1 is (0,1,1). After the next update the actual two-copy disagreement at site 0 is 1. The separate replicas obtained by flipping site 0 or site 1 in that common first row both agree with its next output at site 0, giving replica count 0 there. Independent literal-rule-table and XOR/OR finite-row controls PASS.

Only the initial five background bits at -2 through 2 enter this local calculation, namely (1,1,0,0,1). Hence the embedding also occurs on an iid cylinder of probability 1/32; it is not confined to an iid-null finite background. No asymptotic probability or speed is inferred.

**Outcome and limits.** This refutes pointwise support/count domination by the replica process for our simultaneous two-copy damage. It does not prove its cone endpoints differ, contradict the source's stated profile, or invalidate every Lyapunov notion. Any comparison theorem must specify the process and establish the relevant endpoint relation separately. Next inspect primary definitions of extremal perturbation exponents before importing an existence result; the actual iid single-flip recurrence and speed remain OPEN. Hand scope audit pending independent reading.

## GC530 — Shift-maximized exponents see rare zero windows (2026-10-08)

**Source and scope.** Targeted reading of [Tisseur, Cellular automata and Lyapunov exponents](https://arxiv.org/pdf/math/0312136): introduction, section 3.1 definitions and Proposition 3.1 statement, section 3.2 definitions and Proposition 3.2 statement with the adjacent convergence question. Not a full-paper or proposition-proof audit. The extremal quantities maximize over spatial shifts and allow arbitrary one-sided perturbations. Average quantities are defined using a liminf of normalized integrals; their definition does not assert convergence of that sequence. Neither definition is the fixed-origin single-flip front.

**Prediction and counterfactual.** Predict the extremal quantities for Rule 30 on fair iid rows attain radius speed 1 in both directions. Counterfactual an extremal limit existence theorem establishes our selected pair's speed is unsupported. Unexpected check: the infinite zero row has probability zero, yet arbitrarily long finite zero windows occur somewhere almost surely. This is a hand proof with two independent bounds, not a numerical experiment.

**Definitions used.** Write W_0^+(x) for rows agreeing with x at every coordinate at least 0, and W_0^-(x) for rows agreeing at every coordinate at most 0. Let tilde-Lambda_n^+ be the least nonnegative s guaranteeing agreement at all coordinates at least s, for every allowed W_0^+ perturbation and all updates 1 through n. Define tilde-Lambda_n^- analogously with agreement at coordinates at most -s. Lambda_n^+ and Lambda_n^- maximize these quantities over spatial shifts of x. Radius-one locality gives both Lambda_n values at most n for every row.

**Matching lower bounds on iid rows.** Fix n at least 1. Almost surely an iid row has a translate whose coordinates -2n through 2n are all zero: disjoint windows each have positive probability, so the probability none is zero tends to zero. At this translate flip only site -1. This is allowed in W_0^+. At update n the background output at coordinate n-1 is zero, while the perturbed output is 1. Its entire initial cone [-1,2n-1] lies in the zero window, so outside bits cannot affect the calculation. The isolated seed's rightmost black cell advances one site every update, since the local triple at its next right edge is 100. Any threshold s at most n-1 therefore fails, proving tilde-Lambda_n^+=n there.

For W_0^- flip site 1 instead. At update n the disagreement at coordinate 1-n persists. Its initial cone [1-2n,1] also lies inside the window. The isolated seed's next left-edge triple is 001, with output 1. Any s at most n-1 includes this disagreement in the purported agreement region. Hence tilde-Lambda_n^-=n at this translate.

Taking the countable intersection of the probability-one zero-window events gives, simultaneously for every n,

    Lambda_n^+=Lambda_n^-=n almost surely.

Consequently both corresponding extremal exponents are 1. The radius bound and the explicit isolated-seed light-cone witnesses are separate upper and lower controls. This direct derivation does not rely on importing the proof of Tisseur's existence proposition.

**Outcome and limits.** Spatial maximization selects worst-case finite windows arbitrarily far away. It supplies no typical speed for the actual fixed-origin simultaneous damage pair; GC529 already guards the distinct replica notion. The result is a quantifier audit, with no novelty priority or prize claim, pending independent reading. General iid single-flip recurrence, weighted large-jump control and inward-speed existence remain OPEN. Next inspect a source only if its process actually retains simultaneous damage and the fixed-origin quantifiers; otherwise return to actual front-state reasoning.

## GC531 — The plus shielding exponent is already exact for every background (2026-10-08)

**Scope and prediction.** Contract GC530 rather than extend its window argument. Predict the existing rightmost-damage law fixes both plus quantities at horizon n for every full-shift background. Counterfactual reflection supplies the minus shielding value is unsupported: Rule 30 is asymmetric. Unexpected check: a candidate shielding distance s is defeated at time s+1, not by assuming the perturbation starts at the shield boundary itself. No experiment or novelty claim; hand audit pending independent reading.

**Exact right edge, independent of the background.** Let two rows differ on a finite nonempty set with rightmost site R. At coordinate R+1 their centre and right inputs agree, while their left inputs differ. In f(l,c,r)=l XOR (c OR r), the two outputs therefore differ regardless of those common inputs. Every coordinate greater than R+1 has identical input triples. Thus the rightmost disagreement after one update is exactly R+1, and induction gives R+t. This uses the same exact law already underlying GC505 and GC526. Finite background support is unnecessary; only the disagreement set must be finite.

**Extremal quantity without spatial selection.** Flip just site -1 in any row x. The resulting row belongs to W_0^+(x). At time n its rightmost disagreement is n-1. Hence every nonnegative agreement threshold s at most n-1 fails. Radius-one locality supplies the independent upper bound n, so tilde-Lambda_n^+(x)=n for every x. Its spatial maximum Lambda_n^+ is also n. GC530's zero-window witness is needed only for its minus extremal argument, not the plus argument.

**Shielding quantity.** In the primary [Tisseur definition](https://arxiv.org/pdf/math/0312136), section 3.3, I_n^+(x) is the smallest nonnegative s for which every row agreeing with x at coordinates at least -s continues to agree at coordinates at least 0 during updates 1 through n. For any candidate s<n, flip site -s-1. At time s+1<=n its rightmost disagreement is exactly 0, so this candidate fails. With s=n, radius-one cones for coordinates at least 0 and updates at most n lie wholly inside the protected initial half-line. Therefore

    I_n^+(x)=n for every x and n>=1.

Its integral against the fair iid measure is exactly n. The normalized integral is exactly 1 at every horizon, so the plus average exponent is 1 and this particular defining sequence converges. This is a direct Rule 30 calculation, not a general convergence assertion from a liminf definition. No value or convergence is established for the minus average exponent.

**Controls, correction and limits.** The XOR right-edge identity supplies the lower witness for arbitrary backgrounds; the causal radius supplies the upper guarantee. The n=1 endpoint requires flipping -1 and observing site 0, consistent with GC505's unconditional rightmost damage bit. Source section labels in GC530 were imprecise: propagation definitions are in 3.1, Proposition 3.1 in 3.2, and average definitions plus Proposition 3.2 in 3.3. The targeted reading scope and results are unchanged; this correction is retained explicitly.

The plus quantities track influence moving right, the already deterministic edge of our single-flip pair. The difficult left edge and its inward speed are not determined by them. Stop plus-exponent elaboration; actual minus-front state, record recurrence and weighted-jump estimates remain OPEN.

## GC532 — Fresh exposure is exactly a record of damage span (2026-10-08)

**Scope and prediction.** Return to the actual single-flip pair, using GC509's specified exposure procedure and the exact rightmost disagreement R_t=t. Predict its fresh ticks are exactly strict records of the span of the disagreement set. Counterfactual unbounded span guarantees positive inward speed is unsupported; a rate estimate is still missing. Unexpected check: exposure after N updates records spans before update N, not the span at time N. Hand deduction, no experiment, novelty or prize claim; pending independent reading.

**Exact geometric meaning.** Write w_t=t-L_t+1 for damage span, including any undamaged holes between its endpoints. GC509 defines J_t=L_t-1-t and B_N=min(0,J_0,...,J_(N-1)). Thus J_t=-w_t and the number of exposed negative initial sites satisfies

    E_0=0;
    E_N=max(w_0,...,w_(N-1)) for N>=1.

Freshness J_t<B_t is exactly w_t>E_t. Since w_0=1, each fresh tick is a strict new span record. The front cannot move left more than one site per update, so w_(t+1)<=w_t+2. Each increase of the running maximum has size 1 or 2 (the first has size 1). Therefore GC510's F_N, the number of fresh ticks before N, obeys

    F_N<=E_N<=2*F_N.

Consequently infinitely many fresh ticks are equivalent, pathwise, to unbounded damage span. Finitely many fresh ticks are equivalent to a uniformly bounded span over all times, and hence to eventual bounded span, since every finite prefix has finite span. This supplies the converse missing from GC512's finite-exposure implication. It uses no iid assumption or fresh-bit fairness, only the stated exposure scheme and right-edge identity.

**What a speed would force.** If L_N/N converges to -v, then w_N/N converges to a=1+v>=0. A sequence with nonnegative terms and ratio tending to a has its prefix maximum divided by N tending to a too: finitely many early terms vanish after division, and later terms lie between (a-epsilon)t and (a+epsilon)t. The lower bound uses t=N-1. This includes a=0. Hence

    E_N/N -> 1+v.

Combining with the pathwise bounds gives liminf F_N/N >= (1+v)/2 and limsup F_N/N <= 1+v, with the latter capped at 1. These are necessary conditional bounds, not existence of a speed or a record density. They quantify why unbounded span alone falls short: it need not supply any positive normalized maximum.

**Independent controls and endpoint guard.** At N=1, only w_0 enters, so E_1=1 regardless of the next front. For first-step displacements -1,0,+1, the spans w_1 are 3,2,1 and E_2 is respectively 3,2,1, matching GC509's directly revealed endpoints. GC523's actual escape cycle has spans 1,2,1,2,..., so E_N=2 from N=2 onward, with exactly its two fresh records. These controls check the offset and bounded-span equivalence independently of an asymptotic assumption. No new finite enumeration was run.

**Outcome and next.** The recurrence target is now geometric: prove the actual iid single-flip damage span unbounded almost surely. GC526 excludes eventual span at most 2, but does not exclude arbitrary finite bounds. A bounded-span classification or uniform probabilistic escape-from-confinement argument would serve that target; a width census or scalar closure does not prove it. Positive inward speed still needs stronger growth and convergence control. Stop bookkeeping reformulation and seek a mechanism forcing new span records.

## GC533 — Recurring zero windows on the right ray would force unbounded span (2026-10-08)

**Scope and predictions.** Seek an actual escape-from-confinement mechanism serving GC532, retaining arbitrary damage holes and the deterministic rightmost site t. Predict a background zero window along that edge forces any span bound M to fail shortly. Counterfactual ordinary fixed-frame mixing implies recurrence on the moving right ray is unsupported. Unexpected check: the relevant moving map has its permutive input at coordinate 0, not at a negative coordinate. Hand finite-cone proof, no experiment; conditional recurrence implication pending reading, with its dynamical premise OPEN.

**Uniform escape witness.** Fix integer M>=1 and h=ceil(M/2). At time t suppose the actual span w_t<=M and the first background is zero at every site from t-2M through t. Then L_t lies between t-M+1 and t. During each of the next h updates, the leftmost damage advances left exactly one site. Indeed, assuming the first k such advances, its below-front common bit is at coordinate L_t-k-1 and time t+k. Its backward cone in the row at time t is

    [L_t-2k-1, L_t-1], for 0<=k<h.

This lies inside [t-2M,t]: the lower endpoint is at least t-M-2k, which is at least t-2M for these k. A wholly zero initial cone produces a zero output. GC505's exact left-edge derivative then forces the next advance. The right edge still advances right at every update, so

    w_(t+h)=w_t+2h>M.

The argument is uniform in the damage word and outside background, and requires no independence from the selected front. It also works for a bounded span interval starting at an arbitrary time.

**A precise sufficient dynamical premise.** Define b_i(t)=u_(t+i)(t) and H=shift composed with Rule 30, where shift(x)_i=x_(i+1). Then b(t)=H^t u(0), with

    H(b)_i=b_i XOR (b_(i+1) OR b_(i+2)).

For each M, let C_M be the zero cylinder on coordinates -2M through 0. If the actual iid background's H orbit visits every C_M infinitely often almost surely, then no eventual finite span bound can persist: pick a visit after that bound begins and apply the uniform witness. Countably many M suffice. GC532 then gives infinitely many fresh ticks almost surely. This implication establishes neither that visit premise nor a transport rate.

The fair iid measure is H-invariant by G97 and shift invariance. Ergodicity of H would be a sufficient stronger premise: Birkhoff gives visit frequency equal to the positive cylinder measure 2^(-(2M+1)). Invariance alone does not give visits to every positive-measure cylinder on almost every orbit; it only supports recurrence for points already in that cylinder. This prevents silently using Poincare recurrence to fill the gap.

**Critical-direction guard and independent controls.** The existing PRIOR-ART mixing entry attributes a theorem requiring a negative leftmost neighbourhood coordinate. Ordinary Rule 30 has endpoint -1; H has endpoint 0. That hypothesis is lost exactly on the right light-cone ray. The old entry also records a nonergodic permutive example with neighbourhood [0,2], so permutativity at 0 alone cannot be substituted for the missing premise. The linked thesis could not be opened in this block; its claim remains attributed to the earlier reader, not newly verified here.

For M=1, h=1 and one zero below the singleton already gives span 3; the longer stated cylinder is a sufficient uniform witness. For M=2, h=1 and every initial span at least 1 exceeds 2 after the forced left advance. GC523's bounded escape template contains a black bit immediately below the singleton on its zero-step phase, so it fails the zero-window premise; the witness does not contradict that actual deterministic escape. These local controls and the explicit cone endpoints are independent of the unproved recurrence premise.

**Outcome and next.** This supplies a damage-independent finite witness for escape from every bounded span, reducing one possible recurrence approach to zero-cylinder visits along a specified critical ray. A bounded directional-dynamics search found no usable theorem in inspected material; absence is not claimed. Next audit this critical-ray visit premise or derive a different reachable-state return mechanism. No speed run, width census, ergodicity assertion or prize conclusion.

## GC534 — The critical ray is a parity cocycle over its own right tail (2026-10-08)

**Bounded audit and retained failure.** The follow-up search for a critical-ray ergodicity theorem supplied no usable result. Ordinary Rule 30 mixing does not settle GC533's map H=shift composed with F. A proposed fresh-left-pivot proof also stalls: H^t(x)_0=F^t(x)_t has initial cone [0,2t], so its leftmost XOR pivot is always X_0, not a newly revealed negative bit. One-time fair marginals do not restart that pivot. This is a failure of that proof route, not a nonergodicity theorem.

**Prediction and unexpected control.** Predict an exact two-state phase extension after splitting site 0 from its right tail. Counterfactual this representation by itself supplies ergodicity is unsupported. Unexpected check: the first critical-ray update already correlates with the initial boundary bit, despite both marginals being fair. Hand formulas only, no experiment or search expansion.

**Exact right-half factor.** Write z=x_0 and Y=(x_1,x_2,...). Let G be H restricted to this autonomous right tail, so G(Y)_j=Y_j XOR (Y_(j+1) OR Y_(j+2)), with indices j>=1. Put q(Y)=Y_1 OR Y_2. The right-half evolution is exactly

    (z,Y) -> (z XOR q(Y), G(Y)).

After t updates, its boundary bit is z XOR Q_t(Y), where Q_t is the parity of q(Y),q(GY),...,q(G^(t-1)Y). Under the iid product law z is independent fair, so each boundary marginal is fair regardless of the parity law. Yet at t=1,

    E[(-1)^z * (-1)^(z XOR q(Y))]=E[(-1)^q(Y)]=-1/2,

since q is zero with probability 1/4. This exact control refutes temporal independence; it does not refute ergodicity or decay at large times.

**A specific invariant-phase obstruction.** Suppose a measurable function phi on the right tail takes values in {-1,+1} and satisfies

    phi(GY)=(-1)^q(Y) * phi(Y) almost surely.

Then K(z,Y)=(-1)^z*phi(Y) is unchanged by the right-half map: both factors acquire (-1)^q and cancel. K takes each sign with probability 1/2, because z is independent fair. Such a phi would therefore give a nonconstant invariant function and refute ergodicity of H already on this factor. Existence of phi is not proved. Its absence alone would also be insufficient unless ergodicity of the autonomous base were justified separately.

The base is another copy of the same one-sided rule. Assuming its ergodicity as a fresh premise merely relocates the unresolved problem. The equation is a concrete phase-obstruction question, not an independent theorem that resolves the critical ray. A constant phi fails because q is not zero almost surely. This is an independent immediate control on the proposed obstruction.

**Outcome and next.** The critical-ray visit route now has two explicit obstacles: no fresh left pivot, and a possible measurable invariant parity phase over the right tail. No usable directional theorem, invariant phase or cylinder-visit proof was obtained in this bounded block. Retain that failure and stop generic mixing transfer. Next an actual conditional confinement-escape mechanism, or a carefully justified phase-obstruction analysis; no numerical mixing fit can settle the measurable equation or the selected prize trace.

## GC535 — No finite-prefix sign phase solves the critical-ray equation (2026-10-08)

**Scope and predictions.** Audit GC534's possible invariant sign without enumerating widths. Predict its equation has no sign solution determined by a fixed finite prefix of the right tail. Counterfactual the same witness rules out every measurable phase is unsupported. Unexpected check: a null fixed point is insufficient for an almost-sure equation, so use a positive iid cylinder with the same finite observations. Hand proof, no experiment or novelty claim, pending independent reading.

**Positive-cylinder obstruction.** Retain G(Y)_j=Y_j XOR (Y_(j+1) OR Y_(j+2)) and q(Y)=Y_1 OR Y_2. Suppose phi(Y) in {-1,+1} depends only on Y_1 through Y_m, with m>=1. On the cylinder

    Y_1=1, Y_2=...=Y_(m+2)=0,

the first m bits of GY equal those of Y: its first bit remains 1 and all the other listed prefix outputs remain zero. Thus phi(GY)=phi(Y). Yet q(Y)=1, requiring phi(GY)=-phi(Y) in GC534's equation. The equation therefore fails throughout this cylinder, of iid measure 2^(-(m+2)), regardless of the unseen tail. No finite-prefix sign phase can satisfy it almost surely. For a constant phase (m=0), it fails whenever q=1, of probability 3/4.

**Continuous phases also excluded.** A continuous function from the compact binary one-sided space to the discrete signs depends on some finite prefix: continuity supplies a prefix neighbourhood at each point, a finite subcover supplies a uniform maximum prefix length. Hence the cylinder argument rules out every continuous sign solution, even if equality was requested only almost surely. It also rules out a measurable solution having an almost-sure finite-prefix or continuous version: G preserves the iid tail measure, so changing phi on a null set changes neither side of its equation except on a null set. Tail invariance follows by projecting G97's H-invariant product measure.

**Independent fixed-point and scope controls.** The infinite tail Y*=(1,0,0,...) is fixed by G and has q(Y*)=1. An everywhere sign solution already contradicts this fixed point. Its iid probability is zero, however; the positive cylinder above is what makes the finite-prefix almost-sure exclusion valid. At m=1 the cylinder is 100 on the first three tail sites; the observed output prefix is again 1 and the cocycle is odd, checking the smallest nonconstant-prefix case directly. An arbitrary measurable phi can depend on arbitrarily distant coordinates and need not be continuous at Y*; none of these controls excludes it.

**Outcome and next.** The local/continuous invariant-phase route is CLOSED: any GC534 sign obstruction, if it exists, must have genuinely unbounded tail dependence and no continuous almost-sure version. This does not prove H ergodic, prove the base ergodic, establish GC533 cylinder visits or give a front speed. Stop finite phase searches. Next a justified measurable obstruction analysis or a different actual confinement-escape mechanism.

## GC536 — A measurable phase would need irreducible prefix error (2026-10-08)

**Scope and prediction.** Audit the unrestricted measurable possibility left open by GC535, with no finite phase census. Predict its finite-prefix approximations have an explicit error floor depending on prefix length, and its sign marginal cannot be strongly biased. Counterfactual ordinary convergence of prefix approximations contradicts these floors is unsupported: the floors themselves tend to zero. Unexpected check: the two comparison errors can be bounded using invariance, without assuming Y and GY independent. Hand probability argument, no experiment or existence assertion; pending reading.

**Conditional hypothesis.** Suppose a measurable sign phi solves phi(GY)=(-1)^q(Y)*phi(Y) almost surely under the iid tail measure. Let psi_m be any sign predictor depending on its first m bits, and put epsilon_m=P(psi_m(Y)!=phi(Y)). G preserves that measure, so the same error probability epsilon_m holds at GY. Whenever both predictions are correct, psi_m satisfies the phase equation on this sample. A union bound, with no independence premise, gives

    P(psi_m(GY)!=(-1)^q(Y)*psi_m(Y))<=2*epsilon_m.

GC535's positive cylinder makes the left side at least 2^(-(m+2)) for m>=1, whatever the predictor. Consequently

    epsilon_m>=2^(-(m+3)), for every m>=1.

Thus an exact measurable phase cannot admit sign-valued prefix approximations with error o(2^(-m)). A continuous almost-sure version would have zero error beyond some finite prefix and is already excluded. No lower bound uniform in m is proved.

**Marginal obstruction and an independent control.** For a constant predictor the phase-equation defect is P(q=1)=3/4. The same comparison bound gives error at least 3/8 for either constant sign, hence

    3/8<=P(phi=+1)<=5/8.

Independently, the exact equation says the phase switches sign with probability 3/4. Since its old and new sign marginals are equal by invariance, positive-to-negative and negative-to-positive transitions each have probability 3/8. Each sign must therefore have mass at least 3/8, reproducing the bound without the predictor comparison. This also gives E[phi(Y)*phi(GY)]=-1/2, a conditional identity rather than an observed mixing coefficient.

**Failure of the proposed approximation shortcut.** Finite-prefix conditional expectations approximate a measurable sign in mean square, so sign predictors can have epsilon_m tending to zero. GC535 alone therefore cannot exclude a measurable solution by appealing to approximation: positive defect at every finite m is compatible with defects tending to zero. The displayed exponentially decreasing floors remain compatible with that limit. No rate theorem for a hypothetical solution is supplied here, and an approximate phase is not an exact invariant function.

**Outcome and next.** Any measurable obstruction must be nonlocal, have both signs with substantial mass, and resist exponentially accurate prefix prediction at the stated rate. These are necessary conditions only; no phase is constructed or excluded. This completes the local-to-measurable scope audit. Stop phase elaboration unless a genuinely new regularity or return mechanism is justified; critical-ray zero visits, unbounded damage span and inward speed remain OPEN.

## GC537 — A fresh tick chooses between two known damage words (2026-10-08)

**Scope and prediction.** Return to the actual iid single-flip pair and GC509's exposure procedure. Conditional on a fresh tick, expose its intervening initial bits but leave the pivot X_(J_t) unrevealed. Predict the entire next damage at sites at least L_t is already determined, not just a left-move probability. Counterfactual this supplies the same law at reused pivots or restarts the whole state is unsupported. Unexpected check: next damage words differ by one site, but the selected background and future history can differ. Hand argument conditional on GC509's fresh-pivot proof, pending joint independent reading; no experiment or novelty claim.

**Known healing branch.** For sites i>=L_t, the exact damage derivative in GC507 uses only the known current damage word and background values u_i(t),u_(i+1)(t). Their initial cone endpoints are at least L_t-t=J_t+1. After revealing the intervening bits down to J_t+1, all these inputs are known without X_(J_t). Let A_t be the resulting next damage set restricted to sites at least L_t. This set is finite and nonempty: the rightmost next damage is t+1. Define

    K_t=min(A_t)-L_t, so 0<=K_t<=w_t,

where w_t=t-L_t+1. Both A_t and K_t are measurable before revealing the pivot. No site farther left than L_t-1 can become damaged, and the derivative at L_t-1 is 1-u_(L_t-1)(t).

**Exact conditional two-branch law.** GC509's triangular cone makes this below-front background bit fair after the intervening reveals, independently of the already determined A_t. Hence the full next damage set is, with equal conditional probabilities,

    A_t union {L_t-1}, or A_t.

The corresponding displacement Delta_t is -1 or K_t. In particular

    E[Delta_t | pre-pivot information]=(K_t-1)/2;
    Var(Delta_t | pre-pivot information)=(K_t+1)^2/4.

This is a conditional statement on fresh ticks only. K_t is a function of the selected background and complete damage word, not an iid random jump drawn anew. Reused ticks retain their known pivot and need a separate law.

**Independent first-step controls.** At time 0, A_0 contains site 1 unconditionally and contains site 0 exactly when X_1=0. Thus K_0=0 for X_1=0 and K_0=1 for X_1=1. The two conditional means are -1/2 and 0; averaging gives -1/4, exactly GC505's independently checked first-step expectation. Combining the fair pivot with the fair X_1 gives its probabilities 1/2,1/4,1/4 for displacements -1,0,+1. No new finite enumeration was run.

**Limits and next.** The one-site difference between the next damage branches does not make their full background states identical. The pivot also enters the background update at and around the old front, so the branches can select different future environments. GC508's singleton-reset guard and GC506's position-only failure still apply. The conditional variance grows with K_t; this formula supplies no bounded-jump concentration estimate or integrable excursion law. Actual finite span at a tick bounds K_t, but the span is not uniformly bounded.

The useful missing input is now explicit: control the known healing jump and later reused-state recovery at fresh encounters, while retaining the full selected state. No bound on their frequency, weighted budget, general recurrence or inward-speed existence is established. Stop scalar closure or phase reformulation; next a justified reachable-state constraint on this healing branch.

## GC538 — Safe fresh branches would force inward rate at least one third (2026-10-08)

**Scope and prediction.** Use GC537's fresh healing offset K and GC521's unit-right reversal. Predict a specific nonvacuous restriction gives positive inward transport without an invariant front law. Counterfactual merely saying all sufficiently late fresh ticks have K<=1 is sufficient fails if there are no such ticks. Unexpected check: retain an actual fresh start, and apply an unconditional martingale probability-one statement rather than conditioning fair bits on future survival. Hand implication conditional on the earlier exposure proof, pending joint independent reading; no experiment or actual restriction theorem.

**Precise hypothesis S.** There exists a finite fresh tick tau such that every fresh tick at or after tau has K_t<=1. This includes the starting tick itself. No assertion is made that S has positive or full iid probability. The stronger hypothesis that every fresh tick from time 0 has K<=1 implies S.

**Actual bounded return blocks.** Starting at a fresh tick under this restriction, a left branch has Delta=-1 and the next tick is fresh; a healed K=0 branch has Delta=0 and the next tick is fresh. A healed K=1 branch has Delta=+1, creates a tie, and GC521 forces Delta=-1 at the following tick. The tick after that is fresh. Thus every fresh start returns to freshness in one or two updates, with net displacement -1 for its left branch and 0 for either healed branch. The condition is nonvacuous, so this proves infinitely many fresh ticks pathwise on S. There are no other reused ticks after tau.

**Accounting without future conditioning.** Retain GC510's global counts F_N of fresh ticks, A_N of their left advances, and T_N of tie left advances. Its exponential moment bound holds for either sign of lambda; exponential Markov and a summable union therefore give

    A_N-F_N/2=o(N) almost surely.

Establish this full-probability set first, then intersect it with S. Do not assert fair coins conditional on S. On each such history, the finite prefix before tau contributes only constants. Each nonfresh tick afterward is the forced tie reversal of a preceding fresh K=1 branch. Up to a final incomplete block,

    N=F_N+T_N+O(1);
    T_N<=F_N-A_N+O(1);
    L_N=-A_N+O(1).

Here the constants may depend on the finite prefix and starting position, but not N. The last identity holds because each unit-right/tie-left pair cancels, stationary healed steps contribute zero, and the only remaining net left moves are fresh left branches.

Consequently N<=2F_N-A_N+O(1)=(3/2)*F_N+o(N), giving liminf F_N/N>=2/3. Since F_N<=N, substitution in the position identity yields

    1/3<=liminf (-L_N/N)<=limsup (-L_N/N)<=1/2

almost surely on S. Speed existence is not supplied; these are bounds on lower and upper rates under the stated dynamical restriction.

**Independent endpoint controls and consequence.** If all fresh offsets after the start are 0, every tick is fresh and the same identities give inward speed 1/2. If all are 1, every healed branch has its tie reversal, so T_N=F_N-A_N+O(1), N=(3/2)*F_N+o(N), and inward speed is 1/3. These are conditional limiting cases, not claims that either actual iid event occurs. The actual first +1,-1 control from GC505 checks the length-two zero-displacement block.

If an actual inward speed v exists with 0<v<1/3, GC532 gives unbounded span and infinitely many fresh ticks. There must then be infinitely many fresh encounters with K>=2: otherwise take a fresh start after the last one and apply the bound above. This is a conditional consequence, not an inference from a finite measured value or a positive-density claim. The reported approximate value 0.246 is not treated as a proven limit.

**Outcome and next.** A clean reachable-state restriction would suffice for positive inward rate, but its lower bound would exclude any true speed below one third. Thus a derivation of the observed lower rate must retain large healing branches and their recoveries; an eventual small-branch closure cannot represent it. No restriction, recurrence or speed theorem is established for actual iid Rule 30. Next control those large fresh branches and ensuing reused states, rather than discard them.

## GC539 — Large fresh branches have a necessary occupation cost (2026-10-08)

**Scope and predictions.** Keep arbitrary actual large healing branches rather than impose GC538's safe restriction. Predict a transport budget in terms of time spent in their fresh-to-fresh blocks and the current unfinished span deficit. Counterfactual counting their starts controls transport is unsupported; a few long blocks can dominate time. Unexpected check: a terminal jump can make span collapse before return, so retain its deficit explicitly. Hand proof conditional on GC509, pending independent reading; no experiment or asserted limiting speed.

**Block partition.** Start a block at each fresh tick s. It consists of updates s through r-1, where r is the next fresh tick; the last block can be infinite. Classify it as safe if its known healing offset K_s<=1, and large otherwise. This uses K before its pivot is revealed, regardless of which branch the pivot later chooses. Let B_N be the number of updates before N that belong to large blocks, including any unfinished prefix. Let G_N count safe starts before N and A_N^safe their fresh left choices. Put Q_N=max(E_N-w_N,0), with GC532's exposure maximum E_N and span w_N. These are counts of update time, starts, choices and deficit respectively, not interchangeable frequencies.

**Safe contribution and fair selection.** A safe block lasts one update on a left branch or K=0 healing, and two on K=1 healing. Its net displacement is -1 on the left branch and 0 otherwise. A final unfinished safe block can contribute +1, from the unit right step awaiting reversal. Thus its total displacement is at most -A_N^safe+1, and its total occupied time satisfies

    N-B_N<=2*G_N-A_N^safe.

The safe indicator is known after gap reveals but before the pivot. GC509's fair-pivot proof therefore applies with this predictable selection: each selected centered increment is a fair sign of size 1/2, otherwise zero. The same two-sided exponential-moment argument as GC510 gives

    A_N^safe-G_N/2=o(N) almost surely.

No independence of selected states, conditioning on future return, or positive safe-start frequency is assumed. Combining the two displays yields A_N^safe>=(N-B_N)/3-o(N).

**Large contribution and terminal guard.** At a fresh start s, w_s is a strict record. Until the next fresh tick r, span is at most w_s. At r it exceeds w_s by 1 or 2, since each update can increase span by at most 2. A completed large block consequently has displacement

    L_r-L_s=(r-s)-(w_r-w_s)<=(r-s).

If a large block is unfinished at N>s, its revealed running maximum is E_N=w_s. Its displacement is (N-s)+(E_N-w_N), so its excess over duration is exactly Q_N. Hence the sum of all large-block displacements is at most B_N+Q_N. This bound deliberately retains the terminal deficit; no uniform upper bound on jump size is introduced.

Adding both contributions, with L_0=0, proves on the martingale probability-one set

    -L_N>=N/3-(4/3)*B_N-Q_N-o(N).

The bounded safe endpoint is absorbed in o(N). This is an actual-history occupation budget, not a new recurrence premise.

**Necessary condition if speed exists.** If L_N/N tends to -v, GC532 gives w_N/N and E_N/N both tending to 1+v. Thus Q_N/N tends to zero. Rearranging the budget then gives

    liminf B_N/N >= (1-3v)/4,

whenever the right side is positive. In particular a true inward speed in (0,1/3) requires positive lower time occupation in large-start blocks, strengthening GC538's infinite-large-start conclusion. It does not give a positive lower frequency of their starts: their durations may be arbitrarily long. The measured approximately 0.246 is not substituted for a proven v.

**Independent controls and limits.** With no large blocks, Q_N=0 except for harmless record endpoints, and the bound recovers GC538's one-third lower rate. GC523's actual finite-background escape has its last fresh start at time 1 with K=2; all later update time lies in that large block, B_N=N-1, while Q_N is bounded. Its outward slope 1 agrees with the budget's rate -1 when occupation tends to 1. This deterministic control tests the partition and unfinished-block guard, not the iid martingale premise. At a fresh endpoint, Q_N=0 and the previous block is completed, checking the one-tick convention separately.

No occupation estimate, integrable excursion duration, unbounded-span proof or limiting speed is obtained. Next target a bound on large-block time or its full conditioned state, retaining the terminal deficit when speed existence is unavailable. Do not replace occupation by a finite branch census.

## GC540 — Two record averages suffice for speed without iid renewal (2026-10-08)

**Scope and prediction.** Turn GC539's missing excursion control into a precise sufficient criterion. Predict finite mean record spacing removes unfinished-excursion effects; an additional mean span gain then fixes the speed. Counterfactual a finite spacing mean alone forces span-gain convergence is unsupported. Unexpected check: future recovery bounds an interior span collapse even though individual right jumps have no universal size bound. Hand criterion pending reading, no experiment or assertion that either mean exists.

**Actual record quantities and assumptions.** Assume infinitely many fresh ticks and list them as tau_0=0<tau_1<... . Write d_j=tau_(j+1)-tau_j for each return-block duration, and r_j=w_(tau_(j+1))-w_(tau_j) for its new span gain. GC532 gives r_j in {1,2}. Suppose

    tau_j/j -> d<infinity.

Necessarily d>=1. This is a hypothesis about the actual return process, not independence, an integrability theorem or existence of an invariant record law. It implies d_j/j->0 by subtracting the limits of tau_(j+1)/j and tau_j/j.

**Interior-excursion control.** For tau_j<N<tau_(j+1), no new record has occurred, so E_N=w_(tau_j) and w_N<=w_(tau_j). Since span can increase by at most 2 per update, recovery to the next record requires

    w_(tau_(j+1))-w_N<=2*(tau_(j+1)-N).

Thus 0<=Q_N=w_(tau_j)-w_N<=2*d_j. At a fresh endpoint Q_N=0. The finite spacing-mean assumption therefore gives Q_N/N->0 throughout time, without first assuming a speed exists. Also

    L_N-L_(tau_j)=(N-tau_j)+(w_(tau_j)-w_N),

so the interior displacement is nonnegative and at most 3*d_j. Since d_j=o(tau_j), interpolation from record times to every time has error o(N). This closes the terminal-deficit issue under an explicit return assumption, not unconditionally.

**Gain bounds from fair fresh choices.** Each fresh left choice returns immediately with span gain 2. Every other completed block has gain at least 1. With F_(tau_j)=j, this gives

    w_(tau_j)>=1+j+A_(tau_j), and w_(tau_j)<=1+2j.

GC510's two-sided moment bound gives A_N-F_N/2=o(N) on its global probability-one set. Under tau_j/j->d finite, applying it at tau_j shows A_(tau_j)/j->1/2. Consequently lower and upper mean span gains are at least 3/2 and at most 2. This use of the global set requires no fairness conditioned on the spacing hypothesis.

If in addition the actual record gain average converges,

    (r_0+...+r_(j-1))/j -> g,

then 3/2<=g<=2 almost surely under the hypotheses. Since L_(tau_j)=tau_j+1-w_(tau_j), and interior errors vanish, the limiting inward speed exists and equals

    v=g/d-1.

This is a conditional theorem. No value for d or g, nor their convergence, is proved here.

**What duration control alone gives.** Without gain convergence, the same interpolation and gain bounds yield

    liminf (-L_N/N)>=3/(2*d)-1;
    limsup (-L_N/N)<=2/d-1.

In particular d<3/2 would suffice for a positive lower inward rate, but would not alone establish speed existence. These bounds can be combined with GC510's unconditional upper inward-rate bound 1/2. They do not assert that such a small actual mean duration occurs.

**Independent endpoint controls and limits.** GC538's conditional all-K=0 case has d=1 and g=3/2, giving v=1/2. Its all-K=1 case has d=3/2 and g=2, giving v=1/3. These are conditional controls, not actual event probabilities. GC523's finite-record escape fails the infinite-record premise, so its outward speed cannot be inserted into the ratio. A large jump near the end of a short completed excursion cannot leave a linear deficit: the two-site-per-update recovery bound is the independent guard missing from a naive endpoint-only ratio.

**Outcome and next.** An iid renewal assumption is unnecessary if these two actual Cesaro averages can be justified. The open probabilistic work is now explicit: prove recurrent records, finite limiting mean duration, and limiting mean record gain from the full conditioned state. No such inputs, transport value or prize result are supplied. Stop accounting refinements; next an actual return-duration estimate or a justified induced-state law.

## GC541 — Healing return is a predictable deterministic excursion (2026-10-08)

**Scope and prediction.** Advance GC540's actual return-duration target using the exposure scheme itself. Predict that each fresh pivot chooses between two return outcomes specified by the pre-pivot state, because reused ticks reveal no new initial bits. Counterfactual this makes successive excursions iid or decides infinite return in finite computation is unsupported. Unexpected check: an infinite return-time predicate can be measurable before the pivot without being finitely decidable. Hand proof conditional on GC509, pending joint review; no experiment, return-tail estimate or novelty claim.

**Why no hidden bits enter the excursion.** At a fresh tick t, reveal the intervening bits through J_t+1. Force the remaining pivot to the unique value that makes the common below-front background black, namely the healed branch. Both copies' initial bits at that negative pivot are changed together, preserving their original single flip at site 0. The initial tail from J_t upward is then entirely specified. After this update the exposure boundary is B=J_t.

At every following reused tick, its cone endpoint J_s>=B. GC509's exact damage calculation therefore uses only the already specified initial tail and known damage history, and the boundary stays B. The next front and whether it creates a new record are determined from those bits. Iterate until the first fresh tick is detected, or indefinitely if none is detected. Unrevealed bits below B cannot affect any of these damage transitions before that return.

Consequently the healing branch has a return duration H_t in {1,2,...} union {infinity}, determined by the exposed pre-pivot information. Each finite-time no-return event is a function of that information; their countable intersection gives a measurable infinite-return predicate. This is not a finite decision procedure for that predicate. If return occurs, its span gain rho_t is 1 or 2 and is determined by the same branch simulation.

**Exact induced choice, not regeneration.** The actual fair fresh pivot selects, conditionally in equal proportions,

    (duration, span gain)=(1,2), or (H_t,rho_t),

where the second gain is defined only when H_t is finite. The first outcome is the left branch, which immediately creates a new record. If H_t is finite, the conditional mean duration is (1+H_t)/2 and its variance is (H_t-1)^2/4. Its conditional mean span gain is (2+rho_t)/2. If H_t is infinite, the conditional duration mean is infinite in the extended sense. All of these are state-dependent quantities; no iid rewards, integrability or convergence of their averages is supplied.

GC537-GC538 give H=1 for K=0 and H=2 for K=1. For K>=1, healing initially reduces span by K-1, and return must exceed its old record by at least one. The maximum two-site span growth gives H>=1+ceil(K/2). GC522 improves the K=2 case to H>=3, because its next update cannot move the front left. These are lower duration bounds, not upper recovery estimates.

**An exact recurrence obstruction identity.** Let C_t be the event that time t is fresh and its predictable healing table has H_t=infinity. The event is measured before revealing that pivot. Time t is the last fresh tick exactly when C_t occurs and the pivot chooses healing: its other choice returns immediately. Thus

    P(time t is the last fresh tick)=P(C_t)/2.

There is always a first fresh tick at time 0. The last-fresh events are disjoint, so countable additivity yields

    P(finitely many fresh ticks)=(1/2)*sum_(t>=0) P(C_t).

In particular the sum is at most 2. Almost-sure recurrence is equivalent to these infinite-healing tables having zero encounter probability at every deterministic t. This is a precise alternative target, not a proof that those probabilities vanish. It avoids conditioning pivot fairness on actual future escape: the deterministic counterfactual table is specified first.

**Independent controls and limits.** K=0 and K=1 reproduce the actual one- and two-update return blocks, including the forced unit reversal. GC523's last fresh tick at time 1 has a healed K=2 branch with no future records, so its deterministic finite-background table has H=infinity. That background requires an infinite zero half-row and is iid null; it supplies no positive P(C_t). The other fair-pivot branch would return in one update. These controls retain the actual transition and measure distinctions.

**Outcome and next.** The genuine missing input is now a property of predictable healing tables: exclude infinite excursions almost surely for recurrence, then control their durations and induced states for GC540's averages. No upper duration bound, zero-probability proof or speed theorem is established. Stop further accounting; next a full-state restriction on the deterministic healed excursion or a different open main-line lead.


### GC542 — Normal block statistics do not force hard indexing (2026-10-08)

**Lane and prediction.** Switch from the unresolved actual healed-return estimates to the owner's domino question for Problems 2 and 3. Predict that even binary normality, stronger than limiting balance and aperiodicity together, does not force linear indexed computation. Counterfactual: proving all fixed-block frequencies for the singleton would itself settle Problem 3. Independent controls are the band sum and exact boundary indices. Unexpected check: maximal fixed-block limiting empirical entropy still permits cheap exact random access. Hand algorithm audit and targeted primary reading; no experiment, no Rule 30 realization or novelty claim. Independent review pending.

**Known statistical example.** Let c be the infinite binary word obtained by concatenating the ordinary binary representations of positive integers, with no leading zeros: 1, 10, 11, 100, 101, ... . The primary chapter [Normal numbers and computer science](https://www.irif.fr/~carton/Enseignement/MPRI/Dynam-symbol/Documents/chapter.pdf), printed page 2, states that Champernowne's construction works in every integer base and is normal in that base; printed page 3 supplies the equivalent overlapping-block definition. We invoke this established result, not an independently proved normality theorem. Thus every length-h binary word has limiting frequency 2^(-h). In particular c is balanced and not eventually periodic. To check the latter implication independently, a period-p tail has at most p distinct length-h factors; for 2^h>p it omits a factor whose normal frequency would be positive. A finite prefix cannot repair the missing limiting frequency.

**Exact indexed algorithm, proved directly.** Number bits from n=1. The band of k-bit integers contains 2^(k-1) integers and k*2^(k-1) bits. Its cumulative endpoint is

    S_0=0; S_k=sum_(j=1)^k j*2^(j-1)=(k-1)*2^k+1.

The displayed identity follows by induction: adding (k+1)*2^k to S_k gives k*2^(k+1)+1. Choose the unique k with S_(k-1)<n<=S_k, set a=n-S_(k-1)-1, and divide a=q*k+r with 0<=r<k. Then 0<=q<2^(k-1), so the integer represented at that position is m=2^(k-1)+q. The requested bit is

    c(n)=(m >> (k-1-r)) & 1.

No earlier bits are generated. Scanning bands up to this k takes O(log(n+1)) iterations with O(log(n+1))-bit integers. Ordinary schoolbook arithmetic, including the final division, yields a conservative O((log(n+1))^3) bit-operation bound and O(log(n+1)) working space. This is o(n). It does not rely on unit-cost arithmetic of arbitrarily large integers.

**Hand controls.** S_1=1 and S_2=5: n=1 gives 1; positions 2 through 5 give 10 followed by 11. At n=S_k the algorithm selects q=2^(k-1)-1 and r=k-1, the last bit of 2^k-1, hence 1. At n=S_k+1 it selects the next band, q=r=0, the first bit of 2^k, also 1. Both endpoint conventions agree with direct concatenation. Outputting all first n bits still requires at least n bit writes; this output obligation is separate from computing one indexed bit. The source [Alvarez and Becher, Mathematics of Computation 86 (2017)](https://www-2.dc.uba.ar/staff/becher/papers/mcom3188.pdf), printed page 2930, likewise distinguishes independent-digit access from full-prefix generation for decimal Champernowne. Its elementary-operation count is not imported as a bit-cost bound.

**Domino consequence and open question.** This is a sequence-level separation, not a theorem about the singleton Rule 30 orbit. Even replacing Problem 2's balance target by full normality, together with Problem 1's nonperiodicity, cannot entail a general linear indexing lower bound. Nor do correct limiting block statistics imply algorithmic incompressibility or cryptographic unpredictability. A shared Rule 30 structural lemma could still resolve several prizes, possibly in opposite directions as GC518 illustrates; its computational consequence must be proved separately. The productive question remains: which specific, certified representation of the singleton trace admits a shortcut, or which bottleneck can be proved for a precisely defined algorithm class? The finite-state certificates GC487 and GC528 remain restricted lower bounds and do not supply that all-algorithm bottleneck. Statistical-to-time inference CLOSED; actual Rule 30 balance, normality and indexing complexity remain OPEN. Stop generic counterexample elaboration and return to a Rule 30 structural lead.


## GC543 — Fixed healing offset does not bound recovery duration (2026-10-08)

**Prediction and scope.** Return to actual GC541 tables. Predict that the single offset K=2 has unbounded possible healing durations, including on positive iid cylinders. Counterfactual a deterministic bound H<=f(K) exists for every encountered fresh table is false. Unexpected check: the table's defining cylinder omits the fresh pivot, because that pivot is forced in its counterfactual simulation. Independent controls are GC524's exact cycle characterization and GC532's span-record identity. Hand corollary conditional on those pending audits; no experiment, novelty, mean estimate or speed claim.

**Cylinder and fresh start.** In the original initial single-flip experiment at site 0, let A_n, n>=1, prescribe X_-1=1 and X_j=0 for 1<=j<=4n-1. All other bits, including X_0 and X_-2, are free. Under the original fair iid measure P(A_n)=2^(-4n). The first update then has damage exactly {0,1}, so at time 1 its front is 0 and span is 2. Time 0 exposed pivot -1; time 1 is fresh at pivot -2. These facts do not depend on X_-2.

Force this new pivot to 0 when constructing its healed table. GC524's exact characterization now applies from time 0: the forced pair has n complete displacement cycles (0,2). Its first time-1 healing jump is 2, so the pre-pivot offset K_1=2. Through rows 0 to 2n its span alternates 1,2, and after the time-1 record there is no further fresh tick through time 2n. Consequently the first possible next fresh tick is time 2n+1 or later. With GC541's duration convention (difference of consecutive fresh times), H_1>=2n on A_n, allowing H_1=infinity. Thus

    P(time 1 is fresh, K_1=2, H_1>=2n)>=2^(-4n).

This is an unconditional lower bound for a pre-pivot table encounter, not a claim that selected backgrounds remain iid. The cylinder contains only already exposed information at time 1: the nonnegative half and X_-1. Its freely varying X_-2 cannot change K_1 or H_1. The actual pivot chooses this healed table with probability one half; including X_-2=0 recovers GC524's original 2^(-(4n+1)) cylinder probability. Including X_-2=1 instead gives the immediate left-return branch.

**Controls and failure retained.** At n=1, K_1=2 and H_1>=2 match GC522's prohibition of immediate left return after a two-site jump. The n=2 cylinder forces rows through time 4 to have spans 1,2,1,2,1; this excludes fresh times 2,3,4 and gives H_1>=4, checking the endpoint count. The infinite intersection of these cylinders requires a zero positive half and has probability zero, just as GC523 warns. The exponentially decreasing lower bounds neither give positive infinite-duration probability nor force divergent expectation. They are not upper tail bounds.

**Outcome and next.** No finite deterministic duration cap based solely on healing offset can control the actual tables: K=2 has arbitrarily long durations with positive encounter probability. Any successful recurrence or speed argument must retain additional environment information or estimate a probabilistic duration tail; finite K or bounded mean K alone supplies no such estimate here. Offset-only deterministic recovery CLOSED. Actual almost-sure finite H and its mean remain OPEN. Stop elaborating the corridor; next a genuinely wider full-state estimate or another structural lead.


## GC544 — A one-tick black run can precede an arbitrarily long white run (2026-10-08)

**Lane and prediction.** Return to GC494's missing actual adjacent-run coupling. Predict that no finite universal function of a black run's duration bounds the next white duration over all finite Rule 30 seeds. This tests a concrete route, not another observed maximum-run census. Counterfactual this disproves such a selected-singleton bound is unsupported. Unexpected check: the first evolved row's nearest black distances are unequal, so GC496's first-arrival law is exact without a resonance tail. Hand proof and two independent algebraic controls; no experiment, external novelty or prize claim. Independent reading pending.

**Actual finite family.** For any integer m>=1, take initial black support every site in [-m,m] and zero outside. The centre is initially black, and its left neighbour is black, so its next value is 1 XOR (1 OR 1)=0. Thus the initial black run has length exactly 1, also agreeing with GC495's first checkerboard mismatch at depth 1. Applying Rule 30 to the entire row gives precisely

    support at time 1 = {-m-1, -m, m+1}.

Indeed site -m-1 sees 001 and becomes black; site -m sees 011 and becomes black. All sites -m+1 through m-1 see 111 and become white, site m sees 110 and becomes white, and site m+1 sees 100 and becomes black. More distant sites see 000. These disjoint endpoint and interior cases also work for m=1.

At the white-run start time 1, the nearest left black site is -m and the nearest right black site is m+1. GC496 therefore gives white duration exactly m: the centre is zero at physical times 1 through m, and black at time m+1. Its prefix is consequently

    1, followed by m zeros, followed by 1.

An independent finite-cone check uses the explicit time-1 support: before m additional updates neither extreme can reach the centre; at update m only the black bit at -m lies in the cone. Its leftmost XOR coefficient is 1, so it flips the zero-background centre to black. The right site m+1 and the farther left site -m-1 remain outside that cone. This reproduces the arrival and endpoint count without a probabilistic assumption.

**Controls and failed inference.** At m=1 the initial support {-1,0,1} evolves to {-2,-1,2}, giving centre samples 101 through time 2. At m=2 the time-1 support is {-3,-2,3}; the centre remains white for two samples before black at time 3, giving 1001. The family retains a finite nonzero seed for every m. Its support radius grows with m; there is no claim that these initial rows are reached at run starts of the singleton orbit.

Since the preceding black duration is always 1 and the following white duration is m, no finite bound w<=f(b) depending solely on b holds over all finite seeds. A uniform two-sided comparability of consecutive opposite-colour runs likewise fails. The first pair's signed black-minus-white length 1-m can be arbitrarily negative, but this is one initial pair in each different orbit, not an asymptotic discrepancy theorem. The linear dependence on seed radius agrees with known finite-support duration bounds. No singleton balance or imbalance is established.

**Outcome and next.** Universal local adjacent-duration coupling CLOSED. A viable GC494 proof must use additional information about the selected singleton's reachable run-start rows, or control cumulative signed residuals without pairwise comparability. Next identify a singleton-specific constraint on the run-start state; stop extending this finite-seed family.


## GC545 — A long white-start gap requires a preceding solid black block (2026-10-08)

**Prediction and scope.** Audit a reachable-row constraint at an actual black-to-white transition, after GC544 ruled out duration-only pairing. Predict an exact predecessor certificate for the new row's left gap and a necessary right-prefix condition. Counterfactual these identities give a singleton sublinear gap estimate is unsupported. Unexpected check: the right condition uses pairs of zero outputs and loses two sites, reflecting Rule 30's asymmetry. Hand Boolean proof, no experiment, novelty claim or new family. Independent reading pending.

Let u be the row at the last black tick of a centre run and v=F(u) the first white row. Then u_0=1 and v_0=0 force u_-1=1. Let ell>=1 be the contiguous black depth to the left: u_i=1 for -ell<=i<=0 and u_(-ell-1)=0. For finite rows ell exists. The first left black distance p in v is exactly ell. Indeed for -ell+1<=i<=0 the OR term is 1 and u_(i-1)=1, so v_i=0. At i=-ell the OR term is still 1 but u_(-ell-1)=0, so v_(-ell)=1. This gives the claimed first site independently of the right tail.

There is a complementary necessary condition on a right gap. Suppose v_1,...,v_(q-1) are zero, with q>=2. Then

    u_i=1 for 0<=i<=q-2;
    u_(q-1) OR u_q=1.

For the induction, if u_(i-1)=1 and v_i=v_(i+1)=0, the first equation requires u_i OR u_(i+1)=1. Were u_i=0, it would force u_(i+1)=1, making the second output v_(i+1)=1, a contradiction. Thus u_i=1. Apply this successively for i=1,...,q-2; the final zero output supplies the displayed OR. For q=2 there is no induction step and the final OR follows directly from v_1=0. No claim of an exact right distance from this necessary prefix alone.

In particular, at a white-run start whose nearest black distances both exceed or equal m>=2, the previous row contains a solid black interval at least [-m,m-2], of length 2m-1, and additionally u_(m-1) OR u_m=1. If p=m exactly, its preceding left boundary is white at -m-1. This is an actual transition constraint, valid also at selected singleton white starts, not a statement that all such predecessor blocks are reachable there. GC517's empty-gap delay min(p,q) is therefore at most ell; a sublinear bound on these preceding left solid blocks would suffice for that delay obligation only.

**Independent controls and limits.** GC544's solid interval [-m,m] has ell=m and evolves to p=m,q=m+1, saturating the left identity. For the singleton's first black-to-white transition, u has support {-1,0,1}; ell=1 and v has support {-2,-1,2}, so p=1,q=2 and the right endpoint OR is 1. The asymmetric endpoint allowance survives this smallest control. An infinite solid left half has no finite ell and evolves with no left black arrival; it is outside the finite-row hypothesis.

**Outcome and next.** Long white-start empty gaps cannot arise without long preceding black spatial blocks. This removes arbitrary white-row gap patterns from the transition analysis, but establishes no upper bound on these solid blocks along the singleton, no control of resonant post-arrival matches and no signed cumulative cancellation. Selected spatial-block growth remains OPEN. Stop certificate reformulation; the next useful input must actually constrain these predecessor blocks on the selected orbit, or change lead.


## GC546 — Exact right endpoint and resonance at a white start (2026-10-08)

**Scope and prediction.** Bounded proof audit of GC545's necessary-only right endpoint, not a new duration scan. Predict an exact formula with one exterior bit. Counterfactual the maximal preceding solid block alone determines resonance is false. Unexpected check: that single exterior bit can switch a nonresonant arrival to a tied arrival. Hand Boolean proof, no experiment, selected growth estimate or novelty claim; independent review pending.

Keep GC545's last-black row u and first-white row v. Let r>=0 be the largest right depth with u_0,...,u_r black, so u_(r+1)=0; let z=u_(r+2). Finite rows ensure r exists. For 1<=i<=r, the left input and the OR are both 1, hence v_i=0. At the next two sites,

    v_(r+1)=1 XOR z=1-z;
    v_(r+2)=z OR u_(r+3).

If z=0, the first of these is black, regardless of the second. If z=1, the first is white and the second is black. The new nearest right black distance therefore is exactly q=r+1+z. This includes r=0, where the interior range is empty. Combining with GC545 gives p=ell and

    m=min(ell,r+1+z);
    resonance iff ell=r+1+z.

Off resonance, GC496 gives the whole white duration exactly m. On resonance the separate GC513 post-arrival checkerboard tail is still required; this formula does not bound it. A resonant centre is necessarily displaced toward the right end of its preceding block: its left depth exceeds the right depth by exactly 1 or 2. This is a geometric restriction on any actual singleton transition too, with no frequency claim.

**Independent controls.** A solid interval [-m,m] has ell=r=m,z=0, hence p=m,q=m+1, recovering GC544. For support {-2,-1,0}, ell=2,r=0,z=0 yields p=2,q=1 and white duration 1. Add only site 2: the maximal centre solid block remains [-2,0], but z=1 gives p=q=2 and white duration at least 3. Direct one-step rows give the same distances: without the added site, v has support {-3,-2,1}; with it, support {-3,-2,2,3}. Thus a block-only resonance test fails on genuine finite rows, without claiming either is a singleton run-start row.

**Outcome and next.** GC545's two-site right allowance is now exact and both cases are realized. A selected-state argument must retain the exterior bit z as well as block geometry. No selected block-growth bound, tie frequency, post-arrival duration bound or signed cancellation is established. End this transition audit; next a different open lead unless a genuine singleton dynamical estimate becomes available.


## GC547 — Effective trace coordinates preserve prefix information, not runtime (2026-10-08)

**Lane and prediction.** Change from stalled selected run-growth estimates to a bounded algorithm audit of reviewed G130. Predict exact first-difference preservation and an effective polynomial prefix inverse at a fixed computable right tail. Counterfactual either a short description or this inverse settles Problem 3 is unsupported. Unexpected check: the actual singleton trace always has a short generating description, even if its fixed-block statistics are normal. Hand algorithm proof, no experiment, novelty claim or prize result; review pending.

**Exact first difference.** Fix the same initial right data at sites i>=0 for two rows. Write their negative input bits in order -1,-2,... . If their first differing input is at -d, G130's triangular formula says their centre samples agree through time d-1 and differ at time d. Conversely a first trace difference at d forces the first negative-input difference there. Thus the coordinate homeomorphism preserves the length of every common prefix exactly, not merely continuity. The fixed centre value at time 0 is omitted from both prefix counts. This does not assert preservation of Hamming distance: later samples may differ extensively.

**Effective finite-prefix algorithms.** Given the first N negative bits and right bits through N, simulate the finite backward cone to obtain centre times 1 through N in O(N^2) Boolean updates. For inverse construction, solve negative bits successively. At stage n, set the still-unknown bit at -n temporarily to zero, evolve its depth-n centre cone using the known higher bits, and XOR that tentative output with the desired trace bit. G130's coefficient 1 makes this the unique required input bit. This costs O(n^2) updates per stage and hence O(N^3) in total, with O(N) working cells and the input/output storage. These are conservative direct bounds, not optimality claims. Access to supplied right bits is included as input; if they come from a computable tail, its separate generation cost must be added.

**Description consequence for the actual seed.** A single fixed program can output the singleton's first N centre bits from N: initialize its known seed and run the finite cone. Encoding N in binary with a self-delimiting length header uses O(log(N+1)) bits. Hence there exists a generating description of that prefix of logarithmic length, regardless of balance, normality or indexed runtime. A claim that the singleton's prefixes require linear-length unrestricted descriptions would therefore be false. Runtime-limited descriptions are a different obligation and are not bounded by this observation.

**Independent controls and limits.** Changing only the first negative bit changes the next centre bit directly; changing the depth-d bit leaves earlier cones unchanged and flips the depth-d endpoint. Identical all-zero negative halves produce identical traces at any fixed right tail, checking uniqueness. A noncomputable fixed right tail would invalidate a uniform computability conclusion but not the supplied-prefix algorithms. The inverse outputs all N input bits and reads an entire trace prefix; it is not an algorithm reading only the indexed bit at N. Its cubic bound is no shortcut for Problem 3. The fixed-tail space is not preserved by Rule 30, so this coordinate identity is not a temporal conjugacy.

**Outcome and next.** The reviewed coordinate theorem is effective with explicit prefix costs, while information content and indexed work remain separate. Unrestricted incompressibility is CLOSED as a possible singleton complexity target. Actual indexed lower bounds require a specified resource model; the finite-state certificate lane stays restricted. Next audit an actual algorithm class or seek a structural identity; no prefix-size or trace census expansion.


## GC548 — Official Problem 3 wording contains distinct runtime targets (2026-10-08)

**Prediction and scope.** Audit the official target before proposing a restricted algorithm class. Predict that a displayed finite-limsup predicate excludes every O(n) algorithm, a different assertion from excluding sublinear algorithms. Counterfactual this supplies a shortcut or resolves a prize is unsupported. Unexpected check: an oscillating runtime separates an eventual linear lower bound from the absence of a sublinear algorithm. Primary-source reading and elementary quantifiers; no experiment, Rule 30 runtime bound or submission. Hand audit pending review.

**Primary text checked.** The current [prize page](https://rule30prize.org/) asks about a linear minimum for indexed centre-cell computation. Its linked [official announcement](https://writings.stephenwolfram.com/2019/10/announcing-the-rule-30-prizes/), sections Problem 3 and Formal Statements, discusses shortcuts below linear effort but displays a nonexistence predicate using finite limsup of effort divided by n. The same announcement considers a finite machine with the digits of n as input, and suggests total cell updates for a cellular-automaton cost model. It requires correctness for all indices. This reading reports a wording distinction; it does not assign an intended correction or reinterpret the committee's decision.

**Own quantifier audit.** Fix a uniform finite exact algorithm A, valid for every index, and write T_A(n) for its nonnegative finite runtime under a stated model. The following are distinct:

    (i) No exact A has T_A(n)=o(n).
    (ii) Every exact A has T_A(n)=Omega(n), eventually at all indices.
    (iii) No exact A has T_A(n)=O(n).

The displayed finite-limsup nonexistence predicate has meaning (iii): for each exact A, limsup T_A(n)/n is infinite. By contrast (i) only requires this limsup to be positive, possibly infinite. Statement (ii) requires a strictly positive liminf for each A. Thus (ii) implies (i), and (iii) implies (i), but the two stronger requirements differ from each other. All constants and thresholds may depend on the fixed algorithm. Choosing a different hardcoded machine separately for each n is outside this quantifier order.

**Independent runtime controls.** These are synthetic cost functions, not actual Rule 30 algorithms. T(n)=n is linear and eventually Omega(n), while its limsup ratio is finite; it separates a linear lower threshold from the no-O(n) predicate. T(n)=ceil(sqrt(n)) is sublinear, violating all three corresponding lower-bound demands. Let T(n)=n on powers of two and ceil(log2(n+1)) otherwise. Its limsup ratio is 1 and liminf ratio is 0: it is neither sublinear nor eventually Omega(n). Replacing its power-of-two values by n^2 gives infinite limsup but still zero liminf. These endpoint controls establish the stated logical distinctions without attributing any of these runtimes to the singleton.

**Outcome and next.** Future work must spell out whether it excludes o(n), excludes O(n), or proves an eventual Omega(n) bound, plus its machine and bit-cost conventions. A uniformly correct o(n) algorithm would contradict both the displayed formula and the prose shortcut target. An O(n) algorithm alone would contradict the displayed formula but need not contradict the prose linear-minimum question. No such algorithm is established here. The formal/prose distinction is retained for any candidate's verification; no contact or submission is made. Next choose a resource-specific restricted claim with these quantifiers explicit, rather than call finite-state or description bounds the full prize target.

