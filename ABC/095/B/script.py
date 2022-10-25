donut_count, confectionery_mix = map(int, input().split())

amount_needed_to_make_donuts = []
for i in range(donut_count):
    amount_needed_to_make_donuts.append(int(input()))

# 最低限1種類以上は作らないとダメ
confectionery_mix -= sum(amount_needed_to_make_donuts)
# 作ったドーナツの個数を初期値として設定
result = donut_count

# 最小のお菓子の素で作れるドーナツを最大個数作る
min_donut = min(amount_needed_to_make_donuts)
while min_donut <= confectionery_mix:
    confectionery_mix -= min_donut
    result += 1

print(result)
