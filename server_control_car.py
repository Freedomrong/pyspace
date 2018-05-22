256#!/usr/bin/env python3
# -*- coding=utf-8 -*-

'''
这个脚本控制gdb以及获得返回值
'''

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
        s.bind(('192.168.0.110',7777))
        s.listen(10)
    except socket.error as msg:
        print(msg)
        sys.exit(1)
    print('waiting connection...')

    conn, addr = s.accept()
    print('Accept new connection from {0}'.format(addr))
    while True:
        #input_data = input('please input:')
        #conn.send(input_data.encode('utf-8'))
        conn.send(b'w')
        time.sleep(2)
        conn.send(b'a')
        time.sleep(2)
        #conn.send(b'cutoff')

if __name__ == '__main__':
    print('')
    socket_service()
