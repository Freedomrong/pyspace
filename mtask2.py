#!/usr/bin/env python3
'''
该脚本于工程目录下的t.py脚本配合使用，开启gdb之后的所以操作均在工程目录下的脚本内完成
'''
import os
import sys
import multiprocessing #多进程
import time
import virtkey #虚拟键盘
import socket #TCP
import telnetlib #telent

w1 = 0 #标记变量,值变为1代表进程内的函数运行到了最后一行
w2 = 0
w3 = 0

def worker_1(interval):#openocd与FT2232连接

    print("worker_1")
    print('\n')
    os.system('sudo openocd -f interface/ftdi/open_jtag.cfg -f  target/stm32f1x.cfg')
    print("end worker_1")

def worker_2(interval):#编译代码，以及打开arm gdb

    print("worker_2")
    print('\n')
    os.system('pwd')
    os.chdir('../')
    os.chdir('workspace/simple-gcc-stm32-project/')
    os.system('make clean')
    os.system('make')
    os.system('arm-none-eabi-gdb -q -x t.py LED_project.elf')
    print("end worker_2")
    time.sleep(3)

    #当进程运行到这里时，说明gdb已经已经正常退出了，而openocd占用的进程目前只知道通过CTRL＋C快捷键强制关闭，故以下使用模拟键盘的方法在此关闭openocd
    v = virtkey.virtkey()

    v.press_keysym(65507)#按下左CTRL
    v.press_unicode(ord('c'))#按下C
    v.release_keysym(ord('c'))#释放C
    v.release_keysym(65507)#释放左CTRL

def worker_3(interval):#这里在进程3中临时写这一段程序只用来加载elf文件

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
    print("worker_3")

    tn=telnetlib.Telnet()
    tn.write(b'reset\n')

    print("end worker_3")
    
    

if __name__ == "__main__":
    p1 = multiprocessing.Process(target = worker_1, args = (2,))#openocd与FT2232连接
    p2 = multiprocessing.Process(target = worker_2, args = (3,))#编译代码，打开arm-gdb
    p3 = multiprocessing.Process(target = worker_3, args = (4,))#在gdb中模拟键盘输入初始化指令
    #p4 = multiprocessing.Process(target = worker_4, args = (5,))

    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(('192.168.0.101',8080))
    
#    start_variable = int(input())
#    if start_variable == 1000:
#                      p1.start()
#                      time.sleep(5)
#                      p2.start()
#                      time.sleep(8)
#                      p3.start()

    #应该让以下代码循环执行起来
    while(1):#但是ctrl+c的方法关闭进程2的同时也会直接杀掉全部进程，所以采用大循环的方法并不行
        start_data = s.recv(4)
        if start_data == b'1000':#目前1000指令，完成openocd于目标板连接，完成编译代码、使用gdb开启工程目录下脚本以及加载elf文件
                          print(start_data)
                          p1.start()
                          time.sleep(5)
                          s.send(b'Openocd has connected FT2232')
                          p2.start()
                          time.sleep(12)
                          s.send(b'gdb ok!!!')#目前问题，这条反馈信息发的太早了，进程2还没有执行完呢，可以考虑将这条反馈指令，加到进程内部
                          #time.sleep(8)
                          #p3.start()
                          #time.sleep(2)
                          #p4.start()
                          
                          
        if start_data == b'1001':#目前1001指令只完成openocd于目标板连接
                          print(start_data)
                          p1.start()

        if start_data == b'1002':#1002对比1001只是少了编译环节，用以节约时间
                          print(start_data)
                          p1.start()
                          time.sleep(5)
                          s.send(b'Openocd has connected FT2232')
                          p3.start()
                          time.sleep(8)
                          s.send(b'gdb ok!!!')

        # print("The number of CPU is:" + str(multiprocessing.cpu_count()))
        # for p in multiprocessing.active_children():
        #     print("child   p.name:" + p.name + "\tp.id" + str(p.pid))
        # print("END!!!!!!!!!!!!!!!!!")
