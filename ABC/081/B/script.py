# いらない情報を捨てるためのinput()
input()
# 全数値について割り算をするという条件だが、同じ数字であれば割り切れる回数も同じなのでSetで保持
numbers = set(map(int, input().split()))

counter = 0
while True:
    break_flg = False
    tmp = set()
    for n in numbers:
        # 割った値と余りを取得
        q, mod = divmod(n, 2)
        if mod == 0:
            tmp.add(q)
        else:
            break_flg = True
            break

    if break_flg:
        break

    # 割り算した後のsetで上書き
    numbers = tmp
    counter += 1

print(counter)
