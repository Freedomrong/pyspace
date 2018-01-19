#!/usr/bin/env python3
import math
r = float(input("请输入圆的半径但不超过10: "))
if r <= 10:
    s = (math.pi) * (r * r)
    print("圆的面积={:15.10f}".format(s))#一共15位，小数点后10位
else:
    r = float(input("请重新输入圆的半径但不超过10: "))
    s = (math.pi) * (r * r)
    print("圆的面积={:15.10f}".format(s))#一共15位，小数点后10位
