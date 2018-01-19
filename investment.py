#!/usr/bin/env python3
amount = float(input("请输入数额"))
inrate = float(input("请输入利率"))
period = int(input("请输入期限"))
value = 0;
year  = 1;
while year <= period:
      value = amount + (inrate * amount);
      print("Year {} Rs. {:.2f}".format(year,value))
      #Year {} Rs. {:.2f}".format(year, value) 称为字符串格式化，大括号和其中的字符会被替换成传入 str.format() 的参数
      #也即 year 和 value。其中 {:.2f} 的意思是替换为 2 位精度的浮点数。
      amount = value;
      year = year + 1; 
