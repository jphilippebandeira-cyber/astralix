"""gen2.py - generateur de Reels V2 (1080x1920, 30 fps, rendu image par image).

Usage : python3 gen2.py specs.json [outdir]

Compatible avec le format de gen.py :
  {"NOM": {"dur": 24, "ac": "#ff6a1a", "brand": "...",
           "scenes": [{"t": 0, "v": "<html>", "cap": "texte *mot ^mot"}]}}
  - t   : debut de la scene (s)          - v   : HTML libre (comme gen.py)
  - cap : sous-titre ; *mot = surligne (boite jaune), ^mot = couleur d'accent

Options V2 (toutes facultatives) :
  niveau reel  : "handle" (filigrane), "loop" (defaut true : la derniere 0,35 s
                 reaffiche le hook -> boucle propre), "beat" (s entre punch-ins,
                 defaut 1.4), "theme" ("dark" defaut | "light"), "sfx_gain" (0-1)
  niveau scene : "kind" = html | big | gpt | wa | lock | list | cta
                 "msgs" (gpt/wa) = [{"from": "in"|"out"|"user"|"bot", "text": "...",
                                     "at": s relatif, "audio": "0:06"}]
                   at <= 0 -> message deja present (pas d'animation, pas de son)
                 "title" (wa : nom du contact ; gpt : titre de l'app)
                 "label" (badge "EXEMPLO SIMULADO" sur les ecrans simules, mettre "" pour retirer)
                 "big" (big/cta : texte principal, accepte *mot et ^mot)
                 "sub" (texte secondaire), "items" (list), "word" (cta : mot a commenter)
                 "stamp" = {"text": "X", "at": 0.6, "color": "#e11d48"} (tampon qui claque)
                 "notif" (lock : {"app": "WhatsApp", "from": "Ana", "text": "..."}), "clock" (lock)
                 "zoom" (false pour figer la camera), "focus" (0-1 : point vertical du zoom)
                 "sfx" = [{"at": s relatif, "type": "click|notif|pop|whoosh|type|send"}]
Aucune musique n'est generee : seulement des sons d'interface courts.
"""
import asyncio, json, sys, os, subprocess, wave, struct, html as H
import numpy as np
from playwright.async_api import async_playwright

W, HGT, FPS, SR = 1080, 1920, 30, 44100

