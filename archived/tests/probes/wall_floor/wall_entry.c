/* wall_smc.c (Local, L1540): the probability that a row is in a closed set at time n, by reversing time. Law: a row with a letter at its wall at time 0, all lower cells independent and fair, rain above. By the count 2*4^n,
   P_n = |U| 2^(10-K) 8^n g(n), where U is the set of K-cell windows and g(n) is the probability that a row with top K cells in U, and fair cells below, has its n forward images all reading letters. g is estimated by sequential Monte Carlo: fresh cells enter at the bottom of y_0, five for each past tick, and each particle keeps only the last three cells of each past row. Usage: ./wall_smc SETFILE N NMAX SEED */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
typedef unsigned char u8; typedef unsigned long long u64;
#define MR 128
typedef struct { u8 c[MR]; } part;  /* c[s]: last three cells of row s, newest in bit 0 */
static u64 rs; static inline u64 rnd(void){ rs^=rs<<13; rs^=rs>>7; rs^=rs<<17; return rs; }
static const u8 FIX[8]={1,1,0,0,0,1,1,1};
/* add cell b to y_0 at offset K; rows s>=1 get cell at K-5s. Returns 0 if a letter fails. b9[s] stores cell 8 of row s for the check at 9. */
static inline int addcell(part*p,int K,int b,u8*m8){ p->c[0]=((p->c[0]<<1)|b)&7; for(int s=1;s<MR;s++){ int k=K-5*s; if(k<0) break; u8 pr=p->c[s-1]; int a=(pr>>2)&1,bb=(pr>>1)&1,cc=pr&1; int v=a^(bb|cc); int old=p->c[s]&1; p->c[s]=((p->c[s]<<1)|v)&7; if(k<8){ if(v!=FIX[k]) return 0; } else if(k==9){ if(v==old) return 0; } else if(k==10){ if(v) return 0; } } return 1; }
typedef struct { part p; } P2;
int main(int c,char**a){ long N=atol(a[2]); int NMAX=atoi(a[3]); rs=strtoull(a[4],0,10)*2654435761ULL+88172645463325252ULL; for(int i=0;i<20;i++) rnd(); static char S[256][800]; int nU=0,K=0; FILE*f=fopen(a[1],"r"); char line[800]; while(fgets(line,800,f)){ int n=strcspn(line,"\n"); line[n]=0; if(!n) continue; strcpy(S[nU++],line); K=n; } fclose(f);
  P2*A=malloc(sizeof(P2)*N),*B=malloc(sizeof(P2)*N); if(!A||!B){ puts("no memory"); return 1; } static P2 base[8192]; int nb=0; long tried=0; for(int i=0;i<nU;i++){ for(int e=0;e<32;e++){ tried++; P2 q; memset(&q,0,sizeof q); int ok=1; static u8 y0[900],y1[900]; for(int k=0;k<K;k++) y0[k]=S[i][K-1-k]=='#'; for(int j=0;j<5;j++) y0[K+j]=(e>>j)&1; for(int k=0;k<K;k++) y1[k]=y0[k+3]^(y0[k+4]|y0[k+5]); int inU=0; for(int r=0;r<nU&&!inU;r++){ int eq=1; for(int k=0;k<K;k++) if(y1[k]!=(S[r][K-1-k]=='#')){ eq=0; break; } if(eq) inU=1; } if(inU) continue; for(int k=0;k<K+5;k++){ if(!addcell(&q.p,k,y0[k],0)){ ok=0; break; } } if(ok) base[nb++]=q; } } printf("set: %d windows of %d cells; extensions tried %ld, with y_1 outside and known past settled %d\n",nU,K,tried,nb); for(long i=0;i<N;i++) A[i]=base[rnd()%nb];
  double lg=log2((double)nb/(double)tried); int Kc=K+5; int n0=(K+5-11+4)/5; double total=0; printf("m log2 e_m e_m cumulative\n");
  for(int n=n0;n<=NMAX;n++){ int target=10+5*n; long alive=0; for(long i=0;i<N;i++){ P2 q=A[i]; int ok=1; for(int k=Kc;k<=target;k++){ int b=rnd()>>63; if(!addcell(&q.p,k,b,0)){ ok=0; break; } } if(ok){ B[alive++]=q; } } if(target>=Kc) Kc=target+1; if(alive==0){ printf("n %d all dead\n",n); break; } double fr=(double)alive/N; lg+=log2(fr); double lp=log2((double)nU)+10-K+3.0*n+lg; total+=exp2(lp); if(1) printf("%d %.3f %.4e %.4e (survival %.4f, 8f %.4f)\n",n,lp,exp2(lp),total,fr,8*fr); fflush(stdout); for(long i=0;i<N;i++) A[i]=B[i<alive?i:rnd()%alive]; }
  return 0; }
