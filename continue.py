#!/usr/bin/env
while True:
    n = int(input("请输入正数："))
    if n < 0:
        continue
    elif n == 0:
        break
    else:
        print("Square is ", n ** 2)
print("Goodble")
