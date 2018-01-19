#!/usr/bin/env python3
# def change():
#     a = 90#函数内部的局部变量a赋值为90，只在change函数内部（当这个函数被调用时）有效
#     print(a)
#
# a=9#函数外部的全局变量
# print("Before the function call ", a)
# print("inside change function", end=' ')
# change()
# print("After the function call ", a)
def change():
    global a#a不再只是函数内部的局部变量了，而是全局变量
    a = 90
    print(a)
a = 9
print("Before the function call ", a)
print("inside change function", end=' ')
change()#调用change函数后，全局变量a的值变为90
print("After the function call ", a)
