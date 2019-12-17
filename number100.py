#!/usr/bin/env python3
number = int(input("请输入一个数："))
if number < 100:
    print("{}小于100".format(number))
elif number == 100:
    print("{}等于100".format(number))
else:
    print("{}大于100".format(number))
