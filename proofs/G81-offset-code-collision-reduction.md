# offset-code collision reduction

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT81. offset-code collision
reduction (second-read by Local, 2026-10-06)"; rebuild with `python3 proofs/build.py`. Edit the proof in PROOFS.md
and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

Whether two surviving Collatz numbers can ever meet reduces to a finite check on step patterns.

**What it says.** Two numbers that survive with the same number of odd steps a and meet at the same value exist
exactly when two allowed step patterns of a fixed length have offsets equal modulo 3^a. GPT showed this, built the
two meeting numbers explicitly when such patterns exist, and showed that no meeting is possible below a = 7.

**Why it matters.** It replaces an open-ended search over numbers with a finite search over patterns for each a,
which GPT has set out in advance.

**An everyday picture.** Instead of watching every car to see whether two ever arrive at the same parking space,
check the finite list of routes on the map.

## The formal statement and proof

### G81. Reduce the admitted-collision question to offset residues (2026-10-06)

Reply to Local L040. Absence of a collision in both finite start samples is not a singleton theorem. There is a finite coding question for each odd count that avoids a larger actual-start scan.

Fix a>=1 and t_a=floor(log_2(3^a)), computed as bit_length(3^a)-1. Let W_a contain every length-t_a coefficient-admitted parity word with exactly a ones. For each word use its affine intercept B. Then a pair of distinct words in W_a with equal B modulo3^a exists if and only if there exists a same-odd-count admitted terminal collision (at some horizon and within a common dyadic width). In particular this is equivalent to a collision somewhere in G73's width/horizon domain, where the terminal labels the odd count.

**Necessity and reduction to one horizon.** If two admitted starts meet after t steps with odd count a, their affine equations give

    3^a*(n'-n)=B-B'.

Their words are distinct, since the same affine map is injective in the start, and offsets agree modulo3^a. Admission implies t<=t_a. Pad both words with zeroes to length t_a. Their intercepts and odd counts stay unchanged and their coefficient prefixes remain admitted. These are abstract parity words; padding need not be the continuation of the original starts. The coding collision persists.

**Sufficiency and explicit realization.** Conversely take distinct words in W_a with intercepts B,B' congruent modulo A=3^a. Put M=2^t_a and delta=(B-B')/A. The offsets cannot be equal: equal A,B at this common length would give the same least parity representative, hence the same word. Thus delta!=0. Both intercepts are odd, since admission forces first bit1, so delta is even. G72's offset bound gives abs(delta)<a/3<M.

Let r=(-B*A^(-1)) modulo M be the least representative of the first word. Choose n=r+2*M if delta>0, and n=r+3*M if delta<0; put n'=n+delta. Both lie in[2*M,4*M), have the same width t_a+2, and are distinct positive odd integers. The residue congruence for B' holds because A*n'+B'=A*n+B. Thus they realize the two prescribed words by the parity bijection, and their terminals are equal. They are coefficient-admitted through t_a, and t_a<=3*2^(t_a+1), so this witness is within G73's domain. No actual-survival or prize solution is implied.

This also recovers L040's lower threshold: delta is a nonzero even integer and abs(delta)<a/3, so a>=7. For a<=6 the offset residue map is injective. For higher a its injectivity is an open coding question here. G73's short-label theorem does not prove it.

**Unexpected admission guard.** The unrestricted words101000000 and100000001 have a2 and intercepts7 and259, equal modulo9. They realize the recorded625/597 collision, since(7-259)/9=-28. Both first fail the coefficient barrier at step2 (their first two bits are10); neither belongs to W_2, whose maximal admitted horizon is3. Thus a modular collision below a7 does not refute the admitted threshold. This guard also distinguishes abstract padding of admitted words from extending a nonadmitted word backwards into the set.

**Next finite search, preregistered NOT RUN.** CI1: enumerate W_a for a1..12 using increasing odd positions with p_i<=floor(i*log_2(3)); independently check full-prefix admission and compare affine-recursion intercepts with the position sum. Require no residue collision for a1..6. CI2 blind prediction: no residue collision for a7..12; retain a refutation, and if one occurs construct and directly evolve the two witness starts above before asserting an admitted collision. Report word counts and all colliding residue groups (or their absence), without extrapolation. Independently check the unrestricted7/259 guard and its first deficits. Counterfactual: admission can be omitted from the a>=7 threshold; must fail on that guard. This is a small finite word-code search, not a repeated Local start population or a large compute job. The lemma uses the recorded Terras parity bijection and affine/barrier identities; no novelty claim. Independent Local reading requested.


### G81 offset-code outcome (2026-10-06)

CI1 checks all68722 fixed-cardinality position sets at a1..12 against independent full-prefix admission; exactly4403 admitted words remain. Counts by a are1,1,2,3,7,12,30,85,173,476,961,2652. Affine-recursion and position-sum intercepts and direct parity representatives agree. There are no colliding intercept residues in any of the12 classes. CI2 HELD: the blind no-collision prediction for a7..12 survives this complete finite search. Consequently, via G81, same-odd-count admitted collisions with a<=12 are excluded across widths and horizons, not just in one finite start interval. This is an exhaustive finite code verification with an analytic reduction; it is not an all-a singleton theorem or an asymptotic rarity estimate. G73's domain additionally ensures any terminal collision has the same odd count.

The unrestricted guard independently gives intercepts7/259, common terminal11 and first deficits2 for both starts625/597, refuting omission of admission. No collision witness could be constructed in this population because no code collision occurred; the constructive branch therefore remains empirically unexercised. Probe: `tests/probes/prizes/collatz_gpt_offset_codes.py`; predictions at9a9a46d (published via050f51c), GPT's Intel host, Python, under1 s. The first included-word pass was followed by the full excluded-set completeness control to check enumeration coverage; both passed. Independent Local reading and reproduction of the new reduction remain requested.

*Second reader's note on G80 and G81 (Local, 2026-10-06; chat L043).* Both correct. G80: with $a \ge \ell_{t+1}$ both
intermediate states are admitted, so $f_t(a) = (F(a) + 2F(a+1) + F(a+2))/4$, and a mixed pair's two contributions sum to the
second difference; the block accounting telescopes; the boundary guard shows why the condition is needed. Checked: the
two-step identity on all 6,376 admitted $(T, t, a)$ states with $T \le 30$, in exact rationals. G81: a collision gives
$3^a(n' - n) = B - B'$ and padding to $t_a$ keeps $B$ and admission; conversely $\delta = (B - B')/3^a$ is nonzero (equal
least representatives would give equal words), even (every admitted word starts with 1, so $B$ is odd) and below
$a/3 < M$ in size, so $n = r + 2M$ or $r + 3M$ and $n' = n + \delta$ realize both words with equal terminals; the 7/259 guard
checks. Checked independently with my own enumeration (`collatz_audit_g67_g69.py`, G81 part): the counts $|W_a|$ for
$a \le 12$ agree with GPT's, and **the search extends to $a = 17$** ($|W_a|$ = 8045, 17637, 51033, 108950, 312455 for
$a = 13$ to 17) **with no offset-residue collision**, so by G81 there is no same-odd-count admitted collision for
$a \le 17$ at any width or horizon.
