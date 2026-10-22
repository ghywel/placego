# One finite Mahler joint plateau forces zero; multiplier13

*The waiting room (not yet verified). Derived from [PROOFS.md](../PROOFS.md), entry "GPT G296 — One finite Mahler
joint plateau forces zero; multiplier13 (2026-10-14 22:18 BST; waiting room, GC1252)"; rebuild with `python3
proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** in the waiting room: stated with a proof, not yet checked by a second reader.

## In plain words

No whole number except 0 passes Mahler's 3/2 test together with 13 times itself, and a count that stops growing just
once is enough to prove it.

**What it says.** Mahler asked whether some positive number, multiplied by 3/2 again and again, can keep the part
after the decimal point below a half for ever. A whole number passes the test if some fraction below a half, added
to it, does this; that depends only on which numbers are odd in the chain made from it by "times 3/2, rounded up",
and its last n binary digits settle the first n of those. For an odd multiplier, list the n-digit endings that let a
number and its multiple both pass n steps: the even endings match the previous list one for one, so the list grows
by exactly the number of its odd endings, and any passing pair other than 0, once its chain reaches an odd number,
would put an odd ending on every list. So one length with no growth rules out every such pair, and 13 has one: its
list has 11 endings at both six and seven digits, and exact fractions confirm that no odd seven-digit ending
survives.

**Why it matters.** An earlier result showed that multipliers leaving remainder 3 on division by 4 forbid such
pairs, and it had been proposed that remainder 1 always allows them; 13 leaves remainder 1, so that proposal is
false. When the count stalls, a finite check settles an endless question, with no guessing about longer lengths. It
is about pairs, not any single number: if numbers of Mahler's kind exist, no two have whole parts in the ratio 1 to
13, but his problem stays open, and the multipliers 5 and 9 remain undecided.

**An everyday picture.** A bucket under a tap that might be leaking: no water ever leaves, and the level rises only
when a fresh drop (an odd ending) falls, so a leaking tap would raise it between any two looks. Two looks that find
the same level prove the tap is not leaking, with no need to watch it for ever; the water already in the bucket,
like the 11 endings left at every length from six digits on, is old water, not a sign of a leak.

## The formal statement and proof

*Status:* PROOF-SKETCH with an exact finite certificate; independent reader requested.
*Where:* RULE30-GPT.md GC1252; mahler_gpt_joint_extension_review.py thirteen, registered30c56a34.
Filing check: proof_dupes --near W296 passes; nearest G51,C7,G294 read. G51 supplies the window certificate,
C7 is the Rule30 affine-column table, and G294 is the Mahler rung equivalence. None states this finite plateau
criterion or the multiplier13 certificate. The original inverse-branch identity is credited to GC1246.


**Claim (PROOF-SKETCH with an exact finite certificate; independent carrying read requested).** Let K be the
closed Mahler admissible set, T(x)=(3x+(x mod2))/2, and A_t its length-t prefix residue set. For an odd integer e put

    F_e(t) = {r mod2^t : r in A_t and er mod2^t in A_t}.

For t>=2, the map r ->3r/2 mod2^(t-1) is a bijection from the EVEN members of F_e(t) onto F_e(t-1).
If |F_e(t)|=|F_e(t-1)| at any finite t, then K intersect e^(-1)K={0}, and equivalently K intersect eK={0}.
The depth6/depth7 plateau for e=13 supplies such a certificate: both full sets have11 members and the depth7 set
has no odd member. Thus

    K intersect13K = {0},

even though13=1 mod4 has the opposite sign from Cloud8.110's sufficient exclusion rule. The proposed universal
Mahler sign-plus converse is false. This is a pair-set exclusion, not a Mahler Z-number proof.

**Even-prefix bijection.** Prepending a0 to a parity code preserves admissibility. Removing a leading0 does too:
its fractional tail at age0 is2/3 times the shifted tail. These facts hold for finite valid windows, and for K
by shift continuity and closure. For even r, T(r)=3r/2. Since e is odd, er is even and T(er)=eT(r). Multiplication
by3 makes r ->3r/2 a bijection between the even residues modulo2^t and all residues modulo2^(t-1). The two
admissibility conditions are preserved in both directions, so it restricts to the stated joint-set bijection.
Consequently

    |F_e(t)| - |F_e(t-1)| = number of ODD members of F_e(t).

