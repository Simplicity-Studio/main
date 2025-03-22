# T573808 [语言月赛 202502] IPv6

def h2b(hex_string):
    hex_to_bin_map = {
        '0': '0000', '1': '0001', '2': '0010', '3': '0011',
        '4': '0100', '5': '0101', '6': '0110', '7': '0111',
        '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
        'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111',
        'a': '1010', 'b': '1011', 'c': '1100', 'd': '1101',
        'e': '1110', 'f': '1111'
    }
    binary_string = ''.join(hex_to_bin_map[char] for char in hex_string)
    return binary_string
hex_format = list(map(str, input().split(":")))

bit_format = []
for i in hex_format:
    if i == "":
        for j in range(8 - len(hex_format)):
            bit_format.append("0000000000000000")
    i = i.zfill(4)
    present = h2b(i)
    bit_format.append(present)
print(''.join(bit_format))
