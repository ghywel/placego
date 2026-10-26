# Finite beginnings and finite diary edits: carrying review and extension

GPT, 26 October 2026, GC1911 / MI835. Full L972 and its79-line report read at0d397728eda8696100d9fbda24f8d0bc2951435a; GC1898 direct L3–L5 proofs reread. **B1–B3 and the single-tock bridge carry at every-trace hand-proof scope.** The finite-edit extension was independently carried by Local L974 at060762a082c2e4c0d55bf9de07520f27f2d4a7c4 and is adopted at every-trace scope in GC1912. **Latest: section5 carries L973 and closes shortening by ANY finite trace edit; the earlier question is retained as the hypothesis tested in this block.** No experiment, random-trace inference, new job or portal submission.

## Question → response → challenge → better question

Does changing a tock produce another finite beginning? Local's proof gives an exact finite test. The disagreement must disappear before it gets beyond the original beginning's expanding white edge. Otherwise that white region traps it forever. This is the first bridge in this exchange that directly uses the finite beginning, rather than a typical random diary.

It does not guarantee that any change succeeds, or that a successful change shortens the beginning. “One survivor forces more” remains conditional on finding an edit that passes the test. A width upper bound that grows with the edit time does not prove that every partner is wider.

The better question is whether **several coordinated changes can succeed where one change fails**, and whether the resulting finite beginning can be shorter. The same white-edge proof appears to test any fixed finite bundle of changes. We have not established that suitable bundles exist for a hypothetical eternal survivor.

## 1. Carrying read of L972

Write c_0(t)=0 and c_(d+1)(t)=c_d(t+1) XOR (c_d(t) OR c_(d-1)(t)). Rearranging gives the actual forward local update for every d>=1. Thus the reconstruction evolves from F_d=c_d(0) with the zero wall; no compatibility with an unspecified exterior is being assumed. A row starting with support<=W has support<=W+t at time t.

For one trace flip at tau, induction on d gives delta_d(t)=0 for t>tau, so every live pair has an integer height0<=H_d<=tau. The top cannot rise, and an empty pair stays empty. B1 is exactly the floor identity.

At a live column d>W+H_d+2, both the input c_(d-1)(H_d+1) and the cell c_d(H_d) are zero by that support bound. State01 would force c_d(H_d)=1 XOR s=1, by the direct two-copy OR argument of GC1898, contradicting zero. The remaining states11 and10 keep the height:11 stays11 when s=0, and10 becomes11. The support inequality remains true at the next column, so induction locks11 at the same height forever. This checks B2 and B2′ without an ancestry assumption.

At that fixed height, the original row is eventually white and delta is1 at every sufficiently distant column. The modified row there is therefore eventually black. A finite modified beginning would have finite rows at each fixed time, contradiction. This checks B3. It is not necessary, or generally true, that its time-zero row is eventually black.

Set D=W+tau+2. If the pair is live at D+1, then D+1>W+H_(D+1)+2, and the locked case applies. Therefore the precise bounded criterion is

    F' finite  iff  (delta_(D+1), delta_D) is the empty pair.

Equivalently its last live column is at most D. A finite last live column also satisfies d<=W+H_d+2; otherwise it would lock. By the floor identity the changed cells are bounded by D (a harmless loose endpoint), and by triangular reconstruction no cell before tau+1 changes. This verifies the stated interval[tau+1,D].

To implement the empty-pair criterion by direct reconstruction, it suffices to use levels0..tau and columns through D+1, knowing higher differences vanish. A safe explicit trace prefix ends at tau+D=W+2tau+2, since c_d(t) depends only on a_t,...,a_(t+d-1). Thus “about W+2tau” can be replaced by this concrete safe endpoint. No run is authorized by identifying it.

## 2. Finite bundles use the same mechanism — HAND candidate

Let a' differ from a on any nonempty finite set S of times, and put tau=max S. Assume F is finite of support<=W. The same theorem holds with D=W+tau+2:

    F' finite  iff  the difference pair is empty at column D+1.

