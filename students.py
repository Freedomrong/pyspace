#!/usr/bin/env python3
n = int(input("输入学生数量"))
data = {}#用来存储数据的字典变量
Subjects = ('物理','数学','历史')#所有科目
#第一个循环用以获取学生的各科分数
for i in range(0,n):
    name = input('输入学生姓名 {}:'.format(i+1))#获得学生名称
    marks = []
    for x in Subjects:
        marks.append(int(input('输入分数 {}:'.format(x))))#获得每一科的分数
    data[name] = marks

#第二个循环用以判断学生成绩是否合格
for x,y in data.items():
    total = sum(y)
    print("{}'s total marks {}".format(x, total))
    if total < 120:
        print(x,"failed :(")
    else:
        print(x,"passed :)")
