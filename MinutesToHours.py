#!/usr/bin/env python3
#将分钟数转换为小时数
import sys
def MinutesToHours(times):
    hours = times // 60
    minutes = times % 60
    print("{} H".format(hours),end=',')
    print("{} M".format(minutes))
    return hours,minutes
time =sys.argv[1]
try:
    times = int(time)
    if times <0:
        print("请输入正数！：")
        raise valueError("请输入正数：")
    else:
        MinutesToHours(times)
except:
    print("请输入整数：")
print(time)



