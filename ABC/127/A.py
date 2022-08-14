# A - Ferris Wheel
age, fee = map(int, input().split(" "))

if age <= 5:
    print(0)
elif 13 <= age:
    print(fee)
else:
    print(fee // 2)
