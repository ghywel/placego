# A finite soundness checker for the channel bound

2026-10-23, GPT, CL594 task 3. **The finite obligations and a generic soundness argument are specified below. A four-minute width-16 physical-closure check is not established.** This is a statement/data-size estimate only: no generator, DFA construction, kernel benchmark or concrete closure-check run was performed for this task. If discharged, this changes the channel row from an externally certified graph bound to a formal bound on every physical visible trace; it does not solve Q01.

Sources read: `entropy2.c`'s actual scalar/bit transition and subset construction; the fixed GC1702 certificate/data report; GC1705's row/weight/tree reconciliation; CL591 and CL594's reported timings; the corrected `channel_tree_encoding.py`. The public kit's `Rule30ZeroBoundary.col1_five_check` and `col1_black_among_five` show the relevant pattern: a finite Bool check, a generic physical light-cone lemma, then a theorem using both. The other submitter's Q_P source is not public in the sources Cloud located; I have not read or reproduced that person's checker. This is the same proof architecture, not a claim to know their implementation.

## Concrete transition and sampling phase

Take m >= 1 and let R_m be the finite type of m-bit rows, with bit k representing physical column k+1. Let F_m(s,tau,u) be one Rule 30 step on that row, with left boundary tau and right boundary u. At cell k its output is left XOR (center OR right), using tau at k=0 and u at k=m-1. Equivalently, on the natural encoding of s,

```math
F_m(s,\tau,u)=\left(((s\ll1)\mathbin{\lor}\tau)
\mathbin{\oplus}\left(s\mathbin{\lor}((s\gg1)\mathbin{\lor}(u\ll(m-1)))\right)\right)
\mathbin{\&}(2^m-1).
```

The semantic definition should use `Fin m -> Bool`; a bit-extensionality lemma proves the integer implementation equal to it. This isolates endian, masking and boundary conventions from the large finite check.

For the white-even clock, define

```math
G_m(s,u,v)=F_m(F_m(s,0,u),1,v),\qquad o(s)=s\bmod2.
```

The visible label is o(s) **before** these two steps. Every actual right-half orbit has row s_n at time 2n, label b_n=o(s_n), and s_(n+1)=G_m(s_n,u_n,v_n), where u_n and v_n are its actual two boundary bits. Treating all four pairs independently is a safe overapproximation. An eventual clock is handled by restarting at a sufficiently late white phase with an arbitrary row; no seed-width assumption is used.

## Certificate and exact finite check

Use a finite live state type I = Fin N, root r, transition delta: I -> Bool -> Option I, represented concrete sets S_i subset R_m, a positive integer weight w_i for each live state, and positive integers D,R. An absent successor is dead, with weight zero and represented set empty. A concrete representation can distinguish `All` from a finite sorted set/trie, avoiding an explicit list at the root.

The checker must establish these obligations:

1. **Representation and domain:** lookup and enumeration implement the same finite sets; all rows are m-bit and all live successor IDs are in range. Any ordering invariant needed for lookup is either checked or guaranteed by a proved constructor. Padding is not a live state.
2. **Root coverage:** every s in R_m belongs to S_r. With `S_r = All` this is structural, not 65,536 separate root-membership witnesses at m=16.
3. **Labelled closure:** for every i, every s in S_i and every u,v in Bool, delta(i,o(s)) is some live j and G_m(s,u,v) belongs to S_j.
4. **Dead-edge safety:** equivalently, if delta(i,b) is dead, S_i has no row with output b. This is already forced by obligation 3 because G_m is total. It must not be replaced by zero target weight alone.
5. **Weight linkage and inequality:** w_i > 0 and

```math
D\bigl(w_{\delta(i,0)}+w_{\delta(i,1)}\bigr)\le Rw_i,
\qquad w_{\mathrm{dead}}=0.
```

The two labels are summed with multiplicity even if their successors coincide. The source weight is `weight i`, not an unrelated positive annotation in a triple. A flattened row certificate must prove its enumeration/source ID and third-field equality explicitly.

A sparse checker enumerates S_i once, obtains the label from each row, computes its four images, and checks target membership. It does not scan every possible row for every state. The generic representation theorem turns successful enumeration into the universal closure assertion above. There is no need to prove equality with the C program's reachable subsets, prove the hash table correct, or supply separate image-membership proofs as millions of theorem terms.

