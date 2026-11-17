#!/usr/bin/env python3
"""Rank moments in a rendered flow field by how likely they are to hide a defect.

    ./prospect.sh <source> [options]      # wrapper that renders, then runs this

WHAT THIS IS FOR. Finding defects is a two-stage job and the stages have
different strengths. A human eye is slow but reliable: it sees a visually
incoherent frame immediately and is not fooled by a number. This is fast but
literal: it sees data perturbation, which correlates with defects but is not
the same thing. So this decides nothing -- it produces a shortlist of moments
worth a human look, turning "watch the whole film" into "check these twenty".

Expect false positives. A perturbation that turns out to be statistical noise
is a correct outcome for this tool, not a failure of it.

THE SIGNAL. For every pixel, the distance between its flow vector and the
MEDIAN of its neighbourhood. A genuine motion boundary is a contiguous region,
so most of its neighbours share its value and its deviation stays small. An
isolated false match -- the estimator locking confidently onto the wrong shape
-- is a local minority everywhere and deviates hugely. So this sees false
matches and largely ignores real motion.

THE THRESHOLD IS RELATIVE, deliberately. What counts as a lot of outlier
pixels depends entirely on the material -- flat animation and grainy live
action sit orders of magnitude apart, and a fixed count either floods on one
or goes silent on the other. So a moment is flagged when it is unusual
*against the rest of this scan*: median plus k robust deviations. The
consequence worth understanding is that this finds the worst moments in what
it is given, not moments that are bad in absolute terms. If a whole scan is
uniformly poor there is no outlier to find, and it says so instead of
inventing a ranking.

STREAMING. Frames are consumed one at a time and only per-frame scalars are
kept. This matters: a 60-second clip at 1920x1038 is 3886 output frames, which
is 21.6 GB of raw RGB. An earlier version held all of it and would simply die.
Nothing here scales with clip length except two small arrays of floats.

Input is a flow visualiser's output (see flowvis.py), which encodes f.x in R
and f.y in G as 0.5 + f*0.05 -- +-10 px full scale. Either give it a rendered
file, or pipe raw rgb24 into it with --stream.
"""
import argparse
import os

# MUST be set before numpy is imported, because that is when the BLAS backend
# initialises its thread pool. The work here is parallelised across PROCESSES,
# so a per-worker thread pool is not merely redundant -- with a worker per core
# each spawning a pool sized for every core, MSYS2's OpenBLAS build exhausts
# memory and dies with "Memory allocation still failed after 10 retries".
for _v in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS",
           "NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(_v, "1")

import subprocess
import sys

import numpy as np

FF = os.environ.get("FFMPEG", "ffmpeg")
FP = os.environ.get("FFPROBE", "ffprobe")
SCALE = 10.0 / 127.5          # one 8-bit step, in pixels


def probe(path, key):
    out = subprocess.run(
        [FP, "-v", "error", "-select_streams", "v:0", "-show_entries",
         f"stream={key}", "-of", "default=noprint_wrappers=1:nokey=1", path],
        capture_output=True, text=True).stdout.strip().splitlines()
    return out[0] if out else ""


def read_exactly(fh, n):
    """Pipes return short reads; a frame must be assembled from several."""
    chunks = []
    got = 0
    while got < n:
        b = fh.read(n - got)
        if not b:
            return None
        chunks.append(b)
        got += len(b)
    return b"".join(chunks)


