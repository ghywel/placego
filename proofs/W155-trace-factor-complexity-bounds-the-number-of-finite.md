# Trace factor complexity bounds the number of finite-tail exceptions

*The waiting room (not yet verified). Derived from [PROOFS.md](../PROOFS.md), entry "G155. Trace factor complexity
bounds the number of finite-tail exceptions (2026-10-07)"; rebuild with `python3 proofs/build.py`. Edit the proof in
PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** in the waiting room: stated with a proof, not yet checked by a second reader.

## In plain words

The number of possible finite-tail exceptions in the Rudin–Shapiro family grows at most linearly with their radius.

**What it says.** A finite row of radius L is fixed by the first ceil(L/2) visible symbols. Rudin–Shapiro has only linearly many such factors. If one exception exists, its time shifts also provide a linear lower bound.

**Why it matters.** The count is either zero or linear. This sharpens the counting constraint but still leaves the specified word unresolved; independent review is pending.

**An everyday picture.** Counting the possible seats does not tell us whether anyone occupies one.

## The formal statement and proof

**Status and target.** Symbolic deduction, independent review pending; no computation. Uses reviewed G139 inverse locality, G140 coding/radius growth and G154 (Local L112). The record search found G147/G154's exponential fixed-radius count and G139's fixed-depth temporal factor bound, but not this growing-radius exception count. This is an elementary application of substitution factor counting, not a new general complexity theorem. Prediction: Rudin–Shapiro's exception count is at most linear in radius. Counterfactual: temporal zero entropy alone resolves whether there is even one finite-tail exception; the matching conditional lower bound shows the remaining gap.

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
