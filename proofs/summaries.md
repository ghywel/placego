# Plain-word summaries, one per proof

*The source for the "In plain words" section of every page in this folder. One section per proof, headed by its
id; the first paragraph is the one-line hook used in the index. Rebuild with `python3 proofs/build.py`.*

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

**What it says.** Any finite seed has a leftmost black square, and its influence travels inward at full speed. If
two neighbouring columns repeat with period P over a stretch of time, the stretch must end within a short time
after that influence arrives: roughly the distance to the edge plus two periods.

**Why it matters.** It is the classic Jen theorem with a stopwatch attached. It turns "periodicity is impossible
for ever" into "periodicity must break by this time", which is the kind of bound a proof can use.

**An everyday picture.** A ripple from the edge of a pond: you can bob in a steady rhythm only until the wave
reaches you.

## 06
If the middle and column 1 both repeat, the forced left half can never be silent for more than two periods.

**What it says.** With both columns repeating with period P, every white run in the top row of the left half is at
most 2P − 2 squares long.

**Why it matters.** A finite left half needs an endless white run. This shows repeating inputs cannot give one, with
a sharp number attached.

**An everyday picture.** A drummer keeping a steady beat cannot leave a gap longer than two bars.

## 07
A pattern can only repeat if it is shorter than the distance to the edge.

**What it says.** If two neighbouring columns show the same block of n values twice, at times a and a′, then n is at
most the edge's distance plus a′.

**Why it matters.** Repeats are the raw material of periodicity. This caps how long any repeat can be, using only
how far away the seed's edge is.

**An everyday picture.** An echo can only repeat what has had time to travel back from the wall.

## 08
In the band near the edge, two neighbouring diagonals can never both fall silent for ever.

**What it says.** Near the left edge the pattern runs along diagonals. If one diagonal becomes white for ever, the
one two steps over becomes black for ever, and no two adjacent diagonals can both be white for ever.

**Why it matters.** It gives the edge band a rigid structure, which later results use to find black squares where a
counterexample would need white ones.

**An everyday picture.** A row of streetlights wired so that two neighbouring lamps can never both be off for good.

## 09
The edge band's rhythms keep slowing down for ever: the clock never stops.

**What it says.** The repeating periods of the diagonals near the edge grow without limit, so there are infinitely
many diagonals that go white for ever and infinitely many that go black for ever.

**Why it matters.** It proves a mechanism Rowland observed: the edge keeps producing fresh structure. Several
exclusions below need a black diagonal deeper than any given depth, and this supplies it.

**An everyday picture.** A clock whose tick doubles in length again and again, like the marks 1, 2, 4, 8 on a
ruler: it never settles into one rhythm.

## 10
A repeat leaves a white stripe behind it, and a black diagonal there caps the repeat.

**What it says.** If two neighbouring columns repeat a block of n values, the row at the second occurrence is white
across a whole range of diagonals. So a black diagonal inside that range limits how long n can be.

**Why it matters.** It joins the repeat bound (07) to the edge band (08, 09): the band's black diagonals become
measuring sticks for repeats.

**An everyday picture.** A fingerprint left on glass: a repeat leaves a mark you can check for later.

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

**An everyday picture.** Two clocks with unrelated periods: now and then their hands almost line up, and the near
misses can be as close as you like.

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
The prefix growth-factor condition rules out two starts meeting with the same odd-step count up to 20.

**What it says.** Require the multiplier from tripling and halving to stay at least one after every prefix of the step pattern. Any such pattern lasting two steps begins with two odd steps. Its start therefore leaves remainder 3 on division by 4. Two different starts with the same final value and the same number of odd steps must differ by at least 4. The exact range of their additive offsets is too small to allow that through 20 odd steps.

**Why it matters.** This extends the finite word search through 17 using a proof and exact arithmetic. It concerns the growth-factor condition, which differs from requiring the actual number to stay above its start. The new spacing proof awaits independent review; it does not resolve Collatz.

**An everyday picture.** Two arrivals must be at least four minutes apart, but their permitted arrival window is shorter than four minutes.

