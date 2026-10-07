# a four-window certificate for phase mixing

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT195. a four-window
certificate for phase mixing (second-read by Local, 2026-10-07)"; rebuild with `python3 proofs/build.py`. Edit the
proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

Four windows can certify local phase mixing, but a return path is essential.

**What it says.** Parallel quotient edges with opposite exchange labels occur exactly at a shared-tail pattern involving four admitted windows and opposite lower-order labels at the source. Inside a recurrent component they defeat both potential equations. A dyadic return in that same component then forces eventual admission of large dyadic periods, using reviewed G194. G195 independent review is pending.

**Why it matters.** This gives a concrete sufficient witness to seek without classifying a whole larger graph. The actual return-eight graph contains the local pattern but is acyclic, so local branching alone proves no persistence. Long overlap also excludes this pattern on the known short-period return walks themselves; a reachable detour would be needed. Rooted and normalized growth remain open.

**An everyday picture.** Two routes can reach the same doorway with the cards exchanged differently. To repeat the choice, there must also be a way back to the departure point.

## The formal statement and proof

### GPT G195 — A four-window certificate for phase mixing (2026-10-07; second reader pending)

**Statement, using independently reviewed G194.** In G193's quotient at m>=1, two distinct edge orbits have the same source and target exactly when there is an (m-1)-bit word T such that

    F_m(0T)=F_m(1T)=F_m(T0)=F_m(T1)=1,
    V_m(0T)+V_m(1T)=1.

Their source is the unordered pair {0T,1T}, their target {T0,T1}, and their exchange labels are0 and1. If this edge lies on a positive closed walk, its strongly connected component makes both G194 potential systems insoluble. If the component's cycle gcd is a power of two, every sufficiently large dyadic period is admitted. A known dyadic return in that SAME quotient component already certifies the gcd condition; no full component census is needed for this implication.

**Prediction and counterfactual before hand controls.** Oppositely labeled parallel edges should arise precisely when dropping the leading bit erases the difference between the two source windows. A single such pair should obstruct both potentials. The counterfactual that the local pattern alone forces persistence will be checked on the independently acyclic return-eight graph. No computational job runs here.

**Exact local characterization.** G189 gives V_m(Z)=last(Z)+A_(m-1)(the preceding bits), with V1(Z)=Z covering the m1 boundary. For a fixed source, each proposed target orientation therefore fixes both appended bits uniquely. There is at most one edge of each exchange label.

Two distinct edge orbits with the same quotient endpoints must consequently have opposite labels. Lift both from the canonical source (X,Y). Their ordered targets must be exchanged copies of one another. Since each target's first m-1 bits equal the corresponding source tail, this requires tail(X)=tail(Y)=T. The source windows are distinct in H_m, so they are0T and1T. The target windows are distinct too, so they areT0 andT1. Source and target admission supplies all four F conditions and the source V condition.

Conversely those conditions put {0T,1T} in the quotient. The two target windows have opposite V values by the affine last-bit identity. Both are F-admitted, so appending0,1 in either order gives valid H_m edges with exchanged ordered targets. These are the two distinct edge orbits and their labels differ.

**Recurrence and the dyadic witness.** Both potential equations in G194 assign the SAME right-hand side to parallel edges. Their left-hand sides differ by1, because their labels differ while their cyclic-class wrap bits agree. Thus neither system can be soluble in a component containing them. If the edge lies on a positive closed walk, both endpoints lie in one cyclic strongly connected component. G194's persistent case then applies exactly when its gcd g is a power of two.

If a known dyadic return q occurs in that component, its quotient closed walk has length h=q/2. Therefore g divides h, already making g a power of two. A return elsewhere does not suffice. Persistence would give ambient first returns at most r for every sufficiently large dyadic q, via G190; it supplies neither exact first return r nor rooted ancestry. Finding this certificate would refute divergence of the minimum AMBIENT return delay, while leaving the rooted and normalized growth questions open.

**Independent boundary control and identified unexpected transient check.** At m1, F1(0)=0, so the four-window certificate fails, agreeing with the empty retained graph. At m3 take T=01. G192's admitted triples include001,101,010,011. Their V3 values are respectively1,0,0,1. From canonical source (101,001), appending(0,1) gives canonical target (010,011), label0; appending(1,0) gives its swap, label1. Thus this parallel pair really occurs in Rule30, rather than only in an abstract control.

Unexpected check: G192 proves this actual graph acyclic. The parallel pair is therefore transient and gives no persistent component. The missing return path is a mathematical requirement, not an optional computational check. G194's abstract bipartite control supplies the contrasting recurrent example, with both labels in each direction and dyadic admissions at all q>=4.

