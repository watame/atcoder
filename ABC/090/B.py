# B - Palindromic Numbers
min, max = map(int, input().split())

count = 0
for i in range(min, max + 1):
    str_num = str(i)
    if str_num == str_num[::-1]:
        count += 1

print(count)