def raw_frames(path=None, dims=None):
    """Yield one frame's raw bytes at a time, plus its dimensions.

    Only the bytes are yielded, not decoded arrays: the decode and the metric
    both happen in a worker process, so the reader stays cheap enough to keep
    the pipe drained. That matters -- measured on a 16-thread machine, the
    single-threaded version left the GPU at 5% and the CPU at 10% because
    ffmpeg and the analyser were taking turns instead of overlapping.
    """
    proc = None
    if path:
        # Dimensions are probed, never assumed: a wrong size reinterprets the
        # byte stream and still produces a full, plausible ranking.
        w, h = int(probe(path, "width")), int(probe(path, "height"))
        proc = subprocess.Popen(
            [FF, "-v", "error", "-i", path, "-f", "rawvideo",
             "-pix_fmt", "rgb24", "-"],
            stdout=subprocess.PIPE)
        fh = proc.stdout
    else:
        w, h = dims
        fh = sys.stdin.buffer

    nbytes = w * h * 3
    try:
        while True:
            buf = read_exactly(fh, nbytes)
            if buf is None:
                break
            yield buf, w, h
    finally:
        if proc:
            try:
                proc.stdout.close()
            except Exception:
                pass
            proc.wait()


def analyse(job):
    """One frame's metric. Module-level and self-contained so it can be run in
    a worker process (Windows spawns rather than forks, so closures are out)."""
    buf, w, h, radius, threshold = job
    a = np.frombuffer(buf, np.uint8).reshape(h, w, 3)
    fx = (a[..., 0].astype(np.float32) - 127.5) * SCALE
    fy = (a[..., 1].astype(np.float32) - 127.5) * SCALE
    dev = np.hypot(fx - med_blur(fx, radius), fy - med_blur(fy, radius))
    return int((dev > threshold).sum()), float(dev.max())