CSS = r'''
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:1920px;overflow:hidden;background:var(--bg)}
body{font-family:Inter,'Noto Color Emoji',sans-serif;color:var(--fg);position:relative}
#world{position:absolute;inset:0;transform-origin:50% 50%;will-change:transform}
.sc{position:absolute;inset:0;display:none}
.sc.on{display:block}
/* ---------- compat gen.py (kind html) ---------- */
.stage{position:absolute;left:0;right:0;top:250px;height:900px;display:flex;align-items:center;justify-content:center}
.icon{width:300px;height:300px;border-radius:70px;background:#1d1d22;display:grid;place-items:center;font-size:160px;box-shadow:0 30px 60px rgba(0,0,0,.35)}
.win{background:#1d1d22;color:#e8e8ee;border-radius:34px;width:900px;padding:40px 46px;box-shadow:0 30px 70px rgba(0,0,0,.35);font-size:46px}
.dots{display:flex;gap:12px;margin-bottom:30px;font-size:26px;color:#888;align-items:center}.dots i{width:20px;height:20px;border-radius:50%;display:inline-block}
.mono{font-family:'DejaVu Sans Mono',monospace;font-size:52px;line-height:1.75}
.chip{display:inline-block;padding:10px 22px;border-radius:14px;color:#fff;font-size:30px;font-weight:700;margin:6px}
.card{background:#fff;color:#111;border-radius:30px;padding:40px;box-shadow:0 20px 50px rgba(0,0,0,.2);width:420px;height:560px;display:flex;flex-direction:column;justify-content:center;text-align:center;font-size:44px;font-weight:800}
.lab{font-size:34px;font-weight:900;letter-spacing:.06em;margin-bottom:20px}
.node{position:absolute;display:flex;flex-direction:column;align-items:center;gap:12px;font-weight:900;font-size:30px;letter-spacing:.05em}
.node .b{width:150px;height:150px;border-radius:36px;background:#1d1d22;display:grid;place-items:center;font-size:70px}
.node .t{font-size:24px;padding:6px 14px;border-radius:10px;color:#fff;font-weight:700}
.cta{background:#ffd23f;color:#111;border-radius:20px;padding:40px 50px;font-size:58px;font-weight:900;text-align:center;width:880px;line-height:1.2}
/* ---------- badge exemple ---------- */
.ex{position:absolute;top:var(--ext,212px);left:50%;transform:translateX(-50%);background:rgba(255,210,63,.95);color:#111;font-weight:900;font-size:26px;letter-spacing:.12em;padding:8px 22px;border-radius:999px;z-index:5;white-space:nowrap}
/* ---------- big ---------- */
.big{position:absolute;left:70px;right:70px;top:330px;bottom:820px;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center}
.big .t{font-size:132px;font-weight:900;letter-spacing:-4px;line-height:1.0;color:var(--fg)}
.big .s{margin-top:34px;font-size:50px;font-weight:600;color:var(--mut)}
.hl{background:#ffd23f;color:#111;padding:0 .14em;border-radius:.12em;box-decoration-break:clone;-webkit-box-decoration-break:clone}
.ac{color:var(--ac)}
/* ---------- ChatGPT simule ---------- */
.gpt{position:absolute;inset:0;background:#212121;color:#ececec}
.gpt .hd{position:absolute;top:120px;left:0;right:0;height:80px;display:flex;align-items:center;justify-content:center;gap:14px;font-size:40px;font-weight:700}
.gpt .hd small{font-size:30px;color:#9b9b9b;font-weight:500}
.gpt .body{position:absolute;left:56px;right:56px;top:300px;bottom:830px;display:flex;flex-direction:column;justify-content:center;gap:40px;overflow:hidden}
.gpt .u{align-self:flex-end;max-width:860px;background:#303030;border-radius:48px;padding:32px 44px;font-size:54px;line-height:1.28}
.gpt .a{align-self:flex-start;max-width:968px;font-size:54px;line-height:1.38;display:flex;gap:22px}
.gpt .a .av{flex:none;width:62px;height:62px;border-radius:50%;border:2px solid #555;display:grid;place-items:center;font-size:34px;margin-top:4px}
.gpt .in{position:absolute;left:46px;right:46px;bottom:700px;height:104px;border-radius:52px;background:#303030;display:flex;align-items:center;padding:0 40px;font-size:38px;color:#9b9b9b;gap:20px}
.gpt .in .tx{flex:1;color:#ececec;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.gpt .in .ph{color:#8e8e8e}
.gpt .in .go{width:70px;height:70px;border-radius:50%;background:#ececec;color:#212121;display:grid;place-items:center;font-size:40px;font-weight:900}
.caret{display:inline-block;width:4px;height:1em;background:#ececec;vertical-align:-0.15em;margin-left:4px}
.dot{display:inline-block;width:26px;height:26px;border-radius:50%;background:#ececec;vertical-align:middle}
/* ---------- WhatsApp simule ---------- */
.wa{position:absolute;inset:0;background:#0b141a;color:#e9edef}
.wa .bg{position:absolute;inset:0;background-color:#0b141a;background-image:radial-gradient(rgba(255,255,255,.035) 2px,transparent 2.5px);background-size:46px 46px}
.wa .hd{position:absolute;top:0;left:0;right:0;height:300px;background:#1f2c34;display:flex;align-items:flex-end;padding:0 40px 34px;gap:26px}
.wa .hd .ar{font-size:54px;color:#aebac1}
.wa .hd .pp{width:104px;height:104px;border-radius:50%;background:var(--ac);display:grid;place-items:center;font-size:52px;font-weight:800;color:#fff}
.wa .hd .nm{font-size:46px;font-weight:600}.wa .hd .st{font-size:32px;color:#8696a0;margin-top:4px}
.wa .body{position:absolute;left:34px;right:34px;top:390px;bottom:810px;display:flex;flex-direction:column;justify-content:flex-end;gap:16px;overflow:hidden}
.wa .m{max-width:860px;padding:22px 30px 16px;border-radius:26px;font-size:52px;line-height:1.3;position:relative;white-space:pre-line;box-shadow:0 2px 2px rgba(0,0,0,.25)}
.wa .m .tm{font-size:26px;color:#8696a0;float:right;margin:16px 0 0 22px;white-space:nowrap}
.wa .m.in{align-self:flex-start;background:#202c33;border-top-left-radius:6px}
.wa .m.out{align-self:flex-end;background:#005c4b;border-top-right-radius:6px}
.wa .m.out .tm{color:#9fd8cb}.wa .m.out .tm b{color:#53bdeb;font-weight:700}
.wa .typ{align-self:flex-start;background:#202c33;border-radius:24px;padding:26px 30px;display:flex;gap:12px}
.wa .typ i{width:18px;height:18px;border-radius:50%;background:#8696a0;display:block}
.wa .aud{display:flex;align-items:center;gap:22px;min-width:560px}
.wa .aud .pl{font-size:46px}.wa .aud .wv{flex:1;height:54px;display:flex;align-items:center;gap:5px}
.wa .aud .wv i{display:block;width:7px;border-radius:4px;background:#8696a0}
.wa .bar{position:absolute;left:24px;right:24px;bottom:690px;height:100px;display:flex;gap:16px;align-items:center}
.wa .bar .f{flex:1;height:100px;border-radius:50px;background:#202c33;display:flex;align-items:center;padding:0 36px;font-size:38px;color:#8696a0}
.wa .bar .mic{width:100px;height:100px;border-radius:50%;background:#00a884;display:grid;place-items:center;font-size:46px}
/* ---------- ecran verrouille ---------- */
.lock{position:absolute;inset:0;background:radial-gradient(ellipse at 50% 0%,#2a3a5a,#0a0d16 70%)}
.lock .ck{position:absolute;top:290px;left:0;right:0;text-align:center;font-size:250px;font-weight:300;letter-spacing:-6px;color:#f4f6ff}
.lock .dt{position:absolute;top:262px;left:0;right:0;text-align:center;font-size:44px;font-weight:600;color:#c9d0e6}
.lock .nt{position:absolute;left:50px;right:50px;top:690px;background:rgba(245,245,250,.93);color:#111;border-radius:44px;padding:34px 40px;display:flex;gap:28px;box-shadow:0 20px 50px rgba(0,0,0,.45)}
.lock .nt .ic{flex:none;width:96px;height:96px;border-radius:24px;background:#25d366;display:grid;place-items:center;font-size:56px}
.lock .nt .a{font-size:32px;color:#555;display:flex;justify-content:space-between;width:100%}
.lock .nt .f{font-size:42px;font-weight:800;margin-top:6px}.lock .nt .x{font-size:42px;margin-top:4px;line-height:1.25}
/* ---------- liste ---------- */
.lst{position:absolute;left:120px;right:120px;top:300px;bottom:800px;display:flex;flex-direction:column;justify-content:center;gap:30px}
.lst .h{font-size:64px;font-weight:900;margin-bottom:12px;letter-spacing:-1px}
.lst .it{display:flex;align-items:center;gap:30px;font-size:62px;font-weight:800;background:var(--card);border-radius:30px;padding:30px 36px}
.lst .it b{flex:none;width:86px;height:86px;border-radius:24px;background:var(--ac);color:#fff;display:grid;place-items:center;font-size:48px}
/* ---------- CTA commentaire ---------- */
.ctaw{position:absolute;left:60px;right:60px;top:300px;bottom:800px;display:flex;flex-direction:column;justify-content:center;align-items:center;gap:46px;text-align:center}
.ctaw .t{font-size:96px;font-weight:900;letter-spacing:-3px;line-height:1.02}
.ctaw .box{width:940px;height:132px;border-radius:66px;background:var(--card);display:flex;align-items:center;padding:0 22px 0 46px;gap:20px;border:3px solid var(--line)}
.ctaw .box .pp{width:84px;height:84px;border-radius:50%;background:var(--ac);flex:none}
.ctaw .box .tx{flex:1;text-align:left;font-size:58px;font-weight:900;letter-spacing:2px}
.ctaw .box .ph{color:var(--mut);font-weight:500;letter-spacing:0;font-size:44px}
.ctaw .box .go{font-size:44px;font-weight:800;color:var(--ac)}
.ctaw .s{font-size:46px;font-weight:600;color:var(--mut)}
/* ---------- tampon ---------- */
.stamp{position:absolute;left:50%;top:560px;z-index:6;font-size:120px;font-weight:900;padding:10px 46px;border:12px solid currentColor;border-radius:30px;letter-spacing:4px;transform:translate(-50%,-50%) rotate(-10deg);background:rgba(0,0,0,.35)}
/* ---------- sous-titres (hors camera) ---------- */
#cap{position:absolute;left:70px;right:150px;top:1180px;height:330px;display:flex;align-items:center;justify-content:center;text-align:center;z-index:20}
#cap .c{font-size:86px;font-weight:900;line-height:1.08;letter-spacing:-1.5px;color:#fff;
 text-shadow:0 0 6px #000,0 4px 0 #000,4px 0 0 #000,-4px 0 0 #000,0 -4px 0 #000,3px 3px 0 #000,-3px 3px 0 #000,3px -3px 0 #000,-3px -3px 0 #000,0 10px 30px rgba(0,0,0,.6)}
#cap .c .hl{text-shadow:none;color:#111}
#cap .c .ac{color:var(--ac2)}
#brand{position:absolute;left:0;right:0;top:1530px;text-align:center;font-size:32px;font-weight:700;color:rgba(255,255,255,.55);z-index:20;letter-spacing:.02em}
#flash{position:absolute;inset:0;background:#fff;opacity:0;z-index:30;pointer-events:none}
'''

