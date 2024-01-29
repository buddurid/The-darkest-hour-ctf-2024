this challenge was the first pwn challenge and it was straight-forward from the name of it 'bufferoverflow'
for those who are not familiar with the term there are plenty of ressources out there in the internet but here is a quick recap and example. if you are granted the right to write in a variable more than it's size then you'll end up writing in memory that is used for other variables youre not supposed to be writing into . 
consider this simple c code below . 
```
#include <stdlib.h>
#include <stdlib.h>
int main(){

        char b[8]="name";
        char a[4];
        printf("value of b before reading input :%s\n",b);
        read(0,a,16);
        printf("value of b after reading from input :%s",b);
        return 0 ;
}
```

although the string a was declared of size 4, we can right up to 16 characters in a . So what happens is after the writing the first 4 chars , we start overwriting other memory and in this case the variable b . 

![output](/images/c-result.png)


in our case , the scanf function didnt specifie any limits like **scanf(%16s,input)** so it will end up reading chars until it reaches \n or space or tabulation or whatever . but what do we overwrite and what do we overwrite with ? 
1. Where??
    * usually , we tend to overwrite the return address which is situated right after rbp . you can look up how far is rbp from our buffer in a debugger like IDA or in gdb . well go with IDA in this one 

    ![ida2](/images/ida2.png)


    as we see our buf is 0x100 away from rbp  && size allocated for rbp is always 8 bytes in x86/64 architecture >>> our buffer is away 0x100+8 bytes from the ret adsress 


2. What to write in ret adress ??
    * at some point , the program will execute whatever is pointed by the value stored in the return address that we can overwrite . the program's code must be stored in a place in memory . so we overwrite this with a pointer to memory that has code in it and it will execute it . well m0ngi was generous enough to give a function **deprecated()** that opens a shell so we'll need to get it's location in memory . we can look that up with gdb . 

![func](/images/funcs.png)


onething to mention is that data in memory is written in little-endian format , so lets suppose you want to write 0x0000000012345678 in memory . what you need to write isn't b'\x00\x00\x00\x00\x12\x34\x56\x78' but b'\x78\x56\x34\x12\x00\x00\x00\x00'. luckily **pwntools** ratta7na and we can use p64(0x0000000012345678) 

look up the full script(solver.py) in the challenge files

after running the script locally you could look up the flag location and then read it 
