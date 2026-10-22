// dscan.c — exact scan of D(n) = max_{m<n}(m+tau(m)) - n for 2 <= n <= N.
// Segmented divisor-count sieve (one core), built-in wall-clock limit.
// Outputs (to stdout): per dyadic block j (n in [2^j, 2^(j+1))): count of n with D(n)=d for d<DCAP,
// min D and argmin; per dyadic block the histogram of tau(m) (for the heuristic model).
// Also logs every n with D(n) <= DLOG to the file given as argv[4].
// usage: dscan N SEG TLIMIT_SEC logfile DLOG histfile
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <math.h>
#include <time.h>

#define DCAP 256
#define TMAX 8192
#define JMAX 48

static uint64_t dh[JMAX][DCAP];      // D histogram per dyadic block of n (D clipped at DCAP-1)
static uint64_t th[JMAX][TMAX];      // tau histogram per dyadic block of m
static uint64_t dmin_v[JMAX], dmin_n[JMAX];

static double now(void){ struct timespec t; clock_gettime(CLOCK_MONOTONIC,&t); return t.tv_sec+1e-9*t.tv_nsec; }

int main(int argc, char **argv){
    if(argc<7){ fprintf(stderr,"usage: dscan N SEG TLIMIT logfile DLOG histfile\n"); return 1; }
    uint64_t N = strtoull(argv[1],0,10);
    uint64_t S = strtoull(argv[2],0,10);
    double TL = atof(argv[3]);
    FILE *lf = fopen(argv[4],"w");
    int DLOG = atoi(argv[5]);
    FILE *hf = fopen(argv[6],"w");
    double t0 = now();
    // primes up to sqrt(N)+1
    uint64_t P = (uint64_t)sqrt((double)N) + 2;
    char *isc = calloc(P+1,1);
    uint32_t *pr = malloc(sizeof(uint32_t)*(P/2+10)); size_t np=0;
    for(uint64_t i=2;i<=P;i++){ if(!isc[i]){ pr[np++]=(uint32_t)i; for(uint64_t j=i*i;j<=P;j+=i) isc[j]=1; } }
    uint64_t *rem = malloc(sizeof(uint64_t)*S);
    uint32_t *tau = malloc(sizeof(uint32_t)*S);
    for(int j=0;j<JMAX;j++){ dmin_v[j]=UINT64_MAX; dmin_n[j]=0; }
    uint64_t R = 0;          // R = max_{m < current n} (m + tau(m)); before m=1, empty -> 0
    uint64_t lastm = 0;      // last m fully processed
    int stopped = 0;
    for(uint64_t L=1; L<=N; L+=S){
        uint64_t H = L+S; if(H>N+1) H=N+1;   // m in [L,H)
        uint64_t len = H-L;
        for(uint64_t i=0;i<len;i++){ uint64_t m=L+i; int e=__builtin_ctzll(m); rem[i]=m>>e; tau[i]=e+1; }
        for(size_t k=1;k<np;k++){
            uint64_t p=pr[k];
            if(p*p >= H) break;
            uint64_t st = ((L + p - 1)/p)*p;
            for(uint64_t m=st; m<H; m+=p){
                uint64_t i=m-L; uint64_t r=rem[i]/p; uint32_t e=1;
                while(r % p == 0){ r/=p; e++; }
                rem[i]=r; tau[i]*= (e+1);
            }
        }
        for(uint64_t i=0;i<len;i++){
            uint64_t m=L+i;
            uint32_t t = tau[i]*(rem[i]>1 ? 2u : 1u);
            int jm = 63-__builtin_clzll(m);
            th[jm][t<TMAX?t:TMAX-1]++;
            uint64_t v = m + t; if(v>R) R=v;
            uint64_t n = m+1;      // R is now max_{m'<n}(m'+tau(m'))
            if(n>=2){
                uint64_t D = R - n;
                int jn = 63-__builtin_clzll(n);
                dh[jn][D<DCAP?D:DCAP-1]++;
                if(D < dmin_v[jn] && n>24){ dmin_v[jn]=D; dmin_n[jn]=n; }
                if((int64_t)D <= DLOG) fprintf(lf,"%llu %llu\n",(unsigned long long)n,(unsigned long long)D);
            }
        }
        lastm = H-1;
        if(now()-t0 > TL){ stopped=1; break; }
    }
    double el = now()-t0;
    printf("# N=%llu processed m<=%llu (n<=%llu) stopped=%d elapsed=%.1fs\n",(unsigned long long)N,(unsigned long long)lastm,(unsigned long long)(lastm+1),stopped,el);
    printf("# block j: n in [2^j,2^(j+1)) ; dmin argmin ; counts D=0..40\n");
    for(int j=1;j<JMAX;j++){
        uint64_t tot=0; for(int d=0;d<DCAP;d++) tot+=dh[j][d];
        if(!tot) continue;
        printf("B %d %llu %llu %llu :", j,(unsigned long long)tot,(unsigned long long)dmin_v[j],(unsigned long long)dmin_n[j]);
        for(int d=0; d<=40; d++) printf(" %llu",(unsigned long long)dh[j][d]);
        printf("\n");
    }
    // tau histograms
    for(int j=0;j<JMAX;j++){
        uint64_t tot=0; for(int t=0;t<TMAX;t++) tot+=th[j][t];
        if(!tot) continue;
        fprintf(hf,"T %d %llu",j,(unsigned long long)tot);
        for(int t=0;t<TMAX;t++) if(th[j][t]) fprintf(hf," %d:%llu",t,(unsigned long long)th[j][t]);
        fprintf(hf,"\n");
    }
    // full D histogram (all d) per block for later
    for(int j=1;j<JMAX;j++){
        uint64_t tot=0; for(int d=0;d<DCAP;d++) tot+=dh[j][d];
        if(!tot) continue;
        fprintf(hf,"D %d %llu",j,(unsigned long long)tot);
        for(int d=0;d<DCAP;d++) if(dh[j][d]) fprintf(hf," %d:%llu",d,(unsigned long long)dh[j][d]);
        fprintf(hf,"\n");
    }
    fclose(lf); fclose(hf);
    return 0;
}
