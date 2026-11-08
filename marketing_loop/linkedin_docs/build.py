import json, sys, asyncio
from playwright.async_api import async_playwright
DECKS = json.load(open('decks.json'))
CSS = """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800;900&display=swap');
@page{size:1080px 1350px;margin:0}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:Inter,Arial,sans-serif;color:#111}
.s{width:1080px;height:1350px;padding:150px 80px 0;position:relative;page-break-after:always;background:linear-gradient(160deg,#fff 0%,#eef0f4 100%)}
.n{font-size:220px;font-weight:900;color:#FF6A1A;line-height:1}
.k{font-size:38px;font-weight:800;color:#FF6A1A;letter-spacing:2px;text-transform:uppercase;margin-bottom:28px}
h1{font-size:112px;font-weight:900;line-height:1.05;letter-spacing:-2px;margin-top:30px}
h2{font-size:86px;font-weight:900;line-height:1.08;letter-spacing:-1.5px;margin-bottom:34px}
p{font-size:48px;line-height:1.4;color:#333;margin-bottom:22px}
.box{background:#111;color:#f4f4f4;border-radius:22px;padding:44px 46px;font-size:43px;line-height:1.42;font-family:'Inter',monospace}
.box b{color:#FF8A45}
.tip{margin-top:36px;font-size:38px;color:#555;border-left:6px solid #FF6A1A;padding-left:22px}
.f{position:absolute;left:90px;right:90px;bottom:70px;display:flex;justify-content:space-between;font-size:32px;font-weight:600;color:#9aa0aa}
.dark{background:#111}.dark h1,.dark h2{color:#fff}.dark p{color:#ccc}
"""
def slide(s,i,n):
    t=s.get('t'); cls='s dark' if t=='end' else 's'
    h=''
    if t=='cover':
        h=f"<div class='n'>{s['num']}</div><h1>{s['title']}</h1><p style='margin-top:40px'>{s['sub']}</p>"
    else:
        if s.get('k'): h+=f"<div class='k'>{s['k']}</div>"
        h+=f"<h2>{s['title']}</h2>"
        for x in s.get('p',[]): h+=f"<p>{x}</p>"
        if s.get('box'): h+=f"<div class='box'>{s['box']}</div>"
        if s.get('tip'): h+=f"<div class='tip'>{s['tip']}</div>"
    arrow=' →' if i<n else ''
    return f"<div class='{cls}'>{h}<div class='f'><span>are-ia.com · O Guia Definitivo da IA</span><span>{i}/{n}{arrow}</span></div></div>"
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(viewport={'width':1080,'height':1350})
        for name,d in DECKS.items():
            n=len(d); html=f"<html><head><meta charset='utf-8'><style>{CSS}</style></head><body>"+''.join(slide(s,i+1,n) for i,s in enumerate(d))+"</body></html>"
            await pg.set_content(html, wait_until='networkidle')
            await pg.pdf(path=f'{name}.pdf', width='1080px', height='1350px', print_background=True)
            for i in ():
                pass #(path=f'/tmp/claude-0/prev_{name}_{i}.png', clip={'x':0,'y':1350*(i-1),'width':1080,'height':1350}, full_page=True)
        await b.close()
asyncio.run(main())
