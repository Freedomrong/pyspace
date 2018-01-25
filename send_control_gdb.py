#!/usr/bin/env python3
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
        s.bind(('192.168.0.103',8000))
        s.listen(10)
    except socket.error as msg:
        print(msg)
        sys.exit(1)
    print('waiting connection...')

    conn, addr = s.accept()
    print('Accept new connection from {0}'.format(addr))

    if(conn.recv(64) == b'gdb is ready!'):
        print('gdb is ready!')
        print('**可以输入debug_start**********************************')
        print('**可以输入mem_poll*************************************')
        print('**可以输入dwt******************************************')
        while 1:
            input_data = input('please input:')
            conn.send(input_data.encode('utf-8'))
            data_client = conn.recv(4096)   #这里有一个很大的问题，比如 monitor mww 是对地址进行写入，是没有返回值的，在这里接受时会卡死
            print(data_client)

if __name__ == '__main__':
    print('这个脚本是gdb调试所使用，监听的端口号是8000')
    socket_service()
