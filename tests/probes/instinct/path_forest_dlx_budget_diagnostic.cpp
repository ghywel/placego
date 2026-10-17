// B132/MI284: isolated STATIC minimum-token budget on SAME first3 B131 inputs.
// Reuse archived DLX construction/cover/uncover; do not execute its old main.
// Sole search change: reject a state with remaining tokens < remaining root minima.
// No memoization, symmetry change, new order, altered columns or larger caps.
// OUTCOME MI285:all controls/first3 literal rows pass;10/37/64 states.
// Static budget alone clears B131's third-target cap;no full2000 run.
#define main b131_archived_entrypoint
#include "path_forest_dlx_pilot.cpp"
#undef main

uint64_t capacity_prunes=0;
int root_minimum(int m,int target){
 int n=1;while(n<=m&&(n%2!=target%2||n*(2*m-n)<target))++n;
 return n;
}
bool fits_capacity(int tokens,int minimum){return tokens>=minimum;}
struct BudgetDLX:DLX{
 std::vector<int>lower;
 int required=0;
 BudgetDLX(int m,const std::vector<int>&t):DLX(m,t){
  for(int x:t){lower.push_back(root_minimum(m,x));required+=lower.back();}
 }
 bool visit(int tokens,int minimum){
  budget.node();
  if(!fits_capacity(tokens,minimum)){++capacity_prunes;return false;}
  if(!a[0].R){
   std::fill(answer.begin(),answer.end(),0);
   for(int r:picked)answer[rowbin[r]]=rowmask[r];
   return true;
  }
  // This is B131's unchanged minimum-column rule and linked row order.
  int c=a[0].R;
  for(int j=a[c].R;j;j=a[j].R)if(size[j]<size[c])c=j;
  if(!size[c])return false;
  cover(c);
  for(int r=a[c].D;r!=c;r=a[r].D){
   int id=a[r].row,b=rowbin[id],card=__builtin_popcount(rowmask[id]);
   picked.push_back(id);
   for(int j=a[r].R;j!=r;j=a[j].R)cover(a[j].C);
   bool ok=visit(tokens-card,minimum-lower[b]);
   for(int j=a[r].L;j!=r;j=a[j].L)uncover(a[j].C);
   picked.pop_back();
   if(ok){uncover(c);return true;}
  }
  uncover(c);return false;
 }
 bool run_pruned(){
  auto before=a;auto counts=size;
  bool ok=visit(m,required);same(before,counts);++budget.restored;
  if(!picked.empty())throw std::runtime_error("picked stack not restored");
  return ok;
 }
};
bool solve_pruned(int m,const std::vector<int>&t,std::vector<Mask>&answer){
 if(m<1||m>28||t.empty()||t.size()>8||std::accumulate(t.begin(),t.end(),0)!=m*m)
  throw std::runtime_error("query hypothesis");
 budget.reset();int required=0;
 for(int target:t){
  if(target<1||target>122)throw std::runtime_error("target range");
  int least=root_minimum(m,target);if(least>m)return false;required+=least;
 }
 if(required>m)return false;
 BudgetDLX model(m,t);bool ok=model.run_pruned();answer=model.answer;
 if(ok&&!literal(m,t,answer))throw std::runtime_error("literal rejection");
 return ok;
}
void diagnostic_controls(){
 std::vector<Mask>ans;
 BudgetDLX audit(28,{97,97,97,97,99,99,99,99});audit.restoration_audit();
 if(!audit.run_pruned()||!literal(28,{97,97,97,97,99,99,99,99},audit.answer))throw std::runtime_error("positive fixture");
 if(solve_pruned(3,{3,3,3},ans))throw std::runtime_error("global conflict");
 if(solve_pruned(26,{67,67,67,67,102,102,102,102},ans))throw std::runtime_error("lower fixture");
 std::vector<int>t{75,87,88,93,109,110,110,112};int sum=0;
 for(int x:t)sum+=root_minimum(28,x);
 if(sum!=26||!fits_capacity(23,sum-3)||fits_capacity(21,sum-3))throw std::runtime_error("boundary budget");
 unsigned checked=0;
 for(int m=1;m<=6;++m){
  std::set<std::vector<int>>oracle;std::array<int,3>sums{};
  std::function<void(int)>assign=[&](int j){
   if(j==m){if(*std::min_element(sums.begin(),sums.end())>0){
    std::vector<int>v(sums.begin(),sums.end());std::sort(v.begin(),v.end());oracle.insert(v);}return;}
   for(int b=0;b<3;++b){sums[b]+=2*j+1;assign(j+1);sums[b]-=2*j+1;}
  };assign(0);
  for(int x=1;x<=m*m/3;++x)for(int y=x;y<=(m*m-x)/2;++y){
   std::vector<int>q{x,y,m*m-x-y};bool ok=solve_pruned(m,q,ans);++checked;
   if(ok!=bool(oracle.count(q)))throw std::runtime_error("tiny assignment oracle");
  }
 }
 if(checked!=189)throw std::runtime_error("oracle count");
}
int main(int argc,char**argv){
 unsigned completed=0;std::vector<int>pending;std::string status="ERROR",reason;
 uint64_t controlnodes=0,controlupdates=0,controlprunes=0;clock_t loopstart=0;
 std::vector<uint64_t>query_us,query_nodes,query_updates,query_prunes;
 try{
  if(argc!=2)throw std::runtime_error("catalogue output path required");
  catalogue(0,0,0);if(catalogued!=129658)throw std::runtime_error("catalogue size");
  std::ofstream out(argv[1]);for(unsigned s=0;s<cat.size();++s){out<<s;for(Mask mask:cat[s])out<<' '<<mask;out<<'\n';}
  out.close();if(!out)throw std::runtime_error("catalogue output");
  diagnostic_controls();controlnodes=budget.total;controlupdates=budget.updates;controlprunes=capacity_prunes;
  std::cout<<"# B132 static-budget DLX m28:first3 targets;8(size,tokens);nodes\n";loopstart=clock();
  for(unsigned i=0;i<3;++i){
   pending.clear();int x;for(int j=0;j<8;++j){if(!(std::cin>>x))throw std::runtime_error("missing input");pending.push_back(x);}
   if(!std::is_sorted(pending.begin(),pending.end())||pending.front()<68||pending.back()>122)throw std::runtime_error("input domain");
   auto before_updates=budget.updates,before_prunes=capacity_prunes;clock_t before=clock();std::vector<Mask>ans;
   if(!solve_pruned(28,pending,ans))throw std::runtime_error("FIRST_NO_WITNESS");
   query_us.push_back(static_cast<uint64_t>(1000000.0*(clock()-before)/CLOCKS_PER_SEC));
   query_nodes.push_back(budget.local);query_updates.push_back(budget.updates-before_updates);query_prunes.push_back(capacity_prunes-before_prunes);
   for(int v:pending)std::cout<<v<<' ';
   for(Mask mask:ans){std::cout<<__builtin_popcount(mask)<<' ';for(int j=0;j<28;++j)if(mask&(1u<<j))std::cout<<2*j+1<<' ';}
   std::cout<<budget.local<<'\n';std::cout.flush();if(!std::cout)throw std::runtime_error("output");
   ++completed;pending.clear();budget.check();
  }
  if(std::cin>>reason)throw std::runtime_error("extra input");reason.clear();status="COMPLETE_SAME_FIRST3";
 }catch(const Cap&e){status="UNKNOWN_CAP";reason=e.what();}
 catch(const std::exception&e){reason=e.what();status=reason=="FIRST_NO_WITNESS"?"FIRST_NO_WITNESS":"ERROR";}
 rusage r{};getrusage(RUSAGE_SELF,&r);
 std::cerr<<"{\"status\":\""<<status<<"\",\"reason\":\""<<reason<<"\",\"completed\":"<<completed
 <<",\"control_nodes\":"<<controlnodes<<",\"pilot_attempted_nodes\":"<<budget.total-controlnodes
 <<",\"pending_nodes\":"<<(pending.empty()?0:budget.local)<<",\"link_updates\":"<<budget.updates
 <<",\"control_updates\":"<<controlupdates<<",\"capacity_prunes\":"<<capacity_prunes
 <<",\"control_prunes\":"<<controlprunes<<",\"matrices\":"<<budget.matrices<<",\"restored\":"<<budget.restored
 <<",\"built_incidences\":"<<budget.built<<",\"max_matrix_nodes\":"<<budget.max_matrix_nodes
 <<",\"search_loop_cpu_seconds\":"<<(loopstart?double(clock()-loopstart)/CLOCKS_PER_SEC:0)
 <<",\"cpu_seconds\":"<<double(clock()-budget.start)/CLOCKS_PER_SEC<<",\"rss_native\":"<<r.ru_maxrss<<",\"pending_target\":[";
 for(size_t i=0;i<pending.size();++i)std::cerr<<(i?",":"")<<pending[i];
 auto array=[&](const char*name,const std::vector<uint64_t>&values){std::cerr<<"],\""<<name<<"\":[";for(size_t i=0;i<values.size();++i)std::cerr<<(i?",":"")<<values[i];};
 array("query_cpu_us",query_us);array("query_nodes",query_nodes);array("query_updates",query_updates);array("query_prunes",query_prunes);
 std::cerr<<"]}\n";return status=="COMPLETE_SAME_FIRST3"?0:2;
}
