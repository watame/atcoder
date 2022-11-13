# B - Do you know the second highest mountain?
mountain_count = int(input())
mountain_dict = {}
for i in range(mountain_count):
    name, height = input().split()
    mountain_dict[int(height)] = name

print(sorted(mountain_dict.items(), reverse=True)[1][1])
