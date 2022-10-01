num = int(input())

hex_str = str(hex(num)).upper()[2::]
if num < 16:
    hex_str = "0" + hex_str
print(hex_str)
