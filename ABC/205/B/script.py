# B - Permutation Check
count = int(input())
numbers = set(map(int, input().split()))

if count == len(numbers):
    print("Yes")
else:
    print("No")
