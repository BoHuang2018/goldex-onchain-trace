import re,glob,json,os,datetime as dt
from zoneinfo import ZoneInfo
H=set()
for f in glob.glob('raw/**/*.json',recursive=True):
    H.update(re.findall(r'0x[0-9a-fA-F]{64}',open(f).read()))
H={h.lower() for h in H}
def full(p):
    p=p.lower(); m=[h for h in H if h.startswith(p)]
    if len(m)!=1: raise Exception(f'prefix {p} -> {len(m)}')
    return m[0]
LAB={
'0x46340b20830761efd32832a74d7169b29feb9758':'Crypto.com 12 熱錢包 (Etherscan)',
'0xee7ae85f2fe2239e27d9c1e23fffe168d63b4055':'Binance Hot Wallet 34 (Etherscan)',
'0x9642b23ed1e01df1092b92641051881a322f5d4e':'MEXC 16 熱錢包 (Etherscan)',
'0x9e4a53d4ebf53594ac004bcd3b443db17cb74b81':'詐騙入金地址 #1',
'0xef0776617364dd4df0c1a12642d1a211e45c18bf':'詐騙入金地址 #2',
'0xc5d40064bb1683a91ebe6117acf4880a6a2d17a3':'詐騙入金地址 #3',
'0xdb685588535daba6c971450128f86d72c94f4002':'詐騙入金地址 #4',
'0xdca1bed54a13b4eaab1d8568935745becbfeca60':'詐騙入金地址 #5',
'0x0bfce0574ee5ef4dab2d6e7bf0f1eb359def4ad1':'H1 詐騙歸集錢包 (未標記)',
'0xc5d0af894ee89e6304cd84048678556ce99cb14c':'H2 詐騙歸集錢包 (未標記)',
'0x4a14347083b80e5216ca31350a2d21702ac3650d':'Tokenlon AMM 兌換合約 (Etherscan)',
'0x9fc2813fae90b100ef4b2a0254ab2529f71922d9':'R1 中轉 (未標記)',
'0xdb037e856332d0a8dde4249c8d507ffb044fccb0':'R2 中轉 (未標記)',
'0x505526c0e42864e8c84822fe8c4367e0bcc11134':'R3 中轉 (未標記)',
'0x0132683b3f35a79400824872df7527a1392f231a':'R4 中轉 (未標記)',
'0x0438db3ab49fc1313d65b1fc2422f5e85cfd8e02':'R5 中轉 (未標記)',
'0x35f7db19885a3d4c3b471d0d2118c7914bf62627':'R6 中轉 (未標記)',
'0x7cbf20c3212dc076d66e3b4e1c6f9c310174c928':'R7 中轉 (未標記)',
'0xda2142378e6db3423965c14de6f5d0876c69af0a':'X1 大型洗錢樞紐 (未標記; tayvano 研究列為 Theft-Comingled)',
'0xfef2a9e08d92fb348485219ddb5322fe24960477':'X2 大型歸集樞紐 (2025-10-16 被 Tether 凍結)',
'0xde8d7bdd9c0e9182dc0bfd4ab16a280871eb79a5':'X3 中轉樞紐 (未標記)',
'0x97915f7decbec83814afe9d6bfc773431942acc4':'X4 樞紐 (2025-10-16 被 Tether 凍結)',
'0x11235534a66a33c366b84933d5202c841539d1c9':'X5 高頻服務地址 (13萬筆交易; 未標記; PDF 稱 Bitget, 未證實)',
'0xf68540248f124d871fe34941ba8936c2655ea5a6':'出金錢包 A (假提領)',
'0xd199416af0882d9eff042502adcf38f2d676ee46':'出金錢包 B (假提領)',
'0x0457dbcc707cac75f9849153233f5b16b5ad67b1':'出金錢包 C (假提領; 也收 #5 的錢)',
'0xaddc0a707984978617d790d5b7cbdb3abe834b53':'Y1 OTC 型中轉 (未標記)',
'0x53ff606a6d7116e18ee9dca80824fa0d70bcf1eb':'Y2 OTC 型中轉 (未標記)',
'0x132ed574f32b739febf95d9d6bd2f24001aeafdc':'Y3 OTC 型中轉 (未標記)',
'0xd4d63125735eb997faf89add73c48764134c39fe':'Y5 X2 的接替歸集錢包 (未標記)',
'0x5a5c6fb3696e3caa2208ebd3b2fb0888609f5cf4':'中轉 (A→此→X2; 未標記)',
'0xd6e7f03ebd4aad7a0210fe08fe7ed1cbacc6cc18':'Picasso 的 MEXC 入金地址',
'0xc803bbd1696863bab1135c67df85f354069caf2d':'Picasso 的 Binance 入金地址 (Etherscan: Binance Deposit)',
'0xb15fb9fbd4030b226568f364779d71902b4031df':'Picasso 的 Crypto.com 入金地址',
'0x53111926268275d7b2a223e0dff6b422842eb00b':'未標記 (資助 A)',
'0xcf595b7c23fa21d88fb547c3ebe620f37ba602d4':'未標記 (資助 A/C)',
'0xc847493177312bff0fac8b915f3fc43ded19d08b':'未標記 (資助 C; 也替 #5 付 gas)',
'bc1ptd59u475ynjgkqx5z4afmj6xcdmw6wufa2n6p9z29q9x36efq56qcylnvm':'詐騙 BTC 入金地址',
'13ZncoU2nomZStLChHJvefEjWm1kp14V3z':'Binance BTC 入金地址 (歸集到 Binance 儲備錢包)',
'bc1qm34lsc65zpw79lxes69zkqmk6ee3ewf0j77s3h':'Binance BTC 熱/儲備錢包 (Binance PoR)',
}
def ab(a):
    return a if a.startswith(('bc1','1','3')) else a.lower()
HOPS=[]
def add(chunk,step,frm,to,tok,amt,utc,pfx,note=''):
    tx=pfx if len(pfx)==64 else full(pfx)
    HOPS.append(dict(chunk=chunk,step=step,frm=frm,to=to,tok=tok,amt=amt,utc=utc,tx=tx,note=note))
