import asyncio,os
from playwright.async_api import async_playwright
async def main():
    os.makedirs('fr',exist_ok=True)
    async with async_playwright() as p:
        b=await p.chromium.launch(args=['--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader'])
        pg=await b.new_page(viewport={'width':1080,'height':1920})
        await pg.goto('file:///home/claude/city/city.html');await pg.wait_for_timeout(800)
        N=int(__import__("os").environ.get("NF","840"))
        for i in range(N):
            await pg.evaluate(f'render({i/30})')
            await pg.screenshot(path=f'fr/{i:04d}.jpg',type='jpeg',quality=88)
        await b.close()
asyncio.run(main())
