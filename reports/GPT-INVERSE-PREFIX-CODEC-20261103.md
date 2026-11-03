# The pair-stream inverse is a lossless prefix codec — GC2415

GPT, 3 November 2026. **PROVED two-party, hand**, Local L1353 carrying read
adopted in GC2418, conditional on the actual kit identities.
No Lean compilation or new enumeration. This is an application of an elementary
finite-prefix argument to the kit's actual maps, not a new general theorem
about reversible cellular automata.

## What is already known, and what is added

Record searched: the current kit c42f6e51 lean/equivalents/catalogs, portal and
open PR index; the record search for uninverse/prefix isometry; complete final
[PR86](https://github.com/WolframInstitute/Rule30PrizeKit/pull/86) metadata,
conversation/review lists and exact head32770177c045f07df77310ac5a23ee9a3b8ff039.
Its Rule30SeparatorEquivalences source is byte-identical to current main,
SHA256a6d7d4b0722a483d7f660b9c5b2a4c164ac07cc1030fbfe9a374f4f062f02daa.
PR75/76/84 comparisons are in the [C2 report](GPT-PR75-76-HYPOTHESIS-COMPARISON-20261103.md).

Known PR86 result: `uninverse (inverse e)=e`, hence inverse is injective.
Known WedgeBridge result: `inverse_prefix`, forward prefix locality.
The inspected declarations do not state the other composition or prefix
isometry. The following completes that specific map's dictionary, conditional
on those existing identities and with a short decoder locality proof.

The general prefix-permutation principle is classical. For a primary example,
[Anashin, section2, Note2.2 and Proposition2.3](https://arxiv.org/html/math/0602083#S2)
uses compatible finite-residue bijections to obtain a full bijection and
measure preservation; Note2.5 gives isometry. We use a four-letter prefix tree,
not a field of “4-adic numbers,” and prove the needed elementary statement
below. No priority is claimed for that principle.

**Pull.** Does reconstruction itself lose information, or does the hard-core
restriction do the work? A positive answer should replace an existential
stream search by an exact decoder test for each finite label word. Cheap
objection: a left inverse alone never proves surjectivity. The extra ingredient
here is causality of BOTH maps at exactly the same prefix length.

## Definitions, retaining the actual kit's indexing

Alphabet A={0,1,2,3}. A stream is a function from nonnegative integers to A.
“Agree through length n” means equal at indices0,...,n-1; length0 is vacuous.
Write F=`inverse`, D=`uninverse`, and T=`stepInverse` from the kit.

- boundary(q)=3-q;
- shift(v)(t)=v(t+1);
- lift(a,v)(0)=a and lift(a,v)(t+1)=unphi(lift(a,v)(t),v(t+1));
- T(v)=lift(unphi(boundary(v(0)),v(1)),shift(v));
- D(v)(j)=boundary(T^j(v)(0)).

The kit's stepInverseIter iterates T exactly as written. Its `inverse_prefix`
says that F's first n outputs use only its first n inputs. Its
`uninverse_inverse` says D(F(e))=e for EVERY four-letter stream.

## 1. Decoder causality: no extra output digit is consumed

If v and w agree through length m+1, T(v) and T(w) agree through length m.
For m=0 there is nothing to show. Otherwise their initial lift labels agree,
since v(0),v(1) are known. Induct on t<m. At t=0 this gives equal labels. To
advance from t to t+1<m, the lift recurrence consumes shift(v)(t+1)=v(t+2),
whose index is at most m, hence available. The previous lift values agree by
induction. This proves the claim for all m.

Iterating it, if v,w agree through length m+j, T^j(v),T^j(w) agree through
length m. Take m=1: D(v)(j) uses only v(0),...,v(j). Consequently v,w agreeing
through length n implies D(v),D(w) agree through length n. The apparent use of
v(1) in T's initial label causes no one-digit loss for D: output0 uses no T,
output1 uses one T and exactly two input digits, and so forth.

Endpoint checks by hand: F(e)(0)=boundary(e(0));
F(e)(1)=phi(e(0),boundary(e(1))). D(v)(0)=boundary(v(0)), and
D(v)(1)=boundary(unphi(boundary(v(0)),v(1))). The kit's two phi/unphi identities
verify both compositions on these first two symbols. No default tail is used
as mathematical evidence.

## 2. Finite-prefix permutations and the right-inverse identity

For each n, F and D induce maps F_n,D_n on the SAME finite set A^n. These are
well-defined by their respective causality; arbitrary completions give the
same outputs on that prefix. The existing identity D F=id implies
D_n F_n=id on A^n. Thus F_n is injective. Domain and codomain both have4^n
elements, so F_n is surjective, and therefore F_n D_n=id as well.

Now let v be ANY infinite four-letter stream. On every finite prefix n,
F(D(v)) has prefix F_n(D_n(v-prefix))=v-prefix. Two streams equal on every
finite prefix are equal. Hence

**F(D(v))=v for every v.**

Together with the already-known D(F(e))=e, this proves that these literal maps
are mutual inverses. There is no compactness selection, arbitrary diagonal
subsequence or unproved compatibility choice: D supplies the single stream,
and all prefix identities hold for that same stream.

Moreover, e,f agree through length n if and only if F(e),F(f) do. Forward is
known forward locality; reverse applies D's equal-length locality. In
particular the first disagreement index is preserved exactly. Equivalently,
with distance4^(-j) for first differing index j, F is a bijective isometry.
This says nothing about injectivity of Rule30's full one-step row update:
F is the specifically encoded inverse-cone stream map.

## 3. Exact separator criterion: a decoded language, not an unknown image

HardCore(e) means each e(j) is1 or2, and no pair e(j),e(j+1) is11. Because F
and D are two-sided inverses,

v belongs to F(HardCore) if and only if HardCore(D(v)).

The reverse implication is the addition to the already-known necessary
`hardCore_uninverse_constraints`: if D(v) is hard-core, use e=D(v) and
F(e)=v. Thus for each exact candidate v=liftWord(u,const c), c=2 or3,

no hard-core e has F(e)=v if and only if there exists j with
D(v)(j) outside{1,2}, OR D(v)(j)=D(v)(j+1)=1.

A witness at j uses at most the first j+2 symbols of v. The candidate v itself
is completely specified by the finite label word u and c; no additional
endpoint stream must be guessed. This is a full equivalence, not just a
one-sided rejection screen. It does NOT prove a witness exists for every u.
That all-word assertion is precisely the remaining separator question.

A concrete family-level target is now: prove that every normalized label word
u produces one of those decoded obstructions. A length-dependent bound B(m)
valid for all labels of length m would suffice. Conversely, if SEP holds,
there are only finitely many normalized u of length m, so a common finite
B(m) exists by taking their maximum obstruction index. This equivalence is
nonquantitative; it supplies no useful bound and no finite-state closure.
Do not replace it with an automatically enlarged label census.

## 4. A count consequence and its exact limit

Each hard-core prefix extends to an infinite hard-core stream (append2's).
Since F_n is a permutation, the number of length-n prefixes in F(HardCore)
is exactly the number of hard-core words of length n. Let h_0=1,h_1=2. Ending
in2 permits any previous hard-core word, and ending in1 requires the previous
symbol2, so h_n=h_(n-1)+h_(n-2). Thus h_n is Fibonacci number Fib(n+2).

For uniformly independent four-symbol input v, the probability that D(v)'s
first n symbols satisfy the hard-core test is therefore Fib(n+2)/4^n, and
F preserves the uniform four-symbol product measure by its prefix permutations.
The infinite hard-core image has measure0. This is a direct finite counting
consequence of the classical prefix principle, not a measurement or an
assumption that the actual seed is random.

**No separator conclusion follows from that zero measure.** The countable
family liftWord(u,const c) could lie inside a null set. Nor is this prefix
count automatically shift entropy of the image under the ordinary shift:
F conjugates the input shift to T, not to the ordinary output shift. Keep the
population, map and quantifiers explicit. This is exactly where a random
information argument could otherwise conceal the hard part.

## Next read and next question

The original carrying request on decoder locality and the finite F_n/D_n
argument is COMPLETE: Local L1353 read the actual definitions and every carrying
step. This promotes the stated hand result; no formal compilation is claimed.
If carried, these are small dictionary lemmas to use with the existing kit,
not a reason to recreate PR86's already-delivered package. No new posting owner
or package is being opened.

Next mathematics: derive a label-family obstruction for the exact decoded
candidate, keeping all label dependence; if its proposed finite summary is
not closed, identify the first missing dependency rather than increasing a
sample. Independent alternative remains the final A1/A2 packet reviews.

My own pull: the full pair-stream coordinate change forgets nothing at all;
the difficult information restriction is the physically allowed language and
finite origin, which a lossless encoding does not provide for free.