THEMES = {
    'dark': {'bg': '#0e0f13', 'fg': '#ffffff', 'mut': '#a3a8b6', 'card': '#1c1e25', 'line': '#2c2f39'},
    'light': {'bg': '#f3f4f7', 'fg': '#111111', 'mut': '#5c6170', 'card': '#ffffff', 'line': '#dcdfe6'},
}


def rich(s):
    """*mot -> surligne, ^mot -> accent, \n -> <br>."""
    out = []
    for w in str(s).split(' '):
        if w.startswith('*'):
            out.append(f'<span class=hl>{H.escape(w[1:])}</span>')
        elif w.startswith('^'):
            out.append(f'<span class=ac>{H.escape(w[1:])}</span>')
        else:
            out.append(H.escape(w))
    return ' '.join(out).replace('\\n', '<br>').replace('\n', '<br>')


def scene_html(i, s, spec):
    k = s.get('kind', 'html')
    label = s.get('label', 'EXEMPLO SIMULADO')
    ext = {'wa': '318px', 'lock': '168px'}.get(k, '212px')
    badge = f'<div class=ex style="--ext:{ext}">{H.escape(label)}</div>' if label and k in ('gpt', 'wa', 'lock') else ''
    stamp = ''
    if s.get('stamp'):
        st = s['stamp']
        stamp = f'<div class=stamp id=st{i} style="color:{st.get("color", "#ff3b4e")};display:none">{H.escape(st["text"])}</div>'
    if k == 'big':
        inner = f'<div class=big><div class=t>{rich(s.get("big", ""))}</div>' + (f'<div class=s>{rich(s["sub"])}</div>' if s.get('sub') else '') + '</div>'
    elif k == 'gpt':
        inner = (f'<div class=gpt><div class=hd>{H.escape(s.get("title", "ChatGPT"))} <small>›</small></div>'
                 f'<div class=body id=b{i}></div><div class=in><span>＋</span><span class=tx id=in{i}></span><div class=go>↑</div></div></div>')
    elif k == 'wa':
        t = s.get('title', 'Cliente')
        inner = (f'<div class=wa><div class=bg></div><div class=hd><span class=ar>←</span><div class=pp>{H.escape(t[:1])}</div>'
                 f'<div><div class=nm>{H.escape(t)}</div><div class=st id=wst{i}>{H.escape(s.get("status", "online"))}</div></div></div>'
                 f'<div class=body id=b{i}></div><div class=bar><div class=f>🙂&nbsp;&nbsp;Mensagem</div><div class=mic>🎤</div></div></div>')
    elif k == 'lock':
        n = s.get('notif', {})
        inner = (f'<div class=lock><div class=dt>{H.escape(s.get("date", "terça-feira"))}</div><div class=ck>{H.escape(s.get("clock", "23:47"))}</div>'
                 f'<div class=nt id=nt{i}><div class=ic>💬</div><div style="flex:1"><div class=a><span>{H.escape(n.get("app", "WhatsApp"))}</span><span>agora</span></div>'
                 f'<div class=f>{H.escape(n.get("from", "Cliente"))}</div><div class=x>{H.escape(n.get("text", ""))}</div></div></div></div>')
    elif k == 'list':
        its = ''.join(f'<div class=it id=li{i}_{j}><b>{j + 1}</b>{rich(x)}</div>' for j, x in enumerate(s.get('items', [])))
        inner = f'<div class=lst>' + (f'<div class=h>{rich(s["big"])}</div>' if s.get('big') else '') + its + '</div>'
    elif k == 'cta':
        inner = (f'<div class=ctaw><div class=t>{rich(s.get("big", "Comenta"))}</div>'
                 f'<div class=box><div class=pp></div><div class=tx id=ct{i}></div><div class=go>Publicar</div></div>'
                 + (f'<div class=s>{rich(s["sub"])}</div>' if s.get('sub') else '') + '</div>')
    else:  # compat gen.py
        inner = f'<div class=stage>{s.get("v", "")}</div>'
    return f'<div class=sc id=sc{i}>{inner}{badge}{stamp}</div>'


