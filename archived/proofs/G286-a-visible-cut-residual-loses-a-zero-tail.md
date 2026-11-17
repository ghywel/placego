# A visible cut residual loses a zero-tail clock charge

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT286. A visible cut residual loses a
zero-tail clock charge (second-read by Local, 2026-10-13)"; rebuild with `python3 proofs/build.py`. Edit the proof
in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

Recent signals at the wall, the starting beat and the remainder of the white tail's depth after dividing by 28
cannot always tell whether the next black beat holds.

**What it says.** Picture the centre column forced to blink black, white, black, white: the wall. A black beat holds
only if the square to the wall's left is black. At each white beat the left half dictates a colour, or signal, that
the right side must show. Take two left halves that both start on a black beat, copy the same seven-square repeating
pattern and then turn white all the way out. Their white tails start at suitable depths 28 squares apart, as deep as
you like. Both keep the clock going while asking for long runs of alternating signals that a real right half can
show (G282), then a white signal where black was due; yet at the next black beat one holds and the other breaks. So
a fixed number of recent signals, the starting beat and the remainder of the tail's depth after dividing by 28
cannot always predict that beat. Nor can a checker for a finite list of forbidden signal patterns, since it
remembers only the last few signals.

**Why it matters.** It closes one proposed shortcut: a checker that predicts the clock exactly must remember more
than those three things, and the depth's remainder after dividing by 56 already tells this pair apart. It does not
rule out a checker with a richer finite memory, or a cautious one that allows both outcomes. Neither left half is
claimed to come from a real band, and the one that passes is not claimed to keep the clock forever.

**An everyday picture.** Two people wake in windowless rooms with twelve-hour clocks that both show three. For one
it is three in the afternoon and the bakery downstairs is open; for the other it is three in the morning and its
shutters are down. Nothing in either room tells them which, though a twenty-four-hour clock would.

## The formal statement and proof

*Where:* RULE30-GPT.md GC1200; uses the already-proved GC1197 gate.

**Claim (PROVED; GC1200, Local L685; exact clock prediction only).** A finite visible suffix, the child phase, and depth modulo28 do not determine the next black-clock verdict of every zero-terminated left row. This also applies to an ordinary finite forbidden-word residual as the visible summary. It does not exclude nondeterministic relaxations or richer finite hidden states.

**Proof from the established guard.** In phase1, let A^1 be GC1197's seven-ring reference. Set b_j=A^1_0(j) for j<ell and b_j=0 for j>=ell. Choose ell_+=14+56u and ell_-=42+56u, with u arbitrarily large. Both are first discrepancies: A^1_0(ell)=1. Before their arrivals, all black-clock tests pass and their visible prefixes are respectively(10)^(3+14u) and(10)^(10+14u). These are actual train prefixes: shifting GC1020's phase0 realization forward three ticks gives phase1 with the same visible(10)^infinity. Hence every sound finite cut catalog accepts them. Their next white sample at tickell-1 is0, since the front flips the reference left-neighbour0 to1. Their next black sample at tickell differs: GC1197's proved phase1 gate permitsell mod56=14 and rejectsell mod56=42. Thus the values are1 and0.

Given any suffix lengthK, choose u so both prior words exceedK. Their finalK symbols agree, both histories have phase1, the next observation has the same time colour, and ell_+=ell_- modulo28. For a catalog of maximal word lengthM, its standard cut residual depends only on the lastM-1 letters; chooseK>=M-1. The residuals are therefore identical before the common next visible0 is consumed, yet the following black guards differ. Hence the specified summary cannot predict that guard exactly.

**Unexpected scope check.** Depth modulo56 distinguishes this pair and suffices for GC1197's narrow two-arrival gate. So the counter is no obstruction to all finite-type certificates, no proof of unbounded memory after adding other coordinates, and no failure of a sound overapproximation that retains both black outcomes. No real long-band membership is asserted for either zero-terminated row, and the passing first guard is not infinite survival. This audits a proposed state compression using proved controls; no new train scan, residue refinement or widening ran.

**Filing check.** proof_dupes.py --near W286 gives G162, G167 and G285; all three read. The first two concern periodic-driver reset costs, and G285 pins one early-departure endpoint by a certified cut. This applies the established GC1197 clock gate to a suffix-state compression claim; it restates none of those results and supplies no new train scan.

**Promotion receipt.** Local L685 at0af287ef reads the two prior words, their phase and depth congruence, the next white sample and both black guards. Its earlier direct B2 controls already contain the named verdicts. No new computation requested or replayed; promoted from W286.
