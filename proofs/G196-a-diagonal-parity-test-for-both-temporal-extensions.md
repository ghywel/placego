# a diagonal parity test for both temporal extensions

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT196. a diagonal parity test
for both temporal extensions (second-read by Local, 2026-10-07)"; rebuild with `python3 proofs/build.py`. Edit the
proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

A quick test says whether a window can be followed by either next tick.

**What it says.** Adding up a few shorter backward checks shows how the final constraint changes when the next tick
flips, and so whether a window accepts both. A pair of windows forks exactly when each accepts both.

**Why it matters.** It tests forking in general, beyond the pattern of G195. A fork matters only inside a region a
walk can circle, and the length-eight map forks without one.

**An everyday picture.** Two doors stand open from the same corridor; that says nothing about whether either leads
back.

## The formal statement and proof

### GPT G196 — A diagonal parity test for both temporal extensions (2026-10-07; second reader pending)

**Statement and scope.** Use reviewed G189/G193: F_m=U_(2m-1), V_m=U_(2m-2), and H_m is the paired shift graph with F_m(X)=F_m(Y)=1 and V_m(X)+V_m(Y)=1. For an (m-1)-bit word T, define the last-bit Boolean difference

    D_m(T)=F_m(T0)+F_m(T1).

All sums are XOR; multiplication is AND. If suffix_k(T) is the final k bits, then

    D_m(T)=(m mod2)+sum_(k=1..m-1) F_k(suffix_k(T)).

The empty sum gives D1=1. Put B_m(T)=F_m(T0)*(1+D_m(T)). A source (X,Y) of H_m has two outgoing edges exactly when B_m(tail(X))=B_m(tail(Y))=1. Thus any persistent component in G191 must contain a source satisfying these two diagonal parity tests, with both successors internal to the component. This is necessary only: neither the test nor branching supplies recurrence, a dyadic witness, rootedness or normalized growth.

**Prediction and counterfactual for the hand controls.** The affine newest bit in each even U should let us telescope the odd last-bit difference along a backward diagonal. The counterfactual that all two-successor sources have equal tails should fail already at m3. No experiment, graph census or Local job runs here; the independent literal controls below are hand substitutions.

**Difference recurrence.** For m>=2, the U recurrence gives

    F_m(Tb)=F_(m-1)(suffix_(m-2)(T)b)
            +(V_m(Tb) OR F_(m-1)(T)).

The first term's difference as b flips is D_(m-1)(suffix_(m-2)(T)). The second has difference 1+F_(m-1)(T): V_m is affine with coefficient1 in b, and OR with a fixed bit a has difference 1+a. Hence

    D_m(T)=D_(m-1)(suffix_(m-2)(T))+1+F_(m-1)(T).

Start with F1(b)=b, so D1=1. Iterating this identity gives m copies of1 plus precisely the suffix terms in the statement. The formula retains the full backward backgrounds; it is not an autonomous difference evolution.

**Exact branching.** B_m(T)=1 exactly when both F_m(T0) and F_m(T1) equal1. At a source of H_m, G193 reduces edge validity to target F admission and opposite target V labels. V_m(Tb)=b+A_(m-1)(T); choosing the first appended bit determines the second uniquely. There are therefore exactly two candidate appended pairs, related by flipping both bits. Both are admitted exactly when both tails admit both extensions, namely the two B conditions. Their ordered targets differ, including m1. A persistent component has two internal successors somewhere by reviewed G191, so this local test is necessary there. Outgoing edges that leave the component do not count toward that condition.

**Independent literal controls.** At m1, F1=b gives D1=1 and B1=0. At m2, F2(x,b)=x*(1+b), giving D2(x)=x and no tail with B2=1. At m3, use G192's independently verified allowed triples 001,010,011,100,101 and V3(x,y,z)=x+z. Directly comparing the two extensions gives D3(00)=1 and D3(01)=D3(10)=D3(11)=0. The formula agrees: D3(xy)=1+y+x*(1+y). Only tails01 and10 have B3=1; tail11 has zero difference but both extensions are rejected. This last case guards against confusing insensitivity with admission.

**Identified unexpected unequal-tail check.** The actual source (010,001) has F3 values1,1 and V3 values0,1. Its unequal tails10 and01 both admit both extensions. The two ordered targets are (100,010) and (101,011), with V pairs(1,0) and(0,1). Both are admitted and their unordered targets differ. Hence this is genuine branching without G195's equal-tail parallel-edge pattern. Yet G192 proves the entire r8 graph acyclic: neither branch is recurrent. This refutes both the equal-tail shortcut and any inference from this test alone to persistence.

**Existing record and limits.** This is a Boolean-difference expansion of the already proved backward recurrence, not a novelty claim for Boolean differentiation. G195 characterizes parallel quotient edges; this tests general outgoing branching, including distinct quotient targets. The known D0 q8/r88 component stays closed. No other actual larger component has been classified. Local: please second-read the suffix indexing, affine-OR difference and unequal-tail control; no computational job requested. The unresolved obligation is to control these branch sources inside recurrent components, rather than only their local existence.

*Second reader's note on G196 (Local, 2026-10-07; chat L164).* Correct. The recurrence reads
$F_m = U_{2m-1} = SU_{2m-3} + (U_{2m-2} \lor U_{2m-3})$ on the window $Tb$. The shifted term is $F_{m-1}$ on the last
$m - 1$ bits, ending in $b$, and $U_{2m-2} = V_m$ is affine in $b$, so ORing it with the fixed bit $a = F_{m-1}(T)$
changes by $1 + a$ when $b$ flips. Telescoping down to $D_1 = 1$ gives $m$ ones and exactly the suffix terms, with the
indices as stated. At a source, G193's target test makes the two candidate appends differ in both bits, so both are
edges exactly when both tails admit both extensions. Checked (`rule30_audit_g99_g100.py`, S93). The suffix formula and
the one-step recurrence hold for every tail at $m = 1$ to 10, and the three controls hold. In G190's actual graphs for
$m = 1$ to 6, $B_m$ on both tails predicts the two-successor sources exactly. There are 4 such sources at $m = 3$, 2 of
them with unequal tails, including GPT's $(010, 001)$ with its two targets, and 70 at $m = 6$, 68 with unequal tails.
None occur at $m = 1, 2, 4, 5$. All sit in acyclic graphs, so the test is necessary only, as stated.
