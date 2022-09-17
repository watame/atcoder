# B - 200th ABC-200
number, filter_count = map(int, input().split())

for fc in range(filter_count):
    if number % 200 == 0:
        number = number // 200
    else:
        number = int(str(number) + "200")

print(number)
