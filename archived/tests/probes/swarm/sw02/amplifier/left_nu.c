// nu_K(Y): evolve Y under F until width >= K, read the top K cells inward, iterate L until periodic, step to L^-(t+W).
// Prints hashes of nu mod 2^K' for each listed level K'. Rows on stdin as decimal. Exact bit arithmetic.
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
typedef uint64_t u;
static u *A,*B,*V,*N,*SN;
static inline int width(u*y,long n){ for(long i=n-1;i>=0;i--) if(y[i]){ return i*64+64-__builtin_clzll(y[i]); } return 0; }
static u hashlvl(u*v,long Kl){ long n=(Kl+63)/64; u h=1469598103934665603ULL; for(long i=0;i<n;i++){ u w=v[i]; if(i==n-1&&Kl%64) w&=(1ULL<<(Kl%64))-1; h^=w; h*=1099511628211ULL; h^=h>>29; } return h; }
int main(int c,char**a){ long K=atol(a[1]); int nl=c-2; long *lv=malloc(sizeof(long)*(nl+1)); for(int i=0;i<nl;i++) lv[i]=atol(a[2+i]);
  long RW=(K+128)/64+4, VW=(K+63)/64+2; A=calloc(RW,8);B=calloc(RW,8);V=calloc(VW,8);N=calloc(VW,8);SN=calloc(VW,8);
  u top= (K%64)?((1ULL<<(K%64))-1):~0ULL; long vw=(K+63)/64; char line[256];
  while(fgets(line,sizeof line,stdin)){ u y0=strtoull(line,0,10); if(!y0) continue; memset(A,0,RW*8); memset(B,0,RW*8); A[0]=y0; int W=64-__builtin_clzll(y0); long t=0; long w=W;
    while(w<K){ long n=w/64+2; u prev=0; for(long i=0;i<n;i++){ u y=A[i],nx=A[i+1]; B[i]=((y>>1)|(nx<<63))^(y|((y<<1)|prev)); prev=y>>63; } u*T=A;A=B;B=T; t++; w++; }
    memset(V,0,VW*8); for(long j=0;j<K;j++){ long p=w-1-j; if((A[p>>6]>>(p&63))&1) V[j>>6]|=1ULL<<(j&63); }
    memcpy(SN,V,VW*8); long steps=0; int done=0;
    while(!done){ for(int s=0;s<64;s++){ u p1=0,p2=0; for(long i=0;i<vw;i++){ u v=V[i]; u s1=(v<<1)|p1, s2=(v<<2)|p2; N[i]=s2^(s1|v); p1=v>>63; p2=v>>62; } N[vw-1]&=top; u*T=V;V=N;N=T; t++; steps++; }
      if(memcmp(V,SN,vw*8)==0) done=1; else memcpy(SN,V,VW*8); }
    long m=(64-((t+W)%64))%64; for(long s=0;s<m;s++){ u p1=0,p2=0; for(long i=0;i<vw;i++){ u v=V[i]; u s1=(v<<1)|p1, s2=(v<<2)|p2; N[i]=s2^(s1|v); p1=v>>63; p2=v>>62; } N[vw-1]&=top; u*T=V;V=N;N=T; }
    printf("%llu %d %ld",(unsigned long long)y0,W,t); for(int i=0;i<nl;i++) printf(" %016llx",(unsigned long long)hashlvl(V,lv[i])); printf("\n"); fflush(stdout); }
  return 0; }
