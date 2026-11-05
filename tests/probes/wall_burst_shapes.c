/* wall_burst_shapes.c (Local, L1530): bursts after a quiet stretch of at least GAP ticks of AAB. A burst is the letter word from the first departure from the period-3 pattern to the last, before the next stretch of 60 quiet ticks.
   Prints the number of distinct shapes, the most common, and the waiting times. Usage: ./wall_burst_shapes ROWS TICKS LOW SEED GAP */
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
#define MS 20000
static char *shape[MS]; static long cnt[MS]; static int ns=0; static long waits[64]; static double wsum=0; static long wn=0; static int wlist[100000];
static int cmpc(const void*a,const void*b){ long x=cnt[*(int*)a],y=cnt[*(int*)b]; return x<y?1:x>y?-1:0; }
int main(int c,char**v){ long rows=atol(v[1]); int ticks=atoi(v[2]), low=atoi(v[3]); s[0]=0x9E3779B97F4A7C15ULL^atol(v[4]); s[1]=0xBF58476D1CE4E5B9ULL; int GAP=atoi(v[5]); for(int i=0;i<20;i++)rnd();
  static unsigned char x[MAXB],z[MAXB]; static char seq[14000]; int n=low+3*ticks+40; if(n>=MAXB) return 1; long bursts=0;
  for(long r=0;r<rows;r++){ x[0]=1; for(int j=1;j<low;j++) x[j]=rnd()&1; { int b=x[low-1]; for(int j=low;j<n;j++){b^=1;x[j]=b;} }
    int top=-1;
    for(int t=0;t<ticks;t++){ if(top<0){ int k=n-3; while(k>=1 && x[k]!=x[k+1]) k--; if(k>=10&&(!memcmp(x+k-9,WA,11)||!memcmp(x+k-9,WB,11))) top=k; } else top+=3;
      char ch='?'; if(top>=0){ if(!memcmp(x+top-9,WA,11)) ch='A'; else if(!memcmp(x+top-9,WB,11)) ch='B'; } seq[t]=ch;
      int m=top>=0?top+40:n; if(m>n) m=n; int p1=1,p2=0; z[0]=1; for(int j=1;j<m;j++){ int o=x[j]^(p1|p2); z[j]=o; p2=p1; p1=o; } for(int j=m;j<n;j++) z[j]=!x[j]; memcpy(x,z,n); }
    /* mark ticks that break period 3 */
    int t=3,quiet=0,qstart=3; while(t<ticks){ if(seq[t]==seq[t-3]){ quiet++; t++; continue; }
      /* a break at t */
      if(quiet>=GAP){ int e=t, q=0, last=t; int u=t; while(u<ticks&&q<60){ if(seq[u]==seq[u-3]) q++; else {q=0; last=u;} u++; }
        if(u<ticks){ int len=last-t+1; char *w=malloc(len+1); memcpy(w,seq+t,len); w[len]=0; int i; for(i=0;i<ns;i++) if(!strcmp(shape[i],w)) break; if(i<ns){cnt[i]++;free(w);} else if(ns<MS){shape[ns]=w;cnt[ns]=1;ns++;} bursts++; if(wn<100000) wlist[wn++]=quiet; wsum+=quiet; int b=0; while((1<<b)<=quiet) b++; waits[b]++; }
        t=last+1; quiet=0; continue; }
      quiet=0; t++; } }
  printf("bursts %ld distinct shapes %d; mean quiet stretch before a burst %.0f; quiet stretches by dyadic length:",bursts,ns,wn?wsum/wn:0); for(int b=0;b<30;b++) if(waits[b]) printf(" <%d:%ld",1<<b,waits[b]); printf("\n");
  static int ord[MS]; for(int i=0;i<ns;i++) ord[i]=i; qsort(ord,ns,sizeof(int),cmpc); long cum=0; for(int i=0;i<ns&&i<12;i++){ cum+=cnt[ord[i]]; printf(" %5ld (cum %.3f) len %4zu %.80s\n",cnt[ord[i]],(double)cum/bursts,strlen(shape[ord[i]]),shape[ord[i]]); } 
  long c10=0; for(int i=0;i<ns&&i<10;i++) c10+=cnt[ord[i]]; printf("top ten shapes cover %.3f\n",bursts?(double)c10/bursts:0); return 0; }
