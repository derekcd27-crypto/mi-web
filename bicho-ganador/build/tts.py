import json, sys, numpy as np, soundfile as sf
from kokoro_onnx import Kokoro
M=sys.argv[1]
k=Kokoro(M+'/kokoro-v1.0.onnx',M+'/voices-v1.0.bin')
segs=json.load(open('build/guion.json')); out=[]; t=0; sr=24000
for s in segs:
    a,sr=k.create(s['text'],voice='em_alex',speed=1.12,lang='es')
    # trim silence
    idx=np.where(np.abs(a)>0.01)[0]; a=a[max(0,idx[0]-600):idx[-1]+1200]
    gap=np.zeros(int(sr*0.22),dtype=a.dtype)
    s['start']=round(t,3); s['dur']=round(len(a)/sr,3); t+=len(a)/sr+0.22
    out.append(a); out.append(gap)
sf.write('build/voz.wav',np.concatenate(out),sr)
json.dump({'total':round(t+0.8,3),'segments':segs},open('build/timeline.json','w'),ensure_ascii=False,indent=1)
print(t)
