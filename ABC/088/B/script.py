# 捨てinput
input()
cards = list(map(int, input().split()))

alice = 0
bob = 0
# ソートして偶数/奇数で取り出す順番を再現
for i, c in enumerate(sorted(cards, reverse=True)):
    if i % 2 == 0:
        alice += c
    else:
        bob += c

print(alice - bob)
