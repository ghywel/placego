/* wall_late.c (Local, L1529): when do x blocks (BA followed by B) stop? For each row: ticks of every occurrence of BAB, up to TICKS. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
typedef unsigned long long u64;
#define MAXB 16384
static u64 s[2];
static inline u64 rotl(u64 x,int k){return (x<<k)|(x>>(64-k));}
static u64 rnd(void){u64 a=s[0],b=s[1],r=a+b;b^=a;s[0]=rotl(a,24)^b^(b<<16);s[1]=rotl(b,37);return r;}
static const unsigned char WA[11]={0,0,1,1,1,1,0,0,0,1,1}, WB[11]={0,1,0,1,1,1,0,0,0,1,1};
int main(int c,char**v){ long rows=atol(v[1]); int ticks=atoi(v[2]), low=atoi(v[3]); s[0]=0x9E3779B97F4A7C15ULL^atol(v[4]); s[1]=0xBF58476D1CE4E5B9ULL; for(int i=0;i<20;i++)rnd();
  static unsigned char x[MAXB],z[MAXB]; static char seq[8192]; long binsx[16]={0}; long lastbin[16]={0}; int n=low+3*ticks+40; if(n>=MAXB) return 1;
  for(long r=0;r<rows;r++){ x[0]=1; for(int j=1;j<low;j++) x[j]=rnd()&1; { int b=x[low-1]; for(int j=low;j<n;j++){b^=1;x[j]=b;} }
    int len=0; int top=-1;
    for(int t=0;t<ticks;t++){ if(top<0){ int k=n-3; while(k>=1 && x[k]!=x[k+1]) k--; if(k>=10&&(!memcmp(x+k-9,WA,11)||!memcmp(x+k-9,WB,11))) top=k; } else top+=3;
      char ch='?'; if(top>=0){ if(!memcmp(x+top-9,WA,11)) ch='A'; else if(!memcmp(x+top-9,WB,11)) ch='B'; else {printf("left the words at t=%d\n",t);} }
      seq[t]=ch;
      /* only rows up to top+4 need work */
      int m = top>=0 ? top+12 : n; if(m>n) m=n;
      int p1=1,p2=0; z[0]=1; for(int j=1;j<m;j++){ int o=x[j]^(p1|p2); z[j]=o; p2=p1; p1=o; }
      if(m<n){ /* rain tail flips */ for(int j=m;j<n;j++){ int o=x[j]^(p1|p2); z[j]=o; p2=p1; p1=o; } }
      memcpy(x,z,n); }
    int last=-1; for(int t=2;t<ticks;t++) if(seq[t-2]=='B'&&seq[t-1]=='A'&&seq[t]=='B'){ last=t; int b=0; while((1<<b)<=t) b++; binsx[b]++; }
    if(last>=0){ int b=0; while((1<<b)<=last) b++; lastbin[b]++; } else lastbin[0]++; }
  printf("rows %ld ticks %d: BAB events by dyadic tick range, per row, density per tick\n",rows,ticks);
  for(int b=1;b<16;b++) if(binsx[b]) printf(" [%d,%d): %ld events, %.5f per row-tick\n",1<<(b-1),1<<b,binsx[b],(double)binsx[b]/rows/(1<<(b-1)));
  printf("last BAB tick by range:"); for(int b=0;b<16;b++) if(lastbin[b]) printf(" <%d:%ld",1<<b,lastbin[b]); printf("\n"); return 0; }
