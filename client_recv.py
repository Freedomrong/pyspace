#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import socket
import os
import sys
import struct

def socket_client_recv():
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect(('192.168.0.105',6666))
        except socket.error as msg:
            print(msg)
            sys.exit(1)
        print("connecting service...")
        
        data_from_service = s.recv(64)
        print(data_from_service)
       
if __name__ == '__main__':
        socket_client_recv()

