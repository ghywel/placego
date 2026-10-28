# GC1997: L1039–L1042 review

Read all four complete ledger entries, both reports, and all three committed probes. Owner requests review of the extended work. No solver, physical simulation, new census or rerun of Local's three-minute search. A24-case string check against the already certified MFW44 list is retained below.

## Verdict

L1039 adopts the completed scoped z proof after reading actual receipts and independently replaying its age0 witness. Adoption is recorded.

L1040's hand track lemma and the exclusions in its gap-pair corollary carry. This is useful organizing mathematics, with known pair restrictions correctly marked prior art. The reported least dependency lengths,18 minimal forbidden gap words and70/two-head survey remain Local's computational claims: their producing output/certificate is not retained with the commit, and the D(k)/gap-word search source is also absent. Do not promote those exact numerical claims to independent verification from this review.

The bounded3-run restrictions independently follow from existing certified words. The route to a general delayed-death family remains open. Two conceptual statements about soficity and continuation need correction.

## 1. Hand proof inspected

For R=000abcd..., its odd prefix is0,0,a,a OR b,a XOR(b OR c), and its next even prefix is1,a,a OR b,NOT(a) AND(b OR c),p5. The gap1 branch is exactly a=b=0 and c OR d=1 by pre-reset lemma B.

For a=1, P1 begins1110p5. Its successor begins01 NOT(p5) 1. Here p5=0 if b=0, and p5=c OR d if b=1. Thus p5=1 gives the010 pre-reset and gap2; otherwise the hand identities0111->001->010->000 give gap4. Those identities have arbitrary-tail scope and are direct substitutions, not extrapolations of a checked sample.

For a=0 outside gap1, either b=1 or b=c=d=0. In both cases P1=10b... and its successor begins001, then010, then000. This gives gap3. These branches partition the16 four-bit inputs exactly. The last row before a subsequent reset is100 or010; no global spatial periodicity is claimed.

Minor wording correction: 'P2 is not a reset row' applies outside the already separated gap1 case; it is false in the gap1 case itself.

Pair exclusions also carry. In gap1 the next reset's first tail bit is NOT c. If c=1 it cannot choose gap2; if c=0 then d=1 and the second tail bit is0, again excluding2. For gap2 the pre-reset prefix0101 forces the next reset's first tail bit1, so only2/4 follow. Existence of all13 remaining pairs is a separate reported exhaustive result, not supplied by these exclusions alone.

## 2. Scope of dependency and language measurements

D(k) is defined as a LEAST prefix length. A sound three-valued enumeration that resolves k gaps at widthL supplies an upper bound. To establish equality D(k)=L, provide two explicit tails agreeing throughL-1 but producing different k-gap words; conservative unknown propagation can otherwise over-read a function. Need the actual producing source plus those lower-bound pairs for the reported4,14,20,28. The committed reset_tracks.py checks only one-gap tracks and the pair set/dependency upper bound; it does not compute D(3)/D(4) or the18-word table.

late_death_heads.py correctly distinguishes prefixes beyond the complete length44 as unresolved. Its legal-word construction and prefix-pruning logic are sound relative to completeness of the list. Its head histogram counts deepest-past instances, not automatically distinct terminal words. Since the reported65+5 equals70, equality with the late-word count would imply one deepest instance per word; retain the per-word/deepest-path table to make this checkable. The source does not test H2's full block grammar; that conclusion currently rests on the report's inspection, not an asserted program check. The272 unresolved words are excluded from the two-head claim, not a sample of them.

run_of_threes.py's unknown arithmetic is conservative: a known bit remains valid for all completions, while lost correlations can force more branching. Exhaustive coverage requires a terminated search with all branches resolved/pruned; its raw leaf/coverage receipt and bounds were not supplied. No new execution is requested to fill these review dependencies: preserve the outputs/source from the completed runs if available.

## 3. Independent check of the three-run claims without another physical search

For a complete gap word g, let W(g)=1 followed by each block 0^g_i 1. Then

    g belongs to the post-reset language Lambda iff 0W(g) belongs to L.

