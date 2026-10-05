from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
from bs import *
import collections,json
a='0xda2142378e6db3423965c14de6f5d0876c69af0a'
L=ltx(a,USDT,23200000,23500000)
json.dump(L,open(str(ROOT)+'/data/raw/da21_usdt.json','w'))
print(len(L),L[0]['time'],L[-1]['time'])
ins=[x for x in L if x['to']==a and x['amt']>0]; outs=[x for x in L if x['frm']==a and x['amt']>0]
print('in',len(ins),round(sum(x['amt'] for x in ins)),'out',len(outs),round(sum(x['amt'] for x in outs)))
c=collections.Counter()
for x in outs: c[x['to']]+=x['amt']
for k,v in c.most_common(15): print('OUT',k,round(v))
c=collections.Counter()
for x in ins: c[x['frm']]+=x['amt']
for k,v in c.most_common(10): print('IN',k,round(v))
