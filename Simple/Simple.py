# Simple and Basic Python Packet sniffer by Nir Mizrahi

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)

while True:
  print s.recvfrom(65565)
  
  
# I have analysed this entire code and wrote from the start to the end
