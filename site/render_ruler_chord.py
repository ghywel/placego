#!/usr/bin/env python3
"""render_ruler_chord.py: the edge ruler's rhythm sped up until it rings as a chord, then back (the owner's ask,
2026-10-09: "the same as ... the Coprime app with the 'Rhythm becomes harmony' example").

RUN-ON:     cpu (Python 3, numpy, scipy; FFmpeg for the encodes); seconds
COMMAND:    python3 site/render_ruler_chord.py OUTDIR      (writes ruler-chord.wav, .m4a and .webm into OUTDIR)

Not part of the published folder: the page (site/wolframrule30/bricks.html) plays the encoded files, which live beside
the page on the site (the Cadence tree's Site/wolframrule30/, merged in by its publish-site.sh), outside this repo.

The rhythm is the page's own (Proposition 23): a white triangle meets the right edge at every even row t, and its size
depends only on v = v2(t). Voice v sounds at rows 2^v (2k + 1), so at R rows a second it is a pulse train at R / 2^(v+1):
the voices' rates stand exactly 1 : 1/2 : 1/4 : ..., and the rhythm the page plays (one note per triangle, an octave
lower for each doubling) is the Gray code counting. Speeding it up therefore fuses it into a stack of octaves.
Each voice is synthesised as in Coprime's wood block (Sources/TuningCore/Timbre.swift `pulse`, Sources/Kernel/synth.c):
unit spikes at the voice's rate, each split between two samples by its fractional position, ringing three resonators
at the body pitch x 1, 2.32, 4.25 (levels 1, 0.5, 0.25; T60 80, 50, 30 ms). The body pitch is the page's note for that
v (1760 Hz / 2^(v-1) to v = 7, A1 = 55 Hz with a longer ring below that), so at slow speed the clicks carry the same
octaves the page's Sound plays. As in Coprime, the rate follows raised-cosine moves in log2(rate): hold slow, rise,
ring (voice 1 at 440 Hz: A4, A3, A2, A1, the deep voices still beating under it), descend, hold slow; then a small room.
"""
import os
import subprocess
import sys

import numpy as np
from scipy.signal import fftconvolve, lfilter

SR = 48000
V = 12                                  # voices v = 1 .. 12 (voice 12 sounds once every 8192 rows)
SLOW, RING = 8.0, 1760.0                # rows a second: 4 triangles a second, and voice 1 at 440 Hz (A4)
LEGS = [(4.0, SLOW), (22.0, RING), (6.0, RING), (18.0, SLOW), (4.0, SLOW)]   # (seconds, target rows a second)
TAIL = 3.0
BETA = 0.42                             # the gain ride's exponent, set by measurement (see the level check)
FFMPEG = os.environ.get('FFMPEG', 'ffmpeg')


def rate_curve(n):
    t = np.arange(n) / SR
    lr = np.full(n, np.log2(SLOW))
    t0, frm = 0.0, np.log2(SLOW)
    for dur, to in LEGS:
        to = np.log2(to)
        m = (t >= t0) & (t < t0 + dur)
        u = (t[m] - t0) / dur
        lr[m] = frm + (to - frm) * (0.5 - 0.5 * np.cos(np.pi * u))
        t0, frm = t0 + dur, to
    lr[t >= t0] = frm
    return 2.0 ** lr


def spikes(phase):
    """unit spikes where phase crosses an integer, split between two samples by the fractional position"""
    x = np.zeros(len(phase) + 1)
    k = np.floor(phase)
    idx = np.nonzero((k[1:] > k[:-1]) & (k[1:] >= 0))[0] + 1
    inc = phase[idx] - phase[idx - 1]
    frac = (phase[idx] - k[idx]) / inc                   # how far past the crossing this sample is, in samples
    np.add.at(x, idx, 1 - frac)
    np.add.at(x, idx + 1, frac)
    return x[:-1]


