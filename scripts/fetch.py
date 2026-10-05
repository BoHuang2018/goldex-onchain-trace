from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
from bs import *
import json,sys,os
for a in sys.argv[1:]:
    p=fstr(ROOT)+'/data/raw/tr_{a.lower()}.json'
    if not os.path.exists(p):
        tr=[simp(t) for t in transfers(a,maxpages=40)]
        json.dump(tr,open(p,'w'))
    else: tr=json.load(open(p))
    l=label(a)
    print(a,len(tr),repr(eslabel(a)),'contract' if l['contract'] else 'EOA',l['name'],l['tags'],'ETH',int(l['coin'] or 0)/1e18)