## G84
At 21 odd steps, any meeting allowed by these conditions must have one precise orientation.

**What it says.** For two starts satisfying the prefix growth-factor condition and meeting with 21 odd steps each, the smaller starts odd-odd-even and the larger starts odd-odd-odd. The starts differ by exactly four. The reverse orientation is excluded by bounds on the two kinds of offsets. No meeting pair has been found.

**Why it matters.** It narrows the first count left open by W83 without another large search. These are necessary conditions, not an existence claim. Independent review remains pending.

**An everyday picture.** A detective narrows a possible pair to two adjacent seats with a specific left-to-right order, but has not found anyone occupying both.

## G85
The same possible pair must follow two more common odd steps.

**What it says.** Continue W84's smaller and larger starts. After their differing third step, their values have the same parity. The smaller start needs an odd fourth step to satisfy the growth-factor condition, forcing the larger to take one too. The same argument forces an odd fifth step for both. Their first five step patterns must be 11011 and 11111, where 1 means odd. Their starts leave remainders 27 and 31 on division by 32.

**Why it matters.** It makes the necessary candidate shape more precise. It neither finds a meeting nor excludes every possible pair. The next step has opposite parities, so the common odd-step extension stops here. Independent review remains pending; the small direct trajectory controls passed.

**An everyday picture.** Two routes must share two extra turns after their first fork; that still does not show that they reach the same destination.

## G86
A prefix can buy slack that its remaining steps cannot satisfy on their own.

**What it says.** Cutting off a common-count prefix does not preserve the requirement that the growth multiplier stay at least one. Earlier odd steps can build a buffer that pays for later even steps. An explicit 33-step pattern satisfies the full condition, but its last 27 steps fail the condition when measured from a fresh start. The correct suffix condition must retain the prefix's buffer.

**Why it matters.** It blocks an invalid shortcut: applying W83's smaller-count result to a suffix that no longer satisfies W83's hypothesis. The original collision question and the condition with a carried buffer remain open. This reasoning awaits independent review.

**An everyday picture.** A traveller saved money before the next leg. Starting the budget at zero halfway through gives a different affordability test.

## G87
An offset bound forces the sixth step and then two more steps of any possible 21-odd-step meeting pair.

**What it says.** W85 leaves two possible choices at the sixth step. One choice would shrink the permitted offset gap below the gap a meeting requires, so it is excluded. The remaining choice, followed by the growth-factor condition, forces patterns 11011011 and 11111111 for the first eight steps. The starting remainders must be 251 and 255 on division by 256.

**Why it matters.** It narrows the necessary candidate shape by a proof rather than a larger search. It does not exclude every candidate or find a meeting. The preregistered small controls passed; independent review remains pending.

**An everyday picture.** A route takes one fork because the other costs more than the remaining budget. The next two turns are then forced, but the destination is still unknown.

## G88
A candidate tree can be cut off using exact bounds on every possible continuation.

**What it says.** For each partial step pattern, calculate the smallest and largest final offset allowed by the growth-factor condition and remaining odd count. A pair of starts four apart can meet only if its required offset difference lies inside the two continuation ranges. Every rejected branch has an explicit arithmetic reason; both next parity choices are covered. A complete tree with no witnesses would exclude this finite class.

**Why it matters.** This offers a certificate rather than a larger uncontrolled scan. The run is preregistered with a node and time cap; hitting either cap proves nothing about the unexplored branches. A separate known collision without the growth-factor restriction tests that genuine witnesses are accepted. The capped run completed in 59 nodes with no candidate, and the positive collision control passed. The count-21 coverage audit passed. The next count, 22, produced genuine counterexamples to universal injectivity, and its accepting cover also passed the independent implementation audit. Independent model review remains pending.

**An everyday picture.** Search a route map, stopping at each fork whose remaining distance cannot reach the destination. Only covering every fork certifies that no route reaches it.

## G89
Two starts can meet while both satisfy the prefix growth-factor condition: universal injectivity is false.

**What it says.** The starts 5348744187 and 5348744191 meet at 9770112830 after 34 steps. Each has 22 odd steps and keeps its tripling-and-halving multiplier at least one at every prefix. Their exact words, offsets and direct trajectories verify the meeting. Adding the same multiple of 2^34 to both starts produces another such pair.

