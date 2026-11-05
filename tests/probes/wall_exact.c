/* wall_exact.c (Local, L1529): the exact factor language of the settled wall, by search on the deepest row. Moving frame, offsets k from the deep cell of the wall pair.
   Forward: y_s(k) = y_(s-1)(k+3) ^ (y_(s-1)(k+4) | y_(s-1)(k+5)). A word w_0 .. w_(L-1) in backward order is attainable iff the row at w_(L-1) has cells below its window
   such that forward steps give the other windows. Any cells below can be completed by a black anchor, so this is the physical language.
   Usage: ./wall_exact LMAX. Prints the count of attainable words by length and the minimal forbidden words. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#define MAXS 40
#define MAXK 260
static signed char y[MAXS][MAXK];
static int L; static const char *W; static long nodes, limit;
static const unsigned char WA[11]={1,1,0,0,0,1,1,1,1,0,0}; /* by offset k = 0..10 */
static const unsigned char WB[11]={1,1,0,0,0,1,1,1,0,1,0};
static int rec(int K){ /* cells y_0(0..K-1) assigned */
  if(++nodes>limit) return -1;
  int Kmax=11+5*(L-1);
  if(K>=Kmax) return 1;
  for(int b=0;b<2;b++){ y[0][K]=b; int ok=1;
    for(int s=1;s<L;s++){ int k=K-5*s; if(k<0) break; y[s][k]=y[s-1][k+3]^(y[s-1][k+4]|y[s-1][k+5]);
      if(k<=10){ const unsigned char *w = W[L-1-s]=='A'?WA:WB; if(y[s][k]!=w[k]){ok=0;break;} } }
    if(ok){ int r=rec(K+1); if(r!=0) return r; } }
  return 0; }
static int attain(const char *w,int n){ L=n; W=w; const unsigned char *t = w[n-1]=='A'?WA:WB; memcpy(y[0],t,11); for(int k=0;k<11;k++) y[0][k]=t[k]; nodes=0;
  /* deep-offset cells of later rows that need only the window */
  for(int s=1;s<L;s++) for(int k=0;k<=10-5*s;k++){ y[s][k]=y[s-1][k+3]^(y[s-1][k+4]|y[s-1][k+5]); const unsigned char *u = W[L-1-s]=='A'?WA:WB; if(y[s][k]!=u[k]) return 0; }
  return rec(11); }
static char *cur[2]; 
int main(int c,char**v){ int LM=atoi(v[1]); limit=c>2?atol(v[2]):200000000L;
  /* breadth by length: keep attainable words; extend on the right by a letter; the word must have both factors attainable */
  char (*A)[MAXS]=malloc(sizeof(char[MAXS])*4000000); long nA=2; strcpy(A[0],"A"); strcpy(A[1],"B"); printf("L=1 attainable 2\n");
  for(int n=2;n<=LM;n++){ char (*N)[MAXS]=malloc(sizeof(char[MAXS])*4000000); long nN=0, forb=0, unk=0; long maxnodes=0;
    /* sorted lookup via a simple hash of words of length n-1 */
    static unsigned char seen[1<<26]; memset(seen,0,sizeof seen);
    for(long i=0;i<nA;i++){ unsigned h=0; for(int j=0;j<n-1;j++) h=(h<<1)|(A[i][j]=='B'); seen[h>>3]|=1<<(h&7); }
    for(long i=0;i<nA;i++) for(int e=0;e<2;e++){ char w[MAXS]; memcpy(w,A[i],n-1); w[n-1]=e?'B':'A'; w[n]=0;
      unsigned h=0; for(int j=1;j<n;j++) h=(h<<1)|(w[j]=='B'); if(!(seen[h>>3]>>(h&7)&1)) continue;
      int r=attain(w,n); if(nodes>maxnodes) maxnodes=nodes;
      if(r==1){ strcpy(N[nN++],w); } else if(r==0){ forb++; printf("  minimal forbidden: %s\n",w); } else { unk++; strcpy(N[nN++],w); printf("  undecided: %s\n",w);} }
    printf("L=%d attainable %ld minimal forbidden %ld undecided %ld max nodes %ld\n",n,nN,forb,unk,maxnodes); fflush(stdout);
    free(A); A=N; nA=nN; }
  return 0; }
