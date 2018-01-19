#!/usr/bin/env python3
name = input("输入文件名称:")
fobj = open(name)
print(fobj.read())
fobj.close()
