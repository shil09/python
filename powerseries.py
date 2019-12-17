#!/usr/bin/env python3
i = int(input("请输入数字n:"))
x = float(input("enter the value of X："))
result = 1.0
n = term =num =1
while n <=i:
    term *= x / n
    result += term
    n += 1
    if term < 0.00001:
        break
    print("No of Times= {} and Sum= {}".format(n,result))



