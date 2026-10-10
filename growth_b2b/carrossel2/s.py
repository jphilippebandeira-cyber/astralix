import asyncio
from playwright.async_api import async_playwright
slides=[
("IA no escritório contábil: 4 cuidados","Para contadores que querem ganhar tempo sem arriscar o cliente","Arraste →"),
("1. Anonimize antes de colar","Tire nome, CPF e CNPJ do cliente do texto. Sigilo e LGPD vêm primeiro.","Dado de cliente fora do chat"),
("2. Exija a fonte","Peça a base legal e confira no site oficial. IA pode errar alíquota e interpretação.","Sem fonte, não use"),
("3. Use arquivo estruturado","OFX, XML ou XLSX dão resposta melhor que PDF escaneado.","Entrada certa, saída melhor"),
("4. A máquina prepara. Você decide.","IA organiza o rascunho. O julgamento e a assinatura são do contador.","Responsabilidade é sua"),
("Quer o método completo?","Guia em português claro com prompts por profissão, inclusive para contadores.","are-ia.com/prompts-para-contador"),
]
html=lambda t,s,f,i:f"""<html><body style='margin:0;width:1080px;height:1350px;background:#0b1220;color:#fff;font-family:Helvetica,Arial,sans-serif;display:flex;flex-direction:column;justify-content:center;padding:90px;box-sizing:border-box'>
<div style='color:#5eead4;font-size:34px;letter-spacing:4px'>ARE-IA · {i+1}/{len(slides)}</div>
<div style='font-size:86px;font-weight:800;line-height:1.1;margin:50px 0'>{t}</div>
<div style='font-size:46px;color:#cbd5e1;line-height:1.35'>{s}</div>
<div style='margin-top:70px;font-size:40px;color:#5eead4;font-weight:700'>{f}</div></body></html>"""
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(viewport={'width':1080,'height':1350})
        for i,(t,s,f) in enumerate(slides):
            await pg.set_content(html(t,s,f,i)); await pg.screenshot(path=f"c{i+1}.png")
        await b.close()
asyncio.run(main())