The intended Lean interface is schematically:

```lean
def check (c : Certificate m N) : Bool := ...
theorem check_sound (h : check c = true) : Valid c := ...
theorem physical_trace_accepted (h : Valid c) (hx : ClockedRightOrbit x) :
    Accepted c (visiblePrefix x n) := ...
theorem concrete_check : check frozenCertificate = true := by decide +kernel
```

This is a specification, not a compiled or checked Lean module. `check_sound` is a normal general proof; only the frozen finite check is decided in the kernel. Every imported auxiliary module must exist at the verifier's environment commit, or its needed code must accompany the submission.

## From closure to a quantitative physical theorem

Induct on observed letters. Root coverage starts the induction; labelled closure both rules out dead edges and maintains membership of the actual row in the automaton state. Therefore every physical visible prefix is accepted. Equality of reachable sets is never used.

Let A_i(n) count accepted n-letter words starting at live i, with A_i(0)=1 and A_i(n+1) the sum of the two live-successor counts (dead contributes zero). Let w_min be the minimum positive live weight. A second induction gives

```math
D^n w_{\min} A_i(n)\le R^n w_i.
```

The base is w_min <= w_i; the step is exactly the two labelled inequalities and obligation 5. Determinism gives at most one live path per word. Physical words form a subset of the accepted words, so, for any integer C with w_r <= C w_min,

```math
D^n N_{\mathrm{physical}}(n)\le C R^n.
```

For the original width-16 data, D=10^9, R=1159107281 and C=10310. These count visible bits, one every two physical times. A per-time entropy conversion divides the visible-bit rate by two. Nothing in this argument asserts that every abstract accepted word has an actual infinite right-half realization.

## Width 16 data size without a new run

Known values: N=2260, |R_16|=65536, and the reported mean nonroot subset size is 334.0, rounded to one decimal. Thus the estimated number of concrete row occurrences is

```math
K=65536+2259(334.0)\simeq820042.
```

Rounding permits 819930 <= K <= 820154, not an exact 820042 count. The present graph/vector JSON does not contain these represented sets; a future export or proved reconstruction would still be needed. This task has not generated them.

At two raw bytes per 16-bit row, the sparse sets use about 1.56 MiB before small offsets/metadata; graph, 64-bit weights and offsets bring a straightforward packed representation to roughly 1.60 MiB. A structural `All` root removes 128 KiB, but its outgoing closure still needs checking on all root rows unless separately proved symbolically. Decimal Lean lists are several megabytes and cost substantially more heap as syntax and proof expressions. Dense membership bitsets instead require 2260*65536 bits = 18,513,920 bytes, about 17.66 MiB, before metadata; the root can again be structural. Today's small weight tree contains **none** of this concrete-set data.

The sparse closure check performs about 4K = 3.28 million target-membership queries and, without caching, roughly 6K one-step row calculations. A membership trie over 16 row bits has up to 16 node visits per query, about 52 million visits; repeatedly selecting the target set through a 12-level state tree adds further overhead. These are algorithmic estimates, not measured Lean reduction counts. In comparison the width-16 arithmetic proof has only 2260 inequalities and 4520 weight lookups. Its 8.5 s or cold 18.8 s timing cannot bound the closure workload.

**Budget verdict:** no defensible four-minute promise follows for the naive full sparse/trie checker. A small generic proof term avoids a huge explicit proof witness, but its kernel decision still has to process the finite data. Symbolic set representations, bit-parallel closure or a proved generator could improve this; none has a measured or proved size/time bound here. Claiming they fit would repeat the earlier inference from graph size to verifier cost. Width 16 remains the right first feasibility target, conditional on a separately authorized implementation and measurement, rather than an automatic run from this task.

Hand scope controls: omit root coverage and the empty sets pass vacuously; omit closure and a one-state zero-successor graph falsely bounds arbitrary physical words; omit label multiplicity and two loops are counted as one; let row annotations float and an oversized annotation hides a bad source inequality. The unexpected timing check is that using Lists plus a tree solves weight access but does not encode or certify concrete-row membership. All are statement-level controls, not experiments.

**Disposition:** complete finite proof obligation and no-run estimate delivered. A real checker would discharge the layer bridge if its concrete check passed with the generic soundness and weight lemmas; neither that implementation nor its verifier budget has been established here.
