// B131/MI282: known Algorithm X / dancing links, SAME2000 mixed E28 pilot.
// Knuth cs/0011047v1; independently translated reversible incidence algorithm.
// Ordinary bin+token columns. No anchors/bin-size model/target-specific repairs.
// All successful/unsuccessful searches restore EVERY node and column count.
// Caps200k states/query,10M total,1B cover+uncover updates,20CPU/40wall/256MiB.
// OUTCOME MI283:all controls/two literal rows pass;third target200001-state
// cap. No rerun/repair. Standard DLX lacks B128's dynamic cardinality pruning.
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
#include <vector>
using Mask=uint32_t;
#ifndef DLX_CPU_CAP_SECONDS
#define DLX_CPU_CAP_SECONDS 20
#endif
#ifndef DLX_WALL_CAP_SECONDS
#define DLX_WALL_CAP_SECONDS 40
#endif
struct Cap:std::runtime_error{using std::runtime_error::runtime_error;};
struct Budget{
 uint64_t total=0,local=0,updates=0,built=0,matrices=0,restored=0;
 size_t max_matrix_nodes=0;clock_t start=clock();
 std::chrono::steady_clock::time_point wall=std::chrono::steady_clock::now();
 void check(){
  if(local>200000||total>10000000||updates>1000000000)throw Cap("work");
  if(double(clock()-start)/CLOCKS_PER_SEC>DLX_CPU_CAP_SECONDS)throw Cap("cpu");
  if(std::chrono::duration<double>(std::chrono::steady_clock::now()-wall).count()>DLX_WALL_CAP_SECONDS)throw Cap("wall");
  rusage r{};getrusage(RUSAGE_SELF,&r);
#ifdef __APPLE__
  auto bytes=r.ru_maxrss;
#else
  auto bytes=r.ru_maxrss*1024L;
#endif
  if(bytes>256L*1024*1024)throw Cap("rss");
 }
 void node(){++local;++total;if(local>200000||total>10000000||(total&1023)==0)check();}
 void update(){++updates;if((updates&65535)==0)check();}
 void build(){++built;if((built&4095)==0)check();}
 void reset(){local=0;check();}
}budget;
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
struct Node{
 int L,R,U,D,C,row;
 bool operator==(const Node&b)const{return L==b.L&&R==b.R&&U==b.U&&D==b.D&&C==b.C&&row==b.row;}
};
struct DLX{
 int m,k,cols;std::vector<Node>a;std::vector<int>size,picked,rowbin;
 std::vector<Mask>rowmask,answer;
 DLX(int count,const std::vector<int>&t):m(count),k(int(t.size())),cols(m+k),a(cols+1),size(cols+1),answer(k){
  for(int c=0;c<=cols;++c)a[c]={(c+cols)%(cols+1),(c+1)%(cols+1),c,c,c,-1};
  Mask all=(1u<<m)-1;size_t reserve=cols+1;
  for(int target:t)for(Mask mask:cat[target])if(!(mask&~all))reserve+=1+__builtin_popcount(mask);
  a.reserve(reserve);
  for(int b=0;b<k;++b)for(Mask mask:cat[t[b]])if(!(mask&~all)){
   int id=int(rowbin.size()),first=-1;rowbin.push_back(b);rowmask.push_back(mask);
   std::vector<int>columns{b+1};
   for(int j=0;j<m;++j)if(mask&(1u<<j))columns.push_back(k+1+j);
   for(int c:columns){
    int n=int(a.size());a.push_back({n,n,a[c].U,c,c,id});
    a[a[c].U].D=n;a[c].U=n;++size[c];
    if(first<0)first=n;
    else{a[n].L=a[first].L;a[n].R=first;a[a[first].L].R=n;a[first].L=n;}
    budget.build();
   }
  }
  ++budget.matrices;budget.max_matrix_nodes=std::max(budget.max_matrix_nodes,a.size());budget.check();
 }
 void cover(int c){
  a[a[c].R].L=a[c].L;a[a[c].L].R=a[c].R;
  for(int i=a[c].D;i!=c;i=a[i].D)for(int j=a[i].R;j!=i;j=a[j].R){
   a[a[j].D].U=a[j].U;a[a[j].U].D=a[j].D;--size[a[j].C];budget.update();
  }
 }
 void uncover(int c){
  for(int i=a[c].U;i!=c;i=a[i].U)for(int j=a[i].L;j!=i;j=a[j].L){
   ++size[a[j].C];a[a[j].D].U=j;a[a[j].U].D=j;budget.update();
  }
  a[a[c].R].L=c;a[a[c].L].R=c;
 }
 void same(const std::vector<Node>&before,const std::vector<int>&counts){
  if(a!=before||size!=counts)throw std::runtime_error("full restoration mismatch");
 }
 void restoration_audit(){
  auto before=a;auto counts=size;
  for(int c=1;c<=cols;++c){cover(c);uncover(c);same(before,counts);}
  int first=a[1].D;if(first==1)throw std::runtime_error("restoration fixture empty");
  std::vector<int>columns;int n=first;
  do{columns.push_back(a[n].C);n=a[n].R;}while(n!=first);
  for(int c:columns)cover(c);
  for(auto it=columns.rbegin();it!=columns.rend();++it)uncover(*it);
  same(before,counts);++budget.restored;
 }
 bool dfs(){
  budget.node();
  if(!a[0].R){
   std::fill(answer.begin(),answer.end(),0);
   for(int r:picked)answer[rowbin[r]]=rowmask[r];
   return true;
  }
  int c=a[0].R;
  for(int j=a[c].R;j;j=a[j].R)if(size[j]<size[c])c=j;
  if(!size[c])return false;
  cover(c);
  for(int r=a[c].D;r!=c;r=a[r].D){
   picked.push_back(a[r].row);
   for(int j=a[r].R;j!=r;j=a[j].R)cover(a[j].C);
   bool ok=dfs();
   for(int j=a[r].L;j!=r;j=a[j].L)uncover(a[j].C);
   picked.pop_back();
   if(ok){uncover(c);return true;}
  }
  uncover(c);return false;
 }
 bool run(){
  auto before=a;auto counts=size;
  bool ok=dfs();same(before,counts);++budget.restored;
  if(!picked.empty())throw std::runtime_error("picked stack not restored");
  return ok;
 }
};
bool solve(int m,const std::vector<int>&t,std::vector<Mask>&answer){
 if(m<1||m>28||t.empty()||t.size()>8||std::accumulate(t.begin(),t.end(),0)!=m*m)
  throw std::runtime_error("query hypothesis");
 budget.reset();int required=0;
 for(int target:t){
  if(target<1||target>122)throw std::runtime_error("target range");
  int least=1;while(least<=m&&(least%2!=target%2||least*(2*m-least)<target))++least;
  if(least>m)return false;required+=least;
 }
 // Generic necessary root test only: odd-token parity and largest-k capacity.
 if(required>m)return false;
 DLX model(m,t);bool ok=model.run();answer=model.answer;
 if(ok&&!literal(m,t,answer))throw std::runtime_error("internal literal rejection");
 return ok;
}
void controls(){
 std::vector<Mask>ans;
 DLX audit(28,{97,97,97,97,99,99,99,99});audit.restoration_audit();
 if(!audit.run()||!literal(28,{97,97,97,97,99,99,99,99},audit.answer))throw std::runtime_error("positive audit fixture");
 if(solve(3,{3,3,3},ans))throw std::runtime_error("global conflict control");
 if(solve(26,{67,67,67,67,102,102,102,102},ans))throw std::runtime_error("root cardinality lower witness");
 unsigned checked=0;
 for(int m=1;m<=6;++m){
  std::set<std::vector<int>>oracle;std::array<int,3>sums{};
  std::function<void(int)>assign=[&](int j){
   if(j==m){if(*std::min_element(sums.begin(),sums.end())>0){
     std::vector<int>v(sums.begin(),sums.end());std::sort(v.begin(),v.end());oracle.insert(v);}return;}
   for(int b=0;b<3;++b){sums[b]+=2*j+1;assign(j+1);sums[b]-=2*j+1;}
  };assign(0);
  for(int x=1;x<=m*m/3;++x)for(int y=x;y<=(m*m-x)/2;++y){
   std::vector<int>t{x,y,m*m-x-y};bool ok=solve(m,t,ans);++checked;
   if(ok!=bool(oracle.count(t)))throw std::runtime_error("tiny assignment oracle");
  }
 }
 if(checked!=189)throw std::runtime_error("oracle count");
}
int main(int argc,char**argv){
 unsigned count=0;std::vector<int>pending;std::string status="ERROR",reason;
 uint64_t controlnodes=0,controlupdates=0;double loopcpu=0;clock_t loopstart=0;
 std::vector<uint64_t>query_us,query_updates;
 try{
  if(argc!=2)throw std::runtime_error("catalogue output path required");
  catalogue(0,0,0);if(catalogued!=129658)throw std::runtime_error("catalogue size");
  std::ofstream out(argv[1]);for(unsigned s=0;s<cat.size();++s){out<<s;for(Mask mask:cat[s])out<<' '<<mask;out<<'\n';}
  out.close();if(!out)throw std::runtime_error("catalogue output");
  controls();controlnodes=budget.total;controlupdates=budget.updates;
  std::cout<<"# B131 DLX m28:8 targets;8(size,tokens);nodes\n";loopstart=clock();
  for(unsigned index=0;index<2000;++index){
   pending.clear();int x;for(int i=0;i<8;++i){if(!(std::cin>>x))throw std::runtime_error("missing input");pending.push_back(x);}
   if(!std::is_sorted(pending.begin(),pending.end())||pending.front()<68||pending.back()>122)throw std::runtime_error("input domain");
   std::vector<Mask>ans;clock_t before=clock();auto updates_before=budget.updates;
   if(!solve(28,pending,ans))throw std::runtime_error("FIRST_NO_WITNESS");
   auto micros=static_cast<uint64_t>(1000000.0*(clock()-before)/CLOCKS_PER_SEC);
   for(int t:pending)std::cout<<t<<' ';
   for(Mask mask:ans){std::cout<<__builtin_popcount(mask)<<' ';for(unsigned j=0;j<28;++j)if(mask&(1u<<j))std::cout<<2*j+1<<' ';}
   query_us.push_back(micros);query_updates.push_back(budget.updates-updates_before);
   std::cout<<budget.local<<'\n';std::cout.flush();if(!std::cout)throw std::runtime_error("output");
   ++count;pending.clear();budget.check();
  }
  if(std::cin>>reason)throw std::runtime_error("extra input");reason.clear();status="COMPLETE_SAME_2000";
 }catch(const Cap&e){status="UNKNOWN_CAP";reason=e.what();}
 catch(const std::exception&e){reason=e.what();status=reason=="FIRST_NO_WITNESS"?"FIRST_NO_WITNESS":"ERROR";}
 if(loopstart)loopcpu=double(clock()-loopstart)/CLOCKS_PER_SEC;
 rusage r{};getrusage(RUSAGE_SELF,&r);
 std::cerr<<"{\"status\":\""<<status<<"\",\"reason\":\""<<reason<<"\",\"completed\":"<<count
 <<",\"catalogue_masks\":"<<catalogued<<",\"total_nodes\":"<<budget.total<<",\"control_nodes\":"<<controlnodes
 <<",\"pilot_attempted_nodes\":"<<budget.total-controlnodes<<",\"pending_nodes\":"<<(pending.empty()?0:budget.local)
 <<",\"link_updates\":"<<budget.updates<<",\"control_updates\":"<<controlupdates
 <<",\"built_incidences\":"<<budget.built<<",\"matrices\":"<<budget.matrices<<",\"restored\":"<<budget.restored
 <<",\"max_matrix_nodes\":"<<budget.max_matrix_nodes<<",\"search_loop_cpu_seconds\":"<<loopcpu
 <<",\"cpu_seconds\":"<<double(clock()-budget.start)/CLOCKS_PER_SEC<<",\"rss_native\":"<<r.ru_maxrss<<",\"pending_target\":[";
 for(size_t i=0;i<pending.size();++i)std::cerr<<(i?",":"")<<pending[i];
 std::cerr<<"],\"query_cpu_us\":[";for(size_t i=0;i<query_us.size();++i)std::cerr<<(i?",":"")<<query_us[i];
 std::cerr<<"],\"query_updates\":[";for(size_t i=0;i<query_updates.size();++i)std::cerr<<(i?",":"")<<query_updates[i];
 std::cerr<<"]}\n";return status=="COMPLETE_SAME_2000"?0:2;
}
