# B - FizzBuzz Sum
limit_number = int(input())

sum_result = 0
for n in range(1, limit_number + 1):
    if not ((n % 3 == 0) or (n % 5 == 0)):
        sum_result += n

print(sum_result)
