#!/usr/bin/env python3
"""local_flag_waiter.py: Local's flag waiter for the shared store (the semaphores protocol in sharedstore/README.md).

Polls the GPT and Cloud flag folders and exits as soon as a flag addressed to local (or to all) appears that is newer
than --since and not yet acknowledged in flags/local. It prints one line per new flag and exits 0, so a background run
wakes Local exactly once. Five failed polls in a row print one STORE ERROR line and exit 2, so a dead connection is
never silent.

The token and the store's address come from the environment (PLACEGO_SITE_TOKEN, PLACEGO_STORE_URL) and are never
printed. Nothing is written to the store.

Run: python3 -I sharedstore/local_flag_waiter.py --since 2026-10-27T10:00:00+00:00 [--interval 60]
"""
import argparse
import json
import os
import re
import ssl
import sys
import time
import urllib.request

FLAG = re.compile(r"^(local|all)\.([A-Z][A-Z-]*)\.(\w+)$")
LEGACY = re.compile(r"^[a-z0-9-]+-local$")


def fetch(url, token, path):
    req = urllib.request.Request(url + "?list=" + path, headers={"X-Store-Token": token})
    with urllib.request.urlopen(req, timeout=20, context=ssl.create_default_context()) as r:
        return json.load(r)["entries"]


def pending(url, token, since):
    acks = {e["name"] for e in fetch(url, token, "flags/local")}
    out = []
    for worker in ("gpt", "cloud"):
        for e in fetch(url, token, "flags/" + worker):
            name, mtime = e["name"], e.get("mtime", "")
            if mtime <= since:
                continue
            m = FLAG.match(name)
            if m:
                if "ack-%s-%s.%s.%s" % (worker, m.group(1), m.group(2), m.group(3)) in acks:
                    continue
            elif not LEGACY.match(name) or any(a.startswith("ack-") and name in a for a in acks):
                continue
            out.append((mtime, worker, name))
    return sorted(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--since", required=True, help="ISO time; only flags written after it count")
    ap.add_argument("--interval", type=float, default=60.0)
    args = ap.parse_args()
    token = os.environ.get("PLACEGO_SITE_TOKEN")
    url = os.environ.get("PLACEGO_STORE_URL")
    if not token or not url:
        print("STORE ERROR: PLACEGO_SITE_TOKEN or PLACEGO_STORE_URL is not set", flush=True)
        return 2
    failures = 0
    while True:
        try:
            new = pending(url, token, args.since)
            failures = 0
        except Exception as exc:                     # transient network or server errors: retry, then report
            failures += 1
            if failures >= 5:
                print("STORE ERROR after 5 polls: %s" % type(exc).__name__, flush=True)
                return 2
            time.sleep(args.interval)
            continue
        if new:
            for mtime, worker, name in new:
                print("NEW FLAG from %s: %s (%s)" % (worker, name, mtime), flush=True)
            return 0
        time.sleep(args.interval)


if __name__ == "__main__":
    sys.exit(main())
