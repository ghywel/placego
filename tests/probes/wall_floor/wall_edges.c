/* wall_edges.c (Local, L1538): which edges of the free graph at width W are real? For each edge v -> u of E(W), search for an actual row y_0 with top W cells u, whose forward image y_1 has top W cells v, and whose past rows read letters for L ticks. Exhaustive when it says dead.
   Usage: ./wall_edges W L NODECAP < E<W>.txt ; writes edges with verdicts to stdout: i j verdict. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef unsigned __int128 u128;
#define MS 48
#define MK 320
static signed char y[MS][MK]; static signed char vv[MK]; static int W,L; static long nodes,cap; static int best;
static const unsigned char FIX[8]={1,1,0,0,0,1,1,1};
static inline int okcell(int s,int k){ if(k<8) return y[s][k]==FIX[k]; if(k==9) return y[s][9]!=y[s][8]; if(k==10) return y[s][10]==0; return 1; }
static int rec(int K){ if(++nodes>cap) return -1; int done=(K-1-10)/5; if(done>best) best=done; if(done>=L) return 1;
  for(int b=0;b<2;b++){ y[0][K]=b; int ok=1; for(int s=1;s<=L;s++){ int k=K-5*s; if(k<0) break; y[s][k]=y[s-1][k+3]^(y[s-1][k+4]|y[s-1][k+5]); if(s==1&&k<W&&y[1][k]!=vv[k]){ ok=0; break; } if(k<=10&&!okcell(s,k)){ ok=0; break; } }
    if(ok){ int r=rec(K+1); if(r) return r; } }
  return 0; }
static int cell(u128 x,int k){ return (int)((x>>(W-1-k))&1); }
int main(int c,char**a){ W=atoi(a[1]); L=atoi(a[2]); cap=atol(a[3]); static u128 V[1<<20]; static int adj[1<<20][4]; static int part[1<<20],term[1<<20]; long n=0; char hx[40]; int p,t,cy,e0,e1,e2,e3; while(scanf("%32s %d %d %d %d %d %d %d",hx,&p,&t,&cy,&e0,&e1,&e2,&e3)==8){ u128 v=0; for(int i=0;i<32;i++){ int d=hx[i]<='9'?hx[i]-'0':hx[i]-'a'+10; v=(v<<4)|d; } V[n]=v; part[n]=p; term[n]=t; adj[n][0]=e0; adj[n][1]=e1; adj[n][2]=e2; adj[n][3]=e3; n++; }
  long real=0,dead=0,capped=0,tot=0; for(long i=0;i<n;i++){ int seen[4],ns=0; for(int s=0;s<4;s++){ int j=adj[i][s],dup=0; for(int q=0;q<ns;q++) if(seen[q]==j) dup=1; if(dup) continue; seen[ns++]=j; tot++; memset(y,0,sizeof y); for(int k=0;k<W;k++){ y[0][k]=cell(V[j],k); vv[k]=cell(V[i],k); } int ok=1; for(int r=1;r<=L&&ok;r++) for(int k=0;k<=W-1-5*r;k++){ y[r][k]=y[r-1][k+3]^(y[r-1][k+4]|y[r-1][k+5]); if(r==1&&y[1][k]!=vv[k]){ ok=0; break; } if(k<=10&&!okcell(r,k)){ ok=0; break; } } nodes=0; best=0; int res=ok?rec(W):0; if(res==1) real++; else if(res==0) dead++; else capped++; printf("%ld %d %d %d\n",i,j,res,best); } fflush(stdout); }
  fprintf(stderr,"W %d L %d: edges %ld real %ld dead %ld capped %ld\n",W,L,tot,real,dead,capped); return 0; }
