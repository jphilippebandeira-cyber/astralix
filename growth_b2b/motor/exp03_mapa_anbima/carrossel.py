import asyncio, base64, datetime, sys
from playwright.async_api import async_playwright
F='/usr/share/fonts/truetype/google-fonts/'
b=lambda n: base64.b64encode(open(F+n,'rb').read()).decode()
CSS=open('css.txt').read().replace('{{','{').replace('}}','}').replace("{b('Poppins-Bold.ttf')}",b('Poppins-Bold.ttf')).replace("{b('Poppins-Regular.ttf')}",b('Poppins-Regular.ttf')).replace("{b('Poppins-Medium.ttf')}",b('Poppins-Medium.ttf'))
CSS+="table{width:100%;border-collapse:collapse;margin-top:34px;font-size:34px}td{padding:26px 0;border-bottom:3px solid #141414}td.r{text-align:right;font-weight:700}"
hoje=datetime.date.fromisoformat(sys.argv[1]); dias=(datetime.date(2026,12,31)-hoje).days
S=[
f"""<div class="tag">Certificações ANBIMA 2026</div><h1>Você tem CPA-10, CPA-20 ou CEA?</h1><p>Se não concluir a transição até <span class="hl"><b>31/12/2026</b></span>, as fontes indicam que perde a certificação da trilha antiga.</p><div class="badge">Faltam {dias} dias</div>""",
"""<div class="tag">O que a sua vira</div><table><tr><td>CPA-10</td><td class="r">CPA</td></tr><tr><td>CPA-20</td><td class="r">CPA + C-Pro R</td></tr><tr><td>CEA</td><td class="r">CPA + C-Pro I*</td></tr></table><p style="font-size:28px;opacity:.7">*As fontes indicam que quem tem CEA também pode optar pela C-Pro R. Confirme no ANBIMA Edu.</p>""",
"""<div class="tag">Como concluir a transição</div><ol><li>Manter a certificação atual válida</li><li>Concluir as microcertificações obrigatórias no ANBIMA Edu (gratuitas)</li><li>Pagar a atualização anual: R$ 115 (CPA) ou R$ 325 (C-Pro). R$ 30 se o banco paga</li><li>Tudo até 31/12/2026</li></ol>""",
"""<div class="tag">Vai fazer prova nova?</div><table><tr><td>CPA · 50 questões · 70%</td><td class="r">R$ 225</td></tr><tr><td>C-Pro R · 45 questões · 32 acertos</td><td class="r">R$ 500</td></tr><tr><td>C-Pro I · 40 questões · 70%</td><td class="r">R$ 500</td></tr></table><p>Todas com 2h30, casos e <span class="hl">árvores de decisão</span>. Decorar não basta mais.</p>""",
"""<div class="tag">Estude com IA (sem colar dado de cliente)</div><pre>Monte um caso de cliente fictício (idade, objetivo, prazo, perfil de risco) e me faça decidir passo a passo, como numa árvore de decisão: em cada etapa, 3 opções. No fim, explique onde errei citando o conceito (suitability, liquidez, risco, tributação).</pre><p style="font-size:30px">A IA erra alíquotas e regras: confira no material oficial. Nunca use dados reais de clientes do banco.</p>""",
"""<div class="tag">Guia completo grátis</div><h2>Formato, pesos dos módulos e 3 prompts de estudo para cada prova.</h2><div class="cta">Link na bio → <b>are-ia.com/certificacoes-anbima-2026</b><br>Comenta <b>ANBIMA</b> que eu te mando por DM.<br><span style="font-size:22px;opacity:.7">Fontes: InfoMoney (14/05/2026), ANBIMA, TopInvest, Brito Finanças, Sindicato dos Bancários de BH. Não somos afiliados à ANBIMA. Confirme no ANBIMA Edu.</span></div>"""]
async def main():
    async with async_playwright() as pw:
        br=await pw.chromium.launch();pg=await br.new_page(viewport={'width':1080,'height':1350})
        import os;os.makedirs('slides',exist_ok=True)
        for i,s in enumerate(S,1):
            await pg.set_content(f"<html><head><style>{CSS}</style></head><body>{s}<div class='foot'><span>ARE-IA · Certificações ANBIMA</span><span>{i}/6</span></div></body></html>")
            await pg.wait_for_timeout(200);await pg.screenshot(path=f"slides/{i}.png")
        await br.close()
asyncio.run(main())
