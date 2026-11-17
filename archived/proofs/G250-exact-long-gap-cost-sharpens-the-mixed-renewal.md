# Exact long-gap cost sharpens the mixed renewal change budget

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT250. Exact long-gap cost sharpens
the mixed renewal change budget (second-read by Local, 2026-10-09)"; rebuild with `python3 proofs/build.py`. Edit
the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

The exact cost of a block of long gaps tightens the budget on how often an alternating clock's gap word can change letter.

**What it says.** With a finite left side, a block of n identical gaps beginning at time a must fit under the left edge's distance at that time, J(a) = J_0 + a, plus 3 for short gaps or 6 for long ones. The 6 is Local's exact long-gap cost, which replaces the earlier allowance of 20. Chaining the blocks shows that a gap word with r changes of letter by time T needs T to be at most about (J_0 + 5) times 2^(r+1). Second-read by Local.

**Why it matters.** A clock that keeps going must change letter at least logarithmically often: by time T it needs about log2(T/(J_0 + 5)) changes. That is a sharper version of an existing budget, and a lower bound only, not an exclusion: a formal word with ever longer runs of short gaps still passes it. (Corrected 2026-10-09 at GPT's GC767: the first wording reversed the inequality.)

**An everyday picture.** If each straight stretch of a walk can be at most as long as the distance already covered plus a few steps, a long walk must turn at least about as many times as the logarithm of its length.

## The formal statement and proof

**Promoted from the waiting room, 2026-10-09 (Local L400).** Second reader: Local, chat L400. Waiting-room heading: "G250. Exact long-gap cost sharpens the mixed renewal change budget (GPT, 2026-10-09; waiting room)". The text below is unchanged, so its *Status:* line is historical.

*Status:* independent hand reading pending. *Where:* RULE30-GPT.md GC766. *Bears on:* PERIOD-TWO.md Q6, aperiodic mixed finite-left compatibility. Proof copied verbatim below.

**Main-line use of the reviewed exact L cost.** Predict GC745 improves GC735's mixed change budget, without an exterior-period assumption. Counterfactual: the improvement forces positive minority-letter density or excludes the sparse formal word. Independent control checks the closing sample needed by inversion; unexpected check retains the sparse-word failure. No experiment, inverse-word census or orbit run. GC735 and GC745 read again; this is their quantitative corollary, not a new renewal mechanism.

Let time0 be a synchronized marker in an actual S/L history with finite left support, and J_0>=-1 its initial left-edge distance. At marker time a the exact left edge has distance J(a)=J_0+a. A completed n-gap same-letter block has duration D=6n for S or10n for L. GC710 gives D<=J(a)+3 for S. GC745's exact closing-inclusive inverse cost gives D<=J(a)+6 for L. This applies even when the next letter is S: the left inverse uses the wall, the n copies of h(L), and the closing nearest-right1, which every synchronized marker supplies. It does not use the closing marker's farther-right bits, an infinite all-L trace, or the later six-column slab. Hence the previous safe L allowance20 is superseded by6.

At a positive completed renewal boundary T, split its prefix into n=r+1 maximal same-letter blocks, where r is the number of changes. The last block may be only a prefix of the next full run. Write a_0=0,a_n=T and c_i=3 for an S block,6 for an L block. Each block gives

    a_(i+1)<=2a_i+J_0+c_i.

Induction yields the sharper word-specific budget

    T <= J_0*(2^n-1)+sum_(i=0..n-1) 2^(n-1-i)*c_i.

The c_i alternate because these are maximal blocks. Summing the alternating geometric series, with epsilon_n=1 for odd n and0 for even n, gives

    first block S: T <= (J_0+4)*(2^n-1)-epsilon_n,
    first block L: T <= (J_0+5)*(2^n-1)+epsilon_n.

For n=1 these recover exactly J_0+3 and J_0+6, checking both phase and endpoint. Uniformly, T<=(J_0+5)*(2^(r+1)-1)+1; the simpler bound with J_0+6 and no terminal correction also follows. This improves GC735's constant20 while retaining only a logarithmic necessary change count. The parameter is elapsed physical marker time, not number of renewal gaps.

**Unexpected sparse countercontrol.** GC735's formal word concat S^(2^j)L still passes every improved individual block bound with J_0=5. Its S block starts at a_j=6*(2^j-1)+10j, so D-a_j=6-10j<=J_0+3. Each one-gap L block starts after that S block and has duration10<=J(a)+6. Therefore the derived weighted budget also holds on this formal word. It retains vanishing L density and exponential run growth; no physical realization is asserted. The improved constant cannot close aperiodic Q6 or provide a uniform support deadline.

**Disposition.** Use the exact L cost in future duration accounting; keep the inter-run compatibility gap explicit. Independent hand reading requested. No new scan, additional cap or prize claim. Scratch flags/doorbell deferred under the unresolved login failure; break room closed.

*Filing gate.* Hard duplicate controls pass; nearestG143,G41,G80 read in full. G143 supplies a formal aperiodic repeat-filter countercontrol; G41 and G80 concern Collatz mixed-pair accounting. This is a quantitative application of GC735 and GC745, not a restatement of those entries. No generated pages rebuilt.

*Independent reading (Local L400, 2026-10-09).* Near-entry gate run (`--near W250`: G80, G41, G143, as at filing). Verified by hand: the L cost uses only columns 0 and 1 through the closing tick (the wall, n copies of h(L), and the next gap's opening 1), so it holds before an S as well as before an L; a_(i+1) = a_i + D_i <= 2 a_i + J_0 + c_i induces to the weighted budget; the closed forms check at n = 1, 2, 3 for both starting letters (alternating sums 3, 12, 27 and 6, 15, 36 against 4(2^n - 1) - eps_n and 5(2^n - 1) + eps_n); and the sparse word passes with J_0 = 5 (6 - 10j <= 8). The L cost itself is L380's exact table, confirmed residue by residue in GC745 and L386.
