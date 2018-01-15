#!/usr/bin/env python3

import os
import sys
import multiprocessing #多进程
import time
import virtkey #虚拟键盘
import socket #TCP
import telnetlib #telent

def worker_1(interval):#openocd与FT2232连接

#    v1 = virtkey.virtkey()
#
#    v1.press_keysym(65507)#按下左CTRL
#    v1.press_keysym(65505)#按下左SHIFT
#    v1.press_unicode(ord('T'))#按下T
#    v1.release_keysym(ord('T'))#释放T
#    v1.release_keysym(65505)#释放左SHIFT
#    v1.release_keysym(65507)#释放左CTRL

    print("worker_1")
    print('\n')
    os.system('sudo openocd -f interface/ftdi/SWD_FT.cfg -f  target/stm32f1x.cfg')
    print("end worker_1")

def worker_2(interval):#编译代码

    print("worker_2")
    print('\n')
    os.system('pwd')
    os.chdir('../')
    os.chdir('workspace/simple-gcc-stm32-project/')
    os.system('make clean')
    os.system('make')
    print("end worker_2")

def worker_3(interval):#开启GDB加载elf文件

    print("worker_3")
    
    print('\n')
    os.system('pwd')
    os.chdir('../')
    os.chdir('workspace/simple-gcc-stm32-project/')
    os.system('arm-none-eabi-gdb -q -x t.py LED_project.elf')

    print("end worker_3")

    #当进程运行到这里时，说明gdb已经已经正常退出了
    v = virtkey.virtkey()

    v.press_keysym(65507)#按下左CTRL
    v.press_unicode(ord('c'))#按下C
    v.release_keysym(ord('c'))#释放C
    v.release_keysym(65507)#释放左CTRL

def worker_4(interval):
    print("worker_4")
    os.system('setserial /dev/ttyUSB1 spd_cust divisor 5')
    os.system('stty -F /dev/ttyUSB1 38400')
    os.system('itmdump -f /dev/ttyUSB1 -d1')
    #os.system('sudo cutecom')
    
    print("end worker_4")
    
    

if __name__ == "__main__":
    p1 = multiprocessing.Process(target = worker_1, args = (2,))#openocd与FT2232连接
    p2 = multiprocessing.Process(target = worker_2, args = (3,))#编译代码，打开arm-gdb
    p3 = multiprocessing.Process(target = worker_3, args = (4,))#在gdb中模拟键盘输入初始化指令
    p4 = multiprocessing.Process(target = worker_4, args = (5,))

    time.sleep(1)
    p4.start()
    time.sleep(1)
    p1.start()
    p3.start()

        # print("The number of CPU is:" + str(multiprocessing.cpu_count()))
        # for p in multiprocessing.active_children():
        #     print("child   p.name:" + p.name + "\tp.id" + str(p.pid))
        # print("END!!!!!!!!!!!!!!!!!")
