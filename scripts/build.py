from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
import sys,json,csv
sys.path.insert(0, '.')
from hops import *
import bs
from zoneinfo import ZoneInfo
A=dict(cc='0x46340b20830761efd32832a74d7169b29feb9758',bn='0xee7ae85f2fe2239e27d9c1e23fffe168d63b4055',mx='0x9642b23ed1e01df1092b92641051881a322f5d4e',
d1='0x9e4a53d4ebf53594ac004bcd3b443db17cb74b81',d2='0xef0776617364dd4df0c1a12642d1a211e45c18bf',d3='0xc5d40064bb1683a91ebe6117acf4880a6a2d17a3',d4='0xdb685588535daba6c971450128f86d72c94f4002',d5='0xdca1bed54a13b4eaab1d8568935745becbfeca60',
h1='0x0bfce0574ee5ef4dab2d6e7bf0f1eb359def4ad1',h2='0xc5d0af894ee89e6304cd84048678556ce99cb14c',tk='0x4a14347083b80e5216ca31350a2d21702ac3650d',
r1='0x9fc2813fae90b100ef4b2a0254ab2529f71922d9',r2='0xdb037e856332d0a8dde4249c8d507ffb044fccb0',r3='0x505526c0e42864e8c84822fe8c4367e0bcc11134',r4='0x0132683b3f35a79400824872df7527a1392f231a',r5='0x0438db3ab49fc1313d65b1fc2422f5e85cfd8e02',r6='0x35f7db19885a3d4c3b471d0d2118c7914bf62627',r7='0x7cbf20c3212dc076d66e3b4e1c6f9c310174c928',
x1='0xda2142378e6db3423965c14de6f5d0876c69af0a',x2='0xfef2a9e08d92fb348485219ddb5322fe24960477',x3='0xde8d7bdd9c0e9182dc0bfd4ab16a280871eb79a5',x4='0x97915f7decbec83814afe9d6bfc773431942acc4',x5='0x11235534a66a33c366b84933d5202c841539d1c9',
pa='0xf68540248f124d871fe34941ba8936c2655ea5a6',pb='0xd199416af0882d9eff042502adcf38f2d676ee46',pc='0x0457dbcc707cac75f9849153233f5b16b5ad67b1',
y1='0xaddc0a707984978617d790d5b7cbdb3abe834b53',y2='0x53ff606a6d7116e18ee9dca80824fa0d70bcf1eb',y3='0x132ed574f32b739febf95d9d6bd2f24001aeafdc',y5='0xd4d63125735eb997faf89add73c48764134c39fe',z='0x5a5c6fb3696e3caa2208ebd3b2fb0888609f5cf4',
bomx='0xd6e7f03ebd4aad7a0210fe08fe7ed1cbacc6cc18',bobn='0xc803bbd1696863bab1135c67df85f354069caf2d',bocc='0xb15fb9fbd4030b226568f364779d71902b4031df',
f1='0x53111926268275d7b2a223e0dff6b422842eb00b',f2='0xcf595b7c23fa21d88fb547c3ebe620f37ba602d4',f3='0xc847493177312bff0fac8b915f3fc43ded19d08b')
R=[ # chunk, step, from, to, tok, txprefix, note
('入金',0,'cc','d1','USDC','0xdb3691613c9c','Picasso 8/11 存入'),('入金',0,'cc','d1','USDC','0x727eaf960840','Picasso 8/11 存入'),
('入金',0,'cc','d2','USDC','0xdb485bcf43b5','Picasso 8/18 存入 (xlsx 寫 1519.3; 鏈上 1509.3)'),('入金',0,'bn','d2','USDC','0xd6924cb29e1e','Picasso 8/18 存入'),
('入金',0,'cc','d3','USDC','0xed5f0c90bc','Picasso 8/22 存入'),('入金',0,'bn','d3','USDC','0x3553a9bf3f','Picasso 8/25 存入'),
('入金',0,'bn','d4','USDC','0x64c6f7e7c0','Picasso 9/04 存入'),('入金',0,'mx','d4','USDC','0xb6b2d38783','Picasso 9/12 存入 (更正後 tx)'),('入金',0,'mx','d4','USDC','0xd522c121df','Picasso 9/18 存入'),
('入金',0,'mx','d5','USDC','0x94a2ef7a13','Picasso 10/20 存入'),('入金',0,'mx','d5','USDC','0x9e265d2165','Picasso 10/30 存入'),
# chunk A
('A: #1/#2/#3餘額→H1→X1',1,'d1','h1','USDC','0xc628f0b423','全為 Picasso 的 1394 + 他人 570'),('A: #1/#2/#3餘額→H1→X1',1,'d2','h1','USDC','0xa66eb6cc48','100% Picasso'),('A: #1/#2/#3餘額→H1→X1',1,'d3','h1','USDC','0x9a6d30bb19','FIFO: 其中 Picasso 約 3325.05'),
('A: #1/#2/#3餘額→H1→X1',2,'h1','tk','USDC','0x016d698c6b','H1 把 USDC 換成 USDT (同一錢包)'),
('A: #1/#2/#3餘額→H1→X1',3,'h1','r1','USDT','0x5de5bd9fb2','混合資金'),('A: #1/#2/#3餘額→H1→X1',4,'r1','r2','USDT','0xce682d9fa0',''),('A: #1/#2/#3餘額→H1→X1',5,'r2','x1','USDT','0x784dab26f2','到達 X1'),
('A: #1/#2/#3餘額→H1→X1',3,'h1','r6','USDC','0xdb0f4a8980',''),('A: #1/#2/#3餘額→H1→X1',4,'r6','x2','USDC','0x44a5a1be47','到達 X2'),
('A: #1/#2/#3餘額→H1→X1',3,'h1','r1','USDT','0x00e273b09a',''),('A: #1/#2/#3餘額→H1→X1',4,'r1','r2','USDT','0xa6eb15e18f',''),('A: #1/#2/#3餘額→H1→X1',5,'r2','x1','USDT','0x422f4844c0','到達 X1'),
('A: #1/#2/#3餘額→H1→X1',3,'h1','r4','USDT','0xd688e60b15',''),('A: #1/#2/#3餘額→H1→X1',4,'r4','x1','USDT','0x105ac94779','到達 X1'),
('A: #1/#2/#3餘額→H1→X1',3,'h1','r4','USDT','0xd68ca96d41',''),('A: #1/#2/#3餘額→H1→X1',4,'r4','x1','USDT','0x0a33b27309','到達 X1 (含 A 錢包 1200)'),
('A: #1/#2/#3餘額→H1→X1',3,'h1','r3','USDT','0xa2c70f9029',''),('A: #1/#2/#3餘額→H1→X1',4,'r3','x1','USDT','0xff13dcddd7','到達 X1'),
('A: #1/#2/#3餘額→H1→X1',3,'h1','r1','USDT','0x3af49300d7',''),('A: #1/#2/#3餘額→H1→X1',4,'r1','r2','USDT','0xefc4bb5a1f',''),('A: #1/#2/#3餘額→H1→X1',5,'r2','x1','USDT','0x9cd9c0996d','到達 X1'),
('A: #1/#2/#3餘額→H1→X1',3,'h1','r4','USDT','0xef126bc3a7',''),('A: #1/#2/#3餘額→H1→X1',4,'r4','x1','USDT','0x5e9edb0e35','到達 X1'),
# chunk B
('B: #3 的 17,836→H2→X2→X3→X4→X5',1,'d3','h2','USDC','0xf143e33272','FIFO: 其中 Picasso 17,836.00'),('B: #3 的 17,836→H2→X2→X3→X4→X5',2,'h2','x2','USDC','0x7eca0e916d','與另一地址的 20,000 合併'),
('B: #3 的 17,836→H2→X2→X3→X4→X5',3,'x2','tk','USDC','0xb8d44217de','X2 把 USDC 換成 USDT'),('B: #3 的 17,836→H2→X2→X3→X4→X5',4,'x2','x3','USDT','0xffc43c2d9b','兌換後 3 分鐘轉出'),
('B: #3 的 17,836→H2→X2→X3→X4→X5',5,'x3','x4','USDT','0x756c8e334c','原額轉出'),
('B: #3 的 17,836→H2→X2→X3→X4→X5',6,'x4','x5','USDT','0xc41768262d','X4 隨後清空 (餘額歸零 9/04)'),('B: #3 的 17,836→H2→X2→X3→X4→X5',6,'x4','x5','USDT','0xda563a0667',''),('B: #3 的 17,836→H2→X2→X3→X4→X5',6,'x4','x5','USDT','0xf616e1e183',''),('B: #3 的 17,836→H2→X2→X3→X4→X5',6,'x4','x5','USDT','0x99af47b6a0',''),
# chunk C
('C: #4 的 60,000→H2→X2→X3→X5',1,'d4','h2','USDC','0x0898e89483','100% Picasso (9/04 存入 6 小時後)'),('C: #4 的 60,000→H2→X2→X3→X5',2,'h2','x2','USDC','0xf6d9e02e28','與他人 25,000 合併'),
('C: #4 的 60,000→H2→X2→X3→X5',3,'x2','tk','USDC','0xd9b9978c51','X2 換成 USDT'),('C: #4 的 60,000→H2→X2→X3→X5',4,'x2','x3','USDT','0xc25802aec8','下一筆 USDT 轉出'),
]+[('C: #4 的 60,000→H2→X2→X3→X5',5,'x3','x5','USDT',p,'') for p in ['0x39fe2f7bf0','0x324de68352','0x03806b180c','0x41f14a6de2','0x8961b2b4e8','0x02250d42dc','0xdc2c7a9cc4','0x7358151458','0xa69f331c33','0xc2c49b8681','0x4230bcd152','0xf5179279f3']]+[
# chunk D
('D: #4 的 10,000→R1→X1',1,'d4','r1','USDC','0x4fa425d352','100% Picasso'),('D: #4 的 10,000→R1→X1',2,'r1','tk','USDC','0x3cb62d0ee8','R1 換成 USDT'),
('D: #4 的 10,000→R1→X1',3,'r1','r4','USDT','0xce3add9d91',''),('D: #4 的 10,000→R1→X1',4,'r4','x1','USDT','0xe0abc28e8f','到達 X1'),
('D: #4 的 10,000→R1→X1',3,'r1','r2','USDT','0xc6d70f1fdc',''),('D: #4 的 10,000→R1→X1',4,'r2','x1','USDT','0x8140047766','到達 X1'),
# chunk E
('E: #4 的 23,007→H1→R3→X1',1,'d4','h1','USDC','0x501bafa597','FIFO: Picasso 23,007.24 (+可能 2,303)'),('E: #4 的 23,007→H1→R3→X1',2,'h1','tk','USDC','0x8338dfa2e5','H1 換 90,000 → USDT'),
('E: #4 的 23,007→H1→R3→X1',3,'h1','r3','USDT','0xdc2670db98','整筆 90,000'),('E: #4 的 23,007→H1→R3→X1',4,'r3','x1','USDT','0x4a4419eb55','1 分鐘後到 X1'),
# chunk F
('F: #4 的 7,961→H1→X1',1,'d4','h1','USDC','0x99455d2775','100% Picasso'),('F: #4 的 7,961→H1→X1',2,'h1','tk','USDC','0x1b33d78d33',''),
('F: #4 的 7,961→H1→X1',3,'h1','r4','USDT','0xfad180edb5',''),('F: #4 的 7,961→H1→X1',4,'r4','x1','USDT','0x3dd6a83e6e','到達 X1'),
('F: #4 的 7,961→H1→X1',3,'h1','r5','USDT','0x1946d1d7e3',''),('F: #4 的 7,961→H1→X1',4,'r5','x1','USDT','0x93ea9b01f7','到達 X1'),
('F: #4 的 7,961→H1→X1',3,'h1','r2','USDT','0x531af1b0ad',''),('F: #4 的 7,961→H1→X1',4,'r2','x1','USDT','0x710d7970a3','到達 X1'),
# chunk G
('G: #4 的 8,078 (9/18)',1,'d4','pa','USDC','0x545872545c','流入出金錢包 A'),('G: #4 的 8,078 (9/18)',2,'pa','z','USDC','0xc4f120bada',''),('G: #4 的 8,078 (9/18)',3,'z','x2','USDC','0x183b53ce77','進入 X2'),
('G: #4 的 8,078 (9/18)',4,'x2','x4','USDT','0x2dc599c052','X2 下一筆大額轉出 (9/25)'),
('G: #4 的 8,078 (9/18)',1,'d4','r1','USDC','0x009c0a56a3',''),('G: #4 的 8,078 (9/18)',2,'r1','tk','USDC','0x6bafde9ab0',''),('G: #4 的 8,078 (9/18)',3,'r1','r2','USDT','0xafc2f8cd77',''),('G: #4 的 8,078 (9/18)',4,'r2','x1','USDT','0x14c41a859c','到達 X1'),
# chunk H
('H: #5 的 35,066',1,'d5','pc','USDC','0x674fd0d25c','100% Picasso'),('H: #5 的 35,066',2,'pc','bomx','USDC','0xe866041f40','以「提領」名義退回 Picasso 的 MEXC'),
('H: #5 的 35,066',1,'d5','pc','USDC','0x04f3681b23',''),('H: #5 的 35,066',2,'pc','tk','USDC','0xab19568fd3',''),('H: #5 的 35,066',3,'pc','r2','USDT','0x6862b46200',''),('H: #5 的 35,066',3,'pc','r2','USDT','0xbd2e5a97ca',''),('H: #5 的 35,066',4,'r2','y1','USDT','0xdb1a909371','到 Y1'),('H: #5 的 35,066',4,'r2','y1','USDT','0xe9e5249dad','到 Y1'),
('H: #5 的 35,066',1,'d5','pc','USDC','0xd1b9dd82fa',''),('H: #5 的 35,066',2,'pc','tk','USDC','0xce0d0a1808',''),('H: #5 的 35,066',3,'pc','r2','USDT','0x6e45d92f69',''),('H: #5 的 35,066',4,'r2','y2','USDT','0x4d3f32f0e8','到 Y2'),
('H: #5 的 35,066',1,'d5','r7','USDC','0x5b524624ea',''),('H: #5 的 35,066',2,'r7','y5','USDC','0x6e453e3104','到 Y5'),
('H: #5 的 35,066',1,'d5','pc','USDC','0x3f7b2c57ca',''),('H: #5 的 35,066',2,'pc','tk','USDC','0x8fd53b832f',''),('H: #5 的 35,066',3,'pc','r2','USDT','0x4b8a70501d',''),('H: #5 的 35,066',4,'r2','y3','USDT','0x7070cc02f1','到 Y3'),
# payouts
('假提領 (付給 Picasso)',0,'h1','pa','USDC','0x3b5efc180a','A 的資金來源'),('假提領 (付給 Picasso)',1,'pa','bocc','USDC','0x67076931f9','8/12 付 Picasso'),
('假提領 (付給 Picasso)',0,'h1','pa','USDT','0xf43698128b','A 的資金來源'),('假提領 (付給 Picasso)',1,'pa','bobn','USDT','0xb4bed157ee','8/27 付 Picasso'),
('假提領 (付給 Picasso)',1,'pa','bobn','USDC','0x16e738855f','9/20 付 Picasso'),('假提領 (付給 Picasso)',1,'pa','bobn','USDC','0x1662213bd1','9/21 付 Picasso'),
('假提領 (付給 Picasso)',0,'f1','pa','USDC','0x70db74f839','A 的資金來源'),('假提領 (付給 Picasso)',1,'pa','bomx','USDC','0x0dcc0f6e62','9/30 付 Picasso'),
('假提領 (付給 Picasso)',1,'pb','bomx','USDC','0x98cb6187f9','10/06 付 Picasso'),
('假提領 (付給 Picasso)',0,'f3','pc','USDC','0xd068a8d54c','C 的資金來源 (另一筆是 Picasso 自己的 10,000)'),
('假提領 (付給 Picasso)',0,'f2','pa','USDC','0xa1ceb39f69','A 的資金來源'),('假提領 (付給 Picasso)',1,'pa','bomx','USDC','0x346b80bf3d','10/27 付 Picasso'),
]
rows=[]
osl=ZoneInfo('Europe/Oslo')
for ch,st,f,t,tok,p,note in R:
    h=full(p); fa,ta=A[f],A[t]
    d=bs.tx(h); tt=bs.txtt(h)
    amt=None
    for x in tt.get('items',[]):
        s=bs.simp(x)
        if s['frm'].lower()==fa and s['to'].lower()==ta and s['sym']==tok and (s['tokaddr'] or '').lower() in (bs.USDC,bs.USDT): amt=s['amt']
    if amt is None: raise Exception(f'no match {p} {f}->{t} {tok}')
    ts=dt.datetime.fromisoformat(d['timestamp'].replace('Z','+00:00'))
    rows.append(dict(chunk=ch,step=st,**{'from':fa,'to':ta},token=tok,amount=round(amt,6),time_utc=ts.strftime('%Y-%m-%d %H:%M:%S UTC'),time_oslo=ts.astimezone(osl).strftime('%Y-%m-%d %H:%M:%S %Z'),tx=h,chain='Ethereum',from_label=LAB.get(fa,''),to_label=LAB.get(ta,''),note=note))
