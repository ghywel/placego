#!/usr/bin/env python3
"""G23, preregistered in RULE30-GPT.md before execution.
SH1: some sampled set is not a cylinder; SH2: some is not affine.
CF: all sampled sets are cylinders. Seed2306, width10, twelve states.
Independent scalar BFS vs untouched entropy2.c via temporary include wrapper.
Controls: full cube/singleton/cylinder/parity/random; unexpected bit reversal.
OUTCOME:155 states/225 live edges independently agree; SH1/SH2 hold, CF fails.
No noninitial cylinders, one affine state. Record rejected at visible index6.
SVG generated; optional PNG unavailable without matplotlib.
Outputs and membership contact sheet stay outside git.
"""
import argparse, json, random, subprocess, tempfile
from pathlib import Path

M = 10
ROOT = Path(__file__).resolve().parents[3]

def step(s, wall, outer):
    cells = [wall] + [(s >> j) & 1 for j in range(M)] + [outer]
    return sum(((30 >> (4*cells[j]+2*cells[j+1]+cells[j+2])) & 1) << j for j in range(M))

def successor(s, bit):
    mid = {step(x, 0, u) for x in s if x & 1 == bit for u in (0, 1)}
    return frozenset(step(x, 1, u) for x in mid for u in (0, 1))

def graph():
    states = [frozenset(range(1 << M))]; ids = {states[0]: 0}; edges = []
    for s in states:
        row = []
        for b in (0, 1):
            t = successor(s, b)
            if not t: row.append(-1); continue
            if t not in ids: ids[t] = len(states); states.append(t)
            row.append(ids[t])
        edges.append(row)
    return states, edges

def shape(s):
    a = sorted(s); base = a[0]; varying = 0; basis = {}
    for x in a:
        y = x ^ base; varying |= y
        while y:
            j = y.bit_length()-1
            if j in basis: y ^= basis[j]
            else: basis[j] = y; break
    coeff = [int(x in s) for x in range(1 << M)]
    h = 1
    while h < len(coeff):
        for i in range(0, len(coeff), 2*h):
            for j in range(i, i+h): coeff[j], coeff[j+h] = coeff[j]+coeff[j+h], coeff[j]-coeff[j+h]
        h *= 2
    peak = max(range(1, 1 << M), key=lambda k: abs(coeff[k]))
    nonconstant = [k for k in range(1, 1 << M) if abs(coeff[k]) < len(s)]
    residual = max(nonconstant, key=lambda k: abs(coeff[k])) if nonconstant else 0
    return dict(residual_mask=residual, residual_abs=abs(coeff[residual]) if residual else 0, size=len(s), fixed=M-varying.bit_count(), cylinder_hull=1 << varying.bit_count(), affine_hull=1 << len(basis), runs=1+sum(y != x+1 for x,y in zip(a,a[1:])), walsh_mask=peak, walsh_abs=abs(coeff[peak]), cylinder=len(s)==1 << varying.bit_count(), affine=len(s)==1 << len(basis))

def reverse(s):
    return frozenset(int(format(x, '010b')[::-1], 2) for x in s)

