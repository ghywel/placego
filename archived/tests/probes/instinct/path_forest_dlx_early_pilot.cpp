// B134/MI288: fixed B133 early-check kernel on ORIGINAL SAME2000, phased cost.
// Only total-scope CPU/wall allowance changes:30CPU/50wall,60wall watchdog.
// Unchanged200k states/query,10M total,1B updates,256MiB;no new search policy.
// OUTCOME MI289:239 literal rows/control/prefix traces pass;same old target240
// caps at200001 states. Completed construction82.4% case CPU;stop DLX tuning.
#define DLX_CPU_CAP_SECONDS 30
#define DLX_WALL_CAP_SECONDS 50
#define DLX_HOIST_LIBRARY_ONLY
#include "path_forest_dlx_hoist_pair.cpp"

using Times=std::array<uint64_t,6>;
std::string active_phase="setup";
uint64_t us(clock_t ticks){return static_cast<uint64_t>(1000000.0*ticks/CLOCKS_PER_SEC);}
struct ProfileDLX:TracedDLX{
 ProfileDLX(int m,const std::vector<int>&t):TracedDLX(m,t,true){}
 bool profiled(Times&phases){
  bool ok=false;clock_t restore_start=0;
  {
   active_phase="snapshot";auto start=clock();auto before=a;auto counts=size;phases[1]=us(clock()-start);
   active_phase="search";start=clock();ok=visit({0,(1u<<k)-1,m,required,0});phases[2]=us(clock()-start);
   active_phase="restoration";restore_start=clock();same(before,counts);++budget.restored;
   if(!picked.empty())throw std::runtime_error("picked stack restoration");
  }
  phases[3]=us(clock()-restore_start);return ok;
 }
};
struct ProfileResult{
 bool ok=false;std::vector<Mask>bins;std::vector<State>trace;Times phases{};
 uint64_t nodes=0,updates=0,prunes=0;
};
ProfileResult profile_case(const std::vector<int>&t,bool keep_trace){
 auto begin=clock();auto before_updates=budget.updates;budget.reset();ProfileResult r;
 if(t.size()!=8||std::accumulate(t.begin(),t.end(),0)!=784)throw std::runtime_error("query hypothesis");
 int required=0;for(int x:t){if(x<68||x>122)throw std::runtime_error("target domain");required+=minimum_tokens(28,x);}
 if(required>28)return r;
 clock_t destroy_start=0;
 {
  active_phase="construction";auto start=clock();ProfileDLX model(28,t);r.phases[0]=us(clock()-start);
  r.ok=model.profiled(r.phases);r.bins=model.answer;r.nodes=budget.local;
  r.updates=budget.updates-before_updates;r.prunes=model.prunes;
  if(r.ok&&!literal(28,t,r.bins))throw std::runtime_error("literal rejection");
  if(keep_trace)r.trace=model.trace;
  active_phase="destruction";destroy_start=clock();
 }
 r.phases[4]=us(clock()-destroy_start);r.phases[5]=us(clock()-begin);active_phase="output";return r;
}
int main(int argc,char**argv){
 unsigned completed=0;bool running=false;clock_t call_start=0,loopstart=0;
 std::vector<int>pending;std::string status="ERROR",reason;
 uint64_t controlnodes=0,controlupdates=0;std::vector<uint64_t>nodes,updates,prunes;std::vector<Times>phases;
 try{
  if(argc!=3)throw std::runtime_error("catalogue and prefix trace paths required");
  catalogue(0,0,0);if(catalogued!=129658)throw std::runtime_error("catalogue size");
  std::ofstream catout(argv[1]),traceout(argv[2]);
  for(unsigned s=0;s<cat.size();++s){catout<<s;for(Mask mask:cat[s])catout<<' '<<mask;catout<<'\n';}
  catout.close();if(!catout||!traceout)throw std::runtime_error("output setup");
  active_phase="controls";pair_controls();controlnodes=budget.total;controlupdates=budget.updates;
  std::cout<<"# B134 fixed early DLX m28:8 targets;8(size,tokens);nodes\n";loopstart=clock();
  for(unsigned index=0;index<2000;++index){
   pending.clear();int x;for(int j=0;j<8;++j){if(!(std::cin>>x))throw std::runtime_error("missing input");pending.push_back(x);}
   if(!std::is_sorted(pending.begin(),pending.end())||pending.front()<68||pending.back()>122)throw std::runtime_error("input domain");
   call_start=clock();running=true;auto r=profile_case(pending,index<3);running=false;
   if(!r.ok){active_phase="completed_negative";throw std::runtime_error("FIRST_NO_WITNESS");}
   nodes.push_back(r.nodes);updates.push_back(r.updates);prunes.push_back(r.prunes);phases.push_back(r.phases);
   for(int t:pending)std::cout<<t<<' ';
   for(Mask mask:r.bins){std::cout<<__builtin_popcount(mask)<<' ';for(int j=0;j<28;++j)if(mask&(1u<<j))std::cout<<2*j+1<<' ';}
   std::cout<<r.nodes<<'\n';std::cout.flush();
   if(index<3){
    traceout<<1<<' '<<index<<' '<<r.trace.size();
    for(auto s:r.trace)traceout<<' '<<s.used<<' '<<s.left<<' '<<s.tokens<<' '<<s.minimum<<' '<<s.rejected;
    traceout<<'\n';traceout.flush();
   }
   if(!std::cout||!traceout)throw std::runtime_error("output");
   ++completed;pending.clear();budget.check();
  }
  if(std::cin>>reason)throw std::runtime_error("extra input");reason.clear();status="COMPLETE_SAME_2000";
 }catch(const Cap&e){status="UNKNOWN_CAP";reason=e.what();}
 catch(const std::exception&e){reason=e.what();status=reason=="FIRST_NO_WITNESS"?"FIRST_NO_WITNESS":"ERROR";}
 rusage rss{};getrusage(RUSAGE_SELF,&rss);
 std::cerr<<"{\"status\":\""<<status<<"\",\"reason\":\""<<reason<<"\",\"completed\":"<<completed
 <<",\"control_nodes\":"<<controlnodes<<",\"pilot_attempted_nodes\":"<<budget.total-controlnodes
 <<",\"pending_nodes\":"<<(pending.empty()?0:budget.local)<<",\"pending_cpu_us\":"<<(!pending.empty()&&call_start?us(clock()-call_start):0)
 <<",\"pending_phase\":\""<<(pending.empty()?"":active_phase)<<"\",\"unfinished_native_call\":"<<(running?"true":"false")<<",\"link_updates\":"<<budget.updates<<",\"control_updates\":"<<controlupdates
 <<",\"matrices\":"<<budget.matrices<<",\"restored\":"<<budget.restored<<",\"built_incidences\":"<<budget.built
 <<",\"max_matrix_nodes\":"<<budget.max_matrix_nodes<<",\"cpu_seconds\":"<<double(clock()-budget.start)/CLOCKS_PER_SEC
 <<",\"search_loop_cpu_seconds\":"<<(loopstart?double(clock()-loopstart)/CLOCKS_PER_SEC:0)<<",\"rss_native\":"<<rss.ru_maxrss<<",\"pending_target\":[";
 for(size_t i=0;i<pending.size();++i)std::cerr<<(i?",":"")<<pending[i];
 auto array=[&](const char*name,const std::vector<uint64_t>&v){std::cerr<<"],\""<<name<<"\":[";for(size_t i=0;i<v.size();++i)std::cerr<<(i?",":"")<<v[i];};
 array("query_nodes",nodes);array("query_updates",updates);array("query_prunes",prunes);
 std::cerr<<"],\"query_phases_us\":[";
 for(size_t i=0;i<phases.size();++i){if(i)std::cerr<<',';std::cerr<<'[';for(int j=0;j<6;++j)std::cerr<<(j?",":"")<<phases[i][j];std::cerr<<']';}
 std::cerr<<"]}\n";return status=="COMPLETE_SAME_2000"?0:2;
}
