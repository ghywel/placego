# Proposition 13 (computed): the wheel's kick alphabet is local

*Siblings, Jen and the squeeze. Derived from [PROOFS.md](../PROOFS.md), entry "26. Proposition 13 (computed): the
wheel's kick alphabet is local"; rebuild with `python3 proofs/build.py`. Edit the proof in PROOFS.md and this
summary in [summaries.md](summaries.md), never this file.*

**Status:** Local's computed proposition; second-read by GPT (GC359) and filed out of the.

## In plain words

The wheel's jolts can only be of a few fixed sizes, and the cells near the edge decide which sizes are possible, whatever happens further in.

**What it says.** Next to the striped edge, the second column runs like a wheel. Now and then something arriving from the chaotic interior knocks it to a new position: a "kick". This result shows, by an exhaustive finite computation, that once the wheel has run for about two and a half turns, a kick can happen at only four points of its turn. At each of those points it can only be one of five or six sizes. For the two kick points actually seen in simulations, the allowed sizes are exactly the sizes that were measured on more than eleven thousand real kicks.

**Why it matters.** It was thought the kick sizes came from the chaotic interior. They do, but only the choice among a short, fixed list does. The list itself is fixed by about sixteen columns of local structure. That bounds how much information a kick can carry. It does not say kicks must keep happening, which is what a full proof would need.

**An everyday picture.** A gearbox: whatever the driver does with the pedal, the car can only be in one of the gears the box was built with. The driver chooses the gear; the gearbox decides what the gears are.

**GC588 entry 26 timing outcome (single-party, awaiting reading).** The 56-observation minimum old lock has a wider necessary local projection than the 57-observation table: it additionally permits class 19, sizes -8 through -4, with only 21 new observations fitted. All shared alphabets agree. The original and settled certificates keep their stated timing; no true short-lock event is constructed.

## The formal statement and proof

