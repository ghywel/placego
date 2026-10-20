#!/usr/bin/env python3
"""build_manifest.py: generate data/manifest.json, the catalogue behind trove.html, from the curated list below.
Run from anywhere: python3 site/wolframcollatzmahler/build_manifest.py . Each item: path (repository-relative), kind, title, what,
schema, source, replay (optional). Size and SHA-256 are computed from the file. Links point at the public repository.
"""
import hashlib, json, os, sys, time
ROOT=os.path.abspath(os.path.join(os.path.dirname(__file__),'..','..'))
REPO='https://github.com/ghywel/placego'; RAW='https://raw.githubusercontent.com/ghywel/placego/main/'
L='tests/probes/lexicon/'
ITEMS=[
 dict(path='site/wolframcollatzmahler/data/records.csv',kind='records',title='The record R(d), clean table (CSV)',
  what='One row per depth and phase, 20..160: the longest white run of the forced left row starting at that depth, whether the '
       'value is exact (proved maximal by SAT with a certificate) or a lower bound, the horizon, and the witness\'s visible word.',
  schema='depth, phase, L, status (exact or >=), T, visible_word.',source='build_data.py from rule30_local_record_traces.txt (L643).',
  replay='python3 site/wolframcollatzmahler/data/replay.py'),
 dict(path='site/wolframcollatzmahler/data/records.json',kind='records',title='The record R(d), with every witness (JSON)',
  what='The same rows with the full witness: the column-1 trace, the forced left row at time 0 and the right half at time 0, so '
       'that every value can be re-derived with a plain Rule 30 loop.',
  schema='JSON: what, source, fields, rows[{depth, phase, L, status, T, visible, trace, left, right}].',
  source='build_data.py (Cloud) from Local\'s record traces.',replay='python3 site/wolframcollatzmahler/data/replay.py'),
 dict(path='site/wolframcollatzmahler/data/forbidden_words.json',kind='forbidden words',title='Certified minimal forbidden visible words (JSON)',
  what='The 1,130 phase-0 and 1,199 phase-1 minimal forbidden words to length 44 as two sorted lists, with the source file\'s digest.',
  schema='JSON: what, source, phase0[], phase1[].',source='build_data.py from rule30_local_mfw44.txt (L640, L641).'),
 dict(path='site/wolframcollatzmahler/data/rings.json',kind='census',title='The S and L rings and the wheel word (JSON)',
  what='The constants of the two travelling waves column 1 can run in, and the unkicked wheel word U with its rotation.',
  schema='JSON: S{cells, ring_hex, shift, words, gap}, L{...}, wheel{word_U, period, rotation, kick_classes}.',
  source='RULE30-PRIZE.md 8.4; CHAT-LEDGER.md GC686, GC1151, CL351, L642; PROOFS.md entry 26.'),
 dict(path='site/wolframcollatzmahler/data/replay.py',kind='probes',title='replay.py: re-check every record row in seconds',
  what='A plain Rule 30 loop and left permutivity, nothing else: replays the right half to the trace, the trace to the left row, '
       'checks the white band and the visible word for every row of records.json.',
  schema='Python 3, standard library.',source='Cloud, 2026-10-11.',replay='python3 site/wolframcollatzmahler/data/replay.py'),
 dict(path=L+'rule30_local_record_traces.txt',kind='records',title='Record witnesses and their traces, depths 20 to 160',
  what='The best known white-run record at every depth 20..160 of the forced left side beside the alternating wall: 141 '
       'blocks, 104 at the exact value (every depth 20..120 and 132, 139, 142). Each block gives the depth, the run L, the '
       'phase, the horizon T, then the column-1 trace, the visible word, the forced left row at time 0 and the right half.',
  schema='Blocks "d=<depth> L=<run> phase=<0|1> T=<horizon> status=<exact|>=>" then four lines trace=, visible=, left=, right= '
         'as 0/1 strings; comment lines start with #.',
  source='rule30_local_record_traces.py (Local), from the RLK/CUT SAT runs; replays both ways with its check mode.',
  replay='python3 tests/probes/lexicon/rule30_local_record_traces.py check'),
 dict(path=L+'rule30_local_witnesses.txt',kind='records',title='Sampled witnesses for lower bounds on the record (Local)',
  what='Right halves at time 0 that, with the forced left half, keep the alternating wall and show a white run of length L at '
       'depth d; lower bounds R_real(d) >= L at deep depths found by random sampling.',
  schema='Blocks "d=<depth> phase=<0|1> L=<run> T=<horizon> cells=<n> verified=yes" then the right half over sites 1..n as 0/1, '
         'wrapped at 100 characters.',
  source='rule30_rreal_sample.c and rule30_witness_check.py (Local).',
  replay='python3 tests/probes/lexicon/rule30_witness_check.py D L PHASE LEFT RIGHT   (see the file header)'),
 dict(path=L+'rule30_intel_witnesses.txt',kind='records',title='Sampled witnesses for lower bounds on the record (Intel)',
  what='The same kind of witnesses as Local\'s file, found independently on a second machine.',
  schema='As rule30_local_witnesses.txt.',source='Intel\'s copy of the sampling probe (2026-10-11).'),
 dict(path=L+'rule30_local_mfw44.txt',kind='forbidden words',title='Certified minimal forbidden visible words to length 44, both phases',
  what='Every word of length up to 44 that column 1, read at the white-wall ticks, can never produce beside the alternating '
       'wall, and that is minimal (both shorter factors occur): 1,130 words in phase 0 and 1,199 in phase 1, each proved '
       'absent by a SAT certificate checked by cake_lpr.',
  schema='Sections "## phase 0" and "## phase 1", one word per line; a header explains the phase convention.',
  source='rule30_sofic_test.py (the exact language by cone SAT) and rule30_mfw_certify.py (certificates), Local.',
  replay='python3 tests/probes/lexicon/rule30_mfw_certify.py   (certificate replay; see its header)'),
 dict(path=L+'rule30_records_local.txt',kind='records',title='Record table with histograms and witness words (Local)',
  what='For each depth, the record white run, the histogram of runs over all seeds, and the witness words.',
  schema='Lines "R d L count", "H d L n" (histogram) and "W d <word>".',source='Local\'s record runs (RRL).'),
 dict(path=L+'rule30_records_cloud.txt',kind='records',title='Independent replay of the records (Cloud)',
  what='Cloud\'s independent replay of the record values and the clock cores, as a check on Local\'s table.',
  schema='Lines "R d L count ; W <words>".',source='Cloud\'s RRX replay.'),
 dict(path=L+'rule30_records_word.txt',kind='records',title='Records by centre word',
  what='Record white runs when the centre is held to words other than 0101, with how many prefixes reach them.',
  schema='Lines "R <word> d = L (k of N prefixes reach it); cap C" and "H <word> d : run:count ...".',source='rule30_records.py'),
 dict(path=L+'rule30_ring_census.txt',kind='census',title='The ring census: Rule 30 on rings of every small size',
  what='For each ring size, the number of cycles, periodic states, the largest period, the longest transient and gliding '
       'cycles (travelling waves). The S ring (84 cells) and L ring (155 cells) are the waves column 1 can run in.',
  schema='Lines "n <size> cycles <c> periodic <p> maxper <m> single <s> maxtransient <t> gliding <g>" with a lengths line.',
  source='rule30_rings.py (Cloud).'),
 dict(path=L+'rule30_ladder_local.txt',kind='census',title='The deep ladder',
  what='How many right halves keep the alternating wall for s steps at each width: the ladder R(m, s) that bounds how far '
       'from the centre a counterexample must sit.',schema='Lines "H w s k count".',source='the ladder probes (Local).'),
 dict(path=L+'rule30_leftside_horizon.txt',kind='census',title='Left-side horizons',
  what='For each seed width and seed, how far the left side keeps the clock.',schema='Lines "H w k = h  phase p  seed x".',
  source='rule30_leftside_horizon.py'),
 dict(path=L+'rule30_mixed_generator_words.txt',kind='forbidden words',title='Visible words of the collar\'s macro generators',
  what='The column-1 words of the typed macro chains beside the wall (S, L blocks), the objects the cut automaton reads.',
  schema='Blocks "name k-word ticks n" then n visible bits.',source='CL297 (Cloud).'),
 dict(path=L+'rule30_intel_minimal_absent_traces.txt',kind='forbidden words',title='Minimal absent traces (Intel, strip form)',
  what='Minimal absent words of the strip relaxation of the visible language, the finite-width face of the exact language.',
  schema='See the file header.',source='Intel\'s strip probes (RULE30-PRIZE.md 8.83).'),
 dict(path=L+'rule30_intel_forced_only.txt',kind='forbidden words',title='Forced-only words (Intel)',what='Words of the forced-only relaxation.',
  schema='See the file header.',source='Intel\'s strip probes.'),
 dict(path=L+'rule30_cloud_channel_truecount_F.txt',kind='counts',title='Channel bound counts',
  what='The exact counts behind the channel bound: how many column-1 words of each length occur beside the wall, in integer '
       'arithmetic.',schema='See the file header.',source='the channel-bound probes (Cloud; RULE30-PRIZE.md 8.20, 8.33).'),
 dict(path='tests/probes/mahler/mahler_contrib_checks.py',kind='outside contribution',
  title='Joshua Coon\'s Lean 4 library on Mahler\'s 3/2 problem: our independent checks',
  what='The first outside contribution: Joshua Coon, with the Astra and Argon AI models in GitHub Copilot, '
       'github.com/jjc16/mahler-3-2-lean4 (142 Lean 4 files on Mathlib; checked at f6d9492 and 04ed5389: all compiled, no sorry, '
       'standard axioms only). This file recomputes its concrete claims from the statements alone: survival horizons, the bound '
       'B(29) >= 4096, the first-defect valuation lock, and the escape deadlines of five windows and unions wider than 1/3.',
  schema='Python 3, standard library; predictions and outcome in the header.',
  source='Cloud, 2026-10-19 (CL463, CL464; MAHLER.md section 4). The library and its paper belong to their author.',
  replay='python3 tests/probes/mahler/mahler_contrib_checks.py 10'),
 dict(path='STATE-OF-THE-PROOF.md',kind='document',title='The state of the proof',what='Where the three prize problems stand, every claim pointing to its section.'),
 dict(path='PERIOD-TWO.md',kind='document',title='Period two: the open case in full',what='Every exact form of the problem, the closed routes, the status board.'),
 dict(path='RULE30-PRIZE.md',kind='document',title='The research record',what='The day-by-day record with its honest summary; section 8 is the work.'),
 dict(path='RECORD-MAP.md',kind='document',title='The record map',what='An index of the record by topic.'),
 dict(path='COLLATZ-PRIZE.md',kind='document',title='Collatz: the prize and the Rule 30 method',what='The Collatz twin: counting form, least-residue lemma, window principle.'),
 dict(path='PRIOR-ART.md',kind='document',title='Prior art',what='The literature found, with what each result does and does not cover.'),
 dict(path='PROOFS.md',kind='proofs',title='Proofs',what='Every statement with a written proof and a second reader, in one file; the proofs directory holds them one per file.'),
 dict(path='tests/probes/PROBES.md',kind='probes',title='The probe index',what='One line per experiment: what it tested, its predictions and its outcome; the scripts are beside it.'),
 dict(path='WORKING-TOGETHER.md',kind='document',title='How we worked together',what='The lanes, the git protocol and the review rules.'),
 dict(path='WORKFLOW-SAVED-MEMORY.md',kind='document',title='The working rules',what='Predictions first, failures retained, two-tier review, and the other standing rules.'),
]
def sha(p):
    h=hashlib.sha256()
    with open(p,'rb') as f:
        for b in iter(lambda:f.read(1<<20),b''): h.update(b)
    return h.hexdigest()
out=[]
for it in ITEMS:
    p=os.path.join(ROOT,it['path'])
    if not os.path.exists(p): print('missing:',it['path'],file=sys.stderr); continue
    it=dict(it); it['bytes']=os.path.getsize(p); it['sha256']=sha(p)
    it['view']=REPO+'/blob/main/'+it['path']; it['raw']=RAW+it['path']; out.append(it)
dest=os.path.join(os.path.dirname(__file__),'data','manifest.json')
json.dump({'generated':time.strftime('%Y-%m-%d %H:%M UTC',time.gmtime()),'repository':REPO,'items':out},open(dest,'w'),indent=1)
print('wrote',dest,'with',len(out),'items')
# embed the catalogue in trove.html so the page works when opened from the file system (fetch is blocked there)
import re
tp=os.path.join(os.path.dirname(__file__),'trove.html'); t=open(tp).read()
payload=json.dumps({'items':out},separators=(',',':')).replace('</','<\\/')
t=re.sub(r'<!-- MANIFEST-JSON -->.*?<!-- /MANIFEST-JSON -->',lambda m:'<!-- MANIFEST-JSON -->'+payload+'<!-- /MANIFEST-JSON -->',t,flags=re.S)
open(tp,'w').write(t); print('embedded in trove.html')
