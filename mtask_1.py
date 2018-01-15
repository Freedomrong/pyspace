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
    os.system('arm-none-eabi-gdb LED_project.elf')
    print("end worker_2")

def worker_3(interval):

    print("worker_3")

    v = virtkey.virtkey()
    #GDB指令，用模拟键盘方法实现输入target remote localhost:3333
    v.press_unicode(ord('t'))
    v.release_keysym(ord('t'))
    v.press_unicode(ord('a'))
    v.release_keysym(ord('a'))
    v.press_unicode(ord('r'))
    v.release_keysym(ord('r'))
    v.press_unicode(ord('g'))
    v.release_keysym(ord('g'))
    v.press_unicode(ord('e'))
    v.release_keysym(ord('e'))
    v.press_unicode(ord('t'))
    v.release_keysym(ord('t'))

    v.press_keysym(65408)#按下SPACE
    v.release_keysym(65408)#释SPACE

    v.press_unicode(ord('r'))
    v.release_keysym(ord('r'))
    v.press_unicode(ord('e'))
    v.release_keysym(ord('e'))
    v.press_unicode(ord('m'))
    v.release_keysym(ord('m'))
    v.press_unicode(ord('o'))
    v.release_keysym(ord('o'))
    v.press_unicode(ord('t'))
    v.release_keysym(ord('t'))
    v.press_unicode(ord('e'))
    v.release_keysym(ord('e'))

    v.press_keysym(65408)#按下SPACE
    v.release_keysym(65408)#释SPACE

    v.press_unicode(ord('l'))
    v.release_keysym(ord('l'))
    v.press_unicode(ord('o'))
    v.release_keysym(ord('o'))
    v.press_unicode(ord('c'))
    v.release_keysym(ord('c'))
    v.press_unicode(ord('a'))
    v.release_keysym(ord('a'))
    v.press_unicode(ord('l'))
    v.release_keysym(ord('l'))
    v.press_unicode(ord('h'))
    v.release_keysym(ord('h'))
    v.press_unicode(ord('o'))
    v.release_keysym(ord('o'))
    v.press_unicode(ord('s'))
    v.release_keysym(ord('s'))
    v.press_unicode(ord('t'))
    v.release_keysym(ord('t'))
    v.press_keysym(58)#按下冒
    v.release_keysym(58)#释放冒号
    v.press_keysym(51)#按下3
    v.release_keysym(51)#释放3
    v.press_keysym(51)
    v.release_keysym(51)
    v.press_keysym(51)
    v.release_keysym(51)
    v.press_keysym(51)
    v.release_keysym(51)

    v.press_keysym(65421)#按下ENTER
    v.release_keysym(65421)#释放ENTER

    #GDB指令，用模拟键盘方法输入monitor reset
    v.press_unicode(ord('m'))
    v.release_keysym(ord('m'))
    v.press_unicode(ord('o'))
    v.release_keysym(ord('o'))
    v.press_unicode(ord('n'))
    v.release_keysym(ord('n'))
    v.press_unicode(ord('i'))
    v.release_keysym(ord('i'))
    v.press_unicode(ord('t'))
    v.release_keysym(ord('t'))
    v.press_unicode(ord('o'))
    v.release_keysym(ord('o'))
    v.press_unicode(ord('r'))
    v.release_keysym(ord('r'))

    v.press_keysym(65408)#按下SPACE
    v.release_keysym(65408)#释SPACE

    v.press_unicode(ord('r'))
    v.release_keysym(ord('r'))
    v.press_unicode(ord('e'))
    v.release_keysym(ord('e'))
    v.press_unicode(ord('s'))
    v.release_keysym(ord('s'))
    v.press_unicode(ord('e'))
    v.release_keysym(ord('e'))
    v.press_unicode(ord('t'))
    v.release_keysym(ord('t'))

    v.press_keysym(65421)#按下ENTER
    v.release_keysym(65421)#释放ENTER

    #GDB指令，用模拟键盘方法输入monitor halt
    v.press_unicode(ord('m'))
    v.release_keysym(ord('m'))
    v.press_unicode(ord('o'))
    v.release_keysym(ord('o'))
    v.press_unicode(ord('n'))
    v.release_keysym(ord('n'))
    v.press_unicode(ord('i'))
    v.release_keysym(ord('i'))
    v.press_unicode(ord('t'))
    v.release_keysym(ord('t'))
    v.press_unicode(ord('o'))
    v.release_keysym(ord('o'))
    v.press_unicode(ord('r'))
    v.release_keysym(ord('r'))

    v.press_keysym(65408)#按下SPACE
    v.release_keysym(65408)#释SPACE

    v.press_unicode(ord('h'))
    v.release_keysym(ord('h'))
    v.press_unicode(ord('a'))
    v.release_keysym(ord('a'))
    v.press_unicode(ord('l'))
    v.release_keysym(ord('l'))
    v.press_unicode(ord('t'))
    v.release_keysym(ord('t'))

    v.press_keysym(65421)#按下ENTER
    v.release_keysym(65421)#释放ENTER

    #GDB指令，用模拟键盘方法输入load,使ARM加载.elf文件
    v.press_unicode(ord('l'))
    v.release_keysym(ord('l'))
    v.press_unicode(ord('o'))
    v.release_keysym(ord('o'))
    v.press_unicode(ord('a'))
    v.release_keysym(ord('a'))
    v.press_unicode(ord('d'))
    v.release_keysym(ord('d'))

    v.press_keysym(65421)#按下ENTER
    v.release_keysym(65421)#释放ENTER

    #以上4条指令为开启GDB调试后必须执行的指令，没有任何选择的余地

    print("end worker_3")


def worker_4(interval):

    c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    c.connect(('192.168.0.101',8080))
    while(1):
        
        control_data = c.recv(4)
        cv = virtkey.virtkey()
        cv.press_unicode(ord(control_data))
        cv.release_keysym(ord(control_data))

        cv.press_keysym(65421)#按下ENTER
        cv.release_keysym(65421)#释放ENTER
    
    

if __name__ == "__main__":
    p1 = multiprocessing.Process(target = worker_1, args = (2,))#openocd与FT2232连接
    p2 = multiprocessing.Process(target = worker_2, args = (3,))#编译代码，打开arm-gdb
    p3 = multiprocessing.Process(target = worker_3, args = (4,))#在gdb中模拟键盘输入初始化指令
    p4 = multiprocessing.Process(target = worker_4, args = (5,))

    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(('192.168.0.101',8080))
    
#    start_variable = int(input())
#    if start_variable == 1000:
#                      p1.start()
#                      time.sleep(5)
#                      p2.start()
#                      time.sleep(8)
#                      p3.start()
                      
    start_data = s.recv(4)
    if start_data == b'1000':
                      print(start_data)
                      p1.start()
                      time.sleep(5)
                      p2.start()
                      time.sleep(8)
                      p3.start()
                      time.sleep(2)
                      p4.start()
                      
                      
    if start_data == b'1001':
                      print(start_data)
                      p1.start()        

    # print("The number of CPU is:" + str(multiprocessing.cpu_count()))
    # for p in multiprocessing.active_children():
    #     print("child   p.name:" + p.name + "\tp.id" + str(p.pid))
    # print("END!!!!!!!!!!!!!!!!!")