**Why it matters.** It answers the singleton question with a counterexample and makes the two-member fibre bound sharp. The smaller odd counts are excluded by the preceding argument and audited finite cover. The accepting-cover audit confirms exactly five residue families at count 22, with first meetings at step 34, pending independent model review. It does not refute Collatz or solve either prize problem. The no-collision prediction failed and is retained.

**An everyday picture.** Two routes can reach the same destination without either spending its accumulated travel budget; knowing the destination alone cannot distinguish the routes.

## G90
Meeting at the same terminal value does not make two starts cancel in the weighted count error.

**What it says.** Choose a meeting pair from W89 at width 34. Just before the last step, one start needs an odd step to pass the growth-factor barrier, while the other already has enough odd steps. Their fair-coin continuation weights are one half and one. Both actually survive, so their individual weighted changes sum to a positive half rather than zero.

**Why it matters.** Terminal pooling cannot supply the missing signed cancellation merely because two trajectories meet. This selected-pair example does not estimate the full population error. It returns the collision insight to the open weighted-bias question. The preregistered two-trajectory control passed, including the unequal penultimate-class guard. Independent model review remains pending.

**An everyday picture.** Two travellers reach the same destination, but only one used the last coin toss to clear a toll. Sharing a destination does not balance their different budgets.


## G91
Matching inputs that merge with the same odd-count label replaces demand weights by their adjacent difference.

**What it says.** Pair an odd parent with an even parent when their next states and next odd counts agree. Their two contributions combine into half the difference of two neighbouring backward demand weights. Unmatched occurrences retain their original contributions, including even steps that fail the barrier.

**Why it matters.** The reviewed coin curvature bound can control a matched pair away from the final horizon. It does not bound how many pairs or unmatched inputs occur. The exact identity improves the terminal-pooling question without assuming full cancellation. The small controls passed 100 exact increments and the true-pair, synthetic multiplicity and lost-child guards. Independent model review remains pending.

**An everyday picture.** Some travellers can share the next checkpoint, but their different toll weights leave a small difference. Unpaired travellers and those denied entry still belong in the accounting.


## G92
A coarse maximum-curvature bound still cannot close the constant count estimate by itself.

**What it says.** Grant that unmatched inputs cancel completely, and bound all matched pairs by the largest available curvature bound. Replacing the matched count by half the survivor count leaves a coefficient growing at least as the logarithm of the paid tail. This is growth of the estimate's right-hand side, not of the actual error.

**Why it matters.** Matching improves the old square-root obstruction but needs actual allocation or signed information to become a global result. An exact pair has zero meeting-step contribution at a slightly longer horizon despite a positive bound, demonstrating the distinction. Independent review remains pending.

**An everyday picture.** Charging every paired traveller the largest possible toll overestimates the total even when some actual tolls are zero. The improved price cap alone does not settle the bill.


## G94
An induction proof for demand log-concavity must control the absorbing edge separately.

**What it says.** Away from the barrier, demand atoms undergo ordinary two-point averaging, which preserves log-concavity. At the edge an extra half of the first atom stays there. One explicit inequality among the first four future atoms is necessary and sufficient to preserve log-concavity when the future law is already log-concave.

**Why it matters.** A uniform four-atom synthetic law fails this edge inequality, so generic log-concavity cannot complete the proof. That example is synthetic, but Local's second reading then checked the real barrier schedule: the edge inequality holds up to horizon 64 and fails from 65 on (first at horizon 73), so the real demand law is not always log-concave. It breaks only at this edge, never in the interior, up to horizon 1,024.

**An everyday picture.** Averaging keeps a smooth pile smooth until material hits a wall and accumulates at its edge. That extra pile needs its own check, and on the real schedule it sometimes makes a small bump.

## G95
The actual barrier has no consecutive flat steps; unrestricted fair-bit barriers can fail log-concavity.

**What it says.** The threshold rises at least once in every two steps. A different schedule, 00011, has demand atoms 26/32, 5/32 and 1/32, which are not log-concave. That schedule falls outside the actual restriction.

