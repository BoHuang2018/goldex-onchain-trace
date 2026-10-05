from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
import requests,time,json,os,hashlib
C=str(ROOT)+'/data/raw/cache'
def hist(addr,token,ts_before,ts_after,limit=1000):
    out=[];ts=ts_before
    while True:
        url=f'https://api.ethplorer.io/getAddressHistory/{addr}'
        prm={'apiKey':'freekey','token':token,'type':'transfer','limit':limit,'timestamp':ts}
        k=hashlib.md5(json.dumps([url,prm]).encode()).hexdigest(); p=f'{C}/ep_{k}.json'
        if os.path.exists(p): d=json.load(open(p))
        else:
            for i in range(5):
                r=requests.get(url,params=prm,timeout=60)
                if r.status_code==200 and 'operations' in r.json(): d=r.json(); break
                time.sleep(3+3*i)
            else: raise Exception(r.text[:300])
            json.dump(d,open(p,'w')); time.sleep(2)
        ops=d['operations']
        if not ops: break
        out+= [o for o in ops if o['timestamp']>=ts_after]
        last=min(o['timestamp'] for o in ops)
        if last<ts_after or len(ops)<limit: break
        ts=last
    # dedupe
    seen=set();res=[]
    for o in out:
        key=(o['transactionHash'],o['from'],o['to'],o['value'])
        if key in seen: continue
        seen.add(key);res.append(o)
    return res
