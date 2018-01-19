#!/usr/bin/env python3
minutes = int(input("输输入分钟数："))
if minutes > 0:
    hours = int(minutes / 60)
    mminutes = minutes % 60
    print("%d小时 %d分钟"%(hours,mminutes))


if minutes < 0:
    print(" valueError:Input number cannot be negative")
