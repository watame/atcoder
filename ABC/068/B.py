# B - Break Number

# 2で何回割れるかを判断する
def count_even(num):
    count = 0
    while 2 <= num and num % 2 == 0:
        num = num // 2
        count += 1
    return count


target_number = int(input())

count = 0
max_number = 1

for i in range(target_number, 0, -1):
    tmp_count = count_even(i)
    if count <= tmp_count:
        count = tmp_count
        max_number = i

print(max_number)
