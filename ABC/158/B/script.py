# B - Count Balls
take_count, blue_count, red_count = map(int, input().split())

# 普通に割った数に青のボールの個数を掛ける
blue = take_count // (blue_count + red_count) * blue_count
# 割った数のあまりの数を確認し、青のボールの数よりも小さければその数を追加する
rest_blue = (
    take_count % (blue_count + red_count)
    if take_count % (blue_count + red_count) < blue_count
    else blue_count
)

print(blue + rest_blue)
