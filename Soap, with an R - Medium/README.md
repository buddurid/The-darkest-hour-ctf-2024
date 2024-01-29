well this one is quite special . and the hardest for sure . 

challenges that provide you with assembly code are no good . 
what makes the challenge quite hard and unique is that there are no win function , no libc , nothing except for a buffer overflow . 
to grasp this challenge you need to understand well the calling convention of both x86/64 and x86 system . 
to sum up , in x86/64 systems arguments for syscalls and functions are stored in rdi,rsi,rdx ... registers . unlike x86 systems that just push the parametrs on the stack . Guess what !!! this challenge made a mix-up . then what ? 
looking at this challenge the only thing we can manipulate is syscalls .
another thing i should mention is that if when we call syscall , a certain kernel function gets executed based on the value of rax and with the parameters that are stored in rdi ,rsi,rdx ... . for example if rax=1 and we call syscall the **write syscall** will get called . you can look up syscall numbers for x86/64 systems [link](https://blog.rchapman.org/posts/Linux_System_Call_Table_for_x86_64/) 

but how can we modifie rax to our own accord ? the thing is all syscalls put the return value in rax register . and for example if we execute the read call and it reads 15 bytes from input , rax will contain 15 after execution , and if make it that we dont change the value of rax and we execute a syscall (thanks to our buffer overflow) we will execute the syscall number 15 that is sigreturn which is litterally Thanos . this sigreturn syscall resets the values of all register(including RIP ) into values from stack . so once we execute this sigreturn , we make rip point to a syscall , rdi = pointer to 'bin/sh' string , rsi=0,and rax into **59** so that syscall num 59 which is execve gets executed . 
so before all that we have to write '/bin/sh' into writable memory that we know its location every runtime (because stack that we write into by default changes its location each runtime) so the first buffer overlow will return into read with a modified stack such as rsi will contain a popped value that we gave to it (we can get a writable adress with gdb : you need to start a process then type vmmap and choose a region that doesnt end with 7ff.... and has r w in their permissions)

you could ask if we had control into rax why not call execve from the beginning the reason is if we dont have anyway to keep rax the same and modifing rdi and rsi in the same time ; for exammple if we jump to the 3rd line of read , yes we could modifie rdi but rax will be set to 0 :(


hope the writeup was helpful in any way , dm me for help if something is foggy or not understandable , fama 7ajet zrebt feha couldnt do better . thanks for reading :) 