def run(out):
    out.mkdir(parents=True, exist_ok=True)
    states, edges = graph()
    with tempfile.TemporaryDirectory() as d:
        d = Path(d)
        src = ROOT/'tests/probes/lexicon/entropy2.c'
        wrapper = '#define main original_main\n#include "'+str(src)+'"\n#undef main\nint main(int argc,char **argv){int r=original_main(argc,argv);if(r)return r;for(size_t q=0;q<N;q++){printf("D %zu",q);for(uint32_t j=0;j<LEN[q];j++)printf(" %u",POOL[OFF[q]+j]);puts("");}return 0;}\n'
        (d/'dump.c').write_text(wrapper)
        subprocess.run(['cc','-O2','-o',str(d/'dump'),str(d/'dump.c'),'-lm'],check=True)
        raw=subprocess.check_output([str(d/'dump'),str(M),'200','cert','.01',str(d/'edges')],text=True)
        csets=[frozenset(map(int,line.split()[2:])) for line in raw.splitlines() if line.startswith('D ')]
        cedges=[list(map(int,line.split()[1:3])) for line in (d/'edges').read_text().splitlines()]
        assert states == csets and edges == cedges
        subprocess.run(['cc','-O2','-o',str(d/'records'),str(ROOT/'tests/probes/lexicon/records.c')],check=True)
        record=subprocess.check_output([str(d/'records'),'13','1'],text=True)
    (out/'record.txt').write_text(record)
    word=next(line.split()[2] for line in record.splitlines() if line.startswith('W '))
    # W is chronological binary, as explicitly printed by records.c.
    q=0; path=[q]; rejected=None
    for i,b in enumerate(word):
        q=edges[q][int(b)]
        if q < 0: rejected=i; break
        path.append(q)
    rng=random.Random(2306); picks=rng.sample(range(1,len(states)),12)
    controls={'cube':frozenset(range(1024)), 'singleton':frozenset([137]), 'cylinder':frozenset(x for x in range(1024) if x&7==5), 'parity':frozenset(x for x in range(1024) if x.bit_count()%2==0), 'random':frozenset(rng.sample(range(1024),128))}
    cs={k:shape(s) for k,s in controls.items()}
    assert cs['cube']['cylinder'] and cs['singleton']['cylinder'] and cs['cylinder']['cylinder']
    assert cs['parity']['affine'] and not cs['parity']['cylinder']
    assert not cs['random']['affine']
    rows=[]
    for label,i in [(f'random-{k+1}',i) for k,i in enumerate(picks)]+[('record-last-valid',path[-1])]:
        row=shape(states[i]); rev=shape(reverse(states[i]))
        for key in ('size','fixed','cylinder_hull','affine_hull','cylinder','affine'): assert row[key]==rev[key]
        rows.append(dict(label=label,id=i,reverse_runs=rev['runs'],**row))
    result=dict(width=M,states=len(states),edges=sum(j>=0 for row in edges for j in row),independent='all exact subsets and labeled transitions agree',controls=cs,record_header=record.splitlines()[0],record_word=word,record_rejected_at=rejected,record_path=path,sample=rows,SH1=any(not r['cylinder'] for r in rows[:12]),SH2=any(not r['affine'] for r in rows[:12]),all_noninitial_cylinders=sum(shape(s)['cylinder'] for s in states[1:]),all_noninitial_affine=sum(shape(s)['affine'] for s in states[1:]),affine_states=[dict(id=i,**shape(s)) for i,s in enumerate(states[1:],1) if shape(s)['affine']])
    (out/'result.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
    # Standalone vector contact sheet; no third-party plotting dependency required.
    svg=['<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="1120" viewBox="0 0 1000 1120">','<rect width="1000" height="1120" fill="white"/>','<text x="12" y="22" font-size="16">Width10 channel sets; black = member; integer x+32y</text>']
    for k,row in enumerate(rows):
        ox=12+(k%4)*248; oy=45+(k//4)*266
        svg.append(f'<text x="{ox}" y="{oy}" font-size="12">{row["label"]} q{row["id"]}: {row["size"]} members</text>')
        svg.append(f'<rect x="{ox}" y="{oy+8}" width="224" height="224" fill="#eeeeee"/>')
        for x in states[row['id']]:
            svg.append(f'<rect x="{ox+7*(x%32)}" y="{oy+8+7*(x//32)}" width="7" height="7" fill="black"/>')
        svg.append(f'<text x="{ox}" y="{oy+247}" font-size="11">fixed {row["fixed"]}; cube {row["cylinder_hull"]}; affine {row["affine_hull"]}</text>')
    svg.append('</svg>'); (out/'shapes.svg').write_text('\n'.join(svg))
    try:
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
        fig,axs=plt.subplots(4,4,figsize=(12,12))
        for ax,row in zip(axs.flat,rows):
            s=states[row['id']]; grid=[[int(32*y+x in s) for x in range(32)] for y in range(32)]
            ax.imshow(grid,cmap='gray_r',vmin=0,vmax=1,interpolation='nearest'); ax.set_title(f"{row['label']} q{row['id']} n{row['size']}\nfixed{row['fixed']} hull{row['cylinder_hull']} affine{row['affine_hull']}",fontsize=9); ax.set_xticks([]);ax.set_yticks([])
        for ax in list(axs.flat)[len(rows):]: ax.axis('off')
        fig.suptitle('Width10 channel subsets; black = member; integer x+32y');fig.tight_layout();fig.savefig(out/'shapes.png');plt.close(fig)
    except ImportError:
        print('PNG UNAVAILABLE: matplotlib missing; SVG and exact results retained')

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);run(p.parse_args().output)