# BTC
rows.append(dict(chunk='BTC',step=0,**{'from':'(Crypto.com BTC 熱錢包) bc1q7cyrfmck2ffu2ud3rn5l5a8yv6f0chkp0zpemf','to':'bc1ptd59u475ynjgkqx5z4afmj6xcdmw6wufa2n6p9z29q9x36efq56qcylnvm'},token='BTC',amount=0.0004273,time_utc='2025-08-11 20:01:02 UTC',time_oslo='2025-08-11 22:01:02 CEST',tx='ef634137e480498d75785721b7de5914f9fa50ca5813ba28e179aa83b1be6c27',chain='Bitcoin',from_label='Crypto.com 提領 (依 xlsx)',to_label='詐騙 BTC 入金地址',note='Picasso 8/11 存入 42,730 sats'))
rows.append(dict(chunk='BTC',step=1,**{'from':'bc1ptd59u475ynjgkqx5z4afmj6xcdmw6wufa2n6p9z29q9x36efq56qcylnvm','to':'13ZncoU2nomZStLChHJvefEjWm1kp14V3z'},token='BTC',amount=0.18930936,time_utc='2025-09-01 01:17:58 UTC',time_oslo='2025-09-01 03:17:58 CEST',tx='9ea48a04bfa8007c599b29763245880f8c3b1c825ffbb008667c62b867a689a6',chain='Bitcoin',from_label='詐騙 BTC 入金地址',to_label=LAB['13ZncoU2nomZStLChHJvefEjWm1kp14V3z'],note='Picasso 的 0.0004273 與他人 0.18888713 一起花出'))
rows.append(dict(chunk='BTC',step=2,**{'from':'13ZncoU2nomZStLChHJvefEjWm1kp14V3z','to':'bc1qm34lsc65zpw79lxes69zkqmk6ee3ewf0j77s3h'},token='BTC',amount=89.55237299,time_utc='2025-09-01 02:48:27 UTC',time_oslo='2025-09-01 04:48:27 CEST',tx="db8aef3eb7f2592e69c1325cf24ab990aec92fa0445ff45988618d1d70c424dd",chain='Bitcoin',from_label=LAB['13ZncoU2nomZStLChHJvefEjWm1kp14V3z'],to_label=LAB['bc1qm34lsc65zpw79lxes69zkqmk6ee3ewf0j77s3h'],note='Binance 內部歸集 (多入一出)'))
json.dump(rows,open(str(ROOT)+'/data/raw/hops.json','w'),ensure_ascii=False,indent=1)
with open(str(ROOT)+'/data/hops.csv','w',newline='',encoding='utf-8-sig') as fo:
    w=csv.writer(fo); w.writerow(['from','to','token','amount','time_utc','time_oslo','tx','chain','label','chunk','step','note'])
    for r in rows: w.writerow([r['from'],r['to'],r['token'],r['amount'],r['time_utc'],r['time_oslo'],r['tx'],r['chain'],f"{r['from_label']} → {r['to_label']}",r['chunk'],r['step'],r['note']])
print(len(rows))
for r in rows: print(r['chunk'][:6],r['step'],r['amount'],r['time_oslo'],r['tx'][:12],r['note'][:20])
