from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
from bs import *
import sys,collections,json
a=sys.argv[1].lower(); sb,eb=int(sys.argv[2]),int(sys.argv[3])
L=[]
for tok in (USDC,USDT): L+=ltx(a,tok,sb,eb)
json.dump(L,open(fstr(ROOT)+'/data/raw/win_{a}_{sb}_{eb}.json','w'))
ins=[x for x in L if x['to'].lower()==a and x['amt']>0]; outs=[x for x in L if x['frm'].lower()==a and x['amt']>0]
print(a,'records',len(L),'in',len(ins),round(sum(x['amt'] for x in ins)),'out',len(outs),round(sum(x['amt'] for x in outs)))
for nm,S_,k in (('OUT',outs,'to'),('IN',ins,'frm')):
    c=collections.Counter(); n=collections.Counter()
    for x in S_: c[x[k]]+=x['amt']; n[x[k]]+=1
    for kk,v in c.most_common(int(sys.argv[4]) if len(sys.argv)>4 else 8): print(nm,kk,round(v),n[kk])
