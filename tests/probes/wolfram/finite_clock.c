// Finite seeds of width w, clock column at position p: lifetime of an alternating column from time 0 (either phase). CL656.
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#define NW 8            // 512-bit rows
#define TCAP 160
typedef struct { uint64_t w[NW]; } Row;
static inline int getb(const Row*r,int i){ return (r->w[i>>6]>>(i&63))&1; }
static inline void setb(Row*r,int i){ r->w[i>>6]|=1ull<<(i&63); }
static void step(const Row*a,Row*b){ // b_i = a_{i-1} xor (a_i or a_{i+1})
  for(int k=0;k<NW;k++){ uint64_t x=a->w[k]; uint64_t left=(x<<1)|(k?(a->w[k-1]>>63):0); uint64_t right=(x>>1)|(k<NW-1?(a->w[k+1]<<63):0); b->w[k]=left^(x|right); } }
int main(int argc,char**argv){ int w=atoi(argv[1]); int off=NW*32; // seed placed at bits off..off+w-1
  int best=-1; uint64_t bests=0; int bestp=-1; int bestD=0; long count_cap=0; static int byp[64];
  for(uint64_t s=1;s<(1ull<<w);s++){ for(int p=0;p<w;p++){ Row a,b; memset(&a,0,sizeof a); for(int i=0;i<w;i++) if((s>>i)&1) setb(&a,off+i);
      int col=off+p; int ph=getb(&a,col); int t=0; for(t=0;t<TCAP;t++){ if(getb(&a,col)!=((ph+t)&1)) break; step(&a,&b); a=b; }
      if(t>=TCAP) count_cap++;
      if(t>best){best=t;bests=s;bestp=p;} if(t>byp[p]) byp[p]=t; } }
  printf("w=%d L(w)=%d seed=0x%llx p=%d capped=%ld  by position:",w,best,(unsigned long long)bests,bestp,count_cap);
  for(int p=0;p<w;p++) printf(" %d",byp[p]); printf("\n"); // print the maximizer's row
  printf("  maximizer bits (left to right): "); for(int i=0;i<w;i++) printf("%d",(int)((bests>>i)&1)); printf("  column at %d\n",bestp);
  return 0; }
