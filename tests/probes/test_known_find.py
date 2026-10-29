"""Offline controls for the prior-art safeguard; no network and no user cache writes."""
import contextlib
import io
import json
from pathlib import Path
import re
import tempfile
import unittest
from unittest.mock import patch

import known_find as k


class KnownFindTest(unittest.TestCase):
    def test_multiline_statement_search(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / 'X.lean'
            p.write_text('theorem existing_name (t : Nat) :\n    hidden_conclusion t := by\n  exact proof\n')
            units = k.lean_units('lean/X.lean', str(p), 'commit')
            hits = k.search([re.compile('hidden_conclusion')], units)
            self.assertTrue(any(u[0] == 'kit source' for u in hits))

    def test_existing_module_addition_and_edit_detected(self):
        def snapshot(text, url='commit1'):
            return k.fingerprints(k.snapshot_units([('kit source', 'X', url, text)]))
        old = snapshot('theorem a : P := proof')
        self.assertEqual(k.snapshot_changes(old, snapshot('theorem a : P := proof', 'commit2')), ([], [], []))
        for new in ['theorem a : Q := proof', 'theorem a : P := proof\ntheorem b : Q := proof']:
            self.assertEqual(k.snapshot_changes(old, snapshot(new)), ([], ['kit source|X'], []))

    def test_portal_metadata_change(self):
        old = k.fingerprints(k.snapshot_units([('portal', 'id', 'url', 'pending')]))
        new = k.fingerprints(k.snapshot_units([('portal', 'id', 'url', 'verified')]))
        self.assertEqual(k.snapshot_changes(old, new), ([], ['portal|id'], []))

    def test_failed_refresh_preserves_checkpoint(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / 'checked.json'
            p.write_text('{"sentinel": true}')
            with patch.object(k, 'CHECKED', str(p)), patch.object(k, 'refresh', return_value=('REFRESH FAILED', True)), contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(k.new_since_last(), 1)
            self.assertEqual(json.loads(p.read_text()), {'sentinel': True})

    def test_old_checkpoint_migration_then_source_change(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / 'checked.json'
            p.write_text('{"keys": ["kit module|X"]}')
            units = [('kit source', 'X', 'url', 'first')]
            out = io.StringIO()
            with patch.object(k, 'CHECKED', str(p)), patch.object(k, 'refresh', return_value=('fresh', True)), patch.object(k, 'stamp', return_value={}), patch.object(k, 'all_units', return_value=units), contextlib.redirect_stdout(out):
                self.assertEqual(k.new_since_last(), 0)
                units[0] = ('kit source', 'X', 'url', 'second')
                self.assertEqual(k.new_since_last(), 0)
            self.assertIn('earlier changes cannot be inferred', out.getvalue())
            self.assertIn('0 added, 1 changed', out.getvalue())


if __name__ == '__main__':
    unittest.main()
