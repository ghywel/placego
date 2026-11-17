"""One forward validation of Cloud's entropy ladder, with witness extraction on its old window."""
import hashlib
import json
import math
import os
from collections import Counter, defaultdict, deque
from pathlib import Path

OUT = Path(os.environ["CAPPED_OUT"])
P = 16
LAST = 65536
MASK = (1 << 65536) - 1


def collect():
    """Stream the low 65536 wheels, sufficient whenever the inspected bit is below the cap."""
    history = deque(maxlen=P + 1)
    row = 1
    previous = None
    steps, patterns = [], []
    widths = (4, 6, 7, 8)
    keys = {w: {} for w in widths}
    ambiguous = {w: set() for w in widths}
    repeats = Counter()
    examples = {}
    strata = Counter()
    profile = [0] * 65
    pointwise_example = None
    prior_b = None
    prior_j = None
    for tick in range(LAST + P + 2):
        history.append(row)
        if len(history) == P + 1:
            a, b = history[0], history[-1]
            diff = a ^ b
            assert diff
            edge = (diff & -diff).bit_length() - 1
            t = tick - P
            assert edge + 64 < MASK.bit_length()
            # Seed 7 is the wall-frame successor of seed 1.
            j = (a ^ history[1])
            j = (j & -j).bit_length()-1
            if prior_b == edge and prior_j <= prior_b and pointwise_example is None:
                pointwise_example = [t-1, prior_b, edge, prior_j]
            prior_b, prior_j = edge, j
            if previous is not None:
                pt, old_edge, a0, b0 = previous
                jump = edge - old_edge
                assert jump >= 0
                if 8192 <= pt <= 32768:
                    decider = (a0 >> (old_edge - 1)) & 1
                    assert (jump > 0) == bool(decider)
                    left, right = a0 >> old_edge, b0 >> old_edge
                    strata[decider, (left >> 1) & 1] += 1
                    for w in widths:
                        mask = (1 << (w+1)) - 1
                        key = (decider, left & mask, right & mask)
                        first = keys[w].setdefault(key, (pt, jump))
                        if first[1] != jump:
                            repeats[w] += 1
                            ambiguous[w].add(key)
                            examples.setdefault(w, [key, first, [pt, jump]])
                    delta = left ^ right
                    for h in range(65):
                        profile[h] += (delta >> h) & 1
                if 16384 <= pt <= LAST:
                    steps.append(jump)
                    patterns.append(((a0 ^ b0) >> old_edge) & 31)
            previous = (t, edge, a, b)
        row = ((row << 2) ^ ((row << 1) | row)) & MASK
    assert len(steps) == len(patterns) == 49153
    assert sum(steps.count(v) for v in [0, 1, 2]) == 29092 + 7268 + 10674
    assert [repeats[w] for w in (4, 6, 8)] == [54, 5, 0]
    bulk = sum(profile[32:])/(33*24577)
    review = {"collision_visits":dict(repeats), "distinct_ambiguous":{w:len(ambiguous[w]) for w in widths},
              "distinct_states":{w:len(keys[w]) for w in widths}, "examples":examples,
              "decider_h1_counts":{str(k):v for k,v in sorted(strata.items())},
              "bad_bulk_offsets_h3_to_64":[h for h in range(3,65) if abs(profile[h]/24577-bulk)>.02],
              "equal_edges_with_J_at_or_below":pointwise_example}
    return steps, patterns, review


def train(data, order):
    counts = {k:defaultdict(Counter) for k in range(order+1)}
    for i in range(order,len(data)):
        for k in counts:
            counts[k][tuple(data[i-k:i])][data[i]] += 1
    return counts


def score(data, orders, alphabet, training):
    """Use identical target ticks at each order; positive probabilities even for unseen symbols."""
    top = max(orders)
    freq = Counter((tuple(data[i-top:i]),data[i]) for i in range(top,len(data)))
    n = sum(freq.values())
    result = {}
    for alpha in (1,8,32):
        loss = Counter()
        for (history, value), m in freq.items():
            pool = training[0][()]
            prob = (pool[value] + .5) / (pool.total() + alphabet*.5)
            for k in range(1,top+1):
                ctx = training[k].get(history[-k:])
                if ctx:
                    prob = (ctx[value] + alpha*prob)/(ctx.total() + alpha)
                if k in orders:
                    loss[k] -= m*math.log2(prob)
        result[alpha] = {k:loss[k]/n for k in orders}
    return {"scores":result,"targets":n,"training_contexts":{k:len(training[k]) for k in orders},
            "unseen_top_context_targets":sum(m for (h,v),m in freq.items() if h not in training[top])}


def main():
    os.nice(10)
    steps, patterns, result = collect()
    for name, data, orders, alphabet in [("steps",steps,(2,4),18),("pattern",patterns,(1,2),16)]:
        data = [min(v,17) for v in data] if name=="steps" else data
        half = len(data)//2
        left, right = data[:half],data[half+256:]
        result[name] = {key:score(test,orders,alphabet,train(fit,max(orders)))
                        for key,fit,test in [("forward",left,right),("reverse",right,left)]}
        payload = bytes(data)
        (OUT/(name+".bin")).write_bytes(payload)
        result[name]["sha256"] = hashlib.sha256(payload).hexdigest()
    (OUT/"review.json").write_text(json.dumps(result,indent=2)+"\n")


if __name__=="__main__":
    main()
