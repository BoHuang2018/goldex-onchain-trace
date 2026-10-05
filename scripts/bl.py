import requests,json,sys
rpc='https://ethereum-rpc.publicnode.com'
T='0x42e160154868087d6bfdc0ca23d96a1c1cfa32f1b72ba9ba27b69b98a0d819dc'
targets={'fef2a9e08d92fb348485219ddb5322fe24960477':'X2','97915f7decbec83814afe9d6bfc773431942acc4':'X4'}
head=int(requests.post(rpc,json={'jsonrpc':'2.0','id':1,'method':'eth_blockNumber','params':[]}).json()['result'],16)
start=int(sys.argv[1]); step=int(sys.argv[2])
b=start;found=[]
while b<head:
    e=min(b+step-1,head)
    r=requests.post(rpc,json={'jsonrpc':'2.0','id':1,'method':'eth_getLogs','params':[{'address':'0xdac17f958d2ee523a2206206994597c13d831ec7','topics':[T],'fromBlock':hex(b),'toBlock':hex(e)}]},timeout=60).json()
    if 'error' in r: print('err',b,r['error']); break
    for l in r['result']:
        a=l['data'][-40:]
        if a in targets: print('FOUND',targets[a],int(l['blockNumber'],16),l['transactionHash']); found.append(l)
    b=e+1
print('done',head)
