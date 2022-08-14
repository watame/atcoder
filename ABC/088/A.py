# A - Infinite Coins
payment = int(input())
one_yen_coin_count = int(input())

if (payment % 500) <= one_yen_coin_count:
    print("Yes")
else:
    print("No")
