#!/usr/bin/env python3
f = 0;
print("Fahrenheit Celsius")
while f <= 250:
	c = (f - 32) / 1.8;
	print("{:5d} {:7.2f}".format(f,c))
	f = f + 25;
