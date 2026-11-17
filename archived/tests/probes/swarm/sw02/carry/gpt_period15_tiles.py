#!/usr/bin/env python3
"""GC2847: independent literal tile/seam check, never a profile-graph census."""
import ast
import hashlib
import itertools
import json
import os
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[5]
OUT = Path(os.environ['CAPPED_OUT'])
KIT = Path(os.environ['K09A_KIT_ROOT'])
PLAN = ROOT / 'tests/probes/swarm/sw02/carry/gpt_period15_tiles_plan.json'
for name, sha in json.loads(PLAN.read_text())['kit_sources_sha256'].items():
    assert hashlib.sha256((KIT/name).read_bytes()).hexdigest() == sha, name


def rotate(word, period, shift=1):
    shift %= period
    return ((word >> shift) | (word << (period-shift))) & ((1 << period)-1)


def check_seams(profiles, period):
    length = len(profiles[0])
    failures = []
    for a, b in itertools.product(range(len(profiles)), repeat=2):
        joined = profiles[a] + profiles[b]
        for r in range(length):
            x, y, z = joined[r:r+3]
            packed = rotate(x, period) ^ (x ^ (y | z))
            scalar = 0
            for t in range(period):
                left, center, right = [(v >> t) & 1 for v in (x, y, z)]
                expected = (30 >> (4*left+2*center+right)) & 1
                if ((x >> ((t+1) % period)) & 1) != expected:
                    scalar |= 1 << t
            assert scalar == packed, 'SCALAR_PACKED_DISAGREE'
            if scalar:
                failures.append([a, b, r, scalar])
    return failures


def decoder(words, maximum):
    for n in range(1, maximum+1):
        for positions in itertools.combinations(range(len(words[0])), n):
            labels = [''.join(w[i] for i in positions) for w in words]
            if len(set(labels)) == len(words):
                return {'positions': positions, 'labels': labels}
    raise AssertionError('NO_DECODER_IN_FIXED_BOUND')


def ordinary_step(row):
    n = len(row)
    return [(30 >> (4*row[(i-1) % n]+2*row[i]+row[(i+1) % n])) & 1
            for i in range(n)]


def ring_controls(profiles, period, longest):
    count = 0
    length = len(profiles[0])
    for ntiles in range(1, longest+1):
        for code in itertools.product(range(len(profiles)), repeat=ntiles):
            row = [profiles[k][r] & 1 for k in code for r in range(length)]
            physical = row[:]
            for t in range(period+1):
                moving = [physical[(i+t) % len(row)] for i in range(len(row))]
                literal = [(profiles[code[i//length]][i % length] >> (t % period)) & 1
                           for i in range(len(row))]
                assert moving == literal, ('ORDINARY_FRAME_OR_PROFILE', code, t)
                if 0 < t < period:
                    assert moving != row, ('SHORTER_MOVING_RETURN', code, t)
                physical = ordinary_step(physical)
            count += 1
    return count


text = (ROOT/'tests/probes/swarm/sw02/carry/cloud_period15_tiles.out').read_text()
arrays = [ast.literal_eval(m) for m in re.findall(r'^\s+choices [01]+ (\[.*\])$', text, re.M)]
words = re.findall(r'\btile:\s*([01]{31})', text)
assert len(arrays) == len(words) == 5
assert all(len(a) == 31 and all(0 <= x < 2**15 for x in a) for a in arrays)
assert [''.join(str(x & 1) for x in a) for a in arrays] == words, 'FRAMING_MISMATCH'
groups = {'binary': (arrays[:2], words[:2], 4), 'ternary': (arrays[2:], words[2:], 3)}
results = {}
for name, (profiles, initial, maxword) in groups.items():
    assert not check_seams(profiles, 15), name
    assert all(x[:2] == profiles[0][:2] for x in profiles)
    pair = profiles[0][:2]
    witnesses = {}
    for d in range(1, 15):
        choices = [(j,t) for j in range(2) for t in range(15)
                   if ((pair[j] >> ((t+d) % 15)) & 1) != ((pair[j] >> t) & 1)]
        assert choices, ('COMMON_PAIR_NOT_PRIMITIVE', name, d)
        witnesses[str(d)] = choices[0]
    dec = decoder(initial, len(profiles)-1)
    mutated = [x[:] for x in profiles]
    mutated[0][15] ^= 1
    mutation_failures = check_seams(mutated, 15)
    assert mutation_failures, 'MUTANT_ACCEPTED'
    results[name] = {'profiles': profiles, 'initial_words': initial, 'decoder': dec,
                     'common_pair': pair, 'primitive_witnesses': witnesses,
                     'local_equations': len(profiles)**2*31*15,
                     'ring_controls': ring_controls(profiles, 15, maxword),
                     'mutation_bad_site_phase_counts': sum(x[3].bit_count() for x in mutation_failures)}

# Exact existing kit certificate as a positive frame/orientation control.
kit_source = (KIT/'lean/Ruliology/CellularAutomata/Rule30MovingWaves.lean').read_text()
old = []
for name in ['zeroProfiles', 'oneProfiles']:
    body = kit_source.split('def '+name+' : List Nat :=', 1)[1]
    old.append(ast.literal_eval('['+body.split('[', 1)[1].split(']', 1)[0]+']'))
assert all(len(a) == 34 for a in old) and not check_seams(old, 12)
results['kit_control_equations'] = 1632

# Fixed unexpected tests, not an alphabet/census enlargement: test the literal
# five-tile union, and all fourteen nonzero phase shifts of one ternary tile.
mixed = check_seams(arrays, 15)
matrix = [[0]*5 for _ in range(5)]
for a,b,r,mask in mixed:
    matrix[a][b] += mask.bit_count()
phase = []
for d in range(1, 15):
    shifted = [a[:] for a in arrays[2:]]
    shifted[0] = [rotate(x, 15, d) for x in shifted[0]]
    bad = check_seams(shifted, 15)
    phase.append({'shift': d, 'bad_equations': sum(x[3].bit_count() for x in bad),
                  'all_seams_valid': not bad})
results['unexpected'] = {'five_tile_all_seams_valid': not mixed,
                         'mixed_seam_bad_equation_matrix': matrix,
                         'shift_one_ternary_tile': phase}
if not mixed:
    results['unexpected']['five_tile_decoder'] = decoder(words, 4)
(OUT/'period15-tiles.json').write_text(json.dumps(results, indent=2)+'\n')
print('PERIOD15_LITERAL_TILE_CHECKS_PASS')
for name in groups:
    x = results[name]
    print(name, 'equations', x['local_equations'], 'rings', x['ring_controls'],
          'decoder', x['decoder'], 'common_pair', x['common_pair'])
print('unexpected', json.dumps(results['unexpected']))
