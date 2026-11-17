# the shifted barrier, a closed shortcut

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT86. the shifted barrier, a closed
shortcut (second-read by Local, 2026-10-06)"; rebuild with `python3 proofs/build.py`. Edit the proof in PROOFS.md
and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

A tempting shortcut fails: the end of a surviving path need not survive on its own.

**What it says.** One might cut off the first few steps and apply G83's result to the rest. But early odd steps
build a cushion that later even steps spend. GPT gave a 33-step pattern that survives as a whole while its last 27
steps, taken from a fresh start, would not.

**Why it matters.** It stops an invalid argument before anyone relies on it. The rest of a path must be judged with
the cushion carried forward.

**An everyday picture.** A walker who climbed a hill first can walk downhill for a while and still end above home;
the downhill stretch on its own would not.

## The formal statement and proof

### G86. Removing the common odd count does not preserve admission (2026-10-06)

A tempting continuation of G85 would reduce a = 21 collisions to the already excluded smaller odd counts by restarting after a short common-count prefix. This route fails: the coefficient barrier carries accumulated slack, and a suffix is not generally admitted relative to its own starting time.

In G85's possible sixth-bit branch(1,0), both trajectories have accumulated five odd steps after six steps. Their new states differ by 14: from w'=3*w+29, the odd/even updates give (3*w+1)/2 and (3*w+29)/2. If they eventually meet with a = 21, the remaining27-step suffixes have16 odd steps. But3^16=43046721<2^27, so neither suffix can satisfy the fresh coefficient barrier even at its endpoint. G83's cutoff through 20 cannot be applied to those suffixes. This is conditional reasoning, not an assertion that this collision branch exists.

The correct suffix condition after a prefix of length s and odd count j is

    3^(j+a_k)>=2^(s+k),

rather than3^a_k>=2^k. It depends on the accumulated prefix ratio. A fresh-admission injectivity proof is not thereby an injectivity proof for all such shifted barriers.

**Unexpected explicit slack guard.** The word 110111 followed by 16 ones and11 zeroes has length 33 and21 ones. Its first six coefficient prefixes are admitted; the subsequent ones increase the coefficient ratio, and among the trailing zeroes the endpoint is the smallest ratio, with3^21>2^33. Thus the full word is admitted. Its27-bit suffix1^16 0^11 first fails the fresh barrier at step 26, since2^25<3^16<2^26, while it remains admitted against the shifted barrier. This is an abstract parity word, realizable by the recorded parity bijection; no meeting pair is implied. Starts27/31 realize G85's six-bit branch and have new states 107/121, illustrating the displacement14 without claiming that they meet.

**Next control, preregistered NOT RUN.** SR1: exact prefix tests of this full word and suffix, require full admission, shifted suffix admission and fresh suffix first deficit26; direct27/31 six-step guard must give odd counts5/5 and states 107/121. Counterfactual that restarting preserves fresh admission must fail. No extended collision enumeration. Record this as a closed shortcut, not closure of the shifted-barrier problem or the original singleton question.

*Second reader's note on G85 and G86 (Local, 2026-10-06; chat L046).* Both correct. G85's affine relations
$u' = 3u + 14$, $v' = 3v + 20$, $w' = 3w + 29$ re-derived; the forced prefixes are vacuous at $a = 21$ and hold for
all five $a = 22$ pairs (11011 / 11111, lower start $27 \bmod 32$). G86 closes a real shortcut: the suffix condition
is $3^{j + a_k} \ge 2^{s + k}$, not a fresh barrier. Checked (K6): the 33-bit word is admitted; its 27-bit suffix
first fails the fresh barrier at 26 and is admitted against the shifted one.
