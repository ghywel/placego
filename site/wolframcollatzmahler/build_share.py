#!/usr/bin/env python3
"""build_share.py: one share image per page (1200 x 630, share/<page>.png) and the Open Graph and Twitter card
tags in each page's head that point at it.

    python3 build_share.py                      # render every page's image and refresh the meta tags
    python3 build_share.py --tags-only          # only refresh the meta tags (no browser needed)
    python3 build_share.py --chrome /path/to/chrome --fonts /dir/with/local.css

Rendering uses a headless Chromium (CHROME in the environment, --chrome, or `chromium` on the PATH). The image is a
flat composition in the site's palette: the page's kicker, its headline and its description beside a Rule 30 pyramid
grown from one black cell with the centre column in ember. Flat colours keep each PNG small.

Fonts: the site uses Source Serif 4 and Inter from Google Fonts. A headless browser that cannot reach them falls
back to the system serif and sans; to get the real faces pass --fonts DIR where DIR/local.css holds @font-face rules
for woff2 files in that directory (the README says how to make one). Nothing in DIR is committed.

Standard library only. Idempotent: running it twice leaves the pages unchanged.
"""
import argparse, html, os, re, shutil, subprocess, sys, tempfile

SITE = 'https://www.wolframcollatzmahler.com/'
HERE = os.path.dirname(os.path.abspath(__file__))
PAGES = ['index', 'learn', 'rule30/index', 'stand', 'trio', 'need', 'problems', 'trove', 'join',
         'cones', 'ring', 'wheelcentre', 'carry', 'record', 'trio-technical', 'mahler-census', 'wolfram', 'collatz', 'mahler', 'contributions']
KICKER = {'index': 'An open problem, handed to everyone', 'learn': 'Learn', 'rule30/index': 'Rule 30, worked',
          'stand': 'Where we stand', 'trio': 'Rule 30, Collatz, Mahler', 'need': 'What we need',
          'problems': 'For mathematicians', 'trove': 'The trove', 'join': 'Join', 'cones': 'Where we stand',
          'ring': 'Where we stand', 'wheelcentre': 'Where we stand', 'carry': 'Where we stand',
          'record': 'What we need', 'trio-technical': 'For mathematicians', 'mahler-census': 'Mahler', 'wolfram': 'Wolfram', 'collatz': 'Collatz', 'mahler': 'Mahler', 'contributions': 'Outside contributions'}

TEMPLATE = '''<!doctype html><html lang="en"><head><meta charset="utf-8">%(fonts)s
<style>
html,body{margin:0}body{width:1200px;height:630px;overflow:hidden;background:#14181d;color:#f4eedf;position:relative;
  font-family:"Source Serif 4",Georgia,"Liberation Serif",serif}
#bar{position:absolute;left:0;right:0;bottom:0;height:10px;background:#d9542b}
#art{position:absolute;right:52px;top:56px;width:420px;height:480px;image-rendering:pixelated}
#text{position:absolute;left:64px;top:60px;width:640px;height:470px;display:flex;flex-direction:column}
#k{font-family:"Inter","Liberation Sans",system-ui,sans-serif;font-size:21px;font-weight:700;letter-spacing:.12em;
  text-transform:uppercase;color:#d8a21c;margin:0 0 18px}
#h{font-size:66px;line-height:1.1;font-weight:600;color:#fff;margin:0 0 22px}
#d{font-family:"Inter","Liberation Sans",system-ui,sans-serif;font-size:24px;line-height:1.42;color:#cfc7b7;margin:0}
#site{position:absolute;left:64px;bottom:40px;display:flex;align-items:center;gap:14px;
  font-family:"Inter","Liberation Sans",system-ui,sans-serif;font-size:22px;font-weight:600;color:#e6dfd0;letter-spacing:.02em}
#site canvas{width:56px;height:32px;image-rendering:pixelated;border-radius:3px}
</style></head><body>
<canvas id="art" width="105" height="120"></canvas>
<div id="text"><p id="k">%(kicker)s</p><h1 id="h">%(head)s</h1><p id="d">%(desc)s</p></div>
<div id="site"><canvas id="mark" width="28" height="16"></canvas>www.wolframcollatzmahler.com</div>
<div id="bar"></div>
<script>
function step(r){const n=r.length,o=new Uint8Array(n);for(let i=0;i<n;i++){const l=i?r[i-1]:0,c=r[i],q=i+1<n?r[i+1]:0;o[i]=l^(c|q);}return o;}
(function(){const c=document.getElementById("art"),W=105,T=120,x=c.getContext("2d");x.fillStyle="#1c2127";x.fillRect(0,0,W,T);
let r=new Uint8Array(W);r[52]=1;for(let t=0;t<T;t++){for(let i=0;i<W;i++)if(r[i]){x.fillStyle=i===52?"#d9542b":"#f4eedf";x.fillRect(i,t,1,1);}r=step(r);}
const m=document.getElementById("mark"),y=m.getContext("2d");y.fillStyle="#14181d";y.fillRect(0,0,28,16);
let s=new Uint8Array(28);s[14]=1;for(let t=0;t<8;t++){for(let i=0;i<28;i++)if(s[i]){y.fillStyle=i===14?"#d9542b":"#f4eedf";y.fillRect(i,t+4,1,1);}s=step(s);}
// shrink the headline until the text block fits above the site line
const h=document.getElementById("h"),box=document.getElementById("text");let fs=66;
while(box.scrollHeight>box.clientHeight&&fs>30){fs-=2;h.style.fontSize=fs+"px";}
})();
</script></body></html>'''


