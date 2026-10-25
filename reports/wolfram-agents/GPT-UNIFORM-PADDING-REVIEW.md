# Uniform white padding: actual family and certificate bindings

GPT, GC1857/MI790, 2026-10-25. **Scoped source/hand and file-binding PASS.**
No Lean, strip transition, certificate evaluation, evolution or benchmark run.
This fills the concrete pumping-family coverage gap after GC1853's generic
machinery read; it does not certify every tail or give an all-width bound.

## Exact evidence

Pin: **3eca23c0a9fa6b153313655e6d51835406c2d06e**.

| Source | Read coverage | SHA-256 |
|---|---|---|
| [Rule30UniformWhitePadding](https://github.com/WolframInstitute/Rule30PrizeKit/blob/3eca23c0a9fa6b153313655e6d51835406c2d06e/lean/Ruliology/CellularAutomata/Rule30UniformWhitePadding.lean) | All121 lines/5022 bytes, all bodies | 222f44a949c36bed5fc9d7f42aa8dd90b78d606f756fb8d13e5851c400dd252f |
| [Certificates/WhitePaddingFamilies](https://github.com/WolframInstitute/Rule30PrizeKit/blob/3eca23c0a9fa6b153313655e6d51835406c2d06e/lean/Ruliology/CellularAutomata/Rule30Certificates/WhitePaddingFamilies.lean) | All semantic definitions/declarations/proof bodies across1136 lines/590327 bytes;156 decimal mask literals parsed as data | a9d248f211ee0870399d85a6a88858515a9518c208d90aa5c33dfdefaf6606ed |

The semantic reading view replaces long decimal literals with their digit
counts; it leaves every statement and proof body intact. The raw source is
retained. No manual comparison of thousands of decimal digits is claimed.
The file-only audit checks all156 masks fit their declared state-set widths,
nine tail lists, five wrapper parameter bindings and all109 cached Heavy111
step indices (28+49+32). It does not check that a stated image equality is true.
Kernel-decided premises were read, not independently replayed.

Also rechecked all128 lines of `Rule30WhitePadding` (SHA256
`c77ac2494c20b6fecd8302ec6d69ed9d52f5590ae648e657b4e7e95da8f44734`)
and the carrying encoding/eventual-word/uniform-soundness bodies of previously
read `Rule30FiniteStrips` (226 lines, SHA256
`3722ce539aff889e63eaeb3929e283299c3be8015a1f5c578c30803840983acd`).
The existing strip abstraction and uniform masked-Jen theorem keep their
prior source-review scope; no imported-library kernel replay claimed.

Eight fixed payloads/readbacks: `cited/gpt-uniform-padding-review-20261025/`,
both new sources, both dependencies, audit script/JSON, semantic reading view,
record search. Record searched: `UniformWhitePadding WhitePaddingFamilies`
-> no hit including ledgers. Public catalogue03:54:20Z unchanged38 entries.
Known-source review only; no startup execution/check pass or new proof status.

## Five explicitly uniform families

For every configuration x with a leftmost black cell lo, every integer column
i, and every r>=N, the column cannot eventually repeat `0^r u`:

| Family | Tail u, in temporal order | Strip width K | Padding threshold N |
|---|---|---|---|
| A | 101011 | 6 | 13 |
| B | 1101 | 7 | 14 |
| C | 11101 | 9 | 23 |
| D | 101 | 9 | 23 |
| E | 1111 | 10 | 31 |

These are the actual five `no_padding*_leftFinite` declarations. They require
x(lo)=black and x(p)=white for p<lo. They allow an arbitrary, even infinite,
right tail. Nonzero finite configurations are included, but finite right
support is not an assumption. Column and transient are both unbounded.
K is the observed neighbour-strip width, not the support width of x.

## What pumps a finite check to all larger r

Starting from ALL K-bit strip states, the first full word reaches S1 and the
second reaches S2. Three separately checked zero evolutions stabilize by N:
the full set, S1 and S2. `zeros_stable` inducts from equality at N,N+1 to
equality at every r>=N. `padding_strip` then proves `stripCert(0^r u,K,2)`:

- two whole periods reach S2 for every permitted r;
- one further period returns into S2;
- every white phase forces a constant neighbour head, including all phases
  of arbitrarily long padding and the finite tail u.

`Forces` is a disjunction: the neighbour head may be constantly white OR
constantly black. It is not a vacuum-set assertion. The forcing head may
differ with the word phase. Sound strip reachability includes BOTH unknown
far-boundary bits at every step; it does not pick a favourable right history.

Given a hypothetical eventual driver word, the actual strip is in these sets
after two periods. White-phase forcing makes the driver's OR with its right
neighbour periodic with the word. Uniform masked Jen contradicts this in a
configuration with a leftmost black cell. This is the carrying physical
argument, rather than a claim that finite reachable sets enumerate all initial
configurations. Nonempty words and positive K are discharged explicitly by
each wrapper; the transient advances by two word periods, not a fixed2 steps.

Unexpected endpoint check: when r=N+1, the position j=N is still WHITE padding.
Its obligation uses `Forces(zeros N S2)`, the stabilized endpoint. Hence the
prefix check correctly uses `List.range(N+1)`, including N. Replacing it by
`range N` would leave this case uncovered. This is a proof-obligation control,
not a counterexample to the family theorem.

## Other declarations in the combined certificate

The bundle also contains vacuum-free suffixes011 at K5,001001 and111001 at K6;
these assert that the vacuum is absent after the suffix from the full set.
They are finite suffix statements, not the five uniform wrappers above.

Cheap tails F..I have the same three-set pumping architecture, with existing
single-seed `no_padding` declarations:

| Tail | K | N |
|---|---|---|
| 1 | 8 | 21 |
| 11 | 6 | 11 |
| 1001 | 8 | 22 |
| 1011 | 6 | 13 |

The Heavy111 component has tail111, K14, N49, with an explicit generic
`strip_certificate` and single-seed exclusion. Its full-set chain stabilizes
at28, S1 at49 and S2 at32. The final proof uses common N49 through
`zeros_stable`; full-set stabilization at28 alone does not justify lowering
the common threshold to28. All cached step/reach dependencies were read and
their index bindings checked; no cached transition was recomputed. These are
sufficient thresholds, not asserted sharp ones.

Uniform `FiniteStrips.not_eventually_word_strip` can consume any proved
stripCert, including Heavy111's explicit certificate. That known generic
composition needs no new experiment; a newly compiled uniform wrapper for
the extra components is not claimed here. No additional universal-tail
certificate-existence result follows from having ten named families.

## Limits and verdict

Hand scope control: for the alternating word01, the tail1 representation has
r=1, below N21; none of A..E has that tail, and Heavy111 is different again.
Thus arbitrarily large padding lengths in the theorem do not cover all short
periods or supply CQ01. The theorem excludes eventual infinite repetition;
it gives no deadline for how long a finite matching trace may last and no
all-width D(W) bound. The all-white configuration is also outside the leftmost
BLACK hypothesis, so zero-input periodicity is no counterexample.

Reasoned/gut: exact bindings and unbounded pumping carry, with no circularity
found. Review COMPLETE, known-source scope. Broader conservation exclusion
stays parked; local-template incubation and held lanes unchanged. No compute,
Local wake, new review request or schedule change.
