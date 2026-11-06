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

# letters
for X in LET: clip('L_'+X,f'Letters/S01_letter_{X}.mp3',[want(SONIA,X)],f'Letter {X}')
clip('L_Z_US','Letters/S01_letter_Z_US.mp3',[want(JENNY,'Z')],'Letter Z (US: zee)')
az=[]
for X in LET: az+= [want(SONIA,X),.42]
clip('AZ','Letters/S01_alphabet_A-Z.mp3',az,'Alphabet A–Z')
FAMS=[['A','H','J','K'],['B','C','D','E','G','P','T','V'],['F','L','M','N','S','X','Z'],['I','Y'],['O'],['Q','U','W'],['R']]
FN=['ei_say','ii_see','e_pen','ai_my','ou_go','uu_you','aa_car']
fa=[]
for i,f in enumerate(FAMS):
    k=[]
    for X in f: k+=[want(SONIA,X),.35]
    clip(f'FAM_{i}',f'Sound_families/S01_family{i+1}_{FN[i]}.mp3',k,f'Family {i+1}: '+' '.join(f))
    fa+=k+[.8]
clip('FAM_ALL','Sound_families/S01_all_7_families.mp3',fa,'All 7 sound families')
ACR=['ATM','KFC','VIP','OK','USA','UK','CEO','FAQ','DIY','ASAP','BBC','ID','VTV','HCMC']
for i,a in enumerate(ACR): clip(f'ACR_{i}',f'Warm-up/S01_warmup_{i+1:02d}_{a}.mp3',plan([('sn',a)],SONIA,gap=.12),a)
for cid,t,fn in [('CAP_J','capital J','capital_J'),('SMALL_J','small j','small_j'),('PH_LOWER',"It's all lower case.",'all_lower_case'),('W_CAR','car','car'),('W_WHY','why','why')]:
    clip(cid,f'Phrases/S01_{fn}.mp3',[want(SONIA,t,'-5%')],t)
ODD=[['A','H','J','E'],['B','D','F','T'],['M','N','L','I'],['Q','U','W','O'],['G','P','V','K'],['S','X','R','F']]
for i,o in enumerate(ODD):
    k=[]
    for X in o: k+=[want(SONIA,X),.55]
    clip(f'ODD_{i}',f'Odd_one_out/S01_odd_{i+1}_{"".join(o)}.mp3',k,'Odd one out '+' '.join(o))
NAMES_TEST=[('Mr','Black'),('Mrs','Green'),('Ms','Hayes'),('Mr','Jarvis'),('Dr','Patel'),
            ('Miss','Nguyen'),('Mr','Pham'),('Ms','Quinn'),('Mrs','Wood'),('Mr','Huynh')]
NUMW=['one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve']
TITLE_SAY={'Mr':'Mister','Mrs':'Missus','Ms':'Ms','Dr':'Doctor','Miss':'Miss'}
for i,(t,n) in enumerate(NAMES_TEST):
    k=[want(RYAN,f'Question {NUMW[i]}.'),.7,want(RYAN,f'{TITLE_SAY[t]} {n}.'),.45]
    toks=tokens(n.upper())
    for j,tk in enumerate(toks): k+=[want(RYAN,tk),.22]
    clip(f'NT_{i}',f'Listening_Spelling_test/S01_NT_q{i+1:02d}_{t}_{n}.mp3',k,f'Question {i+1}: {t} {n}')
SPELL=[['Tom','Nam','Anna','Linh'],['Sarah','James','Hieu','Giang'],['Phuong','Nguyen','Quynh','Jackson'],['Phillips','Wright','anh.tran@gmail.com','mai_vu@yahoo.com']]
LVN=['Easy','Medium','Hard','Challenge']
for L,lst in enumerate(SPELL):
    for k,n in enumerate(lst):
        clip(f'SP_{L}_{k}',f'Spell_the_names/S01_spell_{L+1}{LVN[L]}_{k+1}_{n.replace("@","_at_")}.mp3',plan([('s',n)],SONIA,gap=.3),f'{LVN[L]} {k+1}: {n}')
