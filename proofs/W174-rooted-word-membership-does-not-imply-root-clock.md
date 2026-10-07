# rooted word membership does not imply root-clock membership

*The waiting room (not yet verified). Derived from [PROOFS.md](../PROOFS.md), entry "GPT G174 — rooted word
membership does not imply root-clock membership (RULE30-GPT.md G174; awaiting second reader, 2026-10-07)"; rebuild
with `python3 proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never
this file.*

**Status:** in the waiting room: stated with a proof, not yet checked by a second reader.

## In plain words

A word can occur along a rooted history without every allowed clock occurring there.

**What it says.** The period-four collision's word pair lies ten steps from the root, but every initial root clock reaches it at phase one. The feature self-loop uses phase zero, which satisfies the gate but is not reached on that prefix.

**Why it matters.** Rooted words combined with every gated phase form a larger domain than the actual rooted clock graph. The latter could still support a certificate that fails on the larger domain.

**An everyday picture.** A station is reachable, but that does not mean every departure time appears on the train journey used to reach it.

## The formal statement and proof

**Root-word versus root-clock scope audit (2026-10-07; review requested).** DQ3's period4 source pair(15,12) is word-rooted, reached after10 spatial edges on the unique predecessor chain. In root-to-source order the exact pairs are

    (0,15),(15,15),(15,0),(0,5),(5,15),(15,5),(5,5),(5,0),(0,9),(9,15),(15,12).

Every consecutive triple satisfies the scalar equation; the constant-one root is integer15, not integer1. Carry G8's full-line clock from each initial root time0,1,2,3 along this chain. The source arrival times are9,13,13,13, hence all four arrival phases are1. These values were predicted from literal arithmetic before the independent targeted script `tests/probes/lexicon/rule30_dq3_root_clock_review.py` was executed; its scalar backward, forward and reset checks pass. No tree or quotient census was repeated.

At the actual reached phase1, source features are(1,2,1), its next reset costs2, and the target phase3 features are(1,3,1). The feature self-loop at source phase0 therefore disappears on this particular root-clock edge. Phase0 still satisfies the gate a(-1)=1. This is the identified unexpected guard: a pair can be word-rooted and gated at a clock that no root-start phase reaches. G7's unique predecessor guarantees there is no alternate word path to this same pair; enumerating all four initial clock residues is sufficient for the fixed period4 full-line front.

Consequently the q4 witness rejects a three-distance certificate on rooted word pairs required to cover every gated clock, but does not reject the same family restricted to clock states actually reached from the root. This is a sharper quantifier distinction than saying the witness is simply unrooted. Restart clocks at interior vertices and birth-clamped fronts are different domains; neither was tested or excluded here. G164's separate phase-transfer theorem remains relevant if a reference-clock budget can be proved. The all-period exact-family construction of G173 remains ambient, with no newly claimed rooted-clock membership at larger periods. Next scope to investigate is the explicitly root-reached clock graph, preserving actual clocks through every child rather than treating the gate as sufficient reachability.
