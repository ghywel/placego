/* wall_cols.c (Local, L1530): columns of the strip below the wall on quiet stretches. For rows with letters of period 3 on ticks [T0, T0 + Q), the time word of each offset k < KM:
   its least period on that window; then, against the first such row, the largest K such that some time shift makes all columns below K agree. Usage: ./wall_cols ROWS T0 Q LOW SEED */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
typedef unsigned long long u64;
#define MAXB 30000
#define KM 256
static u64 s[2];
static inline u64 rotl(u64 x,int k){return (x<<k)|(x>>(64-k));}
static u64 rnd(void){u64 a=s[0],b=s[1],r=a+b;b^=a;s[0]=rotl(a,24)^b^(b<<16);s[1]=rotl(b,37);return r;}
static const unsigned char WA[11]={0,0,1,1,1,1,0,0,0,1,1}, WB[11]={0,1,0,1,1,1,0,0,0,1,1};
int main(int c,char**v){ long rows=atol(v[1]); int T0=atoi(v[2]), Q=atoi(v[3]), low=atoi(v[4]); s[0]=0x9E3779B97F4A7C15ULL^atol(v[5]); s[1]=0xBF58476D1CE4E5B9ULL; for(int i=0;i<20;i++)rnd();
  int ticks=T0+Q; int n=low+3*ticks+40; if(n>=MAXB){puts("too long");return 1;}
  unsigned char (*C)[KM]=malloc((size_t)Q*KM), (*R)[KM]=malloc((size_t)Q*KM); static unsigned char x[MAXB],z[MAXB]; static char seq[12000];
  int have=0; long used=0; long kh[12]={0}; int perhist[KM][14]; memset(perhist,0,sizeof perhist); int Rphase=0;
  for(long r=0;r<rows;r++){ x[0]=1; for(int j=1;j<low;j++) x[j]=rnd()&1; { int b=x[low-1]; for(int j=low;j<n;j++){b^=1;x[j]=b;} }
    int top=-1;
    for(int t=0;t<ticks;t++){ if(top<0){ int k=n-3; while(k>=1 && x[k]!=x[k+1]) k--; if(k>=10&&(!memcmp(x+k-9,WA,11)||!memcmp(x+k-9,WB,11))) top=k; } else top+=3;
      char ch='?'; if(top>=0){ if(!memcmp(x+top-9,WA,11)) ch='A'; else if(!memcmp(x+top-9,WB,11)) ch='B'; }
      seq[t]=ch; if(t>=T0 && top>KM) for(int k=0;k<KM;k++) C[t-T0][k]=x[top+1-k];
      int p1=1,p2=0; z[0]=1; for(int j=1;j<n;j++){ int o=x[j]^(p1|p2); z[j]=o; p2=p1; p1=o; } memcpy(x,z,n); }
    int ok=1; for(int t=T0+3;t<ticks;t++) if(seq[t]!=seq[t-3]) ok=0; if(!ok) continue; used++;
    /* least period of each column on the window */
    int per[KM]; for(int k=0;k<KM;k++){ per[k]=0; for(int p=1;p<=Q/2;p++){ int g=1; for(int t=0;t+p<Q;t++) if(C[t][k]!=C[t+p][k]){g=0;break;} if(g){per[k]=p;break;} }
      int cls=13; if(per[k]){ int q=per[k]; if(q%3==0){ q/=3; int m=0; while(q%2==0){q/=2;m++;} if(q==1) cls=m; else cls=12; } else cls=12; } perhist[k][cls]++; }
    if(used<=4){ printf("row %ld column periods:",r); int last=-1; for(int k=0;k<KM;k++) if(per[k]!=last){ printf(" k%d:%d",k,per[k]); last=per[k]; } printf("\n"); }
    if(!have){ memcpy(R,C,(size_t)Q*KM); have=1; continue; }
    /* the best time shift: first compare with shifts up to Q/2 */
    int best=0,bs=0; for(int sft=0;sft<Q/2;sft++){ int K=KM; for(int t=0;t+sft<Q&&K>0;t++){ int k=0; while(k<K&&C[t+sft][k]==R[t][k]) k++; if(k<K) K=k; } if(K>best){best=K;bs=sft;} }
    int b=0; while((1<<b)<=best) b++; kh[b]++; if(used<=14) printf("row %ld best common strip %d cells at shift %d\n",r,best,bs); }
  printf("quiet rows %ld of %ld on ticks [%d,%d)\n",used,rows,T0,T0+Q);
  printf("common strip with the first row, by dyadic length:"); for(int b=0;b<12;b++) if(kh[b]) printf(" <%d:%ld",1<<b,kh[b]); printf("\n");
  printf("offset: classes of column period (m for 3*2^m, o other, n none)\n"); for(int k=0;k<KM;k+=8){ printf(" k=%3d",k); for(int q=0;q<14;q++) if(perhist[k][q]) { if(q<12) printf(" m%d:%d",q,perhist[k][q]); else if(q==12) printf(" o:%d",perhist[k][q]); else printf(" n:%d",perhist[k][q]); } printf("\n"); }
  return 0; }
