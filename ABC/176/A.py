# A - Takoyaki
goal_count, make_count, make_minutes = map(int, input().split(" "))

# 頻出テクニックを利用すると場合分けが不要
# 割られる数に X−1 を足すことで、ちょうど割り切れる時以外は答えが 1 増える
# 例: goal_count = 10, make_count = 3
#   (10 + 3 - 1) / 3 -> 12 / 3 -> 4
# https://atcoder.jp/contests/abc176/editorial/60
print((goal_count + make_count - 1) // make_count * make_minutes)
