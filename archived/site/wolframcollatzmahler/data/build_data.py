#!/usr/bin/env python3
"""build_data.py: clean exports for the trove, built from the record's files (run from anywhere; writes beside itself).
  records.csv / records.json  the record R(d) at every depth the census holds: depth, phase, L, status (exact or >=),
                              horizon T, and the witness's visible word; from rule30_local_record_traces.txt
  forbidden_words.json        the certified minimal forbidden visible words to 44, by phase and length; from rule30_local_mfw44.txt
  rings.json                  the S and L rings (cells, shift, column-1 word, white gap) as constants of the record
  replay.py (beside this)     re-derives every record row from its witness block and checks the band, in seconds
"""
import csv, json, os, hashlib
HERE=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.abspath(os.path.join(HERE,'..','..','..'))
L=os.path.join(ROOT,'tests','probes','lexicon')
def sha(p):
    h=hashlib.sha256(); h.update(open(p,'rb').read()); return h.hexdigest()
# records
src=os.path.join(L,'rule30_local_record_traces.txt'); lines=open(src).read().split('\n'); rows=[]; i=0
while i<len(lines):
    l=lines[i]
    if l.startswith('d='):
        kv=dict(x.split('=',1) for x in l.split()); blk={}
        for j in range(1,5):
            k,v=lines[i+j].split('=',1); blk[k]=v
        rows.append(dict(depth=int(kv['d']),L=int(kv['L']),phase=int(kv['phase']),T=int(kv['T']),status='exact' if kv['status']=='exact' else '>=',
                         visible=blk['visible'],trace=blk['trace'],right=blk['right'],left=blk['left'])); i+=5
    else: i+=1
# one row per (depth, phase): keep the exact one, else the largest L
best={}
for r in rows:
    k=(r['depth'],r['phase'])
    if k not in best or (r['status']=='exact' and best[k]['status']!='exact') or (r['status']==best[k]['status'] and r['L']>best[k]['L']): best[k]=r
recs=[best[k] for k in sorted(best)]
with open(os.path.join(HERE,'records.csv'),'w',newline='') as f:
    w=csv.writer(f); w.writerow(['depth','phase','L','status','T','visible_word'])
    for r in recs: w.writerow([r['depth'],r['phase'],r['L'],r['status'],r['T'],r['visible']])
json.dump({'what':'The record R(d): the longest white run of the forced left row at time 0 starting at depth d, over real traces beside '
                  'the alternating wall; status exact means proved maximal by SAT with a certificate, >= means a witness only.',
           'source':'tests/probes/lexicon/rule30_local_record_traces.txt (Local, L643); sha256 '+sha(src),
           'fields':'depth, phase (0: wall = t mod 2), L, status, T (= depth + L - 1), visible word (column 1 at the white ticks), '
                    'trace (column 1, ticks 0..T), left (the forced left row at time 0, depths 1..T), right (the right half at time 0)',
           'rows':recs},open(os.path.join(HERE,'records.json'),'w'),indent=0)
# forbidden words
src2=os.path.join(L,'rule30_local_mfw44.txt'); ph=None; words={0:[],1:[]}
for l in open(src2).read().split('\n'):
    if l.startswith('## phase'): ph=int(l.split(':')[0].split()[-1]); continue
    w=l.strip().split()[0] if l.strip() else ''
    if w and set(w)<={'0','1'} and ph is not None: words[ph].append(w)
json.dump({'what':'Every minimal forbidden visible word of length <= 44 beside the alternating wall, by phase: a word column 1 '
                  '(read at the white-wall ticks) can never produce, both of whose (n-1)-factors occur; each certified absent by a '
                  'cake_lpr-checked SAT certificate (Local, L640/L641).',
           'source':'tests/probes/lexicon/rule30_local_mfw44.txt; sha256 '+sha(src2),
           'phase0':sorted(words[0],key=lambda w:(len(w),w)),'phase1':sorted(words[1],key=lambda w:(len(w),w))},
          open(os.path.join(HERE,'forbidden_words.json'),'w'),indent=0)
json.dump({'what':'The two travelling waves column 1 can run in beside the alternating wall (RULE30-PRIZE.md 8.4, CHAT-LEDGER.md GC686, GC1151, CL351, L642).',
  'S':{'cells':84,'ring_hex':'0x688eb74a45efb082671ee','bit_i_is_site_i':True,'one_step_is_shift_by':14,'column0_word':'010101',
       'column1_word':'110100','largest_cyclic_white_gap':5},
  'L':{'cells':155,'ring_hex':'0x35409b1caa645d715104db5291a2fe8415260ce','bit_i_is_site_i':True,'two_steps_are_shift_by':31,
       'column0_word':'0101','column1_word':'1101000100','largest_cyclic_white_gap':6,'note':'gap 7 at black-wall rows (L642)'},
  'wheel':{'word_U':'00010011010001001101000100110100010011010001001101001101','period':56,'rotation':'t -> 17 t mod 56','kick_classes':[12,32,42,'...see PROOFS.md entry 26']}},
  open(os.path.join(HERE,'rings.json'),'w'),indent=1)
print('records',len(recs),'| exact',sum(r['status']=='exact' for r in recs),'| words',len(words[0]),len(words[1]))
# embed the records in record.html so the page works when opened from the file system
import re
rp=os.path.join(HERE,'..','record.html'); t=open(rp).read()
payload=json.dumps(json.load(open(os.path.join(HERE,'records.json'))),separators=(',',':')).replace('</','<\\/')
t=re.sub(r'<!-- RECORDS-JSON -->.*?<!-- /RECORDS-JSON -->',lambda m:'<!-- RECORDS-JSON -->'+payload+'<!-- /RECORDS-JSON -->',t,flags=re.S)
open(rp,'w').write(t); print('embedded in record.html')
