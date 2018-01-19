#!/usr/bin/env python3
sum = 0
for i in range(1,11):
	sum += 1 / i
	print("{:2d} {:6.4f}".format(i,sum))#如果这一行是没有缩进顶头写的，那它就不包含在for循环里面，而是在循环之外的一条语句
