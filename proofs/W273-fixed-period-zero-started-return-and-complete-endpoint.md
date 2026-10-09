# Fixed-period zero-started return and complete endpoint interface

*The waiting room (not yet verified). Derived from [PROOFS.md](../PROOFS.md), entry "GPT G273 — Fixed-period
zero-started return and complete endpoint interface (GPT, 2026-10-09; waiting room, GC864-GC865)"; rebuild with
`python3 proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this
file.*

**Status:** in the waiting room: stated with a proof, not yet checked by a second reader.

## In plain words

Every admissible fixed-period walk starting beside a zero column returns to zero, and all its nontrivial excursions end at different nonzero words.

**What it says.** Unique backward reconstruction prevents a live walk from repeating after a zero start. Counting all starts then gives a bijection onto the nonzero endpoints. The compressed return graph has a root tree and separate cycle components. Cloud second-read the return and endpoint arguments, and the component/period counts; its review did not independently reconstruct the physical-root identification or the cited nonroot example. The combined filing remains in the waiting room.

**Why it matters.** Existence and endpoint completeness are structural. Individual depths, restricted-source growth and physical-root ancestry still require more information.

## The formal statement and proof

*Provenance:* GC864 and GC865, hand reasoning; existence agrees independently with Local L487. Coarse bound and endpoint theorem await second reading. Uses G7/G156/G158, no novelty claim for those mechanisms.

#### GC864 — Every fixed-period zero-started excursion returns; the remaining question is quantitative (2026-10-09 21:17 BST)

**Registered hand ancestry audit, review pending.** Prediction: unique backward ancestry forces a first zero return even for arbitrary zero-driver sources not reachable from G7's physical root. Countercontrol: GC863's ambient nonzero cycle has no zero anchor. Unexpected check: the all-zero integrated child stops immediately rather than supplying a live cycle. No computation or RW replay. Existing G7/G156's predecessor mechanism and G158's reset lemma suffice; this is an application of recorded prior art, not a new invariant or prize claim.

**Statement.** Fix any common temporal period q>=1. Start at v_0=(a,0), choose a q-periodic child c when one exists, and stop at the first later pair whose second profile is zero. Every such excursion returns in finitely many edges. If c is nonzero, its return index r obeys the coarse bound

    r <= (2^q-1)^2+2.

No physical-root reachability assumption and no odd-half assumption are required. A source with no q-periodic integrated child has no excursion; it is not a nonreturning live path.

**Proof.** For an edge (a,b)->(b,c), the temporal equation is S c=a XOR(b OR c). Thus every target has exactly one predecessor

    H(b,c)=(S c XOR(b OR c),b).

This is the same backward map as G7/G156, with letters renamed. Every live node has nonzero second profile and therefore exactly one q-periodic child, by reset uniqueness. Hence a path cannot terminate while its driver is nonzero.

Suppose v_i=v_j before the first zero return, with 1<=i<j. Applying H exactly i times gives v_0=v_(j-i). The latter node has nonzero second profile because 1<=j-i<j precedes the first return, whereas v_0 has zero second profile. Contradiction. All live nodes are therefore distinct. There are only finitely many q-profile pairs, so an infinite live path is impossible and a zero return must occur.

For the stated bound put N=2^q. The first live pair v_1=(0,c) has zero first profile. Every later live pair has both profiles nonzero: its first is the previous live driver. There are at most (N-1)^2 such pairs. Thus r-1<=1+(N-1)^2, proving the bound. This elementary bound is deliberately not advertised as sharp for larger q.

**Independent controls and unexpected endpoint.** At q1, the excursion (0,0)->(0,1)->(1,1)->(1,0) returns at r3 and attains the displayed bound. Literal substitution verifies all three edges. If the selected child c=0, integration requires a=0, and v_1=(0,0) is already a return at r1. Continuing its fixed zero loop would violate the specified stopping rule. This is the unexpected endpoint guard.

For the ambient q2 cycle (01,10)->(10,01)->(01,10), H sends each cycle vertex to the other. It cannot be reached by a finite zero-started live path: backward iteration from either vertex stays on that nonzero cycle forever. This supplies the countercontrol missing from an argument based on forward determinism alone. General finite deterministic systems without unique backward ancestry can feed a zero-started path into a nonzero cycle, so that hypothesis is essential.

**Correction to GC863 and interpretation of RW.** GC863 correctly separates reset uniqueness alone from absorption, but its final identification of fixed-q return existence as substantive open work was premature. Adding the already recorded unique predecessor closes that qualitative question for every admissible zero-started excursion, including q32 and beyond. The two initial complementary paths for odd doubled sources return at the same depth by GC863's rotation argument. Consequently one rotated first-return class per source orbit is structural, not a conjecture to be established by a larger census. Different source orbits having distinct return depths is not implied.

The bound at q32 is astronomical; this proof supplies no practical horizon, growth law, parity classification, graph-exit death, or SCC closure. Local's RW sample remains useful to measure depths and returned words and test stronger quantitative/closure predictions. It need not be interpreted as testing whether some admissible fixed-q excursion never returns. The physical first-zero tree and arbitrary zero-started excursions are different domains; only their shared backward-ancestry mechanism was used. No settling theorem or prize result follows.


#### GC865 — The full fixed-q zero-return interface is bijective, but its parity census does not bound depths (2026-10-09 21:21 BST)

**Registered hand continuation of GC864; review pending.** Predict ancestry makes different first excursions have different return words, and the complete source count then exhausts the nonzero return words. Countercontrol: omitting the zero-source excursion loses one endpoint. Unexpected check: literal q2 excursions have odd lengths but different returned-word parity. Read G158, G200 and G202 first; the overlap-parity shortcut is already closed and is not reopened. No experiment, RW replay, new literature claim or prize-board row.

Let N=2^q, with all profiles represented in a fixed temporal phase. Include every zero-driver source (a,0) for which q-periodic integration exists, and distinguish its two initial children. Discard just the all-zero child from a=0, and stop every other excursion at its first later zero driver. By GC864 all these excursions return. Integration exists precisely for even total q-block parity of a. There are N/2 such sources, each with two children, so there are N-1 nontrivial excursions.

**Endpoint uniqueness.** Suppose two excursions have the same return pair (w,0), at lengths r and s with r>=s. Applying the unique predecessor H exactly s times gives the second source at depth r-s of the first excursion. If r>s, this is an internal zero driver (strictly before r), contradicting first return. If r=s, both sources coincide, and backward reconstruction of every intermediate pair also identifies the initial child. Thus the excursions are identical. An endpoint w=0 is impossible: H(0,0)=(0,0), so its entire backward ancestry is zero, contrary to the nonzero first child. There are N-1 possible nonzero endpoint words. The injective map between two sets of size N-1 is therefore bijective.

**What the parity count actually says.** In this complete fixed-q interface, exactly N/2 excursions return to odd-parity words and N/2-1 return to nonzero even-parity words. This is a global identity, not a distribution for physical-root-reachable sources or RC16's odd-doubled-source subset. It does not assign parity to an individual source, bound a return length, or prove reachability from the physical root. The compressed zero-driver graph has indegree exactly one at each nonzero word, no incoming edge at zero, outdegree two at each nonzero even-parity word, outdegree zero at odd-parity words, and outdegree one at zero after the discarded trivial child. These degree counts alone do not exclude components disconnected from the physical root.

**Rotation classes and least periods.** H commutes with rotation. Hence the endpoint-injectivity argument also identifies two excursions whenever their endpoint words are temporal rotations: rotate one whole path and apply the same proof. Distinct initial excursion orbits therefore have distinct return-word orbits. This makes one distinct return class per odd-doubled source orbit structural, strengthening GC863's count clarification. It does not make their depths distinct. Moreover a temporal period of the endpoint pair propagates backward through H to the first child pair. Thus an excursion whose first child has least period q returns to a word of least period q; a period drop cannot hide a repeated orbit.

**Independent literal q2 control and unexpected parity guard.** In temporal order, the zero source's nontrivial excursion is (00,00)->(00,11)->(11,11)->(11,00), with length3 and returned word11 of even parity. Source11 has initial children c=01 or10; each has the exact path (11,00)->(00,c)->(c,11)->(11,c)->(c,c)->(c,00), length5, returned word c of odd parity. Substitution uses S c=NOT c and verifies every edge. These three excursions exhaust the three nonzero endpoint words. The last two have different literal return words and equal lengths. All three lengths are odd, while endpoint parities differ at this same q. Therefore length parity does not determine endpoint parity even at fixed q, and complete endpoint coverage does not imply distinct lengths.

If the source00 is omitted, only01 and10 are returned in this q2 control; endpoint11 is missing. This is the countercontrol to applying the global parity census to only the odd-doubled-source sample. The all-zero endpoint remains excluded, not counted as a fourth return.

**Disposition.** The exact endpoint census is another consequence of the recorded integration/reset/backward mechanism. It narrows what a computational endpoint census can teach: depths, source-to-endpoint matching and root reachability carry information; endpoint completeness in the full fixed-q domain is structural. The attempted universal length-parity inference fails at q2. G200's cumulative-stage growth, individual return parity prediction in the restricted domain, and SCC closure remain open. Next useful step must retain the source-to-endpoint matching or a quantitative path invariant, rather than promote this global parity count into a growth estimate.


**GPT filing audit (2026-10-09 21:22 BST).** The duplicate check passes for W273. Its three nearest older entries G203, G200 and G188 were read in full: they give overlap lower bounds, cumulative-stage telescoping and short-return exclusions. This entry instead uses finite backward ancestry for existence and a global endpoint bijection; it does not restate their conclusions. Its base mechanism is still G7/G156/G158, with no novelty claim. The first query used G273, which the waiting-room parser does not expose; rerunning with its actual W273 ID succeeds. No browser, TeX, run or proof promotion.


#### GC866 — Zero-return cycles are outside the physical root component; qualitative return does not remove ancestry (2026-10-09 21:26 BST)

**Registered hand graph audit; review pending.** Predict GC865's compressed interface has a root tree and disjoint cycle components, with constant least period and even least-block parity on each cycle. Countercontrol: degree balance alone cannot force connectivity. Unexpected check: GC864's universal first return is compatible with G199's nonabsorbing backward ancestry. No graph enumeration or RW run; existing G7/G158/G199 and pending GC864-GC865 are the dependencies. This is a graph-theoretic consequence, not a new quantitative route.

At fixed q, make one vertex for each q-bit word a. A directed edge a->w is each nontrivial first excursion (a,0)->...->(w,0); discard only the all-zero initial child. GC865 gives indegree0 at zero and indegree1 everywhere else. Following the unique incoming edge backwards therefore either ends at zero or enters a directed cycle. Any two vertices in a weak component have the same backward endpoint or cycle, because an edge links a vertex to its unique predecessor. Thus the zero component is an outward directed tree; every other weak component contains exactly one directed cycle with outward trees attached. No directed path can enter that cycle from outside it, since every cycle vertex has already used its sole incoming edge.

The zero component is exactly the compressed physical-root zero-driver tree: its first edge expands the nontrivial path from (0,0) through (0,1), the G7 root, to its next zero. Subsequent compressed edges expand compatible paths with that ancestry. Conversely every physical-root zero-driver node is reached by contracting its successive first excursions. Every other component is outside the backward basin of (0,0). This proves connectivity classification, not a method for deciding a given large word's component without reconstructing ancestry.

**Least periods on a cycle.** Let nonzero a have least temporal period d. Integration yields a first child of least period d when a's d-block has even parity, and least period2d when its d-block has odd parity (the latter requires2d dividing q). Reset continuation preserves that child's period as an upper bound. Any period of a later pair propagates backward through H, so the returned word has exactly the first child's least period. Consequently every compressed edge either keeps the source's least period or doubles it. Around a directed cycle no period can increase, so every cycle edge keeps a common least period d and every source on it has even parity in its own d-block. Cap-q parity alone would miss this distinction for repeated odd blocks.

**Component count, with an independent abstract guard.** In the zero component let E count nonzero even-cap-parity vertices and O count odd-cap-parity vertices. Its edge count is1+2E and its vertex count is1+E+O; the tree identity gives O=E+1. In a cycle component the edge and vertex counts agree, giving O=E. Thus the global excess of one odd endpoint belongs to the root component but does not exclude additional cycle components.

For an abstract eight-vertex control, take root0->e0 and e0->o0,o1, plus e1->e2,o2 and e2->e1,o3. Nonroot indegrees are one, the three e vertices have outdegree two, the four o vertices have outdegree zero, and root outdegree is one. The same global counts as q3 coexist with a disconnected two-cycle. This is an abstract degree control, not a claimed Rule30 graph; it refutes inferring root connectivity from those counts.

**Unexpected actual scope reconciliation.** Reviewed G199's cap8 source a=10110100 is outside the physical-root backward basin, although it has even cap parity and admits nontrivial zero excursions. By the compressed graph classification it belongs to a cycle component, possibly in an outward tree rather than on the cycle itself. There is therefore a compressed cycle somewhere in that component; no cycle word, period or length was computed here. Every individual first excursion still returns by GC864. Following the unique predecessors of successive zero-driver nodes never reaches the all-zero pair. These statements coexist: first return to a zero driver and backward absorption at the all-zero pair are different events.

**Disposition.** The compressed graph exposes rather than removes G199's missing ancestry. Fixed-q interface cycles outside the root tree cannot refute physical-root settling; their existence also does not invalidate universal first-return existence. This compressed source graph is not G190's paired-window graph at fixed return distance, so its cycles do not contradict QX's named SCC closures. Root-component growth still needs quantitative path or matching information. Stop connectivity/degree-count reformulations as a growth strategy; next choose a concrete quantitative subclaim or a requested proof audit. No prize-board promotion or new computation.

**GPT continuation duplicate audit (2026-10-09 21:27 BST).** Adding GC866 changes W273's nearest neighbours to G198, G191 and G190. All three were read in full: their fixed-return paired-window graphs evolve temporal windows and permit recurrent branching; this compressed graph evolves whole zero-driver sources through spatial excursions and has indegree one. No statement about those window SCCs follows from this component classification. The continuation reconciles reviewed G199 with GC864, rather than improving G191's absolute-delay or main-line normalized-growth bounds. No duplicate paragraph or heading found.

**Partial second reading received (GPT, 2026-10-09 21:38 BST).** Cloud CL103 atc111e308 verifies GC864's return proof and bound and GC865's endpoint bijection and controls by hand, without computation replay. Those two parts are second-read. The subsequent GC866 component continuation has not been second-read; this combined entry therefore remains in the waiting room. GC867 separately accepts Local L489's Lean statement match, with compiler verification explicitly Local's evidence, not an independent GPT compilation.
