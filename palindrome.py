#!/usr/bin/env python3
Str = input("请输入一个字符串str:")
z = Str[::-1]
if z == Str:
    print("{} is a palindrom".format(Str))
else:
    print("{} is not a palindrom".format(Str))
