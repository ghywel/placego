# Three consecutive right-prefix doublings are forbidden after an even base

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT249. Three consecutive right-prefix
doublings are forbidden after an even base (second-read by Local, 2026-10-09)"; rebuild with `python3
proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

The diagonals along the single cell's right edge, and those of any finite seed, cannot double their combined period three times in a row.

**What it says.** Read the pattern in lines parallel to its right edge. Each line repeats, with a period that is a power of 2, and the combined period of the first j lines can double from one line to the next. GPT proves it can never double at three consecutive lines once it has passed 1, because the third doubling would need an odd count where the count is always even. So the combined period of the first j lines is at most 2 to the power ceil((2j - 1)/3). Second-read by Local, with literal checks on the single cell and 30 random seeds.

**Why it matters.** It gives every finite seed a guaranteed band of ordered diagonals at its right edge that grows with time, at least about 1.5 lines for each doubling of the elapsed time. That is a universal lower bound, well under the single cell's measured rate of about 2.5, and it says nothing about the centre column.

**An everyday picture.** A counter whose digits can each slow down by half, but never three digits in a row, cannot fall behind faster than two halvings in every three steps.

## The formal statement and proof

**Promoted from the waiting room, 2026-10-09 (Local L400).** Second reader: Local, chat L400. Waiting-room heading: "G249. Three consecutive right-prefix doublings are forbidden after an even base (GPT, 2026-10-09; waiting room)". The text below is unchanged, so its *Status:* line is historical.

*Status:* independent hand reading pending. *Where:* RULE30-GPT.md GC763. *Provenance:* exact text of GC763 below; uses the known dyadic xor-integrator mechanism, not a prize claim.

**Lane change from the stalled critical parity flux to the open band/core rate bound.** Hand prediction: two successive new maximal right periods force an even OR-driver parity at the next depth once the old period is even. Counterfactual: every successive depth can double the joint prefix period. Independent control uses half-period complementation and the OR truth table; unexpected control keeps two adjacent doublings possible. No experiment or period scan. Existing records GC755/756 and the finite-defect paired cancellations GC729/751 checked; those cancellations concern different moving-frame background defects. Rowland's Lemma2 and section3 read at the author's PDF: the known dyadic integration/restart mechanism is the premise, not a novelty claim.

Normalize any nonempty finite seed so its rightmost black bit is at0. Let D_j(t)=x_t(t-j), with D_(-1)=0, D_0=1, and define Q_j=lcm(p_0,...,p_j), where p_j is D_j's least temporal period. The exact recurrence is

    D_j(t+1) xor D_j(t)=D_(j-1)(t) OR D_(j-2)(t).

GC755/756 give pure dyadic periods, Q_j either Q_(j-1) or2Q_(j-1), and no need for individual-period monotonicity. Moreover Q_0=1 and Q_1=Q_2=2 for every seed: both first drivers are identically1, regardless of the two initial bits.

Suppose Q_(j-1)=q>=2 and Q_j=2q, Q_(j+1)=4q. Since a new prefix maximum must occur in the newly added diagonal, D_j has least period2q and D_(j+1) has least period4q. Their drivers have periods dividing q and2q respectively. A running XOR doubles its driver's allowed period only if the XOR of that block is1. Therefore, for every t,

    D_j(t+q)=1-D_j(t),
    D_(j+1)(t+2q)=1-D_(j+1)(t).

The next driver h(t)=D_(j+1)(t) OR D_j(t) has period dividing4q. Pair its samples t and t+2q for0<=t<2q. The first input complements and the second repeats; the OR pair XOR equals1-D_j(t). Hence the XOR of all4q driver samples equals the parity of the white count of D_j over2q ticks. Its q-half complementation makes that count exactly q, which is even. Integrating h thus gives D_(j+2) a period dividing4q, so Q_(j+2)=4q. Three successive prefix doublings are impossible. This is a parity obstruction, not a claim that every two doublings are followed by exactly one plateau.

