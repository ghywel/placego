// smodel.c — test heuristic models for P(D(n) <= delta) on a window of n.
// Window: n in [X, X+W). Needs tau(m) for m in [X-K, X+W), K >= max tau (exact, since m+tau(m) < n for m < n-K).
// For each m we also record ts_y(m) = tau(y-smooth part of m) for y in YS.
// Models, per delta:
//  IND : prod_{k=1..K} F(k+delta), F = law of tau(m) over the window (same for every n).
//  SEMI_y : prod_{k=1..K} G_y( floor((k+delta)/ts_y(n-k)) ), G_y = law of tau(y-rough part) over the window;
//           the y-smooth parts of n-k are taken EXACTLY from n (deterministic), the rough parts as independent.
// Observed: #{n in window : D(n) <= delta}, D computed exactly.
// usage: smodel X W K TLIMIT
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <math.h>
#include <time.h>
static double now(void){ struct timespec t; clock_gettime(CLOCK_MONOTONIC,&t); return t.tv_sec+1e-9*t.tv_nsec; }
#define NY 3
static const uint32_t YS[NY] = {7, 31, 211};
#define ND 5
static const int DS[ND] = {6, 8, 10, 12, 14};
#define TM 16384
int main(int argc, char **argv){
    uint64_t X = strtoull(argv[1],0,10), W = strtoull(argv[2],0,10), K = strtoull(argv[3],0,10);
    double TL = atof(argv[4]); double t0 = now();
    uint64_t L = X - K, H = X + W; uint64_t len = H - L;
    uint64_t P = (uint64_t)sqrt((double)H) + 2;
    char *isc = calloc(P+1,1); uint32_t *pr = malloc(sizeof(uint32_t)*(P/2+10)); size_t np=0;
    for(uint64_t i=2;i<=P;i++){ if(!isc[i]){ pr[np++]=(uint32_t)i; for(uint64_t j=i*i;j<=P;j+=i) isc[j]=1; } }
    uint64_t *rem = malloc(8*len); uint32_t *tau = malloc(4*len);
    uint16_t *ts[NY]; for(int y=0;y<NY;y++){ ts[y]=malloc(2*len); }
    for(uint64_t i=0;i<len;i++){ uint64_t m=L+i; int e=__builtin_ctzll(m); rem[i]=m>>e; tau[i]=e+1; for(int y=0;y<NY;y++) ts[y][i]=e+1; }
    for(size_t k=1;k<np;k++){
        uint64_t p=pr[k]; if(p*p>=H) break;
        uint64_t st=((L+p-1)/p)*p;
        for(uint64_t m=st;m<H;m+=p){ uint64_t i=m-L; uint64_t r=rem[i]/p; uint32_t e=1; while(r%p==0){r/=p;e++;} rem[i]=r; tau[i]*=(e+1);
            for(int y=0;y<NY;y++) if(p<=YS[y]) ts[y][i]*=(e+1); }
    }
    uint32_t tmax=0;
    for(uint64_t i=0;i<len;i++){ if(rem[i]>1) tau[i]*=2; if(tau[i]>tmax) tmax=tau[i]; }
    if(tmax > K){ fprintf(stderr,"K=%llu < max tau %u\n",(unsigned long long)K,tmax); }
    // laws over the window part [X, X+W) (m values)
    static double F[TM], G[NY][TM];
    for(uint64_t i=K;i<len;i++){ uint32_t t=tau[i]; F[t<TM?t:TM-1]+=1; for(int y=0;y<NY;y++){ uint32_t r=tau[i]/ts[y][i]; G[y][r<TM?r:TM-1]+=1; } }
    double c=0; for(int t=0;t<TM;t++){ c+=F[t]; F[t]=c/W; }
    for(int y=0;y<NY;y++){ c=0; for(int t=0;t<TM;t++){ c+=G[y][t]; G[y][t]=c/W; } }
    static double lF[TM], lG[NY][TM];
    for(int t=0;t<TM;t++){ lF[t]= F[t]>0? log(F[t]) : -1e300; for(int y=0;y<NY;y++) lG[y][t]= G[y][t]>0? log(G[y][t]) : -1e300; }
    // IND prediction (same for every n)
    double ind[ND];
    for(int d=0;d<ND;d++){ double s=0; for(uint64_t k=1;k<=K;k++){ uint64_t t=k+DS[d]; if(t>=TM) t=TM-1; s+=lF[t]; } ind[d]=W*exp(s); }
    // observed + SEMI
    double semi[NY][ND]; memset(semi,0,sizeof semi); uint64_t obs[ND]={0};
    uint64_t done=0;
    for(uint64_t i=K;i<len;i++){
        uint64_t n=L+i; // need max over m in [n-K, n-1] of m+tau(m)
        uint64_t R=0; for(uint64_t k=1;k<=K;k++){ uint64_t v=(n-k)+tau[i-k]; if(v>R) R=v; }
        int64_t D=(int64_t)(R-n);
        for(int d=0;d<ND;d++) if(D<=DS[d]) obs[d]++;
        for(int y=0;y<NY;y++){
            for(int d=0;d<ND;d++){
                double s=0; uint16_t *T=ts[y]; double *lg=lG[y];
                for(uint64_t k=1;k<=K;k++){ uint64_t q=(k+DS[d])/T[i-k]; if(q>=TM) q=TM-1; s+=lg[q]; if(s<-700) break; }
                semi[y][d]+=exp(s);
            }
        }
        done++;
        if((done & 4095)==0 && now()-t0>TL) break;
    }
    printf("X=%llu W=%llu K=%llu maxtau=%u n_done=%llu elapsed=%.1f\n",(unsigned long long)X,(unsigned long long)W,(unsigned long long)K,tmax,(unsigned long long)done,now()-t0);
    double sc = (double)done/W;
    for(int d=0;d<ND;d++){
        printf("delta=%d obs=%llu IND=%.4g",DS[d],(unsigned long long)obs[d],ind[d]*sc);
        for(int y=0;y<NY;y++) printf(" SEMI_y%u=%.4g",YS[y],semi[y][d]);
        printf("\n");
    }
    return 0;
}
