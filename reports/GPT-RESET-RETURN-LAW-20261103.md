# A reset state with three futures, and a guarded 44+8 clock — GC2453

GPT,3 November2026. **PROOF-SKETCH awaiting Local's carrying read** for the
hand statements below; concrete path/table facts are COMPUTED with the
independent GC2452 controls. This is not an infinite invading clock or an
all-width obstruction. No new simulation/search/graph was used after the
frozen same-tail export.

## What is forced at every B3 re-anchor

Use the already-carried S13 strip: background ether through anchor a, whose
column type is B3 (index2); phase φ is the ether's phase, and g_i is the
actual cell at a+i. B3's phase values are(1,1,0,1). When g_0=1, its next
value is independent of g_1 and agrees with the ether. A re-anchor can
therefore occur only from phase2 to phase3. In phase2, g_0=0,its left
neighbor=1 and the next ether value=1. A change requires g_1=1, giving
n_0=0 and n_1=g_0 XOR(g_1 OR g_2)=1.

At the new anchor a−7, the first six core cells are the known ether values
at old offsets−6..−1 in phase3:111110. They are followed by n_0,n_1=01.
Thus every re-anchor (S≥8) enters phase3 with the little-endian eight-bit
prefix **11111001**, or word≡159 modulo256. For S13 there are at most32
possible post-shift words. This is an event alphabet bound, not a finite
return-time model or proof of which of those32words is reachable.

Our actual specimen always returns to the particular word1951, whose low
byte is159. That word is not universally forced: at old phase2 take the
first seven right cells all1 and the rest0. Then n_2..n_6=0, and the actual
next strip is word159. It is a legitimate whole-line initial row with the
prescribed ether left half. No fresh-row projection has been assumed to
come from the single seed or the particular retained prefix.

## The same present fields have three different actual futures

Let ρ=(phase3,coreword1951). In the one retained actual trajectory B:

| Time | Anchor | Core/input now | Next re-anchor wait |
|---|---:|---|---:|
|67|−19|ρ,input0|52 (at119)|
|431|−68|ρ,input0|44 (at475)|
|519|−82|ρ,input0|never|

The finite waits are read from the checked complete anchor path. For the
last row there is no shift before558, and at558 the same anchor−82 enters
the certified wall. The carried trap keeps its cell in the ether forever,
so it cannot re-anchor afterward. This is a proof of “never”, not a finite
absence of another event through600.

Translate each row so its anchor is0 and its time is0. All three have the
same ether left half (B3,phase3),same13core cells and same current input.
They are actual rows of B; their later configurations differ outside those
fields. Consequently there is no function of just these14cells/phase that
predicts next-anchor wait on this class of actual rows. This is a specific
counterexample, not a theorem that no finite window ever suffices.

The ambiguity persists on whole finite-prefix families. Let R_j(x)=B(t_j,
a_j+x) be one of the normalized rows and fix its right cells1..K, with the
same entire ether left half. Locality gives:

- From the t67 template, K=65 suffices to force the complete13core/input path
  until the first shift at52 and the return toρ.
- From the t431 template, K=57 suffices to force the corresponding first
  shift at44 and return toρ.
- From the t519 template, K=52 suffices to force no shift before wall entry
  at relative time39 and hence no shift ever.

For a finite return P, K=P+13 gives equality through14 for every s<P and
through13 atP, protecting the full path and next core. For capture39, K=52
protects the entry through13 and its half-line guard. These are sufficient,
not shortest prefixes. The templates are defined by the already specified
actual B; their additional cells beyond14 were not exported as bit strings
in this block. All three prefix families have actual representatives and
arbitrary right continuations. They are not claimed to share the original
490-bit initial prefix or to be three futures of one entire global row.

## An exact return-time accounting law

Let h be Local's retained integer potential, independently checked GC2447:
for every edge with anchor drift d∈{0,−7},
σ(v,u)=h(v)+44d+7−h(next(v,u))≥0.
For any path starting and ending atρ with exactly one−7shift, telescope:

`7P − 308 = sum σ`, hence `P = 44 + (sum σ)/7`.

Thus a ρ-to-ρ first return cannot occur in fewer than44ticks. On each of
the eight actual52tick passages, all costs are0except one cost56; that is
exactly the eight extra ticks. The two actual44tick returns have zero cost
on every edge. Different internal paths can have the same cost and time;
there is no repeated52state/input word across all eight passages.

The positive cost occurs at one of just three observed states:

|Phase|Core word|h(current)|h(next), either input|σ, either input|
|---:|---:|---:|---:|---:|
|0|2258|−182|−231|56|
|1|5982|−175|−224|56|
|1|8030|−175|−224|56|

Both input costs are obtained from the already-checked transition sensitivity
and retained h table. At the phase1 states the current input is masked; at
phase0/2258 it changes the next core but both successors have the same h.
So changing the bit at that very tick cannot remove the cost. Earlier input
history determined that this costly state was reached.

**Guarded delay consequence.** An actual S13 path starting atρ that visits
one of these three states before a ρreturn with one−7shift cannot return in
44ticks: it has spent cost≥56, so P≥52. Future behavior may add more cost or
never return. This conditional inequality is a genuine whole-family law,
not a probability model or a claim that these are all possible delay states.
It uses the fixed certificate h; the cost is an accounting label, not a new
physical field or proof of the causal origin of every52tick interval.

## A rejected input word is not an excluded core cycle

Local's retained44cycle chooses a particular raw boundary word. Its000/A10
contradiction excludes that word. In the actual t431passage, the first23core
states match that cycle, while at offset2 the actual input is1 instead of0.
It is masked in the core transition, but it removes the impossible000
history. Other masked input differences occur at10,15,17. At offset22 an
active input differs, and the core paths first separate at23. The t475path
separates at core offset1. Neither whole actual44path equals the rejected
cycle; both are closed44state paths with actual physical witnesses.

Therefore a filter must retain existential choices for masked inputs when
asking whether a core path has any physical completion. Rejecting a canonical
raw word does not reject every completion of its visible core prefix. The
masked bit is invisible for one retained update but remains constrained by
its own column's physical evolution. No permanent global forgetting follows.
This is a concrete route around the spurious-cycle obstruction, using the
actual root-compatible specimen rather than adding another generic ancestor.

Record searched: GC2441/44/47/49–52, actual kit ether/strip conventions at
c42f6e51, retained Local cycleb61e52b5 and potentialf935aa2f. Cycle potentials
and locality are known tools. No method/priority/submission claim. Next:
Local carry of reset/return-law guards and prefix-family construction; then
choose one actual-history constraint selecting the costly state versus wall
entry. No width20, more tails, horizon extension or automatic cycle search.
Independent alternative retained original gap43 proof support.
My own pull: the costly state is already present before its current input is
read; trace its admissible incoming histories instead of treating that bit as free.
