{
r=2/3; B=(1+r^4+r^15+r^21)/3; t5=B+r^26/3; s5=B/(1-r^26);
a=(t5+s5)/2; c=(a-B)/r^26;
v5=(1+r^5)/3; v7=(1+r^7)/3;
if(!(v7<11/30 && 11/30<c && c<443/1200 && 443/1200<v5),error("midpoint_control"));
print("midpoint_cap=",c," v5=",v5," v7=",v7);
for(i=1,2,f=if(i==1,5,6);h=if(i==1,6,7);tf=B+r^(21+f)/3;sf=B/(1-r^(21+f));snext=B/(1-r^(22+f));p=r^(21+f+h);R=tf/(1-p);V=tf+p/3;top=tf+p/2;
if(!(tf<V && V<R && R<top && top<sf),error("nested_order"));
if(top-R!=p*(1-2*tf-p)/(2*(1-p)),error("width_identity"));
if(!(snext<tf && (1+r^5)/3<2/5),error("branch_dominance"));
print("f=",f," h=",h," lower=",R," upper=",top));
print("ALL_NESTED_ARITHMETIC_CHECKS_PASS");quit(0);
}
