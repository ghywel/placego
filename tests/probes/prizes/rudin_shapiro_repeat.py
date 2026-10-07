"""RSP preregistration driver: pinned external Walnut; artifacts stay outside Git.

No result is an independently verified theorem merely because Walnut returns TRUE.
The --research switch is required after the instrument controls pass.
"""
import argparse
from collections import deque
import hashlib
import json
import os
from pathlib import Path
import resource
import signal
import subprocess
import time


def read_machine(path):
    lines = [s.split('#')[0].strip() for s in path.read_text().splitlines()]
    lines = [s for s in lines if s]
    if lines[0].lower() in ('true', 'false'):
        return lines[0].lower() == 'true'
    tracks = len(lines.pop(0).split())
    outputs, transitions, state = {}, {}, None
    for line in lines:
        if '->' in line:
            left, right = line.split('->')
            symbol = tuple(map(int, left.split()))
            assert len(symbol) == tracks
            assert (state, symbol) not in transitions, 'nondeterministic export'
            transitions[state, symbol] = int(right)
        else:
            state, out = map(int, line.split())
            outputs[state] = out
    assert outputs and 0 in outputs
    assert all(target in outputs for target in transitions.values())
    return tracks, outputs, transitions


def evaluate(machine, values, padding=0):
    if isinstance(machine, bool):
        return machine
    tracks, outputs, transitions = machine
    assert len(values) == tracks
    width = max(1, max(values).bit_length()) + padding
    state = 0
    for bit in range(width - 1, -1, -1):
        symbol = tuple((v >> bit) & 1 for v in values)
        state = transitions.get((state, symbol))
        if state is None:
            return False
    return outputs[state]


def limits():
    resource.setrlimit(resource.RLIMIT_CPU, (120, 120))


def independent_bad_product(machine):
    """Intersect exported Rep with an independently derived MSD debt comparator.

    Running d=b-2a-q obeys d'=2d+b_bit-2a_bit-q_bit. Values
    <=-1 stay negative forever; values >=3 stay positive forever.
    Saturating at those endpoints therefore gives an exact five-state DFA.
    This verifies emptiness conditional on the exported Rep semantics.
    """
    tracks, outputs, transitions = machine
    assert tracks == 3
    start = (0, 0)
    reached, queue = {start}, deque([start])
    while queue:
        state, debt = queue.popleft()
        if outputs[state] and debt > 0:
            return False, len(reached)
        for a in (0, 1):
            for b in (0, 1):
                for q in (0, 1):
                    target = transitions.get((state, (a,b,q)))
                    if target is None:
                        continue  # a rejecting sink of Rep cannot accept a violation
                    d = max(-1, min(3, 2*debt+b-2*a-q))
                    pair = (target, d)
                    if pair not in reached:
                        reached.add(pair)
                        assert len(reached) <= 100000, 'preregistered state limit'
                        queue.append(pair)
    return True, len(reached)


