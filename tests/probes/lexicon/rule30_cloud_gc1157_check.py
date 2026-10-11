#!/usr/bin/env python3
"""rule30_cloud_gc1157_check.py: Cloud's targeted (tier 2) check of GPT's GC1157 carrying step: the white-ending
extension q+1 of the sharp depth-132 record word q (Local's d = 132, L = 17, phase 0 block in
rule30_local_record_traces.txt; q+1 sets the sample q74 = c[148] to 1, which would make depth 149 white) contains the
certified phase-0 minimal forbidden word 100100001001000010000101 at visible index 51 (tick 102, a white wall), so
no real trace realises q with a white ending and depth 149 is black for the whole root class (CL359).

RUN-ON:     cpu (Python 3 standard library; a second)
COMMAND:    python3 tests/probes/lexicon/rule30_cloud_gc1157_check.py

WHAT. q (74 visible samples, ticks 0..146) is read from Local's block, q+0 and q+1 append the sample at tick 148. The
cut is looked up in rule30_local_mfw44.txt (both phase sections). Every certified phase-0 word is searched in q, q+0
and q+1. The cut's last letter is q74 itself, so a hit at index 51 of q+1 and no hit in q+0 is exactly GPT's claim.

PREDICTIONS (CL359; this check was first run inline and is filed here unchanged). P1: q+1[51:75] is the cut and the
cut is certified in phase 0 (0.8). P2: q and q+0 contain no certified phase-0 word (0.9, the word is real). P3: the
cut is the only certified phase-0 word in q+1 (0.6). Counterfactual: a cut in q or q+0 would mean the certified list or
Local's block is wrong; no cut in q+1 would leave GC1156's physical cylinder as the only argument. Unexpected check:
whether the cut is certified in phase 1 as well (then the rebase phase does not even matter).
Record searched: 100100001001000010000101 (3 files: Local's list, Intel's forced-only list, Cloud's channel counts).
"""
lines=open('tests/probes/lexicon/rule30_local_record_traces.txt').read().split('\n')
i=[k for k,l in enumerate(lines) if l.startswith('d=132 L=17 phase=0 T=148 status=exact')][0]
blk={l.split('=')[0]:l.split('=')[1] for l in lines[i+1:i+5]}
q=blk['visible']; cut='100100001001000010000101'; q1=q+'1'; q0=q+'0'
assert len(q)==74
txt=open('tests/probes/lexicon/rule30_local_mfw44.txt').read().split('\n')
phase=None; words={0:[],1:[]}
for l in txt:
    if l.startswith('## phase'): phase=int(l.split(':')[0].split()[-1]); continue
    w=l.strip().split()[0] if l.strip() else ''
    if w and set(w)<={'0','1'} and phase is not None: words[phase].append(w)
print('certified words: phase 0',len(words[0]),'| phase 1',len(words[1]))
print('(P1) q+1[51:75] =',q1[51:75],'| is the cut:',q1[51:75]==cut,'| visible index 51 = tick 102, white wall:',
      102%2==0,'| cut certified in phase 0:',cut in words[0],'| in phase 1 (unexpected check):',cut in words[1])
for name,s in (('q',q),('q+0',q0),('q+1',q1)):
    hits=[(w,s.find(w)) for w in words[0] if w in s]
    print('  %-3s | certified phase-0 words occurring: %d %s'%(name,len(hits),hits[:3]))
print('(P2) q and q+0 clean:',not any(w in q0 for w in words[0]),'| (P3) q+1 has the cut only:',
      [w for w in words[0] if w in q1]==[cut],'| the cut ends with q74 = 1; with q74 = 0 the window',q0[51:75],
      'is certified:',q0[51:75] in words[0])