JS = r'''
const S=__S__, D=__D__, BEAT=__BEAT__, LOOP=__LOOP__;
const $=id=>document.getElementById(id);
const ease=x=>1-Math.pow(1-Math.min(Math.max(x,0),1),3);
function esc(s){return s.replace(/[&<>]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;'}[c]))}
function rich(s){return s.split(' ').map(w=>w.startsWith('*')?'<span class=hl>'+esc(w.slice(1))+'</span>':w.startsWith('^')?'<span class=ac>'+esc(w.slice(1))+'</span>':esc(w)).join(' ')}
function chunks(cap){ // groupes de 1 a 3 mots, coupe sur la ponctuation
  const w=cap.split(' ').filter(Boolean),out=[];let cur=[];
  w.forEach((x,j)=>{cur.push(x);const p=/[.,!?:;…]$/.test(x),left=w.length-j-1;
    if(p||(cur.length>=4&&left!==1)||cur.length>=5){out.push(cur);cur=[]}});
  if(cur.length){if(cur.length===1&&out.length&&out[out.length-1].length<4)out[out.length-1].push(cur[0]);else out.push(cur)}return out}
function bubbleWA(m,lt,i,j){
  const age=lt-m.at, pop=m.at<=0?1:ease(age/0.18), sc=0.85+0.15*pop;
  const tm=m.time||'23:4'+(7+Math.min(j,2));
  let body=m.audio?'<div class=aud><span class=pl>▶</span><div class=wv>'+Array.from({length:30},(_,k)=>'<i style="height:'+(12+Math.abs(Math.sin(k*1.7))*40)+'px"></i>').join('')+'</div><span style="font-size:30px;color:#8696a0">'+m.audio+'</span></div>':esc(m.text).replace(/\n/g,'<br>');
  const ticks=(m.from==='out'||m.from==='bot')?' <b>✓✓</b>':'';
  return '<div class="m '+((m.from==='out'||m.from==='bot')?'out':'in')+'" style="transform:scale('+sc+');opacity:'+pop+';transform-origin:'+((m.from==='out'||m.from==='bot')?'100%':'0%')+' 100%">'+body+'<span class=tm>'+tm+ticks+'</span></div>'}
function renderScene(i,lt){
  const s=S[i],k=s.kind||'html';
  if(k==='gpt'){
    let h='',typing='';
    (s.msgs||[]).forEach(m=>{
      const user=(m.from==='user'||m.from==='out');
      if(user){
        const tdur=m.at<=0?0:Math.min(1.4,m.text.length/45); // frappe dans la barre
        if(lt<m.at-tdur)return;
        if(lt<m.at){typing=esc(m.text.slice(0,Math.floor(m.text.length*(1-(m.at-lt)/tdur))));return}
        const pop=m.at<=0?1:ease((lt-m.at)/0.18);
        h+='<div class=u style="opacity:'+pop+';transform:translateY('+(1-pop)*40+'px)">'+esc(m.text)+'</div>';
      }else{
        if(lt<m.at)return;
        const cps=m.cps||55, n=m.at<=0?m.text.length:Math.floor((lt-m.at-0.35)*cps);
        const txt=n<=0?'<span class=dot></span>':esc(m.text.slice(0,n)).replace(/\n/g,'<br>')+(n<m.text.length?'<span class=dot style="width:20px;height:20px;margin-left:8px"></span>':'');
        h+='<div class=a><div class=av>✦</div><div>'+txt+'</div></div>';
      }});
    $('b'+i).innerHTML=h;
    $('in'+i).innerHTML=typing?typing+'<span class=caret></span>':'<span class=ph>'+(s.placeholder||'Pergunte alguma coisa')+'</span>';
  }else if(k==='wa'){
    let h='',typingNow=false;
    (s.msgs||[]).forEach((m,j)=>{
      const bot=(m.from==='out'||m.from==='bot');
      if(lt<m.at){ if(bot&&lt>m.at-0.9&&m.at>0)typingNow=true; return}
      h+=bubbleWA(m,lt,i,j)});
    if(typingNow)h+='<div class=typ>'+[0,1,2].map(k=>'<i style="opacity:'+(0.35+0.65*Math.abs(Math.sin(lt*6+k)))+'"></i>').join('')+'</div>';
    $('b'+i).innerHTML=h;
    $('wst'+i).textContent=typingNow?'digitando…':(s.status||'online');
  }else if(k==='lock'){
    const at=(s.notif&&s.notif.at!=null)?s.notif.at:0, p=at<=0?1:ease((lt-at)/0.22);
    $('nt'+i).style.opacity=lt<at?0:p; $('nt'+i).style.transform='translateY('+(1-p)*-80+'px)';
  }else if(k==='list'){
    (s.items||[]).forEach((_,j)=>{const at=(s.step||0.45)*j, el=$('li'+i+'_'+j), p=j===0&&at<=0?1:ease((lt-at)/0.2);
      el.style.opacity=lt<at?0:p; el.style.transform='translateX('+(1-p)*-60+'px)'});
  }else if(k==='cta'){
    const w=s.word||'GUIA', a=s.typeAt!=null?s.typeAt:0.5, n=Math.max(0,Math.min(w.length,Math.floor((lt-a)/0.12)+1));
    $('ct'+i).innerHTML=lt<a?'<span class=ph>Adicione um comentário…</span>':esc(w.slice(0,n))+(n<w.length||Math.floor(lt*2)%2?'<span class=caret style="background:var(--fg)"></span>':'');
  }
  if(s.stamp){const st=$('st'+i),a=s.stamp.at||0;if(lt<a){st.style.display='none'}else{const p=a<=0?1:ease((lt-a)/0.16);st.style.display='block';
    st.style.transform='translate(-50%,-50%) rotate(-10deg) scale('+(1.9-0.9*p)+')';st.style.opacity=p}}
}
function seek(T){
  let t=T, isLoop=false;
  if(LOOP&&T>=D-0.35){t=0;isLoop=true}
  let i=0;S.forEach((s,j)=>{if(t>=s.t)i=j});
  const s=S[i], end=(S[i+1]?S[i+1].t:D), lt=t-s.t, len=end-s.t;
  document.querySelectorAll('.sc').forEach((x,j)=>x.classList.toggle('on',j===i));
  renderScene(i,lt);
  // camera : punch-in a la coupe (1.10 -> 1.0 en 0.22 s) puis micro-coupes tous les BEAT s
  let z=1;
  if(s.zoom!==false){
    const nb=Math.floor(lt/BEAT), bl=lt-nb*BEAT;
    const ui=(s.kind==='gpt'||s.kind==='wa'||s.kind==='lock'), amp=ui?0.05:0.035;
    const base=(nb%2===1)?1+amp:1.0;
    const hit=(i===0&&lt<BEAT&&!isLoop)?0:(1-ease(bl/0.22))*(ui?0.04:0.03);
    z=base+hit+0.012*bl;
  }
  const fy=(s.focus!=null?s.focus:0.42)*100;
  $('world').style.transformOrigin='50% '+fy+'%';
  $('world').style.transform='scale('+z.toFixed(4)+')';
  // flash leger sur les coupes (sauf t=0)
  $('flash').style.opacity=(t>0.05&&lt<0.06&&!isLoop)?0.10:0;
  // sous-titres
  const cs=chunks(s.cap||''), capEnd=len*0.94, per=cs.length?capEnd/cs.length:1;
  const k=Math.min(cs.length-1,Math.floor(lt/per));
  if(cs.length&&k>=0){const pk=(lt-k*per), p=(t===0||isLoop)?1:ease(pk/0.12);
    const txt=cs[k].join(' ').replace(/[*^]/g,''), fs=txt.length>18?72:txt.length>14?80:86;
    $('cap').innerHTML='<div class=c style="font-size:'+fs+'px;transform:scale('+(0.86+0.14*p)+')">'+rich(cs[k].join(' '))+'</div>'}
  else $('cap').innerHTML='';
}
window.seek=seek;
'''


