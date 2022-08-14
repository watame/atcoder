# A - Duplex Printing
n = int(input())

# 奇数の時にも印刷する必要があるので、n+1することで常に偶数にして'/2'で正しい枚数が出力できるようにする
print((n + 1) // 2)
