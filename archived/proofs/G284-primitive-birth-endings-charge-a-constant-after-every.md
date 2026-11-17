# Primitive birth endings charge a constant after every fixed prefix

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT284. Primitive birth endings charge
a constant after every fixed prefix (second-read by Local, 2026-10-13)"; rebuild with `python3 proofs/build.py`.
Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

However a seed word begins, exactly three in four ways of finishing it with three or more squares, the last one
black, are accepted.

**What it says.** The record writes one family of possible births of white stretches in the left half as seed words:
strings of black and white squares, read one at a time by proof E1's rebuild of the row before, which remembers only
its last two squares and so has four possible states. A word is accepted if it ends in black and the rebuild's final
two squares are white then black (type Q) or black then white (type P), the two kinds of birth. Finish any allowed
start with three or more squares, the last one black: whatever the start, exactly three quarters of the endings of
each length are accepted, a quarter as Q and a half as P. Two free squares can steer the rebuild into each of the
four states in exactly one way, later squares keep the four equally common, and the final black square sends one
state to Q, two to P and one to rejection. With only one or two squares to finish, the share depends on the start.

**Why it matters.** So, from three squares up, the acceptance rule turns away exactly one ending in four at every
length, and on its own it can never make long seed words rare. Any such limit would have to come from checks this
count leaves out, such as whether the middle column keeps its black-white beat and whether the real birth, traced to
where it actually starts, runs into a pattern already proved impossible; those checks may add a cost, but nothing
here shows that they do. It counts patterns on paper, not ones shown to occur, and settles no prize.

**An everyday picture.** A wheel of fortune at a fair with four equal segments, two marked P, one marked Q and one
marked "lose". Give it a proper spin, at least two segments' worth before the final click, and it lands on each
segment equally often wherever it started, so three spins in four win however long the spin lasts. A tiny nudge of
one or two segments, though, depends on where the wheel began.

## The formal statement and proof

*Where:* RULE30-GPT.md GC1198; transition reused from G13 and GC1191.

**Claim (PROVED; GC1198, Local L683).** Fix any valid header and any body prefix in GC1191's formal primitive-seed grammar. Among its n-bit body extensions ending in1, for n>=3, exactly 3*2^(n-3) are accepted: 2^(n-3) Q and 2^(n-2) P. Acceptance is therefore3/4, independently of the fixed prefix, parity or first child sample. This counts formal prototypes, not clock survivors or realized records.

**Proof.** G13 reads u by (a,b)->(b,u XOR(a OR b)). Two successive bits u,v produce pair(c,e), where c=u XOR(a OR b) and e=v XOR(b OR c). For each target(c,e) there is exactly one input pair: u=c XOR(a OR b), v=e XOR(b OR c). Thus two free bits distribute uniformly over the four states, from any fixed starting pair. Each state also has two incoming labelled edges, so uniformity persists through the remaining n-3 bits. Immediately before the stipulated final1, each state has 2^(n-3) inputs. That1 maps00 to01 (Q), 01 and11 to10 (P), and10 to00 (reject). Summing proves the counts. Consequently the terminal grammar alone cannot give a bound C*2^(-alpha*n) on its acceptance fraction with fixed finite C and alpha>0. Joint temporal clock and child-origin cut checks are not included and may impose additional cost.

**Unexpected boundary check, by hand.** At n=2, initial00 accepts both extensions01 and11, whereas initial11 accepts01 and rejects11. The n>=3 guard is essential; no two-bit or per-word rejection follows from the fraction. No experiment or survival census was run.

**Filing check.** proof_dupes.py --near W284 reports E1, E2 and G131; all three read. E1 gives G13's reset-word characterization, E2 a protected backward window, and G131 a Sturmian block-factor exclusion. This reuses E1's decoder but counts primitive terminal completions after a fixed prefix; it does not restate those claims.

**Promotion receipt (GPT, 2026-10-13).** Local L683 at ebe7a00f reads the two-bit bijection, uniformity, terminal count and n2 guard by hand; no experiment replay. Promoted from W284.
