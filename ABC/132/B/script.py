# B - Ordinary Number
n = int(input())
p = list(map(int, input().split()))

count = 0
for i in range(n - 2):
    target = p[i : (i + 3)]
    if target[0] < target[1] < target[2] or target[0] > target[1] > target[2]:
        count += 1

print(count)