SYMB=[('at','at'),('dot','dot'),('underscore','underscore'),('hyphen','hyphen, or dash'),('dotcom','dot com'),('dotvn','dot V N'),('doubleS','double S'),('lower','all lower case')]
for i,(fn,t) in enumerate(SYMB): clip(f'SYM_{i}',f'Email_symbols/S01_symbol_{i+1}_{fn}.mp3',[want(SONIA,t)],t)
EMAILS=['lan.pham@gmail.com','tom_baker99@yahoo.com','info@abc-english.vn','minh.anh2002@outlook.com']
for i,e in enumerate(EMAILS): clip(f'EM_{i}',f'Email_symbols/S01_email_{i+1}.mp3',plan([('s',e)],SONIA,gap=.26),e)
QA=[(["What's your name?"],["My name's Linh."]),
    (["How do you spell your first name?"],["It's",('s','LINH')]),
    (["How do you spell your surname?"],["It's",('s','NGUYEN')]),
    (["Sorry, could you spell that again, please?"],["Sure.",('s','NGUYEN')]),
    (['Is that G as in "good"?'],["Yes, that's right."]),
    (['Is that J as in "juice"?'],['No, it\'s G as in "good".']),
    (["What's your email address?"],["It's",('s','linh.ng@gmail.com')]),
    (["Is that all lower case?"],["Yes, it's all lower case."])]
for i,(q,a) in enumerate(QA):
    clip(f'QA_{i}_q',f'Questions_answers/S01_QA{i+1}_question.mp3',plan(q,RYAN,rate='-5%'),'Q: '+q[0])
    clip(f'QA_{i}_a',f'Questions_answers/S01_QA{i+1}_answer.mp3',plan(a,LIBBY,rate='-5%'),'A: '+str(a[0]))
DLG=[('R',["Good morning! Welcome to Bright English Centre. Can I have your name, please?"]),
 ('S',["Sure. My name's Linh. Nguyen Thuy Linh."]),
 ('R',["Nice to meet you, Linh. How do you spell your first name?"]),
 ('S',["It's",('s','LINH')]),
 ('R',["Thanks. And how do you spell your surname?"]),
 ('S',[('s','NGUYEN')]),
 ('R',["Sorry, could you spell that again, please?"]),
 ('S',["Of course.",('s','NGUYEN')]),
 ('R',['Is that G as in "good"?']),
 ('S',["Yes, that's right."]),
 ('R',["Great. And what's your email address?"]),
 ('S',["It's",('s','thuylinh_ng@gmail.com')]),
 ('R',["Is that all lower case?"]),
 ('S',["Yes, all lower case."]),
 ('R',["Let me check.",('s','thuylinh_ng@gmail.com')]),
 ('S',["Perfect. Thank you!"])]
allk=[]
for i,(w,s) in enumerate(DLG):
    k=plan(s,RYAN if w=='R' else LIBBY,rate='-8%')
    clip(f'DLG_{i}',f'Dialogue/S01_dialogue_line{i+1:02d}.mp3',k,f'Line {i+1}')
    allk+=k+[.55]
clip('DLG_ALL','Dialogue/S01_dialogue_FULL.mp3',allk,'Full dialogue')

asyncio.run(fetch_all())
manifest={}
for cid,(fn,keys,label) in CLIPS.items():
    a=render(keys); p=os.path.join(OUT,fn); os.makedirs(os.path.dirname(p),exist_ok=True)
    subprocess.run(['ffmpeg','-v','error','-y','-f','f32le','-ar',str(SR),'-ac','1','-i','-','-codec:a','libmp3lame','-b:a','64k',p],input=a.tobytes(),check=True)
    manifest[cid]={'file':fn,'label':label,'dur':round(len(a)/SR,2)}
json.dump(manifest,open('manifest.json','w'),indent=1)
print(len(manifest),'clips;',len(need),'tts requests')
