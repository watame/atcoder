# B - Factorial Yen Coin
price = int(input())

total_coins = 0
for i in reversed(range(1, 11)):
    factorial = 1
    for ii in range(1, i + 1):
        factorial *= ii
    for c in range(100):
        # 金額よりもコインの額が多い場合は、無意味なのでスキップ
        if price < factorial:
            break
        price -= factorial
        total_coins += 1

print(total_coins)
