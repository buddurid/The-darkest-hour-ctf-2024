this challenge was the first pwn challenge and it was straight-forward from the name of it 'bufferoverflow'
for those who are not familiar with the term there are plenty of ressources out there in the internet but here is a quick recap and example. if you are granted the right to write in a variable more than it's size then you'll end up writing in memory that is used for other variables youre not supposed to be writing into . 
consider this simple c code below . 
'''
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
'''