// Bounded hardware applicability benchmark, not a new mathematical experiment.
#import <Foundation/Foundation.h>
#import <Metal/Metal.h>
#import <dispatch/dispatch.h>
#include <sys/resource.h>
#include <chrono>
#include <thread>
#include <algorithm>
#include <vector>
#include <string>
#include <stdexcept>
#include <cstring>
#include <cstdio>
using Clock=std::chrono::steady_clock;
static double wall(){return std::chrono::duration<double>(Clock::now().time_since_epoch()).count();}
static double cpu(){struct rusage r;getrusage(RUSAGE_SELF,&r);return r.ru_utime.tv_sec+r.ru_utime.tv_usec*1e-6+r.ru_stime.tv_sec+r.ru_stime.tv_usec*1e-6;}
static void require(bool ok,const char *why){if(!ok)throw std::runtime_error(why);}
static void emit(NSDictionary *d){NSData *b=[NSJSONSerialization dataWithJSONObject:d options:0 error:nil];fwrite(b.bytes,1,b.length,stdout);putchar('\n');fflush(stdout);}
static uint32_t mix(uint32_t x){x^=x>>16;x*=0x7feb352dU;x^=x>>15;x*=0x846ca68bU;x^=x>>16;return x;}
static uint32_t packed(uint32_t x,uint32_t steps){for(uint32_t t=0;t<steps;t++)x^=((x<<1)|(x>>31))|((x<<2)|(x>>30));return x;}
// Independent literal-cell oracle: no word shifts/rotates in the update.
static uint32_t literal(uint32_t x,uint32_t steps){bool a[32],b[32];for(int j=0;j<32;j++)a[j]=(x>>j)&1;for(uint32_t t=0;t<steps;t++){for(int j=0;j<32;j++)b[j]=a[j]^(a[(j+31)%32]|a[(j+30)%32]);std::copy(b,b+32,a);}uint32_t y=0;for(int j=0;j<32;j++)y|=uint32_t(a[j])<<j;return y;}
struct Params {uint32_t n,steps;};
static double gpuTotal=0;
static void finish(id<MTLCommandBuffer> cb,double start){
    [cb commit];[cb waitUntilCompleted];
    require(cb.status==MTLCommandBufferStatusCompleted,"METAL_COMMAND_FAILED");
    double elapsed=wall()-start,gt=cb.GPUEndTime-cb.GPUStartTime;
    require(gt>0 && gt<0.100,"GPU_TIMESTAMP_OR_LATENCY_STOP");
    gpuTotal+=gt;
    require(elapsed<0.500 && gpuTotal<3.0,"GPU_TRANSACTION_OR_TOTAL_STOP");
}
static uint64_t digest(const std::vector<uint32_t>& v){uint64_t h=1469598103934665603ULL;for(auto x:v){h^=x;h*=1099511628211ULL;}return h;}
static void cpuTraj(const std::vector<uint32_t>& in,std::vector<uint32_t>& out,uint32_t steps,unsigned threads){
    const uint32_t *a=in.data();uint32_t *b=out.data();size_t n=in.size();
    auto part=[&](unsigned k){for(size_t i=n*k/threads;i<n*(k+1)/threads;i++)b[i]=packed(a[i],steps);};
    if(threads==1)part(0);else dispatch_apply(threads,dispatch_get_global_queue(QOS_CLASS_UTILITY,0),^(size_t k){part((unsigned)k);});
}
static void cpuGraph(const std::vector<uint32_t>& dst,const std::vector<int32_t>& weights,
                     const std::vector<int32_t>& initial,std::vector<int32_t>& old,
                     std::vector<int32_t>& next,std::vector<uint32_t>& result,uint32_t steps,unsigned threads){
    // Workspace is preallocated for every backend; time copying the input/result.
    std::copy(initial.begin(),initial.end(),old.begin());size_t n=old.size();
    for(uint32_t s=0;s<steps;s++){
        const int32_t *v=old.data();int32_t *o=next.data();const uint32_t *d=dst.data();const int32_t *w=weights.data();
        auto part=[&](unsigned k){for(size_t i=n*k/threads;i<n*(k+1)/threads;i++){int32_t best=1000000000;for(size_t e=4*i;e<4*i+4;e++)if(v[d[e]]<1000000000)best=std::min(best,w[e]+v[d[e]]);o[i]=best;}};
        if(threads==1)part(0);else dispatch_apply(threads,dispatch_get_global_queue(QOS_CLASS_UTILITY,0),^(size_t k){part((unsigned)k);});
        old.swap(next);
    }std::memcpy(result.data(),old.data(),n*sizeof(int32_t));
}
static void graphOracle(const std::vector<uint32_t>& dst,const std::vector<int32_t>& w,
                        const std::vector<int32_t>& init,std::vector<int32_t>& result,uint32_t steps){
    std::vector<int64_t> a(init.begin(),init.end()),b(a.size());
    for(uint32_t s=0;s<steps;s++){std::fill(b.begin(),b.end(),1000000000);for(size_t e=0;e<dst.size();e++)if(a.at(dst[e])<1000000000)b.at(e/4)=std::min(b.at(e/4),a.at(dst[e])+w[e]);a.swap(b);}
    result.assign(a.begin(),a.end());
}
static void bench(id<MTLDevice> dev,id<MTLCommandQueue> queue,id<MTLComputePipelineState> pipe,
                  bool traj,uint32_t n,uint32_t steps,int reps){
    @autoreleasepool {
    const size_t nb=size_t(n)*4;size_t declared=traj?2*nb:10*nb;
    require(declared<=128ULL*1024*1024,"TASK_BUFFER_CAP");
    std::vector<uint32_t> input(n),dst(4*n),got(n),expected(n);
    std::vector<int32_t> weights(4*n),init(n),gr,workspaceA(n),workspaceB(n);
    for(uint32_t i=0;i<n;i++){input[i]=mix(i+9173);init[i]=int32_t(mix(i+41)%201)-100;for(uint32_t k=0;k<4;k++){size_t e=4*i+k;dst[e]=mix(uint32_t(e)+193)%n;weights[e]=int32_t(mix(uint32_t(e)+17)%5)-2;}}
    // Frozen special controls: zeros/ones/alternating/singletons/high-bit wrap and INF.
    uint32_t special[]={0,~0U,0xaaaaaaaaU,0x55555555U,1,0x80000000U,3,0xc0000000U};
    for(size_t j=0;j<std::min(size_t(n),size_t(8));j++)input[j]=special[j];
    init[0]=1000000000;
    if(traj){for(uint32_t i=0;i<n;i++)expected[i]=packed(input[i],steps);for(uint32_t i=0;i<std::min(n,256U);i++)require(expected[i]==literal(input[i],steps),"LITERAL_ORACLE_FAILED");}
    else {graphOracle(dst,weights,init,gr,steps);std::memcpy(expected.data(),gr.data(),nb);}
    id<MTLBuffer> a=[dev newBufferWithLength:nb options:MTLResourceStorageModeManaged];
    id<MTLBuffer> b=[dev newBufferWithLength:nb options:MTLResourceStorageModeManaged];
    id<MTLBuffer> d=traj?nil:[dev newBufferWithLength:4*nb options:MTLResourceStorageModeManaged];
    id<MTLBuffer> w=traj?nil:[dev newBufferWithLength:4*nb options:MTLResourceStorageModeManaged];
    require(a&&b&&(traj||(d&&w)),"BUFFER_ALLOCATION_FAILED");
    require(dev.currentAllocatedSize<=128ULL*1024*1024,"DEVICE_ALLOCATION_CAP");
    // Poison initial output to make a missing first download/update observable.
    std::memset(b.contents,0xa5,nb);[b didModifyRange:NSMakeRange(0,nb)];
    Params p{n,steps};
    emit(@{@"event":@"case",@"kind":traj?@"trajectory":@"graph",@"n":@(n),@"steps":@(steps),@"task_buffer_bytes":@(declared),@"device_current_allocated_bytes":@(dev.currentAllocatedSize),@"expected_digest":@(digest(expected))});
    // Warm-up plus five/three declared repeats; reverse order every other repeat.
    for(int rep=-1;rep<reps;rep++)for(int pos=0;pos<4;pos++){
        int arm=(rep>=0 && rep%2)?3-pos:pos;unsigned threads=arm==0?1:arm==1?2:4;
        double start=wall(),ct=cpu(),gt=0;
        if(arm<3){
            if(traj)cpuTraj(input,got,steps,threads);
            else cpuGraph(dst,weights,init,workspaceA,workspaceB,got,steps,threads);
        } else {
            // End-to-end transaction includes host copies, managed upload, encoding,
            // all steps, managed download, queue completion and final result copy.
            std::memcpy(a.contents,traj?(const void*)input.data():(const void*)init.data(),nb);[a didModifyRange:NSMakeRange(0,nb)];
            if(!traj){std::memcpy(d.contents,dst.data(),4*nb);[d didModifyRange:NSMakeRange(0,4*nb)];std::memcpy(w.contents,weights.data(),4*nb);[w didModifyRange:NSMakeRange(0,4*nb)];}
            id<MTLCommandBuffer> cb=[queue commandBuffer];require(cb!=nil,"COMMAND_BUFFER_FAILED");
            id<MTLBuffer> in=a,out=b;
            for(uint32_t s=0;s<(traj?1:steps);s++){
                id<MTLComputeCommandEncoder> enc=[cb computeCommandEncoder];[enc setComputePipelineState:pipe];
                if(traj){[enc setBuffer:in offset:0 atIndex:0];[enc setBuffer:out offset:0 atIndex:1];[enc setBytes:&p length:sizeof(p) atIndex:2];}
                else {[enc setBuffer:d offset:0 atIndex:0];[enc setBuffer:w offset:0 atIndex:1];[enc setBuffer:in offset:0 atIndex:2];[enc setBuffer:out offset:0 atIndex:3];[enc setBytes:&p length:sizeof(p) atIndex:4];}
                NSUInteger tg=std::min(NSUInteger(128),pipe.maxTotalThreadsPerThreadgroup);
                [enc dispatchThreadgroups:MTLSizeMake((n+tg-1)/tg,1,1) threadsPerThreadgroup:MTLSizeMake(tg,1,1)];[enc endEncoding];
                if(!traj){id<MTLBuffer> tmp=in;in=out;out=tmp;}
            }
            id<MTLBuffer> result=traj?b:in;
            id<MTLBlitCommandEncoder> blit=[cb blitCommandEncoder];[blit synchronizeResource:result];[blit endEncoding];
            finish(cb,start);gt=cb.GPUEndTime-cb.GPUStartTime;
            std::memcpy(got.data(),result.contents,nb);
        }
        double elapsed=wall()-start,used=cpu()-ct;
        require(got==expected,"OUTPUT_DISAGREEMENT");
        emit(@{@"event":@"sample",@"kind":traj?@"trajectory":@"graph",@"n":@(n),@"steps":@(steps),@"rep":@(rep),@"backend":arm<3?@"cpu":@"metal",@"threads":arm<3?@(threads):@0,@"wall_ms":@(elapsed*1000),@"cpu_ms":@(used*1000),@"gpu_command_ms":@(gt*1000),@"checked_all_outputs":@YES});
        std::this_thread::sleep_for(std::chrono::milliseconds(20));
    }
    }
}
int main(int argc,char**argv){@autoreleasepool{try{
    require(argc==3,"usage: scope metal-source-or-metallib inventory|prepare|pilot|benchmark");
    NSArray<id<MTLDevice>> *devices=MTLCopyAllDevices();id<MTLDevice> dev=nil;
    for(id<MTLDevice> d in devices){emit(@{@"event":@"device",@"name":d.name,@"low_power":@(d.lowPower),@"removable":@(d.removable),@"unified_memory":@(d.hasUnifiedMemory),@"recommended_working_set_bytes":@(d.recommendedMaxWorkingSetSize),@"current_allocated_bytes":@(d.currentAllocatedSize)});if([d.name containsString:@"RX 6600"]){require(!dev,"AMBIGUOUS_RX6600");dev=d;}}
    require(dev!=nil,"RX6600_NOT_FOUND");
    if(std::string(argv[2])=="inventory")return 0;
    require(std::string(argv[2])=="prepare"||std::string(argv[2])=="pilot"||std::string(argv[2])=="benchmark","BAD_MODE");
    NSError *error=nil;double setup=wall();
    id<MTLLibrary> lib=nil;
    if([@(argv[1]) hasSuffix:@".metal"]){
        NSString *source=[NSString stringWithContentsOfFile:@(argv[1]) encoding:NSUTF8StringEncoding error:&error];require(source!=nil,"SOURCE_READ_FAILED");
        MTLCompileOptions *options=[MTLCompileOptions new];options.languageVersion=MTLLanguageVersion2_3;
        lib=[dev newLibraryWithSource:source options:options error:&error];
    }else lib=[dev newLibraryWithURL:[NSURL fileURLWithPath:@(argv[1])] error:&error];
    if(!lib)emit(@{@"event":@"compiler_error",@"error":error.localizedDescription?:@"unknown"});
    require(lib!=nil,"LIBRARY_COMPILE_OR_LOAD_FAILED");
    id<MTLComputePipelineState> tp=[dev newComputePipelineStateWithFunction:[lib newFunctionWithName:@"trajectories"] error:&error];
    id<MTLComputePipelineState> gp=[dev newComputePipelineStateWithFunction:[lib newFunctionWithName:@"graph_min"] error:&error];require(tp&&gp,"PIPELINE_COMPILE_FAILED");
    id<MTLCommandQueue> q=[dev newCommandQueue];require(q!=nil,"QUEUE_FAILED");
    emit(@{@"event":@"setup",@"selected":dev.name,@"setup_ms":@((wall()-setup)*1000),@"trajectory_execution_width":@(tp.threadExecutionWidth),@"graph_execution_width":@(gp.threadExecutionWidth),@"current_allocated_bytes":@(dev.currentAllocatedSize)});
    if(std::string(argv[2])=="prepare")return 0;
    bool pilot=std::string(argv[2])=="pilot";
    // Non-multiple of group and CPU partition sizes checks padded boundaries.
    bench(dev,q,tp,true,33,128,pilot?3:5);bench(dev,q,gp,false,33,1,pilot?3:5);
    std::vector<uint32_t> sizes=pilot?std::vector<uint32_t>{4096}:std::vector<uint32_t>{4096,262144};
    for(auto n:sizes){bench(dev,q,tp,true,n,128,pilot?3:5);bench(dev,q,gp,false,n,1,pilot?3:5);bench(dev,q,gp,false,n,32,pilot?3:5);}
    emit(@{@"event":@"complete",@"gpu_total_s":@(gpuTotal),@"current_allocated_bytes":@(dev.currentAllocatedSize),@"process_cpu_s":@(cpu())});return 0;
}catch(const std::exception&e){emit(@{@"event":@"failure",@"reason":@(e.what()),@"gpu_total_s":@(gpuTotal)});return 2;}}}
