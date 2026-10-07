# trace factor complexity bounds the number of finite-tail exceptions

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT155. trace factor
complexity bounds the number of finite-tail exceptions (second-read by Local, 2026-10-07)"; rebuild with `python3
proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

There can be only a few finite seeds of each size in the Rudin–Shapiro family, if there are any at all.

**What it says.** A finite seed reaching L squares out is fixed by the first half of that many beats of the column
it makes, so there are no more such seeds than there are different stretches of that length. Rudin–Shapiro has
exactly 8k − 8 different stretches of each length k from 8 on (Allouche and Shallit, 1993), so at most about 4L
seeds reach L squares or less. If one exists, its later rows give about L/2 more.

**Why it matters.** The number of candidates is either zero or grows in proportion to L. That bounds the search but
does not say which, so the question for the original sequence stays open.

**An everyday picture.** A song can be named from its opening notes, so there can be no more songs than different
openings. Counting openings still does not say whether the song exists.

## The formal statement and proof

### G155. Trace factor complexity bounds the number of finite-tail exceptions (2026-10-07)

**Status and target.** Symbolic deduction, independently verified by Local L113; no computation. Uses reviewed G139 inverse locality, G140 coding/radius growth and G154 (Local L112). The record search found G147/G154's exponential fixed-radius count and G139's fixed-depth temporal factor bound, but not this growing-radius exception count. This is an elementary application of substitution factor counting, not a new general complexity theorem. Prediction: Rudin–Shapiro's exception count is at most linear in radius. Counterfactual: temporal zero entropy alone resolves whether there is even one finite-tail exception; the matching conditional lower bound shows the remaining gap.

For a forward-shift-invariant trace family X, let P_X(k) count its length-k factors and N_X(L) count c in X whose compatible initial row Phi(c) has radius at most L. For integers L>=1, put k=ceil(L/2). Then

    N_X(L) <= P_X(k).

**Proof.** G139's inverse recurrence determines the first L initial cells from the visible prefix c_0 through c_(k-1): the physical-time determining window at depth j is [0,j-1], containing exactly ceil(j/2) even samples. Thus two visible words sharing their first k bits have identical initial rows through depth L. If both rows are zero beyond L, the entire rows agree; injectivity of Phi makes the words identical. Hence the exceptional words inject into their length-k prefixes, a subset of X's factors. This also proves Local L112's sharper universal bound 2^k, without assuming that different arbitrary length-k prefixes necessarily produce different length-L rows.

**Rudin–Shapiro bound.** Use G154's four-letter length-two fixed substitution word. For k>=1 choose m minimal with h=2^m>=k; then h<2k. Any length-k factor fits inside two consecutive level-m substituted letters, with its start at one of h offsets in the first. There are at most sixteen ordered letter pairs. Projection to the binary word cannot increase this count, so

    P_(X_r)(k) <= 16*h < 32*k,
    N_(X_r)(L) < 32*ceil(L/2).

This is a deliberately coarse all-length bound, not a claim about the exact known factor complexity. If a finite-tail exception c of radius R exists, its time shifts have distinct radii R+2t. For L>=R this gives

    N_(X_r)(L) >= floor((L-R)/2)+1.

Consequently N_(X_r) is either identically zero or grows linearly in L, with matching upper and conditional lower orders. No existence has been supplied.

**Unexpected endpoint check.** Replacing ceil(L/2) by floor(L/2) is wrong. At depth three G138 gives v_3(0)=1-c_1: words with the same c_0 but different c_1 have different depth-three cells. At even depth four the determining prefix has two symbols, as v_4(0)=c_0*c_1. Thus the count uses the actual growing window, not a fixed-depth entropy limit or an omitted endpoint. The bound is compatible with a dense countable exceptional set and unbounded radii from G154.

**Scope.** This counts hypothetical finite-tail rows within the Rudin–Shapiro family. It excludes neither the original word nor any specified shift and gives no full right extension. The necessary count is linear, not positive entropy. A spatial invariant forcing N_(X_r) to be zero is still missing; another prefix census cannot establish that invariant. No prize conclusion.

*Second reader's note on G155 (Local, 2026-10-07; chat L113).* Correct. The determining window is the one from my G140
note: depth $j$ at time 0 needs the wall-neighbour column at times 0 to $j - 1$, whose even times carry
$\lceil j/2 \rceil$ visible letters, so two words sharing $\lceil L/2 \rceil$ letters share the row through depth $L$.
Two finite rows that agree through $L$ and vanish beyond it are equal, and injectivity of $\Phi$ finishes. The two-block
coverage holds because the fixed word is tiled by level-$m$ blocks of length $h \ge k$, so a factor of length $k$ lies
in two consecutive blocks and is fixed by the pair and an offset. The lower bound uses the radius clock, and the
depth-three endpoint check is right. Checked (`rule30_audit_g99_g100.py`, S49): on 60 random words, for $L$ up to 40,
changing any letter from position $\lceil L/2 \rceil$ on leaves depths 1 to $L$ unchanged, while changing letter
$\lceil L/2 \rceil - 1$ changes depth $L$ when $L$ is odd. Depth 3 is $1 - c_1$ and depth 4 is $c_0 c_1$, and on
$2^{18}$ letters of $r$ the factor counts obey $P(k) \le 16h < 32k$ for $k \le 64$. Descriptive: those counts equal
$8k - 8$ at every tested $k$ from 8 to 64, the value I recall from the automatic-sequences literature for Rudin–Shapiro
(not re-read here). If that value holds, the exception count is at most $8 \lceil L/2 \rceil - 8$ once
$\lceil L/2 \rceil \ge 8$.

**Source-checked refinement (GPT GC184; Local L114 checks the transfer).** Allouche and Shallit1993, Theorem1, gives P_r(k)=8k-8 for k>=8 for the exact substitution and binary coding used here. Consequently N_(X_r)(L)<=8*ceil(L/2)-8 for L>=15. For k=ceil(L/2)=1..7 use2,4,8,16,24,36,46 instead; the affine formula is not asserted below8. The published base enumeration is accepted, not independently rerun. See PRIOR-ART.md for the primary source and scope. This changes only the upper constant, not existence or the zero-or-linear dichotomy.
