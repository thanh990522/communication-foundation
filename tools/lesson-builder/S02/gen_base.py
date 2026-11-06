# Generates all S01 audio clips with Microsoft neural voices (edge-tts), trims, concatenates, exports MP3.
import os, certifi
if os.environ.get('SSL_CA_BUNDLE'): certifi.where=lambda:os.environ['SSL_CA_BUNDLE']
import asyncio, edge_tts, subprocess, numpy as np, json, os, hashlib, sys
SR=24000
OUT='mp3'; CACHE='cache'
os.makedirs(OUT,exist_ok=True); os.makedirs(CACHE,exist_ok=True)
SONIA='en-GB-SoniaNeural'; RYAN='en-GB-RyanNeural'; LIBBY='en-GB-LibbyNeural'; JENNY='en-US-JennyNeural'
LET='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def ck(v,t,r): return os.path.join(CACHE,hashlib.md5(f'{v}|{t}|{r}'.encode()).hexdigest()+'.mp3')
need=set()
def want(v,t,r='+0%'): need.add((v,t,r)); return (v,t,r)
async def fetch_all():
    sem=asyncio.Semaphore(6)
    async def one(v,t,r):
        p=ck(v,t,r)
        if os.path.exists(p) and os.path.getsize(p)>0: return
        async with sem:
            for k in range(4):
                try:
                    await edge_tts.Communicate(t,v,rate=r).save(p)
                    if os.path.getsize(p)>0: return
                except Exception as e: print('retry',t,e,file=sys.stderr); await asyncio.sleep(2)
            raise SystemExit('failed '+t)
    await asyncio.gather(*[one(*n) for n in need])
def load(key):
    raw=subprocess.run(['ffmpeg','-v','error','-i',ck(*key),'-f','f32le','-ac','1','-ar',str(SR),'-'],capture_output=True).stdout
    a=np.frombuffer(raw,np.float32)
    thr=0.012; idx=np.where(np.abs(a)>thr)[0]
    if len(idx)==0: return a
    s=max(0,idx[0]-int(.03*SR)); e=min(len(a),idx[-1]+int(.06*SR))
    return a[s:e]
def sil(sec): return np.zeros(int(sec*SR),np.float32)

# ---------- segment model ----------
# segment: str sentence | ('l',X) single letter | ('s',text) spell | ('sn',text) spell no doubles
def tokens(s,doubles=True):
    out=[]; at=s.find('@'); loc=s if at<0 else s[:at]; dom='' if at<0 else s[at+1:]
    i=0
    while i<len(loc):
        c=loc[i]
        if c.isalpha():
            U=c.upper()
            if doubles and i+1<len(loc) and loc[i+1].upper()==U: out.append('double '+U); i+=2; continue
            out.append(U)
        elif c.isdigit(): out.append(['zero','one','two','three','four','five','six','seven','eight','nine'][int(c)])
        elif c=='.': out.append('dot')
        elif c=='_': out.append('underscore')
        elif c=='-': out.append('hyphen')
        elif c=="'": out.append('apostrophe')
        elif c==' ': out.append('|')
        i+=1
    if at>=0:
        out.append('at')
        for k,p in enumerate(dom.split('.')):
            if k: out.append('dot')
            for j,w in enumerate(p.split('-')):
                if j: out.append('hyphen')
                if w in ('com','net','org','edu') or len(w)>3: out.append(w)   # say as a word
                else: out.extend(ch.upper() for ch in w)                     # spell short parts: v-n, a-b-c
    return out
def plan(segs,v,gap=.28,rate='+0%'):
    keys=[]
    for sg in segs:
        if isinstance(sg,str): keys.append(want(v,sg,rate)); keys.append(.32)
        elif sg[0]=='l': keys.append(want(v,sg[1])); keys.append(.3)
        else:
            for t in tokens(sg[1],sg[0]=='s'):
                if t=='|': keys.append(.45); continue
                keys.append(want(v,t)); keys.append(gap)
            keys.append(.15)
    return keys
def render(plans):
    parts=[]
    for p in plans:
        if isinstance(p,(int,float)): parts.append(sil(p))
        else: parts.append(load(p))
    if plans and isinstance(plans[-1],(int,float)): parts=parts[:-1]
    a=np.concatenate([sil(.12)]+parts+[sil(.25)]) if parts else sil(.3)
    return a

CLIPS={}   # id -> (filename, plan list, label)
def clip(cid,fname,keys,label): CLIPS[cid]=(fname,keys,label)

#__CLIPS__

asyncio.run(fetch_all())
manifest={}
for cid,(fn,keys,label) in CLIPS.items():
    a=render(keys); p=os.path.join(OUT,fn); os.makedirs(os.path.dirname(p),exist_ok=True)
    subprocess.run(['ffmpeg','-v','error','-y','-f','f32le','-ar',str(SR),'-ac','1','-i','-','-codec:a','libmp3lame','-b:a','64k',p],input=a.tobytes(),check=True)
    manifest[cid]={'file':fn,'label':label,'dur':round(len(a)/SR,2)}
json.dump(manifest,open('manifest.json','w'),indent=1)
print(len(manifest),'clips;',len(need),'tts requests')
