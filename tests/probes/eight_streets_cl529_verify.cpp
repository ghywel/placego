/* MI624: independent COMPLETE verification of the existing CL529 finite basis.
Record searched: CL529 AND basis|receipt|check ->13 hits/6 files.
Prediction: for h=0..6 all long-window queries and all H(h)-admitted
short-pool queries have disjoint triples. Exact domain: long M=10+3h,
0..h holes; short 11+h<=M<=9+3h, exactly h holes. No larger census.
Domain predictions: long717722 pools, short1779900 pools; h6 counts
621616/1528956. Twenty sorted offset pairs at each pool before filtering.
Independent controls: combinadic complete-domain bitmap; generic six-cut
admission vs explicit big-bin tests; literal physical six-token witness
verification independent of precomputed union masks; direct subset oracle
confirms any negative. Genuine negatives: 0..11 with targets26/26 (each
triple individually possible but top six total51<52), and 0..10 targets3/4.
Positive control 0,2,5 / 1,3,4 at7/8. The first negative is an actual short
ambient M16,h5 pool with holes12..16; its big-bin cut MUST exclude it.
Unexpected checks: endpoint deletions; physical translation by37 and whole
pool reflection of retained witnesses (sample every65537 successes plus
controls). Do not infer a reflected H(h) theorem.
One unchanged-source run, no patch/retry or widening. CPU120s, wall180s,
RSS512MiB, output1MiB externally enforced. Stop on first confirmed
counterexample, control failure or cap. Completed positive witnesses are
checked individually; an interrupted domain is NOT a pass. Compile with
clang++ -std=c++17 -O3 to an OUTSIDE-GIT executable; no NDEBUG needed.
Known localization carries the unbounded-M interface; this finite run
alone is not a general-hole or CL530/531 theorem. No random input.
*/
#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <stdexcept>
#include <vector>
using U=uint64_t;
U choose_[32][8], queries=0, transforms=0, longp=0, shortp=0, excluded=0, digest=1469598103934665603ULL;
void need(bool x,const char* m){if(!x)throw std::runtime_error(m);}
int pc(U x){return __builtin_popcountll(x);}
int sum(U x){int s=0;while(x){int b=__builtin_ctzll(x);s+=b;x&=x-1;}return s;}
int L(int n){return n*(n-1)/2;}
void mix(U x){digest^=x;digest*=1099511628211ULL;}
struct W{U a,b,all;};
struct Case{int a,b;std::vector<W> witnesses;};
std::vector<U> triples(int M,int s){std::vector<U> a;for(int x=0;x<=M;++x)for(int y=x+1;y<=M;++y)for(int z=y+1;z<=M;++z)if(x+y+z==s)a.push_back((1ULL<<x)|(1ULL<<y)|(1ULL<<z));return a;}
std::vector<Case> cases(int M,int h){std::vector<Case> out;for(int e=0;e<=8;++e)for(int f=std::max(e,9-e);f<=8;++f){Case c{3+3*h+e,3+3*h+f,{}};auto aa=triples(M,c.a),bb=triples(M,c.b);for(U a:aa)for(U b:bb)if(!(a&b))c.witnesses.push_back({a,b,a|b});out.push_back(std::move(c));}need(out.size()==20,"offset domain");return out;}
bool literal(U present,int a,int b){std::vector<int> v;for(int i=0;i<29;++i)if(present&(1ULL<<i))v.push_back(i);int n=v.size();for(int i=0;i<n;++i)for(int j=i+1;j<n;++j)for(int k=j+1;k<n;++k){if(v[i]+v[j]+v[k]!=a)continue;for(int p=0;p<n;++p)for(int q=p+1;q<n;++q)for(int r=q+1;r<n;++r)if(p!=i&&p!=j&&p!=k&&q!=i&&q!=j&&q!=k&&r!=i&&r!=j&&r!=k&&v[p]+v[q]+v[r]==b)return true;}return false;}
bool admitted(U present,int h,int a,int b){int X=pc(present)-6,c=sum(present)-a-b;std::array<int,3> sizes{3,3,X},sums{a,b,c};bool all=true;for(int J=1;J<7;++J){int r=0,t=0;for(int i=0;i<3;++i)if(J&(1<<i)){r+=sizes[i];t+=sums[i];}if(t<L(r)+h*r)all=false;}bool explicit_=c>=L(X)+h*X&&a+c>=L(X+3)+h*(X+3)&&b+c>=L(X+3)+h*(X+3);need(all==explicit_,"admission encoding mismatch");return all;}
void physical(U present,int M,int a,int b,const W&w,bool tr){need(pc(w.a)==3&&pc(w.b)==3&&!(w.a&w.b),"cardinality/disjointness");need((w.a|w.b)==w.all,"union mismatch");need(!(w.all&~present),"unavailable token");need(sum(w.a)==a&&sum(w.b)==b,"literal sum mismatch");if(tr){int ra=0,rb=0,ta=0,tb=0;U pa=0,pb=0;for(int x=0;x<=M;++x){if(w.a&(1ULL<<x)){ra+=M-x;ta+=x+37;pa|=1ULL<<(M-x);}if(w.b&(1ULL<<x)){rb+=M-x;tb+=x+37;pb|=1ULL<<(M-x);}}U refl=0;for(int x=0;x<=M;++x)if(present&(1ULL<<x))refl|=1ULL<<(M-x);need(ra==3*M-a&&rb==3*M-b&&ta==a+111&&tb==b+111,"physical transforms");need(!((pa|pb)&~refl)&&!(pa&pb),"reflected availability");++transforms;}}
template<class F> void holes(int n,int k,F f){need(n<=29&&k<=6&&k>=0,"domain bounds");std::vector<unsigned char> seen(choose_[n][k],0);U count=0;auto visit=[&](U H){need(pc(H)==k&&!(H>>n),"hole mask");U rank=0;int j=0;for(int i=0;i<n;++i)if(H&(1ULL<<i))rank+=choose_[i][++j];need(rank<seen.size()&&!seen[rank],"combinadic duplicate/overflow");seen[rank]=1;++count;f(H);};if(!k)visit(0);else{U H=(1ULL<<k)-1,limit=1ULL<<n;while(H<limit){visit(H);U c=H&-H,r=H+c;H=(((r^H)>>2)/c)|r;}}need(count==choose_[n][k]&&std::all_of(seen.begin(),seen.end(),[](auto x){return x==1;}),"incomplete domain");}
void query(U present,int M,U H,const Case&c){const W* found=nullptr;for(const auto&w:c.witnesses)if(!(w.all&H)){found=&w;break;}if(!found){bool independent=literal(present,c.a,c.b);std::cerr<<"FAIL M="<<M<<" H="<<H<<" a="<<c.a<<" b="<<c.b<<" independently_feasible="<<independent<<"\n";need(false,independent?"search mismatch":"confirmed counterexample");}physical(present,M,c.a,c.b,*found,queries%65537==0);++queries;mix(H);mix(c.a*64+c.b);mix(found->a);mix(found->b);}
int main(){try{for(int n=0;n<=31;++n){choose_[n][0]=1;for(int k=1;k<=7;++k)choose_[n][k]=(n?choose_[n-1][k-1]+choose_[n-1][k]:0);}U full12=(1ULL<<12)-1,full11=(1ULL<<11)-1;need(!literal(full12,26,26),"negative26/26");need(!literal(full11,3,4),"negative3/4");need(literal(full11,7,8),"positive7/8");need(!admitted(full12,5,26,26),"omitted big-bin-cut control");W control{(1ULL<<0)|(1ULL<<2)|(1ULL<<5),(1ULL<<1)|(1ULL<<3)|(1ULL<<4),0};control.all=control.a|control.b;physical(full11,10,7,8,control,true);std::cout<<"CONTROLS PASS\n"<<std::flush;
for(int h=0;h<=6;++h){U lc=0,sc=0,q0=queries;int M=10+3*h;auto cs=cases(M,h);U full=(1ULL<<(M+1))-1;for(int k=0;k<=h;++k)holes(M+1,k,[&](U H){++lc;U present=full^H;for(const auto&c:cs)query(present,M,H,c);});U expect=0;for(int k=0;k<=h;++k)expect+=choose_[M+1][k];need(lc==expect,"long count");longp+=lc;
for(int m=11+h;m<=9+3*h;++m){auto ts=cases(m,h);U all=(1ULL<<(m+1))-1;holes(m+1,h,[&](U H){++sc;U present=all^H;for(const auto&c:ts){if(admitted(present,h,c.a,c.b))query(present,m,H,c);else ++excluded;}});}U expected_short=0;for(int m=11+h;m<=9+3*h;++m)expected_short+=choose_[m+1][h];need(sc==expected_short,"short count");if(h==6)need(lc==621616&&sc==1528956,"h6 published counts");shortp+=sc;std::cout<<"h="<<h<<" long="<<lc<<" short="<<sc<<" witnesses="<<queries-q0<<" PASS\n"<<std::flush;}
need(longp==717722&&shortp==1779900,"entire finite basis counts");std::cout<<"COMPLETE long="<<longp<<" short="<<shortp<<" literal_witnesses="<<queries<<" excluded="<<excluded<<" physical_transforms="<<transforms<<" fnv64="<<std::hex<<digest<<"\n";return 0;}catch(const std::exception&e){std::cerr<<"STOP "<<e.what()<<"\n";return 1;}}