def page(spec):
    th = THEMES.get(spec.get('theme', 'dark'), THEMES['dark'])
    ac = spec.get('ac', '#ff6a1a')
    scs = ''.join(scene_html(i, s, spec) for i, s in enumerate(spec['scenes']))
    js = (JS.replace('__S__', json.dumps(spec['scenes'], ensure_ascii=False))
            .replace('__D__', str(spec['dur'])).replace('__BEAT__', str(spec.get('beat', 1.4)))
            .replace('__LOOP__', 'true' if spec.get('loop', True) else 'false'))
    root = ''.join(f'--{k}:{v};' for k, v in th.items()) + f'--ac:{ac};--ac2:{spec.get("ac2", ac)};'
    brand = spec.get('handle') or spec.get('brand', '')
    return (f'<!doctype html><html><head><meta charset=utf-8><style>:root{{{root}}}{CSS}</style></head><body>'
            f'<div id=world>{scs}</div><div id=cap></div><div id=brand>{H.escape(brand)}</div><div id=flash></div>'
            f'<script>{js}</script></body></html>')


# ---------------- sons d'interface (synthese courte, pas de musique) ----------------
def _env(n, a=0.002, d=0.06):
    t = np.arange(n) / SR
    return np.minimum(1, t / a) * np.exp(-t / d)