def run_formula(java, walnut, outdir, name, command):
    session = outdir / name
    session.mkdir()
    script = session / 'commands.txt'
    script.write_text(command + '\nexit;\n')
    # Walnut 7.1 resolves its positional filename inside Command Files.
    command_file = walnut / 'Command Files' / (name + '.txt')
    command_file.parent.mkdir(exist_ok=True)
    command_file.write_bytes(script.read_bytes())
    log = session / 'console.txt'
    started = time.monotonic()
    peak_kib, stopped = 0, None
    with log.open('w') as stream:
        proc = subprocess.Popen(
            [str(java), '-Xmx768m', '-jar', str(walnut / 'build/libs/Walnut-all.jar'),
             '--home-dir=' + str(walnut), '--session-dir=' + str(session), command_file.name],
            cwd=walnut, stdout=stream, stderr=subprocess.STDOUT,
            start_new_session=True, preexec_fn=limits)
        while proc.poll() is None:
            sample = subprocess.run(['ps', '-o', 'rss=', '-p', str(proc.pid)],
                                    capture_output=True, text=True, check=False)
            if sample.stdout.strip():
                peak_kib = max(peak_kib, int(sample.stdout.strip()))
            if peak_kib > 1024 * 1024:
                stopped = 'RSS limit: 1 GiB'
            elif time.monotonic() - started > 180:
                stopped = 'additional wall limit: 180 seconds'
            if stopped:
                os.killpg(proc.pid, signal.SIGKILL)
                break
            time.sleep(.2)
        code = proc.wait()
    paths = list(session.rglob(name + '.txt'))
    paths = [p for p in paths if p.name != 'commands.txt']
    record = dict(name=name, returncode=code, stopped=stopped,
                  wall_seconds=round(time.monotonic()-started, 3), sampled_peak_rss_kib=peak_kib,
                  command=command)
    (session / 'run.json').write_text(json.dumps(record, indent=2) + '\n')
    print(json.dumps(record), flush=True)
    if code or stopped or not paths:
        raise RuntimeError('Formula incomplete; inspect its external console log')
    # The result library file has the same name as the definition.
    machine_path = next((p for p in paths if p.parent.name == 'Automata Library'), paths[0])
    machine = read_machine(machine_path)
    if not isinstance(machine, bool):
        record['states'] = len(machine[1])
    record['certificate_sha256'] = hashlib.sha256(machine_path.read_bytes()).hexdigest()
    (session / 'run.json').write_text(json.dumps(record, indent=2) + '\n')
    # Later formulas reference this definition in Walnut's home library.
    destination = walnut / 'Automata Library' / (name + '.txt')
    destination.parent.mkdir(exist_ok=True)
    destination.write_bytes(machine_path.read_bytes())
    return machine


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--java', type=Path)
    parser.add_argument('--walnut', type=Path)
    parser.add_argument('--out', type=Path)
    parser.add_argument('--verify-rep', type=Path,
                        help='Replay the exported relation/product check without Java')
    parser.add_argument('--research', action='store_true')
    args = parser.parse_args()
    if args.verify_rep:
        rep = read_machine(args.verify_rep)
        for a in range(16):
            for b in range(16):
                for q in range(16):
                    expected = q>=1 and b>=a and all(
                        ((s & (s>>1)).bit_count() ^
                         ((s+q) & ((s+q)>>1)).bit_count()) % 2 == 0
                        for s in range(a,b+1))
                    assert bool(evaluate(rep,(a,b,q))) == expected, (a,b,q)
                    assert bool(evaluate(rep,(a,b,q),3)) == expected
        empty, states = independent_bad_product(rep)
        print(json.dumps({'rep_sha256': hashlib.sha256(args.verify_rep.read_bytes()).hexdigest(),
                          'rep_states':len(rep[1]), 'product_states':states,
                          'safe_zero_conditional_on_rep_semantics':empty,
                          'literal_and_padding_controls':4096}))
        return
    if not all((args.java, args.walnut, args.out)):
        parser.error('--java, --walnut and --out are needed for formula runs')
    args.out.mkdir(parents=True, exist_ok=False)
    words = args.walnut / 'Word Automata Library'
    rs = read_machine(words / 'RS.txt')
    integers = list(range(4096)) + [2**k+d for k in range(1, 64) for d in (-1, 0, 1)]
    for n in integers:
        expected = (n & (n >> 1)).bit_count() % 2
        assert evaluate(rs, (n,)) == expected
        assert evaluate(rs, (n,), 3) == expected
    print('RSP0: independent RS generator and padding controls pass', flush=True)
    specifications = {
        'RSP_ZERO': 'msd_2\n0 0\n0 -> 0\n1 -> 0\n',
        'RSP_ALT': 'msd_2\n0 0\n0 -> 0\n1 -> 1\n1 1\n0 -> 0\n1 -> 1\n',
        'RSP_DYAD': 'msd_2\n0 0\n0 -> 0\n1 -> 1\n1 1\n0 -> 1\n1 -> 2\n2 0\n0 -> 2\n1 -> 2\n',
    }
    for name, text in specifications.items():
        (words / (name + '.txt')).write_text(text)
    rep = run_formula(args.java, args.walnut, args.out, 'rsp_rep',
        'def rsp_rep "?msd_2 q>=1 & b>=a & (As ((a<=s & s<=b) => RS[s]=RS[s+q]))":')
    count = 0
    for a in range(16):
        for b in range(a, 16):
            for q in range(1, 16):
                expected = all(((s & (s>>1)).bit_count() ^
                                ((s+q) & ((s+q)>>1)).bit_count()) % 2 == 0
                               for s in range(a, b+1))
                assert bool(evaluate(rep, (a,b,q))) == expected, (a,b,q)
                assert bool(evaluate(rep, (a,b,q), 3)) == expected
                count += 1
    print('RSP0: %d literal repeat and padding controls pass' % count, flush=True)
    for word, expected in [('RSP_ZERO', False), ('RSP_ALT', False), ('RSP_DYAD', True)]:
        name = word.lower() + '_control'
        repeat = f'q>=1 & b>=a & (As ((a<=s & s<=b) => {word}[s]={word}[s+q]))'
        formula = f'Aa,b,q (({repeat}) => b<=2*a+q)' if expected else (
            f'EC Aa,b,q (({repeat}) => b<=2*a+q+C)')
        result = run_formula(args.java, args.walnut, args.out, name,
                             f'eval {name} "?msd_2 {formula}":')
        assert isinstance(result, bool) and result == expected, (word,result)
    print('RSP0: negative, positive and unexpected padding controls pass', flush=True)
    if args.research:
        result = run_formula(args.java, args.walnut, args.out, 'rsp_safe_zero',
            'eval rsp_safe_zero "?msd_2 Aa,b,q ($rsp_rep(a,b,q) => b<=2*a+q)":')
        print('RSP1 raw decision:', result, '; independent certificate review pending', flush=True)
        print('Independent bad-product emptiness:', independent_bad_product(rep),
              '; conditional on exported Rep semantics', flush=True)


if __name__ == '__main__':
    main()
