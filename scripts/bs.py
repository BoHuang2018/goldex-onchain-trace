from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
import requests, json, time, os, hashlib
BASES={'eth':'https://eth.blockscout.com/api/v2','base':'https://base.blockscout.com/api/v2','arb':'https://arbitrum.blockscout.com/api/v2','op':'https://optimism.blockscout.com/api/v2','polygon':'https://polygon.blockscout.com/api/v2'}
CACHE=str(ROOT)+'/data/raw/cache'; os.makedirs(CACHE,exist_ok=True)
S=requests.Session(); S.headers['User-Agent']='Mozilla/5.0'
def get(url,params=None,cache=True):
    key=hashlib.md5((url+json.dumps(params,sort_keys=True)).encode()).hexdigest()
    p=f'{CACHE}/{key}.json'
    if cache and os.path.exists(p): return json.load(open(p))
    for i in range(6):
        try:
            r=S.get(url,params=params,timeout=40)
            if r.status_code==429: time.sleep(3+i*3); continue
            if r.status_code==404: d={'_404':True}; break
            r.raise_for_status(); d=r.json(); break
        except Exception as e:
            err=e; time.sleep(2+i*2)
    else: raise Exception(f'fail {url} {err}')
    json.dump(d,open(p,'w')); return d
def tx(h,chain='eth'): return get(f'{BASES[chain]}/transactions/{h}')
def txtt(h,chain='eth'): return get(f'{BASES[chain]}/transactions/{h}/token-transfers')
def addr(a,chain='eth'): return get(f'{BASES[chain]}/addresses/{a}')
def tokbal(a,chain='eth'): return get(f'{BASES[chain]}/addresses/{a}/token-balances')
def transfers(a,chain='eth',maxpages=50,filt=None):
    out=[];params={'type':'ERC-20'}
    if filt: params['filter']=filt
    for _ in range(maxpages):
        d=get(f'{BASES[chain]}/addresses/{a}/token-transfers',params)
        out+=d.get('items',[])
        n=d.get('next_page_params')
        if not n: break
        params={'type':'ERC-20',**({'filter':filt} if filt else {}),**{k:str(v) for k,v in n.items()}}
    return out
def label(a,chain='eth'):
    d=addr(a,chain)
    tags=[t['name'] for t in (d.get('metadata') or {}).get('tags',[])] if d.get('metadata') else []
    return {'name':d.get('name'),'tags':tags,'contract':d.get('is_contract'),'coin':d.get('coin_balance'),'ens':d.get('ens_domain_name')}
def simp(t):
    tok=t['token']; dec=int(tok.get('decimals') or 18)
    v=int(t['total'].get('value') or 0)/10**dec if t.get('total') else 0
    return dict(time=t['timestamp'],frm=t['from']['hash'],to=t['to']['hash'],sym=tok.get('symbol'),amt=v,tx=t['transaction_hash'],tokaddr=tok['address_hash'] if 'address_hash' in tok else tok.get('address'))
import re, html as _h
def eslabel(a):
    a=a.lower(); p=f'{CACHE}/es_{a}.txt'
    if os.path.exists(p): return open(p).read()
    for i in range(4):
        r=S.get(f'https://etherscan.io/address/{a}',headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/125 Safari/537.36'},timeout=30)
        t=re.search(r'<title>\s*(.*?)\s*</title>',r.text,re.S)
        if t and 'Etherscan' in t.group(1): break
        time.sleep(3)
    t=_h.unescape(t.group(1)).strip() if t else ''
    lab=t.split('|')[0].strip()
    if lab.lower().startswith('address') or lab.lower().startswith('contract'): lab=''
    # also check warning/phish
    pass
    open(p,'w').write(lab); time.sleep(0.6); return lab
USDT='0xdac17f958d2ee523a2206206994597c13d831ec7'; USDC='0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48'
def ltx(a,token,sb,eb):
    out=[];page=1
    while True:
        r=get('https://eth.blockscout.com/api',{'module':'account','action':'tokentx','address':a,'contractaddress':token,'startblock':str(sb),'endblock':str(eb),'sort':'asc','offset':'1000','page':str(page)})
        res=r.get('result') or []
        if isinstance(res,str): raise Exception(res)
        out+=res
        if len(res)<1000: break
        page+=1
    return [dict(time=time.strftime('%Y-%m-%dT%H:%M',time.gmtime(int(x['timeStamp']))),frm=x['from'],to=x['to'],sym=x['tokenSymbol'],amt=int(x['value'])/10**int(x['tokenDecimal']),tx=x['hash'],block=int(x['blockNumber'])) for x in out]
