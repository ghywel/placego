/* wall_spec.c (Local, L1534): difference rate at every lag from 1 to 200 for chosen offsets on the window chain, in quiet AAB stretches. Prints for each offset the ten lowest lags. Usage: ./wall_spec W N T SEED */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef unsigned char u8; typedef unsigned long long u64;
static u8 TOUT[4][256], TST[4][256];
static void mk(void){ for(int s=0;s<4;s++) for(int b=0;b<256;b++){ int p1=s>>1,p2=s&1,o=0; for(int i=0;i<8;i++){ int c=(b>>i)&1; int q=c^(p1|p2); o|=q<<i; p2=p1; p1=q; } TOUT[s][b]=o; TST[s][b]=(p1<<1)|p2; } }
static u64 rs; static inline u64 rnd(void){ rs^=rs<<13; rs^=rs>>7; rs^=rs<<17; return rs; }
#define MAXW 1024
#define HB 256
#define ML 200
static const int OFF[]={26,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,68,72,76,80,84,88,96,104,112,120,128}; 
#define NO 30
static u8 hist[HB][NO]; static long diff[NO][ML+1],tot[ML+1];
int main(int c,char**a){ mk(); int W=atoi(a[1]); long N=atol(a[2]); long T=atol(a[3]); rs=strtoull(a[4],0,10)*2654435761ULL+88172645463325252ULL; for(int i=0;i<20;i++) rnd(); int nb=W/8,nw=W/64; static u64 A[MAXW/64+2],B[MAXW/64+2];
  for(long ch=0;ch<N;ch++){ for(int i=0;i<nw;i++) A[i]=rnd(); A[nw]=0; { u64 top=0x63C; int base=W-11; for(int i=0;i<11;i++){ int j=base+i; u64 m=1ULL<<(j&63); if((top>>i)&1) A[j>>6]|=m; else A[j>>6]&=~m; } } long quiet=0; int l[4]={-1,-1,-1,-1};
    for(long t=1;t<=T;t++){ u8*x=(u8*)A; u8*o=(u8*)B; A[nw]=(u64)2; int s=rnd()>>62; for(int i=0;i<nb+1;i++){ o[i]=TOUT[s][x[i]]; s=TST[s][x[i]]; } for(int i=0;i<nw;i++) A[i]=(B[i]>>3)|(B[i+1]<<61);
      u64 topw=(A[(W-11)>>6]>>((W-11)&63)); if(((W-11)&63)>53) topw|=A[((W-11)>>6)+1]<<(64-((W-11)&63)); topw&=2047; int L=topw==0x63C?0:topw==0x63A?1:2; if(l[2]>=0&&L==l[2]) quiet++; else quiet=0; l[2]=l[1]; l[1]=l[0]; l[0]=L; int slot=t%HB; for(int o2=0;o2<NO;o2++){ int j=W-1-OFF[o2]; hist[slot][o2]=(A[j>>6]>>(j&63))&1; }
      if(quiet>ML+60&&(t%5==0)){ for(int g=1;g<=ML;g++){ int s2=(int)((t-g+(long)HB*1000)%HB); tot[g]++; for(int o2=0;o2<NO;o2++) diff[o2][g]+=hist[slot][o2]^hist[s2][o2]; } } } }
  for(int o2=0;o2<NO;o2++){ printf("offset %3d:",OFF[o2]); int used[ML+1]={0}; for(int r=0;r<9;r++){ int b=-1; double br=2; for(int g=1;g<=ML;g++) if(!used[g]){ double v=(double)diff[o2][g]/tot[g]; if(v<br){ br=v; b=g; } } used[b]=1; printf(" %d:%.3f",b,br); } puts(""); } return 0; }
