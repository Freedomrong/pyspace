#!/usr/bin/env python
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
        s.bind(('192.168.0.103',6666))
        s.listen(10)
    except socket.error as msg:
        print msg
        sys.exit(1)
    print 'waiting connection...'

    while 1:
        conn, addr = s.accept()
        t = threading.Thread(target=deal_data, args=(conn, addr))
        t.start()

        #向客户端发送文件
        filepath = raw_input('please input file path: ')
        if os.path.isfile(filepath):
            # 定义定义文件信息。128s表示文件名为128bytes长，l表示一个int或log文件类型，在此为文件大小
            fileinfo_size = struct.calcsize('128sl')
            # 定义文件头信息，包含文件名和文件大小
            fhead = struct.pack('128sl', os.path.basename(filepath), os.stat(filepath).st_size)
            s.send(fhead)
            print 'client filepath: {0}'.format(filepath)

            fp = open(filepath, 'rb')
            while 1:
                data = fp.read(1024)
                if not data:
                    print '{0} file send over...'.format(filepath)
                    break
                s.send(data)

def deal_data(conn, addr):
    print 'Accept new connection from {0}'.format(addr)
    #conn.settimeout(500)
    conn.send('Hi, Welcome to the server!')   #这里的格式与python2.x中是不一样的，形参是字节类型需要注意

if __name__ == '__main__':
    socket_service_send()
