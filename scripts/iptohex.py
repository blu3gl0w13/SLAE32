#!/usr/bin/env python

####################################
#
# IPv4 to Hex converter
# by Michael Born (@blu3gl0w13)
# August 30, 2016
#
####################################

import socket
import sys
import struct

if len(sys.argv) < 3:
    print "Usage: %s <ipv4 address> <port>" % sys.argv[0]
    sys.exit(1) 


ip = sys.argv[1]
port = int(sys.argv[2])
output = socket.inet_aton(ip).encode('hex')



print "\n[+] Hex version of IP is: 0x%s" % output
print "[+] Little Endian version of IP is: 0x%s\n" % hex(struct.unpack('<L', struct.pack('>L', int(output,16))) [0])[2:]
print "[+] Hex version of PORT is: 0x%02x" % port
print "[+] Little Endian version of PORT is: 0x%s\n" % hex(struct.unpack('<H', struct.pack('>H', port)) [0])[2:]
print "[+] PORT IP Shellcode is: \\x%s\\x%s\\x%s\\x%s\\x%s\\x%s" % (hex(port)[2:4], hex(port)[4:6], output[0:2], output[2:4], output[4:6], output[6:8]) 
print "[+] IP PORT shellcode is: \\x%s\\x%s\\x%s\\x%s\\x%s\\x%s\n\n" % (output[0:2], output[2:4], output[4:6], output[6:8], hex(port)[2:4], hex(port)[4:6])
