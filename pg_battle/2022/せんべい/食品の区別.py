# 1種類あたりの食品の数
food_count = int(input())

# インデックスを表示できるよう、辞書型で情報を保持
foods = {}
for i, f in enumerate(map(int, input().split())):
    # インデックスを1オリジンに変換
    foods[f] = i + 1

# 辞書のキーで配列をソート（ソート後はタプルの配列になる）
sort_foods = sorted(foods.items())
# lambdaを用いて、タプルの各要素の1インデックスの値を元にソートする
# 食品は「food_count*3」の数だけあるので、ソートしたリストの中間だけ取得する
# -> ましゅまろの範囲とかつおぶしの範囲を除いた、中間のところだけを表示する対象とする
for i in sorted(sort_foods[food_count:-food_count], key=lambda i: i[1]):
    # 出力するのはインデックスだけ
    print(i[1])
