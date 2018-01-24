#!/usr/bin/env/ python3
#-*- coding = utf-8 -*-

import os
import sys
import struct

def jieyasuo():
    print('de tar.gz is doing')
    os.system('rm -f -r /home/pi/pyspace/new_simple-gcc-stm32-project')
    os.system('tar zxvf new_simple-gcc-stm32-project.tar.gz')
    print('end de tar.gz')


if __name__ == '__main__':
    #先调用接收脚本
    os.system('python /home/pi/pyspace/client_recv.py')
    #再解压缩
    jieyasuo()
