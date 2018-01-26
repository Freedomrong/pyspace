#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import tkinter as tk

window  = tk.Tk()
window.title('my window')
window.geometry('200x200')

#定义Entry文本框
e = tk.Entry(window, show = None)  #类似密码显示的话，show = ‘×’
e.pack()

def insert_point():
    var = e.get()
    t.insert('insert', var)

def insert_end():
    var = e.get()
    #t.insert('end', var)
    t.insert(0.1, var)  #有内容时第0行的第1位输入var的内容


#定义button1
b1 = tk.Button(window, text = 'insert_point', width = 15, height = 2, command = insert_point)
b1.pack()

#定义button2
b2 = tk.Button(window, text = 'insert_end', width = 15, height = 2, command = insert_end)
b2.pack()

#定义text文本框
t = tk.Text(window, height = 2)
t.pack()

window.mainloop()
