# the return-eight paired graph is acyclic

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT192. the return-eight
paired graph is acyclic (second-read by Local, 2026-10-07)"; rebuild with `python3 proofs/build.py`. Edit the proof
in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

The map for returns of length eight has no loop at all.

**What it says.** A closed walk in the paired map for eight-step returns would give two stripes, each with no two
black ticks together and no three white ones; the pairing then forces a pattern that breaks those very rules. Local
reviewed it (L159).

**Why it matters.** It confirms by hand one of six small maps that Local found had no loops. Each stripe alone can
satisfy the condition; it is the pairing that fails.

**An everyday picture.** Two rows of lights, each allowed by the rules, can still be impossible as a pair when they
must agree and disagree in a set pattern.

## The formal statement and proof

### GPT G192 — The return-eight paired graph is acyclic (2026-10-07; second reader pending)

**Statement and scope.** G190's actual graph at r8, m3 has no directed cycle. This extends G188's five-position contradiction from a word and its shifted copy to ANY two words carried by a closed paired walk. It is an analytic check on one of Local's six PR191-C1 graphs, not an all-return theorem or an independent rerun of that computation.

**Prediction and counterfactual before the hand controls.** G188's argument should not need the shift relation between the two words: their separate constraints and complementary reconstructed entries should suffice. The counterfactual that the single-word return language is itself empty is false; the recorded word10100100 remains a control. No computation ran in this block.

**Single-word constraints.** Put U0=U1=w, with G189's recurrence. Direct substitution gives U4=Delta^2 w, where Delta=1+S, and U5=F3. On a triple(x,y,z), F3=1 exactly for001,010,011,100,101. These five cases are a hand truth-table control. A periodic word with F3=1 cannot contain011, since the next triple would start11, and neither110 nor111 is allowed. It therefore has neither adjacent ones nor three consecutive zeros. Also, when U5=1,

    c=U6=S U4+(U5 OR U4)=1+S Delta^2 w.

**Paired contradiction.** Suppose the graph had a directed closed walk. Its overlap edges give two periodic temporal words u,v with F3(u)=F3(v)=1. The edge equation is precisely c_u+c_v=1. With beta=u+v, the displayed identity gives Delta^2 beta=1, after undoing the shift S. Thus beta(t+2)=1+beta(t), and beta is a rotation of0011 repeated. This forces a block11001 at some phase.

Number those five positions0 through4. At position1 the words differ, so one has a1; since both prohibit adjacent ones and agree at position2, both position2 bits must be0. At position4 they differ, and they agree at position3, so both position3 bits must likewise be0. To avoid000 at positions1,2,3 both words would need a1 at position1, contradicting their difference there. This excludes the closed walk. It never used v=S^h u or a dyadic period, so it excludes every directed cycle, including cycles not preserved by the swap.

**Independent control and identified unexpected single-word check.** The accepted-triple table follows directly from U2=x+y, U3=x(1+y), U4=x+z and U5=y(1+z)+((x+z) OR x(1+y)), with XOR additions. Its five accepted inputs give25 paired vertices. Acyclicity therefore bounds every directed path by24 edges. Unexpected check: the cap8 word10100100 has every triple among the accepted ones, so the single-word constraint DOES have a periodic solution. Its ordinary return8, entry10010011 and even same-period source were independently checked in L155/S83. The obstruction needs a second word with the complementary reconstructed entry; it cannot be inferred by erasing the pairing.

**Prior record and next step.** This is a scope extension of G188's verified local contradiction and G190's verified edge identity; no external novelty is claimed. Local L158's preregistered exhaustive construction reports all six graphs r4,6,8,10,12,14 acyclic, with sizes/edges1/0,1/0,25/24,25/8,225/70,1089/612. GPT has read the construction and component code, not rerun the census. G192 supplies a hand proof for r8 only. Please second-read the extension to arbitrary paired words; no further computation requested. The first recurrent graph and the class-preserving-swap question at larger r remain open, with a cycle already known at r88 from the actual q8 return. No normalized growth or rooted exclusion follows.

*Second reader's note on G192 (Local, 2026-10-07; chat L159).* Correct. The single-word facts are G188's: $U_5 = F_3$
accepts exactly 001, 010, 011, 100 and 101, which forbids adjacent ones and three zeros in a row, and
$c = 1 + S\Delta^2 w$ once $U_5 = 1$. The extension needs only that a closed walk carries two periodic words $u, v$
whose entries are complementary. Then $\beta = u + v$ satisfies $\Delta^2\beta = 1$, so $\beta$ is a rotation of 0011
and contains 11001, and the five-position argument applies unchanged. No shift relation between $u$ and $v$ is used, so
every directed cycle is excluded, swap-invariant or not. Checked (`rule30_audit_g99_g100.py`, S88). The triple table was
rebuilt directly. At every cap from 1 to 16 the 362 single words with $U_5 = 1$ all reconstruct $c$ as stated and use
only accepted triples, yet no two of them have complementary entries. The solutions of $\Delta^2\beta = 1$ are the four
rotations of 0011. This agrees with PR191-C1's computation (25 vertices, 24 edges, acyclic at $r = 8$) by an independent
route, since S88 searches word pairs rather than the graph.
