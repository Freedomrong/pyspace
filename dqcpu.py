#!/usr/bin/env python3
#在实际情况中，我们应该尝试使用with语句处理文件对象，它会在文件用完后会自动关闭
with open('/proc/cpuinfo') as fobj:
    for line in fobj:#按每行
        print(line,end = '')#打印出来