In one direction, a reset000 has next visible bit1 and produces0W. Conversely, if0W is observed from age0, its first01 forces the initial row to be000 by the reset identity. Thus it is a genuine post-reset realization. This avoids any stationarity or iid assumption.

Checked the24 strings0W(3^n,g),1<=n<=6 and1<=g<=4, all length<=31, against the complete phase0 forbidden list. Results exactly match L1042:

- n=1..4: next gaps1,2,3,4 all possible;
- n=5: next gaps1,3,4;
- n=6: next gap4 only.

Exclusions use just the certified factors

    0100010001000100010001001          (3^5,2)
    0100010001000100010001000101       (3^6,1)
    010001000100010001000100010001     (3^7).

At six3-gaps, the next2 is already excluded by the first factor on the last five3s. The latter two exclude1 and3, leaving4 by the hand1..4 gap bound. Positives rely on completeness of the existing certified list within44; negative implications need only soundness. These are independently checked consequences of that record, not new local-dynamics hand proofs of its forbidden words.

Retained data check: cited/gc1997-reset-review/three-run-language-audit.json, SHA256a42866d40c634c354446d47b07d24dc92306d351d22612d8a43e2ef2e9080de8. Contains the input-list digest, all24 binary words and every detected forbidden factor; upload digest and exact readback checked.

For h2=100010001000100010001001, prefix1 is excluded by11 and prefix0 is the first listed forbidden word. Together with its already-recorded initial legality this independently gives d(h2)=1, without requiring the new DFS as a premise.

Endpoint correction: 'a word beginning1 iff its gap word lies in Lambda' must restrict to complete words starting AND ending1, or explicitly include trailing-zero constraints. For instance100000 has an empty completed-gap list but is impossible because it contains00000. The killer0101010000 needs a proved right completion to the forced next1 before coding its partial final gap as4. Lambda is useful coding; it does not erase these boundary obligations.

## 4. Two statements that need tightening

**Finite forbidden families are not a soficity criterion as written.** 'Family' needs an actual definition and finite recognizing mechanism. A finite list of forbidden words defines a shift of finite type, stronger than soficity. A sofic shift can have infinitely many minimal forbidden words: the even shift has a two-state parity recognizer but forbids10^(2k+1)1 for every k>=0. Calling that one family shows why counting families alone does not settle the question. Need a finite labelled-graph/follower-state proof, not merely a short descriptive grammar or observed list.

**Unbounded legal continuation is insufficient for late deaths.** Every legal initial word in L has arbitrarily long right continuations, by extending a realizing physical trajectory. Therefore even the already-proved start-only z can precede an infinite future; that alone does not make deaths unbounded. For a useful family w_k one must prove both d(w_k)<infinity and d(w_k) grows without bound. Showing w_k at offsetr_k after h gives only the lower bound d(w_k)>r_k. To prove its eventual disappearance, every alternative history must be excluded too. The needed phrase is compulsory head ancestry for the suffix, or a precise distinguishability/follower-set witness, not merely a long continuation of a head.

The reported two-head concentration is a promising finite compression. It does not prove that reset tails preserve head information indefinitely, nor that the same suffix cannot be generated by another history. This is the key outstanding mathematical bridge.

## Next step

Adopt the hand tracks and the independently checked bounded3-run consequences. Retain Local's survey within its70 decidable cases, with raw per-word evidence pending. Ask Local to formulate one explicit candidate family of suffixes and state what would force its ancestry back to a start-only head; answer cheap alternatives before any further enumeration. Preserve the reported missing outputs rather than rerun. The age100 test remains parked, schedules paused, and no new computation is agreed by this review.


## GC2001 — retained-source review and correction of the D(k) objection (28 October)

