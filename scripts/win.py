from bs import *
import sys
a=sys.argv[1].lower(); sb,eb=int(sys.argv[2]),int(sys.argv[3]); mn=float(sys.argv[4]) if len(sys.argv)>4 else 100
L=[]
for tok in (USDC,USDT): L+=ltx(a,tok,sb,eb)
L.sort(key=lambda x:x['block'])
for x in L:
    if x['amt']<mn: continue
    o=x['frm'].lower()==a
    print(x['time'],'OUT' if o else 'IN ',x['sym'],round(x['amt'],2),x['to'] if o else x['frm'],x['tx'])
