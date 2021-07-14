# Simple Packet sniffer by Nir Mizrahi
# Works only with Linux

import socket

# create an INET, raw socket
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)

# receive a packet
while True:
  print s.recvfrom(65565)
  
  
# the output will be a mess but this is because this code is unpacked and its just a dump of the network packets in hex.
# in the next code (sniffer.py) we will unpack the packets and it will look visualy better and more readable:)
