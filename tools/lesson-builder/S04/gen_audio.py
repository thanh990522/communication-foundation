# Generates all S02 audio clips with Microsoft neural voices (edge-tts), trims, concatenates, exports MP3.
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


import content as C
def slug(t): return ''.join(ch if ch.isalnum() else '_' for ch in t)[:40].strip('_')
cap=lambda t:t[0].upper()+t[1:]
# warm-up: say the time / date
for i,(f,em,ans) in enumerate(C.WARM):
    k=[]
    for part in ans.split(' / '): k+=[want(SONIA,cap(part)+'.','-8%'),.5]
    clip(f'WA_{i}',f'Warm-up/S04_say_{i+1}.mp3',k,ans)
# on at in + ordinals
for i,(p_,u,xs) in enumerate(C.TIMEW):
    for j,x in enumerate(xs): clip(f'TW_{i}_{j}',f'Time_words/S04_{p_}_{j+1}.mp3',[want(SONIA,x,'-8%')],x)
for i,(o,w) in enumerate(zip(C.ORDINALS,C.ORD_SAY)): clip(f'OR_{i}',f'Time_words/S04_ordinal_{o}.mp3',[want(SONIA,'the '+w,'-8%')],'the '+w)
# vocabulary
for i,v in enumerate(C.VOCAB):
    clip(f'VW_{i}',f'Vocabulary/S04_word_{i+1}_{slug(v["w"])}.mp3',[want(SONIA,v['w']),.7,want(SONIA,v['w'],'-15%')],v['w'])
    clip(f'VC_{i}',f'Vocabulary/S04_phrase_{i+1}_{slug(v["col"])}.mp3',[want(SONIA,v['col']),.6,want(SONIA,v['ex'],'-5%')],v['col'])
for i,(s_,opts,ans,k_) in enumerate(C.COLL):
    t=s_.replace('___',ans); clip(f'CO_{i}',f'Collocations/S04_coll_{i+1}.mp3',[want(SONIA,t,'-5%')],t)
# grammar
for i,(t,pat,x) in enumerate(C.GRAM): clip(f'GR_{i}',f'Grammar/S04_present_continuous_{i+1}.mp3',[want(SONIA,x,'-6%')],x)
for i,(q,y,n_) in enumerate(C.GRAM_QA):
    clip(f'GQ_{i}_q',f'Grammar/S04_question_{i+1}.mp3',[want(RYAN,q,'-5%')],q)
    clip(f'GQ_{i}_y',f'Grammar/S04_question_{i+1}_yes.mp3',[want(LIBBY,y,'-5%')],y)
    clip(f'GQ_{i}_n',f'Grammar/S04_question_{i+1}_no.mp3',[want(LIBBY,n_,'-5%')],n_)
for i,(s_,opts,ans) in enumerate(C.DIARYQ):
    t=s_.replace('___',ans) if '___' in s_ else s_+' '+ans
    clip(f'MQ_{i}',f'Diary/S04_mai_{i+1}.mp3',[want(SONIA,t,'-5%')],t)
# numbers 13 / 30
NUM={'13':'thirteen','30':'thirty','14':'fourteen','40':'forty','15':'fifteen','50':'fifty','16':'sixteen','60':'sixty','17':'seventeen','70':'seventy','18':'eighteen','80':'eighty','19':'nineteen','90':'ninety'}
for i,(a_,b_,sa,sb) in enumerate(C.PAIRS):
    clip(f'NP_{i}_0',f'Numbers/S04_{a_}.mp3',[want(SONIA,NUM[a_]),.5,want(SONIA,NUM[a_],'-20%')],a_)
    clip(f'NP_{i}_1',f'Numbers/S04_{b_}.mp3',[want(SONIA,NUM[b_]),.5,want(SONIA,NUM[b_],'-20%')],b_)
for i,(s_,pi,ans) in enumerate(C.PAIR_TEST):
    n=C.PAIRS[pi][ans]; t=s_.replace('___',n)
    clip(f'PT_{i}',f'Numbers/S04_which_{i+1}.mp3',[want(RYAN,t,'-8%')],t)
# confirm intonation
for i,(q,a_) in enumerate(zip(C.CONFIRM_Q,C.CONFIRM_S)):
    clip(f'CQ_{i}',f'Intonation/S04_check_{i+1}.mp3',[want(LIBBY,q,'-8%')],q)
    clip(f'CS_{i}',f'Intonation/S04_confirm_{i+1}.mp3',[want(RYAN,a_,'-8%')],a_)
# frames
for i,(f,exs) in enumerate(C.FRAMES):
    for j,x in enumerate(exs): clip(f'FR_{i}_{j}',f'Sentence_frames/S04_frame{i+1}_{j+1}.mp3',[want(SONIA,x,'-5%')],x)
# questions & answers
for i,(q,ans) in enumerate(C.QA):
    clip(f'QA_{i}_q',f'Questions_answers/S04_QA{i+1}_question.mp3',[want(RYAN,q,'-5%')],'Q: '+q)
    for j,a_ in enumerate(ans): clip(f'QA_{i}_a{j}',f'Questions_answers/S04_QA{i+1}_answer_{"abc"[j]}.mp3',[want(LIBBY,a_,'-5%')],'A: '+a_)
# phone call: receptionist (Libby) & Nam (Ryan)
allk=[]
for i,(w,t) in enumerate(C.DIALOGUE):
    k=[want(LIBBY if w=='R' else RYAN,t,'-6%')]
    clip(f'DLG_{i}',f'Dialogue/S04_phone_call_line{i+1:02d}.mp3',k,f'Line {i+1}')
    allk+=k+[.55]
clip('DLG_ALL','Dialogue/S04_phone_call_FULL.mp3',allk,'Full dialogue')
# scramble
for i,s_ in enumerate(C.SCRAMBLE): clip(f'SC_{i}',f'Game/S04_sentence_{i+1}.mp3',[want(SONIA,s_,'-5%')],s_)


asyncio.run(fetch_all())
manifest={}
for cid,(fn,keys,label) in CLIPS.items():
    a=render(keys); p=os.path.join(OUT,fn); os.makedirs(os.path.dirname(p),exist_ok=True)
    subprocess.run(['ffmpeg','-v','error','-y','-f','f32le','-ar',str(SR),'-ac','1','-i','-','-codec:a','libmp3lame','-b:a','64k',p],input=a.tobytes(),check=True)
    manifest[cid]={'file':fn,'label':label,'dur':round(len(a)/SR,2)}
json.dump(manifest,open('manifest.json','w'),indent=1)
print(len(manifest),'clips;',len(need),'tts requests')
