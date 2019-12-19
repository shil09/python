#!/usr/bin/env python3
fobj = open("/tmp/String.txt")
s = fobj.read()
print(s)
a = ""
for i in s:
    if i.isdigit():
        a += i

print(a)
