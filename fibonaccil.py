#!/usr/bin/env python3
a,b=0,1
n = int(input("请输入一个数："))
while b < n:
    print(b,end=',')
    a,b = b,a+b
print()

