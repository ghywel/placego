/* site/open/r30.js: a small Rule 30 engine and the page's drawings. No dependencies. Every drawing animates only while
   it is on screen, and stands still if the reader prefers reduced motion. */
(function(){
"use strict";
const reduced=matchMedia&&matchMedia("(prefers-reduced-motion: reduce)").matches;
const css=n=>getComputedStyle(document.documentElement).getPropertyValue(n).trim();
function step(row,leftOut,rightOut){ // one Rule 30 step on an array of 0/1; cells outside are given
  const n=row.length,out=new Uint8Array(n);
  for(let i=0;i<n;i++){const l=i?row[i-1]:leftOut,c=row[i],r=i+1<n?row[i+1]:rightOut;out[i]=l^(c|r);}
  return out;
}
function onScreen(el,cb){ // cb(true/false) as the element enters and leaves the viewport
  if(!("IntersectionObserver" in window)){cb(true);return;}
  new IntersectionObserver(es=>es.forEach(e=>cb(e.isIntersecting)),{threshold:.05}).observe(el);
}
function fit(canvas,wCells,hCells,scale){ // size a canvas for a grid; returns the 2d context and the cell size
  const s=scale||Math.max(1,Math.floor(Math.min(900/wCells,900/hCells)));
  canvas.width=wCells*s;canvas.height=hCells*s;return [canvas.getContext("2d"),s];
}
function paintGrid(ctx,s,rows,W,colours){ // rows: array of Uint8Array of width W; colours(i,t,bit) -> fill or null
  for(let t=0;t<rows.length;t++)for(let i=0;i<W;i++){const f=colours?colours(i,t,rows[t][i]):(rows[t][i]?css("--cell"):null);
    if(f){ctx.fillStyle=f;ctx.fillRect(i*s,t*s,s,s);}}
}
// 1. The pyramid from one black cell, growing row by row; the centre column tinted.
function pyramid(canvas,T,opts){
  opts=opts||{};const W=2*T+1,[ctx,s]=fit(canvas,W,T,opts.scale);
  let row=new Uint8Array(W);row[T]=1;const rows=[row];let t=0,live=false,timer=null;
  const draw=()=>{ctx.fillStyle=css("--paper");ctx.fillRect(0,0,canvas.width,canvas.height);
    paintGrid(ctx,s,rows,W,(i,tt,b)=>b?(i===T&&opts.centre?css("--accent"):css("--cell")):(i===T&&opts.centre?css("--accent-soft"):null));};
  const tick=()=>{if(!live)return;if(t<T-1){rows.push(step(rows[t],0,0));t++;draw();}else if(opts.loop){rows.length=1;t=0;draw();}};
  draw();if(reduced){while(t<T-1){rows.push(step(rows[t],0,0));t++;}draw();return;}
  onScreen(canvas,v=>{live=v;if(v&&!timer)timer=setInterval(tick,opts.ms||40);else if(!v&&timer){clearInterval(timer);timer=null;}});
}
// 2. The rule: the eight neighbourhoods and what each gives.
function ruleTable(el){
  const cases=[[1,1,1],[1,1,0],[1,0,1],[1,0,0],[0,1,1],[0,1,0],[0,0,1],[0,0,0]];
  el.innerHTML=cases.map(c=>{const o=c[0]^(c[1]|c[2]);
    const cell=b=>`<span style="display:inline-block;width:18px;height:18px;border:1px solid var(--line);background:${b?"var(--cell)":"transparent"};margin:1px"></span>`;
    return `<div style="display:inline-block;margin:6px 10px;text-align:center;font-family:var(--sans);font-size:12px;color:var(--mute)">
      <div>${cell(c[0])}${cell(c[1])}${cell(c[2])}</div><div style="margin-top:2px">${cell(o)}</div><div>${o}</div></div>`;}).join("");
}
// 3. The centre column as a coin: heads black, tails white, read down from the seed.
function coin(canvas,n){
  const W=2*n+1;let row=new Uint8Array(W);row[n]=1;const bits=[];for(let t=0;t<n;t++){bits.push(row[n]);row=step(row,0,0);}
  const s=Math.max(4,Math.floor(900/n));canvas.width=n*s;canvas.height=s*2;const ctx=canvas.getContext("2d");
  ctx.fillStyle=css("--paper");ctx.fillRect(0,0,canvas.width,canvas.height);
  bits.forEach((b,i)=>{ctx.fillStyle=b?css("--cell"):css("--paper");ctx.fillRect(i*s,0,s,s);ctx.strokeStyle=css("--line");ctx.strokeRect(i*s+.5,.5,s-1,s-1);});
  return bits;
}
// 4. A clamped centre (the wall x_0(t) = t mod 2, or any word), a right half, and the left half the two force.
function clamped(canvas,T,W,wallWord,right,opts){
  opts=opts||{};const wall=t=>wallWord[t%wallWord.length];const Tc=T+W+2,R=W+Tc+4;
  let row=new Uint8Array(R);for(let i=0;i<right.length;i++)row[i]=right[i];
  const rights=[],c=new Uint8Array(Tc);
  for(let t=0;t<Tc;t++){rights.push(row);c[t]=row[0];row=step(row,wall(t),0);}
  let prev=new Uint8Array(Tc);for(let t=0;t<Tc;t++)prev[t]=wall(t);let prev2=c;const lefts=[];
  for(let k=1;k<=W;k++){const n=prev.length-1,cur=new Uint8Array(n);for(let t=0;t<n;t++)cur[t]=prev[t+1]^(prev[t]|prev2[t]);lefts.push(cur);prev2=prev;prev=cur;}
  const G=[];for(let t=0;t<T;t++){const g=new Uint8Array(2*W+1);for(let k=1;k<=W;k++)g[W-k]=lefts[k-1][t];g[W]=wall(t);for(let i=0;i<W;i++)g[W+1+i]=rights[t][i];G.push(g);}
  const [ctx,s]=fit(canvas,2*W+1,T,opts.scale);ctx.fillStyle=css("--paper");ctx.fillRect(0,0,canvas.width,canvas.height);
  paintGrid(ctx,s,G,2*W+1,(i,t,b)=>{if(i===W)return b?css("--accent"):css("--accent-soft");if(i===W+1&&opts.markColumn1)return b?"#2b4a9b":"#dfe5f5";return b?css("--cell"):null;});
  return {grid:G,trace:c};
}
// 5. Collatz: the parity sequence of n under T(n) = n/2 or (3n+1)/2, as a strip.
function collatzStrip(canvas,n0,steps){
  let n=BigInt(n0);const bits=[];for(let t=0;t<steps;t++){const odd=n%2n===1n;bits.push(odd?1:0);n=odd?(3n*n+1n)/2n:n/2n;if(n===1n&&t>0&&bits.length>=steps)break;}
  strip(canvas,bits);return bits;
}
// 6. Mahler: the fractional parts of xi (3/2)^n, each cell black when the part is at least 1/2.
function mahlerStrip(canvas,xi,steps){
  const bits=[];let x=xi;for(let t=0;t<steps;t++){bits.push(x-Math.floor(x)>=.5?1:0);x=(x-Math.floor(x))*1.5+Math.floor(x)*1.5;x=x-Math.floor(x);}
  // float drift is real past about 50 terms; the strip is an illustration, not an orbit computation
  strip(canvas,bits);return bits;
}
function strip(canvas,bits){const n=bits.length,s=Math.max(4,Math.floor(900/n));canvas.width=n*s;canvas.height=s;const ctx=canvas.getContext("2d");
  ctx.fillStyle=css("--paper");ctx.fillRect(0,0,canvas.width,canvas.height);bits.forEach((b,i)=>{if(b){ctx.fillStyle=css("--cell");ctx.fillRect(i*s,0,s,s);}
  ctx.strokeStyle=css("--line");ctx.strokeRect(i*s+.5,.5,s-1,s-1);});}
window.R30={step,pyramid,ruleTable,coin,clamped,collatzStrip,mahlerStrip,strip,onScreen};
})();
