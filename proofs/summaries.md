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
(2026-10-07). Plain-words pass done through G198 (2026-10-07); entries after it may still be drafts.*

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
then no white run inside that band is longer than 2P.

**Why it matters.** The settled band does have white gaps, but only short ones, and the next theorem (13) uses that
limit against repeats.

**An everyday picture.** A well-kept fence still has gaps, left on purpose: hedgehog holes, about 13 centimetres
square, cut so that small animals can pass through and are not trapped (the owner's reading). The settled band is
that fence. Its white gaps are never wider than 2P, so only something small can get through; page 13 shows that a
long repeat, which needs a white stripe roughly as long as itself (page 10), is too big.

## 13
The white stripe a repeat leaves cannot sit inside the settled band.

**What it says.** Combining 10 and 12: if the band near the edge is settled, a repeat's white stripe would have to
lie in it, and it cannot be longer than 2P there, so the repeat is bounded.

**Why it matters.** A sharper cap on repeats, from the edge band's own regularity.

**An everyday picture.** Driving round a busy car park: spaces keep opening as cars leave, but each is small and
gone within moments, and you pass the car about to leave just before it goes, so a driver who needs a long space
where they are can circle for ever while spaces are made all around them (the owner's reading). The settled band is
that car park. White gaps are born in it all the time, but none is wider than 2P or older than P steps (12), so the
long white stripe a repeat needs is never there at the moment and place it is needed.

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

## C2
While the middle column stays white, column 1 can switch on but never off.

**What it says.** When the middle square is white, column 1's next value is "column 1 or column 2". So across a
white stretch of the wall, once column 1 turns black it stays black until the stretch ends.

**Why it matters.** It turns column 1 into a one-way switch during white stretches, which sharply limits what the
right side can say there. Walls with long white and long black stretches ("slow walls") are studied with this tool.

**An everyday picture.** A set-reset latch (the owner's picture): column 2 can press "set", and pressing it again
changes nothing; only a black beat of the wall, a button the right side cannot reach, resets it. Proof 03 is the
same latch with its reset written in.

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

## C4
How fast news travels leftwards in Rule 30 is an exact bookkeeping identity: full speed, minus the times it gets
squashed.

**What it says.** Compare two copies of Rule 30 that differ somewhere and watch the leftmost difference. Read along
the diagonals, the difference never moves backwards, and it is held back only when the square just below it on the
diagonal is black. So its average speed equals full speed minus (how often it is held back) times (how far it is set
back each time). The measured numbers, 0.41 and 1.84, give a speed of about a quarter. A diagonal that turns white
for good becomes a barrier: damage that crosses it never heals.

**Why it matters.** It turns a measured speed into an exact identity, and explains why the band of white diagonals
left of the middle acts as a one-way wall for information.

**An everyday picture.** A rumour running down a queue: it moves one person per tick, except when it meets a
sceptic, who knocks it back a few places.

## C5
In a random row, Rule 30 keeps the row random, so white triangles of each width appear at an exact, predictable rate.

**What it says.** Start from a row of fair coin flips. Rule 30 keeps it a row of fair coin flips: it never
"unshuffles". So the number of white triangles with a top of width L, per square, is exactly 3 / 2^(L+4): each extra
square of width halves the rate.

**Why it matters.** It is a statement of the kind the prize's second problem asks for (how often things happen),
proved for random rows. The single-cell pattern matches it to about 0.05% in its central region, a measured sign
that the famous pattern behaves randomly there.

**An everyday picture.** A well-shuffled deck: the chance of a run of L reds is a clean power of a half, and Rule 30
is a shuffle that never undoes itself.

## C6
On a ring with a prime number of squares, any rhythm that is rare must be a pattern travelling round the ring.

**What it says.** Wrap Rule 30 round a ring of p squares, p prime. Turning the ring by one square commutes with the
rule, so it takes each repeating cycle to a cycle of the same length. Because p is prime, a cycle either comes in a
family of p copies or is turned into itself. So a cycle whose length occurs fewer than p times is a glider: turning
the ring does the same as running time on. The census found every cycle length distinct at p = 13, 17, 19, 23 and
29, so there every cycle is a glider. GPT's G55 later made this an exact criterion.

**Why it matters.** It is an exact, structural fact about Rule 30 in small closed worlds, of the kind the record
wants to tell apart from mere measurement.

**An everyday picture.** A carousel: if a horse's ride is not repeated by any other horse, the ride must simply be
the carousel going round.

## C7
The first three columns left of the middle just copy or flip column 1; the first real mixing happens in the fourth.

**What it says.** Next to the blinking wall, column −1 is column 1 flipped, column −2 is column 1 held for two
ticks, and column −3 is column 1 flipped one tick later. The first time two of column 1's bits are combined ("and")
is column −4.

**Why it matters.** It locates exactly where Rule 30's non-linearity first bites near the wall, and the counting
results begin here. It also marks a difference from the Collatz twin: there, knowing the pattern of odd and even
steps makes the whole orbit simple arithmetic (Terras's formula); here, knowing column 1 does so for only three
columns.

**An everyday picture.** A game of telephone in which the first three players pass the message on faithfully (some
of them saying the opposite), and the fourth starts mixing two messages together.

## E1
GPT found exactly which stretches of a row erase all memory when you rebuild the row before it.

**What it says.** You can rebuild an earlier row from a later one, square by square, keeping two squares of memory
as you go (four possible states). Some stretches of the later row send all four states to the same one, whatever you
started with: they "reset" the rebuild. GPT proved that a stretch resets exactly when it contains white, then a run
of black squares of length 1, 4, 7, 10, ..., then white, then any square. The shortest are 0100 and 0101. GPT's
first guess was wrong, and the failure is kept on record.

**Why it matters.** A reset means two different pasts become identical from that point on: information from further
away is wiped. This is an exact measure of when the right side's influence is forgotten.

**An everyday picture.** Directions that get you to the town square from anywhere in town, even if you do not know
where you started.

## E2
A single changed bit from the right side is forgotten at a steady rate as you go back in time: three squares per step.

**What it says.** Take a wall with one white beat (a "hole") followed by a long run of black. Change column 1 only
at that hole. Going back r rows, the two versions of the left half agree everywhere from depth 4r + 4 on, and the
first part of that agreement is a shared checkerboard. Each step back costs the protected checkerboard three
squares.

**Why it matters.** It measures exactly how quickly one bit of news from the right fades in the left half, a precise
piece of the "how much can get through" accounting.

**An everyday picture.** A footprint on a beach: each wave narrows it by the same amount, until it is gone.

## E3
For walls with one white beat per period, checking three columns on the right rules out no more than checking two.

**What it says.** Instead of asking for a whole right half obeying Rule 30, ask only that the first k columns obey
it, with the next column free (a "relaxation of width k"). Which patterns of column 1 at the white beats are then
possible? For walls with one white beat per period p, widths two and three give the same answer: for even p, never
two black in a row; for p = 3, never black, white, white; for odd p of 5 or more, anything.

**Why it matters.** It tests whether the right side's own rules squeeze the channel. Here the third column adds
nothing visible, even though it changes what happens out of sight.

**An everyday picture.** Checking an alibi with more witnesses: the third witness tells you nothing the second did
not.

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

**An everyday picture.** A lock that gives way to none of the first four picks: if it can be opened, it needs a
fifth.

## E7
Jen's classic argument works from the left half alone, without assuming anything about the right.

**What it says.** Jen's theorem says two neighbouring columns that both repeat force infinitely many black squares.
GPT showed the same argument works in the setting the record studies: a forced left half that starts out eventually
white, with no assumption that a right half exists. It holds for Rule 30 with any repeating, non-constant wall, and
for its sibling Rule 210 with the blinking wall.

**Why it matters.** It removes a hidden assumption, so the tool can be used exactly where the record needs it.

**An everyday picture.** Proving there is a leak from inside the house, without having to inspect the pipes outside.

## F1
After k Collatz steps, a number's remainder in base 2 has become a remainder in base 3, and the rest passes through
untouched.

**What it says.** Write a starting number as 2^k times m plus a remainder r. After k steps, with a odd steps among
them, it becomes 3^a times m plus the value r itself reaches, which is below 3^a. This is Terras's identity (1976),
restated.

**Why it matters.** It is the Collatz twin of the forced left half, and the avenue Collatz has that Rule 30 lacks:
after the free bits, the state is an explicit number. All the counting work of GPT's G39 to G75 builds on it.

**An everyday picture.** A bureau de change that converts your loose coins into another currency and hands your
banknotes back untouched.

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

**An everyday picture.** A circular hike that ends higher than it starts: begin at its lowest point, and you are
never below where you set off.

## G40
Swapping neighbouring odd and even steps shifts a Collatz number's final value by an exact, predictable amount.

**What it says.** Group a step pattern into pairs: two evens, two odds, or a mixed pair. Turning a mixed pair round
(odd-even into even-odd) changes the final value, counted in base 3, by an amount that depends only on where the
pair sits. So the spread of final values over all the swaps is built from independent pieces, and its frequency
fingerprint is a product of simple factors.

**Why it matters.** The Collatz count needs final values to spread out evenly. This gives an exact handle on that
spreading, the Collatz analogue of a random walk built from independent steps.

**An everyday picture.** A row of switches, each adding its own fixed amount to a meter: the spread of possible
readings is the switches' spreads combined.

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

**An everyday picture.** A choir of many independent voices can still all hit one note together if each happens to
be tuned to it; adding voices does not wash that note out.

## G43
An exact translation table between base 3, where the Collatz state lives, and odd or even, which decides the next step.

**What it says.** Suppose you know a number's remainder after dividing by a power of 3, and you want to know whether
the number is odd. GPT wrote down exactly how much each frequency of the remainder's distribution contributes to
that question, with an explicit formula.

**Why it matters.** F1 puts the Collatz state in base 3, but the next step is decided by base 2. This is the exact
bridge between them, and it says which frequencies matter most.

**An everyday picture.** A phrasebook that tells you exactly how much each word of one language counts towards a yes
or no in another.

## G44
A remainder modulo 3^a can imitate only so many fair coin tosses; ask for more and the repetition shows.

**What it says.** If the remainder is uniformly random, the next d odd-or-even steps look like fair coin tosses,
with an exact error formula, as long as 2^d is much smaller than 3^a. Beyond that the steps are fixed by the
remainder and carry no new randomness. GPT also showed one tempting comparison with coin tosses fails for long
patterns.

**Why it matters.** It is an exact information budget: the Collatz state after the free bits can pay for about 1.58
a fair coin tosses and no more.

**An everyday picture.** A deck of cards can fake only so many coin tosses; deal enough and the deck repeats.

## G45
For a given step pattern, the numbers that follow it and stay above their start are a fixed class with a height limit.

**What it says.** All numbers that follow a given pattern of odd and even steps share one remainder modulo a power
of 2. If the pattern's growth factor dips below 1, such a number can still stay at or above its start, but only if
it is small: below a ceiling the pattern fixes exactly.

**Why it matters.** It separates two notions the count uses: "the growth factor stays above 1" and "the number
actually stays above its start". They differ only for small numbers, below the ceilings.

**An everyday picture.** A fairground ride with a maximum height: only those under the bar get on.

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

**An everyday picture.** A walk that must end at or above home but heads downhill at the end: the only way is to
arrive back at your own front door.

## G48
A simple formula for how far above or below its start a number ends after its first dip.

**What it says.** For any pattern whose growth factor first drops below 1 at its last step, the gap between end and
start is a fixed number minus a fixed multiple of how far the start sits up its class. A gap of zero is a return to
the start; a positive gap means it ended higher.

**Why it matters.** It turns survival through a first dip into a short, exact calculation, which G48's certificate
(next page) then carries out.

**An everyday picture.** A lift that drops a fixed number of floors per extra passenger: whether you end above your
floor is simple arithmetic.

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

**An everyday picture.** The same engine fitted to a different car: it runs, but the race is a different one.

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

**An everyday picture.** A shooting target with two rings: one for the whole number and one for the fraction, both
drawn exactly.

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

**An everyday picture.** Counting a parcel service's deliveries by the van-load rather than by the parcel.

## G54
A simple two-by-two calculation bounds the information reaching the left half, for every repeating wall.

**What it says.** List the gaps between the wall's white beats. Each gap gives one of three small 2-by-2 tables;
multiply them together. The size of the product (its largest eigenvalue) gives a ceiling on how fast information can
reach any column on the left.

**Why it matters.** It is a quick, explicit bound for every rhythm at once. It is coarse, so it does not close the
gap on its own.

**An everyday picture.** A pipe made of sections of known width: the narrowest combination limits the flow.

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

**An everyday picture.** Tracking a crowd's centre to see whether it is drifting round a roundabout.

## G57
How a Rule 30 pattern drifts round a prime ring is set exactly by where its "and" operations happen.

**What it says.** Rule 30 is a simple sum of neighbours plus a correction wherever two neighbouring squares are both
black. GPT showed that the drift of G56's phase is an exact formula in that correction: where the correction sits,
weighted by position.

**Why it matters.** It ties the drift to Rule 30's non-linear part, the part that makes it hard. It does not yet say
the drift is never zero.

**An everyday picture.** A ship's drift is set entirely by where its rudder pushes: no push, no turn.

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

**An everyday picture.** A tapestry that can be finished, but only with an endless roll of thread.

## G61
In Rule 210, column 1 can carry a hidden black bit only at moments when the visible signal switches on.

**What it says.** With the blinking wall, column 1's update rules allow a black square at odd ticks only where the
visible signal goes from white to black. For the signal of the initially empty left half (GPT's G26), that happens
only at times 3, 15, 63, 255, ..., one less than a power of 4.

**Why it matters.** It pins down where the right side can do anything interesting at all: rarely, at predictable
times.

**An everyday picture.** A night-watch who may only leave the post when the lighthouse flashes on.

## G62
In Rule 210, the first pair of black squares next to the wall can appear only at a sparse list of even times: 0, 6,
30, 126, ...

**What it says.** Adding column 2's own update to G61, a black pair in columns 1 and 2 can occur only at even times,
and only where the visible signal switches off. For the signal of the initially empty left half those times are 0,
6, 30, 126, and so on.

**Why it matters.** It restricts where Rule 210's non-linear term can act near the wall to a very thin set.

**An everyday picture.** A train that can stop only at stations whose numbers come from a fixed, thinning timetable.

## G63
While the visible signal holds steady, each column on the right is forced into a fixed rhythm too.

**What it says.** In Rule 210 with the blinking wall, if column 1's visible signal is constant over a stretch, then
columns 1, 2, 3, ... on the right are each forced into a fixed repeating pattern over that stretch, shortened a
little at each end for each column further out.

**Why it matters.** It replaces G61 and G62's single-square restrictions with a whole forced strip of the right
half.

**An everyday picture.** A row of dominoes: once the first stands still, the next ones must stand still too, except
near the ends.

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

**An everyday picture.** Two people pushing a swing from opposite sides at the same moment: their pushes cancel, and
the swing keeps its rhythm.

## G66
If the left half's black squares stay within a fixed distance, the right side's columns are still almost predictable.

**What it says.** For left halves whose black squares lie within distance R of the wall, every fixed right column
still has zero entropy, uniformly. In Rule 90 a finite disturbance is felt only near times that are powers of 2.

**Why it matters.** So G65's freedom comes only from letting the left half spread without limit, which pins down
exactly where freedom lives.

**An everyday picture.** A pebble dropped in a pond makes ripples you can see clearly only at certain moments; a
fixed handful of pebbles cannot fill the pond with noise.

## G67
The largest possible "offset" at a first dip, and the pattern that reaches it.

**What it says.** Collatz's arithmetic after a step pattern is "multiply by 3^a, add an offset, divide by 2^t". At a
first dip below 1, GPT found the largest the offset can be: it is reached by putting the odd steps as early as the
rules allow. The offset is at most a third of a times 3^a.

**Why it matters.** This envelope feeds the ceilings: with the offset bounded, so is the height limit of G45.

**An everyday picture.** The heaviest load a lorry can carry and still pass the bridge's weighbridge.

## G68
At a first dip, the start and the end share the same height limit.

**What it says.** For a pattern whose growth factor first dips below 1, a start survives exactly when the start is
at most the ceiling, and equally exactly when the end value is at most the same ceiling. GPT also gave quick tests
that read only the first few or the last few steps of a pattern and can rule out the whole pattern at once.

**Why it matters.** Two descriptions of the same exceptions agree, which makes them easier to count and check.

**An everyday picture.** A door you may enter only if you are under a certain height, and leave only if you are
under the same height.

## G69
A known theorem about how close powers of 2 and 3 can get gives a polynomial cap on every height limit.

**What it says.** A published bound (Rhin's, as stated by Rozier and Terracol) says powers of 2 and 3 cannot be too
close. From it, the ceiling at a first dip after t steps is below t^14.3 / 3.

**Why it matters.** G46 showed the ceilings are unbounded; this shows they grow only polynomially. Exceptions are
confined to fairly small numbers.

**An everyday picture.** The clocks of G46 do nearly line up, but never closer than a known margin, which limits how
bad a near miss can be.

## G70
Above a polynomial size, "the growth factor stays above 1" and "the number stays above its start" pick out exactly
the same numbers.

**What it says.** Count the numbers that actually stay at or above their start for T steps, and those whose growth
factor stays at least 1 for T steps. The two sets can differ only for numbers below T^14.3 / 3.

**Why it matters.** It lets the team count the easier quantity (the growth factor) and know it matches the real one
for large starting numbers.

**An everyday picture.** Two exam markers who agree on every script except those from a small, known set of early
candidates.

## G71
The surviving count loses numbers only at the critical boundary, and the loss is set by whether the leftover number
is odd or even.

**What it says.** Each tick, every surviving pattern has two continuations, except those sitting exactly on the
survival boundary, which lose their even continuation. For real Collatz numbers, at the first step after the free
bits, which boundary numbers are lost is decided by whether F1's base-3 remainder is odd or even.

**Why it matters.** It locates exactly where real Collatz numbers can depart from fair coins in the count: an
odd-even imbalance on the boundary.

**An everyday picture.** A queue where only people standing on the line can be sent home, and a coin they carry
decides who.

## G72
Few surviving Collatz numbers can arrive at the same value: at most 1 + a/3 of them.

**What it says.** Among starting numbers of a given size that survive m steps with a odd steps, at most 1 +
floor(a/3) can end on the same value.

**Why it matters.** Paths rarely merge, so counting end values nearly counts starts. The bookkeeping stays almost
one to one.

**An everyday picture.** Few trains can arrive at the same platform at the same minute.

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

**An everyday picture.** A household budget: the final balance is the sum of every month's surplus or deficit.

## G75
Those weights are uniformly small: about (log h)/√h, where h is the number of steps still to go.

**What it says.** How much one extra odd step changes the chance of surviving h more fair coin tosses is at most
about (log h)/√h, whatever the state.

**Why it matters.** Late imbalances count for little. It controls the coin side only; the real Collatz imbalances
still need their own bound.

**An everyday picture.** On a long walk, one extra step makes little difference to where you end up, and less the
longer the walk.

## G77
The simplest way of combining G74 and G75 cannot bound the Collatz count for all horizons: that route is closed.

**What it says.** The goal is to show the real Collatz count never exceeds the coin-toss prediction by more than a
fixed factor. The crudest approach takes G75's largest weight, assumes every class is as unbalanced as it can be,
and feeds the hoped-for bound back in. GPT showed that this approach gives a bound that grows like the square root
of the number of steps, so it can never give a fixed factor. GPT also noted that a big cancellation ratio in the
data does not by itself rule out a useful bound.

**Why it matters.** It closes one tempting route cleanly, and says what is left open: sharper estimates that use how
the numbers are actually spread out, or real cancellation between plus and minus terms.

**An everyday picture.** Estimating a household's spending by assuming every purchase cost the most it possibly
could: the estimate keeps climbing even if the real budget is fine.

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

**An everyday picture.** A step forward then back, or back then forward: either way you end almost where you
started, unless a wall stops one of the steps.

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

**An everyday picture.** Watching a film by its changes from frame to frame instead of the frames themselves: the
changes follow a simpler script.

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

**An everyday picture.** Two people who may only stand on every fourth paving stone cannot share a path shorter than
four stones unless they stand on the same one.

## G84
At 21 odd steps, the first case left open, any meeting of two surviving numbers would have to take one exact form.

**What it says.** Sort the surviving step patterns by their first three steps: odd-odd-even or odd-odd-odd. Two
patterns that begin the same way cannot meet at 21 odd steps, so a meeting needs one of each kind, and the two
starting numbers must differ by exactly 4.

**Why it matters.** It narrows any search for a meeting at 21 to one precise shape, instead of all patterns.

**An everyday picture.** A detective who cannot yet name the culprit, but has proved it must be one of two twins who
arrived four minutes apart.

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

**An everyday picture.** Pruning a family tree: if no descendant of a branch could have been born in the right year,
you need not trace that branch any further.

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

**An everyday picture.** Two overlapping charges on a bill reduced to the small difference between them; charges
with no match stay in full.

## G92
Even with the pairing tool, the crude estimate still grows, slowly, with the length of the run.

**What it says.** Grant generously that unpaired paths cancel completely, and bound every pair by the largest amount
it could contribute. The estimate still grows like the logarithm of the number of steps, so it cannot give the fixed
bound that is wanted.

**Why it matters.** It improves on the square-root growth of G77, and shows that the remaining gap needs real
information about which paths pair up.

**An everyday picture.** Assuming every repair costs the most it possibly could: the estimate still creeps up, only
more slowly than before.

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

**An everyday picture.** A staircase with no two landings in a row can still be uneven underfoot.

## G96
Watching one square change and following a moving pattern are different measurements.

**What it says.** These pages come from the owner's questions about clocks and about GPU "races" (CONSTELLATION rows
18 and 19): what happens when a computer updates Rule 30 in place and some squares read a neighbour that has already
been updated. They are about Rule 30 for its own sake, not directly about the prize. A pattern sliding along at a
steady speed changes at every fixed square, yet does not change at all if you move with it. GPT wrote both kinds of
change exactly. The change at a fixed square is Rule 210 applied to the row (C.8), though the pattern of changes
does not itself follow Rule 210.

**Why it matters.** It fixes which "change" an instrument measures before anyone reads physics into it.

**An everyday picture.** From the platform a passing train changes the view every moment; from inside the carriage
nothing changes at all.

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

**An everyday picture.** In a queue you may not know the person next to you, yet know the person two places back.

## G101
The same hidden memory appears for an observer moving at three-quarter speed.

**What it says.** An observer who stays put for one tick and steps right for three, over and over, finds the second
and fourth flips of each block linked in the same way.

**Why it matters.** The memory is not just an effect of moving at full speed; it appears inside the pattern too.

**An everyday picture.** The link in the queue is still there if you walk along it more slowly.

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

**An everyday picture.** A dish comes out right if nothing anywhere in its chain of ingredients was spoiled; the
longer the chain, the more chances for spoilage.

## G104
Races that read the right neighbour leave each row looking perfectly random; races that read the left leave a trace
in neighbouring pairs.

**What it says.** With right-reading races, every row still has exactly the statistics of fair coin flips. With
left-reading races the share of black squares stays a half, but neighbouring squares differ a little more often than
they should.

**Why it matters.** It explains how a glitching computation can look statistically perfect: inspecting one row
cannot reveal right-reading races.

**An everyday picture.** A tampered deck can still look perfectly shuffled; only the order in which the cards come
out gives it away.

## G105
Joining the row into a ring changes an exact probability, even though large rings look fair.

**What it says.** On a small ring, the number of earlier rows that lead to an all-white row depends on whether a
race happened, so the exact probabilities differ from the fair ones.

**Why it matters.** Results proved on the endless line cannot be assumed exact on the finite rings that computers
actually run.

**An everyday picture.** Joining the ends of a chain removes the free end you would use to rebuild it.

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

**An everyday picture.** A message and its encrypted copy each look like gibberish, yet with the key either one
gives back the other.

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

**An everyday picture.** A cracked bell sounds wrong at almost every pitch; finding one pitch where it sounds true
does not prove it is sound.

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

**An everyday picture.** Remembering yesterday as well as today can still miss an older cause.

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

**An everyday picture.** A lock that opens only when three digits are right: knowing two of them tells you nothing.

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

**An everyday picture.** Two diaries of the same day agree on everything except what one writer misheard.

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

**An everyday picture.** A note and its octaves: start at three and keep doubling.

## G125
The sideways rule's repeating patterns are exactly Rule 30's repeating patterns on a ring.

**What it says.** The sideways rule reads Rule 30 along time instead of across space, turning pairs of columns into
sequences of three symbols (CONSTELLATION row 5). A pattern that repeats in that view is the same thing as a ring of
squares whose row comes back to itself in time.

**Why it matters.** It hands every repeating sideways pattern to the ring census, which already lists them all for
rings of up to 29 squares, with no new computation.

**An everyday picture.** A strip of wallpaper that repeats sideways can be rolled into a cylinder, provided the
pattern also matches all the way through time.

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

**An everyday picture.** Each pass through a sieve removes more grains; it does not say what is left at the end.

## G128
However many sideways steps you take, every possible sequence of black and white still appears in some column.

**What it says.** The patterns that survive every sideways step are exactly the pairs of neighbouring columns in
complete Rule 30 histories, and either column of such a pair can be any sequence at all.

**Why it matters.** It closes a broad route: narrowing by sideways steps alone can never rule out a blinking column.
Any proof must use the blinking wall itself or the finiteness of the seed.

**An everyday picture.** A sieve that, however often you shake it, still lets every single grain through on its own.

## G129
For each seed size, whether a finite seed can keep the middle blinking is a finite check.

**What it says.** Fix the blinking wall and a maximum size for the seed's left part. The possible histories then
form a closed, bounded family: if there are none, a finite rectangle of the pattern already shows the contradiction.
Each left seed allows at most one complete sequence of visible bits.

**Why it matters.** It restates the prize's left-half question as one finite question per size, and Local showed the
records already answer it up to size about 84 (L083). The open part is one statement covering every size.

**An everyday picture.** Testing a key against locks of every size: each lock is a finite test, but the claim is
about all of them.

## G130
Fix the seed's right part, and any wall forces exactly one left part, though usually an infinite one.

**What it says.** Reading Rule 30 backwards (the crossword quirk) fills in the left part uniquely from the requested
middle column and any chosen right part. Even an all-white right part works, if the left part may be infinite.

**Why it matters.** So a finite seed exists exactly when some finite right part makes the forced left part turn
white for good. That is the precise target.

**An everyday picture.** Given the film and one half of the opening frame, the other half is fixed, but it may need
an endless canvas.

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

**An everyday picture.** A wobbling top needs a push every so often, and the gaps between pushes cannot keep
stretching without limit.

## G134
The same holds for every rotation angle whose continued-fraction digits (the whole numbers you get by repeatedly
taking off a number's whole part and turning what is left upside down) stay bounded.

**What it says.** G133's spacing limit extends from the golden ratio to every irrational angle of "bounded type",
whose continued-fraction digits never grow large.

**Why it matters.** A larger family of kicked patterns is excluded.

**An everyday picture.** The same rule for every top that wobbles at a steadily irrational rate.

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

**An everyday picture.** A filter that turns away some impostors and lets one through, which still faces every other
check.

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

**An everyday picture.** A library holds every story and one story can be very plain; neither tells you whether a
book ends.

## G141
Holding the wall fixed changes how the past works: an earlier row need not be unique, or finite.

**What it says.** Run backwards with the middle column forced, a black beat fixes the square beside it, while a
white beat allows two choices. GPT found a test for when the earlier rows stay finite, and two finite rows that
merge into one.

**Why it matters.** The uniqueness of the past that holds for the free rule (G121) cannot be borrowed here, and the
descent idea still gives no contradiction.

**An everyday picture.** A gatekeeper who lets two different visitors into the same room erases which one came.

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

**An everyday picture.** The same tune started on the off-beat clashes with the band.

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

**An everyday picture.** A distant drumbeat can fall silent only if it was a repeating rhythm already fading away.

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

**An everyday picture.** A staircase that can only climb on every other step.

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

**An everyday picture.** Another impostor the filter lets through: the next checks must catch it, or show it is
genuine.

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

**An everyday picture.** In a scale built only from octaves, a note three times the base frequency never sounds.

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

**An everyday picture.** A shopping trip that comes out even after the refund at the till can still take the card
over its limit halfway round the shop.

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

**An everyday picture.** A long-distance timetable must still price the local stopping trains that share its track.

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

**An everyday picture.** A train that serves your station does not stop there at every time on the timetable; the
fare rule need only work for the trains that actually stop.

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

**An everyday picture.** Check that two train journeys really share a station before replacing the stations by
summaries; join the summaries first and the lost connection cannot be recovered.

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

**An everyday picture.** A detective needs a clear fingerprint whenever one is asked for, not one on every surface
of the room.

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

**An everyday picture.** A row of switches where each setting decides the next must come round in a loop; allow one
free choice and the counting no longer limits the journey.

## G190
An even-length return can be followed by keeping the stripe's two halves together.

**What it says.** Follow two windows of the stripe side by side, one on each half. A return after a doubling is a
walk through the finite map of such pairs that ends with the two starting windows swapped. Joined to its swapped
copy, the walk closes into a full repeating stripe whose halves are opposites.

**Why it matters.** It keeps the tick-by-tick link between the halves that a simple count of black and white would
lose. The real maps have not been classified, and it gives no delay estimate.

**An everyday picture.** Slide two strips of paper through a frame until their starting patterns have changed
places; a copy with the strips swapped completes the pattern.

## G191
Walks that swap the two halves either exist for every large period or for none.

**What it says.** In a finite map with a swap symmetry, walks to the swapped start of half a period's length either
exist for every large enough power-of-two period, or only for periods below the number of positions in the map.
Checking one period beyond eight times the square of that number decides which. Local reviewed it (L157). In Rule
30's maps, the first case needs a fork inside a region the walk can circle.

**Why it matters.** It turns 'do return delays keep growing?' into a finite check on each map. The real maps are
still unclassified.

**An everyday picture.** Two runners on a circular track, starting apart: whether they can ever swap places at a
given lap depends on how the track's loops are arranged, not on luck.

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

**An everyday picture.** On a two-lane running track, the lanes can stay apart, cross once a lap, or cross in ways
that fit many lap counts; a lap chart shows which.

## G195
A small local pattern proves the swaps can mix, but only if a way back exists.

**What it says.** Two steps from the same place with opposite order bits occur exactly at one small pattern of four
windows. Inside a region a walk can circle, that pattern settles G194's test in favour of every large period. The
length-eight map contains the pattern but has no loop, so there it proves nothing.

**Why it matters.** It gives something concrete to search for without classifying a whole map, and shows why a local
fork alone is not enough.

**An everyday picture.** Two doors from the same hall lead to rooms where the cards end up in different orders; to
choose again and again, there must also be a corridor back to the hall.

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

**An everyday picture.** A changed letter on a ticker tape stays in view until enough tape has passed through the
window.

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

**An everyday picture.** Two copies of the same photograph can show where a journey ended without telling us where it began.

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
