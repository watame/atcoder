# A - Duplex Printing
n = int(input())

duplex_print_num = n // 2
if n % 2 == 0:
    print(duplex_print_num)
else:
    print(duplex_print_num + 1)