Proof: induction still gives delta_d(t)=0 for all t>tau. Nothing in the proof of top nonincrease, the direct L3–L5 cases or the white-region contradiction uses there being exactly one changed trace bit. Hence the preceding carrying argument applies without alteration after the initial bound H<=tau. Empty pairs remain empty; live pairs at D+1 lock and force an infinite modified row. The unchanged prefix before min S gives the same safe reconstruction bound W+2tau+2. If S contains only odd times, every even trace entry is preserved, so a finite partner of an eternal survivor is again an eternal survivor. No existence or abundance follows.

This is a generalization of Local's argument, not a stochastic result and not a claim of novelty against external literature. Record searched: finite.{0,60}(trace edit|tock flip|flipped tock) returned4 hits in3 files, all the present L972 discussion/index; earlier GC1898 triangularity and GC1894 window results were also consulted. The search is not a proof of absence of prior art.

## 3. Two useful guards, by hand

**A genuinely late first change cannot shorten.** Let mu=min S. The known leading-bit formula is c_d(0)=a_(d-1) XOR a function of earlier trace bits. Thus F'_d=F_d for d<=mu and F'_(mu+1)=1 XOR F_(mu+1). If mu>=W, this puts a black cell at mu+1>W. Any finite partner is then strictly wider. For a single tock flip, a narrower partner necessarily has tau<W. For a bundle, the necessary condition is min S<W; later coordinated flips are not excluded. This is stronger and more precise than inferring widening from an upper bound.

**Unexpected control: a remembered tock need not make the floor all black.** Take F=0, so a=0, and flip only tau=1. The reconstructed modified rows are zero for t>=2 and all1 at t=1,d>=1: the latter follows from c'_(d+1)(1)=c'_d(1) OR c'_(d-1)(1), with boundary0 and c'_1(1)=1. At time0, F'_0=F'_1=0 and

    F'_(d+1)=1 XOR (F'_d OR F'_(d-1)).

The pairs00 -> 01 -> 10 -> 00 give F'_d=1 exactly when d=2 modulo3. This infinite beginning really has the single-pulse trace. It exhibits Local's locked upper row, while the floor is periodic rather than all black. This checks the non-vacuous infinite branch without a solver or simulation. It is a boundary control, not an eternal-survivor example: its even trace is white.

## 4. What changed and what is next

L972's conditional finite-partner test is now independently carried. Please have Local read the finite-bundle extension and the earliest-edit guard above; they use the same mechanism and need no separate computation. A hypothetical minimal survivor would have to resist every finite odd-time edit that cancels its exterior without creating a new one. The theorem decides each fixed edit in finite time, but does not bound the edit times needed to find one or prove one exists. That is the missing coverage step, not an achieved infinite-to-finite reduction.

Gut verdict: warmer on this deterministic bridge than on another fitted memory table. Reasoned verdict: an actual conditional reduction gained; the reduction's successful-edit existence hypothesis remains open. Continue the hand question while Local repairs the already-proposed SAT launcher; no new experimental lane.


## 5. L973 arrives during the review: finite edits preserve actual width

Full L973/addendum read at88e8dbfe30810fccd8706e4086bb42f14e0b7c86. **B0 and B4 carry**, with W the actual deepest black cell of a nonempty finite start. GC1894's targeted twins review already states the same edge-speed invariant for exact in-step mergers; this is its application to edited traces, not a novel edge theorem.

The scope immediately includes the finite bundles of section2. If S is finite and tau=max S, then a'=a at all times>=tau+1. Since c_d(t) depends only on a_t,...,a_(t+d-1), the ENTIRE rows coincide at time tau+1, regardless of what their time-zero supports are. If both starts are finite and nonempty, their actual widths at that time are W+tau+1 and W'+tau+1. The outermost black cell advances exactly one place per step: at the next cell beyond it the other two inputs are white, and all still farther cells remain white. Equal rows therefore force W'=W.

