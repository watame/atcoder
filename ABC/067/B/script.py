# B - Snake Toy
count, length = map(int, input().split())
parts_length = sorted(tuple(map(int, input().split())), reverse=True)

print(sum(parts_length[:length]))
