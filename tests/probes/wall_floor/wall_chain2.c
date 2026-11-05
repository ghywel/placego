/* wall_chain.c (Local, L1534): the window chain at width W: a row's top W cells, fair random lower states at the low end, for T ticks, with no growth in cost. N chains from random cells under a letter.
   Records breaks from AAB by time, and for each chain the tick from which its letters are periodic to the end. Chains that stop breaking are candidates for locks; their top cells are written to chain_cand.txt.
   Usage: ./wall_chain W N T SEED */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef unsigned char u8; typedef unsigned long long u64;
static u8 TOUT[4][256], TST[4][256];
static void mk(void){ for(int s=0;s<4;s++) for(int b=0;b<256;b++){ int p1=s>>1,p2=s&1,o=0; for(int i=0;i<8;i++){ int c=(b>>i)&1; int q=c^(p1|p2); o|=q<<i; p2=p1; p1=q; } TOUT[s][b]=o; TST[s][b]=(p1<<1)|p2; } }
static u64 rs; static inline u64 rnd(void){ rs^=rs<<13; rs^=rs>>7; rs^=rs<<17; return rs; }
#define MAXW 2048
int main(int c,char**a){ mk(); int W=atoi(a[1]); long N=atol(a[2]); long T=atol(a[3]); rs=strtoull(a[4],0,10)*2654435761ULL+88172645463325252ULL; for(int i=0;i<20;i++) rnd(); int nb=W/8; int nw=W/64; static u64 A[MAXW/64+2],B[MAXW/64+2]; long dy[48]={0},dyt[48]={0}; long endAB=0,endAAB=0,endOther=0; FILE*f=fopen("chain_cand.txt","w"); long lastAAB[8]={0};
  for(long ch=0;ch<N;ch++){ for(int i=0;i<nw;i++) A[i]=rnd(); A[nw]=0; /* top 11 cells = letter A */ { u64 top=(rnd()>>63)?0x63C:0x63A; int base=W-11; for(int i=0;i<11;i++){ int j=base+i; u64 m=1ULL<<(j&63); if((top>>i)&1) A[j>>6]|=m; else A[j>>6]&=~m; } }
    int l1=-1,l2=-1,l3=-1; long lastbreakAAB=0,lastbreakAB=0; long nbreak=0; long bad=0; int prev=0;
    for(long t=1;t<=T;t++){ u8*x=(u8*)A; u8*o=(u8*)B; A[nw]=(u64)2; /* rain above: cells W, W+1, W+2 = 0,1,0 */ int s=rnd()>>62; for(int i=0;i<nb+1;i++){ o[i]=TOUT[s][x[i]]; s=TST[s][x[i]]; } /* drop three low cells */ for(int i=0;i<nw;i++) A[i]=(B[i]>>3)|(B[i+1]<<61);
      /* mask cells at and above W are cleared by A[nw] reset next tick */ u64 topw=(A[(W-11)>>6]>>((W-11)&63)); if(((W-11)&63)>53) topw|=A[((W-11)>>6)+1]<<(64-((W-11)&63)); topw&=2047; int L=topw==0x63C?0:topw==0x63A?1:2; if(L==2){ bad++; }
      /* AAB check: breaks when the letter differs from three ticks ago */ if(l3>=0&&L!=l3){ lastbreakAAB=t; nbreak++; int k=0; long y=t; while(y>1){ y>>=1; k++; } dy[k]++; } if(l2>=0&&L!=l2){ lastbreakAB=t; } l3=l2; l2=l1; l1=L; }
    long lim=T/2; { int k=0; long y=T; while(y>1){ y>>=1; k++; } for(int i=0;i<=k;i++) dyt[i]+=1; }
    if(lastbreakAB<lim){ endAB++; } else if(lastbreakAAB<lim){ endAAB++; for(int i=0;i<8;i++){ } fprintf(f,"AAB since %ld: ",lastbreakAAB); for(int j=W-1;j>=W-400;j--) fputc((A[j>>6]>>(j&63))&1?'#':'.',f); fputc('\n',f); fflush(f); } else endOther++; if(ch%100==99){ fprintf(stderr,"%ld chains\n",ch+1); } if(bad) fprintf(stderr,"chain %ld bad letters %ld\n",ch,bad); }
  printf("W %d chains %ld ticks %ld: letters AB from before T/2 %ld, AAB from before T/2 %ld, other %ld\n",W,N,T,endAB,endAAB,endOther); printf("changes of the lag-3 letter by dyadic tick, per chain:"); for(int i=0;i<40;i++) if(dyt[i]&&dy[i]) printf(" 2^%d:%.2f",i,(double)dy[i]/N); puts(""); return 0; }
