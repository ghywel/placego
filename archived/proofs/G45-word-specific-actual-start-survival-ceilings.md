# Word-specific actual-start survival ceilings

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT45. Word-specific actual-start
survival ceilings"; rebuild with `python3 proofs/build.py`. Edit the proof in PROOFS.md and this summary in
[summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

For a given step pattern, the numbers that follow it and stay above their start are a fixed class with a height limit.

**What it says.** All numbers that follow a given pattern of odd and even steps share one remainder modulo a power
of 2. If the pattern's growth factor dips below 1, such a number can still stay at or above its start, but only if
it is small: below a ceiling the pattern fixes exactly.

**Why it matters.** It separates two notions the count uses: "the growth factor stays above 1" and "the number
actually stays above its start". They differ only for small numbers, below the ceilings.

**An everyday picture.** A soft-play area with a height bar at the door: only children under the bar get in, and the
bar is set by the play area, not by the child.

## The formal statement and proof

**Where:** RULE30-GPT.md G45, 2026-10-06; copied verbatim. **Bears on:** PERIOD-TWO.md §7 question9, the actual stopping-time count. **Status:** analytic derivation, second-read by Local, 2026-10-06 (note below); GPT's own preregistered controls had not run at publication.

### G45 theorem and proof: actual-start survival is a residue class cut by a ceiling

Fix a binary parity word w of lengthT>=1. Let a_t count its ones in the first t positions and define B_0=0. Reading the bit b at positiont, update

    B_(t+1)=3^b*B_t+b*2^t.

The usual affine iteration gives n_t=(3^a_t*n+B_t)/2^t for a start n realizing this word. Its realizing starts form the residue class

    n = r_w modulo2^T,
    r_w = -B_T*(3^a_T)^(-1) modulo2^T.

This is the known parity bijection. To see the congruence characterization directly, necessity follows from integrality of n_T. Conversely the congruence propagates to each prefix by reducing modulo2^t: B_T is3^(a_T-a_t)*B_t modulo2^t, so the prefix affine expressions are integers. At each step integrality of the next expression forces the prescribed parity; induction gives the word. The inverse exists because3^a_T is odd.

Actual survival throughT means n_t>=n for every1<=t<=T. If3^a_t>2^t, this condition holds automatically for positive n, since B_t>=0. Equality is impossible for t>=1 by unique prime factorisation. At a deficient prefix3^a_t<2^t, it is equivalent to

    n <= floor(B_t/(2^t-3^a_t)).

Define K_w to be the minimum of these integer ceilings over deficient prefixes, or infinity if there are none. Then the positive starts realizing w and surviving throughT are exactly

    n congruent to r_w modulo2^T, with1<=n<=K_w.

For w-bit starts put L=2^(w-1), U=min(2^w-1,K_w). The exact count for this word is0 if U<L, otherwise

    floor((U-r_w)/2^T)-floor((L-1-r_w)/2^T).

Summing over all lengthT words gives the actual-start survivor count, with no population identified with coefficient survivors by assumption. Words whose coefficient barrier survives have K_w=infinity. Every other word has a finite ceiling, so its actual-survival exceptions are restricted to small starts relative to that particular word. No bound on these ceilings uniform over word length has been proved here.

**Unexpected analytic scope check.** The word1010 has B_4=7,a_4=2 and deficient final coefficient9/16. Its ceiling is K=1 and its residue is1 modulo16. The positive start1 follows the cycle1,2,1,2,1 and stays at or above its start, although its coefficient barrier already fails at step2, where3/4<1. Thus the two notions are not universally equal. This does not challenge their recorded agreement for starts of20 to32 bits.

**What remains.** The formula isolates two contributions: coefficient-admissible residues, and bounded-start exceptions from words with a coefficient deficit. It is an exact finite enumeration identity, not a better bound on either contribution. Both depend on the specific words and realizing residue classes. The generic all-cylinder mixing failure in G44 does not settle their sum. The affine mechanism is established parity machinery; no novelty claim.

*Second reader's note on G45 (Local, 2026-10-06; chat L012).* Correct. The update $B_{t+1} = 3^b B_t + b\,2^t$ is the
affine iteration; the converse of the residue-class statement follows from $B_T \equiv 3^{a_T - a_t} B_t \pmod{2^t}$
(every later term carries a factor $2^s$ with $s \ge t$) and the oddness of 3; survival at a deficient prefix is
exactly $n \le \lfloor B_t / (2^t - 3^{a_t}) \rfloor$; the counting formula is the standard count of a residue class
in an interval; the example 1010 ($B_4 = 7$, $K = 1$, $r = 1$; the orbit $1, 2, 1, 2, 1$) checks. Independently, the
sum of the formula over all words equals a brute-force count of actual survivors (iterates $\ge n$ through $T$
steps) for every $w = 1$ to 12 and $T = 1$ to 14: 168 cases, zero failures (`collatz_audit_g39_g42.py`, G45 part).
