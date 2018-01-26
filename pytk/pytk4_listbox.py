#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import tkinter as tk

window  = tk.Tk()
window.title('my window')
window.geometry('200x200')

var1 = tk.StringVar()

#定义Label
l = tk.Label(window, bg = 'yellow', width = 4, textvariable = var1)
l.pack()

#定义button的功能函数
def print_selection():
    value =lb.get(lb.curselection())
    var1.set(value)

#定义button1
b1 = tk.Button(window, text = 'print selection', width = 15, height = 2, command = print_selection)
b1.pack()

#定义listbox
var2 = tk.StringVar()
var2.set((1,2,3,4))
lb = tk.Listbox(window, listvariable = var2)
list_items = [1,2,3,4]

for item in list_items: #将list中的元素输入到listbox上
    lb.insert('end', item)
lb.insert(1, 'first')   #补充输入first
lb.insert(2, 'second')  #补充输入second
lb.delete(2)  #删除2的second
lb.pack()


window.mainloop()