**Why one plateau is decisive.** A plateau makes the right side zero. Suppose x!=0 and x,ex both lie in K.
Write k=v2(x). Until age k both orbits are even, so

    T^k(x)=(3/2)^k x is odd,    T^k(ex)=e*T^k(x).

Forward invariance of K puts both points in K. Their residues would therefore give an odd member of F_e(t),
a contradiction. This uses a fixed finite cutoff; it does not extrapolate the observed plateau to untested
depths. It also shows that every later finite count stays constant: odd prefixes cannot reappear after an
empty odd level, and the even-prefix bijection then accounts for all later survivors.

**Exact depth7 certificate for13.** A code starting11 anywhere is inadmissible: its fractional tail is at least
5/9>1/2. Among length7 codes starting1, exactly13 avoid11 (the elementary Fibonacci recursion); all13 occur in
the following table. The prefix-code bijection G51 makes this exhaustive for odd residues not already ruled out
by11. Each displayed window is [L,H), hence empty if L>=H. Every row has an empty input or product window.

| r | code(r) | L,H for r | 13r mod128 | product code | L,H for product |
|---|---|---|---|---|---|
| 9 | 1010000 | 13/27, 1/2 | 117 | 1000011 | 889/2187, 97/243 |
| 13 | 1001001 | 1009/2187, 347/729 | 41 | 1010011 | 1213/2187, 1/2 |
| 21 | 1000001 | 793/2187, 275/729 | 17 | 1011101 | 1477/2187, 1/2 |
| 25 | 1010101 | 1261/2187, 1/2 | 69 | 1000111 | 1033/2187, 35/81 |
| 37 | 1000100 | 97/243, 937/2187 | 97 | 1011010 | 455/729, 1/2 |
| 45 | 1001010 | 347/729, 13/27 | 73 | 1010001 | 1117/2187, 1/2 |
| 53 | 1000010 | 275/729, 97/243 | 49 | 1011110 | 503/729, 1/2 |
| 73 | 1010001 | 1117/2187, 1/2 | 53 | 1000010 | 275/729, 97/243 |
| 77 | 1001000 | 35/81, 1009/2187 | 105 | 1010010 | 383/729, 1/2 |
| 85 | 1000000 | 1/3, 793/2187 | 81 | 1011100 | 157/243, 1/2 |
| 89 | 1010100 | 133/243, 1/2 | 5 | 1000110 | 323/729, 35/81 |
| 101 | 1000101 | 937/2187, 35/81 | 33 | 1011011 | 1429/2187, 1/2 |
| 105 | 1010010 | 383/729, 1/2 | 85 | 1000000 | 1/3, 793/2187 |

The window endpoints can be checked by seven rational updates. Starting L=0,H=1/2, set C_0=0 and
C_j=3*C_(j-1)+b_(j-1)*2^(j-1). Intersect the initial window with
[C_j/3^j,(C_j+2^(j-1))/3^j) for j=1..7. This is precisely0<=u_j<1/2 for
u_j=(3^j*u_0-C_j)/2^j; the empty-window verdict uses exact fractions, with no tolerance.
As a second finite check, direct enumeration gives

    F_13(6)={0,4,6,9,16,20,24,30,32,45,56},
    F_13(7)={0,4,6,16,20,30,56,64,80,88,96}.

The second set has no odd member. The full counts are11; Cloud's count9 omits the two finite zero shadows.
The permanent finite survivors are moving shadows of0, not evidence for9 nonzero infinite points.

**Provenance and limits.** Cloud discovered the plateau (CL385-386,8.111,S14). GPT's prior exact inverse-branch
identity (GC1246) supplies the finite-cutoff reduction; GC1251 registered it before the direct13 check.
The13 run uses no Cloud constructor: exact initial-fraction windows, all residues only through8,28 checked
finite even-prefix bijections. The complete table above is a post hoc extraction at that same depth, not a
new blind experiment. The general reduction is a hand argument; the table is an exact finite certificate
awaiting independent verification. No literature priority or prize claim. It does not decide the sign-plus
cases5 or9, and it does not transfer to the nonlinear ternary power map.

**GC1253 reconciliation.** Cloud8.112 was independently derived and supplies the same odd-point reduction and
an independent depth7 enumeration. GPT's carrying read verifies its reduction and13 application; that core is
now PROVED in section M. The general finite-plateau criterion and explicit table are retained here as a refinement
awaiting Cloud's read, rather than counting the same13 theorem twice. Earlier pending labels are historical.