def sfx(kind):
    rng = np.random.default_rng(7)
    if kind == 'click':
        n = int(SR * 0.03); x = rng.standard_normal(n) * _env(n, 0.0005, 0.004)
        return np.convolve(x, np.ones(6) / 6, 'same') * 0.5
    if kind == 'type':
        n = int(SR * 0.025); x = rng.standard_normal(n) * _env(n, 0.0004, 0.003)
        return np.convolve(x, np.ones(4) / 4, 'same') * 0.22
    if kind == 'pop':
        n = int(SR * 0.09); t = np.arange(n) / SR
        f = 520 + 900 * np.exp(-t / 0.02)
        return np.sin(2 * np.pi * np.cumsum(f) / SR) * _env(n, 0.001, 0.03) * 0.35
    if kind == 'send':
        n = int(SR * 0.14); t = np.arange(n) / SR
        f = 700 + 1100 * (t / t[-1])
        return np.sin(2 * np.pi * np.cumsum(f) / SR) * _env(n, 0.002, 0.05) * 0.22
    if kind == 'notif':
        out = np.zeros(int(SR * 0.36))
        for st, fr in ((0, 1046.5), (0.11, 1568.0)):
            n = int(SR * 0.25); t = np.arange(n) / SR
            tone = (np.sin(2 * np.pi * fr * t) + 0.3 * np.sin(2 * np.pi * fr * 2 * t)) * _env(n, 0.002, 0.07)
            s0 = int(st * SR); out[s0:s0 + n] += tone[:len(out) - s0]
        return out * 0.22
    if kind == 'whoosh':
        n = int(SR * 0.28); t = np.arange(n) / SR
        x = rng.standard_normal(n)
        k = int(30 + 0 * t[0]); x = np.convolve(x, np.ones(k) / k, 'same')
        e = np.sin(np.pi * t / t[-1]) ** 2
        return x * e * 0.5
    return np.zeros(1)


