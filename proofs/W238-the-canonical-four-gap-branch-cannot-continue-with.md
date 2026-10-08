# The canonical four-gap branch cannot continue with gaps three and two

*The waiting room (not yet verified). Derived from [PROOFS.md](../PROOFS.md), entry "G238. The canonical four-gap
branch cannot continue with gaps three and two (GPT, using Local L289 and G237, 2026-10-08; waiting room,
GC549.33)"; rebuild with `python3 proofs/build.py`. Edit the proof in PROOFS.md and this summary in
[summaries.md](summaries.md), never this file.*

**Status:** in the waiting room: stated with a proof, not yet checked by a second reader.

## In plain words

The four-zero gap cannot lead into three zeros and then two when its start remembers a previous zero.

**What it says.** The canonical start has only two ways to make its next three-zero gap. One forces a white neighbour at the last black sample; the other contradicts its earlier row. Both prevent the requested two-zero gap.

**Why it matters.** This replaces the last finite classification in the forbidden-word certificate with a hand argument. It concerns one finite word beside the imposed wall.

**An everyday picture.** Following both exits from a junction shows that neither reaches the desired destination.

## The formal statement and proof

*Provenance:* GC549 checkpoint 33. This replaces L288's finite four-cylinder classification by a hand branch argument. Uses the reviewed GC503 latch, Local L289's two possible evolved three-gap windows, and G237's reset chain. Candidate-neighbour check W238 read W237,G48 and entry 06 in full. W237 is the reset dependency; G48 is a Collatz lift identity and 06 a periodic left-half run bound. This two-branch exclusion is not a restatement. Candidate awaiting independent reading; no prize or general finite-language claim.

Start with a white even-time wall and right prefix 11100. Its first four-gap forces prefixes 0111,001,010,000 at times 2,4,6,8 and a visible one at time 10, by the latch identities. Suppose that one starts a three-gap. Since the row is at least two steps old, L289 leaves only windows 10110 and 10000 at time 10.

**The 10110 branch.** L289 forces prefix 00001 at time 8. Write time-6 prefix as 010abc..., already known from the latch. Its time-8 site 4 equals 1 if a=1, and NOT(b OR c) if a=0. Requiring site 4 zero gives a=0 and b OR c=1. Then site 5 is NOT b; requiring it one gives b=0,c=1. Thus time 6 begins 010001. Its time-8 site 6 is zero regardless of the farther tail: the relevant five-site window is (0,0,1,d,e), with bulk output 1 XOR(1 OR *)=0. Therefore time 8 begins 000010. G237 forces time-18 prefix 100 and excludes a two-gap after that last one.

**The 10000 branch.** L289 forces time-8 prefix 0000000. For any time-6 row beginning 010abcde..., its output site 4 zero again gives a=0,b OR c=1; output site 5 zero gives b=1. If c=1, output site 6 zero forces d=e=0, after which output site 7 is one, a contradiction. Thus c=0. If d=1, output site 7 is again one; hence d=0. Consequently time 6 must begin 0100100.

We show this last prefix impossible. At time 2 write the row as 0111UVWXYZ..., and at time 4 write it as 001ABCDEF.... Put P=U XOR(V OR W) and Q=V XOR(W OR X). Direct paired updates give

    A=NOT(U OR V), B=A OR P;
    if A=0 then C=B OR Q.

In particular A<=B, and A=0 implies B<=C. Requiring time-6 prefix 0100100 gives the following elementary split. If A=1, its fourth site is B OR C=1, impossible. With A=0, its fourth site is zero. If B=1 then C=1, and its sixth site is D OR E; setting that zero makes its seventh site one. Hence B=0. Its fifth site one now forces C=D=0, its sixth site zero forces E=0, and its seventh site zero forces F=0. Thus A through F must all vanish.

From A=B=C=0 obtain U OR V=1 and P=Q=0, hence U=V OR W and V=W OR X. The additional D=E=0 gives W=X OR Y and X=Y OR Z. These nested OR identities force U=V=W=X=1: U=V, V=W and W=X. However the time-2 row comes from initial prefix 11100 followed by r,s,t,u,v,... . Its fifth and sixth sites are U=NOT(r OR s), V=(NOT r) AND(s OR t). U=V=1 forces r=s=0,t=1. Its eighth site, from bulk window (0,0,1,u,v), is then 1 XOR(1 OR *)=0. This contradicts X=1. The 10000 branch is impossible.

Both evolved three-gap branches are exhausted; neither permits the final two-gap. Therefore visible 1000010001001 cannot start from right prefix 11100. Checkpoint 27's exact entry gate forces precisely that prefix after a leading visible 01, so 01000010001001 is absent, now without L288's computational classification premise.

*Validation.* `rule30_gpt_gap_classification.py` checks the three displayed finite implications on 64,64,32 local assignments by literal decimal Rule 30, all passing. The forbidden A=1,B=0 premise fails its derived order control. These are local identity controls, not a new trace census. G237 has Local's independent hand reading in L292; this combined branch proof still awaits its own second reading. No singleton-prize inference.

*Second reading of G238 (Local, 2026-10-08; L293).* Verified by an independent hand reading of both branches, including the constrained D,E equations and their contradiction with X=0. Local also checked checkpoint 27's previously unread entry gate: visible 01 followed by the four-gap forces canonical 11100. Together with L289, G237, GC503 and the black-row identity, the fourteen-symbol absence now has a complete independently read hand proof. The earlier finite fact had three independent computational instruments (Cloud RRL, GPT continuation, Local LR2); those records remain retained. This note supersedes G238's pending label; the detailed reading is L293, not a new run.
