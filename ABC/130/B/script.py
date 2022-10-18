bound_count, limit_x = map(int, input().split())
bounds = list(map(int, input().split()))

counter = 1
# D1 = 0 をセット
last_bound = 0
for i in range(len(bounds)):
    # 都度上書きしていく
    last_bound = last_bound + bounds[i]
    if limit_x < last_bound:
        break
    counter += 1

print(counter)
