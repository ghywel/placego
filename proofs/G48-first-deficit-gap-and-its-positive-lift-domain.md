# First-deficit gap and its positive-lift domain

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT48. First-deficit gap and its
positive-lift domain"; rebuild with `python3 proofs/build.py`. Edit the proof in PROOFS.md and this summary in
[summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

A simple formula for how far above or below its start a number ends after its first dip.

**What it says.** For any pattern whose growth factor first drops below 1 at its last step, the gap between end and
start is a fixed number minus a fixed multiple of how far the start sits up its class. A gap of zero is a return to
the start; a positive gap means it ended higher.

**Why it matters.** It turns survival through a first dip into a short, exact calculation, which G48's certificate
(next page) then carries out.

**An everyday picture.** A prepayment electricity meter: the credit left is the top-up minus a fixed price per unit
used, so whether you are still in credit at the end is a single subtraction.

## The formal statement and proof

**Where:** RULE30-GPT.md G48, 2026-10-06; copied verbatim. **Bears on:** PERIOD-TWO.md §7 question9. **Status:** short derived affine identity, second-read by Local, 2026-10-06 (note below the certificate). G47 controls passed.

### G48 audit identity: the first-deficit gap

For a first-deficit word of lengtht, all proper nonempty prefixes have coefficient above1 and the final coefficient A/2^t, A=3^a, is below1. Let D=2^t-A, let r be its realizing residue in[0,2^t), and q its terminal value. Set g=q-r, an integer. For a start n=r+2^t*m, the affine lift identity gives

    n_t-n = g-D*m.

Since every proper prefix already stays above any positive start by its coefficient, actual survival through this word is exactly m>=m_min and g-D*m>=0, where m_min=0 if r>0 and1 if r=0. Thus surviving positive lifts have m_min<=m<=floor(g/D). Gap0 at a surviving lift is a periodic return; positive gap is a strictly higher terminal state. A formal g=0 at r=0 does not supply a positive survivor, since m_min=1. The word0 gives that necessary domain control: r=q=0, but all positive realizing starts descend immediately.

This is a derived form of G45 and the known affine lift lemma, not a new stopping-time estimate. In particular general interleaved words have not been shown to satisfy g<=0; G47's single-run congruence proof cannot silently be extended to them.
