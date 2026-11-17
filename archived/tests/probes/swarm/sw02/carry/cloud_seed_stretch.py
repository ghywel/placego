# Replay (Cloud, CL766) for RS-2 T5(iii): the seed's centre column to tick 120,000 and its longest run of consecutive flips.
T = 120000; mid = T + 2; row = 1 << mid; c = []
for t in range(T):
    c.append((row >> mid) & 1)
    row = (row << 1) ^ (row | (row >> 1))
assert ''.join(map(str, c[:20])) == "11011100110001011001"
best = (0, 0); run = 0
for t in range(T - 1):
    if c[t + 1] != c[t]:
        run += 1
        if run > best[0]: best = (run, t - run + 1)
    else: run = 0
J, start = best
print(f"centre column to tick {T}: longest run of consecutive flips J = {J}, starting at tick {start} (cells {''.join(map(str, c[start:start+J+1]))})")
print("runs of at least 16 flips start at ticks:", [s for s in range(T - 40) if all(c[s + k + 1] != c[s + k] for k in range(16)) and (s == 0 or c[s] == c[s - 1])])
