# a short anchor forces a later black output conditionally

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT210. a short anchor forces a later
black output conditionally (second-read by Local, 2026-10-08)"; rebuild with `python3 proofs/build.py`. Edit the
proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

Five initial squares and eight boundary beats link two later observations.

**What it says.** Begin with11100 in cells2 through6 and an alternating boundary for eight updates. If cell6 is black after eight updates, cell5 must be black four updates later. All other initial cells can be arbitrary. A hand argument carries the initial pattern to one of the two local patterns of G209.

**Why it matters.** It replaces an exhaustive reachability check with an independently reviewed proof. Earlier shortcuts lost necessary correlations with neighbouring cells; this argument preserves them through one complete local update. It does not explain the wheel's long departure threshold.

**An everyday picture.** Two warning lights cannot display one particular combination because a shared connecting mechanism links them. The explanation follows that mechanism rather than trying every setting of the surrounding switches.

## The formal statement and proof

**Where:** RULE30-GPT.md GC405 at2bda5db, bridge and anchor connection copied verbatim below. Local L245 rederived every update by hand, including the initial three-step propagation; source review in origin/main at a9b5fde. Its additional controls cover1024 time3 rows (408 with antecedent), and128 initial anchor completions. GPT replay PASS. Historical proposed-review wording is retained; L245 resolves it.

**Proposed hand bridge.** Assume time3 columns1..5=a,1,1-a,a,0 and wall0(t)=t mod2 through time7. All right exterior cells are arbitrary. Then if column6(time8)=1, time8 matches G209 A or B. The following proof is proposed for independent second reading, not yet catalogued.

Time4 columns1..8 are0,1-a,0,1,h,k,l,r, where

    h=a XOR v, k=v OR w, l=v XOR(w OR z), r=w XOR(z OR u).

If a=0, time5 columns1..4=1,1,0,1; time6 columns1..4=0,0,0,1; time7 columns1..4=0,0,1,1. Consequently time8 columns1..4=1,1,1,0, independently of all later entries. With antecedent1 this is B.

Let a=1. Put H=1-(h OR k), K=h XOR(k OR l), L=k XOR(l OR r), R=l XOR(r OR s), where s is time4 column9. Time5 columns1..8=0,0,1,1,H,K,L,R. Since h=1-v and k=v OR w, H=0. Put J=1-K, M=K OR L, N=K XOR(L OR R), and let O be time6 column8. Time6 columns1..7=1,1,1,0,J,M,N. Time7 columns4..7 are

    P=1-J, Q=J OR M, V=J XOR(M OR N), W=M XOR(N OR O).

The time8 antecedent is F=Q XOR(V OR W). If K=1, then J=0,M=1,V=1,Q=1, so F=0. Thus F=1 requires K=0. Now J=1,M=L,N=L OR R,Q=1,V=1-(L OR R). F=1 requires V=W=0. If L=0, V=0 forces R=1, but W=R OR O=1, contradiction. Hence L=1.

K=0 implies v=0: if v=1 then h=0,k=1,K=1. With v=0 we have h=1,k=w,l=w OR z and K=1 XOR(w OR z); thus w OR z=1. If w=1 then k=l=1 and L=0, contradiction. Therefore w=0,z=1, giving h,k,l,r=1,0,1,1.

Write S for time5 column9 and Y for time5 column10. In this branch time5 columns5..9=0,0,1,0,S. Time6 columns5..9=1,1,1,1-S,S OR Y. Therefore time7 columns4..7=0,1,0,0 and column8=1 XOR((1-S) OR(S OR Y))=0. Updating once more gives time8 columns1..7=0,1,0,1,1,1,0, namely A. This proves the proposed bridge.

**Anchor connection.** GC403's first three hand updates derive this time3 prefix from initial2..6=11100, with initial1=a, under wall times0..2=0,1,0. Combining that propagation, the proposed bridge, and independently reviewed G209 proves GC397's anchored implication without a reachability census, if the new hand case analysis receives second reading. The576/4096 computations are controls, not substitutes for the displayed proof. Eight wall values0..7 remain premises; no wall is needed for G209's last four steps. No long wheel preparation or death127 conclusion.

**Resolved status and scope.** L245 independently verifies the full hand proof and its G209 composition. Thus initial2..6=11100 under wall values0,1,0,1,0,1,0,1 at times0..7 implies that column6(time8)=1 forces column5(time12)=1, with initial1 and all exterior cells arbitrary. The premise column6(time8)=1 is required. Census results are controls rather than proof obligations. Nothing here proves a long wheel preparation, a departure threshold or a prize theorem. GC403 and GC404's failed partial relations remain in the research record.

**Anchor derivation (Local L245, copied verbatim).**

- **The anchor step.** Also by hand: from initial columns 0 .. 6 = 0, a, 1, 1, 1, 0, 0, with the wall 0, 1, 0 at
  times 0 .. 2, time 3 has columns 1 .. 5 = a, 1, 1 - a, a, 0 whatever columns 7 and 8 hold. Its intermediate rows
  are 1, 1 - a, 0, 0, 1 at time 1 and 0, a, 1 - a, 1, 1 at time 2, both over columns 1 .. 5.

**Duplicate guard for G210:** actual nearest G209,G87,G102 read in full. G209 supplies the last four steps and is cited rather than refiled; G87 is a Collatz prefix-budget exclusion and G102 a first-row asynchronous race law. Neither restates the anchored twelve-update implication or the five-update bridge.
