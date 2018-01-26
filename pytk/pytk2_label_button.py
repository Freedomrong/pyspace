#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import tkinter as tk

window  = tk.Tk()
window.title('my window')
window.geometry('200x200')

var = tk.StringVar()    #字符串类型显示变量

#定义label
l = tk.Label(window, textvariable = var, bg = 'green', font = ('Arial', 12), width =15, height = 2)

l.pack()

on_hit = False  #button点击变量

def hit_me():   #button按下时候所执行的函数
    global on_hit   #声明其为全局变量
    if on_hit == False:
        on_hit = True
        var.set('you hit me')   #将显示变量更改为'you hit me'
    else:
        on_hit = False
        var.set('')  #显示变量清空

#定义button
b = tk.Button(window, text = 'hit_me', width = 15, height = 2, command = hit_me)
b.pack()

window.mainloop()
