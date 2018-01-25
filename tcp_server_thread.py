#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import socket
import os
import sys
import struct
import threading
import time
import multiprocessing

rsw = False

def socket_service(sw, s):
    while (sw == True):
        conn, addr = s.accept()
        print('Accept new connection from {0}'.format(addr))
        conn.send(b'Hi, Welcome to the server!\n')
        conn.send(b'And your connect is well\n')
        sw = False

    while (sw == False):
        input_data = input('please input:')
        conn.send(input_data.encode('utf-8'))
        sw = False
    rsw = True

def recv(s):
    print('p2_recv')
    while True:
        data_client = s.recv(2048)
        print(data_client,'\r\n')

if __name__ == '__main__':

    try:
        sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sk.bind(('192.168.0.103',6666))
        sk.listen(10)
    except socket.error as msg:
        print(msg)
        sys.exit(1)
    print('waiting connection...')
    rsw = True

    p1 = multiprocessing.Process(socket_service(rsw, sk), args = (2,))#openocd与FT2232连接
    p2 = multiprocessing.Process(target = recv(sk), args = (3,))#编译代码，打开arm-gdb
    #t1 = threading.Thread(target = socket_service(rsw, sk), name = 't1')
    #t2 = threading.Thread(target = recv, name = 't2')

    p1.start()
    p2.start()
