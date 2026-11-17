/* wall_floors.c (Local, L1532): exact periodic solutions below a wall whose letters repeat WORD, searched for a floor: a solid black column Y_c = all ones with c > 7. Everything above a floor is shielded.
   Columns as in wall_periodic.c. Stops at the first floor on each branch. Usage: ./wall_floors P KMAX CAP [WORD]. Without WORD, runs every primitive-or-not letter word of period exactly dividing P with no BB, no AAA. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef unsigned long long u64;
#define KM 2000
static int P,KMAX; static u64 MASK; static u64 Y[KM]; static long cap,nodes; static int deepest; static long found; static int firstc,lastc; static long hist[KM]; static u64 keep[KM]; static int keepK;
static u64 rotl1(u64 w){ return ((w<<1)|(w>>(P-1)))&MASK; }
static void rec(int K){ if(K>deepest) deepest=K; if(K>=KMAX) return; if(++nodes>cap) return;
  u64 d=rotl1(Y[K-5])^Y[K-2]; u64 m=Y[K-1]; if(m&~d) return; u64 f=d&~m; u64 sub=m;
  for(;;){ Y[K]=f|sub; if(Y[K]==MASK&&K>7&&Y[K-2]==MASK&&Y[K-3]==0&&Y[K-5]==0&&Y[K-6]==MASK&&Y[K-1]==(rotl1(Y[K-4])^MASK)){ found++; hist[K]++; if(!firstc||K<firstc){ firstc=K; memcpy(keep,Y,sizeof(u64)*(K+1)); keepK=K; } if(K>lastc) lastc=K; } else rec(K+1); if(nodes>cap) return; if(sub==0) break; sub=(sub-1)&m; } }
static int run(const char*W){ int n=strlen(W); u64 b=0; for(int t=0;t<P;t++) if(W[t%n]=='B') b|=1ULL<<t; int cst[8]={1,1,0,0,0,1,1,1}; for(int k=0;k<8;k++) Y[k]=cst[k]?MASK:0; Y[8]=b^MASK; Y[9]=b; Y[10]=0; Y[11]=b^MASK;
  for(int K=5;K<=11;K++){ u64 val=Y[K-2]^(Y[K-1]|Y[K]); if(val!=rotl1(Y[K-5])) return -1; }
  nodes=0; deepest=0; found=0; firstc=0; lastc=0; memset(hist,0,sizeof hist); rec(12); return 0; }
int main(int c,char**v){ P=atoi(v[1]); KMAX=atoi(v[2]); cap=atol(v[3]); MASK=(P==64)?~0ULL:((1ULL<<P)-1);
  if(c>4){ int r=run(v[4]); printf("P=%d %s: %s deepest %d nodes %ld%s floors %ld first %d last %d:",P,v[4],r?"BAD":"",deepest,nodes,nodes>cap?" CAPPED":"",found,firstc,lastc); int sh=0; for(int k=0;k<KM&&sh<12;k++) if(hist[k]){ printf(" %d:%ld",k,hist[k]); sh++; } puts(""); return 0; }
  for(u64 w=0;w<(1ULL<<P);w++){ char W[70]; for(int i=0;i<P;i++) W[i]=(w>>i)&1?'B':'A'; W[P]=0; int ok=1,anyB=0; for(int i=0;i<P;i++){ if(W[i]=='B'){ anyB=1; if(W[(i+1)%P]=='B') ok=0; } if(W[i]=='A'&&W[(i+1)%P]=='A'&&W[(i+2)%P]=='A') ok=0; } if(!ok||!anyB) continue; /* canonical rotation: smallest */ int canon=1; for(int r=1;r<P;r++){ u64 x=((w>>r)|(w<<(P-r)))&MASK; if(x<w) canon=0; } if(!canon) continue; { int prim=1; for(int d=1;d<P;d++) if(P%d==0){ u64 x=((w>>d)|(w<<(P-d)))&MASK; if(x==w) prim=0; } if(!prim&&getenv("PRIM")) continue; }
    int r=run(W); printf("P=%d %s: %sdeepest %d nodes %ld%s floors %ld first %d last %d:",P,W,r?"BAD ":"",deepest,nodes,nodes>cap?" CAPPED":"",found,firstc,lastc); int sh=0; for(int k=0;k<KM&&sh<8;k++) if(hist[k]){ printf(" %d:%ld",k,hist[k]); sh++; } puts(""); fflush(stdout); }
  return 0; }