Empty-start guard: zero stays zero, whereas a nonempty finite start has a black edge forever. Thus a zero/nonzero finite pair cannot have equal later rows either. If the trace edit is nonempty, both starts cannot be zero. The pulse control above is consistent: its partner is infinite.

**Consequence: no finite collection of trace changes can shorten one finite start to another.** This closes the section2 shortening suggestion, not just Local's one-flip suggestion. For a finite partner, the difference is confined to[min S+1,W]. In particular min S>=W is impossible for any nonempty finite edit, rather than merely forcing a wider partner. That strengthens section3's conditional earliest-edit guard. A single tock tau>=W is never forgotten sideways for a finite start, by the already-carried bridge.

For a free single flip in a width-W lane, the claimed link to L955 carries in its exact sense: there is a unique finite candidate obtained by reconstructing its first W trace entries and appending zeros. It is the desired partner exactly when its full trace has the single specified difference; then the rows already agree at tau+1. GC1894 supplies the finite comparison window (tau=2j+1, W=2n): beyond the known free chapter compare [W,W+4j+3]. Do not replace this by “inspect only W outward columns”: B4 bounds the SUPPORT of a finite partner, not by itself the observation horizon of the finiteness test. Actual support endpoint and a lane's padded width are also distinct.

The candidate finite-bundle white-edge criterion still stands and needs Local's read; it may classify same-width partners. Its proposed use for decreasing width is now CLOSED. No new census should be designed to look for shorter finite partners from finitely many diary edits: this invariant already forbids them. We need a transformation that preserves the required ticks while changing an unbounded set of later tocks, or a different measure of simplification that does not pretend to decrease support. That is a sharper open question, not a new launch or a solved reduction.

Reasoned verdict after the new evidence: L972/L973 carried; finite-edit shortening ruled out by the existing edge invariant and tail reconstruction. Gut verdict: the finite test remains useful, but its tempting descent application is closed. Retain this boundary before another compression experiment is proposed.


## 6. GC1912: how sparse could an infinite edit be? A planning consequence of the known window

L974 carries the finite-bundle criterion, earliest-edit guard and pulse control. No pending dependence remains there. The next question is what an unbounded edit would have to change. This paragraph applies GC1894's existing reconstruction window and GC1886's edge speed; it is a hand planning guard, not a new prize result or separate review request.

Let two nonempty finite starts have different actual widths, and let W be the larger width. At any time s, both rows are supported within W+s. If their watched diaries agreed on the whole interval

    [s, 2s+W−1],

the first W+s observations at time s would reconstruct equal full rows, contradicting their unequal outer edges. Thus every such interval contains a diary difference. If both starts pass all required ticks, that difference must be a tock. No survivor existence is assumed.

Disjoint windows starting at s_n=W(2^n−1) therefore each require a changed entry. Among times0,...,T−1 there are at least floor(log2(1+T/W)) changes. This lower bound need not be sharp and proves no positive-density requirement: it only excludes edit schedules that leave one of these growing windows completely unchanged. Equal-width merged twins are the unexpected countercontrol—those diaries can agree forever after merging, so the different-actual-width hypothesis cannot be dropped.

A simple retiming does not evade the edge invariant for free. If a'(t)=a(t+k) for all sufficiently large t (take t+k>=0), the rows at times t and t+k coincide by reconstruction. Their widths give W'=W+k. Looking later in the old diary makes the new finite beginning wider. Looking earlier requires an earlier/ancestor-type replacement, with even k needed for automatic preservation of the tick phase. This returns to the existing ancestor/merger question, rather than providing a new shortening construction.

The unresolved task is to name an actual support-reducing operation that keeps all ticks and supplies the required endless changed tocks. Neither the logarithmic necessary bound nor tail retiming supplies that operation. No new experiment or prior-art novelty claim; record search for trace agreement/common-block/shifted-tail wording had no hit, while the broader row-recovery search returned the GC1894 source used here. Exact sources were read, not replaced by the search result.
