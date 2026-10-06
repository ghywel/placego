# Plain-word summaries, one per proof

*The source for the "In plain words" section of every page in this folder. One section per proof, headed by its
id; the first paragraph is the one-line hook used in the index. Rebuild with `python3 proofs/build.py`.*

*How it is kept. Whoever adds or moves a PROOFS.md entry writes a first draft here, since the build refuses to run
without one: the hook, then What it says, Why it matters and An everyday picture, with no control names or review
status (the page's status line carries those). Cloud rewrites drafts into plain words for a general reader in
batches. Plain-words pass done through W122 (2026-10-06); entries after it may still be drafts.*

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

**Why it matters.** It is Jen's classic theorem with a stopwatch attached: not just "the rhythm breaks some day" but
"by this time", which is the kind of bound a proof can use. It assumes nothing about the right side, so the rhythm
is interrupted whether or not anything there "sees" the wave coming (the owner's reading). Nor can the wave be
blocked: the proof relies on Rule 30 passing its left input straight through and on the edge always advancing, and a
rule that could block news from the left would fall outside it.

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

**An everyday picture.** A forger who copies the opening of a signature too exactly is caught by that very
precision.

## 12
Once the edge band settles into its rhythm, it has no long white gaps.

**What it says.** If the diagonals near the edge have been repeating with a common period P for at least P steps,
then no white run inside that band is longer than 2P.

**Why it matters.** It shows the settled band is "crowded" with black, which the next theorem uses against repeats.

**An everyday picture.** A well-kept fence has no long missing stretches.

## 13
The white stripe a repeat leaves cannot sit inside the settled band.

**What it says.** Combining 10 and 12: if the band near the edge is settled, a repeat's white stripe would have to
lie in it, and it cannot be longer than 2P there, so the repeat is bounded.

**Why it matters.** A sharper cap on repeats, from the edge band's own regularity.

**An everyday picture.** A long empty parking space cannot hide in a car park that is always full.

## 14
A perfectly regular wheel, never nudged, cannot produce the pattern.

**What it says.** If column 1 is the trace of a wheel turning by a fixed irrational angle (a "Sturmian" sequence,
like the pattern of a clock hand passing a mark), the left half is never finite. With Jen's theorem for rational
angles, no un-kicked wheel of any speed works.

**Why it matters.** Column 1 next to a blinking wall really does behave like a wheel with occasional kicks. This
proves the kicks are necessary: any counterexample must come from the kicks, never from the turning alone.

**An everyday picture.** A metronome left alone keeps time; to break the rhythm somebody has to bump it.

## 15
The same holds for almost every wheel speed, whatever pattern of marks it passes.

**What it says.** Theorem 14 used one mark; this allows any finite set of arcs as marks. For almost every rotation
speed, no such coding gives a finite left half.

**Why it matters.** It widens 14 from one simple kind of wheel to nearly all of them.

**An everyday picture.** It does not matter how many notches you cut in the wheel: turning it alone never does the
trick.

## 16
In Rule 30's simpler cousin, Rule 90, the blinking middle is impossible, proved with Pascal's triangle.

**What it says.** Rule 90 just adds neighbours (exclusive-or). Its patterns are Sierpinski triangles, and at times
that are powers of 2 the middle must be white twice in a row, so it cannot blink for ever.

**Why it matters.** It shows the kind of proof that works for the linear cousin, and why Rule 30, with its "or", is
harder: the clean arithmetic is missing.

**An everyday picture.** Sierpinski's triangle of triangles: every power of 2 is a fresh, empty triangle at the
centre.

## 17
If both the middle and column 1 eventually repeat, the left half cannot be finite (Jen's theorem).

**What it says.** Two neighbouring columns that both repeat from some point on force infinitely many black squares
on the left.

**Why it matters.** It settles every periodic column 1 at once. Since a finite seed makes column 1 irregular, the
open case is exactly the irregular one.

**An everyday picture.** Two drummers keeping steady beats cannot hush the whole crowd to their left.

## 18
Next to a blinking wall, Rule 30's sibling Rule 210 behaves exactly like the simple cousin Rule 90.

**What it says.** With the wall blinking, every black square of Rule 210's forced left half sits on one colour of a
checkerboard, and on that checkerboard the rule reduces to Rule 90's simple addition.

**Why it matters.** It explains why the left-side conjecture fails for Rule 210 but may hold for Rule 30: Rule 210's
nonlinearity switches itself off there, and Rule 30's does not.

**An everyday picture.** A dancer who only ever steps on the black squares of a chessboard never meets the white
ones.

## 19
A counterexample would have to be almost frozen: the right side can only whisper.

**What it says.** Next to a blinking wall, every column on the left carries at most 0.0646 bits of new information
per tick, a certified bound computed exactly.

**Why it matters.** A counterexample cannot look random on the left; it must be nearly frozen. It shrinks the
haystack the needle could be in.

**An everyday picture.** A walkie-talkie that can transmit about six letters per hundred seconds.

## 20
We ran the pure wheel until it repeated, about 15 billion ticks, and checked: it fails.

**What it says.** With column 1 exactly the never-kicked wheel, the joint pattern of the two columns repeats after a
cycle of 15,009,104,432 steps, and inside that cycle the left half is never finite. Certified by computation.

**Why it matters.** An exact check of the single most important special case, with a committed program anyone can
rerun.

**An everyday picture.** Watching a combination lock's dial until every position has come round again.

## C1
While the middle column stays black, the left half next to it is a fixed checkerboard, whatever the right side does.

**What it says.** Suppose the middle column is black for a stretch of k + 1 ticks. Then the first k squares to its
left, at the start of that stretch, alternate white, black, white, black, and column 1 has no say in it.

**Why it matters.** Black stretches are where the right side is silenced (proof 01). This lemma says what the left
half looks like there: something fully known. A candidate's left half is therefore predictable in those places, and
GPT's later results on slow walls (E4, E5) build on it.

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
with one square trimmed from each end. So every white triangle in Rule 30 is an exact isosceles triangle, fixed by
the row, place and width where it is born.

**Why it matters.** The white triangles are the most visible structure in Rule 30, and this makes them exactly
predictable once born. The gaps in the record's "ladder" are the bases of such triangles. It was also checked on a
million runs; the neighbouring Rule 110 breaks it.

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
A Collatz number that ran off to infinity would have to change its step pattern endlessly: it could not loop or repeat.

**What it says.** A published theorem (Dubickas, 2009): if an orbit grew for ever, its sequence of odd and even
steps would have at least about 1.7 n different patterns of length n. Repeating or nearly repeating step patterns
are impossible.

**Why it matters.** It is Collatz's counterpart of Jen's theorem for Rule 30: it rules out the simple
counterexamples and says any real one must look irregular.

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
Mahler's 3/2 problem needs two conditions at once, and its known cellular-automaton form works differently from Rule 30.

**What it says.** Mahler asked whether some number, multiplied by 3/2 again and again, always has a fractional part
below a half. GPT showed this needs both an integer step pattern and a fractional-part condition. For example, two
odd steps in a row are forbidden, and a repeating pattern can satisfy the fractional part while matching no whole
number. The known cellular automaton for the problem is not of Rule 30's "left-invertible" kind.

**Why it matters.** It sets out honestly what transfers from the record's methods to Mahler's problem, and warns
where it does not.

**An everyday picture.** A lock with two dials: getting one right is not enough.

## G51
The exact finite form of Mahler's two conditions over T steps: a class of whole numbers and a window of fractions.

**What it says.** For a pattern of T steps, the whole-number starts form one class modulo 2^T, and the allowed
starting fractions form one exact interval. Both are written down explicitly.

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

**What it says.** Give each black square its position, and average the positions in arithmetic modulo p. This
"phase" moves by exactly one when the ring is turned by one, so it measures drift. A cycle's total drift is the sum
of the phase changes along it.

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
exactly when two allowed step patterns of a fixed length have offsets equal modulo 3^a. GPT showed this, built the
two meeting numbers explicitly when such patterns exist, and showed that no meeting is possible below a = 7.

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
2 and 3. Knowing only the last two leaves it a coin toss; adding the first makes it certain.

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
A root's backward tails must have spatial periods that grow without bound.

**What it says.** The farther back we follow a nonzero finite root's unique history, the longer the repeating patterns far to the left must become. Their periods form a chain in which each divides the next, with infinitely many increases.

**Why it matters.** A repeating row with a fixed period has only finitely many states. It cannot take arbitrarily many steps to reach zero for the first time. This rules out a uniformly bounded family of ancestor patterns, but supplies no contradiction to a column that eventually alternates.

**An everyday picture.** A clock with finitely many states cannot postpone its first stop arbitrarily long.

## G124
Periodic rows that fade completely have tightly restricted repeating lengths.

**What it says.** If a spatially repeating Rule 30 row eventually becomes all-zero, its shortest repeating block has length one, or three times a power of two. Every such length occurs.

**Why it matters.** Once the output contains both colors, a repeating predecessor can keep its period or double it. The constant-one row has the special period-three predecessors that start this chain. This classifies one family of spatial patterns, but does not exclude an eventually alternating temporal column.

**An everyday picture.** Following a repeating pattern backward can lengthen its loop by doubling, after one initial loop of length three.

## G125
Cycles in the sideways rule are the same spacetime patterns as recurrent ring states.

**What it says.** A finite cycle of the sideways map closes the columns into a spatial ring. Its time tracks must repeat, and its starting ring row must already lie on a temporal cycle.

**Why it matters.** This identifies all sideways periodic points through finite-ring recurrence. A row that is merely heading toward a cycle does not qualify, because the sideways construction needs a consistent infinite past as well as a future. The correspondence supplies no restriction on nonperiodic sideways orbits.

**An everyday picture.** Closing a strip around a cylinder requires the pattern to match throughout its past and future.

## G126
Six forbidden words completely describe the sideways rule's first ternary image.

**What it says.** A ternary sequence has a predecessor exactly when it avoids six short words. A local construction produces a predecessor for every allowed sequence.

**Why it matters.** The old forbidden words were only a necessary test. This supplies both necessity and sufficiency, including nonperiodic sequences, while showing that the image still contains many freely chosen patterns. It does not describe the deeper images or enforce a prize problem's wall.

**An everyday picture.** A short checklist now determines whether a whole sequence can pass through one stage, but later stages may impose more rules.

## G127
A predecessor inside the image may require a longer repeating pattern.

**What it says.** A period-two target has a period-four predecessor inside the image, but no period-two predecessor there. Therefore no predecessor choice that commutes with shifting can stay inside the image for every target.

**Why it matters.** Failure of a local inverse is not failure of every predecessor. A separate certificate shows genuine loss at the next layer: an allowed target forces a forbidden word in every predecessor. This establishes one strict image inclusion, not a rule for all deeper layers.

**An everyday picture.** A repeating request may need a response with a longer loop, even when a short local response exists outside the allowed set.

## G128
The unrestricted sideways limit still contains every binary temporal trace.

**What it says.** Adjacent columns in a full spacetime diagram give exactly the sideways limit set. Projecting onto either column can produce any binary time sequence, so the limit contains nonperiodic sequences and retains at least one bit of word-count entropy per site.

**Why it matters.** Strict image losses do not imply a small or finite limit. The result allows unrestricted infinite spatial rows; fixing an alternating wall or insisting on a finite seed adds constraints that this argument does not remove.

**An everyday picture.** A shrinking set of paired records can still contain every possible individual record.


## G129
Finite left support becomes an explicit constraint on the sideways limit.

**What it says.** Fix a wall and a maximum initial left radius. The admissible pairs form a compact class: every forced initial cell farther left must be zero. If this class is empty, some finite rectangle already witnesses the failure. Each left seed permits at most one complete visible itinerary.

**Why it matters.** This connects unrestricted spacetime extension to the boundary condition the prize needs. Growing support cannot be passed through compactness as though the radius were fixed. Neither the compactness statement nor the itinerary count proves that the alternating-wall classes are empty or that their time factors have zero entropy.

**An everyday picture.** Matching every finite view can yield a whole picture, but a picture assembled from ever larger canvases need not fit one finite canvas.


## G130
Every wall has one forced left seed once the initial right tail is fixed.

**What it says.** Successive left-permutive inversion gives a unique infinite left row for any prescribed temporal wall and any fixed initial right tail. Even a right tail of zeros can realize every wall if infinite left support is allowed.

**Why it matters.** A finite global seed exists exactly when some finite right-tail choice gives an eventually-zero forced left row. Arbitrarily long finite-prefix realizations can instead require growing left support; they do not settle this condition.

**An everyday picture.** Fixing one half of the starting picture determines the other half from the requested movie, but the determined half may need an infinite canvas.


## G131
Finite recoding preserves the repetitions that exclude a Sturmian companion.

**What it says.** Any fixed finite block function of a Sturmian sequence is excluded beside the alternating wall with finite left support. This includes rotation codes on several arcs when all endpoints belong to one rotation orbit, for every phase and every irrational angle.

**Why it matters.** The earlier theorem transfers with a fixed repetition margin; no new numerical evidence or assumption of an invertible code is needed. Unrelated endpoint orbits and general aperiodic companions remain open.

**An everyday picture.** Reading a fixed group of neighboring symbols cannot erase a long repeated stretch except at its ends.


## G132
A higher-dimensional rotation can still expose only one circle coordinate.

**What it says.** The earlier exclusion applies to torus observables that factor through an integer circle projection and an allowed arc code. Rational projected angles give periodic codes; irrational ones inherit the Sturmian obstruction. Endpoint conventions do not change the conclusion.

**Why it matters.** This covers some partitions with several original endpoint orbits, such as a circle covering. It leaves genuinely multidimensional partitions and general unrelated endpoints open.

**An everyday picture.** Several rotating coordinates can be read through one dial. The exclusion concerns what that dial displays, not how many hidden coordinates are moving.


## G133
A golden-angle code needs kicks often enough to interrupt long unbroken stretches.

**What it says.** The earlier repetition proof gives a uniform linear bound on how long a visible companion can agree with a golden-angle Sturmian word beside a finite left seed. Consecutive disagreement times therefore obey a geometric upper bound; super-geometrically separated flips cannot rescue the code.

**Why it matters.** This reaches a class of kicked, aperiodic companions rather than only exact rotation codes. It gives no positive entropy or kick-density bound, and does not exclude every sparse schedule or the measured rational wheel.

**An everyday picture.** A correction cannot postpone the next correction arbitrarily far when the underlying repeated stretches grow at a controlled rate.


## G134
The spacing restriction extends from the golden angle to every irrational rotation with bounded partial quotients.

**What it says.** A finite-left companion cannot track such a Sturmian code for an arbitrarily long interval relative to the current time and initial radius. Corrections with unbounded successive spacing ratios therefore cannot maintain the alternating wall.

**Why it matters.** This excludes sparse kicked codes across a larger family of irrational angles. It also makes the finite-offset step explicit. Unbounded-type angles, positive entropy and the measured rational wheel remain open.

**An everyday picture.** For these rotations, the repeated patterns grow at a controlled rate, so a correction cannot postpone the next correction indefinitely.


## G135
The correction-spacing limit holds for every irrational Sturmian angle, even when resets change the angle.

**What it says.** The repetition obstruction itself controls the growth of the scales used in the proof. This gives one uniform bound on an uninterrupted Sturmian-coded stretch, without assuming bounded partial quotients. Phase and angle can both change between pieces, but reset times cannot spread faster than geometrically.

**Why it matters.** This removes the angle restriction from the sparse-correction exclusion and reaches phase-reset codes. Geometric resets, general arc observables and a positive entropy theorem remain open.

**An everyday picture.** Changing the dial at each reset cannot make the next uninterrupted stretch arbitrarily long relative to the current time.


## G136
Finite recodings retain the uniform spacing bound, with an explicit allowance for their window width.

**What it says.** A code that reads a fixed finite block of a mechanical word cannot evade the repetition obstruction. Rational angles are included by finite-prefix approximation. Resetting the code, phase and angle between pieces still requires corrections no farther apart than a geometric bound, provided the reading widths stay bounded.

**Why it matters.** This reaches recoded and orbit-endpoint reset companions. The window bound is essential: increasingly wide recodings can imitate any selected finite binary prefix. General companions and positive entropy remain open.

**An everyday picture.** Reading several neighboring symbols adds a fixed allowance. Increasing that reading window indefinitely changes the problem.


## G137
Sparse powers of two pass the entire repetition test, while faster integer powers fail it.

**What it says.** The word with ones exactly at powers of two satisfies every necessary repetition inequality and has only linearly many different words of each length. Replacing two by any integer at least three creates zero runs that violate the inequality.

**Why it matters.** The repetition condition excludes some geometric defect schedules, but cannot by itself prove positive entropy or exclude every sparse one. Passing the condition is not a Rule 30 realization.

**An everyday picture.** A useful filter can reject some candidates while admitting a sparse one that still needs every other physical constraint checked.


## G138
The inverse wall equations expose a sparse nonlinear gate, but do not yet control the initial tail.

**What it says.** The first five forced columns have explicit formulas in neighboring visible bits. For the dyadic candidate, the depth-four even-time product is nonzero only once. That does not make the initial row finite: even a constant code with an identically zero product forces an infinite checkerboard tail.

**Why it matters.** This begins the wall-specific audit beyond repetition tests and records why a low-depth sparse gate is insufficient. An all-depth invariant is still missing.

**An everyday picture.** One quiet gate does not certify that the rest of the circuit is quiet.


## G139
A sparse temporal input can produce zero temporal entropy at every fixed depth while leaving the spatial initial tail unresolved.

**What it says.** The wall inverse reads only a finite forward time window at each fixed depth. Dyadic pulses therefore create defects only in widening neighborhoods before those pulses. Each fixed column, and each fixed finite left window, has zero temporal word-count entropy.

**Why it matters.** Irregularity measured across the initial row does not contradict this temporal theorem. The reading window grows with depth, so the theorem cannot establish a finite initial tail or rule one out.

**An everyday picture.** Looking along time at one location and looking across space at one instant measure different patterns.


## G140
The wall's whole compatible family and a single dyadic orbit have different entropy, and neither settles finite support.

**What it says.** The existing wall coding turns two evolution steps into one shift of the visible word. The full compatible family has entropy one, while the dyadic orbit closure has entropy zero. That orbit closure contains an infinite checkerboard state as a limit.

**Why it matters.** An infinite-support limit does not rule out a finite starting row when its support bound grows with time. The missing statement still concerns the starting row's spatial tail.

**An everyday picture.** The variety of an entire library differs from the variety along one story; a limit of growing finite objects need not stay finite.


## G141
An imposed wall changes the predecessor problem: finite ancestors need not be unique or exist.

**What it says.** Backward through a black wall phase, the nearest-left bit is fixed. Backward through a white phase, it has two choices. Finite inverse-tail graphs determine whether the resulting ancestors stay finite. A concrete pair of finite rows merges under the imposed boundary while passing the first black-time condition.

**Why it matters.** Whole-line injectivity cannot be imported into this boundary problem. Descent through finite ancestors can stop at a root, so it still supplies no prize contradiction.

**An everyday picture.** Holding a boundary externally can discard information that ordinary evolution would carry into the other half of the system.


## G142

If a finite pattern can keep the alternating wall's condition forever, its successive rows must approach an infinite pattern along some subsequence. This is necessary because its outermost black cell moves outward at every step: a compact family made entirely of finite compatible patterns would force a predecessor with a smaller radius than the family's smallest one. So finding an infinite limit does not refute a finite starting pattern. The question of whether any finite starting pattern works is still open.


## G143

There is a particular way to turn an irrational rotation into black and white symbols that passes every repetition test we have required of the wall's neighbour. It is not periodic, its constant runs are at most two symbols long, and its number of distinct words grows only linearly. Differentiating it gives a Sturmian sequence, but some good rotation approximations flip every symbol instead of repeating it. Tracking that sign proves it passes the test at every period. This does not show that Rule 30 can produce it from a finite pattern; it shows that the repetition test alone cannot rule it out.


## G144

For half-circle rotation codes started exactly at a partition boundary, the repetition test has a precise exceptional class. A code passes with some fixed allowance exactly when its angle's continued fraction eventually consists of twos and its convergent numerators are eventually odd. Outside that countable class, the proof gives repeated intervals whose excess grows without bound. Within it, the test still cannot decide whether a finite Rule 30 pattern produces the code. Other starting phases remain open.

## G145

Moving the starting point of the silver-angle rotation by half a turn makes a decisive difference. The boundary-start code passes our repetition test, but this half-phase code has an explicit sequence of prefix repeats whose excess grows without bound. The first one is the period-seven witness already checked by Local. No finite allowance rescues this phase, so it is excluded as a finite-wall companion. The boundary-start code still has no established finite Rule 30 realization.
