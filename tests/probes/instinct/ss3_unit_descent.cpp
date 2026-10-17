// B153/MI318 engine. See ss3_unit_descent.py and notebook for preregistration.
// All n12 labelled 3^4 partitions; sorted SS targets; exact E<=2 distances.
#include <algorithm>
#include <array>
#include <chrono>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <map>
#include <queue>
#include <stdexcept>
#include <sys/resource.h>
#include <unordered_map>
#include <vector>
using namespace std;
using T = array<int,4>;
struct Group { vector<uint32_t> w; vector<char> goal;
    unordered_map<uint32_t,int> index; array<vector<int>,3> dist; };
map<T,Group> groups;
size_t partitions=0, nodes=0, visits=0;
auto began=chrono::steady_clock::now();
void check(bool x) { if(!x) throw runtime_error("instrument assertion"); }
void budget() {
    check(nodes<=2000000 && visits<=200000000);
    rusage usage{};check(getrusage(RUSAGE_SELF,&usage)==0);
    check(usage.ru_maxrss<256L*1024*1024);
    check(chrono::duration<double>(chrono::steady_clock::now()-began).count()<55);
}
bool ss(T t) {
    for(int m=1;m<16;m++) {
        int c=0,s=0; for(int j=0;j<4;j++) if(m>>j&1) {c+=3;s+=t[j];}
        if(s<c*(c-1)/2 || s>c*11-c*(c-1)/2) return false;
    } return true;
}
void add(T t,uint32_t w,bool goal) {
    if(!is_sorted(t.begin(),t.end()) || !ss(t)) return;
    auto it=groups.find(t); check(it!=groups.end());
    it->second.w.push_back(w);it->second.goal.push_back(goal);++nodes;
}
void enumerate(int x,T counts,T sums,uint32_t w) {
    if(x==12) {
        ++partitions;add(sums,w,true);
        for(int a=0;a<4;a++) for(int b=0;b<4;b++) if(a!=b) {
            T t=sums;--t[a];++t[b];add(t,w,false);
        } return;
    }
    for(int j=0;j<4;j++) if(counts[j]<3) {
        ++counts[j];sums[j]+=x;
        enumerate(x+1,counts,sums,w|(uint32_t(j)<<(2*x)));
        --counts[j];sums[j]-=x;
    }
}
int owner(uint32_t w,int x) { return w>>(2*x)&3; }
uint32_t sw(uint32_t w,int x,int y) {
    uint32_t z=owner(w,x)^owner(w,y); return w^(z<<(2*x))^(z<<(2*y));
}
// Generate every move literally, including those outside this target's E<=2 set.
template<class F> void neighbors(uint32_t w,int mode,F emit) {
    array<array<int,3>,4> bins{};T count{};
    for(int x=0;x<12;x++) bins[owner(w,x)][count[owner(w,x)]++]=x;
    for(int a=0;a<4;a++) for(int b=a+1;b<4;b++) {
        for(int x:bins[a]) for(int y:bins[b]) {
            if(mode || abs(x-y)==1) {++visits;emit(sw(w,x,y));}
        }
        if(mode==2) for(int i=0;i<3;i++) for(int j=0;j<3;j++) {
            // Omit one token from each triple; exchange the other two pairs.
            uint32_t v=w;int z=a^b;
            for(int k=0;k<3;k++) {
                if(k!=i) v^=uint32_t(z)<<(2*bins[a][k]);
                if(k!=j) v^=uint32_t(z)<<(2*bins[b][k]);
            }
            ++visits;emit(v);
        }
    }
}
T sums(uint32_t w) {T s{};for(int x=0;x<12;x++)s[owner(w,x)]+=x;return s;}
int error(uint32_t w,T t) {T s=sums(w);int e=0;for(int j=0;j<4;j++)e+=abs(s[j]-t[j]);return e;}
int main(int argc,char**argv) {try {
    rlimit cpu{60,61};check(setrlimit(RLIMIT_CPU,&cpu)==0);
    check(argc==2);ofstream out(argv[1]);check(bool(out));
    for(int a=3;a<=30;a++)for(int b=a;b<=30;b++)for(int c=b;c<=30;c++) {
        int d=66-a-b-c;T t{a,b,c,d};if(d>=c&&d<=30&&ss(t))groups[t];
    }
    enumerate(0,T{},T{},0);check(partitions==369600);budget();
    for(auto &[t,g]:groups) {
        for(size_t i=0;i<g.w.size();i++) {
            check(g.index.emplace(g.w[i],int(i)).second);
            check(error(g.w[i],t)==(g.goal[i]?0:2));
        }
        for(int mode=0;mode<3;mode++) {
            auto &d=g.dist[mode];d.assign(g.w.size(),-1);queue<int> q;
            for(size_t i=0;i<g.w.size();i++) if(g.goal[i]) {d[i]=0;q.push(i);}
            while(!q.empty()) {
                int i=q.front();q.pop();neighbors(g.w[i],mode,[&](uint32_t v) {
                    auto it=g.index.find(v);if(it==g.index.end())return;
                    int j=it->second;if(d[j]<0) {d[j]=d[i]+1;q.push(j);}
                });
                if((q.size()&255)==0)budget();
            }
            map<int,int> hist;int worst=-1,wi=-1,un=0;
            for(size_t i=0;i<g.w.size();i++)if(!g.goal[i]) {
                hist[d[i]]++;if(d[i]<0)un++;if(d[i]>worst){worst=d[i];wi=i;}
                if(mode && g.dist[mode-1][i]>=0)
                    check(d[i]>=0 && d[i]<=g.dist[mode-1][i]);
            }
            out<<"H "<<t[0]<<' '<<t[1]<<' '<<t[2]<<' '<<t[3]<<' '<<mode;
            for(auto [depth,n]:hist)out<<' '<<depth<<':'<<n;out<<'\n';
            if(un) {
                for(size_t i=0;i<g.w.size();i++)if(d[i]<0) {
                    out<<"U "<<t[0]<<' '<<t[1]<<' '<<t[2]<<' '<<t[3]<<' '<<mode<<' '<<g.w[i]<<'\n';
                    break;
                }
            }
            if(wi>=0) {
                out<<"P "<<t[0]<<' '<<t[1]<<' '<<t[2]<<' '<<t[3]<<' '<<mode<<' '<<g.w[wi];
                while(d[wi]) {
                    int next=-1;neighbors(g.w[wi],mode,[&](uint32_t v) {
                        auto it=g.index.find(v);
                        if(it!=g.index.end() && d[it->second]==d[wi]-1)next=it->second;
                    });check(next>=0);wi=next;out<<' '<<g.w[wi];
                }out<<'\n';
            }
        }
        int goals=count(g.goal.begin(),g.goal.end(),1);
        out<<"C "<<t[0]<<' '<<t[1]<<' '<<t[2]<<' '<<t[3]<<' '<<goals<<' '<<g.w.size()-goals<<'\n';
        if(t==T{7,10,23,26} || t==T{16,16,17,17}) {
            for(size_t i=0;i<g.w.size();i++) {
                out<<"D "<<t[0]<<' '<<t[1]<<' '<<t[2]<<' '<<t[3]<<' '<<g.w[i];
                for(int mode=0;mode<3;mode++)out<<' '<<g.dist[mode][i];out<<'\n';
            }
        }budget();
    }
    // Reflection of values, then reversal of bin labels keeps target sorted.
    size_t reflected=0;
    for(auto &[t,g]:groups) {
        T r{33-t[3],33-t[2],33-t[1],33-t[0]};auto &h=groups.at(r);
        for(size_t i=0;i<g.w.size();i++) {
            uint32_t v=0;for(int x=0;x<12;x++)v|=uint32_t(3-owner(g.w[i],11-x))<<(2*x);
            auto j=h.index.at(v);
            for(int mode=0;mode<3;mode++)check(g.dist[mode][i]==h.dist[mode][j]);
            ++reflected;
        }
    }
    out<<"TOTAL "<<partitions<<' '<<groups.size()<<' '<<nodes<<' '<<visits<<' '<<reflected<<'\n';
    budget();check(bool(out));return 0;
}catch(const exception&e){cerr<<e.what()<<'\n';return 2;}}
