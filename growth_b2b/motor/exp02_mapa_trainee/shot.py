import asyncio
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch()
        for name,url,w in [("idx","index.html",1200),("uni","unilever/index.html",420)]:
            pg=await b.new_page(viewport={'width':w,'height':900})
            await pg.goto("file:///home/claude/mapa-trainee/site/"+url); await pg.wait_for_timeout(800)
            await pg.screenshot(path=f"/tmp/claude-0/-home-claude-astralix/b343b4ff-0334-5065-aef6-08b9ceff0042/scratchpad/{name}.png",full_page=True)
        await b.close()
asyncio.run(main())
