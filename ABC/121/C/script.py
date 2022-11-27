# C - Energy Drink Collector
store_count, required_count = map(int, input().split())
value_store = sorted([tuple(map(int, input().split())) for _ in range(store_count)])

cost = 0
for vs in value_store:
    if vs[1] <= required_count:
        cost += vs[0] * vs[1]
        required_count -= vs[1]
    else:
        cost += vs[0] * required_count
        break

print(cost)
