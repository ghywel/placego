# a closed arrival-phase gate removes only transient front states

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT160. a closed arrival-phase gate
removes only transient front states (second-read by Local, 2026-10-07)"; rebuild with `python3 proofs/build.py`.
Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

The clock that times the resets settles into a narrower set of positions within two steps, but every repeating loop
was already inside it.

**What it says.** The reset-timing clock of G8 enters, within two steps, a restricted set of arrival positions and
never leaves. That can trim the starting stretch of a timing calculation. But every loop the clock can repeat
already lies inside the set, so the known obstacle to a fast settling bound (G8's slope 2) survives.

**Why it matters.** It removes a distraction from the start of the calculation, not the obstacle itself.

**An everyday picture.** A ticket barrier that every regular commuter already walks through: it stops the odd stray
visitor, never the daily traffic.

## The formal statement and proof

### G160. A closed arrival-phase gate removes only transient front states (2026-10-07)

**Statement.** Use G8's common-period-P full-line reset-front graph, excluding the zero word-pair. For a state (a,b,r), define the gate by

- if a is nonzero: a(r-1)=1;
- if a=0: (S b XOR b)(r-1)=1.

Indices are modulo P. The gate is forward invariant. Every nonzero compatible front path is in it after at most two edges. The rooted front starts at the exceptional pair (0,1) and enters the gate after one edge. Every compatible phase-augmented cycle lies entirely inside the gate.

**Proof.** An edge goes to (b,c,r'), with S c=a XOR(b OR c). If b is nonzero, r'=r+delta(b,r) is exactly one time past the first black b cell at or after arrival. Thus b(r'-1)=1 and the child is in the first part of the gate regardless of the parent's phase.

If b=0, delta=0 and r'=r. The child obeys S c XOR c=a. Since (a,b) is not the zero pair, a is nonzero and c is nonconstant. A gated parent has a(r-1)=1, so the child's second gate condition holds. This proves invariance. From any ungated state an active b enters immediately. If b=0, its child has nonconstant driver c, so the following edge enters immediately. No nonzero pair has the zero pair as a child, by the same recurrence. Hence two edges suffice. The root has constant-one driver and cost1, giving the gated child (1,1). On a cycle every state has at least two preceding edges on the same cycle; the two-edge entry assertion puts every state inside the gate. Square.

**Phase counts and certificate transfer.** For a fixed pair of common period P, the gate allows exactly the number of black bits in a when a is nonzero, or the number of transitions in b when a=0. On its relative-phase fiber of size q, use the corresponding counts in q letters. This is an exact local restriction, not a census of reachable states. If a phase-sensitive potential on the gated graph bounds interval debt at slope gamma>=0 by H, the whole nonzero graph has the bound H+2P: discard at most two initial edges, each of cost at most P, and apply the gated certificate to the rest. For the rooted front, the initial cost is1, giving H+1 instead. Intervals wholly inside the discarded part obey the same conservative bound. These are full-line front statements; birth clamps and sublinear period growth remain separate obligations.

**Controls and identified unexpected check (symbolic, no run).** The root (0,1) itself fails the second gate condition because a constant word has no transitions; its first child satisfies the first condition. The derivative condition at a=0 is essential, as the period-two integrated children have zero first coordinate yet valid arrival phases.

The two-step threshold is needed on the unrestricted graph. In temporal order take a=0101, b=0000, r=1 at period4. Integration gives c=0011. The parent fails a(0)=1, and the child (0,c,1) still fails Delta c(0)=1. Its active c then enters on the next edge. This checks a local compatible path, not root reachability. The identified unexpected cycle guard is that every cycle already lies in the gate: G8's compatible slope-2 obstruction survives unchanged. Gate pruning cannot improve cycle means or cure that obstruction; it removes transient arrival phases only.

**Record and scope.** This is a direct finite-graph consequence of G8's reviewed next-black arrival rule and G7's diagonal recurrence. It does not depend on the pending G157-G159 proofs. No computation or literature novelty claim is made. A uniform gated potential size bound remains unproved; the gate by itself gives neither a settling bound nor a prize result.

*Second reader's note on G160 (Local, 2026-10-07; chat L116).* Correct. With an active driver the arrival lands one past
a black driver cell, so the child is gated whatever the parent's phase. With a zero driver the phase is kept, and the
child's word difference equals the parent's first word, so a gated parent gives a gated child. A nonzero pair never has
the zero pair as a child, so two edges always reach an active driver. Every state on a cycle has two cycle edges before
it and is therefore gated. The transfer charge is at most $P$ per discarded edge, and 1 for the root's edge. Checked
exhaustively (`rule30_audit_g99_g100.py`, S54) on the full-line front graph for every $P \le 7$: the gate is invariant,
every state is gated within two edges, and every state of every cyclic strongly connected component is gated (5,894
cyclic states at $P = 7$). The gated phases of each pair number the black cells of $a$, or the transitions of $b$ when
$a = 0$. GPT's period-four control fails the gate at the parent and at both integrated children, and enters at the next
edge. A muddled first draft of the control's boolean expression was rewritten before the recorded run.
