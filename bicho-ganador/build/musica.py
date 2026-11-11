import json, numpy as np, soundfile as sf
sr=44100; tl=json.load(open('timeline.json')); T=tl['total']; n=int(T*sr); t=np.arange(n)/sr
bpm=112; beat=60/bpm; mix=np.zeros(n)
def add(sig,at,g=1.0):
    i=int(at*sr); j=min(n,i+len(sig)); 
    if i<n: mix[i:j]+=g*sig[:j-i]
def env(L,a=0.005,dcy=8): x=np.arange(int(L*sr))/sr; return np.minimum(x/a,1)*np.exp(-x*dcy)
kick=lambda: np.sin(2*np.pi*np.cumsum(55+90*np.exp(-np.arange(int(.3*sr))/sr*30))/sr)*env(.3,0.001,9)
rng=np.random.default_rng(1)
hat=lambda: rng.standard_normal(int(.06*sr))*env(.06,0.001,60)*0.25
notes=[57,60,64,62, 57,60,65,64, 55,59,62,60, 57,60,64,67]  # A minor-ish arp
f=lambda m:440*2**((m-69)/12)
def pluck(m,L=.22): x=np.arange(int(L*sr))/sr; return (np.sign(np.sin(2*np.pi*f(m)*x))*0.3+np.sin(2*np.pi*f(m)*x))*env(L,0.003,14)*0.18
def bass(m,L): x=np.arange(int(L*sr))/sr; return np.sin(2*np.pi*f(m-24)*x)*env(L,0.01,3)*0.5
k=0; b=0.0
while b<T:
    win=[s for s in tl['segments'] if s['scene']=='winner'][0]
    hush= win['start']<=b<win['start']+1.3   # drum-roll hush before reveal
    if not hush:
        add(kick(),b,0.9); add(hat(),b+beat/2)
        add(pluck(notes[k%16]),b); add(pluck(notes[(k+2)%16]+12,.15),b+beat/2,0.6)
        if k%4==0: add(bass(notes[k%16],beat*4),b)
    else:
        for r in np.arange(0,beat,beat/8): add(rng.standard_normal(int(.03*sr))*env(.03,0.001,80)*0.5,b+r)
    b+=beat; k+=1
# whoosh at each scene change
for s in tl['segments'][1:]:
    L=.35; w=rng.standard_normal(int(L*sr)); x=np.arange(len(w))/sr
    w=np.convolve(w,np.ones(12)/12,'same')*np.sin(np.pi*x/L)**2*0.6; add(w,s['start']-0.2)
# ding on winner reveal
win=[s for s in tl['segments'] if s['scene']=='winner'][0]; x=np.arange(int(1.5*sr))/sr
ding=sum(np.sin(2*np.pi*f(m)*x) for m in (76,79,84))*np.exp(-x*3)*0.25; add(ding,win['start']+1.3)
# fade
fade=np.minimum(1,np.minimum(t/0.3,(T-t)/1.2)); mix*=fade
mix/=np.abs(mix).max()+1e-9
sf.write('musica.wav',(mix*0.9).astype(np.float32),sr)
