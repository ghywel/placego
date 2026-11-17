# A two-block decoder carries visible cuts into physical middle parities

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT291. A two-block decoder carries
visible cuts into physical middle parities (second-read by Local, 2026-10-13)"; rebuild with `python3
proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

Inside the left half, whether two neighbouring counts come out odd or even spells out one bit that the middle column
hears from the right.

**What it says.** Suppose the middle column blinks black and white, and the left half's starting row has a long
white stretch that begins, just after a black square, at least eight squares out. Slanting lines run inward from the
white triangle it makes toward the middle column, one for each white beat. Give each line a reading: away from its
two ends, count the spots where two white squares side by side appear or disappear between that line and the next,
and write 1 if the count is odd, 0 if it is even. From the fifth line on, provided the stretch is long enough and
the blinking keeps going a few ticks beyond the next line, the known fact that the middle never hears two 1s in a
row gives this: the middle hears a 1 at a line's white beat exactly when that line reads 1 and the next reads 0, so
N neighbouring lines give N − 1 heard bits. Apart from the ends this translation loses nothing either way, and a
proven ban on a run of heard bits, kept with its own side conditions, becomes a ban on a window of readings one
longer: never five heard 0s in a row becomes never four 0s in a row.

**Why it matters.** It carries what is known about the heard bits into the inside of the left half, on lines that
reach ever deeper. But a translation that loses nothing is a new way to read the same information, not a new
obstacle: it puts no limit on how long the white stretch can be, and does not show that the blinking must break.

**An everyday picture.** A church clock striking the hour: you only know a stroke was the last when the next beat
stays silent. Likewise, the middle hears a 1 exactly where a run of 1s among the readings ends, which shows once the
next line reads 0.

## The formal statement and proof

**PROVED, Local L692 at39d3ca1d.** Source: RULE30-GPT.md GC1207, retaining G290's actual origin and source paths. For d>=8,a>=4,k=d+2a+e, with k+5<=E and the actual clock through k+5, no11 implies q(k-1)=M_a(1-M_(a+1)). If q(k-1)=1 the two parities are10; if it is0, a first parity1 forces the next parity1. Hence N actual middle parities recover N-1 visible samples, with a necessary one-parity endpoint loss.

Formal middle words avoid111/0010; decoding any such two-sided word and re-encoding is identity. Actual no00000 additionally forbids middle0000. A sound length-r visible cut tests r decoded products in an r+1 parity window, retaining its phase and origin requirements. This is a finite word guard on the joint physical sources, not an entropy payment, closed hidden update or record bound. GC1207 gives the local reverse-consistency calculation and registered Boolean controls, with its failed fixture endpoint expectation retained.


L692 checks both decoder cases, the k+5 endpoint, local reverse consistency, the four-zero equivalence and the retained fixture correction by hand.
