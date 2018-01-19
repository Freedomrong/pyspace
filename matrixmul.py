#!/usr/bin/env python3
n = int(input("输入方阵的阶数n："))
print("输入矩阵A的值")
a = []
for i in range(n):
    a.append([int(x) for x in input().split()])#先使用input()获得用户输入的字符串，
                                               #再使用split()分割字符串得到一系列的数字字符串
                                               #然后用int()从每个数字字符串创建对应的整数值
print("输入矩阵B的值")
b = []
for i in range(n):
    b.append([int(x) for x in input().split()])
c = []
for i in range(n):
    c.append([a[i][j] * b[j][i] for j in range(n)])#得到矩阵乘积的每一行数据
print("After matrix multiplication")
print("-" * 7 * n)
for x in c:
    for y in x:
        print(str(y).rjust(5), end='')
    print()
print("-" * 7 * n)
