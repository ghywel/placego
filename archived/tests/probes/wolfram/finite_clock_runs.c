// Longest alternating stretch in any column, any start time, of a finite seed's evolution (CL657). Rows 512 bits; T = 200.
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#define NW 8
#define T 200
#define K 12
typedef struct { uint64_t w[NW]; } Row;
static inline int getb(const Row*r,int i){ return (r->w[i>>6]>>(i&63))&1; }
static inline void setb(Row*r,int i){ r->w[i>>6]|=1ull<<(i&63); }
static void step(const Row*a,Row*b){ for(int k=0;k<NW;k++){ uint64_t x=a->w[k]; uint64_t left=(x<<1)|(k?(a->w[k-1]>>63):0); uint64_t right=(x>>1)|(k<NW-1?(a->w[k+1]<<63):0); b->w[k]=left^(x|right); } }
static Row rows[T+1];
int main(int argc,char**argv){ int w=atoi(argv[1]); int off=NW*32;
  int best=0; uint64_t bests=0; int bestp=0,bestt=0; int capped=0;
  for(uint64_t s=1;s<(1ull<<w);s++){ memset(&rows[0],0,sizeof(Row)); for(int i=0;i<w;i++) if((s>>i)&1) setb(&rows[0],off+i);
    for(int t=0;t<T;t++) step(&rows[t],&rows[t+1]);
    for(int p=-K;p<w+K;p++){ int col=off+p; int run=1, start=0; int prev=getb(&rows[0],col);
      for(int t=1;t<=T;t++){ int c=getb(&rows[t],col); if(c!=prev){ run++; } else { if(run>best){best=run;bests=s;bestp=p;bestt=start;} run=1; start=t; } prev=c; }
      if(run>best){best=run;bests=s;bestp=p;bestt=start;} if(run>=T) capped++; } }
  printf("w=%d M(w)=%d seed=0x%llx column=%d start=%d capped=%d  bits: ",w,best,(unsigned long long)bests,bestp,bestt,capped);
  for(int i=0;i<w;i++) printf("%d",(int)((bests>>i)&1)); printf("\n"); return 0; }
