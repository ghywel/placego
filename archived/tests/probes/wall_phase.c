/* wall_phase.c (Local, L1530): which phase is a row in over time? In each block of 300 ticks: AAB (period 3 throughout), AB (period 2 throughout), or mixed. Transition counts between phases, and the share per time.
   Usage: ./wall_phase ROWS TICKS LOW SEED */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
typedef unsigned long long u64;
#define MAXB 70000
#define BL 300
static u64 s[2];
static inline u64 rotl(u64 x,int k){return (x<<k)|(x>>(64-k));}
static u64 rnd(void){u64 a=s[0],b=s[1],r=a+b;b^=a;s[0]=rotl(a,24)^b^(b<<16);s[1]=rotl(b,37);return r;}
static const unsigned char WA[11]={0,0,1,1,1,1,0,0,0,1,1}, WB[11]={0,1,0,1,1,1,0,0,0,1,1};
static long share[200][3]; static long burstrows[80]; static long tr[3][3]; static long stay2[64];
int main(int c,char**v){ long rows=atol(v[1]); int ticks=atoi(v[2]), low=atoi(v[3]); s[0]=0x9E3779B97F4A7C15ULL^atol(v[4]); s[1]=0xBF58476D1CE4E5B9ULL; for(int i=0;i<20;i++)rnd();
  static unsigned char x[MAXB],z[MAXB]; static char seq[23000]; int n=low+3*ticks+40; if(n>=MAXB) return 1;
  for(long r=0;r<rows;r++){ x[0]=1; for(int j=1;j<low;j++) x[j]=rnd()&1; { int b=x[low-1]; for(int j=low;j<n;j++){b^=1;x[j]=b;} }
    int top=-1;
    for(int t=0;t<ticks;t++){ if(top<0){ int k=n-3; while(k>=1 && x[k]!=x[k+1]) k--; if(k>=10&&(!memcmp(x+k-9,WA,11)||!memcmp(x+k-9,WB,11))) top=k; } else top+=3;
      char ch='?'; if(top>=0){ if(!memcmp(x+top-9,WA,11)) ch='A'; else if(!memcmp(x+top-9,WB,11)) ch='B'; } seq[t]=ch;
      int m=top>=0?top+40:n; if(m>n) m=n; int p1=1,p2=0; z[0]=1; for(int j=1;j<m;j++){ int o=x[j]^(p1|p2); z[j]=o; p2=p1; p1=o; } for(int j=m;j<n;j++) z[j]=!x[j]; memcpy(x,z,n); }
    int prev=-1, run2=0, nb=0; for(int b=0;(b+1)*BL<=ticks;b++){ int p3=1,p2=1; for(int t=b*BL+3;t<(b+1)*BL;t++){ if(seq[t]!=seq[t-3]) p3=0; if(seq[t]!=seq[t-2]) p2=0; } int ph=p3?0:p2?1:2; if(b<200) share[b][ph]++; if(prev>=0) tr[prev][ph]++; if(prev==0&&ph==2&&b>=3) nb++; 
      if(ph==1) run2++; else { if(run2){ int q=run2<63?run2:63; stay2[q]++; } run2=0; } prev=ph; } if(run2){ int q=run2<63?run2:63; stay2[q]++; } burstrows[nb<79?nb:79]++; }
  printf("share by time block of %d ticks: AAB, AB, mixed\n",BL); for(int b=0;(b+1)*BL<=ticks&&b<200;b+=(b<8?1:8)) printf(" t=%6d %6ld %6ld %6ld\n",b*BL,share[b][0],share[b][1],share[b][2]);
  printf("block transitions (rows from, columns to; AAB, AB, mixed):\n"); for(int a=0;a<3;a++) printf(" %8ld %8ld %8ld\n",tr[a][0],tr[a][1],tr[a][2]);
  printf("rows by number of departures from AAB after block 3:"); for(int q=0;q<80;q++) if(burstrows[q]) printf(" %d:%ld",q,burstrows[q]); printf("\n"); printf("AB stretches in blocks:"); for(int q=1;q<64;q++) if(stay2[q]) printf(" %d:%ld",q,stay2[q]); printf("\n"); return 0; }