def resonate(x, body, scale):
    y = np.zeros_like(x)
    for ratio, amp, t60 in ((1.0, 1.0, 0.08), (2.32, 0.5, 0.05), (4.25, 0.25, 0.03)):
        w = 2 * np.pi * body * ratio / SR
        if not 0 < w < 0.9 * np.pi:
            continue
        r = 10 ** (-3.0 / (t60 * scale * SR))
        y += lfilter([amp * np.sin(w)], [1, -2 * r * np.cos(w), r * r], x)
    return y


def main():
    out = sys.argv[1] if len(sys.argv) > 1 else '.'
    os.makedirs(out, exist_ok=True)
    total = sum(d for d, _ in LEGS) + TAIL
    n = int(total * SR)
    R = rate_curve(n)
    rows = 1.0 + np.cumsum(R) / SR                       # the ruler's row; voice v sounds as rows passes 2^v (2k + 1)
    L, Rt = np.zeros(n), np.zeros(n)
    ride = (R / SLOW) ** -BETA                           # loudness follows the event rate; ride it so the chord does not
                                                       # come in some 26 dB above the clicks (a crescendo of ~12 dB stays)
    for v in range(1, V + 1):
        phase = (rows - 2 ** v) / 2 ** (v + 1)
        x = spikes(phase)
        body, scale = (1760.0 / 2 ** (v - 1), 1.0) if v <= 7 else (55.0, 4.0)
        y = resonate(x * ride, body, scale) * (0.35 * min(1.0, 0.45 + 0.08 * v))
        pan = ((v % 5) - 2) * 0.22                       # spread the voices a little, as Coprime pans its blocks
        L += y * np.sqrt(0.5 * (1 - pan)); Rt += y * np.sqrt(0.5 * (1 + pan))
    # the room: decaying noise, T60 1.6 s, mixed at 0.18 (Coprime's piece uses room 0.18, 1.6, 0.45)
    rng = np.random.default_rng(30)
    m = int(1.6 * SR)
    env = 10 ** (-3.0 * np.arange(m) / m)
    for ch in (0, 1):
        ir = rng.standard_normal(m) * env
        ir /= np.sqrt((ir ** 2).sum())
        sig = L if ch == 0 else Rt
        wet = fftconvolve(sig, ir)[:n]
        if ch == 0:
            L = 0.82 * L + 0.18 * wet
        else:
            Rt = 0.82 * Rt + 0.18 * wet
    # level: the ringing chord is far denser than the slow clicks, so a gentle limiter keeps both audible
    st = np.stack([L, Rt], axis=1)
    t_ring = sum(d for d, _ in LEGS[:2])                 # the ring holds from here for LEGS[2]'s seconds
    ring = st[int(t_ring * SR): int((t_ring + LEGS[2][0]) * SR)]
    st *= 10 ** (-14 / 20) / np.sqrt((ring ** 2).mean())   # the ringing chord at -14 dBFS RMS
    st = np.tanh(st / 0.9) * 0.9                         # the summit is compressed, never clipped
    fade = int(0.5 * SR)
    st[-fade:] *= np.linspace(1, 0, fade)[:, None]
    pcm = (np.clip(st, -1, 1) * 32767).astype('<i2')
    wav = os.path.join(out, 'ruler-chord.wav')
    import wave
    with wave.open(wav, 'wb') as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(pcm.tobytes())
    subprocess.run([FFMPEG, '-y', '-loglevel', 'error', '-i', wav, '-c:a', 'aac_at', '-b:a', '160k',
                    os.path.join(out, 'ruler-chord.m4a')], check=True)
    subprocess.run([FFMPEG, '-y', '-loglevel', 'error', '-i', wav, '-c:a', 'opus', '-strict', '-2', '-b:a', '128k',
                    '-ar', '48000', os.path.join(out, 'ruler-chord.webm')], check=True)
    print('rendered %.1f s; peak rate %.0f rows/s (voice 1 at %.0f Hz)' % (total, R.max(), R.max() / 4))


if __name__ == '__main__':
    main()
