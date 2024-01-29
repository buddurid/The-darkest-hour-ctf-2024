
## fuck shellcode !!!! 

we start the challenge in a disassembler like IDA or ghidra and read the main func . it reads input from user then executes it as shellcode.

if you're not familiar with shellcode its litterally machine code . remember the return adress in the previous challenge , well that return address points to shellcode that the program converted from the code the user wrote in either c/assembly/whatever tf . 

you can code your own assembly (mawsa3 belek) then compile it and copy its shellcode using objcopy or using pwn.asm('''shellcode''') . Or the pussy way out : copy shellcode from the net as there are no restrictions on the size neither the bytes of the shellcode . 
to sum up , the shellcode will try to execute this command : excv('/bin/sh',0,0).
when looking up make sure the architecture is x86/64 because thats the arch of our executable . Try multiple shellcodes until it works as a lot of them dont set up the second parameter properly and its crucial .  



