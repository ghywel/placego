# two shared black observations shield the next tick

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT112. two shared black
observations shield the next tick (second-read by Local, 2026-10-06)"; rebuild with `python3 proofs/build.py`. Edit
the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

Two shared black observations force the next source samples to agree in the right-reading coupling.

**What it says.** Starting from a shared row, a shared white first-step right neighbour forces agreement immediately to its left. Two shared black source observations then shield the next update.

**Why it matters.** Finite positive-probability cylinders turn that local identity into a proposed infinite-line first-order Markov counterexample for every interior rate. WH1-WH3 are NOT RUN and independent review is pending; no claim about higher memory orders or survival follows.

**An everyday picture.** Today's matching signal can conceal yesterday's influence on tomorrow's error.

## The formal statement and proof

### G112. Two shared black observations shield the next tick and obstruct bulk first-order memory closure (2026-10-06)

**Status:** local proof and infinite-ensemble counterexample proposed; WH1-WH3 preregistered NOT RUN, independent review pending. This explains Local L066's deterministic bin without repeating its production enumeration. It extends G109-G111 by a local argument, not by taking a ring limit. The general issue of projected Markov processes is established lumpability theory; the claim here is only this Rule30 coupling identity.

Let z_t be synchronous Rule30 and y_t its right-reading raced copy, with common initial row x. At each site the raced update reads the old left and centre and either the old or updated right neighbour. Write I_t=z_t(0), E_t=z_t(0) XOR y_t(0), K_t=(I_t,E_t). Flags may be arbitrary provided right recursions terminate. For the probabilistic conclusion use iid fair initial bits and fresh independent Bernoulli(eps) flags,0<eps<1, on the infinite line; these recursions terminate almost surely at every site and finite tick.

**First-step white agreement lemma.** If z_1(j+1)=y_1(j+1)=0, then z_1(j)=y_1(j). If x(j)=1, its old centre masks both right-read alternatives. If x(j)=0, the ideal right output0 equals x(j) XOR (x(j+1) OR x(j+2)), forcing x(j+1)=0. Both the old and updated raced right alternatives are then0, so the target updates agree. The lemma uses common initial input; it is not asserted for arbitrary later unequal rows.

**Two-black shielding.** Suppose z_1(0)=y_1(0)=z_2(0)=y_2(0)=1. The black old centre at site0 shields its tick2 right read. Output1 therefore forces z_1(-1)=y_1(-1)=0. Applying the white agreement lemma at j=-2 gives z_1(-2)=y_1(-2). When site-1 updates on tick2, its centre is0 but its old and updated right alternatives are both1. Its output is consequently the shared old left value XOR1, so z_2(-1)=y_2(-1). Site0's black old centre again shields tick3, yielding z_3(0)=y_3(0). Thus the refined bin

    B={I1=1,I2=1,E1=0,E2=0}

has next error E3=0 for every compatible shared-input history. This is a deterministic three-tick statement, independent of the rate and outside flag patterns.

**Positive finite cylinders, not an infinite clean event.** Define the nine update nodes C: tick1 sites-2..2, tick2 sites-1..1 and tick3 site0. Their ordinary ancestors are initial sites-3..3.

For initial word0110000 on-3..3 and all nine flags in C zero, both source traces have I1=I2=1, so B occurs. This cylinder has probability(1-eps)^9/128>0.

For initial word0000010 on-3..3, set only site0's tick1 flag in C to1 and all other eight to0. Its updated right neighbour at tick1 is an unflagged node of C, so no extra outside recursion enters. The ideal source trace at ticks0..3 is0011 and the raced trace0110: I2=1,E2=0,E3=1. The cylinder has probability eps*(1-eps)^8/128>0. Outside initial bits and flags are unrestricted in both constructions.

Take A={I2=1,E2=0} and S={E3=1}. The cylinders prove P(B)>0 and P(S and A)>0. The shielding identity proves P(S|B)=0, whereas P(S|A)>0. Since B further specifies past K1 within A, this violates the first-order Markov property of the single-site paired observable at tick2, even allowing time-dependent kernels. This proves neither failure of every finite memory order nor a long-time survival law. Each separate trace can remain iid fair as in G107; coupling memory is a different question. This is not a single-seed or prize claim.

**WH1-WH3 preregistered NOT RUN.** WH1: all initial rows and effective right-flag patterns on rings W3..5 (672 effective cases, equivalently1344 full flag assignments), test the first-step white agreement implication at every site. It must hold; this small one-step control is not Local's three-tick production table. WH2: implement the two explicit finite cylinders with shrinking boundaries and literal Rule30 table, independently compare the declared four-bit traces and synchronous XOR/OR updates; predict B and A intersect S respectively. WH3, unexpected orientation guard: on a W5 left-reading scan, initial00001 and only site1 flagged yield ideal/raced shared white output at site2 but different output at site1. The counterfactual that white agreement works for either scan direction must fail. Publish these predictions and instrument before execution; no production sweep or random trial.

*Second reader's note on G112 (Local, 2026-10-06; chat L069).* Correct, and both points GPT asked me to challenge
hold. White agreement: if $x(j) = 1$ the old centre masks both right reads; if $x(j) = 0$ the ideal white output
forces $x(j+1) = 0$, so both right alternatives are 0. The nine-node cylinders are closed: every unflagged node reads
the old snapshot, and the one flagged node (site 0, tick 1) reads an unflagged node of the cone. Checked
(`rule30_audit_g99_g100.py`, S14): white agreement at every site of every ring of 3 to 6 cells under every right flag
word; both cylinders on the line (the first gives $B$ with $E_3 = 0$, the second ideal 0011 and raced 0110 with
$I_2 = 1$, $E_2 = 0$, $E_3 = 1$); the left-scan guard breaks agreement as stated. The second cylinder lies in the child
$(0, 1, 1, 0)$, the one with the interior root in my spectrum: at that rate it matches its parent's rate, but here it
supplies $S \cap A$ at every rate, which is all the argument needs.
