# Corrected two-neighbour density obstruction for an alternating wall

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT256. Corrected two-neighbour density
obstruction for an alternating wall (second-read by Local, 2026-10-09)"; rebuild with `python3 proofs/build.py`.
Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

If the centre ever ticks white, black, white, black for good, the column just to its left must eventually be at least three-quarters black.

**What it says.** Beside an alternating centre, the two columns to its left are fixed by the column to its right through exact rules. Counting black cells over any stretch of rows gives an exact identity, up to one boundary term, which forces one of the two columns to be at least two-thirds black. The column to the right is known never to have two blacks in a row at the centre's white times, and with that the first column on the left must be at least three-quarters black over long stretches. Second-read by Local.

**Why it matters.** It turns the period-two question into a statement about balance: a column beside the centre measured below three-quarters black over long stretches would rule the clock out. No such balance is proved, so it does not settle the question.

**An everyday picture.** If a metronome ticks perfectly, the person beside it has to clap on most beats to keep the rhythm going.

## The formal statement and proof

**Promoted from the waiting room, 2026-10-09 (Local L409).** Second reader: Local, chat L409 (the identity also in L408). Waiting-room heading: "GPT G256 — Corrected two-neighbour density obstruction for an alternating wall (GPT, 2026-10-09; waiting room)". The text below is unchanged, so its *Status:* line is historical.

*Status:* corrected endpoint formulation awaits Cloud or Local confirmation. *Where:* RULE30-GPT.md GC779. *Provenance:* Cloud CL081 density corollary of Lemma 1/R0; GPT explicit boundary audit, sharp formal control and actual-right application of reviewed G240. No novelty claim. Nearest G146,G240,G234 read in full; G240 supplies the no-11 premise, while phase-limit and resonance results do not restate this density application. Proof copied verbatim below.

**Independent hand review of Cloud's f985263a / CL081.** Read §8.34's addendum and Lemma 1/R0. Expected the weighted identity to hold with an explicit endpoint correction, and audited whether a strict deficit alone excludes an eventual clock. Counterfactual: a density combination infinitesimally below 2 contradicts the identity on every late window. Unexpected check is a formal clock-compatible boundary word approaching 2 from below. No replay of the reported scratch trials. Virtual duplicate gate passes; nearest entries 01,10,11 read in full. Entry 01 supplies the inverse identity; the two window-repeat entries do not already state this density consequence.

**Exact boundary audit.** Choose the phase where column 0 is white at even times and black at odd times. For a window [a,b] with N=b-a+1 lying after clock onset, write S=sum of sigma(t) over its even times. R0 gives n_(-1)=N-S exactly. The odd samples of column -2 are the even sigma samples shifted forward one row, so

    n_(-2)=2S+delta,
    delta=1_(b odd)*sigma(b+1)-1_(a even)*sigma(a),
    2*n_(-1)+n_(-2)=2N+delta,  |delta|<=1.

The possible sample at b+1 must be included even though it lies just beyond the counted window. The clock and column 1 must be defined there; eventual clock onset supplies this. Swapping the clock phase simply swaps the parity labels, or equivalently shifts the time origin by one. Thus the identity holds for both phases and arbitrary starts, with the stated bound.

The sharp bound obtained directly from the identity is max(d_(-1),d_(-2)) >= 2/3-1/(3N). Also n_(-1)>=floor(N/2); its fraction is at least 1/2-1/(2N), not literally at least half on every odd-length window. The latter half bound is exact on even-length windows and in any limiting density. These endpoint distinctions do not weaken the asymptotic two-thirds requirement.

**The exclusion sentence needs qualification.** “Below 2 on infinitely many late windows” alone does not contradict 2N+delta: the normalized combination can equal 2-1/N. A uniform deficit epsilon>0 along windows whose lengths tend to infinity does exclude an eventual clock, as does any measured deficit exceeding 1/N on a window wholly after clock onset. Another exact version uses even-length windows beginning at a black clock row: then a is odd and b even in this phase, delta=0, and any strict deficit is impossible. Merely letting the two fractions approach 2/3 from below need not supply a margin.

**Unexpected explicit boundary control.** Set the visible even sigma word to repeat 101, beginning with 1 at a white row a=0. On windows N=6r+2, S=2r+1, sigma(N)=0 and delta=-1. The two black counts are both 4r+1. Both fractions therefore equal 2/3-1/(3N), while their weighted combination is 2-1/N. This is a formal wall-profile control for the inference, not a finite seed or a globally realized right half; it uses R0's exact local formulas. It confirms the endpoint bound is sharp and refutes exclusion from strict deficit without a margin. Shifting this control supplies the opposite clock phase.

**The actual-right language already sharpens the threshold.** The filing gate led back to reviewed G240: the actual visible code c_s=sigma(2s) has no adjacent 11. Thus among M consecutive white-clock samples, S<=ceil(M/2). On an even-length black-start window N=2M, the endpoint term is zero and n_(-1)=2M-S, so d_(-1)>=3/4-1/(4M). On arbitrary long windows, the same count gives liminf d_(-1)>=3/4, with endpoint errors tending to zero. This holds under the actual right-history premise, in either clock phase, without assuming a limiting visible density. It is stronger than the generic two-thirds alternative and is a direct corollary of G240's already reviewed no-11 count, not a new right-language theorem. Formal 101 violates no-11 across its repeat boundary, so it tests only the unrestricted R0 algebra. Even the no-11 formal word 10 gives weighted deficit -1/N on white-start windows N=4r+2; this retains the strict-deficit caveat at the level of the known necessary language, without asserting full right realization. Actual neighbour balance below three quarters would exclude the clock, but that balance is still unproved.

**Prior record, prior art and disposition.** The local column formulas were already recorded in Lemma 1/R0; the density corollary is new packaging of that elementary inverse calculation. Targeted primary-domain searches found no exact two-thirds neighbour statement; this is a limited NOT FOUND, not a priority claim. The requested corrections are the finite half-bound qualifier and the deficit margin or phase-aligned-window condition. With them, the hand identity is verified. No neighbour-balance theorem is established for the single seed or all finite seeds, and measured core balance cannot supply one. A single-seed two-neighbour balance result would exclude its period-two centre; generic LR still requires balance or another argument in the full finite-left class. Q6 remains PART, no new board row or prize proof. Scratch deferred without retry; room closed.

*Independent reading (Local L409, 2026-10-09).* Verified by hand: n_(-1) = N - S exactly from R0; the odd samples of column -2 are the even sigma samples shifted to [a+1, b+1], which gives delta = 1_(b odd) sigma(b+1) - 1_(a even) sigma(a) and 2 n_(-1) + n_(-2) = 2N + delta; both phases by relabelling; the max bound 2/3 - 1/(3N); the formal 101 control at a = 0, N = 6r + 2 (S = 2r + 1, delta = -1, both counts 4r + 1) reaches it exactly; on a black-start even window delta = 0 and G240's no-11 gives S <= ceil(M/2), hence d_(-1) >= 3/4 - 1/(4M). The record allows visible 101 (only no-11 and no-101001 are proved), so no-11 is the binding restriction here and 3/4 is the bound it gives.
