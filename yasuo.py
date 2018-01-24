#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import socket
import os
import sys
import struct
import threading
import time

def yasuo():
    print('tar.gz is doing...')
    os.system('rm -i /home/user/pyspace/simple-gcc-stm32-project.tar.gz')
    os.system('tar zcvf /home/user/pyspace/simple-gcc-stm32-project.tar.gz simple-gcc-stm32-project/')
    print('end tar.gz...')


if __name__ == '__main__':
    #先压缩
    yasuo()
    #再调用发送脚本
    os.system('python /home/user/pyspace/service_send.py')
