# B - Palace
def calc_avg_temp(temperature, x):
    return temperature - x * 0.006


place_count = int(input())
temperature, average_temperature = map(float, input().split())
heights = list(map(float, input().split()))

# 最も平均温度に近い値を保持する
# -> 平均温度との距離が最も近い値を求めれば良いので、単純引き算をした上で絶対値に変換し距離情報を取得する
close_temp_dist = abs(calc_avg_temp(temperature, heights[0]) - average_temperature)
close_idx = 0
for idx in range(1, place_count):
    temp_dist = abs(calc_avg_temp(temperature, heights[idx]) - average_temperature)
    # より近い温度のが見つかった場合は値を更新
    if temp_dist < close_temp_dist:
        close_temp_dist = temp_dist
        close_idx = idx

print(close_idx + 1)
