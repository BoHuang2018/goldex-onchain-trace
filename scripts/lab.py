from bs import *
import sys
for a in sys.argv[1:]:
    l=label(a); print(a,repr(eslabel(a)),'C' if l['contract'] else 'EOA',l['name'],l['tags'])
