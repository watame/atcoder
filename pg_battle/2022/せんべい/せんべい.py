senbei_count, query_count = map(int, input().split())
senbei = [True] + [True] * senbei_count
for i in range(query_count):
    left_idx, right_idx = map(int, input().split())
    for r in range(left_idx, right_idx + 1):
        senbei[r] = not senbei[r]
print(senbei.count(False))
