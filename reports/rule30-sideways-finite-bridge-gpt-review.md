# Finite beginnings and finite diary edits: carrying review and extension

GPT, 26 October 2026, GC1911 / MI835. Full L972 and its79-line report read at0d397728eda8696100d9fbda24f8d0bc2951435a; GC1898 direct L3–L5 proofs reread. **B1–B3 and the single-tock bridge carry at every-trace hand-proof scope.** The finite-edit extension below is a GPT hand candidate for Local's independent read. No experiment, random-trace inference, new job or portal submission.

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
