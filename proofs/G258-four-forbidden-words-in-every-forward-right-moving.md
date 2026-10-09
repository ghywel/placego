# Four forbidden words in every forward right-moving G trace

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT258. Four forbidden words in every
forward right-moving G trace (second-read, 2026-10-09)"; rebuild with `python3 proofs/build.py`. Edit the proof in
PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

Along Rule 30's diagonal moving right one cell each tick, four short colour patterns never occur.

**What it says.** Reading white as0 and black as1, the patterns are00100,11011,000111 and111000. Neighbouring diagonal traces would be forced to give one bit two different values, so each pattern is impossible for any starting row. Local and GPT independently read each other's two proofs. A singleton run cannot sit between two runs each at least two ticks long, and two neighbouring runs cannot both be at least three ticks long.

**Why it matters.** These are uniform local restrictions that eliminate some options before a cyclic-profile search. They do not bound one run's length, determine the required parity, or solve the alternating-centre problem; a fixed centre follows a different line.

**An everyday picture.** A short rhythm may look possible on its own, but the neighbours needed to produce it would have to play two incompatible notes at once.

## The formal statement and proof

*Where:* RULE30-GPT.md GC800/GC802; Local L426. *Credit:* GPT's six-tick obstruction, independently read by Local; Local's five-tick companion, independently read by GPT. *Status:* both hand proofs verified. No literature novelty or prize claim.

**Setting and statement.** Let G(y)(i)=y(i) xor (y(i+1) OR y(i+2)), and let D(t) be a column of any forward G orbit. Delta V(t)=V(t+1) xor V(t). Then D never contains 00100,11011,000111 or111000, provided the whole word lies in the defined orbit. No periodicity or finite-support assumption is needed. G columns are the right-moving physical Rule30 traces x_t(i+t), not fixed-site centre columns.

Neighbouring columns D,U,W,X,Y,Z,H always obey

    Delta D=U OR W; Delta U=W OR X; Delta W=X OR Y;
    Delta X=Y OR Z; Delta Y=Z OR H.

**Five-tick pair (Local; independently read by GPT).** Suppose D=00100 at ticks0..4, so Delta D=0110. The first equation gives U=W=0 at0 and3, and U OR W=1 at1 and2. If U(1)=1, the second equation at0 forces X(0)=1, and the third forces W(1)=1. U(2)=1 would contradict W(1)<=Delta U(1)=0; U(2)=0 would force W(2)=1 against Delta U(2)=0. Thus U(1)=0. Now W(1)=1. Delta U(0)=0 gives X(0)=0; Delta W(0)=1 therefore gives Y(0)=1. The second equation at1 forces U(2)=1. The fourth equation at0 forces X(1)=1. The third at1 forces W(2)=0, and at2 forces X(2)=0 because W(3)=0. This contradicts Delta U(2)=1=W(2) OR X(2). Four equations suffice. D enters only through Delta D, so 11011 gives the same contradiction; no global colour-complement symmetry of G is assumed.

**Six-tick pair (GPT; independently read by Local).** At a transition r, let D have three equal bits through r and three opposite bits from r+1. The first equation forces U=W=0 at r-2,r-1,r+1,r+2. If U(r)=0, then W(r)=1 but Delta U(r)=0, impossible; hence U(r)=1. The second equation at r-1 gives X(r-1)=1, and the third gives W(r)=1. The third at r+1 gives X(r+1)=0. At r, the third and fourth imply 1=X(r) OR Y(r) with Y(r)<=Delta X(r)=X(r), so X(r)=1. The fourth at r-1 gives Y(r-1)=0. The third at r-2 gives X(r-2)=Y(r-2)=0. Finally the fourth at r-2 forces Z(r-2)=1 against Delta Y(r-2)=0 in the fifth. Both orientations have the same Delta D values. In particular D(r+3) is needed to force W(r+2)=0; no undefined endpoint is used.

**Cyclic consequences.** A singleton run cannot have both neighbouring runs of length at least2. Two adjacent runs cannot both have length at least3. Thus at least half the runs of a nonconstant cyclic trace have length1 or2, counted by runs, not time. GC799's existence of a short run is included as a corollary, not separately filed.

**Independent controls and limits.** GPT's complete eleven-bit/five-update cone check finds neither six-tick word; physical fixed-site centre controls contain each32 times. Local independently reproduces those counts. Local's larger trace-word census is received, not independently replayed: its claimed completeness through length8 is not part of this theorem. The actual cyclic right tail D=0011,U=W=0101,X=1010,Y=0101,Z=1010,H=0101 satisfies all five equations and continues by alternating profiles, so length2 runs remain possible. Unexpected scope guard: a single G seed at2N has leftmost black front2N-2t, giving site0 N initial zeros before its first1. Individual runs are therefore unbounded in nonconstant forward finite-support traces. No cyclic maximum-run, time-density, marked-end parity, all-L bridge or prize conclusion follows.

**Duplicate and reading gate.** GC801 read G188/G224/G189 for the six-tick candidate: those concern spatial zero returns or coefficient stencils. The combined statement and summary gate additionally reads entry29 (Rule210 empty-left uniqueness) and G256 (alternating-centre neighbour density); these concern different rules or frames and do not restate these forbidden G words. Final actual nearest G188,08,G251 were also read in full:08 propagates eventual constant diagonals under the rooted band premise, and G251 bounds L-block overlap with a settled-white diagonal. Neither states these universal local words. Formal/summary scores are retained in GC802. Local L426 verifies the six-tick proof; GPT GC802 verifies every branch of the five-tick proof, especially U(2) and the final W(2)=X(2)=0 contradiction.
