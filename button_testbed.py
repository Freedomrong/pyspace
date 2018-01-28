#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import tkinter as tk
import os

window  = tk.Tk()
window.title('my window')
window.geometry('200x200')

var = tk.StringVar()    #字符串类型显示变量

#定义label
l = tk.Label(window, textvariable = var, bg = 'yellow', font = ('Arial', 12), width =15, height = 2)
l.pack()

def hit_me1():   #button按下时候所执行的函数
    var.set('运行完成yasuo.py')   #将显示变量更改为'you hit me'
    os.system('python /home/user/pyspace/yasuo.py')

def hit_me2():   #button按下时候所执行的函数
    var.set('运行完成send_control.py')   #将显示变量更改为'you hit me'
    os.system('python /home/user/pyspace/send_control.py')

#定义button1
b1 = tk.Button(window, text = 'yasuo.py', width = 15, height = 2, command = hit_me1)
b1.pack()

#定义button2
b2 = tk.Button(window, text = 'send_control.py', width = 15, height = 2, command = hit_me2)
b2.pack()


window.mainloop()
