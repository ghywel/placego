"""GC1158: deterministic-after-seed presentation of exact inverse images.

Predictions BEFORE controls: at fixed k=1,2,3,4,7,13,26,149 the sharp132
root q+0 accepts and q+1 rejects on the final output letter under their
common root seed and the certified24 cut. Black raw bits and the unused
terminal root sample change no output. Countercontrol: at k4, root
001001 and101001 have identical output pairs, but their seeded paths
distinguish the certified6 cut101001. An unlabelled factor is insufficient.
Unexpected: a black pivot has no new bit and cannot repair a wrong output.
Independent: literal Wolfram-table inverse versus GC971 XOR/OR image;
direct root substring test versus cut-automaton acceptance.
Record searched: GC978|GC970|root|provenance with annotation|label|
register|origin|transduc|recover|inverse ->366 hits99 files; seed|prefix|
window with decoder|decode|transduc|recover.*column|column.*recover
->98 hits51 files. G25, GC971/978/980, GC1157 read. Exact-image semantics
reused; new target is a constructive seeded decoder and its state bound.
No solver, closure search, language census or relaxed-record computation.
The state bound is not a white-record bound; the window grows with k.
RT input SHA256 dea50d7a8c9b0437491ced1b035daeb3df6d0693c605f2e315a589e90bd2413e.

OUTCOME 2026-10-11 17:21 BST (one Intel CPU process): all 64 fixed-root
controls PASS at the eight declared depths; q+1 rejects on the last letter.
The k4 images collide, but the two seeded paths accept/reject [None, 7].
Thus forbidding the bad root's whole image would also forbid a permitted
root image; this does not rule out unlabelled exact image automata.
Black-pivot corruption rejects at index 0. Only constant black raw patterns
0/1 and terminal choices 0/1 were tested; arbitrary masking is G25's proof.
Initial harness failure retained: the terminal comparison was indented
inside the last-bit loop, comparing two good completions before collecting
the bad ones. Moving it outside that loop fixed the assertion; no change
to the decoder and no mathematical counterexample. General exactness and
the state bound are a tier-2 proof sketch, not established by these tests.
"""
from hashlib import sha256
from pathlib import Path

from rule30_local_record_traces import blocks, OUT
from rule30_rrl_transducer import literal_image

TABLE = (0, 1, 1, 1, 1, 0, 0, 0)
CUT = '100100001001000010000101'
DEPTHS = (1, 2, 3, 4, 7, 13, 26, 149)


def pair(k, phase, raw):
    """One exact pair at depth k from k effective inputs and the clock."""
    assert len(raw) == k
    u = tuple((phase+t) % 2 for t in range(k+1))
    v = tuple(raw)+(0,)
    for _ in range(k):
        left = tuple(next(a for a in (0, 1)
                          if TABLE[4*a+2*u[t]+v[t]] == u[t+1])
                     for t in range(len(u)-1))
        u, v = left, u
    return u[0], v[0]


class Cuts:
    def __init__(self, words):
        self.words = tuple(words)
        self.prefixes = {''} | {f[:i] for f in words for i in range(1, len(f))}

    def step(self, suffix, bit):
        s = suffix+str(bit)
        if any(s.endswith(f) for f in self.words):
            return None
        return max((p for p in self.prefixes if s.endswith(p)), key=len)


def decode(word, k, phase, seed, forbidden):
    """Return recovered visible bits or the first rejected output index.

    seed contains exactly the first k-1 root physical-time inputs;
    root black-time values are canonically zero. Index -1 is a bad seed.
    """
    assert k >= 1 and len(seed) == k-1
    cuts = Cuts(forbidden)
    window, suffix, visible = tuple(seed), '', []
    for t, b in enumerate(window):
        if (phase+t) % 2:
            assert b == 0
        else:
            visible.append(b)
            suffix = cuts.step(suffix, b)
            if suffix is None:
                return None, -1
    for t, letter in enumerate(word):
        a, companion = divmod(letter, 2)
        reference, expected_companion = pair(k, (phase+t) % 2, window+(0,))
        if companion != expected_companion:
            return None, t
        if (phase+t+k-1) % 2 == 0:
            bit = a ^ reference
            # The terminal pivot must be monic even with nonlinear past.
            flipped, same_companion = pair(k, (phase+t) % 2, window+(1,))
            assert flipped == 1-reference and same_companion == expected_companion
            visible.append(bit)
            suffix = cuts.step(suffix, bit)
            if suffix is None:
                return None, t
        else:
            if a != reference:
                return None, t
            bit = 0
        window = (window+(bit,))[1:]
    return tuple(visible), None


def root_word(q, phase=0, odd=0, terminal=0):
    # Pair horizon 2*|q|+phase: last letter's v is unused.
    n = 2*len(q)+phase
    return tuple(2*((phase+t) % 2) +
                 (terminal if t == n-1 else
                  int(q[(t-phase)//2]) if (phase+t) % 2 == 0 else odd)
                 for t in range(n))


def canonical_seed(root, k):
    return tuple(a % 2 if a//2 == 0 else 0 for a in root[:k-1])


def main():
    assert sha256(Path(OUT).read_bytes()).hexdigest() == (
        'dea50d7a8c9b0437491ced1b035daeb3df6d0693c605f2e315a589e90bd2413e')
    q = next(b for b in blocks(OUT) if b[0] == 132)[6]
    controls = 0
    for k in DEPTHS:
        outputs = []
        for last in '01':
            baseline = None
            for odd, terminal in ((0, 0), (0, 1), (1, 0), (1, 1)):
                root = root_word(q+last, odd=odd, terminal=terminal)
                out = root
                for _ in range(k):
                    out = literal_image(out)
                if baseline is None:
                    baseline = out
                assert out == baseline
                seed = canonical_seed(root, k)
                got, failed = decode(out, k, 0, seed, (CUT,))
                assert (CUT not in q+last) == (failed is None)
                if last == '0':
                    assert got == tuple(map(int, q+last))
                else:
                    assert failed == len(out)-1
                outputs.append(out)
                controls += 1
        good, bad = outputs[0], outputs[-1]
        assert good[:-1] == bad[:-1] and good[-1] ^ bad[-1] == 2
    # A genuine algebraic overlap of accepted and forbidden-root images.
    roots = [root_word(q) for q in ('001001', '101001')]
    images = []
    for root in roots:
        out = root
        for _ in range(4):
            out = literal_image(out)
        images.append(out)
    assert images[0] == images[1]
    outcomes = [decode(images[i], 4, 0, canonical_seed(roots[i], 4), ('101001',))[1]
                for i in (0, 1)]
    assert outcomes == [None, len(images[1])-1]
    # Wrong output at a black terminal pivot cannot borrow a fresh bit.
    root = root_word('001001')
    out = root
    for _ in range(4):
        out = literal_image(out)
    assert (0+4-1) % 2 == 1
    corrupt = (out[0] ^ 2,)+out[1:]
    assert decode(corrupt, 4, 0, canonical_seed(root, 4), ())[1] == 0
    print('Root cut transported at eight fixed depths; controls', controls, 'PASS')
    print('k4 unlabelled image collision, seeded accept/reject', outcomes, 'PASS')
    print('Black-pivot output corruption rejects immediately PASS')


if __name__ == '__main__':
    main()
