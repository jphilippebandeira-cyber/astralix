import numpy as np, wave, sys
sr=44100; bpm=100; beat=60/bpm; dur=float(sys.argv[1]); out=sys.argv[2]
t=np.arange(int(sr*dur))/sr; y=np.zeros_like(t)
def n(f): return 440*2**((f-69)/12)
chords=[[57,60,64],[53,57,60],[48,52,55],[55,59,62]]  # Am F C G
bar=4*beat
for i,start in enumerate(np.arange(0,dur,bar)):
    ch=chords[i%4]; m=(t>=start)&(t<start+bar); tt=t[m]-start
    env=np.minimum(1,tt/0.4)*np.exp(-tt/3.5)
    for k in ch:
        f=n(k); y[m]+=0.06*env*(np.sin(2*np.pi*f*tt)+0.3*np.sin(2*np.pi*2*f*tt)+0.15*np.sin(2*np.pi*f*1.003*tt))
    bass=n(ch[0]-12); y[m]+=0.09*env*np.sin(2*np.pi*bass*tt)
for b in np.arange(0,dur,beat):
    m=(t>=b)&(t<b+0.25); tt=t[m]-b
    y[m]+=0.35*np.exp(-tt*18)*np.sin(2*np.pi*(55+90*np.exp(-tt*30))*tt)
for h in np.arange(beat/2,dur,beat):
    m=(t>=h)&(t<h+0.05); tt=t[m]-h
    y[m]+=0.04*np.exp(-tt*80)*np.random.randn(m.sum())
y[t>dur-1.5]*=np.linspace(1,0,(t>dur-1.5).sum())
y=y/np.abs(y).max()*0.8
w=wave.open(out,'w'); w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr); w.writeframes((y*32767).astype(np.int16).tobytes()); w.close()
