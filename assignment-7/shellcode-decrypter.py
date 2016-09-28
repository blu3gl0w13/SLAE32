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
import argparse
import os
import hashlib


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
  print "\n\n[+] RAW AES Decrypted Shellcode (non hex encoded): \n\"%s\"\n\n" % clearText
  sys.exit(0)

def main():
  # Setup the argument parser

  parser = argparse.ArgumentParser()
  parser.add_argument("-s", "--shellcode", help="Shellcode to decrypt", dest='shellcode', required=True)
  parser.add_argument('-k', '--key', help='Key to use for decryption', dest='key', required=True)
  options = parser.parse_args()

  # Prepare some objects
  shellcode = (options.shellcode).decode('hex')[32::]
  IV = (options.shellcode).decode('hex')[:16]
  salt = (options.shellcode).decode('hex')[16:32]
  key = options.key

  aesDecrypter(key, IV, shellcode, salt)

if __name__ != main:
  main()
