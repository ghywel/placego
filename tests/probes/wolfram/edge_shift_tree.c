// edge_shift_tree.c, Cloud, 2026-11-02 (Block 27, DQ-024): the doubling bit's exact law after 101 as a descent calculus.
// Right diagonals R_j(t) = bit j of Phi^t(a), Phi(x) = x ^ ((x<<1)|(x<<2)), for an odd seed a. Prefix periods L_j by the
// kit's lifting rule (S_rule: L_j = L_(j-1) * (1 + parity of g_j = R_(j-1)|R_(j-2) over L_(j-1))), e_j = log2 L_j,
// d_j = e_j - e_(j-1). For each j the letters d_(j-1), d_(j-2), ... are read backwards and the functional
// F_c(f; P) = sum_{s<P} c(s mod 2^m) f(s) mod 2 is rewritten by three exact moves (pairing at an OR under a doubling
// letter, forcing at a diagonal under a doubling letter, integration at a diagonal under a non-doubling letter), each
// carrying a constant K, until a leaf: FORCED (value K), FREE_G (a 0 at an OR), SMALL_* (a period too small for the
// resolution), DEEP (resolution cap), BOTTOM (below diagonal 0). At every leaf the remaining functional is evaluated by
// one streamed pass and K + F must equal d_j (the exact-identity check). Usage: ./edge_shift_tree SEEDHEX N
#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>
typedef unsigned __int128 u128;
#define MM 14
static inline u128 step(u128 x){ return x ^ ((x<<1)|(x<<2)); }
static inline int bit(u128 x,int i){ return i<0?0:(int)((x>>i)&1); }
int main(int argc,char**argv){
  if(argc<3){fprintf(stderr,"usage: SEEDHEX N\n");return 2;}
  u128 a=strtoull(argv[1],0,0); int N=atoi(argv[2]); if(N>62)N=62;
  uint64_t L[64]; int e[64], d[64];
  L[0]=1; e[0]=0; d[0]=0;
  static unsigned char c[1<<MM], c2[1<<MM];
  printf("# seed=%s N=%d\n",argv[1],N);
  printf("j e_j d_j word leaf m depth K val check\n");
  for(int n=1;n<=N;n++){
    // lifting: parity of g_n over L_(n-1)
    u128 x=a; int par=0; for(uint64_t t=0;t<L[n-1];t++){ par^=bit(x,n-1)|bit(x,n-2); x=step(x); }
    L[n]=L[n-1]*(par?2:1); int ee=0; uint64_t l=L[n]; while(l>1){l>>=1;ee++;} e[n]=ee; d[n]=e[n]-e[n-1];
    int j=n; if(j<3){ printf("%d %d %d - BOTTOM 0 0 0 -1 -1\n",j,e[j],d[j]); continue; }
    // descent
    int level=0; /*0 G,1 R*/ int idx=j; uint64_t P=L[j-1]; int m=0; c[0]=1; int K=0; char word[80]; int wl=0; const char*leaf=0;
    while(1){
      int sz=1<<m; int sumc=0; for(int s=0;s<sz;s++) sumc+=c[s];
      if(level==0){
        if(idx-2<0){leaf="BOTTOM";break;}
        int letter=d[idx-1]; word[wl++]='0'+letter; if(wl>=78){leaf="LONG";break;}
        if(letter==1){ uint64_t half=P/2; if(half%sz){leaf="SMALL_G";break;}
          K^=(int)(((half>>m)*(uint64_t)sumc)&1); level=1; idx=idx-2; P=half; }
        else { leaf="FREE_G"; break; }
      } else {
        if(idx<1){leaf="BOTTOM";break;}
        int letter=d[idx]; word[wl++]='0'+letter; if(wl>=78){leaf="LONG";break;}
        if(letter==1){ uint64_t half=P/2; if(half%sz){leaf="SMALL_R";break;}
          K^=(int)(((half>>m)*(uint64_t)sumc)&1); leaf="FORCED"; break; }
        else { if(P%sz){leaf="SMALL_R";break;} if(m+1>MM){leaf="DEEP";break;}
          int total=(int)(((P>>m)*(uint64_t)sumc)&1); K^=(bit(a,idx)&total);
          int pre=0; for(int u=0;u<2*sz;u++){ pre^=c[u%sz]; c2[u]=(unsigned char)((total^pre)&1); }
          memcpy(c,c2,2*sz); m++; level=0; }
      }
    }
    word[wl]=0;
    // leaf evaluation: K + F_c(object; P)
    int val;
    if(!strcmp(leaf,"FORCED")) val=K;
    else { int sz=1<<m; u128 y=a; int F=0;
      for(uint64_t t=0;t<P;t++){ int f = level==0 ? (bit(y,idx-1)|bit(y,idx-2)) : bit(y,idx); F^=c[t&(sz-1)]&f; y=step(y); }
      val=K^F; }
    printf("%d %d %d %s %s %d %d %d %d %s\n",j,e[j],d[j],word,leaf,m,wl,K,val,val==d[j]?"ok":"FAIL");
    fflush(stdout);
  }
  return 0; }
