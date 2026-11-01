import asyncio,json,sys,os,subprocess,html
from playwright.async_api import async_playwright
CSS='''*{box-sizing:border-box;margin:0}body{width:1080px;height:1920px;background:radial-gradient(ellipse at 50% 30%,#ffffff,#eceef3);font-family:Inter,sans-serif;color:#111;overflow:hidden;position:relative}
.stage{position:absolute;left:0;right:0;top:120px;height:1050px;display:flex;align-items:center;justify-content:center}
.sc{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;opacity:0;transform:scale(.94) translateY(30px);transition:all .45s cubic-bezier(.2,.8,.2,1)}
.sc.on{opacity:1;transform:none}
.cap{position:absolute;left:60px;right:60px;top:1260px;text-align:center;font-size:92px;font-weight:800;letter-spacing:-2px;line-height:1.08;min-height:220px}
.cap span{display:inline-block;opacity:0;transform:translateY(20px);transition:all .18s;margin:0 10px}.cap span.on{opacity:1;transform:none}
.cap .hl{color:var(--ac)}.cap .h2{color:#5b4bdb}
.icon{width:300px;height:300px;border-radius:70px;background:#16161a;display:grid;place-items:center;font-size:160px;box-shadow:0 30px 60px rgba(0,0,0,.25)}
.win{background:#16161a;color:#e8e8ee;border-radius:34px;width:860px;padding:40px 46px;box-shadow:0 30px 70px rgba(0,0,0,.25);font-size:46px}
.dots{display:flex;gap:12px;margin-bottom:30px;font-size:26px;color:#888;align-items:center}.dots i{width:20px;height:20px;border-radius:50%;display:inline-block}
.mono{font-family:'DejaVu Sans Mono',monospace;font-size:52px;line-height:1.75}
.chip{display:inline-block;padding:10px 22px;border-radius:14px;color:#fff;font-size:30px;font-weight:700;margin:6px}
.card{background:#fff;border-radius:30px;padding:40px;box-shadow:0 20px 50px rgba(0,0,0,.12);width:420px;height:560px;display:flex;flex-direction:column;justify-content:center;text-align:center;font-size:44px;font-weight:800}
.lab{font-size:34px;font-weight:900;letter-spacing:.06em;margin-bottom:20px}
.node{position:absolute;display:flex;flex-direction:column;align-items:center;gap:12px;font-weight:900;font-size:30px;letter-spacing:.05em}
.node .b{width:150px;height:150px;border-radius:36px;background:#16161a;display:grid;place-items:center;font-size:70px}
.node .t{font-size:24px;padding:6px 14px;border-radius:10px;color:#fff;font-weight:700}
.cta{background:#ffd23f;border-radius:20px;padding:40px 50px;font-size:58px;font-weight:900;text-align:center;width:880px;line-height:1.2;box-shadow:0 20px 50px rgba(0,0,0,.15)}
.brand{position:absolute;bottom:70px;left:0;right:0;text-align:center;font-size:34px;color:#9aa0ac;font-weight:600}
'''
def page(spec):
    scs=''.join(f'<div class=sc id=sc{i}>{s["v"]}</div>' for i,s in enumerate(spec['scenes']))
    js=json.dumps([{'t':s['t'],'cap':s['cap']} for s in spec['scenes']])
    return f'''<!doctype html><meta charset=utf-8><style>:root{{--ac:{spec.get("ac","#ff6a1a")}}}{CSS}</style>
<div class=stage>{scs}</div><div class=cap id=cap></div><div class=brand>{spec["brand"]}</div>
<script>const S={js};const cap=document.getElementById('cap');
S.forEach((s,i)=>{{setTimeout(()=>{{document.querySelectorAll('.sc').forEach(x=>x.classList.remove('on'));document.getElementById('sc'+i).classList.add('on');
cap.innerHTML='';const w=s.cap.split(' ');const per=(((S[i+1]?S[i+1].t:s.t+3)-s.t)*1000*0.7)/w.length;
w.forEach((x,j)=>{{const sp=document.createElement('span');let c='';if(x.startsWith('*')){{c='hl';x=x.slice(1)}}else if(x.startsWith('^')){{c='h2';x=x.slice(1)}}sp.className=c;sp.textContent=x;cap.appendChild(sp);setTimeout(()=>sp.classList.add('on'),j*per)}})}},s.t*1000+100)}});</script>'''
async def render(name,spec):
    open(name+'.html','w').write(page(spec));dur=spec['dur']
    async with async_playwright() as p:
        b=await p.chromium.launch();c=await b.new_context(viewport={'width':1080,'height':1920},record_video_dir='v_'+name,record_video_size={'width':1080,'height':1920})
        pg=await c.new_page();await pg.goto(f'file://{os.getcwd()}/{name}.html');await pg.wait_for_timeout(int(dur*1000)+900);await c.close();await b.close()
    f=[x for x in os.listdir('v_'+name) if x.endswith('.webm')][0]
    ts=[s['t'] for s in spec['scenes']]
    fc=''.join(f'[2]adelay={int(t*1000+100)}|{int(t*1000+100)},volume=0.35[b{i}];' for i,t in enumerate(ts))
    mix='[1]'+''.join(f'[b{i}]' for i in range(len(ts)))+f'amix=inputs={len(ts)+1}:normalize=0,afade=t=out:st={dur-1.5}:d=1.5[o]'
    music=f"aevalsrc='0.04*sin(2*PI*130.8*t)*(0.6+0.4*sin(2*PI*2*t))+0.03*sin(2*PI*196*t)+0.025*sin(2*PI*261.6*t)*(0.5+0.5*sin(2*PI*0.5*t))':d={dur}"
    subprocess.run(['ffmpeg','-y','-loglevel','error','-ss','0.6','-i',f'v_{name}/{f}','-f','lavfi','-i',music,'-f','lavfi','-i','sine=f=900:d=0.08','-t',str(dur),'-filter_complex',fc+mix,'-map','0:v','-map','[o]','-c:v','libx264','-pix_fmt','yuv420p','-r','30','-crf','19','-c:a','aac','-shortest',name+'.mp4'],check=True)
specs=json.load(open(sys.argv[1]))
async def main():
    for n,s in specs.items():await render(n,s)
asyncio.run(main())
