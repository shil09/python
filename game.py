#!/usr/bin/env python3
#棍子游戏，有21根棍子，每次只能选1-4根，谁选到最后一根谁就会输，用户先选
sticks = 21 #棍子数量

while True:
    print("sticks left: ",sticks)
    sticks_taken = int(input("Please you take sticks(1-4):"))
    if sticks == 1:
        print("you took the last stick,you loose")
        break
    if sticks_taken >= 5 or sticks_taken <=0:
        print("wrong choice")
        continue
    print("Computer took:",(5 - sticks_taken),"\n")
    sticks -= 5




