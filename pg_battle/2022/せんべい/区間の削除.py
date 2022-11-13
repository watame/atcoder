# lenが1かつ、値が1以上の場合にtrue
def len_is_one_and_grater_one(array):
    return len(array) == 1 and 1 < array[0]


n = int(input())
numbers = list(map(int, input().split()))

result = 0
tmp = [numbers[0]]
for i in range(1, n):
    # 連番の場合はtmpに格納
    if numbers[i] - numbers[i - 1] == 1:
        tmp.append(numbers[i])
    else:
        # 連番じゃなかったら、こっち
        # 配列の中身をチェックして、連番じゃなかったらresultに追加する
        if len_is_one_and_grater_one(tmp):
            result += tmp[0]
        tmp = []
        tmp.append(numbers[i])

# 連番じゃない場合は、最後にtmpが余っているので必要であればresultに追加
if len_is_one_and_grater_one(tmp):
    result += tmp[0]

print(result)
