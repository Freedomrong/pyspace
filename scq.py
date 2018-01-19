#!/usr/bin/env python3
"""
使用yield语句创建一个简单的生成器
"""
def my_generator():
    print("Inside my generator")
    yield 'a'
    yield 'b'
    yield 'c'

"""
使用counter_generator生成器函数完成与dqq.py中Counter类相同的功能
"""
def counter_generator(low,high):
    while low <= high:
        yield low
        low += 1

my_generator()
print('\n')

#在for循环中使用my_generator():生成器
for char in my_generator():
    print(char)
print('\n')

#在for循环中使用counter_generator()生成器
for i in counter_generator(5,10):
    print(i,end = ' ')
print('\n')
