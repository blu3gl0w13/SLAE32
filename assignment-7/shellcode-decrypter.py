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
from Crypto.Cipher import ARC4
import sys
import argparse


#---------------------------------------
#
# Define our Encryption Functions
#
#--------------------------------------

def aesDecrypter(key, initVector, shellcode):
  decrypterObject = AES.new(key, AES.MODE_CBC, initVector)
  messageToDecrypt = shellcode
  clearText = decrypterObject.decrypt(messageToDecrypt)
  print "\n\n[+] RAW AES Decrypted Shellcode: \n%s" % clearText.encode('hex')
  decryptedShellcode = ''
  decryptedShellcode2 = ''

  for i in bytearray(clearText):
    decryptedShellcode += '\\x%02x' % i
    decryptedShellcode2 += '0x%02x,' % i
  print "\nShellcode Length: %d" % len(clearText)
  print "\nKey: %s" % key
  print "\nIV: %s" % initVector
  print "\n[+] AES Decrypted Shellcode: \n" + decryptedShellcode
  print "\n[+] AES Decrypted Shellcode2: \n" + decryptedShellcode2[:(len(decryptedShellcode2) - 1):]
  sys.exit(0)

def rc4Decrypter(key, shellcode):
  decrypterObject = ARC4.new(key)
  messageToDecrypt = shellcode
  clearText = encrypterObject.decrypt(messageToDecrypt)
  print "\n\n[+] RAW RC4 Encrypted Shellcode: \n%s" % clearText.encode('hex')
  decryptedShellcode = ''
  decryptedShellcode2 = ''

  for i in bytearray(cipherText):
    decryptedShellcode += '\\x%02x' % i
    decryptedShellcode2 += '0x%02x,' % i
  print "\nShellcode Length: %d" % len(clearText)
  print "\nKey: %s" % key
  print "\nRC4 Encrypted Shellcode: \n" + decryptedShellcode
  print "\nRC4 Encrypted Shellcode2: \n" + decryptedShellcode2[:(len(decryptedShellcode2) - 1):]
  sys.exit(0)

def main():
  # Setup the argument parser

  parser = argparse.ArgumentParser()
  parser.add_argument("-s", "--shellcode", help="Shellcode to decrypt", dest='shellcode', required=True)
  parser.add_argument('-k', '--key', help='Key to use for decryption', dest='key', required=True)
  parser.add_argument('-c', '--cipher', help='Cipher to use for decryption', choices=['rc4','aes','RC4','AES'], dest='cipher', required=True)
  parser.add_argument('-iv', '--init-vector', help='AES IV to use for decryption (AES only)', dest='initVector')
  options = parser.parse_args()

  # Prepare some objects

  key = options.key
  initVector = options.initVector
  shellcode = options.shellcode

  if options.cipher == 'aes' or options.cipher == 'AES':
    # pad shellcode with nops until it is in chunks of 16
    #while (len(bytearray(shellcode)) % 16 !=0):
    #  shellcode += '\\x90'

    if initVector == 'None':
      print "\n[-] Error! IV option not set. Exiting..."
      parser.print_help()
      sys.exit(1)
    if len(initVector) != 16:
      print "\n[-] Error! IV is not 16 bits long. Exiting..."
      sys.exit(1)
    if (len(key) != 16) and (len(key) != 24) and (len(key) != 32):
      print "\n[-] Error! AES Keys must be 16, or 24, or 32 bits. Exiting..."
      sys.exit(1)

    aesDecrypter(key, initVector, shellcode)


  elif options.cipher == 'rc4' or options.cipher == 'RC4':
    rc4Decrypter(key,shellcode)


  else:
    print "[-] Error! Not sure how you got here. Exiting..."
    sys.exit(1)


if __name__ != main:
  main()
