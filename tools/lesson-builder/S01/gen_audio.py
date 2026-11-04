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
            out.append(p)
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
for cid,t,fn in [('CAP_J','capital J','capital_J'),('SMALL_J','small j','small_j'),('PH_LOWER',"It's all lower case.",'all_lower_case'),('PH_CAPS',"It's all capitals.",'all_capitals'),('PH_CAPQ','Is that a capital letter?','capital_letter_question'),('W_CAR','car','car'),('W_WHY','why','why')]:
    clip(cid,f'Phrases/S01_{fn}.mp3',[want(SONIA,t,'-5%')],t)
UN=[[ 'capital M',('l','A'),('l','I'),'capital A',('l','N'),('l','H'),'underscore','nine','eight'],
    ['small j','capital T',('l','R'),('l','A'),('l','N')],
    ['capital L',('l','I'),('l','N'),('l','H'),'capital V',('l','O')],
    [('s','bao.ng'),'all lower case']]
UNS=['MaiAnh_98','jTran','LinhVo','bao.ng']
for i,u in enumerate(UN): clip(f'UN_{i}',f'Capitals/S01_username_{i+1}_{UNS[i]}.mp3',plan(u,SONIA),UNS[i])
ODD=[['A','H','J','E'],['B','D','F','T'],['M','N','L','I'],['Q','U','W','O'],['G','P','V','K'],['S','X','R','F']]
for i,o in enumerate(ODD):
    k=[]
    for X in o: k+=[want(SONIA,X),.55]
    clip(f'ODD_{i}',f'Odd_one_out/S01_odd_{i+1}_{"".join(o)}.mp3',k,'Odd one out '+' '.join(o))
QUIZ=['E','G','A','V','N','J','I','R','H','Q','Y','X']
for i,q in enumerate(QUIZ):
    clip(f'Q_{i}',f'Listening1_Which_letter/S01_L1_item{i+1:02d}.mp3',[want(SONIA,q),.9,want(SONIA,q)],f'Item {i+1}')
SPELL=[['Tom','Nam','Anna','Linh'],['Sarah','James','Hieu','Giang'],['Phuong','Nguyen','Quynh','Jackson'],['Phillips','Wright','anh.tran@gmail.com','mai_vu@yahoo.com']]
LVN=['Easy','Medium','Hard','Challenge']
for L,lst in enumerate(SPELL):
    for k,n in enumerate(lst):
        clip(f'SP_{L}_{k}',f'Spell_the_names/S01_spell_{L+1}{LVN[L]}_{k+1}_{n.replace("@","_at_")}.mp3',plan([('s',n)],SONIA,gap=.3),f'{LVN[L]} {k+1}: {n}')
ASK=['How do you spell your name?','How do you spell that?','Could you spell that again, please?','Sorry, was that M or N?','Is that double L?','Is that a capital letter?']
for i,t in enumerate(ASK): clip(f'TKA_{i}',f'Spelling_toolkit/S01_ask_{i+1}.mp3',[want(SONIA,t,'-5%')],t)
ANS=[["It's",('s','LINH')],["That's double S."],['B as in "boy".'],['V as in "Vietnam".'],["Yes, that's right."],['All lower case.']]
for i,s in enumerate(ANS): clip(f'TKB_{i}',f'Spelling_toolkit/S01_answer_{i+1}.mp3',plan(s,SONIA,rate='-5%'),str(s))
SYM=['at','dot','underscore','hyphen','dot com','double S']
for i,t in enumerate(SYM): clip(f'TKS_{i}',f'Spelling_toolkit/S01_symbol_{i+1}_{t.replace(" ","_")}.mp3',[want(SONIA,t)],t)
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
clip('MODEL','Fluency/S01_spell_card_model.mp3',plan(["Hi, my name is Linh.","My first name is spelled",('s','LINH'),"My surname is spelled",('s','NGUYEN'),"My email address is",('s','thuylinh_ng@gmail.com'),"That's all lower case. Thank you!"],SONIA,rate='-5%'),'Model answer')

asyncio.run(fetch_all())
manifest={}
for cid,(fn,keys,label) in CLIPS.items():
    a=render(keys); p=os.path.join(OUT,fn); os.makedirs(os.path.dirname(p),exist_ok=True)
    subprocess.run(['ffmpeg','-v','error','-y','-f','f32le','-ar',str(SR),'-ac','1','-i','-','-codec:a','libmp3lame','-b:a','64k',p],input=a.tobytes(),check=True)
    manifest[cid]={'file':fn,'label':label,'dur':round(len(a)/SR,2)}
json.dump(manifest,open('manifest.json','w'),indent=1)
print(len(manifest),'clips;',len(need),'tts requests')
