// B124/MI269: one capped complete canonical-buffer q8 attempt.
// Normalized enumeration is checked independently on original targets in Python.
// Stop first negative or cap. No repair, alternate buffer, other parity or level.
// 100k states/profile, 50M total, 60 CPU s, 90 wall s, 256 MiB RSS.
// Predictions, counterfactuals and independent controls: GPT-MATH-INSTINCT MI269.
#include <algorithm>
#include <array>
#include <chrono>
#include <cstdint>
#include <ctime>
#include <functional>
#include <iostream>
#include <map>
#include <numeric>
#include <stdexcept>
#include <string>
#include <sys/resource.h>
#include <unordered_set>
#include <vector>
using Mask=uint32_t;
using Buckets=std::map<int,std::vector<Mask>>;
struct Cap:std::runtime_error {using std::runtime_error::runtime_error;};
struct Budget {
 uint64_t total=0,local=0,maxlocal=0; clock_t start=clock();
 std::chrono::steady_clock::time_point wall=std::chrono::steady_clock::now();
 void check(){
  if(local>100000 || total>50000000)throw Cap("nodes");
  if(double(clock()-start)/CLOCKS_PER_SEC>60)throw Cap("cpu");
  if(std::chrono::duration<double>(std::chrono::steady_clock::now()-wall).count()>90)throw Cap("wall");
  rusage r{};getrusage(RUSAGE_SELF,&r);
#ifdef __APPLE__
  auto bytes=r.ru_maxrss;
#else
  auto bytes=r.ru_maxrss*1024L;
#endif
  if(bytes>256L*1024*1024)throw Cap("rss");
 }
 void step(){++total;++local;if(local>100000||total>50000000||(total&1023)==0)check();}
 void reset(){maxlocal=std::max(maxlocal,local);local=0;check();}
} budget;
Buckets catalogue(const std::vector<int>&pool){
 if(pool.size()>28)throw std::runtime_error("pool mask overflow");
 Buckets c;
 for(unsigned i=0;i<pool.size();++i)for(unsigned j=i+1;j<pool.size();++j)
 for(unsigned k=j+1;k<pool.size();++k)c[pool[i]+pool[j]+pool[k]].push_back((1u<<i)|(1u<<j)|(1u<<k));
 return c;
}
bool solve(const std::vector<int>&pool,const std::vector<int>&targets,const Buckets&cat,std::vector<Mask>&answer){
 if(pool.size()!=3*targets.size()||targets.size()>8)throw std::invalid_argument("triple inventory");
 if(std::accumulate(pool.begin(),pool.end(),0)!=std::accumulate(targets.begin(),targets.end(),0))throw std::invalid_argument("sum");
 std::vector<const std::vector<Mask>*>opts;
 static const std::vector<Mask>empty;
 for(int t:targets){auto it=cat.find(t);opts.push_back(it==cat.end()?&empty:&it->second);}
 std::unordered_set<uint64_t>dead;answer.assign(targets.size(),0);
 const Mask all=(1u<<pool.size())-1;
 std::function<bool(unsigned,Mask)>dfs=[&](unsigned left,Mask used){
  budget.step();if(!left)return used==all;
  uint64_t key=(uint64_t(left)<<28)|used;if(dead.count(key))return false;
  unsigned chosen=0;size_t best=SIZE_MAX;
  for(unsigned i=0;i<targets.size();++i)if(left&(1u<<i)){
   size_t count=0;for(Mask m:*opts[i])if(!(m&used))++count;
   if(!count){dead.insert(key);return false;}
   if(count<best){best=count;chosen=i;}
  }
  for(Mask m:*opts[chosen])if(!(m&used)){
   answer[chosen]=m;if(dfs(left^(1u<<chosen),used|m))return true;
  }
  dead.insert(key);return false;
 };
 return dfs((1u<<targets.size())-1,0);
}
std::vector<int>buffer(int a){
 std::vector<int>c=a<=91?std::vector<int>{1,3,5,7,9,11,a-36}:std::vector<int>{1,3,5,7,9,a-80,55};
 std::sort(c.begin(),c.end());
 if(std::adjacent_find(c.begin(),c.end())!=c.end()||std::accumulate(c.begin(),c.end(),0)!=a||c.front()<1||c.back()>55)throw std::runtime_error("buffer");
 return c;
}
void controls(){
 std::vector<int>p{1,3,5,7,9,11,13,15,101,1001,10001,100001};
 std::vector<int>t{111,1011,10023,100023};auto c=catalogue(p);std::vector<Mask>r;
 for(int s:t)if(c.find(s)==c.end())throw std::runtime_error("individual feasibility control");
 budget.reset();if(solve(p,t,c,r))throw std::runtime_error("global negative control");
 for(auto ts:std::vector<std::vector<int>>{{69,69,69,93,121,121,121,121},{97,97,97,97,99,99,99,99}}){
  auto b=buffer(ts[0]);p.clear();for(int x=1;x<=55;x+=2)if(!std::binary_search(b.begin(),b.end(),x))p.push_back(x);
  t.assign(ts.begin()+1,ts.end());c=catalogue(p);budget.reset();if(!solve(p,t,c,r))throw std::runtime_error("positive control");
 }
 p.push_back(57);bool rejected=false;
 try{solve(p,t,c,r);}catch(const std::invalid_argument&){rejected=true;}
 if(!rejected)throw std::runtime_error("wrong pool size control");
}
int main(){
 unsigned count=0;std::array<int,22>counts{};std::vector<int>pending;int active_h=-1;
 std::string status="ERROR",reason;
 try{
  controls();
  std::cout<<"# B124 original targets followed by seven buffer tokens and seven triples\n";
  std::vector<int>holes;for(int h=10;h<=21;++h)holes.push_back(h);for(int h=1;h<=3;++h)holes.push_back(h);
  for(int h:holes){
   active_h=h;int base=h>=10?13:11,a=h>=10?2*h+49:2*h+91;
   int lo=h>=10?h+5:h+29,hi=h>=10?41:44;
   std::vector<int>pool;for(int j=0;j<22;++j)if(j!=h)pool.push_back(j);
   const auto cat=catalogue(pool);std::vector<int>s;
   std::function<void(int,int,int)>enumerate=[&](int n,int lower,int left){
    if(n==0){
     if(left)throw std::runtime_error("enumeration total");
     pending={a};for(int x:s)pending.push_back(3*base+2*x);
     budget.reset();std::vector<Mask>ans;
     if(!solve(pool,s,cat,ans))throw std::runtime_error("FIRST_CANONICAL_NO_WITNESS");
     for(int t:pending)std::cout<<t<<' ';
     for(int x:buffer(a))std::cout<<x<<' ';
     for(Mask m:ans)for(unsigned j=0;j<pool.size();++j)if(m&(1u<<j))std::cout<<base+2*pool[j]<<' ';
     std::cout<<'\n';if(!std::cout)throw std::runtime_error("output");
     ++count;++counts[h];pending.clear();budget.check();return;
    }
    for(int x=lower;x<=hi;++x){
     if(n*x>left)break;if(x+(n-1)*hi<left)continue;
     s.push_back(x);enumerate(n-1,x,left-x);s.pop_back();
    }
   };
   enumerate(7,lo,231-h);
  }
  if(count!=258180)throw std::runtime_error("domain count mismatch");
  status="COMPLETE";
 }catch(const Cap&e){status="UNKNOWN_CAP";reason=e.what();}
 catch(const std::exception&e){reason=e.what();status=reason=="FIRST_CANONICAL_NO_WITNESS"?"FIRST_CANONICAL_NO_WITNESS":"ERROR";}
 budget.maxlocal=std::max(budget.maxlocal,budget.local);rusage r{};getrusage(RUSAGE_SELF,&r);
 std::cerr<<"{\"status\":\""<<status<<"\",\"reason\":\""<<reason<<"\",\"count\":"<<count
 <<",\"total_nodes\":"<<budget.total<<",\"max_profile_nodes\":"<<budget.maxlocal
 <<",\"cpu_seconds\":"<<double(clock()-budget.start)/CLOCKS_PER_SEC<<",\"rss_native\":"<<r.ru_maxrss
 <<",\"active_h\":"<<active_h<<",\"pending_target\":[";
 for(size_t i=0;i<pending.size();++i)std::cerr<<(i?",":"")<<pending[i];
 std::cerr<<"],\"hole_counts\":{";bool first=true;
 for(int h=0;h<22;++h)if(counts[h]){std::cerr<<(first?"":",")<<'\"'<<h<<"\":"<<counts[h];first=false;}
 std::cerr<<"}}\n";return status=="COMPLETE"?0:2;
}
