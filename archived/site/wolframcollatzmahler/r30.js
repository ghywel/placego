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
/* ---- decoration: glyphs, ribbons, door art, the hero reader. Appended for the redesign of 2026-10-11. ---- */
(function(){
"use strict";
const R=window.R30, css=n=>getComputedStyle(document.documentElement).getPropertyValue(n).trim();
const INK=()=>css("--ink")||"#14181d", CREAM=()=>css("--cream")||"#f4eedf", EMBER=()=>css("--ember")||"#d9542b",
      TEAL=()=>css("--teal")||"#1f7a8c", GOLD=()=>css("--gold")||"#d8a21c", GREEN=()=>css("--green")||"#2f8f5b";
function rows30(W,T,seedRow){let r=seedRow||(()=>{const a=new Uint8Array(W);a[W>>1]=1;return a;})();const out=[r];for(let t=1;t<T;t++){r=R.step(r,0,0);out.push(r);}return out;}
function randomRow(W,seed){let x=seed>>>0||1;const a=new Uint8Array(W);for(let i=0;i<W;i++){x^=x<<13;x>>>=0;x^=x>>>17;x^=x<<5;x>>>=0;a[i]=x&1;}return a;}
// glyph kinds: pyramid, cones, strip, wheel, coin, ring, collatz, circle, map, trove, join, people
function glyph(canvas,kind,colour){
  const s=16;canvas.width=s*4;canvas.height=s*4;const ctx=canvas.getContext("2d");const n=canvas.width;
  ctx.fillStyle=INK();ctx.fillRect(0,0,n,n);const fg=colour||CREAM(),ac=EMBER();
  const cell=(x,y,c)=>{ctx.fillStyle=c||fg;ctx.fillRect(x*4,y*4,4,4);};
  if(kind==="pyramid"){const rs=rows30(16,8);for(let t=0;t<8;t++)for(let i=0;i<16;i++)if(rs[t][i])cell(i,t+4,i===8?ac:fg);}
  else if(kind==="cones"){for(let y=0;y<16;y++)for(let x=0;x<16;x++){if(x>=8&&x<8+Math.max(0,8-Math.abs(y-8)))cell(x,y,GREEN());else if((x+y)%3===0)cell(x,y,"#3a4450");}cell(7,0,ac);for(let y=1;y<16;y++)cell(7,y,ac);}
  else if(kind==="strip"){for(let x=0;x<16;x++)cell(x,7,(x*7)%3?fg:"#3a4450");}
  else if(kind==="wheel"){for(let k=0;k<56;k+=2){const a=k*17/56*2*Math.PI;cell(8+Math.round(6*Math.cos(a)),8+Math.round(6*Math.sin(a)),k%14?fg:ac);}}
  else if(kind==="coin"){const rs=rows30(41,16);for(let t=0;t<16;t++)cell(t,8,rs[t][20]?fg:"#3a4450");}
  else if(kind==="ring"){for(let k=0;k<24;k++){const a=k/24*2*Math.PI;cell(8+Math.round(6.5*Math.cos(a)),8+Math.round(6.5*Math.sin(a)),k%3?fg:"#3a4450");}}
  else if(kind==="collatz"){let v=27,x=0;const pts=[];while(x<16){pts.push(v);v=v%2?(3*v+1)/2:v/2;x++;}const mx=Math.max(...pts);pts.forEach((p,i)=>cell(i,15-Math.round(p/mx*13),TEAL()));}
  else if(kind==="circle"){for(let k=0;k<40;k++){const a=k/40*2*Math.PI;cell(8+Math.round(6.5*Math.cos(a)),8+Math.round(6.5*Math.sin(a)),a<Math.PI?GOLD():"#3a4450");}let x=.37;for(let i=0;i<6;i++){const a=x*2*Math.PI;cell(8+Math.round(4*Math.cos(a)),8+Math.round(4*Math.sin(a)),ac);x=(x*1.5)%1;}}
  else if(kind==="map"){for(let y=2;y<14;y+=4)for(let x=2;x<14;x++)cell(x,y,(x+y)%5?"#3a4450":fg);cell(13,13,ac);cell(2,2,GREEN());cell(8,6,TEAL());}
  else if(kind==="trove"){for(let y=4;y<13;y++)for(let x=3;x<13;x++)if(y===4||y===12||x===3||x===12)cell(x,y,fg);for(let y=6;y<11;y+=2)for(let x=5;x<11;x+=2)cell(x,y,GOLD());}
  else if(kind==="join"){for(let x=2;x<14;x++)cell(x,8,"#3a4450");cell(3,8,fg);cell(7,8,fg);cell(11,8,fg);cell(12,7,ac);cell(13,8,ac);cell(12,9,ac);}
  else if(kind==="people"){[[4,6],[8,6],[12,6]].forEach(([x,y],i)=>{cell(x,y,i===0?ac:fg);cell(x-1,y+2,i===0?ac:fg);cell(x,y+2,i===0?ac:fg);cell(x+1,y+2,i===0?ac:fg);cell(x,y+3,i===0?ac:fg);});}
  else{const rs=rows30(16,8);for(let t=0;t<8;t++)for(let i=0;i<16;i++)if(rs[t][i])cell(i,t+4);}
}
function ribbon(canvas,seed){const W=Math.max(240,Math.floor((canvas.clientWidth||900)/4)),T=6;canvas.width=W;canvas.height=T;const ctx=canvas.getContext("2d");
  ctx.fillStyle=INK();ctx.fillRect(0,0,W,T);const rs=rows30(W,T,randomRow(W,seed||2026));ctx.fillStyle="#5b6672";
  for(let t=0;t<T;t++)for(let i=0;i<W;i++)if(rs[t][i])ctx.fillRect(i,t,1,1);}
function doorArt(canvas,kind){const W=300,H=96;canvas.width=W;canvas.height=H;const ctx=canvas.getContext("2d");ctx.fillStyle=INK();ctx.fillRect(0,0,W,H);
  if(kind==="pyramid"){const rs=rows30(W,H);ctx.fillStyle=CREAM();for(let t=0;t<H;t++)for(let i=0;i<W;i++)if(rs[t][i])ctx.fillRect(i,t,1,1);ctx.fillStyle=EMBER();for(let t=0;t<H;t++)if(rs[t][W>>1])ctx.fillRect(W>>1,t,1,1);}
  else if(kind==="map"){ctx.fillStyle="#2a323b";for(let y=0;y<H;y+=8)for(let x=0;x<W;x+=8)if(((x/8+y/8)*7)%11<4)ctx.fillRect(x+2,y+2,4,4);
    const cols=[GREEN(),TEAL(),EMBER()];for(let k=0;k<3;k++){ctx.fillStyle=cols[k];ctx.fillRect(40+k*90,30,70,36);}ctx.fillStyle=INK();ctx.font="bold 11px Inter,system-ui,sans-serif";["PROVED","MEASURED","OPEN"].forEach((w,k)=>ctx.fillText(w,48+k*90,52));}
  else if(kind==="need"){ctx.fillStyle="#2a323b";for(let x=0;x<W;x+=10)ctx.fillRect(x,48,6,1);const r=rows30(60,40,randomRow(60,7));ctx.fillStyle=CREAM();for(let t=0;t<40;t++)for(let i=0;i<60;i++)if(r[t][i])ctx.fillRect(20+i*2,8+t*2,2,2);
    ctx.fillStyle=EMBER();ctx.fillRect(150,8,2,80);ctx.fillStyle=GOLD();ctx.font="bold 12.5px Inter,system-ui,sans-serif";ctx.fillText("R(d) < ∞, every d?",160,54);}
}
function heroReader(art,reader,tally,T){ // the big pyramid on ink with the centre column read off below as coin flips
  if(!art)return;const W=2*T+1,s=2;art.width=W*s;art.height=T*s;const ctx=art.getContext("2d");
  const rctx=reader.getContext("2d");const n=120;reader.width=n*6;reader.height=18;
  let row=new Uint8Array(W);row[T]=1;const rows=[row];let t=0,live=false,timer=null,black=0;
  const reduced=matchMedia("(prefers-reduced-motion: reduce)").matches;
  const draw=()=>{ctx.fillStyle=INK();ctx.fillRect(0,0,art.width,art.height);ctx.fillStyle=CREAM();
    for(let tt=0;tt<rows.length;tt++){const r=rows[tt];for(let i=0;i<W;i++)if(r[i]&&i!==T)ctx.fillRect(i*s,tt*s,s,s);}
    ctx.fillStyle=EMBER();for(let tt=0;tt<rows.length;tt++)if(rows[tt][T])ctx.fillRect(T*s,tt*s,s,s);ctx.fillStyle="rgba(217,84,43,.25)";ctx.fillRect(T*s,0,s,art.height);
    rctx.fillStyle=INK();rctx.fillRect(0,0,reader.width,reader.height);black=0;
    for(let k=0;k<Math.min(rows.length,n);k++){const b=rows[k][T];black+=b;rctx.fillStyle=b?EMBER():"#3a4450";rctx.fillRect(k*6+1,3,4,12);}
    if(tally)tally.innerHTML="centre column so far: <b>"+black+"</b> black, <b>"+(Math.min(rows.length,n)-black)+"</b> white, of "+Math.min(rows.length,n);};
  const tick=()=>{if(!live)return;if(t<T-1){rows.push(R.step(rows[t],0,0));t++;draw();}else{rows.length=1;t=0;draw();}};
  draw();if(reduced){while(t<T-1){rows.push(R.step(rows[t],0,0));t++;}draw();return;}
  R.onScreen(art,v=>{live=v;if(v&&!timer)timer=setInterval(tick,28);else if(!v&&timer){clearInterval(timer);timer=null;}});
}
function decorate(){
  document.querySelectorAll("h2").forEach(h=>{if(h.querySelector("canvas.glyph"))return;const c=document.createElement("canvas");c.className="glyph";c.setAttribute("aria-hidden","true");
    glyph(c,h.dataset.glyph||"pyramid");h.insertBefore(c,h.firstChild);});
  document.querySelectorAll("canvas.ribbon").forEach((c,i)=>ribbon(c,2026+i*7));
  document.querySelectorAll("canvas.door-art").forEach(c=>doorArt(c,c.dataset.art));
  document.querySelectorAll("canvas.panel-glyph").forEach(c=>glyph(c,c.dataset.glyph));
  document.querySelectorAll("canvas.brand-mark").forEach(c=>{c.width=28;c.height=16;const x=c.getContext("2d");x.fillStyle=INK();x.fillRect(0,0,28,16);const rs=rows30(28,8);x.fillStyle=CREAM();for(let t=0;t<8;t++)for(let i=0;i<28;i++)if(rs[t][i])x.fillRect(i,t+4,1,1);x.fillStyle=EMBER();for(let t=0;t<8;t++)if(rs[t][14])x.fillRect(14,t+4,1,1);});
}
Object.assign(R,{glyph,ribbon,doorArt,heroReader,decorate});
if(document.readyState==="loading")document.addEventListener("DOMContentLoaded",decorate);else decorate();
})();
