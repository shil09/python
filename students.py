#!/usr/bin/env python3
n = int(input("请输入学生数量："))
data = {}  #空字典
subjects = ('physics','maths','history') #所有科目
for i in range(0,n):
    name = input("请输入学生名字：{}".format(i + 1))
    marks = []
    for x in subjects:
        marks.append(int(input("输入科目成绩{}:".format(x)))) #获得每一科的分数
    data[name] = marks
for x,y in data.items():
    total = sum(y)
    print("{}的总分是{}".format(x,total))
    if total < 120:
        print(x,"failed")
    else:
        print(x,"passed")


