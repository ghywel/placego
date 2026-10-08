# four shaped precursors of an open white block

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT211. four shaped precursors of an
open white block (second-read by Local, 2026-10-08)"; rebuild with `python3 proofs/build.py`. Edit the proof in
PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

A white block has four possible preceding patterns, with variation only at one end.

**What it says.** If Rule30 produces L consecutive white cells, the L+2 cells feeding that update are either all white or have L black cells followed by01,10 or11. Those are exactly the four possibilities, regardless of cells outside the interval.

**Why it matters.** It identifies the shape of an actual white block's previous row. It preserves the exceptions at the right boundary that a constant-row shortcut would lose. An arbitrary initial row need not have a finite predecessor, so this alone cannot strengthen the initial-row record search.

**An everyday picture.** A row of lights can go dark through four switch arrangements. Three arrangements look the same along most of the row but differ at the end; that small difference matters when the row has an open boundary.

## The formal statement and proof

**Where:** RULE30-GPT.md GC409 at9c2aac9, statement/proof/controls copied verbatim below. Local L248 at495f2ab checked necessity, sufficiency and L=1; its alternative derivation uses left permutivity and the two right boundary inputs. This is a finite open-interval specialization of the existing preimage method, without a novelty claim.

**Claim.** L consecutive zero outputs of synchronous Rule30 have exactly four input words on their L+2-cell backward interval:

    0^(L+2), 1^L01, 1^(L+1)0, 1^(L+2).

**Proof.** Index the old input0..L+1 and new zero outputs1..L. Each equation is x_(j-1)=x_j OR x_(j+1). If x0=0, the first equation gives x1=x2=0; induction gives every input zero. If x0=1 and a first zero occurs at i<L, then i>=1 and equation j=i+1 forces x_(i+1)=0; equation j=i now says x_(i-1)=0, contradicting its being1. Thus x0..x_(L-1) are all1. The remaining equation j=L requires(x_L OR x_(L+1))=1, giving terminal pairs01,10,11. Every listed word satisfies every equation, proving necessity and sufficiency for all L>=1.

Preregistered controls L1..8 inspect2040 inputs, scalar XOR-OR versus independent decoded Rule30 truth table: exactly4 precursors at each length. Unexpected endpoint guard retains both nonconstant terminal patterns. A claim that the entire precursor interval is constant would be false: the last two cells are essential open-boundary exceptions.

**Scope guard.** The zero block must be an output of an actual Rule30 update for this precursor description to apply to a particular previous row. RR's free time0 block does not justify a finite-support predecessor premise. Allfour unrestricted branches supply no new initial-row obstruction; G121's finite-root failure remains. No cofinal zero-run bound or prize conclusion.

**Duplicate guard for G211:** actual nearest G202,G209,G201 read in full. Their temporal overlap balance, four-update output patterns and post-split sibling support do not state this finite one-update precursor shape. G105's whole-ring count and G104's general right-to-left inversion are cited methods, not new count claims; the open-boundary terminal exceptions are the statement filed here.
