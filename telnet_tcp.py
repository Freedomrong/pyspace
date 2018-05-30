#!/usr/bin/env python3
'''
telnetlib返回数据的功能较为薄弱，单独开一个线程运行以下脚本，还不如在gdb中使用monitor透传指令
'''


import os
import sys
import multiprocessing #多进程
import time
import virtkey #虚拟键盘
import socket #TCP
import telnetlib #telent


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('192.168.0.101',8080))

ocd = telnetlib.Telnet('127.0.0.1',4444)

while(1):
    s1 = s.recv(64)
    control_data = s1
    ocd.write(control_data)
    send_data = ocd.read_very_eager()
    s.send(send_data)
