# canonical ancestor tails have unbounded periods

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT123. canonical ancestor
tails have unbounded periods (second-read by Local, 2026-10-06)"; rebuild with `python3 proofs/build.py`. Edit the
proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

Run a root backwards for ever, and the repeating pattern on its far left keeps getting longer.

**What it says.** Rule 30 can be run backwards in exactly one way if rows may stretch endlessly to the left (G122).
Doing that from a root, each earlier row repeats far to the left with some period, and the periods keep growing,
each a multiple of the last, without limit.

**Why it matters.** It closes a hoped-for shortcut, that a seed's backward history stays simple. It holds for every
root, so it cannot single out a counterexample.

**An everyday picture.** Rewinding a film further and further shows ever longer repeating wallpaper at its edge,
never one fixed pattern.

## The formal statement and proof

### G123. Canonical ancestor tails of every nonzero finite root have unbounded spatial periods (2026-10-06)

**Status:** all-depth paper theorem conditional on G121-G122's proved inverse construction;independent review pending. No measurement or new experiment. This concerns spatial periods in backward ancestors,not the source's temporal period or a prize solution.

Let r be a nonzero finite root,and let x_n be its unique right-quiescent nth canonical predecessor,with x_0=r. G122 inductively supplies an eventually periodic far-left tail for each x_n. Let C_n be the unique two-sided periodic extension of that tail,with least spatial period p_n. C_0 is the zero row,C_1 the one row,and p_0=p_1=1,p_2=3.

The extensions obey F(C_n)=C_(n-1). To see this,far enough left the local update on x_n reads only its periodic tail,so F(C_n) agrees there with the tail of F(x_n)=x_(n-1). Both extended rows are periodic;agreement on a left half-line forces agreement at every site. Thus F^n(C_n)=0 and F^(n-1)(C_n)=1. Zero is absorbing,so C_n first reaches zero after exactly n steps. This is exact for all n,not a horizon fit.

All n+1 rows C_n,F(C_n),...,F^n(C_n) are distinct. A repeat before hitting zero would put the deterministic orbit on a cycle,which cannot later hit absorbing zero for the first time. Every row in this trajectory has spatial period dividing p_n,because a translation-commuting cellular automaton preserves any input period. They therefore occupy n+1 distinct labeled configurations on a p_n-cell ring,which has 2^p_n configurations. Consequently

    n+1 <= 2^p_n,
    p_n >= ceil(log2(n+1)).

In particular the ancestor-tail spatial periods are unbounded for every nonzero finite root. Moreover p_(n-1) divides p_n:the output's least period divides any period of its input. Combined with G122,p_(n-1)<=p_n<=4*p_(n-1). The divisibility chain must have infinitely many strict increases. No linear growth law,exact multiplier sequence,or bounded gaps between increases is established.

**Independent perspective and unexpected check.** The same bound is the finite-state absorbing-orbit bound:a p-bit deterministic system cannot have a first-hit transient of length>=2^p. This checks the indexing without the inverse graphs. The nonzero-root hypothesis is essential:the zero row has all canonical ancestors zero,all periods 1,and first-hit time 0. Treating every finite row as a root,or every inverse depth as a first-hit time,would incorrectly apply the bound to this counterexample. For a non-root finite row,first descend to its root as in G121;the finite ancestry contributes a time offset,so the statement above is anchored at the root.

**What this bridges and what it does not.** This crosses from the finite inverse transducer to an all-depth necessity:uniformly bounded ancestor-tail periods are impossible. The natural candidate ranking is the first-hit depth on each periodic ring;it decreases under forward evolution,but its state space changes with p_n. It is not a ranking for the forced0101 walk and provides no contradiction to a temporal wall. The missing theorem remains a link from an eventual0101 wall to bounded ancestor-tail periods,or another incompatible restriction. Since unbounded tail periods occur for every nonzero finite root,the property alone cannot distinguish a hypothetical period-two counterexample from other seeds. The counting here is a finite-state pigeonhole proof,not a survivor-decay assumption. The finite-state pigeonhole bound is elementary. G105 supplies related absorbing-zero ring examples, not this ancestor-depth claim. No novelty claim for the general orbit bound.
