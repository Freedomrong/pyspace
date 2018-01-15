#!/usr/bin/env python3

import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect(('192.168.0.102',8080))

s.send(b'123')

while(1):
    data = s.recv(8)
    #if data == b'l':
    print(data)
    

