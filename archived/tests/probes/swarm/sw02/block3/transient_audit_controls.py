"""Fixed CL757 detector/trap controls. Import only; the frozen parent stage calls run.

This is a same-GPT control, not a second-party carrying read. No new seeds,
window lift, support census, or horizon extension is part of this module.
"""
from __future__ import annotations

import importlib.util
from pathlib import Path
import json
import re


def _cloud_module():
    path = Path(__file__).with_name('cloud_transient_scan.py')
    spec = importlib.util.spec_from_file_location('cl757_fixed_audit_cloud', path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _step_int(row: int, tick: int) -> int:
    """Actual finite row at tick -> tick+1, center black iff tick is even."""
    return ((row << 1) | (1 - tick % 2)) ^ (row | (row >> 1))


def _window_step(word: int, left: int, outside: int) -> int:
    return (((word << 1) | left) ^
            (word | (word >> 1) | (outside << 15))) & 65535


def _window_step_cells(word: int, left: int, outside: int) -> int:
    cells = [(word >> j) & 1 for j in range(16)]
    out = []
    for j in range(16):
        a = left if j == 0 else cells[j - 1]
        c = outside if j == 15 else cells[j + 1]
        out.append(a ^ (cells[j] | c))
    return sum(bit << j for j, bit in enumerate(out))


def _template(gaps):
    bits = [0] * (sum(gaps) + 1)
    offset = 0
    bits[0] = 1
    for gap in gaps:
        offset += gap
        bits[offset] = 1
    return bits


def _matches(bits, template):
    return [s for s in range(len(bits) - len(template) + 1)
            if bits[s:s + len(template)] == template]


def _synthetics(cloud):
    import numpy as np
    E, A = [3, 3, 5, 3, 5, 5, 5, 5], [2, 5]
    result = []
    for n in (4, 5, 6):
        bits = _template(E + A * n + E)
        start2 = 34 + 7 * n
        assert len(bits) == 69 + 7 * n
        assert _matches(bits, _template(E)) == [0, start2]
        acc = {}
        cloud.analyse([0], np.array([bits], dtype=np.uint8), [1], acc)
        assert acc[1]['return_words'] == {str(n): 1}
        assert acc[1]['maxE'] == 2
        result.append({'kind': 'exact', 'n': n, 'samples': len(bits),
                       'E_start_samples': [0, start2],
                       'return_words': acc[1]['return_words']})
        mutant = bits.copy()
        mutant[35] ^= 1  # Interior of first A, outside both E blocks.
        acc_mut = {}
        cloud.analyse([0], np.array([mutant], dtype=np.uint8), [1], acc_mut)
        assert acc_mut[1]['maxE'] == 2
        assert acc_mut[1]['return_words'] == {'nonA' + str(start2): 1}
        result.append({'kind': 'interior_A_mutant', 'n': n, 'cell_sample': 35,
                       'return_words': acc_mut[1]['return_words']})
        clipped = bits[:-1]  # Remove terminal E's last black.
        acc_clip = {}
        cloud.analyse([0], np.array([clipped], dtype=np.uint8), [1], acc_clip)
        assert acc_clip[1]['maxE'] == 1
        assert acc_clip[1]['return_words'] == {}
        result.append({'kind': 'terminal_E_truncated', 'n': n,
                       'samples': len(clipped), 'maxE': acc_clip[1]['maxE']})
    return result


def _trap_audit(path: Path):
    source = path.read_text()
    match = re.search(r'def trapCodes : List Nat := \[(.*?)\]', source, re.S)
    assert match is not None
    codes = list(map(int, re.findall(r'\d+', match.group(1))))
    trap = set(codes)
    assert len(codes) == len(trap) == 829
    assert all(0 <= w < 65536 for w in trap)
    transitions = {}
    edge_rows = []
    for word in sorted(trap):
        edges = []
        for x1 in (0, 1):
            for x2 in (0, 1):
                nxt = _window_step(_window_step(word, 0, x1), 1, x2)
                scalar = _window_step_cells(
                    _window_step_cells(word, 0, x1), 1, x2)
                assert nxt == scalar
                assert nxt in trap
                edges.append((nxt, x1, x2))
                edge_rows.append([word, x1, x2, nxt])
        transitions[word] = edges
    template = _template([3, 3, 5, 3, 5, 5, 5, 5])
    current = {w for w in trap if (w & 1) == template[0]}
    layers = [sorted(current)]
    edge_counts = []
    predecessors = []
    for head in template[1:]:
        reached = {}
        count = 0
        for word in sorted(current):
            for nxt, x1, x2 in transitions[word]:
                if (nxt & 1) == head:
                    count += 1
                    reached.setdefault(nxt, (word, x1, x2))
        predecessors.append(reached)
        current = set(reached)
        layers.append(sorted(current))
        edge_counts.append(count)
    witness = None
    if current:
        terminal = min(current)
        words = [terminal]
        exteriors = []
        for pred in reversed(predecessors):
            old, x1, x2 = pred[words[-1]]
            words.append(old)
            exteriors.append([x1, x2])
        words.reverse()
        exteriors.reverse()
        assert [(w & 1) for w in words] == template
        witness = {'odd_windows': words, 'temporal_column17_pairs': exteriors}
    return trap, {
        'trap_size': len(trap), 'scalar_checked_edges': len(edge_rows),
        'closure': True, 'edges': edge_rows,
        'exterior_semantics': 'column17 at odd t and even t+1, independently chosen; overapproximation of actual histories',
        'E_template': template, 'E_layers': layers,
        'E_layer_edge_counts': edge_counts,
        'E_path_possible_in_temporal_boundary_graph': bool(current),
        'E_graph_witness': witness,
        'scope': 'Empty E path set excludes E after actual trap entry. A nonempty graph path alone is not a physical witness.'}


def _saved_totals(path: Path):
    data = json.loads(path.read_text())
    assert data['mode'] == 'random'
    assert data['args'] == ['30', '30', '20000', '8001', '2']
    a = data['acc']['30']
    perrow = {int(k): v for k, v in a['E_per_row'].items()}
    hist = {int(k): v for k, v in a['E_hist'].items()}
    total = sum(k * v for k, v in perrow.items())
    assert sum(perrow.values()) == a['rows'] == 20000
    assert sum(v for k, v in perrow.items() if k) == a['withE'] == 1531
    assert total == sum(hist.values()) == 1532
    assert sum(v for b, v in hist.items() if b < 2000) == 1529
    assert sum(v for b, v in hist.items() if 2000 <= b < 4000) == 3
    assert sum(v for b, v in hist.items() if b >= 4000) == 0
    assert sum(a['lock_hist'].values()) + a['unlocked'] == a['rows']
    assert sum(a['periods'].values()) + a['unlocked'] == a['rows']
    return {'rows': a['rows'], 'with_E': a['withE'], 'E_launches': total,
            'launches_before_2000': 1529, 'launches_2000_3999': 3,
            'launches_4000_to_last_observable': 0,
            'last_observable_E_launch_tick': 7933,
            'E_hist': hist, 'E_per_row': perrow,
            'lock_hist': a['lock_hist'], 'unlocked_by_suffix_detector': a['unlocked'],
            'latest_E_root': a['latestE_row'], 'late_suffix_root': a['lock_max_row'],
            'scope': 'Event counts, not conditional hazards; launches after7933 cannot be detected at horizon8001.'}


def _root_replay(cloud, root: int, trap):
    import numpy as np
    horizon = 8001
    row = root
    heads = []
    low16 = []
    first_entry = None
    for tick in range(1, horizon + 1):
        if tick % 2:
            heads.append(row & 1)
            low16.append(row & 65535)
            if first_entry is None and (row & 65535) in trap:
                first_entry = {'tick': tick, 'sample': (tick - 1) // 2,
                               'low16': row & 65535}
            if first_entry is not None:
                assert (row & 65535) in trap
        if tick < horizon:
            row = _step_int(row, tick)
    packed = cloud.evolve([root], horizon)[0].tolist()
    assert packed == heads
    E_template = _template([3, 3, 5, 3, 5, 5, 5, 5])
    starts = _matches(heads, E_template)
    cloud_starts = np.flatnonzero(cloud.match(
        np.array([heads], dtype=np.uint8), cloud.E_T)[0]).tolist()
    assert starts == cloud_starts
    s0s, ps = cloud.lock_times(np.array([heads], dtype=np.uint8))
    s0, period = int(s0s[0]), int(ps[0])
    independent_candidates = []
    for p in (2, 5, 7):
        mismatches = [j for j in range(len(heads) - p)
                      if heads[j] != heads[j + p]]
        start = 1 + max(mismatches, default=-1)
        if len(heads) - start >= 10 * p:
            independent_candidates.append((start, p))
    expected = min(independent_candidates, default=(-1, 0))
    assert (s0, period) == expected
    events = []
    for s in starts:
        events.append({'start_tick': 2 * s + 1, 'end_tick': 2 * (s + 34) + 1,
                       'start_low16': low16[s], 'end_low16': low16[s + 34],
                       'start_in_trap': low16[s] in trap,
                       'end_in_trap': low16[s + 34] in trap,
                       'starts_after_entry': first_entry is not None and s >= first_entry['sample']})
    return {'root_at_tick1': root, 'horizon': horizon,
            'independent_int_vs_cloud_all_odd_heads': True,
            'first_trap_entry': first_entry, 'odd_low16': low16,
            'E_events': events,
            'observed_suffix': {'start_sample': s0, 'period_samples': period,
                                'start_tick': 2 * s0 + 1 if s0 >= 0 else None,
                                'permanent_lock_claim': False},
            'final_width': row.bit_length()}


def run(cloud_json_path, trap_lean_path) -> dict:
    cloud = _cloud_module()
    totals = _saved_totals(Path(cloud_json_path))
    assert totals['latest_E_root'] == 1045436333
    assert totals['late_suffix_root'] == 637749532
    synthetics = _synthetics(cloud)
    trap, trap_result = _trap_audit(Path(trap_lean_path))
    empty = 0
    for tick in range(293):
        empty = _step_int(empty, tick)
    assert empty & 65535 == 49415
    assert empty & 65535 in trap
    controls = [_root_replay(cloud, root, trap)
                for root in (1045436333, 637749532)]
    assert max(e['start_tick'] for e in controls[0]['E_events']) == 2693
    assert controls[1]['observed_suffix']['start_sample'] == 3951
    return {'saved_aggregate_audit': totals, 'synthetic_return_controls': synthetics,
            'trap_graph': trap_result,
            'empty_even0_to_293_control': {'low16': empty & 65535, 'in_trap': True},
            'retained_root_replays': controls,
            'new_rows_or_horizon': False, 'status': 'ALL_FIXED_CONTROLS_PASS'}
