"""GC1165: injectivity and outward growth do not exclude periodic columns.

Requested inference audit (L648, 8.93 [J]), not a Rule30 counterexample.
Two tracks over GF(2): u'=A u, v'=A v+u, A=Rule150. The zero state is
quiescent. Every nonzero finite row expands one site at both ends; the
rightmost-difference test gives finite injectivity. Starting u0=delta0,
v0=a finite reflection-symmetric set of paired sites, the centre is
(1,t mod2) forever. Including delta0 in v0 flips that phase.
Proof: A=z^-1+1+z; in A^t=product over t's binary digits of
(z^-2^k+1+z^2^k), the constant term comes only from the all-1 choice,
since the largest selected power exceeds the sum of every smaller one.
Thus [z^0]A^t=1. Reflection symmetry cancels each paired contribution at
0. F^t gives v_t=A^t v0+(t mod2)A^(t-1)delta0. Distinct members have
no full-state intersection at different times either, because u_t has
endpoints -t,+t, which determine t; finite injectivity handles equal t.

BEFORE controls: 32 seeds (subsets of +-1..+-4, both centre phases),
ticks0..32; literal cell rule, Laurent product and closed form must agree;
centre, support ends and distinct full rows must obey the claims.
Countercontrol: remove +u; the zero v track stays constant, no period2.
Unexpected: v0=delta1 must fail the symmetric-family alternation at tick1.
Record searched: Rule.?150|injectiv|merg|isolated.orbit|periodic.column
with linear|grow|symmetr|matrix|basin ->111 hits40files; G121, 8.93 read.
Rule150 already recorded; no new prior-art theorem, rate or prize claim.
No solver, ring enumeration, language membership or Local run repeated.

OUTCOME 2026-10-13 12:51 BST: all1056 tested complete states agree across the
three constructions; both centre phases, exact endpoints and distinct rows
pass. Coupling-removal and nonsymmetric-seed countercontrols pass. The
all-time claims are proof sketches from the displayed algebra, awaiting
Local's carrying-step review; finite controls alone are not that proof.
"""
from itertools import product


def multiply(a, b):
    out = set()
    for x in a:
        for y in b:
            z = x+y
            if z in out:
                out.remove(z)
            else:
                out.add(z)
    return out


def power(t):
    out, k = {0}, 0
    while t:
        if t & 1:
            out = multiply(out, {-(1 << k), 0, 1 << k})
        t >>= 1
        k += 1
    return out


def literal(u, v, coupling=True):
    lo, hi = min(u | v)-1, max(u | v)+1
    a, b = set(), set()
    for i in range(lo, hi+1):
        ui = (150 >> (4*(i-1 in u)+2*(i in u)+(i+1 in u))) & 1
        vi = (150 >> (4*(i-1 in v)+2*(i in v)+(i+1 in v))) & 1
        vi ^= int(coupling and i in u)
        if ui:
            a.add(i)
        if vi:
            b.add(i)
    return a, b


def main():
    roots = []
    for word in product((0, 1), repeat=4):
        pairs = {i for r, b in enumerate(word, 1) if b for i in (-r, r)}
        for phase in (0, 1):
            v = pairs ^ ({0} if phase else set())
            roots.append((phase, v))
    paths, checked = [], 0
    for phase, v0 in roots:
        u, v = {0}, set(v0)
        left, right = min(u | v), max(u | v)
        path = []
        for t in range(33):
            p = power(t)
            q = multiply(p, v0) ^ (power(t-1) if t % 2 else set())
            assert (u, v) == (p, q)
            assert (int(0 in u), int(0 in v)) == (1, phase ^ (t % 2))
            assert (min(u | v), max(u | v)) == (left-t, right+t)
            path.append((frozenset(u), frozenset(v)))
            u, v = literal(u, v)
            checked += 1
        paths.append(path)
    assert all(len({p[t] for p in paths}) == len(roots) for t in range(33))
    # Coupling is essential; the v track remains zero without it.
    u, v = {0}, set()
    for t in range(8):
        assert (int(0 in u), int(0 in v)) == (1, 0)
        u, v = literal(u, v, coupling=False)
    # A nonsymmetric extra cell changes the very first expected black tick.
    u, v = literal({0}, {1})
    assert (int(0 in u), int(0 in v)) == (1, 0)
    print(checked, 'literal/Laurent/closed-form states agree; two phases, endpoints and distinct rows PASS')
    print('Coupling removal and nonsymmetric tick1 countercontrols PASS')
    print('All-time conclusion uses the stated algebra; no Rule30 or basin census')


if __name__ == '__main__':
    main()
