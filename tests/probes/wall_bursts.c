/* wall_bursts.c (Local, L1529): quiet stretches between bursts of BAB events on long runs. Usage: ./wall_bursts ROWS TICKS LOW SEED */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
typedef unsigned long long u64;
#define MAXB 40100
static u64 s[2];
static inline u64 rotl(u64 x,int k){return (x<<k)|(x>>(64-k));}
static u64 rnd(void){u64 a=s[0],b=s[1],r=a+b;b^=a;s[0]=rotl(a,24)^b^(b<<16);s[1]=rotl(b,37);return r;}
static const unsigned char WA[11]={0,0,1,1,1,1,0,0,0,1,1}, WB[11]={0,1,0,1,1,1,0,0,0,1,1};
int main(int c,char**v){ long rows=atol(v[1]); int ticks=atoi(v[2]), low=atoi(v[3]); s[0]=0x9E3779B97F4A7C15ULL^atol(v[4]); s[1]=0xBF58476D1CE4E5B9ULL; for(int i=0;i<20;i++)rnd();
  static unsigned char x[MAXB],z[MAXB]; static char seq[14000]; int n=low+3*ticks+40; if(n>=MAXB) return 1; long gh[24]={0}; long none=0;
  for(long r=0;r<rows;r++){ x[0]=1; for(int j=1;j<low;j++) x[j]=rnd()&1; { int b=x[low-1]; for(int j=low;j<n;j++){b^=1;x[j]=b;} }
    int top=-1;
    for(int t=0;t<ticks;t++){ if(top<0){ int k=n-3; while(k>=1 && x[k]!=x[k+1]) k--; if(k>=10&&(!memcmp(x+k-9,WA,11)||!memcmp(x+k-9,WB,11))) top=k; } else top+=3;
      char ch='?'; if(top>=0){ if(!memcmp(x+top-9,WA,11)) ch='A'; else if(!memcmp(x+top-9,WB,11)) ch='B'; }
      seq[t]=ch; int m=top>=0?top+40:n; if(m>n) m=n;
      int p1=1,p2=0; z[0]=1; for(int j=1;j<m;j++){ int o=x[j]^(p1|p2); z[j]=o; p2=p1; p1=o; } for(int j=m;j<n;j++) z[j]=!x[j]; memcpy(x,z,n); }
    int last=-1000000, cnt=0; int starts[2000],ns=0, ends[2000]; for(int t=2;t<ticks;t++) if(seq[t-2]=='B'&&seq[t-1]=='A'&&seq[t]=='B'){ if(t-last>60){ if(ns<2000){starts[ns]=t; ns++;} } if(ns) ends[ns-1]=t; last=t; }
    if(r<16){ printf("row %ld bursts (start,len):",r); for(int i=0;i<ns&&i<26;i++) printf(" %d+%d",starts[i],ends[i]-starts[i]); printf("\n"); }
    if(ns<2) none++; for(int i=1;i<ns;i++){ int g=starts[i]-ends[i-1]; int b=0; while((1<<b)<=g) b++; gh[b]++; } }
  printf("quiet gaps by dyadic length:"); for(int b=0;b<24;b++) if(gh[b]) printf(" <%d:%ld",1<<b,gh[b]); printf("\nrows with fewer than two bursts %ld of %ld\n",none,rows); return 0; }