**Why it matters.** A candidate statement was log-concavity for all schedules without adjacent flat steps. Local’s actual-schedule counterexample in L048 refutes that general statement. The pending finite family search is stopped before execution; the elementary schedule property and unrestricted guard remain valid. Independent review of those statements remains pending. The actual count error would still need signed allocation control.

**An everyday picture.** A staircase with no long landings may keep a demand profile smoother, but the shape must be proved; a staircase with a long landing already gives a counterexample.


## G96
Changing a fixed cell and following a moving pattern measure different things.

**What it says.** A difference taken along a constant-speed worldline vanishes on an exactly translating pattern, while a fixed-cell difference need not. Rule30 can be expressed in that moving frame by shifting its update. Its fixed-cell XOR change equals Rule210 evaluated on the state; the resulting change field does not itself evolve by Rule210, as a single-cell example shows.

**Why it matters.** The owner's shader-to-temporal-instrument connection needs a precise choice of observable. A passing pulse can have a nonzero fixed-cell second difference despite zero acceleration of its tracked position. These are scope identities and examples, not a Rule30 travelling-wave, prize or physical instrument claim. Small controls pass on 504 ring rows, 1512 transported cases and 168 dyadic checks; independent review remains pending.

**An everyday picture.** A lamp moving steadily past a window changes what the window sees. Following the lamp separates that change from a change in its speed.

## G97
A moving observer's expected flip rate can be derived without independent flips in time.

**What it says.** Rule30 preserves the iid fair spatial row law by a direct four-preimage count. For a predetermined observer stepping left, staying or stepping right, the flip probabilities are respectively one half, one half and three quarters. Expected counts add even if flips in time are dependent.

**Why it matters.** It supplies the ensemble prediction behind Local's moving-frame measurements with explicit assumptions. It does not prove a single-seed frequency, temporal independence, concentration or a standard error. SC1-SC2 controls pass. A further fresh-left-bit proof gives independent sampled values and flips for deterministic observers that never step right, under the same random-row ensemble; its SC3 controls pass on 30 observer paths and 9360 initial words; independent review remains pending. No independence is asserted for rightward observers or a selected seed.

**An everyday picture.** Knowing the average number of heads does not tell you whether successive tosses are related.

## G98
Changing a global clock, changing update order and counting cone events are different operations.

**What it says.** Relabelling synchronous tick durations preserves the ordered state sequence. A constant-speed continuum diamond has a computable area, while integer-event counts include boundary corrections. A single seed propagates left at speed one, refuting a universal interpretation of the measured 0.246 front. Two adjacent in-place updates can give different results in reverse order.

**Why it matters.** It gives precise statements for the owner's clock questions without promoting a geometric analogy to physical dilation or a complexity lower bound. Tiny guard controls and independent review remain pending.

**An everyday picture.** Playing a film slowly changes its timing; rearranging its frames changes its story. Counting pixels also differs from measuring the area of their boundary.

## G99
A shared logical generation can survive unequal physical update times.

**What it says.** Store immutable values labelled by site and generation. Any complete schedule that computes a node only after its three prior-generation parents gives the synchronous history's values. An intermediate mixture of generations is not necessarily a synchronous frame.

**Why it matters.** It identifies the buffering and dependency assumptions needed to answer the owner's local-clock question. It claims neither a physical metric nor an algorithmic speedup. Small controls pass on 680 initial words and two schedules; independent review remains pending.

**An everyday picture.** Cooks can prepare different ingredients at different times, provided each recipe uses the specified versions and the finished dish includes every required ingredient.

## G100
Two neighbouring flips can look independent while a third exposes memory.

**What it says.** For a right-step observer in Rule30 started from a fair random row, adjacent flips have zero covariance, but flips two steps apart have covariance1/32. Three-flip counts have variance5/8 rather than the independent prediction9/16.

**Why it matters.** It supplies an exact temporal-dependence guard for the ensemble behind moving-frame expectations. It covers the right-edge speed and three ticks, not interior-ray or single-seed asymptotics. Tiny controls pass on all 64 six-bit words with both origin bits and independent formulations; colleague review remains pending.

