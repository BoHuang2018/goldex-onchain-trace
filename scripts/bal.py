from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
from bs import *
import json
A={'0x9e4a53D4eBf53594Ac004Bcd3B443db17cB74B81':'詐騙入金 #1','0xEF0776617364dd4Df0C1A12642D1a211E45C18bf':'詐騙入金 #2','0xc5D40064Bb1683A91ebE6117ACF4880a6a2D17A3':'詐騙入金 #3','0xdb685588535daba6c971450128f86d72c94f4002':'詐騙入金 #4','0xdca1bed54a13b4eaab1d8568935745becbfeca60':'詐騙入金 #5',
'0xf68540248F124D871FE34941ba8936C2655EA5A6':'出金錢包 A','0xd199416AF0882d9eFf042502adCF38F2d676eE46':'出金錢包 B','0x0457DbCc707CAc75F9849153233F5b16B5aD67b1':'出金錢包 C','0x225a8d7b30f7830f8dadf3dd5a0d92e895e80d06':'假稅地址',
'0x0bFCe0574ee5ef4dAb2d6e7Bf0F1EB359DEF4AD1':'歸集錢包 H1','0xc5D0af894EE89E6304cD84048678556cE99Cb14C':'歸集錢包 H2','0x9FC2813fAe90b100Ef4B2a0254Ab2529f71922D9':'中轉 R1','0xdb037e856332D0A8dDE4249C8D507FFB044FCCB0':'中轉 R2','0x505526C0E42864E8c84822fE8C4367e0BCC11134':'中轉 R3','0x0132683b3f35A79400824872Df7527a1392F231a':'中轉 R4','0x0438DB3AB49Fc1313D65b1FC2422f5e85cfD8E02':'中轉 R5','0x35F7db19885a3d4c3B471D0d2118c7914Bf62627':'中轉 R6','0x7cBf20c3212Dc076d66E3b4e1C6f9c310174c928':'中轉 R7','0xD33706b3ebb32F12f9FF61c77678711A299e56E8':'中轉 R8',
'0xDA2142378e6dB3423965C14dE6F5D0876c69Af0a':'大型洗錢樞紐 X1','0xfEF2a9E08D92Fb348485219DDb5322fE24960477':'大型歸集樞紐 X2','0xDe8d7BdD9C0e9182dc0bfD4Ab16A280871eb79A5':'X2 下游 X3','0x97915f7decbec83814afe9d6bfc773431942acc4':'X2 下游 X4','0x11235534a66a33c366b84933d5202c841539d1c9':'終點 X5 (PDF稱Bitget)','0xAddC0a707984978617d790D5B7CBdb3Abe834B53':'OTC型 Y1','0x53fF606a6D7116e18ee9Dca80824Fa0d70bCF1EB':'OTC型 Y2','0x132ED574f32B739feBF95d9D6Bd2f24001aEafDc':'OTC型 Y3','0xF6646DFF904ce2924c3cB3018D28F9Aa55f7b921':'OTC型 Y4','0xD4D63125735Eb997FAf89aDd73C48764134C39fE':'Y5'}
R=USDC,USDT
out=[]
for a,n in A.items():
    tb=get(f'https://eth.blockscout.com/api/v2/addresses/{a}/token-balances',cache=False)
    usdc=usdt=0
    if isinstance(tb,list):
        for t in tb:
            ad=(t['token'].get('address_hash') or t['token'].get('address') or '').lower()
            if ad==USDC: usdc=int(t['value'])/1e6
            if ad==USDT: usdt=int(t['value'])/1e6
    d=get(f'https://eth.blockscout.com/api/v2/addresses/{a}',cache=False)
    eth=int(d.get('coin_balance') or 0)/1e18
    out.append(dict(addr=a,name=n,usdc=usdc,usdt=usdt,eth=eth))
    print(n,a,'USDC',round(usdc,2),'USDT',round(usdt,2),'ETH',round(eth,5))
json.dump(out,open(str(ROOT)+'/data/raw/balances.json','w'),ensure_ascii=False)
