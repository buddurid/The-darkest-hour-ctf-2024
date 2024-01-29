# gcc -masm=intel -z noexecstack -nostdlib -no-pie -o main main.s
.intel_syntax noprefix
.global _start

.data

welcome: 
  .ascii "Hello!\nWelcome to the Darkest Hour of the night.\nOne skill you may need here is an understanding of x64 assembly.\nAnd a SOaP.\n\0"
  .set welcome_size, . - welcome


.text

_start:
  lea rdi, [rip + welcome]
  mov esi, OFFSET welcome_size
  call printf

  call hour

  push 0
  pop rdi
  call exit

printf:
  push rbp
  mov rbp, rsp

  # size
  push rsi
  pop rdx

  # buf
  push rdi
  pop rsi

  # fd=1 (stdout)
  push 1
  pop rdi
  
  # syscall 1: write
  push 1
  pop rax

  syscall

  leave
  ret

exit:
  push 60
  pop rax
  syscall

read:
  pop rbx # saved RIP

  pop rdx
  pop rsi
  push 0
  pop rdi

  # Syscall 0: read
  push 0
  pop rax

  syscall

  push rbx # saved RIP
  ret

hour:
  sub rsp, 0x100

  push rsp
  push 0x250
  call read
  
  add rsp, 0x100
  ret
