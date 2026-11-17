/* wall_periodic.c (Local, L1530): every solution of the wall-frame rule with time period dividing P below a wall whose letters repeat a given word (backward order).
   Columns Y_k are P-bit words; bit t is the cell at tick t. Rule: Y_k(t) = Y_(k+3)(t+1) ^ (Y_(k+4)(t+1) | Y_(k+5)(t+1)). Known: Y_0..Y_7 constants, Y_8 = not b, Y_9 = b, Y_10 = 0, Y_11 = not b.
   Column K: d(t) = Y_(K-5)(t-1) ^ Y_(K-2)(t). Where Y_(K-1)(t) = 1 need d(t) = 1 and Y_K(t) is free; where it is 0, Y_K(t) = d(t).
   Usage: ./wall_periodic P WORD KMAX CAP. Prints the solutions per offset, and the first column profile found at the deepest level. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
typedef unsigned long long u64;
#define KM 400
static int P, KMAX; static u64 MASK; static u64 Y[KM]; static u64 count[KM]; static long cap, nodes; static int deepest=0; static u64 bestY[KM];
static u64 rotl1(u64 w){ /* (rot w)(t) = w(t-1) */ return ((w<<1)|(w>>(P-1)))&MASK; }
static void rec(int K){ count[K]++; if(K>deepest){deepest=K; memcpy(bestY,Y,sizeof(u64)*K);} if(K>=KMAX) return; if(++nodes>cap) return;
  u64 d=rotl1(Y[K-5])^Y[K-2]; u64 m=Y[K-1];
  if(m&~d) return;            /* a masked tick with d = 0 */
  u64 forced=d&~m; /* where unmasked, Y_K = d */
  /* enumerate subsets of m */
  u64 sub=m; for(;;){ Y[K]=forced|sub; rec(K+1); if(nodes>cap) return; if(sub==0) break; sub=(sub-1)&m; } }
int main(int c,char**v){ P=atoi(v[1]); const char*W=v[2]; KMAX=atoi(v[3]); cap=atol(v[4]); MASK=(P==64)?~0ULL:((1ULL<<P)-1); int n=strlen(W); if(P%n){puts("P must be a multiple of the word length");return 1;}
  u64 b=0; for(int t=0;t<P;t++) if(W[t%n]=='B') b|=1ULL<<t;
  int cst[8]={1,1,0,0,0,1,1,1}; for(int k=0;k<8;k++) Y[k]=cst[k]?MASK:0; Y[8]=b^MASK; Y[9]=b; Y[10]=0; Y[11]=b^MASK;
  /* check the known relations: K from 5 to 11 */
  for(int K=5;K<=11;K++){ u64 d=rotl1(Y[K-5])^Y[K-2]; u64 val=Y[K-2]^(Y[K-1]|Y[K]); if(val!=rotl1(Y[K-5])){ printf("known columns fail at K=%d\n",K); return 1; } }
  rec(12);
  printf("P=%d word %s: solutions by offset:",P,W); for(int K=12;K<=KMAX;K++) if(count[K]) printf(" %d:%llu",K,count[K]); printf("\ndeepest %d nodes %ld%s\n",deepest,nodes,nodes>cap?" CAPPED":"");
  return 0; }
