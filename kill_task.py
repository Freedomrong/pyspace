#!/usr/bin/env python3
import os
import sys
import multiprocessing
import time
import virtkey
import socket

w1 = 0 #标记变量,值变为1代表进程内的函数运行到了最后一行
w2 = 0
w3 = 0

def worker_1(interval):#

    print("worker_1")

    print("end worker_1")

def worker_2(interval):#

    print("worker_2")

    print("end worker_2")
    

def worker_3(interval):

    print("worker_3")

    print("end worker_3")


def worker_4(interval):

    print("worker_4")

    print("end worker_4")
    

if __name__ == "__main__":
    p1 = multiprocessing.Process(target = worker_1, args = (2,))#openocd与FT2232连接
    p2 = multiprocessing.Process(target = worker_2, args = (3,))#编译代码，打开arm-gdb
    p3 = multiprocessing.Process(target = worker_3, args = (4,))#在gdb中模拟键盘输入初始化指令
    p4 = multiprocessing.Process(target = worker_4, args = (5,))

    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(('192.168.0.101',8080))
    

    p1.start()
    p2.start()
    p3.start()
    p4.start()

    print(p1.pid)
    print(p2.pid)
    print(p3.pid)
    print(p4.pid)
