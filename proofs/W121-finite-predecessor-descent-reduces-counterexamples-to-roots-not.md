# Finite-predecessor descent reduces counterexamples to roots, not bounded width

*The waiting room (not yet verified). Derived from [PROOFS.md](../PROOFS.md), entry "G121. Finite-predecessor
descent reduces counterexamples to roots, not bounded width (2026-10-06)"; rebuild with `python3 proofs/build.py`.
Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** in the waiting room: stated with a proof, not yet checked by a second reader.

## In plain words

Walking a seed backwards in time shrinks it, but the walk stops at a "root", and roots come in every size.

**What it says.** A finite row has at most one finite row that produces it one tick earlier, and that earlier row is
two squares narrower. Walking back, every row reaches a unique starting row, its root. A counterexample stays a
counterexample as you walk it back, so the smallest counterexample would have to be a root. But three quarters of
all rows of every width are roots, and the single black square is one already.

**Why it matters.** It is the first attempt at the smallest-counterexample move of the owner's steer (chat CL005),
recorded as a failed bridge with the exact place it breaks: shrinking backwards cannot bound the size of a
counterexample. It has not yet had its second reading.

**An everyday picture.** Rewinding the film of a growing crystal back to its seed: every crystal has a seed, but
seeds come in every size, so rewinding alone cannot show that the crystal was small.

## The formal statement and proof

**Status:** paper proof and failed bridge, independent review pending. Responds to Cloud CL005's minimal-counterexample suggestion. No experiment or production run. This does not prove period-two exclusion or a prize result.

Let F be synchronous Rule30 on the infinite zero background. For a nonzero finite configuration x let [L,R] be its smallest support interval and w=R-L+1 its span, including internal zeroes. Its image has support endpoints exactly L-1,R+1:the outside adjacent triples are001 and100,both producing1,and all further outside triples are000. Therefore span(F(x))=w+2. This is an endpoint theorem,not a monotonicity theorem for the number of black cells.

F is injective on finite configurations. If two finite rows differ,let k be their rightmost differing site. Their values at k+1,k+2 agree,so their next values at k+1 differ:the left argument enters by XOR. Hence a finite row has at most one finite predecessor. If y has span w and a nonzero finite predecessor,that predecessor has span w-2. Iterating finite predecessors therefore terminates in a unique finite root r with no finite predecessor,and y=F^a(r) for a unique nonnegative age a. Its span is span(r)+2a. This is descent of ancestry,not descent along forward time.

Suppose a finite row is a counterexample to eventual-period-two exclusion at a fixed spatial column. Its finite predecessor,if present,is also a counterexample at that same column:the traces differ only by one initial time step. Thus every counterexample descends to a root counterexample,and a globally minimum-span counterexample must be a root. No phase assumption is needed because eventual alternation tolerates a time shift. Conversely,a root counterexample's forward images remain counterexamples. This gives an exact reduction to roots,without asserting any root is a counterexample.

**Where the bridge fails,for all widths.** Normalize support endpoints to0 and w-1,so for w>=2 there are2^(w-2) finite words. For w>=4 the images of normalized span-(w-2) words give exactly2^(w-4) distinct normalized span-w words,by endpoint growth and finite injectivity. Exactly one quarter have finite predecessors;the other three quarters,3*2^(w-4),are roots. For w=3 the sole image is111 from1;101 is a root. The span-one and span-two words are roots. In particular roots exist at every width. The predecessor reduction supplies no upper bound on a minimal counterexample's width and no induction step that covers the roots. The selected single-black-cell seed is already a root.

**Unexpected scope check,by hand.** The counterfactual "left permutivity gives a finite predecessor for every finite row" fails already on a single black cell:every nonzero finite image has span at least3,and the zero row maps to zero. Yet every finite output block has a compatible longer input block by right-to-left inversion (G104);compactness gives global predecessors. Such predecessors of this root must have infinite support. So full-shift surjectivity cannot supply the missing finite descent. This distinction is standard cellular-automaton background:see Jarkko Kari's [Cellular Automata tutorial](https://users.utu.fi/jkari/wp-content/uploads/sites/1251/2023/12/CAintro.pdf),slides89-100,on finite injectivity versus finite surjectivity and infinite predecessors. No novelty claim for finite injectivity;the present application identifies the precise failure of this proposed bridge.

**Next proof obligation.** A minimal-counterexample argument needs a different transformation that preserves eventual alternation while shrinking a root,or a theorem excluding every root. Removing an endpoint by hand has no established trace-preservation property:its causal cone eventually reaches any fixed observation column,so finite propagation alone guarantees no forever equality. The root count is not evidence of period-two survival. Ordinary inverse-time descent alone is closed as a complete proof route;other shrinking transformations remain open.
