#!/usr/bin/env python3
"""Restore the chunk files of the eight-street certificate stream from the released level files.

Usage:  python3 l8_release_unpack.py RELEASEDIR OUTDIR

Reads manifest.json and E<m>.jsonl.xz from RELEASEDIR, checks every compressed file's SHA-256, splits each level back
into its chunk files E<m>_l<l1>.jsonl (a chunk ends at its footer line), and checks every level's uncompressed SHA-256
and the whole stream's SHA-256 against the manifest. Then run, on OUTDIR:
    python3 l8_certificates.py check OUTDIR      (re-verifies every tiling; prints both digests)
    python3 l8_stream_verify.py OUTDIR           (independent completeness and tiling verifier)
"""
import sys, os, json, hashlib, lzma

def sha_file(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for block in iter(lambda: f.read(1 << 20), b''): h.update(block)
    return h.hexdigest()

if __name__ == '__main__':
    rel, out = sys.argv[1], sys.argv[2]; os.makedirs(out, exist_ok=True)
    man = json.load(open(os.path.join(rel, 'manifest.json')))
    stream = hashlib.sha256(); written = []
    for m in sorted(man['levels'], key=int):
        v = man['levels'][m]; xz = os.path.join(rel, v['xz_file'])
        assert sha_file(xz) == v['xz_sha256'], f"compressed file {v['xz_file']} does not match the manifest"
        lvl = hashlib.sha256(); names = []; buf = []
        with lzma.open(xz, 'rb') as z:
            for raw in z:
                lvl.update(raw); stream.update(raw); buf.append(raw)
                if b'"end"' in raw:
                    r = json.loads(raw); name = f"E{r['m']}_l{r['l1']}.jsonl"
                    with open(os.path.join(out, name), 'wb') as f: f.writelines(buf)
                    names.append(name); buf = []
        assert not buf, f"level {m} ends without a footer"
        assert lvl.hexdigest() == v['sha256'], f"level {m} does not match the manifest"
        assert sorted(names) == v['chunks'], f"level {m} chunk names differ from the manifest"
        written += names; print(f"E{m}: {len(names)} chunk files restored", flush=True)
    assert stream.hexdigest() == man['stream_sha256'], "stream digest does not match the manifest"
    print(f"{len(written)} chunk files; stream sha256 {stream.hexdigest()} matches the manifest")
