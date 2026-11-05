/* wall_layer.c (Local, L1530): is the ordered layer below the wall of fixed size, or does it grow with time? Rate at which y_t(k) differs from y_(t+3)(k), over all rows, in dyadic time windows, by offset.
   Usage: ./wall_layer ROWS TICKS LOW SEED */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
typedef unsigned long long u64;
#define MAXB 30000
#define KM 512
static u64 s[2];
static inline u64 rotl(u64 x,int k){return (x<<k)|(x>>(64-k));}
static u64 rnd(void){u64 a=s[0],b=s[1],r=a+b;b^=a;s[0]=rotl(a,24)^b^(b<<16);s[1]=rotl(b,37);return r;}
static const unsigned char WA[11]={0,0,1,1,1,1,0,0,0,1,1}, WB[11]={0,1,0,1,1,1,0,0,0,1,1};
static long D[16][KM], N[16];
int main(int c,char**v){ long rows=atol(v[1]); int ticks=atoi(v[2]), low=atoi(v[3]); s[0]=0x9E3779B97F4A7C15ULL^atol(v[4]); s[1]=0xBF58476D1CE4E5B9ULL; for(int i=0;i<20;i++)rnd();
  int n=low+3*ticks+40; if(n>=MAXB) return 1; static unsigned char x[MAXB],z[MAXB]; static unsigned char H[4][KM];
  for(long r=0;r<rows;r++){ x[0]=1; for(int j=1;j<low;j++) x[j]=rnd()&1; { int b=x[low-1]; for(int j=low;j<n;j++){b^=1;x[j]=b;} }
    int top=-1,have=0;
    for(int t=0;t<ticks;t++){ if(top<0){ int k=n-3; while(k>=1 && x[k]!=x[k+1]) k--; if(k>=10&&(!memcmp(x+k-9,WA,11)||!memcmp(x+k-9,WB,11))) top=k; } else top+=3;
      if(top>KM+2){ unsigned char *cur=H[t&3]; for(int k=0;k<KM;k++) cur[k]=x[top+1-k]; have++;
        if(have>3){ unsigned char *old=H[(t+1)&3]; /* t-3 */ int b=0; while((1<<b)<=t) b++; N[b]++; for(int k=0;k<KM;k++) D[b][k]+=cur[k]!=old[k]; } }
      int p1=1,p2=0; z[0]=1; for(int j=1;j<n;j++){ int o=x[j]^(p1|p2); z[j]=o; p2=p1; p1=o; } memcpy(x,z,n); } }
  int ks[]={20,24,28,32,40,48,56,64,80,96,128,160,200,256,320,400,500};
  printf("rate of y_t(k) != y_(t+3)(k); columns are offsets\n ticks        "); for(unsigned i=0;i<sizeof ks/sizeof ks[0];i++) printf("%6d",ks[i]); printf("\n");
  for(int b=8;b<16;b++) if(N[b]){ printf("[%5d,%5d)",1<<(b-1),1<<b); for(unsigned i=0;i<sizeof ks/sizeof ks[0];i++) printf(" %.3f",(double)D[b][ks[i]]/N[b]); printf("\n"); }
  return 0; }
