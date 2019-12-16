#!/usr/bin/env python3
#num = int(input("enter number:"))
sum = 0
ave = 0
n = 10
i = 0
while i < n:
    num = float(input("enter {} number:".format(i)))
    sum=sum + num
    i = i + 1
ave =  sum / n
print("N = {},Sum = {}".format(n,sum))
print("ave={:.2f}".format(ave))
