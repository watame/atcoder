# B - Base K
base = int(input())
number_one, number_two = map(int, input().split())


# 特定の基数,数値を10進数の数値にに変換する
def convert_decimal(base, number):
    result = 0
    for c, n in enumerate(str(number)[::-1]):
        # 各桁で基数を用いた計算を実施する
        result += int(n) * base**c
    return result


print(convert_decimal(base, number_one) * convert_decimal(base, number_two))
