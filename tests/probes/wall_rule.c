/* wall_rule.c (Local, L1529): the run structure of the letters. x = BA, y = BAA. Sequences read x^a1 y^b1 x^a2 y^b2 ...  Tables of the pairs (b_i, a_(i+1)) and (a_i, b_i), interior runs only.
   Usage: ./wall_rule ROWS TICKS LOW SEED */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
typedef unsigned long long u64;
#define MAXB 12000
#define M 40
static u64 s[2];
static inline u64 rotl(u64 x,int k){return (x<<k)|(x>>(64-k));}
static u64 rnd(void){u64 a=s[0],b=s[1],r=a+b;b^=a;s[0]=rotl(a,24)^b^(b<<16);s[1]=rotl(b,37);return r;}
static const unsigned char WA[11]={0,0,1,1,1,1,0,0,0,1,1}, WB[11]={0,1,0,1,1,1,0,0,0,1,1};
static long ba[M][M], ab[M][M];
int main(int c,char**v){ long rows=atol(v[1]); int ticks=atoi(v[2]), low=atoi(v[3]); s[0]=0x9E3779B97F4A7C15ULL^atol(v[4]); s[1]=0xBF58476D1CE4E5B9ULL; for(int i=0;i<20;i++)rnd();
  static unsigned char x[MAXB],z[MAXB]; static char seq[8192]; static char blk[8192]; int n=low+3*ticks+40;
  for(long r=0;r<rows;r++){ x[0]=1; for(int j=1;j<low;j++) x[j]=rnd()&1; { int b=x[low-1]; for(int j=low;j<n;j++){b^=1;x[j]=b;} }
    int len=0; 
    for(int t=0;t<ticks;t++){ int top=n-3; while(top>=1 && x[top]!=x[top+1]) top--;
      if(top>=10){ if(!memcmp(x+top-9,WA,11)) seq[len++]='A'; else if(!memcmp(x+top-9,WB,11)) seq[len++]='B'; }
      int p1=1,p2=0; z[0]=1; for(int j=1;j<n;j++){ int o=x[j]^(p1|p2); z[j]=o; p2=p1; p1=o; } memcpy(x,z,n); }
    /* blocks */
    int i=0,nb=0; while(i<len&&seq[i]!='B') i++;
    while(i<len){ int j=i+1; while(j<len&&seq[j]=='A') j++; if(j>=len) break; blk[nb++]= (j-i-1==1)?'x':'y'; i=j; }
    /* runs */
    int runs[4096],typ[4096],nr=0; for(int a=0;a<nb;){ int b=a; while(b<nb&&blk[b]==blk[a]) b++; runs[nr]=b-a; typ[nr]=blk[a]; nr++; a=b; }
    for(int k=1;k+2<nr;k++){ int p=runs[k]<M?runs[k]:M-1, q=runs[k+1]<M?runs[k+1]:M-1; if(typ[k]=='y') ba[p][q]++; else ab[p][q]++; } }
  printf("rows: y-run b, then the next x-run a; columns a = 1..24\n     "); for(int a=1;a<=24;a++) printf("%7d",a); printf("\n");
  for(int b=1;b<=12;b++){ printf("b=%2d ",b); for(int a=1;a<=24;a++) printf("%7ld",ba[b][a]); printf("\n"); }
  printf("rows: x-run a, then the next y-run b; columns b = 1..12\n     "); for(int b=1;b<=12;b++) printf("%7d",b); printf("\n");
  for(int a=1;a<=24;a++){ printf("a=%2d ",a); for(int b=1;b<=12;b++) printf("%7ld",ab[a][b]); printf("\n"); }
  return 0; }
