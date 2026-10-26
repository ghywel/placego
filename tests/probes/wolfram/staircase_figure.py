#!/usr/bin/env python3
"""Standalone mathematical figure from a fresh scalar single-seed evolution.

No screenshot is opened or modified. Pillow draws the computed cells and labels.
Usage: python staircase_figure.py OUTPUT.png
"""
import sys
from PIL import Image, ImageDraw, ImageFont


T=112;span=2*T+1
g=[bytearray(span)];g[0][T]=1
for t in range(T):
    r=g[-1]
    g.append(bytearray((30>>(4*(r[i-1] if i else 0)+2*r[i]+(r[i+1] if i+1<span else 0)))&1 for i in range(span)))

im=Image.new('RGB',(1060,750),'#faf8f2');d=ImageDraw.Draw(im)
def font(size):
    try:return ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf',size)
    except OSError:return ImageFont.load_default(size=size)
ink='#172028';gold='#b6750c';green='#087d5d';red='#bc433c'
d.text((35,20),'Why the staircase ends in a blinking column',font=font(28),fill=ink)
d.text((35,58),'Computed afresh from one initial 1. Cream = 1; dark = 0. Time runs downward.',font=font(17),fill=ink)
ox,oy,size=85,125,26
xmin,xmax,tmin,tmax=80,96,91,110
for x in range(xmin,xmax+1):d.text((ox+(x-xmin)*size+4,oy-25),str(x),font=font(12),fill=ink)
for t in range(tmin,tmax+1):
    d.text((ox-38,oy+(t-tmin)*size+5),str(t),font=font(13),fill=ink)
    for x in range(xmin,xmax+1):
        v=g[t][T+x];xx=ox+(x-xmin)*size;yy=oy+(t-tmin)*size
        d.rectangle((xx,yy,xx+size-1,yy+size-1),fill='#ebe6da' if v else '#15181c',outline='#77766f')
        d.text((xx+9,yy+5),str(v),font=font(12),fill='#55564f' if v else '#b8b9b3')
for x,a,b in [(83,94,99),(85,95,101),(87,95,103),(89,98,105),(91,100,107)]:
    xx=ox+(x-xmin)*size;yy=oy+(a-tmin)*size
    d.rectangle((xx+1,yy+1,xx+size-2,oy+(b-tmin+1)*size-2),outline=gold,width=3)
x,a,b=92,100,108;xx=ox+(x-xmin)*size
d.rectangle((xx-2,oy+(a-tmin)*size-2,xx+size+1,oy+(b-tmin+1)*size+1),outline=green,width=4)
d.text((ox,oy+(tmax-tmin+1)*size+15),'x = position        t = update number',font=font(16),fill=ink)
lines=[('STEADY STRIPES',gold,24),('Gold frames: 1 stays 1.',ink,20),('Heights: 6, 7, 9, 8, 8.',ink,20),('',ink,14),
       ('THE ENDPOINT',green,24),('Green frame: 101010101',ink,20),('Nine alternating cells.',ink,20),('',ink,14),
       ('THE LOCAL REASON',ink,24),('Beside a steady 1:',ink,20),('11 is forbidden.',ink,20),('00 locks a new 0 / 1 pair.',ink,20),('That pair builds the next step.',ink,20),('',ink,14),
       ('No next step → alternation.',green,22),('',ink,14),('The green frame ends at t = 108.',ink,18),('The next cell is also 1:',ink,18),('this clock is temporary.',ink,18)]
yy=122
for s,col,sz in lines:
    d.text((570,yy),s,font=font(sz),fill=col);yy+=sz+9
d.text((35,710),'Single-party hand derivation + finite checks; no claim of endless period 2 or a new prize result.',font=font(16),fill=ink)
im.save(sys.argv[1])
