/* wall_try.c (Local, L1532): a word of cells at the top of a row, random cells below, T backward ticks: when do the letters first leave their cycle?
   Usage: ./wall_try WORD N T SEED LOWMAX. WORD in # and . from low to high, ending at the wall pair. Prints the survivors and the first departures. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef unsigned char u8; typedef unsigned long long u64;
static u8 TOUT[4][256], TST[4][256];
static void mk(void){ for(int s=0;s<4;s++) for(int b=0;b<256;b++){ int p1=s>>1,p2=s&1,o=0; for(int i=0;i<8;i++){ int c=(b>>i)&1; int q=c^(p1|p2); o|=q<<i; p2=p1; p1=q; } TOUT[s][b]=o; TST[s][b]=(p1<<1)|p2; } }
static u64 rs; static u64 rnd(void){ rs^=rs<<13; rs^=rs>>7; rs^=rs<<17; return rs; }
int main(int c,char**a){ mk(); const char*W=a[1]; int n=strlen(W); long N=atol(a[2]); int T=atoi(a[3]); rs=strtoull(a[4],0,10)*2654435761ULL+88172645463325252ULL; int LM=atoi(a[5]);
  int WB=(3*T+LM+n+200)/8+16; u8*r=malloc(WB),*q=malloc(WB); long surv=0; long first[40]={0}; int minT=1<<30; long sumT=0;
  for(long tr=0;tr<N;tr++){ memset(r,0,WB); int low=8+rnd()%(LM-8); r[0]|=1; for(int j=1;j<low;j++) if(rnd()>>63) r[j>>3]|=1<<(j&7); for(int i=0;i<n;i++) if(W[i]=='#'){ int j=low+i; r[j>>3]|=1<<(j&7); } int b=W[n-1]=='#'; for(int j=low+n;j<WB*8;j++){ b^=1; if(b) r[j>>3]|=1<<(j&7); }
    int d=low+n-2; char prev2='?',prev1='?'; int dep=-1;
    /* letter at each tick */
    for(int t=0;t<T;t++){ int s; { int p1=1,p2=0; u8 o=r[0]&1; for(int j=1;j<8;j++){ int cc=(r[0]>>j)&1; int qq=cc^(p1|p2); o|=qq<<j; p2=p1; p1=qq; } q[0]=o; s=(p1<<1)|p2; } for(int i=1;i<WB;i++){ q[i]=TOUT[s][r[i]]; s=TST[s][r[i]]; } u8*tmp=r; r=q; q=tmp; d+=3; 
      int v=0; for(int i=0;i<11;i++){ int j=d+2-11+i; if((r[j>>3]>>(j&7))&1) v|=1<<i; } char L=(v==0x63C)?'A':(v==0x63A)?'B':'?';
      int ok; /* compare with the letter 3 ticks ago, once known, and also keep a record: use cycle by word detection */
      static char seq[4]; if(t<3){ seq[t]=L; ok=(L!='?'); } else ok=(L==seq[t%3]);
      if(!ok){ dep=t; break; } }
    if(dep<0) surv++; else { sumT+=dep; if(dep<minT) minT=dep; int k=0; int x=dep; while(x>1&&k<39){ x>>=1; k++; } first[k]++; } }
  printf("trials %ld ticks %d: survivors %ld; first departure earliest %d; by dyadic tick:",N,T,surv,minT==1<<30?-1:minT); for(int i=0;i<30;i++) if(first[i]) printf(" 2^%d:%ld",i,first[i]); puts(""); return 0; }
