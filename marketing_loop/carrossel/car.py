import asyncio,json,sys
from playwright.async_api import async_playwright
CSS='''*{margin:0;box-sizing:border-box}body{width:1080px;height:1350px;font-family:Inter,sans-serif;background:radial-gradient(ellipse at 50% 20%,#fff,#eceef3);color:#111;padding:110px 90px;display:flex;flex-direction:column}
.n{font-size:150px;font-weight:900;color:var(--ac);line-height:1}.h{font-size:84px;font-weight:900;letter-spacing:-2px;line-height:1.05;margin:30px 0}
.b{font-size:44px;line-height:1.4;color:#333}.box{margin-top:40px;background:#16161a;color:#e8e8ee;border-radius:30px;padding:44px;font-family:'DejaVu Sans Mono',monospace;font-size:36px;line-height:1.55}
.ft{margin-top:auto;display:flex;justify-content:space-between;font-size:30px;color:#9aa0ac;font-weight:700}.cta{background:#ffd23f;border-radius:24px;padding:50px;font-size:60px;font-weight:900;margin-top:50px;line-height:1.2}'''
async def main(spec,out):
  S=json.load(open(spec))
  async with async_playwright() as p:
    b=await p.chromium.launch();pg=await b.new_page(viewport={'width':1080,'height':1350})
    for i,s in enumerate(S['slides']):
      await pg.set_content(f"<meta charset=utf-8><style>:root{{--ac:{S['ac']}}}{CSS}</style>{s}<div class=ft><span>{S['brand']}</span><span>{i+1}/{len(S['slides'])} →</span></div>")
      await pg.screenshot(path=f"{out}_{i+1}.png")
    await b.close()
asyncio.run(main(sys.argv[1],sys.argv[2]))
