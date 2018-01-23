#!/usr/bin/env python
# -*- coding=utf-8 -*-

import socket
import os
import sys
import struct

def socket_client_recv():
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect(('192.168.0.103',6666))
        except socket.error as msg:
            print msg 
            sys.exit(1)
        print "connecting service..."
        
        data_from_service = s.recv(64)
        print data_from_service
        
        data_from_service = s.recv(64)
        print data_from_service
   
        while 1:
                fileinfo_size = struct.calcsize('128sl')
                buf = s.recv(fileinfo_size)
                if buf:
                        filename, filesize = struct.unpack('128sl', buf)
                        fn = filename.strip('\00')
                        new_filename = os.path.join('./', 'new_' + fn)
                        print 'file new name is {0}, filesize if {1}'.format(new_filename, filesize)

                        recvd_size = 0  # 定义已接收 文件的大小
                        fp = open(new_filename, 'wb')
                        print 'start receiving...'

                        while not recvd_size == filesize:
                                if filesize - recvd_size > 1024:
                                        data = s.recv(1024)
                                        recvd_size += len(data)
                                else:
                                        data = s.recv(filesize - recvd_size)
                                        recvd_size = filesize
                                fp.write(data)
                        fp.close()
                        print 'end receive...'
                s.close()
                break
       
if __name__ == '__main__':
        socket_client_recv()

