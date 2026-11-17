// B128/MI277 prereg: SAME2000 mixed E28 sample, unrestricted subset exact cover.
// No cardinality, parity, anchor, cycle or canonical-buffer restriction.
// Full catalogue dump for independent MITM; literal per-bin token stream.
// Caps200k nodes/query,10M total,1B catalogue scans,60CPU/90wall/256MiB.
// OUTCOME MI278:239 literal rows;target240 UNKNOWN on scan cap,109105 pending
// nodes. All controls pass. No rerun or search/cap repair;full domain OPEN.
#include <algorithm>
#include <array>
#include <chrono>
#include <cstdint>
#include <ctime>
#include <fstream>
#include <functional>
#include <iostream>
#include <numeric>
#include <set>
#include <stdexcept>
#include <string>
#include <sys/resource.h>
#include <unordered_set>
#include <vector>
using Mask=uint32_t;
struct Cap:std::runtime_error{using std::runtime_error::runtime_error;};
struct Budget{
 uint64_t total=0,local=0,scans=0;clock_t start=clock();
 std::chrono::steady_clock::time_point wall=std::chrono::steady_clock::now();
 void check(){
  if(local>200000||total>10000000||scans>1000000000)throw Cap("work");
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
 void node(){++local;++total;if(local>200000||total>10000000||(total&1023)==0)check();}
 void scan(){++scans;if((scans&65535)==0)check();}
 void reset(){local=0;check();}
} budget;
std::array<std::vector<Mask>,123>cat;
uint64_t catalogued=0;
void catalogue(unsigned next,int sum,Mask mask){
 cat[sum].push_back(mask);if((++catalogued&1023)==0)budget.check();
 for(unsigned j=next;j<28;++j){int s=sum+2*j+1;if(s>122)break;catalogue(j+1,s,mask|(1u<<j));}
}
bool literal(int m,const std::vector<int>&t,const std::vector<Mask>&bins){
 if(t.size()!=bins.size())return false;Mask used=0,all=(1u<<m)-1;
 for(unsigned i=0;i<t.size();++i){
  Mask mask=bins[i];if(!mask||(mask&used)||(mask&~all))return false;used|=mask;
  int sum=0;for(int j=0;j<m;++j)if(mask&(1u<<j))sum+=2*j+1;
  if(sum!=t[i])return false;
 }
 return used==all;
}
bool solve(int m,const std::vector<int>&t,std::vector<Mask>&answer){
 if(m<1||m>28||t.empty()||t.size()>8||std::accumulate(t.begin(),t.end(),0)!=m*m)
  throw std::runtime_error("query hypothesis");
 for(int x:t)if(x<1||x>122)throw std::runtime_error("query target range");
 budget.reset();Mask all=(1u<<m)-1;answer.assign(t.size(),0);
 std::unordered_set<uint64_t>dead;
 std::function<bool(unsigned,Mask)>dfs=[&](unsigned left,Mask used){
  budget.node();if(!left)return used==all;
  if((left&(left-1))==0){answer[__builtin_ctz(left)]=all^used;return bool(all^used);}
  uint64_t key=(uint64_t(left)<<28)|used;if(dead.count(key))return false;
  std::array<std::vector<Mask>,8>fits;std::array<uint64_t,28>counts{};
  unsigned chosen=0;size_t best=SIZE_MAX;int mincards=0;
  for(unsigned i=0;i<t.size();++i)if(left&(1u<<i)){
   int minimum=29;
   for(Mask mask:cat[t[i]]){
    budget.scan();if((mask&used)||(mask&~all))continue;
    fits[i].push_back(mask);minimum=std::min(minimum,__builtin_popcount(mask));
    Mask bits=mask;while(bits){unsigned j=__builtin_ctz(bits);++counts[j];bits&=bits-1;}
   }
   if(fits[i].empty()){dead.insert(key);return false;}
   mincards+=minimum;if(fits[i].size()<best){best=fits[i].size();chosen=i;}
  }
  if(mincards>__builtin_popcount(all^used)){dead.insert(key);return false;}
  Mask pivot=0,bits=all^used;
  while(bits){Mask bit=bits&-bits;unsigned j=__builtin_ctz(bit);bits^=bit;
   if(counts[j]<best){best=counts[j];pivot=bit;}
  }
  if(!best){dead.insert(key);return false;}
  std::vector<std::pair<unsigned,Mask>>choices;
  if(!pivot){for(Mask mask:fits[chosen])choices.push_back({chosen,mask});}
  else{
   std::set<int>equivalent;
   for(unsigned i=0;i<t.size();++i)if((left&(1u<<i))&&equivalent.insert(t[i]).second)
    for(Mask mask:fits[i])if(mask&pivot)choices.push_back({i,mask});
  }
  for(auto row:choices){answer[row.first]=row.second;
   if(dfs(left^(1u<<row.first),used|row.second))return true;
  }
  dead.insert(key);return false;
 };
 bool ok=dfs((1u<<t.size())-1,0);
 if(ok&&!literal(m,t,answer))throw std::runtime_error("internal witness rejected");
 return ok;
}
void controls(){
 std::vector<Mask>ans;
 if(solve(3,{3,3,3},ans))throw std::runtime_error("global conflict control");
 if(solve(26,{67,67,67,67,102,102,102,102},ans))throw std::runtime_error("lower witness control");
 if(!solve(28,{97,97,97,97,99,99,99,99},ans))throw std::runtime_error("unrestricted positive control");
 unsigned checked=0;
 for(int m=1;m<=6;++m){
  std::set<std::vector<int>>oracle;std::array<int,3>sums{};
  std::function<void(int)>assign=[&](int j){
   if(j==m){if(*std::min_element(sums.begin(),sums.end())>0){
     std::vector<int>v(sums.begin(),sums.end());std::sort(v.begin(),v.end());oracle.insert(v);}return;}
   for(int b=0;b<3;++b){sums[b]+=2*j+1;assign(j+1);sums[b]-=2*j+1;}
  };assign(0);
  for(int a=1;a<=m*m/3;++a)for(int b=a;b<=(m*m-a)/2;++b){
   std::vector<int>t{a,b,m*m-a-b};bool ok=solve(m,t,ans);++checked;
   if(ok!=bool(oracle.count(t)))throw std::runtime_error("tiny assignment oracle");
  }
 }
 if(checked!=189)throw std::runtime_error("oracle count");
}
int main(int argc,char**argv){
 unsigned count=0;std::vector<int>pending;std::string status="ERROR",reason;
 uint64_t controlnodes=0,pilotnodes=0;double loopcpu=0;clock_t loopstart=0;std::vector<uint64_t>query_us;
 try{
  if(argc!=2)throw std::runtime_error("catalogue output path required");
  catalogue(0,0,0);if(catalogued!=129658)throw std::runtime_error("catalogue size");
  std::ofstream out(argv[1]);for(unsigned s=0;s<cat.size();++s){out<<s;
   for(Mask mask:cat[s])out<<' '<<mask;out<<'\n';}
  out.close();if(!out)throw std::runtime_error("catalogue output");
  controls();controlnodes=budget.total;
  std::cout<<"# B128 unrestricted m28:8 targets;8(size,tokens);nodes\n";
  loopstart=clock();
  for(unsigned index=0;index<2000;++index){
   pending.clear();int x;
   for(int i=0;i<8;++i){if(!(std::cin>>x))throw std::runtime_error("missing input target");pending.push_back(x);}
   if(!std::is_sorted(pending.begin(),pending.end())||pending.front()<68||pending.back()>122)
    throw std::runtime_error("pilot input domain");
   std::vector<Mask>ans;clock_t before=clock();
   if(!solve(28,pending,ans))throw std::runtime_error("FIRST_NO_WITNESS");
   auto micros=static_cast<uint64_t>(1000000.0*(clock()-before)/CLOCKS_PER_SEC);
   for(int t:pending)std::cout<<t<<' ';
   for(Mask mask:ans){std::cout<<__builtin_popcount(mask)<<' ';
    for(unsigned j=0;j<28;++j)if(mask&(1u<<j))std::cout<<2*j+1<<' ';}
   query_us.push_back(micros);std::cout<<budget.local<<'\n';if(!std::cout)throw std::runtime_error("witness output");
   ++count;pending.clear();budget.check();
  }
  if(std::cin>>reason)throw std::runtime_error("extra input target");reason.clear();status="COMPLETE_SAME_2000";
 }catch(const Cap&e){status="UNKNOWN_CAP";reason=e.what();}
 catch(const std::exception&e){reason=e.what();status=reason=="FIRST_NO_WITNESS"?"FIRST_NO_WITNESS":"ERROR";}
 if(loopstart)loopcpu=double(clock()-loopstart)/CLOCKS_PER_SEC;
 pilotnodes=budget.total-controlnodes;
 rusage rss{};getrusage(RUSAGE_SELF,&rss);
 std::cerr<<"{\"status\":\""<<status<<"\",\"reason\":\""<<reason<<"\",\"completed\":"<<count
 <<",\"catalogue_masks\":"<<catalogued<<",\"total_nodes\":"<<budget.total
 <<",\"control_nodes\":"<<controlnodes<<",\"pilot_attempted_nodes\":"<<pilotnodes
 <<",\"pending_nodes\":"<<(pending.empty()?0:budget.local)<<",\"catalogue_scans\":"<<budget.scans
 <<",\"search_loop_cpu_seconds\":"<<loopcpu<<",\"cpu_seconds\":"<<double(clock()-budget.start)/CLOCKS_PER_SEC
 <<",\"rss_native\":"<<rss.ru_maxrss<<",\"pending_target\":[";
 for(size_t i=0;i<pending.size();++i)std::cerr<<(i?",":"")<<pending[i];
 std::cerr<<"],\"query_cpu_us\":[";
 for(size_t i=0;i<query_us.size();++i)std::cerr<<(i?",":"")<<query_us[i];
 std::cerr<<"]}\n";return status=="COMPLETE_SAME_2000"?0:2;
}
