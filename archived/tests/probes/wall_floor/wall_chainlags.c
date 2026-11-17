/* wall_chainlags.c (Local, L1534): lag difference rates by offset on the window chain, in quiet AAB stretches, and how deep a quiet row agrees with a set of reference words. Usage: ./wall_chainlags W N T SEED [REFFILE] */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef unsigned char u8; typedef unsigned long long u64;
static u8 TOUT[4][256], TST[4][256];
static void mk(void){ for(int s=0;s<4;s++) for(int b=0;b<256;b++){ int p1=s>>1,p2=s&1,o=0; for(int i=0;i<8;i++){ int c=(b>>i)&1; int q=c^(p1|p2); o|=q<<i; p2=p1; p1=q; } TOUT[s][b]=o; TST[s][b]=(p1<<1)|p2; } }
static u64 rs; static inline u64 rnd(void){ rs^=rs<<13; rs^=rs>>7; rs^=rs<<17; return rs; }
#define MAXW 1024
#define HB 256
#define NL 5
static const int LAG[NL]={3,6,12,24,48};
static long diff[NL][MAXW],tot; static u8 hist[HB][MAXW]; static int let[HB];
static char ref[64][700]; static int nref=0, reflen[64]; static long agree[700];
int main(int c,char**a){ mk(); int W=atoi(a[1]); long N=atol(a[2]); long T=atol(a[3]); rs=strtoull(a[4],0,10)*2654435761ULL+88172645463325252ULL; for(int i=0;i<20;i++) rnd(); if(c>5){ FILE*f=fopen(a[5],"r"); while(fscanf(f,"%699s",ref[nref])==1){ reflen[nref]=strlen(ref[nref]); nref++; } fclose(f); } int nb=W/8,nw=W/64; static u64 A[MAXW/64+2],B[MAXW/64+2]; long ticks=0;
  for(long ch=0;ch<N;ch++){ for(int i=0;i<nw;i++) A[i]=rnd(); A[nw]=0; { u64 top=0x63C; int base=W-11; for(int i=0;i<11;i++){ int j=base+i; u64 m=1ULL<<(j&63); if((top>>i)&1) A[j>>6]|=m; else A[j>>6]&=~m; } } int quiet=0; int l[4]={-1,-1,-1,-1};
    for(long t=1;t<=T;t++){ u8*x=(u8*)A; u8*o=(u8*)B; A[nw]=(u64)2; int s=rnd()>>62; for(int i=0;i<nb+1;i++){ o[i]=TOUT[s][x[i]]; s=TST[s][x[i]]; } for(int i=0;i<nw;i++) A[i]=(B[i]>>3)|(B[i+1]<<61);
      u64 topw=(A[(W-11)>>6]>>((W-11)&63)); if(((W-11)&63)>53) topw|=A[((W-11)>>6)+1]<<(64-((W-11)&63)); topw&=2047; int L=topw==0x63C?0:topw==0x63A?1:2; if(l[2]>=0&&L==l[2]) quiet++; else quiet=0; l[2]=l[1]; l[1]=l[0]; l[0]=L; int slot=t%HB; let[slot]=L;
      /* cells by offset: offset k = cell W-1-k... with wall pair at offsets 0,1 */ if(t>500&&quiet>120){ for(int k=0;k<W&&k<MAXW;k++){ int j=W-1-k; hist[slot][k]=(A[j>>6]>>(j&63))&1; } if(quiet>180&&(t%3==0)){ ticks++; for(int li=0;li<NL;li++){ u8*h0=hist[slot],*h1=hist[(t-LAG[li]+HB*8)%HB]; for(int k=0;k<W;k++) diff[li][k]+=h0[k]^h1[k]; } tot++; if(nref){ int best=0; for(int r=0;r<nref;r++){ int k=0; while(k<reflen[r]&&(ref[r][reflen[r]-1-k]=='?'||(ref[r][reflen[r]-1-k]=='#')==hist[slot][k])) k++; if(k>best) best=k; } agree[best]++; } } } } }
  printf("quiet samples %ld\noffset lag3 lag6 lag12 lag24 lag48\n",tot); for(int k=12;k<W&&k<220;k+=(k<72?2:8)){ printf("%4d",k); for(int li=0;li<NL;li++) printf(" %.4f",(double)diff[li][k]/tot); puts(""); }
  if(nref){ printf("deepest agreement with a reference word:"); long cum=0; for(int k=699;k>=0;k--){ if(agree[k]){ cum+=agree[k]; } } long run=0; for(int k=0;k<700;k++) if(agree[k]){ run+=agree[k]; printf(" %d:%ld",k,agree[k]); } puts(""); } return 0; }