**Uniform bound.** From depth2 onward each increment of log2(Q_j) is0 or1, and each consecutive triple has at most two ones. Splitting the j-2 increments into triples plus a remainder gives, for j>=2,

    log2(Q_j) <= 1+ceil(2(j-2)/3)=ceil((2j-1)/3).

The same bound holds at j=0,1 by their exact base values. Consequently, with m=floor(log2(t)), t>=1, all diagonals through j=floor((3m+1)/2) have Q_j<=2^m<=t. GC756's age-period prefix therefore obeys

    R_prefix(t) >= floor((3*floor(log2(t))+1)/2).

This sharpens GC756's universal logarithmic lower bound; it is still far below the measured single-cell coefficient near2.5. It proves neither an upper bound on prefix width, an asymptotic coefficient, nor any core-column aperiodicity. The generic return-to-seed ruler H(t) inherits the same lower bound with m=v2(t).

**Independent and unexpected controls.** For the single cell, hand integration gives D_1=D_2=0101 repeating, D_3=0011 repeating, and D_4=00101101 repeating. Thus prefix periods actually double at depths3 and4: a stronger no-two-doublings assertion is false. Their next OR driver has period8 word00111111 with six black samples, so D_5 has period dividing8, as the parity argument requires. These are literal short-word calculations, not a new run. The q-even premise is essential to the paired sum; no odd-q generalization is asserted. Empty seeds are outside the normalization.

**Disposition.** A useful universal growth bound is now available for the right-prefix ruler without assuming individual-period monotonicity. Independent hand reading requested; no computational run requested. The critical all-L bridge lane remains open after GC762's failed invariant. Scratch flags/doorbell deferred without retry; break room closed.

*Filing gate (GPT, 2026-10-09).* Hard duplicate controls pass; nearest36,09,G124 read in full before filing. Entry36 supplies the single-cell ruler/half-period mechanism but no triple-doubling bound;09 concerns eventual left diagonals;G124 classifies spatial periods of zero-reaching rows. This entry refines the generic right-prefix growth bound rather than restating those results. No generated proof pages rebuilt.

*Received corroboration (GPT GC764, 2026-10-09).* Local L399/c56e8743 reports the single-cell right prefixes through depth34 and30 random16-cell seeds satisfy the bound. This is received finite checking, not an explicit all-depth hand verification; the waiting-room status remains. Normalization control: opposite initial bits in D1/D2 make their OR constant1 and D3 period2, so the upper bound must not be read as a mandatory staircase.

*Final neighbour refresh.* After the normalization receipt, the nearest set is36,09,G151; all read in full. G151 excludes consecutive spatial-predecessor period doublings by a reset word; G249 instead excludes triple temporal-prefix doublings by an even OR-driver sum. Their domains and bounds differ.

*Independent reading (Local L400, 2026-10-09).* Near-entry gate run (`--near W249`: G151, 36, 09, as at filing). Verified by hand: a new prefix maximum lies in the new diagonal, so p_j = 2q and p_(j+1) = 4q; a running XOR of a driver of period dividing q (resp. 2q) doubles only by complementing, giving D_j(t+q) = 1 - D_j(t) and D_(j+1)(t+2q) = 1 - D_(j+1)(t); pairing t with t+2q gives h(t) xor h(t+2q) = 1 - D_j(t), so the 4q-sum is the white count of D_j over 2q ticks, exactly q, even; hence D_(j+2) repeats after 4q. Purity: by induction every D_j is a running XOR of a purely periodic driver, so it is purely periodic. Base Q_0 = 1, Q_1 = Q_2 = 2 (both drivers are constant 1). The triple rule from depth 2 gives log2 Q_j <= 1 + ceil(2(j-2)/3) = ceil((2j-1)/3). Literal checks (L399): the single cell's prefixes reproduce A094605 to j = 34, and 30 random 16-cell seeds show no triple doubling and no breach of the bound.
