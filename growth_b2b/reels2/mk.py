import sys, subprocess, html as H
from playwright.sync_api import sync_playwright
T="""<html><body style="margin:0;width:1080px;height:1920px;background:{bg};font-family:'DejaVu Sans',sans-serif;color:#fff;display:flex;flex-direction:column;justify-content:center;padding:0 90px;box-sizing:border-box">
<div style="font-size:42px;letter-spacing:6px;color:{ac};font-weight:700">{a}</div>
<div style="font-size:{fs}px;line-height:1.1;font-weight:800;margin:36px 0">{b}</div>
<div style="font-size:50px;line-height:1.32;color:#e5e7eb">{c}</div>
<div style="position:absolute;bottom:150px;left:90px;font-size:40px;color:{ac}">are-ia.com · @areiacurso</div></body></html>"""
def build(name, scenes):
    with sync_playwright() as p:
        b=p.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1920})
        for i,(a,bb,c,bg,ac,d) in enumerate(scenes):
            fs=100 if len(bb)<28 else 80
            pg.set_content(T.format(a=H.escape(a),b=H.escape(bb),c=H.escape(c),bg=bg,ac=ac,fs=fs)); pg.screenshot(path=f'{name}_{i}.png')
    procs=[]
    for i,s in enumerate(scenes):
        d=s[5]
        fade="" if i==0 else "fade=t=in:st=0:d=0.25,"
        procs.append(subprocess.Popen(["ffmpeg","-y","-loglevel","error","-loop","1","-framerate","30","-t",str(d),"-i",f"{name}_{i}.png","-vf",fade+"scale=1080:1920,format=yuv420p","-c:v","libx264","-preset","ultrafast",f"{name}_{i}.mp4"]))
    [q.wait() for q in procs]
    open(f"{name}.txt","w").write("".join(f"file '{name}_{i}.mp4'\n" for i in range(len(scenes))))
    subprocess.run(["ffmpeg","-y","-loglevel","error","-f","concat","-safe","0","-i",f"{name}.txt","-f","lavfi","-i","anullsrc=r=44100:cl=stereo","-shortest","-c:v","copy","-c:a","aac",f"{name}.mp4"])
A=[
("BANCO OU GRANDE EMPRESA","Sua empresa restringe IA?","Dá para usar dentro das regras. 4 cuidados.","#0f172a","#fbbf24",5),
("CUIDADO 1","Leia a política interna","Se existe regra, ela manda. Na dúvida, pergunte ao TI ou ao compliance.","#0b3b2e","#6ee7b7",5),
("CUIDADO 2","Nunca cole dado de cliente","Nome, CPF, conta, contrato: troque por códigos antes de usar qualquer IA.","#3b0d0d","#fca5a5",5),
("CUIDADO 3","Use a ferramenta aprovada","Conta pessoal com dado da empresa é risco. Use a que a empresa liberou.","#1e1b4b","#a5b4fc",5),
("CUIDADO 4","Comece pelo que não é sensível","Rascunho de e-mail, resumo de texto público, roteiro de reunião.","#0b3b2e","#6ee7b7",5),
("AMOSTRA GRÁTIS","Comenta GUIA","e eu te mando a amostra do Guia Definitivo da IA.","#0f172a","#fbbf24",4),
]
B=[
("RECÉM-FORMADO","Sem saber usar IA?","5 prompts para o primeiro emprego.","#0f172a","#fbbf24",5),
("PROMPT 1 · CURRÍCULO","Reescreva sem inventar","Reescreva este item do meu currículo com verbo de ação e resultado. Não invente dados: [texto]","#0b3b2e","#6ee7b7",5),
("PROMPT 2 · ENTREVISTA","Treine com a IA","Seja o entrevistador da vaga de [cargo]. Pergunte uma coisa por vez e dê feedback.","#1e1b4b","#a5b4fc",5),
("PROMPT 3 · E-MAIL","E-mail profissional","Escreva um e-mail curto para [pessoa] sobre [assunto]. Tom cordial, 5 linhas.","#3b0d0d","#fca5a5",5),
("PROMPT 4 · APRENDER","Aprenda rápido","Explique [tema] para quem é novo na área, com exemplo do dia a dia e 3 perguntas para eu testar.","#0b3b2e","#6ee7b7",5),
("PROMPT 5 · CONFERIR","Cheque a resposta","Liste o que você pode ter errado ou inventado acima e como eu verifico em fonte oficial.","#1e1b4b","#a5b4fc",5),
("AMOSTRA GRÁTIS","Comenta GUIA","e eu te mando a amostra do Guia Definitivo da IA.","#0f172a","#fbbf24",4),
]
build("banco",A); build("formado",B)