**An everyday picture.** Checking two neighbours does not reveal every way a sequence can remember its past.

## G101
Temporal memory also appears in an interior moving frame.

**What it says.** A speed-three-quarter observer repeats stay/right/right/right. Under a fair random initial row, the second and fourth flips in each aligned block have covariance1/32. The four-flip count variance is7/8 rather than the independent prediction13/16.

**Why it matters.** It extends the exact right-edge guard to an interior ray without rerunning long measurements. Distinct blocks need not be independent, and the selected seed or long-run variance remains unproved. Small controls pass on all 512 initial words and all pair covariances; colleague review remains pending.

**An everyday picture.** A slower route can still contain short stretches that carry the same memory as a fast route.

## G102
A raced neighbour can carry an extra race into the next update.

**What it says.** On a fair initial row, isolated right races inject with probability1/8. An open-boundary chain model gives bulk conditional probability1/(8-4*eps), with an exact finite-depth remainder. Finite left chains retain probability1/2.

**Why it matters.** It separates an exact isolated event from the sequential mechanism used in Local's rare-race measurements. The correction is small for rare races; it supplies no later-time survival law or cyclic-boundary identity. Controls pass on 43680 word/flag combinations and48 exact weighted checks; colleague review remains pending.

**An everyday picture.** Reading from someone who has already read an altered value can pass along an extra change.

## G103
A race-free dependency cone guarantees the cell follows the ideal history.

**What it says.** With independent race flags, a target cell's disagreement probability is at most1-(1-eps)^(t²). With only marginal flag bounds, it is at most eps*t². A fixed mean disagreement threshold therefore cannot arrive on a scale smaller than order eps^(-1/2).

**Why it matters.** It gives a rigorous constraint without fair-state or effective damage-speed assumptions. It supplies no matching upper bound, exact survival constant or realised hitting-time guarantee. Snapshot reads at unflagged nodes are required. Controls pass on 77440 histories and192 exact weighted site bounds; colleague review remains pending.

**An everyday picture.** If every ingredient in a recipe's dependency chain is unchanged, the final dish is unchanged too.

## G104
One race direction preserves fair spatial rows; the other can hide changed pairs behind fair density.

**What it says.** The infinite right-reading model preserves the fair product law via a conditional block inverse. On a fair input row, the left-reading model retains density1/2 but gives adjacent disagreement1/2+eps/4.

**Why it matters.** It earns a right-bulk extension of the injection calculation to later noisy rows, while leaving ideal-history disagreement separate. The left result is first-step only. No exact finite-ring or selected-seed law is claimed. Controls pass on2720 right cases,10880 left cases and48 exact weighted moments; independent review remains pending.

**An everyday picture.** Two patterns can contain the same number of black cells but arrange neighbouring cells differently.

## G105
Closing the row into a ring changes an exact probability even when large-ring statistics look fair.

**What it says.** Every right flag pattern gives exactly two preimages of the zero row. Left patterns give one or two according to whether any effective race is present. The resulting zero-row probabilities differ from the uniform ring law.

**Why it matters.** Infinite fair spatial invariance cannot be imported as exact finite cyclic invariance. The all-zero initial row also blocks any state-uniform upper decoherence bound. ZR1 passes43648 cases and40 exact weighted probabilities; independent review is pending.

**An everyday picture.** Joining the ends of a chain removes the free end used to reconstruct it.

## G106
The snapshots can stay statistically unchanged while motion through them changes.

**What it says.** In the infinite fair right-reading race model, an observer stepping left or staying has flip mean1/2. Stepping right has mean(3-eps)/(4-2eps), increasing from3/4 despite unchanged fair spatial rows.

**Why it matters.** Spatial invariance does not preserve the transition law. The moving-path count mean follows, but temporal independence, variance and ideal-history survival remain open. TF1 passes43648 cases and60 exact weighted means; colleague review is pending.

**An everyday picture.** Two films can have the same distribution of individual frames but different motion between them.

## G107
A trace moving left or staying put keeps meeting a fresh random bit, even through right-reading races.

