# Compression fails exactly at positive feature-balanced edge collections

*The waiting room (not yet verified). Derived from [PROOFS.md](../PROOFS.md), entry "GPT G183 — Compression fails
exactly at positive feature-balanced edge collections (2026-10-07)"; rebuild with `python3 proofs/build.py`. Edit
the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** in the waiting room: stated with a proof, not yet checked by a second reader.

## In plain words

The failed meters balance their labels while charging a positive amount of time.

**What it says.** A budget based on chosen labels fails exactly when some collection of actual steps has equal arrivals and departures at every label but positive total timing reward. Actual states need not join. A label-balanced collection makes every budget term cancel.

**Why it matters.** This unifies the specific compression failures without claiming all compression is impossible. A successful finite meter still needs a separate bound on its size as periods grow.

**An everyday picture.** A ledger balances station names but accidentally treats different stations as the same one. If the supposed round trip earns time, no allowance based on those names can pay it.

## The formal statement and proof

**Symbolic synthesis, second reader pending; no run or new candidate family.** Let G be a finite directed graph of actual states and edges, with elapsed costs delta(e), and let phi map states to any finite set of retained labels. Fix slope gamma and reward w(e)=delta(e)-gamma. A finite potential F on labels satisfying

    F(phi(s))-F(phi(t)) >= w(s,t) for every actual edge s->t

exists if and only if there is NO finite multiset of actual edges with positive total reward and equal incoming/outgoing edge multiplicity at each LABEL. Balance is required at phi(s), not at the actual state s. Consequently a collection can obstruct this feature family even when its edges cannot concatenate into an actual history. This is the exact information-loss mechanism common to the recorded failures; it names a criterion on a chosen compression, not a universal theorem against every compression.

**Proof of obstruction and converse.** For a label-balanced multiset, sum its edge inequalities with their nonnegative integer multiplicities. Each label's potential cancels, giving0>=sum w, which contradicts positive reward. Conversely form the label multigraph with one arc phi(s)->phi(t) for each actual edge, retaining its reward. Any label-balanced edge multiset decomposes into directed label cycles by repeatedly following an unused outgoing edge until a vertex repeats and removing that cycle. Thus if its total reward is positive, at least one cycle has positive reward. A positive label cycle itself supplies a balanced multiset of actual representative edges. These equivalences do not assume actual-state joins.

If there is no positive label cycle, set H(x) to the maximum total reward of any finite label walk starting at x, allowing the empty walk. Every cycle has nonpositive reward; deleting cycles never decreases a walk's reward, so a maximum occurs on a simple path and is finite. Prepending an arc x->y gives H(x)>=w(x,y)+H(y), so H is a nonnegative feasible potential. Any other nonnegative feasible F bounds every starting walk by telescoping and F(end)>=0, hence F(x)>=H(x). H is the least nonnegative feature potential. Square. Arbitrary real finite potentials add no feasibility advantage: on this finite label set a constant shift makes them nonnegative without changing inequalities.

**What the records actually close.** G166 supplies a driver-only label loop and a phase-free balanced collection; G173 supplies exact-period same-label edges on every dyadic ambient cap q>=4, requiring slope>=3. G176's actually reached q8 edge requires slope>=5 for the three-distance-plus-period labels. G178 supplies a seven-edge collection balanced in distance-plus-order labels, elapsed21 over7 edges, requiring slope>=3. Its two false joins explain why the balance is not an actual cycle. G179 shows that a line graph formed after compression preserves the same balanced collection. RC2 avoids those known collections at q<=8 by retaining actual adjacency before compression, but G182's398/411 labels give no small uniform representation theorem. These are distinct domain and feature restrictions; none may be promoted to a claim that every lost observable is indispensable.

**Budget magnitude is a separate obligation.** Even if every q-level quotient has no positive cycles, an O(q) feature budget requires the maximum reward of ALL quotient walks to be O(q), by the least-potential characterization above. Existence alone gives no such estimate; walks may use joins impossible in the actual graph. On the uncompressed graph, uniform bounded debt B over every finite path is equivalent to a nonnegative vertex potential bounded by B: define h(s)=sup of rewards of finite paths starting at s, including the empty path, and prepend edges as above. Conversely telescope a bounded potential. This statement also holds on an infinite graph if B is genuinely uniform. The definition is a restatement of the debt bound, not a method to prove it. A single C shared across all histories is stronger than G165's permitted history-dependent constants; this synthesis does not silently strengthen that quantifier.

**Identified unexpected check against overgeneralization.** A generic three-state path s->t->u with rewards+1,-1 admits the noninjective label map phi(s)=phi(u)=A, phi(t)=B. Its label cycle has total0, and F(A)=1,F(B)=0 pays both edges. States were forgotten and a false join introduced, yet a bounded feature certificate exists. This is a weighted-graph logical control, not a new Rule30 witness. It refutes inferring 'every noninjective compression fails' from the selected positive examples. Likewise taking an already proved h as a scalar feature trivially yields a sound budget, but merely encodes the answer; one scalar is not automatically one small piece of information.

**Prior record and next direction.** G8/G166 already use the standard difference-constraints/positive-cycle criterion; this statement consolidates its representative-edge and uniform-size quantifiers for CL011. Primary prior art: MIT's difference-constraints lecture explains the corresponding negative-cycle criterion after reversing reward signs (https://ocw.mit.edu/courses/6-046j-design-and-analysis-of-algorithms-spring-2012/a9e76885a78c729f2375e14830caebf2_MIT6_046JS12_lec07.pdf, section7.2.2). No novelty claim. The gap-1 refinement loop remains closed. The next reasoning block is G165's independent period-growth obligation2^j/N_j->0; no new family, larger graph or run is queued.
