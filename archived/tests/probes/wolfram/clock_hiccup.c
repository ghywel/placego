// The owner's hiccup in the clock (CL655). Frame: d1_engine.py's physical side. For each W, each start r: the bit-0 trace to TMAX
// and the clock death d0. Hiccups: REM (drop even t_h), WHITE (white at even t_h), BLACK (black at odd t_h). Prints D(W) and the
// per-t_h maxima, and the survivors' black fraction at odd times.
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
typedef unsigned __int128 u128;
#define TMAX 100
static inline u128 pstep(u128 r){ return (r>>1)^(r|(r<<1)); }
int main(int argc,char**argv){ int W=atoi(argv[1]); uint64_t N=1ull<<W, mask=N-1;
  u128 *tr=malloc(N*sizeof(u128)); int *d0=malloc(N*sizeof(int)); int D=0;
  static long surv[TMAX+1], blk[TMAX+1];
  for(uint64_t r=1;r<N;r++){ u128 x=r; u128 t=0; int dd=-1; for(int s=0;s<=TMAX;s++){ if(x&1) t|=((u128)1<<s); if(dd<0&&(s%2==0)&&!(x&1)) dd=s; x=pstep(x);} tr[r]=t; d0[r]=dd<0?TMAX+2:dd; if(d0[r]>D&&d0[r]<=TMAX)D=d0[r]; 
    for(int s=0;s<d0[r]&&s<=TMAX;s++){ surv[s]++; if((t>>s)&1) blk[s]++; } }
  printf("W=%d D(W)=%d\n",W,D);
  // even-white mask: positions of even white times
  u128 evenmask=0; for(int s=0;s<=TMAX;s+=2) evenmask|=((u128)1<<s);
  printf("type t_h D_h  (D_h - D)\n");
  for(int th=0;th<=D+2;th++){
    int Drem=-1,Dwhite=-1,Dblack=-1; long nwhite=0;
    for(uint64_t r=1;r<N;r++){ int dd=d0[r]; u128 t=tr[r];
      if(th%2==0){ // REM and WHITE
        u128 later = (~t) & evenmask & ~(((u128)1<<(th+1))-1); // even white times > th
        int nxt = later? __builtin_ctzll((uint64_t)later) : -1; if(later && (uint64_t)later==0) nxt=-1;
        if(later){ uint64_t lo=(uint64_t)later; if(lo) nxt=__builtin_ctzll(lo); else nxt=64+__builtin_ctzll((uint64_t)(later>>64)); }
        int drem = (dd==th)? (later? nxt: TMAX+2) : dd; if(drem>Drem) Drem=drem;
        if(dd==th){ int dw = later? nxt: TMAX+2; if(dw>Dwhite) Dwhite=dw; nwhite++; }
      } else { int db; if(dd>th){ db = ((t>>th)&1)? dd : th; } else db=dd; if(db>Dblack) Dblack=db; }
    }
    if(th%2==0) printf("REM   %3d %3d  (%+d)   WHITE %3d %3d  (%+d)  [starts selected %ld]\n",th,Drem,Drem-D,th,Dwhite,Dwhite-D,nwhite);
    else printf("BLACK %3d %3d  (%+d)   survivors at t_h %ld, black there %ld (%.3f)\n",th,Dblack,Dblack-D,surv[th],blk[th],surv[th]?(double)blk[th]/surv[th]:0);
  }
  return 0; }