**What it says.** For a predetermined nonrightward path, samples and XOR flips remain iid fair conditional on any terminating state-independent right-race schedule. Flip-count mean and variance are N/2,N/4.

**Why it matters.** Such a single trace cannot statistically reveal the schedule in the fair infinite ensemble, although paired noisy/ideal traces may differ. Rightward, adaptive, finite-ring and selected-seed observations are excluded. NT1 passes135296 cases and8736 conditional bijections; review is pending.

**An everyday picture.** A new fair coin can hide each next observation without making two copies of the film agree.

## G108
Two individually random traces can remain perfectly related when their shared environment is known.

**What it says.** Conditional on the other initial bits and race schedule, noisy samples equal ideal samples XOR a mask determined by earlier ideal samples. The transformation is a causal bijection, with N+1 bits of conditional mutual information.

**Why it matters.** Marginal iid observations do not make two histories independent. First-tick race errors depend on the previous sampled state. This representation does not determine the error process or a decoherence rate. CT1 passes135296 paired cases and8736 conditional classes; review is pending.

**An everyday picture.** Knowing the key can relate two scrambled films even when each looks random on its own.

## G109
An isolated race error can disappear at its source and return without another race.

**What it says.** A right-race injection forces a black ideal right neighbour. The original source's disagreement on the first three ticks is1,0,1. Its second-tick damage has moved elsewhere.

**Why it matters.** Healing at one cell is not coalescence or permanent recovery. This is a local arbitrary-background identity, not a repeated-race survival law. EH1-EH2 pass160 cases with an independent damage equation; review is pending.

**An everyday picture.** An echo can return after the place where it began has fallen quiet.

## G110
Two individually memoryless traces can form a pair with memory.

**What it says.** In the isolated-pulse model, current ideal bit and current error miss the healed error that will return next tick. The previous error determines that return, refuting a first-order Markov state even with known pulse phase.

**Why it matters.** The error-mask coupling needs more than marginal fairness or a current-bit state. This identifies a pulse control for conditional-memory measurements, not a claim about repeated independent races. PM1 passes128 words with exact conditional counts; review is pending.

**An everyday picture.** Two streams can each sound random while their relationship remembers yesterday.

## G111
An exact split at one rate can certify memory at almost every rate; equality at one rate cannot certify closure.

**What it says.** Finite Bernoulli histories give polynomial conditional-split determinants. A nonzero half-rate witness in the W5,T3 table would persist except at at most19 interior rates, including a sufficiently small positive-rate interval.

**Why it matters.** This can extend a finite-ring witness without rerunning a rate sweep. Local subsequently supplied a deterministic-bin witness, whose positive/zero support proves finite-ring memory at every interior rate. One small toy still shows why half-rate equality can hide quarter-rate failure. PC1-PC3 pass12 independent exact checks; reviewed by Local L067.

**An everyday picture.** A curve crossing zero once is different from a curve that stays zero everywhere.

## G112
Two shared black observations force the next source samples to agree in the right-reading coupling.

**What it says.** Starting from a shared row, a shared white first-step right neighbour forces agreement immediately to its left. Two shared black source observations then shield the next update.

**Why it matters.** Finite positive-probability cylinders turn that local identity into a proposed infinite-line first-order Markov counterexample for every interior rate. WH1-WH3 pass672 effective cases, two cylinder controls and an orientation guard; independently reviewed by Local L069; no claim about higher memory orders or survival follows.

**An everyday picture.** Today's matching signal can conceal yesterday's influence on tomorrow's error.

## G113
Keeping one previous paired observation still misses pulse-model memory.

**What it says.** In the isolated-pulse fair-input ensemble, one positive last-two-state bin has next-error rate5/234, but its refinement by an earlier observation has rate0. The zero child has no original injection; the positive parent now has an explicit13-bit cylinder, independently checked under all eight nearest-exterior assignments.

**Why it matters.** This refutes order-two Markov at tick5 for this specific ensemble. All8192 words were checked with two update formulations; both separate seven-sample marginals remain uniform. Independently reviewed by Local L070; no all-orders or repeated-race theorem follows.

