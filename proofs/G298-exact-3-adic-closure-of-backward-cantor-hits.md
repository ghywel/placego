# Exact 3-adic closure of backward Cantor hits and mixed terminal states

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT298. Exact 3-adic closure of
backward Cantor hits and mixed terminal states (second-read by Local, 2026-10-15)"; rebuild with `python3
proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

Every base-3 ending whose last nonzero digit is 1 is shared by infinitely many numbers that, multiplied by some
power of 4, have no digit 2.

**What it says.** In base 3 (counting in 1s, 3s, 9s, 27s and so on), 64 is 2101 and 256, four times 64, is 100111.
Numbers like 64, which times some power of 4 have no 2, never have 2 as their last nonzero digit, yet every ending
whose last nonzero digit is 1 is shared by infinitely many of them. A set that holds 4n whenever it holds n, and has
a 2 in every member, can hold none of them; if it also holds a number ending in 1, that number times 1, 4, 16, ...
gives it members with every ending that finishes in 1, so no such ending tells members from non-members. A machine
with a fixed number of settings, reading from the last digit back, can therefore pick out such a set only if every
group of settings it can reach after a last digit 1, and never leave, holds both yes and no settings.

**Why it matters.** Such a machine whose set held 1024 would prove what the mathematician Paul Erdős expected: that
256 is the last power of 2 written in base 3 without a 2. This is only a test any such machine must pass; it does
not show whether one exists, and Erdős's question stays open. Passing is not enough: the set of numbers that end in
1 and start with 2 passes, yet holds 64 but not 256, four times 64.

**An everyday picture.** A doorman reads each ticket number from the right-hand end. If every ending, however long,
turns up on both real tickets and fakes, he cannot wave anyone in or turn anyone away before he reaches the
left-hand end, however good his notes.

## The formal statement and proof

**PROVED, Local L733 at8a2aff86.** Promoted in GC1263. The original proof and independent review below are
retained verbatim; PROOF-SKETCH and review-request labels in them are historical. Former waiting-room heading:
GPT G298, GC1262, 2026-10-15 12:22 BST. This is a necessary DFA condition, not K2-prime or Erdős proved.

**Status:** PROOF-SKETCH; independent carrying read requested. Let C-star be the positive integers with only
ternary digits 0 and 1, and B-star={n>=1 : 4^j n belongs to C-star for some j>=0}. Let H consist of zero and the
3-adic integers whose lowest nonzero ternary digit is 1. Then the closure of B-star in Z_3 is exactly H.
Every residue ball in H away from zero contains infinitely many elements of B-star.

**Construction in a unit ball.** Fix k>=1 and r=1 mod3, viewed modulo 3^k. Powers of4 run through every residue
1 mod3 modulo3^k, so choose j>=0 with 4^j r=1 mod3^k. This generation fact is the existing free-part identity
(CONSTELLATION G.1); it also follows from v3(4^(3^t)-1)=t+1, proved by cubing 1+3^(t+1)u with 3 not dividing u.
Put m=4^j. Choose P>=1 with 3^P=1 mod m (P=1 if j=0). Choose an arbitrarily large positive M satisfying
M=-3^(-k) mod m. The inverse exists because m is a power of2. Define

    y = 1 + sum_(t=0)^(M-1) 3^(k+tP),       n = y / m.

The exponents are distinct and positive, so y is in C-star. Modulo m, the sum is M*3^k, so y=0 mod m and n is a
positive integer in B-star. Modulo3^k, y=1, hence n=4^(-j)=r mod3^k. Increasing M by multiples of m gives
arbitrarily large distinct n in that same ball. This uses the subset-sum congruence observation already in
SW01-OBJECTS proposal5 step3(e); the present claim applies it to the whole backward-hitting set, not a new
method for the original orbit.

**All strata and the closure.** A finite member of C-star has lowest nonzero digit1. Dividing by4^j preserves
that digit and the 3-adic valuation, so B-star is contained in H. The complement of H is open: fixing a finite
prefix through a lowest nonzero digit2 fixes nonmembership. Thus H is closed. For any a>=0, multiply the unit-ball
construction by3^a; this preserves C-star and commutes with4, proving density in the stratum of valuation a
and lowest digit1. Zero is a limit of 3^a in C-star as a increases, but zero itself is not in B-star. These
observations prove both inclusions of the claimed closure.

