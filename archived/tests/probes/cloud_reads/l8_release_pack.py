#!/usr/bin/env python3
"""Pack the eight-street certificate stream for public release, and fingerprint it in the same pass.

Usage:  python3 l8_release_pack.py CERTDIR RELEASEDIR [--workers N] [--preset P]

CERTDIR holds the chunk files E<m>_l<l1>.jsonl written by l8_certificates.py. Nothing in it is changed.
RELEASEDIR receives one compressed file per level, E<m>.jsonl.xz, and manifest.json with:
  - stream_sha256: SHA-256 of all chunk files concatenated in sorted name order (the digest l8_certificates.py check
    and l8_stream_verify.py print; 90fea878... for the retained 19 October 2026 run);
  - timing_free_sha256: the same stream with the elapsed-time field removed from each chunk footer (identical for
    every regeneration with the same programs);
  - per level: chunk names, record count, bytes and SHA-256 of the uncompressed level file, bytes and SHA-256 of the
    compressed file.
Each level file is its chunk files concatenated in sorted name order, so concatenating the level files E24..E32
reproduces the stream byte for byte. l8_release_unpack.py restores the chunk files. Run it outside git: the data
stays out of the repository.
"""
import sys, os, json, hashlib, lzma, argparse
from multiprocessing import Pool

def chunk_files(certdir):
    files = sorted(f for f in os.listdir(certdir) if f.endswith('.jsonl'))
    levels = {}
    for f in files:
        levels.setdefault(int(f[1:f.index('_')]), []).append(f)
    # the global sorted order must equal the level-by-level order, so level files concatenate to the stream
    assert [f for m in sorted(levels) for f in levels[m]] == files, "chunk names do not group by level"
    return files, levels

def fingerprint(certdir, files):
    h, hc, records, footers = hashlib.sha256(), hashlib.sha256(), 0, 0
    for fn in files:
        with open(os.path.join(certdir, fn), 'rb') as f:
            for raw in f:
                h.update(raw)
                if b'"end"' in raw:
                    r = json.loads(raw); footers += 1
                    hc.update((json.dumps({k: v for k, v in r.items() if k != 'seconds'}) + "\n").encode())
                else:
                    hc.update(raw); records += 1
    return h.hexdigest(), hc.hexdigest(), records, footers

def pack_level(args):
    certdir, releasedir, m, names, preset = args
    out = os.path.join(releasedir, f"E{m}.jsonl.xz")
    raw_h, n_bytes, n_rec = hashlib.sha256(), 0, 0
    with lzma.open(out, 'wb', preset=preset) as z:
        for fn in names:
            with open(os.path.join(certdir, fn), 'rb') as f:
                for raw in f:
                    raw_h.update(raw); n_bytes += len(raw); z.write(raw)
                    if b'"end"' not in raw: n_rec += 1
    xz_h = hashlib.sha256()
    with open(out, 'rb') as f:
        for block in iter(lambda: f.read(1 << 20), b''): xz_h.update(block)
    return m, {'chunks': names, 'records': n_rec, 'bytes': n_bytes, 'sha256': raw_h.hexdigest(),
               'xz_file': os.path.basename(out), 'xz_bytes': os.path.getsize(out), 'xz_sha256': xz_h.hexdigest()}

if __name__ == '__main__':
    ap = argparse.ArgumentParser(); ap.add_argument('certdir'); ap.add_argument('releasedir')
    ap.add_argument('--workers', type=int, default=4); ap.add_argument('--preset', type=int, default=6)
    a = ap.parse_args(); os.makedirs(a.releasedir, exist_ok=True)
    files, levels = chunk_files(a.certdir)
    s, sc, records, footers = fingerprint(a.certdir, files)
    print(f"{len(files)} chunk files, {footers} footers, {records} records", flush=True)
    print(f"stream sha256      {s}", flush=True)
    print(f"timing-free sha256 {sc}", flush=True)
    with Pool(a.workers) as pool:
        per = dict(pool.map(pack_level, [(a.certdir, a.releasedir, m, levels[m], a.preset) for m in sorted(levels)]))
    man = {'stream_sha256': s, 'timing_free_sha256': sc, 'records': records, 'chunk_files': len(files),
           'xz_preset': a.preset, 'levels': {str(m): per[m] for m in sorted(per)}}
    assert sum(v['records'] for v in per.values()) == records
    with open(os.path.join(a.releasedir, 'manifest.json'), 'w') as f: json.dump(man, f, indent=1)
    for m in sorted(per):
        v = per[m]; print(f"E{m}: {v['records']} records, {v['bytes']} bytes -> {v['xz_bytes']} xz, sha256 {v['xz_sha256']}")
    print("manifest.json written")