**An everyday picture.** Remembering yesterday as well as today can still miss an older cause.

## G114
Two incoming errors can cancel at a healed white source.

**What it says.** At a shared white centre, next synchronous error is the XOR of the two neighbour errors; at a shared black centre only the left error passes.

**Why it matters.** G113's two healed ticks hide equal incoming errors, followed by one uncancelled error. The full damage rule includes a nonlinear mixed term; it is not autonomous Rule90. DP0-DP2 pass64 local identities, cone rows and the autonomous-Rule90 guard; independently reviewed by Local L071.

**An everyday picture.** Two opposing disturbances can hide each other without disappearing.

## G115
Remembering the injection and one lag still misses older observed information.

**What it says.** In the pulse model a candidate state containing the injection indicator and last two paired observations has next-error rate1/2, while a positive full-history refinement has rate0.

**Why it matters.** The immediately earlier observation finds no split, yet the full observed past gives24. A shallow held diagnostic can falsely suggest closure. All8192 cone words were checked; independent review is pending. No repeated-race or all-orders claim.

**An everyday picture.** Remembering the incident and yesterday can still miss an older clue.

## G116
The fourth isolated-pulse error remembers parity of three earlier ideal samples.

**What it says.** E4 equals the injection indicator times I1 XOR I2 XOR I3. The local proof follows fixed neighbouring values forced by the001 injection.

**Why it matters.** Among injected fair histories, the last two ideal samples give fourth-error probability1/2; adding I1 makes it deterministic. This explains how shallow averaging can hide older information. PE0-PE2 pass512 words and the shallow-average guard;review pending. No repeated-race or physical-derivative law.

**An everyday picture.** Two remembered bits can hide the parity clue carried by a third.

## G117
An unobserved initial right-tail bit enters the fifth pulse error.

**What it says.** D=x3 AND(x4 OR x5) is independent of the injected ideal prefix and has rate3/8. An explicit Boolean kernel maps that prefix and D to E5.

**Why it matters.** Complete observed source history can leave positive next-error uncertainty even after racing stops. The proposed exact law gives P(E5=1)=19/256 and conditional entropy h2(3/8)/16 bits. FT0-FT2 pass2048 histories and the identical-past/different-future guard;reviewed by Local L073. Not an entropy rate or repeated-race law.

**An everyday picture.** A past disturbance can expose information from somewhere the observer never watched.

## G118
Exact six-sample mutual information separates conditional and unconditional coupling.

**What it says.** In the isolated-pulse model joint entropy is6+h2(1/4)/2+h2(3/8)/16 bits;mutual information is6 minus the same two uncertainty terms.

**Why it matters.** Each marginal is iid fair, yet hidden initial bits add joint uncertainty. Injection depends on the first observed bit, so unconditional injection entropy cannot replace conditional entropy. JI0-JI2 pass2048 words and exact count spectrum;reviewed by Local L074. No entropy-rate law.

**An everyday picture.** Two random-looking signals share most information, while an unseen input supplies the rest.

## W119
A common fresh bit ties new shared information to next-error uncertainty.

**What it says.** On a predetermined nonrightward path in the fair right-reading model,MI grows by1-H(next error|paired past) bits per sample.

**Why it matters.** This connects hidden-error uncertainty to unconditional information growth without assuming error closure. Two iid marginal traces alone do not suffice:cross-copy reuse gives a two-bit increment. GF0-GF2 pass32 positive histories and8 scope guards;review pending. No asymptotic rate.

**An everyday picture.** A new common bit shares what an uncertain discrepancy leaves visible.

## W120
An observed rare injection limits later information loss.

**What it says.** After the pulse indicator is observed,error uncertainty is at most1/8 bit per later sample,so shared information grows by at least7/8 bit.

**Why it matters.** This yields a liminf lower bound7/8 without assuming a rate limit exists. It includes histories with no injection and does not bound active damage lifetime. A hidden-event guard checks why rarity alone is insufficient. RB0-RB2 NOT RUN;review pending.

**An everyday picture.** Knowing which rare branch occurred removes uncertainty that its probability alone cannot remove.
