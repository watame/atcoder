# C - Tax Increase
eight_tax, ten_tax = map(int, input().split())

result = -1

# breakで解除するので、ループ数は関係ないが8%で100円の税金がかかる値のMAXは1250なので、そこを終点にする
for i in range(1, 1251):
    e_tax = i * 8 // 100
    t_tax = i * 10 // 100
    if e_tax == eight_tax and t_tax == ten_tax:
        result = i
        break
print(result)
