from pwnlib.util.cyclic import *

c = cyclic(100)
pos = cyclic_find(b'baaa')
print(pos)