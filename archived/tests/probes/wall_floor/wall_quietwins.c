/* wall_quietwins.c (Local, L1534): on the window chain in quiet AAB stretches, the distinct top-D windows and how often each occurs. Usage: ./wall_quietwins W N T SEED D */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef unsigned char u8; typedef unsigned long long u64; typedef unsigned __int128 u128;
static u8 TOUT[4][256], TST[4][256];
static void mk(void){ for(int s=0;s<4;s++) for(int b=0;b<256;b++){ int p1=s>>1,p2=s&1,o=0; for(int i=0;i<8;i++){ int c=(b>>i)&1; int q=c^(p1|p2); o|=q<<i; p2=p1; p1=q; } TOUT[s][b]=o; TST[s][b]=(p1<<1)|p2; } }
static u64 rs; static inline u64 rnd(void){ rs^=rs<<13; rs^=rs>>7; rs^=rs<<17; return rs; }
#define MAXW 1024
#define HM (1<<22)
static u128 key[HM]; static long cnt[HM];
static int cmpc(const void*a,const void*b){ long x=cnt[*(int*)a],y=cnt[*(int*)b]; return x<y?1:x>y?-1:0; }
int main(int c,char**a){ mk(); int W=atoi(a[1]); long N=atol(a[2]); long T=atol(a[3]); rs=strtoull(a[4],0,10)*2654435761ULL+88172645463325252ULL; int D=atoi(a[5]); for(int i=0;i<20;i++) rnd(); int nb=W/8,nw=W/64; static u64 A[MAXW/64+2],B[MAXW/64+2]; long tot=0,distinct=0;
  for(long ch=0;ch<N;ch++){ for(int i=0;i<nw;i++) A[i]=rnd(); A[nw]=0; { u64 top=0x63C; int base=W-11; for(int i=0;i<11;i++){ int j=base+i; u64 m=1ULL<<(j&63); if((top>>i)&1) A[j>>6]|=m; else A[j>>6]&=~m; } } long quiet=0; int l[4]={-1,-1,-1,-1};
    for(long t=1;t<=T;t++){ u8*x=(u8*)A; u8*o=(u8*)B; A[nw]=(u64)2; int s=rnd()>>62; for(int i=0;i<nb+1;i++){ o[i]=TOUT[s][x[i]]; s=TST[s][x[i]]; } for(int i=0;i<nw;i++) A[i]=(B[i]>>3)|(B[i+1]<<61);
      u64 topw=(A[(W-11)>>6]>>((W-11)&63)); if(((W-11)&63)>53) topw|=A[((W-11)>>6)+1]<<(64-((W-11)&63)); topw&=2047; int L=topw==0x63C?0:topw==0x63A?1:2; if(l[2]>=0&&L==l[2]) quiet++; else quiet=0; l[2]=l[1]; l[1]=l[0]; l[0]=L;
      if(quiet>200){ u128 v=0; for(int k=0;k<D;k++){ int j=W-1-k; if((A[j>>6]>>(j&63))&1) v|=((u128)1)<<k; } u64 h=((u64)v*0x9E3779B97F4A7C15ULL^(u64)(v>>64)*0xC2B2AE3D27D4EB4FULL)>>42; while(cnt[h]&&key[h]!=v) h=(h+1)&(HM-1); if(!cnt[h]){ key[h]=v; distinct++; } cnt[h]++; tot++; } } }
  int*idx=malloc(sizeof(int)*distinct); long n=0; for(int i=0;i<HM;i++) if(cnt[i]) idx[n++]=i; qsort(idx,n,sizeof(int),cmpc); printf("D %d: quiet ticks %ld, distinct windows %ld\n",D,tot,distinct); double cum=0; for(long i=0;i<n&&i<(c>6?atol(a[6]):24);i++){ cum+=(double)cnt[idx[i]]/tot; printf("%7.4f %7.4f ",(double)cnt[idx[i]]/tot,cum); for(int k=D-1;k>=0;k--) putchar((key[idx[i]]>>k)&1?'#':'.'); puts(""); } { long m[6]={0}; double c2=0; int thr[5]={0,0,0,0,0}; double q[5]={.5,.9,.99,.999,.9999}; int qi=0; for(long i=0;i<n&&qi<5;i++){ c2+=(double)cnt[idx[i]]/tot; while(qi<5&&c2>=q[qi]){ printf("mass %.4f in %ld windows\n",q[qi],i+1); qi++; } } } return 0; }
