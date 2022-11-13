food_count = int(input())
foods = [0] + list(map(int, input().split()))
foods_set = set(foods[1::])
for i in range(food_count):
    # 最小値と最大値を削除する
    foods_set.remove(min(foods_set))
    foods_set.remove(max(foods_set))
# インデックスを取得
res = set()
for f in foods_set:
    res.add(foods.index(f))
# 小さい順に表示
for r in sorted(res):
    print(r)