def auto_sfx(spec):
    ev = []
    for i, s in enumerate(spec['scenes']):
        t0 = s['t']; k = s.get('kind', 'html')
        if i == 0:
            ev.append((0.0, 'pop'))
        else:
            ev.append((t0, 'whoosh'))
        if k == 'gpt':
            for m in s.get('msgs', []):
                if m['at'] <= 0:
                    continue
                if m.get('from') in ('user', 'out'):
                    td = min(1.4, len(m['text']) / 45)
                    for q in np.arange(m['at'] - td, m['at'], 0.075):
                        ev.append((t0 + q, 'type'))
                    ev.append((t0 + m['at'], 'send'))
                else:
                    ev.append((t0 + m['at'] + 0.35, 'pop'))
        elif k == 'wa':
            for m in s.get('msgs', []):
                if m['at'] <= 0:
                    continue
                ev.append((t0 + m['at'], 'send' if m.get('from') in ('out', 'bot') else 'notif'))
        elif k == 'lock':
            ev.append((t0 + (s.get('notif', {}).get('at') or 0) + 0.02, 'notif'))
        elif k == 'list':
            for j in range(len(s.get('items', []))):
                ev.append((t0 + (s.get('step', 0.45)) * j, 'click'))
        elif k == 'cta':
            a = s.get('typeAt', 0.5)
            for j in range(len(s.get('word', 'GUIA'))):
                ev.append((t0 + a + 0.12 * j, 'type'))
            ev.append((t0 + a + 0.12 * len(s.get('word', 'GUIA')) + 0.25, 'click'))
        if s.get('stamp'):
            ev.append((t0 + s['stamp'].get('at', 0), 'pop'))
        for x in s.get('sfx', []):
            ev.append((t0 + x['at'], x['type']))
    if spec.get('loop', True):
        ev.append((spec['dur'] - 0.35, 'whoosh'))
    return ev


