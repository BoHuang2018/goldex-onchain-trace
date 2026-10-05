from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
from bs import *
import sys
a=sys.argv[1].lower(); sb=int(sys.argv[2]); eb=int(sys.argv[3])
L=[]
for tok in (USDC,USDT): L+=ltx(a,tok,sb,eb)
L.sort(key=lambda x:(x['block']))
# need starting balance: get balance at sb-1 via sum? approximate by computing from first records; use blockscout coin? Use running sum from sb with offset unknown -> compute relative then fix with final known balance at freeze
bal=0;pts=[]
for x in L:
    if x['amt']==0: continue
    if x['to'].lower()==a: bal+=x['amt']
    if x['frm'].lower()==a: bal-=x['amt']
    pts.append((x['time'],x['block'],bal,x['tx']))
print(len(L),'final relative',round(bal,2))
for mark in sys.argv[4:]:
    m=int(mark); sub=[p for p in pts if p[1]>=m]
    mn=min(sub,key=lambda p:p[2])
    print('after block',m,'min relative bal',round(mn[2],2),'at',mn[0],mn[3][:14],'end',round(sub[-1][2],2))
import json; json.dump(pts,open(fstr(ROOT)+'/data/raw/libr_{a}.json','w'))
