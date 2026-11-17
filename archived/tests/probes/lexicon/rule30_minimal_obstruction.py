#!/usr/bin/env python3
"""GC1001: logarithmic-query minimal forbidden factor extraction.
For a factor-closed language containing the empty word, with a decided
Boolean membership oracle. Produces a MINIMAL factor, not a shortest one.
No solver invocation or Rule30 census; prediction in RULE30-GPT.md.
"""

def minimal_obstruction(word, member):
    cache = {}
    def known(w):
        if w not in cache:
            value = member(w)
            if type(value) is not bool:
                raise ValueError('Undecided membership; no obstruction verdict')
            cache[w] = value
        return cache[w]
    if not known(''):
        raise ValueError('Empty word must belong to the language')
    if known(word):
        raise ValueError('Input word is present; no obstruction')
    # Shortest absent PREFIX: every shorter prefix is present.
    lo, hi = 0, len(word)
    while hi-lo > 1:
        mid = (lo+hi)//2
        if known(word[:mid]):
            lo = mid
        else:
            hi = mid
    prefix = word[:hi]
    # Furthest absent SUFFIX of that prefix.
    lo, hi = 0, len(prefix)
    while hi-lo > 1:
        mid = (lo+hi)//2
        if known(prefix[mid:]):
            hi = mid
        else:
            lo = mid
    result = prefix[lo:]
    assert not known(result)
    assert known(result[:-1]) and known(result[1:])
    return result, len(cache)

if __name__ == '__main__':
    import itertools
    for forbidden in (('11',), ('01010', '11'), ('000', '101')):
        member = lambda w: not any(f in w for f in forbidden)
        for n in range(1, 10):
            for bits in itertools.product('01', repeat=n):
                w = ''.join(bits)
                if member(w):
                    continue
                f, calls = minimal_obstruction(w, member)
                assert f in w and not member(f)
                # Independent exhaustive proper-factor control.
                assert all(member(f[a:b]) for a in range(len(f)+1)
                           for b in range(a, len(f)+1) if (a,b) != (0,len(f)))
                assert calls <= 2*n.bit_length()+5
    f, _ = minimal_obstruction('0101011', lambda w: '01010' not in w and '11' not in w)
    assert f == '01010'  # A minimal obstruction, despite the shorter '11'.
    try:
        minimal_obstruction('11', lambda w: True if not w else None)
    except ValueError:
        pass
    else:
        raise AssertionError('UNKNOWN was not rejected')
    print('Minimality/query-bound/UNKNOWN/not-shortest controls PASS')
