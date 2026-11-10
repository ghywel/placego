# Unrestricted Tail Closing Fails on the Constrained Class of the Zero-Boundary Left Half: Three Eventually Periodic Rows of Rule 30

Gareth Herbert; Claude (Anthropic); GPT (OpenAI). 10 November 2026.

## 1. The statement

The kit's zero-boundary left half runs rule 30 beside a white wall (`Rule30ZeroBoundary.zrow`). Its constrained class `K = InX` consists of the rows whose depth `1` is black at every even tick. The kit's `Q01` asks whether `K` contains no finite row.

A *closing* property would let one recover a row of `K` from its future, up to a finite part. This module shows that the unrestricted form fails, using three eventually periodic rows read from depth `1`:
- `rowA` repeats `1011111`;
- `rowB` is `11` followed by repeats of `01001011001000`;
- `rowC` repeats `1100001`.

With `G` for two ticks:
- `two_A`, `two_B`, `two_C`: `G A = C`, `G B = C` and `G C = A`, at every depth.
- `inX_A`, `inX_B`, `inX_C`: all three are in `K`.
- `free_A`, `free_B`, `free_C`, `theta_A`, `theta_B`, `theta_C`: their free words, depth `1` at the odd ticks, are `1010…`, `001010…` and `0101…`. The kit's `Theta` recovers each row from its free word (`Theta_unique`).
- `differ_AB`: `A` and `B` differ at every depth `14 q + 3`. `differ_one_tick`: one tick later they differ at every depth `14 q + 4`.
- `not_unrestricted_closing`: so it is false that any two rows of `K` with the same row after one double step agree from some depth on.

## 2. The cycle

Two ticks at a depth `k ≥ 3` read the start only at depths `k - 2, …, k + 2` (`zrow_two`). So if the start is periodic from some depth on, an identity for two ticks at depth `k` carries over to `k` plus the period (`two_shift`, `periodic_ind`). The kernel checks one period of depths by `decide`, together with the small depths next to the wall. That gives the three identities at every depth.

## 3. Membership and free words

The even-tick rows from `A` are `A, C, A, C, …`, and from `B` they are `B, C, A, C, …`. Each of these rows is black at depth `1`, so all three starts lie in `K`. The odd-tick rows give the free words by the same induction. The kit's `Theta_unique` then identifies each row with `Theta` of its free word: `A` and `B` have different free words and the same image under `G`.

## 4. The failure, and what it does not touch

Since `A` and `B` differ at every depth `14 q + 3`, they agree on no tail of depths, while `G A = G B`. That refutes the unrestricted eventual-tail closing property on `K`. This is not merely an accident of choosing one double step: the kit's semiflow identity `zrow_shift` implies that the two runs agree at every tick from tick 2 on. They therefore also agree after every positive number of double steps.

The open [kit pull request 52](https://github.com/WolframInstitute/Rule30PrizeKit/pull/52) states guarded closing properties, `HomoclinicClosing` and `AllPastClosing`, proves them equivalent and relates them to a finite-support reduction. These assume that the gate streams are legal: every eight-bit window lies in a set of ten values. They are not contradicted. In that pull request's convention the gate words are the complemented even heads one tick later. For `F A` and `F B` these are `0` and `1` followed by the common future `1010…`, whose first window has the value `85`, outside the ten legal windows. The one-tick mismatch at `14 q + 4` (`differ_one_tick`) shows that the infinite difference survives that change of convention. This explicit pair refutes the unrestricted version obtained by dropping legality; it does not identify legality as the only possible sufficient restriction.

## 5. Worked numbers

The cell below checks, independently of the Lean module:
- the three two-tick identities on the first 600 depths;
- depth `1` black at every even tick for 40 double steps from each row;
- the first eight bits of each free word;
- the residues modulo `14` of the depths `d ≥ 3` where `A` and `B` differ, and that the difference is exactly those residues;
- the one-tick split at `14 q + 4`.

The mismatch set is the nine residues `0, 1, 3, 5, 6, 8, 9, 11, 12` modulo `14`, plus depth `2` (COMPUTED). The module proves the subsequence `14 q + 3`, which is enough for the failure.

## 6. Prior art and scope

- **The framework** is the kit's: `Rule30ZeroBoundary` with `zrow`, `InX`, `Theta` and `Theta_unique`.
- **The guarded neighbours.** The closest statements are in open kit pull request 52 (`Rule30GateTailReduction`: `HomoclinicClosing`, `AllPastClosing` and their equivalence under `GateLegal`). Also relevant is pull request 47's synchronizing-carrier families, which assume a synchronizing future and so exclude this alternating one. This module gives an explicit obstruction to unrestricted closing, rather than contradicting either guarded result.
- **What is not here.** The finite-row form of closing and its equivalence with `Q01`, carried by hand in our record, is not formalized. Nothing is said about legal gate streams. Nothing here decides `Q01` or period `2`.
- **History.** The three rows and their two-tick cycle come from our programme's swarm run (LN-03.1) as Cloud computed and carried them. GPT compared them with pull request 52 and translated the mismatch into its convention, and Local carried that step. A Local sub-agent formalized the module under Local's direction.
