import json, subprocess, sys, html as H
from playwright.sync_api import sync_playwright
cfg=json.load(open(sys.argv[1])); name=cfg['name']; D=cfg['dur']
CSS="""body{margin:0;width:1080px;height:1920px;background:transparent;font-family:'DejaVu Sans',sans-serif}
.w{position:absolute;left:70px;right:70px;top:%dpx;text-align:center}
.t{display:inline;font-weight:800;font-size:%dpx;line-height:1.22;color:#fff;
 -webkit-box-decoration-break:clone;box-decoration-break:clone;background:rgba(0,0,0,.55);padding:6px 18px;border-radius:14px;
 text-shadow:0 3px 12px rgba(0,0,0,.6)}
.h{color:#FFD60A}"""
def page(txt,top,fs):
    # **word** => highlight
    parts=txt.split('**'); s=''.join(f'<span class="h">{H.escape(p)}</span>' if i%2 else H.escape(p) for i,p in enumerate(parts)).replace('\n','<br>')
    return f"<html><head><style>{CSS%(top,fs)}</style></head><body><div class='w'><div class='t'>{s}</div></div></body></html>"
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1920})
    for i,c in enumerate(cfg['caps']):
        pg.set_content(page(c['t'],c.get('top',1080),c.get('fs',74))); pg.screenshot(path=f'{name}_c{i}.png',omit_background=True)
    pg.set_content("<html><body style='margin:0;width:1080px;height:1920px;background:linear-gradient(180deg,rgba(0,0,0,.55) 0%,rgba(0,0,0,0) 22%,rgba(0,0,0,0) 45%,rgba(0,0,0,.65) 100%)'><div style=\"position:absolute;top:120px;left:0;right:0;text-align:center;font:700 34px 'DejaVu Sans';letter-spacing:8px;color:#FFD60A\">ARE-IA · IA NO TRABALHO</div></body></html>")
    pg.screenshot(path=f'{name}_grad.png',omit_background=True)
bgs=cfg['bg']  # list of {file, start, len}
inputs=[];filt=[];segs=[]
for k,bg in enumerate(bgs):
    inputs+=['-ss',str(bg.get('ss',0)),'-t',str(bg['len']*1.0/bg.get('speed',1)),'-i',bg['file']]
    sp=bg.get('speed',1)
    filt.append(f"[{k}:v]setpts=PTS/{sp},scale=1080:1920:force_original_aspect_ratio=increase,crop=w=1080:h=1920:x='(iw-1080)*t/{bg['len']}':y='(ih-1920)/2',eq=brightness=-0.06:saturation=1.15,fps=30,format=yuv420p,setsar=1[b{k}]")
    segs.append(f"[b{k}]")
n=len(bgs)
filt.append(''.join(segs)+f"concat=n={n}:v=1:a=0[bg]")
inputs+=['-i',f'{name}_grad.png']; gi=n
filt.append(f"[bg][{gi}:v]overlay=0:0[v0]")
last='v0'
for i,c in enumerate(cfg['caps']):
    inputs+=['-loop','1','-t',str(D),'-i',f'{name}_c{i}.png']; ii=gi+1+i
    a,e=c['a'],c['b']
    filt.append(f"[{ii}:v]format=rgba,fade=t=in:st={a}:d=0.18:alpha=1,fade=t=out:st={e-0.15}:d=0.15:alpha=1[o{i}]")
    filt.append(f"[{last}][o{i}]overlay=0:0:enable='between(t,{a},{e})'[v{i+1}]"); last=f'v{i+1}'
filt.append(f"[{last}]drawbox=x=0:y=0:w='iw*t/{D}':h=10:color=0xFFD60A@0.9:t=fill[vout]")
inputs+=['-i',cfg['music']]; ai=gi+1+len(cfg['caps'])
cmd=['ffmpeg','-y','-loglevel','error']+inputs+['-filter_complex',';'.join(filt),'-map','[vout]','-map',f'{ai}:a','-t',str(D),'-c:v','libx264','-preset','superfast','-crf','20','-c:a','aac','-b:a','160k','-shortest',f'{name}.mp4']
subprocess.run(cmd,check=True)
