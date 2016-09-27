#!/usr/bin/env python

####################################################
#
# shellcode-crypter.py
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

# Setup the argument parser

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--shellcode", help="Shellcode to encrypt", dest='shellcode', action=store)

group1 = parser.add_argument_group('aes', 'AES cipher options')
group1.add_argument('-k', '--key', help='AES key to use for encryption', dest='key', action=store)
group1.add_argument('-iv', '--init-vector', help='AES IV to use for encryption', dest='initVector', action=store)
group2 = parser.add_argument_group('rc4', 'RC4 cipher options')
group2.add-argument('-k', '--key', help='RC4 key to use for encryption', dest='key', action=store)
options = parser.parse_args()

# Prepare some objects

key = options.key
initVector = options.initVector
shellcode = options.shellcode

#---------------------------------------
#
# Define our Encryption Functions
#
#--------------------------------------

def aesCryptor(key, initVector, shellcode):
  encrypterObject = AES.new(key, AES.MODE_CBC, initVector)
  messageToEncrypt = shellcode
  cipherText = encrypterObject.encrypt(messageToEncrypt)
  print "AES Encrypted Shellcode: %s" % ciphertext.encode('hex')
  shellCodeLength = len(ciphertext)
  encryptedShellcode = ''
  encryptedShellcode2 = ''

  for i in bytearray(ciphertext):
    encryptedShellcode += '\\x%02x' % i
    encryptedShellcode2 += '0x%02x,' % i

  print "Len: %d" % len(ciphertext)
  print "\nAES Encrypted Shellcode: " + encryptedShellcode
  print "\nAES Encrypted Shellcode2: " + encryptedShellcode2


def rc4Cryptor(key, shellcode):
  encrypterObject = ARC4.new(key)
  messageToEncrypt = shellcode
  cipherText = encrypterObject.encrypt(messageToEncrypt)
  print "Encrypted Shellcode: %s" % ciphertext.encode('hex')
  shellCodeLength = len(ciphertext)
  encryptedShellcode = ''
  encryptedShellcode2 = ''

  for i in bytearray(ciphertext):
    encryptedShellcode += '\\x%02x' % i
    encryptedShellcode2 += '0x%02x,' % i

  print "Len: %d" % len(ciphertext)
  print "\nRC4 Encrypted Shellcode: " + encryptedShellcode
  print "\nRC4 Encrypted Shellcode2: " + encryptedShellcode2


