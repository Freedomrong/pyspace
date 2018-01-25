#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import socket
import os
import sys
import struct
import threading
import time

def socket_service():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(('192.168.0.103',6666))
        s.listen(10)
    except socket.error as msg:
        print(msg)
        sys.exit(1)
    print('waiting connection...')

    sw = True

    while (sw == True):
        conn, addr = s.accept()
        print('Accept new connection from {0}'.format(addr))
        conn.send(b'Hi, Welcome to the server!\n')
        conn.send(b'And your connect is well\n')
        sw = False

    while (sw == False):
        input_data = input('please input:')
        conn.send(input_data.encode('utf-8'))
        data_client = conn.recv(4096)
        print(data_client)

if __name__ == '__main__':
    socket_service()
