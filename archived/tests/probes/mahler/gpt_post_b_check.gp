{
default(realprecision,38);
r=2/3; B=(1+r^4+r^15+r^21)/3;
ts=vector(5,i,B+r^(24+i)/3);
ss=vector(5,i,B/(1-r^(25+i)));
if(!(2/5<B && B<ts[1] && ts[1]<81/200),error("basic_bounds"));
if(!(ts[2]<ss[1] && ss[1]<ts[1]),error("interleaving"));
for(f=5,7, q=r^(21+f); if(ts[f-3]-ts[f-2]!=q/9,error("T_width")); if(ss[f-4]-ss[f-3]!=B*q/(3*(1-q)*(1-r*q)),error("S_width")); if((ss[f-3]-ss[f-2])/(ss[f-4]-ss[f-3])!=r*(1-q)/(1-r^2*q),error("S_ratio")));
a=(ts[2]+ss[1])/2; v1=ts[2]; v2=B+r^26*v1;
if(!(v1<a && a<v2 && v2<ss[1]),error("two_block_counterexample"));
print("ALL_EXACT_CHECKS_PASS");print("B=",B);print("T4=",ts[1]);print("T5=",ts[2]);print("S5=",ss[1]);print("midpoint=",a+0.0);print("v2=",v2+0.0);
quit(0);
}
