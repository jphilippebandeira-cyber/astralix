import asyncio
from playwright.async_api import async_playwright
slides=[
("4 ERROS ao usar IA no trabalho","(e como evitar cada um)","Arraste →"),
("1. Colar dados de clientes no chat","Tire nome, CPF e contato antes. É questão de LGPD.","Anonimize sempre"),
("2. Pedir sem contexto","Diga seu cargo, o objetivo, o formato e o tom. Prompt vago = resposta vaga.","Contexto → resultado"),
("3. Aceitar a primeira resposta","Toda saída é rascunho. Confira fatos, números e nomes antes de enviar.","Revise sempre"),
("4. Deixar a IA decidir sobre pessoas","IA organiza informação. A decisão final é sempre humana.","Pessoas decidem"),
("Quer o método completo?","Guia em português claro, com prompts por profissão. Amostra grátis no link da bio.","are-ia.com/amostra"),
]
html=lambda t,s,f,i:f"""<html><body style='margin:0;width:1080px;height:1350px;background:#0b1220;color:#fff;font-family:Helvetica,Arial,sans-serif;display:flex;flex-direction:column;justify-content:center;padding:90px;box-sizing:border-box'>
<div style='color:#5eead4;font-size:34px;letter-spacing:4px'>ARE-IA · {i+1}/{len(slides)}</div>
<div style='font-size:92px;font-weight:800;line-height:1.08;margin:50px 0'>{t}</div>
<div style='font-size:46px;color:#cbd5e1;line-height:1.35'>{s}</div>
<div style='margin-top:70px;font-size:40px;color:#5eead4;font-weight:700'>{f}</div></body></html>"""
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/opt/pw-browsers/chromium') if False else await p.chromium.launch()
        pg=await b.new_page(viewport={'width':1080,'height':1350})
        for i,(t,s,f) in enumerate(slides):
            await pg.set_content(html(t,s,f,i)); await pg.screenshot(path=f"slide{i+1}.png")
        await b.close()
asyncio.run(main())
