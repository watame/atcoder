# A - Biscuit Generator
generate_timing, biscuit_count, calculate_seconds = map(int, input().split(" "))

print(calculate_seconds // generate_timing * biscuit_count)
