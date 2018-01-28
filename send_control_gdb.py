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
        s.bind(('192.168.0.103',8000))
        s.listen(10)
    except socket.error as msg:
        print(msg)
        sys.exit(1)
    print('waiting connection...')

    conn, addr = s.accept()
    print('Accept new connection from {0}'.format(addr))

    if(conn.recv(256) == b'gdb is ready!'):
        print('gdb is ready!')
        while 1:
            while 1:
                print('**(1)可以输入debug_start********************************************************')
                print('*****(1.1)请不要debug模式下输入c或者continue，请用 monitor resume 代替********')
                print('*****(1.1)配合break使用时可以输入continue********************************')
                print('*****(1.2)还有openocd指令monitor rest以及monitor halt ***************************')
                print('**(2)可以输入mem_poll***********************************************************')
                print('**(3)可以输入dwt****************************************************************')
                print('请输入相应指令')
                input_data = input('please input:')
                if((input_data != 'debug_start') and (input_data != 'mem_poll') and (input_data != 'dwt')):
                    print('请重新输入')
                else:
                    conn.send(input_data.encode('utf-8'))
                    data_client = conn.recv(256)
                    print(data_client)
                    break

            while 1:
                input_data = input('please input:')
                if((input_data == 'debug_end') or (input_data == 'mem_end') or (input_data == 'dwt_end')):
                    conn.send(input_data.encode('utf-8'))
                    data_client = conn.recv(256)
                    print(data_client)
                    break

                if((input_data == 'c')): #or (input_data == 'continue')):
                    print('请重新输入')
                else:
                    conn.send(input_data.encode('utf-8'))
                    data_client = conn.recv(4096)   #这里有一个很大的问题，比如 monitor mww 是对地址进行写入，是没有返回值的，在这里接受时会卡死
                    print(data_client)

                # input_data = input('please input_debug_command:')
                # conn.send(input_data.encode('utf-8'))
                # data_client = conn.recv(4096)
                # print(data_client)


if __name__ == '__main__':
    print('这个脚本是gdb调试所使用，监听的端口号是8000')
    socket_service()