*Where:* chat L216; `tests/probes/lexicon/rule30_kick_layers.py` (KL), with its outcome in the header. *Bears on:*
PERIOD-TWO.md row 6.1 (a statement about the kicks' sizes); RULE30-PRIZE.md §8.43 and §8.44; the measured alphabets of
`rule30_kicks.py` (KK0). *Status:* Local's computed proposition; second-read by GPT (GC359) and filed out of the
waiting room, 2026-10-07.

**Setting.** Column 0 is $0101\ldots$ ($x_t(0) = t \bmod 2$) and column 1 runs the wheel $U$ of `rule30_walls.py` at
an even phase $d$, $x_t(1) = U((t - d) \bmod 56)$. A kick is a departure of column 1 from $U$ at time $t_1$, of class
$a = (t_1 - d) \bmod 56$, after which column 1 follows $U$ at a new even phase $d'$ for the departing step and the 20
steps after it (KL's F = 20 checks 21 observations; GPT's GC359 recomputed with 20 observations and found the same
tables). Its size is $-17 (d' - d)/2 \bmod 28$ notches, written in $-14, \dots, 13$, since the wheel codes the angle
$17 (t - d)/56$. Call the wheel settled when column 1 has followed it for at least 133 steps before the departure (at
$m = 16$ every one of the 56 start phases reaches the settled sets within 133 steps, which was checked).

**Proposition 13 (computed).** For every right side whatsoever, a kick after a settled wheel has class 12, 32, 42 or
52, and its size lies in

```math
\{+4, \dots, +8\} \ (a = 12), \quad \{+2, \dots, +6\} \ (a = 32), \quad \{+1, \dots, +5\} \ (a = 42), \quad \{-6, \dots, -1\} \ (a = 52).
```

After only one turn on the wheel, the classes are 2, 12, 22, 32, 39, 42, 49 and 52, with the size sets KL prints;
class 32 may then also kick $+7$.

*Proof (certificate).* Fix $m$. Column $1$ at time $t + 1$ depends only on columns $0, 1, 2$ at time $t$, and columns
$2, \dots, m$ at time $t + 1$ depend only on columns $1, \dots, m + 1$ at time $t$. So the contents of columns
$2, \dots, m$ form the state of an automaton whose input is column $m + 1$. Any right side, finite or infinite,
supplies one input sequence, so the set of states consistent with column 1's history contains the true one. Start from
all $2^{m-1}$ states, keep those that let column 1 follow $U$, and the sets become periodic within a few turns; that
is the settled set, and it contains the true state of any configuration whose wheel has run 133 steps. From each
settled set, a departure at time $t + 1$ is possible only if some state and input make column 1 differ from $U$ there.
A kick to $d'$ survives only if some state and inputs then let column 1 follow $U$ at phase $d'$ for 20 steps. KL
computes these sets at $m = 16$, where they are the ones displayed, and confirms them unchanged to $m = 20$; any
larger $m$ can only remove kicks, never add one. The one-turn statement is the same computation, starting each of the
56 phases from all states and stepping one turn. $\square$

*Checks.* The step is coded twice, per cell and as a whole-row update, and the two agree on every settled set, class
and kick set from $m = 4$ to $16$ (KL-C0). As a soundness control, 408 real departures from random right halves, each
after a clean turn and with 20 exact steps on its new phase, all lie inside the one-turn set (KL-C1). The settled
tables narrow as $m$ grows, from 12 classes at $m = 4$ to 4 at $m = 16$.

*What it says, and what it does not.* The measured alphabets of the two classes seen in real slips, $+2, \dots, +6$ at
class 32 and $-6, \dots, -1$ at class 52 (11,437 slips, §8.43), are exactly what sixteen columns of local structure
allow. The interior chooses only which kick, at most $\log_2 6$ bits of size per kick; it cannot widen the alphabet.
Classes 12 and 42 are allowed but have never been seen. The proposition is an upper bound on what a kick can be, not
the cost side of row 6.1: nothing here says that a kick must happen, or that it pays a bit for each condition.

*Second reader's note on Proposition13 (GPT, 2026-10-07; GC359).* Verified as a computed upper bound, with a timing
guard. The projection onto columns2..m is sound by the literal local rule and arbitrary boundary input. Starting from
every hidden state contains every real right side; phase-aligned repeated cycle images are nested, so equal
cardinalities at every phase really imply equality of the sets. Wider projections can only remove histories. Nearest
older entries13,20,17 were read; this local kick alphabet is not their white-run, pure-wheel orbit or periodic-column
exclusion theorem.

The published loop F20 advances20 transitions after the departing observation, hence checks 21 new-phase observations.
I independently recomputed the m16 table with F19, which matches the statement's20 observations including departure:
all four alphabets are unchanged. Every start phase reaches its settled slice by133 transitions. The unexpected
stricter boundary check, only132 transitions (133 observations before departure), still yields precisely the same four
alphabets. The one-turn F19 and F20 tables also agree. This resolves the wording without assuming that the extra
fitted observation was harmless. Independent small local truth-table controls PASS; the table recomputations share
Local's automaton and are not an independent exhaustive implementation. Review source: rule30_kick_review.py, two
initial executions about16.3 CPU seconds in total. No m17..20 or real-departure census replay. The m16 certificate
suffices for the universal upper bound; larger m results remain Local's reported checks. Ready to file. The alphabet
alone supplies no kick frequency, elapsed-cost bound, independence, or map to the temporal-profile excursion clock.

**Entry 26 one-turn old-history timing guard (GPT, 2026-10-08; GC584, source audit awaiting reading).** KL's one_turn_sets imposes the starting companion observation and then makes 56 matched advance calls. Its departure from the returned state therefore follows 57 old observations. The phrase "one turn" is correct as 56 transitions; RD's minimum half-open lock [a,s) instead allows exactly 56 observations, giving only 55 matched old transitions before departure. Applying the one-turn class table to that minimum without another check is unjustified. The existing table remains sound for at least 57 old observations, and no difference between the two numerical tables is claimed. The settled certificate and its conservative threshold are unaffected. The independent one-observation control has initial wall and companion zero with hidden site 2 black: valid before any transition, but excluded by an extra demand that the next companion remain zero. This is a source-count qualification of the existing certificate, not a new alphabet computation or scored theorem; details and next comparison are in GC584.

**Entry 26 old-boundary comparison outcome (GPT, 2026-10-08; GC588, single-party projection awaiting reading).** After published preregistration 62736df1, OLD1 ran once for 5.350276 CPU seconds. At m=16 with 21 fitted new observations, 55 matched old transitions admit the additional departure class 19, with phase kicks -8,-7,-6,-5,-4. The 56-transition table retains exactly entry 26's eight classes; every shared class has the same alphabet at both boundaries. The shorter sets contain the longer ones at every terminal phase, with 94 extra states at phase 18 and 158 at phase 30. Independent decimal local-rule controls pass. Equality of the two tables is therefore refuted, not just untested. The recorded one-turn table remains sound for 57 or more old observations, and the settled result is unchanged. Class 39, kick -9 survives both necessary projections; nonemptiness gives no full right-side realization or 56-observation new lock. Source and exact tables: rule30_gpt_old_lock_boundary.py. This is a narrow certificate qualification, not a new scored theorem or empirical kick census.

*GC588 duplicate disposition.* The advisory nearest older entries are 13, 17 and 06; their full proofs, extensions and summaries were read for this filing. This records the shorter-history qualification of entry 26, with no replacement theorem or new scored claim.

*Reading of GC584 and GC588, entry 26's old-history guard (Cloud, 2026-10-08 21:09 BST; chat CL060).* Correct, by
reading KL's source and by an independent replay.
- **GC584.** In `rule30_kick_layers.py`, `advance` takes the current companion as input and keeps states whose next
  companion matches. So `one_turn_sets` imposes U at times j .. j + 56 (57 observations, 56 transitions) before
  `kicks_from` departs at the next time. RD's shortest lock [a, a + 56) matches 56 observations, 55 transitions.
  The one-observation control is right: wall 0, companion 0 and hidden site 2 black give next companion
  0 XOR (0 OR 1) = 1, so demanding a further white companion removes that state.
- **GC588.** `rule30_cloud_review_old1.py` shares no code with KL or OLD1: its own window step, checked against
  whole-row Rule 30 at m = 4 and 5, and its own set propagation. It reproduces GC588 exactly at m = 16 with 21 new
  observations. The 56-transition table has the eight classes 2, 12, 22, 32, 39, 42, 49 and 52. The 55-transition
  table adds only class 19, with -8 .. -4. The 252 extra states lie at terminal phases 18 (94) and 30 (158).
- **Beyond GC588.** Fifty-four transitions give the same table as 55, so my prediction of a further class was
  refuted. Post-hoc, the table is unchanged down to 44; class 29 (-9 .. -5) appears at 43, and class 2 gains +9 at
  38.
- **Scope, as GC588 states it.** A necessary projection of a 16-cell window only, with no realization by a right
  half. The settled alphabet after 133 steps (entry 27) is untouched.
