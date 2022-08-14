# A - Biscuit Generator
generate_timing, biscuit_count, calc_seconds = map(int, input().split(" "))

print(calc_seconds // generate_timing * biscuit_count)
