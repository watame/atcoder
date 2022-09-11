# B - 1%
saving_goal = int(input())

year = 0
# 預けている金額(初期値として100円持っている)
money = 100
while money < saving_goal:
    year += 1
    # 1%の利息が付くので、預金額を100で割った整数値のみを足し合わせる
    # 少数をintに丸めると誤差が出てしまうので、割り算で考える必要がある
    money = money + money // 100

print(year)
