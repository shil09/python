#!/usr/bin/env python3
i = 1
print("*" * 60)
while i <= 9:
    j = 1
    while j <=9:
        print("{:5d}".format(i * j),end=' ')
        j += 1
    print()
    i += 1
print("*" * 60)