def build_audio(spec, path):
    n = int(SR * spec['dur'])
    buf = np.zeros(n)
    g = spec.get('sfx_gain', 0.9)
    for at, kind in auto_sfx(spec):
        x = sfx(kind); s0 = int(at * SR)
        if s0 < 0 or s0 >= n:
            continue
        e = min(n, s0 + len(x)); buf[s0:e] += x[:e - s0] * g
    buf = np.clip(buf, -0.95, 0.95)
    st = np.repeat((buf * 32767).astype(np.int16)[:, None], 2, axis=1)
    with wave.open(path, 'wb') as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(st.tobytes())


async def render(name, spec, outdir):
    os.makedirs(outdir, exist_ok=True)
    hp = os.path.abspath(os.path.join(outdir, name + '.html'))
    open(hp, 'w').write(page(spec))
    wav = os.path.join(outdir, name + '.wav'); build_audio(spec, wav)
    mp4 = os.path.join(outdir, name + '.mp4')
    nf = int(round(spec['dur'] * FPS))
    ff = subprocess.Popen(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', str(FPS), '-c:v', 'mjpeg', '-i', '-',
                           '-i', wav, '-map', '0:v', '-map', '1:a', '-c:v', 'libx264', '-preset', 'medium', '-crf', '18',
                           '-pix_fmt', 'yuv420p', '-r', str(FPS), '-c:a', 'aac', '-b:a', '160k', '-shortest', '-movflags', '+faststart', mp4],
                          stdin=subprocess.PIPE)
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={'width': W, 'height': HGT})
        await pg.goto('file://' + hp)
        await pg.evaluate('document.fonts.ready')
        for f in range(nf):
            await pg.evaluate(f'seek({f / FPS:.4f})')
            ff.stdin.write(await pg.screenshot(type='jpeg', quality=92))
        await b.close()
    ff.stdin.close(); ff.wait()
    os.remove(wav)
    print('ok', mp4, nf, 'frames')


def main():
    specs = json.load(open(sys.argv[1]))
    outdir = sys.argv[2] if len(sys.argv) > 2 else '.'
    only = sys.argv[3:]  # noms facultatifs
    async def run():
        for n, s in specs.items():
            if not only or n in only:
                await render(n, s, outdir)
    asyncio.run(run())


if __name__ == '__main__':
    main()
