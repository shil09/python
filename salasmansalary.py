#!/usr/bin/env python3
#基本工资1500，每销售一台可获得200+2%提成
basic_salary = 1500 #基本工资
sale_numbers = int(input("请输入销售数量：")) #销售数量
sale_prince = float(input("请输入单价:")) #每台单价
act_salary = basic_salary + sale_numbers * 200 + sale_prince * sale_numbers * 0.02 #算出当月工资
print("当月实际工资：{}".format(act_salary))

