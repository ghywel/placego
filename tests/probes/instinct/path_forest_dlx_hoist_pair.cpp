// B133/MI286: paired late/early evaluation of the SAME necessary token bound.
// Full exact mathematical-state traces; rejected children counted in both modes.
// Known DLX implementation inherited unchanged. No new heuristic or larger run.
#define main b131_archived_entrypoint
#include "path_forest_dlx_pilot.cpp"
#undef main

int minimum_tokens(int m,int target){
 int k=1;while(k<=m&&(k%2!=target%2||k*(2*m-k)<target))++k;return k;
}
struct State{
 Mask used;unsigned left;int tokens,minimum,rejected;
 bool operator==(const State&b)const{return used==b.used&&left==b.left&&tokens==b.tokens&&minimum==b.minimum&&rejected==b.rejected;}
};
struct TracedDLX:DLX{
 bool early;int required=0;std::vector<int>lower;std::vector<State>trace;uint64_t prunes=0;
 TracedDLX(int m,const std::vector<int>&t,bool mode):DLX(m,t),early(mode){
  for(int x:t){lower.push_back(minimum_tokens(m,x));required+=lower.back();}
 }
 bool record(State s){
  budget.node();s.rejected=s.tokens<s.minimum;trace.push_back(s);
  if(s.rejected)++prunes;
  return !s.rejected;
 }
 bool visit(State s){
  if(!record(s))return false;
  if(!a[0].R){
   std::fill(answer.begin(),answer.end(),0);
   for(int r:picked)answer[rowbin[r]]=rowmask[r];return true;
  }
  int c=a[0].R;
  for(int j=a[c].R;j;j=a[j].R)if(size[j]<size[c])c=j;
  if(!size[c])return false;
  cover(c);
  for(int r=a[c].D;r!=c;r=a[r].D){
   int id=a[r].row,b=rowbin[id];Mask mask=rowmask[id];
   State child{s.used|mask,s.left^(1u<<b),s.tokens-__builtin_popcount(mask),s.minimum-lower[b],0};
   if(early&&child.tokens<child.minimum){
    // Same rejected child visit/accounting, without its reversible mutations.
    if(record(child))throw std::runtime_error("early rejection accounting");
    continue;
   }
   picked.push_back(id);
   for(int j=a[r].R;j!=r;j=a[j].R)cover(a[j].C);
   bool ok=visit(child);
   for(int j=a[r].L;j!=r;j=a[j].L)uncover(a[j].C);
   picked.pop_back();
   if(ok){uncover(c);return true;}
  }
  uncover(c);return false;
 }
 bool run_traced(){
  auto before=a;auto counts=size;
  bool ok=visit({0,(1u<<k)-1,m,required,0});same(before,counts);++budget.restored;
  if(!picked.empty())throw std::runtime_error("picked stack restoration");return ok;
 }
};
struct Result{
 bool ok=false;std::vector<Mask>bins;std::vector<State>trace;
 uint64_t nodes=0,updates=0,prunes=0,micros=0;
};
Result run_case(int m,const std::vector<int>&t,bool early,bool audit=false){
 clock_t before=clock();auto updates=budget.updates;Result result;budget.reset();
 if(m<1||m>28||t.empty()||t.size()>8||std::accumulate(t.begin(),t.end(),0)!=m*m)throw std::runtime_error("query hypothesis");
 int required=0;
 for(int x:t){if(x<1||x>122)throw std::runtime_error("target range");int n=minimum_tokens(m,x);if(n>m)return result;required+=n;}
 if(required>m)return result;
 {
  TracedDLX model(m,t,early);if(audit)model.restoration_audit();
  result.ok=model.run_traced();result.bins=model.answer;result.trace=std::move(model.trace);
  result.nodes=budget.local;result.updates=budget.updates-updates;result.prunes=model.prunes;
  if(result.ok&&!literal(m,t,result.bins))throw std::runtime_error("literal rejection");
 } // include matrix destruction in case timing, in both arms
 result.micros=static_cast<uint64_t>(1000000.0*(clock()-before)/CLOCKS_PER_SEC);return result;
}
void same_results(const Result&a,const Result&b){
 if(a.ok!=b.ok||a.trace!=b.trace||a.nodes!=b.nodes||a.prunes!=b.prunes||(a.ok&&a.bins!=b.bins))throw std::runtime_error("paired trace/witness mismatch");
}
void pair_controls(){
 std::vector<int>positive{97,97,97,97,99,99,99,99};
 auto a=run_case(28,positive,false,true),b=run_case(28,positive,true,true);same_results(a,b);
 if(!a.ok)throw std::runtime_error("positive fixture");
 for(auto q:std::vector<std::pair<int,std::vector<int>>>{{3,{3,3,3}},{26,{67,67,67,67,102,102,102,102}}}){
  auto x=run_case(q.first,q.second,false),y=run_case(q.first,q.second,true);same_results(x,y);if(x.ok)throw std::runtime_error("negative fixture");
 }
 unsigned checked=0;
 for(int m=1;m<=6;++m){
  std::set<std::vector<int>>oracle;std::array<int,3>sums{};
  std::function<void(int)>assign=[&](int j){
   if(j==m){if(*std::min_element(sums.begin(),sums.end())>0){std::vector<int>v(sums.begin(),sums.end());std::sort(v.begin(),v.end());oracle.insert(v);}return;}
   for(int b=0;b<3;++b){sums[b]+=2*j+1;assign(j+1);sums[b]-=2*j+1;}
  };assign(0);
  for(int x=1;x<=m*m/3;++x)for(int y=x;y<=(m*m-x)/2;++y){
   std::vector<int>q{x,y,m*m-x-y};auto a=run_case(m,q,false),b=run_case(m,q,true);same_results(a,b);
   if(a.ok!=bool(oracle.count(q)))throw std::runtime_error("tiny oracle");++checked;
  }
 }
 if(checked!=189)throw std::runtime_error("oracle count");
}
int main(int argc,char**argv){
 std::string status="ERROR",reason;unsigned completed=0,active_arm=0;bool running=false;std::vector<int>pending;
 uint64_t controlnodes=0,controlupdates=0;clock_t loopstart=0;std::array<std::vector<uint64_t>,2>nodes,updates,prunes,cpu;
 try{
  if(argc!=3)throw std::runtime_error("catalogue and trace paths required");
  catalogue(0,0,0);if(catalogued!=129658)throw std::runtime_error("catalogue size");
  std::ofstream catout(argv[1]),traceout(argv[2]);
  for(unsigned s=0;s<cat.size();++s){catout<<s;for(Mask mask:cat[s])catout<<' '<<mask;catout<<'\n';}
  catout.close();if(!catout||!traceout)throw std::runtime_error("output setup");
  pair_controls();controlnodes=budget.total;controlupdates=budget.updates;
  std::cout<<"# B133 paired DLX:arm,index,targets;8(size,tokens);nodes\n";loopstart=clock();
  for(unsigned index=0;index<3;++index){
   pending.clear();int x;for(int j=0;j<8;++j){if(!(std::cin>>x))throw std::runtime_error("missing input");pending.push_back(x);}
   if(!std::is_sorted(pending.begin(),pending.end())||pending.front()<68||pending.back()>122)throw std::runtime_error("input domain");
   std::array<Result,2>pair;
   for(unsigned position=0;position<2;++position){
    unsigned arm=position^(index%2);active_arm=arm;running=true;pair[arm]=run_case(28,pending,arm==1);running=false;
    const auto&r=pair[arm];if(!r.ok)throw std::runtime_error("FIRST_NO_WITNESS");
    nodes[arm].push_back(r.nodes);updates[arm].push_back(r.updates);prunes[arm].push_back(r.prunes);cpu[arm].push_back(r.micros);
    std::cout<<arm<<' '<<index<<' ';for(int t:pending)std::cout<<t<<' ';
    for(Mask mask:r.bins){std::cout<<__builtin_popcount(mask)<<' ';for(int j=0;j<28;++j)if(mask&(1u<<j))std::cout<<2*j+1<<' ';}
    std::cout<<r.nodes<<'\n';std::cout.flush();
    traceout<<arm<<' '<<index<<' '<<r.trace.size();
    for(const auto&s:r.trace)traceout<<' '<<s.used<<' '<<s.left<<' '<<s.tokens<<' '<<s.minimum<<' '<<s.rejected;
    traceout<<'\n';traceout.flush();if(!traceout||!std::cout)throw std::runtime_error("stream output");
   }
   same_results(pair[0],pair[1]);++completed;pending.clear();budget.check();
  }
  if(std::cin>>reason)throw std::runtime_error("extra input");reason.clear();status="COMPLETE_FIRST3_PAIRS";
 }catch(const Cap&e){status="UNKNOWN_CAP";reason=e.what();}
 catch(const std::exception&e){reason=e.what();status=reason=="FIRST_NO_WITNESS"?"FIRST_NO_WITNESS":"ERROR";}
 rusage rss{};getrusage(RUSAGE_SELF,&rss);
 std::cerr<<"{\"status\":\""<<status<<"\",\"reason\":\""<<reason<<"\",\"completed_pairs\":"<<completed
 <<",\"control_nodes\":"<<controlnodes<<",\"pilot_attempted_nodes\":"<<budget.total-controlnodes
 <<",\"pending_nodes\":"<<(running?budget.local:0)<<",\"pending_arm\":"<<(running?int(active_arm):-1)
 <<",\"link_updates\":"<<budget.updates<<",\"control_updates\":"<<controlupdates
 <<",\"matrices\":"<<budget.matrices<<",\"restored\":"<<budget.restored
 <<",\"built_incidences\":"<<budget.built<<",\"max_matrix_nodes\":"<<budget.max_matrix_nodes
 <<",\"cpu_seconds\":"<<double(clock()-budget.start)/CLOCKS_PER_SEC
 <<",\"search_loop_cpu_seconds\":"<<(loopstart?double(clock()-loopstart)/CLOCKS_PER_SEC:0)
 <<",\"rss_native\":"<<rss.ru_maxrss<<",\"pending_target\":[";
 for(size_t i=0;i<pending.size();++i)std::cerr<<(i?",":"")<<pending[i];
 auto arrays=[&](const char*name,const std::array<std::vector<uint64_t>,2>&values){
  std::cerr<<"],\""<<name<<"\":[";
  for(int a=0;a<2;++a){if(a)std::cerr<<',';std::cerr<<'[';for(size_t i=0;i<values[a].size();++i)std::cerr<<(i?",":"")<<values[a][i];std::cerr<<']';}
 };
 arrays("query_nodes",nodes);arrays("query_updates",updates);arrays("query_prunes",prunes);arrays("query_cpu_us",cpu);
 std::cerr<<"]}\n";return status=="COMPLETE_FIRST3_PAIRS"?0:2;
}
