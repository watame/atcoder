# B - Savings
saving_goal = int(input())

day = 0
money = 0
while money < saving_goal:
    day += 1
    money += day

print(day)
