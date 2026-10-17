// B159/MI326. Fixed n12,3^4 joint-realization lift diagnostic; see sibling .py.
#include <algorithm>
#include <array>
#include <chrono>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <map>
#include <stdexcept>
#include <sys/resource.h>
#include <vector>
using T=std::array<int,4>;
struct Edge {int depth=9;uint32_t word=0;int mask=0;};
struct Fibre {int count=0;std::array<Edge,12> edge;};
std::map<T,Fibre> fibres;
std::vector<int> matchings;
long words=0, canonical=0, trials=0;
auto began=std::chrono::steady_clock::now();
void check(bool x){if(!x)throw std::runtime_error("instrument assertion");}
void budget(){
 rusage u{};check(getrusage(RUSAGE_SELF,&u)==0);
 check(u.ru_maxrss<192L*1024*1024 && trials<=3000000);
 check(std::chrono::duration<double>(std::chrono::steady_clock::now()-began).count()<45);
}
int owner(uint32_t w,int x){return (w>>(2*x))&3;}
bool ss(const T&t){
 if(t[0]+t[1]+t[2]+t[3]!=66)return false;
 for(int m=1;m<16;++m){int c=0,s=0;for(int j=0;j<4;++j)if(m>>j&1){c+=3;s+=t[j];}
  if(s<c*(c-1)/2||s>c*(23-c)/2)return false;
 }return true;
}
int index(int a,int b){return 3*a+b-(b>a);}
void leaf(const T&s,uint32_t w){
 ++words;if(!std::is_sorted(s.begin(),s.end()))return;
 ++canonical;auto it=fibres.find(s);check(it!=fibres.end());auto &f=it->second;++f.count;
 for(int mask:matchings){++trials;T d{};bool active=true;
  for(int k=0;k<11;++k)if(mask>>k&1){int lo=owner(w,k),hi=owner(w,k+1);
   if(lo==hi){active=false;break;}++d[lo];--d[hi];
  }
  if(!active)continue;
  int a=-1,b=-1;bool unit=true;
  for(int j=0;j<4;++j){if(d[j]==-1&&a<0)a=j;else if(d[j]==1&&b<0)b=j;else if(d[j]!=0)unit=false;}
  if(!unit||a<0||b<0)continue;
  T y=s;--y[a];++y[b];check(ss(y));
  int depth=__builtin_popcount((unsigned)mask);auto &e=f.edge[index(a,b)];
  if(depth<e.depth)e={depth,w,mask};
 }
}
void enumerate(int x,T&c,T&s,uint32_t w){
 if(x==12){leaf(s,w);return;}
 for(int j=0;j<4;++j)if(c[j]<3){++c[j];s[j]+=x;
  enumerate(x+1,c,s,w|(uint32_t(j)<<(2*x)));--c[j];s[j]-=x;
 }
 if(x==2)budget();
}
int main(int argc,char **argv){try{
 check(argc==2);rlimit cpu{30,31};check(setrlimit(RLIMIT_CPU,&cpu)==0);
 for(int a=3;a<=30;++a)for(int b=a;b<=30;++b)for(int c=b;c<=30;++c){T t{a,b,c,66-a-b-c};
  if(t[3]>=c&&t[3]<=30&&ss(t))fibres[t];
 }
 for(int m=1;m<(1<<11);++m)if(!(m&(m<<1))&&__builtin_popcount((unsigned)m)<=3)matchings.push_back(m);
 check(matchings.size()==140);T c{},s{};enumerate(0,c,s,0);budget();
 check(words==369600&&canonical==19344&&fibres.size()==630);
 std::ofstream out(argv[1]);check(bool(out));out<<"TOTAL "<<words<<' '<<canonical<<' '<<trials<<' '<<matchings.size()<<'\n';
 for(const auto &[t,f]:fibres){out<<"C";for(int z:t)out<<' '<<z;out<<' '<<f.count<<'\n';
  for(int a=0;a<4;++a)for(int b=0;b<4;++b)if(a!=b){T y=t;--y[a];++y[b];if(!ss(y))continue;
   const auto &e=f.edge[index(a,b)];out<<"E";for(int z:t)out<<' '<<z;
   out<<' '<<a<<' '<<b<<' '<<(e.depth==9?-1:e.depth)<<' '<<e.word<<' '<<e.mask<<'\n';
  }
 }
 check(bool(out));return 0;
}catch(const std::exception&e){std::cerr<<e.what()<<'\n';return 1;}}
