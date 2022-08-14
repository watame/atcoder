# A - Takoyaki
goal_count, make_count, make_minutes = map(int, input().split(" "))

if goal_count % make_count == 0:
    print(goal_count // make_count * make_minutes)
else:
    print((goal_count // make_count + 1) * make_minutes)
