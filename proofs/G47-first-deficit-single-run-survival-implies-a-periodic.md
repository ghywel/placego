# First-deficit single-run survival implies a periodic return

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT47. First-deficit
single-run survival implies a periodic return"; rebuild with `python3 proofs/build.py`. Edit the proof in PROOFS.md
and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

For those patterns, surviving to the end would mean coming back to exactly the starting number: a cycle.

**What it says.** For the "k odd, then even" patterns, a starting number survives the whole pattern only if it ends
exactly where it began.

**Why it matters.** Surviving through a dip below 1 is then possible only by a cycle, and the only known positive
Collatz cycle is 1, 2, 1. It is a clean link between the count and the cycle question.

**An everyday picture.** A walk that must end at or above home but heads downhill at the end: the only way is to
arrive back at your own front door.

## The formal statement and proof

**Where:** RULE30-GPT.md G47, 2026-10-06; copied verbatim. **Bears on:** PERIOD-TWO.md §7 question9. **Status:** complete analytic argument, second-read by Local, 2026-10-06 (note below); GPT's RC controls published, not run at publication. G46's KC controls passed; G46 argument independently audited by Local L014.

### G47 theorem and proof: this first-deficit family realizes only by a return

Use G46's word1^k followed by j-k zeros, k>=1,j=ceil(k*log2(3)). Put D=2^j-3^k>0 and B=2^(j-k). Any positive start realizing its first k ones has n=2^k*m-1 for a positive integer m, by the exact odd-run identity in G31. After those k odd steps its value is3^k*m-1. Realizing the following j-k zeros requires

    3^k*m-1 = 0 moduloB,
    D*m = -1 moduloB.

The final value is n_j=(3^k*m-1)/B. Since the first segment increases and the even segment decreases, actual survival through this word is equivalent to n_j>=n. Direct subtraction gives

    n_j-n = (B-1-D*m)/B.

The positive integer D*m is congruent to B-1 moduloB, so D*m>=B-1. Survival requires the reverse inequality. Both hold exactly when D*m=B-1, making n_j=n. Therefore there is an actual surviving positive start for this word if and only if

    D divides B-1.

If so it is unique: m=(B-1)/D and n=2^k*m-1. Conversely this value has the prescribed initial odd run and subsequent even run:3^k*m-1=B*n, with n positive odd, so its next j-k parities are zero and its final value is n. All intermediate values are at least n. It lies below2^j and is the single positive representative that can pass the ceiling. Thus this is a genuine periodic return, not a divergent orbit.

At k=1,j=2,D=1,B=2 the criterion gives start1 and the known1,2 cycle. No assertion that this is the only qualifying k for all lengths is proved here. Excluding other positive cycles would require additional reasoning or a precisely audited external result. The criterion is a specialization of G33's known periodic affine formula, sharpened by the monotone shape and first-deficit condition. It does not apply to arbitrary interleaved parity words or bound their actual-survival exceptions. In particular G46's unbounded formal ceilings alone cannot produce nonperiodic exceptions in this specific family.

*Second reader's note on G47 (Local, 2026-10-06; chat L017).* Correct. A start with $k$ initial odd steps is
$n = 2^k m - 1$ and reaches $3^k m - 1$; the $j - k$ even steps need $2^{j-k} \mid 3^k m - 1$, i.e.
$Dm \equiv -1 \pmod B$ since $2^j m \equiv 0$; the path's minimum after the start is its last value, so survival is $n_j \ge n$,
and $n_j - n = (B - 1 - Dm)/B$ forces $Dm = B - 1$; the converse and $n < 2^j$ check. Exact search: for $k = 1$ to
3000 the criterion holds only at $k = 1$ (the cycle $1, 2$), and the candidate start passes a direct test there
(`collatz_audit_g39_g42.py`, G47 part). **A connection that closes G47's open clause by citation, to be audited
against the paper:** a cycle made of one run of odd steps followed by one run of even steps is a *circuit* (a
1-cycle) in R. P. Steiner, "A theorem on the Syracuse problem", Proc. 7th Manitoba Conference on Numerical
Mathematics and Computing (1977), 553 to 559, which proves that the only circuit is the trivial one; Simons and de
Weger (2005) extend this to $m$-cycles for small $m$. Every qualifying member of G47's family is such a circuit, so
with Steiner's theorem $k = 1$ is the only one, for every length. The method (linear forms in logarithms) is
reported in the secondary literature and not yet checked against the paper.
