import asyncio, sys, os, json, base64, datetime
from playwright.async_api import async_playwright
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from data import P
F='/usr/share/fonts/truetype/google-fonts/'
b=lambda n: base64.b64encode(open(F+n,'rb').read()).decode()
CSS=f"""@font-face{{font-family:P;src:url(data:font/ttf;base64,{b('Poppins-Bold.ttf')});font-weight:700}}
@font-face{{font-family:P;src:url(data:font/ttf;base64,{b('Poppins-Regular.ttf')});font-weight:400}}
@font-face{{font-family:P;src:url(data:font/ttf;base64,{b('Poppins-Medium.ttf')});font-weight:600}}
*{{margin:0;box-sizing:border-box}}body{{width:1080px;height:1350px;background:#F4F1EA;color:#141414;font-family:P;padding:90px 88px;position:relative;display:flex;flex-direction:column}}
.tag{{font-size:24px;font-weight:600;letter-spacing:3px;text-transform:uppercase;opacity:.55}}
h1{{font-size:96px;line-height:1.05;font-weight:700;margin-top:36px;letter-spacing:-2px}}
h2{{font-size:62px;line-height:1.12;font-weight:700;margin-top:26px}}
p{{font-size:40px;line-height:1.42;margin-top:30px}}
.hl{{background:linear-gradient(transparent 55%,#FFD43B 55%);padding:0 6px}}
.badge{{display:inline-block;background:#141414;color:#FFD43B;font-weight:700;font-size:44px;border-radius:999px;padding:14px 34px;margin-top:50px;align-self:flex-start}}
.facts{{display:grid;grid-template-columns:1fr 1fr;gap:22px;margin-top:46px}}
.f{{border:3px solid #141414;border-radius:24px;padding:26px 28px}}.f b{{display:block;font-size:22px;letter-spacing:2px;text-transform:uppercase;opacity:.6}}.f span{{font-size:38px;font-weight:700;line-height:1.2}}
ol{{list-style:none;counter-reset:c;margin-top:30px;padding:0}}li{{counter-increment:c;font-size:36px;line-height:1.35;margin-top:26px;padding-left:76px;position:relative}}
li:before{{content:counter(c);position:absolute;left:0;top:0;width:52px;height:52px;border-radius:50%;background:#141414;color:#F4F1EA;text-align:center;line-height:54px;font-size:28px;font-weight:700}}
.chip{{display:inline-block;background:#E5DFD1;border-radius:999px;padding:12px 26px;font-size:32px;margin:14px 12px 0 0}}
pre{{white-space:pre-wrap;font-family:P;font-size:29px;line-height:1.45;background:#fffdf8;border:3px solid #141414;border-radius:24px;padding:30px;margin-top:30px}}
.cta{{margin-top:auto;margin-bottom:70px;background:#141414;color:#F4F1EA;border-radius:26px;padding:40px;font-size:36px;line-height:1.4}}.cta b{{color:#FFD43B}}
.foot{{position:absolute;left:88px;right:88px;bottom:56px;display:flex;justify-content:space-between;font-size:22px;opacity:.6}}"""
def fmt(d):
    y,m,dd=d.split('-');return f"{dd}/{m}"
def slides(p,hoje):
    dias=None
    if p['prazo']:
        dias=(datetime.date.fromisoformat(p['prazo'])-hoje).days
    badge = ("Fecha HOJE" if dias==0 else "Fecha AMANHÃ" if dias==1 else f"Fecha em {dias} dias") if dias is not None and dias>=0 else "Inscrições abertas"
    et="".join(f"<li>{e}</li>" for e in p['etapas'][:6])
    ch="".join(f'<span class="chip">{v}</span>' for v in p['valoriza'][:5])
    v=p['valoriza']
    pr=f"Faça o papel de entrevistador(a) da {p['nome'].split(' (')[0]}. Faça UMA pergunta por vez sobre {v[0].lower()}{(' e '+v[1].lower()) if len(v)>1 else ''}. Avalie cada resposta minha pelo método STAR e diga o que faltou. Não escreva a resposta por mim."
    S=[f"""<div class="tag">Dossiê · Trainee 2027</div><h1>Trainee <span class="hl">{p['nome'].split(' (')[0]}</span> 2027</h1><p>Prazo, salário, etapas e como se preparar com IA, sem colar.</p><div class="badge">{badge}{' · '+fmt(p['prazo']) if p['prazo'] and dias is not None and dias>=0 else ''}</div>""",
       f"""<div class="tag">O básico</div><div class="facts"><div class="f"><b>Prazo</b><span>{fmt(p['prazo']) if p['prazo'] else 'Não informado'}</span></div><div class="f"><b>Salário</b><span>{p['salario']}</span></div><div class="f" style="grid-column:1/3"><b>Local</b><span>{p['local']}</span></div><div class="f" style="grid-column:1/3"><b>Quem pode</b><span style="font-size:30px;font-weight:600">{p['formacao']}</span></div></div>""",
       f"""<div class="tag">Etapas do processo</div><ol>{et}</ol>""",
       f"""<div class="tag">O que a vaga valoriza</div><h2>Prepare histórias que <span class="hl">provem</span> isto:</h2><div style="margin-top:20px">{ch}</div><p style="font-size:32px">E a IA? {p['ia']}</p>""",
       f"""<div class="tag">Treine com IA (você responde)</div><pre>{pr}</pre><div class="cta">Dossiê completo grátis, com perguntas prováveis e mais 2 prompts: <b>link na bio → Mapa Trainee 2027</b>.<br><span style="font-size:24px;opacity:.7">Fonte: descrição pública da vaga ({p['fonte'].split('/')[2]}), 12–13/10/2026. Confirme no site oficial.</span></div>"""]
    return S, badge
async def main(slugs, hoje):
    async with async_playwright() as pw:
        br=await pw.chromium.launch();pg=await br.new_page(viewport={'width':1080,'height':1350})
        for p in P:
            if p['slug'] not in slugs: continue
            S,badge=slides(p,hoje);os.makedirs(f"carrosseis/{p['slug']}",exist_ok=True)
            for i,s in enumerate(S,1):
                await pg.set_content(f"<html><head><style>{CSS}</style></head><body>{s}<div class='foot'><span>ARE-IA · Mapa Trainee 2027</span><span>{i}/5</span></div></body></html>")
                await pg.wait_for_timeout(200);await pg.screenshot(path=f"carrosseis/{p['slug']}/{i}.png")
            print(p['slug'],badge)
        await br.close()
hoje=datetime.date.fromisoformat(sys.argv[1]); slugs=sys.argv[2].split(',')
asyncio.run(main(slugs,hoje))
