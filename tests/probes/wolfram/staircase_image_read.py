#!/usr/bin/env python3
"""Read a marked screenshot without modifying it; bounded image diagnostic.

Frozen plan: reports/rule30-staircase-investigation.md. Requires Pillow.
Input is a private local image argument, never saved or copied into git.
Classify dark/light/obscured cell centres, then test all cardinal time axes,
both spatial handednesses, and both colour encodings against rule 30.
No recovery of obscured cells is used in scoring.
"""
import argparse
import json
import resource
import signal
from PIL import Image


def main():
    resource.setrlimit(resource.RLIMIT_CPU, (20, 20))
    # This host rejects AS and DATA limits; fixed input/array sizes bound work.
    # Peak RSS is measurement, not a hard memory cap.
    resource.setrlimit(resource.RLIMIT_FSIZE, (2 * 1024**2, 2 * 1024**2))
    signal.alarm(30)
    p = argparse.ArgumentParser()
    p.add_argument('image')
    a = p.parse_args()
    im = Image.open(a.image).convert('RGB')
    assert im.size == (228, 228), 'Grid specification is for the supplied crop only'
    grid = []
    for r in range(32):
        row = []
        for c in range(32):
            rgb = im.getpixel((round(3.6 + 7.18*c), round(0.6 + 7.16*r)))
            dark = sum(abs(v-w) for v,w in zip(rgb, (21,24,28)))
            light = sum(abs(v-w) for v,w in zip(rgb, (235,230,218)))
            row.append(0 if dark < 75 else 1 if light < 75 else None)
        grid.append(row)
    scores = []
    for name, (dr,dc) in [('down',(1,0)), ('up',(-1,0)), ('right',(0,1)), ('left',(0,-1))]:
        for hand in [-1,1]:
            sr,sc = hand*dc, -hand*dr
            for invert in [0,1]:
                total = bad = 0
                for r in range(1,31):
                    for c in range(1,31):
                        q = [grid[r+sr][c+sc],grid[r][c],grid[r-sr][c-sc],grid[r+dr][c+dc]]
                        if None in q: continue
                        l,m,rr,n = [v ^ invert for v in q]
                        total += 1
                        bad += ((30 >> (4*l+2*m+rr)) & 1) != n
                scores.append(dict(time=name,hand=hand,invert=invert,total=total,bad=bad))
    print(json.dumps({'peak_rss_host_units':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
                      'scores': sorted(scores,key=lambda s:s['bad']/s['total']),
                      'grid_light_is_1': [''.join('?' if b is None else str(b) for b in row) for row in grid]}, indent=2))


if __name__ == '__main__':
    main()
