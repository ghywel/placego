"""GC2620. Replay only CL715's fixed exit sample using a packed autonomous prefix."""
import hashlib
import json
import os
from pathlib import Path

T, W, TH, LO, K = 65536, 8192, 32768, 4096, 31129
PERIODS = (1, 2, 4, 8, 16)
OUT = Path(os.environ["CAPPED_OUT"])


def main():
    os.nice(10)
    mask = (1 << (K + 1)) - 1
    # Two further wheels suffice for the first cell outside either front.
    keep = 4 * mask + 3
    rows = [1]
    for _ in range(T - W + 16):
        v = rows[-1]
        rows.append(((v << 2) ^ ((v << 1) | v)) & keep)
    assert rows[:3] == [1, 7, 19]
    assert (rows[T - W] ^ rows[T - W + 16]) & mask == 0
    # The prefix is autonomous, so this equality certifies all later rows.
    cycle = rows[T - W:T - W + 16]
    masks = {}
    remaining = mask
    for p in PERIODS:
        bad = 0
        for phase, v in enumerate(cycle):
            bad |= v ^ cycle[(phase + p) % 16]
        masks[p] = remaining & ~bad
        remaining ^= masks[p]
    assert remaining == 0

    later = [0] * (K + 1)   # Published zero sentinel for no mismatch.
    periods = [0] * (K + 1)
    for p, bits in masks.items():
        while bits:
            low = bits & -bits
            periods[low.bit_length() - 1] = p
            bits ^= low
    # First difference encountered in reverse is the last later-end mismatch.
    unseen = mask
    for vtime in range(T - W + 16, 0, -1):
        differing = 0
        for p, bits in masks.items():
            if vtime >= p:
                differing |= (rows[vtime] ^ rows[vtime - p]) & bits
        new = differing & unseen
        unseen ^= new
        while new:
            low = new & -new
            later[low.bit_length() - 1] = vtime
            new ^= low
    onsets = [max(0, t - p + 1) for t, p in zip(later, periods)]
    published = [-1] * (TH + 1)
    for k, t in enumerate(later):
        if t < TH:
            published[t + 1] = max(published[t + 1], k)
    for t in range(1, TH + 1):
        published[t] = max(published[t], published[t - 1])
    prefix = []
    k = -1
    for t in range(TH + 1):
        while k < K and onsets[k + 1] <= t:
            k += 1
        prefix.append(k)
        mismatch = (rows[t] ^ rows[t + 16]) & mask
        assert k == ((mismatch & -mismatch).bit_length() - 2 if mismatch else K)
    B0, B1 = published[LO], published[TH]
    assert (B0, B1) == (3117, 24452)

    def first_exit(front):
        values = bytearray()
        counts = {}
        next_ray = LO
        reentry_intervals = []
        first = None
        for t in range(1, TH + 1):
            threshold = 2*t - front[t]
            if next_ray > LO and threshold < next_ray:
                left = max(LO, threshold)
                right = min(next_ray - 1, TH, 2*t)
                if left <= right:
                    reentry_intervals.append((left, right))
            while next_ray < threshold and next_ray <= TH:
                j = next_ray
                k = 2*t - j
                assert t > (j + 1)//2 and 0 <= k - 2 <= front[t-1]
                d = k - front[t]
                assert d in (1, 2) and k <= K + 2
                bit = (rows[t] >> k) & 1
                values.append(bit)
                key = (d, front[t] - front[t-1])
                group = counts.setdefault(key, [0, 0])
                group[0] += bit
                group[1] += 1
                if first is None:
                    first = [j, t, k, bit]
                next_ray += 1
        assert len(values) == TH - LO + 1
        right = LO - 1
        reentered = 0
        for a,b in sorted(reentry_intervals):
            reentered += max(0, b - max(right, a-1))
            right = max(right, b)
        return values, {"black":sum(values),"n":len(values),"density":sum(values)/len(values),
                        "first":first,"reentered_by_TH":reentered,
                        "by_offset_jump":{str(key):v for key,v in sorted(counts.items())}}

    result = {}
    for name, front in [("published", published), ("prefix", prefix)]:
        bits, item = first_exit(front)
        file = OUT / (name + "-bits.bin")
        file.write_bytes(bits)
        item["bits_sha256"] = hashlib.sha256(bits).hexdigest()
        mean_t = (LO + TH)/2
        item["slope"] = sum((t-mean_t)*front[t] for t in range(LO,TH+1))/sum((t-mean_t)**2 for t in range(LO,TH+1))
        item["B_samples"] = [front[2**i] for i in range(8,16)]
        result[name] = item
    result["unequal_front_ticks"] = sum(a != b for a,b in zip(published[LO:],prefix[LO:]))
    result["first_early_hole"] = next(([t, published[t], prefix[t]] for t in range(TH+1) if published[t]>prefix[t]), None)
    result["wheel0_to_8"] = list(zip(periods[:9],later[:9],onsets[:9]))
    result["front_at_times_0_to_4"] = published[:5]
    result["origin_initial_assert_possible"] = (published[0]>=0 or published[1]>=2)
    (OUT / "replay.json").write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps(result))
    assert format(result["published"]["density"], ".4f") == "0.4311"


if __name__ == "__main__":
    main()
