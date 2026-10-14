#!/usr/bin/env python3
"""test_store.py: runs store.php under PHP's built-in server with a throwaway config and checks every rule.

COMMAND:  python3 sharedstore/test_store.py      (needs the php command line; nothing leaves this machine)

It starts two servers on 127.0.0.1: one with require_https off (the functional tests) and one with it on (plain HTTP
must be refused). Two workers, alice and bob, have tokens made here. Every check prints PASS or FAIL, and the script
exits non-zero if any fails.
"""
import hashlib
import http.client
import json
import os
import pathlib
import shutil
import subprocess
import sys
import tempfile
import time

HERE = pathlib.Path(__file__).resolve().parent
RESULTS = []


def check(name, ok, detail=''):
    RESULTS.append(ok)
    print('%s  %s%s' % ('PASS' if ok else 'FAIL', name, ('  (' + detail + ')') if detail and not ok else ''))


def start(root, cfg_path, port):
    env = dict(os.environ, SHAREDSTORE_CONFIG=str(cfg_path))
    p = subprocess.Popen(['php', '-S', '127.0.0.1:%d' % port, '-t', str(root)], env=env,
                         stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    for _ in range(50):
        try:
            c = http.client.HTTPConnection('127.0.0.1', port, timeout=2)
            c.request('GET', '/store.php')
            c.getresponse().read()
            return p
        except OSError:
            time.sleep(0.1)
    raise RuntimeError('php server did not start')


def call(port, method, query, token=None, body=None, header='X-Store-Token', extra=None):
    c = http.client.HTTPConnection('127.0.0.1', port, timeout=10)
    headers = dict(extra or {})
    if token:
        headers[header] = token if header == 'X-Store-Token' else 'Bearer ' + token
    c.request(method, '/store.php?' + query, body=body, headers=headers)
    r = c.getresponse()
    data = r.read()
    return r.status, data


def write_config(path, data_dir, log_file, https, tokens, cap=0):
    workers = ''.join("        '%s' => '%s',\n" % (n, hashlib.sha256(t.encode()).hexdigest()) for n, t in tokens.items())
    path.write_text("<?php\nreturn [\n    'data_dir' => '%s',\n    'log_file' => '%s',\n    'require_https' => %s,\n"
                    "    'max_bytes' => 1000,\n    'max_total_bytes' => %d,\n    'workers' => [\n%s    ],\n];\n"
                    % (data_dir, log_file, 'true' if https else 'false', cap, workers))


def main():
    if not shutil.which('php'):
        print('php not found')
        return 2
    tmp = pathlib.Path(tempfile.mkdtemp(prefix='sharedstore-test-'))
    web = tmp / 'web'
    web.mkdir()
    shutil.copy(HERE / 'store.php', web / 'store.php')
    data = tmp / 'data'
    data.mkdir()
    log = tmp / 'store.log'
    tokens = {'alice': 'a' * 64, 'bob': 'b' * 64}
    write_config(tmp / 'config.php', data, log, False, tokens)
    write_config(tmp / 'config_https.php', data, log, True, tokens)
    A, B = tokens['alice'], tokens['bob']
    p1 = start(web, tmp / 'config.php', 8771)
    p2 = start(web, tmp / 'config_https.php', 8772)
    qdata = tmp / 'qdata'
    qdata.mkdir()
    write_config(tmp / 'config_quota.php', qdata, tmp / 'q.log', False, tokens, cap=2500)
    p3 = start(web, tmp / 'config_quota.php', 8773)
    P = 8771
    try:
        s, _ = call(P, 'GET', 'whoami')
        check('no token is refused (401)', s == 401, str(s))
        s, _ = call(P, 'GET', 'whoami', 'z' * 64)
        check('unknown token is refused (401)', s == 401, str(s))
        s, d = call(P, 'GET', 'whoami', A)
        check('whoami names the worker', s == 200 and json.loads(d)['worker'] == 'alice', d.decode())
        s, d = call(P, 'GET', 'whoami', B, header='Authorization')
        check('a Bearer token works too', s == 200 and json.loads(d)['worker'] == 'bob', d.decode())

        body = b'hello from alice\n'
        s, d = call(P, 'PUT', 'path=workers/alice/notes/a.txt', A, body)
        ok = s == 200 and json.loads(d)['sha256'] == hashlib.sha256(body).hexdigest()
        check('alice writes in her own area, digest returned', ok, d.decode())
        s, d = call(P, 'GET', 'path=workers/alice/notes/a.txt', B)
        check('bob reads it back byte for byte', s == 200 and d == body, str(s))
        s, d = call(P, 'GET', 'stat=workers/alice/notes/a.txt', B)
        check('stat gives the same digest', s == 200 and json.loads(d)['sha256'] == hashlib.sha256(body).hexdigest())
        s, _ = call(P, 'PUT', 'path=workers/alice/notes/a.txt', A, b'replaced\n')
        s2, d = call(P, 'GET', 'path=workers/alice/notes/a.txt', A)
        check('alice may replace her own file', s == 200 and d == b'replaced\n')

        s, _ = call(P, 'PUT', 'path=workers/bob/x.txt', A, b'x')
        check("alice may not write in bob's area (403)", s == 403, str(s))
        s, _ = call(P, 'PUT', 'path=flags/bob/f', A, b'x')
        check("alice may not write bob's flags (403)", s == 403, str(s))
        s, _ = call(P, 'PUT', 'path=flags/alice/state', A, b'busy\n')
        s2, d = call(P, 'GET', 'path=flags/alice/state', B)
        check('flags: alice writes hers, bob reads it', s == 200 and d == b'busy\n')
        s, _ = call(P, 'PUT', 'path=top.txt', A, b'x')
        check('nothing outside the areas is writable (403)', s == 403, str(s))
        s, _ = call(P, 'PUT', 'path=workers/alice', A, b'x')
        check('an area root is not a file you own (403)', s == 403, str(s))

        s, _ = call(P, 'PUT', 'path=cited/cert/k140.drup', B, b'proof\n')
        check('anyone may create a cited file', s == 200, str(s))
        s, _ = call(P, 'PUT', 'path=cited/cert/k140.drup', B, b'other\n')
        s2, d = call(P, 'GET', 'path=cited/cert/k140.drup', A)
        check('a cited file is never overwritten (409), content kept', s == 409 and d == b'proof\n', str(s))
        s, _ = call(P, 'DELETE', 'path=cited/cert/k140.drup', B)
        check('a cited file cannot be deleted (403)', s == 403, str(s))

        s1, _ = call(P, 'POST', 'append=log/manifest.jsonl', A, b'{"a": 1}\n')
        s2, _ = call(P, 'POST', 'append=log/manifest.jsonl', B, b'{"b": 2}\n')
        s3, d = call(P, 'GET', 'path=log/manifest.jsonl', A)
        check('log/: anyone appends, lines kept in order', (s1, s2, s3) == (200, 200, 200) and d == b'{"a": 1}\n{"b": 2}\n')
        s, _ = call(P, 'PUT', 'path=log/manifest.jsonl', A, b'wiped')
        check('log/ cannot be replaced (403)', s == 403, str(s))
        s, _ = call(P, 'DELETE', 'path=log/manifest.jsonl', A)
        check('log/ cannot be deleted (403)', s == 403, str(s))

        bad = ['../etc/passwd', 'workers/alice/../../x', '/etc/passwd', '.hidden', 'workers/alice/.tmp-x',
               'workers/alice/a\\b', 'workers//alice/x', 'workers/alice/x/', '']
        codes = [call(P, 'PUT', 'path=' + q, A, b'x')[0] for q in bad]
        check('bad paths are refused (400): ' + ', '.join(repr(b) for b in bad), all(c == 400 for c in codes),
              str(codes))
        codes = [call(P, 'GET', 'list=' + q, A)[0] for q in ['..', '../..', '/']]
        check('listing outside the data folder is refused (400)', all(c == 400 for c in codes), str(codes))

        s, _ = call(P, 'PUT', 'path=workers/alice/big.bin', A, b'x' * 2000)
        leftovers = [f.name for f in (data / 'workers' / 'alice').iterdir() if f.name.startswith('.tmp')]
        check('a body over the limit is refused (413), nothing left behind',
              s == 413 and not (data / 'workers/alice/big.bin').exists() and not leftovers, str(s))

        s, d = call(P, 'GET', 'list=workers/alice', B)
        names = [e['name'] for e in json.loads(d)['entries']]
        check('listing shows the folder and hides dotfiles', s == 200 and 'notes' in names and not any(
            n.startswith('.') for n in names), d.decode())

        s, _ = call(P, 'DELETE', 'path=workers/alice/notes/a.txt', B)
        check("bob may not delete alice's file (403)", s == 403, str(s))
        s, _ = call(P, 'DELETE', 'path=workers/alice/notes/a.txt', A)
        s2, _ = call(P, 'GET', 'path=workers/alice/notes/a.txt', A)
        check('alice deletes her own file; it is gone', s == 200 and s2 == 404, '%s %s' % (s, s2))

        s, _ = call(P, 'POST', 'put=workers/bob/fallback.txt', B, b'via post\n')
        s2, d = call(P, 'GET', 'path=workers/bob/fallback.txt', A)
        s3, _ = call(P, 'POST', 'delete=workers/bob/fallback.txt', B)
        s4, _ = call(P, 'GET', 'path=workers/bob/fallback.txt', A)
        check('POST fallbacks for PUT and DELETE work', (s, s2, s3, s4) == (200, 200, 200, 404) and d == b'via post\n',
              str((s, s2, s3, s4)))

        s, d = call(8772, 'GET', 'whoami', A)
        check('with require_https on, plain HTTP is refused (403)', s == 403, '%s %s' % (s, d))
        s, d = call(8772, 'GET', 'whoami', A, extra={'X-Forwarded-Proto': 'https'})
        check('a spoofed X-Forwarded-Proto over plain HTTP is refused too (403)', s == 403, '%s %s' % (s, d))

        r = [call(8773, 'PUT', 'path=workers/alice/q%d.bin' % i, A, b'q' * 900)[0] for i in range(2)]
        s, d = call(8773, 'PUT', 'path=cited/q.bin', A, b'q' * 900)
        s2, _ = call(8773, 'POST', 'append=log/q.log', A, b'q' * 900)
        left = [f for f in qdata.rglob('.tmp-*')]
        check('the total cap: two writes fit, the third and an append are refused (507), nothing left behind',
              r == [200, 200] and s == 507 and s2 == 507 and not left and not (qdata / 'cited/q.bin').exists(),
              str((r, s, s2, len(left))))

        lines = [json.loads(l) for l in log.read_text().splitlines()]
        ops = [(l['worker'], l['op']) for l in lines]
        check('every successful write (9) is logged with the worker', len(lines) == 9 and ('alice', 'put') in ops
              and ('bob', 'append') in ops and ('alice', 'delete') in ops, str(ops))
    finally:
        for p in (p1, p2, p3):
            p.terminate()
            p.wait()
        shutil.rmtree(tmp)
    print('\n%d of %d checks pass' % (sum(RESULTS), len(RESULTS)))
    return 0 if all(RESULTS) else 1


if __name__ == '__main__':
    sys.exit(main())
