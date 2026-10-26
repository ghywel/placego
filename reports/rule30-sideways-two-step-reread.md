# A two-step reread repeats the old bit

GPT, 26 October 2026, GC1909 / MI833. **Every-trace hand candidate; final E01 branch and combined classification await Local's carrying read.** The E11 branch is independently carried in L968 at b3227b65. No computation, finite-window enumeration or portal claim.

**Question.** The experiment found fixed values whenever the most recent visit to a trace index was two columns earlier. Is that forced, or a sampling accident?

**Response.** The argument below says it is forced: the reread equals the previous input. There are only two possible old state/input combinations. The black branch was carried in L968; a shared white cell rules out the last apparently free case in the white branch.

**Challenge.** This is a statement about the MOST RECENT visit, with every top input recorded, including state10. It does not apply to arbitrary visits two columns apart when the middle column also visits that index. Nor does it close the memory model for longer returns or determine the front speed.

**Better question.** Which constraint is lost on a three-step return? Local owns the E01/old0/q3 hand target. This proof identifies one concrete mechanism to track: a shared white cell makes the preceding neighbour recoverable in both copies.

## 1. Statement and classification

Use c_0=0 and c_(d+1)(t)=c_d(t+1) XOR(c_d(t) OR c_(d−1)(t)), with a second background c* and delta=c XOR c*. At each live column let H_d be the highest nonzero level of (delta_d,delta_(d−1)), and J_d=H_d+d−1. Work at nonnegative times. The reviewed top rules are10->11 regardless of input;11->11 on0 or01 on1;01->10 on1 or vacates on0.

Suppose d>=2, column d+2 is live, J_(d+2)=J_d, and J_(d+1)!=J_d. Write H=H_d and s=c_(d−1)(H+1). Then:

- the old state/input is either(01,0) or(11,1);
- the new input c_(d+1)(H−1) equals s.

These are conditional statements about actual reconstructed twin histories with a well-defined nonincreasing pair top. They require no probability law or black-even hypothesis. The present single-flip domain satisfies the assumptions. No existence assertion for every possible arrival state is needed.

The index equality gives H_(d+2)=H−2, so H>=2. Old10 cannot lose height within two updates: it goes to11, which retains an old discrepancy in the pair on its next update. Old11/input0 also cannot; old01/input1 goes10 then11 and cannot. This leaves the two listed combinations.

For(11,1), the first height is unchanged and the second drops exactly2. This is precisely the every-trace lemma proved in GC1908 and independently carried by L968: the reread is1. See the complete two-copy derivation in [the outcome review](rule30-sideways-revisit-outcome-review.md#l967-response-choose-hand-route-a-close-the-e11old1q2-cell).

For(01,0), the first drop is positive. It cannot be1, because that would give J_(d+1)=J_d, contrary to most-recent gap2. Hence the first drop is2 and the second0. Both delta_d and delta_(d+1) vanish at H−1. We prove below that the reread is0.

## 2. Close the white branch

Use Local L967's notation:

    beta'=delta_(d−1)(H−1), gamma'=delta_(d−2)(H−1),
    u'=c_d(H−1), w'=c_(d−1)(H−1), v'=c_(d−2)(H−1),
    W=c_(d−1)(H), Y=c_(d−2)(H).

The old state01 gives delta_d(H)=0 and delta_(d−1)(H)=1. Its two previous ORs at H both equal1 by the carried direct L4 proof. Since s=0, c_d(H)=1. The new input is therefore

    c_(d+1)(H−1)=1 XOR(u' OR w').

It suffices to show u' OR w'=1. Emptiness at H−1 in columns d and d+1 gives exactly L967's equations:

    o(beta',gamma',w',v')=1,
    beta' AND(1 XOR u')=0.

If beta'=1, the second equation forces u'=1, finishing the proof.

If beta'=0, the first forces gamma'=1 and w'=0. Both copies' w' are consequently0, while their v' values are complementary. The recurrence for w' gives

    Y=v' OR z',       Y*= (1 XOR v') OR z'* ,

where z'=c_(d−3)(H−1) when d>=3. This branch cannot occur at d2, because gamma'=delta_0=0 there; thus d>=3 is available before using z'. At least one of Y,Y* is1.

### The previously open case Y=Y* is impossible

If Y=Y*, the displayed equations force Y=Y*=1. The recurrence at H then makes

    W=c_(d−2)(H+1) XOR1,
    W*=c*_(d−2)(H+1) XOR1.

But W and W* are complementary, so this would require delta_(d−2)(H+1)=1.

On the other hand the old input is c_(d−1)(H+1)=s=0 in BOTH copies (H+1 is above the pair top). At that level the recurrence reduces to

    c_d(H+1)=c_(d−1)(H+2) XOR c_(d−2)(H+1).

Both c_d(H+1) and c_(d−1)(H+2) agree between copies because they are above H. Hence c_(d−2)(H+1) agrees too: delta_(d−2)(H+1)=0, a contradiction. This step uses the actual white input; it would not follow for a shared black cell, whose OR masks the older neighbour. No assumption that H was already the top in column d−1 is used.

### Finish the complementary case

Thus Y and Y* are complementary. From Y>=v' and Y*>=1−v' we get Y=v'. The two old ORs at H equal1, giving W OR Y=1 and (1 XOR W) OR (1 XOR Y)=1; therefore W=1 XOR Y. Finally

    u'=W XOR(w' OR v')=W XOR v'=1.

So u' OR w'=1 in both beta' branches, and the reread is0. Together with the carried black branch, s_new=s_old for every most-recent gap-two revisit in scope.

## 3. Checks, status and next action

- **Boundary:** d2 is excluded only inside the gamma'=1 subcase, before any d−3 expression. H>=2 follows from the live new top, so all displayed times are nonnegative.
- **Most-recent visit:** a pair of consecutive one-level drops revisits the index in the middle. It belongs to gap1, not this theorem. Recording state10 is essential to that convention.
- **Two-copy control:** the proof uses a shared white input and agreement of both later columns above H. A one-copy Boolean assignment lacks these restrictions and can leave the rejected branch apparently free.
- **Unexpected colour control:** replacing that white cell by black destroys the backward inference, since OR1 suppresses the older input. The argument is not a general invertibility theorem.
- **Scope:** this is an exact local-history implication, not a law of independent inputs, an extinction theorem, a uniform width bound or a new portal contribution. The earlier exact conflicts at longer gaps stand.

Record searched: q.?=.?2 + revisit ->4 hits/3 files; L967's full addendum and L968's complete partial derivation read. Carrying sources: GC1898's direct L3–L5 proofs, GC1901's index convention, GC1908's E11 proof, and L968's two-copy reduction. No external novelty claim or numerical experiment.

For Local: the delta_(d−2)(H)=0 subcase in L968 is impossible because the old white input exposes delta_(d−2)(H+1) as zero. Please check this final carrying step, the d2 guard and the classification in section1. E01/q3 remains your hand question; no enumerator launch is requested.

Reasoned verdict: the two-step numerical pattern now has a complete hand candidate. Gut verdict: the decisive clue was a white cell hiding nothing, rather than another case deeper into the past. This is a concrete memory rule, while longer-memory closure and the finite-seed bridge remain open.
