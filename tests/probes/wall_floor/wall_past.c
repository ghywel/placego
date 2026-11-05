/* wall_past.c (Local, L1536): can a row step into a set of windows from outside it, after a long settled past? Exact, on rows: the row inside the set is y_0, its past rows follow by the forward rule y_s(k) = y_(s-1)(k+3) ^ (y_(s-1)(k+4) | y_(s-1)(k+5)), and search runs over the cells of y_0 below the window.
   Conditions: y_1's top w cells are not in the set; every past row reads a letter at its wall. Reports for each window the longest settled past found, up to L.
   Usage: ./wall_past SETFILE W L NODECAP : SETFILE holds words low..high, cut to their top W cells. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MS 140
#define MK 900
static signed char y[MS][MK]; static int W,L; static long nodes,cap; static int best; static char T[256][700]; static int nT;
static const unsigned char FIX[8]={1,1,0,0,0,1,1,1};
static inline int okcell(int s,int k){ if(k<8) return y[s][k]==FIX[k]; if(k==9) return y[s][9]!=y[s][8]; if(k==10) return y[s][10]==0; return 1; }
static int inT(void){ for(int i=0;i<nT;i++){ int eq=1; for(int k=0;k<W;k++) if(y[1][k]!=(T[i][W-1-k]=='#')){ eq=0; break; } if(eq) return 1; } return 0; }
static int rec(int K){ if(++nodes>cap) return -1; /* rows up to s are complete at offset 10 when K-1-5s >= 10 */ int done=(K-1-10)/5; if(done>best) best=done; if(done>=L) return 1;
  for(int b=0;b<2;b++){ y[0][K]=b; int ok=1; for(int s=1;s<=L;s++){ int k=K-5*s; if(k<0) break; y[s][k]=y[s-1][k+3]^(y[s-1][k+4]|y[s-1][k+5]); if(k<=10&&!okcell(s,k)){ ok=0; break; } }
    if(ok&&K==W+4&&inT()) ok=0; if(ok){ int r=rec(K+1); if(r) return r; } }
  return 0; }
int main(int c,char**a){ W=atoi(a[2]); L=atoi(a[3]); cap=atol(a[4]); char line[800]; FILE*f=fopen(a[1],"r"); while(fgets(line,800,f)){ int n=strcspn(line,"\n"); line[n]=0; if(!n) continue; char*p=line+n-W; int dup=0; for(int i=0;i<nT;i++) if(!strncmp(T[i],p,W)) dup=1; if(!dup){ strncpy(T[nT],p,W); nT++; } } fclose(f); printf("w %d: %d windows, target past %d\n",W,nT,L);
  int hist[MS+1]; memset(hist,0,sizeof hist); int capped=0,reach=0; for(int i=0;i<nT;i++){ memset(y,0,sizeof y); for(int k=0;k<W;k++) y[0][k]=T[i][W-1-k]=='#'; int ok=1; for(int s=1;s<=L&&ok;s++) for(int k=0;k<=W-1-5*s;k++){ y[s][k]=y[s-1][k+3]^(y[s-1][k+4]|y[s-1][k+5]); if(k<=10&&!okcell(s,k)){ ok=0; break; } } nodes=0; best=0; int r=ok?rec(W):0; if(r==1) reach++; else if(r<0) capped++; hist[best>MS?MS:best]++; printf(" window %d: %s, best past %d, nodes %ld\n",i,r==1?"REACHES":r<0?"capped":"dead",best,nodes); }
  printf("reached %d capped %d of %d\n",reach,capped,nT); return 0; }
