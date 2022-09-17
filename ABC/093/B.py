# B - Small and Large Integers
min, max, index = map(int, input().split())

# 各閾値を超え内容にifで調整
min_range_max = max if max <= min + index else min + index
max_range_min = min if max - index + 1 <= min else max - index + 1
# 各閾値からリストを作り、結合する
target = list(range(min, min_range_max)) + list(range(max_range_min, max + 1))

# setで重複削除して、listをソートする
for r in sorted(set(target)):
    print(r)
