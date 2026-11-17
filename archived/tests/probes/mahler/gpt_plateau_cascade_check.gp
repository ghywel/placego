{
r=2/3; P=(1+r^4+r^15)/3; Q=(1+r^4)/3; B=P+r^21/3; T4=B+r^25/3;
fixed=[1/(3*(1-r^5)),Q/(1-r^16),P/(1-r^22)];
if(fixed!=[81/211,177147/443105,12550483683/31376865305],error("fixedpoints"));
if(vecmax(fixed)>=2/5,error("dominance"));
costs=[(1+r^3)/3,(1+r^4+r^14)/3,(1+r^4+r^15+r^20)/3];
if(vecmin(costs)<=T4,error("forbidden_costs"));
if(costs[2]-T4!=r^14*(1-r-r^7-r^11)/3,error("cost2_identity"));
if(costs[3]-T4!=r^20*(1-r-r^5)/3,error("cost3_identity"));
for(f=5,6,q=r^(21+f);s=B/(1-q);top=B+q/2;w=top-s; if(!(0<w && s<top && top<=T4),error("interval_order")); if(w!=q*(1-2*B-q)/(2*(1-q)),error("width_identity")); print("f=",f," plateau_width=",w));
print("ALL_PLATEAU_ARITHMETIC_CHECKS_PASS");quit(0);
}
