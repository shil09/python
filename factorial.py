#!/usr/bin/env python3
import sys
# 一个计算阶乘的程序
def fact(n):
    """
    :arg n : 数字
    :returns: 返回n的阶乘
    """
    if n == 0 :
        return 1
    return n * fact(n -1)

def div(n):
    """
    只是做除法
    """
    res = 10 / n
    return res

def main(n):
    res = fact(n)
    print(res)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))



