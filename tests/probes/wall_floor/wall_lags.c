/* wall_lags.c (Local, L1534): on real rows in quiet AAB stretches, the rate at which a cell differs from itself L ticks later, for L = 3, 6, 12, 24, 48, 96 and offsets to 400. Rows: 40 random cells, rain above. Quiet = letters pure AAB over the last 120 ticks.
   Usage: ./wall_lags N T SEED */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef unsigned char u8; typedef unsigned long long u64;
static u8 TOUT[4][256], TST[4][256];
static void mk(void){ for(int s=0;s<4;s++) for(int b=0;b<256;b++){ int p1=s>>1,p2=s&1,o=0; for(int i=0;i<8;i++){ int c=(b>>i)&1; int q=c^(p1|p2); o|=q<<i; p2=p1; p1=q; } TOUT[s][b]=o; TST[s][b]=(p1<<1)|p2; } }
static u64 rs; static u64 rnd(void){ rs^=rs<<13; rs^=rs>>7; rs^=rs<<17; return rs; }
#define KM 512
#define HB 128
static u8 hist[HB][KM]; static int letters[HB];
static const int LAG[6]={3,6,12,24,48,96}; static const int OFF[]={16,20,24,26,28,30,32,36,40,44,48,52,56,60,64,72,80,96,112,128,160,192,256,320,400};
#define NO 25
static long diff[6][NO],tot[6][NO];
int main(int c,char**a){ mk(); long N=atol(a[1]); int T=atoi(a[2]); rs=strtoull(a[3],0,10)*2654435761ULL+88172645463325252ULL; int WB=(3*T+300)/8+16; u8*r=malloc(WB),*q=malloc(WB); long quiet=0;
  for(long row=0;row<N;row++){ memset(r,0,WB); u64 x=rnd()&((1ULL<<40)-1); x|=1; for(int i=0;i<5;i++) r[i]=(x>>(8*i))&255; int b=(x>>39)&1; for(int j=40;j<WB*8;j++){ b^=1; if(b) r[j>>3]|=1<<(j&7); }
    int run=0; int d=-1; int settled=0;
    for(int t=0;t<T;t++){ int s; { int p1=1,p2=0; u8 o=r[0]&1; for(int j=1;j<8;j++){ int cc=(r[0]>>j)&1; int qq=cc^(p1|p2); o|=qq<<j; p2=p1; p1=qq; } q[0]=o; s=(p1<<1)|p2; } int lim=(40+3*(t+1)+120)/8+2; if(lim>WB) lim=WB; for(int i=1;i<lim;i++){ q[i]=TOUT[s][r[i]]; s=TST[s][r[i]]; } memcpy(q+lim,r+lim,WB-lim); /* rain above: flip phase */ for(int i=lim;i<WB;i++) q[i]=TOUT[s][r[i]],s=TST[s][r[i]]; u8*tmp=r; r=q; q=tmp;
      int L0=40+3*(t+1)+80; if(L0>WB*8-16) L0=WB*8-16; d=-1; for(int j=L0;j>=1;j--){ int a1=(r[j>>3]>>(j&7))&1,a0=(r[(j+1)>>3]>>((j+1)&7))&1; if(a1==a0){ d=j; break; } } if(d<KM+2) continue;
      /* the deep cell of the wall pair is at d; offset k = cell d+1-k */ int slot=t%HB; for(int k=0;k<KM;k++){ int j=d+1-k; hist[slot][k]=(r[j>>3]>>(j&7))&1; }
      u64 v=0; for(int k=0;k<11;k++) v|=(u64)hist[slot][k]<<(10-k); int L=(v==0x63C)?1:(v==0x63A)?2:0; letters[slot]=L;
      /* quiet test: last 120 letters are periodic with period 3 */ int ok=L!=0&&t>=HB; if(ok){ for(int i=0;i<HB-30&&ok;i++){ int s1=(t-i+HB)%HB,s2=(t-i-3+HB*2)%HB; if(letters[s1]!=letters[s2]||letters[s1]==0) ok=0; } }
      if(ok){ quiet++; for(int l=0;l<6;l++){ int s2=(t-LAG[l]+HB*4)%HB; for(int o=0;o<NO;o++){ int k=OFF[o]; tot[l][o]++; diff[l][o]+=hist[slot][k]!=hist[s2][k]; } } } } }
  printf("quiet ticks %ld\nlag\\offset",quiet); for(int o=0;o<NO;o++) printf(" %5d",OFF[o]); puts(""); for(int l=0;l<6;l++){ printf("%9d ",LAG[l]); for(int o=0;o<NO;o++) printf(" %.3f",tot[l][o]?(double)diff[l][o]/tot[l][o]:0.0); puts(""); } return 0; }
