from bs import *
import sys
for a in sys.argv[1:]:
    c=get(f'https://eth.blockscout.com/api/v2/addresses/{a}/counters')
    print(a,c.get('transactions_count'),c.get('token_transfers_count'),repr(eslabel(a)))