def med_blur(a, r):
    """Median over a (2r+1) box, sampled on a decimated grid.

    Sampling the neighbourhood rather than using every pixel is fine here:
    what is wanted is the neighbourhood's consensus value, not an exact
    median, and it keeps the working set to a few hundred MB.
    """
    h, w = a.shape
    p = np.pad(a, r, mode="edge")
    step = max(1, r // 3)
    stack = [p[dy + r:dy + r + h, dx + r:dx + r + w]
             for dy in range(-r, r + 1, step)
             for dx in range(-r, r + 1, step)]
    return np.median(np.stack(stack, 0), axis=0)


def hhmmss(t):
    m, s = divmod(t, 60)
    h, m = divmod(int(m), 60)
    return f"{h:d}:{m:02d}:{s:06.3f}" if h else f"{int(m):d}:{s:06.3f}"


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("flowvis", nargs="?",
                    help="flow visualiser render; omit when using --stream")
    ap.add_argument("--stream", action="store_true",
                    help="read raw rgb24 from stdin instead of a file")
    ap.add_argument("--width", type=int)
    ap.add_argument("--height", type=int)
    ap.add_argument("--source", default="<source>",
                    help="original source path, for the emitted clip commands")
    ap.add_argument("--src-fps", type=float, default=24000.0 / 1001.0)
    ap.add_argument("--out-fps", type=float, default=60.0)
    ap.add_argument("--offset", type=float, default=0.0,
                    help="seconds into the source that this render starts")
    ap.add_argument("--radius", type=int, default=6)
    ap.add_argument("--threshold", type=float, default=3.0,
                    help="px of flow deviation that counts a pixel as an outlier")
    ap.add_argument("--k", type=float, default=3.0,
                    help="robust deviations above the scan median to flag a frame")
    ap.add_argument("--top", type=int, default=20)
    ap.add_argument("--gap", type=int, default=6,
                    help="output frames of quiet that separate two candidates")
    ap.add_argument("--progress", type=int, default=0,
                    help="print a heartbeat every N frames (0 = off)")
    ap.add_argument("--jobs", type=int, default=0,
                    help="analysis worker processes (0 = cpu_count-2, 1 = serial)")
    ap.add_argument("--save", metavar="FILE",
                    help="write per-frame measurements here so the scan can be "
                         "re-analysed later without re-rendering")
    ap.add_argument("--load", metavar="FILE",
                    help="re-analyse a saved scan instead of rendering one")
    ap.add_argument("--exclude", metavar="FILE",
                    help="file of source timestamps (one per line, first column) "
                         "to mask out before ranking -- typically scene cuts")
    ap.add_argument("--exclude-pad", type=int, default=4,
                    help="output frames masked either side of each timestamp")
    args = ap.parse_args()

    if args.load:
        counts, peaks = [], []
        w = h = 0
        with open(args.load) as fh:
            for line in fh:
                line = line.rstrip("\n")
                if not line.strip():
                    continue
                if line.startswith("#"):
                    parts = line.split()
                    if len(parts) >= 3:
                        if parts[1] == "size":
                            w, h = (int(v) for v in parts[2].split("x"))
                        elif parts[1] == "src_fps":
                            args.src_fps = float(parts[2])
                        elif parts[1] == "out_fps":
                            args.out_fps = float(parts[2])
                        elif parts[1] == "offset":
                            args.offset = float(parts[2])
                        elif parts[1] == "source" and args.source == "<source>":
                            args.source = line.split(None, 2)[2]
                    continue
                f = line.split("\t")
                counts.append(int(f[1])); peaks.append(float(f[2]))
        if not counts:
            raise SystemExit(f"no measurements in {args.load}")
        print(f"  loaded {len(counts)} frames from {args.load}")
        report(counts, peaks, w, h, args)
        return


    if args.stream:
        if not (args.width and args.height):
            sys.exit("--stream needs --width and --height")
        src = raw_frames(dims=(args.width, args.height))
    else:
        if not args.flowvis:
            sys.exit("give a flow visualiser render, or use --stream")
        src = raw_frames(path=args.flowvis)

    # Capped as well as scaled: each worker's median stack is a few hundred MB
    # at a realistic analysis grid, so one worker per core would trade a
    # bottleneck for an out-of-memory failure.
    jobs = args.jobs or max(1, min(8, (os.cpu_count() or 4) - 2))
    counts, peaks = [], []
    w = h = 0

    if jobs <= 1:
        for i, (buf, w, h) in enumerate(src):
            c, p = analyse((buf, w, h, args.radius, args.threshold))
            counts.append(c); peaks.append(p)
            if args.progress and (i + 1) % args.progress == 0:
                print(f"    ...{i + 1} frames", file=sys.stderr, flush=True)
    else:
        # Submission is BOUNDED to a couple of frames per worker. An unbounded
        # map would read the whole stream into memory, which is the 21.6 GB
        # problem this tool exists to avoid; a bounded window keeps every
        # worker fed while holding only a few tens of MB.
        from collections import deque
        from concurrent.futures import ProcessPoolExecutor
        limit = jobs * 2
        with ProcessPoolExecutor(max_workers=jobs) as ex:
            pending = deque()
            done = 0
            for buf, w, h in src:
                pending.append(ex.submit(
                    analyse, (buf, w, h, args.radius, args.threshold)))
                while len(pending) >= limit:
                    c, p = pending.popleft().result()
                    counts.append(c); peaks.append(p); done += 1
                    if args.progress and done % args.progress == 0:
                        print(f"    ...{done} frames", file=sys.stderr, flush=True)
            while pending:
                c, p = pending.popleft().result()
                counts.append(c); peaks.append(p); done += 1

    if args.save:
        with open(args.save, "w") as fh:
            fh.write(f"# prospect scan\n")
            fh.write(f"# size {w}x{h}\n")
            fh.write(f"# out_fps {args.out_fps}\n")
            fh.write(f"# src_fps {args.src_fps}\n")
            fh.write(f"# offset {args.offset}\n")
            fh.write(f"# radius {args.radius}\n")
            fh.write(f"# threshold {args.threshold}\n")
            fh.write(f"# source {args.source}\n")
            fh.write("# frame\toutliers\tpeak_px\n")
            for i, (c, pk) in enumerate(zip(counts, peaks)):
                fh.write(f"{i}\t{c}\t{pk:.4f}\n")
        print(f"  saved {len(counts)} measurements to {args.save}")

    report(counts, peaks, w, h, args)


def report(counts, peaks, w, h, args):
    """Rank and print. Split out so a saved scan can be re-ranked."""
    n = len(counts)
    if n == 0:
        sys.exit("no frames read")
    counts = np.array(counts)
    peaks = np.array(peaks)

    # Scene cuts are enormous, loud and -- once handled -- uninteresting. They
    # dominate the ranking AND inflate the robust deviation, which raises the
    # threshold and hides everything smaller. Masking them does not merely
    # remove them from the list; it lets the rest of the material be scored
    # against its own baseline instead of against the cuts.
    masked = np.zeros(n, dtype=bool)
    if args.exclude:
        stamps = []
        for line in open(args.exclude):
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            try:
                stamps.append(float(line.split()[0]))
            except ValueError:
                continue
        for ts in stamps:
            k = int(round((ts - args.offset) * args.out_fps))
            lo = max(0, k - args.exclude_pad)
            hi = min(n, k + args.exclude_pad + 1)
            masked[lo:hi] = True
        print(f"  masked {int(masked.sum())} of {n} frames "
              f"around {len(stamps)} excluded timestamps")

    live = counts[~masked]
    if live.size == 0:
        sys.exit("everything was masked")

    med = float(np.median(live))
    mad = float(np.median(np.abs(live - med)))
    sigma = 1.4826 * mad
    # A floor keeps a genuinely clean scan from flagging single-pixel noise
    # just because its own variance is tiny.
    floor = max(30.0, 0.00002 * w * h)
    cut = max(med + args.k * sigma, med * 1.5, floor)

    total = int(live.sum())
    print(f"  {n} output frames at {w}x{h}"
          + (f", {live.size} after masking" if masked.any() else ""))
    print(f"  {total} outlier pixels, {total / live.size:.1f} per frame "
          f"(median {med:.0f}, robust sd {sigma:.0f})")
    print(f"  flagging frames above {cut:.0f} outlier pixels")

    hot = [i for i in range(n) if counts[i] > cut and not masked[i]]
    if not hot:
        print("  nothing stands out -- this material looks uniform to the metric")
        return

    frac = len(hot) / max(1, int((~masked).sum()))
    if frac > 0.4:
        print(f"  NOTE: {frac:.0%} of frames flagged. This scan is broadly")
        print("  perturbed rather than containing isolated defects, so the")
        print("  ranking below is weak -- the whole window is worth watching.")

    segments = []
    for i in hot:
        if segments and i - segments[-1][1] <= args.gap:
            segments[-1][1] = i
        else:
            segments.append([i, i])

    scored = sorted(
        ((int(counts[a:b + 1].max()), a, b, float(peaks[a:b + 1].max()))
         for a, b in segments), reverse=True)

    print(f"  {len(segments)} candidate moments")
    print()
    print("  rank  time (in source)          src frames    peak px   worst dev")
    print("  " + "-" * 68)
    for rank, (mx, a, b, pk) in enumerate(scored[:args.top], 1):
        t0 = args.offset + a / args.out_fps
        t1 = args.offset + b / args.out_fps
        f0 = int(t0 * args.src_fps)
        f1 = int(t1 * args.src_fps) + 1
        print(f"  {rank:>4}  {hhmmss(t0):>10} - {hhmmss(t1):<10} "
              f"{f0:>7}-{f1:<7} {mx:>7} {pk:>10.1f}")

    print()
    print("  To cut any of these for a closer look (frame-exact, lossless):")
    print()
    for _mx, a, b, _pk in scored[:min(5, args.top)]:
        mid = args.offset + ((a + b) / 2) / args.out_fps
        pad = max(6, int((b - a) / 2 * args.src_fps / args.out_fps) + 4)
        print(f"    ./clip.sh {args.source} {mid:.3f} {pad}")
    print()
    print("  Times are positions in the SOURCE, usable directly in a player")
    print("  showing either the source or the interpolated output.")




if __name__ == "__main__":
    main()
