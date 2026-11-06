// Settling ticks tau_g(Y): least tick from which the top g wheels are on their cycle. Output theta_g = tau_g + width at listed g.
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
typedef uint64_t u;
static u *A,*B,*V,*N,*SN,*V0,*CY;
int main(int c,char**a){ long K=atol(a[1]); int nl=c-2; long *lv=malloc(sizeof(long)*nl); for(int i=0;i<nl;i++) lv[i]=atol(a[2+i]);
  long RW=(K+128)/64+4, VW=(K+63)/64+2; A=calloc(RW,8);B=calloc(RW,8);V=calloc(VW,8);N=calloc(VW,8);SN=calloc(VW,8);V0=calloc(VW,8);CY=calloc(VW*64,8);
  u top=(K%64)?((1ULL<<(K%64))-1):~0ULL; long vw=(K+63)/64; char line[256];
  #define LSTEP() do{ u p1=0,p2=0; for(long i=0;i<vw;i++){ u v=V[i]; u s1=(v<<1)|p1,s2=(v<<2)|p2; N[i]=s2^(s1|v); p1=v>>63; p2=v>>62; } N[vw-1]&=top; u*T=V;V=N;N=T; }while(0)
  while(fgets(line,sizeof line,stdin)){ u y0=strtoull(line,0,10); if(!y0) continue; memset(A,0,RW*8);memset(B,0,RW*8);A[0]=y0; int W=64-__builtin_clzll(y0); long t=0,w=W;
    while(w<K){ long n=w/64+2; u prev=0; for(long i=0;i<n;i++){ u y=A[i],nx=A[i+1]; B[i]=((y>>1)|(nx<<63))^(y|((y<<1)|prev)); prev=y>>63; } u*T=A;A=B;B=T; t++; w++; }
    memset(V,0,VW*8); for(long j=0;j<K;j++){ long p=w-1-j; if((A[p>>6]>>(p&63))&1) V[j>>6]|=1ULL<<(j&63); }
    memcpy(V0,V,VW*8); long t0=t; memcpy(SN,V,VW*8); int done=0;
    while(!done){ for(int s=0;s<64;s++){ LSTEP(); t++; } if(memcmp(V,SN,vw*8)==0) done=1; else memcpy(SN,V,VW*8); }
    long tc=t; for(int s=0;s<64;s++){ memcpy(CY+s*VW,V,VW*8); LSTEP(); }   // CY[s] = state at tick tc + s
    memcpy(V,V0,VW*8); long tt=t0; long f=0; int li=0; long *tau=calloc(nl,sizeof(long));
    while(li<nl){ long s=((tt-tc)%64+64)%64; u*C=CY+s*VW; long wi=f>>6; while(wi<vw && V[wi]==C[wi]) wi++; long nf=(wi>=vw)?K:wi*64+__builtin_ctzll(V[wi]^C[wi]); if(nf>K) nf=K; if(nf<f) nf=f; f=nf;
      while(li<nl && f>=lv[li]){ tau[li]=tt; li++; } if(li>=nl) break; LSTEP(); tt++; }
    printf("%llu %d",(unsigned long long)y0,W); for(int i=0;i<nl;i++) printf(" %ld",tau[i]+W); printf("\n"); fflush(stdout); free(tau); }
  return 0; }