**Finite-word consequence.** Suppose L is any set of positive integers with 4L subset L, L disjoint from C-star,
and a unit x=1 mod3 in L. Then L is disjoint from B-star, by iterating its forward closure. In each residue ball
r+3^k Z_3 with r=1 mod3 there are infinitely many members of L: choose j with x*4^j=r mod3^k and then increase j
by multiples of 3^(k-1). There are also infinitely many nonmembers, supplied by B-star above. Thus neither
membership nor nonmembership is decided by any fixed low-digit prefix in that stratum. In particular L cannot
be relatively open or relatively closed in the positive-integer subspace there. No regularity is used in this paragraph.

For an LSD-first DFA recognising L on canonical positive numerals, let q be any state reached by a word
beginning with1. Both accepted and rejected canonical words extend that prefix, with arbitrarily large length.
Consequently q has an accepting continuation and a rejecting continuation, each ending with a nonzero digit.
Every terminal strongly connected component reachable after the first1 therefore contains both an accepting
and a rejecting state: all its continuation paths stay inside it. This is a necessary graph condition only.
G297 permits the unit normalization of the seed-free question without changing the fixed state bound; this
corollary makes no state-count claim about the prescribed-seed question.

**Sharp countercontrol.** The regular language of units1 mod3 whose MOST significant digit is2 has both accepted
and rejected extensions after every LSD prefix starting1, and avoids C-star. Yet it is not x4-closed:64=(2101)_3
is in it, whereas4*64=256=(100111)_3 is not. Thus density, regularity and the mixed-component condition do not
settle K2-prime. The missing inference is a contradiction from universal x4 closure together with such finite
terminal structure, or an explicit automaton satisfying both. This result does not supply that inference.

**Controls and scope.** tests/probes/swarm/erdos_gpt_cylinder.py had predictions before its first execution;
40 separated-digit constructions,160 valuation lifts, seven unit-group controls and the independent205->820
example pass. Unexpected zero check: zero belongs to the closure only. The regular-language countercontrol fails
closure as predicted. These are small controls of the written argument, not an enumeration of automata or
proof of Erdős. The modular construction and terminal-component implication are the carrying steps to review.

Filing check: proof_dupes --near W298 passes. Nearest G297, G68 and G191 read: G297 is the unit normalization
used here; G68 concerns Collatz endpoint congruences, and G191 involutive graph path periods. This extends G297
with a backward-hitting closure calculation and its DFA consequence; it restates none of those full claims.

**Independent carrying second read (Local, L733, 2026-10-15 12:25 BST). VERIFIED.** Each step was checked:
- *Generation.* By lifting the exponent, v_3(4^n - 1) = 1 + v_3(n), so 4 has order 3^(k-1) mod 3^k, the size of the
  subgroup 1 mod 3; j with 4^j r = 1 mod 3^k exists.
- *The construction.* With m = 4^j, P the order of 3 mod m, and M = -3^(-k) mod m, the sum gives y = 1 + M 3^k = 0
  mod m, since 3^(k+tP) = 3^k mod m; y = 1 mod 3^k, so n = y/m = 4^(-j) = r mod 3^k. The exponents 0 and k + tP are
  distinct, so y is in C-star, and M can grow by multiples of m.
- *The inclusion.* B-star is in H: a finite member of C-star has lowest nonzero digit 1, and dividing by 4^j keeps
  the valuation and the lowest digit, since 4 = 1 mod 3.
- *Closedness and density.* H is closed, because a lowest digit 2 is fixed by a finite prefix. Scaling by 3^a gives
  density in every stratum. Zero is a limit point only.
- *The finite-word consequence.* L meets no member of B-star (iterate 4L subset L). It has infinitely many members in
  each ball r + 3^k Z_3, r = 1 mod 3: x 4^j for j in a residue class mod 3^(k-1), distinct as integers. A number of
  the ball at least 3^k has the prefix's k digits as its lowest digits, so both accepted and rejected canonical words
  extend any LSD prefix that begins with 1.
- *The terminal-component step.* The end state of an accepted (rejected) continuation from a state in a terminal
  component lies in that component and is (is not) in F.
- *The countercontrol* (units 1 mod 3 with most significant digit 2; 64 = (2101)_3 in it, 256 = (100111)_3 not) is
  correct.

Status: PROVED (a proof with a second reader), as a necessary condition only, as stated. Not used to constrain the
registered SAT runs.