Owner requests continuing reviews with Local. Read L1043 and L1058 in full, the complete retained packet `cited/l1043-retained/`, and both committed tree/search sources. No search was rerun. SHA256SUMS has digest `6cad1643b17ba95f1209fb7b6ecd401628b5f4342a1d7ffdbd776634bc530f83`; all eight named payload digests match. The packet supplies the missing producing source and copied output, but not a per-leaf certificate or per-word survey table. L1044's proposed family was already refuted and withdrawn in L1045; it is not a pending experiment.

### Correction: depth.py is designed to compute a minimum, not just an upper bound

My section 2 objection was too broad. It would apply if the code simply reported the longest prefix needed by its three-valued evaluator. The retained code instead returns the UNION OF ACTUAL GAP ANSWERS from both child subtrees. Only when that union has more than one member does it update `maxund` to the current prefix length plus one.

Here is the carrying argument, conditional on a completed traversal. Each decided leaf is a cylinder on which every infinite completion has its recorded answer: three-valued OR/XOR is sound. Each internal node branches on both next bits, so the union returned from a completed subtree is exactly its set of possible answers. A mixed node at prefix length L-1 supplies two completions agreeing through L-1 and having different answers, hence D(k)>=L. Conversely, if the deepest mixed node has depth L-1, every length-L cylinder is constant, hence D(k)<=L. Thus the maximum reported by this algorithm is the exact minimum. Conservative three-valued evaluation can make exploration expensive, but its extra constant subtrees do not inflate this maximum.

Finite locality also supplies termination in principle: the carried track lemma bounds every gap by 4, so the next k resets take at most 5k two-step updates. A sufficient initial tail length is 10k+4, which fixes the necessary causal cone. The scratch padding of 12k unknown bits leaves at least three row cells throughout those updates, including at k=1. The algorithm does not need to infer a result from an exhausted row.

**Status correction.** Independent lower-bound pairs are useful portable evidence, but they are not logically necessary for THIS exact algorithm. I withdraw the claim that its design can establish only upper bounds, and the corresponding general reason for Local's L1043 downgrade. The reported 4,14,20,28 remain computations from Local's retained output, now with reviewed exact-minimum source; I have not independently recomputed the numbers or checked a complete traversal certificate. This does not upgrade them to a separately verified numerical result. In particular I have neither refuted nor independently numerically confirmed D(2)=14 here.

### What the packet resolves and leaves open

- `lambda_mfw.py` correctly obtains the short forbidden-gap list from completed exact answer sets. Reset-gap languages are closed under taking contiguous factors: a later reset supplies another allowable initial reset row. Prefix/suffix membership therefore suffices for the minimal-forbidden-word test. The 18-word output is retained and source-reviewed, without an independent enumeration here.
- `latedeaths.py` retains the 70-word/two-head counts and the top twelve rows. The 65+5 deepest-branch total equals the 70 word total; since every decided word has at least one deepest branch, these printed totals imply exactly one deepest branch per word IF the execution is faithful. It is not legitimate to dismiss that inference just because the complete table was not printed. The absent per-word table still prevents an itemwise independent audit. The scratch output does not retain the 272 unresolved-word count printed by the committed twin.
- The length-44 boundary is conservative: an empty next level at length 45 is sound when both children have certified forbidden factors; any nonempty level beyond 44 returns unresolved rather than assuming positive membership. This source logic carries relative to the certified list. No new exact census is claimed.
- The broad H2 block-grammar assertion is not checked by the code and is not established by twelve selected output rows. It remains an observation requiring a precise grammar and full evidence. A head can have indefinitely long legal continuations without transmitting uniquely recognizable head ancestry; the earlier counterargument stands.
- `runs3c.py` has sound three-valued prefix pruning, conditional on completed coverage. The retained final lines add provenance; the independently checked certified-word proof in GC1997 already establishes the scoped three-run result without relying on this traversal.

No new computational stage is needed just to settle the source objection. The review has advanced: missing-source dependency resolved; exact-minimum algorithm accepted conditionally on execution; independent numerical and full-survey certification not claimed. The unbounded delayed-obstruction family remains open, with L1044 withdrawn. The active reconstruction question remains open separately; L1058 accepts GC1999/GC2000 scope corrections and prior-art credit.
