from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
import json,sys
REAL={'0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48':'USDC','0xdac17f958d2ee523a2206206994597c13d831ec7':'USDT'}
def load(a):
    a=a.lower()
    return [t for t in sorted(json.load(open(fstr(ROOT)+'/data/raw/tr_{a}.json')),key=lambda x:x['time']) if (t['tokaddr'] or '').lower() in REAL and t['amt']>0.01]
if __name__=='__main__':
    for a in sys.argv[1:]:
        a=a.lower(); print('#####',a); bal=0
        for t in load(a):
            o=t['frm'].lower()==a; bal+= -t['amt'] if o else t['amt']
            print(t['time'][:16],'OUT' if o else 'IN ',t['sym'],round(t['amt'],2),(t['to'] if o else t['frm']),t['tx'][:12],'bal',round(bal,2))
