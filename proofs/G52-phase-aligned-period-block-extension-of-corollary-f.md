# Phase-aligned period-block extension of Corollary F

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT52. Phase-aligned period-block
extension of Corollary F"; rebuild with `python3 proofs/build.py`. Edit the proof in PROOFS.md and this summary in
[summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

Near-repeats in column 1 rule out a finite seed for every repeating wall, not only black-white.

**What it says.** Corollary F (proof 11) says that, for the blinking wall, a block of column 1 repeated almost at
once is fatal to a finite seed. GPT extended this to every repeating wall, provided the repeats line up with whole
periods of the wall, and later covered the case of an initially empty left half.

**Why it matters.** It widens one of the record's sharpest tools from one rhythm to all of them.

**An everyday picture.** An echo that comes back too soon gives away a wall that is too close, whatever the shape of
the room.

## The formal statement and proof

**Where:** RULE30-GPT.md G52; copied proof. **Status:** second-read by Local, 2026-10-06 (note below); GPT's MF controls not run at publication. The original index's plausible extension is not promoted before review.

### G52 theorem and proof: Corollary F for phase-aligned period blocks

Let a nonconstant Rule30 wall tau have period p>=2 from time0. For each period m, let v_m be the vector of column1 bits at the white phases within times pm,...,pm+p-1, in phase order. Suppose there is a fixed integer K>=0 and pairs i_j<i'_j with i'_j-i_j tending to infinity for which the vectors v at these indices have a common future of at least ell_j periods, with ell_j>=i'_j-K. Then the forced left half cannot have an initially finite nonempty black support.

Proof. Assume finite support and let its leftmost black cell be at depth L. The universal band lemma B2 supplies an eventually-black diagonal b>=L+pK, black from time t_b. Matching white-phase vectors for ell_j complete periods makes the column pair(-1,0) identical for p*ell_j times from a=pi_j and a'=pi'_j. This follows directly from Lemma1: at a white phase the left neighbour depends on the matching visible bit, and at a black phase it is independent of that bit; tau(t) and tau(t+1) agree because both shifts are multiples of p. Choose j so p(i'_j-i_j)>b and pi'_j>=t_b. Theorem A triple-prime with distance L-1 from the leftmost black cell to column-1 gives

    p*ell_j <= L-1+pi'_j-b <= pi'_j-pK-1,

contradicting ell_j>=i'_j-K. This reuses the checked half-line versions of Lemma1, B2 and the window principle; no full right-half realization is required. For0101 there is one white phase per period and this is Corollary F's existing statement. It is a derived extension, without a novelty claim. Empty initial left rows are not included in this stated version; their forced first birth and time shift need a separate scope check.

Phase alignment matters. For wall001 and visible bits all0, Lemma1 gives column-1 values0,1,1 at phases0,1,2. Shifting by one visible-bit index exchanges the two white phases (physical times0 and1), whose left-neighbour values differ. Identical visible-bit futures alone therefore do not justify repeating the pair at those physical shifts. The block statement above supplies the missing alignment. It does not prove that an arbitrary near-square in the ungrouped visible sequence can be aligned, nor supply a new channel/squeeze certificate.

### G52 addendum: the empty initial left row is covered

The phase-aligned period-block theorem also excludes an empty initial left row. A nonconstant cyclic binary wall has a phase j in[0,p-1] with tau(j)=1 and tau(j+1)=0. Lemma1 forces x_j(-1)=1 there, independently of column1. Starting from an empty left row, every finite-time left row has finite support by the local update rule. Once a leftmost black cell exists, it advances left at each subsequent step: the new cell just left of it has input100 and Rule30 outputs1. Consequently the left row at time p is finite and nonempty.

Shift the whole forced evolution forward by p. Its wall has the same phase and its period-block word is v'_m=v_(m+1). The near-square hypothesis persists with slack K+1. For any sufficiently long original pair(i,i',ell), if i>=1 use shifted indices(i-1,i'-1) and the same length ell. If i=0, discard the first common block and use shifted indices(0,i') with length ell-1. In both cases the gap still tends to infinity and the new common length is at least its later shifted index minus(K+1). G52's proved nonempty-row case now contradicts finiteness of the shifted row. This completes the initially-empty case without assuming a realized full right half. The original limitation above records the first scoped version; this addendum removes it by an explicit time-shift argument.

The statement still requires phase-aligned period-block repeats. It does not exclude all unaligned visible-bit near-squares or solve any Rule30 prize question. This is a derived extension of the checked band/window lemmas, awaiting independent review.

**G52 control status:** MF1-MF2 pass50 walls/288 samples/8016 transitions; analytic extension and empty-row addendum independently read by Local (L023/L024).

*The addendum above was written by GPT after Local's first reading below; Local second-read it the same day
(chat L024): correct. A nonconstant wall has a phase with black then white, where Lemma 1 makes column $-1$ black
whatever column 1 is; the leftmost black cell then persists and moves left ($100 \to 1$), so the left row at time
$p$ is finite and nonempty; shifting by one period keeps the near-square hypothesis with slack $K + 1$, using indices
$(i - 1, i' - 1)$ when $i \ge 1$ and $(0, i')$ with length $\ell - 1$ when $i = 0$; the nonempty case then applies.*

*Second reader's note on G52 (Local, 2026-10-06; chat L023).* Correct. Matching white-phase vectors over $\ell_j$
complete periods at shifts that are multiples of $p$ make the pair $(-1, 0)$ identical over $p\ell_j$ times, by
Lemma 1 and the periodicity of $\tau$ (including $\tau(t+1)$ at a block's last time); Theorem A‴ at distance
$L - 1$ with $b < p(i'_j - i_j)$ black at time $p\,i'_j$ gives $p\ell_j \le p\,i'_j - pK - 1$, against
$\ell_j \ge i'_j - K$; such $j$ exist because $i'_j - i_j \to \infty$. The 001 example checks (column $-1$ reads
0, 1, 1 at the three phases with column 1 white). Checked: the window-matching step on 1,764 random nonconstant
walls of periods 2 to 9 with arbitrary bits at black phases, zero failures (`rule30_audit_g52.py`). GPT's own MF1 and MF2 controls (`tests/probes/rule30_gpt_period_blocks.py`) replicated unchanged by Local on
2026-10-06 at 05f1619: 50 walls, 288 samples, 8,016 transitions, and the 001 misalignment.
