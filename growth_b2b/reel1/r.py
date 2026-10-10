from playwright.sync_api import sync_playwright
scenes=[
("QUASE NINGUÉM TE ENSINOU","a usar IA no trabalho.","E o erro mais comum é colar dados de cliente no chat.","#0f172a","#fbbf24"),
("DICA 1","Anonimize antes","Troque nome, CPF e CNPJ por códigos: [CPF_1], [PESSOA_1].","#0b3b2e","#6ee7b7"),
("DICA 2","Peça com método","Cargo + objetivo + formato. Prompt vago gera resposta vaga.","#1e1b4b","#a5b4fc"),
("DICA 3","Confira a fonte","Exija a fonte oficial e leia o texto original. A decisão é sua.","#3b0d0d","#fca5a5"),
("AMOSTRA GRÁTIS","Comenta GUIA","e eu te mando a amostra do Guia Definitivo da IA.","#0f172a","#fbbf24"),
]
html="""<html><body style="margin:0;width:1080px;height:1920px;background:{bg};font-family:'DejaVu Sans',sans-serif;color:#fff;display:flex;flex-direction:column;justify-content:center;padding:0 90px;box-sizing:border-box">
<div style="font-size:44px;letter-spacing:6px;color:{ac};font-weight:700">{a}</div>
<div style="font-size:104px;line-height:1.08;font-weight:800;margin:36px 0">{b}</div>
<div style="font-size:54px;line-height:1.3;color:#e5e7eb">{c}</div>
<div style="position:absolute;bottom:150px;left:90px;font-size:40px;color:{ac}">are-ia.com · @areiacurso</div></body></html>"""
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1920})
    for i,(a,bb,c,bg,ac) in enumerate(scenes):
        pg.set_content(html.format(a=a,b=bb,c=c,bg=bg,ac=ac)); pg.screenshot(path=f's{i}.png')
