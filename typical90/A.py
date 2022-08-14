# 033 - Not Too Bright（★2）
# 解説：https://twitter.com/e869120/status/1390436977808351234?s=20&t=GP8LPvJhd9dmR1erO78AEg
height, width = map(int, input().split(" "))

if height < 2 or width < 2:
    # 2マス以上でなければ全部ライトアップすればOK
    print(max(height, width))
else:
    # 4マスの中に2つ以上ライトアップするのはNG
    # -> 縦、横で各2マスに1つしか存在できない
    #    ※3マス目が存在した場合にも配置が可能なので、小技を使って切り上げ計算する
    height_light = (height + 2 - 1) // 2
    width_light = (width + 2 - 1) // 2
    print(height_light * width_light)
