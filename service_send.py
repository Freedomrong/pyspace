#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import socket
import os
import sys
import struct
import threading
import time

def socket_service_send():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(('192.168.0.105',6666))
        s.listen(10)
    except socket.error as msg:
        print(msg)
        sys.exit(1)
    print('waiting connection...')

    while 1:
        conn, addr = s.accept()
        t = threading.Thread(target=deal_data, args=(conn, addr))
        t.start()

def deal_data(conn, addr):
    print('Accept new connection from {0}'.format(addr))
    #conn.settimeout(500)
    conn.send(b'Hi, Welcome to the server!')   #这里的格式与python2.x中是不一样的，形参是字节类型需要注意

if __name__ == '__main__':
    socket_service_send()
