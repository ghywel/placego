# exact-period witnesses reject three-distance coefficients

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT171. exact-period witnesses reject
three-distance coefficients (second-read by Local, 2026-10-07)"; rebuild with `python3 proofs/build.py`. Edit the
proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

Choosing the formula by each state's own shortest period does not rescue the three distances either.

**What it says.** Three real steps whose stripes have exactly period q, and no shorter one, still make contradictory
demands on G169's three-distance formula, even when its multiples may depend on each state's own period. A change
far along a stripe alters its period while the three distances, which look only as far as the next black beat, stay
the same.

**Why it matters.** It closes the escape left open by G170: the trouble is in what the three distances throw away,
not in mixing periods.

**An everyday picture.** A fare set from the first mile of a route cannot tell apart two routes that part only
later.

## The formal statement and proof

### GPT G171 — exact-period witnesses reject three-distance coefficients (RULE30-GPT.md G171; awaiting second reader, 2026-10-07)

**Stronger restriction; independent review requested.** For every dyadic q>=16, restrict to gated edges whose source and target pairs both have least temporal period exactly q. A potential of the three-distance form in G170, with coefficients selected by this least pair period, still requires gamma>=3q/(q+1). Thus no fixed gamma<3 can be certified at all sufficiently large dyadic periods by this family, even after removing all lower-period states and allowing arbitrary period-dependent coefficients. G170's embedded-state proof alone did not imply this stronger scope.

**Exact-period first edge.** Let b have black bits only at3,7,q-1, let a=S b XOR b, and take arrival r=0. The compatible child is c=b. Since b(0)=0 and b(q-1)=1, a(q-1)=1 and the source is gated. It costs4 and reaches(b,b,4); that target is gated because b(3)=1. The source distance triple is(3,4,3): D(a,0)=3, D(b,0)=4 and a XOR b=S b has first black bit2. From phase4 the target has distances(4,4,0), because its next black bit is7. Hence the first constraint remains

    -alpha_q+3*chi_q >=8-2*gamma.

The word b has odd weight3. A proper-period word at a dyadic common period repeats an even number of times and has even weight. Therefore b, and both endpoint pairs containing b, have least period q. The far black bit at q-1 creates exact-period membership without changing the local distance triples.

**Exact-period zero edge.** Let c have black bits only at1,q-1, and put a=S c XOR c. Use(a,0,0)->(0,c,0). The scalar integration equation holds, the cost is0, and the source/target gates follow from c(0)=0,c(q-1)=1. The feature triples are(1,0,1) and(0,2,2), so

    alpha_q-2*beta_q-chi_q >=-2*gamma.

The two black positions are not opposite at q>=16, so c cannot be a repetition of a proper dyadic divisor: a two-black word with a proper period would have to repeat twice with opposite black positions. Thus c has least period q. Also a has least period q. If a had period dividing q/2, then the difference c(t+q/2) XOR c(t) would be constant, since its temporal difference is0. Constant0 contradicts c's least period; constant1 would force c to have q/2 black bits, contrary to its weight2. This checks exact-period membership of the source as well as the child, which a common-period closure check would not suffice to establish.

**Third edge and contradiction.** The single pulse b at q-1 supplies the gated edge(b,b,0)->(b,0,0), both pairs of least period q, with constraint q*(beta_q-chi_q)>=2q-2*gamma. All three edges now use the same least-period coefficients and constant, which cancels on each edge. Multiply the first two inequalities by q/2 and the third by1. Their left sides cancel and give0>=6q-2*gamma*(q+1), hence gamma>=3q/(q+1). This is an explicit three-edge dual certificate, not a numerical feasibility result. Square.

**Known arithmetic controls and identified unexpected guard.** At q16 the first word is b=32904 and its preceding word is a=49356; the first arrival becomes phase4, not phase0. The second edge uses c=32770 and a=49155. Its preceding word must also have exact period16; checking only c would leave the coefficient cancellation unjustified. The pulse is32768. At gamma5/2 the certificate reads0>=q-5, hence0>=11 at q16. The original G170 embedding changed common period without changing least period; these sparse constructions genuinely change least period while retaining the same three observed distances. No run was used to obtain these controls.

**Counterfactual and remaining scope.** If coefficients were chosen by additional state features, the three inequalities could use different coefficients and cancellation would fail. Nonlinear features, explicit pair interactions, history-dependent or rooted-only certificates remain open. Root reachability of these witnesses is not asserted, and no positive compatible cycle or finite-seed obstruction is claimed. The bound3q/(q+1) is necessary only, not sufficient. This closes the least-period-coefficient escape for the specific three-reset-distance linear family, including finitely many exceptional small periods, but not the all-period O(q) debt conjecture. It uses G169-G170's algebra with explicit compatible exact-period witnesses; no novelty claim is made for linear duality or period counting. Next direct-charge proposals need additional joint state information rather than a period lookup for these same three features.

*Second reader's note on G171 (Local, 2026-10-07; chat L133).* Correct. The first edge is compatible because
$S b = a \oplus b$, and both ends are gated: the arrival moves to phase 4, where $b(3) = 1$. It keeps the triples
$(3, 4, 3) \to (4, 4, 0)$, since $b$'s next black bit after phase 4 is 7. The zero edge keeps $(1, 0, 1) \to (0, 2, 2)$,
and the pulse edge is as in G166. The exact-period arguments hold. An odd-weight word cannot repeat at a dyadic period.
The two black positions 1 and $q - 1$ are opposite only when $q = 4$. A period of $q/2$ in $a$ would make
$c(t + q/2) \oplus c(t)$ constant, which neither value allows. So the same least-period coefficients appear in all three
inequalities, and the dual weights cancel them as in G170. Checked (`rule30_audit_g99_g100.py`, S66) at
$q = 16, 32, 64$: compatibility, gates, costs, triples and least period exactly $q$ for every endpoint word. At $q = 16$
the words are 32904, 49356, 32770, 49155 and 32768, as stated.
