#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

#label值变量
var = tk.StringVar()

#定义label
l = tk.Label(window, bg = 'yellow', width = 20, text = 'empty')
l.pack()

#定义label中的text赋值函数,是Radiobutton的command参数，就是会在Radiobutton中被调用
def print_selection():
    l.config(text = 'you have selected ' + var.get())

r1 = tk.Radiobutton(window, text = 'option A', variable = var, value = 'A', command = print_selection)
r1.pack()

r2 = tk.Radiobutton(window, text = 'option B', variable = var, value = 'B', command = print_selection)
r2.pack()

r3 = tk.Radiobutton(window, text = 'option c', variable = var, value = 'c', command = print_selection)
r3.pack()


window.mainloop()
