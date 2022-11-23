# C - Christmas Eve
count, display_count = map(int, input().split())
woods = sorted([int(input()) for _ in range(count)])

# 初期値として十分に大きい値を入れる
result = 10_000_000_000
for i in range(0, (count + 1) - display_count):
    # 最初の要素と最後の要素の差を取れば良い
    result = min(result, woods[i + display_count - 1] - woods[i])

print(result)
