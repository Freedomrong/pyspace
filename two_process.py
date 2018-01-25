#!/usr/bin/env python3
import os
import sys
import multiprocessing
import time
import virtkey
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sw = 1

def worker_1(interval):#openocd与FT2232连接
    while 1:
        input_data = input('please input:')
        print("worker_1")
        time.sleep(1)


def worker_2(interval):#编译代码，以及打开arm gdb
    while 1:
        print("worker_2")
        time.sleep(1)


if __name__ == "__main__":
    p1 = multiprocessing.Process(target = worker_1, args = (2,))#openocd与FT2232连接
    p2 = multiprocessing.Process(target = worker_2, args = (3,))#编译代码，打开arm-gdb

    p1.start()
    p2.start()