**Record and limits.** G193/G194 already retain parallel choices; this adds their exact Rule30 window criterion and the same-component witness shortcut. No novelty is claimed for generic graph potentials. No larger-r window or recurrent component has been tested, including r88. Local: second-read the necessity of equal tails and the transient guard; no job requested. The next bounded structural question is whether a known return component can reach one of these four-window pairs and return from its target. That question remains open, and absence of this sufficient certificate would not rule out persistence by longer oppositely labeled paths.

**G195 continuation: long overlap excludes the certificate on the observed walk (GPT, 2026-10-07; second reader pending).** On any dyadic swap walk of length h=q/2 in G190, if m-1>=h, none of its source vertices can have equal tails. Hence none can be the source of G195's parallel edge pair. This does not exclude other vertices in the same strongly connected component.

**Prediction and counterfactual before controls.** The difference between the two temporal halves should have period h; a whole h-block of zeros should therefore be impossible. The counterfactual that the known short-period witness itself is a suitable place to search for the local certificate fails in this overlap regime. No computation runs.

Close the walk by its swapped copy, as in reviewed G190, to obtain a q-periodic word w. Put beta(t)=w(t)+w(t+h). Then beta(t+h)=beta(t). If the source windows at some t share a tail, beta is zero at t+1 through t+m-1. When m-1>=h, that interval contains a full h-block; h-periodicity forces beta identically zero. But w would then be h-periodic, and so would c=U_(2m)(w), contradicting c(t+h)=1+c(t). This proves the exclusion.

A further simple-cycle guard applies when m>=q. The word w has least period q: it is q-periodic and its derived c has least period q. If two unordered quotient vertices at times0<=s<t<h coincide, their m-bit first windows either coincide or are exchanged. At least one full q-block then shows that shifting w by t-s or t-s-h preserves w. Neither shift is0 modulo q, contrary to least period q. Thus the h vertices on this particular quotient walk are distinct. The component can still contain additional edges and vertices; a simple observed circuit is not a certificate that the entire component is a simple cycle.

**Actual controls and identified unexpected sharp-length guard.** The reviewed q8/r88 witness has h4,m43; the rooted q16/r52808 witness has h8,m26403. Both therefore exclude the four-window certificate on their observed paths and have simple quotient circuits of length4 and8 respectively. These are hand consequences of their verified parameters, not new graph runs. Unexpected check: an h-periodic nonzero difference can contain h-1 consecutive zeros. For h4, take the word-only control w=00001000; beta=w+S4w=10001000, which has three consecutive zeros. This is not asserted to satisfy the return graph. It checks why the zero-block argument requires h zeros and cannot silently use h-1.

The next recurrence question must therefore concern a detour from a known return component to a four-window pair and back, or a longer pair of equal-length paths with opposite labels. Inspecting only the known periodic circuit cannot answer it. No detour search, PR191-B1 restart or larger-r census is requested.

*Second reader's note on G195 (Local, 2026-10-07; chat L162).* Correct. By G189's affine form, $V_m$ of a window is its
last bit plus a function of the earlier bits. A target orientation therefore fixes both appended bits, so each source
has at most one edge per label, and parallel quotient edges must carry opposite labels. Exchanged ordered targets share
their first $m - 1$ bits with the two source tails, so the tails are equal, which forces the windows $0T, 1T$ and
$T0, T1$. The converse follows by appending 0 and 1 in both orders. Equal right-hand sides with unequal labels defeat
both of G194's potentials. Checked (`rule30_audit_g99_g100.py`, S91) on G190's graphs for $m = 1$ to 6, pruned to $H_m$.
Each source has at most one edge per label, every parallel pair carries opposite labels, and the parallel pairs are
exactly the four-window pairs. There is one at $m = 3$ (GPT's $T = 01$, reproduced edge for edge) and one at $m = 6$,
none elsewhere, all in acyclic graphs and so transient, as the guard says. On 300 random strongly connected labelled
graphs with an opposite parallel pair added, neither potential is soluble. The overlap continuation is also correct: on
a closed swap walk, $\beta = w + S^h w$ has period $h$, so equal tails over $m - 1 \ge h$ positions would make $\beta$
vanish and $w$, hence $c$, $h$-periodic, against $c(t + h) = 1 + c(t)$. S92 confirms on both actual even returns
($q = 8$, $m = 43$; rooted $q = 16$, $m = 26{,}403$) that $\beta$ is nonzero, no source on the walk has equal tails, and
the walk's quotient vertices are distinct. GPT's $h - 1$ guard (00001000) has three zeros in a row in $\beta$ but not
four.
