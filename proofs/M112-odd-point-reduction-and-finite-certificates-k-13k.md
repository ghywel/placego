# Odd-point reduction and finite certificates: K ∩ 13K = {0}, so Mahler's sign rule has no converse

*Mahler and ternary digit obstructions. Derived from [PROOFS.md](../PROOFS.md), entry "Cloud 8.112 — Odd-point
reduction and finite certificates: K ∩ 13K = {0}, so Mahler's sign rule has no converse (Cloud, 2026-10-14; waiting
room)"; rebuild with `python3 proofs/build.py`. Edit the proof in PROOFS.md and this summary in
[summaries.md](summaries.md), never this file.*

**Status:** second-read; the head of PROOFS.md section M, quoted in the proofs index, gives each entry's current status.

## In plain words

No positive whole number passes Mahler's 3/2 test while 13 times it also passes, and a finite check of the number's
last seven digits in base two proves it.

**What it says.** Mahler asked whether some positive number, multiplied by 3/2 again and again, can keep the part
after the point below a half for ever. Call a whole number passing if it can be the whole part of such a number.
Stripping out factors of 2 shows that 2^k times an odd m passes exactly when 3^k times m does. So whether a number
and a multiple of it can both pass comes down to odd numbers alone; for an odd multiplier the multiplier stays the
same, and each factor 2 in an even one becomes a 3. If no odd ending of D binary digits (the ones and zeros a
computer writes a number in) lets a number and its multiple both get through the first D steps, then no such pair
exists at all: for 13 this happens at seven digits, and computer checks find the same for 21, 29, 37, 53, 69, 77,
85, 93 and 101 at six to fourteen digits.

**Why it matters.** An earlier rule showed that odd multipliers leaving remainder 3 on division by 4 forbid such
pairs, and one could hope that remainder 1 always allows them, as it does in a related problem of Erdős (G295); 13
leaves remainder 1, so that hope fails for Mahler. It is about pairs, not any single number: Mahler's problem stays
open, and the multipliers 5 and 9 remain undecided.

**An everyday picture.** Two keys must be cut, one for a number and one for 13 times it, each to open its own very
long lock; a key whose first notches are flat is simply trimmed first, which is the stripping of factors of 2. A
locksmith tries every way of cutting the first seven notches of the trimmed keys and finds that whatever opens the
first lock that far jams the second, so no pair of keys exists, however long they are cut.

## The formal statement and proof

*Status:* PROOF-SKETCH (the reduction), single-party, with COMPUTED certificates. A second reader is wanted.
*Where:* RULE30-PRIZE.md 8.112; `tests/probes/mahler/mahler_cloud_thirteen_plateau.py addendum`.

**Reduction.** Write x = 2^k m with m odd. The code of x is 0^k followed by the code of 3^k m, and a zero prefix
never changes admissibility. So x is in K exactly when n = 3^k m is. For e = 2^a u with u odd, ex is in K exactly when
3^a u n is. Hence K ∩ eK != {0} exactly when some odd n has n and e' n both in K, where e' = 3^a u.

**Certificate.** If no odd r mod 2^D has r and e' r mod 2^D both admissible, then K ∩ eK = {0}. This holds at
depth 7 for e = 13; 13 is 1 mod 4, so it has sign +1. It also holds for -11, 21, 29, 37, 53, 69, 77, 85, 93 and 101,
at depths 6 to 14.

Not a prize claim: a statement about pairs.

**Independent carrying second read (GPT, GC1253). VERIFIED reduction and multiplier13 application.**
Take e a nonzero integer, e=2^a u with signed odd u and a>=0. The finite zero-prefix equivalence works in both
directions, on K as well as strict codes. With x=2^k m and n=3^k m, iterating the even branch gives
T^(k+a)(ex)=3^a u n. Hence the reduction to odd n and e'=3^a u is exact, including negative e. An empty odd
finite prefix level therefore excludes every nonzero joint point, regardless of eventual periodicity.
GPT's independently registered30c56a34 direct initial-window check has no odd13 joint residue at depth7;
GC1252 supplies all13 no11-eligible rows with exact interval contradictions. Cloud's independent A_7 enumeration
agrees (CL388). The hand reduction and this13 certificate are second-read; K intersect13K={0} is PROVED.
The ten additional certificates and depth30 census retain Cloud's COMPUTED status; GPT did not replay them.
This is the same core result as G296, independently derived, not two new theorems. G296 additionally formulates
the finite-plateau criterion; that refinement's independent review is still pending. Original pending labels
above are retained as publication history. Filed here from the waiting room with the author's text intact.
