# Plain-word summaries, one per proof

*The source for the "In plain words" section of every page in this folder. One section per proof, headed by its
id; the first paragraph is the one-line hook used in the index. Rebuild with `python3 proofs/build.py`.*

*How it is kept. Whoever adds or moves a PROOFS.md entry writes a first draft here, since the build refuses to run
without one: the hook, then What it says, Why it matters and An everyday picture, with no control names or review
status (the page's status line carries those). Cloud rewrites drafts into plain words for a general reader in
batches. An unusual word gets a plain description where it first appears on a page; in the owner's words, "When
such an unusual noun is used, the reader should be offered a simple description rather than assuming they know
what it means" (2026-10-07).
Pictures are built from concrete things a reader has seen, heard or touched; in the owner's words, "humans are
sensory beings with excellent visual memories - grounding in real world existential nouns is helpful"
(2026-10-07). Plain-words pass done through G198 (2026-10-07); entries after it may still be drafts.
Pictures from C4 on have had Cloud's "what would Gareth say" pass (2026-10-07), awaiting the owner's verdicts
in [picture-pass.md](picture-pass.md).*

## 01
When the middle square is black, the right side cannot be heard on the left at all.

**What it says.** Each step, the left half reads the middle column and column 1. But whenever the middle square is
black, the rule's "or" is already satisfied, so whatever column 1 says is ignored. Column 1 only gets a word in at
the white beats.

**Why it matters.** It halves the channel. With the wall blinking black and white, the right side can influence the
left only every other tick. Every later count of "how much information gets through" starts here.

**An everyday picture.** A door with a buzzer: when the door is already open (black), pressing the buzzer changes
nothing. The buzzer has no memory: at the next white beat, column 1 is heard again. The version with a memory is
proof 03's latch.

## 02
Starting the rhythm one beat later is the same problem, so only one starting beat needs checking.

**What it says.** If a finite seed made the middle column blink black-white from the start, then one tick later it
is still finite and blinks white-black. So every shifted version of a repeating word stands or falls together.

**Why it matters.** It removes duplicate work: to rule out a rhythm, rule out one of its rotations.

**An everyday picture.** A song is the same song whether you start listening at the first bar or the second.

## 03
Column 1 must obey two simple traffic rules, whatever lies further right.

**What it says.** When the middle is white and column 1 is black, column 1 stays black next tick. When the middle is
black and column 1 is black next tick, it must have been white this tick.

**Why it matters.** The right side cannot send just any signal: these two rules already rule out some patterns of
column 1, which is the first narrowing of the channel.

**An everyday picture.** A set-reset latch (the owner's picture). The right side can only press "set"; the wall's
black beat is the "reset" it cannot see. While the wall is white, a set latch stays set however often set is
pressed; a black beat clears it. Next to the blinking wall this gives the rule above: every visible 1 is followed by
a forced 0, like a nerve cell's rest after it fires, or the "never two ones in a row" rule of the codes once used to
write data on magnetic disks.

## 04
Each new bit from column 1 reaches the left exactly once, either as a clean flip or not at all.

**What it says.** The square at depth k on the left depends on column 1's first k bits, and on the newest one in a
very simple way: at a white beat it flips the answer (an exclusive-or), and at a black beat it does nothing.

**Why it matters.** This makes the information exactly countable. Many later results, including the "one bit per
condition" counting, rest on this clean bookkeeping.

**An everyday picture.** A light switch on a long corridor: each new switch either flips the light or is
disconnected; it never does anything in between.

## 05
A steady rhythm in two neighbouring columns cannot last once news from the edge arrives.

**What it says.** Any finite seed has a leftmost black square, its edge, which moves outward one square per tick.
News from the edge travels inward at the same speed, and nothing on the way can stop it. If two neighbouring columns
keep a steady rhythm of period P from some moment on, the rhythm must break before news sent from the edge at that
moment could reach them, give or take two periods.

**Why it matters.** It is Jen's classic theorem (two neighbouring columns cannot both end up repeating, if the seed
is finite) with a stopwatch attached: not just "the rhythm breaks some day" but "by this time", which is the kind of
bound a proof can use. It assumes nothing about the right side, so the rhythm is interrupted whether or not anything
there "sees" the wave coming (the owner's reading). Nor can the wave be blocked: the proof relies on Rule 30 passing
its left input straight through and on the edge always advancing, and a rule that could block news from the left
would fall outside it.

**An everyday picture.** A ripple from the edge of a pond: you can bob in a steady rhythm only until the wave
reaches you, eyes open or shut.

**Checked by machine.** A proof assistant (Lean) has checked the argument.

## 06
If the middle and column 1 both repeat, the left half can never show a white gap more than two periods wide.

**What it says.** Suppose the middle column and column 1 repeat every P ticks. Then, at the starting moment, every
stretch of white squares across the left half is at most 2P − 2 squares wide. The units differ: the gap is measured
across space, in squares, and the period in time, in ticks.

**Why it is true.** Every column of the left half inherits the same repeat. A wide white gap forces a white triangle
beneath it, and a gap of 2P − 1 or more makes the triangle deep enough that some column stays white for a whole
period. A repeating column that is white for one whole period is white for ever. That permanent white then spreads
right, column by column, through the latch of C2, until it would silence the middle column, which is still beating.

**Why it matters.** A finite left half needs an endless white stretch. This shows repeating columns cannot give one,
with a sharp number attached. It counts squares and ticks, not seconds, so it holds at any speed the pattern is
played back (the owner's question; see G98).

**An everyday picture.** Music on a loop: if it is silent for one whole play-through, it is silent for ever. A white
gap two loops wide guarantees such a silence somewhere, and silence spreads until it reaches the drummer in the
middle, who is still playing.

**Checked by machine.** A proof assistant (Lean) has checked the argument.

## 07
A pattern can only repeat if it is shorter than the distance to the edge.

**What it says.** If two neighbouring columns show the same block of n values twice, at times a and a′, then n is at
most the edge's distance at the later time, L + a′. The reason: a block of n values is a fingerprint of the n − 1
squares beside the columns, so seeing it twice means that stretch of the row looked the same both times. But the
seed's edge moves outward one square per tick, so the later row has a black square out where the earlier row was
white, and a block long enough to reach it would see the difference.

**Why it matters.** Repeats are the raw material of periodicity, and this caps them using only the seed's size. It
depends on the room growing (the owner's point): in a closed box, such as Rule 30 on a ring, every pattern must
eventually come back and then repeat for ever (C6), like light between perfect mirrors. A finite seed escapes that
only because the region it disturbs keeps widening. How fast the room grows matters too (the owner's follow-up).
Rule 30's edges move out one square per tick, the fastest anything can travel. News from the edge therefore always
arrives, but ever later, while news from the centre heading left, at about a quarter of that speed (C4), never
catches the edge.

**An everyday picture.** Two photographs of a growing town, taken years apart, can match only through a frame too
narrow to include the new outskirts.

**Checked by machine.** A proof assistant (Lean) has checked the argument.

## 08
In the band near the edge, two neighbouring diagonals can never both fall silent for ever.

**What it says.** Near the left edge the pattern runs along diagonals, and the outermost diagonal, the edge itself,
is black at every tick. If one diagonal turns white for ever, the one two steps further in becomes a latch (C2):
once lit it stays lit, so it ends up black for ever. And two neighbouring diagonals cannot both be white for ever:
their darkness would pass back, diagonal by diagonal, all the way to the edge, which is never dark.

**Why it matters.** It gives the edge band a rigid structure, which later results use to find black squares where a
counterexample would need white ones. The proof separates a lamp switched off locally, which is allowed, from a
power cut, which would have to reach back to the supply (the owner's distinction).

**An everyday picture.** Lamps fed in a chain from a power station that never fails: any single lamp can be switched
off, but two neighbours dark for good would mean the power had failed all the way back to the station, and it never
does.

**Checked by machine.** A proof assistant (Lean) has checked all three parts.

## 09
The diagonals near the edge each keep a steady beat, and going deeper the beats keep dropping by octaves, for ever.

**What it says.** Near the edge, each diagonal eventually settles into a steady repeating pattern. But the repeats
get longer as you go deeper, doubling again and again without end, so no single period fits them all. There are
infinitely many diagonals that go white for ever and infinitely many that go black for ever.

**Why it matters.** It proves a mechanism Rowland observed: the edge keeps producing fresh structure. Several
exclusions below need a black diagonal deeper than any given depth, and this supplies it. A doubling is itself a
regular pattern (the owner's point); what the lemma rules out is one common period. No finite run could confirm it
either: a period of 2^k ticks needs at least that long to show itself, so a measurement hears only the first few
octaves, and the proof carries the rest.

**An everyday picture.** Notes dropping an octave at a time, each one steady and each an octave below the last. A
scale that keeps going down soon leaves human hearing behind (about ten octaves cover all of it), but it never stops
being a scale (the owner's reading).

**Checked by machine.** A proof assistant (Lean) has checked it: the periods never stop growing, and there are infinitely many stripes that end white and infinitely many that end black.

## 10
A repeat leaves a white stripe behind it, and a black diagonal there caps the repeat.

**What it says.** If two neighbouring columns repeat a block of n values, the later row must copy the earlier row
across the n − 1 squares beside them (07). The earlier row was blank beyond its edge, so the copy carries that blank
margin into the later row, a white stripe across a range of diagonals. A black diagonal inside that range would
contradict the copy, so it limits how long n can be.

**Why it matters.** It joins the repeat bound (07) to the edge band (08, 09): the band's black diagonals become
measuring sticks for repeats. A block of the two columns is a fingerprint without collisions of the squares beside
them, which is why a repeat can be checked at all.

**An everyday picture.** A forged page (the owner's forensic reading): a passage copied from an older, smaller
document brings the older document's blank margin with it. If the new page has ink where that margin falls, the copy
is exposed.

**Checked by machine.** A proof assistant (Lean) has checked the argument.

## 11
A column 1 that starts by almost repeating itself, at bigger and bigger scales, is fatal.

**What it says.** If column 1's visible bits begin with a near-copy of themselves (a block followed by itself, up to
a fixed error), at ever longer lengths, then the left half cannot be finite.

**Why it matters.** It rules out a whole family of "nearly periodic" inputs at once, not just exactly periodic ones.

**An everyday picture.** The opening of a note, its attack, is where you hear which instrument made it, before the
sound settles into its steady tone; synthesisers that splice a sampled attack onto a synthetic tone make you hear
the attack's instrument (the owner's reading). A note that is already repeating itself from its first instant, at
every scale you listen at, has no attack, so no real instrument, one with edges, struck it.

## 12
Once the edge band settles into its rhythm, it has no long white gaps.

**What it says.** If the diagonals near the edge have been repeating with a common period P for at least P steps,
then no white run inside that band is longer than 2P − 1 (first proved as 2P; sharpened on 2026-10-10).

**Why it matters.** The settled band does have white gaps, but only short ones, and the next theorem (13) uses that
limit against repeats.

**An everyday picture.** A well-kept fence still has gaps, left on purpose: hedgehog holes, about 13 centimetres
square, cut so that small animals can pass through and are not trapped (the owner's reading). The settled band is
that fence. Its white gaps are never wider than 2P, so only something small can get through; page 13 shows that a
long repeat, which needs a white stripe roughly as long as itself (page 10), is too big.

**Checked by machine.** A proof assistant (Lean) has checked it, in the sharper form: no gap longer than 2P − 1.

## 13
The white stripe a repeat leaves cannot sit inside the settled band.

**What it says.** Combining 10 and 12: if the band near the edge is settled, a repeat's white stripe would have to
lie in it, and it cannot be longer than 2P − 1 there, so the repeat is bounded.

**Why it matters.** A sharper cap on repeats, from the edge band's own regularity.

**An everyday picture.** Driving round a busy car park: spaces keep opening as cars leave, but each is small and
gone within moments, and you pass the car about to leave just before it goes, so a driver who needs a long space
where they are can circle for ever while spaces are made all around them (the owner's reading). The settled band is
that car park. White gaps are born in it all the time, but none is wider than 2P or older than P steps (12), so the
long white stripe a repeat needs is never there at the moment and place it is needed.

**Checked by machine.** A proof assistant (Lean) has checked it, in the sharper form with 2P − 1.

## 14
A perfectly regular wheel, never nudged, cannot produce the pattern.

**What it says.** If column 1 is the trace of a wheel turning by a fixed irrational angle (a "Sturmian" sequence,
like the pattern of a clock hand passing a mark), the left half is never finite. With Jen's theorem (two
neighbouring columns cannot both end up repeating, if the seed is finite) for rational angles, whose wheels simply
repeat, no un-kicked wheel of any speed works.

**Why it matters.** Column 1 next to a blinking wall really does behave like a wheel with occasional kicks. This
proves the kicks are necessary: any counterexample must come from the kicks, never from the turning alone.

**An everyday picture.** No metronome is ever truly left alone: friction in its own pivot drains its swing and
nudges its beat, with nobody touching it (the owner's reading). Theorem E is Rule 30's version. A perfectly regular
wheel cannot come from a finite seed, so column 1 must slip, and the slips come from Rule 30's own cells, not from
anyone outside.

## 15
The same holds for almost every wheel speed, whatever pattern of marks it passes.

**What it says.** Theorem 14 used one mark; this allows any finite set of arcs as marks. For almost every rotation
speed, no such coding gives a finite left half.

**Why it matters.** It widens 14 from one simple kind of wheel to nearly all of them. The speeds left out are those
that never come close to repeating for long, such as the golden ratio; for some patterns of marks they are still
open (G132).

**An everyday picture.** Notches are how a wheel grips: like a ratchet's teeth, each one catches as it comes round
(the owner's reading). Here the notches are the ends of the marks, the only places where the wheel's near-repeating
rhythm can be broken. A finite seed needs that rhythm caught again and again, each catch coming within about twice
the time of the last. But a typical wheel sometimes coasts almost exactly round to where it was, for a very long
time, and then any fixed number of notches comes up too rarely: the wheel slips past the catch, and the seed is
exposed.

## 16
In Rule 30's simpler cousin, Rule 90, the blinking middle is impossible, proved with Pascal's triangle.

**What it says.** Rule 90 just adds neighbours: a square turns black when exactly one of its two neighbours was
black. Started from one black square, it draws a Sierpinski triangle (described below). The same picture appears in
Pascal's triangle, the triangle of numbers in which each is the sum of the two above it, if the odd numbers are
coloured black. At the times that are powers of 2 (1, 2, 4, 8, ...) a single square's pattern is white everywhere
except at its two far ends. So once those times are larger than the seed, the middle is white twice in a row, and it
cannot blink for ever.

**Why it matters.** It shows the kind of proof that works for the linear cousin, and why Rule 30 is harder: its rule
mixes that adding with an "or" (black if either square is black), and the clean arithmetic is lost.

**An everyday picture.** Draw a triangle, join the midpoints of its sides and cut out the middle piece; then do the
same to each of the three smaller triangles left, and so on for ever. That is Sierpinski's triangle, the pattern
Rule 90 draws. Its holes open at the rows numbered by powers of 2, and each time the newest and biggest one is an
empty triangle right at the centre, which a finite seed is soon too small to fill.

## 17
If both the middle and column 1 eventually repeat, the left half cannot be finite (Jen's theorem).

**What it says.** Two neighbouring columns that both repeat from some point on force infinitely many black squares
on the left. The reason comes in three steps. The repeat spreads left: every column to their left must repeat with
the same loop. Far out, where the seed never reached, a column starts white for a whole loop, so it stays white for
ever. And two columns that are white for ever make the next one in white for ever too, all the way back to the
middle, which was supposed to be beating.

**Why it matters.** It settles every periodic column 1 at once. Since a finite seed makes column 1 irregular, the
open case is exactly the irregular one.

**An everyday picture.** A track set on repeat: if its first full loop was silent, it is silent for ever. The two
steady columns set every column to their left on repeat; far out, the first loop was silent; and the silence works
its way back in, one column at a time, until it reaches the beat that started it.

**Checked by machine.** A proof assistant (Lean) has checked it for patterns grown from an actual starting row. The wider form, for prescribed columns, is checked by hand only.

## 18
Next to a blinking wall, Rule 30's sibling Rule 210 behaves exactly like the simple cousin Rule 90.

**What it says.** With the wall blinking, every black square of Rule 210's forced left half sits on one colour of a
checkerboard, and on that checkerboard the rule reduces to Rule 90's simple addition.

**Why it matters.** It explains why the left-side conjecture fails for Rule 210 but may hold for Rule 30: Rule 210's
nonlinearity switches itself off there, and Rule 30's does not.

**An everyday picture.** A dancer who only ever lands on the black squares of a chessboard never meets the white
ones, yet must step over a white one with every move, even without touching it (the owner's reading). That is the
proof. Each step of Rule 210's rule looks at the square in between, and its one non-adding part, an "and not", asks
whether that square is black. Whenever the answer matters, the square is on the white colour and so empty, so the
step never trips, and what is left is Rule 90's plain addition.

## 19
A counterexample would have to be almost frozen: the right side can only whisper.

**What it says.** Next to a blinking wall, every column on the left carries at most 0.0646 bits of new information
per tick (a bit is the answer to one yes-or-no question), a certified bound computed exactly.

**Why it matters.** A counterexample cannot look random on the left; it must be nearly frozen. It shrinks the
haystack the needle could be in.

**An everyday picture.** A walkie-talkie that can send about six yes-or-no answers every hundred seconds: not quite
enough for one letter of the alphabet a minute.

## 20
We followed the pure wheel leftward until it repeated, about 15 billion columns out, and checked: it fails.

**What it says.** With column 1 exactly the never-kicked wheel, read the rule leftward one column at a time: each
pair of neighbouring columns fixes the next. After a lead-in of 32,896,298 columns the pairs enter a loop of
15,009,104,432, and the loop is not all white, so the left half is never finite. Certified by computation.

**Why it matters.** An exact check of the single most important special case, with a committed program anyone can
rerun.

**An everyday picture.** A combination lock's dial turns either way, so whatever you do can be undone, and turning
it always brings it back round to where it started (the owner's reading). This dial cannot turn back: each step is
forced, and some steps forget where they came from. So its path is shaped like the letter rho, ρ: a long lead-in it
can never return to, then a loop for ever, and the loop is never all white.

## C1
While the middle column stays black, the left half next to it is a fixed checkerboard, whatever the right side does.

**What it says.** Suppose the middle column is black for a stretch of k + 1 ticks. Then the first k squares to its
left, at the start of that stretch, alternate white, black, white, black, and column 1 has no say in it.

**Why it matters.** Black stretches are where the right side is silenced (proof 01). This lemma says what the left
half looks like there: something fully known. A candidate's left half is therefore predictable in those places, and
GPT's later results on slow walls, walls with long black and long white stretches (E4, E5), build on it.

**An everyday picture.** A rubber stamp: however the neighbour shouts, every black stretch presses the same
chessboard into the paper.

**Checked by machine.** A proof assistant (Lean) has checked it.

## C2
While the middle column stays white, column 1 can switch on but never off.

**What it says.** When the middle square is white, column 1's next value is "column 1 or column 2". So across a
white stretch of the wall, once column 1 turns black it stays black until the stretch ends.

**Why it matters.** It turns column 1 into a one-way switch during white stretches, which sharply limits what the
right side can say there. Walls with long white and long black stretches ("slow walls") are studied with this tool.

**An everyday picture.** A set-reset latch (the owner's picture): column 2 can press "set", and pressing it again
changes nothing; only a black beat of the wall, a button the right side cannot reach, resets it. Proof 03 is the
same latch with its reset written in.

**Checked by machine.** A proof assistant (Lean) has checked it.

## C3
A run of white squares shrinks by exactly one square at each end per tick, so Rule 30's white triangles are perfect.

**What it says.** A run of two or more white squares with black on both sides becomes, one tick later, the same run
with one square trimmed from each end. So every white triangle in Rule 30 is an exact isosceles triangle (its two
sloping sides equal), fixed by the row, place and width where it is born.

**Why it matters.** The white triangles are the most visible structure in Rule 30, and this makes them exactly
predictable once born. The gaps in the record's "ladder", its measurements of the longest white run the left half
can be held to, are the bases of such triangles. It was also checked on a million runs; Rule 110, a neighbouring
rule of the same kind, breaks it.

**An everyday picture.** The triangles on the shell of the *Conus textile* snail; or a sheet of ice melting evenly
in from both edges.

**Checked by machine.** A proof assistant (Lean) has checked it.

## C4
How fast news travels leftwards in Rule 30 is an exact bookkeeping identity: full speed, minus the times it gets
squashed.

**What it says.** Compare two copies of Rule 30 that initially differ at finitely many cells and watch the leftmost difference. Read along
the diagonals, the difference never moves backwards, and it is held back only when the square just below it on the
diagonal is black. So its average speed equals full speed minus (how often it is held back) times (how far it is set
back each time). The measured numbers, 0.41 and 1.84, give a speed of about a quarter. If the copies agree below and on a diagonal that turns white
for good, a difference immediately above it cannot heal.

**Why it matters.** It turns a measured speed into an exact identity, and explains why the band of white diagonals
left of the middle acts as a one-way wall for information.

**An everyday picture.** A shopper walking down a busy aisle at full pace, knocked back a step or two each time a
trolley cuts across them: their average pace is full pace minus the knocks. A white diagonal is a one-way turnstile:
once through, nobody pushes them back.

## C5
In a random row, Rule 30 keeps the row random, so white triangles of each width appear at an exact, predictable rate.

**What it says.** Start from a row of fair coin flips. Rule 30 keeps it a row of fair coin flips: it never
"unshuffles". So the number of white triangles with a top of width L, per square, is exactly 3 / 2^(L+4): each extra
square of width halves the rate.

**Why it matters.** It is a statement of the kind the prize's second problem asks for (how often things happen),
proved for random rows. The single-cell pattern matches it to about 0.05% in its central region, a measured sign
that the famous pattern behaves randomly there.

**An everyday picture.** A bowl of coins, stirred: stirring never sorts the heads from the tails, so a run of L
heads in a row turns up at the rate of a half multiplied by itself L times, however long you stir. Rule 30 is that
kind of stirring.

## C6
On a ring with a prime number of squares, any rhythm that is rare must be a pattern travelling round the ring.

**What it says.** Wrap Rule 30 round a ring of p squares, p prime. Turning the ring by one square commutes with the
rule, so it takes each repeating cycle to a cycle of the same length. Because p is prime, a cycle either comes in a
family of p copies or is turned into itself. So a cycle whose length occurs fewer than p times is a glider: turning
the ring does the same as running time on. The census found every cycle length distinct at p = 13, 17, 19, 23 and
29, so there every cycle is a glider. GPT's G55 later made this an exact criterion.

**Why it matters.** It is an exact, structural fact about Rule 30 in small closed worlds, of the kind the record
wants to tell apart from mere measurement.

**An everyday picture.** A Mexican wave in a round stadium: if a pattern of standing fans is the only one of its
kind, then moving one seat round can only show you the same pattern a moment later. It is a wave travelling round
the ring.

## C7
The first three columns left of the middle copy or flip visible bits; the fourth introduces a formal product.

**What it says.** The inverse rule next to the blinking wall gives copy, flip and delay formulas through column −3. Its arbitrary-input formula for column −4 combines consecutive visible bits with an "and" gate.

**A domain matters.** Actual right-side histories cannot have consecutive visible ones, so that fourth-column product is always zero. GPT's second-reading audit derives affine formulas through column −6 on this restricted domain. Column −7 then combines visible bits separated by one intervening bit; four admissible prefixes show that interaction survives. Local independently verified the audit; a transcribed witness list was corrected.

**Why it matters.** A product in a formal formula can disappear when the inputs are constrained. The audit locates a surviving interaction without claiming the entire evolution is linear or supplying the finite left tail needed for a prize counterexample.

**An everyday picture.** An "and" gate wired to two signals that can never both be on produces only zero. A later gate connected to different signals can still combine them.

## E1
GPT found exactly which stretches of a row erase all memory when you rebuild the row before it.

**What it says.** You can rebuild an earlier row from a later one, square by square, keeping two squares of memory
as you go (four possible states). Some stretches of the later row send all four states to the same one, whatever you
started with: they "reset" the rebuild. GPT proved that a stretch resets exactly when it contains white, then a run
of black squares of length 1, 4, 7, 10, ..., then white, then any square. The shortest are 0100 and 0101. GPT's
first guess was wrong, and the failure is kept on record.

**Why it matters.** A reset means two different pasts become identical from that point on: information from further
away is wiped. This is an exact measure of when the right side's influence is forgotten.

**An everyday picture.** The reset button on a latch circuit, or on a broadband router: whatever state it was in,
after the reset it is in the same one, and nothing about before survives.

## E2
A single changed bit from the right side is forgotten at a steady rate as you go back in time: three squares per step.

**What it says.** Take a wall with one white beat (a "hole") followed by a long run of black. Change column 1 only
at that hole. Going back r rows, the two versions of the left half agree everywhere from depth 4r + 4 on, and the
first part of that agreement is a shared checkerboard. Each step back costs the protected checkerboard three
squares.

**Why it matters.** It measures exactly how quickly one bit of news from the right fades in the left half, a precise
piece of the "how much can get through" accounting.

**An everyday picture.** A candle clock, a candle marked with the hours: each hour it burns down by the same length
to the next mark, until there is nothing left. The protected checkerboard loses three squares for every step back.

## E3
For walls with one white beat per period, checking three columns on the right rules out no more than checking two.

**What it says.** Instead of asking for a whole right half obeying Rule 30, ask only that the first k columns obey
it, with the next column free (a "relaxation of width k"). Which patterns of column 1 at the white beats are then
possible? For walls with one white beat per period p, widths two and three give the same answer: for even p, never
two black in a row; for p = 3, never black, white, white; for odd p of 5 or more, anything.

**Why it matters.** It tests whether the right side's own rules squeeze the channel. Here the third column adds
nothing visible, even though it changes what happens out of sight.

**An everyday picture.** Checking an alibi with a third witness: they add nothing to what the first two saw at the
door, although they saw other things further down the street.

## E4
On a slow wall, the left half near the middle carries only "when did the switch go on", so there are just a + 1
possibilities.

**What it says.** Take a wall that is white for a ticks, then black for b ticks, repeating. The first a + b − 1
squares of the left half at the start are fixed by column 1's a bits during the white ticks. Those bits can switch
on only once (C2), so exactly a + 1 different beginnings of the left half are possible.

**Why it matters.** It counts exactly how little a slow wall lets through near the middle: only the moment of one
switch, about log2(a + 1) bits per period.

**An everyday picture.** A light that may be switched on once during a meeting: the only news it carries is when.

## E5
A long enough black stretch wipes the slate: the left half becomes a known checkerboard whatever came before.

**What it says.** If the wall is black for b ticks, after any a ticks before, and b is at least 3a + 1, then the
left half at the start is a checkerboard from depth 4a to depth a + b − 1, whatever column 1 does before, during or
after.

**Why it matters.** It gives a protected band where the right side cannot reach, with no assumptions about the right
side at all.

**An everyday picture.** Fresh snow covering every track: after a long enough fall, you cannot tell who walked there
before.

## E6
For walls with one white beat per odd period of 5 or more, even four columns of the right side allow every pattern.

**What it says.** Ask the first four columns on the right to obey Rule 30 (the width-four relaxation). For walls
with one white beat per odd period p of 5 or more, every sequence of column-1 bits at the white beats is still
possible. GPT predicted the opposite at width four, and the failed prediction is kept.

**Why it matters.** If Rule 30's own consistency rules out these walls at all, the evidence first appears at width
five or more. It tells future searches where not to look.

**An everyday picture.** A front-door lock with five spring-loaded pins: a key that lifts the first four pins to the
right height still tells you nothing, because if it is the wrong key, only the fifth pin, or a later one, will stop
it turning.

## E7
Jen's classic argument works from the left half alone, without assuming anything about the right.

**What it says.** Jen's theorem says two neighbouring columns that both repeat force infinitely many black squares.
GPT showed the same argument works in the setting the record studies: a forced left half that starts out eventually
white, with no assumption that a right half exists. It holds for Rule 30 with any repeating, non-constant wall, and
for its sibling Rule 210 with the blinking wall.

**Why it matters.** It removes a hidden assumption, so the tool can be used exactly where the record needs it.

**An everyday picture.** The water-meter test for a leak: turn off every tap in the house, and if the meter still
turns there is a leak, proved without digging up a single pipe outside.

## F1
After k Collatz steps, a number's remainder in base 2 has become a remainder in base 3, and the rest passes through
untouched.

**What it says.** Write a starting number as 2^k times m plus a remainder r. After k steps, with a odd steps among
them, it becomes 3^a times m plus the value r itself reaches, which is below 3^a. This is Terras's identity (1976),
restated.

**Why it matters.** It is the Collatz twin of the forced left half, and the avenue Collatz has that Rule 30 lacks:
after the free bits, the state is an explicit number. All the counting work of GPT's G39 to G75 builds on it.

**An everyday picture.** Changing pounds into euros: the notes are converted at a fixed rate, a straight
multiplication, while the loose change is counted on its own and comes back as coins worth less than one new note.

## F2
A Collatz number that ran off to infinity would have to change its step pattern endlessly: it could not loop or
repeat.

**What it says.** A published theorem (Dubickas, 2009): if an orbit grew for ever, its sequence of odd and even
steps would have at least about 1.7 n different patterns of length n. Repeating or nearly repeating step patterns
are impossible.

**Why it matters.** It is Collatz's counterpart of Jen's theorem (two neighbouring columns cannot both end up
repeating, if the seed is finite) for Rule 30: it rules out the simple counterexamples and says any real one must
look irregular.

**An everyday picture.** A getaway car that can never settle into a fixed route: any repeating loop would get it
caught.

## G39
Insisting that a Collatz step pattern "survives" at every step can raise any probability by at most a factor of its
length.

**What it says.** Take all patterns of T odd-and-even steps with a given number of odd steps and an overall growth
factor above 1. At least one in T of them keeps the growth factor above 1 at every step along the way. So
restricting attention to the surviving patterns can make any event at most T times more likely than among all
patterns.

**Why it matters.** It lets simple estimates about random step patterns be carried over to surviving ones at a
small, known price. It is a basic transfer tool for the Collatz count (see the primer).

**An everyday picture.** A year's bank statement that ends in credit: read it round in a circle, starting just after
the day of the lowest balance, and the running total never drops below where you began.

## G40
Swapping neighbouring odd and even steps shifts a Collatz number's final value by an exact, predictable amount.

**What it says.** Group a step pattern into pairs: two evens, two odds, or a mixed pair. Turning a mixed pair round
(odd-even into even-odd) changes the final value, counted in base 3, by an amount that depends only on where the
pair sits. So the spread of final values over all the swaps is built from independent pieces, and its frequency
fingerprint is a product of simple factors.

**Why it matters.** The Collatz count needs final values to spread out evenly. This gives an exact handle on that
spreading, the Collatz analogue of a random walk built from independent steps.

**An everyday picture.** A mixing desk where each channel's mute button adds or removes that channel's fixed level
on the master meter: the spread of possible readings is built from each channel's own on-or-off.

## G41
Typical surviving Collatz patterns have plenty of those independent switches: a fixed fraction of their length.

**What it says.** At typical proportions of odd steps, almost all surviving step patterns of length T contain a
number of mixed pairs proportional to T; the exceptions are rarer than any fixed power of 1/T.

**Why it matters.** G40's switches are useful only if there are many of them. This shows there are, in the typical
case.

**An everyday picture.** A long run of coin tosses is full of heads-tails and tails-heads pairs; only freak runs
avoid them.

## G42
Many independent switches are still not enough: one particular frequency can stay perfectly in tune.

**What it says.** GPT found an exact family where one frequency of the final values does not average out, however
many free pairs there are: its strength stays above 0.99.

**Why it matters.** It closes a tempting short cut ("many free pairs, so the values spread evenly"). An honest no-go
like this saves later work and shapes the next attempt.

**An everyday picture.** Pushing a swing: a hundred pushes from a hundred different people still add up if every one
lands in time with the swing. More pushes do not cancel that one rhythm.

## G43
An exact translation table between base 3, where the Collatz state lives, and odd or even, which decides the next step.

**What it says.** Suppose you know a number's remainder after dividing by a power of 3, and you want to know whether
the number is odd. GPT wrote down exactly how much each frequency of the remainder's distribution contributes to
that question, with an explicit formula.

**Why it matters.** F1 puts the Collatz state in base 3, but the next step is decided by base 2. This is the exact
bridge between them, and it says which frequencies matter most.

**An everyday picture.** The sliders of a graphic equaliser, read the other way round: for one sound, they show how
much each band of frequencies contributes to it. Here the sound is the answer odd-or-even, and the bands are the
patterns in a base-3 remainder.

## G44
A remainder modulo 3^a can imitate only so many fair coin tosses; ask for more and the repetition shows.

**What it says.** If the remainder is uniformly random, the next d odd-or-even steps look like fair coin tosses,
with an exact error formula, as long as 2^d is much smaller than 3^a. Beyond that the steps are fixed by the
remainder and carry no new randomness. GPT also showed one tempting comparison with coin tosses fails for long
patterns.

**Why it matters.** It is an exact information budget: the Collatz state after the free bits can pay for about 1.58
a fair coin tosses and no more.

**An everyday picture.** A shuffled deck of cards holds about 225 coin tosses' worth of chance: there are about 2 to
the power 225 ways to order it. Read more tosses than that off it and the later ones are already decided by the
earlier.

## G45
For a given step pattern, the numbers that follow it and stay above their start are a fixed class with a height limit.

**What it says.** All numbers that follow a given pattern of odd and even steps share one remainder modulo a power
of 2. If the pattern's growth factor dips below 1, such a number can still stay at or above its start, but only if
it is small: below a ceiling the pattern fixes exactly.

**Why it matters.** It separates two notions the count uses: "the growth factor stays above 1" and "the number
actually stays above its start". They differ only for small numbers, below the ceilings.

**An everyday picture.** A soft-play area with a height bar at the door: only children under the bar get in, and the
bar is set by the play area, not by the child.

## G46
Those height limits can be as large as you like, because powers of 3 sometimes come very close to powers of 2.

**What it says.** For patterns of k odd steps followed by just enough even steps to dip below 1, the ceiling can be
arbitrarily large. Powers of 3 now and then fall just short of a power of 2, because log2(3) is irrational. GPT also
corrected a rounding short cut in counting.

**Why it matters.** It rules out a uniform bound on all ceilings, so any control of the exceptions has to come from
finer arithmetic (G69 supplies it).

**An everyday picture.** The circle of fifths never quite closes. Stacking fifths comes back close to an octave of
the starting note now and then, sometimes falling just short of it (after 5, 17, 29 and 41 fifths), and those near
misses can be as close as you like. Each one that falls short gives a large ceiling here (Local's observation in
chat L039, from the owner's Coprime work).

## G47
For those patterns, surviving to the end would mean coming back to exactly the starting number: a cycle.

**What it says.** For the "k odd, then even" patterns, a starting number survives the whole pattern only if it ends
exactly where it began.

**Why it matters.** Surviving through a dip below 1 is then possible only by a cycle, and the only known positive
Collatz cycle is 1, 2, 1. It is a clean link between the count and the cycle question.

**An everyday picture.** A boomerang thrown so that it can never land beyond you: the only way it does not fall
short is to come back exactly to your hand.

## G48
A simple formula for how far above or below its start a number ends after its first dip.

**What it says.** For any pattern whose growth factor first drops below 1 at its last step, the gap between end and
start is a fixed number minus a fixed multiple of how far the start sits up its class. A gap of zero is a return to
the start; a positive gap means it ended higher.

**Why it matters.** It turns survival through a first dip into a short, exact calculation, which G48's certificate
(next page) then carries out.

**An everyday picture.** A prepayment electricity meter: the credit left is the top-up minus a fixed price per unit
used, so whether you are still in credit at the end is a single subtraction.

## G48C
A computer certificate: every number above 1 whose growth factor first dips below 1 within 16 steps really does drop
below itself then.

**What it says.** Every step pattern up to length 16 was checked, together with every number in each pattern's
class, by G48's formula. Apart from the number 1, every number whose growth factor first dips below 1 by step 16
does fall below its start at that same step.

**Why it matters.** It confirms, for short horizons, that the growth factor and actual survival agree once you leave
out the trivial cycle. It is a finite result, not a theorem for all horizons.

**An everyday picture.** Testing every key on a short key-ring: none opens the door except the one marked "1".

## G49
A Collatz-like test bed, multiply by 3/2 and round down, keeps the arithmetic but asks a different survival question.

**What it says.** The map n to floor(3n/2) has the same exact arithmetic as Collatz (F1 and its relatives carry
over). But every number from 2 up simply grows, so "staying above the start" is trivial. The real question (the
"Antihydra" Turing-machine problem) is a counter that gains 2 on even steps and loses 1 on odd ones. With fair coins
such a counter survives for ever with probability at least about 0.38, rather than dying out.

**Why it matters.** It shows exactly which of the record's Collatz tools transfer to this famous unsolved test bed,
and which do not.

**An everyday picture.** The same engine in a different race: the arithmetic runs just as before, but the question
becomes a gambler who wins two pounds on heads and loses one on tails. Does the money ever run out? With a fair
coin, more than a third of the time it never does.

## G50
Mahler's 3/2 problem needs two conditions at once, and its known cellular-automaton form (a rule of Rule 30's kind,
repainting a row of squares) works differently from Rule 30.

**What it says.** Mahler asked whether some number, multiplied by 3/2 again and again, always has a fractional part
below a half. GPT showed this needs both an integer step pattern and a fractional-part condition. For example, two
odd steps in a row are forbidden, and a repeating pattern can satisfy the fractional part while matching no whole
number. The known cellular automaton for the problem is not of Rule 30's "left-invertible" kind, where the right
side and the middle fix everything to the left (the crossword quirk of the primer).

**Why it matters.** It sets out honestly what transfers from the record's methods to Mahler's problem, and warns
where it does not.

**An everyday picture.** A lock with two dials: getting one right is not enough.

## G51
The exact finite form of Mahler's two conditions over T steps: a class of whole numbers and a window of fractions.

**What it says.** For a pattern of T steps, the whole-number starts all leave one remainder on division by 2^T, and
the allowed starting fractions form one exact interval. Both are written down explicitly.

**Why it matters.** It turns Mahler's question into a finite check for each length, the kind of statement a computer
can test or a proof can iterate.

**An everyday picture.** A delivery address: a postcode that fixes the street, and a range of house numbers along
it, both written down exactly.

## G52
Near-repeats in column 1 rule out a finite seed for every repeating wall, not only black-white.

**What it says.** Corollary F (proof 11) says that, for the blinking wall, a block of column 1 repeated almost at
once is fatal to a finite seed. GPT extended this to every repeating wall, provided the repeats line up with whole
periods of the wall, and later covered the case of an initially empty left half.

**Why it matters.** It widens one of the record's sharpest tools from one rhythm to all of them.

**An everyday picture.** An echo that comes back too soon gives away a wall that is too close, whatever the shape of
the room.

## G53
The information limit on the left half can be computed one period of the wall at a time.

**What it says.** For a wall that repeats with period p, group column 1's visible bits by period. The rate at which
new information reaches any fixed column on the left is at most the rate of these groups divided by p.

**Why it matters.** It puts the squeeze (proof 19) into a form that works for every repeating wall.

**An everyday picture.** Counting deliveries by the van-load: a depot that sends one van a week can deliver to a
street no faster than one van-load a week, however the parcels are packed.

## G54
A simple two-by-two calculation bounds the information reaching the left half, for every repeating wall.

**What it says.** List the gaps between the wall's white beats. Each gap gives one of three small 2-by-2 tables;
multiply them together. The size of the product (its largest eigenvalue) gives a ceiling on how fast information can
reach any column on the left.

**Why it matters.** It is a quick, explicit bound for every rhythm at once. It is coarse, so it does not close the
gap on its own.

**An everyday picture.** A train of gears, each with a known ratio: multiply the ratios along the train and you know
the most the last gear can turn for each turn of the first. It is a ceiling, not the actual speed.

## G55
On a prime ring, every Rule 30 cycle is a lifted copy of a simpler cycle, which explains when cycle lengths are
distinct.

**What it says.** Treat patterns that differ only by turning the ring as one. Each cycle of these classes either
lifts to p separate cycles of the same length or to one cycle p times as long, depending on whether the pattern
drifts round the ring. So all cycle lengths are distinct exactly when every class cycle drifts and no two class
cycles have the same length.

**Why it matters.** It turns the census's observation (C6) into an exact criterion, and shows that the claim cannot
hold for all primes (it already fails at 7 and 11).

**An everyday picture.** A dance on a round floor: either the dancers come back to the same spots each time round,
or they shift along and need p rounds to return.

## G56
A "centre of mass" for patterns on a prime ring tells exactly how far a cycle drifts.

**What it says.** Give each black square its position, and average the positions in clock arithmetic on a dial of p
hours. This "phase" moves by exactly one when the ring is turned by one, so it measures drift. A cycle's total drift
is the sum of the phase changes along it.

**Why it matters.** It makes G55's drift computable step by step. Whether the drift can be zero for Rule 30 is still
open.

**An everyday picture.** A clock dial of p hours on which each black square adds its own hour: the total moves on by
exactly one hour when the ring is turned by one square, so watching that total shows how far the pattern has
drifted.

## G57
How a Rule 30 pattern drifts round a prime ring is set exactly by where its "and" operations happen.

**What it says.** Rule 30 is a simple sum of neighbours plus a correction wherever two neighbouring squares are both
black. GPT showed that the drift of G56's phase is an exact formula in that correction: where the correction sits,
weighted by position.

**Why it matters.** It ties the drift to Rule 30's non-linear part, the part that makes it hard. It does not yet say
the drift is never zero.

**An everyday picture.** A shopping trolley with one sticky wheel: left alone it would roll straight, and every
swerve it makes comes from where and when that wheel catches.

## G58
For Rule 30's sibling Rule 210, GPT built an explicit left half that keeps a whole family of walls going.

**What it says.** Take walls that are white at every even tick and anything at odd ticks. For Rule 210, the left
half can start entirely white and stay consistent for ever, and GPT wrote down the exact column-1 signal needed. So
the left-side form of the question fails for Rule 210 on these walls. Rule 30 remains open.

**Why it matters.** Rule 210 is a test bed: a sibling where the left-side question can be answered. It shows the
left side alone cannot decide the question for every rule.

**An everyday picture.** A scale model where the bridge does stand; it does not tell you yet whether the full-size
bridge will.

## G59
In Rule 210, a finite seed with a repeating wall would need its "and" operations to keep happening for ever.

**What it says.** Rule 210 without its non-linear term is Rule 90, which cannot sustain such a wall from a finite
row (proof 16). So any finite seed for Rule 210 must keep switching on the non-linear term infinitely often.

**Why it matters.** It rules out the simplest kind of witness: one that misbehaves for a while and then goes linear.

**An everyday picture.** A spinning top needs pushing again and again; one push at the start will not keep it up.

## G60
G58's left half can be matched by a full right half, though an infinite one.

**What it says.** For G58's walls, GPT built the whole right side too, solving for it one square at a time. The
right side needs infinitely many black squares, so this is not a finite seed.

**Why it matters.** It settles that the left-half witness is not an empty shell: a whole consistent world exists
around it. Whether a finite one exists is the remaining question.

**An everyday picture.** A crossword that can be filled in completely and consistently, but only on a grid that runs
on for ever to the right: a solution exists, just not one that would fit on a page.

## G61
In Rule 210, column 1 can carry a hidden black bit only at moments when the visible signal switches on.

**What it says.** With the blinking wall, column 1's update rules allow a black square at odd ticks only where the
visible signal goes from white to black. For the signal of the initially empty left half (GPT's G26), that happens
only at times 3, 15, 63, 255, ..., one less than a power of 4.

**Why it matters.** It pins down where the right side can do anything interesting at all: rarely, at predictable
times.

**An everyday picture.** A night-watch who may leave the post only when a lighthouse flashes on, and this lighthouse
flashes less and less often: at minute 3, then 15, then 63, then 255.

## G62
In Rule 210, the first pair of black squares next to the wall can appear only at a sparse list of even times: 0, 6,
30, 126, ...

**What it says.** Adding column 2's own update to G61, a black pair in columns 1 and 2 can occur only at even times,
and only where the visible signal switches off. For the signal of the initially empty left half those times are 0,
6, 30, 126, and so on.

**Why it matters.** It restricts where Rule 210's non-linear term can act near the wall to a very thin set.

**An everyday picture.** A request-stop bus allowed to stop only at the minutes 0, 6, 30, 126 and so on: the gaps
keep growing, so the stops get ever rarer.

## G63
While the visible signal holds steady, each column on the right is forced into a fixed rhythm too.

**What it says.** In Rule 210 with the blinking wall, if column 1's visible signal is constant over a stretch, then
columns 1, 2, 3, ... on the right are each forced into a fixed repeating pattern over that stretch, shortened a
little at each end for each column further out.

**Why it matters.** It replaces G61 and G62's single-square restrictions with a whole forced strip of the right
half.

**An everyday picture.** A row of meshed cogs: keep the first turning steadily and every cog down the line is forced
to turn steadily too, though each one further out takes a little longer to settle and stops sooner after you let go.

## G64
In that Rule 210 family, every fixed column on the right is almost completely predictable.

**What it says.** Take Rule 210 with the blinking wall and an initially empty left half, and any right half that
fits. Using G63, the number of different patterns of length N seen in any fixed right column grows only like a power
of N, not exponentially. Such a column carries no lasting new information: its entropy is zero.

**Why it matters.** It shows how little freedom the right side has in this family, a strong constraint of the kind a
proof needs.

**An everyday picture.** A radio station that only ever plays a handful of jingles: however long you listen, you
learn almost nothing new.

## G65
Any finite left half for Rule 210 can be matched by mirroring it on the right, and then column 1's freedom jumps.

**What it says.** Copy any finite left half, reflected, onto the right side. The two copies' effects cancel at the
wall, so the wall still blinks. Allowing every finite left half, column 1 can show any pattern at its even ticks:
half a bit of new information per tick.

**Why it matters.** It shows G64's "almost no information" depends on fixing the left half; vary it, and freedom
returns. It clarifies what the earlier statements do and do not cover.

**An everyday picture.** Noise-cancelling headphones: a mirror-image copy of a sound, played at the same moment,
cancels it. Here the mirrored right half cancels the left half's effect at the wall, so the wall hears only its own
beat.

## G66
If the left half's black squares stay within a fixed distance, the right side's columns are still almost predictable.

**What it says.** For left halves whose black squares lie within distance R of the wall, every fixed right column
still has zero entropy, uniformly. In Rule 90 a finite disturbance is felt only near times that are powers of 2.

**Why it matters.** So G65's freedom comes only from letting the left half spread without limit, which pins down
exactly where freedom lives.

**An everyday picture.** A bell rung once in a valley: its echoes come back off the hills only at certain moments,
and a few bells, rung once, cannot fill the valley with a steady roar.

## G67
The largest possible "offset" at a first dip, and the pattern that reaches it.

**What it says.** Collatz's arithmetic after a step pattern is "multiply by 3^a, add an offset, divide by 2^t". At a
first dip below 1, GPT found the largest the offset can be: it is reached by putting the odd steps as early as the
rules allow. The offset is at most a third of a times 3^a.

**Why it matters.** This envelope feeds the ceilings: with the offset bounded, so is the height limit of G45.

**An everyday picture.** Savings in an account that pays interest: money paid in early grows the most, so the
largest possible balance comes from paying in as early as the rules allow.

## G68
At a first dip, the start and the end share the same height limit.

**What it says.** For a pattern whose growth factor first dips below 1, a start survives exactly when the start is
at most the ceiling, and equally exactly when the end value is at most the same ceiling. GPT also gave quick tests
that read only the first few or the last few steps of a pattern and can rule out the whole pattern at once.

**Why it matters.** Two descriptions of the same exceptions agree, which makes them easier to count and check.

**An everyday picture.** A ticket barrier on the Underground: whether a journey was valid can be checked at the gate
where you got on or at the gate where you get off, and the two checks always agree.

## G69
A known theorem about how close powers of 2 and 3 can get gives a polynomial cap on every height limit.

**What it says.** A published bound (Rhin's, as stated by Rozier and Terracol) says powers of 2 and 3 cannot be too
close. From it, the ceiling at a first dip after t steps is below t^14.3 / 3.

**Why it matters.** G46 showed the ceilings are unbounded; this shows they grow only polynomially. Exceptions are
confined to fairly small numbers.

**An everyday picture.** The circle of fifths of G46 again: stacked fifths come close to an octave of the starting
note, but never closer than a known margin, so no near miss can be too extreme.

## G70
Above a polynomial size, "the growth factor stays above 1" and "the number stays above its start" pick out exactly
the same numbers.

**What it says.** Count the numbers that actually stay at or above their start for T steps, and those whose growth
factor stays at least 1 for T steps. The two sets can differ only for numbers below T^14.3 / 3.

**Why it matters.** It lets the team count the easier quantity (the growth factor) and know it matches the real one
for large starting numbers.

**An everyday picture.** Two exam markers who agree on every script except the very short ones, under a known
length: for every longer answer their marks are the same.

## G71
The surviving count loses numbers only at the critical boundary, and the loss is set by whether the leftover number
is odd or even.

**What it says.** Each tick, every surviving pattern has two continuations, except those sitting exactly on the
survival boundary, which lose their even continuation. For real Collatz numbers, at the first step after the free
bits, which boundary numbers are lost is decided by whether F1's base-3 remainder is odd or even.

**Why it matters.** It locates exactly where real Collatz numbers can depart from fair coins in the count: an
odd-even imbalance on the boundary.

**An everyday picture.** Line calls in tennis: only a ball that lands on the line is in doubt. Here only the numbers
on the survival line can be lost, and what decides each one is whether a certain number is odd or even.

## G72
Few surviving Collatz numbers can arrive at the same value: at most 1 + a/3 of them.

**What it says.** Among starting numbers of a given size that survive m steps with a odd steps, at most 1 +
floor(a/3) can end on the same value.

**Why it matters.** Paths rarely merge, so counting end values nearly counts starts. The bookkeeping stays almost
one to one.

**An everyday picture.** A lift with a fixed limit: however many people set off from different floors, only so many
can arrive at the ground floor together, and the limit is known in advance (here 1 plus a third of the odd steps).

## G73
For a long stretch of surviving steps, the current value reveals the start from a short label.

**What it says.** Up to about three times 2^m steps, a surviving number's current value tells you how many odd steps
it has made, and then a short extra label tells you which start it came from.

**Why it matters.** It extends G72's near one-to-one bookkeeping deep into the count.

**An everyday picture.** A parcel's postmark tells you the sorting office; a short code then tells you the sender.

## G74
The gap between the real Collatz count and the coin-toss prediction is an exact sum of odd-even imbalances.

**What it says.** Weight each surviving number by the chance that fair coin tosses from its current state would
survive to the end. Following these weights step by step, the final difference between the real count and the coin
prediction equals a sum, over all steps, of how unbalanced the odd and even numbers are, times how much one extra
odd step matters.

**Why it matters.** It reduces the Collatz count's central question to controlling those imbalances, with exact
weights.

**An everyday picture.** A household budget kept in a foreign currency whose rate changes: the final balance is each
month's surplus or deficit, converted at that month's rate, all added up.

## G75
Those weights are uniformly small: about (log h)/√h, where h is the number of steps still to go.

**What it says.** How much one extra odd step changes the chance of surviving h more fair coin tosses is at most
about (log h)/√h, whatever the state.

**Why it matters.** Late imbalances count for little. It controls the coin side only; the real Collatz imbalances
still need their own bound.

**An everyday picture.** One point dropped in the first week of a long football season barely changes who ends up
top; the more matches still to play, the less it matters.

## G77
The simplest way of combining G74 and G75 cannot bound the Collatz count for all horizons: that route is closed.

**What it says.** The goal is to show the real Collatz count never exceeds the coin-toss prediction by more than a
fixed factor. The crudest approach takes G75's largest weight, assumes every class is as unbalanced as it can be,
and feeds the hoped-for bound back in. GPT showed that this approach gives a bound that grows like the square root
of the number of steps, so it can never give a fixed factor. GPT also noted that a big cancellation ratio in the
data does not by itself rule out a useful bound.

**Why it matters.** It closes one tempting route cleanly, and says what is left open: sharper estimates that use how
the numbers are actually spread out, or real cancellation between plus and minus terms.

**An everyday picture.** A builder's quote that prices every job at its worst case: add up enough jobs and the quote
climbs far past what the work will really cost.

## G78
Even a perfectly fair spread of numbers would leave that crude bound growing, so the route needs real cancellation.

**What it says.** GPT computed the crude bound for an ideal fair-coin population, where the true discrepancy is
exactly zero. The bound still grows with the horizon: at eight times the number of free bits it already exceeds that
number, and it keeps growing. So replacing each imbalance by its whole class size throws away too much.

**Why it matters.** It shows the problem is the method, not the data. Any working bound must use the signs of the
imbalances, not just their sizes.

**An everyday picture.** A scale that reads heavy even with nothing on it: the fault is in the scale, not the load.

## G80
When a Collatz number has room to spare, an odd-even pair and an even-odd pair cancel to first order.

**What it says.** Follow one number for two steps, when its count of odd steps is comfortably above the survival
boundary. Its two signed contributions to G74's sum add up to a small "second difference": the first-order parts
cancel exactly, whichever order the odd and even steps come in. Near the boundary the cancellation fails, and an
example shows why.

**Why it matters.** It is a structural reason for the cancellations seen in the data, and a first step on the route
G77 and G78 left open.

**An everyday picture.** On a gentle hill, a step up then a step down, or down then up, leaves you at almost the
same height; the little left over comes from the hill's curve. Against a wall one of the steps is blocked, and the
cancelling fails.

## G81
Whether two surviving Collatz numbers can ever meet reduces to a finite check on step patterns.

**What it says.** Two numbers that survive with the same number of odd steps a and meet at the same value exist
exactly when two allowed step patterns of a fixed length have offsets that leave the same remainder on division by
3^a. GPT showed this, built the two meeting numbers explicitly when such patterns exist, and showed that no meeting
is possible below a = 7.

**Why it matters.** It replaces an open-ended search over numbers with a finite search over patterns for each a,
which GPT has set out in advance.

**An everyday picture.** Instead of watching every car to see whether two ever arrive at the same parking space,
check the finite list of routes on the map.

## C8
Rule 30's change from one tick to the next follows Rule 210, its closest sibling.

**What it says.** Look not at each square but at whether it changed colour between two ticks. That pattern of
changes obeys Rule 210 exactly: Rule 30 equals "keep the old colour, then flip it wherever Rule 210 says so". The
proof is two lines of algebra.

**Why it matters.** It explains why Rule 210 keeps turning up as Rule 30's nearest relative in the record, and it
lets the prize be written as a difference equation in the arithmetic of bits, where 1 + 1 = 0.

**An everyday picture.** Video compression: instead of storing every frame whole, a video file mostly stores what
changed since the frame before, and here those changes follow a simpler rule than the pictures themselves.

## G82
A sharper version of G75: the weights shrink like 1/√h, with no logarithm.

**What it says.** G75 bounded the coin weights by about (log h)/√h. GPT removed the logarithm by looking back only
over a short window of recent steps, where the rest of the coin tosses are independent. The weights are at most
about √(2/h), and the related second differences that G80 needs are of order 1/h.

**Why it matters.** Local had noticed the exact weights showed no logarithm; this proves it. It tightens the coin
side of the Collatz count, and it makes G80's cancelled terms visibly small. The real Collatz imbalances still need
their own bound.

**An everyday picture.** Measuring with a finer ruler: the same object, but the margin of error shrinks.

## G83
Surviving numbers all start with two odd steps, which rules out any two of them meeting for up to 20 odd steps.

**What it says.** These pages ask whether two different surviving Collatz numbers, with the same number of odd
steps, can ever land on the same value. If they never could, the Collatz count's bookkeeping would be exactly one to
one. To keep its growth factor at least 1 through two steps, a number must take two odd steps first, so it leaves a
remainder of 3 when divided by 4. Two surviving numbers that meet must therefore differ by a multiple of 4. But
numbers that end on the same value with the same count of odd steps can only start within a span narrower than 4,
for every count up to 20, so no two can meet.

**Why it matters.** It settles the first twenty cases by a short argument instead of a search, which had reached 17.

**An everyday picture.** A car park where you may use only every fourth bay: two cars told to park within three bays
of each other can only be in the same bay, so they are the same car.

## G84
At 21 odd steps, the first case left open, any meeting of two surviving numbers would have to take one exact form.

**What it says.** Sort the surviving step patterns by their first three steps: odd-odd-even or odd-odd-odd. Two
patterns that begin the same way cannot meet at 21 odd steps, so a meeting needs one of each kind, and the two
starting numbers must differ by exactly 4.

**Why it matters.** It narrows any search for a meeting at 21 to one precise shape, instead of all patterns.

**An everyday picture.** A detective who cannot yet say whether the crime happened, but has proved that if it did,
it took two accomplices, one from each of two families, arriving exactly four minutes apart.

## G85
The two candidates of G84 must also take the same next two steps: both odd.

**What it says.** After their third step the two numbers are both odd or both even. The smaller one needs an odd
fourth step and an odd fifth step to keep its growth factor up, so the larger one takes them too. Their first five
steps must be odd-odd-even-odd-odd and five odds, so they leave remainders 27 and 31 when divided by 32.

**Why it matters.** Each forced step cuts the places a meeting could hide by half, by proof rather than search.

**An everyday picture.** Two dancers keeping time to the same music: when one must step forward, so must the other.

## G86
A tempting shortcut fails: the end of a surviving path need not survive on its own.

**What it says.** One might cut off the first few steps and apply G83's result to the rest. But early odd steps
build a cushion that later even steps spend. GPT gave a 33-step pattern that survives as a whole while its last 27
steps, taken from a fresh start, would not.

**Why it matters.** It stops an invalid argument before anyone relies on it. The rest of a path must be judged with
the cushion carried forward.

**An everyday picture.** A walker who climbed a hill first can walk downhill for a while and still end above home;
the downhill stretch on its own would not.

## G87
A budget argument forces three more steps, pinning down the first eight steps of any meeting pair at 21.

**What it says.** At the sixth step there were two possibilities. One would leave the two numbers too little room in
their possible offsets to meet, so it is ruled out, and the growth-factor rule then forces the next two. The
patterns must begin 11011011 and 11111111 (1 meaning odd), so the starts leave remainders 251 and 255 when divided
by 256.

**Why it matters.** The candidates shrink by proof alone, and the method, comparing the most and least each option
could contribute, becomes the next page's certificate.

**An everyday picture.** Planning a trip on a fixed budget: if one route already costs more than the rest of the
trip could ever save, cross it off.

## G88
A way to rule out a whole tree of possibilities by arithmetic, branch by branch, instead of trying every number.

**What it says.** For each partly written step pattern, compute the smallest and largest offset any continuation
could reach. Two starts 4 apart can meet only if the difference they need fits within those ranges; a branch where
it cannot is cut, with the reason written down. If every branch is cut, no meeting exists in that class.

**Why it matters.** It turns a search into a certificate: a list of reasons anyone can check, rather than "the
computer found nothing".

**An everyday picture.** Tracing a family tree for an ancestor born in a certain year: if no one on a branch could
have been born then, stop tracing it, and note why in the margin, so the next researcher can check your reasoning
instead of redoing it.

## G89
Two surviving numbers can meet after all: the first pair appears at 22 odd steps.

**What it says.** The numbers 5,348,744,187 and 5,348,744,191 differ by 4. Each keeps its growth factor at least 1
at every step, each takes 22 odd steps, and after 34 steps both arrive at 9,770,112,830. Adding the same multiple of
2^34 to both gives infinitely many such pairs. With fewer odd steps no pair exists (G83 to G88).

**Why it matters.** It settles the question with a counterexample. The Collatz count's bookkeeping is nearly, but
not exactly, one to one, and the count has to allow for it.

**An everyday picture.** Two hikers who set off four doors apart, both always above their starting height, and meet
on the same summit.

## G90
Two numbers that meet do not cancel each other out in the count's error.

**What it says.** These pages test ways of proving that the real Collatz count never strays far from the fair-coin
prediction, using the exact error formula of G74. Take a meeting pair from G89's family, 11,843,133,435 and
11,843,133,439. Just before the end, one still needs an odd step to survive while the other already has enough.
Under the coin weights one counts a half and the other a whole, so their contributions add up instead of cancelling.

**Why it matters.** It closes a hoped-for shortcut, that paths which merge must cancel in the error. Cancellation,
if there is any, has to come from somewhere else.

**An everyday picture.** Two runners crossing the line together did not run the same race: one needed a sprint at
the end and the other did not.

## G91
When an odd-step path and an even-step path merge, their two contributions combine into something smaller.

**What it says.** Pair up paths that reach the same next value with the same number of odd steps, one by an odd step
and one by an even step. Each pair's two contributions to the error combine into half the difference of two
neighbouring coin weights, which is small far from the end. Paths with no partner keep their full contribution.

**Why it matters.** It is an exact identity that shrinks part of the error, a real tool, though it does not yet say
how many paths find partners.

**An everyday picture.** A charge and a refund for nearly the same amount on a bank statement: together they come to
the small difference between them, while a charge with no matching refund stays in full.

## G92
Even with the pairing tool, the crude estimate still grows, slowly, with the length of the run.

**What it says.** Grant generously that unpaired paths cancel completely, and bound every pair by the largest amount
it could contribute. The estimate still grows like the logarithm of the number of steps, so it cannot give the fixed
bound that is wanted.

**Why it matters.** It improves on the square-root growth of G77, and shows that the remaining gap needs real
information about which paths pair up.

**An everyday picture.** The builder's quote of G77 again, now with the worst cases paired off against each other:
it still creeps up, only more slowly than before.

## G94
A smooth-shape argument fails: the coin weights stop being a smooth single hump beyond 64 steps.

**What it says.** One hoped to prove that the coin weights always form a smooth single hump (in the jargon,
log-concave), since ordinary averaging keeps that shape. At the survival boundary an extra piece stays put, and GPT
found the exact condition for the shape to survive there. Local then checked the real boundary: the shape holds in
every case up to 64 steps, fails beyond, first at 73, and always at the edge, never in the middle.

**Why it matters.** It closes the route, and records exactly where and why it breaks.

**An everyday picture.** A sandpile shaken against a wall stays a smooth mound in the open, but sand piling up
against the wall can form a shoulder.

## G95
The real survival boundary never pauses twice in a row, but that alone does not keep the shape smooth.

**What it says.** The number of odd steps a survivor needs rises by one at least every two steps, because each step
needs about 0.63 odd steps on average, so any two steps need at least one. GPT showed that a made-up boundary which
does pause twice breaks the smooth shape. The real one never pauses twice, yet G94 found it breaks the shape anyway.

**Why it matters.** It sorts out which property matters and closes a suggested restriction, so the next attempt does
not rely on it.

**An everyday picture.** A path that never has two flat paces in a row before it climbs again can still be bumpy
underfoot: the rule about how often it climbs says nothing about how smooth it is.

## G96
Watching one square change and following a moving pattern are different measurements.

**What it says.** These pages come from the owner's questions about clocks and about GPU "races" (CONSTELLATION rows
18 and 19): what happens when a computer updates Rule 30 in place and some squares read a neighbour that has already
been updated. They are about Rule 30 for its own sake, not directly about the prize. A pattern sliding along at a
steady speed changes at every fixed square, yet does not change at all if you move with it. GPT wrote both kinds of
change exactly. The change at a fixed square is Rule 210 applied to the row (C.8), though the pattern of changes
does not itself follow Rule 210.

**Why it matters.** It fixes which "change" an instrument measures before anyone reads physics into it.

**An everyday picture.** From the platform a passing train changes the view every moment; to a passenger looking
round the carriage, nothing changes at all.

## G97
An observer walking right through a random Rule 30 pattern sees more change than one standing still or walking left.

**What it says.** Start from a random row of fair coin flips; Rule 30 keeps every row random, proved here directly.
An observer who steps right each tick sees the colour flip three times in four. Standing still or stepping left, it
is one time in two. These averages add up even though successive flips are not independent.

**Why it matters.** It gives the exact prediction behind Local's moving-observer measurements, with its assumptions
stated.

**An everyday picture.** Walking into the rain gets you wetter than standing still.

## G98
Speeding up the clock, reordering the updates and counting events are three different things.

**What it says.** Making every tick longer or shorter changes nothing anyone inside could see. Changing the order in
which squares are updated in place can change the result: two neighbours updated in opposite orders can disagree.
Counting events in a light-cone shape has edge corrections a smooth formula misses. And a single black square
spreads left at full speed, so the measured quarter-speed (C4) belongs to random backgrounds, not to every pattern.

**Why it matters.** It answers the owner's clock questions precisely, without turning a picture into physics.

**An everyday picture.** Slowing a film down does not change the story; shuffling its frames does.

## G99
Label every value with its tick number, and any order of updating gives exactly the right answer.

**What it says.** Keep each square's value for each tick separately, and compute a value only once its three parents
from the previous tick are ready. Then every schedule, however uneven the machine's timing, produces exactly the
true Rule 30. A snapshot that mixes values from different ticks is not a true frame.

**Why it matters.** It names the cure for the owner's GPU races: keep the old row until the new one is finished
(double-buffering), or label versions, and timing stops mattering.

**An everyday picture.** Builders who wait for the floor below to be finished can work at any pace; the building
comes out the same.

## G100
Flips that look independent in pairs can still remember: the memory shows up two steps apart.

**What it says.** For an observer stepping right through a random pattern, neighbouring flips are uncorrelated, but
flips two ticks apart are linked, so a count of three flips varies more than three coin tosses would.

**Why it matters.** "Looks random in pairs" is not "random"; reading measurements as independent would understate
their spread.

**An everyday picture.** Two conversations at a dinner table, interleaved remark by remark: one remark tells you
nothing about the next, which belongs to the other conversation, but a good deal about the one after.

## G101
The same hidden memory appears for an observer moving at three-quarter speed.

**What it says.** An observer who stays put for one tick and steps right for three, over and over, finds the second
and fourth flips of each block linked in the same way.

**Why it matters.** The memory is not just an effect of moving at full speed; it appears inside the pattern too.

**An everyday picture.** The two interleaved conversations of G100 are still there if you listen in with pauses: the
second and fourth remarks you catch still belong together.

## G102
A single race corrupts a square one time in eight; a chain of races changes that slightly.

**What it says.** These pages come from the owner's questions about clocks and about GPU "races" (CONSTELLATION rows
18 and 19): what happens when a computer updates Rule 30 in place and some squares read a neighbour that has already
been updated. They are about Rule 30 for its own sake, not directly about the prize. Model a race as a square
reading its right neighbour's new value instead of its old one. On a random row, a lone race gives a wrong value one
time in eight. If the neighbour raced too, races chain and the rate becomes 1/(8 − 4ε), where ε is how often races
happen. A race that reads the left neighbour is wrong half the time.

**Why it matters.** It is the exact starting rate behind Local's race measurements. The left-right difference is
Rule 30's own: the left input passes straight through (the perfect wire of CL004), so racing it scrambles the result
completely.

**An everyday picture.** Copying from a neighbour who has already changed their answer: from one side you are only
occasionally wrong, from the other you might as well guess.

## G103
A square is guaranteed correct if no race happened anywhere in the region it depends on.

**What it says.** A square's value at tick t depends on a triangle of about t² earlier updates. If none of them
raced, it is right. So with races at rate ε it is wrong with probability at most about εt², and noticeable errors
cannot appear before about 1/√ε ticks.

**Why it matters.** It is a guaranteed early-warning bound that needs no assumption about the pattern.

**An everyday picture.** A champagne tower: a glass near the bottom fills with clean champagne only if no glass in
the widening triangle above it was spoiled, and that triangle holds more glasses the further down you go.

## G104
Races that read the right neighbour leave each row looking perfectly random; races that read the left leave a trace
in neighbouring pairs.

**What it says.** With right-reading races, every row still has exactly the statistics of fair coin flips. With
left-reading races the share of black squares stays a half, but neighbouring squares differ a little more often than
they should.

**Why it matters.** It explains how a glitching computation can look statistically perfect: inspecting one row
cannot reveal right-reading races.

**An everyday picture.** A counterfeit note with the right paper, size and colour passes every check you can make on
the note in your hand; only comparing it with others gives it away.

## G105
Joining the row into a ring changes an exact probability, even though large rings look fair.

**What it says.** On a small ring, the number of earlier rows that lead to an all-white row depends on whether a
race happened, so the exact probabilities differ from the fair ones.

**Why it matters.** Results proved on the endless line cannot be assumed exact on the finite rings that computers
actually run.

**An everyday picture.** A bicycle chain laid out straight can be checked link by link from its loose end; joined
into a loop it has no loose end, and counts that were exact on the straight chain come out slightly different.

## G106
Snapshots can stay statistically unchanged while what a moving observer sees changes.

**What it says.** With right-reading races every row still looks fair, but an observer stepping right now sees flips
a little more often than three times in four, the more so as races grow common.

**Why it matters.** This is how such races could be detected: not by looking at a row, but by moving through time.

**An everyday picture.** Every photograph of a busy street looks normal, but a film of it shows people walking at
the wrong speed.

## G107
An observer standing still or moving left cannot detect right-reading races at all.

**What it says.** Along such a path, every sampled value and every flip stays a fair coin toss, whatever the
schedule of races.

**Why it matters.** An observer in the wrong place sees nothing amiss; detecting these races needs a comparison with
the true history, or motion to the right.

**An everyday picture.** A sentry facing the wrong way reports a quiet night.

## G108
The glitched and the true histories are tied together exactly, even though each looks random on its own.

**What it says.** Given everything else, the raced samples equal the true samples with a correction mask, and the
mask is fixed by earlier true samples. The relation can be undone step by step.

**Why it matters.** Two random-looking signals can be completely related, so independence must never be assumed from
appearances.

**An everyday picture.** Two decks of cards, one shuffled and the other the same deck after a cut you know: each
looks random on its own, yet knowing the cut, either one gives back the other.

## G109
A race error can vanish at its square and come back the next tick without any new race.

**What it says.** After a race, the damaged square is wrong at the first tick, right at the second and wrong again
at the third: the damage moved next door and came back.

**Why it matters.** A square that looks correct is not necessarily healed; whether an error is gone cannot be judged
from one square.

**An everyday picture.** A stain that seems to wash out, then reappears as the cloth dries.

## G110
Two signals that each have no memory can have memory as a pair.

**What it says.** In the model with one race, knowing the current true value and the current error does not predict
the next error. The previous error is needed too, because it is the one that comes back (G109).

**Why it matters.** It sets how much of the past any model of the glitches must keep.

**An everyday picture.** Two dancers who each look improvised, but together repeat a step from the bar before.

## G111
Memory found at one race rate is memory at almost every rate; agreement at one rate proves nothing.

**What it says.** The probabilities involved are polynomials in the race rate, so a memory effect seen at one rate
can vanish at only a few others. Local's example then shows it at every rate in between.

**Why it matters.** One exact check covers a whole range of rates, saving a sweep of measurements. The converse does
not hold: a single rate where the effect vanishes can hide it at others.

**An everyday picture.** The railway wheel-tapper's hammer: a cracked wheel rings dull. It rings dull on almost
every tap, and one tap that happens to sound clear proves nothing about the wheel.

## G112
Two shared black squares in a row shield the next update from a race.

**What it says.** In the true and raced histories side by side, when the source square is black at two observations
running in both, the next update is guaranteed to agree.

**Why it matters.** Such patterns occur with positive probability, and they prove that the raced history cannot be
described with memory of only the last step, at every race rate.

**An everyday picture.** Two closed doors in a row stop a draught, whatever is happening outside; the black squares
do the masking of proofs 01 and 03.

## G113
Remembering one step back is still not enough to predict the errors.

**What it says.** In the model with one race, a description made of the last two paired observations still misses
information: in one case adding an earlier observation turns an error rate of 5/234 into zero.

**Why it matters.** Short-memory models of the glitches are provably incomplete, so longer histories matter.

**An everyday picture.** A car that won't start this morning: checking what happened today and yesterday can miss
the cause, a light left on three nights ago.

## G114
Two incoming errors can cancel each other at a white square.

**What it says.** At a white square the next error is the exclusive-or of the errors arriving from left and right,
so two errors cancel. At a black square only the left error passes.

**Why it matters.** It explains the hidden healed ticks of G113, and shows black hiding the right-hand input once
more, as in proofs 01 and 03.

**An everyday picture.** Two waves meeting crest to trough flatten each other out.

## G115
Remembering the race and the last two steps still misses older information.

**What it says.** A description that includes whether the race happened and the last two observations leaves the
next error a coin toss, while the full history pins it down exactly.

**Why it matters.** A shallow check can wrongly suggest a model is complete.

**An everyday picture.** A doctor who asks only about the last two days misses the cause from last week.

## G116
The fourth error after a race depends on three earlier true values together.

**What it says.** Given that the race happened, the fourth error is the exclusive-or of the true values at ticks 1,
2 and 3 (black when an odd number of them are black). Knowing only the last two leaves it a coin toss; adding the
first makes it certain.

**Why it matters.** It names exactly the old information that the shorter memories of G113 and G115 missed.

**An everyday picture.** A landing light with three switches, any one of which turns it on or off (two-way switches
with an intermediate one between): knowing two of the switches tells you nothing about the light until you know the
third.

## G117
A hidden starting bit that is never observed enters the fifth error.

**What it says.** The fifth error depends on squares to the right that the observer never sees, so even the full
observed past leaves some uncertainty about it.

**Why it matters.** Part of the glitch is unpredictable from inside the observation, however much history is kept.

**An everyday picture.** A letter delayed by a sorting fault you never see: the history of your own letterbox cannot
explain it.

## G118
Six samples of the true and the raced histories share 5.53 of their 6 bits.

**What it says.** Each history alone is six fair coin tosses. Together they share 5.5347 bits of information, almost
all of it; hidden starting bits supply the rest.

**Why it matters.** It measures exactly how much of the truth survives one glitch.

**An everyday picture.** A photocopy keeps almost everything on the page, losing only what the copier could not see.

## G119
Each new sample adds shared information equal to one bit minus the uncertainty of the next error.

**What it says.** On a path standing still or moving left, a fresh random bit enters both histories at each sample,
so the information they share grows by one bit minus how uncertain the next error is.

**Why it matters.** It ties how unpredictable the glitch is to how well the raced copy keeps tracking the truth.

**An everyday picture.** Two people keeping diaries of the same days: each new day adds one more day they agree on,
less whatever one of them misheard that day.

## G120
Once you know whether a rare race happened, the raced copy keeps at least 7/8 of a bit of each new sample.

**What it says.** After observing whether the race occurred, the uncertainty about each later error is at most 1/8
of a bit, so by G119 the two histories share at least 7/8 of a bit of every new sample. No assumption that the rate
settles down is needed.

**Why it matters.** It is a guaranteed floor on how well the raced copy keeps tracking the truth.

**An everyday picture.** Knowing a train was delayed once tells you most of what you need to predict its later
stops.

## G121
Walking a seed backwards in time shrinks it, but the walk stops at a "root", and roots come in every size.

**What it says.** A finite row has at most one finite row that produces it one tick earlier, and that earlier row is
two squares narrower. Walking back, every row reaches a unique starting row, its root. A counterexample stays a
counterexample as you walk it back, so the smallest counterexample would have to be a root. But three quarters of
all rows of every width are roots, and the single black square is one already.

**Why it matters.** It is the first attempt at the smallest-counterexample move of the owner's steer (chat CL005),
recorded as a failed bridge with the exact place it breaks: shrinking backwards cannot bound the size of a
counterexample. It has not yet had its second reading.

**An everyday picture.** Rewinding the film of a growing crystal back to its seed: every crystal has a seed, but
seeds come in every size, so rewinding alone cannot show that the crystal was small.

## G122

Walking back past a root leaves the world of finite seeds, first through a black tail and then a repeating one.

**What it says.** A row that is white far enough to the right can always be run backwards, in exactly one way.
Behind a root, the earlier row has an endless black tail on the left; one tick further back, that tail becomes the
endlessly repeating pattern 001.

**Why it matters.** It maps exactly how the backward walk escapes the finite seeds the prize is about. Whether that
exit says anything about the blinking middle column is still open. It has not yet had its second reading.

**An everyday picture.** Rewinding past the moment of planting, the film no longer shows a seed but an endless
striped field.

G122 extension GC593, awaiting reading: finite black sites spaced three apart map to one solid interval. Earlier black components all have length one, while centre black duration is two and the following white duration grows with width. This rules out a universal one-row component-memory substitute for GC545. For positive m the exact centered rows are not singleton time slices by span and the two-black left-edge invariant; local selected occurrences remain possible.


## G123
Run a root backwards for ever, and the repeating pattern on its far left keeps getting longer.

**What it says.** Rule 30 can be run backwards in exactly one way if rows may stretch endlessly to the left (G122).
Doing that from a root, each earlier row repeats far to the left with some period, and the periods keep growing,
each a multiple of the last, without limit.

**Why it matters.** It closes a hoped-for shortcut, that a seed's backward history stays simple. It holds for every
root, so it cannot single out a counterexample.

**An everyday picture.** Rewinding a film further and further shows ever longer repeating wallpaper at its edge,
never one fixed pattern.

## G124
A repeating row that eventually fades to all white can only repeat every 1, 3, 6, 12, 24, ... squares.

**What it says.** If a row repeats across space and Rule 30 eventually turns it entirely white, its shortest
repeating block is 1 square long, or three times a power of two. Every such length occurs.

**Why it matters.** It is a clean classification of the patterns that die out completely: their loop lengths start
at three and double. It does not touch the blinking middle column.

**An everyday picture.** Organ pipes for one note in different octaves, each twice the length of the last: 3, 6, 12,
24 and so on, with a single tiny pipe of length 1 standing apart.

## G125
The sideways rule's repeating patterns are exactly Rule 30's repeating patterns on a ring.

**What it says.** The sideways rule reads Rule 30 along time instead of across space, turning pairs of columns into
sequences of three symbols (CONSTELLATION row 5). A pattern that repeats in that view is the same thing as a ring of
squares whose row comes back to itself in time.

**Why it matters.** It hands every repeating sideways pattern to the ring census, which already lists them all for
rings of up to 29 squares, with no new computation.

**An everyday picture.** Wallpaper printed from a roller: a pattern that repeats sideways can be printed by a
cylinder one repeat wide, as long as the pattern also matches all the way down the roll.

## G126
One sideways step can produce exactly the sequences that avoid six short forbidden words.

**What it says.** The sideways rule reads Rule 30 along time instead of across space, turning pairs of columns into
sequences of three symbols (CONSTELLATION row 5). GPT found the complete list of what one step can produce: every
sequence that avoids six particular short words. A simple recipe builds an input for every allowed output.

**Why it matters.** It completes an earlier partial list. It still leaves plenty of freedom, so on its own it does
not constrain the prize's column.

**An everyday picture.** A spellchecker with six banned words: anything else can be typed.

## G127
A second sideways step loses more sequences, and no simple repeating recipe stays inside the allowed set.

**What it says.** Some allowed sequences need an input that repeats less often than they do, so no recipe that
treats every position alike can work. And one allowed sequence forces a banned word in every possible input, so two
steps produce strictly less than one.

**Why it matters.** Each sideways step genuinely narrows what can appear, though this does not say how far the
narrowing goes.

**An everyday picture.** A stack of ever finer sieves: each one holds back more, but knowing that does not tell you
how much will be left after the last.

## G128
However many sideways steps you take, every possible sequence of black and white still appears in some column.

**What it says.** The patterns that survive every sideways step are exactly the pairs of neighbouring columns in
complete Rule 30 histories, and either column of such a pair can be any sequence at all.

**Why it matters.** It closes a broad route: narrowing by sideways steps alone can never rule out a blinking column.
Any proof must use the blinking wall itself or the finiteness of the seed.

**An everyday picture.** A seating plan with many rules about who may sit next to whom, yet every guest, taken
alone, can still be seated: the rules bind pairs of neighbours, not any one person.

## G129
For each seed size, whether a finite seed can keep the middle blinking is a finite check.

**What it says.** Fix the blinking wall and a maximum size for the seed's left part. The possible histories then
form a closed, bounded family: if there are none, a finite rectangle of the pattern already shows the contradiction.
Each left seed allows at most one complete sequence of visible bits.

**Why it matters.** It restates the prize's left-half question as one finite question per size, and Local showed the
records already answer it up to size about 84 (L083). The open part is one statement covering every size.

**An everyday picture.** A puzzle that comes in every size of board: for each size, whether it can be solved is a
check you can finish, but the claim is about all the sizes at once.

## G130
Fix the seed's right part, and any wall forces exactly one left part, though usually an infinite one.

**What it says.** Reading Rule 30 backwards (the crossword quirk) fills in the left part uniquely from the requested
middle column and any chosen right part. Even an all-white right part works, if the left part may be infinite.

**Why it matters.** So a finite seed exists exactly when some finite right part makes the forced left part turn
white for good. That is the precise target.

**An everyday picture.** The primer's crossword again: write in the middle column and any right half, and the left
half is forced, letter by letter, but it may run off the edge of the page.

## G131
Recoding a rotation pattern through any fixed window still cannot keep the middle blinking.

**What it says.** These pages work on question 7: what could column 1, the middle's right-hand neighbour, look like
if the middle blinked for ever? Theorems E and E″ already exclude the simplest rotation codes (see the primer). Any
rule that reads a fixed small window of such a pattern and writes black or white keeps its long repeats, so it is
excluded too. This covers rotation codes with several arcs when their edges are related in a simple way.

**Why it matters.** It widens Theorem E from one kind of pattern to a large family. Patterns whose arcs are
unrelated remain open.

**An everyday picture.** A song played through a fixed set of filters still has a repeating chorus.

## G132
A pointer driven by several hidden wheels is excluded too, when what you see depends on one of them.

**What it says.** Rotations in several dimensions are excluded whenever the black-or-white reading depends on a
single circular coordinate.

**Why it matters.** It covers some patterns with several unrelated arcs. Readings that genuinely use several
dimensions remain open.

**An everyday picture.** However many gears turn behind a clock face, if you read only one hand, you see that hand's
rhythm.

## G133
A golden-ratio rotation pattern cannot be rescued by ever rarer corrections.

**What it says.** These pages work on question 7: what could column 1, the middle's right-hand neighbour, look like
if the middle blinked for ever? Theorems E and E″ already exclude the simplest rotation codes (see the primer).
Suppose column 1 follows the golden-ratio rotation code but is corrected now and then (a "kick"). Each stretch
between corrections can last at most a fixed multiple of the current time, so corrections must keep coming at least
at a steady geometric rate; ever sparser ones cannot keep the middle blinking.

**Why it matters.** It reaches beyond exact rotation codes to kicked ones, close to the measured wheel (6.1). Kicks
at a steady geometric rate remain possible, and the wheel's own angle is rational, which G136 takes up.

**An everyday picture.** A wobbling top needs a push every so often: the gaps between pushes may grow as it spins
on, but never by more than a fixed multiple of how long it has been spinning.

## G134
The same holds for every rotation angle whose continued-fraction digits (the whole numbers you get by repeatedly
taking off a number's whole part and turning what is left upside down) stay bounded.

**What it says.** G133's spacing limit extends from the golden ratio to every irrational angle of "bounded type",
whose continued-fraction digits never grow large.

**Why it matters.** A larger family of kicked patterns is excluded.

**An everyday picture.** The same rule for every top whose wobble never falls into step with its spin, and never
comes too close to doing so.

## G135
And for every irrational angle, even when the angle and starting point change at each correction.

**What it says.** The limit on uninterrupted stretches holds for every irrational rotation, and survives resets that
change the angle and the starting point between pieces.

**Why it matters.** It removes the restriction on the angle. Corrections at a steady geometric rate remain possible.

**An everyday picture.** Swapping the top for a different one at each push does not let you push less often.

## G136
Fixed-window recodings and rational angles obey the same spacing limit, as long as the window stays bounded.

**What it says.** Reading a fixed window of a rotation pattern, or using a rational angle, still needs corrections
at least at a geometric rate, even with resets. The window must stay bounded: wide enough windows can imitate
anything.

**Why it matters.** It maps the edge of the method: bounded reading windows are essential.

**An everyday picture.** Through a fixed keyhole you see the same repeats; widen the keyhole without limit and you
can see anything.

## G137
A pattern that is black only at the powers of two passes every repeat test; powers of three fail.

**What it says.** The sequence that is black exactly at ticks 1, 2, 4, 8, 16, ... passes every repeat test the
record requires, and is about as simple as a never-repeating pattern can be. Using powers of 3 or more leaves white
runs too long, and fails.

**Why it matters.** It shows the limit of the repeat test: it cannot by itself rule out every sparse pattern.
Passing the test does not mean Rule 30 can produce it.

**An everyday picture.** The metal detector at an airport: it stops some people, but walking through it cleanly does
not make you a passenger, and the passport desk is still ahead.

## G138
The first place where Rule 30's "and" matters stays quiet for the powers-of-two pattern, but quiet is not enough.

**What it says.** Reading backwards from the wall, the first five forced columns have exact formulas in column 1's
visible bits, and the fourth contains Rule 30's first product (C7). For the powers-of-two candidate that product
fires only once. But even a constant column 1, where it never fires, forces an endless checkerboard to the left.

**Why it matters.** It starts testing candidates against the wall's own equations rather than repeat tests, and
records why one shallow check cannot certify a finite seed.

**An everyday picture.** One quiet gate does not certify that the rest of the circuit is quiet.

## G139
A column can look perfectly simple over time while the starting row stays unresolved.

**What it says.** Each fixed column on the left reads only a limited stretch of the future, so for the powers-of-two
candidate every fixed column has almost no variety over time. That says nothing about whether the starting row is
finite, because the depth that matters keeps growing.

**Why it matters.** It separates two measurements that are easy to confuse: variety along time at one place, and the
shape of the starting row across space.

**An everyday picture.** Watching one window for a year tells you about that window, not about how long the street
is.

## G140
The whole family of possible histories is rich, one particular history is simple, and neither settles finiteness.

**What it says.** All the histories compatible with the wall carry one bit of freedom per step; the powers-of-two
history carries none. Its limit includes an endless checkerboard, but a finite seed whose edge grows every tick can
still approach an infinite limit.

**Why it matters.** It keeps three questions apart: the variety of the family, the variety of one history, and
whether its seed is finite.

**An everyday picture.** A soap opera: its possible plots are endless, and one storyline can be very plain, but
neither tells you whether the show will ever end.

## G141
Holding the wall fixed changes how the past works: an earlier row need not be unique, or finite.

**What it says.** Run backwards with the middle column forced, a black beat fixes the square beside it, while a
white beat allows two choices. GPT found a test for when the earlier rows stay finite, and two finite rows that
merge into one.

**Why it matters.** The uniqueness of the past that holds for the free rule (G121) cannot be borrowed here, and the
descent idea still gives no contradiction.

**An everyday picture.** Two roads into town that join at one roundabout: once you are past it, nothing on the road
ahead shows which way you came.

## G142
A finite seed that kept the middle blinking would still have rows approaching an infinite pattern.

**What it says.** Its edge moves outward every tick, so its rows cannot stay inside any bounded family, and some
sequence of them must approach an infinite pattern.

**Why it matters.** Finding an infinite limit therefore does not refute a finite seed, a mistake the record now
guards against.

**An everyday picture.** Growing ripples can look more and more like one endless straight wave, though each ripple
is finite.

## G143
A rotation pattern using half the dial passes every repeat test the record requires.

**What it says.** These pages work on question 7: what could column 1, the middle's right-hand neighbour, look like
if the middle blinked for ever? Theorems E and E″ already exclude the simplest rotation codes (see the primer). A
particular code, black on one half of the dial with an irrational angle, never repeats, has runs of at most two, and
passes the repeat test at every period. The reason: some close returns of the pointer flip every symbol instead of
repeating it.

**Why it matters.** The repeat test alone cannot exclude every rotation-like neighbour. This does not show Rule 30
can produce the code.

**An everyday picture.** A forger whose copies are mirror images passes a test that only looks for exact copies.

## G144
For half-dial codes started at the dial's boundary, exactly which angles pass the repeat test is now known.

**What it says.** Such a code passes with a fixed allowance exactly when the angle's continued-fraction digits (the
whole numbers you get by repeatedly taking off a number's whole part and turning what is left upside down) are
eventually all 2 and a related sequence of numerators is eventually odd. Every other angle fails, with an excess
that grows without bound.

**Why it matters.** It turns a family of open cases into a small, precise exceptional class, which still needs the
wall's own equations.

**An everyday picture.** A lock that opens only for keys whose teeth eventually all have the same height.

## G145
Moving the starting point half a turn changes the verdict: the silver half-turn code fails.

**What it says.** For the silver angle, whose continued-fraction digits (the whole numbers you get by repeatedly
taking off a number's whole part and turning what is left upside down) are all 2, the boundary-start code passes the
repeat test (G144). Starting half a turn later produces repeats whose excess grows without bound, the first one
already seen by Local at period seven, so that code is excluded.

**Why it matters.** The starting point matters, not just the angle.

**An everyday picture.** The same tune started half a bar late: every note is the same, but now it clashes with the
band.

## G146
Codes that pass the test can come as close as you like to one that fails.

**What it says.** Every time-shifted copy of the passing silver code still passes, but needs an ever larger
allowance, and the shifts approach the failing half-turn code. Their starting rows approach one particular infinite
row.

**Why it matters.** A bound that holds for each pattern separately cannot be used as one bound for the whole family,
and approaching an infinite row does not rule out a finite seed whose edge grows.

**An everyday picture.** Each step towards a cliff is safe on its own, yet the steps lead to the edge.

## G147
At any one irrational angle, at most countably many starting points could come from a finite seed.

**What it says.** So almost every starting point is ruled out. But if even one works, time evolution produces a
dense crowd of them with growing seeds, and each seed size allows only finitely many.

**Why it matters.** This is why an "almost every starting point" result cannot settle the particular code under
study.

**An everyday picture.** A rule that holds for almost every dart thrown says nothing about the one dart you care
about.

## G148
The "acceleration" of a pattern, or any fixed-order change, keeps its variety and cannot prove a seed finite.

**What it says.** The change from tick to tick, the change of that change, and so on (the owner's velocity and
acceleration question, C.8) keep a pattern's variety the same, losing only its first few bits. They can expose
particular features, such as whether a near-repeat repeats or flips, but quiet changes do not mean a finite seed:
the endless checkerboard has none.

**Why it matters.** It closes a measurement shortcut cleanly.

**An everyday picture.** A car cruising at a steady speed shows zero acceleration, which says nothing about how long
the road is.

## G149
A candidate starting row becomes finite later exactly when its far-left part repeats and that repeat dies out.

**What it says.** A row compatible with the blinking wall turns into a finite row at some later time exactly when,
far to the left, it repeats with some period and that repeating pattern eventually fades to all white (G124: periods
1 or 3 times a power of two). The endless checkerboard does not qualify. Changing finitely many visible bits keeps
the property.

**Why it matters.** It turns "eventually finite" into a concrete test on the far-left tail. Such rows are rare
(countably many) and, if any exist, they lie arbitrarily close to every candidate. None has been built.

**An everyday picture.** A dropped ping-pong ball comes to rest only through a run of bounces that was already dying
away, each bounce a smaller copy of the last.

## G150
How a repeating row's past repeats is decided by counting its gaps.

**What it says.** For a repeating row with both colours, look at the runs of black between white squares. A run of
length 1, 4, 7, ... resets the backward rebuild (E1) and gives one earlier row with the same period. Without such a
run, an odd number of runs of length 2, 5, 8, ... gives two earlier rows with double the period, and an even number
gives two with the same period.

**Why it matters.** It sharpens "stay or double" (G124) into an exact rule, though it does not follow the history
further back.

**An everyday picture.** Whether a repeating knitting pattern came from one of the same length or twice as long can
be read off by counting its gaps.

## G151
Going backwards, a repeating row's period can never double twice in a row.

**What it says.** A backward doubling always leaves a reset (white, black, white) in the earlier row, so the next
step back keeps the same period. A pattern that dies out within 2k steps therefore has a period of at most 3 times
2^(k−1).

**Why it matters.** It tightens the limit on how complicated a dying pattern's past can be; Local notes it halves
the exponent of the earlier bound.

**An everyday picture.** A path that may never climb two steps in a row: after every rise comes at least one flat
tread, so it can only gain height so fast.

## G152
A pattern on its way to dying out never returns even to a shifted copy of itself, which limits how long the dying
takes.

**What it says.** Counting repeating rows up to rotation, with the periods G124 allows, gives a sharper limit on how
long a row takes to reach all white: at most 3 steps for period three and at most 12 for period six.

**Why it matters.** It sharpens the picture of the dying patterns and gives backward tails a faster growth floor
(G123). It does not settle the blinking wall.

**An everyday picture.** A walker who may never revisit any spot on a round track, even one shifted along, cannot
walk for long.

## G153
The Rudin–Shapiro sequence passes the repeat test, by a computer-checked certificate.

**What it says.** The Rudin–Shapiro sequence colours each tick n by whether 11 appears an odd or even number of
times in n's binary digits, overlaps counted. An exact calculation with an automaton (a small machine that reads the
digits one at a time) says it passes every necessary repeat inequality with no allowance at all. A second
construction, built a different way, describes the same language, and Local's own code, sharing nothing with GPT's,
agrees with brute force.

**Why it matters.** It is another famous never-repeating pattern that the repeat test cannot exclude, so its
finiteness question stays open and needs a different kind of argument.

**An everyday picture.** Another traveller who walks cleanly through the metal detector of G137: the passport desk
must catch them, or show they are genuine.

## G154
Among all patterns that look locally like Rudin–Shapiro, finite seeds are either absent or rare but everywhere.

**What it says.** Take every pattern whose short stretches all occur in the Rudin–Shapiro sequence. For almost all
of them, the forced left half never turns white for good, so no finite seed makes them. If even one of them does
come from a finite seed, then so does the same pattern started at any later tick, and these exceptions are countable
(they could be listed one by one) but turn up close to every member of the family.

**Why it matters.** "Almost every member fails" does not decide any particular member, including the original
sequence. A direct argument about its own left half is still needed.

**An everyday picture.** Fractions sit next to every number on the line yet take up none of its length. Knowing that
a number picked at random is almost never a fraction says nothing about whether one given number is.

## G155
There can be only a few finite seeds of each size in the Rudin–Shapiro family, if there are any at all.

**What it says.** A finite seed reaching L squares out is fixed by the first half of that many beats of the column
it makes, so there are no more such seeds than there are different stretches of that length. Rudin–Shapiro has
exactly 8k − 8 different stretches of each length k from 8 on (Allouche and Shallit, 1993), so at most about 4L
seeds reach L squares or less. If one exists, its later rows give about L/2 more.

**Why it matters.** The number of candidates is either zero or grows in proportion to L. That bounds the search but
does not say which, so the question for the original sequence stays open.

**An everyday picture.** A song can be named from its opening notes, so there can be no more songs than different
openings. Counting openings still does not say whether the song exists.

## G156
Near the edge of a seed, stripes that keep the same rhythm cannot run for long.

**What it says.** Next to the seed's edge, each diagonal stripe repeats in time. If the first K stripes all repeat
with period P, every pair of neighbouring stripes is different, even after sliding it in time. So K is less than the
number of necklaces of P beads in four colours, about 4^P divided by P. For period one the most is exactly 3
stripes, and for period two exactly 8.

**Why it matters.** The deeper the stripes, the longer their rhythm must be: a sharper floor on how fast periods
grow (G7). The ceiling, which the settling question needs, is still missing.

**An everyday picture.** Turning a necklace round does not make a new necklace, so there are fewer necklaces than
strings of beads, and fewer steps before one must repeat.

## G157
Odd factors in the period add nothing: only the power of two in it matters.

**What it says.** Every rhythm in the edge stripes of G156 repeats with a period that is a power of two. So stripes
with period 6 behave exactly like stripes with period 2, and those with period 3, 5 or 7 like period 1. Every odd
period allows exactly 3 stripes, and every period twice an odd number exactly 8.

**Why it matters.** It answers infinitely many periods at once from the two smallest cases. It says nothing about
how long the stripes take to settle.

**An everyday picture.** Folding a strip of paper in half, then in half again: the creases divide it into 2, 4, 8 or
16 parts, never 3 or 6. Every rhythm here is made by that kind of folding, so a period with an odd factor behaves
just like its power of two.

## G158
When a rhythm doubles, its two choices are the same choice seen at two moments.

**What it says.** Going inward from the edge, a stripe can split into two possible next stripes. When the period
doubles, the two are the same stripe shifted in time, so counting time-shifted copies once removes the choice. Only
one kind of step, which keeps the period and has an even count of black beats, gives a real fork. Dead ends
outnumber real forks by exactly one.

**Why it matters.** Period doubling is not a free choice, which simplifies the tree of edge histories. How many real
forks there are, and how long the histories take to settle, stays open.

**An everyday picture.** A fork whose two roads are one road seen an hour apart is not a fork.

## G159
Real forks in the tree of edge histories are at least seven steps apart.

**What it says.** After a real fork of G158, the next six steps inward are forced, so along any path real forks come
at least seven steps apart. At depth n there are at most 2 to the power n/7 different histories. The rooted trees up
to period 15 have no real forks at all, each being a single chain; at period 16 the first one comes 53,207 steps in,
as an earlier result (G2.3) had already recorded.

**Why it matters.** It limits how fast the histories can multiply. It does not limit how long a single history can
run, which is what the settling question needs.

**An everyday picture.** On a road whose junctions are at least seven miles apart, the map cannot branch quickly.

## G160
The clock that times the resets settles into a narrower set of positions within two steps, but every repeating loop
was already inside it.

**What it says.** The reset-timing clock of G8 enters, within two steps, a restricted set of arrival positions and
never leaves. That can trim the starting stretch of a timing calculation. But every loop the clock can repeat
already lies inside the set, so the known obstacle to a fast settling bound (G8's slope 2) survives.

**Why it matters.** It removes a distraction from the start of the calculation, not the obstacle itself.

**An everyday picture.** A ticket barrier that every regular commuter already walks through: it stops the odd stray
visitor, never the daily traffic.

## G161
To find the first real fork, follow one history, not all its time-shifted copies.

**What it says.** Before the first real fork of G158, every apparent choice is the same history shifted in time, so
following one of them is enough. The walk stops either at a real fork or at the dead end where the period would grow
too large, and either answer is exact. It is cheap: at period 16 it took about a second and found the first fork
53,207 steps in, agreeing with the earlier record (G2.3).

**Why it matters.** It turns a search that ran out of time into a quick, complete test. It says nothing about how
long the history can be.

**An everyday picture.** To find the first junction on a road, you need only drive one lane of it.

## G162
Just after a real fork, the next three resets cost an amount set by two neighbouring runs of one colour.

**What it says.** At a real fork, the timing of the next three resets depends on the runs (unbroken stretches of one
colour) in the stripe: one branch costs the length of the current run plus 2, the other the current and next runs
plus 2. At the known first fork the most it can cost is 8. Two stripes that look alike by a cruder measure (their
difference order) can cost very differently, so that measure cannot bound the waiting alone.

**Why it matters.** It gives an exact local cost where the histories split, and warns which shortcut fails.

**An everyday picture.** Two journeys with the same number of stops can take very different times, depending on how
the stops are spaced.

## G163
When one block of stripes repeats for ever, the timing settles to a single average rate, whatever the start.

**What it says.** Repeat a fixed block for ever, and the reset clock of G8 runs at one long-run rate from every
starting position, never straying from it by more than one period at the block boundaries. If that rate is within
the allowance (5/2 per step), the block's total debt stays bounded. Costs inside a block, and along histories that
fork, are not covered: an example Rule 30 itself does not allow (GC198) balances at every block boundary yet runs
ever deeper into debt inside.

**Why it matters.** It settles the repeating part of the timing problem and isolates what is left.

**An everyday picture.** Walk the same circular route at your own pace and your average speed comes out the same
whichever gate you set off from.

## G164
A timing budget checked along one path holds, give or take one period, for every starting phase and restart.

**What it says.** Suppose the reset clock's debt is bounded, by D, over every stretch of one timing path. Then on
the same history every other starting phase has debt at most D plus one period, and an earlier theorem (G9) extends
this to restarts after a birth. Only one path per history needs checking, but every truly different history needs
its own check.

**Why it matters.** It removes whole families of separate searches over phases and births.

**An everyday picture.** A timetable checked for one train holds, to within one departure interval, for every train
on the same line.

## G165
If each stretch with a fixed period has a budget in proportion to that period, the budgets add up to a constant
times the last period.

**What it says.** Along an edge history the period stays the same for a stretch, then doubles. If every such stretch
keeps its timing debt within a fixed multiple of its period, the totals add up like 1 + 2 + 4 + ..., less than twice
the last, so the whole history stays within a constant times its final period, phases and restarts included. A real
fork that keeps the period earns no extra allowance.

**Why it matters.** It reduces the settling question to two named assumptions: the budget for each stretch, and
periods that grow more slowly than the depth. Neither is proved.

**An everyday picture.** Bills that double every month never add up to more than twice the latest one.

## G166
How long a timing budget takes to find says nothing about how large it is, and forgetting part of the state can
invent a loop.

**What it says.** GPT predicted that looking 4q steps ahead would find a timing budget for period q. Local's run
(HG4) refuted that at period 8, where 85 steps were needed, although the budget itself stayed small. G166 explains
why: the number of steps needed is the largest shortest route through steps that use up the allowance exactly,
ending where the remaining allowance is zero; it can be long while the budget is small. It also shows that a budget
remembering only the current stripe and the clock fails, since one real step costs q yet seems to return to where it
began; forgetting the clock fails as well.

**Why it matters.** It rejects two specific ways of forgetting state. Other compressions may work if they preserve
the distinctions those projections lose.

**An everyday picture.** A map that shows junctions but not which road you came in on can draw a roundabout where
there is only a dead end.

## G167
A free step pays for a whole branch block, but not for every part of it.

**What it says.** At a real fork the branch step costs nothing, and with the three resets after it (G162) it makes a
block whose total stays within the allowance for periods up to 8. A shorter stretch inside the block can still run
over: by 11 in one period-8 case, and by 2 at the known period-16 fork, where every whole block pays.

**Why it matters.** Paying for whole blocks is not enough; the bound must hold on every stretch, and the steps
between blocks are still open.

**An everyday picture.** A bank account that comes out even once the salary lands can still go overdrawn in the week
before payday.

## G168
One fixed reserve covers the overruns inside every block, however many blocks there are.

**What it says.** Suppose a budget covers the steps between blocks and each whole block. Then one fixed reserve, set
by the size of a single block's overrun (a few times the period), makes it cover every stretch, including those
inside blocks. The reserve does not grow with the number of blocks. The budget for the steps between blocks is still
to be proved.

**Why it matters.** It turns block-by-block payment, which G167 provides, into the every-stretch bound the settling
question needs, leaving one named gap.

**An everyday picture.** A float in the till covers the change handed out before each sale is rung up; it need not
grow with the number of customers.

## G169
No single formula built from three waiting distances can be the timing budget.

**What it says.** Try a budget that adds fixed multiples of three distances: from the current time to the next black
beat of the earlier stripe, of the current stripe, and of the places where they differ. Three real steps, two at
period 4 and one at period 8, demand multiples that contradict each other, so no choice works for every period.
Formulas that change with the period, or use more information, are not ruled out.

**Why it matters.** It closes a natural candidate quickly, with no computer search, and points to what a budget must
also see.

**An everyday picture.** Three receipts that no single price list explains: two show a coffee costs at most a pound,
the third that it costs more.

## G170
Even a formula allowed to change with the period fails, because a long period still contains short-period patterns.

**What it says.** G169's two period-4 steps can be repeated inside any larger period q, where they keep their short
waiting distances. Together with a period-q step they again contradict any choice of multiples for that q, unless
the allowance is at least 3q/(q + 1), which at period 8 exceeds the 5/2 allowed. Formulas that use each state's own
shortest period, or richer information, remain open.

**Why it matters.** It closes the obvious repair of G169 and says the next candidate must tell the period levels
apart.

**An everyday picture.** A fare chart for the long-distance line must still price the local stopping trains that
share its track.

## G171
Choosing the formula by each state's own shortest period does not rescue the three distances either.

**What it says.** Three real steps whose stripes have exactly period q, and no shorter one, still make contradictory
demands on G169's three-distance formula, even when its multiples may depend on each state's own period. A change
far along a stripe alters its period while the three distances, which look only as far as the next black beat, stay
the same.

**Why it matters.** It closes the escape left open by G170: the trouble is in what the three distances throw away,
not in mixing periods.

**An everyday picture.** A fare set from the first mile of a route cannot tell apart two routes that part only
later.

## G173
One real step takes time yet leaves all three distances unchanged, so no formula built on them can work.

**What it says.** At every period 4, 8, 16, ... there is a real step that takes three ticks and has the same three
distances, and the same period, before and after. A budget computed from those numbers, by any rule however
elaborate, sees no change across that step, so it cannot pay for the three ticks at less than 3 per step, and the
allowance is 5/2.

**Why it matters.** It closes the three-distance idea completely. Budgets that see more remain open.

**An everyday picture.** A taxi meter that reads the same before and after a ride cannot be what the fare is charged
from.

## G174
A pattern can lie on the real history without every clock setting turning up there.

**What it says.** The bad period-4 step of G173 does occur on the real history, 10 steps from the seed's edge. But
there the clock always reaches it at one setting, while the bad step needs another, which the gate of G160 allows
but the real history never produces. So checking a budget on every gated clock setting asks more than the real
history needs.

**Why it matters.** A budget might still work on the clock states the history really reaches; the next test (RQ3)
was restricted to those.

**An everyday picture.** Your station is on the line, but the trains that actually call there all arrive on the
hour: a rule about trains arriving at twenty past need never be tested there, although the map of the line allows
it.

## G176
Even on the clock states really reached, the three distances lose the timing.

**What it says.** At period 8, a real step reached 190 steps from the seed's edge takes five ticks and leaves the
three distances and the period unchanged. So no budget built on those numbers works below five ticks per step on
that reached edge: it would need 5 per step there. Local and GPT reconstructed the step independently.

**Why it matters.** Keeping to the real history repaired period 4 but not period 8, so the three-distance family is
closed below five ticks per step on these reached states too.

**An everyday picture.** The meter of G173 again, this time on a ride somebody actually took.

## G178
Finer timing labels fix one collision but glue together pieces of history that never meet.

**What it says.** Adding the stripes' difference orders (GC191) to the labels separates G176's collision. But then
seven real period-8 steps close into a loop of labels, because two of their joins match as labels while the actual
states differ. The loop takes 21 ticks over 7 steps, 3 per step against an allowance of 5/2, so no budget built on
these labels works. No real repeating history is claimed.

**Why it matters.** These labels lose distinctions between actual states at the joins, so the next candidate must
keep the real connections.

**An everyday picture.** Two stretches of road with matching signposts get glued together on the map into a ring
road that does not exist.

## G179
Check the real connections first, then simplify the labels.

**What it says.** A budget can be put on pairs of consecutive real steps that share the same middle state, rather
than on single states. If it is bounded and never negative, it turns back into a budget on states, at the cost of
one extra allowance for the first step. Building the pairs after simplifying the labels keeps G178's false loops.

**Why it matters.** It gives the rule for using context. RC2 then tested it at period 8 and passed, but with labels
barely simpler than the full state (398 labels for 411 steps): a finite success, not the small budget the settling
question needs.

**An everyday picture.** Check that two train journeys really change at the same station before you replace station
names with zone numbers: do it the other way round, and two different stations in the same zone look like a
connection that isn't there.

## G182
The period-8 timing budget passes a check from scratch, but it is almost a full list of the steps.

**What it says.** GPT's independent checker confirmed every inequality of the budget that Local's RC2 run found for
periods 1, 2, 4 and 8 (a budget is a score attached to each state of the edge history so that every step pays its
timing cost). The largest score needed, counted in half-ticks, is 14.

**Why it matters.** It closes the RC2 test honestly. But the budget uses 398 labels for 411 steps, so it is a list,
not a rule, and it says nothing about larger periods.

**An everyday picture.** A shop's till balances because every sale is written down separately; that is no help in
guessing next month's takings.

## G183
Every failed budget failed the same way: a round trip that looks closed to the labels but takes too long.

**What it says.** A budget built on chosen labels fails exactly when some collection of real steps arrives at and
leaves every label equally often, so that it looks like a closed round trip, yet takes more time than the allowance.
The real states along it need not join up at all.

**Why it matters.** It explains all the failed candidates of G166 to G182 at once, without claiming that every
shortcut must fail. A budget that works would still need a bound on its size as the period grows.

**An everyday picture.** A map that gives two stations the same name shows a round trip that does not exist, and a
fare chart built on the names cannot charge for it.

## G184
How fast periods must grow along an edge history: stages that are long only in proportion to their period are not
enough.

**What it says.** Along a history the period stays fixed for a stretch, a stage, and then doubles. Divide each
stage's length by its period. Depth divided by the current period is then a running total that halves at each
doubling before the new stage's share is added. For the period to become small compared with the depth, that total
must grow without bound; stages whose length is a fixed multiple of their period leave it stuck.

**Why it matters.** It states gap 2 exactly, as a condition on stage lengths that can be checked, and shows which
easy hopes are not enough.

**An everyday picture.** Savings that are halved at every birthday: only deposits that keep outgrowing the halving
make the balance climb for ever.

## G185
After a doubling, a stripe can become maximally complex again in just three steps.

**What it says.** One measure of a stripe is how many times it must be compared with itself shifted by one tick
before nothing is left (its difference order). GPT builds a family of compatible histories that start a new stage
one above the minimum and reach the maximum three steps later, the last step jumping almost the whole way. Local
checked that the period-4 member lies on the real history.

**Why it matters.** It kills the hope that this measure climbs one notch per step and so forces long stages.
Something else must bound the stage lengths.

**An everyday picture.** A kettle's gauge can jump to full in a moment; that tells you nothing about when it will
boil.

## G186
For the Thue–Morse and paperfolding cases, slow period growth only some of the time is enough.

**What it says.** Assume the timing budget of gap 1. Then to exclude Thue–Morse and the recorded paperfolding codes,
it is enough that the period is very small compared with the depth at infinitely many depths, not at all of them.
Local second-read it (L151).

**Why it matters.** It weakens what gap 2 has to prove. Neither this nor the budget is yet proved on the real
histories.

**An everyday picture.** A detective doesn't need fingerprints on every surface in the room, only that, however long
the search goes on, another clear print keeps turning up.

## G187
The period need only be a small enough fraction of the depth, not a vanishing one.

**What it says.** A fixed timing budget sets a fixed fraction. If the period falls below that fraction of the depth
infinitely often, the Thue–Morse and paperfolding contradictions go through. Lining the repeat up with the period's
power of two improves the fraction. Local verified the reduction (L152).

**Why it matters.** It weakens gap 2 further, to a target with a definite size. The real histories have not been
shown to meet it.

**An everyday picture.** A photograph needs the subject to fit in the frame with room to spare, not to shrink to a
dot.

## G188
After a period doubles, an all-white stripe cannot come back within eleven steps.

**What it says.** Once the period is at least 4, the doubling leaves the stripe's two halves as exact opposites of
each other, and that rules out an all-white stripe at each of the next eleven steps, checked one position at a time.
A return at step eleven exists elsewhere, but only with an odd period, which a doubling cannot produce.

**Why it matters.** It is a real restriction on the history, but of fixed length: it does not grow with the period,
so it gives no long-term growth.

**An everyday picture.** A train that has just left a terminus cannot be back within eleven stations; that says
nothing about how long the line is.

## G189
An odd-length return to an all-white stripe takes longer as the period grows.

**What it says.** For a stripe whose period is a power of two, a first return to all white after an odd number of
steps takes at least twice the number of doublings so far, plus three. Working backwards from the end, each new tick
of the stripe is fixed by a few before it, so an odd return follows a set track. Even-length returns can branch, and
escape the argument.

**Why it matters.** It gives a restriction that grows with the period, though only slowly, and isolates the even
returns as the hard case.

**An everyday picture.** A model railway whose points (the switches where the track divides) are all fixed follows
one set route, and you can count how long a circuit takes; make one set of points free to go either way, and the
count no longer limits the journey.

## G190
An even-length return can be followed by keeping the stripe's two halves together.

**What it says.** Follow two windows of the stripe side by side, one on each half. A return after a doubling is a
walk through the finite map of such pairs that ends with the two starting windows swapped. Joined to its swapped
copy, the walk closes into a full repeating stripe whose halves are opposites.

**Why it matters.** It keeps the tick-by-tick link between the halves that a simple count of black and white would
lose. The real maps have not been classified, and it gives no delay estimate.

**An everyday picture.** A barn dance where two partners end a figure on each other's spots: dance the figure again
and they are back where they started, and the two figures together make one full repeat of the dance.

## G191
Walks that swap the two halves either exist for every large period or for none.

**What it says.** In a finite map with a swap symmetry, walks to the swapped start of half a period's length either
exist for every large enough power-of-two period, or only for periods below the number of positions in the map.
Checking one period beyond eight times the square of that number decides which. Local reviewed it (L157). In Rule
30's maps, the first case needs a fork inside a region the walk can circle.

**Why it matters.** It turns 'do return delays keep growing?' into a finite check on each map. The real maps are
still unclassified.

**An everyday picture.** A model railway with sidings and loops: whether two trains can end up in each other's
places after a given number of laps depends on how the track is laid, and checking up to a known number of laps
settles it for good.

## G192
The map for returns of length eight has no loop at all.

**What it says.** A closed walk in the paired map for eight-step returns would give two stripes, each with no two
black ticks together and no three white ones; the pairing then forces a pattern that breaks those very rules. Local
reviewed it (L159).

**Why it matters.** It confirms by hand one of six small maps that Local found had no loops. Each stripe alone can
satisfy the condition; it is the pairing that fails.

**An everyday picture.** Two rows of lights, each allowed by the rules, can still be impossible as a pair when they
must agree and disagree in a set pattern.

## G193
The paired map can be shrunk, provided each step records whether the pair changed order.

**What it says.** Many positions in the paired map can be dropped without losing any loop or any swapping walk, and
the two windows can then be stored as an unordered pair, as long as each step carries one bit saying whether their
order flipped. The bits along a walk then tell a swap from an ordinary return.

**Why it matters.** It makes the swap visible and the maps smaller. It classifies no larger map and gives no growth
bound.

**An everyday picture.** Two cards kept in an envelope, with a note at each move saying whether their order changed:
back at the same pair, the notes say which card is now on top.

## G194
Two yes-or-no equations decide whether a loop region can keep swapping.

**What it says.** For a region of the shrunken map that a walk can circle, two simple equations on the order bits
decide everything: either swaps never happen, or they are locked to one period, or every large enough power-of-two
period allows one.

**Why it matters.** It turns the swap question for any one region into a quick finite test. No larger real region
has been classified.

**An everyday picture.** Two strands of rope coiled together: they may never cross, cross once every turn of the
coil, or cross in a way that fits coils of almost any length; a quick count on one turn shows which.

## G195
A small local pattern proves the swaps can mix, but only if a way back exists.

**What it says.** Two steps from the same place with opposite order bits occur exactly at one small pattern of four
windows. Inside a region a walk can circle, that pattern settles G194's test in favour of every large period. The
length-eight map contains the pattern but has no loop, so there it proves nothing.

**Why it matters.** It gives something concrete to search for without classifying a whole map, and shows why a local
fork alone is not enough.

**An everyday picture.** A triangle of railway track (a wye) can turn a train round, putting its carriages in the
opposite order; but to choose between turning and not turning again and again, there must be a line that brings the
train back to the junction.

## G196
A quick test says whether a window can be followed by either next tick.

**What it says.** Adding up a few shorter backward checks shows how the final constraint changes when the next tick
flips, and so whether a window accepts both. A pair of windows forks exactly when each accepts both.

**Why it matters.** It tests forking in general, beyond the pattern of G195. A fork matters only inside a region a
walk can circle, and the length-eight map forks without one.

**An everyday picture.** Two doors stand open from the same corridor; that says nothing about whether either leads
back.

## G197
A stripe that leaves the known loop cannot rejoin it quickly.

**What it says.** While the first changed tick is still inside the window, the unchanged part keeps recording the
old phase, so the window cannot match the old loop whatever follows. For the known exits at period 16, that means at
least 26,396 steps before any rejoining.

**Why it matters.** It shows that a short search for a way back cannot succeed here. It does not show that a way
back, or any legal continuation, exists.

**An everyday picture.** A typo in the scrolling news ticker at the bottom of a television screen stays in view
until enough text has scrolled past.

## G198
A way back matters only if it arrives out of step with the old loop.

**What it says.** In a region containing the known loop, swaps keep happening exactly when some walk leaves and
comes back at a position different from the one its length predicts. Coming back in step keeps the old period
locked.

**Why it matters.** It names the exact thing a search would have to find. No out-of-step return is known for the
period-16 exits, and finding only in-step ones would not rule one out.

**An everyday picture.** A clock hand taken off and put back: it agrees with the old rhythm only if it lands where
the elapsed ticks say it should.


## G199
Two identical periodic strips do not tell us where they came from.

**What it says.** A recorded eight-tick strip, paired with itself, runs backward to a starting pair excluded by the complete rooted eight-tick map. It never reaches the zero starting point.

**Why it matters.** Equal endpoint strips and a period that is a power of two cannot replace the ancestry test. A second recorded doubled entry returns after88 steps, whereas the unique rooted eight-tick entry needs371. Even the stronger doubled-entry condition cannot replace ancestry.

**An everyday picture.** Two identical shells on a beach tell you nothing about which tide brought them in.

## SP01
How many odd socks a laundry loss leaves, and how long a wait for a matching pair takes.

**What it says.** A drawer holds n matched pairs. If k socks go missing at random, the number left without their
partner (orphans) is k(2n − k)/(2n − 1) on average. Two socks pulled out at random match with chance 1/(2n − 1), so
someone who pulls two at random from a full drawer each morning waits 2n − 1 mornings on average for a matching
pair. A drawer of identical black socks never strands one while two remain. Cloud proved it by counting; GPT
counted again a different way and checked every small case exactly.

**Why it matters.** It came from the owner's break-room story about socks, and shows the room's chatter becoming a
checked result. GPT's reading also marks where it stops: the waiting time assumes the drawer is refilled every
morning, and with two pairs and no refill a match before the drawer empties has only a one-in-three chance.

**An everyday picture.** Ten pairs of patterned socks in a drawer, two grabbed in the dark each morning: about once
in nineteen mornings they match.

## SP02
Taking turns to trim a cake always gives everyone a fair share, but not always a share nobody envies.

**What it says.** In the last-diminisher rule (each person in turn may trim the offered piece down to what they
think is their fair share; the last to trim takes it) everyone ends up with at least a fair share by their own
judgement, and with two people nobody envies the other. The first person served gets exactly a fair share, and
envies someone unless the other pieces all look equal to them. Cloud's spark claimed that from three people up envy
is certain; GPT showed it is not, with a whole family of tastes for which nobody envies anybody, and a worked
three-person example that Cloud checked in exact fractions.

**Why it matters.** It keeps a refuted claim and its correction side by side, as the record does for the prize
work. Fairness (a fair share each) and freedom from envy (nobody prefers another's share) are different
guarantees, and this rule gives only the first.

**An everyday picture.** A cake is plain except for a band of icing along one end, and three people all prize the
icing above everything else. The first takes all the plain cake and a sliver of the icing; the rest of the iced end
is cut in half, and since icing is icing to everyone, nobody would swap.

## SP03
Why a line of marchers or cars ripples like a concertina when people react too slowly.

**What it says.** Each walker adjusts their speed to the gap in front of them as it was a reaction time earlier.
Multiply how strongly they respond by how late they respond: if the product is at most a half, no ripple grows from
one walker to the next; above a half, slow ripples grow at every walker. Between a half and $\pi/2$, each walker
on their own would still settle. This is a classical result of traffic research (Chandler, Herman and Montroll, 1958), here with
its proof written out.

**Why it matters.** It is the threshold the marching spark (SC9) measured: a half-second delay kept the column
together, while a one-second delay made the back's ripples a hundred times the front's.

**An everyday picture.** On a motorway one driver taps the brakes, and a mile back the traffic stops dead for no
visible reason: the phantom jam.


## G200
A period can last through several returns to zero before it doubles.

**What it says.** On one rooted history, add the distances between successive zero drivers inside a period stage. Their sum is exactly the stage's length. Intermediate even-parity zeros branch without changing the period; only the final odd-parity zero doubles it. A bound on the number of returns would let the largest return control the sum, but that bound is unknown.

**Why it matters.** The period16 stage already has an intermediate branch. Its measured first return is only the first contribution to its total length. This keeps the growth target tied to the whole stage.

**An everyday picture.** A journey can be long because one stretch is long or because it has many short stretches. Measuring only the longest stretch misses the second possibility.


## G201
Two branches separate their black cells for one profile, then can overlap again.

**What it says.** Immediately after complementary post-split drivers, the two resulting profiles have disjoint black cells. Together they leave no two consecutive zeros. That separation is temporary: at the known rooted period16 branch, both following profiles are black at phase3.

**Why it matters.** A joint bound on two siblings need not control whichever history is selected, and this separation cannot be carried forward as an invariant to bound cumulative returns.

**An everyday picture.** Two lanes can be clear of each other at one junction and meet at the next. The first junction alone does not describe the whole journey.


## G202
Shared black cells between neighbouring profiles add up to the source a stretch returns to, plus an even surplus.

**What it says.** Take one stretch of history between two all-white profiles and count the black cells each profile shares with the next. Counted odd or even, the total matches the source the stretch returns to: even for a branch that keeps the period, odd for the exit that doubles it. Counted exactly, the total is that source's number of black cells plus twice the number of moments when the next profile turns from white to black while the current one is white. Three odd-or-even counts of a pair do not predict the next profile's count: the actual history has two pairs that agree on all three and are followed by profiles that differ.

**Why it matters.** It is an exact check that any future argument about the total length of returns must pass, and it bounds the shared cells over a whole period stage from below. But one step can share many cells at once, so the bound does not show that stages grow longer.

**An everyday picture.** A light switch's final position tells you whether it was flipped an odd or even number of times, never how many. Counting people through a door is closer, but a wide door lets several through at once, so the count does not say how long it stood open.


## G203

**Status:** GPT hand proof, awaiting independent review.

**What it says.** Each nonconstant zero-return excursion already pays a fixed overlap cost at its start and finish. Longer returns pay at least one extra unit in the rise count.

**Why it matters.** A charge that is compulsory in every excursion must be separated from a growing surplus. These bounds still do not establish period growth.

**An everyday picture.** A journey's departure and arrival costs are already in the bill; paying them does not tell us how far the journey went.


## G204

**Status:** GPT hand comparison, awaiting review; conditional on Local's finite run bounds.

**What it says.** The history reaching period64 first also has the shortest period32 stage. The remaining histories have already been followed far enough to rule out a shorter stage.

**Why it matters.** Entry minima can belong to different histories. This comparison preserves each history's entry and exit rather than subtracting unrelated minima. It gives a finite stage value, not future growth.

**An everyday picture.** The first runner to finish need not have run the shortest race; comparing starting times and how far the others have progressed can settle that separately.


## 21
Every way the left side can grow through period sixteen has been listed, and there are only sixteen.

**What it says.** Started from the single cell, the left side can branch at a few places while its repeating pattern is sixteen steps long. Following every branch shows exactly fifteen places where it can split, and sixteen ways it can go, each reaching a repeat length of thirty-two after between about 88,000 and 894,000 steps. The single cell's own history gets there first.

**Why it matters.** It replaces a lower bound with a complete list. Every possible history is now known to take at least 87,867 steps to double its repeat length to thirty-two, and at most 894,235.

**An everyday picture.** A family tree drawn out to the last cousin: instead of guessing how many lines there are, every line has been followed until it ends.


## 22
No history reaches a repeat length of sixty-four before about 65.8 million steps.

**What it says.** Following all sixteen histories further, side by side, the first one to double its repeat length again, from thirty-two to sixty-four, does so after 65,821,413 steps. Every other history is still at thirty-two at more than 67 million steps.

**Why it matters.** The number of steps each doubling takes, measured against the repeat length, has jumped from about 2,746 to over a million. That is finite evidence that the doublings keep slowing down, though not a proof that they always will.

**An everyday picture.** Runners on many paths at once: the first to cross the line sets a time that every other runner is known to be slower than, because everyone else was still running when the first one finished.

## SP04
Why a granny bow can't be tugged into a reef bow: they are different knots, and only one is its own mirror image.

**What it says.** Under every shoelace bow is either a reef knot or a granny knot. The two are different knots: no
amount of pulling, pushing or adjusting turns one into the other without untying. The reef is made of a left-handed
half-knot and a right-handed one, and is its own mirror image; the granny's two halves have the same hand, so it has
a separate mirror twin. The proof uses the Jones polynomial, a formula that any two equivalent knots share, and a
computer check worked it out directly from drawings of the knots.

**Why it matters.** It came out of two break-room entries, GPT's bow and Local's word heterochiral, which turn out to
describe the same thing. It is a classical result, written out here so that it can be checked on its own page.

**An everyday picture.** A bow whose loops lie along the shoe instead of across it is usually tied as a granny.
Tugging will not fix it; retying with the first half-knot crossed the other way will.


## 23
Some histories take more than 26 billion steps to double their repeat length from thirty-two to sixty-four.

**What it says.** All the histories were followed side by side, through every place where one splits into two, for about 26.4 billion steps. Fifty-six of the seventy-three that arose doubled their repeat length to sixty-four along the way. The first did so after about 66 million steps, the last of them after about 26.2 billion. Seventeen had still not doubled when the count stopped.

**Why it matters.** It shows how widely the histories spread out at this stage: the slowest are at least four hundred times slower than the fastest. The doublings keep getting rarer, and much more so for some histories than for others.

**An everyday picture.** A marathon where the leader crosses the line in two hours and the course has to close while some runners are still out after a week: the finishing times say as much about the spread as about the winner.

## 24

After a lone black cell drives the pattern, the three steps that follow cost the most when the clock arrives just after that cell.

**What it says.** The project keeps a reference clock and charges a "debt" when the pattern runs slower than that clock allows. When a driving row has a single black cell, the next two rows are forced into a known shape (GPT's GC340). This result shows that the debt over those three steps is largest when the clock arrives one step after the black cell, whatever the arrival time. So the worst case can be priced exactly, without the extra allowance that a general shift of the clock would add.

**Why it matters.** The open target is to show that the clock's debt stays bounded. Each lone-cell event can now be charged its exact worst case rather than a padded one, a saving of nearly a full period for each event. It does not yet say how many such events a history has, or how they overlap.

**An everyday picture.** A train that leaves once an hour: the longest you can wait is when you arrive just after it has gone. Whatever time you turn up, after it leaves you are on its timetable, so only your first wait depends on when you came.

**GC570 extension of entry 24 (awaiting reading).** A full-line driver list beginning with a pulse has fixed suffix delays after every arrival, so its all-interval debt is worst just after that pulse. Reviewed GC335's joined seven-edge window therefore has full-line any-arrival charge 4q-31/2 rather than 5q-33/2 for dyadic q>=8. Birth interruptions and interior restarts remain outside this sharpening. No rooted count or gap bound.

**GC571 joined-window birth extension (awaiting reading).** Checking all seven restarted suffixes gives the uniform all-subinterval budget D=4q-31/2 for dyadic q>=8. G9 then transfers D without phase overhead to the fixed list with normalized birth barriers beta_j<=j. Actual global block normalization, rooted counts and complementary gap debt remain separate. The old E restart guard is explicitly paid by its q-1 first delay.

**GC572 actual birth normalization (awaiting reading).** Under b_j=max(0,j+1-L), a consecutive nonzero block pays at most one clamp at its entrance and none inside. GC335's actual joined-window debt is therefore at most 4q-29/2 for dyadic q>=8, or 4q-31/2 if its entrance clamp is inactive. The additional tick is attained by a formal reset control; rooted attainment is not asserted. Counts and complementary gaps remain open.

**GC573 mixed-gap birth accounting (awaiting reading).** Each positive clamp under the standing schedule follows a distinct zero driver, so sum c<=W(M-1)<=W(M). G6 gives T(M)<=M+sum z along the actual clamped path. This absorbs the explicit birth term but leaves selected zero waits uncontrolled; comparing to an unclamped path is not justified.


## 25
How heavy the row before a lone black cell is can be read off the row after it: count its black stretches.

**What it says.** Take a driving row with a single black cell, and the row it produces next. The row before the lone cell is fixed by that next row, and its number of black cells is twice the next row's number of black stretches, give or take one depending on what sits at and just after the lone cell. So a "heavy" earlier row, with more than three black cells, forces the next row to have at least two separate black stretches. It also fixes whether that earlier row has an odd or even number of black cells.

**Why it matters.** GPT's latest steps charge each lone-cell event a debt that depends on the lengths of the first gap and the first black stretch, and bound those lengths by the earlier row's weight. This identity explains where GPT's weight thresholds come from, and with GPT's bound it shows that one of the earlier caps is never reached. It does not count how many such events there are.

**An everyday picture.** A fence painted in stripes: the number of places where the paint changes colour is always twice the number of painted stretches. Knowing how many colour changes a painter made tells you how many stretches there are, and so how long any one stretch can be.

## 26

The wheel's jolts can only be of a few fixed sizes, and the cells near the edge decide which sizes are possible, whatever happens further in.

**What it says.** Next to the striped edge, the second column runs like a wheel. Now and then something arriving from the chaotic interior knocks it to a new position: a "kick". This result shows, by an exhaustive finite computation, that once the wheel has run for about two and a half turns, a kick can happen at only four points of its turn. At each of those points it can only be one of five or six sizes. For the two kick points actually seen in simulations, the allowed sizes are exactly the sizes that were measured on more than eleven thousand real kicks.

**Why it matters.** It was thought the kick sizes came from the chaotic interior. They do, but only the choice among a short, fixed list does. The list itself is fixed by about sixteen columns of local structure. That bounds how much information a kick can carry. It does not say kicks must keep happening, which is what a full proof would need.

**An everyday picture.** A gearbox: whatever the driver does with the pedal, the car can only be in one of the gears the box was built with. The driver chooses the gear; the gearbox decides what the gears are.

**GC588 entry 26 timing outcome (single-party, awaiting reading).** The 56-observation minimum old lock has a wider necessary local projection than the 57-observation table: it additionally permits class 19, sizes -8 through -4, with only 21 new observations fitted. All shared alphabets agree. The original and settled certificates keep their stated timing; no true short-lock event is constructed.


## G205
A short prescribed stretch of the wheel forces the neighbouring column; a longer stretch forces the next two as well.

**What it says.** Beside the alternating wall, suppose column1 follows the recorded56-step wheel. Thirteen consecutive observations determine column2 at their centre. One hundred and forty-three observations determine columns2,3 and4 at their centre. Their values follow three explicit56-step words. The statement allows any right exterior.

**Why it matters.** This is a precise form of local rigidity: a temporal pattern in one column restricts its neighbours. It supplies fixed-depth forcing, rather than proving that the forced region keeps widening with time.

**An everyday picture.** Hearing a short passage from a familiar duet determines the other singer's note at its centre. A longer passage determines two more voices, although it does not tell us what the whole orchestra is playing.

## G206
Once a departure is impossible after a given amount of time on the wheel, it remains impossible after longer stays.

**What it says.** Consider every starting parity and allowed phase, with an unrestricted initial row. A witness with a longer wheel history can be cut to a shorter history before the same departure and subsequent21 observations. After shifting the clock by an even amount, the shortened witness is one of the allowed cases. Thus impossibility across all cases persists as the required duration grows.

**Why it matters.** It supplies the monotonicity premise for the threshold search and carries a certified prohibition to longer histories. It does not verify a solver's answer or establish the minimum threshold.

**An everyday picture.** A recording showing a singer hold a tune for a minute also contains a recording of its last thirty seconds. Changing where the recording begins does not change the ending.

## 27
Once the wheel has turned for 140 steps, its jolts come in exactly sixteen kinds, and a fourth kind is impossible.

**What it says.** Earlier work showed the wheel's jolts ("kicks") could only come at four points of its turn, with at most six sizes each. This result settles the list exactly once the wheel has run 140 steps. One of the four points can never produce a kick at all, which three independent checks confirm, the last with machine-verified proofs. At the other three points, every size on the list really can happen, with an example found for each. So after 140 steps there are exactly sixteen possible kinds of kick.

**Why it matters.** It turns an upper bound into an exact answer, and it explains why one kind of kick never appears in simulations. It does not say how often each kind happens, or whether the kicks must go on for ever, which a full proof would need.

**An everyday picture.** A vending machine with a fixed menu: someone has now pressed every button that works and confirmed which one never dispenses anything.

## 28
When the wheel is jolted to a new position, it lands on a spot of the same parity and the opposite colour, which is why its forward jolts all land in one short stretch.

**What it says.** Next to a column that alternates black and white, the neighbouring column behaves like a wheel turning a fixed step each tick. When it jumps to a new position (a kick), the new position must have the same parity as the old one and the opposite colour, and a jump can only start right after a white. The wheel's only black spots at even positions form one short run, so every forward jump from the usual starting points lands there.

**Why it matters.** A two-line argument explains the landing window Cloud saw in the tables, and why each forward kind of jolt has at most six sizes. It does not say which jolts actually happen; that needs the computed results (entries 26 and 27).

**An everyday picture.** A chess bishop on a white square can only ever reach white squares, whatever the position on the board. Here the rule is a little different (same parity, opposite colour), but it fixes the possible landings before any details of the game come into play.

## 29
Rule 210 with an empty left half has exactly one way to keep its centre alternating: start from the sites that share no factor with 6.

**What it says.** Fix every cell left of the centre white and ask the centre to read white, black, white, black for ever. Then the starting row on the right must be black exactly at 1, 5, 7, 11, 13, ..., the numbers coprime to 6. That row works (its centre counts are odd numbers of the form (2^n + 1)/3), and no other row does.

**Why it matters.** It settles a whole family that a long chain of GPT's lemmas had been narrowing column by column: there is only one member, and it is a plain Rule 90 pattern. It also shows that no finite starting row with an empty left half can keep this clock. It says nothing yet about rows with something on the left, or about Rule 30.

**An everyday picture.** Think of a row of dominoes where any wrong piece, placed anywhere, topples into the centre within three more pieces. Checking that once for each of six positions in the repeating pattern, plus the first 121 pieces by hand, leaves room for only one arrangement.

## 30
The Collatz demand laws always rise to a single peak and then fall, at every horizon.

**What it says.** In GPT's accounting of how Collatz-style survivors are spread over odd-step counts, each time step reshapes a "demand" distribution by one of two averaging moves. One move can create a dip on its own, but in the real schedule it never acts alone: it always follows the other, smoothing move, and that pair keeps any single-peaked shape single-peaked. So every actual demand law has one peak.

**Why it matters.** It supplies the shape condition an earlier comparison (G218) needed, so that comparison holds for every real case, not just the 1,024 horizons checked by computer. It orders the available error bounds; it does not bound the error itself or prove anything about Collatz.

**An everyday picture.** Pouring sand through two sieves in a fixed order: the coarse sieve alone can leave a ridge, but because the fine one always goes first, the pile that comes out still has a single top.

## 31
Even with a few black cells allowed on the left, Rule 210 cannot keep its centre alternating from a finite starting row.

**What it says.** Allow any black cells within six places left of the centre. If one sits at an even distance, the alternating centre fails within six steps. If all sit at odd distances, there is exactly one way to continue on the right, and it is the coprime-to-6 pattern of entry 29 with a few cells mirrored, which never ends. So no finite starting row of this kind works.

**Why it matters.** It answers question B, whether a finite starting row can produce the alternating centre, for every left side of width up to six. Wider left sides remain open, because the check close to the centre does not carry over by symmetry.

**An everyday picture.** A melody that must keep a steady beat: a few extra notes at the start can be answered by adjusting a few notes on the other side, but the tune itself never ends, so no finite score keeps the beat.

## G207
Three specified beats on one column make a neighbouring bit repeat two steps later.

**What it says.** If one column reads white, black, black on three consecutive rows, and its right neighbour begins white, that neighbour has the same bit on the following row and two rows later. The cells farther right cannot change this equality.

**Why it matters.** It explains why two apparently free choices next to the wheel move together. It provides a local reason for a correlation that was first found by checking a finite graph. It does not decide whether their shared value is black or white.

**An everyday picture.** Two switches that appear independent but move together because of a connecting rod. Seeing the connection explains their agreement without telling you which position they will occupy.

## G208
Following the wheel for long enough fixes two more columns beside it.

**What it says.** Requiring Rule30 through column15 makes columns2 through6 follow five fixed words. A193-observation wheel window fixes column5 at its centre; a conservative303-observation window fixes all five there. Shorter strips may still have choices that cannot continue through the wider exact dynamics.

**Why it matters.** It extends the known fixed strip by two columns and separates a local ambiguity from a choice that can survive wider constraints. It does not show that the fixed strip grows without limit or settle the prize problem.

**An everyday picture.** A jigsaw piece may fit a small patch but fail when another row of pieces is added. The wider patch fixes a choice that the smaller one leaves open.

## G209
Two small initial patterns guarantee a black square four ticks later.

**What it says.** Under Rule30, either the seven-cell pattern0101110 or five specified cells in the pattern1110?1 guarantee that the fifth cell is black after four updates. Every unspecified initial cell may be chosen freely. The proof needs no blinking wall or wheel.

**Why it matters.** A short Boolean argument explains the final step of a correlation first found by exhaustive computation. Reaching either pattern from an earlier prescribed strip remains a separate computed obligation; this does not explain the wheel's eventual departure limit.

**An everyday picture.** A few correctly placed dominoes guarantee one particular fall, even though the rest of the arrangement is unknown. Establishing that those dominoes were placed correctly is a different job.

## G210
Five initial squares and eight boundary beats link two later observations.

**What it says.** Begin with11100 in cells2 through6 and an alternating boundary for eight updates. If cell6 is black after eight updates, cell5 must be black four updates later. All other initial cells can be arbitrary. A hand argument carries the initial pattern to one of the two local patterns of G209.

**Why it matters.** It replaces an exhaustive reachability check with an independently reviewed proof. Earlier shortcuts lost necessary correlations with neighbouring cells; this argument preserves them through one complete local update. It does not explain the wheel's long departure threshold.

**An everyday picture.** Two warning lights cannot display one particular combination because a shared connecting mechanism links them. The explanation follows that mechanism rather than trying every setting of the surrounding switches.

## G211
A white block has four possible preceding patterns, with variation only at one end.

**What it says.** If Rule30 produces L consecutive white cells, the L+2 cells feeding that update are either all white or have L black cells followed by01,10 or11. Those are exactly the four possibilities, regardless of cells outside the interval.

**Why it matters.** It identifies the shape of an actual white block's previous row. It preserves the exceptions at the right boundary that a constant-row shortcut would lose. An arbitrary initial row need not have a finite predecessor, so this alone cannot strengthen the initial-row record search.

**An everyday picture.** A row of lights can go dark through four switch arrangements. Three arrangements look the same along most of the row but differ at the end; that small difference matters when the row has an open boundary.

## G212
A sequence of observations cannot recover more information from a noisy initial row than its fresh inputs permit.

**What it says.** For T centre observations starting from independent fair bits, independently flipping each initial bit with probability q leaves at most T times one minus the binary entropy of q bits of information about the observations. Evolving the noisy row and comparing its centre trace obeys the same bound.

**Why it matters.** Each new observation uses a fresh leftmost input. Even after seeing the noisy row and earlier observations, that input retains the channel's uncertainty. Adding these conditional uncertainties gives a sound bound for the whole trace, despite correlations that prevent adding marginal information. It does not establish complexity for a particular seed.

**An everyday picture.** Each answer depends on another hidden switch. A noisy view leaves uncertainty about every fresh switch; the full sequence must still pay for that uncertainty.

## G213
Cumulative parity imbalance interacts with changes in future survival demand.

**What it says.** The exact count increment can be rewritten using cumulative odd-minus-even counts and neighbouring differences of the demand weights. Centering those cumulative counts gives an upper bound from their range times the full variation of the demand.

**Why it matters.** It offers another way to study the actual allocation without assuming a bell-shaped demand law. Both boundary jumps must be counted. The bound can be worse than the earlier absolute sum, and a useful asymptotic estimate still needs control of the actual allocation.

**An everyday picture.** Instead of counting surpluses separately in every bin, keep a running surplus and pair it with how the price changes between bins. The endpoint price changes matter too.


## G214
A finite Rule210 row cannot keep a nonzero periodic centre while its nonlinear gates remain silent for too long.

**What it says.** With initial support bounded by R and centre period p, every time s after periodicity begins has a nonlinear activation by time3*s+2*R+3*p.

**Why it matters.** It quantifies the earlier requirement of arbitrarily late nonlinear events. The proof separates two shifted linear copies at a dyadic time, forcing a full period of centre zeros if no gate fires. It does not locate the gate or exclude a finite witness.

**An everyday picture.** Two expanding copies eventually leave a gap at a watched point. A repeating signal there needs another contribution before that gap lasts an entire period.


## G215
A black periodic wall sample requires odd parity of actual nonlinear events in its selected backward cone.

**What it says.** At one black time in G214's dyadic block, the binomial propagation weights select an odd number of active source cells. For full0101, all strictly-left sources disappear and selected cells have time plus site even.

**Why it matters.** It places the required events inside a precise causal cone. Merely counting events in a geometric cone misses zero coefficients and cancellation. The cone still grows, so finite compatibility remains open.

**An everyday picture.** Several contributions can reach an observation, but some paths carry zero weight and two matching contributions cancel. The selected total must match the observation.

## G216
The two nearest nonlinear source columns cannot supply a black0101 wall sample.

**What it says.** Their allowed activation times have the wrong parity to affect odd centre times. Together with G215's left-source exclusion, a required event must begin at site2 or farther right.

**Why it matters.** It sharpens spatial necessity term by term. The sources can still activate at times when they are invisible to that observation. A finite seed gives a site2 contribution, so the same local argument cannot discard that site.

**An everyday picture.** A signal can be present but miss the observation's timing. The nearest signals miss; a farther signal can arrive.


## G217
Demand-weighted centering improves the earlier global range bound on cumulative parity allocation.

**What it says.** Center the cumulative imbalance at a weighted median, with weights given by absolute demand gradients. This minimizes the resulting absolute-sum bound and never exceeds the global midpoint estimate.

**Why it matters.** It retains which cumulative values the changing demand actually uses. Seven small cases show improvement over an older absolute bound in four cases, but no general comparison or asymptotic count estimate follows.

**An everyday picture.** Choose a reference value using the points that carry weight, rather than distant extremes that nobody uses.


## G218
Unimodal demand makes weighted centering no worse than the earlier absolute allocation bound.

**What it says.** If nonnegative demand rises to a mode and then falls, use the cumulative imbalance at that mode as a centre. Telescoping on the two sides bounds the optimized objective by the original weighted absolute sum.

**Why it matters.** It provides a shape condition under which the new bound is guaranteed to improve or tie. Actual demand unimodality is unproved; a separated-spike demand defeats general domination. The terminal single-spike layer ties exactly.

**An everyday picture.** With one hill in the weights, choosing a reference at its summit accounts for both slopes. Multiple hills need another argument.


## G219
A critical averaging step need not restore unimodality after an edge fold.

**What it says.** An explicitly log-concave five-atom input develops a strict internal valley after the flat-edge and critical operators. A critical step alone preserves this example's unimodality.

**Why it matters.** Isolated flat steps cannot justify arbitrary-input shape induction. The actual backward law needs an additional reachable-law constraint; this synthetic failure does not establish actual non-unimodality.

**An everyday picture.** One local smoothing step does not necessarily undo a distortion introduced at the boundary.


## G220
Demand superlevel intervals give an allocation bound no worse than both earlier absolute bounds, without assuming demand shape.

**What it says.** Split each demand level into its connected intervals, sum the signed imbalance inside each, then take absolute values. The resulting bound is at most the original weighted absolute sum and at most optimized centering.

**Why it matters.** This removes the need for actual unimodality solely to order the bounds. A uniform count estimate still requires controlling interval imbalance; cancellation between separate intervals and times is discarded.

**An everyday picture.** Group contributions only where the demand level connects them. Empty gaps should not make unrelated contributions into one interval.


## G221
The gap between optimized centering and component allocation is exactly a weighted distance to endpoint segments.

**What it says.** Each demand component gives a real segment joining its cumulative-imbalance endpoint values. The two bounds tie precisely when all those segments share a point; merely touching is enough.

**Why it matters.** It identifies which geometry explains the recorded ties and where a strict improvement must occur. It does not estimate the component bound itself or the final count ratio.

**An everyday picture.** One common meeting point costs nothing extra. Separate acceptable meeting intervals impose an unavoidable travel cost.


## G222
Interior two-step00 and11 occurrences at the same count pair to a second difference.

**What it says.** Match their minimum multiplicity. The matched coefficient is curvature divided by2, while each mixed word contributes negative curvature divided by4. Unmatched equal-bit and boundary contributions remain explicit.

**Why it matters.** It names a second mechanism for temporal cancellation, beyond individual mixed paths. The actual class allocation and residual terms still need control.

**An everyday picture.** Two opposite changes can shed their shared trend while leaving curvature; matching the wrong labels breaks that bookkeeping.


## G223
Matching parent branches by next count gives the same curvature identity with a triangle bound no worse than state matching.

**What it says.** Pool all odd and even occurrences landing in the same count bin, regardless of their integer states. Pairing their minimum multiplicity cancels more nonnegative demand than keeping states separate.

**Why it matters.** Actual state coalescence is unnecessary for this weighted cancellation. The unmatched signed mass remains open, and this grouping can lose cancellation already captured by the original class bound.

**An everyday picture.** Contributions can share the same accounting label without reaching the same physical place.

## G224
At certain observation times, each column at a power-of-two distance has only a short list of chances to affect the centre.

**What it says.** The binary walk-counting coefficients select exact source times on these columns. The list grows only with the number of doublings of the observation time. Other columns still contribute.

**Why it matters.** It replaces a whole time interval with a precise list to check. It does not say that an allowed source actually turns on.

**An everyday picture.** A timetable lists the departures that can reach a station before a particular appointment. An entry in the timetable does not mean someone boarded that train.

## G225
A neighbouring pair can send a selected signal only when the first column changes its effective beat.

**What it says.** On the second source column, an active pair at an even time forces a switch in the first column. For the specified empty-left rhythm, the preceding timetable shrinks to two endpoints. At the smallest exceptional scale there is only one endpoint.

**Why it matters.** Actual update equations remove most of the coefficient-selected possibilities. Farther columns and whether the remaining pairs activate still need checking.

**An everyday picture.** A timetable offers several departures, but a gate opens only at two of them. Those are the departures still possible; an open gate does not guarantee a passenger.

## G226
A white square prevents a particular neighbouring black pair two steps later.

**What it says.** In Rule210, a white square forces the pair two places to its right, two ticks later, to contain at least one white square. Under the alternating wall this removes later even-time sources in column2.

**Why it matters.** A pattern can obey forward equations yet have no allowed past. This checks that missing obligation and removes a previously apparent source possibility.

**An everyday picture.** A ticket may let someone enter the departure gate, but the required connection never arrived. Checking the journey before the gate can rule out what the gate alone permits.

## G227
The next column has a short timetable inherited from its required past.

**What it says.** Under the specified empty-left alternating wall, column3 can contribute at an early time and, on alternate doubling scales, one later time. Its other candidate times are blocked by predecessor conditions.

**Why it matters.** It combines the exact coefficient timetable with actual update constraints. It still leaves more distant columns and whether permitted sources occur unresolved.

**An everyday picture.** A connecting train can run only after its feeder arrives. Intersect the two timetables and most of the departures disappear, even though they looked possible on the second timetable alone.

## G228
The fourth column's candidate source times miss the required predecessor times.

**What it says.** Under the specified empty-left alternating wall, a black even-time bit in column2 needs an upward switch in the first column. A column4 source needs such a bit two ticks earlier. Its selected times never meet that schedule at the stated doubling scales.

**Why it matters.** It removes another entire column from the source certificate at those observation times. It leaves the third column and more distant sources unresolved.

**An everyday picture.** A shop can receive a delivery only after a connecting service arrives. Its delivery slots and that service's arrivals fall on different days, so those slots cannot be filled.

## G229
Eight specified centre bits are enough to rule out an early source pair.

**What it says.** With an empty initial left side, the first eight alternating centre bits permit only one pattern in the seven initial right cells that can affect them. That pattern has no active column3 pair at time1. More distant cells cannot change these observations.

**Why it matters.** A short prefix allowed an early source, but its longer obligations remove it. The result covers every farther tail through a finite dependency argument, without constructing a continuing clock.

**An everyday picture.** A row of seven switches controls eight lamps in a particular sequence. Checking every switch setting leaves one that matches the sequence; switches outside the wired group cannot alter those lamps during the check.

## G230
A third clock beat shuts every later odd-time gate in the first column.

**What it says.** Under the alternating wall, an even-time black bit in column2 requires its neighbouring bit in column1 to be black. The next white wall beat therefore makes column1 white. Earlier results handle the initial exceptions for the empty-left family.

**Why it matters.** Candidate gate times from weaker local checks never actually activate later. This removes column3 from the selected source sum, while farther columns remain unresolved.

**An everyday picture.** A gate can be open at one stage, but the next interlock always closes it before the scheduled departure. Checking the whole short sequence removes possibilities that one stage alone allowed.

## G231
The incoming and outgoing gates demand a one-beat visit that the clock never makes.

**What it says.** A positive-time even column2 bit can be black only if three consecutive effective inputs are010. The empty-left clock has no such isolated positive one. Its longer initial prefix also removes the time-zero bit, so this even track is entirely white.

**Why it matters.** The predecessor theorem then removes every even column4 source, extending the earlier removal at particular observation times. Farther columns remain uncontrolled.

**An everyday picture.** A visit needs arrival immediately followed by departure. A timetable in which every visit lasts at least two beats cannot supply that one-beat slot.

## G232
A two-step readout has one precisely identified nonlinear correction.

**What it says.** With a white intervening bit, the central bit two updates later is the XOR of two original bits and their farther adjacent product. If that product vanishes, the readout is additive. G231 supplies the needed premises for the stated clock family.

**Why it matters.** It expresses even column5 as the discrepancy between the next column3 bit and the prescribed effective input. It does not assume that discrepancy vanishes.

**An everyday picture.** Two signals add cleanly unless a particular pair activates a correction. Identifying that pair tells us exactly which extra condition makes the simpler readout valid.

## G233
The third column marks the switches of the prescribed effective stream.

**What it says.** In the empty-left alternating-clock family, even column3 is white exactly at effective switches. Combining this with the two-step readout gives an exact formula for even column5 from three consecutive effective inputs, including the initial boundary.

**Why it matters.** These tracks are determined without enumerating entire right seeds. They provide explicit inputs for farther predecessor arguments while leaving whole-right uniqueness open.

**An everyday picture.** A lamp marks whether two consecutive timetable entries agree. A second lamp reads a combination of three entries; neither lamp tells us the whole timetable beyond them.

## 32
No finite starting row of Rule 210 can make the centre alternate white and black forever.

**What it says.** For any finite left side, the only possible alternating-centre realization is the parity background already identified in G65, and that realization needs infinitely many black cells on the right. A first change from it sends a clearing front through pairs of diagonals and eventually meets a black background gate, where the centre clock fails.

**Why it matters.** This replaces the radius-six bound of entry31 with a hand proof for every finite radius, and proves Local's conjectured2w life law. It is an auxiliary Rule210 theorem; Rule30 still needs its own argument. Local supplied the conjecture and independent orbit evidence, GPT supplied the proof, and Local verified it by hand.

**An everyday picture.** A travelling reset can pass a finite run of open gates, but reaches a closed gate eventually. Arbitrary choices farther along cannot repair the failure.


## 33
Infinitely many finite starting rows (11, 101, 1011, 10101, ...) grow into exactly the single cell's Rule 30 pattern, except for a striped fringe on the right edge, so they all share its centre column.

**What it says.** Put a black cell, then an alternating white-black stretch, then a black cell. That fringe rides the pattern's right edge and flips every cell it touches at every step. Its two innermost stripes are always opposite, so the OR in Rule 30, the only way the fringe could reach inward, is already 1. The inside of the pattern never learns the fringe is there.

**Why it matters.** It answers the owner's cipher question in miniature: the centre column is an autokey encryption of the starting row, and it cannot tell which of infinitely many finite keys made it. A scan of every right half up to 16 cells found no other such seed. It does not touch the prize problems' difficulty, since every one of these seeds has the same column as the single cell. Cloud proved it by hand after an exploratory scan; it waits for a second reader.

## 34
A finite seed that shares the single cell's centre column must start its left half exactly where its right half, on its own, would first break that column.

**What it says.** Rule 30 pushes any difference on the left rightward at exactly one cell per step. So a black cell added deep on the left reaches the centre at a time equal to its depth, and changes the column there. A left half can only help if it arrives at the very moment the right half would go wrong. With a white or a fringe right half nothing ever goes wrong, so the left half must be white.

**Why it matters.** It turns the open half of Proposition 20 into two finite searches. Run them up to right halves of 28 cells, and left halves 500 deep, and they find nothing outside the fringe family. Whether the family is complete for all sizes is still open. Cloud proved it by hand; it waits for a second reader.

## 35
A Rule 30 row whose pattern slides faster than light is always a repeating ring. If it slides left, every short stretch of cells is the start of exactly one such row.

**What it says.** Some rows just slide: one step of the rule, or a few, gives the same row moved over. If the slide is faster than one cell per step, the rule cannot have made the row from its neighbours alone, so each cell is forced by a fixed stretch of cells beside it. That pins the row down and makes it repeat. Sliding left, Rule 30's exact passing-on of its left neighbour means nothing is lost, so every stretch of |s| + p cells grows into one sliding row. Sliding right, information is lost through the OR, and such rows are rare.

**Why it matters.** GPT's all-S ring is one of these rows: it turns 14 cells each step. A census of every sliding row up to 28-cell stretches finds it is the only one with a period-two column at all, so sliding rows give no new mixed S/L witnesses. Cloud proved it by hand; it waits for a second reader.

## 36
At every second step a white triangle touches Rule 30's right edge, and its size depends only on how many times 2 divides the step number.

**What it says.** The owner noticed that the triangles along the right edge start at evenly spaced points and differ only in size. The proof reads the edge's diagonals, each of which repeats with a period that is a power of two. At an even step, the diagonals whose period divides the step are white, as at the start. The first one whose period does not divide it has just been flipped to black. So the triangle's width is fixed by the highest power of 2 dividing the step: 2, 3, 5, 6, 8, 14, 15, 23, and so on.

**Why it matters.** It is exact order inside the side of the pattern that looks chaotic: a ruler sequence, nested like the supertiles of a hierarchical tiling. It explains why the widest triangles of the whole pattern sit on the edge at steps like 32,768 and 65,536. Cloud proved it by hand; it waits for a second reader.

## 37
A finite pattern in Rule 30 can never leave one column fixed for ever, black or white.

**What it says.** Start with finitely many black cells and run Rule 30. No single column can settle into always black or always white. If it stayed black, the rule would force a black-white stripe pattern running off to the left for ever, needing infinitely many black cells. If it stayed white, a black cell from the right walks in, sticks beside it, and forces the same endless stripes. Either way the finite start is contradicted.

**Why it matters.** This is the first case, period 1, of the question Wolfram asks: can the centre column ever settle into a repeating pattern? Condrey proved this case in 2026. Our team had cited it; here it is written out and checked twice by hand. The proof also shows exactly where the right side of the pattern is needed, which matters for the harder period-2 case.

**An everyday picture.** A row of dominoes that must alternate standing and fallen: fix one domino for ever and the alternation runs off to the horizon, but a finite set of dominoes has no horizon to fill.

## 38
In Rule 30, no pattern that starts from finitely many black cells can settle into a column that beats "one white, then q black" for ever, when q is 7 or at least 9.

**What it says.** Pick any column of a Rule 30 picture grown from finitely many black squares. It can never end up repeating one white tick followed by seven black ticks, nor one white tick followed by nine or more black ticks. A small window around the column, thirteen squares wide, is followed through every way it could possibly evolve. In every case where it can run for ever, the column next door is forced into a repeating beat of its own. Two neighbouring columns that both repeat for ever are impossible for a finite start, by a classical theorem.

**Why it matters.** It closes most of a whole family of rhythms that the centre column might have settled into. The method came from an outside project. We checked its finite cases independently and repaired a gap in its general argument. The cases it cannot reach include the rhythm that matters most, one white then one black, which is Wolfram's period-2 question.

**An everyday picture.** A drummer who plays one rest and then a long roll, over and over, forces the drummer beside them into a fixed pattern too. Two locked drummers side by side cannot both keep going when the band started from a finite crowd.

**Checked by machine.** A proof assistant (Lean) has checked the argument for every period it covers: periods 14 and above by one route, and 7 and 9 to 13 by the two-sided strip, one small step at a time.

## 39
In the walk that builds Rule 30's repeating columns one after another, every walk that starts from a blank column comes back to a blank column, whatever the period.

**What it says.** Each new column is forced by the two before it, and you can also run the rule backwards to recover the earlier column from the later two. A walk that never came back to a blank column would have to loop, and running it backwards from the loop would lead to a column before the start, which cannot exist.

**Why it matters.** It explains a computer census in which every such walk did return, and it is checked line by line by a proof assistant.

**An everyday picture.** A one-way trail through a finite maze where every junction has one way in: if you start at the entrance, you cannot end up circling forever, so you must reach an exit.

## 40
No Rule 30 picture grown from finitely many black squares can end up with a column that beats one black tick and then ten or more white ticks, over and over.

**What it says.** Next to such a column, a narrow strip of eight cells is forced into one fixed rhythm, whatever lies further out. So the neighbouring column repeats too. Two neighbouring columns repeating for ever is something a pattern with a left edge cannot do, because the edge sweeps leftwards and breaks the rhythm.

**Why it matters.** It closes almost all of one of the two "Condrey ends", a family of rhythms that had no closed case. The same short argument also gives a simpler, uniform proof of most of the other end.

**An everyday picture.** A long silence broken by a single drumbeat, over and over, forces the neighbouring drummer into one fixed rhythm too, and two locked drummers side by side cannot both keep going while a crowd advances on them from the left.

**Checked by machine.** A proof assistant (Lean) has checked the whole argument, the finite computation included.

## 41
The same short argument that closed the white end also rules out 139 more drumbeat patterns that a column of a finitely seeded Rule 30 picture might have settled into.

**What it says.** For each of these patterns, a narrow strip of eight or ten cells beside the column is forced into one fixed rhythm, so the neighbouring column repeats too, which a pattern with a left edge cannot sustain. The patterns are long: periods 10 to 18, each with a long run of white or of black ticks.

**Why it matters.** It widens the list of rhythms known to be impossible, and the computation was done twice by independently written programs.

**An everyday picture.** A rule that silences a whole family of drum patterns at once, checked by two separate referees.

**Checked by machine.** A proof assistant (Lean) has checked every one of the 139 patterns, along with the argument.

## 42
The stripes running down the left edge of a Rule 30 picture each settle into a beat, and every beat is a power of 2.

**What it says.** Number the diagonal stripes from the left edge of the pattern. Each one eventually repeats, and stripe
number k repeats with a period that divides 2 to the power k − 2: 1, 2, 4, 8 and so on, never 3 or 5. Each stripe is
driven by the two stripes beside it, and a stripe driven by two regular beats can at most double their period.

**Why it matters.** The record took this from Jen's 1986 paper, which is still unread; now it rests on the record's own
proof. It also explains the gap sizes seen in the settled band: an odd beat leaves only gaps of one cell.

**An everyday picture.** A row of drummers, each copying the two to their left with one simple rule. However the first
drummers play, each new drummer settles into a beat at most twice as long as the beats feeding them.

**Checked by machine.** A proof assistant (Lean) has checked the argument and its consequences for the gaps.

## G259
Two neighbouring columns that repeat on unrelated odd and coprime cycles cannot both be alive in Rule 30's right half: one goes blank and the other freezes.

**What it says.** Picture each column of a Rule 30 history as a strip of tape repeating in time. Suppose one column repeats every m steps, with m odd, and its right-hand neighbour repeats every n steps, with n sharing no factor with m. Then the neighbour must be all white, and the first column must never change. The neighbour's black ticks, stepping n at a time, would land on every phase of the first column's cycle, including a phase where the first column cannot accept one.

**Why it matters.** It rules out one way a hypothetical period-310 pattern might be built from smaller pieces: columns repeating every 5 steps cannot sit next to columns repeating every 31. At least every other column must carry the full 155-step cycle.

**An everyday picture.** Two gears with coprime numbers of teeth: a mark on one eventually meets every tooth of the other. If even one tooth cannot take the mark, the mark cannot be there at all.

## G260
In one family of hypothetical repeating patterns, a hidden parity is always odd, which pins down one choice that had looked free.

**What it says.** Suppose a Rule 30 pattern repeats every 310 steps, and a certain column next to its turning point repeats every 5. Then that column must be the beat 01011, and a parity that decides the next column's orientation comes out odd. So the next column's direction is forced, with no choice left.

**Why it matters.** It closes one branch of a search for possible period-2 patterns by pure reasoning, without a computer search. The harder branches, columns repeating every 31 or 155 steps, remain open.

**An everyday picture.** A combination lock with a hidden wheel: once you know one dial turns every 5 clicks, the hidden wheel can only sit in one position.

## G261
In the same hypothetical repeating pattern, every column that repeats on a short cycle must contain both a lone black beat and a lone white beat.

**What it says.** A column repeating every 5 or 31 steps cannot be made only of long runs: it needs at least one isolated black tick and one isolated white tick. The parity that fixes the next column's direction then reduces to a short sum over the column's white phases, one term per phase.

**Why it matters.** It turns the remaining question for the 31-step case into a small, exact bookkeeping problem, instead of a search over every possible column.

**An everyday picture.** A drum pattern that loops quickly must have at least one single hit and one single rest; and to know how the next drummer must play, you only need to tally a few beats of the loop.

## G262
In the hypothetical repeating pattern, if a short-cycle column has only lone white beats and its optional beats all lean the same way, the hidden parity is forced odd.

**What it says.** The column's white beats each stand alone. Rule 30 forbids two long black stretches separated by one white beat, so the long and short black stretches must take turns. Taking turns fixes the count of compulsory beats, and the parity that decides the next column's direction comes out odd.

**Why it matters.** It closes one more branch in the search for a period-2 pattern, again by reasoning alone. Anything that escapes must have a longer white stretch somewhere, or optional beats that lean both ways.

**An everyday picture.** Fence posts between single gaps: if no two tall posts may stand side by side, tall and short must alternate, and you can count them without looking.

## G263
When every white stretch in a short-cycle column has odd length, the hidden parity just counts the white stretches of length 3, 7, 11 and so on.

**What it says.** Take the same hypothetical repeating pattern. Suppose the column's white stretches all have odd length, and its optional beats all lean the same way. Then the parity that decides the next column's direction is odd unless an odd number of white stretches have length 3 more than a multiple of 4. If every white stretch has length 1, 5, 9 and so on, it is always odd.

**Why it matters.** It turns a whole family of possible escapes into one count. A pattern that escapes this way must have an odd number of white stretches of length 3, 7, 11 and so on, which narrows where to look.

**An everyday picture.** Counting cars in a train by the length of each carriage, but only caring whether each carriage is one longer or three longer than a multiple of four.

## G264
In Rule 30's moving frame, a column that stays white for a while forces a growing wedge of white to its right.

**What it says.** If one column holds the same colour for L steps in a row, the columns to its right are pushed to white in a widening wedge: two columns lose one step each, then the next two another, and so on. At the start of the run, 2L - 2 cells to the right are white. On a ring this makes the ring at least 2L cells around, or the whole row would be white and stay white for ever.

**Why it matters.** It turns a property of one column into a hard constraint on its neighbours and on the size of any repeating pattern that contains it. For the template under study it means any ring containing it has at least 14 cells.

**An everyday picture.** A long pause in one drummer's part silences the drummers beside them for a shrinking stretch, like a shadow narrowing with distance.

## G265
A Rule 150 variant with the extra AND applied only on even cells grows from a single black cell exactly like the simpler Rule 90, and its centre goes white for good.

**What it says.** Split the cells into even and odd. Every two steps, the even cells follow Rule 90's famous triangle pattern and the odd cells blank out. The extra AND does fire on the in-between steps, but over each pair of steps its effect reduces to a product of neighbouring even cells, and Rule 90's pattern never lights two neighbouring even cells at once, so that product is always zero. The centre of Rule 90's triangle is white after the start, so this variant's centre is black only at the first two steps.

**Why it matters.** It turns a measured curiosity from an experiment into a proof: here the centre's silence is permanent, not just observed for a while. It also shows how a carefully placed AND can cancel itself out over two steps instead of breaking the pattern.

**An everyday picture.** A correction that is applied and then exactly undone a moment later, because the lights it depends on always come on in alternating seats.

## G266
In a simplified version of Mahler's 3/2 problem, where carries may travel at most one place, how long the key digit can stay 0 is fixed exactly by how many times 2 divides the starting whole number.

**What it says.** Mahler asked whether one binary digit of xi times (3/2)^n can stay 0 for ever. Let carries in the addition travel at most one place, or not at all. Then, for a whole-number part g, the digit stays 0 for exactly as many steps as the number of times 2 divides g, plus one: 1, 2, 1, 3, 1, 2, 1, 4 and so on. The deeper fractional digits cannot help, because each step simply strips one factor of 2 off the whole-number part.

**Why it matters.** It explains exactly the ruler pattern the computer run found, and shows that the fractional digits only start to matter once carries can travel two places or more. That is where the simplified problem begins to look like the real one.

**An everyday picture.** A stack of coins halved each turn, losing exactly one layer a step: you know in advance exactly how many turns it lasts.

## G267
A column of Rule 30, read in its light-speed frame, can never show the nine-beat pattern five whites, two blacks, a white, a black.

**What it says.** A computer search had found that this short pattern never occurs. Here is the reason. Working backwards from the first black beat pins down where the nearest black cell must have started, and in both possible places a forced white beat lands exactly where the pattern needs a black one.

**Why it matters.** Two earlier arguments about a hypothetical repeating pattern relied on this pattern being forbidden. Now that rests on proof instead of a search.

**An everyday picture.** A ripple arriving at the shore at a fixed speed: once you know when its front arrived, you know exactly which later moments must be calm.

## G268
Another short pattern can never appear in a column of Rule 30 read in its light-speed frame: three whites, two blacks, a white, a black, a white, two blacks.

**What it says.** Assume the pattern appears and follow the black front that must have produced it. The pattern's first black pins down where the front started. Its middle beats pin down the next few cells. Its last two blacks pin down two more. Then, running the front two steps back in time, no earlier row could have produced those cells.

**Why it matters.** It was the last search-only fact used to rule out a family of hypothetical repeating patterns, and it is now proved twice: once by hand, and once by a computer certificate that a formally verified checker has confirmed.

**An everyday picture.** A footprint trail that, traced backwards, would need the walker to have stood in two places at once.

## G269
If the black-cell counts down the columns of a repeating stretch of Rule 30 follow a fixed repeating odd-even pattern, the stretch cannot have a lead-in: it repeats from its very first column.

**What it says.** Fix an odd time period. Each column then has exactly two possible left neighbours, one with an odd count of black cells and one with an even count. A prescribed odd-even pattern picks at most one of them. So every column has at most one possible predecessor, and a finite system in which every state has at most one predecessor and goes on for ever can only run in closed loops. A starting column of the kind that never has a predecessor therefore cannot begin such a stretch.

**Why it matters.** It removes one way the critical case could have hidden a lead-in, and it says what any real one would need: an odd-even pattern that does not repeat from the start.

**An everyday picture.** A one-way train line on which every station has only one incoming track: a train that runs for ever must be going round a loop, so it cannot have started at a terminus.

## G270
A hypothetical bridge in the critical case cannot end by settling into a shifted or time-delayed copy of the reference pattern it started from, at the period under study.

**What it says.** Suppose a pattern starts as the repeating reference on the left and ends as a shifted or time-delayed copy of the same reference on the right. Its middle can then be cut out and looped back into the reference, repeated just enough times to line the copies up exactly. That gives a pattern that differs from the reference in only a finite stretch, and a finite change of that kind was already shown to need a much longer period.

**Why it matters.** It closes one of the escape routes left open in the main critical case. The other backgrounds stay open.

**An everyday picture.** A detour that leaves a ring road and rejoins it further round can be driven again and again until the laps add up to whole circuits, which shows the detour is a real change to the road.

## G271
If a column of Rule 30 stays black for nine steps in a row, the two cells just to its right are pinned to white then black, whatever happens further right, for as long as the column stays black.

**What it says.** Nine black steps squeeze every possible right-hand neighbourhood into the same two-cell pattern, and that pattern then keeps itself going. So a wall that is black for at least nine steps between its white moments always has a white cell beside it at each white moment after the first.

**Why it matters.** It explains a computer finding that a side channel next to such walls carries no information, and it needs no assumption about the left side or about the starting row being finite.

**An everyday picture.** A door held shut long enough: whatever pushes from the far side, the latch has dropped and stays down.

## G272
In the critical case, once a hypothetical bridge leaves the reference pattern's family of shifted and delayed copies, it can never come back to it.

**What it says.** Treat all time-shifted copies of each column as one. The reference pattern is then a single point. Any route that left that point and came back could be rotated and repeated into a finite change of the reference, which an earlier result forbids.

**Why it matters.** It says exactly where any other repeating background would have to live: strictly downstream of the reference, never on a loop through it.

**An everyday picture.** A one-way exit from a roundabout: you can leave and drive somewhere else, but no road brings you back onto it.

## G234
A finite early clock does not prevent arbitrarily delayed resonance in a deeper white interval.

**What it says.** A fixed finite alternating centre prefix and a deeper odd white interval can be realized together in a finite seed. Independent far-left pivots make the interval midpoint stay white for any prescribed additional finite delay. Second reading pending.

**Why it matters.** An early clock prefix alone cannot exclude the resonant state; the later retained clock samples must interact with it. This is a composition of existing triangular and latch arguments, with no full RR clock witness.

**An everyday picture.** Two preparations occupy disjoint regions, so fixing one leaves the other free until the intervening dynamics brings them together.


**Finite-horizon extension.** If an odd white-block RR cone witness has a black nearer endpoint, its whole clock cone can be retained while outer pivots give any finite midpoint resonance delay. Those pivots first reach the clock strictly after its existing horizon; existence of the original witness is an explicit premise.


## G235

The critical-ray bit cannot become constant under a fair initial row, except on a null set.

**What it says.** Its right tail would have to reach the all-zero infinite state. Invariance of the fair measure makes that absorption event null. Both bit values therefore recur infinitely often almost surely.

**Why it matters.** This proves the single-bit baseline without critical-ray ergodicity. Simultaneous longer zero windows and damage escape remain open.

**An everyday picture.** A steady reading at the boundary would require every position farther along the tail to stop contributing, not only its nearest two neighbours.


## G236

The row after a history-bearing four-gap entry retains a restriction three sites beyond its familiar prefix.

**What it says.** From initial prefix 0001, a two-step output beginning 11100 cannot continue with 011. A sixteen-state spatial image map proves this in three subset transitions.

**Why it matters.** A canonical five-site prefix does not erase the incoming history. The missing visible 4,3,2 factor still needs its continuation linked to this spatial restriction.

**An everyday picture.** Two objects can share the same label at the front while their permitted contents farther inside remain different.


## G237

Six initial sites force a later black reading whose neighbour rules out a two-zero gap.

**What it says.** Starting with 000010 beside the alternating wall forces five successive local transitions. The final black site has a white neighbour, so its next gap contains one or three zeros.

**Why it matters.** This supplies the missing cancellation in the fourth branch of a finite forbidden-word certificate. The earlier classification of branches still uses a checked computation.

**An everyday picture.** Two marks labelled unknown can still refer to the same number; subtracting that number from itself gives zero.


## G238

The four-zero gap cannot lead into three zeros and then two when its start remembers a previous zero.

**What it says.** The canonical start has only two ways to make its next three-zero gap. One forces a white neighbour at the last black sample; the other contradicts its earlier row. Both prevent the requested two-zero gap.

**Why it matters.** This replaces the last finite classification in the forbidden-word certificate with a hand argument. It concerns one finite word beside the imposed wall.

**An everyday picture.** Following both exits from a junction shows that neither reaches the desired destination.


## G239

Perfectly balanced blocks can still carry choices.

**What it says.** Six equal-length gap blocks have the same number of ones and zero net charge, yet their arbitrary concatenations have positive entropy and bounded charge discrepancy.

**Why it matters.** Exact wheel balance and the listed forbidden words alone cannot establish zero boundary entropy. These abstract words have no proved Rule 30 realization.

**An everyday picture.** Six boxes can weigh the same while holding different messages.


## G240

The third edge-source depth is active at least half the time.

**What it says.** Its even and odd samples are complements of consecutive visible right symbols. The no-adjacent-ones gate gives a deterministic lower density of one half.

**Why it matters.** Cloud's aggregate excess already has a concrete near-wall contribution, but active sources can still cancel after propagation.

**An everyday picture.** Many lamps can be on even when their combined parity is zero.

**GC585 boundary extension of W240 (awaiting reading).** If the left half were finite with deepest black L, its moving edge forces an active source at depth L+t+2. The first exterior cells still stay white because their Gray and source contributions cancel exactly. Silent depth 6 excludes L up to 4; a general contradiction needs silent positions hitting every possible moving-edge ray, or another clock-dependent obstruction. No such covering family or finite clock witness is proved.

**GC586 extension of W240 (awaiting reading).** The compulsory moving-edge sources alone contribute the repeating parity pattern 110 to exterior time-zero red sets. A finite white tail would require the interior sources to match that same pattern. The first double hit cancels at depth L+4. This is a standard Pascal/Fibonacci identity under the finite-left hypothesis; no obstruction to the required interior compensation has been proved.

G240 extension GC589, awaiting reading: at white times E14=c1*c3*c6 in the no-11 quotient. Nonzero forces the reviewed forbidden visible factor 101001. This hand identity explains Local's SS measurement; no-11 alone fails on formal code 0101001. No general silent-depth family follows.

G240 extension GC590, awaiting reading: a silent triple (depth j, colour p, onset A) covers L<=j-A-2 of parity j-p. Complete ray interception is equivalent to unbounded thresholds in both parity classes. This sharpens L308; no infinite Rule 30 family is proved, and missing a ray does not realize it.

GC589 scoped Local receipt L310: product and missing-factor step read by hand; P13 confirmed earlier, P12 not separately derived; independent SS supports E14 silence.
G240 extension GC591, awaiting reading: every positive-L ray reaches depth j by age j-3. Later firing witnesses shift to every earlier matching-parity age. SO's six shallow targets and E30 white therefore cannot be rescued by a later onset for this route, conditional on Local's replayed witnesses; finite SAT cones extend by the existing inverse construction. No finite-tail witness or global source-family exclusion.

G240 extension GC592, awaiting reading: r+1 consecutive diagonal source events are equivalent to one black followed outward by 2r+1 zeros at the starting row. Infinite streak means a zero tail. This closes a separate one-ray streak census as a new mechanism; known realizable white-run bounds already bound it. No clock exclusion or experiment.

**G240 / GC597 extension (awaiting reading):** relaxed A/B-compatible twin rays three depths apart cancel the exterior Fibonacci parity signature. Actual simultaneous outer event at distance D limits the inner streak to floor(D/2) by GC592; hence persistent parallel compensation is impossible beside the mandatory frontier. Intermittent parity supply remains open.

**G240 / GC598 extension (awaiting reading):** interior source contributions of ages <=A have eventual dyadic target period Q>A. Comparing depths k and k+Q removes them and forces late-source parity in two of three target residues. A three-target check requires an event older than A; finite fragments cannot suffice. No event density or prize exclusion follows.

**G240 / GC599 extension (awaiting reading):** the actual moving outer strip 11001 alternates with 11011, producing endlessly restarting isolated events at frontier offsets three and four. It also occurs on singleton time two. Joint streak caps do not bound restart count; no imposed full clock or parity compensation is established.

**G240 / GC600 extension (awaiting reading):** for dyadic Q and k>=L+Q, the required target difference weights each interior source by binom(k-j,t-Q). Ages are Q plus binary subsets of k-j, reaching Q+k-j. Finite-frontier geometry removes negative-index entrants; no localization near Q or prize exclusion follows.


## G241

A finite Gray-rule clock leaves a boundary term in the source certificate.

**What it says.** At late dyadic times the Rule 30 Gray split demands source parity zero, and at the next time it demands the initial visible right bit.

**Why it matters.** The forced odd source parity from the Rule 210 comparison cannot be copied into this split. The cancellation question remains.

**An everyday picture.** A surviving baseline changes how much a correction must supply.

**GC567 G241 scope control (awaiting reading).** Two selected forward Gray sources cancel at target 4 in the actual singleton Rule 30 orbit; one contributes at target 2. Realizability alone does not forbid source-parity cancellation. This finite control is outside G241's full-clock hypothesis and is separate from inverse sideways sources. No balance or asymptotic claim.


## G242

Four zeros imply the fifth in the fixed inverse certificate.

**What it says.** At depths 14 through 17, the four zero equations force one visible code and also zero at depth 13. The code contains a forbidden right-hand factor.

**Why it matters.** A hand argument removes the redundant anchor found by the finite audit. Its scope is still this fixed depth window.

**An everyday picture.** Four conditions recover a fifth that had seemed independent.

**W242 review update (2026-10-08).** Local independently verified the hand argument in L295 (fbcce01a). The four specified zeros force the same nine-symbol code and recover the omitted first zero. This remains a fixed-window result, with its actual exclusion supplied by the forbidden right-word factor.

**W242 phase application (2026-10-08; scope reading pending).** Six zeros at initial depths 13 through 18 rule out a black-start clock through time 18: after one tick, four zeros remain at exactly the depths G242 excludes. This gives an upper bound of five on that phase-specific depth-13 record, without asserting its measured value.

**W242 phase review update (2026-10-08).** Local L296 independently verifies the six-zero phase application and its exact deadline; its previous pending label is superseded.


## G243

A new right-edge bit can be masked by correlated gates beside the wall.

**What it says.** Flipping the last initial right-cone bit changes the visible cell at time 2 with probability 1/4, and at time 4 with probability 1/8, for fair independent initial right bits. Four independent gates would instead predict 1/16.

**Why it matters.** A concrete boundary information channel is already unlike the fresh-gate model. No large-time channel strength or entropy conclusion follows.

**An everyday picture.** One door can already be open because of what opened the earlier doors.


**W243 all-time extension (GC558; reading pending).** After the initial sample, two successive visible samples cannot both depend on their respective last initial right-cone bits. A white odd-time companion forces the next odd-time companion black, closing the next path. This bounds the frequency of these particular activations by one half; other input channels remain possible.

**W243 reading update (2026-10-08).** Local L297 verifies the original time-2/time-4 statement and its controls. The GC558 all-time isolation extension remains pending; the original statement is second-read.


## G244

A positive average of active last inputs would prove positive boundary-language entropy.

**What it says.** The visible-prefix entropy is at least the expected count of active last initial cone bits. If their average activation probability stays positive, the actual wall language has positive entropy.

**Why it matters.** This is a concrete sufficient target that does not require independent activations or a stationary visible measure. Its large-time lower bound remains unproved; inactivity of these particular inputs does not imply zero entropy.

**An everyday picture.** Each exposed fresh switch that still reaches the observation contributes a bit of conditional uncertainty.

**W243/W244 review disposition (2026-10-08).** Local L298 verifies the isolation extension and L299 verifies the entropy inequality. Both are now second-read.

**W244 channel audit (GC560; reading pending).** The first half of every last-input path lies outside the wall cone and has independent fair gates, so activation probability is at most 2^(-n). Its mean density is zero and only finitely many such activations occur almost surely. This closes that particular positive-mean route, without bounding total visible entropy above.

**GC560 review disposition (Local L300, verified c51e30f via 4d7b4639).** Exponential masking and summable last-pivot activation are second-read. G244's chosen positive-mean route is closed under the fair-right ensemble; its entropy inequality remains correct, with no entropy upper inference.

**GC563 extension of W244 (awaiting reading).** Conditioning only on visible history gives next-black probability equal to the posterior of a hidden white pair when the current bit is zero. With beta_n the optimal history-only prediction error, 1+2 sum beta_n <= visible-prefix entropy <=1+(N-1)h2(mean beta). Positive average beta suffices for positive support entropy; no such lower bound is shown. A random-phase alternating comparator has persistent productive events but zero prediction error and entropy rate. Standard inequalities, no runtime or actual comparator realization claim.

**GC563 reading (Local L302, verified 2ca1aa0).** Visible posterior recursion and both prediction-error entropy bounds are second-read; average beta positivity remains open.

**GC564 G244 finite posterior control (awaiting reading).** At two-symbol histories 00 and 10, the next-black probabilities are exactly 5/12 and 3/16; 01 forces zero. Three-symbol masses are 7,5,4,13,3 over 32, matching GC502's collision 67/256, and beta_1=1/4. The initial white-pair to black-pair surgery cannot be transported after history 00 because evolved hidden pair 11 is impossible in that fibre. No long-time posterior estimate or new run.

**GC565 G244 gap-start target (awaiting reading).** At an observable first-zero gap start, restrict to actual hidden sites 2 and 4 black. GC503 makes the next two symbols 01 or 00 according to hidden site 3. Weighted posterior entropy gamma on this event lower-bounds two-symbol conditional entropy; overlapping blocks give H_N >= (1/2) sum gamma. Average gamma positivity remains unproved. Removing the hidden gate fails when sites 4 and 5 are both white. Initial four-symbol proposal sharpened to two; standard entropy algebra, no experiment or universal wheel-profile assumption.

**GC566 upstream local control (awaiting consolidated reading).** Actual even-row prefix 1110e evolves in two ticks to 0,1,1-e,1, independently of the exterior, and its next three visible outputs are 0,0,e. Refines reviewed GC504. The initial cylinders are real; later fifth-cell edits have no established lift preserving the complete observed-history fibre. No posterior or frequency bound. Stop local entropy-target rewrites; move to a distinct structural-balance audit.


## G245

On a ring of seven cells the Gray-code rule is a pure clock, and no straight relabelling turns Rule 30 into it.

**What it says.** On seven cells in a ring, Rule 60 (each cell becomes itself XOR its left neighbour) has one fixed state and nine cycles of length seven, and the other 64 states fall onto those cycles after one step. No affine change of coordinates of the whole ring carries Rule 30 onto a nonconstant copy of this clock: Rule 30's AND term cannot be relabelled away.

**Why it matters.** It closes the hope that Rule 30 on a small ring is the Gray clock in disguise. Any link between Rule 30's wheel phase and a clock has to be partial, not a full change of variables.

**An everyday picture.** A seven-hour clock whose hand always moves on. Rule 30 is that clock with a sticky gear, and renumbering the face does not unstick it.

**Seven-ring Gray-clock scope and affine-factor obstruction (GPT GC561, waiting room).**

Rule 60 T=I+S on seven cells has rank-six even-parity image, one fixed point and nine seven-cycles; the other 64 full-ring states enter that image in one step. No nonconstant affine full-state map can intertwine seven-ring Rule 30 with any linear update: every distinct quadratic monomial has its corresponding map coefficient as coefficient, forcing all linear map coefficients zero. Standard linear algebra and Boolean polynomial uniqueness. Does not exclude nonlinear factors, restricted domains or explain the wall wheel. Cloud CL051 algebra scope audit; no experiment.

**G245 reading receipt (GPT, Cloud CL052 at c5c1e1d).** Cloud independently verifies the rank-six Gray image, nine seven-cycles, one-step transients and full-state affine-factor coefficient argument. G245 is second-read with its original closed-ring scope. Kick/phase measurements accompanying the reading are separate post-hoc evidence, not an affine-factor construction.


## G246

The second-last input that could still change the wall's visible bit almost surely stops mattering.

**What it says.** With fair random right inputs beside the alternating wall, the chance that the visible bit at time 2n depends on the initial cell at site 2n is at most 4n/2^n. These chances have a finite sum, so with probability one only finitely many such inputs ever matter.

**Why it matters.** With the matching result for the last input (W244's channel audit), it closes the route that looked for the wall's information in its newest inputs alone. Any information must come from deeper ones.

**An everyday picture.** A whisper passed along a long queue: the last two people to join are almost never the ones whose words reach the front.

**Second-last right-cone sensitivity is summable (GPT GC562, waiting room).** Under fair right inputs at the alternating wall, sensitivity of the time-2n visible bit to initial site 2n has probability at most 4n*2^(-n). Exact two-copy damage paths have one stay and otherwise move left; each path pays for at least n-1 independent baseline white gates outside the wall cone. Summing over at most 2n paths gives the bound and almost-sure finite activity. Extends GC560 to the two-bit outer frontier, without an entropy upper bound or earlier-input conclusion. Standard damage algebra and G97 fresh-pivot sampling; no experiment.

**G246 reading receipt (Local L301, verified 764ed53 via 8743fe979).** One-stay recurrence, fresh cones and summable second-last sensitivity bound independently hand-read as correct.


## G247

Two longest possible waits for rows with more than one black cell force the following wait to be short.

**What it says.** In a repeating row of q cells containing at least two black cells, the longest reset delay is q-1. If two compatible successive rows both attain it along the same uninterrupted clock, the next row is black at its arrival, so its delay is one.

**Why it matters.** Compatibility restricts consecutive extreme waits. But the three delays still add to 2q-1, so this fact alone gives no average-speed bound independent of the period.

**An everyday picture.** Three traffic lights on a route: the timing of two long stops can require the third light to be green when you reach it. That green light does not refund all the time already spent waiting.

**G247 reading receipt (Local L305, verified 36f7bc519c20).** Both supports, forced third bit and endpoint arithmetic independently checked; second-read in its original full-line scope.

G247 extension GC594, awaiting reading: consecutive delays a,b with a+b>q and b<q force the next compatible driver black at inherited arrival. The first driver may be singleton. Three ordinary nonsingleton waits total at most 2q-1. Strict crossing, the second delay guard and uninterrupted births matter; the bound is period-dependent and gives no rooted frequency or global Q7 conclusion.

G247 extension GC595, awaiting reading: ordinary blocks have no internal conservative birth clamps; GC594 applies after their entrance phase changes. Whole-prefix cost sums their triple envelopes plus singleton waits and one global zero-driver clamp charge. At common period four, slope-5/2 debt is <=1+(5/2) times singleton count. No bound on that count or generalization to larger periods is proved.

**G247 / GC596 extension (awaiting reading):** conservative common-q prefixes satisfy T-gamma M<=2(q-1-gamma)+(3q-2-3gamma)P for (2q-1)/3<=gamma<=q-1. Zero separators cancel at the same threshold as triples. This envelope yields sub-three only for dyadic q=2,4; it is no dynamical lower bound.


## G248

The gap crossing a single wheel splice determines whether its two kick readings disagree by half a turn.

**What it says.** If the old and new visible words are pure wheel phases meeting at one cut, an even number of zeros between their adjoining black cells makes the phase and charge readings agree modulo 28. An odd number makes them differ by 14.

**Why it matters.** Crossing gaps of two or four zeros eliminate this discrepancy within the single-splice domain. A general transient can alter several gaps, and an empirical instant event still needs to be shown to fit the domain. No integer direction or prize theorem follows.

**An everyday picture.** Two rulers can agree on a circular scale while their full readings differ by a complete turn. Here an odd gap additionally moves one reading halfway around the circle.

**GC582 extension of W248 (awaiting reading).** The same parity test applies to RB's adjacent finite locks, including an odd physical cut. For a general pair of locks, count complete zero gaps between black samples inside the locks: phase and charge differ by 14 exactly when an odd number of these gaps have odd length. Two odd gaps cancel. Endpoint choices within a pure lock do not change this parity; no integer direction, actual gap restriction or replay follows.

## G249

The diagonals along the single cell's right edge, and those of any finite seed, cannot double their combined period three times in a row.

**What it says.** Read the pattern in lines parallel to its right edge. Each line repeats, with a period that is a power of 2, and the combined period of the first j lines can double from one line to the next. GPT proves it can never double at three consecutive lines once it has passed 1, because the third doubling would need an odd count where the count is always even. So the combined period of the first j lines is at most 2 to the power ceil((2j - 1)/3). Second-read by Local, with literal checks on the single cell and 30 random seeds.

**Why it matters.** It gives every finite seed a guaranteed band of ordered diagonals at its right edge that grows with time, at least about 1.5 lines for each doubling of the elapsed time. That is a universal lower bound, well under the single cell's measured rate of about 2.5, and it says nothing about the centre column.

**An everyday picture.** A counter whose digits can each slow down by half, but never three digits in a row, cannot fall behind faster than two halvings in every three steps.

## G250

The exact cost of a block of long gaps tightens the budget on how often an alternating clock's gap word can change letter.

**What it says.** With a finite left side, a block of n identical gaps beginning at time a must fit under the left edge's distance at that time, J(a) = J_0 + a, plus 3 for short gaps or 6 for long ones. The 6 is Local's exact long-gap cost, which replaces the earlier allowance of 20. Chaining the blocks shows that a gap word with r changes of letter by time T needs T to be at most about (J_0 + 5) times 2^(r+1). Second-read by Local.

**Why it matters.** A clock that keeps going must change letter at least logarithmically often: by time T it needs about log2(T/(J_0 + 5)) changes. That is a sharper version of an existing budget, and a lower bound only, not an exclusion: a formal word with ever longer runs of short gaps still passes it. (Corrected 2026-10-09 at GPT's GC767: the first wording reversed the inequality.)

**An everyday picture.** If each straight stretch of a walk can be at most as long as the distance already covered plus a few steps, a long walk must turn at least about as many times as the logarithm of its length.

## G251

A permanently white diagonal near the left edge also limits how long a block of long gaps can last.

**What it says.** Along a long-gap block the left side must copy the 155-cell all-L ring, so a diagonal running parallel to the left edge reads the ring every 33 cells. That reading never has more than 7 whites in a row, so a diagonal already settled to white cannot share more than 7 of its samples with the copied ring. This caps the block's duration at the left edge's distance minus the diagonal's depth, plus a term for when the diagonal settled. Second-read by Local, with the ring arithmetic checked literally.

**Why it matters.** It is the long-gap twin of the earlier short-gap bound, so both letters now carry onset-sensitive limits. It is still not a uniform deadline and does not settle the period-two question.

**An everyday picture.** A wall of bricks with at most seven white bricks in a row cannot hide a white stripe longer than that, wherever the stripe crosses it.

## G252

A hypothetical all-L row that turns back on itself every 310 steps but ends on the right in a pattern repeating every 155 would need a particular odd correlation somewhere between the two.

**What it says.** Far left such a row copies the 155-cell ring, whose columns hold an even number of black cells over 310 steps. Far right its columns repeat every 155 steps, and the last column that does not must hold exactly 155 blacks, an odd number. An exact parity rule links neighbouring columns, so somewhere between the two ends a pair of neighbouring columns must overlap in an odd number of black cells. Second-read by Local.

**Why it matters.** It pins down what an exclusion of this case would have to forbid. It does not forbid it, and the same counting says nothing at period 620 or beyond.

**An everyday picture.** If a row of switches starts with an even count and ends with an odd one, some neighbouring pair along the way must be where the parity changed.

## G253

When two time-periodic histories of the shifted rule first differ in some column, the difference must come as a swapped pair and vanish at the next tick.

**What it says.** Take two histories whose columns agree everywhere to the left of column k and differ at column k at some time. Then the column just to the left is black at that moment and white at the next, so the difference in column k cannot last two ticks running. The difference also comes with an opposite difference in the next column to the right: a black-white pair swapped for white-black. Second-read by Local, with an exhaustive check of the local cases.

**Why it matters.** It rules out the simplest way of building a different history beside the all-L ring, a single flipped cell, and says what any real departure must look like. It does not by itself forbid one, or settle the uniqueness question.

**An everyday picture.** Two identical queues that first differ at one place must do so by two neighbours swapping, and the first of the pair is back in line by the next step.

## G254

Starting from a random row, the colours along Rule 30's rightward diagonal cannot be produced by any rule that only remembers the last two of them.

**What it says.** Start from fair coin tosses and read the cells along the line that moves right one cell per step. Its first three correlations are exactly -1/2, 1/4 and -1/4. A process that remembers only its last two values, and is symmetric under swapping black and white as this one is, would be forced by the first two of those numbers to have -1/8 as the third. So it is not that kind of process. Second-read by Local, with the three correlations recomputed independently.

**Why it matters.** It closes one simple way of describing the diagonal's memory. It says nothing about longer memories or about the single cell's own diagonal.

**An everyday picture.** A forecaster who looks only at the last two days cannot match a climate whose three-day pattern breaks the rule those two days imply.

## G255

Over a random row, how much a fixed window's black count now predicts the same window's count k steps later is exact, and drops to zero once k reaches the window's width.

**What it says.** Each cell is correlated with exactly one cell k steps later, the one k places to its right along the light-speed diagonal, and with no other. So two windows' black counts are correlated only through the pairs of cells that line up that way. For one window of width w watched over time this gives the diagonal's correlation times max(w - k, 0)/w, which is exactly zero from k = w on, while a window that moves right with the diagonal keeps the full correlation. Second-read by Local, with exact checks for a width-3 window.

**Why it matters.** A fixed window's correlation vanishing at large lags is geometry, not evidence that Rule 30 forgets: the memory has moved out of the window along the diagonal.

**An everyday picture.** Watching a fixed stretch of a conveyor belt, you lose sight of each parcel once it has moved past the end, even though the parcel itself is unchanged.

## G256

If the centre ever ticks white, black, white, black for good, the column just to its left must eventually be at least three-quarters black.

**What it says.** Beside an alternating centre, the two columns to its left are fixed by the column to its right through exact rules. Counting black cells over any stretch of rows gives an exact identity, up to one boundary term, which forces one of the two columns to be at least two-thirds black. The column to the right is known never to have two blacks in a row at the centre's white times, and with that the first column on the left must be at least three-quarters black over long stretches. Second-read by Local.

**Why it matters.** It turns the period-two question into a statement about balance: a column beside the centre measured below three-quarters black over long stretches would rule the clock out. No such balance is proved, so it does not settle the question.

**An everyday picture.** If a metronome ticks perfectly, the person beside it has to clap on most beats to keep the rhythm going.

## G257

Over a random row, a pair of neighbouring cells two steps later is completely independent of the pair now, yet the next two steps together are not.

**What it says.** Watch cells 0 and 1. Their colours two steps later are independent of their colours now: two fresh random cells further left decide them. But a three-way average across the starting cell, cell 0 two steps on, and cell 1 three steps on comes out at exactly 1/8, not 0. So the starting pair and the following two-step block are dependent. Second-read by Local, with GPT's exact replay over all 256 starting words repeated.

**Why it matters.** Independence of one later row does not mean independence of the whole future. Statements about the rule forgetting its start have to be made carefully about which observations are compared.

**An everyday picture.** Two snapshots of a shuffled deck can each look unrelated to the start, while a pair of consecutive snapshots still gives the original order away.



## G258

Along Rule 30's diagonal moving right one cell each tick, four short colour patterns never occur.

**What it says.** Reading white as0 and black as1, the patterns are00100,11011,000111 and111000. Neighbouring diagonal traces would be forced to give one bit two different values, so each pattern is impossible for any starting row. Local and GPT independently read each other's two proofs. A singleton run cannot sit between two runs each at least two ticks long, and two neighbouring runs cannot both be at least three ticks long.

**Why it matters.** These are uniform local restrictions that eliminate some options before a cyclic-profile search. They do not bound one run's length, determine the required parity, or solve the alternating-centre problem; a fixed centre follows a different line.

**An everyday picture.** A short rhythm may look possible on its own, but the neighbours needed to produce it would have to play two incompatible notes at once.


## G273

Every admissible fixed-period walk starting beside a zero column returns to zero, and all its nontrivial excursions end at different nonzero words.

**What it says.** Unique backward reconstruction prevents a live walk from repeating after a zero start. Counting all starts then gives a bijection onto the nonzero endpoints. The compressed return graph has a root tree and separate cycle components. Cloud second-read the return and endpoint arguments, and the component/period counts; its review did not independently reconstruct the physical-root identification or the cited nonroot example. The combined filing remains in the waiting room.

**Why it matters.** Existence and endpoint completeness are structural. Individual depths, restricted-source growth and physical-root ancestry still require more information.

## G274

The complete-domain mean chain length has a counting bound, and an explicitly defined random comparison has an exact conditional length law.

**What it says.** With N=2^q there are N(N-1) live states and N-1 chains, so mean live length is at most N. Original return depth adds one. In the uniform partial-bijection comparison, fixing total chain mass makes the lengths minus their two endpoints a uniform weak composition. Cloud second-read the counting text; formal filing remains separate.

**Why it matters.** A matching conditioned mean cannot establish randomness or restricted-source growth. This supplies a precise benchmark, not a Rule30 distribution theorem.

## G275

Separate primitive temporal periods and rotation copies before comparing chain lengths.

**What it says.** Live pair period stays constant. For dyadic q, subtracting the q/2-period domain gives a primitive-source mean live length at most 2^q+2^(q/2)-1. Each primitive quotient chain represents q equal-length literal chains. A uniform rotation-equivariant comparison induces the conditional composition law on this quotient. Second reading is pending.

**Why it matters.** Period mixing and automatic copies can distort a comparison. Removing them still gives no lower bound on the rooted sample.

## G276

A fixed small source subset has substantial mean-length spread under the specified quotient comparison.

**What it says.** Uniform weak compositions give an exact subset-sum distribution and variance. With the reported q8 mass, the two odd-doubled source orbits have a mean less than one eighth of a comparison standard deviation from its expectation. A fifteen-composition hand control checks the formula; second reading is pending.

**Why it matters.** That mean is a weak discriminator of this abstract benchmark. No random draw, trajectory replay, source-arithmetic invariant or growth theorem is supplied.


## G277

Disjoint rotation copies give every primitive dyadic first excursion an explicit return cap.

**What it says.** The rotation quotient has m live vertices and a source chains. Reserving two endpoints for every other chain leaves at most m-2(a-1) vertices for one chain. Its original return depth is at most (2^q-2^(q/2))*(2^q+2^(q/2)-3)/q+3. Cloud CL119 second-read this accounting; the period and quotient mechanisms are credited to W275.

**Why it matters.** This improves the universal cap by a factor roughly q but remains exponential. No lower growth or prize statement follows; a stronger counting bound needs compulsory additional excluded mass.


**W277 continuation (GC892).** G203's already second-read short-return exclusion gives live minimum5 for primitive dyadic q>=4, strengthening the cap to m-5a+6. Cloud CL119 accepted this accounting corollary given G203; it remains exponential and does not review the quotient random ensemble. Further fixed-baseline optimization is closed as a growth route; no promotion.


## G278

Exact start and finish edges do not constrain matching in a partial-bijection comparison.

**What it says.** For primitive dyadic periods at least four, the forced three-pair prefix and two-pair suffix occupy five disjoint state families. Join them by any rotation-equivariant source-to-endpoint permutation and complete unused states with self-loops. This retains the boundary edges, period and equivariance while allowing any matching. Cloud CL120 second-read the construction and controls; formal promotion remains separate.

**Why it matters.** The middle bridge explicitly omits the interior successor-coordinate and Boolean recurrence constraints; the q4 control violates them. Boundary-only reasoning is closed, not the actual Rule30 source-matching problem or Q7.


## G279

Restoring the successor coordinate still leaves many interior comparison maps.

**What it says.** Coordinate-preserving live partial bijections are permutations in each fixed-driver row. For primitive dyadic periods at least four, the exact start/end edges reserve two row slots. Arbitrary remaining completions transported over driver rotations preserve pair periods and all those boundary facts. A q4 swap changes the first interior continuation and explicitly violates the omitted Boolean equation. Cloud CL121 second-read the family and controls; formal promotion remains separate.

**Why it matters.** The actual Boolean recurrence is essential to recover the unique Rule30 continuation. This does not claim arbitrary endpoint matching in the stronger model or a new growth bound; the next target needs a consequence of that equation, not another restatement.


## G280

Changing one driver bit flips either nothing or exactly the interval to the next common reset.

**What it says.** With a remaining common black driver bit, cyclic children are unique. Their difference vanishes at the changed tick, becomes the complement of the original child bit just after it, and propagates to the next black reset. Direct q4 controls check both outcomes; a family attains Hamming response q-1. Cloud CL122 and Local L510 independently second-read it by hand; formal promotion remains separate.

**Why it matters.** This is a consequence of the actual Boolean recurrence, not the relaxed permutation model. It rejects uniform local sensitivity of the cyclic inverse but supplies no rooted occurrence frequency or return-growth bound. Removing the last reset is explicitly excluded.


## G281

Several changed driver bits produce XORs of final-driver reset intervals, so their effects can cancel.

**What it says.** The exact difference equation is a linear reset equation forced by delta times the complement of the original child. For fixed nonzero drivers and uniformly all parent words, response rank is the number of changed ticks, collision probability is2^-k, and expected response weight is half the union of intervals. A q4 example reduces two lengths totaling five to one changed bit. Second reading pending.

**Why it matters.** Response lengths are not additive charges. Excluding the two terminal parents changes the collision rate, and neither averaging measure represents a rooted history without a new premise. No return-growth bound is supplied.


**W281 continuation (GC899).** At fixed parent x, child z is compatible iff z*(1+x+S z)=0. Its nonzero-driver fibre has2^weight(z)-indicator[x=Delta z] members: driver bits on child-black sites are free. Direct q4 controls and constant-child/terminal/q1 guards agree. Primitive alternating fibres are realized across distinct rooted prefixes, with2^(q/2)-2^(q/4) drivers for dyadic q>=4. Cross-driver collisions do not violate pair-map injectivity and give no within-history frequency or growth law. Second reading pending.


**W281 second-reading receipt (2026-10-10 00:16 BST).** Local L511 atb9f47663 independently checks GC897's forcing law, Green intervals, rank/collision/union mean, cancellation and measure guard, and GC899's fibre formula, endpoints and primitive rooted-prefix count. PASS by hand with scope retained: no rooted frequency or return bound. Formal promotion remains separate.


**W281 continuation (GC901).** Alternating child under parent1 is followed by complemented doubled driver bits, recovering primitive q, possibly with weight2. The prefix examples are zero-started fixed-q excursions; ancestry from the smaller-period physical root is not asserted. No full-state coalescence, recurrence frequency or stage-growth bound follows. Second reading pending.


**GC901 second-reading receipt (2026-10-10 00:26 BST).** Local L512 at77967ffa verifies the reset/copy formula, primitive-period transfer, q4/q8 sparse controls and full-alternating terminal guard by hand. PASS with zero-started-root scope and no physical ancestry, rooted frequency or return bound. This continuation is reviewed; formal promotion remains separate.


**W281 scope correction (GC903).** The q4 zero-starts0/1110 and0/1011 are on the same28-step B cycle; a seven-step-to-rotation certificate proves nonabsorption. GC899's rooted-prefix wording means arbitrary zero-started excursions only: these controls are NOT in the physical(0,1) root tree. Fibre/period-recovery formulas and their reviews remain valid; no larger-q ancestry conclusion. Second reading pending.


**W281 continuation (GC904).** Antiperiodic driver and nonzero half-periodic parent force primitive dyadic child. At a genuine doubling prefix0,c,1,e,f, f is primitive and G201 implies q/4<=weight(f)<=q/2. Parent0 and q2 guards retained. One-profile corollary only, no cumulative charge or stage bound; second reading pending.

## G282

Beside an externally imposed alternating clock, the finite right seed
1001 keeps its first column on 1100 forever. Its first fourteen cells
settle into an eight-step pattern. At the one phase where the band
needs information from farther right, the previous sixteen boundary
bits invoke the existing period-8 lock to supply exactly the bit needed.
A finite warmup and strong induction prove eternal persistence; arbitrary
initial tails beyond site 46 are allowed too. Independently confirmed by Cloud and Local (CL189, L595).

**Why it matters.** This settles KIMI Question 2
and gives a concrete use of retained temporal information. It does not
construct a finite left half or settle the period-2 prize.


## W283

Once the prepared train slab encounters a black cell at its critical
boundary phase, its next twelve white-time readings are fixed. A small
seven-cell transition table forces the exit gaps4 then5, even with arbitrary
inputs farther right. This explains the universal exit packet; it does not
erase entry information from later futures. Independent review is pending.

GC1027's corollary places the decision exactly: a long train forces the
slab to its penultimate car; that car's exterior gate decides the first
following symbol. The last-car slab need not persist. This repairs the
proposed train-memory interface and removes its first-symbol suffix census.

GC1028 reduces the fixed q T^12 exit obstruction to39 nine-bit interior
targets after conditioning on the actual prefix and prepared slab. It
isolates the earlier-history exclusion still needing a structural proof.
