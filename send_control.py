#!/usr/bin/env python3
# -*- coding=utf-8 -*-

'''
这个控制mtask2开启opeocd以及gdb
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
        s.bind(('192.168.0.103',6666))
        s.listen(10)
    except socket.error as msg:
        print(msg)
        sys.exit(1)
    print('waiting connection...')

    conn, addr = s.accept()
    print('Accept new connection from {0}'.format(addr))

    while 1:
        input_data = input('please input:')
        conn.send(input_data.encode('utf-8'))
        data_client = conn.recv(4096)
        print(data_client)
        break
    #这里程序执行完毕之后要关闭连接关闭脚本,但是这里掐断连接mtask2那里写的自动关闭就失效了，因为mtask2连接的6666端口被关闭了
    #conn.close()
    #s.close()

if __name__ == '__main__':
    print('**这个脚本是控制开启openocd以及gdb所使用,监听的端口号是6666***')
    print('**出现please input*************************************')
    print('*输入1000，openocd开启,完成编译代码,开启gdb且gdb会加载脚本**')
    print('*输入1001，openocd开启***********************************')
    print('*输入1002，openocd开启,开启gdb且gdb会加载脚本**************')
    socket_service()
