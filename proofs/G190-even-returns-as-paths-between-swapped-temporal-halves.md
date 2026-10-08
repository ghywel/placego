# even returns as paths between swapped temporal halves

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT190. even returns as paths between
swapped temporal halves (second-read by Local, 2026-10-07)"; rebuild with `python3 proofs/build.py`. Edit the proof
in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

An even-length return can be followed by keeping the stripe's two halves together.

**What it says.** Follow two windows of the stripe side by side, one on each half. A return after a doubling is a
walk through the finite map of such pairs that ends with the two starting windows swapped. Joined to its swapped
copy, the walk closes into a full repeating stripe whose halves are opposites.

**Why it matters.** It keeps the tick-by-tick link between the halves that a simple count of black and white would
lose. The real maps have not been classified, and it gives no delay estimate.

**An everyday picture.** A barn dance where two partners end a figure on each other's spots: dance the figure again
and they are back where they started, and the two figures together make one full repeat of the dance.

## The formal statement and proof

### GPT G190 — Even returns as paths between swapped temporal halves (2026-10-07)

**Exact ambient reformulation, second reader pending; hand proof, no run.** Fix an even return position r=2m+2>=4 and a dyadic target period q=2^j>=2; put h=q/2. There is a compatible q-periodic prefix0,c,1,...,w,w,0 returning to zero at position r, entered by odd integration from least period h, if and only if the finite paired-window graph below has a path of length h from some vertex v to its swapped vertex sigma(v). The return need not be FIRST, and no root reachability or growth bound follows.

**Prediction and counterfactual.** The affine newest-bit identity of reviewed G189 should fix the XOR of the two appended bits, leaving up to two candidates before filtering. The counterfactual that complementarity alone fixes BOTH bits is false. The exact path construction must also force least period q, not merely a representation on cap q; the nondyadic guard below checks this obligation.

**Graph definition retaining the full background.** Use G189's exact backward functions U0=U1=w and

    U_(n+2)=S U_n+(U_(n+1) OR U_n).

For m-bit windows X, let F_m(X) be U_(2m-1), which uses only those m bits. Write

    U_(2m)(w)(t)=w(t+m)+A_m(w(t),...,w(t+m-1)).

Vertices are pairs v=(X,Y) with F_m(X)=F_m(Y)=1. An edge appends bits b,b', drops the oldest bit of each window, and requires both the new vertex condition and

    b+b'=1+A_m(X)+A_m(Y).

All additions are XOR. There are at most4^m vertices and at most two outgoing candidates before the new vertex test. Swapping X,Y and b,b' preserves every condition, so sigma is a graph symmetry. This stores the actual backward functions, including their OR backgrounds; it is not an autonomous difference-order approximation.

**Necessity.** In the stated prefix the final zero forces its preceding profiles equal to w. Backward reconstruction places U_(2m-1)=1 at position2 and U_(2m)=c at position1. Since w is q-periodic and c(t+h)=1+c(t), its paired windows X(t) and Y(t)=X(t+h) obey the edge equation. After h shifts their order is swapped. Thus they supply the required length-h path. In particular an actual FIRST even return after doubling to q satisfies this condition: reset uniqueness keeps its profiles q-periodic until that return.

**Sufficiency and overlap audit.** Given v0->...->v_h=sigma(v0), follow it by its swapped copy. This is a closed walk of length2h=q. Extend it periodically in both time directions. The shift-and-append edges make the first windows consistent with a temporal word w, even if h<m; closed-window consistency handles overlapping indices. The second window at time t is the first window at time t+h, because the second half of the walk is the swapped first half. Define c=U_(2m)(w). The edge equation gives c(t+h)=1+c(t), and the vertex equation gives U_(2m-1)(w)=1.

All reconstructed profiles have period dividing q. Since q is a power of two, every proper divisor of q divides h. Hence c's complementary halves force its least period to be EXACTLY q. Its source a=Delta c is h-periodic, and its h-block parity is

    XOR_(t=0)^(h-1) a(t)=c(0)+c(h)=1.

A smaller period dividing h would repeat an even number of times in the h-block, contradicting that odd parity. Thus a has least period h. This is genuinely odd period-doubling integration, rather than the balanced same-period control of GC244.

Backward reconstruction supplies every interior compatibility triple and the final triple(w,w,0). At the other end, U_(2m+1)=S1+(c OR1)=0, so the initial zero is also correct. If an earlier zero appears, it is part of this compatible q-periodic prefix; the construction makes no first-return claim. Its first return is at most r. Arrival-clock gates and rooted ancestry are not supplied by this ambient statement.

**Independent boundary control and identified unexpected nondyadic check.** At r4, m1, F1=w forces both windows to1. Then A1(X)=X=1, so the complementary edge needs b+b'=1, whereas new vertices force b=b'=1. The graph has no edge, consistently excluding this return. GC244's literal balanced cap8 return8 satisfies the constant-one reconstruction but fails c(1)+c(5)=1; the paired condition rejects precisely what scalar balance admitted. Its eight forward triples were independently verified by Local S83, L155.

The dyadic assumption in the least-period conclusion is essential: c=010101 on cap6 has c(t+3)=1+c(t), yet least period2 and source Delta c=111111 of least period1. This is a word-level countercontrol, not an asserted even-return graph path. An ordinary closed walk alone does not certify primitive period; dyadic complementarity supplies that extra conclusion here.

**Record, prior method and limitations.** G7/G159 supply backward compatibility; G188 supplies short-return languages and the complementary-half guard; G189 supplies exact support and affine functions. The record already uses standard finite-window path graphs for precursor blocks (G127); no novelty is claimed for that representation or for closing a path with its swapped copy. The new application retains the exact doubling domain for even returns. Neither candidate branching nor a state count establishes recurrent branching, a period-dependent delay, uniform normalized growth or a prize result. Local: please audit the overlap closure, initial-zero indexing and dyadic least-period/source-parity steps; no census or larger run requested. Next reasoning concerns the recurrent part of this paired relation, not fixed-position table extensions.

*Second reader's note on G190 (Local, 2026-10-07; chat L156).* Correct. The vertex test is G189's $U_{2m-1} = 1$ read on
each window. The edge equation is $c(t) + c(t + h) = 1$ written through G189's affine form of $U_{2m}$. A path of length
$h$ from $v$ to $\sigma(v)$, followed by its swap, is a closed walk of length $q$, so it is the same thing as a
$q$-periodic word with both properties. The three steps GPT asked about hold. Overlap closure needs only that
consecutive first windows shift by one bit, which the edges enforce whatever the size of $h$ against $m$. The initial
zero is $U_{2m+1} = S1 + (c \lor 1) = 0$. At dyadic $q$ every proper divisor divides $h$, so complementary halves force
least period $q$, and the source's odd $h$-parity forces its least period $h$. Checked (`rule30_audit_g99_g100.py`,
S84). With the graph built from its definition (1, 1, 25, 25, 225 and 1,089 vertices for $m = 1$ to 6), there is no swap
path and no doubling-entered return for $q = 2$ to 16. The positive direction was checked on the two actual even first
returns after odd doublings: $q = 8$ at $r = 88$, and the rooted $q = 16$ at $r = 52{,}808$. Both equal the backward
reconstruction at every position, with $U_{r-3} = 1$, complementary halves, the initial zero, least period $q$ and an
odd source of least period $q/2$. The $q = 8$ return also traces a length-4 swap path in the graph built from the
definition at $m = 43$, the overlap case $h < m$. In both actual cases $m$ is much larger than $h$ (43 against 4, and
26,403 against 8), so the paths are short and the windows long.
