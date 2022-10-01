comic_count = int(input())
comics = sorted(map(int, input().split()))

# 余っているコミック数をカウントする
rest_comic_count = 0
comic_set = {comics[0]}

# 1巻がなければ0を表示する
if 1 not in comic_set:
    print(0)
    exit()

for idx, c in enumerate(comics[1:]):
    if c in comic_set:
        rest_comic_count += 1
        continue

    comic_set.add(c)
print(comic_set)

next_comic = comics[0]
comic_list = sorted(list(comic_set))[1 : comic_count - 1]
limit = comic_count - 1
for idx, c in enumerate(comic_list):
    print(idx, c)
    next_comic += 1

print(sorted(list(comic_set)))


print(rest_comic_count)
# 2冊ずつ交換する
