# B - Distance
import math

point_count, distance_limit = map(int, input().split())

counter = 0
for c in range(point_count):
    x, y = map(int, input().split())
    # 原点からの距離 <= distance_limit の場合だけカウントアップ
    if math.sqrt(x**2 + y**2) <= distance_limit:
        counter += 1

print(counter)
