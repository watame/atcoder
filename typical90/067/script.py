# 067 - Base 8 to 9
# 任意の基数から任意の基数に変換する
def convert_base(from_base: int, to_base: int, number: str):
    base_ten = 0
    # 対象となるn進数を10進数に変換
    for c, n in enumerate(str(number)[::-1]):
        # 各桁で基数を用いた計算を実施する
        base_ten += int(n) * from_base**c

    to_base_str = ""
    # 10進数を変換後の基数で割って基数に対応した値にする
    while to_base <= base_ten:
        to_base_str = str(base_ten % to_base) + to_base_str
        base_ten = base_ten // to_base
    # 最後に残ったあまりを文字列に追加する
    to_base_str = str(base_ten) + to_base_str

    return to_base_str


number_str, convert_number_str = input().split()

for i in range(int(convert_number_str)):
    number_str = convert_base(8, 9, number_str).replace("8", "5")

print(number_str)
