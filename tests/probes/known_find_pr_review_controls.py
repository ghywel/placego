"""GC2129 adversarial PR-index review controls; offline, isolated temporary cache, no git/network execution.
The initial L1149 implementation is predicted to fail four safety properties. Keep those failures; this is
an independent review harness, not a live-index or mathematical certificate. Run with Python unittest.
"""
import io
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch
import urllib.request
import urllib.parse

import known_find as k


class PRIndexReview(unittest.TestCase):
    def fixture(self, root, mode):
        cache = Path(root)
        old = {'number': 55, 'head': 'oldhead', 'comments': [], 'title': 'old', 'body': '',
               'author': 'public-author', 'url': 'https://example.invalid/pr/55', 'updated': ''}
        index = cache / 'prs.json'
        index.write_text(json.dumps({'prs': [old]}))
        previous = index.read_bytes()
        source = cache / 'pr-src' / '55-oldhead'
        source.mkdir(parents=True)
        (source / 'DONE').write_text('oldhead')
        (source / 'FILES.json').write_text(json.dumps({'files': ['Old.lean'], 'lean': ['Old.lean']}))
        (source / 'Old.lean').write_text('theorem prior_fact : True := trivial\n')
        pull = {'number': 55, 'head': {'sha': 'newhead'}, 'title': 'new', 'body': '',
                'user': {'login': 'public-author'}, 'html_url': old['url'], 'updated_at': ''}
        def api(path):
            return [pull] if '/pulls?' in path else []
        def git(*args, **kwargs):
            if args[0] == 'fetch':
                return subprocess.CompletedProcess(args, 1 if mode == 'head_fail' else 0, '', 'injected fetch failure')
            if args[0] == 'rev-parse':
                return subprocess.CompletedProcess(args, 0, 'newhead\n', '')
            if args[0] == 'diff':
                return subprocess.CompletedProcess(args, 1 if mode == 'diff_fail' else 0,
                                                   '' if mode == 'diff_fail' else 'Missing.lean\n',
                                                   'injected diff failure')
            raise AssertionError(args)
        return index, previous, source, api, git

    def fetch_fixture(self, root, mode):
        index, previous, source, api, git = self.fixture(root, mode)
        with patch.object(k, 'CACHE', root), patch.object(k, 'PRS', str(index)), \
             patch.object(k, 'PR_SRC', str(Path(root) / 'pr-src')), patch.object(k, 'KIT_DIR', root), \
             patch.object(k, 'api_list', side_effect=api), patch.object(k, 'git', side_effect=git), \
             patch.object(k.shutil, 'which', return_value=None), \
             patch.object(k.subprocess, 'run', return_value=subprocess.CompletedProcess([], 1, b'', b'injected missing blob')):
            errors = k.fetch_prs()
        return errors, index, previous, source

    def test_head_fetch_failure_preserves_previous_index_and_sources(self):
        with tempfile.TemporaryDirectory() as root:
            errors, index, previous, source = self.fetch_fixture(root, 'head_fail')
            self.assertTrue(errors)
            self.assertEqual(index.read_bytes(), previous)
            self.assertTrue((source / 'Old.lean').exists())

    def test_failed_blob_is_not_marked_complete(self):
        with tempfile.TemporaryDirectory() as root:
            errors, index, previous, source = self.fetch_fixture(root, 'blob_fail')
            self.assertTrue(errors, 'an unreadable listed Lean blob must make coverage incomplete')
            self.assertFalse((Path(root) / 'pr-src' / '55-newhead' / 'DONE').exists())
            self.assertEqual(index.read_bytes(), previous)

    def test_failed_rest_diff_is_not_marked_complete(self):
        with tempfile.TemporaryDirectory() as root:
            errors, index, previous, source = self.fetch_fixture(root, 'diff_fail')
            self.assertTrue(errors, 'a failing git diff is not an empty complete file list')
            self.assertFalse((Path(root) / 'pr-src' / '55-newhead' / 'DONE').exists())
            self.assertEqual(index.read_bytes(), previous)

    def test_two_same_minute_comments_are_distinct_daily_units(self):
        name = '#51 comment public-author 2026-10-29T04:35'
        units = [('open PR comment', name, 'https://example.invalid/#comment-1', 'first proof'),
                 ('open PR comment', name, 'https://example.invalid/#comment-2', 'second proof')]
        snap = k.snapshot_units(units)
        self.assertEqual(len(snap), 2, 'distinct public comments must not overwrite one another')
        changed = list(units)
        changed[0] = changed[0][:3] + ('first proof corrected',)
        self.assertEqual(len(k.snapshot_changes(k.fingerprints(snap),
                                              k.fingerprints(k.snapshot_units(changed)))[1]), 1)

    def test_rest_api_pagination_reads_second_page(self):
        calls = []
        def get(req, timeout):
            url = req.full_url
            calls.append(url)
            first = urllib.parse.parse_qs(urllib.parse.urlsplit(url).query)['page'] == ['1']
            page = [{'number': i} for i in range(100)] if first else [{'number': 100}]
            return io.BytesIO(json.dumps(page).encode())
        with patch.object(k.shutil, 'which', return_value=None), patch.object(urllib.request, 'urlopen', side_effect=get):
            result = k.api_list('repos/example/project/pulls?state=open&per_page=100')
        self.assertEqual(len(result), 101)
        self.assertEqual(len(calls), 2)
        self.assertTrue(calls[-1].endswith('page=2'))


if __name__ == '__main__':
    unittest.main()
