# C - Divide the Problems
contest_count = int(input())
difficulties = list(map(int, input().split()))

# 全部並び替えて真ん中の差分だけみる
sorted_difficulties = sorted(difficulties)
print(
    sorted_difficulties[contest_count // 2]
    - sorted_difficulties[contest_count // 2 - 1]
)