def page_facts(slug):
    path = os.path.join(HERE, slug + '.html')
    s = open(path, encoding='utf-8').read()
    title = html.unescape(re.search(r'<title>(.*?)</title>', s, re.S).group(1).strip())
    m = re.search(r'<meta name="description" content="([^"]*)"', s)
    desc = html.unescape(m.group(1)) if m else title
    m = re.search(r'<h1[^>]*>(.*?)</h1>', s, re.S)
    head = html.unescape(re.sub(r'<[^>]+>', '', m.group(1))).strip() if m else title
    head = re.sub(r'\s+', ' ', head)
    return path, s, title, desc, head


W, H = 1200, 630


def crop_png(src, dst, w, h):
    """Keep the top-left w x h of an 8-bit RGB/RGBA PNG (the new headless mode's capture is a little taller
    than the window it is asked for, so the page is rendered tall and cut here). Standard library only."""
    import struct, zlib
    d = open(src, 'rb').read()
    sw, sh = struct.unpack('>II', d[16:24]); depth, ct = d[24], d[25]
    if depth != 8 or ct not in (2, 6): sys.exit('crop_png: unsupported PNG (%d-bit, colour type %d)' % (depth, ct))
    bpp = 3 if ct == 2 else 4; pos = 8; idat = b''
    while pos < len(d):
        ln, = struct.unpack('>I', d[pos:pos + 4]); typ = d[pos + 4:pos + 8]
        if typ == b'IDAT': idat += d[pos + 8:pos + 8 + ln]
        pos += 12 + ln
    raw = zlib.decompress(idat); stride = sw * bpp; prev = bytearray(stride); out = bytearray(); i = 0
    for y in range(min(h, sh)):
        f = raw[i]; line = bytearray(raw[i + 1:i + 1 + stride]); i += 1 + stride
        if f:
            for x in range(stride):
                a = line[x - bpp] if x >= bpp else 0; b = prev[x]; c = prev[x - bpp] if x >= bpp else 0
                if f == 1: line[x] = (line[x] + a) & 255
                elif f == 2: line[x] = (line[x] + b) & 255
                elif f == 3: line[x] = (line[x] + (a + b) // 2) & 255
                else:
                    p = a + b - c; pa = abs(p - a); pb = abs(p - b); pc = abs(p - c)
                    line[x] = (line[x] + (a if pa <= pb and pa <= pc else b if pb <= pc else c)) & 255
        prev = line
        row = line[:w * bpp]
        if bpp == 4: row = bytes(v for j, v in enumerate(row) if j % 4 != 3)   # drop alpha: smaller file
        out += b'\0' + row
    def chunk(t, b): return struct.pack('>I', len(b)) + t + b + struct.pack('>I', zlib.crc32(t + b) & 0xffffffff)
    png = b'\x89PNG\r\n\x1a\n' + chunk(b'IHDR', struct.pack('>IIBBBBB', w, h, 8, 2, 0, 0, 0)) \
        + chunk(b'IDAT', zlib.compress(bytes(out), 9)) + chunk(b'IEND', b'')
    open(dst, 'wb').write(png)


def render(slug, head, desc, chrome, fonts_css, outdir):
    name = slug.replace('/index', '')
    out = os.path.join(outdir, name + '.png')
    tmp = tempfile.mkdtemp(prefix='share-')
    try:
        fonts = ('<link rel="stylesheet" href="file://%s">' % os.path.abspath(fonts_css)) if fonts_css else \
            '<link href="https://fonts.googleapis.com/css2?family=Source+Serif+4:wght@600&family=Inter:wght@600;700&display=swap" rel="stylesheet">'
        page = TEMPLATE % {'fonts': fonts, 'kicker': html.escape(KICKER[slug]), 'head': html.escape(head),
                           'desc': html.escape(desc)}
        src = os.path.join(tmp, 'share.html'); open(src, 'w', encoding='utf-8').write(page)
        png = os.path.join(tmp, 'share.png')
        cmd = [chrome, '--headless=new', '--no-sandbox', '--disable-gpu', '--hide-scrollbars',
               '--window-size=%d,%d' % (W, H + 160), '--virtual-time-budget=8000', '--screenshot=' + png, 'file://' + src]
        proxy = os.environ.get('HTTPS_PROXY')
        if proxy: cmd.insert(1, '--proxy-server=' + proxy)
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        if not os.path.exists(png):
            sys.exit('render failed for %s:\n%s' % (slug, r.stderr[-2000:]))
        crop_png(png, out, W, H)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    return out


def set_tags(slug, path, s, title, desc, head):
    name = slug.replace('/index', '')
    url = SITE + ('' if slug == 'index' else slug + '.html')
    alt = 'Wolfram, Collatz, Mahler: %s, beside a Rule 30 pyramid grown from one black cell' % head.rstrip('.')
    tags = '\n'.join([
        '<meta property="og:type" content="website">',
        '<meta property="og:site_name" content="Wolfram · Collatz · Mahler">',
        '<meta property="og:title" content="%s">' % html.escape(title, quote=True),
        '<meta property="og:description" content="%s">' % html.escape(desc, quote=True),
        '<meta property="og:url" content="%s">' % url,
        '<meta property="og:image" content="%sshare/%s.png">' % (SITE, name),
        '<meta property="og:image:width" content="1200">',
        '<meta property="og:image:height" content="630">',
        '<meta property="og:image:alt" content="%s">' % html.escape(alt, quote=True),
        '<meta name="twitter:card" content="summary_large_image">',
    ])
    # drop any earlier block, then put the fresh one after the description (or the title)
    s2 = re.sub(r'\n<meta (?:property="og:[^"]*"|name="twitter:card")[^>]*>', '', s)
    anchor = re.search(r'<meta name="description" content="[^"]*">', s2) or re.search(r'<title>.*?</title>', s2, re.S)
    s2 = s2[:anchor.end()] + '\n' + tags + s2[anchor.end():]
    if s2 != s:
        open(path, 'w', encoding='utf-8').write(s2)
    return s2 != s


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--chrome', default=os.environ.get('CHROME') or shutil.which('chromium') or shutil.which('chromium-browser')
                    or shutil.which('google-chrome') or shutil.which('chrome'))
    ap.add_argument('--fonts', help='directory holding local.css and its woff2 files')
    ap.add_argument('--tags-only', action='store_true')
    ap.add_argument('--out', default=os.path.join(HERE, 'share'))
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    fonts_css = os.path.join(a.fonts, 'local.css') if a.fonts else None
    if fonts_css and not os.path.exists(fonts_css): sys.exit('no local.css in ' + a.fonts)
    if not a.tags_only and not a.chrome: sys.exit('no browser found: pass --chrome or set CHROME (or --tags-only)')
    for slug in PAGES:
        path, s, title, desc, head = page_facts(slug)
        if not a.tags_only:
            out = render(slug, head, desc, a.chrome, fonts_css, a.out)
            print('%-16s %6d bytes  %s' % (slug, os.path.getsize(out), head))
        changed = set_tags(slug, path, s, title, desc, head)
        if changed: print('%-16s tags written' % slug)


if __name__ == '__main__':
    main()
