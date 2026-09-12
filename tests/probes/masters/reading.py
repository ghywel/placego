"""check.sh's reading of one psnr stats file, by the ladder's own rules (analyze.py's parse / mean_interp).
    reading.py <stats> <tests dir>   ->   "<ladder mean> <min past 5> <frames>"
"""
import re
import sys

stats, tests = sys.argv[1], sys.argv[2]
ns = {}
exec(open(tests + "/analyze.py").read().split("def fmt(")[0], ns)
frames = ns["parse"](stats)
m = ns["mean_interp"](frames)
vals = []
for line in open(stats):
    r = re.search(r"n:(\d+) .*?psnr_y:([0-9.]+|inf)", line)
    if r:
        vals.append((int(r.group(1)), 99.0 if r.group(2) == "inf" else float(r.group(2))))
past = [v for n, v in vals if n > 5]
print("%.2f %.2f %d" % (99.0 if m == float("inf") else (m if m is not None else float("nan")),
                        min(past) if past else float("nan"), len(vals)))
