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
        s.bind(('192.168.0.102',6666))
        s.listen(10)
    except socket.error as msg:
        print msg
        sys.exit(1)
    print 'waiting connection...'

    while 1:
        conn, addr = s.accept()
        print 'Accept new connection from {0}'.format(addr)
        conn.send('Hi, Welcome to the server!')
        conn.send('And your connect is well')

        filepath = raw_input('please input file path: ')
        fileinfo_size = struct.calcsize('128sl')
        fhead = struct.pack('128sl', os.path.basename(filepath), os.stat(filepath).st_size)
        conn.send(fhead)
        print 'client filepath: {0}'.format(filepath)
        fp = open(filepath, 'rb')
        while 1:
            data = fp.read(1024)
            if not data:
                print '{0} file send over...'.format(filepath)
                break
            conn.send(data)
        conn.close()
        break

if __name__ == '__main__':
    socket_service_send()
