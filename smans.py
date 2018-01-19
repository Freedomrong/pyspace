#!/usr/bin/env python3
b_s = 1500
b_r = 200
c_r = 0.02
nofc = int(input("Enter the number of inputs sold: "))
p = float(input("Enter the total prices: "))
b = (b_r * nofc)
c = (c_r * nofc * p)
print("Bonus           ={:6.2f}".format(b))
print("Commision       ={:6.2f}".format(c))
print("Gross salary    ={:6.2f}".format(b_s + b + c))
