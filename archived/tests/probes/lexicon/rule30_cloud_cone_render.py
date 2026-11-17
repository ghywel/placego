#!/usr/bin/env python3
"""rule30_cloud_cone_render.py: the owner's observation (2026-10-11 17:20 BST) on the clamped-centre renders: the half-
plane to the left of the wheel column shows plainly regular patches inside otherwise chaotic texture. This script draws
the model's account on the same picture: every left cell x(-k, t) is a function of columns 0 and 1 over the ticks
t..t+k (left permutivity), so wherever both columns repeat exactly at lag P over a stretch of ticks, every cell in the
leftward cone under that stretch (t >= s1, t + k <= s2) repeats at lag P as well, and the cone is exactly periodic. The
cones are tinted (green: white cells pale, black cells dark); kicks of the wheel are the cone boundaries, diagonals
running up and to the left. Reported: the fraction of drawn left cells inside a cone, and the lag used.

RUN-ON:     cpu (Python 3 standard library plus numpy; seconds)
COMMAND:    python3 tests/probes/lexicon/rule30_cloud_cone_render.py [OUTDIR=.] [T=150] [W=110] [SCALE=6]

Every lag P from 2 to 120 is tried; a cell is tinted by the SMALLEST lag whose cone holds it (both columns repeat at
lag P over the cell's window). Beside 0101 the wheel between kicks is made of 10- and 6-step pieces and this right
half starts in the period-4 word 0011, so the short lags carry most of the regularity, not 56; beside U only
multiples of 56 can occur. Colours: lag 4 yellow, 6 amber, 10 green, 56 teal, others blue-grey. The same 12-cell
right half as the CL358 renders. The PNGs are written by a pure-Python writer and belong outside git.
"""
import numpy as np, zlib, struct, sys, os
U=[int(b) for b in "00010011010001001101000100110100010011010001001101001101"]
OUT=sys.argv[1] if len(sys.argv)>1 else '.'
T=int(sys.argv[2]) if len(sys.argv)>2 else 150; W=int(sys.argv[3]) if len(sys.argv)>3 else 110
S=int(sys.argv[4]) if len(sys.argv)>4 else 6
right=np.array([int(b) for b in '111101101110'],dtype=np.uint8)
def panel(wall):
    Tc=T+W+2; R=W+Tc+4
    row=np.zeros(R,dtype=np.uint8); row[:len(right)]=right
    rights=np.zeros((Tc,R),dtype=np.uint8); c=np.zeros(Tc,dtype=np.uint8)
    walls=np.array([wall(t) for t in range(Tc)],dtype=np.uint8)
    for t in range(Tc):
        rights[t]=row; c[t]=row[0]
        left=np.concatenate(([walls[t]],row[:-1])); rn=np.concatenate((row[1:],[0])); row=left^(row|rn)
    prev=walls.copy(); prev2=c.copy(); lefts=[]
    for k in range(1,W+1):
        n=len(prev)-1; cur=prev[1:]^(prev[:-1]|prev2[:n]); lefts.append(cur[:T]); prev2,prev=prev,cur
    G=np.zeros((T,2*W+1),dtype=np.uint8)
    for k in range(1,W+1): G[:,W-k]=lefts[k-1][:T]
    G[:,W]=walls[:T]; G[:,W+1:]=rights[:T,:W]
    return G,walls,c
def cones(walls,c,P):
    Tc=len(c); eq=np.zeros(Tc,dtype=bool); eq[:Tc-P]=(c[:Tc-P]==c[P:])&(walls[:Tc-P]==walls[P:])
    # run[t] = length of the run of eq ones starting at t
    run=np.zeros(Tc+1,dtype=np.int64)
    for t in range(Tc-1,-1,-1): run[t]=run[t+1]+1 if eq[t] else 0
    inc=np.zeros((T,W),dtype=bool)        # inc[t, k-1]: cell (-k, t) inside a cone
    for k in range(1,W+1): inc[:,k-1]=run[:T]>=k+1
    return inc
TINT={4:((255,245,170),(150,130,0)),6:((250,225,175),(150,85,0)),10:((200,245,200),(0,110,40)),
      56:((185,235,235),(0,105,110))}; OTHER=((215,220,240),(50,60,120))
def rgb(G,lag):   # lag[t, k-1]: the smallest lag whose cone holds cell (-k, t), 0 if none
    H,Wd=G.shape; img=np.full((H,Wd,3),255,dtype=np.uint8); img[G==1]=(0,0,0)
    for k in range(1,W+1):
        col=W-k
        for P in np.unique(lag[:,k-1]):
            if P==0: continue
            pale,dark=TINT.get(int(P),OTHER); m=lag[:,k-1]==P
            img[m&(G[:,col]==0),col]=pale; img[m&(G[:,col]==1),col]=dark
    img[:,W]=np.where(G[:,W:W+1]==1,(200,0,0),(255,215,215))
    img[:,W+1]=np.where(G[:,W+1:W+2]==1,(0,60,200),(205,220,255))
    return np.repeat(np.repeat(img,S,axis=0),S,axis=1)
def png(img,path):
    H,Wd,_=img.shape; raw=b''.join(b'\x00'+img[y].tobytes() for y in range(H))
    def chunk(t,d): return struct.pack('>I',len(d))+t+d+struct.pack('>I',zlib.crc32(t+d)&0xffffffff)
    open(path,'wb').write(b'\x89PNG\r\n\x1a\n'+chunk(b'IHDR',struct.pack('>IIBBBBB',Wd,H,8,2,0,0,0))
                          +chunk(b'IDAT',zlib.compress(raw,9))+chunk(b'IEND',b''))
imgs=[]
for name,wall in (('0101',lambda t:t%2),('U',lambda t:U[t%56])):
    G,walls,c=panel(wall); lag=np.zeros((T,W),dtype=np.int64); share={}; allok=True
    for P in range(2,121):
        inc=cones(walls,c,P)
        if not inc.any(): continue
        # check: every cell flagged inside a cone equals its copy P later (when that copy is drawn)
        allok&=all(G[t,W-k]==G[t+P,W-k] for k in range(1,W+1) for t in range(T-P) if inc[t,k-1])
        new=inc&(lag==0); lag[new]=P; share[P]=new.mean()
    top=sorted(share.items(),key=lambda x:-x[1])[:6]
    print('centre %-4s | left cells drawn %d | inside some cone (lags 2..120) %.3f | flagged cells equal their copy: %s'
          %(name,T*W,(lag>0).mean(),allok))
    print('   share by smallest lag:',', '.join('%d: %.3f'%(P,v) for P,v in top))
    img=rgb(G,lag); imgs.append(img); png(img,os.path.join(OUT,'cones_%s.png'%name))
gap=np.full((12,imgs[0].shape[1],3),(120,120,120),dtype=np.uint8)
png(np.concatenate((imgs[0],gap,imgs[1])),os.path.join(OUT,'cones_both.png')); print('written to',OUT)
