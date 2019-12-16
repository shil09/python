#!/usr/bin/env python3
#整数运算示例
days = int(input("请输入天数：")) #输入总天数
months = days // 30 #//取整，算几个月
days = days % 30 #%取余，算几天
print("{}个月{}天".format(months,days)) #输出几个月几天
